"""Append a dated Sign-Off entry to SIGNOFF_LOG.md.

Appends only — never reads the log's existing content into memory beyond a
small tail check used to decide whether a blank-line separator is needed.
Exists so a calling agent can record a Sign-Off entry without spending
context tokens on the file's growing history (see CLAUDE.md's Sign-Off
section for what belongs in an entry).
"""
import argparse
import datetime
import json
import os
import re
import sys

_TAIL_PEEK_BYTES = 8

METRICS_SCHEMA_VERSION = 1
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_TIME_RE = re.compile(r"^\d{2}:\d{2}$")

# Field name -> validator(value) -> bool. Anything not listed here (beyond the
# required fields) is an unknown key and gets rejected — typo protection matters
# more than forward compatibility, since schema_version gates evolution.
_OPTIONAL_METRICS_FIELDS = {
    "backfilled": lambda v: isinstance(v, bool),
    "time": lambda v: isinstance(v, str) and bool(_TIME_RE.match(v)),
    "traps_rehit": lambda v: _is_str_list(v),
    "claims_live": lambda v: _is_str_list(v),
    "claims_contradicted": lambda v: _is_str_list(v),
    "unverified_load_bearing": lambda v: v is None or isinstance(v, int),
    "launches": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "crashes": lambda v: isinstance(v, list)
    and all(isinstance(c, dict) and isinstance(c.get("cause"), str) for c in v),
    "issues_opened": lambda v: _is_int_list(v),
    "issues_closed": lambda v: _is_int_list(v),
    "issues_touched": lambda v: _is_int_list(v),
    "notes": lambda v: isinstance(v, str),
}


def _is_str_list(v):
    return isinstance(v, list) and all(isinstance(x, str) for x in v)


def _is_int_list(v):
    return isinstance(v, list) and all(
        isinstance(x, int) and not isinstance(x, bool) for x in v
    )


class MetricsValidationError(Exception):
    """Raised when a metrics block fails schema validation or can't be parsed."""


def validate_metrics(block):
    """Return a list of human-readable errors; empty list means valid."""
    if not isinstance(block, dict):
        return ["metrics block must be a JSON object"]

    errors = []
    if block.get("schema_version") != METRICS_SCHEMA_VERSION:
        errors.append(
            f"schema_version must be {METRICS_SCHEMA_VERSION} "
            f"(got {block.get('schema_version')!r})"
        )
    date = block.get("date")
    if not (isinstance(date, str) and _DATE_RE.match(date)):
        errors.append(f"date must be a YYYY-MM-DD string (got {date!r})")

    for key, value in block.items():
        if key in ("schema_version", "date"):
            continue
        if key not in _OPTIONAL_METRICS_FIELDS:
            errors.append(f"unknown field {key!r} (typo?)")
        elif not _OPTIONAL_METRICS_FIELDS[key](value):
            errors.append(f"field {key!r} has the wrong type/shape")
    return errors


def load_and_validate_metrics(metrics_path):
    """Load a metrics JSON file, validate it, and return the normalized block.

    Raises MetricsValidationError (with all problems listed) on any failure,
    so callers can fail loudly BEFORE touching the prose log.
    """
    try:
        with open(metrics_path, "r", encoding="utf-8") as f:
            block = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        raise MetricsValidationError(f"could not read metrics file: {e}") from e

    errors = validate_metrics(block)
    if errors:
        raise MetricsValidationError("; ".join(errors))

    block.setdefault("backfilled", False)
    return block


def append_metrics_line(sidecar_path, block):
    """Append the block as exactly one JSON line to the sidecar file."""
    with open(sidecar_path, "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(block, ensure_ascii=False) + "\n")


def format_entry(date, communication_notes, work_notes, heading_suffix=None, time=None):
    heading = f"#### {date}"
    if time:
        heading += f" {time}"
    if heading_suffix:
        heading += f" {heading_suffix}"
    return (
        f"{heading}\n\n"
        f"**Communication notes:** {communication_notes}\n\n"
        f"**Work notes:** {work_notes}\n"
    )


def _trailing_newline_count(path):
    """Count trailing blank-line-worthy newlines, tolerant of CRLF line endings.

    Peeked in binary mode, so a raw byte scan would miscount a CRLF file
    (each line ending is `\\r\\n`, and a bare `\\r` byte would otherwise
    look like "not a newline" and stop the count early).
    """
    size = os.path.getsize(path)
    if size == 0:
        return 0
    with open(path, "rb") as f:
        f.seek(max(0, size - _TAIL_PEEK_BYTES), os.SEEK_SET)
        tail = f.read()
    text = tail.decode("utf-8", errors="ignore").replace("\r\n", "\n").replace("\r", "\n")
    count = 0
    for ch in reversed(text):
        if ch != "\n":
            break
        count += 1
    return count


def append_entry(log_path, entry_text):
    prefix = ""
    if os.path.exists(log_path) and os.path.getsize(log_path) > 0:
        trailing = _trailing_newline_count(log_path)
        if trailing == 0:
            prefix = "\n\n"
        elif trailing == 1:
            prefix = "\n"

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(prefix)
        f.write(entry_text)


def main():
    parser = argparse.ArgumentParser(
        description="Append a dated Sign-Off entry to a SIGNOFF_LOG.md-style file "
        "without reading the file's existing content."
    )
    parser.add_argument("log_path", help="Path to the Sign-Off log file")
    parser.add_argument(
        "--communication-notes-file",
        required=True,
        help="Path to a text file containing the entry's Communication notes",
    )
    parser.add_argument(
        "--work-notes-file",
        required=True,
        help="Path to a text file containing the entry's Work notes",
    )
    parser.add_argument(
        "--date",
        help="Entry date, YYYY-MM-DD (default: today)",
    )
    parser.add_argument(
        "--time",
        help="Entry time, HH:MM 24-hour (default: current local time, but only "
        "when --date is not explicitly passed — an explicit --date signals a "
        "backfill, whose real time is unknown and should not be guessed)",
    )
    parser.add_argument(
        "--heading-suffix",
        help="Optional suffix appended to the date heading, e.g. '(second entry)'",
    )
    parser.add_argument(
        "--metrics-file",
        help="Path to a JSON file with this session's structured metrics block "
        "(schema_version 1); validated and appended as one line to the sidecar",
    )
    parser.add_argument(
        "--metrics-sidecar",
        help="Path to the JSONL metrics sidecar (default: signoff_metrics.jsonl "
        "next to the log file)",
    )
    args = parser.parse_args()

    date = args.date or datetime.date.today().isoformat()
    # An explicit --date signals a backfill (unknown historical time) — only
    # default to "now" when the caller didn't override the date, i.e. a real
    # live session.
    time_value = args.time or (
        None if args.date else datetime.datetime.now().strftime("%H:%M")
    )

    # Validate metrics FIRST so a malformed block fails loudly before the
    # prose log is touched — the two appends must not be able to half-happen.
    metrics_block = None
    if args.metrics_file:
        try:
            metrics_block = load_and_validate_metrics(args.metrics_file)
        except MetricsValidationError as e:
            print(f"Metrics validation failed (prose log untouched): {e}", file=sys.stderr)
            sys.exit(2)
        if time_value and "time" not in metrics_block:
            metrics_block["time"] = time_value

    with open(args.communication_notes_file, "r", encoding="utf-8") as f:
        communication_notes = f.read().strip()
    with open(args.work_notes_file, "r", encoding="utf-8") as f:
        work_notes = f.read().strip()

    entry_text = format_entry(
        date, communication_notes, work_notes, heading_suffix=args.heading_suffix, time=time_value
    )
    append_entry(args.log_path, entry_text)
    print(f"Appended Sign-Off entry for {date} to {args.log_path}")

    if metrics_block is not None:
        sidecar = args.metrics_sidecar or os.path.join(
            os.path.dirname(os.path.abspath(args.log_path)), "signoff_metrics.jsonl"
        )
        append_metrics_line(sidecar, metrics_block)
        print(f"Appended metrics line for {date} to {sidecar}")


if __name__ == "__main__":
    main()

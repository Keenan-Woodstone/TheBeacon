"""Append one line to a Dossiers CheckIn.txt for a dossier submission.

Two logs: Dossiers/CheckIn.txt for the 20 private, git-ignored slots, and
Dossiers/Shared/CheckIn.txt for the 20 shared, git-tracked ones. Pass
whichever log matches the slot you used.

Ported from Thyrsus/Dionysus (2026-08-27), unchanged. See DOSSIERMASTER.md
for the full Dossiers/ process this supports.
"""
import argparse
import datetime

_MIN_SLOT = 1
_MAX_SLOT = 20


def format_line(date, time, badge, issue, dossier, file_name):
    return f"{date} {time} | {badge} | {issue} | {dossier} | {file_name}\n"


def append_line(checkin_path, line):
    with open(checkin_path, "a", encoding="utf-8", newline="\n") as f:
        f.write(line)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Append a Dossiers/CheckIn.txt line for a dossier submission."
    )
    parser.add_argument("checkin_path", help="Path to Dossiers/CheckIn.txt (private slots) or Dossiers/Shared/CheckIn.txt (shared slots)")
    parser.add_argument("--badge", required=True, help="Submitting agent's badge/session identifier")
    parser.add_argument("--issue", required=True, type=int, help="Issue number the dossier relates to")
    parser.add_argument("--dossier", required=True, type=int, help=f"Dossier slot number ({_MIN_SLOT}-{_MAX_SLOT})")
    parser.add_argument("--file-name", required=True, help="Name of the file/folder placed in the slot")
    parser.add_argument("--date", help="YYYY-MM-DD (default: today)")
    parser.add_argument("--time", help="HH:MM 24-hour (default: current local time)")
    args = parser.parse_args(argv)

    if not (_MIN_SLOT <= args.dossier <= _MAX_SLOT):
        parser.error(f"--dossier must be between {_MIN_SLOT} and {_MAX_SLOT} (got {args.dossier})")

    date = args.date or datetime.date.today().isoformat()
    time = args.time or datetime.datetime.now().strftime("%H:%M")

    line = format_line(date, time, args.badge, args.issue, args.dossier, args.file_name)
    append_line(args.checkin_path, line)
    print(f"Appended dossier check-in to {args.checkin_path}")


if __name__ == "__main__":
    main()

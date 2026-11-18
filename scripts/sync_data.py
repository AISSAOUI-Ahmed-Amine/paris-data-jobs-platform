#!/usr/bin/env python3
"""Copy the latest job-postings export into data/raw/<today>/.

    python scripts/sync_data.py
    python scripts/sync_data.py --source "C:/path/to/export"

By default it reads the export folder ../learning/data next to this project, which the
job-collection kit refreshes every morning. Keeping one dated folder per day gives the
history that the incremental models and snapshots of weeks 3 and 4 need.
"""
import argparse
import datetime as dt
import pathlib
import shutil
import sys

FILES = ("postings.ndjson", "posting_checks.ndjson")
PROJECT = pathlib.Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default=str(PROJECT.parent / "learning" / "data"), help="folder that holds the export files")
    ap.add_argument("--day", default=dt.date.today().isoformat(), help="name of the dated folder to write")
    args = ap.parse_args()

    source = pathlib.Path(args.source)
    missing = [name for name in FILES if not (source / name).exists()]
    if missing:
        sys.exit(f"Not found in {source}: {', '.join(missing)}")
    target = PROJECT / "data" / "raw" / args.day
    target.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        shutil.copy2(source / name, target / name)
        with open(target / name, encoding="utf8") as f:
            rows = sum(1 for _ in f)
        print(f"{name}: {rows} rows -> {target / name}")


if __name__ == "__main__":
    main()

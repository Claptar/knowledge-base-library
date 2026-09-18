#!/usr/bin/env python3
"""Print one chapter task row from book-tasks.json.  Usage: task.py <key>"""
import json, sys
from pathlib import Path
rows = json.loads((Path(__file__).resolve().parents[3] / "conversion-cache" / "book-tasks.json").read_text())
for r in rows:
    if r["key"] == sys.argv[1]:
        print(json.dumps(r, indent=1)); break
else:
    sys.exit(f"no task with key {sys.argv[1]}")

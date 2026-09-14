#!/usr/bin/env python3
"""Summarise what an unpacked course directory actually contains.

OCW exports arrive as a flat pile of files whose only structure is the naming
convention, so "what is in this course and what is worth adapting" is otherwise
a question you answer by reading 400 filenames.

    python3 course_inventory.py sources/ocw-6041sc
    python3 course_inventory.py sources/ocw-*  --full

Groups are a guess from filenames and nothing more. `unclassified` is not a bug
— it is the pile to look at by hand, and it is printed for that reason.
"""
import argparse
import re
from collections import defaultdict
from pathlib import Path

# `_` is a regex word character, so \b does not fire between "MIT8_592JS11" and
# "PS1" — which silently dumped every problem set into `unclassified`. Use an
# explicit separator class instead.
SEP = r"(?:^|[^A-Za-z0-9])"

# Ordered: the first pattern that matches wins.
GROUPS = [
    ("video transcript", r"_transcript\.pdf$"),
    # 8.591J-2004 names a per-lecture outline `l12_syllabus.pdf` beside
    # `l12_notes.pdf`. Match the outline first or `l12_` swallows both.
    ("lecture outlines", r"^l\d+[\s_-]*syllabus"),
    # `_L01.pdf` (6.041SC slides) and `l1_notes.pdf` (8.591J-2004) are both
    # lectures; neither contains the string "lec".
    ("lecture notes",   rf"lec(ture)?[\s_-]*\d|lecture|^l\d+[\s_-]*notes|{SEP}l\d+(\.|$)"),
    ("recitation",      rf"{SEP}rec(itation)?[\s_-]*\d|recitation"),
    ("tutorial",        rf"{SEP}tut(orial)?[\s_-]*\d|tutorial"),
    ("problem sets",    rf"pset|problem[\s_-]*set|{SEP}ps[\s_-]*\d|assn|assignment"
                        rf"|{SEP}hw[\s_-]*\d|homework"),
    # `exam` must not fire inside "Example" -- it filed 13 worked-example
    # clips as exams before this negative lookahead was added.
    ("exams",           rf"exam(?!ple)|quiz|{SEP}qu\d|final|midterm"),
    ("solutions",       rf"sol(ution)?s?{SEP}|sol(ution)?s?$|soln"),
    ("compiled",        r"compiled|complete|full[\s_-]*text|notes[\s_-]*all"),
    # Video-derived items with a descriptive title and no lecture/exam marker are
    # the named worked-example clips -- "Coupon Collector", "Competing
    # Exponentials". Per SKILL.md step 2 these are usually the part worth
    # adapting, so they get their own group rather than falling to unclassified.
    ("worked examples", r"_\d+k(__\d+)?(\.|$)"),
]

# 7.91J and 8.591J-2014 ship video-derived PDFs named by bare YouTube id
# (`1EMonM7qAU8.pdf`), each paired with a caption file of the same stem. The id
# carries no meaning, so the only honest grouping is "this came from a recording".
VIDEO_ID = re.compile(r"^[A-Za-z0-9_-]{11}(__\d+)?$")


def classify(name):
    """Return the group label for a filename, from its naming convention alone."""
    low = name.lower()
    # A PDF transcript is a transcript whatever else the name says.
    if re.search(r"_transcript\.pdf$", low):
        return "video transcript"
    if VIDEO_ID.match(Path(name).stem):
        return "recordings"
    # Solutions before problem sets: "pset3_sol" is a solution.
    if re.search(rf"sol(ution)?s?{SEP}|sol(ution)?s?$|soln", low):
        return "solutions"
    for label, pat in GROUPS:
        if label in ("solutions", "video transcript"):
            continue
        if re.search(pat, low):
            return label
    return "unclassified"


def report(d, full=False):
    """Print a grouped summary of one course directory."""
    pdfs, trans, other = [], [], []
    for p in sorted(d.iterdir()):
        if not p.is_file():
            continue
        s = p.suffix.lower()
        (pdfs if s == ".pdf" else trans if s in {".srt", ".vtt"} else other).append(p)

    # One recording may ship as both .srt and .vtt; count the recording once.
    recordings = sorted({p.with_suffix("").name for p in trans})

    print(f"\n{'=' * 78}\n{d.name}\n{'=' * 78}")
    print(f"{len(pdfs)} PDFs · {len(recordings)} recordings ({len(trans)} caption files)"
          + (f" · {len(other)} other" if other else ""))

    buckets = defaultdict(list)
    for p in pdfs:
        buckets[classify(p.name)].append(p.name)
    if buckets:
        print("\n  documents")
        for label, _ in GROUPS + [("unclassified", "")]:
            names = buckets.get(label)
            if not names:
                continue
            print(f"    {label:16s} {len(names):4d}")
            if full or label == "unclassified":
                for n in names:
                    print(f"      {n}")

    if recordings:
        rbuckets = defaultdict(list)
        for name in recordings:
            rbuckets[classify(name)].append(name)
        print("\n  recordings")
        for label in [g[0] for g in GROUPS] + ["unclassified"]:
            names = rbuckets.get(label)
            if not names:
                continue
            print(f"    {label:16s} {len(names):4d}")
            if full or label == "unclassified":
                for n in names:
                    print(f"      {n}")
        print("\n  Recordings classified 'unclassified' are usually the short worked-example")
        print("  clips — often the part worth adapting. See SKILL.md step 2.")


def main():
    """CLI entry point."""
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dirs", nargs="+", type=Path)
    ap.add_argument("--full", action="store_true", help="list every filename, not just counts")
    args = ap.parse_args()
    for d in args.dirs:
        if d.is_dir():
            report(d, args.full)


if __name__ == "__main__":
    main()

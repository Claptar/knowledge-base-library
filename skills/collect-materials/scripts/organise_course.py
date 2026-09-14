#!/usr/bin/env python3
"""Sort a flat course export into subdirectories by what each file is.

An unpacked OCW course is a few hundred files in one directory whose only
structure is the naming convention. This moves them into named folders using the
same classifier as course_inventory.py, so "the problem sets" is a path rather
than a grep.

    python3 organise_course.py sources/ocw-6041sc                     # dry run
    python3 organise_course.py sources/ocw-*  --apply                 # do it

**Dry run is the default.** Nothing moves until --apply, and the plan printed by
a dry run is exactly what --apply performs. Already-organised directories are
left alone, so it is safe to re-run after adding files.

Layout produced:

    <course>/
      lectures/      recitations/   tutorials/
      psets/         solutions/     exams/
      worked-examples/              the named clips: slides + captions together
      recordings/                   video-derived files we could not name further
      transcripts-pdf/              OCW's PDF transcripts, which duplicate the above
      other/                        whatever the classifier could not place

Captions live beside the material they belong to rather than in one pile:
a worked example's .srt goes to worked-examples/ with its slides, because they
are one object.
"""
import argparse
import shutil
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from course_inventory import classify  # noqa: E402

FOLDER = {
    "lecture notes": "lectures",
    "lecture outlines": "lecture-outlines",
    "recordings": "recordings",
    "recitation": "recitations",
    "tutorial": "tutorials",
    "problem sets": "psets",
    "solutions": "solutions",
    "exams": "exams",
    "compiled": "compiled",
    "worked examples": "worked-examples",
    "video transcript": "transcripts-pdf",
    "unclassified": "other",
}
KNOWN = set(FOLDER.values()) | {"transcripts"}


def plan(d):
    """Return [(src, dest)] for every file that should move."""
    moves = []
    for p in sorted(d.iterdir()):
        if p.is_dir():
            continue
        label = classify(p.name)
        if p.suffix.lower() in {".srt", ".vtt"}:
            # A caption belongs with the material it captions, not in a pile of
            # its own -- a clip's slides and its transcript are one object. Only
            # a caption we could not place at all falls back to recordings/.
            folder = FOLDER.get(label, "recordings")
            if folder in ("other", "transcripts-pdf"):
                folder = "recordings"
        else:
            folder = FOLDER.get(label, "other")
        moves.append((p, d / folder / p.name))
    return moves


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dirs", nargs="+", type=Path)
    ap.add_argument("--apply", action="store_true", help="actually move files")
    args = ap.parse_args()

    total = 0
    for d in args.dirs:
        if not d.is_dir():
            continue
        if any((d / k).is_dir() for k in KNOWN):
            print(f"{d.name}: already organised, skipping")
            continue
        moves = plan(d)
        if not moves:
            continue
        counts = defaultdict(int)
        for _, dest in moves:
            counts[dest.parent.name] += 1
        print(f"\n{d.name}  ({len(moves)} files)")
        for folder in sorted(counts):
            print(f"    {folder:20s} {counts[folder]:4d}")
        total += len(moves)
        if args.apply:
            for src, dest in moves:
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src), str(dest))
            print("    moved.")

    if not args.apply and total:
        print(f"\nDry run — {total} files would move. Re-run with --apply to do it.")


if __name__ == "__main__":
    main()

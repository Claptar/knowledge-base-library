#!/usr/bin/env python3
"""Rename an organised source folder to this repository's own convention.

Courses arrive from different places with incompatible naming — OCW alone uses
four schemes in six courses. Rather than teach every downstream script each
source's conventions, normalise once at ingest and let everything after read one
layout:

    <index-or-slug>-<artefact type>.<ext>

    lectures/01-slides.pdf  01-transcript.pdf  01-captions.srt
    worked-examples/ch1-coupon-collector-transcript.pdf
    psets/03-questions.pdf

An index is used where the title carries no information ("Lecture 4"); a
slugified title is kept where it does — for a worked-example clip the title *is*
the content, and `07` would throw that away.

Every rename is recorded in `_manifest.csv` at the source root, because the
original filename is the only route back to the thing on the publisher's site.
Losing it would break the repo's rule that every claim can be checked against
its source.

    python3 normalise_names.py sources/ocw-6041sc          # dry run
    python3 normalise_names.py sources/* --apply

Dry run is the default.
"""
import argparse
import csv
import re
import shutil
from pathlib import Path

CAPTIONS = {".srt", ".vtt"}

# Per-folder artefact type for non-caption files. `None` means work it out from
# the filename (a lecture folder holds both slides and transcripts).
FOLDER_TYPE = {
    "lectures": None,
    "recitations": None,
    "tutorials": None,
    "lecture-outlines": "outline",
    "psets": "questions",
    "solutions": "solutions",
    "exams": "exam",
    "compiled": "compiled",
    "transcripts-pdf": "transcript",
    "recordings": "transcript",
    "worked-examples": "transcript",
    "other": None,
}

# Folders whose filenames carry a real title worth keeping.
TITLED = {"worked-examples", "recordings", "other"}

# Ordered: the first that matches gives the index.
INDEX_PATTERNS = [
    r"lec(?:ture)?[\s_-]*(\d{1,2})(?!\d)",
    r"(?:^|[^a-z0-9])l[\s_-]*(\d{1,2})(?!\d)",
    r"(?:pset|problem[\s_-]*set|ps)[\s_-]*(\d{1,2})(?!\d)",
    r"(?:rec|recitation)[\s_-]*(\d{1,2})(?!\d)",
    r"(?:tut|tutorial)[\s_-]*(\d{1,2})(?!\d)",
    r"(?:quiz|qu|exam|midterm)[\s_-]*(\d{1,2})(?!\d)",
    r"(?:hw|assn|assignment)[\s_-]*(\d{1,2})(?!\d)",
]

# Course-code prefixes (MIT6_041SCF13_) carry no information once the file is
# inside a folder named for that course.
PREFIX = re.compile(r"^mit[0-9a-z_]*?\d{2}[a-z]?_", re.I)
VIDEO_ID = re.compile(r"^[A-Za-z0-9_-]{11}(__\d+)?$")


DATE = re.compile(r"(?<!\d)(\d{1,2})[-_](\d{1,2})[-_](\d{2,4})(?!\d)")


def date_of(stem):
    """US-format date in the filename, as YYYY-MM-DD, or None."""
    m = DATE.search(stem)
    if not m:
        return None
    mo, day, yr = (int(g) for g in m.groups())
    if not (1 <= mo <= 12 and 1 <= day <= 31):
        return None
    return f"{yr + 2000 if yr < 100 else yr:04d}-{mo:02d}-{day:02d}"


def index_of(stem):
    low = stem.lower()
    for pat in INDEX_PATTERNS:
        m = re.search(pat, low)
        if m:
            return f"{int(m.group(1)):02d}"
    return None


def artefact_type(path, folder):
    if path.suffix.lower() in CAPTIONS:
        return "captions"
    fixed = FOLDER_TYPE.get(folder)
    if fixed:
        return fixed
    low = path.stem.lower()
    if "syllabus" in low:
        return "outline"
    if "notes" in low:
        return "notes"
    # A video-derived PDF is a transcript: `_300k` is the video stream marker,
    # and every one checked opened with "Transcript – ...".
    if re.search(r"_\d+k(__\d+)?$|_transcript$", low) or VIDEO_ID.match(path.stem):
        return "transcript"
    return "slides"


def discriminator(title, base, atype):
    """What the title still says once the index and type words are removed."""
    d = title
    for word in (base, atype, "lec", "lecture", "quiz", "exam", "pset", "ps",
                 "rec", "recitation", "tut", "tutorial", "notes", "syllabus"):
        d = re.sub(rf"(?:^|-){re.escape(word)}(?:-|$)", "-", d)
    d = re.sub(r"\d+k", "", d)
    d = re.sub(r"[^a-z0-9]+", "-", d).strip("-")
    return re.sub(r"-{2,}", "-", d)


def slugify(stem):
    s = PREFIX.sub("", stem)
    s = re.sub(r"_\d+k(__\d+)?$", "", s)      # video stream marker
    s = re.sub(r"__\d+$", "", s)              # dedup suffix
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return re.sub(r"-{2,}", "-", s) or "untitled"


def plan(root):
    """Return [(src, dest, index, type, title)] for one source folder."""
    moves, used = [], set()
    for folder_path in sorted(p for p in root.iterdir() if p.is_dir()):
        folder = folder_path.name
        for f in sorted(p for p in folder_path.iterdir() if p.is_file()):
            atype = artefact_type(f, folder)
            if folder in TITLED:
                base = VIDEO_ID.match(f.stem) and slugify(f.stem) or slugify(f.stem)
                idx = None
            else:
                # A dated item is identified by its date, not a fabricated index.
                idx = date_of(f.stem) or index_of(f.stem)
                base = idx or slugify(f.stem)
            title = slugify(f.stem)
            dest = folder_path / f"{base}-{atype}{f.suffix.lower()}"
            if dest in used or (dest.exists() and dest != f):
                # Quiz 1 from three offerings is quiz01_f09 / _s09 / _revi. All
                # three reduce to index 01, and a bare counter would throw away
                # which is which -- so disambiguate with what the title still
                # carries, and fall back to a counter only when nothing is left.
                disc = discriminator(title, base, atype)
                dest = folder_path / f"{base}-{atype}-{disc}{f.suffix.lower()}" if disc else dest
                n = 2
                while dest in used or (dest.exists() and dest != f):
                    dest = folder_path / f"{base}-{atype}-{disc or ''}{n}{f.suffix.lower()}"
                    n += 1
            used.add(dest)
            moves.append((f, dest, idx or "", atype, slugify(f.stem)))
    return moves


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("roots", nargs="+", type=Path)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    for root in args.roots:
        if not root.is_dir():
            continue
        moves = [m for m in plan(root) if m[0] != m[1]]
        if not moves:
            print(f"{root.name}: already normalised")
            continue
        print(f"\n{root.name}  ({len(moves)} renames)")
        for src, dest, *_ in moves[:4]:
            print(f"    {src.parent.name}/{src.name}")
            print(f"      -> {dest.name}")
        if len(moves) > 4:
            print(f"    ... and {len(moves) - 4} more")

        if args.apply:
            rows = []
            for src, dest, idx, atype, title in moves:
                rows.append({
                    "path": f"{dest.parent.name}/{dest.name}",
                    "original": src.name,
                    "folder": dest.parent.name,
                    "index": idx,
                    "type": atype,
                    "title": title,
                })
                shutil.move(str(src), str(dest))
            manifest = root / "_manifest.csv"
            with manifest.open("w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=["path", "original", "folder",
                                                   "index", "type", "title"])
                w.writeheader()
                w.writerows(sorted(rows, key=lambda r: r["path"]))
            print(f"    renamed; manifest -> {manifest}")

    if not args.apply:
        print("\nDry run. Re-run with --apply.")


if __name__ == "__main__":
    main()

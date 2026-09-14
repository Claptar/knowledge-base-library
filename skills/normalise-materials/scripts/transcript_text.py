#!/usr/bin/env python3
"""Turn a .srt/.vtt caption file into readable timestamped prose.

Caption files store one hard-wrapped fragment per cue, so a single sentence is
split across four or five of them and roughly two thirds of the file is cue
numbers and timings. This rejoins the fragments into paragraphs and keeps a
timestamp at the head of each, because those timestamps are the only pointer
back to the recording.

    python3 transcript_text.py LECTURE.srt              > lecture.md
    python3 transcript_text.py sources/ocw-*/ -o out/   # whole directory

It does not interpret anything. Spoken mathematics comes through as spoken —
"sigma squared over n" stays that phrase, because turning it into LaTeX is a
judgement the skill makes and marks, not something a parser should guess at.
"""
import argparse
import re
import sys
from pathlib import Path

CUE = re.compile(
    r"(\d{1,2}):(\d{2}):(\d{2})[,.](\d{3})\s*-->\s*(\d{1,2}):(\d{2}):(\d{2})[,.](\d{3})"
)
SENTENCE_END = re.compile(r"[.!?][\"')\]]?$")


def parse(text):
    """Yield (start_seconds, text) per cue, for both SRT and WebVTT."""
    for block in re.split(r"\n\s*\n", text.replace("\r\n", "\n")):
        lines = [l for l in block.strip().split("\n") if l.strip()]
        if not lines:
            continue
        idx = next((i for i, l in enumerate(lines) if CUE.search(l)), None)
        if idx is None:
            continue  # WEBVTT header, NOTE block, or a stray index
        m = CUE.search(lines[idx])
        h, mnt, s = int(m.group(1)), int(m.group(2)), int(m.group(3))
        body = " ".join(lines[idx + 1:]).strip()
        body = re.sub(r"<[^>]+>", "", body)          # inline cue tags
        body = re.sub(r"\s+", " ", body)
        if body:
            yield h * 3600 + mnt * 60 + s, body


def stamp(sec):
    h, rem = divmod(int(sec), 3600)
    m, s = divmod(rem, 60)
    return f"[{h}:{m:02d}:{s:02d}]" if h else f"[{m:02d}:{s:02d}]"


def paragraphs(cues, max_seconds=60):
    """Group cues into paragraphs: break on a sentence end past the time budget."""
    buf, start = [], None
    for sec, body in cues:
        if start is None:
            start = sec
        buf.append(body)
        long_enough = sec - start >= max_seconds
        if long_enough and SENTENCE_END.search(body):
            yield start, " ".join(buf)
            buf, start = [], None
    if buf:
        yield start or 0, " ".join(buf)


def convert(path, max_seconds=60):
    cues = list(parse(path.read_text(encoding="utf-8", errors="replace")))
    if not cues:
        return None
    out = [f"# {path.stem}", ""]
    for sec, text in paragraphs(cues, max_seconds):
        out.append(f"**{stamp(sec)}** {text}")
        out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", type=Path, help="caption files or directories")
    ap.add_argument("-o", "--outdir", type=Path, help="write <stem>.md here instead of stdout")
    ap.add_argument("--seconds", type=int, default=60,
                    help="minimum seconds per paragraph (default 60)")
    args = ap.parse_args()

    files = []
    for p in args.paths:
        if p.is_dir():
            files += sorted(q for q in p.iterdir() if q.suffix.lower() in {".srt", ".vtt"})
        elif p.suffix.lower() in {".srt", ".vtt"}:
            files.append(p)

    # Prefer .srt when both encodings of the same recording are present.
    stems = {f.with_suffix("").name for f in files if f.suffix.lower() == ".srt"}
    files = [f for f in files if f.suffix.lower() == ".srt"
             or f.with_suffix("").name not in stems]

    if not files:
        sys.exit("no .srt or .vtt files found")

    if args.outdir:
        args.outdir.mkdir(parents=True, exist_ok=True)

    for f in files:
        md = convert(f, args.seconds)
        if md is None:
            print(f"skipped (no cues): {f.name}", file=sys.stderr)
            continue
        if args.outdir:
            target = args.outdir / (f.with_suffix("").name + ".md")
            target.write_text(md, encoding="utf-8")
            before, after = f.stat().st_size, len(md.encode())
            print(f"{f.name:58s} {before/1024:6.0f}K -> {after/1024:5.0f}K  {target}")
        else:
            print(md)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Record what is in sources/ so it can be rebuilt, and say what cannot be.

Usage:
    uv run python skills/collect-materials/scripts/lock_sources.py [--sources DIR] [--apply]

`sources/` is gitignored: the bytes are someone else's material and mostly all-rights-reserved, so
they are never committed. What *is* committed is this lockfile — enough to restore the same
versions on another machine, and, for anything that cannot be restored, a clear statement that the
local copy is the only one.

Each source becomes one entry with a `restorable` field, which is the field that matters:

    upstream   a git repo pinned to a commit, or files with a recorded base URL — refetchable
    never      added by hand, with no upstream. **Back this up; nothing else can bring it back**
    dead       had an upstream once and it stopped resolving. Same as `never` from now on

Three fields here are **written by hand and never detected**, and `merge()` carries them across
a rescan:

    material          course | notes | thesis | paper | book | archive | data
    open_access       true for a paper that may be converted; absent means assume paywalled
    mirrors_upstream  true when base + local path is the publisher's own URL

`material` is what `normalise_source.py` reads to decide whether a source is converted at all —
books and paywalled papers never are — so guessing it is exactly the wrong move. A source with no
`material` is skipped and named in the report. (It is not `kind`, which is git-versus-files and is
about restoring the download.)

Run `restore_sources.py` to rebuild from the lockfile. Dry run is the default here too: without
--apply the lockfile is printed rather than written.
"""

import argparse
import hashlib
import subprocess
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pyyaml missing — run this with `uv run python …`, or `uv sync --group dev` first.")

SKIP_DIRS = {".git", "__pycache__", ".DS_Store"}
# A unit with few files and no documents is a website scaffold, not material. Recording the
# distinction is what stops a later session cloning an empty repo and calling it a source.
DOC_EXT = {".pdf", ".ipynb", ".rmd", ".qmd", ".tex", ".srt", ".vtt", ".ps", ".epub", ".djvu"}


def sh(args, cwd=None):
    try:
        r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=60)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:
        return None


def files_under(d: Path):
    for p in sorted(d.rglob("*")):
        if p.is_file() and not any(s in p.parts for s in SKIP_DIRS):
            yield p


def sha256(p: Path, limit=64 * 1024 * 1024):
    """Checksum a file. Large files are identified by size alone — the point is detecting that
    upstream changed, and rehashing a gigabyte of sequencing data every run is not worth it."""
    if p.stat().st_size > limit:
        return None
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def has_git_below(d: Path) -> bool:
    return any(p.is_dir() and p.name == ".git" for p in d.rglob(".git"))


def find_units(root: Path):
    """A unit is a git repo, or a maximal non-git directory with no git repo beneath it."""
    units = []

    def walk(d: Path):
        if (d / ".git").is_dir():
            units.append(("git", d))
            return
        subdirs = [p for p in sorted(d.iterdir()) if p.is_dir() and p.name not in SKIP_DIRS]
        if not has_git_below(d):
            if any(d.rglob("*")):
                units.append(("files", d))
            return
        if any(p.is_file() for p in d.iterdir()):
            units.append(("files-loose", d))
        for s in subdirs:
            walk(s)

    for p in sorted(root.iterdir()):
        if p.is_dir() and p.name not in SKIP_DIRS:
            walk(p)
    return units


# A licence declaration hides in more places than a LICENSE file. Course sites put it in a
# rendered page (`license.qmd`, `license.html`) that GitHub cannot classify, and a MyST site
# declares it in config as `license: {code: MIT, content: CC-BY-4.0}` — where the *content*
# licence is the one that governs an adaptation and the code licence is a decoy.
LICENCE_CANDIDATES = (
    "[Ll][Ii][Cc][Ee][Nn][SsCc]*", "*/[Ll][Ii][Cc][Ee][Nn][SsCc]*",
    "myst.yml", "*/myst.yml", "_quarto.yml", "*/_quarto.yml", "_config.yml", "*/_config.yml",
)
# Longest/most-restrictive fragments first: "licenses/by-nc-sa" must win over "licenses/by".
URL_LICENCES = (
    ("licenses/by-nc-sa", "CC BY-NC-SA 4.0"), ("licenses/by-nc", "CC BY-NC 4.0"),
    ("licenses/by-sa", "CC BY-SA 4.0"), ("licenses/by/", "CC BY 4.0"),
    ("publicdomain/zero", "CC0-1.0"), ("publicdomain/mark", "public domain"),
)
SPDX_LICENCES = (
    ("cc-by-nc-sa", "CC BY-NC-SA 4.0"), ("cc-by-nc", "CC BY-NC 4.0"),
    ("cc-by-sa", "CC BY-SA 4.0"), ("cc-by-4.0", "CC BY 4.0"), ("cc-by", "CC BY 4.0"),
    ("cc0", "CC0-1.0"), ("creative commons legal code", "CC0-1.0"),
    ("bsd 3-clause", "BSD-3-Clause"), ("apache license", "Apache-2.0"),
)


def detect_licence(d: Path):
    """Read the licence, never trust a metadata field.

    Returns (name, file). `unresolved` means *not found*, which is not the same as
    *not licensed* — it is an instruction to look harder before assuming the restrictive answer.
    """
    seen = []
    for pat in LICENCE_CANDIDATES:
        seen += [p for p in d.glob(pat) if p.is_file()]
    for p in seen:
        try:
            t = p.read_text(encoding="utf-8", errors="replace")[:8000]
        except Exception:
            continue
        low = t.lower()
        # A config file may name two licences; the content one governs the material.
        if p.name.endswith((".yml", ".yaml")) and "content:" in low:
            tail = low.split("content:", 1)[1][:120]
            for frag, name in SPDX_LICENCES:
                if frag in tail:
                    return name, p.name
        for frag, name in URL_LICENCES:
            if frag in low:
                return name, p.name
        for frag, name in SPDX_LICENCES:
            if frag in low:
                return name, p.name
        if "mit license" in low:
            # Usually the website theme's licence, with the template author in the copyright line.
            owner = next((l for l in t.splitlines() if "copyright" in l.lower()), "").strip()
            return "MIT (verify: %s)" % (owner or "no copyright line"), p.name
    return "unresolved", None


def build(root: Path):
    entries = []
    for kind, d in find_units(root):
        rel = d.relative_to(root).as_posix()
        fs = list(files_under(d))
        docs = sum(1 for p in fs if p.suffix.lower() in DOC_EXT)
        lic, licfile = detect_licence(d)
        e = {
            "slug": rel,
            "material": None,   # hand-written; see the docstring. merge() carries it across
            "licence": lic,
            "holds": "material" if docs >= 3 else ("scaffolding" if len(fs) < 25 else "unclear"),
            "files": len(fs),
            "bytes": sum(p.stat().st_size for p in fs),
            "fetched": date.today().isoformat(),
        }
        if licfile:
            e["licence_file"] = licfile

        if kind == "git":
            url = sh(["git", "remote", "get-url", "origin"], cwd=d)
            e.update({
                "kind": "git",
                "url": url,
                "branch": sh(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=d),
                "commit": sh(["git", "rev-parse", "HEAD"], cwd=d),
                "restorable": "upstream" if url else "never",
            })
        else:
            # No upstream is recorded by scanning — a file unit is `never` until someone adds a
            # base URL. That is deliberate: claiming something is refetchable when it is not is the
            # failure this file exists to prevent.
            e.update({
                "kind": "files",
                "base": None,
                "restorable": "never",
                "contents": [
                    {"name": p.relative_to(d).as_posix(), "bytes": p.stat().st_size,
                     "sha256": sha256(p)}
                    for p in fs
                ][:500],
            })
        entries.append(e)
    entries.sort(key=lambda e: e["slug"])
    return entries


def merge(old, new):
    """Keep hand-written fields — a base URL, a note, a `dead` marking — across regeneration."""
    by = {e["slug"]: e for e in old.get("sources", [])}
    for e in new:
        p = by.get(e["slug"])
        if not p:
            continue
        for k in ("base", "note", "catalogue", "material", "open_access",
                  "mirrors_upstream"):
            if p.get(k):
                e[k] = p[k]
        # Detection never downgrades a resolved licence. Several licences here were settled by
        # reading the course site rather than a file in the repo, and a rescan must not undo
        # that work — `unresolved` means *not found*, not *not licensed*.
        if e["licence"] == "unresolved" and p.get("licence", "unresolved") != "unresolved":
            e["licence"] = p["licence"]
            if p.get("licence_file"):
                e["licence_file"] = p["licence_file"]
        if p.get("restorable") == "dead":
            e["restorable"] = "dead"
        elif e["kind"] == "files" and e.get("base"):
            e["restorable"] = "upstream"
        if p.get("fetched"):
            e["fetched"] = p["fetched"]
    return new


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sources", type=Path, default=Path("sources"))
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    if not a.sources.is_dir():
        sys.exit(f"no such directory: {a.sources}")

    lock = a.sources / "sources.lock.yml"
    old = {}
    if lock.exists():
        old = yaml.safe_load(lock.read_text(encoding="utf-8")) or {}

    entries = merge(old, build(a.sources))
    doc = {"version": 1, "generated": date.today().isoformat(), "sources": entries}
    text = yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100)

    n = {k: sum(1 for e in entries if e["restorable"] == k) for k in ("upstream", "never", "dead")}
    total = sum(e["bytes"] for e in entries)
    irreplaceable = sum(e["bytes"] for e in entries if e["restorable"] != "upstream")

    print(f"{len(entries)} sources, {total / 2**30:.1f} GB")
    print(f"  upstream (refetchable) : {n['upstream']}")
    print(f"  never (local only)     : {n['never']}")
    print(f"  dead (upstream gone)   : {n['dead']}")
    print(f"\n{irreplaceable / 2**30:.2f} GB exists only on this machine — that is what to back up.")

    if a.apply:
        lock.write_text(text, encoding="utf-8")
        print(f"\nwrote {lock}")
    else:
        print(f"\nDry run. Re-run with --apply to write {lock}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

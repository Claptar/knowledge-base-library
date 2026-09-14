#!/usr/bin/env python3
"""Rebuild sources/ from sources.lock.yml, and report honestly what cannot be rebuilt.

Usage:
    uv run python skills/collect-materials/scripts/restore_sources.py [--sources DIR] [--apply]
    uv run python skills/collect-materials/scripts/restore_sources.py --check

`sources/` is gitignored, so a fresh clone of this repository has none of it. This restores what
has an upstream, at the exact versions recorded, and prints what does not.

Three outcomes per source, and the third is the point of the exercise:

    upstream   git repo at a pinned commit, or files under a recorded base URL — restored
    never      added by hand, no upstream. Only your backup has it
    dead       upstream stopped resolving. Same as `never`, but it used to work

**A restore that reports `never` or `dead` entries has not failed.** Those are the sources your
backup exists for, and the list is the thing to check a backup against.

`--check` verifies what is already on disk against the lockfile's checksums without fetching
anything: use it to find out whether an upstream file changed under you, or a local copy rotted.

Dry run is the default: without --apply nothing is written.
"""

import argparse
import hashlib
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pyyaml missing — run this with `uv run python …`, or `uv sync --group dev` first.")

UA = {"User-Agent": "Mozilla/5.0 (knowledge-base restore_sources.py)"}


def sha256(p: Path, limit=64 * 1024 * 1024):
    if p.stat().st_size > limit:
        return None
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def restore_git(e, dest: Path, apply: bool):
    url, commit, branch = e.get("url"), e.get("commit"), e.get("branch")
    if dest.exists():
        return "exists", ""
    if not apply:
        return "would clone", f"{url} @ {(commit or '?')[:8]}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    args = ["git", "clone", "--quiet"]
    if branch:
        args += ["--branch", branch]
    # Full clone when a commit is pinned: a shallow clone cannot check out an arbitrary commit.
    if not commit:
        args += ["--depth", "1"]
    if subprocess.run(args + [url, str(dest)], capture_output=True).returncode != 0:
        return "FAILED", url
    if commit:
        r = subprocess.run(["git", "checkout", "--quiet", commit], cwd=dest, capture_output=True)
        if r.returncode != 0:
            return "clone ok, COMMIT MISSING", commit[:8]
    return "restored", ""


def restore_files(e, dest: Path, apply: bool):
    base = e.get("base")
    if not base:
        return "no upstream", ""
    want = e.get("contents") or []
    todo = [c for c in want if not (dest / c["name"]).exists()]
    if not todo:
        return "exists", f"{len(want)} files"
    if not apply:
        return "would fetch", f"{len(todo)}/{len(want)} files from {base}"
    dest.mkdir(parents=True, exist_ok=True)
    ok = bad = 0
    for c in todo:
        url = urllib.parse.urljoin(base if base.endswith("/") else base + "/", c["name"])
        out = dest / c["name"]
        out.parent.mkdir(parents=True, exist_ok=True)
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                out.write_bytes(r.read())
        except Exception:
            bad += 1
            continue
        if c.get("sha256") and sha256(out) != c["sha256"]:
            # Not a failure to report as an error: upstream is allowed to change. But the file on
            # disk is no longer the one the lockfile describes, and silence would hide that.
            ok += 1
            print(f"      ! changed upstream: {c['name']}")
        else:
            ok += 1
    return ("restored" if not bad else f"partial ({bad} failed)"), f"{ok}/{len(todo)}"


def check(sources: Path, doc):
    print("Verifying on-disk copies against the lockfile.\n")
    missing = changed = okc = 0
    for e in doc["sources"]:
        d = sources / e["slug"]
        if not d.exists():
            print(f"  MISSING   {e['slug']}  ({e['restorable']})")
            missing += 1
            continue
        for c in e.get("contents") or []:
            p = d / c["name"]
            if not p.exists():
                print(f"  MISSING   {e['slug']}/{c['name']}")
                missing += 1
            elif c.get("sha256") and sha256(p) != c["sha256"]:
                print(f"  CHANGED   {e['slug']}/{c['name']}")
                changed += 1
            else:
                okc += 1
    print(f"\n{okc} verified, {changed} changed, {missing} missing")
    return 1 if (changed or missing) else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sources", type=Path, default=Path("sources"))
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--only", help="restore only slugs matching this regex")
    a = ap.parse_args()

    lock = a.sources / "sources.lock.yml"
    if not lock.exists():
        sys.exit(f"no lockfile at {lock} — run lock_sources.py --apply first")
    doc = yaml.safe_load(lock.read_text(encoding="utf-8"))

    if a.check:
        return check(a.sources, doc)

    entries = doc["sources"]
    if a.only:
        entries = [e for e in entries if re.search(a.only, e["slug"])]

    unreachable = []
    for e in entries:
        dest = a.sources / e["slug"]
        if e["restorable"] != "upstream":
            unreachable.append(e)
            continue
        fn = restore_git if e["kind"] == "git" else restore_files
        status, detail = fn(e, dest, a.apply)
        print(f"  {status:22} {e['slug']}  {detail}")

    if unreachable:
        total = sum(e["bytes"] for e in unreachable) / 2**30
        print(f"\n{len(unreachable)} sources cannot be restored from upstream ({total:.2f} GB).")
        print("These exist only in your backup:\n")
        for e in unreachable:
            note = e.get("note") or ("added by hand" if e["restorable"] == "never" else "")
            print(f"  {e['restorable']:6} {e['slug']:44} {e['licence']:22} {note}")

    if not a.apply:
        print("\nDry run. Re-run with --apply to fetch.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

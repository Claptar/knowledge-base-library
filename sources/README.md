# sources/

Working copies of downloaded source material — OCW notes, lecture PDFs, slides, paper preprints,
scanned chapters.

**Nothing in here is committed.** `.gitignore` excludes everything except this file. The directory
exists so that a source sits at a stable path while it is being adapted, not so that it is stored.

## Why it is not committed

- **Licence.** This repo is published as a site. Most course notes, papers and book chapters may
  not be redistributed, and the ones that may (OCW is CC BY-NC-SA) still carry conditions that a
  notes repo has no business taking on. Linking to a source carries no such conditions.
- **It is the same rule as everywhere else here.** A knowledge base that vendors its sources starts
  drifting from them the day it copies them, and the copy is the thing that goes stale. The repo
  keeps the *verdict* and the *adaptation*; the source stays where it is published.
- **Git is bad at binaries.** A PDF committed once is in the history forever, and the site build
  carries it.

## What is committed instead

| Thing | Where | Why it is the durable part |
| --- | --- | --- |
| The source's URL, and the verdict on it | [`../docs/resources/`](../docs/resources/) | the judgement is expensive; the bytes are not |
| The rewritten version | [`../docs/adapted/`](../docs/adapted/) | his own document, with motivation supplied and proofs converted |
| What he actually got from it | [`../docs/topics/`](../docs/topics/) | the trajectory, which exists nowhere else |

An adapted file names its source, the section, and the date accessed, so the original is one click
away and the adaptation can be checked against it.

## `_archives/`

The publisher's original zips, kept beside the unpacked directories. Together with each source's
`_manifest.csv` they are what makes the rename reversible: the manifest maps a normalised path back
to the publisher's filename, and the zip is the thing that filename came from. Gitignored like
everything else here — if it is lost, the catalogue entry's URL is the route back.

## `sources.lock.yml` — the one committed file

Everything here is gitignored except this lockfile, which records **what `sources/` should contain
and which parts of it cannot be got back**. One entry per source, with a `restorable` field:

| | Means | What to do |
| --- | --- | --- |
| `upstream` | a git repo pinned to a commit, or files under a recorded base URL | restored automatically |
| `never` | added by hand, no upstream — a scanned chapter, a bought book, an unpacked archive | **your backup is the only copy** |
| `dead` | it had an upstream and the link stopped resolving | same as `never` from now on |

```bash
uv run python skills/collect-materials/scripts/lock_sources.py --apply     # record what is here
uv run python skills/collect-materials/scripts/restore_sources.py --apply  # rebuild on a new machine
uv run python skills/collect-materials/scripts/restore_sources.py --check  # has anything changed or rotted?
```

A restore that reports `never` entries has **not** failed — that list is precisely what a backup is
for, and it is much smaller than the whole tree. `--check` compares on-disk files against recorded
checksums, which is how you find out that an instructor quietly replaced a PDF, or that a local
copy rotted.

**Mark a source `dead` by hand** when its link stops working. Nothing detects link rot for you, and
a `dead` entry is a useful record: it says this material existed, we had it, and the only surviving
copy is the backup.

## Backing up the part that cannot be refetched

The lockfile tells you how much of the tree is irreplaceable, and it is usually a small fraction —
books, hand-added files, and publisher archives, rather than the gigabytes of clonable course
repositories. Back **that** up rather than the whole directory.

The simplest arrangement, with no repo changes and no extra tooling: point the whole directory at a
synced folder and let the sync service hold it.

```bash
rmdir sources && ln -s ~/"Google Drive/study-sources" sources
```

Every path in the repo stays the same, nothing extra is committed, and `.gitignore` already covers
a symlink. For a machine where only the irreplaceable part matters, restore the rest instead —
that is what `restore_sources.py` is for.

**Keep `_archives/` whatever else you drop.** The six OCW courses are `never` only because they
were unpacked and renamed at ingest; their publisher zips in `_archives/` are what regenerates
them, so that one directory covers seven entries.

## Using it

Drop a download in, adapt it, and let it be deleted. If it matters, it is in `resources/` with a
link — and if the link dies, that is what `resources/` is for recording.

To keep a durable personal library across machines, point this directory at a synced folder rather
than storing files in the repo:

```bash
rmdir sources && ln -s ~/"Google Drive/study-sources" sources
```

Every path in the repo stays the same, nothing extra is committed, and no connector or auth is
involved. The `.gitignore` entry already covers a symlink.

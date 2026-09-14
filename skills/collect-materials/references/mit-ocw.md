# MIT OpenCourseWare

**Verified:** 2026-09-13. Six courses already held locally — see `docs/resources/courses.md`.

Complete course exports: lecture notes, problem sets with solutions, exams, and for some courses
video with captions. The most generous provider in this catalogue, and the only one with a blanket
licence that permits publishing adaptations.

## Where the material actually is

```
https://ocw.mit.edu/courses/<num>-<title-slug>-<term>/        the course page
https://ocw.mit.edu/courses/<num>-<title-slug>-<term>/download/   the full export
```

Take the **download bundle**, not the individual files. The per-page route means hundreds of
requests and loses the structure; the bundle is one archive with everything in it.

An export arrives as a flat pile of a few hundred files whose only structure is the naming
convention, and **OCW uses four different schemes across six courses**. Normalise once at ingest:

```bash
python3 scripts/course_inventory.py sources/<slug>      # what is in here
python3 scripts/organise_course.py  sources/<slug>      # dry run
python3 scripts/normalise_names.py  sources/<slug>      # dry run
```

Both movers need `--apply`; the inventory only reads. Keep the publisher's zip in
`sources/_archives/` — with `_manifest.csv` it is what makes the rename reversible.

**`normalise_names.py` is not idempotent** — a second `--apply` re-suffixes already-normalised
files and rewrites the manifest with the mangled names. Run it once per source, at ingest.

## What is gated

Nothing. OCW is fully public, no login, no rate limit worth worrying about.

Two real absences rather than gates:

- **Not every course has video**, and not every video has captions. A course listed as having
  lecture videos may have only a subset. Count the `.srt`/`.vtt` files rather than trusting the
  course description — `adapt-recordings` needs captions, and without them there is no transcript.
- **Some courses are notes-only**, with no problem sets or no solutions. The solutions are usually
  the reason to prefer OCW over a textbook, so check before recommending one on that basis.

## Licence

**CC BY-NC-SA**, near-universally, stated on the course page.

This is the one provider whose adaptations may be **published**: they go to `docs/adapted/` with
attribution and carry **the same licence**, because share-alike propagates. The adapted-document
template's footer exists for exactly this.

Two qualifications:

- **Check the individual course page**, because a handful carry a different licence, and
  third-party material inside a course (a reproduced figure, a chapter scan) is frequently excluded
  from the CC grant and labelled as such in place.
- **NC means non-commercial.** Fine for this repo.

The raw export is still never committed — that is a redistribution question, and `sources/` is
gitignored regardless of licence. Only the adaptation is published.

## Gotchas

- **The course number is not unique without the term.** `6.041` has several offerings, and
  `6.041SC` is the self-contained version with the fullest material — prefer the `SC` variant where
  one exists.
- **Course numbers are renumbered.** MIT renumbered much of EECS in 2022; `6.041` material is also
  found under newer numbers. The old URL usually still resolves.
- **`ocw.mit.edu` search is weak.** A site-scoped web search finds courses more reliably.
- **Transcript PDFs and caption files are different things.** The PDF is a cleaned prose transcript;
  the `.srt`/`.vtt` carries the timestamps, which `adapt-recordings` treats as its page numbers.
  Keep both where both exist.

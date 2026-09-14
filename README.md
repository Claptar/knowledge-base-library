# Study reference library

Course material, lecture notes, transcripts and papers converted to uniform markdown and split by
section, so that every part of them can be linked to.

**Browse it:** <https://claptar.github.io/knowledge-base-library/>

This is the companion to [knowledge-base](https://github.com/Claptar/knowledge-base), which holds
the study notes themselves. The split is by authorship:

| | |
| --- | --- |
| [knowledge-base](https://github.com/Claptar/knowledge-base) | his questions, trajectories, own expositions and verdicts on sources |
| this repository | everyone else's material, mechanically converted |

Nearly ten thousand converted pages would have buried seventy-odd pages of actual notes, which is
the whole reason these are two repositories.

## What is here

```
docs/<slug>/            one directory per source, mirroring sources/<slug>/
  index.md              generated contents, licence, link to the original
  **/*.md               the converted pages, one per section
docs/SUMMARY.md         generated nav
sources/                the raw downloads — gitignored in full except the lockfile
  sources.lock.yml      what should be here and how to get it back
```

Every page carries its source URL, its licence and the route it was converted by, and says so at
the top. Pages converted from a PDF carry a warning: prose survives a PDF, mathematics does not.

## Everything here is generated

Do not edit a converted file by hand — the next run overwrites it, and in the meantime it claims to
reproduce a source it no longer matches. The converter is in `skills/`:

```bash
uv sync --group dev --group convert
uv run --group convert --group dev python \
    skills/normalise-materials/scripts/normalise_source.py sources/<slug> --apply
```

See [AGENTS.md](AGENTS.md) for what is converted, what is deliberately not, and the traps.

## Licences

Material here belongs to its authors and is republished under the licence recorded in each page's
front matter, with a link to the original. Books and paywalled papers are never converted. If you
are a rights-holder and want something removed, open an issue and it will be taken down.

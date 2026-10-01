# Study reference library

Other people's courses, written up as one book per course: coherent lecture notes merged from
each course's slides, lecture recordings, notes and problem sets.

**Browse it:** <https://claptar.github.io/knowledge-base-library/>

This is the companion to [knowledge-base](https://github.com/Claptar/knowledge-base), which holds
the study notes themselves. The split is by authorship:

| | |
| --- | --- |
| [knowledge-base](https://github.com/Claptar/knowledge-base) | his questions, trajectories, own expositions and verdicts on sources |
| this repository | everyone else's courses, rewritten as books |

## What is here

```text
docs/<discipline>/<provider>/<course>/   one book per course, several course years merged
  index.md              contents, licence, and a Sources table naming every offering used
  NN-<topic>.md         the chapters
  solutions/            the course's own worked solutions, where it published them
docs/index.md           generated landing page; docs/SUMMARY.md the generated nav
sources/                the raw downloads — gitignored in full except the lockfile
  sources.lock.yml      what should be here and how to get it back
conversion-cache/       paid-for conversions and written chapters, content-addressed
```

A few small courses are not books yet and are still published as converted pages; the landing page
lists them separately.

Every page carries its source and licence at the top. A book is a derivative of every course year
it merges, so it carries the most restrictive of their licences.

## Everything here is generated

Do not edit a book by hand — the next run overwrites it. Two scripts in `skills/` make it:
`normalise_source.py` converts a source into markdown, and `synthesise_book.py` plans each course's
chapters, which are written from that material and then emitted as the book, replacing the
converted pages. [AGENTS.md](AGENTS.md) has the commands, what is deliberately not converted, and
the traps — read it before running either.

## Licences

Material here belongs to its authors and is republished under the licence recorded in each page's
front matter, with a link to the original. Books and paywalled papers are never converted. If you
are a rights-holder and want something removed, open an issue and it will be taken down.

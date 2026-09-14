# CaltechTHESIS

**Verified:** 2026-09-14 — and the verification is the point of this recipe: the site was
reachable for four record pages and then began refusing, which is the thing to plan around.

Caltech's open-access repository of dissertations and theses. Relevant here because Lior Pachter's
group publishes through it, and a thesis is the long-form version of papers already catalogued in
the knowledge base's `docs/resources/cme-transcription.md` — the same
results with the search that produced them left in.

## Where the material actually is

```
https://thesis.library.caltech.edu/<id>/              the record: title, author, advisor, abstract
https://thesis.library.caltech.edu/<id>/<n>/<file>.pdf  the full text
https://thesis.caltech.edu/<id>/                       redirects to thesis.library.caltech.edu
```

`<n>` is a document slot, and it is **not** stable at `01`: Gorin's thesis is at `/16062/03/`, and
Luebbert's at `/16368/10/`. Read the filename off the record page rather than constructing it.

The record page is the real index — advisor, committee, DOI, abstract and the rights row all live
there, and none of it is in the PDF.

## What is gated

Nothing, by policy — this is an open-access repository. **The block is rate limiting, not
authorisation**, and it does not announce itself:

```
curl   https://thesis.library.caltech.edu/16062/   ->  timeout after 30s, no response
agent  fetch of the same URL                       ->  ECONNREFUSED 131.215.225.45:443
```

while `github.com`, `pypi.org` and `ocw.mit.edu` answered normally from the same shell in the same
minute. Four record pages fetched cleanly first; the refusal began on the fifth. **Diagnose it by
fetching an unrelated host** — otherwise this reads as "the internet is down" or, worse, as the
thesis not existing.

The remedy is to wait, or to hand the URLs to the user: a browser on a normal connection is not
blocked, and `sources/` is gitignored, so a manual download costs nothing downstream.

## Licence

**Do not assume, and do not read "open access" as a grant.** CaltechTHESIS records carry a rights
row that varies by thesis:

- a Creative Commons licence, chosen by the author;
- "No commercial reproduction, distribution, display or performance rights in this work are
  provided" — which is not a licence, it is a reservation;
- nothing at all, which means default copyright, held by the author.

The row is on the record page, in the metadata table below the abstract. Read it and put it in the
catalogue entry. A thesis is converted like any other public material — see
[`AGENTS.md`](../../../AGENTS.md) — but an *adaptation* of one is a derivative work, and that is
governed by the licence, so an unresolved rights row keeps the adaptation unpublished.

## Gotchas

- **The thesis is one PDF of several hundred pages.** It converts as one lossy document unless it
  is split, which is what `normalise_source.py` does on its chapter headings — a thesis is the case
  that most rewards splitting, and the one where a single unsplit file is least usable.
- **The bibliography is the harvest.** A Pachter-lab thesis cites the lab's own papers and the
  literature behind them, with the connective argument a bibliography normally hides. Treat it as a
  source of catalogue entries, the same way a syllabus's reading list is treated.
- **Mathematics will be mangled.** These are LaTeX-built PDFs with no public source, so the PDF is
  the only route and the CME equations come through damaged. The conversion is banner-marked; the
  repair pass is `normalise-materials` step 3a, and every repair is marked `**Unverified.**`.
- **Year is the defence year, not the publication year** of the papers inside it. A 2026 thesis can
  be built from 2022 papers, so the thesis is not automatically the newer account.

## Known theses

Six, all from the Pachter group, catalogued with abstracts and rights status in
the knowledge base's `docs/resources/cme-transcription.md`.
Four are biophysical (Gorin, Fang, Felce, Carilli); two are not (Luebbert, Gálvez Merchán).

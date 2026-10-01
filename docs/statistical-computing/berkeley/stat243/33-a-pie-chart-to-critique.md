---
title: "33. A Pie Chart To Critique"
course: "Berkeley Stat 243"
chapter: 33
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 33. A Pie Chart To Critique

## What this covers

This chapter is thin by design, because the underlying material is thin: it is not a lecture but a
single exhibit. STAT 243's graphics unit keeps a short list of real-world graphics for students to
critique against the course's own checklist of good practice, and one item on that list — a
magazine-style infographic titled "Rising Cities" — is the entire content behind this chapter's
three converted copies (one per course year the file was carried forward into). The question this
chapter answers is narrow but real: what, specifically, makes this a bad pie chart, and which of the
course's stated principles does it break? It assumes only that the reader has seen an ordinary pie
chart before; nothing about the shell or about programming is needed, despite the file's name.

## What the artifact actually is

The file converted here is a one-page, image-only PDF — there is no text layer, which is why the
conversion below is a model's reading of the page rather than an extraction. It is an advertisement,
not a course document: it carries interactive callouts ("Discover more on mobile", "Download
Blippar App") typical of augmented-reality print ads from the mid-2010s, consistent with the course
itself dating it to a New York Times advertisement from December 2014.

Its content is a short case for taking urbanization seriously:

- A headline claim: the world's urban population will grow by 2.7 billion by 2050, with nearly 90%
  of that growth in Asia and Africa.
- A narrative: for most of history people lived rurally; roughly two centuries ago migration to
  cities began; around 2007 the balance tipped and, for the first time, most people on Earth lived
  in cities; mature megacities (Tokyo, New York) keep growing while most of the next wave of
  megacities is emerging in Asia and Africa; the consequence is that cities now concentrate most
  economic growth and most consumption of energy, water and food.
- A chart, captioned "Share of worldwide urban population growth from 2010–2050, by region", with
  eight regional shares: Sub-Saharan Africa 29%, India 18%, Other Asia & Oceania 17%, China 13%,
  Americas 11%, Middle East and N. Africa 8%, Europe 3%, Others 1%.

The original page also carried further graphical elements — icons or photographs — that the
conversion could only extract as separate page images with no caption information, so they are not
reproduced here.

## Why the course calls it "a crazy pie chart"

STAT 243's graphics unit does not present this file in isolation. It sits in a numbered list of
example graphics — alongside a trafficking-awareness pie chart, several news-graphic time series,
and a scatterplot of European life expectancy — that the lecture introduces with: *"think about them
in the context of some examples, some of which show \[the course's stated] principles being
violated,"* and this particular item is glossed as an example of "a crazy pie chart." The checklist
it is being measured against, from the same lecture, includes:

- Humans have a hard time comparing areas, volumes or angles — avoid representing data that way,
  including with pie charts; use position or length instead.
- Have a high density of information relative to the space a graphic occupies.
- Keep decoration from crowding out the data.

Measured against that, the chart has two separate problems. First, eight wedges is already more
than an eye can rank by angle alone. Second, and more tellingly, two of those wedges are within a
single percentage point of each other — India at 18% and "Other Asia & Oceania" at 17% — which is
well inside the margin at which a human eye can tell two pie angles apart. The only way a reader
actually recovers "India is very slightly ahead" is by reading the printed "18%" and "17%", which
means the pie itself is not doing the communicating; the numbers stapled onto it are.

<figure>
<svg viewBox="0 0 380 220" role="img" aria-label="Pie chart of the infographic's eight regional shares of urban growth, with the near-tied 18% and 17% wedges highlighted">
  <g stroke="currentColor" stroke-width="1" fill="none">
    <path d="M130,115 L130.00,35.00 A80,80 0 0 1 207.49,134.90 Z"/>
    <path d="M130,115 L68.36,165.99 A80,80 0 0 1 50.63,104.97 Z"/>
    <path d="M130,115 L50.63,104.97 A80,80 0 0 1 75.24,56.68 Z"/>
    <path d="M130,115 L75.24,56.68 A80,80 0 0 1 110.10,37.51 Z"/>
    <path d="M130,115 L110.10,37.51 A80,80 0 0 1 124.98,35.16 Z"/>
    <path d="M130,115 L124.98,35.16 A80,80 0 0 1 130.00,35.00 Z"/>
  </g>
  <g stroke="#d97706" stroke-width="1.5" fill="#d97706" fill-opacity="0.18">
    <path d="M130,115 L207.49,134.90 A80,80 0 0 1 144.99,193.58 Z"/>
    <path d="M130,115 L144.99,193.58 A80,80 0 0 1 68.36,165.99 Z"/>
  </g>
  <text x="169" y="88" font-size="12" fill="currentColor" text-anchor="middle">29%</text>
  <text x="82" y="132" font-size="12" fill="currentColor" text-anchor="middle">13%</text>
  <text x="86" y="96" font-size="12" fill="currentColor" text-anchor="middle">11%</text>
  <text x="106" y="75" font-size="12" fill="currentColor" text-anchor="middle">8%</text>
  <text x="130" y="18" font-size="11" fill="currentColor" text-anchor="middle">Europe 3% &#183; Others 1%</text>
  <text x="164" y="150" font-size="12" font-weight="600" fill="#d97706" text-anchor="middle">18%</text>
  <text x="113" y="162" font-size="12" font-weight="600" fill="#d97706" text-anchor="middle">17%</text>
  <text x="252" y="42" font-size="12" fill="currentColor">Sub-Saharan Africa — 29%</text>
  <text x="252" y="60" font-size="12" font-weight="600" fill="#d97706">India — 18%</text>
  <text x="252" y="78" font-size="12" font-weight="600" fill="#d97706">Other Asia &#38; Oceania — 17%</text>
  <text x="252" y="96" font-size="12" fill="currentColor">China — 13%</text>
  <text x="252" y="114" font-size="12" fill="currentColor">Americas — 11%</text>
  <text x="252" y="132" font-size="12" fill="currentColor">Middle East &#38; N. Africa — 8%</text>
  <text x="252" y="150" font-size="12" fill="currentColor">Europe — 3%</text>
  <text x="252" y="168" font-size="12" fill="currentColor">Others — 1%</text>
</svg>
<figcaption>The eight shares as a pie, redrawn from the infographic's own numbers. The two
highlighted wedges, India (18%) and "Other Asia &#38; Oceania" (17%), differ by only one point of
share but are not distinguishable as angles without reading the printed labels — exactly the
comparing-areas problem the course's checklist warns against.</figcaption>
</figure>

The fix the checklist points toward is not subtle: the same eight numbers laid out as a single
sorted bar (position or length, one shared baseline) would let a reader rank all eight regions, and
see how close India and the rest of Asia and Oceania actually are, without needing a single printed
percentage.

## Exercises

These are not the course's numbered homework — no problem set was supplied with this file — but
they are a direct rewriting of the critique the graphics unit's lecture explicitly invites for this
example and the others on its list.

1. Go through the "good practices for graphics" checklist point by point and decide, for this pie
   chart, whether it satisfies or violates each one. Which violations matter most for a reader
   trying to learn something from the chart in a few seconds?
2. Redraw the same eight regional percentages in a form that lets you compare Sub-Saharan Africa's
   share to India's, and India's to "Other Asia & Oceania"'s, without reading a single printed
   number off the chart.

## Sources

- The chapter's three inputs are all conversions of the same single-page, image-only PDF, reused
  across three snapshots of the course repository: `units/graphics_files/shell.pdf` in
  `berkeley-stat243/fall-2024` (CC BY 4.0) and `berkeley-stat243/fall-2025` (CC BY 4.0), and
  `units/shell.pdf` in `berkeley-stat243/stat243-fall-2021` (CC0-1.0). All three convert to
  byte-for-byte identical text; none of the three contains any course commentary of its own — the
  PDF is the advertisement itself, with no accompanying lecture prose.
- None of the three supplied files says why the course keeps this file, or names it a "crazy pie
  chart" — that framing, and the "good practices for graphics" checklist paraphrased above, are
  quoted from the same course's Graphics unit page (`units/unit12-graphics.qmd`, "1. Good practices
  for graphics", `berkeley-stat243/fall-2024` and `fall-2025`, CC BY 4.0), item 5 of its "Some
  example graphics" list, which links to this exact file. That page was not among the files
  supplied for this chapter; it was consulted only to identify what the artifact is and how the
  course uses it, since the artifact carries no such explanation itself.
- No transcript or recording of the actual in-class discussion of this graphic was supplied, so
  whatever students or the instructor said about it live is not reproduced here.
- The infographic's additional visual elements (icons/photographs extracted as separate page
  images by the conversion) are not reproduced; the conversion records only their file locations,
  with no caption or placement information.

---

[← 32. Scheduling information](32-scheduling-information.md) · [Contents](index.md) · [34. Structuring a Simulation Study →](34-structuring-a-simulation-study.md)

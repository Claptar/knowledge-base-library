---
title: 3. Markdown
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/rmarkdown-cheatsheet.pdf
source_file: sources/gtpb-psls20/background_material/rmarkdown-cheatsheet.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`background_material/rmarkdown-cheatsheet.pdf`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/rmarkdown-cheatsheet.pdf) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3. Markdown

Next, write your report in plain text. Use markdown syntax to describe how to format text in the
final report.

**syntax**

```
Plain text
End a line with two spaces to start a new paragraph.
*italics* and _italics_
**bold** and __bold__
superscript^2^
~~strikethrough~~
[link](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/www.rstudio.com)

# Header 1

## Header 2

### Header 3

#### Header 4

##### Header 5

###### Header 6

endash: --
emdash: ---
ellipsis: ...
inline equation: $A = \pi*r^{2}$
image: ![](https://raw.githubusercontent.com/GTPB/PSLS20/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/path/to/smallorb.png)

horizontal rule (or slide break):

***

> block quote

* unordered list
* item 2
    + sub-item 1
    + sub-item 2

1. ordered list
2. item 2
    + sub-item 1
    + sub-item 2

Table Header  | Second Header
------------- | -------------
Table Cell    | Cell 2
Cell 3        | Cell 4
```

**becomes**

```
Plain text
End a line with two spaces to start a new paragraph.
italics and italics (both rendered in italic type)
bold and bold (both rendered in bold type)
superscript (rendered as "superscript" with a raised 2)
strikethrough (rendered with a line through it)
link (rendered as a blue hyperlink)

Header 1
Header 2
Header 3
Header 4
Header 5
Header 6
(each header renders as a heading of the corresponding level, in decreasing size, levels 1-3
noticeably larger than 4-6)

endash: -
emdash: --
ellipsis: ...
inline equation: A = pi*r^2 (typeset as a proper equation)
image: (renders the image at path/to/smallorb.png — shown in the cheat sheet as the RStudio ball
icon)

horizontal rule (or slide break):
(a horizontal line)

block quote (indented, with a vertical bar to its left)

- unordered list
- item 2
  - sub-item 1
  - sub-item 2

1. ordered list
2. item 2
   1. sub-item 1
   2. sub-item 2
```

| Table Header | Second Header |
| --- | --- |
| Table Cell | Cell 2 |
| Cell 3 | Cell 4 |

## 4. Choose Output

Write a YAML header that explains what type of document to build from your R Markdown file.

**YAML**

A YAML header is a set of key: value pairs at the start of your file. Begin and end the header
with a line of three dashes (- - -).

```yaml
---
title: "Untitled"
author: "Anonymous"
output: html_document
---

This is the start of my report. The above is metadata saved in a YAML header.
```

*The RStudio template writes the YAML header for you* (this callout points at the "New R Markdown"
dialog from panel 2).

The output value determines which type of file R will build from your .Rmd file (in Step 6)

| output value | produces |
| --- | --- |
| `output: html_document` | html file (web page) |
| `output: pdf_document` | pdf document |
| `output: word_document` | Microsoft Word .docx |
| `output: beamer_presentation` | beamer slideshow (pdf) |
| `output: ioslides_presentation` | ioslides slideshow (html) |

---

[← 1. Workflow](01-1-workflow.md) · [Up: contents](index.md) · [5. Embed Code →](03-5-embed-code.md)

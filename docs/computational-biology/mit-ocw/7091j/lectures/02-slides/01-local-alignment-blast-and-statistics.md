---
title: Local Alignment (BLAST) and Statistics
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/02-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Local Alignment (BLAST) and Statistics

7.36 / 20.390 / 6.802

7.91 / 20.490 / 6.874 / HST.506

Lecture #2

C. Burge

Feb. 6, 2014

---

## Topic 1 Info

• CB office hours
- after lectures (Tues/Thurs 2:30-3:00) - 68-271A (except today)
- or by request
• Slides will generally be posted (PDF) by 12:15 pm on day of lecture*

• Overview slide has blue background - readings for upcoming lectures are listed at bottom of overview slide

• Review slides will have purple background

• PS1 is posted

• PS2 will be posted soon. Look at the programming problem

The two Python tutorials will be:

Friday, Feb. 7 3:00 – 4:00 PM
Monday, Feb. 10 4:00 – 5:00 PM

\* If printing, to save paper, can print multiple slides per page using Acrobat Reader.
Under “Page scaling:” choose “Multiple pages per sheet”

---

## For those reg’d for grad versions of course

• Please email by Tuesday Feb 11th:

Name
Email
G/U Program_name
Background (1 sentence)
Comp Bio Interests (1 sentence or a few keywords)

for posting

---

• Sequencing
- Conventional
- 2nd generation

• Local Alignment:
- a simple BLAST-like algorithm
- Statistics of matching
- Target frequencies and mismatch penalties for nucleotide alignments

Background for next two lectures: Z&B Ch. 4 & 5

---

## 1D, 2D and 3D Representations of DNA

© Cancer Research UK. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Types of Nucleotides

• ribonucleotide
• deoxyribonucleotide
• dideoxyribonucleotide

---

## Sanger sequencing method

Primer
5' NNN
3' NNNCATGAGACAGTC…
Template

+ ddGTP:
ddG
GTACTCTddG
GTACTCTGTCAATGddG
GTACTCTGTCAGTATCddG
GTACTCTGTCAGTATCGT

+ ddATP:
GTddA
GTACTCTGTCAA
GTACTCTGTCATddA
GTACTCTGTCAGTATCGT

+ ddCTP:
GTAddC
GTACTddC
GTACTCTGTddC
GTACTCTGTCAGTATddC
GTACTCTGTCAGTATCGT

+ ddTTP:
GddT
GTACddT
GTACTCddT
GTACTCTGddT
GTACTCTGTCATddT
GTACTCTGTCATGddT
GTACTCTGTCAGTATCddT
GTACTCTGTCAGTATCGT

gel electrophoresis
autoradiography (if radiolabeled)

---

## Evolution of Sequencing Technologies

• Traditional Sanger / chain termination sequencing (70s, 80s, 90s)

A T C G …
• Large polyacrylamide gels, radiolabeled DNA, 4 lanes per read

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

• Fluorescent-based / dye terminator sequencing (90s - present)

• Capillary electrophoresis, fluorescent tags for each base, 1 lane per read

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## ‘Next Generation’ Sequencing Technologies

cycle 1
What is base 1?

cycle 2
What is base 2?

cycle 3
What is base 3?

Courtesy of Macmillan Publishers Limited. Used with permission.
Source: Shendure, Jay, and Hanlee Ji. "Next-generation DNA Sequencing." Nature Biotechnology 26, no. 10 (2008): 1135-45.

A variety of technologies. Differ in aspects of:

• DNA template
• Modified nucleotides used
• Imaging / image analysis

Metzker NRG 2010

---

---

[Up: contents](index.md) · [Comparison of Platforms →](02-comparison-of-platforms.md)

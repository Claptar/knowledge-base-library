---
title: 1 Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/section/millman-perez.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/section/millman-perez.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Introduction

**Source:** [`section/millman-perez.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/section/millman-perez.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Computational tools are at the core of modern research. In addition to experiment and theory, the notions of simulation and data-intensive discovery are often referred to as “third and fourth pillars” of science [12]. It is more accurate to simply accept that computing is now inextricably woven into the DNA of science, as today, even theory and experiment are computational. Experimental work requires computing (whether in data collection, preprocessing, or analysis) and theoretical work requires symbolic manipulation and numerical exploration to develop and refine models. Scanning the pages of any recent scientific journal, one is hard-pressed to find an article that does not depend on computing for its findings.

Yet, for all its importance, computing receives perfunctory attention in the training of new scientists and in the conduct of everyday research. It is treated as an inconsequential task that students and researchers learn “on the go” with little consideration for ensuring computational results are trustworthy, comprehensible, and ultimately a secure foundation for reproducible outcomes. Software and data are stored with poor organization, little documentation, and few tests. A haphazard patchwork of software tools is used with limited attention paid to capturing the complex workflows that emerge. The evolution of code is not tracked over time, making it difficult to understand what iteration of the code was used to obtain any specific result. Finally, many of the software packages used by scientists in research are proprietary and closed-source, preventing complete understanding and control of the final scientific results.

We argue that these considerations must play a more central role in how scientists are trained and conduct their research. Our approach grows out of our experience as part of both the research and the open source scientific Python communities. We begin ( _§_ 2) by outlining our vision for scientific software development in everyday research. In the remaining sections, we provide specific recommendations for computational work. First, we describe the routine practices ( _§_ 3) that should be part of the daily conduct of computational work. We next discuss tools and practices developed by open source communities to enable and streamline collaboration ( _§_ 4). Finally, we present an approach to developing and communicating computational work that we call _literate computing_ in contrast to the traditional approach of literate programming ( _§_ 5).

---

[← Contents](01-contents.md) · [Up: contents](index.md) · [2 Computational research →](03-2-computational-research.md)

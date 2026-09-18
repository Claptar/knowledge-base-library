---
title: 2. LOOKING AT INFOVIS THROUGH STATISTICIANS’ EYES
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/gelmanUnwin2013.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/gelmanUnwin2013.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/gelmanUnwin2013.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/gelmanUnwin2013.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2. LOOKING AT INFOVIS THROUGH STATISTICIANS’ EYES

We begin our story in December 2008, when statistician and graphic designer Nathan Yau published on his influential Flowing Data blog$^1$ a list of what he viewed as the five best data visualizations of the year (Yau 2008b). We were struck by the discrepancy between the visual appeal of these displays and their divergence from the usual principles of statistical graphics.

---

$^1$It may be unusual for a journal article to be reacting to a blog—but the blog in question has approximately 15,000 subscribers, about three times more than the most prominent academic statistics blogs and more readers per day than many scientific journals get per year. And the issue is not just circulation. Thanks to Yau and his commenters, Flowing Data is a thoughtful forum on the interface between statistics and graphic design.

Upon further reflection, and after a blog exchange (Gelman 2009a; Yau 2009), we decided that our difficulties with some popular visualizations arose from an insufficient understanding—by ourselves and others—of the multiplicity of goals involved in data display. These goals reflect the differing interests and approaches of two different groups: on the statistical side, data analysts and statisticians are interested in finding effective and precise ways of representing data, whether raw data, statistics, or model analyses. Providing the right comparisons is important, numbers on their own make little sense, and graphics should enable readers to make up their own minds on any conclusions drawn, and possibly see more. On the Infovis side, computer scientists and designers are interested in grabbing the readers’ attention and telling them a story. When they use data in a visualization (and data-based graphics are only a subset of the field of Infovis), they provide more contextual information and make more effort to awaken the readers’ interest. We might argue that the statistical approach concentrates on what can be got out of the available data and the Infovis approach uses the data to draw attention to wider issues. Both approaches have their value, and it would probably be best if both could be combined.

The present article comes, unavoidably, from a statistical perspective, and we discuss ways in which several popular data visualizations do not serve statistical goals. We are not writing this as a critique of the Infovis approach; our intent is to consider the goals being served by graphical displays that we might not choose ourselves, with the ultimate goal of improving communication among graphic designers, statisticians, and users of statistical methods. This is not a division between disciplines so much as a debate going on within all these fields.

One issue that arises is the familiar distinction between exploratory and presentation graphics. With presentation graphics, you prepare some small number of graphs, which may be viewed by thousands, and with exploratory graphics, you prepare thousands of graphs, which are viewed by one person, yourself. Exploratory graphics are all about speed and flexibility and alternative views. Presentation graphics are all about care and specifics and a single view. Presentation graphics can really benefit from a graphic designer’s contribution; for exploratory graphics, it is not so relevant. That said, the first consumer of any graph is the person who makes it, and it can often be useful to use “presentation” skills to communicate to ourselves as well as to others. In either context, much can be gained by thinking carefully about goals.

In this article, we will be writing primarily about static presentation graphics, a well-established and mature field. Modern exploratory data analysis involves using interactive graphics, and such tools are also frequently used for Infovis graphics in Web displays, along with sound and video. However, these approaches are very much in a development phase and we would prefer to encourage further experimentation rather than comment on what are still early efforts.

Data graphics are increasingly being produced in all sorts of contexts. We are happy to see the increasing recognition of the importance of visualizing data, but we have some concerns that practitioners are not fully aware of the multiplicity of goals that arise in graphical presentation. In the present article, we lay out some of these conflicting goals and discuss how awareness of some underlying principles of statistical communication could improve the work of statisticians and graphic designers alike.

---

[← 1. INTRODUCTION](03-1-introduction.md) · [Up: contents](index.md) · [3. UNDERSTANDING AND DIALOGUE RATHER THAN PURE CRITICISM →](05-3-understanding-and-dialogue-rather-than-pure-criticism.md)

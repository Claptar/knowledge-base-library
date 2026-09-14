---
title: Data Management
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s04/bestpractices2017.md
source_file: sources/berkeley-stat243/stat243-fall-2017/section/s04/bestpractices2017.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data Management

**Source:** [`section/s04/bestpractices2017.md`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s04/bestpractices2017.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

My previous research involved fluorescent microscopy and flow imaging so we used Box/Dropbox/Google Drive to store our image data (~1GB per image) and subsequent analysis. Are there better ways to store and share files like these?
A: datproject, dataversion control

Is there a way to avoid data dropping during merge? They point out a situation that many observations data were dropped in a merge, and after they included the dropped observations, the results change. However, it seems they did not mention a solution to avoid data dropping through merge.

Does every dataset need to be normalized? It seems normalizing data takes time and energy. Gentzkow and Shapiro mention some well-trained people can organize data into relational database. When do we need to normalize our data?

---

[← Workflow management](02-workflow-management.md) · [Up: contents](index.md) · [To what extent? →](04-to-what-extent.md)

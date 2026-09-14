---
title: Alignment
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-14-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Alignment

**Source:** `recitations/2014-02-14-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

36

## Alignment


Biological Sequence Analysis - Durbin

37

## Local alignment example

Do a local alignment between these using PAM250 and gap penalty -2:

### **AWEK FWEF**

> © unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

38

## Local alignment solution


alignment:

W E W E

39

## Global alignment solution


alignment: A W E K F W E F

40

||**Global**|**Semiglobal**|**Local (gapped)**|
|---|---|---|---|
|**Penalties at edges?**|Yes|No|No|
|**Reset to 0 instead**<br>**of including**<br>**negative entries?**|No|No|Yes|
|**End of alignment**|Bottom right entry|Highest score entry<br>in bottom row or<br>rightmost column|Highest score entry<br>in matrix|


41

## Reminders

- Pset 1 posted – due Feb 20<sup>th</sup> (no extra problem)

- Pset 2 posted – Due Mar 13<sup>th</sup>

- Project teams due – Feb 25<sup>th</sup>

   - Interests and background directory has been posted

- Lecture videos will be posted on MITx soon – next week?

42

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802 / 6.874 / HST.506 Foundations of Computational and Systems Biology Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Biology Review](02-biology-review.md) · [Up: contents](index.md)

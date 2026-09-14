---
title: Is the p53 pathway activated?
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Is the p53 pathway activated?

**Source:** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Formulate problem probabilistically

- Compute

   - P(p53 pathway activated| data)

- How?

   - Relatively easy to compute p(X up | TF up)

   - Look over lots of experiments and tabulate:

      - X1 up & TF up

      - X1 up & TF not up

      - X1 not up & TF not up

      - X1 not up & TF up


<!-- Start of picture text -->
TF<br>X1  X2  X3<br><!-- End of picture text -->

105

Is the p53 pathway activated?

• Formulate problem probabilistically

• Compute

– P(p53 pathway activated| data)

• How?

– Relatively easy to compute p(X up | TF up)

– P(TF up|X up) = p(X up | TF up) p(TF up)/p(X up)

TF X1 X2 X3 106

Is the p53 pathway activated?

• Formulate problem probabilistically

• Compute

– P(p53 pathway activated| data)

- How?

– Even with p(TF up | X up) how do we compare this explanation of the data to other possible explanations?

– Can we include upstream data?

TF


X1 X2

X3 107

---

[← Is the p53 pathway activated?](43-is-the-p53-pathway-activated.md) · [Up: contents](index.md) · [Application to Gene Networks →](45-application-to-gene-networks.md)

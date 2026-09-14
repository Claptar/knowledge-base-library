---
title: Hypergeometric Test
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Hypergeometric Test

**Source:** `recitations/2014-03-05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For this example, we obtain:

100 _≥ P_ ( _x_ 40) = _P_ ( _i_ ; 100 _,_ 150 _,_ 500) X _i_ =40 _− − − −_ 100<sup><u>�</u></sup> 100 _i_<sup><u>��</u></sup> 500150 100 _i_<sup><u>�</u></sup> = X _i_ =40 ~~�~~ 500150 ~~�~~

= 0 _._ 0112


Therefore, with α = 0.05, we reject the null hypothesis that the overlap between conditions A and B are due to random chance, suggesting there is some similarity between gene expression changes caused by heat shock and oxidative stress

32

## Principal Component Analysis (PCA)

- Typical high-throughput biological experiment: thousands of measurements (e.g. 20,000 gene expression levels)

   - High dimensional data are hard to visualize and interpret

- Can use Principal Component Analysis (PCA): mathematical algorithm for reducing the dimensionality of the data while retaining most of the variation in the data set

   - Accomplishes this reduction by identifying directions, called principal components, along which the variation in the data is maximal

   - By using a few components, each sample can be represented by relatively few numbers instead of thousands values for thousands of variables

   - Can then plot samples in 2D or 3D space by using the top 2 or 3 principal components

33

### PCA identifies the directions along which the data have the largest spread


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Ringnér, Markus. "What is Principal Component Analysis?" _Nature Biotechnology_ 26, no. 3 (2008): 303-4.

- **1**<sup>**st**</sup> **principal comp** **~~o~~ nent (PC1)** is the direction of maximal variation among your data - Magnitude of ~~th~~ is component is related to how much variation there is in this

- direction

- **2**<sup>**nd**</sup> **principal com** **~~po~~ nent (PC2)** is next direction ~~o~~ f remaining maximal variati ~~on~~ in

- your sample that is ~~p~~ erpendicular to PC1

   - Magnitude of ~~th~~ is component will be smaller than that of 1<sup>st</sup>

- and so on for PC3 ~~,~~ PC4, etc. (each PC must be orthogonal to all previous PCs)

###### See 2 page Nature Biotech Primer:

http://www.nature.com/nbt/journal/v26/n3/pdf/nbt0308-303.pdf

34

#### PCA identifies the directions along which the data have the largest spread


-Succssive principal components explain smaller and smaller amounts of variance in the data –this is w ~~h~~ y summarizing data with fir ~~s~~ t 2 or 3 components is an O ~~K~~ first approximation of d ~~at~~ a

- ~~Th~~ is example: first 2

- c ~~omponents retain 22% of~~ total variance; 63 components retain 90% of variance

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Ringnér, Markus. "What is Principal Component Analysis?" _Nature Biotechnology_ 26, no. 3 (2008): 303-4.

-Visualizing data points as projections onto fir ~~st~~ PCs often reveals “cl ~~u~~ stering” of samples into groups – but ma ~~ke~~ sure these are biol ~~o~~ gi ~~c~~ ally relevant and not technic ~~al~~ artifacts (e.g., s ~~amp~~ <u>les cluster</u> into 2 groups based ~~o~~ n which ~~of two~~ different days libraries were prepared)

###### See 2 page Nature Biotech Primer:

http://www.nature.com/nbt/journal/v26/n3/pdf/nbt0308-303.pdf

35

---

[← Hypergeometric Test](17-hypergeometric-test.md) · [Up: contents](index.md) · [Single-cell RNA-seq →](19-single-cell-rna-seq.md)

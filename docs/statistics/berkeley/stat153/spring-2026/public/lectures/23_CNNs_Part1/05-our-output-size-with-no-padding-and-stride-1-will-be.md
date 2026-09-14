---
title: our output size with no padding and stride 1 will be
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/23_CNNs_Part1.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/23_CNNs_Part1.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# our output size with no padding and stride 1 will be

**Source:** [`public/lectures/23_CNNs_Part1.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/23_CNNs_Part1.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

the general formula for the convolution is:


## **Step by step**

• Position (1,1), kernel aligned with top-left 3x3 patch of input


- Position (1,2), slide one column right


- Position (2,1), left edge, one row down


- Position (2,2), right edge, one row down


### **Convolution can be used to find local structure**


<!-- Start of picture text -->
?<br>=<br><!-- End of picture text -->


**Convolution can be used to find local structure**

## **Finding local structure**


**Translation invariant**

## **Other details - padding**

- A way to deal with the edges of image


“Valid” padding - no “Same” padding - output padding, output shrinks matches input size


“full” padding - output is larger than input (rare)

## **Discussion**

• if you were thinking about this in a time series context, how might you think about padding across different directions? (forward or backward in time)

## **Other details - stride**


stride = 1

stride = 2, with padding

## **What do you think would happen?**

Given an image _A_ and the kernel _K_ below


<!-- Start of picture text -->
K<br><!-- End of picture text -->


<!-- Start of picture text -->
Image  A<br><!-- End of picture text -->

---

[← Dumouilin and Visin 2018](04-dumouilin-and-visin-2018.md) · [Up: contents](index.md)

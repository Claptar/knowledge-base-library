---
title: Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/project/givens_hoeting_ch3.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/project/givens_hoeting_ch3.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`project/givens_hoeting_ch3.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/project/givens_hoeting_ch3.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**CHAPTER** **_<u>3</u>_**

# _COMBINATORIAL OPTIMIZATION_

It is humbling to learn that there are entire classes of optimization problems for which most methods—including those described previously—are utterly useless.

We will pose these problems as maximizations except in Section 3.3, although in nonstatistical contexts minimization is often customary. For statistical applications, recall that maximizing the log likelihood is equivalent to minimizing the negative log likelihood.

Let us assume that we are seeking the maximum of _f_ ( **_θ_** ) with respect to **_θ_** = ( _θ_ 1 _, . . . , θp_ ), where **_θ_** ∈ **_�_** and **_�_** consists of _N_ elements for a finite positive integer _N_ . In statistical applications, it is not uncommon for a likelihood function to depend on configuration parameters that describe the form of a statistical model and for which there are many discrete choices, as well as a small number of other parameters that could be easily optimized if the best configuration were known. In such cases, we may view _f_ ( **_θ_** ) as the log profile likelihood of a configuration, **_θ_** , that is, the highest likelihood attainable using that configuration. Section 3.1.1 provides several examples.

Each **_θ_** ∈ **_�_** is termed a _candidate solution_ . Let _f_ max denote the globally maximum value of _f_ ( **_θ_** ) achievable for **_θ_** ∈ **_�_** , and let the set of global maxima be _M_ = { **_θ_** ∈ **_�_** : _f_ ( **_θ_** ) = _f_ max}.Ifthereareties, _M_ willcontainmorethanoneelement. Despite the finiteness of **_�_** , finding an element of _M_ may be very hard if there are distracting local maxima, plateaus, and long paths toward optima in **_�_** , and if _N_ is extremely large.

---

[Up: contents](index.md) · [3.1 HARD PROBLEMS AND NP-COMPLETENESS →](02-3-1-hard-problems-and-np-completeness.md)

---
title: Introduction
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/23-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/23-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# 4.4 Dynamics on Networks

So far, we simply identified the topology of connections between the nodes of a network. In many cases the connectivity is merely the prelude to describing the different states of the network that may arise from the coordinated evolution of its elements. Let us assign a variable xi(t) to each node, whose time evolution is governed by


We have assumed that the dynamics is governed by coupled first order differential equations in time. This is a good approximation in many biological problems. For example, a network of chemical reactions, or proteins and mRNA, could be described (in the mean-field limit) by a set of rate equations for the concentrations Ci(t), such that


For example, in the simple reaction A+B<sup>k−</sup> ⇌k+ C, the concentration of A varies as


What dynamic behaviors can be encoded in such systems of equations? We shall discuss stationary fixed points and cycles as important examples.

---

[Up: contents](index.md) · [4.4.1 Attractive fixed points →](02-4-4-1-attractive-fixed-points.md)

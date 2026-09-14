---
title: Introduction
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentySix153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentySix153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`LectureTwentySix153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentySix153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **STAT 153 & 248 - Time Series Lecture Twenty Six**

**Fall 2025, UC Berkeley**

Aditya Guntuboyina

Dec 04, 2025

## **1 AR to LSTM**

We have an observed time series _{yt}_ . We want to predict future values of this time series. We convert this time series data to regression data ( _xt, yt_ ) via: _xt_ = ( _yt−_ 1 _, . . . , yt−p_ ) for some _p ≥_ 1. We will re-index so that _xt_ and _yt_ are both defined for _t_ = 1 _, . . . , n_ . The models described below will apply to this regression setup. Each model will give a predicted value _µt_ for _yt_ ; _µt_ will be a function of _xt_ as well as past _x_ -values _xt−_ 1 _, xt−_ 2 _, . . . , x_ 1. Our loss function will be the squared error loss<sup>�</sup><sup>_n_</sup> _t_ =1<sup>(</sup><sup>_yt −µt_)2.</sup><sup>_µt_willdependonvariousparameters</sup> defining the model which will be estimated by least squares (in practice, this least squares problem will solved by some variant of the gradient descent algorithm).

---

[Up: contents](index.md) · [1.1 AR ( p ) →](02-1-1-ar-p.md)

---
title: 2 The Sinusoid
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeven153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 The Sinusoid

**Source:** [`LectureSeven153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

When we say sinusoid, we refer to the following function of time _t_ :


Here

- _R_ is called the _amplitude_ . It represents the height of the oscillation from its center line.

- _f_ is called the _frequency_ . It represents the number of oscillations in unit time. If time is measured in seconds, then the unit of _f_ is Hertz (Hz).

1

- 1 _/f_ is called the _period_ . It is the length of time to complete one full oscillation.

- _ϕ_ is called the _phase_ . Without _ϕ_ (i.e., if _ϕ_ = 0), then the above sinusoid becomes _β_ 0 + _R_ cos(2 _πft_ ) so it starts at its maximum value at _t_ = 0. Adding _ϕ_ shifts the wave left or right in time. This captures the fact that different oscillations might ’start’ at different points in their cycle.

- 2 _πf_ is called the _angular frequency_ . Sometimes we use the notation _ω_ = 2 _πf_ for the angular frequency. It measures the rate of change of the angle inside the cosine.

Using the formula cos( _α_ + _β_ ) = (cos _α_ )(cos _β_ ) _−_ (sin _α_ )(sin _β_ ), we can represent the sinusoid (2) in the following equivalent alternative form:


The parameters _β_ 1 _, β_ 2 in (3) are related to _R, ϕ_ in (2) via _β_ 1 = _R_ cos _ϕ_ and _β_ 2 = _R_ sin _ϕ_ . While working with models involving sinusoids, we use the representation (3) because the parameters _β_ 1 and _β_ 2 appear linearly in (3).

---

[← 1 The Sinusoidal Model](01-1-the-sinusoidal-model.md) · [Up: contents](index.md) · [3 Discrete sampling and restricting f to [0 , 1 / 2] →](03-3-discrete-sampling-and-restricting-f-to-0-1-2.md)

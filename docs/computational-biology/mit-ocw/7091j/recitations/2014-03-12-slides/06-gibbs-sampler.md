---
title: Gibbs Sampler
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-12-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Gibbs Sampler

**Source:** `recitations/2014-03-12-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Type of Markov Chain Monte Carlo (MCMC) algorithm that relies on probabilistic optimization

   - Relies on repeated random sampling to obtain results

   - Due to randomness, can get different results from same starting condition; generally want to run algorithm many times and compare results to see how robust solution is

   - Determining when to stop is less well defined since random updates may or may not change at each iteration

   - Not forced to stay in local minimum; possible to “escape” it during a random sampling step

   - Initialization is less important; results from different initializations will often return similar results since they will “cross paths” at some point (sampling step)

      - Contrast this with a deterministic algorithm like the EM algorithm (GPS ChIP-seq peak-finding) – initial conditions are more important and results are deterministic given those initial conditions; cannot escape being stuck in local minimum

8

---

[← Mean-bit score of a motif](05-mean-bit-score-of-a-motif.md) · [Up: contents](index.md) · [Gibbs Sampler →](07-gibbs-sampler.md)

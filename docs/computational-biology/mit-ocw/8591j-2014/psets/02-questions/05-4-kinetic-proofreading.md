---
title: 4 Kinetic Proofreading
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/02-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Kinetic Proofreading

**Source:** `psets/02-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Many cellular processes, such as transcription of a gene, translation of mRNA, or even the recognition of an antibody by a T-cell require high delity. During translation, for example, the ribosomes

3

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 2

are attempting to perform their enzymatic function on a particular substrate, but many other substrates in the cell look similar so it is dicult to perform the enzymatic function accurately. Yet, translation errors occur at typical rates as low as _∼_ 10<sup>_−_4</sup> . In this problem, we will look at a mechanism that is employed to achieve such high accuracy. This was rst suggested by J. J. Hopeld (see ref at end).

Let c be a recognition site, to which two substrates can bind, C, the correct and D, the wrong one. The correct complex then produces the expected product:


The rate of product formation from the complex ( _W_ ) is determined by the strength of the covalent bonds between, for example, two amino acids, and is approximately the same for both the products.

Fidelity is quantied in terms of the error fraction _f_ , which is the ratio of rate of production of wrong product to correct product.

- a. Assuming that the substrate concentrations in the cell are mainteined at a constant (and equal) value for C, D, what is the error fraction? In the limit of _W << kc_ , the error fraction is minimized. What is this minimum value, _f_ 0 ? (Note that being in the same medium, the concentration of the recognition sites, c, is the same for both reactions)

Now consider adding an additional intermediate state of the complex in the above reaction:


- b. What is the error rate in this process? Detailed balance puts a restriction on the values that _m, m_<sup>_′_</sup> can take. What is this constraint? It turns out that under this constraint, _f ≥ f_ 0 , so this might not seem like a good method to increase delity.

Next assume steps 2, 3 in the above reaction are one way steps, i.e. _m_ = 0 _, lc′_ = 0 . The reaction steps can be made strongly directed like this by coupling them with other strongly driven reactions, such as ATP hydrolysis, so that they are nearly one way.

- c. If _m_<sup>_′_</sup> _< kc_ , so that you can assume reaction 1 is in quasi-equilibrium by itself, and with _m_ = 0 _, lc′_ = 0 , show that the error fraction now is _≈ f_ 0 2<sup>.(Theratiooforatesforthe</sup> original and modied complex is the same, since it involves the same substrate falling o.)

Adding multiple steps like this can greatly increase the specicity of the reaction. With _n_ one way steps, the error fraction can be lowered to _f_ 0<sup>_n_.However,ateachofthesesteps,thecellhas</sup> to consume energy (for ATP hydrolysis), so this is a costly function. Another mechanism involves introducing a delay between complex formation and product precipitation. Since the dissociation rate of the worng substrate is higher, this delay allows more time for the wrong substrate to fall o. See Uri Alon proofreadign chapter for details.

Ref: Kinetic Proofreading: A New Mechanism for Reducing Errors in Biosynthetic Processes Requiring High Specicity, J. J. Hopeld, PNAS 71(10), 4135-4139

4

MIT OpenCourseWare http://ocw.mit.edu

8.591J / 7.81J / 7.32 Systems Biology Fall 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 3 Positive feedback and bistability (12 points)](04-3-positive-feedback-and-bistability-12-points.md) · [Up: contents](index.md)

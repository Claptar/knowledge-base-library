---
title: 'Estimation Road Map: D/S/A algorithm for computing the optimal index set'
source: https://vanderlaan-lab.org/teach-files/dsaslides.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/dsaslides.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Estimation Road Map: D/S/A algorithm for computing the optimal index set

**Source:** [`dsaslides.pdf`](https://vanderlaan-lab.org/teach-files/dsaslides.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- The goal is to estimate

I0(Pn) ≡ arg min L(o, Ψ<sup>ˆ</sup> I (Pn) | υ0)dP0(o). I∈I �

Estimation of I0(Pn) involves a two-stage procedure:

- Find the best choice within Is using the empirical risk function, to find the best choice within Is;

- Find the best choice of s using the cross-validated risk function.

Nov. 8, 2004

12

The D/S/A algorithm (Sinisi and van der Laan (2004)) maps the current index set I<sup>0</sup> ∈I of size k into three collections of index sets, namely, deletion set DEL(I<sup>0</sup> ), substitution set SUB(I<sup>0</sup> ), and addition set ADD(I<sup>0</sup> ), of size k − 1, k and k + 1, respectively. Let I<sup>0</sup> = {⃗p<sup>0</sup> 1<sup>, . . .⃗p0</sup> k<sup>} denote the current</sup> index set, where⃗p<sup>0</sup> i<sup>∈Nd, i = 1, 2, · · · , k:</sup>

- DEL(I<sup>0</sup> ) is a set of index sets I where the i<sup>th</sup> vector⃗p<sup>0</sup> i<sup>is</sup> deleted from I<sup>0</sup> , for i = 1, 2, · · · , k;

- • SUB(I<sup>0</sup> ) is a set of index sets I where the i<sup>th</sup> vector⃗p<sup>0</sup> i<sup>is</sup> substituted by one of the new vectors⃗pij =⃗p<sup>0</sup> i<sup>+ δej, where</sup> δ = {−1, 1}, j = 1, 2, · · · , d, for i = 1, 2, · · · , k;

- ADD(I<sup>0</sup> ) is a set of index sets I obtained by adding one of the unit vector ej or one of the new vectors⃗pij in SUB(I<sup>0</sup> ) to I<sup>0</sup> , j = 1, 2, · · · , d, for i = 1, 2, · · · , k.

Nov. 8, 2004

13

Deletion/Substitution/Addition Algorithm

Nov. 8, 2004 14


Nov. 8, 2004

15

---

[← Estimation Road Map: Generating candidate estimators](04-estimation-road-map-generating-candidate-estimators.md) · [Up: contents](index.md) · [Estimation Road Map: Selection of nuisance parameter models →](06-estimation-road-map-selection-of-nuisance-parameter-models.md)

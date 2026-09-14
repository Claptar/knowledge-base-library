---
title: 4.6 Turing patterns
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/24-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4.6 Turing patterns

**Source:** `lectures/24-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

So far we explored variations of a set of variables in time, ignoring dependencies on space. In fact cells actively compartmentalize different molecules in different locations. Genetic information is localized to the nucleus and has to be carried out to the rest of the cell by diffusion of various molecules (mRNA or proteins). Even in the absence of physical barriers,

85

chemical reactions can give rise to interesting patterns of spatio-temporal concentration variations. Since diffusion is the most common mechanism for transport of molecules in space, we shall examine the following set of reaction–diffusion equations


Here, Di is the diffusion coefficient for molecular species i (with concentration Ci) and the reactions are described by local non-linear terms included in {Ci}. Intrigued by the question of how biological patterns (e.g. body shapes, or colorations of animal coats) occur in the first place, Turing postulated a set of morphogens whose concentrations evolve as in Eqs. (4.48).

Let us specifically ask if it is possible to have a stable fixed point {Ci<sup>∗}assolution</sup> to Eqs. (4.48) if spatial variations are forbidden (as in a very well mixed bag with very large {Di}), but which becomes unstable if spatial variations are permitted. To answer this question, let us linearize the reaction-diffusion equations around the fixed point as


Stability of the uniform solution implies that all eigenvalues of the matrix Mij are negative. To examine the stability with respect to spatial variations we introduce Fourier transforms


in terms of which Eq. (4.49) becomes


The original question can now be recast as whether the matrix Mij(k) = Mij − δijDik<sup>2</sup> can have a positive eigenvalue at a finite wave-vector⃗k. The answer is clearly negative if only one chemical species is present, in which case λ(k) = λ(0) − Dk<sup>2</sup> is obviously more negative (hence more stable) at finite⃗k. However, Turing showed that even with two morphogens it is possible to find a finite wave-length instability.

Let us examine the 2 × 2 linear-stability matrix


The product of the two eigenvalues is given by the determinant of the above matrix as


86

At k = 0 (uniform state) both eigenvalues are by fiat negative, and thus det M(0) (the term within the first brackets above) is positive. It is possible that both eigenvalues remain negative at all wavevectors, as depicted by the curves marked by 1 and 2 in the Figure below. For the fixed point to become unstable to a perturbation at finite k, the larger eigenvalue, λ+(k), has to pass through zero and become positive. Note that since


the other eigenvalue, λ−(k), has to become even more negative. Since both the first and last terms in Eq. (4.53) are positive, a change of sign for the eigenvalue is only possible if the middle term is large and positive, i.e.


(The latter is required by the stability condition for k = 0.) If so, then Eq. (4.53) can describe a curve that crosses zero at two points, k+ and k−, with a maximum at an intermediate km. There will then be a band of unstable modes spanning wave-numbers from k− to k+ (curves labelled by 3 in the figure), and by setting this equation (and its derivative) to zero, it is easily checked that


87

The value of the product in Eq. (4.53) must be negative at its maximum if λ+(km) > 0 while λ−(km) < 0, and thus we must require


Clearly the conditions in Eq. (4.55) cannot be simultaneously satisfied if both M11 and M22 are negative, or if both diffusion coefficients have the same value. Let us suppose that M11 < 0 and M22 > 0, in which case the requirement is


The negative diagonal term thus corresponds to the faster diffusing component. Since negative terms are usually associated with inhibition, the above conclusion can be summarized somewhat imprecisely by the statement that finite wavelength instabilities arise from competition of long-range inhibition and short-range excitation. In fact, the additional requirement det M(0) = M11M22 − M12M21 > 0, implies that the off-diagonal terms M12 and M21 must have opposite signs. If M12 < 0, species 1 being both self and cross inhibitory, the instability occurs when the two components are out of phase; otherwise the two species will vary in phase. In the extreme limit of D2 = 0 and M22 < 0 instability sets in for all wavenumbers with k<sup>2</sup> > k−<sup>2=det M(0)/(M22D1).Ofcourse,inallcasestheinstabilitywavelength</sup> must be large enough so that the assumptions implicit in the continuum formulation of reaction-diffusion equations remain valid.

88

������������������ ������������������

������������������������������������������������

�����������

��������������������������������������������������������������������������������������������������

---

[← 4.5 Synchronization](01-4-5-synchronization.md) · [Up: contents](index.md)

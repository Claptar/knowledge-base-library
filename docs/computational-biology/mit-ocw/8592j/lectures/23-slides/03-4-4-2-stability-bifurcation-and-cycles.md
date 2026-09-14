---
title: 4.4.2 Stability, Bifurcation, and Cycles
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/23-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4.4.2 Stability, Bifurcation, and Cycles

**Source:** `lectures/23-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let us consider a bounded set of variables {xi} evolving in time as x˙ i = Fi({xj}). Fixed points are possible solutions to Fi({x<sup>∗</sup> j<sup>}) = 0, but they will correspond to potential outcomes</sup> (attractors) of the dynamics, only if all eigenvalues of the matrix


have negative real parts. (This is the condition for linear stability. For zero eigenvalues stability is determined by examining higher derivatives.) We are interested in physical problems where the functions Fi, and hence all elements of the matrix Mij, are real. The eigenvalues {λi} of a real-valued matrix are either real, or come in complex conjugate pairs u ± iv. In the biological context, the functions Fi may determine the evolution of protein concentrations, and could then include parameters that depend on external stimuli. As such parameters are changed, a fixed point (protein concentrations) may become unstable, causing the system to switch to another state. The initial fixed point becomes unstable at the point where the real part of an eigenvalue changes sign from negative to positive. If this happens for a real eigenvalue, we can focus on the dynamics along the corresponding eigendirection– a one dimensional parametrization is then sufficient to capture the change in behavior near such an instability. If the real part of a complex eigenvalue pair changes sign, we need to analyze the behavior in the corresponding two dimensional surface spanned by the eigenvectors.

79

Let us first consider a single eigenvalue λ(ǫ) that changes sign as a control parameter ǫ goes through zero. Indicating deviations along the corresponding eigendirection by y, at linear level we have y˙ = ǫy. The fixed point at y<sup>∗</sup> = 0 is stable for ǫ < 0, and unstable for ǫ > 0. Higher order terms in the expansion in y are then necessary to determine the fate of the fixed point. The simplest addition is a quadratic term, leading to


(The coefficient of the quadratic term can be set to 1 with proper scaling of y.) This model then admits a stable fixed point at y<sup>∗</sup> = ǫ for ǫ > 0. In this (transcritical) scenario, a stable and an unstable fixed point collide and exchange stability.


The quadratic term in Eq. (4.34) is generically present, unless forbidden by a symmetry. In particular, the symmetry y →−y is consistent only with odd powers of y in the equation for y˙, in which case Eq. (4.34) has to be replaced with


In such a pitchfork bifurcation a pair of stable fixed points appears at ±<sup>√</sup> ǫ for ǫ > 0, and the choice of one or the other is by spontaneous symmetry breaking.


The above changes in dynamic behavior as a parameter is varied are examples of bifurcations. If we do not insist upon starting with a stable fixed point as we have done so far,

80

other forms of bifurcation is possible. For example, if the sign of the cubic term in Eq. (4.34) is changed to positive, there is no longer a stable fixed point for ǫ < 0. The stable fixed points now all appear for ǫ > 0, colliding at ǫ = 0, with a single unstable fixed point for ǫ > 0. Yet another scenario by which a pair of stable fixed points disappear is provided by


where a pair of fixed points (one stable and one unstable) for ǫ > 0 collide and disappear for ǫ < 0.


If the real part of a complex eigenvalue pair, λ± = u(ǫ) ± iv, changes sign, we can focus on the two dimensional plane spanned by the corresponding eigenvectors. The trajectories on this plane now transition from inward spirals to outward spirals.


Of course bounded variables cannot spiral out forever, and the by Poinc´are–Bendixon theorem states that the bounded spiral must approach a closed curve around which it cycles. As an example, let us consider the pair of equations


81

These equations where in fact constructed to have a simple form in polar coordinates (r, θ) in terms of which x = r cos θ and y = r sin θ. It is then easily verified that Eqs. (4.35) are equivalent to


The trajectory now rotates at a uniform angular velocity ω, converging to the center for ǫ ≤ 0, and to a circle of radius r<sup>∗</sup> =<sup>√</sup> ǫ for ǫ > 0.


Note that a symmetric matrix Mij = Mji only has real eigenvalues. Complex eigenvalues, and hence periodic cycles can only occur for antisymmetric matrices. In the above example, the asymmetry is parametrized by ω which sets the angular velocity, but does not enter in the equation for r. Indeed, it is easy to check that for a two by two matrix, complex eigenvalues can only be obtained if the off-diagonal elements have opposite signs (as is the case in Eq. (4.35)). Indeed, in the biological context, a simple scheme for generating oscillations is to use an excitatory element (with positive interactions) in concert with an inhibitory component. (with negative couplings). Other schemes, with three elements each inhibiting the next in a cycle, as in the reprisselator<sup>2</sup> , also lead to oscillations by this mechanism.

> 2M. B. Elowitz and S. Leibler; Nature. 403, 335 (2000).

82

������������������ ������������������

������������������������������������������������

�����������

��������������������������������������������������������������������������������������������������

---

[← 4.4.1 Attractive fixed points](02-4-4-1-attractive-fixed-points.md) · [Up: contents](index.md)

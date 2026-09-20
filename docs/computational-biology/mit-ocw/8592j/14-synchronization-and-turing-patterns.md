---
title: "14. Synchronization and Turing Patterns"
course: "MIT 8.592J"
chapter: 14
source: "https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.592J](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 14. Synchronization and Turing Patterns

## What this covers

This chapter answers two separate questions, both about when a population of identical, locally
coupled units produces a large-scale pattern that none of them shows alone. First: when does a
population of independent, slightly mismatched oscillators lock into a common rhythm with no
external conductor — the Kuramoto model of synchronization? Second: when can a spatially uniform
chemical state that is perfectly stable on its own become unstable once diffusion is switched on,
producing a spontaneous spatial pattern — Turing's mechanism? It assumes a chemical-kinetics
oscillator is already in hand: the lecture opens by referring back to "how simple chemical
reactions can create an oscillator," a result this chapter does not reconstruct.

## Spontaneous synchronization: the Kuramoto model

An oscillator built from chemical kinetics has a phase set by its initial condition, and nothing
more — left alone, two such oscillators drift apart. But biology often needs many oscillators to
act as one: pacemaker cells in the heart, or the cells of an organism keeping circadian time. One
route to synchrony is an external driver — sunlight entraining a circadian clock. The Kuramoto
model addresses the other route: a collection of self-coupled oscillators synchronizing as a
collective, with no conductor.

Each oscillator carries a phase angle $\theta_i$, for $i = 1, \dots, N$. Uncoupled, each advances
at its own constant angular velocity, $\dot\theta_i = \omega_i$, with the $\omega_i$ drawn
independently from a distribution $p(\omega)$. In a biological setting $\omega$ might depend on a
cell's internal chemical concentrations; these vary from cell to cell, but for a given system the
spread is usually small, so $p(\omega)$ is narrowly peaked around some central frequency $\Omega$.
Passing to a frame rotating at $\Omega$ (the shift $\theta_i \to \theta_i - \Omega t$) sets
$\Omega = 0$ without loss of generality.

To get synchronization at all, the phases must be coupled. The simplest coupling that pushes
$\theta_i$ toward $\theta_j$ and respects the $2\pi$ periodicity of phase is $\sin(\theta_j -
\theta_i)$: it vanishes when the two are in phase, and its sign always points $\theta_i$ toward
$\theta_j$. Summing this over all pairs gives the coupled dynamics

$$\dot{\theta}_i = \omega_i + \sum_{j=1}^N W_{ij} \sin(\theta_j - \theta_i), \tag{4.37}$$

with $W_{ij}$ the coupling strength felt by $i$ from $j$. To make the problem tractable, Kuramoto's
simplification is to make every coupling equal, $W_{ij} = K/N$ (scaled by $N$ since each oscillator
now feels $N$ neighbours). Equation (4.37) then collapses into a mean-field form:

$$\begin{aligned}
\dot{\theta}_i &= \omega_i + K\, \Im \left[ e^{-i\theta_i} \left( \frac{\sum_{j=1}^N e^{i\theta_j}}{N} \right) \right] \\
&= \omega_i + K\, \Im \left[ m e^{i\phi} \right],
\end{aligned} \tag{4.38}$$

where $\Im$ denotes imaginary part, and $m e^{i\phi}$ is defined as the average of the phase points
$e^{i\theta_j}$ around the unit circle. The magnitude

$$m = \left| \frac{\sum_{j=1}^N e^{i\theta_j}}{N} \right| \tag{4.39}$$

is the **order parameter**: a single number measuring how synchronized the population is. If each
oscillator runs at its own rate, the phases sweep round the circle more or less independently and
eventually cover it uniformly, so the average — and hence $m$ — is zero. If instead a finite
fraction of the oscillators is locked to the central frequency, they sit still in the rotating
frame, and if they bunch together their contributions add up to something finite. Since the overall
orientation of the sum is a free choice, we may set $\phi = 0$, turning (4.38) into the
self-consistent equation each oscillator actually obeys:

$$\dot{\theta}_i = \omega_i - K m \sin \theta_i. \tag{4.40}$$

## Locked and drifting oscillators

Equation (4.40) has two qualitatively different kinds of solution, splitting the population into
two groups.

**Locked oscillators** sit at a fixed phase, $\dot\theta_i = 0$, which forces

$$\sin \theta_i = \frac{\omega_i}{K m}. \tag{4.41}$$

A solution exists only when $|\omega_i| < K m$: an oscillator can lock to the group only if its own
natural frequency is close enough to the central one, given how strong the coupling and how
synchronized the group already is.

**Drifting oscillators** are the rest, those with $|\omega_i| > K m$. For them (4.40) never
vanishes,

$$\dot{\theta}_i = \omega_i - K m \sin(\theta_i) \neq 0, \tag{4.42}$$

so their phase keeps slipping relative to the group, faster where $\sin\theta_i$ works against them
less and slower where it works against them more — but never actually stopping.

## The synchronization transition

Only the locked oscillators contribute to $m$ (the drifting ones average to zero over a cycle), and
because a locked oscillator's phase depends only on its own $\omega$ through (4.41), the sum over
locked oscillators can be replaced by an integral against $p(\omega)$:

$$m = \frac{1}{N} \sum_{\text{locked } j} e^{i\theta_j} = \int_{-Km}^{Km} d\omega \, p(\omega)\, e^{i\theta(\omega)}. \tag{4.43}$$

Changing variables to $\theta = \arcsin(\omega / K m)$ and expanding the (narrowly peaked)
distribution $p$ to second order around its centre turns this into

$$\begin{aligned}
m &= \int_{-\pi/2}^{\pi/2} d\theta \, (K m \cos\theta)\, p(K m \sin\theta)\, e^{i\theta} \\
&= \int_{-\pi/2}^{\pi/2} d\theta \, (K m \cos\theta) \left[ p(0) - \frac{(K m \sin\theta)^2}{2} |p''(0)| + \cdots \right] (\cos\theta + i\sin\theta) \\
&= K m \left[ \frac{\pi}{2} p(0) - \frac{K^2 m^2 \pi}{8} |p''(0)| + \cdots \right].
\end{aligned} \tag{4.44}$$

(Odd terms in $\sin\theta$ integrate to zero by symmetry, which is why only $p(0)$ and $p''(0)$
survive.) Equation (4.44) is a self-consistency condition on $m$: dividing through by $m$ shows that
$m=0$ always solves it, but a **non-zero** solution exists only when the coefficient of the linear
term exceeds one, i.e. only for coupling strength above a critical value

$$K > K_c = \frac{2}{\pi p(0)}. \tag{4.45}$$

Below $K_c$, no oscillators can lock to the centre and $m=0$ is the only solution: the population
is incoherent. Above $K_c$, the oscillators synchronize and rotate together, and expanding (4.44)
near threshold gives the way $m$ turns on,

$$m \propto \sqrt{K - K_c}, \tag{4.46}$$

a continuous transition — $m$ grows from zero with infinite initial slope, not with a jump.

**Worked example.** If $p(\omega)$ is Gaussian with width $\sigma$, (4.45)-(4.46) evaluate to

$$K_c = \sqrt{\frac{8}{\pi}}\, \sigma, \qquad m \simeq \sqrt{2\pi \left( \frac{K}{K_c} - 1 \right)}. \tag{4.47}$$

The wider the spread of natural frequencies, the larger the coupling needed to overcome it and pull
the population into sync — exactly what the mechanism argument predicts.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="Order parameter m stays at zero below the critical coupling Kc and grows continuously above it">
  <line x1="40" y1="170" x2="300" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="170" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="288" y="188" font-size="12" fill="currentColor">K</text>
  <text x="18" y="28" font-size="12" fill="currentColor">m</text>
  <line x1="140" y1="170" x2="140" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="122" y="188" font-size="12" fill="currentColor">K_c</text>
  <line x1="40" y1="170" x2="140" y2="170" stroke="currentColor" stroke-width="2"/>
  <path d="M140,170 C160,110 220,75 300,45" fill="none" stroke="currentColor" stroke-width="2"/>
  <circle cx="140" cy="170" r="3" fill="currentColor"/>
</svg>
<figcaption>The order parameter is pinned at zero below the critical coupling and rises with
infinite initial slope, as $\sqrt{K-K_c}$, above it — a continuous synchronization transition.</figcaption>
</figure>

## Turing patterns: instability from diffusion

The Kuramoto model coupled phases without any reference to space. Real cells, however, actively
compartmentalize molecules — genetic information sits in the nucleus and has to reach the rest of
the cell by diffusion of mRNA or protein — and chemical reactions coupled to diffusion can generate
spatial structure even with no physical barriers at all. Turing's question, motivated by how
biological patterns (body shapes, coat markings) arise, was whether a set of reacting and diffusing
morphogens could do this. The general reaction-diffusion system is

$$\frac{\partial C_i}{\partial t} = F_i(\{C_j\}) + D_i \nabla^2 C_i, \tag{4.48}$$

with $D_i$ the diffusion coefficient of species $i$ and $F_i$ the local (spatially unaware)
reaction kinetics.

The precise question is this: suppose the well-mixed system (no spatial variation, as if diffusion
were infinitely fast) has a stable fixed point $\{C_i^*\}$. Can that same fixed point become
**unstable** once spatial variation is permitted? Linearizing $C_i(\vec r, t) = C_i^* + c_i(\vec r,
t)$ gives

$$\frac{\partial c_i}{\partial t} = \sum_j M_{ij}\, c_j + D_i \nabla^2 c_i, \qquad M_{ij} = \left. \frac{\partial F_i}{\partial C_j} \right|_{C^*}, \tag{4.49}$$

and stability of the uniform state means every eigenvalue of $M_{ij}$ is negative. Passing to
Fourier modes,

$$c_i(\vec r, t) = \int d\vec k\, e^{i\vec k \cdot \vec r}\, \tilde c_i(\vec k, t), \tag{4.50}$$

turns (4.49) into an ordinary differential equation for each wavevector separately,

$$\frac{d \tilde c_i(\vec k, t)}{dt} = \sum_j \left( M_{ij} - \delta_{ij} D_i k^2 \right) \tilde c_j(\vec k, t), \tag{4.51}$$

so the question becomes: can the matrix $M_{ij}(k) = M_{ij} - \delta_{ij} D_i k^2$ have a positive
eigenvalue at some finite $\vec k$, even though $M_{ij}(0) = M_{ij}$ does not?

With a single species the answer is no: $\lambda(k) = \lambda(0) - D k^2$ only gets more negative as
$k$ grows, so diffusion can only stabilize further, never destabilize. A pattern-forming instability
needs at least two interacting species.

## Two species: the instability condition

For two species, write

$$M(k) = \begin{pmatrix} M_{11} - D_1 k^2 & M_{12} \\ M_{21} & M_{22} - D_2 k^2 \end{pmatrix}. \tag{4.52}$$

The product of its eigenvalues is the determinant,

$$\lambda_+(k)\,\lambda_-(k) = \det M(k) = \big(M_{11}M_{22} - M_{12}M_{21}\big) - \big(M_{11}D_2 + M_{22}D_1\big)k^2 + D_1 D_2 k^4, \tag{4.53}$$

a quadratic in $k^2$ with positive leading coefficient $D_1D_2$. At $k=0$ both eigenvalues are
negative by the assumed stability of the uniform state, so their product — the constant term of
(4.53) — is positive. As $k^2$ increases from zero, this upward parabola can either stay positive
everywhere (both eigenvalues stable at every wavelength) or dip negative over some range, which is
only possible if it crosses zero and $\lambda_+(k)$ actually becomes positive there.

Because the sum of the eigenvalues is also fixed by $M(k)$,

$$\lambda_+(k) + \lambda_-(k) = \operatorname{tr} M(k) = (M_{11}+M_{22}) - (D_1+D_2)k^2, \tag{4.54}$$

and this trace only decreases as $k$ grows, the moment $\lambda_+(k)$ turns positive, $\lambda_-(k)$
must swing even further negative to keep the sum falling — the two eigenvalues cannot destabilize
together. Since the constant and quartic terms of (4.53) are both positive, the parabola can dip
negative only if its linear-in-$k^2$ coefficient is large and positive, requiring

$$\big(M_{11}D_2 + M_{22}D_1\big) > 0, \qquad \text{while} \qquad (M_{11}+M_{22}) < 0 \tag{4.55}$$

(the second condition is just the $k=0$ stability requirement rewritten). When (4.55) holds, the
parabola (4.53) dips below zero between two roots $k_-$ and $k_+$, with its minimum at an
intermediate $k_m$ found from the vertex of the parabola:

$$k_+^2 + k_-^2 = 2k_m^2 = \frac{M_{11}D_2 + M_{22}D_1}{D_1 D_2}. \tag{4.56}$$

For the instability to actually occur — for the parabola's minimum value to be negative rather than
merely small — requires

$$\det M(0) - \frac{(M_{11}D_2 + M_{22}D_1)^2}{4D_1D_2} < 0 \quad \Longrightarrow \quad M_{11}D_2 + M_{22}D_1 > 2\sqrt{D_1D_2\det M(0)}. \tag{4.57}$$

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Three possible eigenvalue curves versus wavenumber: two that stay negative everywhere, and one that rises above zero over a band of wavenumbers">
  <line x1="40" y1="190" x2="320" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <text x="300" y="207" font-size="12" fill="currentColor">k</text>
  <line x1="40" y1="110" x2="320" y2="110" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="20" y="114" font-size="12" fill="currentColor">0</text>
  <text x="16" y="30" font-size="12" fill="currentColor">λ+</text>
  <path d="M150,110 Q180,58 210,110 Z" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <path d="M70,150 C150,150 200,150 300,175" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="55" y="145" font-size="12" fill="currentColor">1</text>
  <path d="M70,150 Q180,110 300,170" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="185" y="102" font-size="12" fill="currentColor">2</text>
  <path d="M70,150 Q180,58 300,170" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="185" y="48" font-size="12" fill="currentColor">3</text>
  <text x="135" y="207" font-size="11" fill="currentColor">k_-</text>
  <text x="173" y="207" font-size="11" fill="currentColor">k_m</text>
  <text x="203" y="207" font-size="11" fill="currentColor">k_+</text>
</svg>
<figcaption>Curves 1 and 2 leave the uniform state stable at every wavelength (2 merely touches
zero); curve 3 crosses zero at $k_-$ and $k_+$, so wavenumbers in that band grow — a Turing
instability with a preferred wavelength near $k_m$.</figcaption>
</figure>

## Long-range inhibition, short-range excitation

Condition (4.55) cannot be met if $M_{11}$ and $M_{22}$ are both negative, nor if $D_1 = D_2$: some
structural asymmetry between the two species is required. Suppose $M_{11} < 0$ and $M_{22} > 0$ —
species 1 is self-damping, species 2 is self-amplifying — then (4.55) and (4.57) reduce to

$$|M_{11}| \frac{D_2}{D_1} < M_{22} < |M_{11}|, \qquad \Longrightarrow \qquad D_1 > D_2. \tag{4.58}$$

The species with the negative (inhibitory) diagonal term must be the **faster-diffusing** one.
Reading $M_{11}<0$ as self-inhibition and $M_{22}>0$ as self-activation, the conclusion is usually
summarized, loosely, as: a finite-wavelength instability comes from **long-range inhibition
competing with short-range excitation** — a locally self-amplifying species that would blow up on
its own is kept in check everywhere except in patches, because a fast-diffusing inhibitor smooths
itself out and suppresses the activator everywhere but where the activator momentarily gets ahead.

The stability requirement $\det M(0) = M_{11}M_{22} - M_{12}M_{21} > 0$ further forces the
off-diagonal terms $M_{12}$ and $M_{21}$ to have opposite signs. Their sign sets the phase
relationship of the resulting pattern: if $M_{12} < 0$ (species 1 is inhibited by species 2 as well
as by itself), the unstable pattern has the two species spatially out of phase; otherwise they vary
in phase. In the extreme case $D_2 = 0$ with $M_{22} < 0$, the instability sets in for every
wavenumber above $k_-^2 = \det M(0) / (M_{22} D_1)$, with no upper cutoff. In every case, though,
the unstable wavelength must stay long enough that the continuum reaction-diffusion description
(4.48) — which assumes concentrations vary smoothly over many molecules — remains a valid
approximation in the first place.

## Sources

Both sections are from the slide deck for lecture 24 of MIT OCW 8.592J/HST.452J *Statistical
Physics in Biology* (Spring 2011, CC BY-NC-SA 4.0): `01-4-5-synchronization.md` (§4.5, the Kuramoto
model, eqs. 4.37-4.47) and `02-4-6-turing-patterns.md` (§4.6, Turing patterns, eqs. 4.48-4.58). No
transcript, lecture notes or exercises were supplied for this lecture. Both slide files carry a
"reconstructed by a model" banner: the source PDF has no text layer, so a model read the pages and
the prose is a paraphrase with the equations flagged as unverified. This chapter transcribes those
equations as given, correcting two evident transcription slips against the internal logic of the
argument — the missing $\tilde c_j(\vec k, t)$ factor on the right of eq. (4.51), and a stray
lowercase $k$ that should read $K$ in eq. (4.44) — but has no transcript or independent source to
check the rest against. The lecture opens by referring to an earlier construction of a chemical
oscillator ("we have established how simple chemical reactions can create an oscillator"), which is
prior material not included among the inputs for this chapter.

---

[← 13. Fixed Points and Hopfield Networks](13-fixed-points-and-hopfield-networks.md) · [Contents](index.md) · [15. Amino Acid Contact Energies →](15-amino-acid-contact-energies.md)

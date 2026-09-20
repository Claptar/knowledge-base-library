---
title: "8. Biological Oscillators"
course: "MIT 8.591J 2004"
chapter: 8
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 8. Biological Oscillators

## What this covers

This chapter asks how a feedback loop between chemical or genetic species can settle into
*sustained periodic behaviour* — a limit cycle — instead of relaxing to a fixed steady state, and
how to locate, inside a model's parameters, the exact boundary where that switch happens. It works
two examples through in full: a generic two-variable feedback oscillator, and Elowitz and Leibler's
repressilator, a synthetic three-gene oscillator built from three repressor proteins wired in a
ring. It assumes the linear-stability toolkit from the earlier lecture on fixed points — nullclines,
the Jacobian, and reading stability off its trace and determinant, or off its eigenvalues — which
the outline calls back to as "section V" and does not re-derive here.

## Two ways for a fixed point to lose stability

For a two-variable system, the eigenvalues of the Jacobian at a fixed point are

$$
\lambda_{1,2} = \frac{\tau \pm \sqrt{\tau^2 - 4\Delta}}{2},
$$

where $\tau$ is the trace and $\Delta$ the determinant. If $\Delta < 0$ the eigenvalues are real
with opposite sign — a saddle, never oscillatory. If $\Delta > 0$ and $\tau^2 < 4\Delta$ the
eigenvalues are a complex-conjugate pair, and the fixed point is a spiral: stable if $\tau < 0$,
unstable if $\tau > 0$. The transition that matters here is the second one: $\Delta$ stays positive
while $\tau$ crosses zero, so a complex pair of eigenvalues crosses the imaginary axis together.
Locally the spiral changes from decaying to growing; because trajectories in these models stay
bounded, what a growing spiral is confined into is a closed orbit around it — a stable limit cycle.
(This kind of transition has a name, a Hopf bifurcation, though the lecture works it out directly
from the sign of $\tau$ each time rather than naming it.) Both examples below turn on exactly this:
a determinant that stays positive, and a trace — or, in the three-variable case, a pair of complex
eigenvalues — that changes sign.

## The two-species feedback oscillator

The system introduced in the previous lecture, where phase-plane pictures already showed
oscillations for some parameter values, is

$$
\dot{x} = -x + ay + x^2 y, \qquad \dot{y} = b - ay - x^2 y. \tag{VII.1}
$$

### Nullclines and the one fixed point

Setting $\dot x = 0$ gives $y(a+x^2) = x$, and setting $\dot y = 0$ gives $y(a+x^2) = b$, so the two
nullclines are

$$
y = \frac{x}{a+x^2}, \qquad y = \frac{b}{a+x^2}. \tag{VII.2}
$$

They share the same denominator, so where they meet, $x = b$ regardless of the value of that
denominator — the two curves cross exactly once. The fixed point is therefore

$$
x^* = b, \qquad y^* = \frac{b}{a+b^2}. \tag{VII.3}
$$

### Trace, determinant, and where oscillation turns on

Differentiating [VII.1] and evaluating at $(x^*,y^*)$ gives the Jacobian

$$
A = \begin{bmatrix} -1+2x^*y^* & a+(x^*)^2 \\ -2x^*y^* & -(a+(x^*)^2) \end{bmatrix}. \tag{VII.4}
$$

Its determinant collapses nicely — the $x^*y^*$ terms cancel between the two off-diagonal
products — leaving $\Delta = a+(x^*)^2 = a+b^2$, always positive for $a>0$. So this system can never
have a saddle: the only way the fixed point can destabilize is through the trace, and by the
argument above, through a Hopf bifurcation. Substituting $x^*=b$ and $y^*=b/(a+b^2)$ into the trace
and putting it over the common denominator $a+b^2$ gives

$$
\Delta = a+b^2 > 0, \qquad \tau = -\frac{b^4+(2a-1)b^2+(a+a^2)}{a+b^2}. \tag{VII.5}
$$

The fixed point is a stable spiral for $\tau<0$ and an unstable one — hence a limit cycle — for
$\tau>0$. Because the denominator is always positive, the sign of $\tau$ is the opposite of the
sign of the numerator.

### Why the boundary folds back on itself

Write $u = b^2$. The numerator of [VII.5] is a quadratic in $u$,

$$
N(u) = u^2 + (2a-1)u + (a+a^2),
$$

an upward-opening parabola, so $N(u)<0$ — the oscillatory case — exactly for $u$ *between* its two
roots, when those roots are real and positive. The discriminant of $N$ is

$$
(2a-1)^2 - 4(a+a^2) = 1 - 8a,
$$

which is non-negative only for $a \le \tfrac{1}{8}$. So for $a>1/8$ the fixed point is stable for
*every* value of $b$: there is no oscillation available at all. For $a \le 1/8$, the two roots

$$
u_\pm = \frac{(1-2a) \pm \sqrt{1-8a}}{2}
$$

bound a finite window $b \in (\sqrt{u_-},\sqrt{u_+})$ in which the system oscillates; outside that
window, for the same $a$, it sits at a stable fixed point. That is exactly the fold in the boundary
curve the outline plots as Figure 10/11: two branches of the same curve, meeting at a cusp where
the discriminant vanishes, at $a=1/8$, $b = \sqrt{3/8} \approx 0.61$.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Oscillatory and stable regions of the two-species model in a-b parameter space">
  <polygon points="50,20 220,22 263,62 220,106 186,122 152,137 118,151 84,171 50,200" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <line x1="50" y1="200" x2="300" y2="200" stroke="currentColor" stroke-width="1.5"/>
  <line x1="50" y1="200" x2="50" y2="15" stroke="currentColor" stroke-width="1.5"/>
  <path d="M50,200 L84,171 L118,151 L152,137 L186,122 L220,106 L254,81 L263,62 L254,44 L237,31 L220,22" fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="263" y1="62" x2="263" y2="200" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="263" y="212" text-anchor="middle" font-size="11" fill="currentColor">a = 1/8</text>
  <text x="300" y="215" text-anchor="middle" font-size="12" fill="currentColor">a</text>
  <text x="35" y="22" text-anchor="middle" font-size="12" fill="currentColor">b</text>
  <text x="110" y="60" font-size="12" fill="currentColor">oscillations</text>
  <text x="110" y="75" font-size="12" fill="currentColor">(stable limit cycle)</text>
  <text x="178" y="150" font-size="12" fill="currentColor">no oscillations</text>
  <text x="178" y="165" font-size="12" fill="currentColor">(stable fixed point)</text>
</svg>
<figcaption>The trace-zero boundary in $(a,b)$-space, redrawn from the outline's Figure 10/11. The
curve is $\tau=0$; treated as a quadratic in $b^2$, its two branches meet at the cusp $a=1/8$, the
rightmost point at which oscillation is possible for any $b$.</figcaption>
</figure>

### Watching the limit cycle in MATLAB

The outline's own check is numerical. `cyclefunc.m` returns the right-hand side of [VII.1] as a
function of the state, and `limitcycle.m` integrates it with `ode23` and plots the trajectory in
the $(x,y)$ plane:

```matlab
% filename: cyclefunc.m
function dydt = f(t,y,flag,a,b)
dydt = [-y(1)+a*y(2)+y(1)*y(1)*y(2);
        b-a*y(2)-y(1)*y(1)*y(2)];
plot(y(1),y(2),'.');
drawnow;
hold on;
axis([0 2 0 2]);
```

```matlab
% filename: limitcycle.m
close; clear;
a=0.1; b=0.5;
options=[];
[t y]=ode23('cyclefunc',[0 50],[0.6 1.4],options,a,b);
plot(y(:,1),y(:,2));
```

The choice $a=0.1$ is not arbitrary: by the window computed above, at $a=0.1$ oscillation occurs for
$b$ between $\sqrt{u_-}\approx 0.42$ and $\sqrt{u_+}\approx 0.79$, and $b=0.5$ sits inside it. Starting
away from the fixed point at $(0.6, 1.4)$, the trajectory should spiral outward and settle onto a
closed loop rather than a point — the limit cycle the phase-plane picture promised.

## The repressilator: a synthetic three-gene oscillator

Elowitz and Leibler built a genetic oscillator "from scratch" in *E. coli* out of three repressor
genes, each repressing the next around a ring:

M. B. Elowitz and S. Leibler, "A synthetic oscillatory network of transcriptional regulators,"
*Nature* **403**, 335–338 (2000).

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="The repressilator's three genes arranged in a repression ring">
  <defs>
    <marker id="repress" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="9" markerHeight="9" orient="auto">
      <line x1="8" y1="0" x2="8" y2="10" stroke="currentColor" stroke-width="1.6"/>
    </marker>
  </defs>
  <line x1="146" y1="50" x2="74" y2="151" stroke="currentColor" stroke-width="1.5" marker-end="url(#repress)"/>
  <line x1="84" y1="170" x2="236" y2="170" stroke="currentColor" stroke-width="1.5" marker-end="url(#repress)"/>
  <line x1="246" y1="151" x2="174" y2="50" stroke="currentColor" stroke-width="1.5" marker-end="url(#repress)"/>
  <circle cx="160" cy="30" r="24" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="160" y="34" text-anchor="middle" font-size="12" fill="currentColor">cI</text>
  <circle cx="60" cy="170" r="24" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="60" y="174" text-anchor="middle" font-size="12" fill="currentColor">lacI</text>
  <circle cx="260" cy="170" r="24" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="260" y="174" text-anchor="middle" font-size="12" fill="currentColor">tetR</text>
</svg>
<figcaption>Each gene represses the next around the ring: cI represses lacI, lacI represses tetR,
tetR represses cI. This cyclic wiring is what makes the Jacobian below a circulant matrix.</figcaption>
</figure>

### From two reactions per gene to one

Writing $m_i$ for mRNA and $p_i$ for protein concentration of gene $i \in \{\text{lacI,tetR,cI}\}$,
repressed by protein $j \in \{\text{cI,lacI,tetR}\}$ respectively, the reactions give (see the
outline's boxed derivation, not reproduced here)

$$
\frac{dm_i}{dt} = -m_i + \frac{\alpha}{1+p_j^n} + \alpha_o, \qquad
\frac{dp_i}{dt} = -\beta(p_i - m_i). \tag{VII.6}
$$

If the mRNA is assumed to reach its steady state fast compared with the protein, it tracks
$m_i \to \alpha/(1+p_j^n)+\alpha_o$ instantly; substituting that into the protein equation, and
measuring time in units of the protein decay rate, collapses the two-step reaction into one
equation per gene:

$$
\frac{dp_1}{dt} = -p_1 + \frac{\alpha}{1+p_3^n} + \alpha_o, \quad
\frac{dp_2}{dt} = -p_2 + \frac{\alpha}{1+p_1^n} + \alpha_o, \quad
\frac{dp_3}{dt} = -p_3 + \frac{\alpha}{1+p_2^n} + \alpha_o. \tag{VII.7}
$$

### The symmetric steady state

All three genes are given the same basal rate $\alpha_o$, maximum rate $\alpha$, and Hill
coefficient $n$, so the steady state is symmetric,

$$
p \equiv p_1 = p_2 = p_3, \tag{VII.8}
$$

and satisfies

$$
p = \frac{\alpha}{1+p^n} + \alpha_o. \tag{VII.9}
$$

### A circulant Jacobian

Linearizing [VII.7] at the symmetric fixed point, $\dot p_i$ depends only on $p_i$ itself (rate
$-1$) and on the one protein that represses it, through

$$
X \equiv -\frac{\alpha n p^{n-1}}{(1+p^n)^2}, \tag{VII.11}
$$

which is negative because $\alpha,n,p>0$. Because the wiring is a ring, each row of the Jacobian is
the previous row shifted by one — a circulant matrix:

$$
A = \begin{bmatrix} -1 & 0 & X \\ X & -1 & 0 \\ 0 & X & -1 \end{bmatrix}. \tag{VII.10}
$$

### Eigenvalues from the cube roots of unity

The eigenvalues solve $\det(A-\lambda I) = 0$. Writing $d = -1-\lambda$, the determinant of this
particular circulant matrix is $d^3 + X^3$, so

$$
-(1+\lambda)^3 + X^3 = 0 \quad \Longleftrightarrow \quad d^3 = -X^3. \tag{VII.13}
$$

The three cube roots of $-X^3$ are $-X$ times the three cube roots of unity, $1, e^{2\pi i/3},
e^{-2\pi i/3}$, giving $d \in \{-X,\ Xe^{2\pi i/3},\ Xe^{-2\pi i/3}\}$ and, since $\lambda=-1-d$,

$$
\lambda_1 = X-1, \qquad
\lambda_{2,3} = -1 - \tfrac{1}{2}X \pm i\tfrac{\sqrt3}{2}X. \tag{VII.14}
$$

The ring's symmetry is doing the work here: it is what turns a $3\times3$ eigenvalue problem into a
cube root, and it is why exactly one eigenvalue is guaranteed real.

### The stability condition, and what it says biologically

$\lambda_1 = X-1$ is always negative, since $X<0$: that eigenvalue never destabilizes the fixed
point. Everything rides on the complex pair. Its real part is $-1-\tfrac12 X$, negative precisely
when $X>-2$; combined with the real eigenvalue's requirement $X<1$ (automatic, since $X<0$), the
fixed point is stable for

$$
-2 < X < 1. \tag{VII.15}
$$

Since $X$ is negative by [VII.11], the binding constraint is $X>-2$, i.e.

$$
\frac{\alpha n p^{n-1}}{(1+p^n)^2} < 2. \tag{VII.16}
$$

Read biologically: $X$ measures the local slope of the repression curve at the steady state —
steeper, more cooperative repression (larger $n$, or $\alpha$ tuned so $p$ sits on the steep part of
the Hill function) makes $|X|$ larger. Below the threshold in [VII.16] the ring sits at a stable
fixed point; cross it, and the complex pair of eigenvalues crosses the imaginary axis together
— the same Hopf mechanism as the two-species example — and the three repressor concentrations
start to oscillate, chasing each other around the ring out of phase.

## Sources

- MIT OCW 8.591J (Systems Biology, Fall 2004), lecture outline "VII Biological Oscillators"
  (`lecture-outlines/10-outline.md`, equations VII.1–VII.16 and the two MATLAB listings
  `cyclefunc.m`/`limitcycle.m`). No transcript, written notes, or problem set accompanied this
  outline in the material supplied.
- The outline itself points to two things it does not contain: the phase-plane analysis of [VII.1]
  from the previous lecture ("L9_notes.pdf"), and the general 2×2 Jacobian/trace/determinant
  formulas it reuses as "[V.4] and [V.5]" from an earlier lecture on linear stability ("section V").
  Neither was supplied here.
- The chemical-reaction derivation of the mRNA/protein equations [VII.6] is referred to in the
  outline as "(see Box)" — a boxed aside on the original slide that was not reconstructed in the
  supplied conversion.
- M. B. Elowitz and S. Leibler, "A synthetic oscillatory network of transcriptional regulators,"
  *Nature* **403**, 335–338 (2000) — cited by the outline for the repressilator construct; the paper
  itself was not supplied.
- The outline's page 2 contains a second extracted figure (a short declining curve with no visible
  caption or axis labels in the conversion) that could not be identified with confidence and is not
  used here.
- The conversion note on the source file flags every equation as unverified (the original PDF had
  no text layer and was read by a model). The algebra in this chapter — nullclines, the Jacobian,
  the trace/determinant, the cube-root eigenvalues, and the discriminant argument for the fold in
  Figure 10/11 — was checked step by step for internal consistency against the outline's stated
  results, but not against the original scanned page.

---

[← 7. Perfect Adaptation by Model Reduction](07-perfect-adaptation-by-model-reduction.md) · [Contents](index.md) · [9. Genetic Toggle Switch and Oscillator →](09-genetic-toggle-switch-and-oscillator.md)

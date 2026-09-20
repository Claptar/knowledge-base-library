---
title: "19. Linear Stability of Fixed Points"
course: "MIT 8.591J 2004"
chapter: 19
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 19. Linear Stability of Fixed Points

## What this covers

How to decide whether a fixed point of a pair of coupled first-order ODEs is stable, without
solving the (generally nonlinear) equations. It assumes the reader knows what a fixed point of an
ODE system is, and how to compute a determinant and eigenvalues of a $2\times 2$ matrix.

## The system and its fixed points

Take two variables coupled through

$$
\begin{aligned}
\dot{x} &= f(x,y) \\
\dot{y} &= g(x,y)
\end{aligned}
$$

A fixed point $(x_o, y_o)$ is a point where both rates vanish simultaneously:

$$
\dot{x} = 0 \rightarrow f(x_o, y_o) = 0, \qquad \dot{y} = 0 \rightarrow g(x_o, y_o) = 0
$$

These two conditions are the system's **nullclines**: the curve $f = 0$ and the curve $g = 0$.
Their intersections are the fixed points. Whether the system settles at such a point, or is
pushed away from it, is a question about the *local* behaviour near $(x_o, y_o)$ — which is why
the next step is to linearize.

## Linearizing near a fixed point

Introduce the deviation from the fixed point,

$$
\tilde{x} \equiv x - x_o, \qquad \tilde{y} \equiv y - y_o,
$$

and expand $f$ and $g$ to first order in a Taylor series about $(x_o, y_o)$. Because
$f(x_o,y_o) = g(x_o,y_o) = 0$, only the linear terms survive:

$$
\begin{aligned}
\dot{\tilde{x}} &\approx \left.\frac{\partial f}{\partial x}\right|_{(x_o,y_o)} \tilde{x}
  + \left.\frac{\partial f}{\partial y}\right|_{(x_o,y_o)} \tilde{y} \equiv a\tilde{x} + b\tilde{y} \\
\dot{\tilde{y}} &\approx \left.\frac{\partial g}{\partial x}\right|_{(x_o,y_o)} \tilde{x}
  + \left.\frac{\partial g}{\partial y}\right|_{(x_o,y_o)} \tilde{y} \equiv c\tilde{x} + d\tilde{y}
\end{aligned}
$$

so that near the fixed point the original nonlinear system behaves like a linear one,

$$
\dot{\vec{X}} = A\vec{X}, \qquad
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}, \qquad
\vec{X} = \begin{bmatrix} \tilde{x} \\ \tilde{y} \end{bmatrix}.
$$

$A$ is the Jacobian of $(f,g)$ evaluated at the fixed point. All of the local dynamics is
carried by two numbers built from it, the trace and the determinant:

$$
\tau = \operatorname{tr}(A) = a + d, \qquad \Delta = \det(A) = ad - bc.
$$

## Eigenvalues of the Jacobian

Look for solutions of the linear system of the form $\dot{\vec{v}} = \lambda\vec{v} = A\vec{v}$:
a direction $\vec{v}$ (the eigenvector) along which the flow is purely a rescaling by $\lambda$
(the eigenvalue). Such $\lambda$ exist only where

$$
\det \begin{bmatrix} a - \lambda & b \\ c & d - \lambda \end{bmatrix} = 0,
$$

the characteristic equation. Expanding it gives a quadratic in $\lambda$ whose roots are

$$
\lambda_{1} = \frac{\tau + \sqrt{\tau^2 - 4\Delta}}{2}, \qquad
\lambda_{2} = \frac{\tau - \sqrt{\tau^2 - 4\Delta}}{2},
$$

equivalently

$$
\Delta = \lambda_1 \lambda_2, \qquad \tau = \lambda_1 + \lambda_2.
$$

So the trace and determinant of the Jacobian are exactly the sum and product of its two
eigenvalues — everything about the local behaviour near the fixed point is encoded in $\tau$ and
$\Delta$ alone, without ever solving for $\lambda_1,\lambda_2$ explicitly.

## The stability condition

A perturbation $\tilde{x},\tilde{y}$ decays back to the fixed point along an eigendirection only
if its eigenvalue is negative. For the fixed point to be stable, **both** eigenvalues must be
negative. Since $\Delta$ is their product and $\tau$ their sum, two negative numbers require

$$
\Delta > 0, \qquad \tau < 0.
$$

That is the stability criterion for a fixed point of a two-variable system, stated purely in
terms of the trace and determinant of the Jacobian — no need to extract the eigenvalues
themselves.

The source material breaks off immediately after stating this criterion ("Now let us use..."),
before going on to whatever example or refinement (e.g. distinguishing node from spiral by the
sign of $\tau^2 - 4\Delta$) it was about to introduce. That refinement is not reproduced here
because it is not in the supplied material.

## Sources

- Transcript: `recordings/l6-syllabus-transcript.md` (MIT OCW 8.591J, 2004), titled "V Stability
  analysis" — covers nullclines through the linearization, Jacobian trace/determinant, eigenvalue
  derivation, and the $\Delta > 0,\ \tau < 0$ stability condition. This is the entire supplied
  transcript; it is short and ends mid-sentence, and no slides, written notes, or exercises were
  supplied alongside it. The file itself is flagged as a model reconstruction of a PDF with no
  text layer ("fidelity: reconstructed"), so every equation above should be treated as a pointer
  back to the original lecture material rather than as independently verified.

---

[← 18. Genetic Switch in Phage Lambda](18-genetic-switch-in-phage-lambda.md) · [Contents](index.md) · [20. Master Equation for Gene Expression →](20-master-equation-for-gene-expression.md)

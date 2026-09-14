---
title: 1. Notation
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 1. Notation

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

We'll make use of the first derivative (the gradient) and second
derivative (the Hessian) of functions. We'll generally denote univariate
and multivariate functions (without distinguishing between them) as
$f(x)$ with $x=(x_{1},\ldots,x_{p})$. The (column) vector of first
partial derivatives (the gradient) is
$f^{\prime}(x)=\nabla f(x)=(\frac{\partial f}{\partial x_{1}},\ldots,\frac{\partial f}{\partial x_{p}})^{\top}$
and the matrix of second partial derivatives (the Hessian) is
$$f^{\prime\prime}(x)=\nabla^{2}f(x)=H_{f}(x)=\left(\begin{array}{cccc}
\frac{\partial^{2}f}{\partial x_{1}^{2}} & \frac{\partial^{2}f}{\partial x_{1}\partial x_{2}} & \cdots & \frac{\partial^{2}f}{\partial x_{1}\partial x_{p}}\\
\frac{\partial^{2}f}{\partial x_{1}\partial x_{2}} & \frac{\partial^{2}f}{\partial x_{2}^{2}} & \cdots & \frac{\partial^{2}f}{\partial x_{2}\partial x_{p}}\\
\vdots & \vdots & \ddots\\
\frac{\partial^{2}f}{\partial x_{1}\partial x_{p}} & \frac{\partial^{2}f}{\partial x_{2}\partial x_{p}} & \cdots & \frac{\partial^{2}f}{\partial x_{p}^{2}}
\end{array}\right).$$ In considering iterative algorithms, I'll use
$x_{0},\,x_{1},\ldots,x_{t},\,x_{t+1}$ to indicate the sequence of
values as we search for the optimum, denoted $x^{*}$. $x_{0}$ is the
starting point, which we must choose (often carefully). If it's unclear
at any point whether I mean a value of $x$ in the sequence or a
sub-element of the $x$ vector, let me know, but hopefully it will be
clear from context most of the time.

I'll try to use $x$ (or if we're talking explicitly about a likelihood,
$\theta$) to indicate the argument with respect to which we're
optimizing and $Y$ to indicate data involved in a likelihood. I'll try
to use $z$ to indicate covariates/regressors so there's no confusion
with $x$.

---

[← Overview](01-overview.md) · [Up: contents](index.md) · [2. Overview →](03-2-overview.md)

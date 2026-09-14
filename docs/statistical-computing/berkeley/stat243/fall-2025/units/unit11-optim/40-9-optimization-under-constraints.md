---
title: 9. Optimization under constraints
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 9. Optimization under constraints

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Constrained optimization is harder than unconstrained, and inequality
constraints harder to deal with than equality constraints.

Constrained optimization can sometimes be avoided by reparameterizing. Some examples include:
- working on the log scale (e.g., to optimize w.r.t. a variance component or other non-negative parameter)
- using the logit transformation to optimize with respect to a parameter on $(0,1)$ (or more generally some other bounded interval, after shifting and scaling to $(0,1)$.

Optimization under constraints often goes under the name of
'programming', with different types of programming for different types
of objective functions combined with different types of constraints.

## Convex optimization (convex programming)

Convex programming minimizes $f(x)$ s.t. $h_{j}(x)\leq0,\,j=1,\ldots,m$
and $a_{i}^{\top}x=b_{i},\,i=1,\ldots,q$, where both $f$ and the
constraint functions are convex. Note that this includes more general
equality constraints, as we can write $g(x)=b$ as two inequalities
$g(x)\leq b$ and $g(x)\geq b$. It also includes $h_{j}(x)\geq b_{j}$ by
taking $-h_{j}(x)$. Note that we can always have $h_{j}(x)\leq b_{j}$
and convert to the above form by subtracting $b_{j}$ from each side
(note that this preserves convexity). A vector $x$ is said to be
feasible, or in the feasible set, if all the constraints are satisfied
for $x$.

There are good algorithms for convex programming, and it's possible to
find solutions when we have hundreds or thousands of variables and
constraints. It is often difficult to recognize if one has a convex
program (i.e., if $f$ and the constraint functions are convex), but
there are many tricks to transform a problem into a convex program and
many problems can be solved through convex programming. So the basic
challenge is in recognizing or transforming a problem to one of convex
optimization; once you've done that, you can rely on existing methods to
find the solution.

Linear programming, quadratic programming, second order cone programming
and semidefinite programming are all special cases of convex
programming. In general, these types of optimization are progressively
more computationally complex.

First let's see some of the special cases and then discuss the more
general problem.

## Linear programming: Linear system, linear constraints

Linear programming seeks to minimize $$f(x)=c^{\top}x$$ subject to a
system of $m$ inequality constraints, $a_{i}^{\top}x\leq b_{i}$ for
$i=1,\ldots,m$, where $A$ is of full row rank. This can also be written
in terms of generalized inequality notation, $Ax\preceq b$. There are
standard algorithms for solving linear programs, including the simplex
method and interior point methods.

Note that each equation in the set of equations $Ax=b$ defines a
hyperplane, so each inequality in $Ax\preceq b$ defines a half-space.
Minimizing a linear function (presuming that the minimum exists) must
mean that we push in the correct direction towards the boundaries formed
by the hyperplanes, with the solution occuring at a corner (vertex) of
the solid formed by the hyperplanes. The simplex algorithm starts with a
feasible solution at a corner and moves along edges in directions that
improve the objective function.

## General system, equality constraints

### Linear equality constraints

Suppose we have an objective function $f(x)$ and we have $q$ equality
constraints, $Ax=b$. We can manipulate this into an unconstrained
problem. The null space of $A$ is the set of $\delta$ s.t. $A\delta=0$.
So if we start with a candidate $x_{c}$ s.t. $Ax_{c}=b$ (e.g., by using
the pseudo inverse, $A^{+}b$), we can form all other candidates (a
candidate is an $x$ s.t. $Ax=b$) as $x=x_{c}+\delta=x_{c}+Bz$ where $B$
is a set of column basis functions for the null space of $A$ and
$z\in\Re^{p-q}$. Consider $h(z)=f(x_{c}+Bz)$ and note that $h$ is a
function of $p-q$ rather than $p$ inputs. Namely, we are working in a
reduced dimension space with no constraints. If we assume
differentiability of $f$, we can express
$\nabla h(z)=B^{\top}\nabla f(x_{c}+Bz)$ and
$H_{h}(z)=B^{\top}H_{f}(x_{c}+Bz)B$. Then we can use unconstrained
methods to find the point at which $\nabla h(z)=0$.

How do we find $B$? One option is to use the $p-m$ columns of $V$ in the
SVD of $A$ that correspond to singular values that are zero. A second
option is to take the QR decomposition of $A^{\top}$. Then $B$ is the
columns of $Q_{2}$, where these are the columns of the (non-skinny) Q
matrix corresponding to the rows of $R$ that are zero.

### Nonlinear equality constraints

For more general (nonlinear) equality constraints, $g_{i}(x)=b_{i}$,
$i=1,\ldots,q$, we can use the Lagrange multiplier approach to define a
new objective function, $$L(x,\lambda)=f(x)+\lambda^{\top}(g(x)-b)$$ for
which, if we set the derivative (with respect to both $x$ and the
Lagrange multiplier vector, $\lambda$) equal to zero, we have a critical
point of the original function and we respect the constraints.

An example occurs with quadratic programming, under the simplification
of affine equality constraints (quadratic programming in general
optimizes a quadratic function under affine inequality constraints -
i.e., constraints of the form $Ax-b\preceq0$). For example we might
solve a least squares problem subject to linear equality constraints,
$f(x)=\frac{1}{2}x^{\top}Qx+m^{\top}x+c$ s.t. $Ax=b$, where $Q$ is
positive semi-definite. The Lagrange multiplier approach gives the
objective function
$$L(x,\lambda)=\frac{1}{2}x^{\top}Qx+m^{\top}x+c+\lambda^{\top}(Ax-b)$$
and differentiating gives the equations $$\begin{aligned}
\frac{\partial L(x,\lambda)}{\partial x} & =m+Qx+A^{\top}\lambda  =  0\\
\frac{\partial L(x,\lambda)}{\partial\lambda} & =Ax  =  b,\end{aligned}$$
which gives us a system of equations that leads to the solution $$\left(\begin{array}{c} x \\ \lambda \end{array} \right) =
\left( \begin{array}{cc} Q & A^{\top} \\ A & 0 \end{array}\right)^{-1}
\left(\begin{array}{c} -m \\ b \end{array}\right).\label{eq:quadProg}$$

Using known results for
inverses of matrices split into blocks, one gets that
$x^{*}=-Q^{-1}m+Q^{-1}A^{\top}(AQ^{-1}A^{\top})^{-1}(AQ^{-1}m+b)$. This
can be readily coded up using strategies from Unit 10.

## The dual problem (optional)

Sometimes a reformulation of the problem eases the optimization. There
are different kinds of dual problems, but we'll just deal with the
Lagrangian dual. Let $f(x)$ be the function we want to minimize, under
constraints $g_{i}(x)=0;\,i=1,\ldots,q$ and
$h_{j}(x)\leq0;\,j=1,\ldots,m$. Here I've explicitly written out the
equality constraints to follow the notation in Lange. Consider the
Langrangian,
$$L(x,\lambda,\mu)=f(x)+\sum_{i}\lambda_{i}g_{i}(x)+\sum_{j}\mu_{j}h_{j}(x).$$

Solving that can be shown to be equivalent to this optimization:
$$\inf_{x}\sup_{\lambda,\mu:\mu_{j}\geq0}L(x,\lambda,\mu)$$ where the
supremum ensures that the constraints are satisfied because the
Lagrangian is infinity if the constraints are not satisfied.

Let's consider interchanging the minimization and maximization. For
$\mu\succeq0$, one can show that
$$\sup_{\lambda,\mu:\mu_{j}\geq0}\inf_{x}L(x,\lambda,\mu)\leq\inf_{x}\sup_{\lambda,\mu:\mu_{j}\geq0}L(x,\lambda,\mu),$$
because $\inf_{x}L(x,\lambda,\mu)\leq f(x^{*})$ for the minimizing value
$x^{*}$ (p. 216 of the Boyd book). This gives us the Lagrange dual
function: $$d(\lambda,\mu)=\inf_{x}L(x,\lambda,\mu),$$ and the Lagrange
dual problem is to find the best lower bound:
$$\sup_{\lambda,\mu:\mu_{j}\geq0}d(\lambda,\mu).$$

The dual problem is always a convex optimization problem because
$d(\lambda,\mu)$ is concave (because $d(\lambda,\mu)$ is a pointwise
infimum of a family of affine functions of $(\lambda,\mu)$). If the
optima of the primal (original) problem and that of the dual do not
coincide, there is said to be a "duality gap". For convex programming,
if certain conditions are satisfied (called *constraint
qualifications*), then there is no duality gap, and one can solve the
dual problem to solve the primal problem. Usually with the standard form
of convex programming, there is no duality gap. Provided we can do the
minimization over $x$ in closed form we then maximize $d(\lambda,\mu)$
w.r.t. the Lagrangian multipliers in a new constrained problem that is
sometimes easier to solve, giving us $(\lambda^{*},\mu^{*})$.

One can show (p. 242 of the Boyd book) that $\mu_{i}^{*}=0$ unless the
$i$th constraint is active at the optimum $x^{*}$ and that $x^{*}$
minimizes $L(x,\lambda^{*},\mu^{*})$. So once one has
$(\lambda^{*},\mu^{*})$, one is in the position of minimizing an
unconstrained convex function. If $L(x,\lambda^{*},\mu^{*})$ is strictly
convex, then $x^{*}$ is the unique optimum provided $x^{*}$ satisfies
the constraints, and no optimum exists if it does not.

Here's a simple example: suppose we want to minimize $x^{\top}x$ s.t.
$Ax=b$. The Lagrangian is $L(x,\lambda)=x^{\top}x+\lambda^{\top}(Ax-b)$.
Since $L(x,\lambda)$ is quadratic in $x$, the infimum is found by
setting $\nabla_{x}L(x,\lambda)=2x+A^{\top}\lambda=0$, yielding
$x=-\frac{1}{2}A^{\top}\lambda$. So the dual function is obtained by
plugging this value of $x$ into $L(x,\lambda)$, which gives
$$d(\lambda)=-\frac{1}{4}\lambda^{\top}AA^{\top}\lambda-b^{\top}\lambda,$$
which is concave quadratic. In this case we can solve the original
constrained problem in terms of this unconstrained dual problem.

Another example is the primal and dual forms for finding the SVM
classifier (see [the Wikipedia
article](https://en.wikipedia.org/wiki/Support_vector_machine#Primal_form)).
In this algorithm, we want to develop a classifier using $n$ pairs of
$y\in\Re^{1}$ and $x\in\Re^{p}$. The dual form is easily derived because
the minimization over $x$ occurs in a function that is quadratic in $x$.
Expressing the problem in the primal form gives an optimization in
$\Re^{p}$ while doing so in the dual form gives an optimization in
$\Re^{n}$. So one reason to use the dual form would be if you have
$n\ll p$.

## KKT conditions (optional)

Karush-Kuhn-Tucker (KKT) theory provides sufficient conditions under
which a constrained optimization problem has a minimum, generalizing the
Lagrange multiplier approach. The Lange and Boyd books have whole
sections on this topic.

Suppose that the function and the constraint functions are continuously
differentiable near $x^{*}$ and that we have the Lagrangian as before:
$$L(x,\lambda,\mu)=f(x)+\sum_{i}\lambda_{i}g_{i}(x)+\sum_{j}\mu_{j}h_{j}(x).$$

For nonconvex problems, if $x^{*}$ and $(\lambda^{*},\mu^{*})$ are the
primal and dual optimal points and there is no duality gap, then the KKT
conditions hold: $$\begin{aligned}
h_{j}(x^{*}) & \leq & 0\\
g_{i}(x^{*}) & = & 0\\
\mu_{j}^{*} & \geq & 0\\
\mu_{j}^{*}h_{j}(x^{*}) & = & 0\\
\nabla f(x^{*})+\sum_{i}\lambda_{i}^{*}\nabla g_{i}(x^{*})+\sum_{j}\mu_{j}^{*}\nabla h_{j}(x^{*}) & = & 0.\end{aligned}$$

For convex problems, we also have that if the KKT conditions hold, then
$x^{*}$ and $(\lambda^{*},\mu^{*})$ are primal and dual optimal and
there is no duality gap.

We can consider this from a slightly different perspective, in this case
requiring that the Lagrangian be twice differentiable.

First we need a definition. A *tangent direction*, $w$, with respect to
$g(x)$, is a vector for which $\nabla g_{i}(x)^{\top}w=0$. If we are at
a point, $x^{*}$, at which the constraint is satisfied,
$g_{i}(x^{*})=0$, then we can move in the tangent direction (orthogonal
to the gradient of the constraint function) (i.e., along the level
curve) and still satisfy the constraint. This is the only kind of
movement that is legitimate (gives us a feasible solution).

If the gradient of the Lagrangian with respect to $x$ is equal to 0,
$$\nabla f(x^{*})+\sum_{i}\lambda_{i}\nabla g_{i}(x^{*})+\sum_{j}\mu_{j}\nabla h_{j}(x^{*})=0,$$
and if $w^{\top}H_{L}(x^{*},\lambda,\mu)w>0$ (with $H_{L}$ being the
Hessian of the Lagrangian) for all vectors $w$ s.t.
$\nabla g(x^{*})^{\top}w=0$ and, for all active
constraints,$\nabla h(x^{*})^{\top}w=0$, then $x^{*}$ is a local
minimum. An active constraint is an inequality for which
$h_{j}(x^{*})=0$ (rather than $h_{j}(x^{*})<0$, in which case it is
inactive). Basically we only need to worry about the inequality
constraints when we are on the boundary, so the goal is to keep the
constraints inactive.

Some basic intuition is that we need positive definiteness only for
directions that stay in the feasible region. That is, our only possible
directions of movement (the tangent directions) keep us in the feasible
region, and for these directions, we need the objective function to be
increasing to have a minimum. If we were to move in a direction that
goes outside the feasible region, it's ok for the quadratic form
involving the Hessian to be negative.

Many algorithms for convex optimization can be interpreted as methods
for solving the KKT conditions.

## Interior-point methods

We'll briefly discuss one of the standard methods for solving a convex
optimization problem. The barrier method is one type of interior-point
algorithm. It turns out that Newton's method can be used to solve a
constrained optimization problem, with twice-differentiable $f$ and
linear equality constraints. So the basic strategy of the barrier method
is to turn the more complicated constraint problem into one with only
linear equality constraints.

Recall our previous notation, in which convex programming minimizes
$f(x)$ s.t. $h_{i}(x)\leq0,\,j=1,\ldots,m$ and
$a_{i}^{\top}x=b_{i},\,i=1,\ldots,q$, where both $f$ and the constraint
functions are convex. The strategy begins with moving the inequality
constraints into the objective function:
$$f(x)+\sum_{j=1}^{m}I_{-}(h_{j}(x))$$ where $I_{-}(u)=0$ if $u\leq0$ and $I_{-}(u)=\infty$ if $u>0$.

This is fine, but the new objective function is not differentiable so we
can't use a Newton-like approach. Instead, we approximate the indicator
function with a logarithmic function, giving the new objective function
$$\tilde{f}(x)=f(x)+\sum_{j=1}^{m}-(1/t^{*})\log(-h_{j}(x)),$$ which is
convex and differentiable. The new term pushes down the value of the
overall objective function when $x$ approaches the boundary, nearing
points for which the inequality constraints are not met. The
$-\sum(1/t^{*})\log(-h_{j}(x))$ term is called the log barrier, since it
keeps the solution in the feasible set (i.e., the set where the
inequality constraints are satisfied), provided we start at a point in
the feasible set. Newton's method with equality constraints ($Ax=b$) is
then applied. The key thing is then to have $t^{*}$ get larger (i.e.,
$t^{*}$ is some increasing function of iteration time $t$) as the
iterations proceed, which allows the solution to get closer to the
boundary if that is indeed where the minimum lies.

The basic ideas behind Newton's method with equality constraints are (1)
start at a feasible point, $x_{0}$, such that $Ax_{0}=b$, and (2) make
sure that each step is in a feasible direction, $A(x_{t+1}-x_{t})=0$. To
make sure the step is in a feasible direction we have to solve a linear
system similar to that in the simplified quadratic programming problem: $$\left(\begin{array}{c}
x_{t+1}-x_{t}\\
\lambda
\end{array}\right)=\left(\begin{array}{cc}
H_{\tilde{f}}(x_{t}) & A^{\top}\\
A & 0
\end{array}\right)^{-1}\left(\begin{array}{c}
-\nabla\tilde{f}(x_{t})\\
0
\end{array}\right),$$ which shouldn't be surprising since the whole idea
of Newton's method is to substitute a quadratic approximation for the
actual objective function.

## Software for constrained and convex optimization

For general convex optimization in Python see the `cvxopt` package. Some
other resources to consider are

-   MATLAB, in particular the `fmincon()` function, the CVX system, and
    MATLAB's linear and quadratic programming abilities.
-   The CVXR package in R.

I haven't looked into CVXR in detail but given the developers include
Stephen Boyd, who is a convex optimization guru, it's worth checking
out.

`cvxopt` has specific solves (see `help(cvxopt.solvers)` for different
kinds of convex optimization. A general purpose one is `cvxopt.solvers.cp`.
Specifying the problem (the objective function, nonlinear constraints, and linear constraints) using the software is somewhat involved, so I haven't worked out an example here.

---

[← 8. Convexity](39-8-convexity.md) · [Up: contents](index.md) · [10. Summary →](41-10-summary.md)

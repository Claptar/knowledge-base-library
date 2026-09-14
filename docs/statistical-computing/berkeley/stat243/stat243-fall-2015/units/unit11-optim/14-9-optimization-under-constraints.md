---
title: 9 Optimization under constraints
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit11-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit11-optim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 9 Optimization under constraints

**Source:** [`units/unit11-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit11-optim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Constrained optimization is harder than unconstrained, and inequality constraints harder to deal with than equality constraints.

Constrained optimization can sometimes be avoided by reparameterizing. E.g., to optimize w.r.t. a variance component or other non-negative parameter, you can work on the log scale.

Optimization under constraints often goes under the name of ’programming’, with different types of programming for different types of objective functions combined with different types of constraints.

### **9.1 Convex optimization (convex programming)**

Convex programming minimizes _f_ ( _x_ ) s.t. _hj_ ( _x_ ) _≤_ 0 _, j_ = 1 _, . . . , m_ and _ai_<sup>_⊤x_=</sup><sup>_bi,i_=1</sup><sup>_, . . . , q_,</sup> where both _f_ and the constraint functions are convex. Note that this includes more general equality constraints, as we can write _g_ ( _x_ ) = _b_ as two inequalities _g_ ( _x_ ) _≤ b_ and _g_ ( _x_ ) _≥ b_ . It also includes _hj_ ( _x_ ) _≥ bj_ by taking _−hj_ ( _x_ ). Note that we can always have _hj_ ( _x_ ) _≤ bj_ and convert to the above form by subtracting _bj_ from each side (note that this preserves convexity). A vector _x_ is said to be feasible, or in the feasible set, if all the constraints are satisfied for _x_ .

There are good algorithms for convex programming, and it’s possible to find solutions when we have hundreds or thousands of variables and constraints. It is often difficult to recognize if one has a convex program (i.e., if _f_ and the constraint functions are convex), but there are many tricks

35

to transform a problem into a convex program and many problems can be solved through convex programming. So the basic challenge is in recognizing or transforming a problem to one of convex optimization; once you’ve done that, you can rely on existing methods to find the solution.

Linear programming, quadratic programming, second order cone programming and semidefinite programming are all special cases of convex programming. In general, these types of optimization are progressively more computationally complex.

First let’s see some of the special cases and then discuss the more general problem.

### **9.2 Linear programming: Linear system, linear constraints**

Linear programming seeks to minimize


subject to a system of _m_ inequality constraints, _a_<sup>_⊤_</sup> _i_<sup>_x≤bi_for</sup><sup>_i_=1</sup><sup>_, . . . , m_,where</sup><sup>_A_isoffull</sup> row rank. This can also be written in terms of generalized inequality notation, _Ax ⪯ b_ . There are standard algorithms for solving linear programs, including the simplex method and interior point methods.

Note that each equation in the set of equations _Ax_ = _b_ defines a hyperplane, so each inequality in _Ax ⪯ b_ defines a half-space. Minimizing a linear function (presuming that the minimum exists) must mean that we push in the correct direction towards the boundaries formed by the hyperplanes, with the solution occuring at a corner (vertex) of the solid formed by the hyperplanes. The simplex algorithm starts with a feasible solution at a corner and moves along edges in directions that improve the objective function.

### **9.3 General system, equality constraints**

Suppose we have an objective function _f_ ( _x_ ) and we have equality constraints, _Ax_ = _b_ . We can manipulate this into an unconstrained problem. The null space of _A_ is the set of _x_ s.t. _Ax_ = 0. So if we start with a candidate _xc_ s.t. _Axc_ = _b_ (e.g., by using the pseudo inverse, _A_<sup>+</sup> _b_ ), we can form all other candidates (a candidate is an _x_ s.t. _Ax_ = _b_ ) as _x_ = _xc_ + _Bz_ where _B_ is a set of column basis functions for the null space of _A_ and _z ∈ℜ_<sup>_p−m_</sup> . Consider _h_ ( _z_ ) = _f_ ( _xc_ + _Bz_ ) and note that _h_ is a function of _p − m_ rather than _p_ inputs. Namely, we are working in a reduced dimension space with no constraints. If we assume differentiability of _f_ , we can express _∇h_ ( _z_ ) = _B_<sup>_⊤_</sup> _∇f_ ( _xc_ + _Bz_ ) and _Hh_ ( _z_ ) = _B_<sup>_⊤_</sup> _Hf_ ( _xc_ + _Bz_ ) _B_ . Then we can use unconstrained methods to find the point at which _∇h_ ( _z_ ) = 0.

How do we find _B_ ? One option is to use the _p − m_ columns of _V_ in the SVD of _A_ that

36

correspond to singular values that are zero. A second option is to take the QR decomposition of _A_<sup>_⊤_</sup> . Then _B_ is the columns of _Q_ 2, where these are the columns of the (non-skinny) Q matrix corresponding to the rows of _R_ that are zero.

For more general (nonlinear) equality constraints, _gi_ ( _x_ ) = _bi_ , _i_ = 1 _, . . . , q_ , we can use the Lagrange multiplier approach to define a new objective function,


for which, if we set the derivative (with respect to both _x_ and the Lagrange multiplier vector, _λ_ ) equal to zero, we have a critical point of the original function and we respect the constraints.

An example occurs with quadratic programming, under the simplification of affine equality constraints (quadratic programming in general optimizes a quadratic function under affine inequality constraints - i.e., constraints of the form _Ax − b ⪯_ 0). For example we might solve a least squares problem subject to linear equality constraints, _f_ ( _x_ ) = 2<sup><u>1</u></sup><sup>_x⊤Qx_+</sup><sup>_m⊤x_+</sup><sup>_c_s.t.</sup><sup>_Ax_=</sup><sup>_b_,</sup> where _Q_ is positive semi-definite. The Lagrange multiplier approach gives the objective function


and differentiating gives the equations


which leads to the solution


which gives us _x_<sup>_∗_</sup> = _−Q_<sup>_−_1</sup> _m_ + _Q_<sup>_−_1</sup> _A_<sup>_⊤_</sup> ( _AQ_<sup>_−_1</sup> _A_<sup>_⊤_</sup> )<sup>_−_1</sup> ( _AQ_<sup>_−_1</sup> _m_ + _b_ ).

Under inequality constraints there are a variety of methods but we won’t go into them.

### **9.4 The dual problem**

Sometimes a reformulation of the problem eases the optimization. There are different kinds of dual problems, but we’ll just deal with the Lagrangian dual. Let _f_ ( _x_ ) be the function we want to minimize, under constraints _gi_ ( _x_ ) = 0; _i_ = 1 _, . . . , q_ and _hj_ ( _x_ ) _≤_ 0; _j_ = 1 _, . . . , m_ . Here I’ve explicitly written out the equality constraints to follow the notation in Lange. Consider the

37

Langrangian,


Solving that can be shown to be equivalent to this optimization:


where the supremum ensures that the constraints are satisfied because the Lagrangian is infinity if the constraints are not satisfied.

Let’s consider interchanging the minimization and maximization. For _µ ⪰_ 0, one can show that


because inf _x L_ ( _x, λ, µ_ ) _≤ f_ ( _x_<sup>_∗_</sup> ) for the minimizing value _x_<sup>_∗_</sup> (p. 216 of the Boyd book). This gives us the Lagrange dual function:


and the Lagrange dual problem is to find the best lower bound:


The dual problem is always a convex optimization problem because _d_ ( _λ, µ_ ) is concave (because _d_ ( _λ, µ_ ) is a pointwise infimum of a family of affine functions of ( _λ, µ_ )). If the optima of the primal (original) problem and that of the dual do not coincide, there is said to be a “duality gap”. For convex programming, if certain conditions are satisfied (called _constraint qualifications_ ), then there is no duality gap, and one can solve the dual problem to solve the primal problem. Usually with the standard form of convex programming, there is no duality gap. Provided we can do the minimization over _x_ in closed form we then maximize _d_ ( _λ, µ_ ) w.r.t. the Lagrangian multipliers in a new constrained problem that is sometimes easier to solve, giving us ( _λ_<sup>_∗_</sup> _, µ_<sup>_∗_</sup> ).

One can show (p. 242 of the Boyd book) that _µ_<sup>_∗_</sup> _i_<sup>=0 unless the</sup><sup>_i_th constraint is active at the</sup> optimum _x_<sup>_∗_</sup> and that _x_<sup>_∗_</sup> minimizes _L_ ( _x, λ_<sup>_∗_</sup> _, µ_<sup>_∗_</sup> ). So once one has ( _λ_<sup>_∗_</sup> _, µ_<sup>_∗_</sup> ), one is in the position of minimizing an unconstrained convex function. If _L_ ( _x, λ_<sup>_∗_</sup> _, µ_<sup>_∗_</sup> ) is strictly convex, then _x_<sup>_∗_</sup> is the unique optimum provided _x_<sup>_∗_</sup> satisfies the constraints, and no optimum exists if it does not.

Here’s a simple example: suppose we want to minimize _x_<sup>_⊤_</sup> _x_ s.t. _Ax_ = _b_ . The Lagrangian is _L_ ( _x, λ_ ) = _x_<sup>_⊤_</sup> _x_ + _λ_<sup>_⊤_</sup> ( _Ax − b_ ). Since _L_ ( _x, λ_ ) is quadratic in _x_ , the infimum is found by setting _∇xL_ ( _x, λ_ ) = 2 _x_ + _A_<sup>_⊤_</sup> _λ_ = 0, yielding _x_ = _−_<sup><u>1</u></sup> 2<sup>_A⊤λ_.So the dual function is obtained by plugging</sup>

38

this value of _x_ into _L_ ( _x, λ_ ), which gives


which is concave quadratic. In this case we can solve the original constrained problem in terms of this unconstrained dual problem.

Another example is the primal and dual forms for finding the SVM classifier (see the Wikipedia article). In this algorithm, we want to develop a classifier using _n_ pairs of _y ∈ℜ_<sup>1</sup> and _x ∈ℜ_<sup>_p_</sup> . The dual form is easily derived because the minimization over _x_ occurs in a function that is quadratic in _x_ . Expressing the problem in the primal form gives an optimization in _ℜ_<sup>_p_</sup> while doing so in the dual form gives an optimization in _ℜ_<sup>_n_</sup> . So one reason to use the dual form would be if you have _n ≪ p_ .

### **9.5 KKT conditions**

Karush-Kuhn-Tucker (KKT) theory provides sufficient conditions under which a constrained optimization problem has a minimum, generalizing the Lagrange multiplier approach. The Lange and Boyd books have whole sections on this topic.

Suppose that the function and the constraint functions are continuously differentiable near _x_<sup>_∗_</sup> and that we have the Lagrangian as before:


For nonconvex problems, if _x_<sup>_∗_</sup> and ( _λ_<sup>_∗_</sup> _, µ_<sup>_∗_</sup> ) are the primal and dual optimal points and there is no duality gap, then the KKT conditions hold:


For convex problems, we also have that if the KKT conditions hold, then _x_<sup>_∗_</sup> and ( _λ_<sup>_∗_</sup> _, µ_<sup>_∗_</sup> ) are primal and dual optimal and there is no duality gap.

We can consider this from a slightly different perspective, in this case requiring that the Lagrangian be twice differentiable.

39

First we need a definition. A _tangent direction_ , _w_ , with respect to _g_ ( _x_ ), is a vector for which _∇gi_ ( _x_ )<sup>_⊤_</sup> _w_ = 0. If we are at a point, _x_<sup>_∗_</sup> , at which the constraint is satisfied, _gi_ ( _x_<sup>_∗_</sup> ) = 0, then we can move in the tangent direction (orthogonal to the gradient of the constraint function) (i.e., along the level curve) and still satisfy the constraint. This is the only kind of movement that is legitimate (gives us a feasible solution).

If the gradient of the Lagrangian with respect to _x_ is equal to 0,


and if _w_<sup>_⊤_</sup> _HL_ ( _x_<sup>_∗_</sup> _, λ, µ_ ) _w >_ 0 (with _HL_ being the Hessian of the Lagrangian) for all vectors _w_ s.t. _∇g_ ( _x_<sup>_∗_</sup> )<sup>_⊤_</sup> _w_ = 0 and, for all active constraints, _∇h_ ( _x_<sup>_∗_</sup> )<sup>_⊤_</sup> _w_ = 0, then _x_<sup>_∗_</sup> is a local minimum. An active constraint is an inequality for which _hj_ ( _x_<sup>_∗_</sup> ) = 0 (rather than _hj_ ( _x_<sup>_∗_</sup> ) _<_ 0, in which case it is inactive). Basically we only need to worry about the inequality constraints when we are on the boundary, so the goal is to keep the constraints inactive.

Some basic intuition is that we need positive definiteness only for directions that stay in the feasible region. That is, our only possible directions of movement (the tangent directions) keep us in the feasible region, and for these directions, we need the objective function to be increasing to have a minimum. If we were to move in a direction that goes outside the feasible region, it’s ok for the quadratic form involving the Hessian to be negative.

Many algorithms for convex optimization can be interpreted as methods for solving the KKT conditions.

### **9.6 Interior-point methods**

We’ll briefly discuss one of the standard methods for solving a convex optimization problem. The barrier method is one type of interior-point algorithm. It turns out that Newton’s method can be used to solve a constrained optimization problem, with twice-differentiable _f_ and linear equality constraints. So the basic strategy of the barrier method is to turn the more complicated constraint problem into one with only linear equality constraints.

Recall our previous notation, in which convex programming minimizes _f_ ( _x_ ) s.t. _hi_ ( _x_ ) _≤_ 0 _, i_ = 1 _, . . . , m_ and _a_<sup>_⊤_</sup> _i_<sup>_x_=</sup><sup>_bi,i_= 1</sup><sup>_, . . . , q_, where both</sup><sup>_f_and the constraint functions are convex.</sup> The strategy begins with moving the inequality constraints into the objective function:


where _I−_ ( _u_ ) = 0 if _u ≤_ 0 and _I−_ ( _u_ ) = _∞_ if _u >_ 0.

40

This is fine, but the new objective function is not differentiable so we can’t use a Newton-like approach. Instead, we approximate the indicator function with a logarithmic function, giving the new objective function


which is convex and differentiable. The new term pushes down the value of the overall objective function when _x_ approaches the boundary, nearing points for which the inequality constraints are not met. The _−_<sup>�</sup> (1 _/t_ ) log( _−hj_ ( _x_ )) term is called the log barrier, since it keeps the solution in the feasible set (i.e., the set where the inequality constraints are satisfied), provided we start at a point in the feasible set. Newton’s method with equality constraints ( _Ax_ = _b_ ) is then applied. The key thing is then to have _t_ get larger as the iterations proceed, which allows the solution to get closer to the boundary if that is indeed where the minimum lies.

The basic ideas behind Newton’s method with equality constraints are (1) start at a feasible point, _x_ 0, such that _Ax_ 0 = _b_ , and (2) make sure that each step is in a feasible direction, _A_ ( _xt_ +1 _− xt_ ) = 0. To make sure the step is in a feasible direction we have to solve a linear system similar to that in the simplified quadratic programming problem (1):


which shouldn’t be surprising since the whole idea of Newton’s method is to substitute a quadratic approximation for the actual objective function.

### **9.7 Software for constrained and convex optimization**

R provides an optimization function, _constrOptim()_ , for optimizing with linear inequality constraints. This is somewhat more limited than the general problem we’ve defined in that the constraints need to be linear rather than general functions, _h_ . However, _constrOptim()_ doesn’t require a convex function. It uses a logarithmic barrier function as discussed above in combination with the methods used in _optim()_ , e.g., Nelder-Mead, BFGS, etc. In fact it uses _optim()_ for the sequential optimizations, i.e., the individual optimizations involved as one changes the value of 1 _/t_ (called _mu_ in _constrOptim()_ ).

Here is how one can use _constrOptim()_ for linear inequality and linear equality constraints. The feasible region is defined to be _u_<sup>_⊤_</sup> _i_<sup>_θ −ci≥_0</sup><sup>_,i_=1</sup><sup>_, . . ._,so for “less than or equal” and for</sup> equality constraints we need to do some basic manipulations to get our actual constraints into the form needed for the R function. _θ_ in the notation of _constrOptim()_ is what we’ve been calling _x_ .

41

_## based on the example in ?constrOptim_ fr <- **function** (x) { _## Rosenbrock Banana function_ x1 <- x[1] x2 <- x[2] 100 * (x2 - x1 * x1)^2 + (1 - x1)^2 } grr <- **function** (x) { _## Gradient of 'fr'_ x1 <- x[1] x2 <- x[2] **c** (-400 * x1 * (x2 - x1 * x1) - 2 * (1 - x1), 200 * (x2 - x1 * x1)) } m <- 100 x1s <- x2s <- **seq** (-5, 5, len = m) xs <- **expand.grid** (x1s, x2s) f <- **apply** (xs, 1, fr) **image.plot** (x1s, x2s, **matrix** ( **log** (f), m)) ui = **rbind** ( **c** (-1,0), **c** (1,-1)) ci = **c** (-0.9, -0.1) _## x1 <= 0.9 ## x2 <= x1 + 0.1 ## this is Region "I" in the figure_ **abline** (v = 0.9) **abline** (.1, 1) out <- **constrOptim** ( **c** (.5,0), fr, grr, ui = ui, ci = ci) out$par ## [1] 0.8999999996 0.8100006078 **points** (out$par[1], out$par[2]) **text** (-1,-2, "I", cex = 2)

42

_## what about constraining to a different region? ("Region II")_ ui = **rbind** ( **c** (-1,0), **c** (-1, 1)) ci = **c** (-0.9,0.1) _## x1 <= 0.9 ## x2 >= x1 + 0.1_

out <- **constrOptim** ( **c** (.5,0), fr, grr, ui = ui, ci = ci)

**## Error in constrOptim(c(0.5, 0), fr, grr, ui = ui, ci = ci): initial value is not in the interior of the feasible region**

_## whoops, not feasible!_ out <- **constrOptim** ( **c** (-3, 2), fr, grr, ui = ui, ci = ci) **points** (out$par[1], out$par[2], pch = 2) **text** (-3,0, "II", cex = 2)


<!-- Start of picture text -->
10<br>8<br>6<br>G<br>II 4<br>2<br>I<br>0<br>−2<br>−4 −2 0 2 4<br>x1s<br>4<br>2<br>0<br>x2s<br>−2<br>−4<br><!-- End of picture text -->

_## how about optimizing along a line (equality constraint)? ## x1 - x2 = 0.1 is the same as_

43

_## x1 - x2 <= 0.1 ## x1 - x2 >= 0.1_ ui = **rbind** ( **c** (-1, 1), **c** (1, -1)) ci = **c** (-0.1, 0.1) out <- **constrOptim** ( **c** (3.1, 3.0), fr, grr, ui = ui, ci = ci) **## Error in constrOptim(c(3.1, 3), fr, grr, ui = ui, ci = ci): initial value is not in the interior of the feasible region** _## hmmm, numerical issues?_

_## ok, how about making a long narrow region around the line? ## this takes a while..._ ui = **rbind** ( **c** (1,-1), **c** (-1,1)) ci = **c** (.099,-.101) _## hmmm, out1 thinks it has converged ..._ out1 <- **constrOptim** ( **c** (3.1, 3.0), fr, grr, ui = ui, ci = ci) out2 <- **constrOptim** ( **c** (3.1, 3.0), fr, **NULL** , ui = ui, ci = ci) **image.plot** (x1s, x2s, **matrix** ( **log** (f), m)) **abline** (-0.1, 1) **points** (out1$par[1], out1$par[2], pch = "1") **points** (out2$par[1], out2$par[2], pch = "2")

44


<!-- Start of picture text -->
10<br>1 8<br>6<br>2<br>4<br>2<br>0<br>−2<br>−4 −2 0 2 4<br>x1s<br>4<br>2<br>0<br>x2s<br>−2<br>−4<br><!-- End of picture text -->

This paper discusses R’s capabilities for convex optimization in more detail.

Given that R is somewhat limited in its treatment of convex optimization, some other resources to consider are

- Python, in particular the _cvxopt_ package, and

- Matlab, in particular the _fmincon()_ function, the CVX system, and Matlab’s linear and quadratic programming abilities.

---

[← 8 Convexity](13-8-convexity.md) · [Up: contents](index.md) · [10 Summary →](15-10-summary.md)

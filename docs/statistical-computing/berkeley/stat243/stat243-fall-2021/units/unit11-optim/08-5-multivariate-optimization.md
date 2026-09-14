---
title: 5 Multivariate optimization
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit11-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit11-optim.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Multivariate optimization

**Source:** [`units/unit11-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit11-optim.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Optimizing as the dimension of the space gets larger becomes increasingly difficult:

1. In high dimensions, there are many possible directions to go.

2. One can end up having to do calculations with large vectors and matrices.

3. Multimodality increasingly becomes a concern (and can be hard to detect).

First we’ll discuss the idea of profiling to reduce dimensionality and then we’ll talk about various numerical techniques, many of which build off of Newton’s method (using second derivative information). We’ll finish by talking about methods that only use the gradient (and not the second derivative) and methods that don’t use any derivative information.

### **5.1 Profiling**

A core technique for likelihood optimization is to analytically maximize over any parameters for which this is possible. Suppose we have two sets of parameters, _θ_ 1 and _θ_ 2, and we can analytically maximize w.r.t _θ_ 2. This will give us _θ_<sup>ˆ</sup> 2( _θ_ 1), a function of the remaining parameters over which analytic maximization is not possible. Plugging in _θ_<sup>ˆ</sup> 2( _θ_ 1) into the objective function (in this case generally the likelihood or log likelihood) gives us the profile (log) likelihood solely in terms of the obstinant parameters. For example, suppose we have the regression likelihood with correlated errors:


where Σ( _ρ_ ) is a correlation matrix that is a function of a parameter, _ρ_ . The maximum w.r.t. _β_ is easily seen to be the GLS estimator _β_<sup>ˆ</sup> ( _ρ_ ) = ( _X_<sup>_⊤_</sup> Σ( _ρ_ )<sup>_−_1</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> Σ( _ρ_ )<sup>_−_1</sup> _Y_ . (In general such a maximum is a function of all of the other parameters, but conveniently it’s only a function of _ρ_ here.) This gives us the initial profile likelihood


13

We then notice that the likelihood is maximized w.r.t. _σ_<sup>2</sup> at


This gives us the final profile likelihood,


a function of _ρ_ only, for which numerical optimization is much simpler.

### **5.2 Newton-Raphson (Newton’s method)**

For multivariate _x_ we have the Newton-Raphson update _xt_ +1 = _xt − f_<sup>_′′_</sup> ( _xt_ )<sup>_−_1</sup> _f_<sup>_′_</sup> ( _xt_ ), or in our other notation,


In class we’ll use the demo code in the Unit 11 code file (not shown here) for an example of finding the nonlinear least squares fit to some weight loss data to fit the model (but note that technically speaking one can use profiling in this case, so it’s not a perfect example):


Some of the things we need to worry about with Newton’s method in general about are (1) good starting values, (2) positive definiteness of the Hessian, and (3) avoiding errors in deriving the derivatives.

A note on the positive definiteness: since the Hessian may not be positive definite (although it may well be, provided the function is approximately locally quadratic), one can consider modifying the Cholesky decomposition of the Hessian to enforce positive definiteness by adding diagonal elements to _Hf_ as necessary.

Next we’ll see that some optimization methods used commonly for statistical models (in particular Fisher scoring and iterative reweighted least squares (IRLS or IWLS) are just NewtonRaphson in disguise.

### **5.3 Fisher scoring variant on N-R**

The Fisher information (FI) is the expected value of the outer product of the gradient of the loglikelihood with itself


14

where the expected value is with respect to the data distribution. Under regularity conditions (true for exponential families), the expectation of the Hessian of the log-likelihood is minus the Fisher information, _Ef Hf_ ( _y_ ) = _−I_ ( _θ_ ). We get the observed Fisher information by plugging the data values into either expression instead of taking the expected value.

Thus, standard N-R can be thought of as using the observed Fisher information to find the updates. Instead, if we can compute the expectation, we can use minus the FI in place of the Hessian. The result is the Fisher scoring (FS) algorithm. Basically instead of using the Hessian for a given set of data, we are using the FI, which we can think of as the average Hessian over repeated samples of data from the data distribution. FS and N-R have the same convergence properties (i.e., quadratic convergence) but in a given problem, one may be computationally or analytically easier. Givens and Hoeting comment that FS works better for rapid improvements at the beginning of iterations and N-R better for refinement at the end.


In class we’ll use the demo code in the Unit 11 code file (not shown here) to try out Fisher scoring in the weight loss example.

The Gauss-Newton algorithm for nonlinear least squares involves using the FI in place of the Hessian in determining a Newton-like step. _nls()_ in R uses this approach. Note that this is not exactly the same updating as our manual coding of FS for the weight loss example.

**Connections between statistical uncertainty and ill-conditionedness** When either the observed or expected FI matrix is nearly singular this means we have a small eigenvalue in the inverse covariance (the precision), which means a large eigenvalue in the covariance matrix. This indicates some linear combination of the parameters has low precision (high variance), and that in that direction the likelihood is nearly flat. As we’ve seen with N-R, convergence slows with shallow gradients, and we may have numerical problems in determining good optimization steps when the likelihood is sufficiently flat. So convergence problems and statistical uncertainty go hand in hand. One, but not the only, example of this occurs when we have nearly collinear regressors.

### **5.4 IRLS (IWLS) for Generalized Linear Models (GLMs)**

As many of you know, iterative reweighted least squares (also called iterative weighted least squares) is the standard method for estimation with GLMs. It involves linearizing the model and using working weights and working variances and solving a weighted least squares (WLS) problem (recalling that the generic WLS solution is _β_<sup>ˆ</sup> = ( _X_<sup>_⊤_</sup> _WX_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> _WY_ ).

15

Exponential families can be expressed as


with _E_ ( _Y_ ) = _b_<sup>_′_</sup> ( _θ_ ) and Var( _Y_ ) = _b_<sup>_′′_</sup> ( _θ_ ). If we have a GLM in the canonical parameterization (log link for Poisson data, logit for binomial), we have the natural parameter _θ_ equal to the linear predictor, _θ_ = _η_ . A standard linear predictor would simply be _η_ = _Xβ_ .

Considering N-R for a GLM in the canonical parameterization (and ignoring _a_ ( _φ_ ), which is one for logistic and Poisson regression), one can show that the gradient of the GLM log-likelihood is the inner product of the covariates and a residual vector, _∇l_ ( _β_ ) = ( _Y − E_ ( _Y_ ))<sup>_⊤_</sup> _X_ , and the Hessian is _Hl_ ( _β_ ) = _−X_<sup>_⊤_</sup> _WX_ where _W_ is a diagonal matrix with _{_ Var( _Yi_ ) _}_ on the diagonal (the working weights). Note that both _E_ ( _Y_ ) and the variances in _W_ depend on _β_ , so these will change as we iteratively update _β_ . Therefore, the N-R update is


where _E_ ( _Y_ ) _t_ and _Wt_ are the values at the current parameter estimate, _βt_ . For example, for logistic exp( _Xi_<sup>_⊤βt_</sup><sup><u>)</u></sup> regression (here with _ni_ = 1), _Wt,ii_ = _pti_ (1 _− pti_ ) and _E_ ( _Y_ ) _ti_ = _pti_ where _pti_ = 1+exp( _Xi_<sup>_⊤βt_).In</sup> the canonical parameterization of a GLM, the Hessian does not depend on the data, so the observed and expected FI are the same, and therefore N-R and FS are the same.

The update above can be rewritten in the standard form of IRLS as a WLS problem,


where the so-called working observations are _Y_<sup>˜</sup> _t_ = _Xβt_ + _Wt_<sup>_−_1</sup> ( _Y −E_ ( _Y_ ) _t_ ). Note that these are on the scale of the linear predictor. The interpretation is that the working observations are equal to the current fitted values, _Xβt_ , plus weighted residuals where the weight (the inverse of the variance) takes the actual residuals and scales to the scale of the linear predictor.

While IRLS is standard for GLMs, you can also use general purpose optimization routines. IRLS is a special case of the general Gauss-Newton method for nonlinear least squares.

16

### **5.5 Descent methods and Newton-like methods**

More generally a Newton-like method has updates of the form


We can choose _Mt_ in various ways, including as an approximation to the second derivative. This opens up several possibilities:

1. using more computationally efficient approximations to the second derivative,

2. avoiding steps that do not go in the correct direction (i.e., go uphill when minimizing), and

3. scaling by _αt_ so as not to step too far.

Let’s consider a variety of strategies.

#### **5.5.1 Descent methods**

The basic strategy is to choose a good direction and then choose the longest step for which the function continues to decrease. Suppose we have a direction, _pt_ . Then we need to move _xt_ +1 = _xt_ + _αtpt_ , where _αt_ is a scalar, choosing a good _αt_ . We might use a line search (e.g., bisection or golden section search) to find the local minimum of _f_ ( _xt_ + _αtpt_ ) with respect to _αt_ . However, we often would not want to run to convergence, since we’ll be taking additional steps anyway.

Steepest descent chooses the direction as the steepest direction downhill, setting _Mt_ = _I_ , since the gradient gives the steepest direction uphill (the negative sign in the equation below has us move directly downhill rather than directly uphill). Given the direction, we want to scale the step


where the contraction, or step length, parameter _αt_ is chosen sufficiently small to ensure that we descend, via some sort of line search. The critical downside to steepest descent is that when the contours are elliptical, it tends to zigzag; here’s an example. Note that I do a full line search (using the golden section method via _optimize()_ ) at each step in the direction of steepest descent - this is generally computationally wasteful, but I just want to illustrate how steepest descent can go wrong, even if you go the “right” amount in each direction.

**par** (mai = **c** (.5,.4,.1,.4)) f <- **function** (x){

x[1]^2/1000 + 4*x[1]*x[2]/1000 + 5*x[2]^2/1000

17

} fp <- **function** (x){ **c** (2 * x[1]/1000 + 4 * x[2]/1000, 4 * x[1]/1000 + 10 * x[2]/1000) } lineSearch <- **function** (alpha, xCurrent, direction, FUN){ newx <- xCurrent + alpha * direction **FUN** (newx) } nIt <- 50 xvals <- **matrix** (NA, nr = nIt, nc = 2) xvals[1, ] <- **c** (7, -4) **for** (t **in** 2:50){ newalpha <- **optimize** (lineSearch, interval = **c** (-5000, 5000), xCurrent = xvals[t-1, ], direction = **fp** (xvals[t-1, ]), FUN = f)$minimum xvals[t, ] <- xvals[t-1, ] + newalpha * **fp** (xvals[t-1, ]) } x1s <- **seq** (-5, 8, len = 100); x2s = **seq** (-5, 2, len = 100) fx <- **apply** ( **expand.grid** (x1s, x2s), 1, f) _## plot f(x) surface on log scale_ **image.plot** (x1s, x2s, **matrix** ( **log** (fx), 100, 100), xlim = **c** (-5, 8), ylim = **c** (-5,2)) **lines** (xvals) _## overlay optimization path_

18


<!-- Start of picture text -->
−2<br>−4<br>−6<br>−8<br>−10<br>−12<br>−4 −2 0 2 4 6 8<br>2<br>1<br>0<br>−1<br>−2<br>−3<br>−4<br>−5<br><!-- End of picture text -->

_<mark>## kind of slow</mark>_

If the contours are circular, steepest descent works well. Newton’s method deforms elliptical contours based on the Hessian. Another way to think about this is that steepest descent does not take account of the rate of change in the gradient, while Newton’s method does.

The general descent algorithm is


where _Mt_ is generally chose to approximate the Hessian and _αt_ allows us to adjust the step in a smart way. Basically, since the negative gradient tells us the direction that descends (at least within a small neighborhood), if we don’t go too far, we should be fine and should work our way downhill. One can work this out formally using a Taylor approximation to _f_ ( _xt_ +1) _− f_ ( _xt_ ) and see that we make use of _Mt_ being positive definite. (Unfortunately backtracking with positive definite _Mt_ does not give a theoretical guarantee that the method will converge. We also need to make sure that the steps descend sufficiently quickly and that the algorithm does not step along a level contour of _f_ .)

The conjugate gradient algorithm for iteratively solving large systems of equations is all about choosing the direction and the step size in a smart way given the optimization problem at hand.

19

#### **5.5.2 Quasi-Newton methods such as BFGS**

Other replacements for the Hessian matrix include estimates that do not vary with _t_ and finite difference approximations. When calculating the Hessian is expensive, it can be very helpful to substitute an approximation.

A basic finite difference approximation requires us to compute finite differences in each dimension, but this could be computationally burdensome. A more efficient strategy for choosing _Mt_ +1 is to (1) make use of _Mt_ and (2) make use of the most recent step to learn about the curvature of _f_<sup>_′_</sup> ( _x_ ) in the direction of travel. One approach is to use a rank one update to _Mt_ .

A basic strategy is to choose _Mt_ +1 such that the secant condition is satisfied:


which is motivated by the fact that the secant approximates the gradient in the direction of travel. Basically this says to modify _Mt_ in such a way that we incorporate what we’ve learned about the gradient from the most recent step. _Mt_ +1 is not fully determined based on this, and we generally impose other conditions, in particular that _Mt_ +1 is symmetric and positive definite. Defining _st_ = _xt_ +1 _− xt_ and _yt_ = _∇f_ ( _xt_ +1) _−∇f_ ( _xt_ ), the unique, symmetric rank one update (why is the following a rank one update?) that satisfies the secant condition is


If the denominator is positive, _Mt_ +1 may not be positive definite, but this is guaranteed for nonpositive values of the denominator. One can also show that one can achieve positive definiteness by shrinking the denominator toward zero sufficiently.

A standard approach to updating _Mt_ is a commonly-used rank two update that generally results in _Mt_ +1 being positive definite is


which is known as the Broyden-Fletcher-Goldfarb-Shanno (BFGS) update. This is one of the methods used in R in _optim()_ .

Question: how can we update _Mt_<sup>_−_1</sup> to _Mt_<sup>_−_</sup> +1<sup>1efficiently?It turnsout there is a way to update</sup> the Cholesky of _Mt_ efficiently and this is a better approach than updating the inverse.

The order of convergence of quasi-Newton methods is generally slower than the quadratic convergence of N-R because of the approximations but still faster than linear. In general, quasiNewton methods will do much better if the scales of the elements of _x_ are similar. Lange suggests

20

using a starting point for which one can compute the expected information, to provide a good starting value _M_ 0.

Note that for estimating a covariance based on the numerical information matrix, we would not want to rely on _Mt_ from the final iteration, as the approximation may be poor. Rather we would spend the effort to better estimate the Hessian directly at _x_<sup>_∗_</sup> .

#### **5.5.3 Stochastic gradient descent**

Stochastic gradient descent (SGD) is the hot method in machine learning, commonly used for fitting deep neural networks. It allows you to optimize an objective function with respect to what is often a very large number of parameters even when the data size is huge.

Gradient descent is a simplification of Newton’s method that does not rely on the second derivative, but rather chooses the direction using the gradient and then a step size, _αt_ :


The basic idea of stochastic gradient descent is to replace the gradient with a function whose expected value is the gradient, _E_ ( _g_ ( _xt_ )) = _f_<sup>_′_</sup> ( _xt_ ):


Thus on average we should go in a good (downhill) direction. Given that we know that strictly following the gradient can lead to slow convergence, it makes some intuitive sense that we could still do ok without using the exact gradient. One can show formally that SGD will converge for convex functions.

SGD can be used in various contexts, but the common one we will focus on is when


for large _n_ . Thus calculation of the gradient is _O_ ( _n_ ), and we may not want to incur that computational cost. How could we implement SGD in such a case? At each iteration we could randomly choose an observation and compute the contribution to the gradient from that data point, or we could choose a random subset of the data (this is _mini-batch SGD_ ), or there are variations where we systematically cycle through the observations or cycle through subsets. However, in some situations, convergence is actually much faster when using randomness. And if the data are or-

21

dered in some meaningful way we definitely do not want to cycle through the observations in that order, as this can result in a biased estimate of the gradient and slow convergence. So one generally randomly shuffles the data before starting SGD. Note that using subsets rather than individual observations is likely to be more effective as it can allow us to use optimized matrix/vector computations.

How should one choose the step size, _αt_ (also called the learning rate)? One might think that as one gets close to the optimum, if one isn’t careful, one might simply bounce around near the optimum in a random way, without actually converging to the optimum. So intuition suggests that _αt_ should decrease with _t_ . Some choices of step size have included:

- _αt_ = 1 _/t_

- set a schedule, such that for _T_ iterations, _αt_ = _α_ , then for the next _T_ , _αt_ = _αγ_ , then for the next _T_ , _αt_ = _αγ_<sup>2</sup> . A heuristic is for _γ ∈_ (0 _._ 8 _,_ 0 _._ 9).

- run with _αt_ = _α_ for _T_ iterations, then with _αt_ = _α/_ 2 for 2 _T_ , then with _αt_ = _α/_ 4 for 4 _T_ and so forth.

### **5.6 Coordinate descent (Gauss-Seidel)**

Gauss-Seidel is also known a back-fitting or cyclic coordinate descent. The basic idea is to work element by element rather than having to choose a direction for each step. For example backfitting used to be used to fit generalized additive models of the form _E_ ( _Y_ ) = _f_ 1( _z_ 1)+ _f_ 2( _z_ 2)+ _. . ._ + _fp_ ( _zp_ ).

The basic strategy is to consider the _j_ th component of _f_<sup>_′_</sup> ( _x_ ) as a univariate function of _xj_ only and find the root, _xj,t_ +1 that gives _fj_<sup>_′_(</sup><sup>_xj,t_+1)=0.One cycles through each element of</sup><sup>_x_to</sup> complete a single cycle and then iterates. The appeal is that univariate root-finding/minimization is easy, often more stable than multivariate, and quick.

However, Gauss-Seidel can zigzag, since you only take steps in one dimension at a time, as we see here.

f <- **function** (x){ **return** (x[1]^2/1000 + 4*x[1]*x[2]/1000 + 5*x[2]^2/1000) } f1 <- **function** (x1, x2){ _# f(x) as a function of x1_ **return** (x1^2/1000 + 4*x1*x2/1000 + 5*x2^2/1000) } f2 <- **function** (x2, x1){ _# f(x) as a function of x2_ **return** (x1^2/1000 + 4*x1*x2/1000 + 5*x2^2/1000)

22

} x1s <- **seq** (-5, 8, len = 100); x2s = **seq** (-5, 2, len = 100) fx <- **apply** ( **expand.grid** (x1s, x2s), 1, f) **image.plot** (x1s, x2s, **matrix** ( **log** (fx), 100, 100)) nIt <- 49 xvals <- **matrix** (NA, nr = nIt, nc = 2) xvals[1, ] <- **c** (7, -4) _## 5, -10_ **for** (t **in seq** (2, nIt, by = 2)){ _## Note that full optimization along each axis is unnecessarily ## expensive (since we are going to just take another step in the next ## iteration. Just using for demonstration here._ newx1 <- **optimize** (f1, x2 = xvals[t-1, 2], interval = **c** (-40, 40))$ xvals[t, ] <- **c** (newx1, xvals[t-1, 2]) newx2 <- **optimize** (f2, x1 = newx1, interval = **c** (-40, 40))$minimum xvals[t+1, ] <- **c** (newx1, newx2) } **lines** (xvals)


<!-- Start of picture text -->
−2<br>−4<br>−6<br>−8<br>−10<br>−12<br>−4 −2 0 2 4 6 8<br>x1s<br>2<br>1<br>0<br>−1<br>x2s<br>−3<br>−5<br><!-- End of picture text -->

In the notes for Unit 9 on linear algebra, I discussed the use of Gauss-Seidel to iteratively

23

solve _Ax_ = _b_ in situations where factorizing _A_ (which of course is _O_ ( _n_<sup>3</sup> )) is too computationally expensive.

**The lasso** The _lasso_ uses an L1 penalty in regression and related contexts. A standard formulation for the lasso in regression is to minimize


to find _β_<sup>ˆ</sup> ( _λ_ ) for a given value of the penalty parameter, _λ_ . A standard strategy to solve this problem is to use coordinate descent, either cyclically, or by using directional derivatives to choose the coordinate likely to decrease the objective function the most (a greedy strategy). We need to use directional derivatives because the penalty function is not differentiable, but does have directional derivatives in each direction. The directional derivative of the objective function for _βj_ is


where we add _λ_ if _βj ≥_ 0 and you subtract _λ_ if _βj <_ 0. If _βj,t_ is 0, then a step in either direction contributes + _λ_ to the derivative as the contribution of the penalty.

Once we have chosen a coordinate, we set the directional derivative to zero and solve for _βj_ to obtain _βj,t_ +1.

The _glmnet_ package in R (described in this Journal of Statistical Software paper) implements such optimization for a variety of penalties in linear model and GLM settings, including the lasso. This Mittal et al. paper describes similar optimization for survival analysis with very large _p_ , exploiting sparsity in the _X_ matrix for computational efficiency; note that they do not use NewtonRaphson because the matrix operations are infeasible computationally.

One nice idea that is used in lasso and related settings is the idea of finding the regression coefficients for a variety of values of _λ_ , combined with “warm starts”. A general approach is to start with a large value of _λ_ for which all the coefficients are zero and then decrease _λ_ . At each new value of _λ_ , use the estimated coefficients from the previous value as the starting values. This should allow for fast convergence and gives what is called the “solution path”. Often _λ_ is chosen based on cross-validation.

The LARS (least angle regression) algorithm uses a similar strategy that allows one to compute _β_ ˆ _λ_ for all values of _λ_ at once.

The lasso can also be formulated as the constrained minimization of _∥Y − Xβ∥_<sup>2</sup> 2<sup>s.t.�</sup> _j_<sup>_|βj| ≤_</sup> _c_ , with _c_ now playing the role of the penalty parameter. Solving this minimization problem would take us in the direction of quadratic programming, a special case of convex programming, dis-

24

cussed in Section 9.

### **5.7 Nelder-Mead**

This approach avoids using derivatives or approximations to derivatives. This makes it robust, but also slower than Newton-like methods. The basic strategy is to use a simplex, a polytope of _p_ + 1 points in _p_ dimensions (e.g., a triangle when searching in two dimensions, tetrahedron in three dimensions...) to explore the space, choosing to shift, expand, or contract the polytope based on the evaluation of _f_ at the points.

The algorithm relies on four tuning factors: a reflection factor, _α >_ 0; an expansion factor, _γ >_ 1; a contraction factor, 0 _< β <_ 1; and a shrinkage factor, 0 _< δ <_ 1. First one chooses an initial simplex: _p_ + 1 points that serve as the vertices of a convex hull.

1. Evaluate and order the points, _x_ 1 _, . . . , xp_ +1 based on _f_ ( _x_ 1) _≤ . . . ≤ f_ ( _xp_ +1). Let _x_ ¯ be the average of the first _p x_ ’s.

2. (Reflection) Reflect _xp_ +1 across the hyperplane (a line when _p_ + 1 = 3) formed by the other points to get _xr_ , based on _α_ .

   - _xr_ = (1 + _α_ )¯ _x − αxp_ +1

3. If _f_ ( _xr_ ) is between the best and worst of the other points, the iteration is done, with _xr_ replacing _xp_ +1. We’ve found a good direction to move.

4. (Expansion) If _f_ ( _xr_ ) is better than all of the other points, expand by extending _xr_ to _xe_ based on _γ_ , because this indicates the optimum may be further in the direction of reflection. If _f_ ( _xe_ ) is better than _f_ ( _xr_ ), use _xe_ in place of _xp_ +1. If not, use _xr_ . The iteration is done.

   - _xe_ = _γxr_ + (1 _− γ_ )¯ _x_

5. If _f_ ( _xr_ ) is worse than all the other points, but better than _f_ ( _xp_ +1), let _xh_ = _xr_ . Otherwise _f_ ( _xr_ ) is worse than _f_ ( _xp_ +1) so let _xh_ = _xp_ +1. In either case, we want to concentrate our polytope toward the other points.

   - (a) (Contraction) Contract _xh_ toward the hyperplane formed by the other points, based on _β_ , to get _xc_ . If the result improves upon _f_ ( _xh_ ) replace _xp_ +1 with _xc_ . Basically, we haven’t found a new point that is better than the other points, so we want to contract the simplex away from the bad point.

      - _xc_ = _βxh_ + (1 _− β_ )¯ _x_

25

- (b) (Shrinkage) Otherwise (if _xc_ is not better than _xh_ ), replace _xp_ +1 with _xh_ and shrink the simplex toward _x_ 1. Basically this suggests our step sizes are too large and we should shrink the simplex, shrinking towards the best point.

• _xi_ = _δxi_ + (1 _− δ_ ) _x_ 1 for _i_ = 2 _, . . . , p_ + 1

Convergence is assessed based on the sample variance of the function values at the points, the total of the norms of the differences between the points in the new and old simplexes, or the size of the simplex. In class we’ll work through some demo code (not shown here) that illustrates the individual steps in an iteration of Nelder-Mead.

We can see the points at which the function was evaluated in the same quadratic example we saw in previous sections. The left hand panel shows the steps from a starting point somewhat far from the optimum, with the first 9 points numbered. In this case, we start with points 1, 2, and 3. Point 4 is a reflection. At this point, it looks like point 5 is a contraction but that doesn’t exactly follow the algorithm above (since Point 4 is between Points 2 and 3 so the iteration should end without a contraction), so perhaps the algorithm as implemented is a bit different than as described above. In any event, the new set is (2, 3, 4). Then point 6 and point 7 are reflection and expansion steps and the new set is (3, 4, 6). Points 8 and 9 are again reflection and expansion steps. The right hand panel shows the steps from a starting point near (actually at) the optimum. Points 4 and 5 are reflection and expansion steps, with the next set being (1, 2, 5). Now step 6 is a reflection but it is the worst of all the points, so point 7 is a contraction of point 2 giving the next set (1, 5, 7). Point 8 is then a reflection and point 9 is a contraction of point 5.

f <- **function** (x, plot = TRUE, verbose = FALSE) { result <- x[1]^2/1000 + 4*x[1]*x[2]/1000 + 5*x[2]^2/1000 **if** (verbose) **print** (result) **if** (plot && cnt < 10) { **points** (x[1], x[2], pch = **as.character** (cnt)) **if** (cnt < 10) cnt <<- cnt + 1 **else** cnt <<- 1 **if** ( **interactive** ()) **invisible** ( **readline** (prompt = "Press <Enter> to continue...")) } **else if** (plot) **points** (x[1], x[2]) **return** (result) }

**library** (fields) **par** (mfrow = **c** (1,2))

26

x1s <- **seq** (-5, 10, len = 100); x2s = **seq** (-5, 2, len = 100) fx <- **apply** ( **expand.grid** (x1s, x2s), 1, f, FALSE) cnt <- 1 **image.plot** (x1s, x2s, **matrix** ( **log** (fx), 100, 100)) init <- **c** (7, -4) **optim** (init, f, method = "Nelder-Mead", verbose = FALSE) ## $par ## [1] -0.0006112564567 0.0001513538132 ## ## $value ## [1] 1.181103575e-10 ## ## $counts ## function gradient ## 65 NA ## ## $convergence ## [1] 0 ## ## $message ## NULL x1s <- **seq** (-.2, .2, len = 100); x2s = **seq** (-.12, .12, len = 100) fx <- **apply** ( **expand.grid** (x1s, x2s), 1, f, FALSE) cnt <- 1 **image.plot** (x1s, x2s, **matrix** ( **log** (fx), 100, 100)) init <- **c** (-0, 0) **optim** (init, f, method = "Nelder-Mead", verbose = FALSE)

27


<!-- Start of picture text -->
3<br>−2<br>−1<br>−4<br>−1<br>8<br>−6<br>−1<br>1 2<br>7 −8 7<br>9<br>9 −1<br>86<br>−10 6 5<br>345 −1<br>12 −12<br>4<br>−2<br>−4 0 2 4 6 8 −0.2 −0.1 0.0 0.1 0.2<br>x1s x1s<br>2<br>0.10<br>1<br>0<br>0.05<br>−1<br>x2s x2s 0.00<br>−2<br>−3<br>−0.05<br>−4<br>−0.10<br>−5<br><!-- End of picture text -->

---

[← Unit 11 — optim Part 07 —](07-unit-11-optim-part-07.md) · [Up: contents](index.md) · [$par ## [1] 0 0 ## ## $value ## [1] 0 ## ## $counts ## function gradient ## 77 NA →](09-value-1-0-counts-function-gradient-77-na.md)

---
title: Yaz − Y0z ⊥ Z0 | W, for all a, z
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Yaz − Y0z ⊥ Z0 | W, for all a, z

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**<u>DEF</u>** (Robins’ version) : Yaz − Y0z is a random variable not depending on z, only on a **<u>DEF</u>** (Pearl’s version) :

Yaz ⊥ Z0 | W for all a, z

A couple of comments on the different assumptions

- It is clear that the article version as well as Pearl’s version imply the lecture version. Apparently the lecture version is the weakest of the four.

17

• Pearl’s assumption is very strong: See Robins, Greenland’s article for relevant discussion.

- If the following model for the counterfactual hold


then


If β3̸ = 0 then Robin’s assumption fails (since if the expectation depends on z the random variables do as well). On the other hand if β3 = 0 then Robin’s assumption might hold.

We now derive a formula used in the estimation of the direct effect.

**<u>Theorem</u>** We have the following relation


**Proof** We have


Nothing much has happened so far, we have used the principle of successive conditioning, the last equality is (depending on one’s framework) a case of definition. Now, in the last expression we are conditioning on the event (Z0 = z). Using this event we may write


Now we use the DEF assumption (lecture version) to trivially get


Finally we use the standard causal result that E(Yaz) = E(Y | A = a, Z = z) (this requires the consistency and randomization assumptions) to get


and the proof is complete.

**Example 1** : Let us assume that we have a model


In that case


is the integrand of the integral in the above theorem. This integrand now needs to be integrated according to the theorem. As the integrand only depends on a, it may be moved outside the integral and we get


**Example 2** : We assume a more elaborate model than in example 1:


Again we compute the integrand of the integral in the theorem, and get

E(Y | A = a, Z = z, W = w) − E(Y | A = 0, Z = z, W = w) = β1a + β4az + β5aw 18

Using the theorem we get


where the next-to-last equation follows by using the standard causal identification. **Example 3** : Suppose we have a (more general) model of the form


where m0, m1 are fixed functions. In that case

E(Y | A = a, Z = z, W = w) − E(Y | A = 0, Z = z, W = w) = am1(z, w)

And we have


Marginal structural models are models for marginal distributions of treatment specific counterfactuals, possibly conditional on baseline covariates. We are looking at an observed data structure O = (W, A, Z, Y ), where W is the baseline covariates, A is the treatment, Z is the intermediate variable and Y is the outcome. They are random variables and time ordering W �→A �→Z �→Y . In the definition of a direct effect of A on Y one blocks the effect of A mediated through the intermediate variable Z.

The full data structure is X<sup>full</sup> = (W, (Za, a ∈ A), (Yaz, a ∈ A, z ∈ Z)) in terms of the counterfactuals (Za, a ∈ A) and (Yaz, a ∈ A, z ∈ Z) for the intermediate variable and outcome, respectively. X denotes the full data structure on a randomly sampled subject, one would like to observe. The direct effect of A (on Y ) is defined to be DF (a) = E(YaZ0) − E(Y0Z0). A direct effect is thus defined as the population mean of individual direct effects, where an individual direct effect is the difference between the outcome when an individual is treated and the intermediate variable is set at its value under no treatment, and the outcome when the same individual is not treated.

In the full data world we would observe, for each individual, the value of the intermediate variable over time resulting from each possible treatment history, and the value of the covariate process over time, including the outcome process, resulting from each combination of possible treatment history and possible intermediate variable history. Instead, our observed data is only a subset of this full data, consisting of a single treatment history and the corresponding intermediate variable and outcome.

Under the following assumptions, we are able to build our new marginal direct effect model.

**CA** (consistency assumption): We assume the existence of counterfactuals such that the observed data are O = (W, A, ZA, YAZA ).

19

**RA** (randomization assumption): We assume (A, Z) ⊥ ((Yaz; a ∈ A, z ∈ Z|)W ) , A ⊥ (Za, a ∈ A)|W

**DEA** (direct effect assumption): E(Yaz − Y0z|Z0 = Z, W ) = E(Yaz − Y0z|W ) for all z.

So **marginal direct effect model** is E(Yaz0 − Y0z0 |V ) = m(a, V |B0) where V is a subset of baseline covariates W and B0 is our parameter of interest of the full data distribution FX , where the parametrization m satisfies m(0, V |B) = 0 for all B.

We will propose a class of estimating functions for this parameter B0. The proof that this class of estimating functions is indeed unbiased relies on the previously established identifiability result of m(a, V |B0), which we state her for convenience. **Theorem**

DF (a, v) = E0(Yaz0 − Y0z0 |V )


We are using 0 as an index for true distribution. EW |V denotes the conditional expectation of W , given V .

How to estimate B using thIS result?

Firstly, we note that


Let θ = (B, η) be the combined parameter. We propose the following class of estimating functions for θ = (B, η) indexed by a vector function h of A, V of the same dimension as the dimension of θ:


We propose as particular choice


Given estimators gn,Z|A,W and gn,A|W of gZ|A,W and gA|W , respectively, and a possibly data dependent index hn (estimating h<sup>∗</sup> ), let θn be the solution of the corresponding estimating equation:


It is of interest to compare this estimator with an estimator of β0 directly based on the identifiability result stated in the theorem above. That is, one substitutes estimates of E(Y | A, Z, W ) and gZ|A,W into the identifiability mapping for E(YaZ0 − Y0Z0 | W ), and one regresses this on a, V according to the regression model m(a, V | β). We refer to the latter estimator as the likelihood based estimator. In the likelihood based estimator, one needs to estimate

(1) E(Y |A, Z, W )

(2) g(Z|A, W )

On the contrast, the IPTW-estimator of β relies on estimation of


(2) g(Z|A, W ) **The IPTW estimator:**

Suppose we observe (W, A, Y = YA), and the randomization assumption A ⊥ (Ya : a) | W (RA) holds. Suppose that we are interested in estimation of β0 in the MSM E(Ya | V ) = m(a, V | β0).

20

Definition:The IPTW estimating function for β0 with nuisance parameter g(A | X) = g(A | W ) is defined as:


where ϵ(β) = YA − m(A, V |β)

Note that the IPTW estimating function is indeed a function of the observed data under RA. We denote the estimator of the nuisance parameter g with gn.

The IPTW estimator of β is defined as the solution of the estimating equation associated with the observed data O and the IPTW estimating function at gn: �ni=1<sup>Dh(Oi|gn, β) = 0whereOifori = 1, ..., nrepresentstheni.i.d.observationsintheobserveddata.</sup>

The IPTW estimating function is **unbiased** at the true β: EPFX ,g Dh(O|β, g) = 0 if the ETA assumption holds for g(A | W ):


Thus, if gn is consistent for g(A | W ), and the ETA holds, then the IPTW estimator is asymptotically linear and thus consistent.

Proof:


Where X = (Ta¯, W<sup>¯</sup> a(Ta¯))a¯ ∈ A ∼ FX for the full data.

The IPTW estimate of β can be obtained in practice by performing a weighted least squares regression of Y on A<sup>¯</sup> and V using the MSM and weights inversely proportional to the treatment mechanism: λ(A<sup>¯</sup> <u>,V )</u> SRA= λ(A<sup>¯</sup> <u>,V )</u> w( A, V<sup>¯</sup> ) = gn(A<sup><u>¯</u></sup> |X) Π<sup>K</sup> t=0<sup>gn(A(t)|</sup> A<sup><u>¯</u></sup> (t−1),L<sup><u>¯</u></sup> (t))<sup>,whereλcanbeanynon-nullfunctionofA¯andV.</sup>

It can indeed be shown that the resulting estimate is a solution of the IPTW estimating equation where h(¯a, V ) = λ(¯a, V ) dβ<sup><u>d</u>(¯a, V |β).</sup>

If we substitute λ by g′ ( ¯A|V ) where g′ is the conditional distribution of A¯ given V,the resulting weights are called stabilized weights: w( A, V<sup>¯</sup> ) =<sup><u>g</u></sup> gnn′<sup><u>(</u></sup> (AA<sup>¯</sup> ||VV ))<sup>.</sup>

In addition, it was shown, see van der Laan and Robins (2002), that the treatment mechanism g should always be estimated even when g is known, as would be the case in a randomized trial. As a result, the

21

IPTW estimator may gain in efficiency by taking into account possible empirical confounding, without loss of consistency.

Estimating Functions, Kelly Moore, September 20, 2004.

**Why do we want to use another procedure than maximum likelihood?** Motivating example: T1, ..., Tn I.I.D T ∼ f0 (unspecified) Parameter of interest: µ0 = S0(t) (Survival function at point t) Likelihood: L(f ) =<sup>�n</sup> i=1<sup>f(xi)</sup> Use piecewise linear densities indexed by knot points (x1, ...xn) Sieve: Sequence of subspaces of the whole space which approximates the whole model

1) Set n equally spaced knot points

2) Maximum Likelihood over piecewise linear densities

Let sieve be M (m) ⊂M where M is all densities.

fˆm(Pn) is Maximum Likelihood of f0 based on the model indexed by m knot points M (m). Pn is the empirical distribution of T1, ..., Tn.

How do we choose the number of knots? **Likelihood Cross-Validation** . Given the sieve, this is a data adaptive procedure for choosing m.

Let Bn ∈{0, 1}<sup>n</sup>


Given Bn, let Pn,B<sup>0</sup> n<sup>, P 1</sup> n,Bn<sup>be the empirical distributionsof the training and validation samples respectively.</sup>

---

[← E(Yaz − Y0z | Z0 = z, W ) = E(Yaz − Y0z | W ), for all z](28-e-yaz-y0z-z0-z-w-e-yaz-y0z-w-for-all-z.md) · [Up: contents](index.md) · [C.V. Likelihood indexed by m →](30-c-v-likelihood-indexed-by-m.md)

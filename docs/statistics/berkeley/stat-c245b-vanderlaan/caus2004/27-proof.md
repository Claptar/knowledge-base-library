---
title: proof
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# proof

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can now derive the **G-computation formula** for parameter E[Yd|V ]


Hence, the parameter of interest is expressible as a function of the observed data O, assuming CA and RA hold.

**Example, continued** To see how the G-computation formula can be converted into an estimator of the parameter of interest, let’s consider how we might estimate E[Yd25|W2 = 1].

**step 1** To estimate the inner expectation E[Y |A = d(W ), W ] from the G-computation formula, first regress Y on A and W . Suppose this yields the regression equation


**step 2** Then, for each subject, plug the values for A = d25(W ), W1, and W2 into the regression equation to compute Y<sup>ˆ</sup> d25 ≡ E<sup>ˆ</sup> [Y |A = d25(W ), W1, W2]. We now have an estimate of the inner expectation.

**step 3** Compute the mean of Y<sup>ˆ</sup> d25 in the female subsample (this is an estimate of the outer expectation from the G-computation formula). This gives E<sup>ˆ</sup> [Yd25 |W2 = 1].

Suppose W2 had been a continuous variable like age (say, with range 18-65) instead of a binary variable like sex. Then step 3 above might not work well, since there likely wouldn’t be enough subjects at any given age to usefully compute an empirical mean. Instead, we could assume a model m(age|β) such as, say,


and then regress Y<sup>ˆ</sup> d25 on age to estimate the β parameters. Then E<sup>ˆ</sup> [Yd25 |age] = m(age|β<sup>ˆ</sup> ).

In fact, since we’re interested in evaluating dynamic regimes dθ for multiple values of θ, rather than formulating a separate model mθ(age|β) for each θ, it would be more useful to formulate a single model m(age, θ|β) that includes θ as an independent variable; e.g.,


To fit this model, we would first complete step 2 for each value of θ, so that for each subject we compute the vector ( Y<sup>ˆ</sup> dθ : allθ). Then we would regress Y<sup>ˆ</sup> dθ (all θ) on age and θ to estimate the β parameters. In our example, where we’re just interested in two θ values (i.e., 25 and 35), this repeated-measures regression would

16

be based on 2n data points, two per subject. Note that because the regression is not based on independent observations (since Y<sup>ˆ</sup> d25 and Y<sup>ˆ</sup> d35 may be correlated), we might want to use generalized least squares to fit the model. Finally, set E<sup>ˆ</sup> [Ydθ |age] = m(age, θ|β<sup>ˆ</sup> ).

As a final note, the bootstrap can be used to get standard errors and confidence intervals for the parameter estimates.

Estimation of direct and indirect causal effects (Kasper Daniel Hansen)

We focus on the point treatment case. The reader is referred to “Estimation of Direct and indirect causal effects in longitudinal studies” by Mark J. van der Laan and Maya L. Petersen, available from http://www.bepress.com/ucbbiostat/paper155.

We are looking at an observed data structure O = (W, A, Z, Y ) with the time (causal) ordering W �→ A �→ Z �→ Y . As usual W is the baseline covariates, A is the treatment, Z is the intermediate variable and Y is the outcome.

We are interested in the direct effect of the treatment on the outcome, which (intuitively) is the effect of A which is not mediated through the intermediate variable Z.

In our approach we will start by treating Z as a response (we will construct counterfactuals for it) as well as a treatment variable (we will index the counterfactual outcomes of the response by Z). This will allow us to define the direct effect of A (on Y ).

We assume existence of counterfactuals

- (Yaz, a ∈A, z ∈Z) (where A is the set of possible values for A and Z is the set of possible values for Z.

- (Za, a ∈A).

The full data structure is thus X<sup>full</sup> = (W, (Za, a ∈A), (Yaz, a ∈A, z ∈Z)).

We are now able to define the parameter of interest: the direct effect of A (on Y ) is defined to be

DF(a) = E(YaZ0) − E(Y0Z0)

Z0 in the definition is a random variable - the counterfactual outcome had A been assigned to 0. Note that we here define the direct effect as a difference between two expectations – this specific form (as opposed to eg. an odds ratio or similar) will be important for the calculations below.

As usual we need a couple of assumptions. They are (more or less) equal to the standard assumptions of causal inference with one extra assumption.

**<u>CA</u>** (consistency assumption): We assume the existence of counterfactuals (described above) such that the observed data are O = (W, A, ZA, YAZA ).

**<u>RA</u>** (randomization assumption): We assume

(A, Z) ⊥ (Yaz, a ∈A, z ∈Z) | W

and


The last (and new) assumption – in lack of better terminology we will call it the direct effect assumption

- has a couple of variants in the literature. In addition a new one saw light during the lecture. **<u>DEF</u>** (direct effect assumption) (lecture version):

---

[← Randomization Assumption (RA) A ⊥ (Yd : d ∈D)|W](26-randomization-assumption-ra-a-yd-d-d-w.md) · [Up: contents](index.md) · [E(Yaz − Y0z | Z0 = z, W ) = E(Yaz − Y0z | W ), for all z →](28-e-yaz-y0z-z0-z-w-e-yaz-y0z-w-for-all-z.md)

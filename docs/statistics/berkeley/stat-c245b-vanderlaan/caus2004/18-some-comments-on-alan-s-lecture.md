---
title: Some comments on Alan’s lecture
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Some comments on Alan’s lecture

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Start by thinking how you would do everything empirically. In the examples given above, we had few time points, binary variables, and low dimensional L. So really, in all these examples, we probably don’t need any models to do G-comp. Just estimate everything empirically. For example, in the two time point case, we have only four possible combinations of L(0), A(0). So, to estimate L(1), all we need to do is take the average L(1) among each of the possible subpopulations: (L(0) = 0, A(0) = 0), (L(0) = 0, A(0) = 1), (L(0) = 1, A(0) = 0), (L(0) = 1, A(0) = 1). However, as we have more covariates, continuous covariates, and covariates and treatment history measured over more time points, we will begin to run out of data to do things empirically. This is where models enter in- to help us deal with the "curse of dimensionality". On this topic, also see discussion of data-reduction methods in the previous lecture.

- To implement G-comp simulation, we need two data matrices: The first is the observed data. We use this to get estimates for our models. The second is the simulated data. We use this to record the results of our simulation and to estimate the distribution of our counterfactual outcomes of interest. A summary of the implementation of G-comp by simulation:

   - (1) Write down the likelihood

   - (2) Sample from the Likelihood and L(0)

   - (3) Get 10,000 simulated counterfactual outcomes (in our example, Y0, Y1)

   - (4) This gives us a data set with each line of data consisting of the counterfactual treatment (a), the covariates, and the simulated outcome. In this data, just do a regression of outcome on treatment (possibly conditional on covariates, if you are interested in that), or fit some other model, depending on what you are interested in.

**Using traditional methods for causal inference in the point treatment setting** Say we are interested in E[Ya | V ] = β0 + β1a + β2aV + β3V, V ⊂ L, (ie V is a subset of L). We can write: E[Ya | L] = E[Y | A = a, L]. Also, E[Ya | V ] = E[E[Ya | L] | V ] = E[E[Y | A = a, L] | V ]. Call E[Y | A = a, L] ≡ P (a, L). We can estimate P (a, L) using a normal regression model. This regression model gives us a predicted outcome for every subject under each treatment of interest that is a function of that subject’s value L. We now have a data set in which each subject contributes one line of data for each treatment of interest (e.g. in the case of a binary treatment, each subject contributes two lines of data). Each line of data contains the subject’s covariate values (L), a treatment (a = 0 or a = 1), and the predicted outcome given the subject’s covariate values and that treatment (P (a, L)). This is just a repeated measures data set with two outcomes measured for each subject, corresponding to the two treatments. We can pool the whole dataset and do a simple regression of Y on a and V .

12

**Introduction to dynamic treatment regimens** Take the observed data to be a collection of treatment history and covariates over time, O = ( A,<sup>¯</sup> X<sup>¯</sup> ). A dynamic treatment regime is a collection of j-specific decision rules, dj, where dj is a function of X<sup>¯</sup> (j) which assigns a treatment at time j = 0, .... We assume the consistency assumption (CA): For all (or a set containing all static treatment regimes and the dynamic treatment regimes the user is interested in) dynamic treatment regimens d<sup>¯</sup> = (dj : j = 0, ...), we assume the existence of X<sup>¯</sup> ¯d, X<sup>full</sup> = ( X<sup>¯</sup> ¯d : d<sup>¯</sup> ∈ D). Under the CA, the observed data can be represented as O = ( A,<sup>¯</sup> X<sup>¯</sup> ¯A<sup>).</sup>

We further assume the SRA: A(j)⊥X<sup>full</sup> | X<sup>¯</sup> (j), A<sup>¯</sup> (j) and a d-specific experimental treatment assignment assumption (ETA), which, informally, states that we need support in our data for this particular dynamic treatment regime d. Formally, this ETA assumption is defined as: for any<sup>¯</sup> l(j) with P ( A<sup>¯</sup> (j − 1) = d<sup>¯</sup> j(<sup>¯</sup> l(j − 1)), L<sup>¯</sup> (j) =<sup>¯</sup> l(j)) > 0, we have P ( A<sup>¯</sup> (j) = d<sup>¯</sup> j(<sup>¯</sup> l(j)), L<sup>¯</sup> (j) =<sup>¯</sup> l(j)) > 0. We can then write the G-comp formula for dynamic treatment regimes. this is the same as the previous G-comp formula, only now we set A using the first action of d(x):

P ( X<sup>¯</sup> ¯d = x¯) =<sup>�</sup> j=0<sup>P(X(j) = x(j) |X¯(j −1) =x¯(j −1),A¯(j −1) = d0(X(0)), d1( ¯X(1)), ..., dj−1( ¯X(j −1)))</sup> More to come on dynamic treatment regimes...

Estimation of G-Computation Formula for Dynamic Treatment Regimes in Point Treatment Studies, Keith Betts, September 20, 2004

Define the data structure as O = (W, A, Y ),

W −→ A −→ Y (time ordering)

The treatment regime is a function of W (where W are the baseline covariates)

A possible question of interest is if everyone in the population is assigned a rule that given their past what treatment should be, what would be the mean outcome?

---

[← Mark van der Laan](17-mark-van-der-laan.md) · [Up: contents](index.md) · [Example →](19-example.md)

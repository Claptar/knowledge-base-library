---
title: COMPUTATIONAL CONSIDERATIONS
source: https://thesis.library.caltech.edu/16062/
source_file: sources/gorin-2023-scrnaseq-foundations/gg_thesis_230602.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# COMPUTATIONAL CONSIDERATIONS

**Source:** `gg_thesis_230602.pdf` from [gorin-2023-scrnaseq-foundations](https://thesis.library.caltech.edu/16062/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **5.1 Key challenges**

The generating function procedure described in Chapter 4 offers some useful advantages: under some fairly restrictive, but physically realistic assumptions, it lets us evaluate joint and marginal distributions by computing integrals and inverse Fourier transforms. These distributions are approximate. The integrals are typically intractable and require numerical quadrature, which is computationally intensive and inexact. However, even when analytical solutions are available, some error is introduced by truncation: the probabilities are evaluated on a _𝑁_ × 𝔰1 × · · · × 𝔰 _𝑛_ grid of total size 𝔰= _𝑁_<sup>�</sup> _𝑖_<sup>𝔰</sup> _𝑖_<sup>, where each 𝔰</sup> _𝑖_<sup>is a non-negative integer that represents the</sup> species-specific grid dimension. The grid is restricted to have a total probability that sums to unity; therefore, errors arise when a significant portion of the probability mass lies outside the evaluation bound.

To obtain accurate estimates, we need a sufficiently large grid. Here, a more formidable challenge arises: if we seek the generating function for a fairly large number of species, increasing the grid grows 𝔰 exponentially in _𝑛_ . This problem grows more acute, and lowers the efficiency, when the number of cells Nc ≪ 𝔰. This limit is easy to achieve: for example, if we have _𝑁_ = 2, _𝑛_ = 3, and a very modest 𝔰 _𝑖_ = 10 for all three species, we yield 𝔰= 2 _,_ 000, which is comparable to a moderate to high-abundance cell type in a single-cell dataset. In other words, if we have Nc = 1 _,_ 000 cells, we generate 2,000 probabilities, then throw away more than half, because the computation of probabilities is coupled through the Fourier transform.

This problem is by no means restricted to generating function methods. Finite state projection also requires evaluating a grid of probabilities and discarding a large fraction of the computed values: as the observed states are coupled to non-observed ones, their probabilities are mathematically related. We are perhaps justified in saying that this problem is intrinsic to discrete distributions more broadly. Even the

49

simplest distributions on N0 implicitly require recursion:


On one hand, it is somewhat obvious that we need to multiply _𝑥_ factors to compute _𝑥_ ! or _𝑝_<sup>_𝑥_</sup> . On the other, it reflects a profoundly important statistical property: the evaluation time for the likelihood of a dataset under the Poisson model is a function of _the highest value_ , 𝔰, rather than the dataset size Nc, because we can “recycle” probabilities for any observed _𝑥<_ 𝔰. Even if Nc is small, a large 𝔰 will create problems in evaluation. From this perspective, we may reasonably say that the foundation of discrete probability was laid by Bernoulli, Poisson, and de Moivre [266], but made practical by Stirling [78] and consequent work on the approximation of special functions [188]. For the Poisson distribution,


If log Γ can be evaluated reasonably efficiently throughout its domain, this approach breaks the tyranny of recursion and removes the dependence on 𝔰.

In sum, despite the generating function methods’ advantages, they have fundamental limitations: integrals are typically intractable, and we are forced to evaluate them on a grid of spectral coordinates. In this section, we outline some strategies for implementing or bypassing these challenges.

### **5.2 Special function approximations**

This section summarizes the content of [104] by G.G. and L.P. The special function approximations were conceptualized, designed, and implemented by G.G.

As discussed in Section 4.6.2, the bivariate PMF of the bursty model is not available in closed form, because the integral in Equation 4.56 is not analytically tractable. Therefore, if we would like to evaluate this PMF, the vast majority of the computational burden involves numerically approximating this integral by quadrature.

We can eliminate quadrature altogether by approximating A( **U** (s)) = 1− _𝑏𝑈_ <u>1</u> _𝑁_<sup>−1</sup> by a series and analytically integrating the terms over (0 _,_ ∞). We have set _𝑘_ to unity with no loss of generality at steady state. This function affords the following

50

expansions:


The first line reports the Taylor expansion about −1, whereas the second reports the Laurent expansion. This choice of expansion produces an overlapping region of convergence; if we had selected, for instance, the simpler Taylor expansion �∞n=0<sup>(</sup><sup>_𝑏𝑈𝑁_)n,integralsuptossuchthat|</sup><sup>_𝑏𝑈𝑁_(</sup><sup>**u**</sup><sup>_,_s)|=1woulddiverge.</sup> We choose 𝔲= 21 _𝑏_<sup>(1 +</sup> √3) as the | _𝑈𝑁_ | threshold for switching from the inner Taylor approximation to the outer Laurent approximation, as it maximizes the distance from the bounds of the region of convergence for non-positive complex **u** (Figure 5.1a).

All positive and negative integer powers of _𝑈𝑁_ have closed-form antiderivatives. We can exploit this property as follows. First, we compute all threshold values of s such that | _𝑈𝑁_ ( **u** _,_ s)| = 𝔲 using numerical root-finding. Next, we partition the domain s ∈[0 _,_ ∞) into disjoint sets of intervals {S<sup>_𝑇_</sup> } and {S<sup>_𝐿_</sup> }, such that | _𝑈𝑁_ ( **u** _,_ s)| _<_ 𝔲 ∀ s ∈ S<sup>_𝑇_</sup> and | _𝑈𝑁_ ( **u** _,_ s)| ≥ 𝔲 ∀ s ∈ S<sup>_𝐿_</sup> . The form of _𝑈𝑁_ guarantees that there is are at most two domains in each set, and at least one Taylor domain S<sup>_𝑇_</sup> .

Next, we calculate the antiderivatives of the powers of _𝑈𝑁_ . For _𝛽_ = _𝛾_ , we find


Per Equation 3.18, _𝑇_ n can be computed by an sum of elementary functions. Similarly, _𝐿_ n can be computed by the sum of a single exponential integral and several elementary functions.

51

For the non-degenerate case _𝛽_ ≠ _𝛾_ , we find


Per Equation 3.21, _𝑇𝑛_ can be computed by a sum of elementary functions. Such a decomposition is not available for _𝐿𝑛_ . For completeness, we note that the antiderivatives in Equations 5.4 and 5.5 are not well-defined when _𝑢𝑀_ = 0, which is the trivial negative binomial case that does not require approximation.

Next, we truncate the summation in Equation 5.3 to upper limits N _𝑇_ and N _𝐿_ and compute the weights of each _𝑈𝑁_<sup>nterm:</sup>


Next, we obtain the approximations for the intervals:


As shown in Figure 5.1b, even low-order approximations can accurately recapitulate distribution shapes. To quantify the performance as a function of approximation order, we used a variant of the Kolmogorov-Smirnov distance. As the generating function is not guaranteed to produce a true PMF, probabilities can be negative and this distance can exceed 1. We find that the error is largely controlled by the Taylor approximation order (Figure 5.1c), whereas the runtime is largely controlled by the Laurent approximation order (Figure 5.1d). By decreasing the Laurent order and increasing the Taylor order, we can improve the time performance while keeping the error fairly low.

52


Figure 5.1: The special function approximation procedure for the two-species bursty model.

**a.** Taylor and Laurent approximation criterion (orange: approximations’ common region of convergence; purple: threshold value of | _𝑈𝑁_ |). **b.** Comparison of marginal mature copy number distributions for a range of approximation orders (#, # tuple and plot location: Laurent and Taylor approximation order; gray: histogram from 10<sup>5</sup> stochastic simulations; red line: distribution calculated from approximation; _𝑏_ = 19, _𝛽_ = _𝛾_ = 0 _._ 4).

**c.** Kolmogorov-Smirnov error between quadrature- and expansion-based joint distributions for 2,500 _𝛽_ = _𝛾_ parameter sets on a uniform grid with log10 _𝑏_ ∈[0 _._ 1 _,_ 2] and log10 _𝛾_ ∈[−1 _,_ 1], calculated for combinations of Taylor and Laurent orders up to 7 (black point: single parameter set; uniform jitter added).

**d.** Runtimes to compute approximations in **c** (black point: single parameter set computed using expansions; orange point: single parameter set computed using numerical quadrature; uniform jitter added).

53

As it stands, this approach is unsuited for large-scale computation. The method essentially substitutes integration with the calculation of special functions, which is helpful if these special functions can be easily approximated. We developed a bespoke algorithm for the exponential integral to implement the degenerate case _𝛽_ = _𝛾_ case, and did not implement the _𝛽_ ≠ _𝛾_ case. It appears unlikely that useful approximations are forthcoming for the considerably more complicated hypergeometric function. In addition, in spite of runtime improvements, the procedure inherits the usual reliance on dense grid sampling (Section 5.1).

Nevertheless, the mathematical approach has some useful lessons for the development of solvers. With extensive prior understanding of the behaviors of functions and distributions, it is possible to develop approximators that take advantage of their properties, optimizing for features of interest while discarding others. These approximators do not generalize, and require considerable up-front work, but can outperform more naïve approaches for certain purposes.

### **5.3 Neural approximations**

This section summarizes the content of [111] by G.G.<sup>_★_</sup> , M.C.<sup>_★_</sup> , T.C., and L.P. The MMNB and KWR approximations were conceptualized and designed by G.G. The nnNB approximation was conceptualized by G.G. and designed by M.C. The DR approximation was conceptualized and designed by M.C. All approximations were implemented by M.C. The quadrature methods were designed and implemented by G.G.

We apply these lessons to develop a solver that bypasses the grid evaluation procedure, taking inspiration from the discussion of the Stirling approximation in Section 5.1 to develop an approximator for the bursty system (Section 4.6.2). First, we recall that the nascent RNA distribution _𝑃_ ( _𝑥𝑁_ ) is negative binomial. To compute the probability of a given microstate, we can apply the definition of conditional probability to find _𝑃_ ( _𝑥𝑀, 𝑥𝑁_ ) = _𝑃_ ( _𝑥𝑁_ ) _𝑃_ ( _𝑥𝑀_ | _𝑥𝑁_ ).

This conditional is, of course, not available in closed form. Nevertheless, we have a qualitative understanding of its properties: _𝑃_ ( _𝑥𝑀_ | _𝑥𝑁_ ) is unimodal, overdispersed relative to Poisson, and supported on N0. Thus, we may be able to construct an approximation _𝑃_<sup>ˆ</sup> ( _𝑥𝑀_ ; Θ<sup>ˆ</sup> ) ≈ _𝑃_ ( _𝑥𝑀_ | _𝑥𝑁_ ). To ensure that _𝑃_<sup>ˆ</sup> is in a reasonable class of approximators, we require it to have the qualitative properties of _𝑃_ ( _𝑥𝑀_ | _𝑥𝑁_ ). To ensure that it improves the computational tractability of the problem, we require that it be a closed-form parametric distribution that can be computed in a non-recursive way for any _𝑥𝑀_ . The challenge is, then, to construct such a _𝑃_<sup>ˆ</sup> and to produce a

54

mapping from Θ = { _𝑥𝑁 , 𝑏, 𝛽, 𝛾_ } to Θ<sup>ˆ</sup> .

The most obvious candidate for an approximator is _𝑃_<sup>ˆ</sup> = _𝑃_ NB, which has the correct distributional support and shape. It remains to specify the map F : Θ → Θ<sup>ˆ</sup> . The conditional moments of the system are intractable. However, we know that those of the bivariate lognormal distribution _are_ tractable; this five-parameter law (Equation 3.29) can be specified by defining the expectations, variances, and correlation of the two dimensions (Equations 3.27 and 3.30). If we proceed in this direction, we find that the conditional distribution is given by Equation 3.31, which is not defined at _𝑦_ 1 = 0 but produces a finite value elsewhere. Therefore, by noting that the lognormal distribution is unimodal, right-skewed, and has a strictly positive support, we can, in principle, obtain a moment-matched negative binomial (MMNB) approximation for the conditional distribution:


First, we compute the parameters for the approximating bivariate lognormal distribution by applying Equations 3.27 and 3.30 to the moments in Table 4.1. Given this law, we compute the parameters ( ˆ _𝜇𝑙_ and _𝜎_ ˆ _𝑙_ ) and moments ( ˆ _𝜇_ and _𝜎_ ˆ ) of the conditional lognormal distribution at _𝑦_ 1 = _𝑥𝑀_ + 1 using Equations 3.31 and 3.26. We shift the argument to ensure the conditional is well-defined for _𝑥𝑀_ = 0. Next, we calculate the shape parameter _𝜈_ ˆ using the following identity:


To ensure the approximating conditional distribution is well-defined, we use Equation 5.8 only when _𝜈_ ˆ only when _𝜎_ ˆ<sup>2</sup> _> 𝜇_ ˆ; otherwise, we fall back to


This procedure comprises the function F used to convert _𝑥𝑁_ and biophysical parameters to the parameters of the approximating distribution.

With this coarse approximation, we can produce PMFs that roughly recapitulate the qualitative properties of the true PMF. The probabilities so obtained are unsuited to the computation of data likelihoods. Taking a broader view, we are part of the way to a usable approximation. It seems reasonable to suppose that we can get further by making minor corrections to the MMNB procedure.

Neural networks are good function approximators, and have previously been used to summarize the dynamics of physical systems [47, 179]. We take inspiration

55

from this approach to propose two improvements. First, we can use the procedure described above, correcting the conditional lognormal moments _𝜇_ ˆ and _𝜎_ ˆ<sup>2</sup> :


where _𝑠_ 1 _, 𝑠_ 2 ∈(0 _,_ 1) are variables output by a neural network function F of Θ, whereas _𝐶_ 1 and _𝐶_ 2 are global (Θ-independent) scaling factors learned by the network. The corrected parameters _𝜇_ ˆ<sup>∗</sup> and _𝜎_ ˆ<sup>∗</sup> so computed can be transformed into _𝜈_ ˆ<sup>∗</sup> using Equation 5.9, then substituted into Equations 5.8 and 5.10 to obtain probability estimates. By generating high-quality conditional distributions from a standard quadrature procedure, and updating F , _𝐶_ 1 and _𝐶_ 2, we can produce a finer approximation to the true PMF. To train the network, we optimize the KLD between conditional distributions. These distributions are defined for all _𝑥𝑀_ ∈ N0, so we truncate them at 𝔰 _𝑀_ = _𝜇𝑀_ +4 _𝜎𝑀_ and normalize to yield strictly positive divergences. This is the neural network negative binomial (nnNB) procedure. The resulting approximations are fairly close to the true distributions, and can be improved further by tuning the neural network.

The nnNB procedure has the desired qualitative and statistical properties: it produces overdispersed bivariate distributions that bypass the Fourier grid evaluation. With a pre-trained network, to obtain the approximate likelihood _𝑃_<sup>ˆ</sup> ( _𝑥𝑁 , 𝑥𝑀_ ) for a parameter set { _𝑏, 𝛽, 𝛾_ }, we need to calculate F only once. Nevertheless, the true conditionals are not negative binomial, and we can achieve better quantitative agreement by generalizing the approximator while retaining its key computational features.

To develop a better approximator, we note that finite Poisson and negative binomial mixtures can also be easily computed in a non-recursive fashion. In other words, we can propose the following functional form:


This approach essentially approximates the true distribution by a weighted sum of basis functions, or kernels of the appropriate functional form. It remains to specify or learn the weights and distributional parameters of these kernels. The Nessie framework [271], seeking to fit fairly complicated univariate distributions, learns all

56

of these parameters simultaneously. However, as we have some qualitative insights into the distribution shape, we can simplify the procedure by judiciously placing the kernels. To improve performance in the high-probability regions, we place the approximators at the Chebyshev nodes of the lognormal quantile function _𝐹_<sup>−1</sup> (Equation 3.28):


where the conditional lognormal _𝜇_ ˆ _𝑙_ and _𝜎_ ˆ _𝑙_ are obtained as in the MMNB procedure. Usefully, Φ<sup>−1</sup> ( _𝑝_ n) need only be computed once. Knowing that _𝑃_<sup>ˆ</sup> should be unimodal, we control the standard deviation of each kernel _𝜎_ ˆ n<sup>∗by the spacing between</sup> adjacent kernels:


where _𝑠_ ∈(0 _,_ 1) is output by a neural function, _𝐶_ 1 = 1, and _𝐶_ 2 = 5. We somewhat arbitrarily set _𝜎_ ˆ N<sup>∗to</sup> ~~√~~ _𝜇_ ˆN, meaning the Nth kernel is Poisson. Therefore, we can effectively approximate distributions by training a neural network function F of Θ, which outputs the weights _𝑤_ 1 _, . . . , 𝑤_ N _, 𝑐𝜎_ , precisely as in the nnNB case. This is the kernel weight regression (KWR) procedure.

In sum, by judiciously constructing kernel functions, then combining them using weights from a pre-trained neural network function, we can approximate conditional distributions for an intractable PMF (Figure 5.2a). To evaluate likelihoods, we can combine these conditional distributions with marginal distributions (Figure 5.2b). We used an adaptive quadrature generating function method as our training data and ground truth (QV20, evaluated using 𝔰 _𝑖_ = _𝜇𝑖_ + 20 _𝜎𝑖_ and truncated to _𝜇𝑖_ + 4 _𝜎𝑖_ for benchmarking). The accuracy of the KWR approximator was comparable to that of practical generating function methods (QV10, QV4, and FQ, or order-60 Gaussian quadrature), with runtimes per 𝔰 comparable to FQ. We additionally trained a direct regression (DR) method, which uses a neural function to map from _𝑥𝑁 , 𝑥𝑀, 𝑏, 𝛽, 𝛾_ to _𝑃_<sup>ˆ</sup> ( _𝑥𝑁 , 𝑥𝑀_ ), in the spirit of [310]; at comparable neural network sizes, this approach yielded fairly poor performance. The differences are evident by inspection of reconstructed distributions: KWR and nnNB produce fair matches to ground truth, MMNB recapitulates the rough distribution shape, and DR suffers from extreme distortions (Figure 5.2d). Comparisons using a non-𝔰-normalized metric confirm these results: KWR produces results far better than a random- _𝑤_ n control and generally better than the other approximation strategies.

57


Figure 5.2: The neural network approximation procedure for the two-species bursty model.

**a.** Univariate conditional distributions are approximated by summing a set of kernel functions with neural network-learned weights (red dashed line: approximation; black line: ground truth distribution).

**b.** Bivariate distributions are reconstructed by multiplying conditional mature RNA probabilities by marginal nascent RNA probabilities (red dashed lines: approximations; black lines: ground truth distributions; heatmap: bivariate probability mass function, lighter is higher probability).

**c.** Runtime and accuracy of predictions, both normalized by grid size, for 256 test parameter sets, comparing three generating function-based methods (QV10, QV4, and FQ), direct regression (DR), the moment-matched negative binomial (MMNB) approximation, and kernel weight regression (KWR) to ground truth (QV20). **d.** Typical distributions obtained by generating function inversion (QV20, leftmost column, ground truth) and various approximation methods.

**e.** Non-normalized grid reconstruction accuracy for 768 test parameter sets.

This approach appears to be quite promising and generalizable: given some prior knowledge distribution shapes, we can design a coarse approximation that exhibits the correct qualitative properties, then augment it with a neural correction. It is unlikely that this approach can generalize to arbitrary distributional dimensionality _𝑛_ : we are still constrained by generating high-quality training data, and the high- _𝑛_ cases require simulation. Nevertheless, some relevant classes of models appear to be immediately tractable. For example, although the case of _𝑛_ = 1 and _𝑁_ = 2 can produce bimodal distributions, the conditionals with respect to _𝑠_ are typically unimodal, suggesting the approximation


58

As it stands, the design advantages of the neural network procedures are essential for variational inference, where each cell c may have a different set of biological parameters and evaluating Nc Fourier transforms is impractical (Section 10.3). Even when the cells’ copy number distributions are assumed to be identical, the procedure provides more stable likelihood functions. Due to the truncation implicit in defining data-based 𝔰 _𝑖_ for generating function evaluation, parameter sets far from the optimum, with a large fraction of probability mass outside this bound, will produce artificially inflated likelihoods.

Nevertheless, we do not yet use the KWR solver to fit parameters when FQ is practical, for three reasons. First, likelihood inflation is a minor problem for parameter inference: method of moments estimates typically place us quite near the likelihood optimum. Second, FQ empirically shows a runtime advantage when the grid sizes are fairly small. Third, the neural approach does not allow us to easily integrate technical noise phenomena; to represent, e.g., the loss of molecules in the sequencing process, we need to retrain the network. For the Bernoulli noise model, we can partially exploit the statistical properties of distributions to forego designing a new solver. For example, the retention probabilities of nascent and mature molecules _𝑝𝑁_ and _𝑝 𝑀_ are identical, we can directly use the neural solvers with _𝑏_ rescaled by _𝑝𝑁_ to evaluate distributions. We can similarly adapt the nnNB procedure when _𝑝 𝑀 < 𝑝𝑁_ , which amounts to computing the nascent marginal and conditional approximator for burst size _𝑏𝑝𝑁_ , then weighing the conditional negative binomial scale parameter by _𝑝 𝑀_ / _𝑝𝑁_ . However, this approach does not generalize to other noise behaviors, and considerable further work is necessary to implement them.

### **<u>5.4</u>** **_<u>Monod</u>_**

This section summarizes the supplementary content of [107] and [106] by G.G. and L.P. The method was conceptualized, designed, and implemented by G.G.

If we operate with bivariate data and assume that observations are independent and arise from a common distribution, it is by far easiest to numerically integrate generating functions. To this end, we developed _Monod_ , a Python package for the inference of biophysical parameters.

At its heart, _Monod_ is a wrapper around a _SciPy_ L-BFGS-B optimizer [302]. To find the optimal parameters for a particular gene, we minimize the divergence between proposed distributions and observations. We calculate bivariate theoretical distributions by applying the inverse Fourier transform method described in [31,

59

261]. Specifically, we define a grid of _𝑔𝑁_ and _𝑔𝑀_ , such that


where _𝑖_ denotes the unit imaginary number. Next, we define the matrix _𝐺 𝑗𝑘_ , such that


where the function _𝐺_ ( _𝑢𝑁 , 𝑢𝑀_ ) is the distribution’s generating function. To approximate the PMF on a 𝔰 _𝑁_ × 𝔰 _𝑀_ grid, we compute the inverse real fast Fourier transform of the matrix _𝐺_ :


We use this form of the transform and truncate 𝔰 _𝑀_ for evaluation because a probability mass function is a real-valued signal with a Hermitian Fourier transform [31].

To find the closed-form generating functions, we directly evaluate them. To find the generating functions only available in integral form, we use order-60 Gaussian quadrature [302] up to the upper bound


this scaling ensures all reactions have equilibrated.

Once we have a proposed distribution _𝑃_ , we optimize the Kullback-Leibler divergence (Equation 3.49) to obtain a point estimate of the biological parameters. To simplify this procedure, we begin at the method of moments estimate, if available. For numerical stability, we use the log10 versions of the parameters.

The usual bursty transcription model (Section 4.6.2) has three biological parameters per gene, which can be fit using the procedure outlined above. However, we would also like to learn the technical noise parameters, such as _𝜆𝑁_ and _𝜆𝑀_ for the Poisson sequencing model (Section 4.6.4). The evaluation of the generating function under this model amounts to applying Equation 4.62.

A naïve approach to this problem is typically futile: if we separately fit _𝑏_ , _𝛽_ , _𝛾_ , _𝜆𝑁_ , _𝜆𝑀_ for each gene, the parameters turn out to be poorly distinguishable. However, we can use a physical argument to simplify the problem. _𝜆𝑁_ and _𝜆𝑀_ are _chemical_ ,

60

not biological parameters; we can reasonably suppose that they only depend on the extant molecules’ properties, rather than obscure biological factors. Therefore, we make the simplest nontrivial assumption that mature molecules are all alike (i.e., have the same _𝜆𝑀,_ g = _𝜆𝑀_ ), whereas the sequencing of nascent molecules is largely controlled by the overall gene length _𝐿_ g (i.e., _𝜆𝑁,_ g = _𝐿_ g _𝐶𝑁_ ). Although this model is fairly crude, it turns out to produce apparently reasonable biological parameter trends (Section 8.2) and provides a foundation for constructing and testing more sophisticated hypotheses.

It remains to simultaneously obtain estimates of parameters


such that the dataset likelihood is maximized. Formally, this is an optimization problem in 3Ng + 2 dimensions. Even if we assume the cell population is comprised of independent samples from a common distribution, the problem is not only intractable, but underspecified, and we need to make two assumptions to make inference practical.

Although the bursty model provides us with a way to evaluate the likelihood of the data Dg for a particular gene, we formally need to optimize the KLD for a 2Ng-dimensional distribution that encodes potential patterns of co-regulation. In other words, if we independently fit each gene’s data, we are intrinsically unable to reproduce correlations between between genes, because those correlations are not part of the model. In Section 10.1, we take the first tentative theoretical steps toward filling this lacuna. However, in the _Monod_ implementation, we sacrifice the gene–gene relationships in favor of tractability.

Even under this implicit assumption of biological gene–gene independence, we retain coupling through the two technical noise parameters _𝐶𝑁_ and _𝜆𝑀_ , which control all genes’ likelihoods, and need to be fit simultaneously with the biological parameters (Equation 5.20). Therefore, we adopt the following schema, which is reminiscent of coordinate descent. We iterate over values of Θ _𝑡_ on a grid. For a given set of Θ _𝑡_ , we independently obtain gene-specific estimates Θ<sup>ˆ</sup> g, i.e., solve Ng relatively simple three-dimensional optimization problems. We store the resulting

61

parameter optima Θ<sup>ˆ</sup> _𝑔_ (Θ _𝑡_ ). Next, we assign


where _𝑃_ (Θ<sup>ˆ</sup> _𝑔_ (Θ _𝑡_ )) is the model probability distribution under parameters Θ<sup>ˆ</sup> _𝑔_ (Θ _𝑡_ ). In other words, whichever Θ _𝑡_ produces the lowest overall divergence is our optimum.

Although this approach is somewhat _ad hoc_ , it provides certain advantages. For example, we can perform goodness-of-fit testing to focus on genes that fairly well recapitulate the data distributions. If we had simultaneously optimized all entries of Θ<sup>ˆ</sup> , we would need to re-run the optimization to account for the removal of some of the data. _Monod_ uses three criteria for goodness-of-fit testing. First, we remove all genes whose parameters are near the search bounds, which usually represent failure to converge, excessive data sparsity, or model misspecification. Although these parameters may recapitulate distributions fairly well, they cannot be easily interpreted. Second, we remove all genes which simultaneously exceed pre-set chi-squared and Hellinger distance bounds, i.e., have unlikely and high-magnitude deviations from the proposed distribution. Typically, some 10% of the genes are discarded under the bursty model, upward of 50% under the extrinsic model, and nearly all under the constitutive model.

In addition, _Monod_ allows the computation of uncertainties in Θ<sup>ˆ</sup> g. To bypass the problem of degeneracy with respect to the technical noise parameters, we compute these uncertainties conditional on the value of Θ<sup>ˆ</sup> _𝑡_ . The uncertainties so derived are necessarily underestimates. Specifically, we use an approach based on the Fisher information matrix (FIM). Given a set of inferred parameters Θ<sup>ˆ</sup> g, the Fisher information matrix I is given by the Hessian of the Kullback-Leibler divergence:


where _𝑖_ and _𝑗_ index over the inferred parameters log10 _𝑏_ , log10 _𝛽_ , and log10 _𝛾_ [312]. The standard deviation of parameter _𝑖_ can be obtained from the diagonal entries of the inverse of the FIM:


With these standard deviations, we use the _𝑧_ -score to estimate 99% confidence intervals as 2 _._ 576 _𝜎𝑖_ [208].

62

Given a set of fits, we can compare biological and technical noise parameters for cell populations. This procedure is somewhat limited by the precision of the inferred technical noise parameters, which are degenerate with respect to the burst size. However, we can make some progress by operating with matched samples. For example, if two cell populations are cell types collected in a single experiment, it appears reasonable to suppose they should have the same Θ _𝑡_ , and any differences are purely biological, on the level of Θg. If we, in addition, strongly believe that the biological differences should be restricted to a handful of genes, rather than genome-wide, we can further “correct” inferred parameter values by subtracting any inter-dataset biases. We take this approach in Chapter 9. On the other hand, if they represent the same tissue processed using two different technologies, it seems reasonable to propose the Θg are identical, whereas Θ _𝑡_ are different. We take this approach in Sections 8.3 and 8.4.

Although these procedures allow us to analyze data and draw interesting conclusions regarding the chemical and biophysical bases of transcriptome differences, the fits are only meaningful if the data meet the fairly restrictive assumptions of the model. For example, _Monod_ does not include the encapsulation phenomena described in Section 4.4.2 or cell type heterogeneity. To account for the former, we remove all low-copy number barcodes, typically by the combination of the _bustools_ filter [197] and knee plot thresholds. To account for the latter, we use two approaches. In the simplest one, we adopt the “marker gene” hypothesis, which supposes that intra-sample cell type differences can largely be attributed to a small number of genes, fit the datasets, and use goodness-of-fit testing to remove poorly fit genes _post hoc_ . In the slightly more sophisticated one, we use pre-existing annotations to fit cell types separately. However, all of these methods represent uncomfortable compromises, and a truly comprehensive methodology should simultaneously and probabilistically account for the biological and technical effects.

To ensure the fits are informative, we further restrict our analysis to a relatively small set of genes with at least modest expression of both nascent and mature transcripts. In addition, we remove genes with excessive expression, as their likelihoods are numerically challenging to compute. This procedure typically retains several thousand genes. When we are interested in making comparisons between datasets, we restrict analysis to the genes that pass this filter in as many datasets as possible.

63

### **5.5 Simulations**

In addition to numerically evaluating distributions, we frequently need to simulate from stochastic systems. In the context of data analysis, simulation provides us with a fully characterized ground truth for benchmarking various data transformations. However, this approach may be overly simplistic, as the simulation may not accurately represent all features of the underlying data-generating process. In the context of model development, simulations allow us to ensure that analytical or numerical solutions are correct.

The former use case is typically fairly straightforward. If we would like to generate realizations from a Markovian system with a particular set of physical phenomena, we either use a version of Gillespie’s stochastic simulation algorithm (SSA) [98, 99] or sample directly from a numerically tractable PMF. If we seek to include other phenomena, we augment the simulator appropriately. For example, if we are interested in generating an observation from a system with cell type heterogeneity, we define cell type-specific parameters, randomly select a cell type, then generate a microstate, or molecular copy number, under the relevant parameters. Although the simulation of such Markovian systems is by no means trivial, it is well-understood, and we do not cover it in any further detail here. Instead, we report two algorithms for the exact stochastic simulation of non-Markovian systems, used to validate their numerical solutions.

### **<u>5.5.1 Review of the SSA</u>**

This section extends a portion of [114] by G.G., S.Y., and L.P. The outline was written by S.Y. and G.G.

The Markovian SSA for a system with time-independent parameters takes the following form:

1. Initialize the system at time _𝑡_ = _𝑡_ 0 and state **x** = **x**<sup>0</sup> .

2. Compute the instantaneous reaction rates of the _𝜇_ th reaction, _𝜙𝜇_ ( **x** ) and the net state efflux rate, _𝜙_ ( **x** ) =<sup>�</sup> _𝜇_<sup>_𝜙_</sup> _𝜇_<sup>(</sup><sup>**x**).</sup>

3. Generate _𝑢_ 1 and _𝑢_ 2, random variables uniformly distributed over (0 _,_ 1).

4. Transform _𝑢_ 1 to obtain the exponentially distributed residence time Δ _𝑡_ = − <u>1</u> _𝜙_ ( **x** )<sup>log</sup><sup>_𝑢_1.</sup>

- _<u>𝜙𝑘</u>_ <u>(</u> **x** <u>)</u>

- 5. Use _𝑢_ 2 to compute the reaction index _𝜇_ , such that<sup>�</sup> _𝑘_<sup>_𝜇_</sup> =<sup>−</sup> 1<sup>1</sup> _𝜙_ ( **x** ) _< 𝑢_ 2 ≤ � _𝑘𝜇_ =1 _<u>𝜙𝜙𝑘</u>_ (( **xx** ))<sup>.</sup>

6. Advance system to time _𝑡_ ← _𝑡_ + Δ _𝑡_ and state **x** ← **x** + Δ **x** _𝜇_ .

64

### 7. Return to step 2 or terminate simulation.

The instantaneous propensity function for zero-order reactions, such as ∅ −→X _𝑐 𝑖_ , is _𝜙𝜇_ ( **x** ) = _𝑐_ , a constant. The propensity function for first-order reactions, such as X _𝑖_ −→∅ _𝑐_ , is _𝜙𝜇_ ( **x** ) = _𝑐𝑥𝑖_ . Higher-order propensity functions are reported in Table 2.1 of [299].

The update vector Δ **x** _𝜇_ consists of the entries of the stoichiometry matrix corresponding to reaction _𝜇_ . This quantity can be random; for example, to simulate the bursty system in Section 4.6.2, we would generate a realization of the geometric distribution with mean _𝑏_ whenever a transcriptional event occurs, and add it to _𝑥𝑖_ . In addition, a stochastic burst size can be easily made time-dependent. However, time dependence in reaction rates, as well as non-Markovian dynamics, require slightly more elaborate adjustments.

### **5.5.2 SDE–CME systems**

This section summarizes a portion of the supplement of [113] by G.G.<sup>∗</sup> , J.J.V.<sup>∗</sup> , M.F., and L.P. The method was conceptualized, designed, and implemented by G.G.

Hybrid continuous–discrete stochastic systems (with _𝑛, 𝑚>_ 0 and _𝐶_<sup>_𝑐𝑑_</sup> ≠ 0) are popular for representing extrinsic variability in reaction rates, such as time-varying environments. However, in general, the simulation of these systems requires approximate schema. The computation of propensities in Section 5.5.1 belies the fact that the more fundamental variable is the flux _𝜙_ ( **x** _, 𝑡_<sup>∗</sup> ):


where the first equality holds generally [227], whereas the second holds only if all _𝜙𝜇_ are time-independent. To compute Δ _𝑡_ if _𝜙𝜇_ is time-dependent, we typically need to use a numerical solver to find the root Δ _𝑡_ where the first line of Equation 5.24 holds. Finally, the reaction index _𝜇_ is drawn from the appropriate categorical

65

### distribution, such that


This task is particularly challenging when rates are time-dependent in a stochastic fashion. For example, Brownian motion is fractal, and does not afford exact roots. Therefore, a system with a Brownian motion component must be solved by sampling the process on a grid, then using interpolation to approximate fluxes [254, 305]. This may lead to errors if the grid is insufficiently fine, or excessive evaluation times if it is too fine.

Curiously, certain non-Brownian extrinsic noise sources do afford exact simulation routines. Specifically, if the stochastic driver _𝑦𝑡_ = _𝑦_ ( _𝑡_ ) is a jump Ornstein– Uhlenbeck process, it has a non-fractal, fully specified structure [43, 57]:


such that N( _𝑡_ ) is a Poisson random variable with mean _𝑎𝑡_ . { _𝐵𝑘_ } is a set of independent and identically distributed realizations of the positive-valued random variable _𝐵_ . This process has the exact solution [241]


where _𝑡𝑘_ are the arrival times of N( _𝑡_ ). To account for the initial condition, we set _𝑡_ 0 = 0 and _𝐵_ 0 = _𝑦_ 0. This class of processes has been exhaustively studied by Barndorff-Nielsen and colleagues in the context of mathematical finance [21, 22].

To generate a single realization of the arrival process on [0 _,𝑇_ ], we draw a Poisson random variable N( _𝑇_ ) with mean _𝑎𝑇_ . To generate the jump times, we draw N( _𝑇_ ) uniform random variables on [0 _,𝑇_ ] and sort them. To generate the jump sizes, we draw N( _𝑇_ ) random variables from the jump distribution. Equation 5.27 immediately yields the time-dependent trajectory _𝑦𝑡_ .

66

If _𝑦𝑡_ drives a transcription process, such that the production of some species _𝑥𝑖_ occurs at the rate _𝑦𝑡_ , the instantaneous propensity of this reaction is simply _𝜙𝑦_ ( **x** _, 𝑡_ ) = _𝑦𝑡_ . Usefully, we can integrate it:


where _𝑡𝑘 < 𝑡_ but _𝑡𝑘_ +1 ≥ _𝑡_ , if one exists. This identity holds because no arrivals take place between _𝑡𝑘_ and _𝑡𝑘_ +1: in this region, the dynamics of _𝑦𝑡_ are a simple deterministic exponential decay. Therefore, we can immediately compute Φ _𝑦_ ( _𝑡𝑘_ ) for all _𝑘_ .

Therefore, to simulate the system, we need to solve the following equation:


where the second line holds because we have assumed all but one of the reactions have time-independent propensities.

First, suppose that _𝑡> 𝑡𝑘_ for all _𝑘_ . In this case, we need to solve the following root-finding problem:


which has an analytical solution in terms of the Lambert W function (Equation 3.23):


67

In the nontrivial case, we use the pre-computed values of Φ _𝑦_ to bound Δ _𝑡_ . Specifically, we find the highest _𝑘_ such that


We immediately find that Δ _𝑡_ = _𝑡𝑘_ − _𝑡_ + Δ _𝑡_<sup>∗</sup> . Δ _𝑡_<sup>∗</sup> is the waiting time between _𝑡𝑘_ and the reaction firing time, and is computed analogously to Equation 5.31:


In other words, the deterministic behavior of the trajectories between jump arrivals events allows us to pre-compute and constrain the reaction times. Once we know the region where the reaction time lies, computing it is as simple as subtracting the total flux up to the jump arrival time (the correction to _𝐶_ 3 in Equation 5.33) and solving a root-finding problem using a special function. The reaction index is then selected according to Equation 5.25, with


Attention must be paid to certain edge cases, as well as the numerical stability of the _𝑊_ calculation. However, overall, this approach provides a generalizable, exact strategy for simulating discrete processes driven by a jump Ornstein–Uhlenbeck process, and can be applied to a broad variety of systems that are not tractable by analytical approaches.

### **5.5.3 Delay master equations**

This section summarizes a portion of [114] by G.G., S.Y., and L.P. The method was conceptualized, designed, and implemented for the case of deterministically delayed degradation by S.Y. and extended to the case of arbitrary delayed degradation and interconversion by G.G. The outline was written by S.Y. and G.G.

To adapt the procedure in Section 5.5.1 to the case of non-Markovian degradation

68

and interconversion, we make the following adjustments.

The first modification treats removal events of delayed species, i.e, transcripts that undergo reactions with non-exponential waiting times. Two empty queues are initialized: one for times and one for reaction indices. Then, if the reaction index generated in step 5 is the creation of a delayed species, the queues are populated with the time and reaction index of the removal of that species. This time is simply _𝑡_ + Δ _𝑡_ , where Δ _𝑡_ is drawn from any distribution on R+. If the system is initialized with delayed species, the queues of times and reaction indices must be pre-defined accordingly. For simplicity, we always assume that existing delayed species were created at _𝑡_ = 0.

The second modification alters the calculation of flux, specifically accounting for the contributions of species that don’t yet exist, but will after some delay. The total flux, _𝜙_ ( **x** ), is computed at each queued reaction event, producing a monotonically increasing, piecewise linear function of Δ _𝑡_ . Then, the residence time corresponding to the random flux generated by − log _𝑢_ 1 is found analytically. The computation of the residence time is essentially equivalent to the direct method outlined in [39], and amounts to linear interpolation between the arrival times of queued reactions.

The third modification ensures that all reactions happen in the correct order. After step 5, the reaction time and event are stored, and before advancing the system in step 6, all queued reactions that are to happen before the stored reaction event are sequentially applied and stored. The resulting ordered list is then converted into system times and states.

69

_C h a p t e r 6_

---

[← STOCHASTIC MODELS AND SOLUTIONS](11-stochastic-models-and-solutions.md) · [Up: contents](index.md) · [SNAPSHOT INFERENCE →](13-snapshot-inference.md)

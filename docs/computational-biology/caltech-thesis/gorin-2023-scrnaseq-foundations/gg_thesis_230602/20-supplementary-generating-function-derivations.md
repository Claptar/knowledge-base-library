---
title: SUPPLEMENTARY GENERATING FUNCTION DERIVATIONS
source: https://thesis.library.caltech.edu/16062/
source_file: sources/gorin-2023-scrnaseq-foundations/gg_thesis_230602.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# SUPPLEMENTARY GENERATING FUNCTION DERIVATIONS

**Source:** `gg_thesis_230602.pdf` from [gorin-2023-scrnaseq-foundations](https://thesis.library.caltech.edu/16062/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Most of this appendix summarizes the mathematical machinery outlined in the supplement to [115] by G.G., J.J.V., and L.P. G.G. developed this approach as a generalization of the framework constructed by G.G. and J.J.V. in [113] by G.G.<sup>∗</sup> , J.J.V.<sup>∗</sup> , M.F., and L.P., as well as by J.J.V. in [299], among other publications. The description was written by G.G. and J.J.V.

Section A.8.2 was adapted by G.G. from a derivation by J.J.V. and G.G. in [113] by G.G.<sup>∗</sup> , J.J.V.<sup>∗</sup> , M.F., and L.P.

Section A.8.3.1 was adapted from [105] by G.G. and L.P. The derivation was performed by G.G.

187

### **A.1 The full master equation**

The full master equation for each _𝑠_ takes the following form:


We annotate the terms in Table A.1, eliding the arguments that do not explicitly appear in the reactions.

To convert the master equation into a partial differential equation, we need to enumerate the functional forms of master equations terms and their generating functions. We begin with the definition of the generating function at time _𝑡_ . In the current derivation, whenever the argument of _𝑃_ is not explicitly specified, it consists

188


Table A.1: Components of the full master equation.

of _𝑠_ , **x** , and **y** . Analogously, whenever the argument of _𝐺_ is not explicitly specified, it consists of _𝑠_ , **g** , and **h** .


Evidently, the generating function of all terms in Equation A.1 that scale as _𝑃_ is _𝐺_ .

### **A.2 Fully discrete master equation terms**

Multiplying _𝐺_ through by _𝑔𝑖_ , we obtain:


Thisfollowsfromrewriting<sup>�∞</sup> _𝑥𝑖_ =0<sup>_𝑔_</sup> _𝑖_<sup>_𝑥𝑖_+1</sup> _𝑃_ ( _𝑥𝑖_ ) as<sup>�∞</sup> _𝑥𝑖_ =−1<sup>_𝑔_</sup> _𝑖_<sup>_𝑥𝑖_+1</sup> _𝑃_ ( _𝑥𝑖_ ), notingthat _𝑃_ ( _𝑥𝑖_ ) = 0 whenever _𝑥𝑖 <_ 0, and reindexing to obtain the equivalent sum<sup>�∞</sup> _𝑥𝑖_ =0<sup>_𝑔_</sup> _𝑖_<sup>_𝑥𝑖𝑃_(</sup><sup>_𝑥𝑖_−1).</sup> Therefore, the generating function of all terms that scale as _𝑃_ ( _𝑥𝑖_ − 1) is _𝑔𝑖𝐺_ . Differentiating with respect to _𝑔𝑖_ :


189

_𝜕𝐺_ _<u>𝑠</u>_ Therefore, the generating function of all terms that scale as _𝑥𝑖𝑃_ is _𝑔𝑖 𝜕𝑔𝑖_<sup>.</sup> Alternatively, we can note that the _𝑥𝑖_ = 0 term of<sup>�∞</sup> _𝑥𝑖_ =0<sup>_𝑔_</sup> _𝑖_<sup>_𝑥𝑖_−1</sup> _𝑥𝑖𝑃_ ( _𝑥𝑖_ ) is zero, and rewrite as the equivalent expression<sup>�∞</sup> _𝑥𝑖_ =0<sup>_𝑔_</sup> _𝑖_<sup>_𝑥𝑖_(</sup><sup>_𝑥𝑖_+1)</sup><sup>_𝑃_(</sup><sup>_𝑥𝑖_+1).</sup> Therefore, the generating function of all terms that scale as ( _𝑥𝑖_ + 1) _𝑃_ ( _𝑥𝑖_ + 1) is<sup>_𝜕𝐺_</sup><sup>_<u>𝑠</u>_</sup> _𝜕𝑔𝑖_<sup>.</sup>

Multiplying this equation through by _𝑔 𝑗_ :


This follows from rewriting<sup>�∞</sup> _𝑥 𝑗_ =0<sup>_𝑔𝑥_</sup> _𝑗_<sup>_𝑗_+1</sup> _𝑃_ ( _𝑥𝑖_ + 1 _, 𝑗_ ) as<sup>�∞</sup> _𝑥 𝑗_ =−1<sup>_𝑔𝑥_</sup> _𝑗_<sup>_𝑗_+1</sup> _𝑃_ ( _𝑥𝑖_ + 1 _, 𝑥 𝑗_ ), noting that _𝑃_ ( _𝑥 𝑗_ ) = 0 whenever _𝑥 𝑗 <_ 0, and reindexing to obtain the equivalent sum �∞ _𝑥 𝑗_ =0<sup>_𝑔𝑥_</sup> _𝑗_<sup>_𝑗𝑃_(</sup><sup>_𝑥𝑖_+ 1</sup><sup>_, 𝑥𝑗_−1).Therefore, the generating function of all terms that scale</sup> as ( _𝑥𝑖_ + 1) _𝑃_ ( _𝑥𝑖_ + 1 _, 𝑥 𝑗_ − 1) is _𝑔 𝑗 𝜕𝑔_<sup>_<u>𝜕𝐺</u>_</sup> _𝑖_<sup>.</sup>

Multiplying the derivative by _𝑔𝑖_ twice:


This follows from rewriting<sup>�∞</sup> _𝑥𝑖_ =0<sup>_𝑔_</sup> _𝑖_<sup>_𝑥𝑖_+1</sup> _𝑥𝑖𝑃_ ( _𝑥𝑖_ ) as<sup>�∞</sup> _𝑥𝑖_ =−1<sup>_𝑔_</sup> _𝑖_<sup>_𝑥𝑖_+1</sup> _𝑥𝑖𝑃_ ( _𝑥𝑖_ ), noting that _𝑃_ ( _𝑥𝑖_ ) = 0 whenever _𝑥𝑖 <_ 0, and reindexingtoobtaintheequivalentsum<sup>�∞</sup> _𝑥𝑖_ =0<sup>_𝑔_</sup> _𝑖_<sup>_𝑥𝑖_(</sup><sup>_𝑥𝑖_−</sup> 1) _𝑃_ ( _𝑥𝑖_ −1). Therefore, the generating function of all terms that scale as ( _𝑥𝑖_ −1) _𝑃_ ( _𝑥𝑖_ − 1) is _𝑔𝑖_<sup>2</sup> _𝜕𝑔𝜕𝐺𝑖_<sup>.</sup>

Multiplying the derivative by _𝑔𝑖𝑔 𝑗_ :


This follows from rewriting<sup>�∞</sup> _𝑥𝑖_ =0<sup>_𝑔𝑥_</sup> _𝑗_<sup>_𝑗_+1</sup> _𝑃_ ( _𝑥 𝑗_ ) as<sup>�∞</sup> _𝑥 𝑗_ =−1<sup>_𝑔𝑥_</sup> _𝑗_<sup>_𝑗_+1</sup> _𝑃_ ( _𝑥 𝑗_ ), noting that _𝑃_ ( _𝑥 𝑗_ ) = 0 whenever _𝑥 𝑗 <_ 0, andreindexingtoobtaintheequivalentsum<sup>�∞</sup> _𝑥 𝑗_ =0<sup>_𝑔𝑥_</sup> _𝑗_<sup>_𝑗𝑃_(</sup><sup>_𝑥𝑗_).</sup> Therefore, the generating function of all terms that scale as _𝑥𝑖𝑃_ ( _𝑥 𝑗_ − 1) is _𝑔𝑖𝑔 𝑗 𝜕𝑔_<sup>_<u>𝜕𝐺</u>_</sup> _𝑖_<sup>.</sup>

190

Multiplying the generating function by a probability-generating function _𝐹_ of a discrete burst distribution _𝑝_ :


This identity may be derived from three equivalent directions. Most simply, it is a statement of the convolution theorem. Alternatively, it may be proven directly using the repeated ( _𝑛_ -fold) application of Cauchy products. Finally, the master equation term essentially aggregates two independent random variables – the process values and the burst sizes – whose sum is equal to **x** . The generating function of the sum of independent variates is the product of their generating functions. Therefore, the generating function of all terms that scale as<sup>�</sup> **z**<sup>_𝑝_(</sup><sup>**z**)</sup><sup>_𝑃_(</sup><sup>**x**−</sup><sup>**z**)is</sup><sup>_𝐹𝐺_.</sup>

### **A.3 Fully continuous master equation terms**

Multiplying _𝐺_ through by _ℎ𝑖_ , we obtain:


This follows from integrating by parts. The product term _𝑒_<sup>**h**T</sup><sup>**y**</sup> _𝑃_ does not contribute to this expression because _𝑃_ is a density with zero mass at any particular value of **y** . Therefore, the generating function of all terms that scale as _𝜕𝑦_<sup>_<u>𝜕𝑃</u>_</sup> _𝑖_<sup>is −</sup><sup>_ℎ𝑖𝐺_.</sup>

Differentiating with respect to _ℎ𝑖_ :


Therefore, the generating function of all terms that scale as _𝑦𝑖𝑃_ is<sup>_𝜕𝐺_</sup> _𝜕ℎ𝑖_<sup>_<u>𝑠</u>_.</sup> Multiplying through by _ℎ 𝑗_ :


191

This follows from integrating by parts. The product term _𝑒_<sup>**h**T</sup><sup>**y**</sup> _𝑦𝑖𝑃_ does not contribute to this expression because it is identically zero at _𝑦𝑖_ = 0 and _𝑃_ vanishes as _𝑦𝑖_ →∞. Therefore, the generating function of all terms that scale as<sup>_𝜕_</sup><sup><u>[</u></sup> _𝜕𝑦_<sup>_<u>𝑦𝑖</u>𝑃_</sup> _𝑗_<sup><u>]</u></sup> is − _ℎ 𝑗 𝜕ℎ_<sup>_<u>𝜕𝐺</u>_</sup> _𝑖_<sup>.</sup> Multiplying the derivative by _ℎ𝑖_ twice:


= This follows from integrating by parts. Again, the product term _𝑒_<sup>**h**T</sup><sup>**y**</sup><sup>_𝜕_</sup><sup><u>[</u></sup><sup>_<u>𝑦𝑖</u>𝑃_</sup><sup><u>]</u></sup> _𝜕𝑦𝑖 𝑒_<sup>**h**T</sup><sup>**y**</sup> _𝑦𝑖 𝜕𝑦_<sup>_<u>𝜕𝑃</u>_</sup> _𝑖_<sup>+</sup><sup>_𝑒_</sup><sup>**h**T</sup><sup>**y**</sup><sup>_𝑃_does not contribute to this expression because</sup><sup>_𝑃_is a density that</sup> vanishes as _𝑦𝑖_ →∞. Therefore, the generating function of all terms that scale as _𝜕_<sup>2</sup> <u>[</u> _<u>𝑦𝑖</u> 𝑃_ <u>]</u> _<u>𝜕𝐺</u>_ is _ℎ_<sup>2</sup> _𝜕𝑦_<sup>2</sup> _𝑖 𝑖 𝜕ℎ𝑖_<sup>.</sup>

Multiplying the generating function by a moment-generating function _𝑀_ of continuous burst distribution _𝑝_ :


which may be derived from the convolution theorem, or MGF identities, identically to Equation A.8. Therefore, the generating function of all terms that scale as _𝑝_ ( **z** ) _𝑃_ ( **y** − **z** ) _𝑑_ **z** is _𝑀𝐺_ .

### **A.4 Mixed master equation terms**

Considering the case where a continuous process drives a discrete one, and multiplying _𝜕ℎ_<sup>_<u>𝜕𝐺</u>_</sup> _𝑖_<sup>by</sup><sup>_𝑔𝑗_:</sup>


The derivation is identical to Equation A.3. Therefore, the generating function of all terms that scale as _𝑦𝑖𝑃_ ( _𝑥 𝑗_ − 1) is _𝑔 𝑗 𝜕ℎ_<sup>_<u>𝜕𝐺</u>_</sup> _𝑖_<sup>.</sup>

192

Considering the case where a discrete process drives a continuous one, and multiplying _𝑔𝑖 𝜕𝑔_<sup>_<u>𝜕𝐺</u>_</sup> _𝑖_<sup>by</sup><sup>_ℎ𝑗_:</sup>


This follows from integrating by parts; as before, the product term does not appear because _𝑃_ is a density. Therefore, the generating function of all terms that scale as _𝜕_ <u>[</u> _𝜕𝑦𝑥𝑖 𝑃𝑗_ <u>]</u> = _𝑥𝑖 𝜕𝑦_<sup>_<u>𝜕𝑃</u>_</sup> _𝑗_<sup>is −</sup><sup>_ℎ𝑗𝑔𝑖_</sup> _𝜕𝑔_<sup>_<u>𝜕𝐺</u>_</sup> _𝑖_<sup>.This concludes the enumeration of generating function</sup> identities.

### **A.5 Converting the master equation to a partial differential equation**

By exploiting the identities derived above and the linearity of the generating function, we can represent Equation A.1 by an equivalent deterministic partial differential equation. We begin by considering the expressions for each entry of **G** separately, eliding the gene state _𝑠_ .

Each entry of the second term on the right-hand side, which represents degradation of the discrete species, takes the form


Each entry of the third term, which represents interconversion of the discrete species, takes the form


193

Each entry of the fourth term, which represents autocatalysis of the discrete species, takes the form


Each entry of the fifth term, which represents catalysis of the discrete species, takes the form


Each entry of the sixth term, which represents bursty production of the discrete species, takes the form


Each entry of the seventh term, which represents the deterministic dynamics of the continuous species, takes the form


194

Each entry of the eighth term, which represents the diffusion dynamics of the continuous species, takes the form


Each entry of the ninth term, which represents the drift of the continuous species, takes the form


Each entry of the tenth term, which represents the bursty production of the continuous species, takes the form


Each entry of the eleventh term, which represents a continuous species driving a discrete one, takes the form


195

Each entry of the twelfth term, which represents a discrete species driving a continuous one, takes the form


Therefore, the PDE form of the master equation is


This equation governs the dynamics of _𝐺 𝑠_ , one of _𝑁_ coupled PDEs. We elide this subscript when it does not directly factor into the calculation. As in Equation A.1, the terms that scale with _𝐺_ , rather than one of its derivatives, may be time- and _𝑠_ -dependent.

### **A.6 Representing the PDE in matrix form**

This formulation in Equation A.27 is somewhat more compact, but may be simplified further. First, we note that the second and third terms on the right-hand side can be represented by the matrix equation


where ∇<sup>_𝑑_</sup> is the length- _𝑛_ column vector gradient with respect to entries of **g** .

Next, the fourth and fifth terms can be represented by


196

The sixth term can be represented by constructing the vector _𝜶_<sup>_𝑑_</sup> and vector function **F** , indexed by _𝜔_ , with elided dependence on _𝑠_ :


The seventh term can be represented similarly to second and third:


where ∇<sup>_𝑐_</sup> is the gradient with respect to entries of **h** .

The eighth term can be represented analogously to the fourth and fifth:


The ninth and tenth term can be represented analogously to the sixth; we construct vector _𝜶_<sup>_𝑐_</sup> and vector function **M** , indexed by _𝜔_ , with elided dependence on _𝑠_ :


The first _𝑚_ entries of _𝜶_<sup>_𝑐_</sup> contain the _𝑚_ scalar drift rates, whereas the other entries contain jump rates, i.e., ( **M** ) _𝑖_ := _ℎ𝑖_ + 1 for _𝑖_ ≤ _𝑚_ .

The eleventh term takes a form analogous to those for second, third, and seventh:


Finally, the twelfth is analogous to fourth and fifth:


Therefore, Equation A.27 can be condensed further for a particular _𝑠_ :


197

Collecting terms:


In other words, the PDE separates into the usual first-order linear form, with terms corresponding to _𝐺_ , ∇<sup>_𝑑_</sup> _𝐺_ , and ∇<sup>_𝑐_</sup> _𝐺_ .

### **A.6.1 Unifying the discrete and continuous species**

However, analyzing Equation A.37 as is obfuscates the mathematical similarities of the discrete and continuous species.

To exploit them, we first introduce the variable **u** , which is a shifted version of **g** concatenated to **h** :


This yields the following form for the gradient-dependent terms:


Next, we define the full gradient of _𝐺_ , such that ∇ _𝐺_ contains the derivatives with respect to all entries of **u** . We define common jump rates and generating functions:


This notation emphasizes that M is formally defined over all values of **u** ; however, each entry, which corresponds to a specific influx process (i.e., a burst, drift, or jump

198

term) possesses nontrivial dependence only on the relevant (discrete or continuous) indices.

We define the common interconversion matrix:


as well as the common diffusion matrix:


This yields the following unified expression for a single state:


In this equation, ∇ _𝐺_ is the gradient of _𝐺_ with respect to **u** . It remains to generalize this expression to multiple states. Of the biological parameters, only the entries of _𝐻_ , _𝜶_ , and M depend on gene state. To specify the influx dynamics, we need to define the full bursting operator, which is a length- _𝑁_ vector function:


where the subscripts of _𝜶_ and M now indicate the gene state. Finally, recalling that the full Jacobian has entries _𝐽𝑠𝑖_ =<sup>_𝜕𝐺_</sup><sup>_<u>𝑠</u>_</sup> _𝜕𝑢𝑖_<sup>, the full PDE system takes the following</sup> form:


### **A.6.2 Solving the partial differential equation**

We seek to integrate this PDE to obtain the generating function at an arbitrary time _𝑡_ . The form is conducive to applying the method of characteristics. First, we define the characteristic variable s. By taking a total derivative with respect to s, we obtain


199

Next, we rewrite the PDE to match the form of the total derivative:


The characteristic curves emanating from ( _𝑡,_ **u** ) that satisfy the PDE are given by:


This is the “downstream” ODE, which governs abundances in isolation from production and regulation.

Therefore, **G** is governed by the following system of ordinary differential equations:


To obtain **G** at _𝑡_ , we integrate this matrix system from s = _𝑡_ to s = 0. We use **G**<sup>0</sup> ( **U** ( _𝑡_ )) as the initial condition, where **G**<sup>0</sup> is the generating function of the initial distribution. This is the “upstream” ODE, which governs the full generating function.

200

### **A.7 Regulation extensions**

This section summarizes some investigations undertaken during the writing of [115] by G.G., J.J.V., and L.P. This derivation was performed by G.G.

We have summarized a considerable breadth of biological phenomena in a common framework. Yet the really “interesting” ones, such as regulation, are still elusive. To see why, we can formalize the challenges of feedback, using the _𝑚_ = 0, _𝑁>_ 1, _𝑛>_ 0 case as an example.

First, we write down the master equation. We are interested in _non-sequestering_ catalysis of state switching, such that reactions of the form


are allowed, whereas reactions of the form


are disallowed. This is mostly a mathematical convenience: in addition to catalysis, we would like to retain the usual non-catalytic switching (encoded in a matrix _𝐻_ ), and restricting the allowed reactions in this way avoid strange and nonphysical edge cases in the vein of


i.e., the spontaneous generation of molecules<sup>9</sup> .

The master equation terms corresponding to the switching reactions are


i.e., any species, indexed by _𝑘_ , can, in principle, catalyze any transition between states. Ostensibly, the summation excludes self-transitions. From Equation A.4, we immediately obtain that the corresponding generating function terms are


Defining the diagonal elements of _𝑅𝑘_ in the usual fashion, such that _𝑅𝑘,𝑠𝑠_ := � _𝑖_ ≠ _𝑠_<sup>_𝑅_</sup> _𝑘,𝑠𝑖_<sup>, we yield the matrix form</sup>


201

where the partial derivative is elementwise. In the case of _𝑛_ = 1, this reduces to the somewhat simpler case


The _right_ -multiplication by the Jacobian matrix _𝐽_ makes all the difference: the system ceases to be tractable by the method of characteristics, as we cannot specify a “downstream” component.

We can illustrate this point more easily by considering the usual _𝑁_ = 2, _𝐷_ = 0 case with Poisson process transcription in the on state [301]. This yields


where _𝑅_ on and _𝑅_ off are the mass action rates of transition catalysis. This matrix equation is equivalent to the system


which combines the autoactivation and autorepression cases in Equations 2.7 and 2.8 of [301]. Parenthetically, we question the authors’ justification for treating these phenomena as mutually exclusive because they “cancel out.” For example, if _𝑅_ on = _𝑅_ off, but both are both extremely high, we obtain a trivial Poisson distribution of RNA, which is qualitatively different from the possibly bimodal _𝑅_ on = _𝑅_ off = 0 case. In addition, this justification ceases to hold when considering _𝑁>_ 2.

202

Let us treat the simplest case, with _𝑘_ on = _𝑘_ off = _𝛾_ = 0. Then we obtain


The next steps are somewhat obscure. We can use eigendecomposition:


Defining _𝑉_ **G**<sup>˜</sup> := **G** , we obtain


and multiplying by _𝑉_<sup>−1</sup> from the left,


This produces _two_ characteristic curves, defined by


Although this functional form is certainly precedented in the study of partial differential equations (see, e.g., Section 22.4 of [79] and Section 2.5 of [153]), it does not appear to lead to a closed-form solution, and the development of a reasonably generic procedure for treating regulation in the same framework remains out of reach for now. Although we do not treat the more general cases with nontrivial _𝐻_ and _𝛾_ , they produce largely the same challenges.

203

### **A.8 Stochastic process identities**

In this section, we outline some useful identities and demonstrate the mathematical capabilities of the current approach.

### **A.8.1 The telegraph process converges to the jump subordinator**

This section adapts a portion of the supplement of [105] by G.G. and L.P. This derivation was performed by G.G.

In Equation 4.22, we have summarized the “upstream” degrees of freedom in terms of a state interconversion matrix _𝐻_ and a state-dependent transcription operator A. The entries of the operator essentially encode the distribution of a memoryless Poisson arrival process. This process, in turn, arises as the approximation of a timescale-separated process; for example, it is well-understood [233, 267] that the reaction schema


is equivalent to


with _𝐵_ a geometrically-distributed random variable with mean _𝑏_ , whenever _𝑘_ off, _𝑘_ init →∞ with<sup>_𝑘_</sup><sup><u>init</u></sup> _𝑘_ off<sup>:=</sup><sup>_𝑏_finite.Thereareanumberofwaystoprovethis.For</sup> example, it is straightforward to consider the case with degradation of X, find its distribution [143], then take the relevant limit and show that the transient distributions match the bursty case. However, this procedure relies on somewhat tedious manipulation of special functions.

The easiest approach being with noticing that this process affords a representation in terms of the instantaneous transcription rate _𝐾_ ( _𝑡_ ), which is equal to zero when _𝑠_ = Soff and _𝑘_ init when _𝑠_ = Son. This process’s value depends on its past, implying that it is not a subordinator<sup>10</sup> (contradicting [7, 8]). The duration of each on period is exponential with scale _𝑘_ off<sup>−1.The total transcriptional intensity of each on period</sup> is exponential with scale _𝑘_ off<sup>−1</sup><sup>_𝑘_init=</sup><sup>_𝑏_.The number of molecules generated per on</sup> period is Poisson, with a mean given by the intensity, i.e., geometric with scale _𝑏_ . As _𝑘_ off →∞, the on periods become infinitesimally short, and the process becomes memoryless, producing a jump subordinator.

204

### **A.8.2 The CIR process converges to the inverse Gaussian subordinator**

This section adapts a portion of [113] by G.G.<sup>∗</sup> , J.J.V.<sup>∗</sup> , M.F., and L.P. This analysis was performed by J.J.V. and G.G.

Consider, now, the case of the Cox–Ingersoll–Ross transcriptional driver (Equations 7.3 and 7.4) coupled to unspecified downstream dynamics. We have some characteristic _𝑈_ corresponding to downstream species and the following ODE for the CIR characteristic _𝑈𝐾_ (s):


For _𝜅_ →∞, both sides of the equation are approximately zero: _𝑈𝐾_ rapidly equilibrates. Applying the quadratic formula:


We have assumed _𝑏_ is finite, so _𝜃_ →∞. Therefore, we find that the transcription operator A( _𝑈𝐾_ (s)) takes the form


We have chosen the negative sign because otherwise _𝑈𝐾_ (s) does not converge to zero, and does not produces a steady-state solution when integrated. This expression is the moment-generating function of the inverse Gaussian subordinator. Interestingly, even though this process is memoryless, it is not a compound Poisson process: it has infinitely many jumps in each finite interval. Although this limit is somewhat degenerate, it is useful to consider, as it fills an apparent lacuna in the finance literature [20, 22]: when _𝑈_ = _𝑒_<sup>−</sup><sup>_𝛾_s</sup> , we find that the stationary distribution has the relatively simple closed-form log-PGF:


In our understanding, this is the solution to the “OU-IG” case listed as “Not known” in Table 2 of [22].

205

### **A.8.3 The Poisson representation facilitates adaptation of finance results**

### **A.8.3.1 Time-dependent bursty processes**

This section adapts a portion of [105] by G.G. and L.P. This derivation was performed by G.G.

We can use the isomorphisms between continuous and discrete processes to bypass tedious calculations. For example, mixture models are fairly popular for representing differentiation trajectories: each latent time is associated with a set of parameters for the negative binomial distribution; these parameters smoothly evolve throughout the trajectory [77, 216], representing modulation of bursty transcription. We can reasonably ask whether this framework can be used to represent “RNA velocity”like trajectories, with meaningful transient effects (Section 6.1.1). This question is interesting given that this holds true for non-bursty processes: the distribution of a process with constitutive production, coupled to some isomerization and degradation reactions, is Poisson with a time-dependent mean (a trivial consequence of Equation 4.25, but explored in further detail in [146]). Is it possible that a time-dependent negative binomial can represent a transient process in the same fashion?

This intuition turns out to be incorrect even in the simplest case with _𝑛_ = 1. The discrete bursty process is a Poisson mixture of the Γ-OU process (Equations 7.1 and 7.2). Therefore, its transient PGF coincides with the transient MGF of the Γ-OU process, which is well-known [241]:


For finite _𝑡_ , Equation A.70 is not the PGF of a negative binomial distribution. In other words, a “pseudotime”-dependent negative binomial distribution simply emulates a collection of local steady states, rather than any transient processes, in the vein of Equation 10.2.

### **A.8.3.2 Autocatalysis**

This section adapts a portion of [115] by G.G., J.J.V., and L.P. This derivation was performed by G.G.

Interestingly, this approach generalizes to cases with _𝐷_ ≠ 0. Suppose we are interested in a 1-species system with _𝑁_ = 1, _𝑛_ = 1, _𝑚_ = 0, involving birth at _𝛼_ ,

206

death at _𝛾_ , and autocatalysis at _𝑞_ :


This system was introduced, but not treated, by Jahnke and Huisinga [146], and, to our knowledge, first solved with master equation and generating function calculations in [300]. However, we can also solve it merely by matching terms, without any new calculations.

This reaction schema yields the following PDE terms:


The same form can be obtained by defining a system with _𝑁_ = 1, _𝑛_ = 0, and _𝑚_ = 1, with drift _𝛼_ , mean-reversion at rate _𝛾_ − _𝑞_ , and diffusion _𝑞_ . This system matches the functional form of a Cox–Ingersoll–Ross (CIR) process with drift _𝑎𝑏_ , mean-reversion rate _𝑎_ and square-root noise with intensity _𝜎_ [62]:


As _𝑡_ →∞, the CIR process approaches the gamma distribution with shape _𝜈_ and scale _𝜃_ :


which follows from standard identities [62]. The distribution has the MGF


207

This is the probability generating function of a negative binomial distribution with the shape _𝜈_ = _𝛼_ / _𝑞_ and mean _𝜈𝜃_ = _𝛾_ − _<u>𝛼𝑞</u>_<sup>.With some algebra, we can rewrite the PGF</sup> as


which is the analytical solution reported in the second line of Eq. 4.47 of [299] under the assumption _𝛾> 𝑞_ . We find, then, that autocatalysis with constitutive transcription yields a stationary distribution equivalent to bursty transcription with no autocatalysis.

### **A.8.3.3 Autocatalysis with bursty production**

This section adapts a portion of [115] by G.G., J.J.V., and L.P. This derivation was performed by G.G.

Obtaining this result, we may ask how the distribution changes if the molecules are produced in geometric bursts _𝐵_ with mean size _𝑏_ :


These reactions yield the following PDE terms:


To solve the system, we first find the solution to the Bernoulli-type differential equation, defining _𝑐_ = − _𝐶_ = _𝛾_ − _𝑞_ for convenience:


208

Then the log-generating function of the stationary distribution is given by the integral of A( _𝑈_ (s)):


To achieve a positive _𝜈_ , we must have


i.e., whereas in the non-bursty case, a steady state was guaranteed by having _𝛾> 𝑞_ , in the bursty case we must impose a more restrictive condition. The second inequality implies that the coefficient of _𝑢_ in the numerator


in other words, ( _𝑏𝑐_ )<sup>−1</sup> _𝑞_ ∈(0 _,_ 1) can be represented by _𝑒_<sup>−</sup><sup>_𝜅𝜏_</sup> for some positive _𝜅_ and _𝜏_ . Therefore, the GF


matches the functional form of the time-dependent MGF of the gamma Ornstein– Uhlenbeck process started at _𝑦_ = 0 [241], and the PGF of the bursty transcription/degradation process started at _𝑥_ = 0, precisely as discussed in Section A.8.3.1.

209

Finally, we define _𝑎_ = _𝑒_<sup>−</sup><sup>_𝜅𝜏_</sup> and rewrite _𝐺_ again:


This is a negative binomial–negative binomial mixture. In other words, the distribution is equivalent to that of a negative binomial distribution with scale parameter _𝑎𝑏_ and stochastic shape parameter _𝑘_ , with _𝑘_ in turn drawn from a negative binomial distribution with the shape _𝜈_ and success probability _𝑎_ . We can confirm this result through a direct calculation:


This expression uses the shape-mean parametrization for the conditional probability _𝑃_ ( _𝑥_ | _𝑘_ ) and the shape-probability parametrization for the mixing probability _𝑃_ ( _𝑘_ ).

However, is is considerably easier to notice that the analysis of the Γ-OU model by Sabino and Petroni [241] states that the transient process law is equivalent to that

210

of an Erlang distribution with scale parameter _𝑎𝑏_ and stochastic shape parameter _𝑘_ , with _𝑘_ in turn drawn from a negative binomial distribution with the shape _𝜈_ and success probability _𝑎_ , or scale 1+1 _𝑎_<sup>.This immediately implies that the distribution of</sup> the corresponding discrete process is a negative binomial-negative binomial mixture with equivalent parameters.

Although this distribution cannot be expressed in closed form, its construction makes the simulation of the bursty transient and stationary autocatalytic processes trivial, and suggests that simple finite approximations (i.e., up to a modest _𝑘_ ) may be developed.

### **A.8.4 Many processes are closed under species-independent, sequestering sampling**

This section adapts and extends a portion of [115] by G.G., J.J.V., and L.P. This derivation was performed by G.G.

Consider a sequestering, species-independent technical noise model, such that the probability of retaining a molecules of any species X _𝑖_ is _𝑝_ . Assume _𝐷_ = 0. The set of downstream characteristics **U** (s) is a linear combination of the entries of **u** . Since integrating sampling amounts to substituting _𝑢𝑖_ ← _𝑝𝑢𝑖_ , this procedure effectively rescales the entire function **U** by _𝑝_ . If the upstream generation process has a scale parameter, such that A( **u** ) involves multiplication by _𝜃𝑢𝑖_ , sampling is equivalent to rescaling _𝜃_ by _𝑝_ . For the common processes, we obtain the rescaling

_𝑘𝑝𝑈_ for constitutive production or drift and


for eachcomponentindexedby _𝜔_ . Thisholdsiftheconstitutiveproductionparameter _𝑘_ is stochastic; for example, sampling amounts to rescaling the parameter _𝜃_ of the usual extrinsic noise model. This also holds with no loss of generality if the burst or drift processes are state-dependent.

It is unclear whether this result generally holds for _𝐷_ ≠ 0. It very well might: the CIR driver coupled to two downstream species has this property, which we exploit in Section 7.1. However, the derivation is somewhat subtle and requires the direct manipulation of differential equations, so the generalization will require further investigation.

For the bursty model with _𝑛_ = 1, the resulting distribution is negative binomial with shape _𝑘_ / _𝛾_ and scale _𝑝𝑏_ . This justifies treating the parameter _𝜈_ in Equation 2.4 as

211

purely biological: the negative binomial shape is invariant under downsampling. However, there is no particular reason to think it is _uniform_ , because the burst size may differ between cell subpopulations<sup>11</sup> .

This result does not hold in its full generality when the sampling probabilities are species-dependent; for example, when _𝑝𝑁_ and _𝑝 𝑀_ are distinct, we can identify _𝑏𝑝𝑁_ and _𝑝𝑁_ / _𝑝 𝑀_ . The result does not hold when non-sequestering noise models are used.

212

_A p p e n d i x B_

---

[← DISCUSSION AND CONCLUSION](19-discussion-and-conclusion.md) · [Up: contents](index.md) · [QUALITATIVE DISCUSSION OF SEQUENCING PROCEDURES AND THEIR CAVEATS →](21-qualitative-discussion-of-sequencing-procedures-and-their-ca.md)

---
title: 02 questions
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/psets/02-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 02 questions

**Source:** `psets/02-questions.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Systems Biology**

**7.81/8.591/9.531**

**Problem Set 2 Due in class**

**Assigned: 10.06.04 Due: 10.19.04**

1. Biochemistry of the chemotaxis network.


<!-- Start of picture text -->
kd<br>T2Ptot  T3P  tot<br>k -d<br>ka  kb<br>k -a<br>k -b<br>kc<br>Effective model  tot  tot<br>T2 T3<br>k -c<br>T2P  T3P<br>1-fL<br>T2  T3<br>LT2P  LT3P<br>Full model<br>fL<br>LT2  LT3<br><!-- End of picture text -->

The _E. coli_ chemotaxis network is represented here in simplified form. T represents the Tar receptor, and L the ligand or attractant. The receptor can by modified by phosphorylation (subscript P) or methylation (subscripts 2 or 3).

- (10) _a._ The Tar receptor binds an extracellular ligand L according to


(10) _b._ We now assume that the ligand binding reaction is in rapid equilibrium, and only consider total amounts of each modified form of receptor. For example,

_T_ 3 _P tot_ = _T_ 3 _P_ + _LT_ 3 _P_ , etc. How would you calculate the effective rate constants _ka_ ,..., _kd_ and _k-a_ ,..., _k-d_ between these total concentration pools in terms of the rate constants of the original methylation /demethylation and phosphorylation/dephosphorylation reactions?

1

**Systems Biology**

**7.81/8.591/9.531**

- (10) _c._ The assumed rates in the models of Spiro _et al._ and Barkai _et al._ are shown in the table below. Write down explicitly the effective rate constants for each model, in terms of the symbols listed in the table.

||_Spiro mo_|_del_||_Barkai m_|_odel_|
|---|---|---|---|---|---|
||_L-unbound_|_L-bound_||_L-unbound_|_L-bound_|
|_ka _|_k8 _|0|_ka _|_0_|_0_|
|_k-a_|_ky _|_ky _|_k-a_|_k0 _|_k0 _|
|_kb _|3_k8 _|1.1_k8 _|_kb _|_kp1_|_kp2_|
|_k-b_|_ky _|_ky _|_k-b_|_k-p1_|_k-p2_|
|_kc _|_k1 _|_k3 _|_kc _|_k_|_k_|
|_k-c_|_k-1_|_k-1_|_k-c_|_0_|_0_|
|_kd _|_k1 _|_k3 _|_kd _|_0_|_0_|
|_k-d_|_k-1_|_k-1_|_k-d_|_km _|_km_|


Note that some effective rate constants are now functions of L. This is appropriate, since we know for example that the receptors should become less phosphorylated as L increases.

i) In the Spiro model, do _ka/k-a_ and _kb/k-b_ increase or decrease with L?

ii) In the Barkai model, we would like _kb_ to decrease and _k-b_ to increase with L. What does this imply about _kp1_ , _kp2_ , _k-p1_ and _k-p2_ ?

(10) _d._ Spiro model. In steady state, after the slow methylation reactions have had time to equilibrate, let α _(L)_ represent the fraction of receptors that are methylated. Consider now the total concentration of phosphorylated and unphosphorylated receptors. Write out explicitly, in terms of α _(L)_ , the effective rates of phosphorylation ( _kp_ ) and dephosphorylation ( _k-p_ ) using


For perfect adaptation to be achieved, the phosphorylated fraction of receptor must be independent of L in steady state. You should have found above that _k-p_ = _ky_ ; it is therefore sufficient for perfect adaptation that _kp_ = _kp *_ is a constant.

_*_

Set _k8_ = 15 s<sup>-1</sup> ; _KL_ = 1x10<sup>6</sup> M<sup>-1</sup> ; and _kp *_ = 15 s<sup>-1</sup> . Plot _ka_ and _kb_ for L = 0, ..., 2 _KL_ . On the same graph, draw a horizontal line showing the desired _kp *_ . Finally, set _kp_ = _kp *_ in the equation above, solve for α _(L)_ , and plot this function. This is the magical form of α _(L)_ required for perfect adaptation. The model of Spiro _et al._ is carefully “tuned” in order to achieve this result. We can contrast this situation with the Barkai model in part _f_ , which is perfectly adapting but requires no fine tuning.

2

**Systems Biology**

**7.81/8.591/9.531**

- (10) _e._ Barkai model. Biochemical evidence suggests that the methylation reaction (whose rate constant was written as _k_ in part _c_ ) operates at saturation with rate _v_ . Show that under this assumption, the entire model reduces to the following reaction scheme:


<!-- Start of picture text -->
k 0<br>T tot  tot<br>2  T 2  p<br>v  km’  km<br>kb  (  L )<br>T 3  tot  T 3  totp<br>k − b  (  L )<br><!-- End of picture text -->

Note that _v_ is a constant _rate_ (measured in M s<sup>-1</sup> ) while _km_ is a rate constant (measured in s<sup>-1</sup> ). What is the value of _km’_ ?


that this value is independent of L if and only if _km’_ = 0. This is the essence of the Barkai model: perfect adaptation is easy to achieve, as long as only the _phosphorylated_ receptors are demethylated by the CheB protein.

3

**Systems Biology**

**7.81/8.591/9.531**

2. Adaptation and frequency response of the chemotaxis network.

With a slight change of notation, the Barkai model of the chemotaxis network (see Problem 1 _f_ ) can be represented as


_*_

Here, _v_ represents the rate of creation of _C_ , the unphosphorylated receptor; _C_ is the phosphorylated or active form of the receptor, the actual signal which induces bacterial tumbling; _km_ and _km’_ are the rate constants of demethylation reactions; and finally, _k+_ and _k-_ are rate constants that represent the effect of ligand binding on the phosphorylation state of the receptor.


concentration causes a drop in the phosphorylated fraction of the receptor.

   -

- (10) _a._ Write down the equations for _dC/dt_ and _dC /dt_ . Solve for the steady state concentrations _Css_ and _C* ss_ . Under what conditions will _C*ss_ be independent of L?

- (10) _b._ Set δ _C_ = _C_ − _C_ ss , δ _C_<sup>*</sup> = _C_ * − _C_<sup>*</sup> ss . Derive the linearized equations representing fluctuations from steady state, driven by fluctuations δ _L_ ( _t_ )  of the ligand concentration. You should obtain


- (10) _c._ Assume for now that δ _L_ = 0, _km’_ = 0, and _km_ = 0. Calculate the eigenvectors and eigenvalues of the above matrix. You will find that one of the eigenvalues is zero. Recalculate this eigenvalue to first order in _km_ .

On a graph of δ _C_ vs. δ _C_<sup>_*_</sup> , plot the eigenvectors and note the slow and fast eigenvalues. Sketch a few typical timecourses for various initial values of {δ _C_ ,δ _C_<sup>_*_</sup> }. This initial perturbation might arise if the system had first reached steady state for one value of L, but that value was abruptly changed. Sketch out such an event, showing a step increase in L at time _t_ = 0, and the subsequent evolution of _C_ , _C*_ , and _CT_ as functions of time.

- (10) _d._ Now assume that δ _L,_ δ _C,_ δ _C_<sup>_*_</sup> _~ e_<sup>_i_ω</sup><sup>_t_</sup> . This corresponds to Fourier transforming the equation above.

4

**Systems Biology**

**7.81/8.591/9.531**

δ _C_ * <u>(ω)</u> Calculate the _transfer function T_ (ω) = . δ _L_ (ω)

Claiming that perfect adaptation holds corresponds to claiming that _T_ (ω) has no dc component ( _T_ (ω = 0) = 0). Show that this is true only if _km’_ = 0. Assume from now on that _km’_ = 0.

- (i) What is the behavior of _T_ (ω) as ω → 0?

(ii) What is the behavior of _T_ (ω) as ω → ∞?

(iii) Calculate the value ω<sup>_*_</sup> at which _T_ (ω) is maximized.

(iv) Make a sketch of _T_ (ω), indicating all the important regimes.

(10) _e._ From this sketch, it should be clear that the chemotaxis network serves as a bandpass filter: variations of L slower than the demethylation rate _km_ are suppressed by the adaptation property of the network; fast fluctuations of L are suppressed because _C*_ cannot respond any faster than the phosphorylation rate.

(i) Suppose _fout_ ( _t_ ) = _dfin_ ( _t_ )/ _dt_ . Calculate _Tdiff(_ ω _)_ = | _fout_ (ω)/ _fin_ (ω)|. This is the transfer function of a differentiator. For what values of ω does the chemotaxis network serve as a differentiator?

(ii) The network most efficiently transmits signals at the frequency ω<sup>_*_</sup> calculated in part _d_ (iii). What is the value of ω _*_ , assuming _km_ ~ 0.01 s<sup>-1</sup> and _k+_ ~ 10 s<sup>-1</sup> ?

(iii) It is said that “a cell compares the attractant concentration at any given time to that 4 seconds ago”, generating a tumble if it registers a decrease or a run if it registers an increase. That is, only by _differentiating_ the input does the cell manage to swim up an attractant gradient. Is the timescale of 4 seconds consistent with your answer from the part (ii)?

5

---

[Up: contents](../index.md)

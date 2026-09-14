---
title: 06 questions Part 04 —
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/06-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 06 questions Part 04 —

**Source:** `psets/06-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The E. coli chemotaxis network is represented in the accompanying gure in a simplied form. _T_ represents the Tar receptor and _L_ the ligand or attractant. The receptor can by modied by phosphorylation (subscript P) or methylation (subscripts 2 or 3). For example,


Problem 3 and Images courtesy of Alexander van Oudenaarden. Used with permission.

- _T_ 2 : Tar receptor that is unmethylated, unphosphorylated and not bound with ligand

- _LT_ 2 : unmethylated, unphosphorylated, bound with ligand

- _T_ 2 _p_ : unmethylated, phosphorylated, not bound with ligand

- _T_ 3 : methylated, unphosphorylated, not bound with ligand

- a. The receptors, independently of their phosphorylation or methylation state, can bind an extracellular ligand L according to the scheme


_kL_ + with the association constant _KL_ = _−_ . _kL_

Calculate the fraction of receptors with a ligand bound to them.

- b. We will assume that the ligand binding reaction is in rapid equilibrium and only consider total amounts of each modied form of receptor. So we will treat _T_ 3<sup>_tot_</sup> _P_<sup>=</sup><sup>_T_3</sup><sup>_P_+</sup><sup>_LT_3</sup><sup>_P_,etc,as</sup> the new relevant dynamical variables reducing the original problem to the analysis of the 4

> 2P.A.Spiro et al. PNAS 94 , 7263-7268 (1997)

> 3N.Barkai and S.Leibler. Nature 387 , 913-917 (1997)

3

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 6

state system depicted below.


Problem 3 and Images courtesy of Alexander van Oudenaarden. Used with permission.

The assumed rates in the models of Spiro et al. and Barkai et al. are shown in the table below.

Write down explicitly the eective rate constants _ka_<sup>+</sup><sup>_, ....., k_</sup> _d_<sup>+and</sup><sup>_k_</sup> _a−, ....., kd−_ for each model in terms of the symbols listed in the table.

|Related eective rate constant|Spiro model|Spiro model|Barkai model|Barkai model|
|---|---|---|---|---|
||L unbound|L bound|L unbound|L bound|
|_k_<sup>+</sup><br>_a_|_k_8|0|0|0|
|_ka_<br>_−_|_ky_|_ky_|_k_0|_k_0|
|_k_<sup>+</sup><br>_b_|3_k_8|1_._1_k_8|_k_<sup>+</sup><br>_p_1|_k_<sup>+</sup><br>_p_2|
|_kb_<br>_−_|_ky_|_ky_|_kp_<br>_−_<br>1|_kp_<br>_−_<br>2|
|_k_<sup>+</sup><br>_c_|_k_<sup>+</sup><br>1|_k_3|_k_|_k_|
|_kc_<br>_−_|_k_1<br>_−_|_k_1<br>_−_|0|0|
|_k_<sup>+</sup><br>_d_|_k_<sup>+</sup><br>1|_k_3|0|0|
|_kd_<br>_−_|_k_1<br>_−_|_k_1<br>_−_|_km_|_km_|


- c. Note that some eective rate constants are now functions of _L_ . This is appropriate since we know, for example, that the receptors should become less phosphorylated as _L_ increases.

   1. In the Spiro model, do _k_<sup>_<u>k</u>_</sup> _a_<sup>_<u>a−</u>_</sup> +<sup>and</sup> _kkbb−_<sup>+</sup> increase or decrease with _L_ ?

   2. In the Barkai model, we would like _kb_<sup>+todecreaseand</sup><sup>_k_</sup> _b−_ to increase with _L_ . What does this imply about _kp_<sup>+</sup> 1<sup>,</sup><sup>_k_</sup> _p−_ 1<sup>,</sup><sup>_k_</sup> _p_<sup>+</sup> 2<sup>and</sup><sup>_k_</sup> _p−_ 2<sup>?</sup>

- d. Spiro model. In steady state, after the slow methylation reactions have had time to equilibrate, let _α_ ( _L_ ) represent the fraction of receptors that are methylated. Consider now the total concentration of phosphorylated and unsphosphorylated receptors. Write out, in terms of _α_ ( _L_ ) and the relevant rate constants from the table shown in part c, the eective rates of phosphorylation ( _kp_<sup>+)anddephosphorylation(</sup><sup>_k_</sup> _p−_ ) using:


For perfect adaptation to be achieved the phosphorylated fraction of receptors must be independent of _L_ in steady state. Show that this will hold if and only if _kp_<sup>+is a constant (i.e.</sup> it is independent of _L_ ). We will name this constant _κ_ . Now set _κ_ = _k_ 8 = 15 s<sup>-1</sup> , _KL_ = 10<sup>6</sup> M<sup>-1</sup> .

4

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 6

   1. Plot _ka_<sup>+and</sup><sup>_k_</sup> _b_<sup>+for</sup><sup>_L_=0to2/</sup><sup>_KL_and,onthesamegraph,drawahorizontalline</sup> showing the desired _κ_ .

   2. Set _kp_<sup>+=</sup><sup>_κ_intheequationabove,solvefor</sup><sup>_α_(</sup><sup>_L_)andplotthisfunction.Thisisthe</sup> magical form of _α_ ( _L_ ) required for perfect adaptation. The model of Spiro et al is carefully tuned in order to achieve this result. W can contrast this situation with the Barkai model in part e, which has perfect adaptation but requires no ne tuning.

- e. Barkai model. Biochemical evidence suggests that the methylation reaction (whose rate constant was written as _k_ in part b) operates at saturation with rate _ν_ . Show that under this assumption the entire model reduces to the following reaction scheme:


Note that _ν_ is a constant rate per unit volume (measured in M s<sup>-1</sup> ) while _km_ is a rate constant (measured in s<sup>-1</sup> ). According to the table in part b, what would the value of _km′_<sup>be?</sup>

Treat _km′_<sup>asanindependentvariablenow.Writedowntheequationfor</sup><sup>_d_(</sup><sup>_T_</sup> 3<sup>_tot_</sup> + _T_ 3<sup>_tot_</sup> _P_<sup>)</sup><sup>_/dt_</sup> and solve for _T_ 3<sup>_tot_</sup> _P_<sup>insteadystate.Showthatthisvalueisindependentof</sup><sup>_L_ifandonlyif</sup> _km′_<sup>=0.ThisistheessenceoftheBarkaimodel:perfectadaptationiseasytoachieve,as</sup> long as the phosphorylated receptors are demethylated by the CheB protein.

5

MIT OpenCourseWare http://ocw.mit.edu

8.591J / 7.81J / 7.32 Systems Biology Fall 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 2 Life at low Reynolds number (10 points)](03-2-life-at-low-reynolds-number-10-points.md) · [Up: contents](index.md)

---
title: 4 Michaelis-Menten Kinetics
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/01-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Michaelis-Menten Kinetics

**Source:** `psets/01-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## 4.1 Paper and pencil calculations

Consider the reaction

_k_ 1+ _k E_ + _S ES →_ 2 _E_ + _P k_<sup>⇌</sup> 1 _−_

- Assume initial concentrations [ _E_ ] = 0 _._ 01 , [ _S_ ] = 1 , [ _ES_ ] = 0 , [ _P_ ] = 0 , and reaction rates

- _k_ 1+ = 1 , _k_ 1 _−_ = 0 _._ 1 , _k_ 2<sup>= 0</sup><sup>_._001.</sup>

   - a. Ignoring the second reaction ( _k_ 1+ , _k_ 1 _− ≫ k_ 2 ), calculate the quasi-equilibrium concentration of [ _ES_ ] ?

   - b. When do you expect to see the rst reaction, _E_ + _S kk_<sup>⇌</sup> 11+ _− ES_ , reach quasi-equilibrium?

   - c. At what time is the substrate concentration depleted to half of its initial value?

## 4.2 **COMPUTATION** Simulations

Simulate the reaction in (a) using the initial concentrations provided. From the simulation data:

- a. Plot the behavior of [ _E_ ] , [ _S_ ] , [ _ES_ ] , and [ _P_ ] vs. time from time _t_ 0 = 0 until time _tf_ = 5 .

- b. Plot the behavior of [ _E_ ] , [ _S_ ] , [ _ES_ ] , and [ _P_ ] vs. time from time _t_ 0 = 0 until time _tf_ = 100 _,_ 000 .

- c. Plot the rate of production of [ _P_ ] vs. the concentration of [ _S_ ] from time _t_ 0 = 0 until time _tf_ = 100 _,_ 000 .

- d. Do these plots agree with your calculations from part (a)?

Now, use the Michaelis-Menten equation to plot the expected rate of production of [ _P_ ] vs. the concentration of [ _S_ ] . What causes the deviation of the simulation data from the Michaelis-Menten equation at substrate concentrations close to the initial concentration?

## 4.3 **COMPUTATION**

## Fitting data

The two vectors listed in Table 1 correspond to 20 experimental measurements of the rate of production of [ _P_ ] (vector _V_ =<sup>_d_</sup> _dt_<sup><u>[</u></sup><sup>_P_</sup><sup><u>]</u></sup> ) and the concentration of substrate [ _S_ ] (vector _S_ ) respectively.

- _<u>S</u>_

- a. The Michaelis-Menten equation says _V_ = _Vmax Km_ + _S_ . Express _Vmax_ and _Km_ explicitly in terms of the reaction rates and the concentrations specied in 4.1.

- b. Plot the data and t them to the Michaelis-Menten equation for estimates of _Vmax_ and _Km_ . Plot the tted curve on the same graph.

- c. We can transform the Michaelis-Menten equation by taking the reciprocal of both sides _V_ <u>1</u> = _VmaxKmS_ + _Vmax_ <u>1</u> . This double reciprocal form is called the Lineweaver-Burk equation. Plot the data as _V_ <u>1</u> vs. _S_ <u>1</u> . Fit the data for estimates of _Vmax_ and _Km_ , and plot the tted line on the same graph.

3

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 1

- d. Compare the tted values of _Vmax_ and _Km_ given in (b) and (c). Why are they dierent? Is the dierence signicant?

<u>Table 1</u>

|V (rate of production of [_P_])|S (concentration of substrate [_S_])|
|---|---|
|0.15|0.10|
|0.34|0.15|
|0.35|0.19|
|0.42|0.24|
|0.48|0.29|
|0.60|0.34|
|0.52|0.38|
|0.63|0.43|
|0.63|0.48|
|0.63|0.53|
|0.60|0.57|
|0.66|0.62|
|0.69|0.67|
|0.63|0.72|
|0.73|0.76|
|0.69|0.81|
|0.74|0.86|
|0.77|0.91|
|0.72|0.95|
|0.75|1.00|


## Feedback (+1 Extra Credit) :

Please use a SEPARATE sheet of paper for this feedback. We will detach it from your problem set and keep it for future reference.

- How much time did you spend?

- Anything confusing?

- Liked a problem?

- Least favorite problem?

- Other comments (e.g., what should we change next time around)?

4

MIT OpenCourseWare http://ocw.mit.edu

8.591J / 7.81J / 7.32 Systems Biology Fall 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 3 Binding Kinetics, Detailed Balance and Cooperation](04-3-binding-kinetics-detailed-balance-and-cooperation.md) · [Up: contents](index.md)

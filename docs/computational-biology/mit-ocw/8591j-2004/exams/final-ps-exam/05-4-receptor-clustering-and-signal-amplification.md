---
title: 4. Receptor clustering and signal amplification
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/exams/final-ps-exam.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4. Receptor clustering and signal amplification

**Source:** `exams/final-ps-exam.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The cells must now sense and move towards the source of the cAMP waves. It is unknown precisely how the amoebae are able convert the small front-to-back difference in cAMP concentration into the large output signal necessary to drive cell motion. However, a similar amplification of small _temporal_ changes in ligand concentration into large changes in receptor activity has been observed in bacterial chemotaxis networks. We will now discuss a receptor clustering model that has been proposed in order to explain this amplification. Consider a receptor molecule _R_ that is activated by the binding of some ligand _L_ . Let α = 0,1 represent the activity of the receptor. Thus,


**_FA04_**

3

**_7.81 / 8.591 / 9.531_**

**_Systems Biology_**

- (5) _a_ . The probability that the system will be found in a state with energy _E_ is proportional to _e_ − _E_ / _kT_ . Show that the energy of the receptor molecule may be written in the form


By calculating the mean activity ~~α~~ and equating this to the value known from chemical kinetics, find an expression for _A_ in terms of _L_ , _k+_ and _k-_ ..

- (5) _b_ . Now consider a lattice of receptors _Ri_ , each with activity α _i_ . Suppose that an active receptor is able to activate nearby receptors even if they are not ligand-bound. The energy of _Ri_ can then be written as


where the sum over _j_ is a sum over the _n_ nearest neighbors of _Ri_ . How does the state of the neighboring receptors influence the energy of _Ri_ ?

- (5) _c._ Assume that the activity of each neighboring receptor may be approximated by its mean value. That is, Σ _nj_ =1α _j_ ≅ _n_ ~~α~~ . By substituting this expression into the above equation, find an expression for the mean activity ~~α~~ _i_ of receptor _Ri_ .

- (5) _d_ . There is nothing special about the particular receptor _Ri_ : our calculations could equally have been applied to any other receptor in the system. Therefore, the mean activity ~~α~~ _i_ must be equal to the mean activity ~~α~~ of the neighboring receptors. Apply this consistency condition to find an equation for ~~α~~ , and show how this equation may be solved graphically. (Hint: it is easier to work with the variable _s_ = ~~α~~ -1/2.)

- (10) _e_ . Explore the possible system responses as a function of the parameters _A_ and _B_ . For low values of _B_ , the equation has a single solution for all _A_ values. For high values of _B_ , the system goes from having one, to three, then back to one solution as _A_ is swept from -∞ to +∞. Find the critical value _Bc_ which separates these two behaviors. Explain why the system response changes as this critical value is crossed. Which regime is more relevant for understanding signaling?

- (5) _f._ Assuming _B_ < _Bc_ , calculate the logarithmic amplification


where _L0_ = _k-_ / _k+_ is the dissociation constant for ligand-receptor binding. Plot _G_ as a function of _B_ , and verify that it approaches the correct limit as _B_ approaches zero. We see that the amplification can be made arbitrarily large by appropriately tuning _B_ . What is the possible disadvantage of doing this?

(10) _g_ . Based on published experimental data, estimate the logarithmic amplification at each stage of the _Escherichia coli_ chemotaxis network. Is there any evidence that receptor clustering contributes to this amplification?

**_FA04_**

4

---

[← 3. Diffusion and cAMP waves](04-3-diffusion-and-camp-waves.md) · [Up: contents](index.md)

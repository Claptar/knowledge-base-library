---
title: Learning From Labelled Data  Maximum Likelihood Estimation
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Learning From Labelled Data  Maximum Likelihood Estimation

**Source:** `lectures/05-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**If we have a sequence that has islands marked, we can simply count**


<!-- Start of picture text -->
P  P  P  P  P  P  P  P<br>L:<br>start End<br>B  B  B  B  B  B  B  B<br>S:  G  C  A  A  A  T  G  C<br>P(Li+1|Li)  P(S|B)  P(S|P)<br>Bi+1  Pi+1  End  A:      1/5  !  A:<br>T:        0  T:<br>Bi  3/5  1/5  1/5  ETC..<br>G:      2/5  G:<br>Pi 1/3  2/3  0  C:      2/5  C:<br>Start  1  0  0<br><!-- End of picture text -->

47

#### **Case 1. When the right answer is known**

**<u>Intuition:</u>** When we know the underlying states, Best estimate is the average frequency of transitions & emissions that occur in the training data

**<u>Drawback:</u>** Given little data, there may be **<u>overfitting</u>** : P(x|) is maximized, but  is unreasonable **0 probabilities – VERY BAD**

**<u>Example:</u>**

Given 10 nucleotides, we observe `x = C, A, G, G, T, C, C, A, T, C`  `= P, P, P, p, p, P, P, P, P, P` Then: aPP = 1;   aPB = 0 eP(A) = .2; eP(C) = .4; eP(G) = .2; eP(T) =.2

48

#### **Pseudocounts**

Solution for small training sets:

###### Add pseudocounts

- Akl = # times kl transition occurs in  + rkl Ek(b) = # times state k in  emits b in x + rk(b)

rkl, rk(b) are pseudocounts representing our prior belief

Larger pseudocounts  Strong priof belief

Small pseudocounts ( < 1): just to avoid 0 probabilities

49

#### **Example: Training Markov Chains for CpG islands**

|**A**<br>**T**<br>**G**<br>**C**<br>**_aA_**<br>**_C_**<br>**_aGC_**<br>**_aAT_**|<br> <br>**_aG_**<br>**_T_**||•<br>•|
|---|---|---|---|
|**+**<br>**A**<br>**C**|**G**|**T**||
|**A**<br>.180<br>.274|.426|.120|•|
|**C**<br>.171<br>.368|**.274**|.188||
|**G**<br>.161<br>.339|.375|.125||
|**T**<br>.079<br>.355|.384|.182||


- Training Set:

   - set of DNA sequences w/ known CpG islands

   - Derive two Markov chain models:

•

- **‘+’ model** : from the CpG islands

- **‘-’ model** : from the remainder of sequence

- Transition probabilities for each model:


<!-- Start of picture text -->
 <br>c c is the number of times<br>  st st<br>a letter  t   followed letter  s<br>st <br>cst' inside the CpG islands<br> t'<br><!-- End of picture text -->

|**-**|**A**|**C**|**G**|**T**|
|---|---|---|---|---|
|**A**|.300|.205|.285|.210|
|**C**|.322|.298|**.078**|.302|
|**G**|.248|.246|.298|.208|
|**T**|.177|.239|.292|.292|


<!-- Start of picture text -->
 <br>a   cst cst is the number of times<br>st  letter  t   followed letter  s<br>c<br>st'<br> t' outside the CpG islands<br><!-- End of picture text -->

50

#### **6: Unsupervised learning**

Estimate model parameters based on **unlabeled** training data

51

---

[← Learning: How to train an HMM](02-learning-how-to-train-an-hmm.md) · [Up: contents](index.md) · [Unlabelled Data →](04-unlabelled-data.md)

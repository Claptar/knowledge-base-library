---
title: Unlabeled Data
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unlabeled Data

**Source:** `lectures/05-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
P  P  P  P  P  P  P  P<br>L:<br>start  End<br>B  B  B  B  B  B  B  B<br>S:  G  C  A  A  A  T  G  C<br><!-- End of picture text -->

An idea:

1. Imagine we start with some parameters

2. We _could_ calculate the most likely path, P*, given those parameters and S

3. We _could_ then use P* to update our parameters by maximum likelihood

**~~P(L~~ i+1** **~~|L~~ i** **~~)~~**<sup>**~~0~~**</sup> **~~P(S|B)~~**<sup>**~~0~~**</sup> **~~P(S|P)~~**<sup>**~~0~~**</sup> **~~P(L~~ i+1** **~~|L~~ i** **~~)~~**<sup>**~~1~~**</sup> **~~P(S|B)~~**<sup>**~~1~~**</sup> **~~P(S|P)~~**<sup>**~~1~~**</sup> **P(Li+1|Li)**<sup>**2**</sup> **P(S|B)**<sup>**2**</sup> **P(S|P)**<sup>**2**</sup> **…**

4. And iterate (to convergence)

**P(Li+1|Li)**<sup>**K**</sup> **P(S|B)**<sup>**K**</sup> **P(S|P)**<sup>**K**</sup>

53

###### **Learning case 2. When the right answer is unknown**

We don’t know the true Akl, Ek(b)

###### **Idea:**

- We estimate our “best guess” on what Akl, Ek(b) are (M step, maximum-likelihood estimation)

- We update the probabilistic parse of our sequence, based on these parameters (E step, expected probability of being in each state given parameters)

- We repeat

###### **Two settings:**

- Simple: Viterbi training (best guest = best path)

- Correct: Expectation maximization (all paths, weighted)

54

######

#### **One path**

#### **All paths**

1.  Scoring x, one path

2.  Scoring x, all paths

P(x,π) Prob of a path, emissions

- P(x) = Σπ P(x,π)

 

Prob of emissions, over all paths

3. Viterbi decoding

   4.  Posterior decoding

   - π^ = {πi | πi=argmaxk ΣπP(πi=k|x)}

- π* = argmaxπ P(x,π)

- Most likely path

   -   Path containing the most likely state at any time point.

5. Supervised learning, given π Λ* = argmaxΛ P(x,π|Λ)

   7.  Unsupervised learning



      - Λ* = argmaxΛ ΣπP(x,π|Λ)

6. Unsupervised learning. Λ* = argmaxΛ maxπP(x,π|Λ) Viterbi training, best path

Baum-Welch training, over all paths

55

#### **Simple casae: Viterbi Training**

**<u>Initialization:</u>**

Pick the best-guess for model parameters (or arbitrary) **<u>Iteration:</u>**

   1. Perform Viterbi, to find <sup>*</sup>

2. Calculate Akl, Ek(b) according to <sup>*</sup> + pseudocounts 3. Calculate the new parameters akl, ek(b)

Until convergence **<u>Notes:</u>**

   - Convergence to local maximum guaranteed. Why?

   - – Does not maximize P(x | )

   - In general, worse performance than Baum-Welch

56

######

#### **One path**

#### **All paths**

1.  Scoring x, one path

2.  Scoring x, all paths

P(x,π) Prob of a path, emissions

  P(x) = Σπ P(x,π) Prob of emissions, over all paths

3. Viterbi decoding

   4.  Posterior decoding

   - π^ = {πi | πi=argmaxk ΣπP(πi=k|x)} i | πi=argmaxk ΣπP(πi=k|x)}  | πi=argmaxk ΣπP(πi=k|x)} i=argmaxk ΣπP(πi=k|x)} =argmaxk ΣπP(πi=k|x)} k ΣπP(πi=k|x)}  ΣπP(πi=k|x)} πP(πi=k|x)} P(πi=k|x)}

- π* = argmaxπ P(x,π) π^ = {πi | πi=argmaxk ΣπP(πi=k|x)} i | πi=argmaxk ΣπP(πi=k|x)}  | πi=argmaxk ΣπP(πi=k|x)} i=argmaxk ΣπP(πi=k|x)} =argmaxk ΣπP(πi=k|x)} k ΣπP(πi=k|x)}  ΣπP(πi=k|x)} πP(πi=k|x)} P(πi=k|x)}  

- Most likely path Path containing the most likely state at any time point.

5. Supervised learning, given π 6.  Unsupervised learning Λ* = argmaxΛ P(x,π|Λ) 

6. Unsupervised learning. Λ* = argmaxΛ ΣπP(x,π|Λ) Λ ΣπP(x,π|Λ)  ΣπP(x,π|Λ) πP(x,π|Λ) P(x,π|Λ) 

Λ* = argmaxΛ maxπP(x,π|Λ) Viterbi training, best path Baum-Welch training, over all paths

      - Λ* = argmaxΛ ΣπP(x,π|Λ) Λ ΣπP(x,π|Λ)  ΣπP(x,π|Λ) πP(x,π|Λ) P(x,π|Λ)

Baum-Welch training, over all paths

57

## Expectation Maximization (EM)

**_The basic idea is the same:_ 1.Use model to estimate missing data (E step) 2.Use estimate to update model (M step) 3.Repeat until convergence EM is a general approach for learning models (ML estimation) when there is “missing data” Widely used in computational biology**

EM pervasive in computational biology Rec 3 (SiPhy), Lec 8 (Kmeans), Lec 9 (motifs)

58

## Expectation Maximization (EM)

**1. Initialize parameters randomly**

**2. E Step Estimate expected probability of hidden labels, Q, given current (latest) parameters and observed (unchanging) sequence**   _Q P_ ( _Labels_ | _S_ , _params_<sup>_t_1</sup> )

**3. M Step Choose new** **<u>maximum likelihood parameters over</u> probability distribution Q, given current probabilistic label assignments** _t t_ 1  _E_   _params_ argmax _Q_  log _P_ ( _S_ , _labels_ | _params_<sup></sup> )  _params_

###### **4. Iterate**

**P(S|Model)** **_guaranteed_ to increase each iteration**

59

**Case 2. When the right answer is unknown**

Starting with our best guess of a model M, parameters :

Given x = x1…xN for which the true  = 1…N is unknown,

We can get to a provably more likely parameter set 

Principle: EXPECTATION MAXIMIZATION

1. Estimate probabilistic parse based on parameters (E step) 2. Update parameters Akl, Ek based on probabilistic parse (M step)

3. Repeat 1 & 2, until convergence

60

#### **Estimating probabilistic parse given params (E step)**


<!-- Start of picture text -->
L<br>P  P  P  P  P  P  P  P<br>L:<br>To estimate  Akl:<br>start B  B  B  B  B  B  B  B  End<br>K<br>At each position i:  i  j<br>S:  G  C  A  A  A  T  G  C<br>Find probability transition kl is used:<br>P(i = k, i+1 = l | x) = [1/P(x)]  P(i = k, i+1 = l,  x 1 …x N) = Q/P(x)<br>where Q = P (x 1 …x i ,  i  = k,  i+1  = l, x i+1 …x N )  =<br>  = P ( i+1  = l, x i+1 …x N |  i  = k)  P(x1…xi,  i  = k)  =<br>  = P(i+1 = l, xi+1xi+2…xN | i = k) fk(i) =<br>  = P(xi+2…xN | i+1 = l) P(xi+1 | i+1 = l) P(i+1 = l | i = k) fk(i) =<br>  = bl(i+1) el(xi+1) akl fk(i)<br>  f k (i) a kl  e l (x i+1 ) b l (i+1)<br>So:  P(  i = k,   i+1 = l | x,   ) =   ––––––––––––––––––<br>P(x |   )<br>(For one such transition, at time step ii+1)<br><!-- End of picture text -->

61

#### **New parameters given probabilistic parse (M step)**

(Sum over all kl transitions, at any time step i)

So,

<mark>f</mark> k <mark>(i) a</mark> kl <mark>e</mark> l <mark>(x</mark> i+1 <mark>) b</mark> l <mark>(i+1)</mark> Akl = i P(i = k, i+1 = l | x, ) = i –––––––––––––––––

P(x | )

Similarly,

Ek(b) = [1/P(x)] {i | xi = b} <mark>f</mark> k <mark>(i) b</mark> k <mark>(i)</mark>

62

#### **Dealing with multiple training sequences**

(Sum over all training seqs, all kl transitions, all time steps i) If we have several training sequences, x<sup>1</sup> , …, x<sup>M</sup> , each of length N,

<mark>f</mark> k <mark>(i) a</mark> kl <mark>e</mark> l <mark>(x</mark> i+1 <mark>) b</mark> l <mark>(i+1)</mark> Akl = x i P(i = k, i+1 = l | x, ) = x i –––––––––––––––– P(x | )

Similarly, Ek(b) = x (1/P(x)) {i | xi = b} <mark>f</mark> k <mark>(i) b</mark> k <mark>(i)</mark>

63

#### **The Baum-Welch Algorithm**

**<u>Initialization:</u>**

Pick the best-guess for model parameters (or arbitrary)

###### **<u>Iteration:</u>**

1. Forward

2. Backward

3.  Calculate new log-likelihood P(x | )   (E step)

4. Calculate Akl, Ek(b)

5.  Calculate new model parameters akl, ek(b)  (M step)

**GUARANTEED TO BE HIGHER BY EXPECTATION-MAXIMIZATION**

Until P(x | ) does not change much

64

#### **The Baum-Welch Algorithm – comments**

Time Complexity:

   - # iterations  O(K<sup>2</sup> N)

- Guaranteed to increase the log likelihood of the model

   - P( | x) = P(x, ) / P(x) = P(x | ) / ( P(x) P() )

- Not guaranteed to find globally best parameters Converges to local optimum, depending on initial conditions

- • Too many parameters / too large model: Overtraining

65

######

#### **One path**

1.  Scoring x, one path

P(x,π)

Prob of a path, emissions

3. Viterbi decoding

   - π* = argmaxπ P(x,π)

Most likely path

5. Supervised learning, given π Λ* = argmaxΛ P(x,π|Λ)

6. Unsupervised learning. Λ* = argmaxΛ maxπP(x,π|Λ) Viterbi training, best path

#### **All paths**

2.  Scoring x, all paths

   - P(x) = Σπ P(x,π)

Prob of emissions, over all paths

4.  Posterior decoding

- π^ = {πi | πi=argmaxk ΣπP(πi=k|x)}

Path containing the most likely state at any time point.

6.  Unsupervised learning

   - Λ* = argmaxΛ ΣπP(x,π|Λ)

Baum-Welch training, over all paths

66

#### **Examples of HMMs for genome annotation**

|**Detection**<br>**of GC-rich**<br>**regions**|**Detection**<br>**of CpG-rich**<br>**regions**|**Detection**<br>**of**<br>**conserved**<br>**regions**|**Detection**<br>**of protein-**<br>**coding**<br>**exons**|**Detection**<br>**of protein-**<br>**coding**<br>**conservatio**<br>**n**|**Detection**<br>**of protein-**<br>**coding**<br>**gene**<br>**structures**|**Detection**<br>**of**<br>**chromatin**<br>**states**|
|---|---|---|---|---|---|---|
|2 states,<br>different<br>nucleotide<br>composition|8 states,<br>4 each +/-,<br>different<br>transition<br>probabilities|2 states,<br>different<br>conservation<br>levels|2 states,<br>different tri-<br>nucleotide<br>composition|2 states,<br>different<br>evolutionary<br>signatures|~20 states,<br>different<br>composition/<br>conservation<br>, specific<br>structure|40 states,<br>different<br>chromatin<br>mark<br>combination<br>s|
|GC-rich / AT-<br>rich|CpG-rich /<br>CpG-poor|Conserved /<br>non-<br>conserved|Coding exon<br>/ non-coding<br>(intron or<br>intergenic)|Coding exon<br>/ non-coding<br>(intron or<br>intergenic)|First/last/mid<br>dle coding<br>exon,UTRs,<br>intron1/2/3,<br>intergenic,<br>*(+/- strand)|Enhancer /<br>promoter /<br>transcribed /<br>repressed /<br>repetitive|
|Nucleotides|Di-<br>Nucleotides|Level of<br>conservation|Triplets of<br>nucleotides|64x64 matrix<br>of codon<br>substitution<br>frequencies|Codons,<br>nucleotides,<br>splice sites,<br>start/stop<br>codons|Vector of<br>chromatin<br>mark<br>frequencies<br>67|


#### **What have we learned ?**

• Generative model.  Hidden states, observed emissions. – Generate a random sequence

- Choose random transition, choose random emission (#0)

- • Scoring:  Finding the likelihood of a given sequence – Calculate likelihood of annotated path and sequence

      - Multiply emission and transition probabilities (#1)

   - Without specifying a path, total probability of generating x

      - Sum probabilities over all paths

      - Forward algorithm (#3)

   - Decoding:  Finding the most likely path, given a sequence – What is the most likely path generating entire sequence?

      - Viterbi algorithm (#2)

   - What is the most probable state at each time step?

- Forward + backward algorithms, posterior decoding (#4)

- • Learning:  Estimating HMM parameters from training data – When state sequence is known

      - Simply compute maximum likelihood A and E (#5a)

   - When state sequence is not known

      - Viterbi training:  Iterative estimation of best path / frequencies (#5b)

      - Baum-Welch:  Iterative estimation over all paths / frequencies (#6)

68

#### **Goals for today: HMMs, part II**

1. Review:  Basics and three algorithms from last time

   - Markov Chains and Hidden Markov Models

   - Calculating likelihoods P(x,π) (algorithm 1)

   - Viterbi algorithm:  Find π* = argmaxπ P(x,π) (alg 3)

   - Forward algorithm:  Find P(x), over all paths (alg 2)

2. Increasing the ‘state’ space / adding memory

   - Finding GC-rich regions vs. finding CpG islands

   - Gene structures GENSCAN, chromatin ChromHMM

3. Posterior decoding: Another way of ‘parsing’

   - Find most likely state πi, sum over all possible paths

4. Learning (ML training, Baum-Welch, Viterbi training)

   - Supervised: Find ei(.) and aij given labeled sequence

   - Unsupervised: given only x  annotation + params

69

MIT OpenCourseWare http://ocw.mit.edu

6.047 / 6.878 / HST.507 Computational Biology Fall 2015

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Unlabelled Data](04-unlabelled-data.md) · [Up: contents](index.md)

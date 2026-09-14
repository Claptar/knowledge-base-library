---
title: Introduction
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/05-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**6.047/6.878/HST.507 Computational Biology: Genomes, Networks, Evolution**

### **Lecture 05 Hidden Markov Models Part II**

1

2

###### **Module 1: Aligning and modeling genomes**

- Module 1: Computational foundations

   - Dynamic programming: exploring exponential spaces in poly-time

   - Introduce Hidden Markov Models (HMMs): Central tool in CS

   - HMM algorithms: Decoding, evaluation, parsing, likelihood, scoring

- This week: Sequence alignment / comparative genomics – Local/global alignment: infer nucleotide-level evolutionary events

   - Database search: scan for regions that may have common ancestry

- Next week: Modeling genomes / exon / CpG island finding – Modeling class of elements, recognizing members of a class

   - Application to gene finding, conservation islands, CpG islands

3

#### **Goals for today: HMMs, part II**

1. Review:  Basics and three algorithms from last time – Markov Chains and Hidden Markov Models

   - Calculating likelihoods P(x,π) (algorithm 1)

   - Viterbi algorithm:  Find π* = argmaxπ P(x,π) (alg 3)

- Forward algorithm:  Find P(x), over all paths (alg 2)

- 2. Increasing the ‘state’ space / adding memory

   - Finding GC-rich regions vs. finding CpG islands

- Gene structures (GENSCAN), chromatin (ChromHMM)

- 3. Posterior decoding: Another way of ‘parsing’

- Find most likely state πi, sum over all possible paths

- 4. Learning (ML training, Baum-Welch, Viterbi training) – Supervised: Find ei(.) and aij given labeled sequence

   - Unsupervised: given only x  annotation + params

4


<!-- Start of picture text -->
Markov chains and Hidden Markov Models (HMMs)<br>Rain  Transitions<br>Summer  Fall  Winter Spring<br>Sun<br>Clouds<br>Transitions  hidden<br>observed<br>Emissions<br>Snow<br>All observed<br><!-- End of picture text -->

- Markov Chain

   - HMM

- Q: states

- p:  initial state probabilities

- A:  transition probabilities

   - Q: states, p: initial, A: transitions

   - V: observations

   - E: emission probabilities

- What you see is what you get: next state only depends on current state (no memory)

- Hidden state of the world determines emission probabilities

- State transitions are a Markov chain

5

#### **HMM nomenclature for this course**


<!-- Start of picture text -->
π=  Summer  Fall  Winter<br>Spring  Transitions:  akl =P( πi=l | πi-1 = k )<br>Transition probability<br>πi<br>from state  k  to state  l<br>Emissions:  ekk ( xii )=P( xi|πi=ki|πi=k|πi=ki=k=k )<br>xi<br>Emission probability of<br><!-- End of picture text -->

**Emissions:** **_ekk_ (** **_xii_ )=P(** **_xi|πi=ki|πi=k|πi=ki=k=k_ ) Emission probability of symbol** **_xi_ from state** **_k_**


**_x=_**

- Vector **_x_** = Sequence of observations

- Vector **_π_** = Hidden path (sequence of hidden states)

- Transition matrix A= akl =probability of **_k_**  **_l_** state transition

- Emission vector **_E=ek(xi)_** = prob. of observing xi from state k

- Bayes’s rule: Use **_P(xi|πi=k)_** to estimate **_P(πi=k|xi)_**

6

#### **Example: The Dishonest Casino**

###### A casino has two dice:

- Fair die

   - P(1) = P(2) = P(3) = P(5) = P(6) = 1/6

- Loaded die

   - P(1) = P(2) = P(3) = P(4) = P(5) = 1/10 P(6) = 1/2

Casino player switches between fair and loaded die on average once every 20 turns

###### **<u>Game:</u>**

1. You bet $1

2. You roll (always with a fair die)

3. Casino player rolls (maybe with fair die, maybe with loaded die)

4. Highest number wins $2

Slide credit: Serafim Batzoglou

7

#### **Examples of HMMs for genome annotation**

|**Application**|**Detection**<br>**of GC-rich**<br>**regions**|**Detection**<br>**of**<br>**conserved**<br>**regions**|**Detection**<br>**of protein-**<br>**coding**<br>**exons**|**Detection**<br>**of protein-**<br>**coding**<br>**conservatio**<br>**n**|**Detection**<br>**of protein-**<br>**coding**<br>**gene**<br>**structures**|**Detection**<br>**of**<br>**chromatin**<br>**states**|
|---|---|---|---|---|---|---|
|**Topology /**<br>**Transitions**|2 states,<br>different<br>nucleotide<br>composition|2 states,<br>different<br>conservation<br>levels|2 states,<br>different tri-<br>nucleotide<br>composition|2 states,<br>different<br>evolutionary<br>signatures|~20 states,<br>different<br>composition/<br>conservation<br>, specific<br>structure|40 states,<br>different<br>chromatin<br>mark<br>combination<br>s|
|**Hidden**<br>**States /**<br>**Annotation**|GC-rich / AT-<br>rich|Conserved /<br>non-<br>conserved|Coding exon<br>/ non-coding<br>(intron or<br>intergenic)|Coding exon<br>/ non-coding<br>(intron or<br>intergenic)|First/last/mid<br>dle coding<br>exon,UTRs,<br>intron1/2/3,<br>intergenic,<br>*(+/- strand)|Enhancer /<br>promoter /<br>transcribed /<br>repressed /<br>repetitive|
|**Emissions /**<br>**Observatio**<br>**ns**|Nucleotides|Level of<br>conservation|Triplets of<br>nucleotides|Nucleotide<br>triplets,<br>conservation<br>levels|Codons,<br>nucleotides,<br>splice sites,<br>start/stop<br>codons|Vector of<br>chromatin<br>mark<br>frequencies|


8

###### **The main questions on HMMs**

**1. Scoring x, one path** = Joint probability of a sequence and a path, given the model – GIVEN a HMM M, a path , and a sequence x,

   - FIND Prob[ x,  | M ]

   - “Running the model”, simply multiply emission and transition probabilities

   - Application:  “all promoter” vs. “all backgorund” comparisons

**2. Scoring x, all paths** = total probability of a sequence, summed across all paths

   - GIVEN a HMM M, a sequence x

   - FIND the total probability P[x | M] summed across all paths

   -  Forward algorithm, sum score over all paths (same result as backward)

**3. Viterbi decoding** = parsing a sequence into the optimal series of hidden states

   - GIVEN a HMM M, and a sequence x,

   - FIND the sequence * of states that maximizes P[ x,  | M ]

   -  Viterbi algorithm, dynamic programming, max score over all paths, trace pointers find path

**4. Posterior decoding** = total prob that emission xi came from state k, across all paths – GIVEN  a HMM M, a sequence x

   - FIND the total probability P[i = k | x, M)

   -  Posterior decoding: run forward & backward algorithms to & from state I =k

**5. Supervised learning** = optimize parameters of a model given training data

   - GIVEN a HMM M, with unspecified transition/emission probs., labeled sequence x,

   - FIND parameters  = (ei, aij) that maximize P[ x |  ]

   - Simply count frequency of each emission and transition observed in the training data

**6. Unsupervised learning** = optimize parameters of a model given training data

   - GIVEN a HMM M, with unspecified transition/emission probs., unlabeled sequence x,

   - FIND parameters  = (ei, aij) that maximize P[ x |  ]

   - Viterbi training:  guess parameters, find optimal Viterbi path (#2), update parameters (#5), iterate

   - Baum-Welch training:  guess, sum over all emissions/transitions (#4), update (#5), iterate

9

######

#### **One path**

1.  Scoring x, one path

P(x,π)

- Prob of a path, emissions

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

10

#### **Probability of given path p, emissions x**


<!-- Start of picture text -->
ast<br>π  is the   1  1  1  1<br>…<br>(hidden) path<br>2  2  2  2<br>…<br>…  …  …  …<br>K  K  K K<br>…<br>es(xi)<br>x  is the<br>(observed)<br>x1 x2 x3 xK<br>sequence<br><!-- End of picture text -->


<!-- Start of picture text -->
π  is the<br>(hidden) path<br><!-- End of picture text -->

Courtesy of Serafim Batzoglou. Used with permission.


<!-- Start of picture text -->
• P(x,) = a01 * Πi ei(xi)    aii+1<br>start  emission transition<br><!-- End of picture text -->

11

#### **Example: One particular P vs. B assignment**

**0.75 0.75 P P P P P P P P L: 0.15 0.25 B B B B B B B B 0.85 0.85 0.85 0.25 0.25 0.25 0.42 0.42 0.30 0.25 0.25 S: G C A A A T G C**  _P P_ ( _G_ | _B_ ) _P_ ( _B_ 1 | _B_ 0 ) _P_ ( _C_ | _B_ ) _P_ ( _B_ 2 | _B_ 1) _P_ ( _A_ | _B_ ) _P_ ( _P_ 3 | _B_ 2)... _P_ ( _C_ | _B_ 7) 3 6 2 2  (0.85)  (0.25)  (0.75)  (0.42)  0.30  0.15  7  6.7  10

12

######

#### **One path**

1.  Scoring x, one path

P(x,π)

Prob of a path, emissions

3. Viterbi decoding

   - π* = argmaxπ P(x,π)

Most likely path

5. Supervised learning, given π Λ* = argmaxΛ P(x,π|Λ)

6. Unsupervised learning.

   - Λ* = argmaxΛ maxπP(x,π|Λ) Viterbi training, best path

#### **All paths**

2.  Scoring x, all paths

   - P(x) = Σπ P(x,π)

Prob of emissions, over all paths

4.  Posterior decoding

- π^ = {πi | πi=argmaxk ΣπP(πi=k|x)}

- Path containing the most likely state at any time point.

6.  Unsupervised learning

   - Λ* = argmaxΛ ΣπP(x,π|Λ)

Baum-Welch training, over all paths

13

#### **Finding the most likely path**


<!-- Start of picture text -->
1  1  1  1<br>…<br>2  2  2  2<br>…<br>…  …  …  …<br>K  K  K K<br>…<br>x1 x2 x3 xK<br><!-- End of picture text -->

- Find path * that maximizes total joint probability P[ x,  ]


<!-- Start of picture text -->
• argmaxπP(x,) =argmaxπ a01 * Πi ei(xi)    aii+1<br>start  emission transition<br><!-- End of picture text -->

14

#### **Calculate maximum P(x,**  **) recursively**

###### **Viterbi algortithm**

Define Vk(i) = Probability of the most likely path through state i=k Compute Vk(i+1) recursively, as a function of maxk’ { Vk’(i) }


<!-- Start of picture text -->
…<br>…<br>ajk  k  Vk(i)<br>hidden<br>Vj(i-1)  j<br>states<br>ek<br>…<br>observations  xi-1  xi<br>• Assume we know Vj for the previous time step (i-1)<br>• Calculate Vk(i) =     ek(xi)   *   maxj (   Vj(i-1)     ajk    )<br>current max  this emission  max ending  Transition<br>in state j at step i  from state j<br><!-- End of picture text -->

all possible previous states j

15

#### **The Viterbi Algorithm**


<!-- Start of picture text -->
State 1<br>2<br>Vk(i)<br>K<br><!-- End of picture text -->

x1   x2   x3 ………………………………………..xN

Input: x = x1……xN

**<u>Traceback:</u>** Follow max pointers back

**<u>Initialization:</u>**

V0(0)=1, Vk(0) = 0, for all k > 0

**<u>In practice:</u>**

**<u>Iteration:</u>** Vk(i) = eK(xi)  maxj ajk Vj(i-1) **<u>Termination:</u>**

P(x, *) = maxk Vk(N)

Use log scores for computation

**<u>Running time and space:</u>** Time:    O(K<sup>2</sup> N) Space:  O(KN)

16

######

#### **One path**

1.  Scoring x, one path

P(x,π)

Prob of a path, emissions

3. Viterbi decoding

   - π* = argmaxπ P(x,π)

- Most likely path

5. Supervised learning, given π Λ* = argmaxΛ P(x,π|Λ)

6. Unsupervised learning. Λ* = argmaxΛ maxπP(x,π|Λ) Viterbi training, best path

#### **All paths**

2.  Scoring x, all paths

   - P(x) = Σπ P(x,π)

Prob of emissions, over all paths

4.  Posterior decoding

- π^ = {πi | πi=argmaxk ΣπP(πi=k|x)}

- Path containing the most likely state at any time point.

6.  Unsupervised learning

   - Λ* = argmaxΛ ΣπP(x,π|Λ)

Baum-Welch training, over all paths

17

#### **P(x)**  **Prob that model emits x, sum over all paths**


<!-- Start of picture text -->
1  1  1  1<br>…<br>2  2  2  2<br>a02 …<br>0<br>…  …  …  …<br>K  K  K  K<br>…<br>e2(x1)<br>x1 x2 x3 xn<br><!-- End of picture text -->

###### Given a sequence x,

What is the probability that x was generated by the model (using any path)? – P(x) = Σπ P(x,π)

- Challenge: exponential number of paths

   - Sum over all paths, weighing the path probability, and the emission probs

   - Prob of emitting sequence: use individual emission probs from each state

   - Prob of path: use both emission and transition prob, based on previous path

• P(x) = Σπ  a01 * Πi ei(xi)    aii+1 start emission transition

18

#### **Calculate total probability Σπ P(x,**  **) recursively**


<!-- Start of picture text -->
…<br>…<br>ajk  k  fk(i)<br>hidden<br>fj(i-1)  j<br>states<br>ek<br>…<br>observations  xi-1  xi<br><!-- End of picture text -->

##### • Assume we know fj for the previous time step (i-1)


<!-- Start of picture text -->
• Calculate  fk(i) =     ek(xi)   *   sumj (   fj(i-1)        ajk    )<br>current sum  this emission  sum ending  transition<br>in state j at step i  from state j<br><!-- End of picture text -->

Sum over all previous states j

19

#### **The Forward Algorithm**


<!-- Start of picture text -->
State 1<br>2<br>fk(i)<br>K<br><!-- End of picture text -->

x1   x2   x3 ………………………………………..xN

Input: x = x1……xN

**<u>Initialization:</u>** f0(0)=1, fk(0) = 0, for all k > 0

**<u>In practice:</u>** Sum of log scores is difficult  approximate exp(1+p+q)  scaling of probabilities

**<u>Iteration:</u>**

fk(i) = eK(xi)  sumj ajk fj(i-1) **<u>Termination:</u>**

**<u>Running time and space:</u>** Time:    O(K<sup>2</sup> N) Space:  O(K)

P(x, *) = sumk fk(N)

20

#### **Goals for today: HMMs, part II**

1. Review:  Basics and three algorithms from last time

   - Markov Chains and Hidden Markov Models

   - Calculating likelihoods P(x,π) (algorithm 1)

   - Viterbi algorithm:  Find π* = argmaxπ P(x,π) (alg 3)

- Forward algorithm:  Find P(x), over all paths (alg 2)

- 2. Increasing the ‘state’ space / adding memory

   - Finding GC-rich regions vs. finding CpG islands

   - Gene structures GENSCAN, chromatin ChromHMM

3. Posterior decoding: Another way of ‘parsing’

   - Find most likely state πi, sum over all possible paths

4. Learning (ML training, Baum-Welch, Viterbi training)

   - Supervised: Find ei(.) and aij given labeled sequence

   - Unsupervised: given only x  annotation + params

21

#### **Increasing the state space (remembering more)**

HMM1:  Promoters = **only Cs and Gs matter** HMM2: Promoters = **it’s actually CpGs that matter** (di-nucleotides, remember previous nucleotide)

22

#### **Increasing the state of the system (looking back)**

- Markov Models are memory-less

   - In other words, all memory is encoded in the states

   - To remember additional information, augment state

- A two-state HMM has minimal memory

   - Two states: GC-rich vs. equal probability

   - State, emissions, only depend on **current** state

   - Current state only encodes **one** previous nucleotide

- How do you count **di** -nucleotide frequencies?

   - CpG islands: di-nucleotides

   - Codon triplets: tri-nucleotides

   - Di-codon frequencies: six nucleotides

-  Expanding the number of states


<!-- Start of picture text -->
a++  a--<br>a+-<br>+  -<br>a-+<br>A: .2  A: 1/4<br>C: .3  C: 1/4<br>G: .3  G: 1/4<br>T: .2  T: 1/4<br><!-- End of picture text -->

23

#### **Remember previous nucleotide: expand both states**


<!-- Start of picture text -->
aPP  aBB<br>aPB<br>CpG+  CpG-<br>aBP<br>A: .1  A: 1/4<br>C: .3  C: 1/4<br>G: .4  G: 1/4<br>T: .2  T: 1/4<br>T: 0  G: 0  C: 0  A: 1  +A A+ A: 1  C: 0  G: 0  T: 0<br>+C C+<br>T: 0  G: 0  C: 1  A: 0  A: 0  C: 1  G: 0  T: 0<br>T: 0  G: 1  C: 0  A: 0  +G G+ A: 0  C: 0  G: 1  T: 0<br>+T T+<br>T: 1  G: 0  C: 0  A: 0  A: 0  C: 0  G: 0  T: 1<br><!-- End of picture text -->

**“Memory” of previous nucleotide is encoded in the current state.**

**GC-rich: 4 states Background: 4 states**

24

#### **HMM for CpG islands**


<!-- Start of picture text -->
A: 1  A: 0  A: 0  A: 0<br>C: 0  C: 1  C: 0  C: 0<br>G: 0  G: 0  G: 1  G: 0<br>T: 0  T: 0  T: 0  T: 1<br>A+ C+ G + T+<br>A- C- G - T-<br>A: 1  A: 0  A: 0  A: 0<br>C: 0  C: 1  C: 0  C: 0<br>G: 0  G: 0  G: 1  G: 0<br>T: 0  T: 0  T: 0  T: 1<br><!-- End of picture text -->

- A single model combines two Markov chains, each of four nucleotides:

   - **‘+’ states** : A+, C+, G+, T+

   - Emit symbols: A, C, G, T in CpG islands

   - – **‘-’ states** : A-, C-, G-, T-

- Emit symbols: A, C, G, T in non-islands

- • Emission probabilities distinct for the ‘+’ and the ‘-’ states

   - Infer most likely set of states, giving rise to observed emissions

   -  ‘Paint’ the sequence with + and - states

**Why we need so many states…**

**In our simple GC-content example, we only had 2 states (+|-) Why do we need 8 states here:  4 CpG+ / 4 CpG-  ?**

 **Encode ‘memory’ of previous state: nucleotide transitions**

25

#### **Training emission parameters for CpG+/CpG- states**


<!-- Start of picture text -->
aAT<br>A  T<br>aAC aGT<br>C  G<br>aGC<br><!-- End of picture text -->

- Count di-nucleotide frequencies:

   - 16 possible di-nucleotides. 16 transition parameters.

   - Alternative:  16 states, each emitting di-nucleotide

   - Derive two Markov chain models:

-

   - **‘+’ model** : from the CpG islands

   - **‘-’ model** : from the remainder of sequence

- Transition probabilities for each model:

   - Encode differences in di-nucleotide frequencies

|**+**|**A**|**C**|**G**|**T**|
|---|---|---|---|---|
|**A**|.180|.274|.426|.120|
|**C**|.171|.368|**.274**|.188|
|**G**|.161|.339|.375|.125|
|**T**|.079|.355|.384|.182|


|**-**|**A**|**C**|**G**|**T**|
|---|---|---|---|---|
|**A**|.300|.205|.285|.210|
|**C**|.322|.298|**.078**|.302|
|**G**|.248|.246|.298|.208|
|**T**|.177|.239|.292|.292|


26

#### **Examples of HMMs for genome annotation**

|**Detection**<br>**of GC-rich**<br>**regions**|**Detection**<br>**of CpG-rich**<br>**regions**|**Detection**<br>**of**<br>**conserved**<br>**regions**|**Detection**<br>**of protein-**<br>**coding**<br>**exons**|**Detection**<br>**of protein-**<br>**coding**<br>**conservatio**<br>**n**|**Detection**<br>**of protein-**<br>**coding**<br>**gene**<br>**structures**|**Detection**<br>**of**<br>**chromatin**<br>**states**|
|---|---|---|---|---|---|---|
|2 states,<br>different<br>nucleotide<br>composition|8 states,<br>4 each +/-,<br>different<br>transition<br>probabilities|2 states,<br>different<br>conservation<br>levels|2 states,<br>different tri-<br>nucleotide<br>composition|2 states,<br>different<br>evolutionary<br>signatures|~20 states,<br>different<br>composition/<br>conservation<br>, specific<br>structure|40 states,<br>different<br>chromatin<br>mark<br>combination<br>s|
|GC-rich / AT-<br>rich|CpG-rich /<br>CpG-poor|Conserved /<br>non-<br>conserved|Coding exon<br>/ non-coding<br>(intron or<br>intergenic)|Coding exon<br>/ non-coding<br>(intron or<br>intergenic)|First/last/mid<br>dle coding<br>exon,UTRs,<br>intron1/2/3,<br>intergenic,<br>*(+/- strand)|Enhancer /<br>promoter /<br>transcribed /<br>repressed /<br>repetitive|
|Nucleotides|Di-<br>Nucleotides|Level of<br>conservation|Triplets of<br>nucleotides|64x64 matrix<br>of codon<br>substitution<br>frequencies|Codons,<br>nucleotides,<br>splice sites,<br>start/stop<br>codons|Vector of<br>chromatin<br>mark<br>frequencies<br>27|


#### **HMM architecture matters: Protein-coding genes**


- © Bill Majoros / GeneZilla. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- Gene vs. Intergenic

- Start & Stop in/out

- UTR: 5’ and 3’ end

- Exons, Introns

- Remembering frame

   - E0,E1,E2

   - I0,I1,I2

- Sequence patterns to transition between states:

   - ATG, TAG, Acceptor/Donor, TATA, AATAA

28

#### **Chromatin State: Emission & Transition Matrices**


© Macmillan Publishers Limited. All rights reserved. This content is excluded from our Creative Commons license. For more information,see http://ocw.mit.edu/help/faq-fair-use/. Source: Ernst, Jason and Manolis Kellis. "Discovery and characterization of chromatin states for systematic                                                     Nature Biotechnology 28, no. 8 (2010): 817-825.annotation of the human genome.“

- **Emission matrix:**

   - Multi-variate HMM

   - Emits vector of values

- **Transition matrix:**

   - Learn spatial relationships

   - No a-priori ‘gene’ structure

**Ernst and Kellis, Nature Biotech 2010, Nature 2011, Nature Methods 2012**

29

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

30

######

#### **One path**

#### **All paths**

1.  Scoring x, one path

   2.  Scoring x, all paths

- P(x,π)

  P(x) = Σπ P(x,π)

- Prob of a path, emissions

   - Prob of emissions, over all paths

3. Viterbi decoding

      4.  Posterior decoding

   - π^ = {πi | πi=argmaxk ΣπP(πi=k|x)}

   -

- π* = argmaxπ P(x,π)

   - Path containing the most likely state at any time point.

- Most likely path

5. Supervised learning, given π Λ* = argmaxΛ P(x,π|Λ)

      6.  Unsupervised learning

         - Λ* = argmaxΛ ΣπP(x,π|Λ)

6. Unsupervised learning.

   - Λ* = argmaxΛ maxπP(x,π|Λ) Viterbi training, best path

Baum-Welch training, over all paths

31

#### **4. Decoding, all paths**

Find the likelihood an emission xi is generated by a state

32

#### **Calculate most probable label at a single position**

**π:**


<!-- Start of picture text -->
x:<br><!-- End of picture text -->


<!-- Start of picture text -->
Sum over all paths<br>P  P  P  P  P  P  P  P<br>B  B  B  B  B  B  B  B<br>G  C  A  A  A  T  G  C<br><!-- End of picture text -->

###### **P(Labeli=B|x)**

- Calculate most probable label, L<sup>*</sup> i<sup>, at each position i</sup>

- • Do this for all N positions gives us {L<sup>*</sup> 1<sup>, L*</sup> 2<sup>, L*</sup> 3<sup>…. L*</sup> N<sup>}</sup>

- How much information have we observed? Three settings: – **Observed nothing: Use prior information**

   - **Observed only character at position i:  Prior + emission probability**

   - **Observed entire sequence: Posterior decoding**

33

#### **Calculate P(π7=** **`CpG+` | x7=G)**

- With no knowledge (no characters)

   - Simply time spent in markov chain states

   - P( πi=k ) =  most likely state ( **prior** )

- With very little knowledge (just that character) – Time spent, adjusted for different emission probs. – Use Bayes rule to change inference directionality

   - P( πi=k | xi=G ) = P(πι=κ) * P(xi=G|πi=k) / P(xi=G)

- With knowledge of entire sequence (all characters) – P( πi=k | x=AGCGCG…GATTATCGTCGTA)

   - Sum over all paths that emit ‘G’ at position 7

 **Posterior** decoding

34

#### **Motivation for the Backward Algorithm**

We want to compute

P(i = k | x), the probability distribution on the i<sup>th</sup> position, given x

We start by computing

P(i = k, x) = P(x1…xi, i = k, xi+1…xN) = P(x1…xi, i = k) P(xi+1…xN | x1…xi, i = k) <mark>= P(x</mark> 1 <mark>…x</mark> i <mark>, </mark> i <mark>= k) P(x</mark> i+1 <mark>…x</mark> N <mark>| </mark> i <mark>= k)</mark>

Forward, fk(i) Backward, bk(i)

35

#### **The Backward Algorithm – derivation**

###### Define the backward probability:

bk(i) = P(xi+1…xN | i = k) = i+1…N P(xi+1,xi+2, …, xN, i+1, …, N | i = k)

= l i+1…N P(xi+1,xi+2, …, xN, i+1 = l, i+2, …, N | i = k)

= l el(xi+1) akl <mark></mark> i+1…N <mark>P(x</mark> i+2 <mark>, …, x</mark> N <mark>, </mark> i+2 <mark>, …, </mark> N <mark>| </mark> i+1 <mark>= l)</mark> = l el(xi+1) akl <mark>b</mark> l <mark>(i+1)</mark>

36

#### **Calculate total end probability recursively**


<!-- Start of picture text -->
…<br>akl  l  bl(i+1)<br>hidden<br>bk(i)  k  …<br>states<br>el<br>…<br>observations  x i  x i+1<br>• Assume we know bl for the next time step (i+1)<br>• Calculate  bk(i)  =    suml (   el(xi+1)       akl         bl(i+1)  )<br>current max  next  transition  prob sum from<br>to next state  state l to end<br>emission<br>sum over all possible next states<br><!-- End of picture text -->

37

#### **The Backward Algorithm**


<!-- Start of picture text -->
State 1<br>2<br>bk(i)<br>K<br><!-- End of picture text -->

x1   x2   x3 ………………………………………..xN

Input: x = x1……xN

**<u>Initialization:</u>** bk(N) = ak0, for all k

**<u>In practice:</u>** Sum of log scores is difficult  approximate exp(1+p+q)  scaling of probabilities

**<u>Iteration:</u>**

bk(i) = l el(xi+1) akl bl(i+1)

**<u>Termination:</u>**

**<u>Running time and space:</u>** Time:    O(K<sup>2</sup> N) Space:  O(K)

P(x) = l a0l el(x1) bl(1)

38

#### **Putting it all together:  Posterior decoding**


<!-- Start of picture text -->
State 1<br>2<br>P(k)<br>K<br><!-- End of picture text -->

x1   x2   x3 ………………………………………..xN

- P(k) = P( πi=k | x ) = fk(i)*bk(i) / P(x)

   - Probability that i<sup>th</sup> state is k, given all emissions x

- Posterior decoding

   - Find the most likely state at position i over all possible hidden paths given the observed sequence x

   - <sup>^</sup> i<sup>= argmax</sup> k<sup>P(</sup> i<sup>= k | x)</sup>

- Posterior decoding ‘path’ <sup>^</sup> i

   - For classification, more informative than Viterbi path *

      - More refined measure of “which hidden states” generated x

   - However, it may give an invalid sequence of states

      - Not all jk transitions may be possible

39

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

- 4. Learning (ML training, Baum-Welch, Viterbi training) – Supervised: Find ei(.) and aij given labeled sequence

   - Unsupervised: given only x  annotation + params

40

#### **One path**

#### **All paths**

1.  Scoring x, one path

2.  Scoring x, all paths

P(x,π) Prob of a path, emissions

- P(x) = Σπ P(x,π)

 

   - Prob of emissions, over all paths

3. Viterbi decoding

      4.  Posterior decoding

      - π^ = {πi | πi=argmaxk ΣπP(πi=k|x)}

   - π* = argmaxπ P(x,π)

-  

- Most likely path Path containing the most likely state at any time point.

######

5. Supervised learning, given π Λ* = argmaxΛ P(x,π|Λ)

6. Unsupervised learning.

   - Λ* = argmaxΛ maxπP(x,π|Λ) Viterbi training, best path

6.  Unsupervised learning

   - Λ* = argmaxΛ ΣπP(x,π|Λ)

Baum-Welch training, over all paths

41

---

[Up: contents](index.md) · [Learning: How to train an HMM →](02-learning-how-to-train-an-hmm.md)

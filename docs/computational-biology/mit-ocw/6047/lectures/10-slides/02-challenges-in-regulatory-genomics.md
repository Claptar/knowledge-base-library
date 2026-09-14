---
title: Challenges in regulatory genomics
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/10-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Challenges in regulatory genomics

**Source:** `lectures/10-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

TFs: Homology to TFs/domains miRNAs: Evolutionary signatures miRNAs: Experimental cloning

TFs: Selex, DIP-Chip, Protein-Binding-Microarrays miRNAs: Evolutionary/structural signatures miRNAs: Experimental cloning of 5’-ends

TFs/miRNAs: _De novo_ comparative discovery**

TFs: Mass Spec (difficult)


Regulator TF/miRNA

Motif Sequence specificity TFs: Enrichment in co-regulated genes/ bound regions **

Evolutionary footprints DNase footprints Chromatin ‘dips’

Network analysis (upcoming lecture)

Targets Functional instances

TFs: ChIP-Chip/ChIP-Seq TFs/miRs: Perturbation response

TFs/miRNAs: Evolutionary signatures** miRNAs: Composition/folding

* = Covered in today’s lecture

13

###### **Motif discovery overview**

1. Introduction to regulatory motifs / gene regulation – Two settings: co-regulated genes (EM,Gibbs), de novo

2. Expectation maximization: Motif matrixpositions – E step: Estimate motif positions Zij from motif matrix – M step: Find max-likelihood motif from all positions Zij

3. Gibbs Sampling: Sample from joint (M,Zij) distribution – Sampling motif positions based on the Z vector

- More likely to find global maximum, easy to implement

- 4. Evolutionary signatures for _de novo_ motif discovery – Genome-wide conservation scores, motif extension

- – Validation of discovered motifs: functional datasets

5. Evolutionary signatures for instance identification – Phylogenies, Branch length score  Confidence score

– Foreground vs. background. Real vs. control motifs.

14

## Enrichment-based discovery methods

**Given a set of co-regulated/functionally related genes, find common motifs in their promoter regions**


- **Align the promoters to each other using local alignment**

- **Use expert knowledge for what motifs should look like**

- **Find ‘median’ string by enumeration (motif/sample driven)**

• **Start with conserved blocks in the upstream regions**

15

###### **Starting positions**  **Motif matrix**

- given aligned sequences  easy to compute profile matrix

###### **shared motif**


<!-- Start of picture text -->
sequence positions<br>1  2  3  4  5  6  7  8<br>0.1  0.3  0.1  0.2  0.2  0.4  0.3  0.1<br>A<br>0.5  0.2  0.1  0.1  0.6  0.1  0.2  0.7<br>C<br>G  0.2  0.2  0.6  0.5  0.1  0.2  0.2  0.1<br>0.2 0.3  0.2  0.2 0.1  0.3  0.3  0.1<br>T<br><!-- End of picture text -->

   - **given profile matrix**

   -

- **easy to find starting position probabilities**

**Key idea:  Iterative procedure for estimating both, given uncertainty**

**(learning problem with hidden variables:  the starting positions)**

16

###### **Basic Iterative Approach**

Given: length parameter _W,_ training set of sequences set initial values for **motif** do

 re-estimate **_starting-positions_** from **_motif_**  re-estimate **_motif_** from **_starting-positions_** until convergence (change < ε) return: **_motif, starting-positions_**

17

###### **Representing Motif M(k,c) and Background B(c)**

- Assume motif has fixed width, _W_

• Motif represented by matrix of probabilities: **_M(k,c)_** the probability of character **_c_** in column **_k_** **`1    2    3 A  0.1  0.5  0.2 C  0.4  0.2  0.1` (~CAG)**  _M_ **`G  0.3  0.1  0.6 T  0.2  0.2  0.1`** • **Background represented by B(c), frequency of each base** **`A  0.26 C  0.24` (near uniform)**  _B_ **`G  0.23` (see also: di-nucleotide etc)** **`T  0.27`**

18

###### **Representing the starting** **<u>position probabilities (Zij)</u>**

• the element        of the matrix       represents the _Z Z ij_ probability that the motif starts in position _j_ in sequence _i_ **`1    2    3    4 seq1  0.1  0.1  0.2  0.6`**  **`seq2  0.4  0.2  0.1  0.3`** _Z_ **`seq3  0.3  0.1  0.5  0.1 seq4  0.1  0.5  0.1  0.3`**

**Some examples:**

**no clear winner two candidates one big winner uniform**


**Z1 Z2 Z3**

**Z4**

19

###### **Starting positions (Zij)**  **Motif matrix M(k,c)**


<!-- Start of picture text -->
X1 k=1 k=2 k=3 k=4 k=5 k=6 k=7 k=8<br>c=A  0.1  0.3  0.1  0.2  0.2  0.4  0.3  0.1<br>X2 M-step<br>X3 c=C  0.5  0.2  0.1  0.1  0.6  0.1  0.2  0.7<br>…<br>Xi  c=G  0.2  0.2  0.6  0.5  0.1  0.2  0.2  0.1<br>E-step<br>… c=T  0.2 0.3  0.2  0.2 0.1  0.3  0.3  0.1<br>Xn<br><!-- End of picture text -->

**Starting positions:  Zij**

**Motif:  M(k,c)**

   - Zij:  Probability that on sequence i, motif start at position j

   - M(k,c): Probability that k<sup>th</sup> character of motif is letter c

- **Computing Zij matrix from M(k,c) is straightforward** – **At each position, evaluate start probability by multiplying across the matrix**

- **Three variations for re-computing motif M(k,c) from Zij matrix**

      - **Expectation maximization**  **All starts weighted by Zij prob distribution**

      - **Gibbs sampling**

      - **Gibbs sampling**  **Single start for each seq Xi by sampling Zij**

      - – **Greedy approach**  **Best start for each seq Xi by maximum Zij**

20

###### **Motif discovery overview**

1. Introduction to regulatory motifs / gene regulation – Two settings: co-regulated genes (EM,Gibbs), de novo

2. Expectation maximization: Motif matrixpositions

- <mark>E step: Estimate motif positions Z</mark> ij <mark>from motif matrix</mark>

- – M step: Find max-likelihood motif from all positions Zij

- 3. Gibbs Sampling: Sample from joint (M,Zij) distribution – Sampling motif positions based on the Z vector

- More likely to find global maximum, easy to implement

- 4. Evolutionary signatures for _de novo_ motif discovery

   - Genome-wide conservation scores, motif extension

- Validation of discovered motifs: functional datasets

- 5. Evolutionary signatures for instance identification – Phylogenies, Branch length score  Confidence score

- – Foreground vs. background. Real vs. control motifs.

21

### **E-step:**

### **Estimate Zij positions from matrix**


<!-- Start of picture text -->
k=1  k=2  k=3  k=4  k=5  k=6  k=7  k=8<br>X1<br>X2  c=A  0.1  0.3  0.1  0.2  0.2  0.4  0.3  0.1<br>X3  c=C  0.5  0.2  0.1  0.1  0.6  0.1  0.2  0.7<br>…<br>Xi  c=G  0.2  0.2  0.6  0.5  0.1  0.2  0.2  0.1<br>E-step<br>… c=T  0.2 0.3  0.2  0.2 0.1  0.3  0.3  0.1<br>Xn<br>Starting positions:  Zij  Motif:  M(k,c)<br><!-- End of picture text -->

22

###### **Three examples for Greedy, Gibbs Sampling, EM**


<!-- Start of picture text -->
Greedy always picks maximum<br>Gibbs sampling picks one at random<br>(or)  two<br>Z1  candidates<br>(and)<br>EM uses both in estimating motif<br><!-- End of picture text -->


<!-- Start of picture text -->
All methods agree<br>Z2<br><!-- End of picture text -->

**one big winner**

**Greedy ignores most of the probability Gibbs sampling rapidly converges to some choice**

**uniform Z3 EM averages over the entire sequence (slow/no convergence)**

23

###### **Calculating P(** **_Xi_ ) when motif position is known**


<!-- Start of picture text -->
•<br>Probability of training sequence Xi, given hypothesized start position j<br> <br>j 1 j  W 1 L<br>  <br>Pr( X i | Zij ,1 M , B )  B ( X i , k )  M ( k j  ,1 X i , k )  B ( X i , k )<br>k  1 k  j k  j  W<br>before motif  motif  after motif<br><!-- End of picture text -->

• **Example:** **`1    2    3 A  0.25 A  0.1  0.5  0.2`** _X_  **`G C T G T A G`**  **`C  0.25`**  **`C  0.4  0.2  0.1`** _B M i_ **`G  0.25 G  0.3  0.1  0.6 T  0.25 T  0.2  0.2  0.1`**   _X Z M B_ Pr( _i_ | _i_ 3 ,1 , ) B(G)  _B_ ( _C_ )  _M_ ,1( _T_ )  _M_ (,2 _G_ )  _M_ (,3 _T_ )  _B_ ( _A_ )  _B_ ( _G_ )  0.25  0.25  2.0  1.0  1.0  0.25  0.25

24

###### **Calculating the Z vector   ( using M )**

• **To estimate the starting positions in** **_Z_ at step** **_t_ likelihood prior** ( _t_ )   ( _t_ ) ( _t_ ) Pr( _X i_ | _Zij_ ,1 _M_ ) Pr( _Zij_ )1    _Z Z X M ij_ Pr( _ij_ |1 _i_ , ) **posterior** Pr( _X i_ ) **evidence**

**(Bayes’ rule)**

- At iteration t, calculate _Zij_ (t) based on M _(t)_

   - We just saw how to calculate Pr( _Xi_ | _Zij_ =1,M<sup>_(t)_</sup> )

   - To obtain total probability Pr( _Xi_ ), sum over all starting positions

( _t_ )   ( _t_ ) Pr( _X i_ | _Zij_ ,1 _M_ ) Pr( _Zij_ )1  _Z_  _ij L W_  1 ( _t_ )   Pr( _X i_ | _Zik_ ,1 _M_ ) Pr( _Zik_ )1  _k_  1

- **Assume uniform priors (motif eq likely to start at any position)**

25

###### **Calculating the Z vector:  Example**


<!-- Start of picture text -->
<br>X G C T G  T A G<br>i<br>      0     1    2    3<br>A  0.25   0.1  0.5  0.2<br>C  0.25    0.4  0.2   0.1<br>p <br>G  0.25    0.3   0.1   0.6<br>T  0.25   0.2   0.2  0.1<br><br>3.0  2.0  1.0  .025  .025  .025  .025<br>Z i 1<br><br>.025  4.0  2.0  6.0  .025  .025  .025<br>Z i 2<br><br>L W  1<br>•<br>then normalize so that<br><br>Z 1<br> ij<br>j  1<br>...<br><!-- End of picture text -->

26

###### **Aside: Simplifying P(** **_Xi_ )**


<!-- Start of picture text -->
•<br>Probability of training sequence Xi, given hypothesized start position j<br> <br>j 1 j  W 1 L<br>  <br>Pr( X i | Zij ,1 M , B )  B ( X i , k )  M ( k j  ,1 X i , k )  B ( X i , k )<br>k  1 k  j k  j  W<br>before motif  motif  after motif<br><br>j  W 1  L<br>M ( k j  ,1 X i , k )<br><br>  B ( X i , k )<br>B X<br>k  j ( i , k ) k  1<br>can be stored in   constant for<br>a matrix  each sequence<br><!-- End of picture text -->

27

###### **Motif discovery overview**

1. Introduction to regulatory motifs / gene regulation – Two settings: co-regulated genes (EM,Gibbs), de novo 2. Expectation maximization: Motif matrixpositions – E step: Estimate motif positions Zij from motif matrix <mark>– M step: Find max-likelihood motif from all positions Z</mark> ij 3. Gibbs Sampling: Sample from joint (M,Zij) distribution – Sampling motif positions based on the Z vector

- More likely to find global maximum, easy to implement

- 4. Evolutionary signatures for _de novo_ motif discovery

- Genome-wide conservation scores, motif extension

- – Validation of discovered motifs: functional datasets

- 5. Evolutionary signatures for instance identification – Phylogenies, Branch length score  Confidence score

- – Foreground vs. background. Real vs. control motifs.

28

### **M-step: Max-likelih motif from Zij positions**


<!-- Start of picture text -->
k=1  k=2  k=3  k=4  k=5  k=6  k=7  k=8<br>X1<br>X2  c=A  0.1  0.3  0.1  0.2  0.2  0.4  0.3  0.1<br>X3  c=C  0.5  0.2  0.1  0.1  0.6  0.1  0.2  0.7<br>…<br>Xi  c=G  0.2  0.2  0.6  0.5  0.1  0.2  0.2  0.1<br>M-step<br>… c=T  0.2 0.3  0.2  0.2 0.1  0.3  0.3  0.1<br>Xn<br>Starting positions:  Zij  Motif: M(k,c)<br><!-- End of picture text -->

29

###### **The M-step: Estimating the motif** **_M_**


<!-- Start of picture text -->
•<br>M k c<br>recall                  represents the probability of  character  ( , ) c  in<br>position  k  ;             stores values for the background  B ( c )<br>n  d<br>( t  1) k , c<br><br>M k c<br>( , ) pseudo-counts<br>( nk c  d )<br> ,<br>c<br><br>where  n Z<br>c k<br>,   ij<br>i { j | X i , j  k  1  c }<br>total # of c’s<br>in data set<br>n  d<br>( t  1) 0, c W<br><br>B c<br>( ) where  <br>n  n n<br>n  d c c c<br>( c ) ,0  j ,<br> ,0<br>c j  1<br><!-- End of picture text -->

30

###### **M-step example: Estimating M(k,c) from Zij**

**`A`** **<mark>`C A G`</mark>** **`C A` X1 =**

**Z1 =  0.1  0.7  0.1  0.1**

**`A G G`** **<mark>`C A G`</mark> X2 =**

**Z2 =  0.4  0.1  0.1 0.4**

- EM: sum over full probability – n1,A= 0.1+0.1+0.4+0.1 = 0.7 – n1,C= 0.7+0.4+0.6 = 1.7 – n1,G= 0.1+0.1+0.1+0.1= 0.4

   - n1,T= 0.2 = 0.2

   - – Total:  T=0.7+1.7+0.4+0.2 = 3.0

**`T`** **<mark>`C A G`</mark>** **`T C` X3 =**

**Z3 =  0.2  0.6  0.1  0.1**

_Z_  _Z_  _Z_  _Z_  1 1,1 1,3 2,1 3,3 _M_ ,1( _A_ )  _Z_ 1,1  _Z_ ,12 ...  _Z_ 3,3  _Z_ ,34  4

**Em approach: Avg’em all Gibbs sampling: Sample one Greedy: Select max**

- Normalize and add pseudo-counts – M(1,A) = (0.7+1)/(T+4) = 1.7/7=0.24 – M(1,C) = (1.7+1)/(T+4) = 2.7/7=0.39 – M(1,G) = (0.4+1)/(T+4) = 1.4/7=0.2 – M(1,T) = (0.2+1)/(T+4) = 1.2/7=0.17

|||**1**|**2**|**3**|
|---|---|---|---|---|
||**A**|0.24|0.39|0.21|
|•<br>M(kc) =|**C**|0.39|0.21|0.18|
|,|**G**|0.2|0.24|0.44|
||**T**|0.17|0.16|0.16|


31

###### **The EM Algorithm**

- EM converges to a local maximum in the likelihood of the data given the model:

_X M B_ Pr( _i_ | , )  _i_

- **Deterministic iterations max direction of ascent**

- **Usually converges in a small number of iterations**

- **Sensitive to initial starting point (i.e. values in** **_M_ )**

32

###### **P(Seq|Model) Landscape**

**EM searches for parameters to increase P(seqs|parameters)**

Useful to think of P(seqs|parameters) as a function of parameters

EM starts at an initial set of parameters

And then “climbs uphill” until it reaches a local maximum


<!-- Start of picture text -->
P(Sequences|params1,params2)<br><!-- End of picture text -->


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**_Where EM starts can make a big difference_**

33

###### **One solution: Search from Many Different Starts**

**To minimize the effects of local maxima, you should search multiple times from different starting points**

###### MEME uses this idea

Start at many points Run for one iteration

Choose starting point that got the “highest” and continue


<!-- Start of picture text -->
P(Sequences|params1,params2)<br><!-- End of picture text -->


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

34

###### **Motif discovery overview**

1. Introduction to regulatory motifs / gene regulation – Two settings: co-regulated genes (EM,Gibbs), de novo 2. Expectation maximization: Motif matrixpositions – E step: Estimate motif positions Zij from motif matrix – M step: Find max-likelihood motif from all positions Zij

3. Gibbs Sampling: Sample from joint (M,Zij) distribution – Sampling motif positions based on the Z vector

- More likely to find global maximum, easy to implement

- 4. Evolutionary signatures for _de novo_ motif discovery – Genome-wide conservation scores, motif extension

- – Validation of discovered motifs: functional datasets

5. Evolutionary signatures for instance identification – Phylogenies, Branch length score  Confidence score

– Foreground vs. background. Real vs. control motifs.

35

#### **Three options for assigning points, and their parallels across K-means, HMMs, Motifs**

|**ate rule**|**Update**<br>**assignments**<br>**(E step)**|**Algorit**<br>**in eac**<br>|**hm implementi**<br>**h of the three**<br>|**ng E step**<br>**settings **<br>|**Update**<br>**model**<br>**parameters**|
|---|---|---|---|---|---|
|**Upd**|**Estimate hidden**<br>**labels**|**Expression**<br>**clustering**|**HMM**<br>**learning**|**Motif**<br>**discovery**|**(M step)**<br>**max**<br>|
|The|hidden label is:|Cluster labels|State path π|Motif positions|**likelihood**|
|Pick a best|Assign each point<br>to best label|**K-means:**<br>Assign each<br>point to nearest<br>cluster|**Viterbi**<br>**training:**label<br>sequence with<br>best path|**Greedy:**Find<br>best motif match<br>in each sequence|Average of<br>those points<br>assigned to<br>label|
|Average all|Assign each point<br>to all labels,<br>probabilistically|**Fuzzy K-**<br>**means:**Assign<br>to all clusters,<br>weighted by<br>proximity|**Baum-Welch**<br>**training:**label<br>sequence w all<br>paths (posterior<br>decoding)|**MEME:**Use all<br>positions as a<br>motif occurrence<br>weighed by motif<br>match score|Average of all<br>points,<br>weighted by<br>membership|
|Sample one|Pick one label at<br>random, based on<br>their relative<br>probability|**N/A:**Assign to<br>a random<br>cluster, sample<br>by proximity|**N/A:**Sample a<br>single label for<br>each position,<br>according to<br>posteriorprob.|**Gibbs sampling:**<br>Use one position<br>for the motif, by<br>sampling from the<br>match scores|Average of<br>those points<br>assigned to<br>label(a<br>sample)|


36

###### **Three examples of Greedy, Gibbs Sampling, EM**


<!-- Start of picture text -->
Greedy always picks maximum<br>Gibbs sampling picks one at random<br>(or)  two<br>Z1  candidates<br>(and)<br>EM uses both in estimating motif<br>All methods agree  one big<br>winner<br>Z2<br><!-- End of picture text -->

**Greedy ignores most of the probability Gibbs sampling rapidly converges to some choice**

**uniform Z3**

**EM averages over the entire sequence (no preference)**

37

###### **Gibbs Sampling**

• A general procedure for sampling from the joint distribution of a set of random variables                              by iteratively sampling from Pr( _U_ 1... _U n_ ) for each _j_ Pr( _U_ | _U_ 1... _U_  1, _U_  1... _Un_ ) _j j j_ • Useful when it’s hard to explicitly express means, stdevs, covariances across the multiple dimensions

- Useful for supervised, unsupervised, semi-supervised learning – Specify variables that are known, sample over all other variables

- Approximate:

   - Joint distribution: the samples drawn

   - Marginal distributions: examine samples for subset of variables

   - Expected value: average over samples

- Example of Markov-Chain Monte Carlo (MCMC)

   - The sample approximates an unknown distribution

   - Stationary distribution of sample (only start counting after burn-in)

   - Assume independence of samples (only consider every 100)

- Special case of Metropolis-Hastings

   - In its basic implementation of sampling step

   - But it’s a more general sampling framework

38

###### **Gibbs Sampling for motif discovery**

- First application to motif finding: Lawrence et al 1993

   - Can view as a stochastic analog of EM for motif discovery task

   - Less susceptible to local minima than EM

- EM maintains distribution **_Zi_** over the starting points for each seq

- Gibbs sampling selects specific starting point **ai** for each seq  but keeps resampling these starting points

given: length parameter _W,_ training set of sequences choose random positions for _a_ do

pick a sequence **_Xi_**

estimate **_p_** given current motif positions _a_ (update step) (using all sequences but _Xi_ )

sample a new motif position _ai_ for _Xi_ (sampling step) until convergence

return: _p, a_

39

###### **Popular implementation: AlignACE, BioProspector**

AlignACE: first statistical motif finder BioProspector: improved version of AlignACE

###### <u>Both use basic Gibbs Sampling algorithm:</u>

1. <u>Initialization:</u>

- a. Select random locations in sequences X1, …, XN

- b. Compute an initial model M from these locations

- 2. <u>Sampling Iterations:</u>

   - a. Remove one sequence Xi

   - b. Recalculate model

   - c. Pick a new location of motif in Xi  according to probability the location is a motif occurrence

- <u>In practice, run algorithm from multiple random initializations:</u>

1. Initialize

2. Run until convergence

3. Repeat 1,2 several times, report common motifs

40

###### **Gibbs Sampling (AlignACE)**

• Given:

– X1, …, XN, _N W M k X_ – motif length W, log ( , _i_ , _ai_  _k_ ) – background B,  _i_  1 _k_  1 _B_ ( _X i_ , _ai_  _k_ )

- Find:

– Model M

– Locations a1,…, aN in X1, …, XN

Maximizing log-odds likelihood ratio This is the same as the EM objective (notice log and notation change)

41

###### **Gibbs Sampling (AlignACE)**

###### <u>Predictive Update:</u>

- Select a sequence xi

- Remove xi, recompute model:


**M**  _d_  ( _X s a_  _k c_ ) <u></u> _<u>s</u>_ <u></u> _<u>i</u>_ , _s_  _M k c_ ( , )  ( _N_ )1  4 _d_

##### where d is a pseudocount  to avoid 0s

42

###### **Sampling New Motif Positions**

- for each possible starting position, _ai=j_ , compute a weight


<!-- Start of picture text -->
<br> W 1<br>j M ( k  j  ,1 X i , k )<br><br>A<br>j <br>B X<br>k  j ( i , k )<br>•<br>randomly select a new starting position  ai  according to these weights<br>(normalizing across the sequence, again like with MEME)<br>•<br>Note, this is equivalent to using the likelihood from MEME because:<br>Aj  Pr( X i | Zij  ,1 p )<br><!-- End of picture text -->

**Prob**

**0**

**|x|**

43

###### **Advantages / Disadvantages**

- Very similar to EM

###### **<u>Advantages:</u>**

- Easier to implement

- Less dependent on initial parameters

- More versatile, easier to enhance with heuristics

###### **<u>Disadvantages:</u>**

- More dependent on all sequences to exhibit the motif

- Less systematic search of initial parameter space

44

###### **Gibbs Sampling and Climbing**

**Because gibbs sampling does always choose the best new location it can move to another place not directly uphill**


<!-- Start of picture text -->
P(Sequences|params1,params2)<br><!-- End of picture text -->


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**_In theory,_ Gibbs Sampling less likely to get stuck a local maxima**

45

###### **Motif discovery overview**

1. Introduction to regulatory motifs / gene regulation – Two settings: co-regulated genes (EM,Gibbs), de novo

2. Expectation maximization: Motif matrixpositions – E step: Estimate motif positions Zij from motif matrix

– M step: Find max-likelihood motif from all positions Zij

3. Gibbs Sampling: Sample from joint (M,Zij) distribution – Sampling motif positions based on the Z vector

– More likely to find global maximum, easy to implement

4. Evolutionary signatures for _de novo_ motif discovery – Genome-wide conservation scores, motif extension

– Validation of discovered motifs: functional datasets

5. Evolutionary signatures for instance identification – Phylogenies, Branch length score  Confidence score – Foreground vs. background. Real vs. control motifs.

46

###### **Motivation for** **_de novo_ genome-wide motif discovery**

- Both TF and region centric approaches are not comprehensive and are biased

- • TF centric approaches generally require transcription factor (or antibody to factor) – Lots of time and money

   - Also have computational challenges

- _De novo_ discovery using conservation is unbiased but can’t match motif to factor and require multiple genomes

47

### Evolutionary signatures for regulatory motifs

###### **Known engrailed binding site**

**_D.mel_**


```
D.mel  CAGCT--AGCC-AACTCTCTAATTAGCGACTAAGTC-CAAGTC
D.sim  CAGCT--AGCC-AACTCTCTAATTAGCGACTAAGTC-CAAGTC
D.sec  CAGCT--AGCC-AACTCTCTAATTAGCGACTAAGTC-CAAGTC
D.yak  CAGC--TAGCC-AACTCTCTAATTAGCGACTAAGTC-CAAGTC
D.ere  CAGCGGTCGCCAAACTCTCTAATTAGCGACCAAGTC-CAAGTC
D.ana  CACTAGTTCCTAGGCACTCTAATTAGCAAGTTAGTCTCTAGAG
       **       *    * *********** *   **** * **
```

•Start by looking at known motif instances •Individual motif instances are preferentially conserved •Can we just take conservation islands and call them motifs?

– No. Many conservation islands are due to chance or perhaps due to non-motif conservation

**Kellis** **_el al,_ Nature 2003 Xie** **_et al._ Nature 2005 Stark** **_et al_ , Nature 2007**

48

### Conservation islands overlap known motifs


<!-- Start of picture text -->
TBP<br>Scer   TATCCATATCTAATCTTACTTATATGTTGT-GGAAAT-GTAAAGAGCCCCATTATCTTAGCCTAAAAAAACC--TTCTCTTTGGAACTTTCAGTAATACG<br>Spar   TATCCATATCTAGTCTTACTTATATGTTGT-GAGAGT-GTTGATAACCCCAGTATCTTAACCCAAGAAAGCC--TT-TCTATGAAACTTGAACTG-TACG<br>Smik   TACCGATGTCTAGTCTTACTTATATGTTAC-GGGAATTGTTGGTAATCCCAGTCTCCCAGATCAAAAAAGGT--CTTTCTATGGAGCTTTG-CTA-TATG<br>Sbay   TAGATATTTCTGATCTTTCTTATATATTATAGAGAGATGCCAATAAACGTGCTACCTCGAACAAAAGAAGGGGATTTTCTGTAGGGCTTTCCCTATTTTG<br>       **   ** ***  **** ******* **   *  *   *     *  *    *  *       **  **      * *** *    ***    *  *  *<br>GAL4  GAL4  GAL4<br>Scer   CTTAACTGCTCATTGC-----TATATTGAAGTACGGATTAGAAGCCGCCGAGCGGGCGACAGCCCTCCGACGGAAGACTCTCCTCCGTGCGTCCTCGTCT<br>Spar   CTAAACTGCTCATTGC-----AATATTGAAGTACGGATCAGAAGCCGCCGAGCGGACGACAGCCCTCCGACGGAATATTCCCCTCCGTGCGTCGCCGTCT<br>Smik   TTTAGCTGTTCAAG--------ATATTGAAATACGGATGAGAAGCCGCCGAACGGACGACAATTCCCCGACGGAACATTCTCCTCCGCGCGGCGTCCTCT<br>Sbay   TCTTATTGTCCATTACTTCGCAATGTTGAAATACGGATCAGAAGCTGCCGACCGGATGACAGTACTCCGGCGGAAAACTGTCCTCCGTGCGAAGTCGTCT<br>             **  **          ** ***** ******* ****** ***** ***  ****   * *** ***** * *  ****** ***    * ***<br>GAL4<br>Scer   TCACCGG-TCGCGTTCCTGAAACGCAGATGTGCCTCGCGCCGCACTGCTCCGAACAATAAAGATTCTACAA-----TACTAGCTTTT--ATGGTTATGAA<br>Spar   TCGTCGGGTTGTGTCCCTTAA-CATCGATGTACCTCGCGCCGCCCTGCTCCGAACAATAAGGATTCTACAAGAAA-TACTTGTTTTTTTATGGTTATGAC<br>Smik   ACGTTGG-TCGCGTCCCTGAA-CATAGGTACGGCTCGCACCACCGTGGTCCGAACTATAATACTGGCATAAAGAGGTACTAATTTCT--ACGGTGATGCC<br>Sbay   GTG-CGGATCACGTCCCTGAT-TACTGAAGCGTCTCGCCCCGCCATACCCCGAACAATGCAAATGCAAGAACAAA-TGCCTGTAGTG--GCAGTTATGGT<br>            ** *   ** *** *      *      ***** ** *  *   ****** **     *   * **     * *             ** ***<br>MIG1<br>Scer   GAGGA-AAAATTGGCAGTAA----CCTGGCCCCACAAACCTT-CAAATTAACGAATCAAATTAACAACCATA-GGATGATAATGCGA------TTAG--T<br>Spar   AGGAACAAAATAAGCAGCCC----ACTGACCCCATATACCTTTCAAACTATTGAATCAAATTGGCCAGCATA-TGGTAATAGTACAG------TTAG--G<br>Smik   CAACGCAAAATAAACAGTCC----CCCGGCCCCACATACCTT-CAAATCGATGCGTAAAACTGGCTAGCATA-GAATTTTGGTAGCAA-AATATTAG--G<br>Sbay   GAACGTGAAATGACAATTCCTTGCCCCT-CCCCAATATACTTTGTTCCGTGTACAGCACACTGGATAGAACAATGATGGGGTTGCGGTCAAGCCTACTCG<br>              ****    *         *    *****     ***               * * *    *  * *    *     *           **<br>MIG1  TBP<br>Scer   TTTTTAGCCTTATTTCTGGGGTAATTAATCAGCGAAGCG--ATGATTTTT-GATCTATTAACAGATATATAAATGGAAAAGCTGCATAACCAC-----TT<br>Spar   GTTTT--TCTTATTCCTGAGACAATTCATCCGCAAAAAATAATGGTTTTT-GGTCTATTAGCAAACATATAAATGCAAAAGTTGCATAGCCAC-----TT<br>Smik   TTCTCA--CCTTTCTCTGTGATAATTCATCACCGAAATG--ATGGTTTA--GGACTATTAGCAAACATATAAATGCAAAAGTCGCAGAGATCA-----AT<br>Sbay   TTTTCCGTTTTACTTCTGTAGTGGCTCAT--GCAGAAAGTAATGGTTTTCTGTTCCTTTTGCAAACATATAAATATGAAAGTAAGATCGCCTCAATTGTA<br>        * *      *    ***       * **   *  *      *** ***    *  *  **  ** *  ********    ****    *<br>Scer   TAACTAATACTTTCAACATTTTCAGT--TTGTATTACTT-CTTATTCAAAT----GTCATAAAAGTATCAACA-AAAAATTGTTAATATAC<br>Spar   TAAATAC-ATTTGCTCCTCCAAGATT--TTTAATTTCGT-TTTGTTTTATT----GTCATGGAAATATTAACA-ACAAGTAGTTAATATAC  GAL1<br>Smik   TCATTCC-ATTCGAACCTTTGAGACTAATTATATTTAGTACTAGTTTTCTTTGGAGTTATAGAAATACCAAAA-AAAAATAGTCAGTATCT<br>Sbay   TAGTTTTTCTTTATTCCGTTTGTACTTCTTAGATTTGTTATTTCCGGTTTTACTTTGTCTCCAATTATCAAAACATCAATAACAAGTATTC<br>       *   *     *     *      * *  **  ***   *  *        *        *  ** **  ** * *  * *    * ***  ATGACTA<br>GAL4<br>Transcription factor binding  Conservation island<br><!-- End of picture text -->

###### **Increase power by testing conservation in many regions**

49

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Genome-wide conservation →](03-genome-wide-conservation.md)

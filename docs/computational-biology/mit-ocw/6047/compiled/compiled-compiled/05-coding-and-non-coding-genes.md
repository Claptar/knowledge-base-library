---
title: Coding and Non-Coding Genes
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/compiled/compiled-compiled.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Coding and Non-Coding Genes

**Source:** `compiled/compiled-compiled.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

127

## CHAPTER **SEVEN**

## HIDDEN MARKOV MODELS I

Anastasiya Belyaeva, Justin Gullingsrud (Sep 26, 2015) William Leiserson, Adam Sealfon (Sep 22, 2014) Haoyang Zeng (Sep 28, 2013) Sumaiya Nazeen (Sep 25, 2012) Chrisantha Perera (Sep 27, 2011) Gleb Kuznetsov, Sheida Nabavi (Sep 28, 2010) Elham Azizi (Sep 29, 2009)

### **Figures**

|7.1|Modeling biological sequences<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>129|
|---|---|---|
|7.2|Prediction Models Using Markov Chain and HMM . . . . . . . . . . . . . . . . . . . .|. .<br>130|
|7.3|Parameterization of HMM Prediction Model . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>130|
|7.4|State of a casino die represented by a Hidden Markov model. . . . . . . . . . . . . . .|. .<br>132|
|7.5|Potential DNA sources: viral injection vs. normal production . . . . . . . . . . . . . .|. .<br>132|
|7.6|A possible sequence of observed die rolls.<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>132|
|7.7|Running the model: probability of a sequence, given path consists of all fair dice . . .|. .<br>133|
|7.8|Running the model: probability of a sequence, given path consists of all loaded dice<br>.|. .<br>133|
|7.9|Partial runs and die switching . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>134|
|7.10|HMMS as a generative model for finding GC-rich regions. . . . . . . . . . . . . . . . .|. .<br>135|
|7.11|Probability of seq, path if all promoter . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>135|
|7.12|Probability of seq, path if all background<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>136|
|7.13|Probability of seq, path sequence if mixed . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>136|
|7.14|Some biological applications of HMM. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>137|
|7.15|The six algorithmic settings for HMMS<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>138|
|7.16|The Viterbi algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>140|
|7.17|The Forward algorithm<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>141|
|7.18|CpG Islands - Incorporating Memory<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>142|


## **7.1 Introduction**

Hidden Markov Models (HMMs) are a fundamental tool from machine learning that is widely used in computational biology. Using HMMs, we can explore the underlying structure of DNA or polypeptide sequences, detecting regions of especial interest. For instance, we can identify conserved subsequences or uncover regions with different distributions of nucleotides or amino acids such as promoter regions and CpG islands. Using this probabilistic model, we can illuminate the properties and structural components of sequences and locate genes and other functional elements.

129

6.047/6.878 Lecture 06: Hidden Markov Models I

This is the first of two lectures on HMMs. In this lecture we will define Markov Chains and HMMs, providing a series of motivating examples. In the second half of this lecture, we wil discuss scoring and decoding. We will learn how to compute the probability of the combination of a particular combination of observations and states. We will introduce the Forward Algorithm, a method for computing the probability of a given sequence of observations, allowing all sequences of states. Finally, we will discuss the problem of determining the most likely path of states corresponding to the given observations, a goal which is achieved by the Viterbi algorithm.

In the second lecture on HMMs, we will continue our discussion of decoding by exploring posterior decoding, which allows us to compute the most likely state at each point in the sequence. We will then explore how to learn a Hidden Markov Model. We cover both supervised and unsupervised learning, explaining how to use each to learn the model parameters. In supervised learning, we have training data available that labels sequences with particular models. In unsupervised learning, we do not have labels so we must seek to partition the data into discrete categories based on discovered probabilistic similarities. In our discussion of unsupervised learning we will introduce the general and widely applicable Expectation Maximization (EM) algorithm.

## **7.2 Motivation:**

### **7.2.1 We have a new sequence of DNA, now what?**

1. **Align it:**

   - with things we know about (database search).

   - with unknown things (assemble/clustering)

2. **Visualize it:** _“Genomics rule #1”: Look at your data!_

   - Look for nonstandard nucleotide compositions.

   - Look for k-mer frequencies that are associated with protein coding regions, recurrent data, high GC content, etc.

   - Look for motifs, evolutionary signatures.

   - Translate and look for open reading frames, stop codons, etc.

   - Look for patterns, then develop machine learning tools to determine reasonable probabilistic models. For example by looking at a number of quadruples we decide to color code them to see where they most frequently occur.

3. **Model it:**

   - Make hypothesis.

   - Build a generative model to describe the hypothesis.

   - Use that model to find sequences of similar **type** .

We’re not looking for sequences that necessarily have common ancestors. Rather, we’re interested in sequences with similar properties. We actually don’t know how to model whole genomes, but we can model small aspects of genomes. The task requires understanding all the properties of genome regions and computationally building generative models to represent hypotheses. For a given sequence, we want to annotate regions whether they are introns, exons, intergenic, promoter, or otherwise classifiable regions.

Building this framework will give us the ability to:

- Emit (generate) sequences of similar type according to the generative model

- Recognize the hidden state that has most likely generated the observation

130

6.047/6.878 Lecture 06: Hidden Markov Models I


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 7.1: Modeling biological sequences

- Learn (train) large datasets and apply to both previously labeled data (supervised learning) and unlabeled data (unsupervised learning).

In this lecture we discuss algorithms for emission and recognition.

### **7.2.2 Why probabilistic sequence modeling?**

- Biological data is noisy.

- Update previous knowledge about biological sequences.

- Probability provides a calculus for manipulating models.

- Not limited to yes/no answers, can provide degrees of belief.

- Many common computational tools are based on probabilistic models.

- Our tools: Markov Chains and HMM.

## **7.3 Markov Chains and HMMS: From Example To Formalizing**

### **7.3.1 Motivating Example: Weather Prediction**

Weather prediction has always been difficult, especially when we would like to forecast the weather many days, weeks or even months later. However, if we only need to predict the weather of the next day, we can reach decent prediction precision using some quite simple models such as Markov Chain and Hidden Markov Model by building graphical models in Figure 7.2.

For the Markov Chain model on the left, four kinds of weather (Sun, Rain, Clouds and Snow) can directly transition from one to the other. This is a “what you see is what you get” in that the next state only depends on the current state and there is no memory of the previous state. However for HMM on the right, all the types of weather are modeled as the emission(or outcome) of the hidden seasons (Summer, Fall, Winter and Spring). The key insight behind is that the hidden states of the world (e.g. season or storm system) determines emission probabilities while state transitions are governed by a Markov Chain.

### **7.3.2 Formalizing of Markov Chain and HMMS**

To take a closer look at Hidden Markov Model, let’s first define the key parameters in Figure 7.3. Vector _x_ represents sequence of observations. Vector _π_ represents the hidden path, which is the sequence of hidden states. Each entry _akl_ of Transition matrix _A_ denotes the probability of transition from state k to state l. Each entry _ek_ ( _xi_ ) of emission vector denotes the probability of observing _xi_ from state k. And finally with these parameters and Bayes’s rule, we can use _p_ ( _xi|πi_ = _k_ ) to estimate _p_ ( _πi_ = _k|xi_ ).

#### **Markov Chains**

A Markov Chain is given by a finite set of states and transition probabilities between the states. At every time step, the Markov Chain is in a particular state and undergoes a transition to another state. The probability of transitioning to each other state depends only on the current state, and in particular is independent of how the current state was reached. More formally, a Markov Chain is a triplet ( _Q_ , _p_ , _A_ ) which consists of:

131

6.047/6.878 Lecture 06: Hidden Markov Models I


<!-- Start of picture text -->
© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

Figure 7.2: Prediction Models Using Markov Chain and HMM


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 7.3: Parameterization of HMM Prediction Model

- A set of states _Q_ .

- A transition matrix _A_ whose elements correspond to the probability _Aij_ of transitioning from state _i_ to state _j_ .

- A vector _p_ of initial state probabilities.

The key property of Markov Chains is that they are memory-less, i.e., each state depends only on the previous state. So we can immediately define a probability for the next state, given the current state:


In this way, the probability of the sequence can be decomposed as follows:


132

6.047/6.878 Lecture 06: Hidden Markov Models I

_P_ ( _xL_ ) can also be calculated from the transition probabilities: If we multiply the initial state probabilities at time _t_ = 0 by the transition matrix _A_ , we get the probabilities of states at time _t_ = 1. Multiplying by the appropriate power _A_<sup>_L_</sup> of the transition matrix, we obtain the state probabilities at time _t_ = _L_ .

#### **Hidden Markov Models**

Hidden Markov Models are used as a representation of a problem space in which observations come about as a result of states of a system which we are unable to observe directly. These observations, or emissions, result from a particular state based on a set of probabilities. Thus HMMs are Markov Models where the states are hidden from the observer and instead we have observations generated with certain probabilities associated with each state. These probabilities of observations are known as emission probabilities.

Formally, a Hidden Markov Model is a 5-tuple ( _Q_ , _A_ , _p_ , _V_ , _E_ ) which consists of the following parameters:

- A series of states, _Q_ .

- A transition matrix, _A_

- A vector of initial state probabilities , _p_ .

- A set of observation symbols, _V_ , for example _{_ A, T, C, G _}_ or the set of amino acids or words in an English dictionary.

- A matrix of emission probabilities, _E_ : For each _s_ , _t_ , in _Q_ , the emission probability is

_esk_ = _P_ ( _vk_ at time _t|qt_ = _s_ )

The key property of memorylessness is inherited from Markov Models. The emissions and transitions depend only on the current state and not on the past history.

## **7.4 Apply HMM to Real World: From Casino to Biology**

### **7.4.1 The Dishonest Casino**

#### **The Scenario**

Imagine the following scenario: You enter a casino that offers a dice-rolling game. You bet $1 and then you and a dealer both roll a die. If you roll a higher number you win $2. Now there’s a twist to this seemingly simple game. You are aware that the casino has two types of dice:

1. Fair die: _P_ (1) = _P_ (2) = _P_ (3) = _P_ (4) = _P_ (5) = _P_ (6) = 1 _/_ 6

2. Loaded die: _P_ (1) = _P_ (2) = _P_ (3) = _P_ (4) = _P_ (5) = 1 _/_ 10 and _P_ (6) = 1 _/_ 2

The dealer can switch between these two dice at any time without you knowing it. The only information that you have are the rolls that you observe. We can represent the state of the casino die with a simple Markov model:

The model shows the two possible states, their emissions, and probabilities for transition between them. The transition probabilities are educated guesses at best. We assume that switching between the states doesn’t happen too frequently, hence the .95 chance of staying in the same state with every roll.

#### **Staying in touch with biology: An analogy**

For comparison, Figure 7.5 below gives a similar model for a situation in biology where a sequence of DNA has two potential sources: injection by a virus versus normal production by the organism itself:

Given this model as a hypothesis, we would observe the frequencies of C and G to give us clues as to the source of the sequence in question. This model assumes that viral inserts will have higher CpG prevalence, which leads to the higher probabilities of C and G occurrence.

133

6.047/6.878 Lecture 06: Hidden Markov Models I


Figure 7.4: State of a casino die represented by a Hidden Markov model


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 7.5: Potential DNA sources: viral injection vs. normal production

#### **Running the Model**

Say we are at the casino and observe the sequence of rolls given in Figure 7.6. We would like to know whether it is more likely that the casino is using the fair die or the loaded die.


Figure 7.6: A possible sequence of observed die rolls.

Let’s look at a particular sequence of rolls.

Therefore, we will consider two possible sequences of states in the underlying HMM, one in which the dealer is always using a fair die, and the other in which the dealer is always using a loaded die. We consider each execution path to understand the implications. For each case, we compute the joint probability of an observed outcome with that sequence of underlying states.

In the first case, where we assume the dealer is always using a fair die, the transition and emission probabilities are shown in Figure 7.7. The probability of this sequence of states and observed emissions is a product of terms which can be grouped into three components: 1 _/_ 2, the probability of starting with the fair die; (1 _/_ 6)10, the probability of the sequence of rolls if we always use the fair die; and lastly (0 _._ 95)9, the

134

6.047/6.878 Lecture 06: Hidden Markov Models I


Figure 7.7: Running the model: probability of a sequence, given path consists of all fair dice

probability that we always continue to use the fair die.

In this model, we assume _π_ = _{F, F, F, F, F, F, F, F, F, F }_ , and we observe _x_ = _{_ 1 _,_ 2 _,_ 1 _,_ 5 _,_ 6 _,_ 2 _,_ 1 _,_ 6 _,_ 2 _,_ 4 _}_ . Now we can calculate the joint probability of _x_ and _π_ as follows:


With a probability this small, this might appear to be an extremely unlikely case. In actuality, the probability is low because there are many equally likely possibilities, and no one outcome is _a priori_ likely. The question is not whether this sequence of hidden states is likely, but whether it is _more_ likely than the alternatives.


Figure 7.8: Running the model: probability of a sequence, given path consists of all loaded dice

Let us consider the opposite extreme where the dealer always uses a loaded die, as depicted in Figure 7.8. This has a similar calculation except that we note a difference in the emission component. This time, 8 of the 10 rolls carry a probability of 1 _/_ 10 because the loaded die disfavors non-sixes. The remaining two rolls of six have each a probability of 1 _/_ 2 of occurring. Again we multiply all of these probabilities together according to principles of independence and conditioning. In this case, the calculations are as follows:


Note the difference in exponents. If we make a direct comparison, we can say that the situation in which a fair die is used throughout the sequence is 52 _×_ 10<sup>_−_10</sup> (as compared with 7 _._ 9 _×_ 10<sup>_−_10</sup> with the loaded die).

135

6.047/6.878 Lecture 06: Hidden Markov Models I

Therefore, it is six times more likely that the fair die was used than that the loaded die was used. This is not too surprising—two rolls out of ten yielding a 6 is not very far from the expected number 1 _._ 7 with the fair die, and farther from the expected number 5 with the loaded die.

#### **Adding Complexity**

Now imagine the more complex, and interesting, case where the dealer switches the die at some point during the sequence. We make a guess at an underlying model based on this premise in Figure 7.9.


Figure 7.9: Partial runs and die switching

Again, we can calculate the likelihood of the joint probability of this sequence of states and observations. Here, six of the rolls are calculated with the fair die, and four with the loaded one. Additionally, not all of the transition probabilities are 95% anymore. The two swaps (between fair and loaded) each have a probability of 5%.


Clearly, our guessed path is far less likely than either of the previous two cases. But if we are looking for the most likely scenario, we cannot possibly calculate _all_ alternatives in this way. We need new techniques for inferring the underlying model. In the above cases we more-or-less just guessed at the model, but what we want is a way to systematically derive likely models. Let’s formalize the models introduced thus far as we continue toward understanding HMM-related techniques.

### **7.4.2 Back to Biology**

Now that we have formalized HMMs, we want to use them to solve some real biological problems. In fact, HMMs are a great tool for gene sequence analysis, because we can look at a sequence of DNA as being emitted by a mixture of models. These may include introns, exons, transcription factors, etc. While we may have some sample data that matches models to DNA sequences, in the case that we start fresh with a new piece of DNA, we can use HMMs to ascribe some potential models to the DNA in question. We will first introduce a simple example and think about it a bit. Then, we will discuss some applications of HMM in solving interesting biological questions, before finally describing the HMM techniques that solve the problems that arise in such a first-attempt/native analysis.

#### **A simple example: Finding GC-rich regions**

Imagine the following scenario: we are trying to find GC rich regions by modeling nucleotide sequences drawn from two different distributions: background and promoter. Background regions have uniform distribution of 0.25 for each of A, T, G, C. Promoter regions have probabilities: A: 0.15, T: 0.13, G: 0.30, C: 0.42. Given one nucleotide observed, we cannot say anything about the region from which it was originated, because

136

6.047/6.878 Lecture 06: Hidden Markov Models I

either region will emit each nucleotide at some probability. We can learn these initial state probabilities based in steady state probabilities. By looking at a sequence, we want to identify which regions originate from a background distribution (B) and which regions are from a promoter model (P).


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 7.10: HMMS as a generative model for finding GC-rich regions.

We are given the transition and emission probabilities based on relevant abundance and average length of regions where _x_ = vector of observable emissions consisting of symbols from the alphabet _{_ A,T,G,C _}_ ; _π_ = vector of states in a path (e.g. BPPBP); _π_<sup>_∗_</sup> = maximum likelihood of generating that path. In our interpretation of sequence, the max likelihood path will be found by incorporating all emission and transition probabilities by dynamic programming.

HMMs are generative models, in that an HMM gives the probability of emission given a state (using Bayes’ Rule), essentially telling you how likely the state is to generate those sequences. So we can always run a generative model for transitions between states and start anywhere. In Markov Chains, the next state will give different outcomes with different probabilities. No matter which state is next, at the next state, the next symbol will still come out with different probabilities. HMMs are similar: You can pick an initial state based on the initial probability vector. In the example above, we will start in state B with high probability since most locations do not correspond to promoter regions. You then draw an emission from the _P_ ( _X|B_ ). Each nucleotide occurs with probability 0.25 in the background state. Say the sampled nucleotide is a G. The distribution of subsequent states depends only on the fact that we are in the background state and is independent of this emission. So we have that the probability of remaining in state B is 0.85 and the probability of transitioning to state P is 0.15, and so on.

We can compute the probability of one such generation by multiplying the probabilities that the model makes exactly the choices we assumed. Consider the examples shown in Figures 7.11, 7.12, and 7.13.


Figure 7.11: Probability of seq, path if all promoter

137

6.047/6.878 Lecture 06: Hidden Markov Models I


Figure 7.12: Probability of seq, path if all background


We can calculate the joint probability of a particular sequence of states corresponding to the observed emissions as we did in the Casino examples:


The pure-background alternative is the most likely option of the possibilities we have examined. But how do we know whether it is the option most likely out of all possibile paths of states to have generated the observed sequence?

The brute force approach is to examine at all paths, trying all possibilities and calculating their joint

138

6.047/6.878 Lecture 06: Hidden Markov Models I

probabilities _P_ ( _x, π_ ) as we did above. The sum of probabilities of all the alternatives is 1. For example, if all states are promoters, _P_ ( _x, π_ ) = 9 _._ 3 _×_ 10<sup>_−_7</sup> . If all emissions are Gs, _P_ ( _x, π_ ) = 4 _._ 9 _×_ 10<sup>_−_6</sup> . If we have use the mixture of _B_ ’s and _P_ ’s as in Figure 7.13, _P_ ( _x, π_ ) = 6 _._ 7 _×_ 10<sup>_−_7</sup> ; which is small because a lot of penalty is paid for the transitions between _B_ ’s and _P_ ’s which are exponential in length of sequence. Usually, if you observe more G’s, it is more likely to be in the promoter region and if you observe more A and Ts, then it is more likely to be in the background. But we need something more than just observation to support our belief. We will see how can we mathematically support our intuition in the following sections.

#### **Application of HMMs in Biology**

HMMs are used in answering many interesting biological questions. Some biological application of HMMs are summarized in Figure 7.14.


Figure 7.14: Some biological applications of HMM

## **7.5 Algorithmic Settings for HMMs**

We use HMMs for three types of operation: **scoring** , **decoding** , and **learning** . We will talk about scoring and decoding in this lecture. These operations can happen for a single path or all possible paths. For the single path operations, our focus is on discovering the path with maximum probability. However, we are interested in a sequence of observations or emissions for all path operations regardless of its corresponding paths.

### **7.5.1 Scoring**

#### **Scoring over a single path**

The Dishonest Casino problem and Prediction of GC-rich Regions problem described in section 7.4 are both examples of finding the probability score corresponding to a single path. For a single path we define the scoring problem as follows:

- **Input:** A sequence of observations _x_ = _x_ 1 _x_ 2 _. . . xn_ generated by an HMM _M_ ( _Q, A, p, V, E_ ) and a path of states _π_ = _π_ 1 _π_ 2 _. . . πn_ .

- **Output:** Joint probability, _P_ ( _x, π_ ) of observing _x_ if the hidden state sequence is _π_ .

139

6.047/6.878 Lecture 06: Hidden Markov Models I


Figure 7.15: The six algorithmic settings for HMMS

The single path calculation is essentially the likelihood of observing the given sequence over a particular path using the following formula:


We have already seen the examples of single path scoring in our Dishonest Casino and GC-rich region examples.

#### **Scoring over all paths**

We define the all paths version of scoring problem as follows:

   - **Input:** A sequence of observations _x_ = _x_ 1 _x_ 2 _. . . xn_ generated by an HMM _M_ ( _Q, A, p, V, E_ ).

- **Output:** The joint probability, _P_ ( _x, π_ ) of observing _x_ over all possible sequences of hidden states _π_ .

- The probability over all paths _π_ of hidden states of the given sequence of observations is given by the

- following formula.


We use this score when we are interested in knowing the likelihood of a particular sequence for a given HMM. However, naively computing this sum requires considering an exponential number of possible paths. Later in the lecture we will see how to compute this quantity in polynomial time.

### **7.5.2 Decoding**

Decoding answers the question: Given some observed sequence, what path gives us the maximum likelihood of observing this sequence? Formally we define the problem as follows:

140

6.047/6.878 Lecture 06: Hidden Markov Models I

- **Decoding over a single path:**

**–** Input: A sequence of observations _x_ = _x_ 1 _x_ 2 _. . . xN_ generated by an HMM _M_ ( _Q, A, p, V, E_ ).

**–** Output: The most probable path of states, _π_<sup>_∗_</sup> = _π_ 1 _∗π_ 2 _∗ . . . πN∗_

- **Decoding over all paths:**

   - Input: A sequence of observations _x_ = _x_ 1 _x_ 2 _. . . xN_ generated by an HMM _M_ ( _Q, A, p, V, E_ ).

   - Output: The path of states, _π_<sup>_∗_</sup> = _π_ 1 _∗π_ 2 _∗ . . . πN∗_ that contains the most likely state at each time point.

In this lecture, we will look only at the problem of decoding over a single path. The problem of decoding over all paths will be discussed in the next lecture.

For the single path decoding problem, we can imagine a brute force approach where we calculate the joint probabilities of a given emission sequence and all possible paths and then pick the path with the maximum joint probability. The problem is that there are an exponential number of paths and using such a brute force search for the maximum likelihood path among all possible paths is very time consuming and impractical. **Dynamic Programming** can be used to solve this problem. Let us formulate the problem in the dynamic programming approach.

We would like to find out the most likely sequence of states based on the observation. As inputs, we are given the model parameters _ei_ ( _s_ ),the emission probabilities for each state, and _aijs_ , the transition probabilities. The sequence of emissions _x_ is also given. The goal is to find the sequence of hidden states, _π_<sup>_∗_</sup> , which maximizes the joint probability with the given sequence of emissions. That is,


Given the emitted sequence _x_ we can evaluate any path through hidden states. However, we are looking for the best path. We start by looking for the optimal substructure of this problem.

For a best path, we can say that, the best path through a given state must contain within it the following:

- The best path to previous state

- The best transition from previous state to this state

- The best path to the end state

Therefore the best path can be obtained based on the best path of the previous states, i.e., we can find a recurrence for the best path. The **Viterbi** algorithm is a dynamic programming algorithm that is commonly used to obtain the best path.

#### **Most probable state path: the Viterbi algorithm**

Suppose _vk_ ( _i_ ) is the known probability of the most likely path ending at position (or time instance) _i_ in state _k_ for each _k_ . Then we can compute the corresponding probabilities at time _i_ + 1 by means of the following recurrence.


_k_

The most probable path _π_<sup>_∗_</sup> , or the maximum _P_ ( _x, π_ ), can be found recursively. Assuming we know _vj_ ( _i −_ 1), the score of the maximum path up to time _i −_ 1, we need to increase the computation for the next time step. The new maximum score path for each state depends on

- The maximum score of the previous states

- The transition probability

- The emission probability.

141

6.047/6.878 Lecture 06: Hidden Markov Models I

In other words, the new maximum score for a particular state at time _i_ is the one that maximizes the transition of all possible previous states to that particular state (the penalty of transition multiplied by their maximum previous scores multiplied by emission probability at the current time).

All sequences have to start in state 0 (the begin state). By keeping pointers backwards, the actual state sequence can be found by backtracking. The solution of this Dynamic Programming problem is very similar to the alignment algorithms that were presented in previous lectures.

The steps of the Viterbi algorithm [2] are summarized below:

1. Initialization ( _i_ = 0): _v_ 0(0) = 1, _vk_ (0) = 0 for _k >_ 0.

2. Recursion ( _i_ = 1 _. . . N_ ): _vk_ ( _i_ ) = _ek_ ( _xi_ ) max _j_ ( _ajkvj_ ( _i −_ 1)); _ptri_ ( _l_ ) = arg max _j_ ( _ajkvj_ ( _i −_ 1)).

3. Termination: _P_ ( _x, π_<sup>_∗_</sup> ) = max _k vk_ ( _N_ ); _πN∗_ = arg max _kvk_ ( _N_ ).

4. Traceback ( _i_ = _N . . ._ 1): _πi∗−_ 1<sup>=</sup><sup>_ptri_(</sup><sup>_π_</sup> _i∗_ ).


Figure 7.16: The Viterbi algorithm

As we can see in Figure 7.16, we fill the matrix from left to right and trace back. Each position in the matrix has _K_ states to consider and there are _KN_ cells in the matrix, so, the required computation time is _O_ ( _K_<sup>2</sup> _N_ ) and the required space is _O_ ( _KN_ ) to remember the pointers. In practice, we use log scores for the computation. Note that the running time has been reduced from exponential to polynomial.

### **7.5.3 Evaluation**

Evaluation is about answering the question: How well does our model of the data capture the actual data? Given a sequence x, many paths can generate this sequence. The question is how likely is the sequence given the model? In other words, is this a good model? Or, how well does the model capture the exact characteristics of a particular sequence? We use evaluation of HMMs to answer these questions. Additionally, with evaluation we can compare different models.

Let us first provide a formal definition of the Evaluation problem.

- Input: A sequence of observations _x_ = _x_ 1 _x_ 2 _. . . xN_ and an HMM _M_ ( _Q, A, p, V, E_ ).

- Output: The probability that _x_ was generated by _M_ summed over all paths.

We know that if we are given an HMM we can generate a sequence of length _n_ using the following steps:

- Start at state _π_ 1 according to probability _a_ 0 _π_ 1 (obtained using vector, _p_ ).

- Emit letter _x_ 1 according to emission probability _eπ_ 1( _x_ 1).

- Go to state _π_ 2 according to the transition probability _aπ_ 1 _|π_ 2

- Keep doing this until emit _xN_ .

142

6.047/6.878 Lecture 06: Hidden Markov Models I

Thus we can emit any sequence and calculate its likelihood. However, many state sequence can emit the same _x_ . Then, how do we calculate the total probability of generating a given _x_ over all paths? That is, our goal is to obtain the following probability:


The challenge of obtaining this probability is that there are too many paths (an exponential number) and each path has an associated probability. One approach may be using just the Viterbi path and ignoring the others, since we already know how to obtain this path. But its probability is very small as it is only one of the many possible paths. It is a good approximation only if it has high probability density. In other cases, the Viterbi path will give us an inaccurate approximation. Alternatively, the correct approach for calculating the exact sum iteratively is through the use of dynamic programming. The algorithm that does this is known as **Forward Algorithm** .

#### **The Forward Algorithm**

First we derive the formula for forward probability _f_ ( _i_ ).


The full algorithm[2] is summarized below:

- Initialization ( _i_ = 0): _f_ 0(0) = 1, _fk_ (0) = 0 for _k >_ 0.

- Iteration ( _i_ = 1 _. . . N_ ): _fk_ ( _i_ ) = _ek_ ( _xi_ )<sup>�</sup> _j_<sup>_fj_(</sup><sup>_i −_1)</sup><sup>_ajk_.</sup>

- Termination: _P_ ( _x, π_<sup>_∗_</sup> ) =<sup>�</sup> _k_<sup>_fk_(</sup><sup>_N_)</sup>


Figure 7.17: The Forward algorithm

From Figure 7.17, it can be seen that the Forward algorithm is very similar to the Viterbi algorithm. In the Forward algorithm, summation is used instead of maximization. Here we can reuse computations of the

143

6.047/6.878 Lecture 06: Hidden Markov Models I

previous problem including penalty of emissions, penalty of transitions and sums of previous states. The required computation time is _O_ ( _K_<sup>2</sup> _N_ ) and the required space is _O_ ( _KN_ ). The drawback of this algorithm is that in practice, taking the sum of logs is difficult; therefore, approximations and scaling of probabilities are used instead.

## **7.6 An Interesting Question: Can We Incorporate Memory in Our Model?**

The answer to this question is - Yes, we can! But how? Recall that, Markov models are memoryless. In other words, all memory of the model is enclosed in states. So, in order to store additional information, we must increase the number of states. Now, look back to the biological example we gave in Section 7.4.2. In our model, state emissions were dependent only on the current state. And, the current state encoded only one nucleotide. But, what if we want our model to count di-nucleotide frequencies (for CpG islands<sup>1</sup> ), or, tri-nucleotide frequencies (for codons), or di-codon frequencies involving six-nucleotide? We need to expand number of states.

For example, the last-seen nucleotide can be incorporated into the HMM’s “memory” by splitting the plus and minus states from our High-GC/Low-GC HMM into multiple states: one for each nucleotide/region combination, as in Figure 7.18.


Figure 7.18: CpG Islands - Incorporating Memory

Moving from two to eight states allows us to retain memory of the last nucleotide observed, while also distinguishing between two distinct regions. Four new states now correspond to each of the original two states in the High/Low-GC HMM. Whereas the transition weights in the smaller HMM were based purely on the frequencies of individual nucleotides, now in the larger one, they are based on di-nucleotide frequencies.

With this added power, certain di-nucleotide sequences, such as CpG islands, can be modeled specifically: the transition from C+ to G+ can be assigned greater weight than the transition from A+ to G+. Further, transitions between + and - can be modeled more specifically to reflect the frequency (or infrequency) of particular di-nucleotide sequences within one or the other.

The process of adding memory to an HMM can be generalized and more memory can be added to allow the recognition of sequences of greater length. For instance, we can detect codon triplets with 32 states, or di-codon sextuplets with 2048 states. Memory within the HMM allows for increasingly tailored specificity in scanning.

> 1CpG stands for C-phosphate-G. So, CpG island refers to a region where GC di-nucleotide appear on the same strand.

144

6.047/6.878 Lecture 06: Hidden Markov Models I

## **7.7 Further Reading**

### **7.7.1 Length Distributions of States and Generalized Hidden Markov Models**

Given a Markov chain with the transition from any state to the end state having probability _τ_ , the probability of generating a sequence of length _L_ (and then finishing with a transition to the end state) is given by:


Similarly, in the HMMs that we have been examining, the length of states will be exponentially distributed, which is not appropriate for many purposes. (For example, in a genomic sequence, an exponential distribution does not accurately capture the lengths of genes, exons, introns, etc). How can we construct a model that does not output state sequences with an exponential distribution of lengths? Suppose we want to make sure that our sequence has length exactly 5. We might construct a sequence of five states with only a single path permitted by the transition probabilities. If we include a self loop in one of the states, we will output sequences of minimum length 5, with longer sequences exponentially distributed. Suppose we have a chain of _n_ states, with all chains starting with state _π_ 1 and transitioning to an end state after _πn_ . Also assume that the transition probability between state _πi_ and _πi_ +1 is 1 _− p_ , while the self transition probability of state _πi_ is p. The probability that a sequence generated by this Markov chain has length _L_ is given by:


This is called the negative binomial distribution.

More generally, we can adapt HMMs to produce output sequences of arbitrary length. In a _Generalized Hidden Markov Model_ [1] (also known as a _hidden semi-Markov model_ ), the output of each state is a string of symbols, rather than an individual symbol. The length as well as content of this output string can be chosen based on a probability distribution. Many gene finding tools are based on generalized hidden Markov models.

### **7.7.2 Conditional random fields**

The conditional random field model a discriminative undirected probabilistic graphical model that is used alternatively to HMMs. It is used to encode known relationships between observations and construct consistent interpretations. It is often used for labeling or parsing of sequential data. It is widely used in gene finding. The following resources can be helpful in order to learn more about CRFs:

- Lecture on Conditional Random Fields from Probabilistic Graphical Models course: `https://class. coursera.org/pgm/lecture/preview/33` . For background, you might also want to watch the two previous segments, on pairwise Markov networks and general Gibbs distributions.

- Conditional random fields in biology: `http://www.cis.upenn.edu/~pereira/papers/crf.pdf`

- Conditional Random Fields tutorial: `http://people.cs.umass.edu/~mccallum/papers/crf-tutorial. pdf`

## **7.8 Current Research Directions**

## **7.9 Tools and Techniques**

## **7.10 What Have We Learned?**

In this section, the main contents we covered are as following:

- First, we introduced the motivation behind adopting Hidden Markov Models in our analysis of genome annotation.

145

6.047/6.878 Lecture 06: Hidden Markov Models I

- Second, we formalized Markov Chains and HMM under the light of weather prediction example.

- Third, we got a sense of how to apply HMM in real world data by looking at Dishonest Casino and CG-rich region problems.

- Fourthly, we systematiclly introduced algorithmic settings of HMM and went into detail of three of them:

   - Scoring: scoring over single path

   - Scoring: scoring over all paths

   - Decoding: Viterbi coding in determing most likely path

- Finally, we discussed the possibility of introducing memory in the analysis of HMM and provided further readings for interested readers.

## **Bibliography**

- [1] Introduction to GHMMs: `www.cs.tau.ac.il/~rshamir/algmb/00/scribe00/html/lec07/node28. html` .

- [2] R. Durbin, S. Eddy, A. Krogh, and G. Mitchison. _Biological sequence analysis_ . eleventh edition, 2006.

146

## CHAPTER **EIGHT**

HIDDEN MARKOV MODELS II - POSTERIOR DECODING AND LEARNING

Charalampos Mavroforakis and Chidube Ezeozue (2012) Thomas Willems (2011) Amer Fejzic (2010) Elham Azizi (2009)

### **Figures**

|8.1|Genomic applications of HMMs . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>146|
|---|---|---|
|8.2|The Forward Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>148|
|8.3|The Backward Algorithm<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>152|
|8.4|HMM for CpG Islands . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>155|
|8.5|Supervised Learning of CpG islands<br>. . . . . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>156|
|8.6|HMM model for alignment with affine gap penalties<br>. . . . . . . . . .|. . . . . . . . . . .<br>159|
|8.7|State Space Diagram used in GENSCAN<br>. . . . . . . . . . . . . . . .|. . . . . . . . . . .<br>161|


## **8.1 Review of previous lecture**

### **8.1.1 Introduction to Hidden Markov Models**

In the last lecture, we familiarized ourselves with the concept of discrete-time Markov chains and Hidden Markov Models (HMMs). In particular, a Markov chain is a discrete random process that abides by the Markov property, i.e. that the probability of the next state depends only on the current state; this property is also frequently called ”memorylessness.” To model how states change from step to step, the Markov chain uses a matrix of transition probabilities. In addition, it is characterized by a one-to-one correspondence between the states and observed symbols; that is, the state fully determines all relevant observables. More formally, a Markov chain is fully defined by the following variables:

- _πi ∈ Q_ , the state at the _i_<sup>_th_</sup> step in a sequence of finite states _Q_ of length _N_ that can hold a value from a finite alphabet Σ of length _K_

- _ajk_ , the transition probability of moving from state _j_ to state _k_ , _P_ ( _πi_ = _k|πi−_ 1 = _j_ ), for each _j, k_ in _Q_

- _a_ 0 _j ∈ P_ , the probability that the initial state will be _j_

Examples of Markov chains are abundant in everyday life. In the last lecture, we considered the canonical example of a weather system in which each state is either rain, snow, sun or clouds and the observables of the system correspond exactly to the underlying state: there is nothing that we don’t know upon making an

147

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning

observation, as the observation, i.e. whether it is sunny or raining, fully determines the underlying state, i.e. whether it is sunny or raining. Suppose, however, that we are considering the weather as it is probabilistically determined by the seasons - for example, it snows more often in the winter than in the spring - and suppose further that we are in ancient times and did not yet have access to knowledge about what the current season is. Now consider the problem of trying to infer the season (the hidden state) from the weather (the observable). There is some relationship between season and weather such that we can use information about the weather to make inferences about what season it is (if it snows a lot, it’s probably not summer); this is the task that HMMs seek to undertake. Thus, in this situation, the states, the seasons, are considered “hidden” and no longer share a one-to-one correspondence with the observables, the weather. These types of situations require a <u>generalization</u> of Markov chains known as Hidden Markov Models <u>(HMMs).</u>

## **_Did You Know?_**

Markov Chains may be thought of as WYSIWYG - What You See Is What You Get

HMMs incorporate additional elements to model the disconnect between the observables of a system and the hidden states. For a sequence of length _N_ , each observable state is instead replaced by a hidden state (the season) and a character emitted from that state (the weather). It is important to note that characters from each state are emitted according to a series of emission probabilities (say there is a 50% chance of snow, 30% chance of sun, and 20% chance of rain during winter). More formally, the two additional descriptors of an HMM are:

- _xi ∈ X_ , the emission at the _i_<sup>_th_</sup> step in a sequence of finite characters _X_ of length _N_ that can hold a character from a finite set of observation symbols _vl ∈ V_

- _ek_ ( _vl_ ) _∈ E_ , the emission probability of emitting character _vl_ when the state is _k_ , _P_ ( _xi_ = _vl|πi_ = _k_ )

In summary, an HMM is defined by the following variables:

- _ajk_ , _ek_ ( _vl_ ), and _a_ 0 _j_ that model the discrete random process

- _πi_ , the sequence of hidden states

- _xi_ , the sequence of observed emissions

### **8.1.2 Genomic Applications of HMMs**

The figure below shows some genomic applications of HMMs

|**Application**|**Detection of**<br>**GC-rich**<br>**region**|**Detection of**<br>**Conserved**<br>**region**|**Detection of**<br>**Protein coding**<br>**exons**|**Detection of**<br>**Protein**<br>**coding**<br>**conservation **|**Detection of**<br>**Protein**<br>**coding gene**<br>**structures**|**Detection of**<br>**chromatin**<br>**states**|
|---|---|---|---|---|---|---|
|**Topology /**<br>**Transitions**|2 states,<br>different<br>nucleotide<br>composition|2 states,<br>difference<br>conservation<br>levels|2 states,<br>different tri-<br>nucleotide<br>composition|2 states,<br>different<br>evolutionary<br>signatures|~20 states,<br>different<br>composition /<br>conservation,<br>specific<br>structure|40 states,<br>different<br>chromatin mark<br>combinations|
|**Hidden States**<br>**/ Annotation**|GC-rich /<br>AT-rich|Conserved/<br>non-<br>Conserved|Coding (exon) /<br>non-Coding<br>(intron or<br>intergenic)|Coding (exon)<br>/ non-Coding<br>(intron or<br>intergenic)|First / last /<br>middle coding<br>exon, UTRs,<br>intron 1/2/3,<br>intergenic,<br>*(+,-)strand|Enhancer /<br>Promoter /<br>Transcribed /<br>Repressed /<br>Repetitive|
|**Emissions /**<br>**Observations**|Nucleotides|Level of<br>conservation|Triplets of<br>nucleotides|64 x 64 matrix<br>of codon<br>substitution<br>frequencies|Codons,<br>nucleotides,<br>splice sites,<br>start/stop<br>codons|Vector of<br>chromatin mark<br>frequencies|


Figure 8.1: Genomic applications of HMMs

148

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning

Niceties of some of the applications shown in figure 8.1 include:

- **Detection of Protein coding conservation**

- This is similar to the application of detecting protein coding exons because the emissions are also not nucleotides but different in the sense that, instead of emitting codons, substitution frequencies of the codons are emitted.

- **Detection of Protein coding gene structures**

Here, it is important for different states to model first, last and middle exons independently, because they have distinct relevant structural features: for example, the first exon in a transcript goes through a start codon, the last exon goes through a stop codon, etc., and to make the best predictions, our model should encode these features. This differs from the application of detecting protein coding exons because in this case, the position of the exon is unimportant.

It is also important to differentiate between introns 1,2 and 3 so that the reading frame between one exon and the next exon can be remembered e.g. if one exon stops at the second codon position, the next one has to start at the third codon position. Therefore, the additional intron states encode the codon position.

- **Detection of chromatin states**

Chromatin state models are dynamic and vary from cell type to cell type so every cell type will have its own annotation. They will be discussed in fuller detail in the genomics lecture including strategies for stacking/concatenating cell types.

### **8.1.3 Viterbi decoding**

Previously, we demonstrated that when given a full HMM ( _Q, A, X, E, P_ ), the likelihood that the discrete random process produced the provided series of hidden states and emissions is given by:


This corresponds to the total joint probability, _P_ ( _x, π_ ). Usually, however, the hidden states are not given and must be inferred; we’re not interested in knowing the probability of the observed sequence given an underlying model of hidden states, but rather want to us the observed sequence to infer the hidden states, such as when we use an organism’s genomic sequence to infer the locations of its genes. One solution to this _decoding_ problem is known as the **Viterbi decoding** algorithm. Running in _O_ ( _K_<sup>2</sup> _N_ ) time and _O_ ( _KN_ ) space, where _K_ is the number of states and _N_ is the length of the observed sequence, this algorithm determines the sequence of hidden states (the path _π_<sup>_∗_</sup> ) that maximizes the joint probability of the observables and states, i.e. _P_ ( _x, π_ ). Essentially, this algorithm defines _Vk_ ( _i_ ) to be the probability of the most likely path ending at state _πi_ = _k_ , and it utilizes the optimal substructure argument that we saw in the sequence alignment module of the course to recursively compute _Vk_ ( _i_ ) = _ek_ ( _xi_ ) _×_ max _j_ ( _Vj_ ( _i −_ 1) _ajk_ ) in a dynamic programming algorithm.

### **8.1.4 Forward Algorithm**

Returning for a moment to the problem of ’scoring’ rather than ’decoding,’ another problem that we might want to tackle is that of, instead of computing the probability of a single path of hidden state emitting the observed sequence, calculating the _total_ probability of the sequence being produced by all possible paths. For example, in the casino example, if the sequence of rolls is long enough, the probability of any _single_ observed sequence and underlying path is very low, even if it is the single most likely sequence-path combination. We may instead want to take an agnostic attitude toward the path and assess the total probability of the observed sequence arising in any way.

In order to do that, we proposed the **Forward algorithm** , which is described in Figure 8.2

149

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning


Figure 8.2: The Forward Algorithm

The forward algorithm first calculates the joint probability of observing the first _t_ emitted characters and being in state _k_ at time _t_ . More formally,


Given that the number of paths is exponential in _t_ , dynamic programming must be employed to solve this problem. We can develop a simple recursion for the forward algorithm by employing the Markov property as follows:


Recognizing that the first term corresponds to _fl_ ( _t −_ 1) and that the second term can be expressed in terms of transition and emission probabilities, this leads to the final recursion:


Intuitively, one can understand this recursion as follows: Any path that is in state _k_ at time _t_ must have come from a path that was in state _l_ at time _t −_ 1. The contribution of each of these sets of paths is then weighted by the cost of transitioning from state _l_ to state _k_ . It is also important to note that the Viterbi algorithm and forward algorithm largely share the same recursion. The only difference between the two algorithms lies in the fact that the Viterbi algorithm, seeking to find only the single most likely path, uses a maximization function, whereas the forward algorithm, seeking to find the total probability of the sequence over all paths, uses a sum.

We can now compute _fk_ ( _t_ ) based on a weighted sum of all the forward algorithm results tabulated during the previous time step. As shown in Figure 8.2, the forward algorithm can be easily implemented in a KxN dynamic programming table. The first column of the table is initialized according to the initial state probabilities _ai_ 0 and the algorithm then proceeds to process each column from left to right. Because there are KN entries and each entry examines a total of K other entries, this leads to _O_ ( _K_<sup>2</sup> _N_ ) time complexity and _O_ ( _KN_ ) space.

In order now to calculate the total probability of a sequence of observed characters under the current HMM, we need to express this probability in terms of the forward algorithm gives in the following way:


Hence, the sum of the elements in the last column of the dynamic programming table provides the total probability of an observed sequence of characters. In practice, given a sufficiently long sequence of emitted characters, the forward probabilities decrease very rapidly. To circumvent issues associated with storing small floating point numbers, logs-probabilities are used in the calculations instead of the probabilities themselves. This alteration requires a slight adjustment to the algorithm and the use of a Taylor series expansion for the exponential function.

150

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning

### **8.1.5 This lecture**

- This lecture will discuss **posterior decoding** , an algorithm which again will infer the hidden state sequence _π_ that maximizes a different metric. In particular, it finds the most likely state at every position over all possible paths and does so using both the **forward** and **backward** algorithm.

- Afterwards, we will show how to encode “memory” in a Markov chain by adding more states to search a genome for dinucleotide CpG islands.

- We will then discuss how to use Maximum Likelihood parameter estimation for supervised learning with a labelled dataset

- We will also briefly see how to use Viterbi learning for unsupervised estimation of the parameters of an unlabelled dataset

- Finally, we will learn how to use Expectation Maximization (EM) for unsupervised estimation of parameters of an unlabelled dataset where the specific algorithm for HMMs is known as the BaumWelch algorithm.

151

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning

## **8.2 Posterior Decoding**

### **8.2.1 Motivation**

Although the **Viterbi decoding** algorithm provides one means of estimating the hidden states underlying a sequence of observed characters, another valid means of inference is provided by **posterior decoding** .

Posterior decoding provides the most likely state at any point in time. To gain some intuition for posterior decoding, let’s see how it applies to the situation in which a dishonest casino alternates between a fair and loaded die. Suppose we enter the casino knowing that the unfair die is used 60 percent of the time. With this knowledge and no die rolls, our best guess for the current die is obviously the loaded one. After one roll, the probability that the loaded die was used is given by


If we instead observed a sequence of N die rolls, how do perform a similar sort of inference? By allowing information to flow between the N rolls and influence the probability of each state, posterior decoding is a natural extension of the above inference to a sequence of arbitrary length. More formally, instead of identifying a single path of maximum likelihood, posterior decoding considers the probability of any path lying in state _k_ at time _t_ given all of the observed characters, i.e. _P_ ( _πt_ = _k|x_ 1 _, . . . , xn_ ). The state that maximizes this probability for a given time is then considered as the most likely state at that point.

It is important to note that in addition to information flowing forward to determine the most likely state at a point, information may also flow backward from the end of the sequence to that state to augment or reduce the likelihood of each state at that point. This is partly a natural consequence of the reversibility of Bayes’ rule: our probabilities change from prior probabilities into posterior probabilities upon observing more data. To elucidate this, imagine the casino example again. As stated earlier, without observing any rolls, the _state_ 0 is most likely to be unfair: this is our prior probability. If the first roll is a 6, our belief that _state_ 1 is unfair is reinforced (if rolling sixes is more likely in an unfair die). If a 6 is rolled again, information flow backwards from the second die roll and reinforces our _state_ 1 belief of an unfair die even more. The more rolls we have, the more information that flows backwards and reinforces or contrasts our beliefs about the state thus illustrating the way information flows backward and forward to affect our belief about the states in Posterior Decoding.

Using some elementary manipulations, we can rearrange this probability into the following form using Bayes’ rule:


Because _P_ ( _x_ ) is a constant, we can neglect it when maximizing the function. Therefore,


Using the Markov property, we can simply write this expression as follows:


Here, we’ve defined _fk_ ( _t_ ) = _P_ ( _πt_ = _k, x_ 1 _, . . . , xt_ ) and _bk_ ( _t_ ) = _P_ ( _xt_ +1 _, . . . , xn|πt_ = _k_ ). As we will shortly see, these parameters are calculated using the **forward algorithm** and the **backward algorithm** respectively. To solve the posterior decoding problem, we merely need to solve each of these subproblems. The forward algorithm has been illustrated in the previous chapter and in the review at the start of this chapter and the backward algorithm will be explained in the next section.

### **8.2.2 Backward Algorithm**

As previously described, the backward algorithm is used to calculate the following probability:


152

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning

We can begin to develop a recursion n by expanding into the following form:


From the Markov property, we then obtain:


The first term merely corresponds to _bl_ ( _t_ +1). Expressing in terms of emission and transition probabilities gives the final recursion:


Comparison of the forward and backward recursions leads to some interesting insight. Whereas the forward algorithm uses the results at _t −_ 1 to calculate the result for _t_ , the backward algorithm uses the results from _t_ + 1, leading naturally to their respective names. Another significant difference lies in the emission probabilities; while the emissions for the forward algorithm occur from the current state and can therefore be excluded from the summation, the emissions for the backward algorithm occur at time _t_ + 1 and therefore must be included within the summation.

Given their similarities, it is not surprising that the backward algorithm is also implemented using a KxN dynamic programming table. The algorithm, as depicted in Figure 8.3, begins by initializing the rightmost column of the table to unity. Proceeding from right to left, each column is then calculated by taking a weighted sum of the values in the column to the right according to the recursion outlined above. After calculating the leftmost column, all of the backward probabilities have been calculated and the algorithm terminates. Because there are KN entries and each entry examines a total of K other entries, this leads to _O_ ( _K_<sup>2</sup> _N_ ) time complexity and _O_ ( _KN_ ) space, bounds identical to those of the forward algorithm.

Just as P(X) was calculated by summing the rightmost column of the forward algorithm’s DP table, P(X) can also be calculated from the sum of the leftmost column of the backward algorithm’s DP table. Therefore, these methods are virtually interchangeable for this particular calculation.

153

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning


Figure 8.3: The Backward Algorithm

## **_Did You Know?_**

Note that even when executing the backward algorithm, forward transition probabilities are used i.e if moving in the backward direction involves a transition from state B _→_ A, the probability of transitioning from state A _→_ B is used. This is because moving backward from state B to state A implies that state B follows state A in our normal, forward order, thus calling for the same transition probability.

### **8.2.3 The Big Picture**

Why do we have to make both forward and backward calculations for posterior decoding, while the algorithms that we have discussed previously call for only one direction? The difference lies in the fact that posterior decoding seeks to produce probabilities for the underlying states of **individual positions** rather than whole sequences of positions. In seeking to find the most likely underlying state of a given position, we need to take into account the entire sequence in which that position exists, both before and after it, as befits a Bayesian approach - and to do this in a dynamic programming algorithm, in which we compute recursively and end with a maximizing function, we must approach our position of interest from both sides.

Given that we can calculate both _fk_ ( _t_ ) and _bk_<sup>(</sup><sup>_t_)in</sup><sup>_θ_(</sup><sup>_K_</sup> 2<sup>_N_)timeand</sup><sup>_θ_(</sup><sup>_KN_)spaceforall</sup><sup>_t_= 1</sup><sup>_. . . n_,we</sup> can use posterior decoding to determine the most likely state _πt∗_ for _t_ = 1 _. . . n_ . The relevant expression is

154

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning

given by


With two methods (Viterbi and posterior) to decode, which is more appropriate? When trying to classify each hidden state, the Posterior decoding method is more informative because it takes into account all possible paths when determining the most likely state. In contrast, the Viterbi method only takes into account one path, which may end up representing a minimal fraction of the total probability. At the same time, however, posterior decoding may give an invalid sequence of states! By selecting for the maximum probability state of each position independently, we’re not considering how likely the transitions between these states are. For example, the states identified at time points _t_ and _t_ + 1 might have zero transition probability between them. As a result, selecting a decoding method is highly dependent on the application of interest.

## **_FAQ_**

- **Q:** What does it imply when the Viterbi algorithm and Posterior decoding disagree on the path?

- **A:** In a sense, it is simply a reminder that our model gives us what it’s selecting for. When we seek the maximum probability state of each independent position and disregard transitions between these max probability states, we may get something different than when we seek to find the most likely total path. Biology is complicated; it is important to think about what metric is most relevant to the biological situation at hand. In the genomic context, a disagreement might be a result of some ’funky’ biology; alternative splicing, for instance. In some cases, the Viterbi algorithm will be close to the Posterior decoding while in some others they may disagree.

## **8.3 Encoding Memory in a HMM: Detection of CpG islands**

CpG islands are defined as regions within a genome that are enriched with pairs of C and G nucleotides on the same strand. Typically, when this dinucleotide is present within a genome, it becomes methylated, and when deamination of the cytosine occurs, as it does at some base frequency, it becomes a thymine, another natural nucleotide, and thus cannot as easily be recognized by the cell as a mutation, causing a C to T mutation. This increased mutation frequency at CpG islands depletes CpG islands over evolutionary time and renders them relatively rare. Because the methylation can occur on either strand, CpGs usually mutate into a TpG or a CpA. However, when situated within an active promoter, methylation is suppressed, and CpG dinucleotides are able to persist. Similarly, CpGs in regions important to cell function are conserved due to evolutionary pressure. As a result, detecting CpG islands can highlight promoter regions, other transcriptionally active regions, or sites of <u>purifying</u> selection within a <u>genome.</u>

## **_Did You Know?_**

CpG stands for [C]ytosine - [p]hosphate backbone - [G]uanine. The ’p’ implies that we are referring to the same strand of the double helix, rather than a G-C base pair occurring across the helix.

Given their biological significance, CpG islands are prime candidates for modelling. Initially, one may attempt to identify these islands by scanning the genome for fixed intervals rich in GC. This approach’s efficacy is undermined by the selection of an appropriate window size; while too small of a window may not capture all of a particular CpG island, too large of a window would result in missing many smaller but bona fide CpG islands. Examining the genome on a per codon basis also leads to difficulties because CpG pairs do not necessarily code for amino acids and thus may not lie within a single codon. Instead, HMMs are much better suited to modelling this scenario because, as we shall shortly see in the section on unsupervised learning, HMMs can adapt their underlying parameters to maximize their likelihood.

Not all HMMs, however, are well suited to this particular task. An HMM model that only considers the single nucleotide frequencies of C’s and G’s will fail to capture the nature of CpG islands. Consider one such HMM with the two following hidden states :

155

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning

- ’+’ state representing CpG islands

- ’-’ state: representing non-islands

Each of these two states then emits A, C, G and T bases with a certain probability. Although the CpG islands in this model can be enriched with C’s and G’s by increasing their respective emission probabilities, this model will fail to capture the fact that the C’s and G’s predominantly occur in pairs.

Because of the Markov property that governs HMM’s, the only information available at each time step must be contained within the current state. Therefore, to encode memory within a Markov chain, we need to augment the state space. To do so, the individual ’+’ and ’-’ states can be replaced with 4 ’+’ states and 4 ’-’ states: A+, C+, G+, T+, A-, C-, G-, T- (Figure 8.4). Specifically, there are 2 ways to model this, and this choice will result in different emission probabilities:

- One model suggests that the state A+, for instance, implies that we are currently in a CpG island and the _previous_ character was an A. The emission probabilities here will carry most of the information and the transitions will be fairly degenerate.

- Another model suggests that the state A+, for instance, implies that we are currently in a CpG island and the _current_ character is an A. The emission probability here will be 1 for A and 0 for all other letters and the transition probabilities will bear most of the information in the model and the emissions will be fairly degenerate. We will assume this model from now on.

## **_Did You Know?_**

The number of transitions is the square of the number of states. This gives a rough idea of how increasing HMM “memory” (and hence states) scale.

The memory of this system derives from the fact that each state can only emit one character and therefore “remembers” its emitted character. Furthermore, the dinucleotide nature of the CpG islands is incorporated within the transition matrices. In particular, the transition frequency from _C_ + to _G_ + states is significantly higher than from _C−_ to a _G−_ states, demonstrating that these <u>pairs</u> occur more often within the islands.

## **_FAQ_**

- **Q:** Since each state emits only one character, can we then say this reduces to a Markov Chain instead of a HMM?

- **A:** No. Even though the emissions indicate the letter of the hidden state, they do not indicate if the state is a CpG island or not: both an A- and an A+ state emit only the observable A.

## **_FAQ_**

- **Q:** How do we incorporate our knowledge about the system while training HMM models eg. some emission probabilities of 0 in the CpG island detection case?

- **A:** We could either force our knowledge on the model by setting some parameters and leaving others to vary or we could let the HMM loose on the model and let it discover those relationships. As a matter of fact, there are even methods that simplify the model by forcing a subset of parameters to be 0 but allowing the HMM to choose which subset.

Given the above framework, we can use posterior decoding to analyze each base within a genome and determine whether it is most likely a constituent of a CpG island or not. But having constructed the expanded HMM model, how can we verify that it is in fact better than the single nucleotide model? We previously demonstrated that the forward or backward algorithm can be used to calculate _P_ ( _x_ ) for a given

156

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning


<!-- Start of picture text -->
A + T + A - T -<br>In other words, all memory is encoded in the states aPP aBB<br>aA a G aA aG<br>aPB<br>To remember additional information, augment state C C + G + T C C - G - T + -<br>Our first HMM had minimal memory aGC aGC aBP<br>aBB A: .1 A: 1/4<br>aPP<br>State, emissions, only depend on  current  state C: .3 C: 1/4<br>one  previous nucleotide + aPB - G: .4T: .2 G: 1/4T: 1/4 eB(1) = ¼<br>di -nucleotide frequencies? aBP<br>• Markov Chain • HMM<br>a++ a--<br>a+- – Q: states – Q: states<br>+ -<br>Di-codon frequencies: six nucleotides a-+ – p: initial state probabilities – V: observations<br>A: .1 A: 1/4 – A: transition probabilities – p: initial state probabilities<br>C: .3 C: 1/4 – A: transition probabilities<br>G: .4 G: 1/4<br>T: .2 T: 1/4 – E: emission probabilities<br><!-- End of picture text -->


<!-- Start of picture text -->
A: 1  A: 0  A: 0  A: 0<br>C: 0  C: 1  C: 0  C: 0<br>G: 0  G: 0  G: 1  G: 0<br>T: 0 T: 0 T: 0 T: 1<br>A+ C+ G + T+<br>A- C- G - T-<br>A: 1  A: 0  A: 0  A: 0<br>C: 0  C: 1  C: 0  C: 0<br>G: 0  G: 0  G: 1  G: 0<br>T: 0 T: 0 T: 0 T: 1<br><!-- End of picture text -->

Figure 8.4: HMM for CpG Islands

model. If the likelihood of our dataset is higher given the second model than the first model, it most likely captures the underlying behavior more effectively.

However, there is one risk in complicating the model, which is overfitting. Increasing the number of parameters for an HMM makes the HMM more likely to overfit the data and be less accurate in capturing the underlying behavior. A common solution to this in machine learning is to use regularization, which is essentially using fewer parameters. In this case, it is possible to reduce number of parameters to learn by constraining all +/- transition probabilities to be the same value and all -/+ transition probabilities to be the same value, as the transitions back and forth from the + and - states are what we are interested in modeling, and the actual bases where the transition occurred are not that important to our model. Thus for this constrained model we have to learn fewer parameters which leads to a simpler model and can help to avoid overfitting.


<!-- Start of picture text -->
aAT<br>A T<br>C G<br>aGC<br><!-- End of picture text -->

## **_FAQ_**

- **Q:** Are there other ways to encode the memory for CpG island detection?

**A:** Other ideas that may be experimented with include

- Emit dinucleotides and figure out a way to deal with overlap.

- Add a special state that goes from C to G.

## **8.4 Learning**

We saw how to score and decode an HMM-generated sequence in two different ways. However, these methods assumed that we already knew the emission and transition probabilities. While we are always free to hazard a guess at these, we may sometimes want to use a more data-driven, empirical approach to deriving these parameters. Fortunately, the HMM framework enables the learning of these probabilities when provided a set of training data and a set architecture for the model.

When the training data is labelled, estimation of the probabilities is a form of supervised learning. One such instance would occur if we were given a DNA sequence of one million nucleotides in which the CpG islands had all been experimentally annotated and were asked to use this to estimate our model parameters.

In contrast, when the training data is unlabelled, the estimation problem is a form of unsupervised learning. Continuing with the CpG island example, this situation would occur if the provided DNA sequence contained no island annotation whatsoever and we needed to both estimate model parameters and identify

157

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning


<!-- Start of picture text -->
P P P P P P P P<br>L:<br>start B B B B B B B B<br>S: G C A A A T G C<br><!-- End of picture text -->

Figure 8.5: Supervised Learning of CpG islands

the islands.

### **8.4.1 Supervised Learning**

When provided with labelled data, the idea of estimating model parameters is straightforward. Suppose that you are given a labelled sequence _x_ 1 _, . . . , xN_ as well as the true hidden state sequence _π_ 1 _, . . . , πN_ . Intuitively, one might expect that the probabilities that maximize the data’s likelihood are the actual probabilities that one observes within the data. This is indeed the case and can be formalized by defining _Akl_ to be the number of times hidden state _k_ transitions to _l_ and _Ek_ ( _b_ ) to be the number of times _b_ is emitted from hidden state _k_ . The parameters _θ_ that maximize _P_ ( _x|θ_ ) are simply obtained by counting as follows:


One example training set is shown in Figure 8.5. In this example, it is obvious that the probability of transitioning from B to P is 3+11<sup>=</sup> 4<sup><u>1</u></sup> (there are 3 B to B transitions and 1 B to P transitions) and the probability of emitting a G from the B state is 2+2+12<sup>=</sup> 5<sup><u>2</u></sup> (there are 2 G’s emitted from the B state, 2 C’s and 1 A)

Notice, however, that in the above example the emission probability of character T from state B is 0 because no such emissions were encountered in the training set. A zero probability, either for transitioning or emitting, is particularly problematic because it leads to an infinite log penalty. In reality, however, the zero probability may merely have arisen due to over-fitting or a small sample size. To rectify this issue and maintain flexibility within our model, we can collect more data on which to train, reducing the possibility that the zero probability is due to a small sample size. Another possibility is to use ’pseudocounts’ instead of absolute counts: artificially adding some number of counts to our training data which we think more accurately represent the actual parameters and help counteract sample size errors.

- _A_<sup>_∗_</sup> _kl_<sup>=</sup><sup>_Akl_+</sup><sup>_rkl_</sup>


Larger pseudocount parameters correspond to a strong prior belief about the parameters, reflected in the fact that these pseudocounts, derived from your priors, are comparatively overwhelming the observations, your training data. Likewise, small pseudocount parameters ( _r <<_ 1) are more often used when our priors are relatively weak and we are aiming not to overwhelm the empirical data but only to avoid excessively harsh probabilities of 0.

### **8.4.2 Unsupervised Learning**

Unsupervised learning involves estimating parameters based on unlabelled data. This may seem impossible - how can we take data about which we know nothing and use it to ”learn”? - but an iterative approach

158

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning

can yield surprisingly good results, and is the typical choice in these cases. This can be thought of loosely as an evolutionary algorithm: from some initial choice of parameters, the algorithm assesses how well the parameters explain or relate to the data, uses some step in that assessment to make improvements on the parameters, and then assesses the new parameters, producing incremental improvements in the parameters at every step just as the fitness or lack thereof of a particular organism in its environment produces incremental increases over evolutionary time as advantageous alleles are passed on preferentially.

Suppose we have some sort of prior belief about what each emission and transition probability should be. Given these parameters, we can use a decoding method to infer the hidden states underlying the provided data sequence. Using this particular decoding parse, we can then re-estimate the transition and emission counts and probabilities in a process similar to that used for supervised learning. If we repeat this procedure until the improvement in the data’s likelihood remains relatively stable, the data sequence should ultimately drive the <u>parameters</u> to their appropriate values.

## **_FAQ_**

- **Q:** Why does unsupervised learning even work? Or is it magic?

- **A:** Unsupervised learning works because we have the sequence (input data) and this guides every step of the iteration; to go from a labelled sequence to a set of parameters, the later are guided by the input and its annotation, while to annotate the input data, the parameters and the sequence guide the procedure.

For HMMs in particular, two main methods of unsupervised learning are useful.

#### **Expectation Maximization using Viterbi training**

The first method, **Viterbi training** , is relatively simple but not entirely rigorous. After picking some initial best-guess model parameters, it proceeds as follows:

- **E step** : Perform Viterbi decoding to find _π_<sup>_⋆_</sup>

   - Calculate _A_<sup>_∗_</sup> _kl_<sup>,</sup><sup>_Ek_(</sup><sup>_b_)</sup><sup>_∗_using pseudocounts based on the transitions and emissions observed in</sup><sup>_π⋆_states</sup> given the latest parameters and observed sequence (Expectation step)

- **M step** : Calculate the new parameters _akl_ , _ek_ ( _b_ ) using the simple counting formalism in supervised learning (Maximization step)

**Iteration** : Repeat the E and M steps until the likelihood _P_ ( _x|θ_ ) converges

Although Viterbi training converges rapidly, its resulting parameter estimations are usually inferior to those of the Baum-Welch Algorithm. This result stems from the fact that Viterbi training only considers the most probable hidden path instead of the collection of all possible hidden paths.

#### **Expectation Maximization: The Baum-Welch Algorithm**

The more rigorous approach to unsupervised learning involves an application of Expectation Maximization to HMM’s. In general, EM proceeds in the following manner:

**Init** : Initialize the parameters to some best-guess state

- **E step** : Estimate the expected probability of hidden states given the latest parameters and observed sequence (Expectation step)

- **M step** : Choose new maximum likelihood parameters using the probability distribution of hidden states (Maximization step)

**Iteration** : Repeat the E and M steps until the likelihood of the data given the parameters converges

159

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning

The power of EM lies in the fact that _P_ ( _x|θ_ ) is guaranteed to increase with each iteration of the algorithm. Therefore, when this probability converges, a local maximum has been reached. As a result, if we utilize a variety of initialization states, we will most likely be able to identify the global maximum, i.e. the best parameters _θ_ . The Baum-Welch algorithm generalizes EM to HMM’s. In particular, it uses the forward and backward algorithms to calculate _P_ ( _x|θ_ ) and to estimate _Akl_ and _Ek_ ( _b_ ). The algorithm proceeds as follows:

- **Initialization** 1. Initialize the parameters to some best-guess state

   - **Iteration** 1. Run the forward algorithm

      2. Run the backward algorithm

      3. Calculate the new log-likelihood _P_ ( _x|θ_ )

      4. Calculate _Akl_ and _Ek_ ( _b_ )

      5. Calculate _akl_ and _ek_ ( _b_ ) using the pseudocount formulas

      6. Repeat until _P_ ( _x|θ_ ) converges

Previously, we discussed how to compute _P_ ( _x|θ_ ) using either the forward or backward algorithm’s final results. But how do we estimate _Akl_ and _Ek_ ( _b_ )? Let’s consider the expected number of transitions from state _k_ to state _l_ given a current set of parameters _θ_ . We can express this expectation as


Exploiting the Markov property and the definitions of the emission and transition probabilities leads to the following derivation:


A similar derivation leads to the following expression for _Ek_ ( _b_ ):


Therefore, by running the forward and backward algorithms, we have all of the information necessary to calculate _P_ ( _x|θ_ ) and to update the emission and transition probabilities during each iteration. Because these updates are constant time operations once _P_ ( _x|θ_ ), _fk_ ( _t_ ) and _bk_ ( _t_ ) have been computed, the total time complexity for this version of unsupervised learning is _θ_ <u>(</u> _K_<sup>2</sup> _NS_ <u>),</u> where _S_ is the total number of iterations.

## **_FAQ_**

**Q:** How do you encode your prior beliefs when learning with Baum-Welch?

**A:** Those prior beliefs are encoded in the initializations of the forward and backward algorithms

160

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning


Figure 8.6: HMM model for alignment with affine gap penalties

## **8.5 Using HMMs to align sequences with affine gap penalties**

We can use HMM to align sequences with affine gap penalties. Recall that affine gap penalties penalizes more to open/ start the gap than to extend it, thus the penalty of a gap of length g is r(g) = -d -(g-1)*e, where d is the penalty to open the gap and e is the penalty to extend an already open gap.

We will look into aligning two sequences with the affine gap penalty. We are given two sequences are X and Y, the scoring matrix S (S(xi,yj) = score of matching xi with yj), gap opening penalty of d and gap extension penalty of e. We can map this problem into an HMM problem by using the following states, transition probabilities and emission probabilities.

<u>States:</u>

There are three states involves: M (matching xi with yj), X (aligning xi with a gap), Y (aligning yj with a gap). Also, alongside each transition, there’s an update of the i,j indices. Whenever we are in state M, (i,j) = (i,j) + (1,1). In state X, (i,j) = (i,j) + (1,0). In state Y, (i,j) = (i,j) + (0,1). Transition <u>probabilities:</u> There are 7 transition probabilities to consider as shown in figure 6. P(next State = M _|_ current = M) = S(xi,yj) P(next State = X _|_ current = M) = d P(next State = Y _|_ current = M ) = d P(next State = X _|_ current = X) = e P(next State = M _|_ current = X ) = S(xi,yj) P(next State = Y _|_ current = Y) = e P(next State = M _|_ current = Y) = S(xi,yj)

We can also save the transition probabilities in a transition matrix A = [aij], where aij = P(next State = j _|_ current = i) and<sup>�</sup> _j_<sup>Aij=1</sup> Emission <u>probabilities:</u> The emission probabilities are: From state M: p _xiyi_ = p(x _i_ aligned to y _j_ ) From state X: q _xi_ = p(x _i_ aligned to gap) From state Y: q _yi_ = p(y _j_ aligned to gap) Example: X = ’VLSPADK’

161

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning

Y = ’HLAESK’

The alignment generated by the model is: MMXXMYM Which corresponds to: X = ’VLSPAD ~~K~~ ’ <u>Y</u> = ’HL ~~<u>A</u>~~ <u>ESK’</u>

## **_Did You Know?_**

For classification purposes, Posterior decoding ’path’ is more informative than Viterbi path as it is a more refined measure of which hidden states generated x. However, it may give an invalid sequence of states, for example when not all j $- _>_ $ k transitions may be possible, it might have state(i) = j and state(i+1) =k

## **8.6 Current Research Directions**

- HMM’s have been used extensively in various fields of computational biology. One of the first such applications was in a gene-finding algorithm known as GENSCAN written by Chris Burge and Samuel Karlin [1]. Because the geometric length distribution of HMM’s does not model exonic regions well, Burge et. al used an adaptation of HMM’s known as hidden semi-Markov models (HSMM’s). These types of models differ in that whenever a hidden state is reached, the length of duration of that state ( _di_ ) is chosen from a distribution and the state then emits exactly _di_ characters. The transition from this hidden state to the next is then analogous to the HMM procedure except that _akk_ = 0 for all _k_ , thereby preventing self-transitioning. Many of the same algorithms that were previously developed for HMM’s can be modified for HSMM’s. Although the details won’t be discussed here, the forward and backward algorithms can be modified to run in _O_ ( _K_<sup>2</sup> _N_<sup>3</sup> ) time, where _N_ is the number of observed characters. This time complexity assumes that there is no upper bound on the length of a state’s duration, but imposing such a bound reduces the complexity to _O_ ( _K_<sup>2</sup> _ND_<sup>2</sup> ), where _D_ is the maximum possible duration of a state.

The basic state diagram underlying Burge’s model is depicted in Figure 8.7. The included diagram only lists the states on the forward strand of DNA, but in reality a mirror image of these states is also included for the reverse strand, resulting in a total of 27 hidden states. As the diagram illustrates, the model incorporates many of the major functional units of genes, including exons, introns, promoters, UTR’s and poly-A tails. In addition, three different intronic and exonic states are used to ensure that the total length of all exons in a gene is a multiple of three. Similar to the CpG island example, this expanded state-space enabled the encoding of memory within the model.

- A recent effort has been made to make an HMM-based approach to homology searches, called HMMER, a viable alternative to BLAST in terms of computational efficiency. Unlike most other homology search algorithms, HMMER, written by Sean Eddy, uses the Forward algorithm’s average over alignment uncertainty, rather than only reporting the maximum likelihood alignment (a la Viterbi ); this approach is often better for detecting more remote homologies, as as divergence times increase, there may become more viable ways of aligning sequences, each of them individually not sufficiently strong to be differentiated from noise but together giving evidence for homology. A particularly exciting recent development is that HMMER is now available as a web server; it can be found at http://www.ebi.ac.uk/Tools/hmmer/.

- An interesting subject that may be explored also concerns the agreement of Viterbi and Posterior decoding paths; not just for CpG island detection but even for chromatin state detection. One may look at multiple paths by sampling, asking questions such as:

   - What is the maximum a posteriori vs viterbi path? Where do they differ?

   - Can complete but maximally disjoint (from Viterbi) paths be found?

162

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning


Figure 8.7: State Space Diagram used in GENSCAN

163

6.047/6.878 Lecture 7: Hidden Markov Models II - Posterio Decoding and Learning

## **8.7 Further Reading**

## **8.8 Tools and Techniques**

## **8.9 What Have We Learned?**

Using the basic computational framework provided by Hidden Markov Models, we’ve learned how to infer the most likely set of hidden states underlying a sequence of observed characters. In particular, a combination of the forward and backward algorithms enabled one form of this inference, i.e. posterior decoding, in _O_ ( _KN_<sup>2</sup> ) time. We also learned how either unsupervised or supervised learning can be used to identify the best parameters for an HMM when provided with an unlabelled or labelled dataset. The combination of these decoding and parameter estimation methods enable the application of HMM’s to a wide variety of problems in computational biology, of which CpG island and gene identification form a small subset. Given the flexibility and analytical power provided by HMM’s, these methods will play an important role in computational biology for the foreseeable future.

## **Bibliography**

- [1] Christopher B Burge and Samuel Karlin. Finding the genes in genomic dna. _Current Opinion in Structural Biology_ , 8(3):346 – 354, 1998.

164

## CHAPTER **NINE**

GENE IDENTIFICATION: GENE STRUCTURE, SEMI-MARKOV, CRFS

Tim Helbig (2011) Jenny Cheng (2010)

### **Figures**

|9.1|Intergenic DNA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|164|
|---|---|---|
|9.2|Intron/Exon Splicing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|164|
|9.3|Delineation of Exons and Open Reading Frames<br>. . . . . . . . . . . . . . . . . . . . . . .|165|
|9.4|Hidden Markov Model Utilizing GT Donor Assumption<br>. . . . . . . . . . . . . . . . . . .|165|
|9.5|Multiple lines of evidence for gene identification . . . . . . . . . . . . . . . . . . . . . . . .|165|
|9.6|HMMs with composite emissions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|166|
|9.7|State diagram that considers direction of RNA translation . . . . . . . . . . . . . . . . . .|166|
|9.8|Conditional random fields: a discriminative approach conditioned on the input sequence .|167|
|9.9|Examples of feature functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|167|
|9.10|Conditional probability score of an emitted sequence . . . . . . . . . . . . . . . . . . . . .|167|
|9.11|A comparison of HMMs and CRFs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|168|


## **9.1 Introduction**

After a genome has been sequenced, a common next step is to attempt to infer the functional potential of the organism or cell encoded through careful analysis of that sequence. This mainly takes the form of identifying the protein coding genes within the sequence as they are thought to be the primary units of function within living systems; this is not to say that they are the only functional units within genomes as things such as regulatory motifs and non-coding RNAs are also imperative elements.

This annotation of the protein coding regions is too laborious to do by hand, so it is automated in a process known as computational gene identification. The algorithms underlying this process are often based on Hidden Markov Models (HMMs), a concept discussed in previous chapters to solve simple problems such as knowing whether a casino is rolling a fair versus a loaded die. Genomes, however, are very complicated sets of data, replete with long repeats, overlapping genes (where one or more nucleotides are part of two or more distinct genes) and pseudogenes (non-transcribed regions that look very similar to genes) among many other obfuscations. Thus, experimental and evolutionary data often needs to be included into HMMs for greater annotational accuracy, which can result in a loss of scalability or a reliance on incorrect assumptions of independence. Alternative algorithms have been utilized to address the problems of HMMs including those based on Conditional Random Fields (CRFs), which rely on creating a distribution of the hidden states of the genomic sequence in question conditioned on known data. Use of CRFs has not phased out HMMs as both are used with varying degrees of success in practice.<sup>1</sup>

> 1 R. Guigo (1997). “Computational gene identification: an open problem.” Computers Chem. Vol. 21.

165

6.047/6.878 Lecture 09: Gene Identification: Gene Structure, Semi-Markov, CRFs

## **9.2 Overview of Chapter Contents**

This chapter will begin with a discussion of the complexities of the Eukaryotic gene. It will then describe how HMMs can be used as a model to parse Eukaryotic genomes into protein coding genes and regions that are not; this will include reference to the strengths and weaknesses of an HMM approach. Finally, the use of CRFs to annotate protein coding regions will be described as an alternative.

## **9.3 Eukaryotic Genes: An Introduction**

Within eukaryotic genomes, only a small fraction of the nucleotide content actually consists of protein coding genes (in humans, protein coding regions make up about 1%-1.5% of the entire genome). The rest of the DNA is classified as intergenic regions (See Figure 9.1) and contains things such as regulatory motifs, transposons, integrons and non-protein coding genes.<sup>2</sup>


Figure 9.1: Intergenic DNA

Further, of the small fraction of the DNA that is transcribed into mRNA, not all of it is translated into protein. Certain regions known as introns, are removed or “spliced” out of the precursor mRNA. This now processed mRNA, containing only “exons” and some other additional modifications discussed in previous chapters, is translated into protein. (See Figure 9.2) The goal of computational gene identification is thus not only to pick out the few regions of the entire Eukaryotic genome that encode for proteins but also to parse those protein coding regions into identities of exon or intron so that the sequence of the synthesized protein can be known.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 9.2: Intron/Exon Splicing

## **9.4 Assumptions for Computational Gene Identification**

The general assumptions for computational gene identification are that exons are delineated by a sequence AG at the start of the exon and a sequence of GT at the end of the exon. For protein-coding genes, the start codon (ATG) and the end codons (TAA, TGA, TAG) delineate the open reading frame. (Most of these ideas can be seen in Figure 9.3) These assumptions will be incorporated into more complex HMMs described below.

> 2“Intergenic region.” http://en.wikipedia.org/wiki/Intergenic ~~r~~ egion

166

6.047/6.878 Lecture 09: Gene Identification: Gene Structure, Semi-Markov, CRFs


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 9.3: Delineation of Exons and Open Reading Frames

## **9.5 Hidden Markov Models**

A toy Hidden Markov Model is a generative approach to model this behavior. Each emission of the HMM is one DNA base/letter. The hidden states of the model are intergenic, exon, intron. Improving upon this model would involve including hidden states DonorG and DonorT. The DonorG and DonorT states utilize the information that exons are delineated by GT at the end of the sequence before the start of an intron. (See Figure 9.4 for inclusion of DonorG and DonorT into the model)


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 9.4: Hidden Markov Model Utilizing GT Donor Assumption

The e in each state represents emission probabilities and the arrows indicate the transition probabilities. Aside from the initial assumptions, additional evidence such as evolutionary conservation and experimental mRNA data can help create an HMM to better model the behavior. (See Figure 9.5)


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 9.5: Multiple lines of evidence for gene identification

167

6.047/6.878 Lecture 09: Gene Identification: Gene Structure, Semi-Markov, CRFs

Combining all the lines of evidence discussed above, we can create an HMM with composite emissions in that each emitted value is a “tuple” of collected values. (See Figure 9.6)


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 9.6: HMMs with composite emissions

A few assumptions of this composite model are that each new emission “feature” is independent of the rest. However, this creates the problem that with each new feature, the tuple increases in length, and the number of states of the HMM increases exponentially, leading to a combinatorial explosion, which thus means poor scaling. (Examples of more complex HMMs that can result in poor scaling can be found in Figure 9.7)


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 9.7: State diagram that considers direction of RNA translation

## **9.6 Conditional Random Fields**

Conditional Random Fields, CRFs, are an alternative to HMMs. Being a discriminative approach, this type of model doesnt take into account the joint distribution of everything, as does a poorly scaling HMM. The hidden states in a CRF are conditioned on the input sequence. (See Figure 9.8)<sup>3</sup>

> 3Conditional Random Field. Wikipedia. http://en.wikipedia.org/wiki/Conditional ~~r~~ andom ~~f~~ ield

168

6.047/6.878 Lecture 09: Gene Identification: Gene Structure, Semi-Markov, CRFs


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 9.8: Conditional random fields: a discriminative approach conditioned on the input sequence

A feature function is like a score, returning a real-valued number as a function of its inputs that reflects the evidence for a label at a particular position. (See Figure 9.9) The conditional probability of the emitted sequence is its score divided by the total score of the hidden state. (See Figure 9.10)


Figure 9.9: Examples of feature functions


Figure 9.10: Conditional probability score of an emitted sequence

Each feature function is weighted, so that during the training, the weights can be set accordingly. The feature functions can incorporate vast amounts of evidence without the Naive Bayes assumption of independence, making them both scalable and accurate. However, training is much more difficult with CRFs than HMMs.

## **9.7 Other Methods**

Besides HMMs and CRFs, other methods do exist for computational gene identification. Semi-markov models generate variable sequence length emissions, meaning that the transitions are not entirely memory-less on the hidden states.

Max-min models are adaptations of support vector machines. These methods have not yet been applied to mammalian genomes.<sup>4</sup>

> 4For better understanding of SVM: http://dspace.mit.edu/bitstream/handle/1721.1/39663/6-034Fall2002/OcwWeb/Electrical-Engineering-and-Computer-Science/6-034Artificial-IntelligenceFall2002/Tools/detail/svmachine.htm

169

6.047/6.878 Lecture 09: Gene Identification: Gene Structure, Semi-Markov, CRFs

## **9.8 Conclusion**

Computational gene identification, because it entails finding the functional elements encoded within a genome, has a lot of practical significance as well as theoretical significance for the advancement of biological fields.

The two approaches described above are summarized below in Figure 9.11:


Figure 9.11: A comparison of HMMs and CRFs

### **9.8.1 HMM**

- generative model

- randomly generates observable data, usually with a hidden state

- specifies a joint probability distribution

- _P_ ( _x, y_ ) = _P_ ( _x|y_ ) _P_ ( _y_ )

- sometimes hard to model dependencies correctly

- hidden states are the labels for each DNA base/letter

- composite emissions are a combination of the DNA base/letter being emitted with additional evidence

### **9.8.2 CRF**

- discriminative model

- models dependence of unobserved variable y on an observed variable _x_

- _P_ ( _y|x_ )

- hard to train without supervision

- more effective for when the model doesnt require joint distribution

170

6.047/6.878 Lecture 09: Gene Identification: Gene Structure, Semi-Markov, CRFs

In practice, the resulting gene specification using CONTRAST, a CRF implementation, is about 46.2% at its maximum. This is because in biology, there are a lot of exceptions to the standard model, such as overlapping genes, nested genes, and alternative splicing. Having models include all of those exceptions sometimes yields worse predictions; this is a non-trivial tradeoff. However, technology is improving and within the next five years, there will be more experimental data to fuel the development of computational gene identification, which in turn will help generate a better understanding of the syntax of DNA.

## **9.9 Current Research Directions**

- **9.10 Further Reading**

- **9.11 Tools and Techniques**

- **9.12 What Have We Learned?**

## **Bibliography**

- 1.R. Guigo (1997). “Computational gene identification: an open problem.”

   - 2.“Intergenic region.” http://en.wikipedia.org/wiki/Intergenic ~~r~~ egion

   - 3.Conditional Random Field. Wikipedia. http://en.wikipedia.org/wiki/Conditional ~~r~~ andom ~~f~~ ield

- 4.http://dspace.mit.edu/bitstream/handle/1721.1/39663/6-034Fall-2002/OcwWeb/Electrical-Engineering-

- and-Computer-Science/6-034Artificial-IntelligenceFall2002/Tools/detail/svmachine.htm

171

6.047/6.878 Lecture 09: Gene Identification: Gene Structure, Semi-Markov, CRFs

172

CHAPTER **TEN** RNA FOLDING

Guest Lecture by Stefan Washietl Scribed by Sam Sinaei (2010) Scribed by Archit Bhise (2012) Scribed by Eric Mazumdar(2014)

|**Figures**||
|---|---|
|10.1 Graphical representation of the hierarchy of RNA strucure complexity . . . . . . . . . . .<br>10.2 The typical representation of RNA secondary structure in textbooks. It clearly shows the<br>secondary substructure in RNA.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|175<br>175|
|10.3 Graph drawing where the back-bone is a circle and the base pairings are the arcs within<br>the circle. Note that the graph is outer-planar, meaning the arcs do not cross. . . . . . . .<br>10.4 A machine readable dot-bracket notation, in which for each paired nucleotide you open a<br>bracket( and close it when you reach its match) and for each unpaired element you have a<br>dot.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|175<br>176|
|10.5 A matrix representation, in which you have a dot for each pair. . . . . . . . . . . . . . . .<br>10.6 Mountain plot, in which for pairs you go one step up in the plot and if not you go one step<br>to the right.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|176<br>176|
|10.7 Example of a scoring scheme for base pair matches. Note that G-U can form a wobble pair<br>in RNA. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|176|
|10.8 The recursion formula for Nussinov algorithm, along with a graphical depiction of how it<br>works. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|177|
|10.9 The diagonal is initialized to 0.<br>Then, the table is filled bottom to top, left to right<br>according to the recurrence relation. In this example, complimentary base pairings are<br>scored as -1 and non-complementary pairings are scored as 0. The optimal score for the<br>entire sequence is found in the upper right corner.<br>. . . . . . . . . . . . . . . . . . . . . .<br>10.10The traceback matrix_Kij_, filled during the recursion, holds the optimal secondary structure<br>when _k_ is paired with _i_ for a subsequence [_i, j_]. If _i_ is unpaired in the optimal structure,<br>_Kij_ = 0. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>10.11Stacking between neighboring base pairs in RNA. The flat aromatic structure of the base<br>causes quantum interactions between stacked bases and changes its physical stability. . . .<br>10.12Various internal substructures in a folded RNA. A hairpin is consisted of a terminal loop<br>connected to a paired region, an internal loop is an unpaired region within the paired<br>region. A Bulge is a special case of an interior loop with a single mis-pair. a Multi loop is<br>a loop which consists of multiple of these components (in this example two hairpins and a<br>paired region, all connected to a loop). . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|178<br>178<br>178<br>179|


173

6.047/6.878 Lecture 08: RNA Structure

- 10.13 _F_ describes the unpaired case, _C_ is described by one of the three conditions : hairpin,interior loop, or a composition of structures i.e. a multi loop. _M_<sup>1</sup> is a multi loop with only one component, where are _M_ might have multiple of them. The _|_ icon is notation for _“or”_ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179

- 10.14A) Single sequence: Terminal symbols are bases or base-pairs, Emission probabilities are base frequencies in loops and paired regions B) Phylo-SCFG: Terminal symbols are single or paired alignment columns, Emission probabilities calculated from phylogenetic model and tree using Felsenstein’s algorithmWe to try to better understand RNA-RNA interactions.183

- 10.15We can study kinetics and folding pathways in further depth. . . . . . . . . . . . . . . . . 184 10.16We can investigate pseudoknots. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184 10.17We can try to better understand RNA-RNA interactions. . . . . . . . . . . . . . . . . . . 185

## **10.1 Motivation and Purpose**

RNA **(Ribonucleic acid)** as a molecule has been posited as being the origin of life. Though it was long considered nothing more than an intermediary between the code in the DNA and the functional proteins, RNA has been shown to serve many different functions, spanning the entire realm of genomics. Part of the cause for its versatility is the many possible conformations that RNA can be found in. Being made up of a more flexible backbone than DNA, RNA exhibits interesting and varied structures that can inform us on its many purposes. Certain structures of RNA, for example, lend themselves to catalytic activities while others serve as the tRNA, and mRNA that are so important during the process of converting the DNA’s code into proteins The aim for this chapter is to learn methods that can explain, or even predict the secondary structure of RNA in the hope that they will shed light on the many properties of this versatile molecule.

To accomplish this, we first look at RNA from a biological perspective and explain the known biological roles of RNA. Then, we study the different methods that exist to predict RNA structure. There are two main approaches to the RNA folding problem: 1) predicting the RNA structure based on thermodynamic stability of the molecule, and looking for a thermodynamic optimum 2) probabilistic models which try to find the states of the RNA molecule in a probabilistic optimum.

Finally, we can use evolutionary data in order to increase the confidence of our predictions by these methods.

## **10.2 Chemistry of RNA**

RNA consists of a 5-carbon sugar, ribose, which is attached to an organic base (either adenine, uracil, cytosine or guanine). There are two biochemical differences between DNA and RNA:

1. the 5-carbon sugar has no hydroxyl group in the 5 position

2. the uracil presence in the RNA which is the non-methylated form of thymine instead of just thymine.

The presence of ribose in RNA makes its structure more flexible than DNA, letting the RNA molecule fold and make bonds within itself which makes the single stranded RNA more than single stranded DNA.

174

6.047/6.878 Lecture 08: RNA Structure

## **10.3 Origin and Functions of RNA**

People initially believed that RNA only acted as an intermediate between the DNA code and the protein, however, in early 80s, the discovery of catalytic RNAs (ribozymes) expanded the perspective on what this molecule can actually do in living things. Sidney Altman and Thomas Cech discovered the first ribozyme, RNase P which is able to cleave off the head of tRNA. Self-splicing introns (group I introns) were also one of the first ribozymes that were discovered. They do not need any protein as catalysts to splice. Single or double stranded RNA also serves as the information storage and replication agent in some viruses.

The **RNA World Hypothesis** , proposed by Walter Gilbert in 1986, suggests that RNA was the precursor to modern life. It relies on the fact that RNA can have both information storage, and catalytic activity at the same time, both of which are fundamental characteristics of a living system. In short, the RNA World hypothesis says that, because RNA can have a catalytic role in cells and there is evidence that RNA can self-replicate without depending on other molecules, an RNA World is a plausible precursor of today’s DNA and protein based world. Although to this day, there are no natural self-replicating RNA found in vivo, selfreplicating RNA molecules have been created in lab via artificial selection. For example, a chimeric construct of a natural ligase ribozyme with an in vitro selected template binding domain has been shown to be able to replicate at least one turn of an RNA helix. For this reason, Gilbert proposed RNA as a plausible origin for life. The theory suggests that through evolution, RNA has passed its information storage role to DNA, a more stable molecule and one less prone to mutation. RNA then assumed the role of intermediate between DNA and proteins, which took over some of RNA’s catalytic role in the cell. Thus, scientists sometimes refer to RNA as molecular fossils. Even though RNA has lost a lot of its information-storage functionality to DNA and its functional properties to proteins, RNA still plays an integral role in the living organisms. For instance, the catalytic portion of the ribosome i.e. the main functional part of the ribosomal complex consists of RNA. RNA also has regulatory roles in the cell, and basically serves as an agent for the cell to sense and react to the environment.

### **10.3.1 Riboswitches**

Regulatory RNAs have different families, and one of the most important ones are **riboswitches** . Riboswitches are involved in different levels of gene regulation. In some bacteria, important regulations are done by simple RNA families. One example is the thermosensor in Listeria, a riboswitch that blocks the ribosomes at low temperature (since the hydrogen bonds are more stable). The RNA then forms a semidouble stranded conformation which does not bind to the ribosome and turns the ribosome off. At higher temperatures (37 C), the double strand opens up and allows ribosome to attach to a certain region in the riboswitch, making translation possible once again. Another famous Riboswitch is the adenine Riboswitch (and in general purine riboswitches) , which regulate protein synthesis. For example the ydhl mRNA which has a terminator stem at the end and blocks it from translation, but when the Adenine concentration increases in the cell, it binds to the mRNA and changes its conformation such that the terminator stem disappears.

### **10.3.2 microRNAs**

There are other sorts of RNAs such as **microRNAs** , a more modern variant of RNA (relatively). Their discovery unveiled a novel non-protein layer of gene regulation (e.g. the EVF-2 and HOTAIR miRNAs). EVF-2 is interesting because its transcribed from an ultra conserved enhancer, and separates from the transcription string by forming a hairpin, and thereafter returns to the very same enhancer (along with a protein Dlx-2) and regulates its activity. HOTAIR RNA induces changes in chromatin state, and regulates

175

6.047/6.878 Lecture 08: RNA Structure

the methylation of Histones, which in turn silences the HOX-D cluster.

### **10.3.3 Other types of RNA**

We can also look at types of **noncoding RNAs** .

**piRNAs** are the largest class of small non-coding RNA molecules in animals. They are primarily involved in the silencing of transposons, but likely have a lot of functions. They are also involved in epigenetic modications, and post-transcriptional gene silencing.

**lncRNAs** are long transcripts produced that operate functionally as RNAs and are not translated into proteins. Many studies implicate lncRNAs in epigenetic modications, maybe acting as a targeting mechanism or as a molecular scaffold for Polycomb proteins. lncRNAs are likely to possess numerous functions, many are nuclear, many are cytoplasmic.

## **10.4 RNA Structure**

We have learned about different functions of RNA, and it should be clear by now how fundamental the role of RNA in living systems is. Because it is impossible to understand how RNA actually does all these activities in the cell, without knowing what its structure is, in this part we will look into the structure of RNA.

RNA structure can be studied in three different levels 10.1:

1. _Primary_ structure: the sequence in which the bases (U, A, C, G) are aligned.

2. _Seconary_ structure: the 2-D analysis of the [hydrogen] bonds between different parts of RNA. In other words, where RNA becomes double-stranded, where RNA forms a hairpin or a loop or other similar forms.

3. _Tertiary_ structure: the complete 3-D structure of RNA, i.e. how the string bends, where it twists and such.

As mentioned before, the presence of ribose in RNA enables it to fold and create double-helixes with itself. The primary structure is fairly easy to obtain through sequencing the RNA. We are mainly interested in understanding the secondary structure for RNA: where the loops and hydrogen bonds form and create the functional attributes of RNA. Ideally, we would like to study the tertiary structure because this is the final state of the RNA, and what gives it its true functionality. However, the tertiary structure is very hard to compute and beyond the scope of this lecture.

Even though studying the secondary structure can be tricky, there are some simple ideas that work quite well in predicting it. Unlike proteins, in RNA, most of the stabilizing]free energy for the molecule comes from its secondary structure (rather than tertiary in case of proteins). RNAs initially fold into their secondary structure and then form their tertiary structure, and therefore there are very interesting facts that we can learn about a certain RNA molecule by just knowing its secondary structure.

Finally, another great property of the secondary structure is that it is usually well conserved in evolution, which helps us improve the secondary structure predictions and also to find ncRNA (non-coding RNA)s. There are widely used representations for the secondary structure of RNA:

176

6.047/6.878 Lecture 08: RNA Structure


© Stefan Washietl. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 10.1: Graphical representation of the hierarchy of RNA strucure complexity


© Stefan Washietl. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 10.2: The typical representation of RNA secondary structure in textbooks. It clearly shows the secondary substructure in RNA.


© Stefan Washietl. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 10.3: Graph drawing where the back-bone is a circle and the base pairings are the arcs within the circle. Note that the graph is outer-planar, meaning the arcs do not cross.

Formally: A secondary structure is a vertex labeled graph on n vertices with an adjacency matrix _A_ = ( _aij_ ) fulfilling:

- _ai,i_ +1 = 1 _for_ 1 _≤ i ≤ n_ 1 (continuous backbone)

- For each _i,_ 1 _≤ i ≤ N_ there is at most one _aij_ = 1 where _j_ ≩ _i_ + _/ −_ 1(a base only forms a pair with one other at the time)

- If _aij_ = _akl_ = 1 _andi < k < jtheni < l < j_ (ignore pseudo knots)

177

6.047/6.878 Lecture 08: RNA Structure


© Stefan Washietl. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 10.4: A machine readable dot-bracket notation, in which for each paired nucleotide you open a bracket( and close it when you reach its match) and for each unpaired element you have a dot.


© Stefan Washietl. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 10.5: A matrix representation, in which you have a dot for each pair.


© Stefan Washietl. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 10.6: Mountain plot, in which for pairs you go one step up in the plot and if not you go one step to the right.

## **10.5 RNA Folding Problem and Approaches**

Finally, we get to the point where we want to study the RNA structure. The goal here is to predict the secondary structure of the RNA, given its primary structure (or its sequence). The good news is we can find the optimal structure using dynamic programming. Now in order to set up our dynamic programming framework we would need a scoring scheme, which we would create using the contribution of each base pairing to the physical stability of the molecule. In other words, we want to create a structure with minimum free energy, in in our simple model we would assign each base pair an energy value. 10.7


Figure 10.7: Example of a scoring scheme for base pair matches. Note that G-U can form a wobble pair in RNA.

The optimum structure is going to be the one with a minimum free energy and by convention negative energy is stabilizing, and positive energy is non-stabilizing. Using this framework, we can use dynamic programming (DP) to calculate the optimal structure because 1) this scoring scheme is additive 2) we disallowed pseudo knots, which means we can divide the RNA into two smaller ones which are independent, and solve the problem for these smaller RNAs.

We want to find a DP matrix _Eij_ , in which we calculate the minimum free energy for subsequence _i_ to

178

6.047/6.878 Lecture 08: RNA Structure

_j_ . The first approach to this is Nussinov’s algorithm.

### **10.5.1 Nussinov’s algorithm**

The recursion formula for this problem was first described by Nussinov in 1978.

The intuition behind this algorithm is as follows: given a subsequence [ _i, j_ ], there is either no edge connecting to the _i_ th base (meaning it is unpaired) _or_ there is some edge connecting the _i_ th base to the _k_ th base where _i < k ≤ j_ (meaning the _i_ th base is paired to the _k_ th base). In the case were the _i_ th base is unpaired, the energy of the subsequence, _Ei,j_ , simply reduces to the energy of the subsequence from _i_ + 1 to _j_ , _Ei_ +1 _,j_ . This is the first term of the Nussinov recurrence relation. If the _i_ th base is paired to the _k_ th base, however, then _Ei,j_ reduces to the energy contribution of the _i, k_ pairing, _βi,k_ , plus the energy of the subsequences formed by dividing [ _i_ + 1 _, j_ ] around _k_ , _Ei_ +1 _,k−_ 1<sup>and</sup><sup>_E_</sup> _k_ +1 _,j_<sup>.Choosingthe</sup><sup>_k_whichminimizes</sup> that value yields the second term of the Nussinov recurrence relation. The optimal subsequence energy, therefore, is the minimum of the subsequence energy when the _i_ th base is paired with the optimal _k_ th base and when the _i_ th base is unpaired. This produces the overall relation described in figure 10.8.


Figure 10.8: The recursion formula for Nussinov algorithm, along with a graphical depiction of how it works.

From this recurrence relation, we can see that the DP matrix will contain entries for all _i, j_ where 1 _≤ i ≤ n_ and _i ≤ j ≤ n_ and _n_ is the length of the RNA sequence. In other words, the matrix will be _n ∗ n_ and only contain entries in the upper right triangle. The matrix is first initialized such that all values on the diagonal are equal to zero. We then iterate over _i_ = _n −_ 1 _..._ 1 and _j_ = _i_ + 1 _...n_ (bottom to top, left to right) and fill each entry according to the recurrence relation. The overall score is the score of the [1 _, n_ ] subsequence, which is the upper right corner of the matrix. Figure 10.9 illustrates this procedure.

When we calculate the minimum free energy, we are often interested in the corresponding fold. In order to recover the optimal fold from the DP algorithm, a traceback matrix is used to store pointers from each entry to its parent entry. Figure 10.10 describes the backtracking algorithm.

This model is very simplistic and there are some limitations to it. Nussinov’s algorithm, as implemented naively, does not take into account some of the limiting aspects of RNA folding. Most importantly, it does not consider stacking interactions between neighboring pairs, a vital factor (even more so than hydrogen bonds) in RNA folding. Figure 10.11

Therefore, it is desirable to integrate biophysical factors into our prediction. One improvement, for instance, is to assign energies to graph faces (structural elements in figure 10.12), rather than single base pairs. The total energy of the structure then becomes the sum of the energies of the substructures. The stacking energies can be calculated by melting oligonucleotides experimentally.

179

6.047/6.878 Lecture 08: RNA Structure


© Stefan Washietl. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 10.9: The diagonal is initialized to 0. Then, the table is filled bottom to top, left to right according to the recurrence relation. In this example, complimentary base pairings are scored as -1 and non-complementary pairings are scored as 0. The optimal score for the entire sequence is found in the upper right corner.


Figure 10.10: The traceback matrix _Kij_ , filled during the recursion, holds the optimal secondary structure when _k_ is paired with _i_ for a subsequence [ _i, j_ ]. If _i_ is unpaired in the optimal structure, _Kij_ = 0.


© Stefan Washietl. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 10.11: Stacking between neighboring base pairs in RNA. The flat aromatic structure of the base causes quantum interactions between stacked bases and changes its physical stability.

### **10.5.2 Zuker Algorithm**

Therefore, we use a variant which includes stacking energies to calculate the RNA structure. This is called the Zuker algorithm. Like Nussinovs, it assumes that the optimal structure is the one with the lowest equilibrium free energy. Nevertheless, it includes the total energy contributions from the various substructures which is partially determined by the stacking energy. Some modern RNA folding algorithms use this algorithm for RNA structure predictions.

In the Zuker algorithm, we have four different cases to deal with. Figure 10.13 shows a graphical outline of the decomposition steps. The procedure requires four matrices. _Fij_ contains the free energy of the overall optimal structure of the subsequence _xij_ . The newly added base can be unpaired or it can form a pair. For

180

6.047/6.878 Lecture 08: RNA Structure


© Stefan Washietl. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 10.12: Various internal substructures in a folded RNA. A hairpin is consisted of a terminal loop connected to a paired region, an internal loop is an unpaired region within the paired region. A Bulge is a special case of an interior loop with a single mis-pair. a Multi loop is a loop which consists of multiple of these components (in this example two hairpins and a paired region, all connected to a loop).

the latter case, we introduce the helper matrix _Cij_ , that contains the free energy of the optimal substructure of _xij_ under the constraint that _i_ and _j_ are paired. This structure closed by a base-pair can either be a hairpin, an interior loop or a multi-loop.

The hairpin case is trivial because no further decomposition is necessary. The interior loop case is also simple because it reduces again to the same decomposition step. The multi-loop step is more complicated. The energy of a multi loop depends on the number of components, i.e. substructures that emanate from the loop. To implicitly keep track of this number, there is a need for two additional helper matrices. _Mij_ holds the free energy of the optimal structure of _xij_ under the constraint that _xij_ is part of a multi loop with at least one component. _Mij_<sup>1holdsthefreeenergyoftheoptimalstructureof</sup><sup>_xij_undertheconstraintthat</sup><sup>_xij_</sup> is part of a multi-loop and has exactly one component closed by pair ( _i, k_ ) with _i < k < j_ . The idea is to decompose a multi loop in two arbitrary parts of which the first is a multi-loop with at least one component and the second a multi-loop with exactly one component and starting with a base-pair.

These two parts corresponding to _M_ and _M_<sup>1</sup> can further be decomposed into substructures that we already know, i.e. unpaired intervals, substructures closed by a base-pair,or (shorter) multi-loops. (The recursions are also summarized in 10.13.


© Stefan Washietl. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 10.13: _F_ describes the unpaired case, _C_ is described by one of the three conditions : hairpin,interior loop, or a composition of structures i.e. a multi loop. _M_<sup>1</sup> is a multi loop with only one component, where are _M_ might have multiple of them. The _|_ icon is notation for _“or”_ .

In reality, however, at room temperature (or cell temperature), RNA is not actually in one single state, but rather varies in a Thermodynamic ensemble of structure. Base pairs can break their bonds quite easily, and although we might find an absolute optimum in terms of free energy, it might be the case that there is another sub-optimal structure which is very different from what e predicted and has an important role in

181

6.047/6.878 Lecture 08: RNA Structure

the cell. To fix the problem we can calculate the base pair probabilities to get the ensemble of structures, and then we can have a much better idea of what the RNA structure probably looks like. In order to do this, we utilize the Boltzman factor:


This gives us the probability of a given structure, in a thermodynamic system. We need to normalize the temperature using the partition function _Z_ ,which is the weighted sum of all structures, based on their Boltzman factor:


We can also represent this ensemble graphically, using a dot plot to visualize the base pair probabilities. To calculate the specific probability for a base pair ( _i, j_ ) , we need to calculate the partition function, which is given by the following formula :


To calculate _Z_ (the partition function over the whole structure), we use the recursion similar to the Nussinovs Algorithm (known as McCaskill Algorithm).The inner partition function is calculated using the formula:


With each of the additions corresponding to a different split in our sequence as the next figure illustrates. Note that the addition are multiplied to the energy functions since it is expressed as a exponential.


Similarly the outer partition function is calculated with a the same idea using the formula:


corresponding to different splits in the area outside the base pairs ( _i, j_ ).


182

6.047/6.878 Lecture 08: RNA Structure

## **10.6 Evolution of RNA**

It is useful to understand the evolution of RNA structure, because it unveils valuable data, and can also give us hints to refine our structure predictions. When we look into functionally important RNAs over time, we realize their nucleotides have changed at some parts, but their structure is well-conserved.

In RNA there are a lot of **compensatory mutations and consistent mutations** . In a consistent mutation, the structure doesnt change e.g. an AU pair mutates to form a G pair. In a compensatory mutation there are actually two mutations, one disrupts the structure, but the second mutation restores it, for example an AU pair changes to a CU which does not pair well, but in turn the U mutates to a G to restore a CG pair. In an ideal world, if we have this knowledge, this is the be the key to predict the RNA structure, because evolution never lies. We can calculate the **mutual information content** for two different RNAs and compare it. In other words, you compare the probabilities of two base pair structures agreeing randomly vs. if they have evolved to be conserve the structure.

The mutual information content is calculated via this formula:


If we normalize these probabilities, and store the MI in bits, we can plot it in a 3D model and track the evolutionary signatures. In fact, this was the method for determining the structure of ribosomal RNAs long before they were found by crystallography.

The real problem is that we dont have so much information, so what we usually do is combine the folding prediction methods with phylogenetic information in order to get a reliable prediction. The most common way to do this is to combine to Zuker algorithm with some covariance scores. For example, we add stabilizing energy if we have a compensatory mutation, and destabilizing energy if we have a single nucleotide mutation.

## **10.7 Probabilistic Approach to the RNA Folding Problem**

_RNA-coding sequence inside the genome_ Finding RNA-coding sequences inside the genome is a very hard problem. However there are ways to do it. One way is to combine the thermodynamic stability information, with a normalized RNAfold score and then we can do a Support Vector Machine (SVM) classification, and compare the thermodynamic stability of the sequence to some random sequences of the same GC content and the same length and see how many standard deviations is the given structure more stable that the expected value.

We can combine it with the evolutionary measure and see if the RNA is more conserved or not. This gives us (with relative accuracy) an idea if the genomic sequence is actually coding an RNA.

We have studied only half of the story. Although the thermodynamic approach is a good way (and the classic way) of folding the RNAs, some part of the community like to study it from a different aspect.

Lets assume for now that we dont know anything about the physics of RNA or the Boltzman factor. Instead, we look into the RNA as a string of letters for which we want to find the most probable structure. We have already learned about the Hidden Markov Models in the previous lectures. They are a nice way to make predictions about the hidden states of a probabilistic system. The question is can we use Hidden Markov models for the RNA folding problem? The answer is yes.

183

6.047/6.878 Lecture 08: RNA Structure

We can represent RNA structure as a set of hidden states of dots and brackets (recall the dot-bracket representation of RNA in part 3). There is an important observation to make here: the positions and the pairings inside the RNA are not independent, so we cannot simply have a state of an opening bracket without any considerations of the events that are happening downstream.

Therefore we need to extend the HMM framework to allow for nested correlations. Fortunately, the probabilistic framework to deal with such a problem already exists. It is known as stochastic context-free grammar (SCFG).

_Context Free Grammar in a nutshell_ You have:

- Finite set of non-terminal symbols (states) e.g. _{A, B, C}_ and terminal symbols e.g. _{a, b, c}_

- Finite set of Production rules. e.g. _{A → aB, B → AC, B → aa, → ab}_

- An initial (start) nonterminal

You want to find a way to get from one state to another (or to a terminal). _A → aB → aAC → aaaC → aaaab_ In a stochastic CFG, the only difference is that each relation has a certain probability.e.g. _P_ ( _B → AC_ ) = 0 _._ 25 _P_ ( _B → aa_ ) = 0 _._ 75

Phylogenetic evaluation is easily combined with SCFGs, since there are many probabilistic models for phylogenetic data. The Probabilistic models are not discussed in detail in this lecture but the following picture basically gives an analogy between the Stochastic models and the methods that we have see so far in the class.

- Analogies to thermodynamic folding:

   - CYK _↔_ Minimum Free energy (Nussinov/Zuker)

   - Inside/outside algorithm _↔_ Partition functions (McCaskill)

- Analogies to Hidden Markov models:

   - CYK Minimum _↔_ Viterbi’s algorithm

   - Inside/outside algorithm _↔_ Forward/backwards algorithm

- Given a parameterized SCFG (Θ _,_ Ω) and a sequence _x_ , the Cocke-Younger-Kasami (CYK) dynamic programming algorithm finds an optimal (maximum probability) parse tree _π_ ˆ: _π_ ˆ = _argmaxProb_ ( _π, x|_ Θ _,_ Ω)

- The _Inside algorithm_ , is used to obtain the total probability of the sequence given the model summed ovver all parse trees,

_Prob_ ( _x|_ Θ _,_ Ω) = Σ _Prob_ ( _x, π|_ Θ _,_ Ω)

### **10.7.1 Application of SCFGs**

- Consensus secondary structure prediction: Pfold

   - First Phylo-SCFG

184

6.047/6.878 Lecture 08: RNA Structure


© Stefan Washietl. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 10.14: A) Single sequence: Terminal symbols are bases or base-pairs, Emission probabilities are base frequencies in loops and paired regions B) Phylo-SCFG: Terminal symbols are single or paired alignment columns, Emission probabilities calculated from phylogenetic model and tree using Felsenstein’s algorithmWe to try to better understand RNA-RNA interactions.

- Structural RNA gene nding: EvoFold

**–** Uses Pfold grammar

- Two competing models:

   - ∗ Non-structural model with all columns treated as evolving independently

   - ∗ Structural model with dependent and independent columns

- Sophisticated parametrization

## **10.8 Advanced topics**

There still remain a host of other problems that need to be solved by studying RNA structure. This section will profile some of them.

### **10.8.1 Other problems**

Observe some of the problems depicted graphically below:

185

6.047/6.878 Lecture 08: RNA Structure


© Stefan Washietl. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 10.15: We can study kinetics and folding pathways in further depth.


© Stefan Washietl. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 10.16: We can investigate pseudoknots.

186

6.047/6.878 Lecture 08: RNA Structure


© Stefan Washietl. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 10.17: We can try to better understand RNA-RNA interactions.

### **10.8.2 Relevance**

There are plenty of RNAs inside the cell aside from mRNAs, tRNAs and rRNAs. The question is what is the relevance of all this non-coding RNA? Some believe it is noise resulted through experiment, some think its just biological noise that doesnt have a meaning in the living organism. On the other hand some believe junk RNA might actually have an important role as signals inside the cell and all of it is actually functional, the truth probably lies somewhere in between.

### **10.8.3 Current research**

_There are conserved regions in the genome that do not code any proteins, and now Stefans et al. are looking into them to see if they have structures that are stable enough to form functional RNAs. It turns out that around 6% of these regions have hallmarks of good RNA structure, which is still 30000 structural elements. The group has annotated some of these elements, but there is still a long way to go. a lot of miRNA, snowRNAs have been found and of course lots of false positives. But there exciting results coming up in this topic! so the final note is, it’s a very good area to work in!_

## **10.9 Summary and key points**

1. The functional spectrum of RNAs is practically unlimited

   - (a) RNAs similar to contemporary Ribozymes and Riboswitches might have existed in an RNA world. Some of them still exist as living fossils in current cells.

   - (b) Evolutionarily younger RNAs including miRNAs and many long ncRNAs form a non-protein based regulatory layer.

187

6.047/6.878 Lecture 08: RNA Structure

2. RNA structure is critical for their function and can be predicted computationally

   - (a) Nussinov/Zuker: Minimum Free Energy structure

   - (b) McCaskill: Partition function and pair probabilities

   - (c) CYK/Inside-Outside: probabilistic solution to the problem using SCFGs

3. Phylogenetic information can improve structure prediction

4. Computational biology of RNAs is an active eld of research with many hard algorithmic problems still open

## **10.10 Further reading**

- Overview

   - Washietl S, Will S. et al. Computational analysis of noncoding RNAs. Wiley Interdiscip Rev RNA. 2012, 10.1002/wrna.1134

- RNA function: review papers by John Mattick

- Single sequence RNA folding

   - Nussinov R, Jacobson AB, Fast algorithm for predicting the secondary structure of single-stranded RNA.Proc Natl Acad Sci U S A. 1980 Nov; 77:(11)6309-13

   - Zuker M, Stiegler P Optimal computer folding of large RNA sequences using thermodynamics and auxiliary information. Nucleic Acids Res. 1981 Jan; 9:(1)133-48

   - McCaskill JS The equilibrium partition function and base pair binding probabilities for RNA secondary structure. Biopolymers. 1990; 29:(6-7)1105-19

   - Dowell RD, Eddy SR, Evaluation of several lightweight stochastic context-free grammars for RNA secondary structure prediction. BMC Bioinformatics. 2004 Jun; 5:71

   - Do CB, Woods DA, Batzoglou S, CONTRAfold: RNA secondary structure prediction without physics-based models. Bioinformatics. 2006 Jul; 22:(14)e90-8

- Consensus RNA folding

   - Hofacker IL, Fekete M, Stadler PF, Secondary structure prediction for aligned RNA sequences. J Mol Biol. 2002 Jun; 319:(5)1059-66

   - Knudsen B, Hein J, RNA secondary structure prediction using stochastic context-free grammars and evolutionary history. Bioinformatics. 1999 Jun; 15:(6)446-54

- RNA gene finding

   - Pedersen JS, Bejerano G, Siepel A, Rosenbloom K, Lindblad-Toh K, Lander ES, Kent J, Miller W, Haussler D Identication and classication of conserved RNA secondary structures in the human genome. PLoS Comput Biol. 2006 Apr; 2:(4)e33

   - Washietl S, Hofacker IL, Stadler PF, Fast and reliable prediction of noncoding RNAs. Proc Natl Acad Sci U S A. 2005 Feb; 102:(7)2454-9

188

6.047/6.878 Lecture 08: RNA Structure

## **Bibliography**

- [1] R Durbin. _Biological Sequence Analysis_ .

- [2] W. Gilbert. ”origin of life: The rna world”. _Nature._ , 319(6055):618, 1986.

- [3] Rachel Sealfon, 2012. Extra information taken from Recitation 5 slides.

- [4] Z. Wang, M. Gestein, and M. Snyder. Rna-seq: a revolutionary tool for transcriptomics. _Nat Rev Genet._ , 10(1):57–63, 2009.

- [5] Stefan Washietl, 2012. All pictures/formulas courtesy of Stefan’s slides.

- [6] R. Weaver. _Molecular Biology_ . 3rd edition.

189

6.047/6.878 Lecture 08: RNA Structure

190

CHAPTER

## **ELEVEN**

RNA MODIFICATIONS

|**Figures**|||
|---|---|---|
|11.1|mRNA is not always an appropriate proxy for protein levels.<br>. . . . . . . . . . . . . . . .|190|
|11.2|Discrepancy between mRNA levels and protein abundance.<br>. . . . . . . . . . . . . . . . .|190|
|11.3|The genetic signals which amino acids are mapped to specific three nucleotide sequences.|190|
|11.4|Depiction of ribosome profiles when Cyclohexamide (elongation freeze) or Harringtonine<br>are used (initiation freeze).<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|192|
|11.5|Ribosome profile when harringtonine is used vs. no drug. The red peaks show the different<br>places initiation of translation can start, depicting the different possible isoforms. . . . . .|192|
|11.6|Ribosome profile when harringtonine is used vs. no drug. The red peaks previously un-<br>identified ORFs.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|193|
|11.7|Ribosome profile when during rich conditions and starvation conditions. This images shows<br>the dramatic decrease in translation of proteins during starvation. The mRNA profile is<br>not indicative of this. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|193|


## **11.1 Introduction**

Many ideas in biology rely on knowing the protein levels in a cell. Protein abundance is often extrapolated from corresponding mRNA levels. This extrapolation is made as it is relatively easy to measure mRNA levels. In addition, for a long time, it was thought that all of the regulation of expression occurred prior to mRNA formation. Now, it is known that expression continues to be regulated at the translation stage. Figure 1 shows that the data available for post-transcriptional regulation is minimal and illustrates an example of how mRNA levels are not indicative of protein abundance.

191

6.047/6.878 Lecture 9: RNA Modifications

```
images/BadProxy.png
```

Figure 11.1: mRNA is not always an appropriate proxy for protein levels.

There are many factors that may be affecting how mRNA is translated, causing mRNA level to not be directly related to protein levels. These factors include:

1. **_Translation elongation rates_**

   - depends on codon usage bias, tRNA adaptation, and RNA editing

2. **_Translation initiation rates_**

   - depends on AUG frequency, TOP presence, type of initiation (cap-dependent/IRES), and secondary

   - structures

3. **_Translation termination rates_**

   - depends on termination codon identity

4. **_mRNA degradation rates_**

   - depends on polyA tail length, capping, mRNA editing, and secondary structure

5. **_Protein degradation rates_**

   - depends on PEST sequences, protein stability, unstructured regions, and the presence of polar amino acids

6. **_Cis and Trans regulatory elements_**

   - depends on AU-rich elements, miRNAs, ncRNAs, and RNA-binding proteins

```
images/ProteinAbundance.png
```

Figure 11.2: Discrepancy between mRNA levels and protein abundance.

## **11.2 Post-Transcriptional Regulation**

### **11.2.1 Basics of Protein Translation**

For the basics of transcription and translation, refer to Lecture 1, sections 4.3 - 4.5.

```
images/GeneticCode.png
```

Figure 11.3: The genetic signals which amino acids are mapped to specific three nucleotide sequences.

The genetic code is almost universal.

192

6.047/6.878 Lecture 9: RNA Modifications

## **_FAQ_**

- **Q:** Why is genetic code so similar across organisms?

- **A:** Genomic material is not only transmitted vertically (from parents) but also horizontally between organisms. This gene interaction creates an evolutionary pressure for an universal genetic code.

## **_FAQ_**

- **Q:** What accounts for the slight differences in the genetic code across organisms?

- **A:** Late/early evolutionary arrival of amino acids can account for the differences. Also, certain species (e.g. bacteria in deep sea vents) have more resources to synthesize specific amino acids, thus they will favor those in the genetic code.

## **_Did You Know?_**

Threonine and Alanine are often accidentally interchanged by tRNA sythetase because they originated from one amino acid.

### **11.2.2 Measuring Translation**

Translation efficiency is defined as,


We are interested in seeing just how much of our mRNA is translated to protein, i.e. the efficiency. However, specifically measuring how much mRNA becomes protein is a difficult task, one that requires a bit of creativity. There are a variety of ways to tackle this problem, but each has its own downfalls:

1. **_Measure mRNA and protein levels directly_**

   - Pitfall: Does not consider rates of synthesis and degradation. This method measures the protein levels for the ’old’ mRNA since there is a time lag from mRNA to protein.

2. **_Use drugs to inhibit transcription and translation_** Pitfall: Drugs have side effects altering translation

3. **_Artificial fusion of proteins with tags_**

   - Pitfall: Protein tags can affect protein stability

4. **_Pulse label with radioactive nucleosides or amino acids (SILAC)_** **in use today** Pitfall: Offers no information on dynamic changes: it is simply a snapshat of the resulting mRNA and protein levels after X hours

193

6.047/6.878 Lecture 9: RNA Modifications

Another common technique is using ’ribosome profiling’ to measure protein translation at subcodon resolution. This is done by freezing ribosomes in the process of translation and degrading the non-ribosome protected sequences. At this point, the sequences can be pieced back together and the frequency with which a region is translated can be interpolated. The disadvantage to using these ribosome footprints, to see which regions are being translated, is that regions in between ribosomes are lost. This technique requires an RNA-seq in parallel.

The question remains, why is Ribosome profiling advantageous? This technique is a better approach to measuring protein abundance as it:

1. Is a **_better measure of protein abundance_**

2. Is **_independent of protein degradation_** (compared to the protein abundance/mRNA ratio)

3. Allows us to **_measure codon-specific translation rates_**

Using ribosome profiling, it is possible to see which codon is being decoded: this is done by mapping ribosome footprints and then deciphering the translating codon based on footprint length. We can the verify our prediction by mapping translated codon profiles based on periodicity (three bases in a codon). The technique can be improved even further by using anti-translation drugs such as _harringtonine_ and _cyclohexamide_ . Cyclohexamide blocks elongation and Harringtonine inhibits initiation. The later can be used to find the starting points (which genes are about to be translated). Figure 4 shows the effects of the drugs on the ribosome profiles.

```
images/TranslationDrugs.png
```

Figure 11.4: Depiction of ribosome profiles when Cyclohexamide (elongation freeze) or Harringtonine are used (initiation freeze).

This technique has much more to offer than simply quantifying translation. Ribosome profiling allows for:

1. **_Prediction of alternative isoforms_** (different places where translation can start)

```
images/AltIsoforms.png
```

Figure 11.5: Ribosome profile when harringtonine is used vs. no drug. The red peaks show the different places initiation of translation can start, depicting the different possible isoforms.

#### 2. **_Prediction of un-indentified ORFs_** (open reading frames)

194

6.047/6.878 Lecture 9: RNA Modifications

```
images/uORFs.png
```

Figure 11.6: Ribosome profile when harringtonine is used vs. no drug. The red peaks previously un-identified ORFs.

3. **_Comparing translation across different environmental conditions_**

```
images/Conditions.png
```

Figure 11.7: Ribosome profile when during rich conditions and starvation conditions. This images shows the dramatic decrease in translation of proteins during starvation. The mRNA profile is not indicative of this.

4. **_Comparing translation across life stages_**

Thus, we see that ribosome profiling is a very powerful tool with lots of potential to reveal previously elusive information about the translation of a genome.

### **11.2.3 Codon Evolution**

#### **Basic concepts**

Something to make clear is that codons are _not_ used with equal frequencies. In fact, which codons can be considered optimal differs across different species based on RNA stability, strand-specific mutation bias, transcriptional efficacy, GC composition, protein hydropathy, and translational efficiency. Likewise, tRNA isoacceptors are not used with equal frequencies within and across species. The motivation for the next section is to determine how we may measure this codon bias.

#### **Measures of Codon Bias**

There are a few methods to accomplish this task:

a) Calculate the frequency of optimal codons, which is defined as “optimal” codons/ sum of “optimal” and “non-optimal” codons. The limitations to this method are that this requires knowing which codon is recognized by each tRNA and it assumes that tRNA abundance is highly correlated with tRNA gene copy number.

b) Calculate a codon bias index. This measures the rate of optimal codons with respect to the total codons encoding for that same amino acid. However, in this case the number of optimal codons are normalized with respect to the expected random usage. _CBI_ = ( _oopt − erand_ ) _/_ ( _otot − erand_ ). The limitation of this method

195

6.047/6.878 Lecture 9: RNA Modifications

is that it requires a reference set of proteins, such as highly expressed ribosomal proteins.

c) Calculate a codon adaptation index. This measures the relative adaptiveness or deviation of the codon usage of a gene towards the codon usage of a reference set of proteins, i.e. highly expressed genes. It is defined as the geometric mean of the relative adaptiveness values, measured as weights associated to each codon over the length of the gene sequence (measured in codons). Each weight is computed as the ratio between the observed frequency of a given codon and the frequency of its corresponding amino acid. The limitation to this approach is that it requires the definition of a reference set of proteins, just as the last method did.

d) Calculate the effective number of codons. This measures the total number of different codons used in a sequence, which measures the bias toward the use of a smaller subset of codons, away from equal use of synonymous codons. _Nc_ = 20 if only one codon is used per amino acid, and _Nc_ = 61 when all possible synonymous codons are used equally. The steps to the process are to compute the homozygosity for each amino acid as estimated from the squared codon frequencies, obtain effective number of codons per amino acid, and compute the overall number of effective codons. This method is advantageous because it does not require any knowledge of tRNA-codon pairing, and it does not require any reference set However, it is limited in that it does not take into account the tRNA pool.

e) Calculate the tRNA adaptation index. Assume that tRNA gene copy number has a high positive correlation with tRNA abundance within the cell. This then measures how well a gene is adapted to the tRNA pool.

It is important to distinguish among when to use each index. The situation in which a certain index is favorable is very context-based, and thus it is often preferable to use one index above all others when the situation calls for it. By carefully choosing an index, one can uncover information about the frequency by which a codon is translated to an amino acid.

#### **RNA Modifications**

The story becomes more complicated when we consider modifications that can occur to RNA. For instance, some modifications can expand or restrict the wobbling capacity of the tRNA. Examples include insosine modifications and xo<sup>5</sup> U modifications. These modifications allow tRNAs to decode a codon that they could not read before. One might ask why RNA modification was positively selected in the context of evolution, and the rationale is that this allows for the increase in the probability that a matching tRNA exists to decode a codon in a given environment.

#### **Examples of applications**

There are a few natural applications that result form our understanding of codon evolution.

- a) Codon optimization for heterologous protein expression

> b) Predicting coding and non-coding regions of a genome

> c) Predicting codon read-through

- d) Understanding how genes are decoded - studying patterns of codon usage bias along genes

196

6.047/6.878 Lecture 9: RNA Modifications

### **11.2.4 Translational Regulation**

There are many known means of regulation at the post-transcriptional level. These include modulation of tRNA availability, changes in mRNA, and cis -and trans-regulatory elements. First, tRNA modulation has a large impact. Changes in tRNA isoacceptors, changes in tRNA modifications, and regulation at tRNA aminoacylation levels. Changes in mRNA that affect translation include changes in mRNA modification, polyA tail, splicing, capping, and the localization of mRNA (importing to and exporting from nucleus). Cisand trans- regulatory elements include RNA interference (i.e. siRNA and miRNA), frameshift events, and riboswitches. Additionally, many regulatory elements are still yet to be discovered!

## **11.3 Current Research Directions**

## **11.4 Further Reading**

## **11.5 Tools and Techniques**

## **11.6 What Have We Learned?**

Hopefully at the end of this chapter we have come to realize the importance in transcriptional regulation. We see that mRNA levels are not 1:1 with protein levels. Additionally, we saw that the genetic code is not universal, and what are considered preferred tRNA-codon pairs are dynamic. Likewise, synonymous mutations are not equivalent across species. We have seen how powerful the technique of ribosome profiling is, as it allows us to measure translation with subcodon resolution. Despite all this, it is possible to model translation and codon evolutions using tools to help increase translation efficiency/folding of proteins in heterologous systems, predict coding regions, understand cell type-specific translation patterns, and compare translation between healthy and disease states. Finally, by analyzing translational regulation, we see how protein levels are tuned, and we see that there are many different ways to achieve post-transcriptional regulation. Perhaps we may come to realize that there is more interconnection between these different regulation strategies than we originally thought.

## **Bibliography**

197

6.047/6.878 Lecture 9: RNA Modifications

198

CHAPTER

**TWELVE**

## LARGE INTERGENIC NON-CODING RNAS

Guest lecture by John Rinn Scribed by Eli Stickgold (2010)

### **Figures**

|12.1|Tuxedo Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|200|
|---|---|---|
|12.2|How spaced seeds indexing works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|200|
|12.3|How Burrows-Wheeler indexing works . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|201|
|12.4|An example of a gap in alignment<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|201|
|12.5|An example of how to use the graph to find transcripts. . . . . . . . . . . . . . . . . . . .|202|
|12.6|_F_1<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|202|
|12.7|_F_2<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|203|
|12.8|Technical variability follows a Poisson distribution<br>. . . . . . . . . . . . . . . . . . . . . .|204|
|12.9|Human fibroblasts specialize via epigenetic regulation to form different skin types based<br>on their location within the body. Research has found that the type of skin in the hands<br>shares a remarkably similar epigenetic signature to the skin in the feet, which is also distally<br>located.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|205|
|12.10|Two skin cell types are analyzed for their chromatin domains. There exists a clear boundary<br>between the lung cell type which is proximal to the body, and the foot cell type which is<br>distal to the body.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|205|
|12.11|Polycomb, a protein that can remodel chromatin so that epigenetic silencing of genes can<br>take place, may be regulated by non-coding RNA such as HOTAIR.<br>. . . . . . . . . . . .|205|
|12.12|lincRNAs neighbor developmental regulators<br>. . . . . . . . . . . . . . . . . . . . . . . . .|207|


## **12.1 Introduction**

Epigenetics is the study of heritable changes in genetic expression and phenotype that do not result from a sequence of DNA. Each cell, despite having an identical copy of the genome, is able to differentiate into

199

6.047/6.878 Lecture 11: Large Intergenic non-Coding RNAs

a specialized type. There are many biological devices for accomplishing these including DNA methylation, histone modification, and various types of RNA.

DNA methylation is a binary code that is effectively equivalent to turning a gene ”on” or ”off”. However, often times a gene might need to be more highly expressed as opposed to just being turned on. For this, histones have tails that are subject to modification. The unique combination of these two elements on a stretch of DNA can be thought of as a barcode for cell type. Even more important is the method of their preservation during replication. In the case of DNA methylation, one appropriately methylated strand is allocated to each mother or daughter cell. By leaving one trail behind, the cell is able to fill in the gaps and appropriately methylate the other cell.

As the intermediary between DNA sequences and proteins, RNA is arguably the most versatile means of regulation. As such, they will be the focus of this chapter.

## **_Did You Know?_**

Cell types can be determined by histone modification or DNA methylation (a binary code, which relies on a euchromatic and heterochromatic state). These histone modifications can be thought of as a type of epigenetic barcode that allows cell DNA to be scanned for types. Non-coding RNAs called Large Intergenic Non-Coding RNAs (lincRNAs) are heavily involved in this process.

A quick history of RNA:

- **1975:** A lab testing relative levels of RNA and DNA in bull sperm discovers twice as much RNA as DNA.

- **1987:** After automated sequencing developed, weird non-coding RNAs are first found.

- **1988:** RNA is proved to be important for maintaining chromosome structures, via chromatin architecture

- **1990s:** A large number of experiments start to research

- **2000s:** Study shows Histone-methyltransferases depend on RNA, as RNAase causes the proteins to delocalize.

Transcription is a good proxy of what’s active in the cell and what will turn into protein. Microarrays led to the discovery of twice as many non-coding genes as coding genes initially; now we know the ratio is even far higher than this.

## **12.2 Noncoding RNAs from Plants to Mammals**

Basic Cycle: large RNA gets chopped up into small RNAs (siRNAs) RNA use by category:

**Protists:** RNA is used as a template to splice out DNA (RNA-dependent DNA elimination and splicing)

- **mRNA and DNA in nucleus:** DNA chopped and recombined based on gaps in mRNA (“quirky phenomena”)

- **Plants:** RNA-dependent RNA polymerase, where the polymerase takes template of RNA and make a copy of it, is available in plants but not humans, and can make small RNAs. Mammals have at most one

200

6.047/6.878 Lecture 11: Large Intergenic non-Coding RNAs

copies. Very different than RNA polymerase and DNA polymerase in structure. From this, we know that plants do DNA methylation with noncoding RNA.

**Flies:** use RNAs for an RNA switch; coordinated regulation of hox gene requires noncoding RNA.

**Mammals:** Non-coding RNAs can form triple helices, guide proteins to them; chromatin-modifying complexes; involved in germ line; guide behaviour of transcription factors.

For the rest of this talk, we focus on specifically lincRNA, which we will define as RNA larger than 200 nucleotides.

### **12.2.1 Long non-coding RNAs**

There are a number of different mechanisms and biological devices by which epigenetic regulation occurs. One of these is long non-coding RNAs which can be thought of as fulfilling an air traffic control function within the cell.

Long non-coding RNAs share many similar characteristics with microRNAs. They are spliced, contain multiple exons, are capped, and poly-adenuated. However, they do not have open reading frames. They look just like protein coding genes, but cannot.

They are better classified by their anatomical position:

**Antisense:** These are encoded on the opposite strand of a protein coding gene.

**Intronic:** Entirely contained with an intron of a protein coding gene.

**Bidirectional:** These share the same promoter as a protein coding gene, but are on the opposite side.

**Intergenic:** These do not overlap with any protein coding genes. Think of them as sitting blindly out in the open. They are much easier targets and will be the focus of this chapter.

## **12.3 Practical topic: RNAseq**

RNA-seq is a method that utilizes next-generation sequencing technology to sequence cDNA allowing us to gain insight into the contents of RNA. The two main problems that RNA-seq addresses are (1) discover new genes such as splice isoforms of previously discovered genes and (2) uncover the expression levels of genes and transcripts from the sequencing data. Additionally, RNA-seq is also beginning to replace many traditional sequencing techniques allowing labs to perform experiments more efficiently.

### **12.3.1 How it works**

The RNA-Seq machine grabs a transcript and breaks it into different fragments, where the fragments are normally distributed. With the speed that the RNA-seq can sequence these transcript fragments (or reads), there are an abundant number of reads allowing us to extract expression levels. The basic idea behind this method relies on the fact that the more abundant a transcript is, the more fragments we’ll sequence from it.

201

6.047/6.878 Lecture 11: Large Intergenic non-Coding RNAs

The tools used to analyze RNA-Seq data are collectively known as the “Tuxedo Tools”


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

#### Figure 12.1: Tuxedo Tools

### **12.3.2 Aligning RNA-Seq reads to genomes and transcriptomes**

Since RNA-Seq produces so many reads, the alignment algorithm must have a fast runtime, approximately of the order of O(n). There are two main strategies for aligning short reads, which require that we already have the transcripts.

1. Spaced seeds indexing


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 12.2: How spaced seeds indexing works

Spaced seeds indexing involves taking each read and breaking it into fragments, or “seeds”. We take every combination of two fragments (“seed pairs”) and compare them to an index of seeds (which will

202

6.047/6.878 Lecture 11: Large Intergenic non-Coding RNAs

take tens of gigabytes of space) for potential hits. Compare the other seeds to the index to make sure we have a hit.

2. Burrows-Wheeler indexing


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 12.3: How Burrows-Wheeler indexing works

Burrows-Wheeler indexing takes the genome and scrambles it up in such a way such that you can look at the read one character at a time and throw out a huge chunk of the genome as possible alignment positions very quickly.

One major problem with these two general purpose alignment strategies is that they don’t account for large gaps in alignment.


Figure 12.4: An example of a gap in alignment

To get around this, TopHat breaks the reads into smaller pieces. These pieces are aligned and reads with pieces that are mapped far apart are flagged for possible intron sites. The pieces that weren’t able to be aligned are used to confirm the splice sites. The reads are then stitched back together to make full read alignments.

There are two strategies for assembling transcripts based on RNA-Seq reads.

203

6.047/6.878 Lecture 11: Large Intergenic non-Coding RNAs

1. Genome-guided approach (used in software such as Cufflinks)

The idea behind this approach is that we don’t necessarily know if two reads come from the same transcript, but we will know if they come from different transcripts. The algorithm is as follows: take the alignments and put them in a graph. Add an edge from _x → y_ if _x_ is to the left of _y_ in the genome, _x_ and _y_ overlap consistently, and _y_ is not contained in _x_ . So we have an edge from _x → y_ if they might come from the same transcript.


Figure 12.5: An example of how to use the graph to find transcripts

If we walk across this graph from left to right, we get a potential transcript. Applying Dilworth’s theorem to read partial orders, we can see that the size of the largest antichain in the graph is the minimum number of transcripts needed to explain the alignment. An antichain is a set of alignments with the property that no two are compatible (i.e. could arise from the same transcript)

2. Genome-independent approach (used in software such as trinity)

The genome-independent approach attempts to piece together the transcripts directly from the reads using classical methods for overlap based read assembly, similar to the genome assembly methods.

### **12.3.3 Calculating expression of genes and transcripts**

We want to count the number of reads from each transcript to find the expression level of the transcript. However, since we divide transcripts into equally-sized fragments, we run into the problem that longer transcripts will naturally produce more reads than a shorter transcript. To account for this, we compute expression levels in FPKM, fragments per kilobase per million fragments mapped.

#### **Likelihood function for a gene**

Suppose we sequence a particular read, call it _F_ 1.


Figure 12.6: _F_ 1

204

6.047/6.878 Lecture 11: Large Intergenic non-Coding RNAs

In order to get this particular read, we need to pick the particular transcript it’s in and then we need to pick this particular read out from the whole transcript. If we define _γ_ green to be the relative abundance of the green transcript, then we have


where _l_ green is the length of the green transcript. Now suppose we look at a different read, _F_ 2.


It could have come from either the green transcript of the blue transcript, so:


We can see that the probability of getting both _F_ 1 and _F_ 2 is just the product of the individual probabilities:


We define this as our likelihood function, _L_ ( _F |γ_ ). Given an input of abundances, we get a probability of how likely our sequence of reads is. So from a set of reads and transcripts, we can build a likelihood function and calculate the values for gamma that will maximize this function. Cufflinks achieves this using hill climbing or EM on the log-likelihood function.

### **12.3.4 Differential analysis with RNA-Seq**

Suppose we perform an RNA-Seq analysis for a gene under two different conditions. How can we tell if there is a significant difference in the fragment counts? We calculate expression by estimating the expected number of fragments that come from each transcript. To test for significance, we need to know the variance of that estimate. We model the variance as:

Var(expression) = Technical variability + Biological variability

Technical variability, which is variability from uncertainty in mapping reads, can be modeled well with a Poisson distribution (see figure below). However, using Poisson to model biological variability, or variability across replicates, results in overdispersion.

205

6.047/6.878 Lecture 11: Large Intergenic non-Coding RNAs


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 12.8: Technical variability follows a Poisson distribution

In the simple case where we have variability across replicates, but no uncertainty, we can mix the Poisson distributions from each replicate into a new distribution to model biological variability. We can treat the lambda parameter of the Poisson distribution as a random variable that follows a gamma distribution:


The counts from this model follow a negative binomial distribution. To figure out the parameters for the negative binomial for each gene, we can fit a gamma function through a scatter plot of the mean count vs. count variance across replicates.

In the simple case where there is read mapping uncertainty, but not biological variability, we need to include the mapping uncertainty in our variance estimate. Since we assign reads to transcripts probabilistically, we need to calculate the variance in that assignment.

The two threads of RNA-Seq expression analysis research focus on the problems in these two simple cases. One of the threads focuses on inferring the abundances of individual isoforms to learn about differential splicing and promoter use, while the other thread focuses on modeling variability across replicates to create more robust differential gene expression analysis. Cuffdiff unites these two separate threads to study the case where we have biological variability and read mapping ambiguity. Since overdispersion can be modeled with a negative binomial distribution and mapping uncertainty can be modeled with a Beta distribution, we combine these two to model this case with a beta negative binomial distribution.

## **12.4 Long non-coding RNAs in Epigenetic Regulation**

Let’s examine human skin as an example of long non-coding RNAs being used in epigenetic regulation. Human skin is huge, in fact it is the largest organ by weight in the body. It is intricate, with specialized features, and it is constantly regenerating to replace old dead cells with new ones. The skin must be controlled so hair only grows on the back of your hand rather than on your palm. Moreover, these boundaries cannot

206

6.047/6.878 Lecture 11: Large Intergenic non-Coding RNAs

change and are maintained ever since birth.

The skin in all parts of the body is composed of an epithelial layer and a layer of connective tissue made up of cells called fibroblasts. These fibroblasts secrete cytokine signals that control the outer layer, determining properties such as the presence or absence of hair. Fibroblasts all around the body are identical except for the specific epigenetic folding that dictates what type of skin will be formed in a given location. Based on whether the skin is distal or proximal, interior or exterior, posterior or anterior, a different set of epigenetic folds will determine the type of skin that forms.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 12.9: Human fibroblasts specialize via epigenetic regulation to form different skin types based on their location within the body. Research has found that the type of skin in the hands shares a remarkably similar epigenetic signature to the skin in the feet, which is also distally located.

It has been found that specific HOX genes delineate these anatomical boundaries during development. Just by looking at the human HOX genetic code, one can predict where a cell will be located. Using ChIPon-chip (chromatin immunoprecipitation microarrays) diamteric chromatin domains have been found among these HOX genes. In the figure below, we can see a clear boundary between the chromatin domains of a cell type located proximally and another located distally. Not only is this boundary precise, but it is maintained across trillions of skin cells.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 12.10: Two skin cell types are analyzed for their chromatin domains. There exists a clear boundary between the lung cell type which is proximal to the body, and the foot cell type which is distal to the body.

HOTAIR or HOX transcript antisense intergenic RNA has been investigated as possible RNA regulator that keeps these boundary between the diametric domains in chromatin. When HOTAIR was knocked out in the HOXC locus, it was hypothesized that the chromatin domains might slip through into one another. While it was found that this HOTAIR did not directly affect the epigenetic boundary, researchers did find evidence of RNA based genomic cross talk. The HOTAIR gene affected a different locus called HOXD.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 12.11: Polycomb, a protein that can remodel chromatin so that epigenetic silencing of genes can take place, may be regulated by non-coding RNA such as HOTAIR.

Through a process of ncRNA dependent Polycomb repression, the HOTAIR sequence can control epigenetic regulation. Plycomb is a portein that puts stop marks on the tails of histones so that they can cause specific folds in the genetic material. On their own histones, are undirected, so it is necessary for some

207

6.047/6.878 Lecture 11: Large Intergenic non-Coding RNAs

mechanism to dictate how they attach to the genome. This process of discovery has led to great interest in the power of long intergenic non-coding RNAs to affect epigenetic regulation.

## **12.5 Integergenic Non-coding RNAs: missing lincs in Stem/Cancer cells?**

### **12.5.1 An example: XIST**

XIST was one of the first lincRNAs to be characterized. It is directly involved in deactivation of one of the female X chromosomes during embryonic development. It has been described as having the ability to ”crumple an entire chromosome”. This is important because deactivation prevents lethal overexpression of genes found on the X chromosome.

RNA is important for getting polychrome complex to chromosome ncRNAs can activate downstream genes in Cis, opposite in trans; Xist does the same thing.

## **12.6 Technologies: in the wet lab, how can we find these?**

How would we find ncRNAs? We have about 20-30 examples of ncRNAs with evidence of importance, but more are out there. Chromatin state maps (from ENCODE, chip-seq) can be used to find transcriptional units that do not overlap proteins. We can walk along map and look for genes (look by eye at chromatin map to find ncRNAs). Nearly 90% of time such a signature is found, RNA will be transcribed from it. We can validate this through northern blot

When looking at a chromatin map to find ncRNAs, we are essentially looking through the map with a window of a given size and seeing how much signal vs. noise we are getting, compared to what we might expect from a random-chance hypothesis. As both large and small windows have benefits, both should be used on each map section. Larger windows encapulate more information; smaller windows are more sensitive.

After finding integenic regions, we find conserved regions.

We check if new regions are under selective pressure; fewer mutations in conserved regions. If a nucleotide never has a mutation between species, it’s highly conserved.

linc-RNAs are more conserved than introns, but less conserved than protein-coding introns, possibly due to non-conserved sequences in loop regions of lincRNAs.

Finding what lincRNAs’ functions are: “Guilt by association”: We can find proteins that correlate with particular lincRNA in terms of expression; lincRNAs are probably correlated to a particular pathway. In this way, we acquire a multidimensional barcode for each lincRNA (what it is and is not related to). We Can cluster lincRNA signatures and identify common patterns. Lots have to do with cell cycle genes. (This approach works 60-70% of the time)

As most lincRNAs are over 3000 bases, many contain sequences for 100 amino acid open reading frames, simply by chance. This results in many false negatives during detection.

208

6.047/6.878 Lecture 11: Large Intergenic non-Coding RNAs

It has been found that many lincRNAs tend to neighbor developmental regions of the genome. They also tend to be lowly expressed compared to protein coding genes.


Figure 12.12: lincRNAs neighbor developmental regulators

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

### **12.6.1 Example: p53**

Independent validation: we use animal models, where one is a wild-type p53, andone is a knockout. We induce p53, then ask if lincRNAs turn on. 32 of 39 lincRNAs found associated with p53 were temporally induced upon turning on p53.

One RNA in particular sat next to a protein-coding gene in the p53 pathway. We tried to figure out if p53 bound to promoter and turned it on. To do this, we cloned the promoter of lincRNA, and asked does p53 turn it on? We IPed the p53 protein, to see if it associated with the lincRNA of the promoter. It turned out that lincRNA is directly related to p53 - p53 turns it on. P53 also turns genes off - certain lincRNAs act as a repressor.

From this example (and others), we start to see that RNAs usually have a protein partner

RNA can bring myriad of different proteins together, allowing the cell lots of diversity. In this way its similar to phosphorylation. RNAs bind to important chromatin complexes, and is required for reprogramming skin cells into stem cells.

209

6.047/6.878 Lecture 11: Large Intergenic non-Coding RNAs

## **12.7 Current Research Directions**

- **12.8 Further Reading**

- **12.9 Tools and Techniques**

## **12.10 What Have We Learned?**

## **Bibliography**

- [1] R.P. Dilworth. A decomposition theorem for partially ordered sets. _Annal of Mathematics_ , 1950.

- [2] Mitchell Guttman, Manuel Garber, Joshua Z Levin, Julie Donaghey, James Robinson, Xian Adiconis, Lin Fan, Magdalena J Koziol, Andreas Gnirke, Chad Nusbaum, and et al. Ab initio reconstruction of cell type-specific transcriptomes in mouse reveals the conserved multi-exonic structure of lincrnas. _Nature Biotechnology_ , 28(5):503–510, 2010.

- [3] C. Trapnell.

210

CHAPTER

**THIRTEEN**

SMALL RNA

Guest Lecture by David Bartel (MIT/Whitehead/HHMI) Scribed by Boyang Zhao (2011)

### **Figures**

|13.1 siRNA and miRNA biogenesis pathways . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>213|
|---|
|13.2 Protein and mRNA changes following miR-223 loss . . . . . . . . . . . . . . . . . . . . . .<br>214|


## **13.1 Introduction**

Large-scale analyses in the 1990s using expressed sequence tags have estimated a total of 35,000 - 100,000 genes encoded by the human genome. However, the complete sequencing of human genome has surprisingly revealed that the numbers of protein-coding genes are likely to be _∼_ 20,000 – 25,000 [12]. While this represents _<_ 2% of the total genome sequence, whole genome and transcriptome sequencing and tiling resolution genomic microarrays suggests that over _>_ 90% of the genome is still actively transcribed [8], largely as non-proteincoding RNAs (ncRNAs). Although initial speculation has been that these are non-functional transcriptional noise inherent in the transcription machinery, there has been rising evidence suggesting the important role these ncRNAs play in cellular processes and manifestation/progression of diseases. Hence these findings challenged the canonical view of RNA serving only as the intermediate between DNA and protein.

### **13.1.1 ncRNA classifications**

The increasing focus on ncRNA in recent years along with the advancements in sequencing technologies (i.e. Roche 454, Illumina/Solexa, and SOLiD; refer to [16] for a more details on these methods) has led to an explosion in the identification of diverse groups of ncRNAs. Although there has not yet been a consistent nomenclature, ncRNAs can be grouped into two major classes based on transcript size: small ncRNAs ( _<_ 200

211

6.047/6.878 Lecture 12: Small RNA

nucleotides) and long ncRNAs (lncRNAs) ( _≥_ 200 nucleotides) (Table 13.1 ) [6, 8, 13, 20, 24]. Among these, the role of small ncRNAs microRNA (miRNA) and small interfering RNA (siRNA) in RNA silencing have been the most well-documented in recent history. As such, much of the discussion in the remainder of this chapter will be focused on the roles of these small ncRNAs. But first, we will briefly describe the other diverse set of ncRNAs.

Table 13.1: ncRNA classifications (based on [6, 8, 13, 20, 24])

|Name|Abbreviation|Function|
|---|---|---|
||_Housekeeping RNAs_||
|Ribosomal RNA|rRNA|translation|
|Transfer RNA|tRNA|translation|
|Small nucleolar RNA<br>i|snoRNA (_∼_60-220 nt)|rRNA modification<br>i|
|Small Cajal body-specific RNA|scaRNA|splicesome modification|
|Small nuclear RNA|snRNA (_∼_60-300 nt)|RNA splicing|
|Guide RNA|gRNA|RNA editing|
|_S_|_mall ncRNAs (<200 nt)_||
|MicroRNA|miRNA (_∼_19-24 nt)|RNA silencing|
|Small interfering RNA|siRNA (_∼_21-22 nt)|RNA silencing|
|Piwi interacting RNA|piRNA (_∼_26-31 nt)|Transposon silencing, epigenetic<br>regulation|
|Tiny transcription initiation RNA|tiRNA (_∼_17-18 nt)|Transcriptional regulation?|
|Promoter-associated short RNA|PASR (_∼_22-200 nt)|_unknown_|
|Transcription start site antisense RNA<br>Termini-associated short RNA|TSSa-RNA (_∼_20-90 nt)<br>TASR|Transcriptional maintainence?<br>_not clear_|
|Antisense termini associated short RNA|aTASR|_not clear_|
|Retrotransposon-derived RNA|RE-RNA|_not clear_|
|3’UTR-derived RNA|uaRNA|_not clear_|
|x-ncRNA|x-ncRNA|_not clear_|
|Small NF90-associated RNA|snaR|_not clear_|
|Unusually small RNA|usRNA|_not clear_|
|Vault RNA|vtRNA|_not clear_|
|Human Y RNA|hY RNA|_not clear_|
||_Long ncRNAs (≥200 nt)_||
|Large intergenic ncRNA|lincRNA|Epigenetics regulation|
|Transcribed ultraconserved regions|T-UCR|miRNA regulation?|
|Pseudogenes|_none_|miRNA regulation?|
|Promoter upstream transcripts|PROMPT|Transcriptional activation?|
|Telomeric repeat-containing RNA|TERRA|telomeric heterochromatin main-<br>tenance|
|GAA-repeat containing RNA|GRC-RNA|_not clear_|
|Enhancer RNA|eRNA|_not clear_|
|Long intronic ncRNA|_none_|_not clear_|
|Antisense RNA|aRNA|_not clear_|
|Promoter-associated long RNA|PALR|_not clear_|
|Stable excised intron RNA|_none_|_not clear_|
|Long stress-induced non-coding transcri|pts<br>LSINCT|_not clear_|


212

6.047/6.878 Lecture 12: Small RNA

### **13.1.2 Small ncRNA**

For the past decades, there have been a number of well-studied small non-coding RNA species. All of these species are either involved in RNA translation (transfer RNA (tRNA)) or RNA modification and processing (small nucleolar RNA (snoRNA) and small nuclear RNA (snRNA)). In particular, snoRNA (grouped into two broad classes: C/D Box and H/ACA Box, involved in methylation and pseudouridylation, respectively) are localized in the nucleous and participates in rRNA processing and modification. Another group of small ncRNAs are snRNAs that interact with other proteins and with each other to form splicesomes for RNA splicing. Remarkably, these snRNAs are modified (methylation and pseudouridylation) by another set of small ncRNAs - small Cajal body-specific RNAs (scaRNAs), which are similar to snoRNA (in sequence, structure, and function) and are localized in the Cajal body in the nucleus. Yet in another class of small ncRNAs, guide RNAs (gRNAs) have been shown predominately in trypanosomatids to be involved in RNA editing. Many other classes have also been recently proposed (see Table 13.1) although their functional roles remain to be determined. Perhaps the most widely studied ncRNA in the recent years are microRNAs (miRNAs), involved in gene silencing and responsible to the regulation of more than 60% protein-coding genes [6]. Given the extensive work that has been focused on RNAi and wide range of RNAi-based applications that have emerged in the past years, the next section (RNA Interference) will be entirely devoted to this topic.

### **13.1.3 Long ncRNA**

Long ncRNAs (lncRNAs) make up the largest portion of ncRNAs [6]. However the emphasis placed on the study of long ncRNA has only been realized in the recent years. As a result, the terminology for this family of ncRNAs are still in its infancy and oftentimes inconsistent in the literature. This is also in part complicated by cases where some lncRNAs can also serve as transcripts for the generation of short RNAs. In light of these confusions, as discussed in the previous chapter, lncRNA have been arbitrarily defined as ncRNAs with size greater than 200 nts (based on the cut-off in RNA purification protocols) and can be broadly categorized into: sense, antisense, bidirectional, intronic, or intergenic [19]. For example, one particular class of lncRNA called long intergenic ncRNA (lincRNA) are found exclusively in the intergenic region and possesses chromatin modifications indicative of active transcription (e.g. H3K4me3 at the transcriptional start site and H3K36me3 throughout the gene region) [8].

Despite the recent rise of interest in lncRNAs, the discovery of the first lncRNAs ( _XIST_ and _H19_ ), based on searching cDNA libraries, dated back to the 1980s and 1990s before the discovery of miRNAs [3, 4]. Later studies demonstrated the association of lncRNAs with polycomb group proteins, suggesting potential roles of lncRNAs in epigenetic gene silencing/activation [19]. Another lncRNA, _HOX Antisense Intergenic RNA (HOTAIR)_ , was recently found to be highly upregulated in metastatic breast tumors [11]. The association of _HOTAIR_ with the polycomb complex again supports a potential unified role of lncRNAs in chromatin remodeling/epigenetic regulation (in either a _cis_ -regulatory ( _XIST_ and _H19_ ), or _trans_ -regulatory (e.g. _HOTAIR_ ) fashion) and disease etiology.

Recent studies have also identified _HULC_ and pseudogene (transcript resembling real genes but contains mutations that prevent their translation into functional proteins) _PTENP1_ that may function as a decoy in binding to miRNAs to reduce the overall effectiveness of miRNAs [18, 25]. Other potential roles of lncRNAs remains to be explored. Nevertheless, it is becoming clear that lncRNAs are less likely to be the result of transcriptional noise, but may rather serve critical role in the control of cellular processes.

213

6.047/6.878 Lecture 12: Small RNA

## **13.2 RNA Interference**

RNA interference has been one of the most significant and exciting discoveries in recent history. The impact of this discovery is enormous with applications ranging from knockdown and loss-of-function studies to the generation of better animal models with conditional knockdown of desired gene(s) to large-scale RNAi-based screens to aid drug discovery.

### **13.2.1 History of discovery**

The discovery of the gene silencing phenomenon dated back as early as the 1990s with Napoli and Jorgensen demonstrating the down-regulation of chalcone synthase following introduction of exogenous transgene in plants [17]. Similar suppression was subsequently observed in other systems [10, 22]. In another set unrelated work at the time, Lee et al. identified in a genetic screen that endogenous _lin-4_ expressed a non-proteincoding product that is complementary to the lin-14 gene and controlled the timing of larval development (from first to second larval state) in _C. elegans_ [15]. We now know this as the first miRNA to be discovered. In 2000, another miRNA, _let-7_ , was discovered in the same organism and was found to be involved in promoting the late-larval to adult transition [21]. The seminal work by Mello and Fire in 1998 (for which was awarded the Nobel Prize in 2006) demonstrated that the introduction of exogenous dsRNA in _C. elegans_ specifically silenced genes via RNA interference, explaining the prior suppression phenomenon observed in plants [7]. Subsequent studies found the conversion of dsRNA into siRNA in the RNAi pathway. In 2001, the term miRNA and the link between miRNA and RNAi was described in three papers in _Science_ [23]. With this, we have come to realize the gene regulatory machinery was composed of predominately of two classes small RNAs, with miRNA involved in the regulation of endogenous genes and siRNA involved in defense in response to viral nucleic acids, transposons, and transgenes [5]. Later works revealed downstream effectors: Dicers (for excision of precursor species) and Argonaute proteins (part of the RNA-induced silencing complex to perform the actual silencing effects), completing our current understanding of the RNA silencing pathways. The details of the mechanism and the differences among the species are further discussed below.

### **13.2.2 Biogenesis pathways**

There is a common theme involved for both siRNA-mediated and miRNA-mediated silencing. In the biogenesis of both siRNA and miRNA, the double-stranded precursors are cleaved by a RNase into short _∼_ 22 nt fragments. One of the strands (the guide strand) is loaded into an Argonaute protein, a central component of the larger ribonucleoprotien complex RISC that facilitates target RNA recognition and silencing. The mechanism of silencing are either cleaveage of the target mRNA or translation repression.

Aside from this common theme, the proteins involved in these processes differ among species and there exists additional steps in miRNA processing prior to its maturation and incorporation into RISC (Figure 13.1). For the biogenesis of siRNA, the precursors are dsRNAs, oftentimes from exogenous sources such as viruses or transposons. However, recent studies have also found endogenous siRNAs [9]. Regardless of the source, these dsRNAs are processed by the RNase III endonuclease, Dicer, into _∼_ 22 nt siRNAs. This RNase III-catalyzed cleavage leaves the characteristic 5’phosphates and 2 nt 3’ overhangs [2]. It is worth noting that different species have evolved with different number of paralogs. This becomes important as, to be discussed later, the miRNA biogenesis pathway also utilizes Dicer for the processing of miRNA precursors (more specifically pre-miRNAs). For species such as _D. melanogaster_ , there are two distinct Dicer proteins and as a result there is typically a preferential processing of the precursors (e.g. Dicer-1 for miRNA cleavage and Dicer-2 for siRNA cleavage) [5]. In contrast, mammals and nematodes only have a single Dicer protein and as such both biogenesis pathways converge to the same processing step [5]. In subsequent steps of the

214

6.047/6.878 Lecture 12: Small RNA

siRNA biogenesis pathway, one of the strands in the siRNA duplex is loaded into RISC to silence target RNAs (Figure 13.1C).


Courtesy of Elsevier, Inc., http://www.sciencedirect.com. Used with permission. Source: Bartel, David P. "MicroRNAs: Genomics, Biogenesis, Mechanism, and Function." _Cell_ 116, no. 2 (2004): 281-97.

Figure 13.1: siRNA and miRNA biogenesis pathways. (A) Biogenesis of plant miRNA (B) Biogenesis of animal miRNA (C) Biogenesis of animal siRNA. Adopted from Bartel, 2004 (ref [2]). Copyright © 2004 Cell Press.

In the miRNA biogenesis pathway, majority of the precursors are pol II transcripts of the intron regions, some of which encode multiple miRNAs in clusters. These precursors, in the form of a stem-loop structure, are named pri-miRNAs. The pri-miRNAs are first cleaved in the nucleus by a RNase III endonuclease (Drosha in animals and Dcl1 in plants) into _∼_ 60-70 nt stem loop intermediates, termed pre-miRNAs [2]. In animals, the pre-miRNA is then exported into the cytoplasm by Exportin-5. This is followed by the cleavage of pre-miRNA intermediate by Dicer to remove the stem loop. One of the strands in the resulting mature miRNA duplex is loaded to RISC, similar to that described for siRNA biogenesis Figure 13.1B. Interestingly, in plants, the pri-miRNA is processed into mature miRNA through two cleavages by the same enzyme, Dcl1, in the nucleus before export into the cytoplasm for loading (Figure 13.1A).

### **13.2.3 Functions and silencing mechanism**

The classical view of miRNA function based on the early discoveries of miRNA has been analogous to a binary switch whereby miRNA represses translation of a few key mRNA targets to initiate a developmental

215

6.047/6.878 Lecture 12: Small RNA

transition. However, subsequent studies have greatly broaden this definition. In plants, most miRNAs bind to the coding region of the mRNA with near-perfect complementarity. On the other hand, animal miRNAs bind with partial complementarity (except for a seed region, residues 2-8) to the 3’ UTR regions of mRNA. As such, there are potentially hundreds targets by a single miRNA in animals rather than just a few [1]. In addition, in mammals, only a few portion of the predicted targets are involved in development, with the rest predicted to cover a wide range of molecular and biological processes [2]. Lastly, miRNA silencing acts through both translation repression and mRNA cleavage (and also destabilization as discussed below)(as shown for example showed by Bartel and coworkers on the miR-196-directed cleavage of _HOXB6_ [26]). Taken together, the modern view of miRNA function has been that miRNA dampens expression of many mRNA targets to optimize expression, reinforce cell identity, and sharpen transitions.

The mechanism for which miRNA mediates the silencing of target mRNA is still an area of active research. As previously discussed, RNA silencing can take the form of either cleavage, destabilization (leading to subsequent degradation of the mRNA), or translation repression. In plants, it has been found that the predominate mode of RNA silencing is through Argonaute-catalyzed cleavage. However, the contribution of these different modes of silencing has been less clear in animals. Recent global analyses from the Bartel group in collaboration with Gygi and Ingolia and Weissman shed light on this question. In a 2008 study, Bartel and Gygi groups examined the global changes in protein level using mass spectrometry following miRNA introduction or deletion [1]. Their results revealed the repression of hundreds of genes by individual miRNAs, and more importantly mRNA destabilization accounts for majority of the highly repressed targets (Figure 13.2).


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Baek, Daehyun, et al. "The Impact of MicroRNAs on Protein Output." _Nature_ 455, no. 7209 (2008): 64-71.

Figure 13.2: Protein and mRNA changes following miR-223 loss, from messages with at least one 8-mer 3’UTR site (blue) or at least one 7-mer (orange). Adopted from Baek et al., 2008 (ref [1]). Copyright © 2008 Macmillan Publishers Limited.

This is further supported by a subsequent study using both RNA-seq and a novel ribosome-profiling first demonstrated by Inoglia and Weissman 2009 that enables the interrogation of global translation activities

216

6.047/6.878 Lecture 12: Small RNA

with sub-codon resolution [14]. The results showed destabilization of target mRNA is the predominate mechanism through which miRNA reduces the protein output.

## **Bibliography**

- [1] Daehyun Baek, Judit Vill´en, Chanseok Shin, Fernando D Camargo, Steven P Gygi, and David P Bartel. The impact of microRNAs on protein output. _Nature_ , 455(7209):64–71, September 2008.

- [2] David P Bartel. MicroRNAs: genomics, biogenesis, mechanism, and function. _Cell_ , 116(2):281–97, January 2004.

- [3] M S Bartolomei, S Zemel, and S M Tilghman. Parental imprinting of the mouse H19 gene. _Nature_ , 351(6322):153–5, May 1991.

- [4] C J Brown, A Ballabio, J L Rupert, R G Lafreniere, M Grompe, R Tonlorenzi, and H F Willard. A gene from the region of the human X inactivation centre is expressed exclusively from the inactive X chromosome. _Nature_ , 349(6304):38–44, January 1991.

- [5] Richard W Carthew and Erik J Sontheimer. Origins and Mechanisms of miRNAs and siRNAs. _Cell_ , 136(4):642–55, February 2009.

- [6] Manel Esteller. Non-coding RNAs in human disease. _Nature Reviews Genetics_ , 12(12):861–874, November 2011.

- [7] A Fire, S Xu, M K Montgomery, S A Kostas, S E Driver, and C C Mello. Potent and specific genetic interference by double-stranded RNA in Caenorhabditis elegans. _Nature_ , 391(6669):806–11, February 1998.

- [8] Ewan a Gibb, Carolyn J Brown, and Wan L Lam. The functional role of long non-coding RNA in human carcinomas. _Molecular cancer_ , 10(1):38, January 2011.

- [9] Daniel E Golden, Vincent R Gerbasi, and Erik J Sontheimer. An inside job for siRNAs. _Molecular cell_ , 31(3):309–12, August 2008.

- [10] S Guo and K J Kemphues. par-1, a gene required for establishing polarity in C. elegans embryos, encodes a putative Ser/Thr kinase that is asymmetrically distributed. _Cell_ , 81(4):611–20, May 1995.

- [11] Rajnish A Gupta, Nilay Shah, Kevin C Wang, Jeewon Kim, Hugo M Horlings, David J Wong, MiaoChih Tsai, Tiffany Hung, Pedram Argani, John L Rinn, Yulei Wang, Pius Brzoska, Benjamin Kong, Rui Li, Robert B West, Marc J van de Vijver, Saraswati Sukumar, and Howard Y Chang. Long non-coding RNA HOTAIR reprograms chromatin state to promote cancer metastasis. _Nature_ , 464(7291):1071–6, April 2010.

- [12] Masahira Hattori. Finishing the euchromatic sequence of the human genome. _Nature_ , 431(7011):931–45, October 2004.

- [13] Christopher L Holley and Veli K Topkara. An introduction to small non-coding RNAs: miRNA and snoRNA. _Cardiovascular Drugs and Therapy_ , 25(2):151–159, 2011.

- [14] Nicholas T Ingolia, Sina Ghaemmaghami, John R S Newman, and Jonathan S Weissman. Genome-wide analysis in vivo of translation with nucleotide resolution using ribosome profiling. _Science (New York, N.Y.)_ , 324(5924):218–23, April 2009.

- [15] R C Lee, R L Feinbaum, and V Ambros. The C. elegans heterochronic gene lin-4 encodes small RNAs with antisense complementarity to lin-14. _Cell_ , 75(5):843–54, December 1993.

- [16] Michael L Metzker. Sequencing technologies - the next generation. _Nature Reviews Genetics_ , 11(1):31– 46, January 2010.

217

6.047/6.878 Lecture 12: Small RNA

- [17] C. Napoli, C. Lemieux, and R. Jorgensen. Introduction of a Chimeric Chalcone Synthase Gene into Petunia Results in Reversible Co-Suppression of Homologous Genes in trans. _The Plant cell_ , 2(4):279– 289, April 1990.

- [18] Laura Poliseno, Leonardo Salmena, Jiangwen Zhang, Brett Carver, William J Haveman, and Pier Paolo Pandolfi. A coding-independent function of gene and pseudogene mRNAs regulates tumour biology. _Nature_ , 465(7301):1033–8, June 2010.

- [19] Chris P Ponting, Peter L Oliver, and Wolf Reik. Evolution and functions of long noncoding RNAs. _Cell_ , 136(4):629–41, February 2009.

- [20] J. R. Prensner and A. M. Chinnaiyan. The Emergence of lncRNAs in Cancer Biology. _Cancer Discovery_ , 1(5):391–407, October 2011.

- [21] B J Reinhart, F J Slack, M Basson, A E Pasquinelli, J C Bettinger, A E Rougvie, H R Horvitz, and G Ruvkun. The 21-nucleotide let-7 RNA regulates developmental timing in Caenorhabditis elegans. _Nature_ , 403(6772):901–6, February 2000.

- [22] N Romano and G Macino. Quelling: transient inactivation of gene expression in Neurospora crassa by transformation with homologous sequences. _Molecular microbiology_ , 6(22):3343–53, November 1992.

- [23] G Ruvkun. Molecular biology. Glimpses of a tiny RNA world. _Science_ , 294(5543):797–9, October 2001.

- [24] Ryan J Taft, Ken C Pang, Timothy R Mercer, Marcel Dinger, and John S Mattick. Non-coding RNAs: regulators of disease. _The Journal of pathology_ , 220(2):126–39, January 2010.

- [25] Jiayi Wang, Xiangfan Liu, Huacheng Wu, Peihua Ni, Zhidong Gu, Yongxia Qiao, Ning Chen, Fenyong Sun, and Qishi Fan. CREB up-regulates long non-coding RNA, HULC expression through interaction with microRNA-372 in liver cancer. _Nucleic acids research_ , 38(16):5366–83, September 2010.

- [26] Soraya Yekta, I-Hung Shih, and David P Bartel. MicroRNA-directed cleavage of HOXB8 mRNA. _Science_ , 304(5670):594–6, April 2004.

218

---

[← Part II](04-part-ii.md) · [Up: contents](index.md) · [Part III →](06-part-iii.md)

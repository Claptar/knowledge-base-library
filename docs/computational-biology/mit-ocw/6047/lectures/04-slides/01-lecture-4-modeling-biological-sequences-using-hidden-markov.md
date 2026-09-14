---
title: Lecture 4 Modeling Biological Sequences using Hidden Markov Models
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/04-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 4 Modeling Biological Sequences using Hidden Markov Models

**Source:** `lectures/04-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1

## **Module 1: Aligning and modeling genomes**

- Module 1: Computational foundations

   - Dynamic programming: exploring exponential spaces in poly-time

   - Linear-time string matching, Hashing, Content-based indexing

   - Hidden Markov Models: decoding, evaluation, parsing, learning

- Last week: Sequence alignment / comparative genomics – Local/global alignment: infer nucleotide-level evolutionary events

   - Database search: scan for regions that may have common ancestry

- This week: Modeling genomes / exon / CpG island finding – Modeling class of elements, recognizing members of a class

   - Application to gene finding, conservation islands, CpG islands

2

#### **We have learned how to align sequences to other sequences**

- L2: Sequence alignment

   - Dynamic programming, duality path  alignment

   - Global / local alignment, general gap penalties

- L3: Rapid string search

   - Exact string match, semi-numerical matching

   - Database search: Hashing, BLAST, variations

- L15:Comparative genomics: evolutionary signatures

   - Tell me how you evolve, I’ll tell you what you are

   - Identifying conserved elements through evolution

- L16: Whole-genome assembly/alignment/duplication: – Finding all common substrings within/across species

   - Contigs/scaffolds, string graphs, glocal alignmt paths

- Problem set 1, project planning, Problem set 2 out

3

**Today: apply these ideas to model DNA sequences …GTACTCACCGGGTTACAGGATTATGGGTTACAGGTAACCGTT…**

- What to do with a completely new piece of DNA – Align it to things we know about (database search)

   - Align it to things we don’t know about (assembly)

- Stare at it

   - Non-standard nucleotide composition?

   - Interesting k-mer frequencies?

   - Recurrent patterns?

- Model it

   - Make some hypotheses about it

   - Build a ‘generative model’ to describe it

   - Find sequences of similar **_type_**

-  How do we model DNA sequences?

4

**Modeling biological sequences with HMMs (a.k.a. What to do with big unlabelled chunks of DNA)**

**Intergenic CpG Promoter First Intron Other Intron island exon exon**


**TTACAGGATTATGGGTTACAGGTAACCGTTGTACTCACCGGGTTACAGGATTATGGGTTACAGGTAACCGGTACTCACCGGGTTACAGGATTATGGTAACGGTACTCACCGGGTTACAGGATTGTTACA GG**

- Ability to **emit** DNA sequences of a certain **_type_**

   - Not exact alignment to previously known gene

   - Preserving ‘properties’ of **type** , not identical sequence

- Ability to **recognize** DNA sequences of a certain type (state) – What (hidden) state is most likely to have generated observations – Find set of states and transitions that generated a long sequence

- Ability to **learn** distinguishing characteristics of each state – Training our generative models on large datasets

   - Learn to classify unlabelled data

5

## **Why Probabilistic Sequence Modeling?**

- Biological data is noisy

- Probability provides a calculus for manipulating models

- Not limited to yes/no answers – can provide “degrees of belief”

- Many common computational tools based on probabilistic models

- Our tools:

   - Markov Chains and Hidden Markov Models (HMMs)

6

## **Markov Chains and Hidden Markov Models**

7

## **Andrey Markov (1856-1922)**


Image in the public domain.

8

## **Predicting tomorrow’s weather**


<!-- Start of picture text -->
• Markov Chain<br>Rain<br>Sun<br>Clouds<br>Transitions<br>Snow<br>All observed<br><!-- End of picture text -->


<!-- Start of picture text -->
• Hidden Markov Model<br>Transitions<br>Summer  Fall  Winter Spring<br>hidden<br>observed<br>Emissions<br><!-- End of picture text -->


- What you see is what you get: next state only depends on current state (no memory)

- Hidden state of the world (e.g. storm system) determines emission probabilities

- State transitions governed by a Markov chain

9

## **HMM nomenclature for this course**


<!-- Start of picture text -->
π=  Summer  Fall<br>Winter Spring  Transitions:  akl =P( πi=l | πi-1 = k )<br>Transition probability<br>πi<br>from state  k  to state  l<br>Emissions:  ekk ( xii )=P( xi|pi=ki|pi=k|pi=ki=k=k )<br>xi<br><!-- End of picture text -->

**Emissions:** **_ekk_ (** **_xii_ )=P(** **_xi|pi=ki|pi=k|pi=ki=k=k_ ) Emission probability of symbol** **_xi_ from state** **_k_**


**_x=_**

- Vector **_x_** = Sequence of observations

- Vector **_π_** = Hidden path (sequence of hidden states)

- Transition matrix A= akl =probability of **_k_**  **_l_** state transition

- Emission vector **_E=ek(xi)_** = prob. of observing xi from state k

- Bayes’s rule: Use **_P(xi|πi=k)_** to estimate **_P(πi=k|xi)_**

10

## **Components of a Markov Chain**

**Definition:** A **_Markov chain_** is a triplet **(** **_Q,_** p **_, A_** ), where:

- **_Q_** is a finite set of states. Each state corresponds to a symbol in the

- alphabet Σ

- **_p_** is the initial state probabilities.

- **_A_** is the state transition probabilities, denoted by **_ast_** for each **_s, t_** in **_Q_ .**

 For each **_s, t_** in **_Q_** the transition probability is: **_ast_** ≡ **_P_ (** **_xi_ =** **_t_** | **_xi-1_ =** **_s_ ) Output:** The output of the model is the set of states at each instant time => the set of states are observable

**Property:** The probability of each symbol **_xi_** depends only on the value of the preceding symbol **_xi-1_** : **_P (xi | xi-1,…, x1) = P (xi | xi-1)_ Formula:** The probability of the sequence:

**_P(x) = P(xL,xL-1,…, x1) = P (xL | xL-1) P (xL-1 | xL-2)… P (x2 | x1) P(x1)_**

Slide credit: Serafim Batzoglou

11

## **Components of an HMM (Hidden Markov Model)**

**Definition:** An **_HMM_** is a 5-tuple **(** **_Q, V, p, A, E_** ), where:

- **_Q_** is a finite set of states, **|Q|=N**

- **V** is a finite set of observation symbols per state, **|V|=M**

- **_p_** is the initial state probabilities.

- **_A_** is the state transition probabilities, denoted by **_ast_** for each **_s, t_** in **_Q_ .**

   -  For each **_s, t_** in **_Q_** the transition probability is: **_ast_** ≡ **_P_ (** **_xi_ =** **_t_** | **_xi-1_ =** **_s_ )**

- **E** is a probability emission matrix, **_esk_** ≡ **_P_ (** **_vk_ at time** **_t_** | **_qt_ =** **_s_ )**

**Output:** Only emitted symbols are observable by the system but not the underlying random walk between states   -> “hidden”

**Property:** Emissions and transitions are dependent on the current state only and not on the past.

Slide credit: Serafim Batzoglou

12

---

[Up: contents](index.md) · [The six algorithmic settings for HMMs One path All paths →](02-the-six-algorithmic-settings-for-hmms-one-path-all-paths.md)

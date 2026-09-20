---
title: "13. HMM Posterior Decoding and Learning"
course: "MIT 6047"
chapter: 13
source: "https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 13. HMM Posterior Decoding and Learning

## What this covers

This chapter asks a question the previous lecture's tools could not answer: once we accept that a
hidden state sequence has many plausible paths through an HMM, not just one, how do we get at what
is actually well-supported at *each individual position*, and how do we get the HMM's transition
and emission probabilities in the first place, rather than assuming they are handed to us? The
first question is answered by **posterior decoding**, which needs a new algorithm — the **backward
algorithm** — to complement the forward algorithm already available. The second is answered here
for the case where training data comes with the hidden states already labelled: **supervised
learning** by counting. Along the way, the chapter works through a genomic case study — the
CpG-island model — that shows how to build "memory" into an HMM at all. It assumes the reader
already has the HMM formalism, the Viterbi algorithm and the forward algorithm from the preceding
lecture; those are recapped only far enough to make the new material self-contained.

## Recap: HMMs, Viterbi, and the forward algorithm

A Markov chain is a discrete random process with the Markov property: the next state depends only
on the current one. It is specified by a set of states $Q$, a transition matrix $a_{jk} = P(\pi_i =
k \mid \pi_{i-1} = j)$, and initial probabilities $a_{0j}$. In an ordinary Markov chain the state
and the observation are the same thing — "what you see is what you get." A **Hidden Markov Model**
breaks that identification: at each step $i$ the chain is in a hidden state $\pi_i$, but what is
observed is a character $x_i$ drawn from an **emission distribution** $e_k(v_l) = P(x_i = v_l \mid
\pi_i = k)$ tied to that state. The canonical toy example is inferring the season (hidden) from the
weather (observed) — the weather is not one-to-one with the season, but it constrains it.

An HMM is fully specified by $(a_{jk}, e_k(v_l), a_{0j})$. Given a hidden path $\pi$ and an emitted
sequence $x$, the joint probability of both is

$$P(x_1, \dots, x_N, \pi_1, \dots, \pi_N) = a_{0\pi_1} \prod_i e_{\pi_i}(x_i)\, a_{\pi_i\pi_{i+1}}.$$

Genomic HMMs of this kind range from very small (two states, distinguishing GC-rich from AT-rich
DNA, or conserved from non-conserved sequence, on the strength of nucleotide or substitution
frequencies alone) to fairly large (around twenty states to describe the internal structure of a
gene — first, middle and last coding exons, three intron phases to keep the reading frame, UTRs,
intergenic sequence — or around forty states to describe combinations of chromatin marks). The
extra states in the larger models exist because the *position* of a feature carries information
that a single state cannot: an intron's phase has to be remembered so that the next exon starts in
the right reading frame, and a first exon has structural features (it starts with a start codon) a
middle exon does not.

Two questions were answered for this model already:

- **Viterbi decoding** finds the single hidden path $\pi^*$ that maximizes the joint probability
  $P(x,\pi)$. It uses the recursion $V_k(i) = e_k(x_i) \times \max_j\big(V_j(i-1)\, a_{jk}\big)$,
  where $V_k(i)$ is the probability of the best path ending in state $k$ at position $i$, in
  $O(K^2N)$ time and $O(KN)$ space ($K$ states, sequence length $N$).
- The **forward algorithm** answers a different question: not which single path is best, but what
  is the total probability of the observed sequence, summed over *every* possible hidden path.
  Define $f_k(t) = P(\pi_t = k, x_1, \dots, x_t)$. Splitting on the state at $t-1$ and using the
  Markov property gives the recursion

  $$f_k(t) = e_k(x_t) \sum_l f_l(t-1)\, a_{lk},$$

  with $f_0(0)=1$ and $f_k(0)=0$ for $k>0$, filled into a $K \times N$ table left to right. The
  total probability of the sequence is then $P(x) = \sum_k f_k(N)$: sum the last column. Viterbi
  and the forward algorithm share almost the same recursion; the only difference is $\max$ versus
  $\sum$. Both run in $O(K^2N)$ time and $O(KN)$ space. In practice the forward probabilities
  underflow quickly for long sequences, so implementations work in log-space.

## Posterior decoding

### The question Viterbi doesn't answer

Viterbi gives one path. But that single most-likely path can represent a vanishingly small
fraction of the total probability mass once a sequence is long — there may be thousands of paths
each individually about as likely, none of them dominant. If what we actually want is a confident
answer to "what state was the process most likely in at position $t$?", summed honestly over every
path consistent with the data, Viterbi is answering a different question.

**Posterior decoding** asks exactly that: for each position $t$, which state $k$ maximizes
$P(\pi_t = k \mid x_1, \dots, x_N)$, the observations to either side of $t$ included? The intuition
is the dishonest-casino example from the previous lecture. Before any rolls are observed, the prior
already favours the loaded die if it is used more often. After one roll,

$$P(\text{die}=\text{loaded} \mid \text{roll}=k) = \frac{P(\text{die}=\text{loaded})\,P(\text{roll}=k\mid\text{die}=\text{loaded})}{P(\text{roll}=k)}.$$

Posterior decoding is the natural extension of this Bayesian update to a sequence of arbitrary
length: information about the state at time $t$ flows in from *both* directions. If two sixes in a
row are rolled, belief that the die was loaded at the first roll is reinforced not only by that
roll but by the roll that came after it — belief flows backward through the sequence as well as
forward.

Formally, by Bayes' rule,

$$\pi_t^* = \operatorname*{argmax}_k P(\pi_t=k \mid x_1,\dots,x_N) = \operatorname*{argmax}_k \frac{P(\pi_t=k, x_1,\dots,x_N)}{P(x)}.$$

$P(x)$ does not depend on $k$, so it can be dropped from the maximization, and splitting the
observations at $t$ and invoking the Markov property gives

$$\pi_t^* = \operatorname*{argmax}_k \; P(\pi_t=k, x_1,\dots,x_t)\; P(x_{t+1},\dots,x_N \mid \pi_t=k) = \operatorname*{argmax}_k f_k(t)\, b_k(t).$$

The first factor is exactly the forward variable $f_k(t)$ from the previous lecture. The second,
$b_k(t) = P(x_{t+1}, \dots, x_N \mid \pi_t = k)$, is new: the probability of everything *after* $t$,
given the state at $t$. Computing it is the job of the backward algorithm.

### The backward algorithm

Expand $b_k(t)$ by splitting on the state at $t+1$:

$$b_k(t) = \sum_l P(x_{t+1},\dots,x_N,\pi_{t+1}=l \mid \pi_t=k).$$

Using the Markov property to factor this joint probability,

$$b_k(t) = \sum_l \underbrace{P(x_{t+2},\dots,x_N \mid \pi_{t+1}=l)}_{b_l(t+1)} \; P(\pi_{t+1}=l\mid \pi_t=k) \; P(x_{t+1}\mid \pi_{t+1}=l),$$

which, written out in transition and emission notation, is the recursion

$$b_k(t) = \sum_l b_l(t+1)\, a_{kl}\, e_l(x_{t+1}).$$

Compared with the forward recursion, two things flip. First, the backward algorithm fills its
$K\times N$ table from *right to left*: it initializes the last column to $b_k(N) = a_{k0}$ (the
probability of ending the chain from state $k$) and works backward, hence the name. Second, the
emission term moves inside the sum: the forward recursion emits $x_t$ from the *current* state $k$,
so $e_k(x_t)$ factors outside the sum over predecessors; the backward recursion needs the emission
at $t+1$, which depends on the *successor* state $l$ being summed over, so $e_l(x_{t+1})$ has to sit
inside the sum. The algorithm still runs in $O(K^2N)$ time and $O(KN)$ space, and it gives $P(x)$
just as the forward algorithm did, now from the leftmost column:

$$P(x) = \sum_l a_{0l}\, e_l(x_1)\, b_l(1).$$

One point of possible confusion: even though the backward algorithm walks the sequence from the
end back to the start, the transition probability it uses at each step is still the *forward*
transition probability. Moving backward from state $B$ (at $t+1$) to state $A$ (at $t$) uses
$a_{AB}$, not some separately-defined "reverse" transition, because $B$ following $A$ is what
happens going forward, and $a_{AB}$ is what its probability is called.

### Why both directions are needed

Every algorithm before this one — Viterbi, the forward algorithm — needed information flowing in
only one direction, because each was answering a question about a *whole path*, computed by working
through the sequence once and reading off the answer at the end. Posterior decoding is different:
it asks for the best state at *every individual position*, and answering that for position $t$
requires everything the data says about $t$ — both what came before it and what came after. A
dynamic program that has to look both ways from an interior point has to be built from two passes
that meet there.

<figure>
<svg viewBox="0 0 400 200" role="img" aria-label="The forward pass and backward pass meeting at a single position t">
<defs>
<marker id="arrowhead" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<polygon points="0,0 10,5 0,10" fill="currentColor"/>
</marker>
</defs>
<line x1="30" y1="160" x2="370" y2="160" stroke="currentColor" stroke-width="1.5"/>
<line x1="30" y1="152" x2="30" y2="168" stroke="currentColor" stroke-width="1.5"/>
<line x1="200" y1="152" x2="200" y2="168" stroke="currentColor" stroke-width="1.5"/>
<line x1="370" y1="152" x2="370" y2="168" stroke="currentColor" stroke-width="1.5"/>
<text x="30" y="185" text-anchor="middle" font-size="12" fill="currentColor">1</text>
<text x="200" y="185" text-anchor="middle" font-size="12" fill="currentColor">t</text>
<text x="370" y="185" text-anchor="middle" font-size="12" fill="currentColor">N</text>
<line x1="36" y1="75" x2="194" y2="75" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowhead)"/>
<text x="115" y="60" text-anchor="middle" font-size="12" fill="currentColor">forward pass: f_k(t)</text>
<line x1="364" y1="115" x2="206" y2="115" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowhead)"/>
<text x="285" y="135" text-anchor="middle" font-size="12" fill="currentColor">backward pass: b_k(t)</text>
<text x="200" y="30" text-anchor="middle" font-size="12" fill="currentColor">P(pi_t = k | x) proportional to f_k(t) . b_k(t)</text>
</svg>
<figcaption>The forward pass carries everything the data up to position t implies about the state
there; the backward pass carries everything the data after t implies. Posterior decoding multiplies
the two, so the estimate at t uses the whole sequence, not just half of it.</figcaption>
</figure>

Both $f_k(t)$ and $b_k(t)$ can be computed for every $t = 1,\dots,N$ in $\Theta(K^2N)$ time and
$\Theta(KN)$ space, so posterior decoding is no more expensive, asymptotically, than either
algorithm alone:

$$\pi_t^* = \operatorname*{argmax}_k P(\pi_t=k\mid x) = \operatorname*{argmax}_k \frac{f_k(t)\, b_k(t)}{P(x)}.$$

### Viterbi versus posterior decoding

Which decoding to use depends on what the answer is for. Posterior decoding is more informative
about any single position, because it weighs *every* path consistent with the data rather than
picking out one; Viterbi's single path can represent only a small sliver of the total probability
once the sequence is long. But posterior decoding can produce a state sequence that is not even a
legal path through the model: because the state at each position is chosen independently of its
neighbours, two adjacent positions can be assigned states between which the transition probability
is zero. Viterbi, by construction, never has this problem — it always returns one coherent path.

When the two disagree, that is itself informative: it is a sign that no single dominant path
explains the data well, and that something more complicated is going on. In genomics this can be a
symptom of real biological complexity — alternative splicing is one example given in the source —
rather than a flaw in either algorithm. Which decoding is "correct" depends on which question is
actually being asked: the best coherent explanation (Viterbi), or the most defensible call at a
given position (posterior).

## Encoding memory in an HMM: CpG islands

CpG islands are regions of a genome enriched for the dinucleotide CG (written CpG, for the
phosphate backbone linking C to G on the *same* strand, as opposed to a G-C base pair across the
double helix). Cytosine in a CpG context is frequently methylated, and methylated cytosine
deaminates to thymine at an elevated rate; the resulting C-to-T mutation looks like an ordinary
substitution rather than DNA damage, so CpG dinucleotides are depleted across the genome over
evolutionary time. Where methylation is suppressed — active promoters — and where purifying
selection acts on the CpG itself, this depletion does not happen, and CpG dinucleotides persist as
a relative excess: an island. Detecting these islands is therefore a way of finding promoters,
other transcriptionally active regions, and sites under selective constraint.

A naive HMM with two states, "+" (island) and "-" (non-island), each emitting A/C/G/T with its own
frequencies, cannot capture this. Such a model can make the "+" state emit more C's and G's, but it
has no way to represent that those C's and G's occur predominantly as *adjacent pairs* — a fact
about the joint behaviour of neighbouring positions, not about single-nucleotide frequencies.

Because of the Markov property, everything an HMM "remembers" about the past has to be encoded in
the identity of the current state — there is nowhere else to put it. So to give the model memory of
the preceding nucleotide, the state space itself has to grow: replace the two states "+" and "-"
with eight, A+, C+, G+, T+, A-, C-, G-, T-. Doubling the number of states this way squares the
number of transitions, which is roughly how the cost of adding memory to an HMM scales.

There are two ways to interpret a state such as A+, and they push the information into different
parts of the model:

- **A+ means "in an island, and the *previous* character was A."** Then the transition
  probabilities out of A+ are largely uninformative (degenerate), and the interesting structure —
  which letter tends to follow which — lives in the emission probabilities.
- **A+ means "in an island, and the *current* character is A."** Then the emission distribution is
  degenerate (A+ emits A with probability 1 and everything else with probability 0), and the
  dinucleotide structure lives entirely in the transition matrix: the probability of moving from
  C+ to G+ is set much higher than from C- to G-, directly encoding that CG pairs are enriched
  inside islands and not outside them.

The lecture adopts the second convention. Each state still emits only its own letter, so knowing
that the current emitted character is, say, A does not by itself say whether the underlying state
is A+ or A-; the model is still genuinely hidden, not a disguised ordinary Markov chain, because the
island/non-island label is not recoverable from a single emitted letter.

Having built this eight-state model, posterior decoding assigns each base in a genome a probability
of lying in an island. Whether the extra states are actually earning their keep can be checked the
same way any two HMMs are compared: compute $P(x)$ for the data under each model with the forward
(or backward) algorithm, and prefer the model that assigns the data higher likelihood.

More states are not free, though: an HMM with more parameters is more prone to overfitting the
training data at the expense of generalizing to new data. One way to keep the CpG model expressive
without letting the parameter count run away is **regularization** — deliberately reducing the
number of free parameters. Here, since what matters for detecting islands is really just the rate
of switching between "+" and "-", the sixteen +$\to$- and -$\to$+ transition probabilities (four
letters each way) can be tied together into a single "+$\to$-" rate and a single "-$\to$+" rate,
throwing away the (probably unimportant) detail of which specific letter the switch happened on.

Other ways of building memory into the model are possible — for instance, emitting whole
dinucleotides directly and dealing with the resulting overlap between consecutive emissions, or
adding a dedicated state just for a C-to-G transition — the eight-state construction above is one
choice among several, not the only way to do it.

## Learning HMM parameters from labelled data

Everything so far assumed the HMM's parameters — the $a_{jk}$ and $e_k(v_l)$ — were already known.
In practice they usually are not, and have to be estimated from data. If the training data comes
with the true hidden state sequence attached (for instance, a genome where CpG islands have already
been experimentally annotated), estimating parameters is **supervised learning**; if the hidden
states are not given and have to be inferred at the same time as the parameters, it is
**unsupervised learning**.

For supervised learning, the maximum-likelihood parameters turn out to be exactly the empirical
frequencies observed in the labelled training data — the obvious estimator is also the correct one.
Concretely, let $A_{kl}$ be the number of times the training data transitions from state $k$ to
state $l$, and $E_k(b)$ the number of times character $b$ is emitted from state $k$. Then

$$a_{kl} = \frac{A_{kl}}{\sum_i A_{ki}}, \qquad e_k(b) = \frac{E_k(b)}{\sum_c E_k(c)}.$$

That is, just count transitions and emissions and normalize. In a worked example with a labelled
training sequence over states including $B$ and $P$: if state $B$ is followed by itself three times
and by $P$ once, the transition estimate is $a_{BP} = 1/(3+1) = 1/4$; if state $B$ emits $G$ twice,
$C$ twice and $A$ once (and nothing else), the emission estimate is $e_B(G) = 2/(2+2+1) = 2/5$.

This counting estimator has an obvious failure mode: any transition or emission that never
happened to occur in the training set gets probability exactly zero. A zero probability is
disastrous for anything computed in log-space, since it contributes an infinite penalty — and a
combination that is merely rare, rather than truly impossible, can easily fail to appear at all in
a finite (or small) sample. Two remedies address this: collect more training data, so that a true
zero and a small-sample zero become distinguishable; or add **pseudocounts** — small counts added
to every $A_{kl}$ and $E_k(b)$ before normalizing, reflecting a prior belief about what the true
parameters roughly look like, so that nothing is ever estimated as exactly impossible on the
strength of a small sample.

## Sources

- MIT 6.047/6.878 Computational Biology (OCW, Fall), *Hidden Markov Models II — Posterior Decoding
  and Learning* (course chapter 8), scribed by Charalampos Mavroforakis and Chidube Ezeozue (2012),
  Thomas Willems (2011), Amer Fejzic (2010) and Elham Azizi (2009). Sections used: 8.1 (review of
  Markov chains, HMMs, Viterbi, and the forward algorithm), 8.1.5 (lecture outline), 8.2 (posterior
  decoding and the backward algorithm, including Figures 8.2 and 8.3), 8.3 (CpG-island HMM, Figure
  8.4), and 8.4–8.4.1 (supervised learning, Figure 8.5), from
  `docs/computational-biology/mit-ocw/6047/compiled/compiled-compiled/04-hidden-markov-models-ii---posterior-decoding-and-learning.md`.
- This source file is a model-reconstructed conversion of a scanned PDF with no text layer (its own
  header flags every equation as unverified); the recursions and worked numbers above follow it as
  given, with only minor index cleanups (e.g. writing the forward algorithm's termination step as
  $P(x)=\sum_k f_k(N)$ throughout, matching how the source itself uses it in the text even though
  one figure box labels it $P(x,\pi^*)$).
- **Not in the supplied source.** The lecture's own outline (section 8.1.5) promises two further
  topics after supervised learning: **Viterbi learning** for unsupervised parameter estimation, and
  the **Baum–Welch algorithm** (EM for HMMs) for unsupervised estimation more generally. The
  supplied file breaks off mid-sentence immediately after introducing pseudocounts (partway through
  section 8.4.1) and the following text jumps to unrelated material from a later chapter on RNA
  evolution — the pages covering Viterbi learning, Baum–Welch, and the CpG-island case study for
  unsupervised learning are missing from this conversion. No slides, transcript or exercises were
  supplied alongside this file for this lecture.

---

[← 12. Genomics of Microbial Ecosystems](12-genomics-of-microbial-ecosystems.md) · [Contents](index.md) · [14. Clustering Gene Expression Data →](14-clustering-gene-expression-data.md)

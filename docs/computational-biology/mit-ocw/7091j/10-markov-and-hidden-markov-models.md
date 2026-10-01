---
title: "10. Markov and Hidden Markov Models"
course: "MIT 7.091J"
chapter: 10
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 10. Markov and Hidden Markov Models

## What this covers

This lecture finishes the treatment of sequence motifs — relative entropy as the right measure of
information under a non-uniform background, inhomogeneous Markov models of position dependence, and
the pseudocount fix for small training sets — and then opens hidden Markov models (HMMs): what the
pieces of an HMM are, how reversing hidden/observable conditioning with Bayes' rule sets up the
problem of inferring hidden states, and the Viterbi algorithm that solves it. It assumes the reader
already has entropy, the weight-matrix (position-specific probability matrix, PSPM) model of a
motif, and basic conditional probability.

## Relative entropy, revisited

Relative entropy between a motif's base distribution $p$ and a background distribution $q$ is

$$D(p\|q) = \sum_{k=1}^{n} p_k \log_2\!\left(\frac{p_k}{q_k}\right),$$

the mean bit-score: if you score a sequence against the motif with a log-odds scheme, $D(p\|q)$ is
the average score a sequence drawn from $p$ would get. In the special case of a uniform background,
$q_k = 1/4^w$ for a motif of width $w$, this reduces to a familiar quantity. Writing it out for a
single position ($q_k=1/4$):

$$\sum_k p_k\log_2\frac{p_k}{q_k} = \sum_k p_k\log_2 p_k - \sum_k p_k \log_2 q_k = -H(p) - \log_2\!\left(\tfrac14\right)\sum_k p_k = -H(p) + 2,$$

using $\sum_k p_k = 1$. So under a uniform background, relative entropy is exactly the usual
information content, $2 - H(p)$, and over a width-$w$ motif this becomes $2w - H_{\text{motif}} =
I_{\text{motif}}$ — the quantity from the previous lecture.

The reason to use relative entropy rather than a bare entropy difference, $H_{\text{before}} -
H_{\text{after}}$, is that it is a better measure once the background stops being uniform. Take a
genome that is 75% A/T: $q_A = q_T = 3/8$, $q_C = q_G = 1/8$. Suppose a one-base motif is simply
"always C" ($p_C = 1$). The naive entropy-difference measure gives $H(q) - H(p) < 2$ bits — and
applying the *uniform-background* formula $2 - H(p)$ to this motif gives exactly 2 bits, which
would predict the motif recurs about once every $2^2 = 4$ bases. That is clearly wrong: in this
background C itself only occurs on average every 8 bases. Relative entropy gets it right because it
weighs the motif against the *actual* background:

$$D(p\|q) = 1 \cdot \log_2\!\left(\frac{1}{1/8}\right) = 3 \text{ bits (the other three terms are all } 0),$$

predicting recurrence once every $2^3 = 8$ bases — matching $q_C = 1/8$ exactly. Relative entropy is
a measure of *information*, not of entropy or uncertainty, and the two coincide only when the
background is uniform. (Also called the Kullback–Leibler distance, or "information for
discrimination.")

**Posed as homework, not solved in lecture:** show that if a two-position motif treats the two
positions as independent — joint probability $p_{ij} = p_i^{(1)}p_j^{(2)}$ for the bases at
positions 1 and 2 — then the entropy of the joint (dinucleotide) distribution decomposes as the sum
of the per-position entropies: $H = -\sum_{i,j}p_{ij}\log_2 p_{ij} = H^{(1)} + H^{(2)}$. The
suggested method is the same one used above: split the log of a product into a sum of logs, then
use linearity of the sum.

## Weight matrices and the independence assumption

A position-specific probability matrix (PSPM, or weight matrix) scores each position of a motif
independently. For the human 5' splice site, the lecture's matrix (rows A/C/G/T, columns positions
$-3$ through $+6$, skipping the invariant GT at $+1,+2$) gives, e.g., $P(G$ at position $-1) = 0.8$.
For a candidate site $S = S_1\cdots S_9 = \texttt{TAGGTCAGT}$,

$$P(S\mid +) = P_{-3}(S_1)\,P_{-2}(S_2)\,P_{-1}(S_3)\cdots P_5(S_8)\,P_6(S_9).$$

This model is *inhomogeneous* (the distribution changes from position to position) but assumes
independence between positions. The natural question the slide poses is: **what if that is not
true** — what if the base at one position depends on its neighbour?

## Inhomogeneous first-order Markov models

If dependence between adjacent positions matters, the natural generalization is a first-order
Markov model: the base at position $k$ depends on the base at position $k-1$ but nothing earlier.
Conditional probabilities are estimated from counts,

$$P_{-2}(A\mid C) = \frac{N_{CA}^{(-3,-2)}}{N_C^{(-3)}},$$

the count of $CA$ at positions $(-3,-2)$ divided by the count of $C$ at position $-3$ — the usual
conditional-probability definition, $P(A\mid B) = P(A,B)/P(B)$, with counts standing in for
probabilities since the normalizing constant cancels. The probability of a sequence under this model
is

$$P(S\mid +) = P_{-3}(S_1)\,P_{-2}(S_2\mid S_1)\,P_{-1}(S_3\mid S_2)\cdots P_6(S_9\mid S_8),$$

and a score is formed as a log-odds ratio against a homogeneous background model $P(S\mid -)$ built
the same way from bulk genomic sequence:

$$R = \frac{P(S\mid +)}{P(S\mid -)}, \qquad s = \log_2 R.$$

Taking the log converts a product of many small probabilities — which underflows numerically — into
a sum.

Scoring real genomic sequence with both a weight-matrix model and a first-order Markov model of the
5' splice site, both partially separate true sites from decoys, with some overlap in the middle of
the score distribution; the Markov model's distribution has a slightly tighter left tail, so it
separates true from decoy a bit better — not dramatically, but consistently. Markov models help when
there genuinely is positional dependence *and* there is enough data to estimate the extra
parameters; 5' splice sites are a good case for this because there are a few thousand well-annotated
examples in the human genome. (Markov models have also been reported to improve modeling of
transcriptional motifs — Zhou & Liu, *Bioinformatics*, 2004 — a result the lecture names without
elaborating.)

## How many parameters, and the limits of training data

Dependence can extend further back than one position: a $k$-th-order Markov model makes the next
base depend on the previous $k$ bases. Parameters per position grow like $4^{k+1}$: a
position-independent (weight-matrix) model needs 4 numbers per position (really 3 free ones, since
the four base probabilities sum to 1, but it is convenient to count 4); first-order needs
$4\times4=16$ per position (except the first, which has no predecessor and needs only 4);
second-order needs $4\times4\times4=64$. The constraint is always data: with only a hundred training
sequences you cannot reliably estimate 64 parameters per position, and the model should be
simplified rather than pushed to higher order.

This motivates a concrete problem. Suppose ten sequences bound by some transcription factor are
aligned, and at position 1 the tally is A:8, C:1, G:1, T:0. Can we conclude T is simply incompatible
with binding? If the true frequency of T at that position were actually 10%, what is the chance a
sample of 10 would show *no* T at all? By the binomial, $P(N=0) = \binom{10}{0}(0.1)^0(0.9)^{10}
\approx 35\%$ — essentially a Poisson with mean 1, so $\approx e^{-1}$. Seeing zero T's is far from
conclusive evidence that T never occurs, so assigning it probability exactly 0 is overconfident.

The principled fix is a **pseudocount**. Maximum-likelihood estimation simply uses the observed
frequency, but treating the true per-position frequencies as drawn from a Dirichlet prior and
computing the Bayesian posterior given the observed counts turns out to be equivalent to adding one
count to every bin before renormalizing:

| Nt | Count | $\Psi$-count | Bayes count | ML estimate | Bayes estimate |
|----|-------|------|------|------|------|
| A | 8 | +1 | 9 | 0.80 | 0.64 |
| C | 1 | +1 | 2 | 0.10 | 0.14 |
| G | 1 | +1 | 2 | 0.10 | 0.14 |
| T | 0 | +1 | 1 | 0.00 | 0.07 |
| total | 10 | | 14 | 1.00 | 1.00 |

Adding a pseudocount pulls probability away from the most frequently observed bases and toward
those never seen — exactly the effect wanted given how little the sample rules out. With a larger
sample (say 80/10/10/0 instead of 8/1/1/0) the same single added count has much less relative
effect, so the Bayes estimate converges to the ML estimate as data accumulates. (A smaller
pseudocount is sometimes used instead — a quarter of a count spread across the four bins — a choice
the lecture notes is debated, without giving the arguments.) The Dirichlet-posterior derivation
itself is not given in lecture; it is in the appendix of Durbin, Eddy, Krogh & Mitchison's
*Biological Sequence Analysis*, and in the course's Probability and Statistics Primer.

## Markov chains, briefly

A Markov chain is a sequence of random variables where the future is conditionally independent of
the past given the present. The running example is genotype at a locus across generations of a
family: Bart's genotype depends on Homer's, but is conditionally independent of Grandpa's once
Homer's is known,

$$P(\text{Bart}=a/a \mid \text{Grandpa}=A/a,\ \text{Homer}=a/a) = P(\text{Bart}=a/a \mid \text{Homer}=a/a).$$

## From Markov chain to hidden Markov chain

Now suppose genotype cannot be observed directly — the sequencer is broken, say — but a phenotype
correlated with it can be: LDL cholesterol, which depends on genotype probabilistically (homozygous
individuals tend toward higher cholesterol, but diet and other factors blur the relationship).
Observed: Grandpa 150 (low), Homer 250 (high), Bart 200 (intermediate). Bart's cholesterol alone is
ambiguous between the two genotypes. But Homer's high cholesterol makes it more likely Homer is
homozygous, and that in turn shifts the prior on Bart's genotype, and hence on how Bart's own
intermediate reading should be interpreted. This — a Markov chain of hidden states, each emitting an
observable that depends probabilistically on the hidden state — is a hidden Markov model.

## HMM terminology and the generative view

An HMM is specified by:

- a set of hidden states and an **initial state distribution** $\pi_i$,
- **transition probabilities** $a_{ij}$ between states,
- **emission probabilities** $b_i(k)$, the chance state $i$ emits observable symbol $k$.

It can be read as a generator, producing an observation sequence $O = O_1 O_2 \cdots O_T$ (from
Rabiner's tutorial):

1. Choose an initial state $q_1 = S_i$ according to $\pi$.
2. Set $t=1$.
3. Choose $O_t = v_k$ according to $b_i(k)$, the emission distribution of the current state.
4. Transition to a new state $q_{t+1}=S_j$ according to $a_{ij}$.
5. Set $t=t+1$; return to 3 if $t<T$, else stop.

HMMs provide a general way to model "sequence labeling" problems — a sequence (genomic, protein,
RNA) has underlying features (promoters, exons, domains) that are to be inferred from the sequence
itself, often using a training set of known examples to learn what each label's composition looks
like. They can be designed just by drawing a graph — states, with transitions between them, possibly
including cycles — which is why they have been called "the Legos of computational sequence
analysis." They were developed in electrical engineering decades ago for speech recognition and are
still used there.

## Designing an HMM: bacterial gene finding

As a design exercise, a bacterial protein-coding gene needs a start codon, an open reading frame,
and a stop codon. Working through the choices live:

- A **Start** state and a **Stop** state, each emitting a fixed codon (3 nucleotides).
- An **N** (intergenic) state. It must be able to emit an arbitrary stretch of sequence, so rather
  than trying to emit "any number" of bases at once, it emits a single base and loops back to
  itself — this is what will make the Viterbi algorithm tractable later.
- A **Codon** state for the open reading frame, which similarly emits one codon (3 nucleotides) and
  loops back to itself, so the ORF can be any length.

Transitions: N → Start → Codon (self-looping) → Stop → N. A question raised in class — shouldn't N
also transition directly to Stop, to allow genes on the reverse strand? — is a real complication the
model as drawn does not handle: a reverse-strand gene would need its own mirror states, emitting the
reverse complement of the stop codon and traversing the cycle the other way, which the lecture notes
but does not draw.

<figure>
<svg viewBox="0 0 360 240" role="img" aria-label="Gene-finding hidden Markov model built up in class: four states cycling N, Start, Codon, Stop">
  <defs>
    <marker id="arrow11" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
    </marker>
  </defs>

  <circle cx="80" cy="190" r="38" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="80" y="188" text-anchor="middle" font-size="13" fill="currentColor">N</text>
  <text x="80" y="203" text-anchor="middle" font-size="10" fill="currentColor">1 nt</text>

  <circle cx="80" cy="50" r="38" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="80" y="48" text-anchor="middle" font-size="13" fill="currentColor">Start</text>
  <text x="80" y="63" text-anchor="middle" font-size="10" fill="currentColor">3 nt</text>

  <circle cx="280" cy="50" r="38" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="280" y="48" text-anchor="middle" font-size="13" fill="currentColor">Codon</text>
  <text x="280" y="63" text-anchor="middle" font-size="10" fill="currentColor">3 nt</text>

  <circle cx="280" cy="190" r="38" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="280" y="188" text-anchor="middle" font-size="13" fill="currentColor">Stop</text>
  <text x="280" y="203" text-anchor="middle" font-size="10" fill="currentColor">3 nt</text>

  <line x1="80" y1="152" x2="80" y2="88" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow11)"/>
  <line x1="118" y1="50" x2="242" y2="50" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow11)"/>
  <line x1="280" y1="88" x2="280" y2="152" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow11)"/>
  <line x1="242" y1="190" x2="118" y2="190" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow11)"/>

  <path d="M 55 215 C 20 240, 20 170, 52 168" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow11)"/>
  <path d="M 305 20 C 345 -5, 345 75, 308 73" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow11)"/>
</svg>
<figcaption>The gene-finding HMM assembled state by state in class. Start and Stop each emit a fixed
codon; Codon self-loops to emit the open reading frame one codon at a time; N self-loops to emit
intergenic sequence one base at a time — the self-loops are what let both regions have arbitrary
length.</figcaption>
</figure>

## CpG islands, and an HMM for them

CpG (cytosine followed by guanine along one strand, not a C–G base pair) is normally rare in
vertebrate genomes because the C in CpG is a methylation target, and methylated C is mutagenic, so
CpGs tend to mutate away over evolutionary time — except where kept unmethylated. Such unmethylated
regions, with elevated CpG and overall C+G content, are **CpG islands**, associated with the
promoters of roughly half of human genes; against a genome background of about 40% C+G, islands
typically run 50–60%. Finding them is one way to predict promoter locations.

The simplest possible HMM for this has two hidden states, **Genome** and **Island**, each emitting a
single base at every position, with the four possible transitions between them (including staying
put). Using Rabiner's notation:

- Initiation: $\pi_{\text{genome}} = 0.99$, $\pi_{\text{island}} = 0.01$ (islands are uncommon).
- Transition: if an island averages about 1 kb, a reasonable island→island probability is
  $P_{ii}=0.999$ (so 0.1% chance per base of leaving); if islands are interspersed roughly every
  100 kb, $P_{gg}=0.99999$ and $P_{gi}=0.00001$; $P_{ig}=0.001$.
- Emission — this is where the predictive power comes from: Genome emits C,G,A,T with probabilities
  0.2, 0.2, 0.3, 0.3; Island emits them with 0.3, 0.3, 0.2, 0.2 (island is C+G rich).

<figure>
<svg viewBox="0 0 380 220" role="img" aria-label="Two-state hidden Markov model for CpG islands with self-loop and cross transitions">
  <defs>
    <marker id="arrow10" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="110" cy="130" r="42" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="110" y="135" text-anchor="middle" font-size="13" fill="currentColor">Genome</text>
  <circle cx="290" cy="130" r="42" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="290" y="135" text-anchor="middle" font-size="13" fill="currentColor">Island</text>

  <path d="M 85 95 C 60 50, 140 50, 135 95" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow10)"/>
  <text x="110" y="42" text-anchor="middle" font-size="12" fill="currentColor">P_gg = 0.99999</text>

  <path d="M 265 95 C 240 50, 320 50, 315 95" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow10)"/>
  <text x="290" y="42" text-anchor="middle" font-size="12" fill="currentColor">P_ii = 0.999</text>

  <path d="M 152 115 C 190 100, 210 100, 248 115" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow10)"/>
  <text x="200" y="95" text-anchor="middle" font-size="12" fill="currentColor">P_gi = 0.00001</text>

  <path d="M 248 148 C 210 165, 190 165, 152 148" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow10)"/>
  <text x="200" y="183" text-anchor="middle" font-size="12" fill="currentColor">P_ig = 0.001</text>
</svg>
<figcaption>The CpG-island HMM: leaving either state is rare, so the model favours long runs of
genome or long runs of island, distinguished only by a mild difference in emission bias.</figcaption>
</figure>

The model as written generates observable sequence from hidden state; in practice we have the
observable sequence (A C T C G A G T A, say) and want the hidden states. That requires reversing the
conditioning.

## Reversing the conditioning: Bayes' rule

From the definition of conditional probability, $P(A\mid B) = P(A,B)/P(B)$. Writing the joint
probability the other way, $P(A,B) = P(B\mid A)P(A)$, and substituting gives Bayes' rule in its
simple form,

$$P(B\mid A) = \frac{P(B)\,P(A\mid B)}{P(A)},$$

and, summing the denominator over all the mutually exclusive cases $B_k$, its general form,

$$P(B_i\mid A) = \frac{P(B_i)\,P(A\mid B_i)}{\sum_k P(B_k)\,P(A\mid B_k)}.$$

For an HMM, let $H$ be the random vector of hidden states and $O$ the random vector of observed
bases, with $h_1,\ldots,h_n$ and $o_1,\ldots,o_n$ specific values. We want $P(H=h_1,\ldots,h_n \mid
O=o_1,\ldots,o_n)$, but the model is written as $P(O\mid H)$. By the definition of conditional
probability and then Bayes' rule,

$$P(H=h_1,\ldots,h_n\mid O=o_1,\ldots,o_n) = \frac{P(H=h_1,\ldots,h_n,\,O=o_1,\ldots,o_n)}{P(O=o_1,\ldots,o_n)} = \frac{P(H=h_1,\ldots,h_n)\,P(O=o_1,\ldots,o_n\mid H=h_1,\ldots,h_n)}{P(O=o_1,\ldots,o_n)}.$$

$P(O=o_1,\ldots,o_n)$ is awkward to compute directly — a sum over every possible hidden-state
sequence, $2^n$ of them for a 2-state model of length $n$ — but it does not depend on the particular
$h_1,\ldots,h_n$ considered, so for finding the *best* hidden sequence it can be treated as an
unknown constant. Maximizing the conditional probability over $h_1,\ldots,h_n$ is therefore the
same as maximizing the joint probability,

$$P(H=h_1,\ldots,h_n,\, O=o_1,\ldots,o_n).$$

The optimal hidden sequence, $H^{\text{opt}} = h_1^{\text{opt}},\ldots,h_n^{\text{opt}}$, is called
the optimal **parse** of the observed sequence.

## The Viterbi algorithm

Define $R_i(h)$ (Rabiner's notation: $\delta_t(j)$) as the probability of the optimal parse of the
subsequence from the start up to position $i$, *ending* in hidden state $h$. This can be solved
recursively: $R_1(h)$ is immediate, and $R_{i}(h)$ is built from $R_{i-1}(\cdot)$.

In full (Rabiner's statement, with $N$ states and sequence length $T$, $\pi_i$ initial, $a_{ij}$
transition, $b_j(k)$ emission):

1. **Initialization:** $\delta_1(i) = \pi_i\, b_i(O_1)$, $\psi_1(i)=0$.
2. **Recursion**, for $2\le t\le T$: $\delta_t(j) = \max_i\big[\delta_{t-1}(i)\,a_{ij}\big]\,b_j(O_t)$,
   with $\psi_t(j) = \operatorname{argmax}_i\big[\delta_{t-1}(i)\,a_{ij}\big]$ recording *which*
   predecessor state won.
3. **Termination:** $P^* = \max_i \delta_T(i)$, $q_T^* = \operatorname{argmax}_i\delta_T(i)$.
4. **Backtracking:** $q_t^* = \psi_{t+1}(q_{t+1}^*)$ for $t=T-1,\ldots,1$.

Recording which predecessor state won at each step (the $\psi$ arrows) is exactly the traceback idea
from Needleman–Wunsch or Smith–Waterman: don't just keep the best score, remember how you got there.

**Worked example.** Take the CpG-island HMM above and the sequence ACG.

| $i$ | base | $R_i(\text{Genome})$ | winning predecessor | $R_i(\text{Island})$ | winning predecessor |
|---|---|---|---|---|---|
| 1 | A | $0.99\times0.3=0.297$ | — (initial) | $0.01\times0.2=0.002$ | — (initial) |
| 2 | C | $0.297\times0.99999\times0.2\approx0.0594$ | Genome | $0.002\times0.999\times0.3\approx0.000599$ | Island |
| 3 | G | $0.0594\times0.99999\times0.2\approx0.01188$ | Genome | $0.000599\times0.999\times0.3\approx0.0001796$ | Island |

At position 1 Genome already wins by about 150-fold: the initial probabilities (0.99 vs 0.01)
dominate the small emission difference (0.3 vs 0.2 for A). At each later position, staying in Genome
beats switching from Island ($G\to G\approx 1$, $I\to G=0.001$), and staying in Island beats
switching from Genome, since $P_{gi}=0.00001$ is a steeper penalty than the emission gain from
Island's C/G bias. Here $R_3(\text{Genome}) \gg R_3(\text{Island})$, so the optimal parse
backtracks to Genome throughout — two bases of C/G bias are not enough to pay for the transition
penalty of leaving and re-entering Genome.

**When does it actually pay to switch?** Consider $(\text{ACGT})_{10000}$ (the four-letter unit
repeated 10,000 times): the optimal parse stays in Genome the whole way, because the repeat unit is
itself unbiased for C/G versus A/T, so the total emission probability is the same whichever state
generates it, while the initial and transition probabilities both favour Genome throughout.

Now consider $\text{A}_{1000}\text{C}_{80}\text{T}_{1000}\text{C}_{20}\text{A}_{1000}\text{G}_{60}\text{T}_{1000}$.
Since the $G\to G$ and $I\to I$ transitions are both close to 1, the only transitions that matter are
the rare $G\to I$ and $I\to G$ ones, and switching into Island and back costs a combined penalty of
about $P_{gi}\times P_{ig} = 10^{-5}\times10^{-3}=10^{-8}$. Each base of a C or G run emitted in
Island rather than Genome gains a factor of $0.3/0.2 = 1.5$ in emission probability, so a run of
length $N$ gains $1.5^N$ — it is worth switching once $1.5^N$ exceeds the $10^{-8}$ transition
penalty, i.e. once $1.5^N \gtrsim 10^8$:

| $N=$ | 20 | 40 | 60 | 80 |
|---|---|---|---|---|
| $1.5^N \approx$ | $3\times10^3$ | $1\times10^7$ | $3\times10^{10}$ | $1\times10^{14}$ |

The run of 20 C's falls well short and is parsed as Genome; the runs of 60 and 80 clear the bar
comfortably and are parsed as Island. So the predicted optimal parse is
$G_{1000}\,I_{80}\,G_{2020}\,I_{60}\,G_{1000}$ (the middle 2020 genome bases are $T_{1000}$, the
too-short $C_{20}$, and $A_{1000}$ run together).

A subtlety the class's own intuition tripped on: it can look as if the algorithm must be
"lagging" — staying in Genome for a few bases into an island run before switching — since at each
position the best parse *ending in Island* still comes from having been in Genome as long as
possible. This is not a defect: $R_i(\text{Island})$ is defined as the best parse *up to that
point* ending in Island, and early in a profitable run the path that stayed in Genome longest
genuinely is the best one ending in Island so far. Viterbi provably returns the globally optimal
parse; the appearance of a lag is an artifact of reading the recursion one step at a time.

## Running time

At each step from position $t$ to $t+1$, with $k$ hidden states there are $k^2$ possible transitions
to consider (every state to every state), so the recursion costs $O(k^2)$ per position and
$O(k^2L)$ overall for a sequence of length $L$ — linear in sequence length. For the CpG-island HMM,
$k=2$, so this is barely more work than reading the sequence once; even a much more complex HMM
stays linear in $L$, comparing favourably with the $O(L^2)$ cost of pairwise sequence comparison.
This efficiency is a major reason for the popularity of HMMs. (If many transitions have probability
zero — as in the gene-finding HMM — the sum can skip those and run faster still.)

## Exercises

- Show that if a two-position motif model treats the two positions as independent, so that the
  joint probability of the dinucleotide factors as $p_{ij} = p_i^{(1)}p_j^{(2)}$, then the entropy of
  the joint distribution equals the sum of the per-position entropies: $H = -\sum_{i,j}p_{ij}\log_2
  p_{ij} = H^{(1)} + H^{(2)}$.

## Sources

- Slides: `computational-biology/mit-ocw/7091j/lectures/10-slides.md` (C. Burge, Lecture 10, March
  11, 2014) — relative entropy definitions and example, the 5' splice site PSPM, the inhomogeneous
  Markov model equations, the WMM-vs-Markov comparison figure, parameter-count and pseudocount
  slides and table, HMM terminology and generative-model procedure, the Simpsons genealogy and
  genotype/phenotype examples, CpG island HMM parameter tables, Bayes' rule slides, the Viterbi
  algorithm equations (32–35), the Viterbi run-length examples and powers-of-1.5 table, and the
  $O(k^2L)$ runtime slide.
- Transcript: `computational-biology/mit-ocw/7091j/recordings/lectures/10.md` — relative-entropy
  derivation and non-uniform-background discussion (00:00–06:58); Markov-model score and WMM
  comparison (06:58–10:28); parameter-counting dialogue and pseudocount example (10:28–18:28); HMM
  introduction, generative view, genotype/phenotype reasoning (18:28–25:10); interactive design of
  the bacterial gene-finding HMM (25:10–30:41); CpG island biology and HMM parameters (30:41–36:58);
  Bayes' rule derivation and its application to HMMs (37:01–45:18); worked Viterbi example on ACG
  (45:18–59:18); run-length examples, the powers-of-1.5 argument, and why the algorithm is not
  "lagging" (59:18–1:11:38); runtime discussion (1:11:38–1:15:00).
- Named in the lecture but not covered in its content: TMHMM (transmembrane-helix HMM, promised for
  a later lecture); the course's NBT Primer on HMMs; Z&B (course textbook) Chapter 6; Rabiner's
  "Tutorial on Hidden Markov Models and Selected Applications in Speech Recognition"; Durbin, Eddy,
  Krogh & Mitchison, *Biological Sequence Analysis* (pseudocount derivation, in its appendix); the
  course's Probability and Statistics Primer; Zhou & Liu, *Bioinformatics* 2004 (Markov models for
  transcriptional motifs). Midterm logistics discussed at the end of the lecture are administrative
  and are omitted here.

---

[← 9. Sequence Motifs and the Gibbs Sampler](09-sequence-motifs-and-the-gibbs-sampler.md) · [Contents](index.md) · [11. Real-World HMMs and RNA Structure →](11-real-world-hmms-and-rna-structure.md)

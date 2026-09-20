---
title: "5. Training Hidden Markov Models"
course: "MIT 6047"
chapter: 5
source: "https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 5. Training Hidden Markov Models

## What this covers

This chapter answers one question: given a sequence and a hidden Markov model, how do you estimate
the model's parameters — the transition probabilities $a_{kl}$ and emission probabilities $e_k(b)$
— from data? It covers both settings the lecture distinguishes: **supervised learning**, where the
true state path $\pi$ is known for the training data, and **unsupervised learning**, where it is
not, via **Viterbi training** and the **Baum-Welch algorithm** (expectation-maximization applied to
HMMs). It assumes the reader already has the vocabulary of Markov chains and hidden Markov models,
the Viterbi algorithm for finding the single most likely path, and the forward and backward
algorithms for computing $P(x)$ and the posterior probability of a state at a given position — the
four algorithms the lecture treats as settled before turning to learning.

## Where learning fits

The course organizes six algorithmic problems along two axes: whether you commit to a single path
through the hidden states or sum over all of them, and whether the task is to score a sequence,
decode the states behind it, or learn the model that generates it.

| | One path | All paths |
| :--- | :--- | :--- |
| **Scoring** | $P(x,\pi)$ — probability of one path and its emissions | $P(x)=\sum_\pi P(x,\pi)$ — total probability of $x$, over all paths (forward algorithm) |
| **Decoding** | $\pi^*=\operatorname{argmax}_\pi P(x,\pi)$ — Viterbi, the single most likely path | $\hat\pi_i=\operatorname{argmax}_k P(\pi_i=k\mid x)$ — posterior decoding, the most likely state at each position |
| **Learning** | $\Lambda^*=\operatorname{argmax}_\Lambda P(x,\pi\mid\Lambda)$ given $\pi$ (supervised); or $\operatorname{argmax}_\Lambda\max_\pi P(x,\pi\mid\Lambda)$ (Viterbi training) | $\Lambda^*=\operatorname{argmax}_\Lambda\sum_\pi P(x,\pi\mid\Lambda)$ — Baum-Welch, weighting over all paths |

The top four cells were the previous lecture's material. This chapter is the bottom row: learning,
first when the path is known, then when it is not.

## Supervised learning: counting when the path is known

Suppose you are given a sequence $x=x_1\ldots x_N$ together with the true underlying path
$\pi=\pi_1\ldots\pi_N$ — for example a genomic region with experimentally confirmed CpG-island
annotations. Define

- $A_{kl}$ = the number of times the transition $k\to l$ occurs in $\pi$,
- $E_k(b)$ = the number of times state $k$ emits symbol $b$ in $x$.

The maximum-likelihood parameters are then just the observed frequencies:

$$a_{kl} = \frac{A_{kl}}{\sum_i A_{ki}}, \qquad e_k(b) = \frac{E_k(b)}{\sum_c E_k(c)}$$

The mechanism is the one the lecture illustrates with a toy path/sequence pair — a path such as
start $\to B\to B\to B\to P\to P\to P\to B\to B\to$ end against a sequence such as
$G\,C\,A\,A\,A\,T\,G\,C$: walk along the path, tally every $k\to l$ transition into an
$A_{kl}$ table and every state-symbol pair into an $E_k(b)$ table, then normalize each row. The
slides set this table up but leave the tally blank — it is a counting exercise, not a worked
example, and the point is only that the parameters are nothing more than relative frequencies.

### The overfitting trap

Counting frequencies breaks down on small training sets. The lecture's example: given ten
nucleotides all labelled with the same state,

$$x = C, A, G, G, T, C, C, A, T, C \qquad \pi = P, P, P, P, P, P, P, P, P, P$$

the maximum-likelihood estimate is

$$a_{PP} = 1,\quad a_{PB} = 0, \qquad e_P(A)=.2,\ e_P(C)=.4,\ e_P(G)=.2,\ e_P(T)=.2$$

$P(x\mid\theta)$ is indeed maximized by these parameters, but $\theta$ itself is not a reasonable
model: a transition probability of exactly zero means the model asserts a $B\to$ background
excursion can *never* happen, purely because it never happened in ten letters. A single such zero
in a long decoding or scoring computation makes the whole path's probability zero.

### Pseudocounts

The fix is to add a pseudocount to every tally before normalizing:

$$A_{kl} = (\text{# times } k\to l \text{ occurs}) + r_{kl}, \qquad E_k(b) = (\text{# times state } k \text{ emits } b) + r_k(b)$$

The $r_{kl}$ and $r_k(b)$ encode a prior belief about the parameters: large pseudocounts encode a
strong prior (the data has to work hard to overturn it), while small pseudocounts ($\varepsilon<1$)
do almost nothing except keep every probability strictly positive.

### Worked example: training Markov chains for CpG islands

Applying exactly this counting procedure to a training set of DNA sequences with known CpG-island
boundaries gives two separate Markov chains — a "+" model fit only to the islands and a "−" model
fit to everything else — with transition probabilities

$$a^+_{st} = \frac{c^+_{st}}{\sum_{t'} c^+_{st'}}, \qquad a^-_{st} = \frac{c^-_{st}}{\sum_{t'} c^-_{st'}}$$

where $c^+_{st}$ (respectively $c^-_{st}$) counts how often letter $t$ follows letter $s$ inside
(respectively outside) the islands. The lecture reports the fitted tables:

**+ model** (inside CpG islands)

| | A | C | G | T |
| :--- | :--- | :--- | :--- | :--- |
| **A** | .180 | .274 | .426 | .120 |
| **C** | .171 | .368 | .274 | .188 |
| **G** | .161 | .339 | .375 | .125 |
| **T** | .079 | .355 | .384 | .182 |

**− model** (outside CpG islands)

| | A | C | G | T |
| :--- | :--- | :--- | :--- | :--- |
| **A** | .300 | .205 | .285 | .210 |
| **C** | .322 | .298 | .078 | .302 |
| **G** | .248 | .246 | .298 | .208 |
| **T** | .177 | .239 | .292 | .292 |

The asymmetry is exactly the CpG signal: inside islands, C is much more likely to be followed by G
(row **C**, column **G**: .274 vs .078 outside) — a CpG dinucleotide is suppressed everywhere else
in the genome by methylation-driven mutation, but preserved inside the islands.

## Unsupervised learning: the path is hidden

Now suppose the "right answer" is unknown — the lecture's example is a newly sequenced genome
(a porcupine) where neither the location nor the base composition of its CpG islands has been
measured. The question becomes: update the parameters $\theta$ to maximize $P(x\mid\theta)$, with
no labelled $\pi$ to count against.

The shared idea behind both methods below:

1. Start with some guess at the parameters.
2. Use those parameters to produce some estimate of the hidden path.
3. Use that estimate to update the parameters by maximum likelihood, exactly as in the supervised
   case.
4. Iterate to convergence.

The two methods differ only in step 2 — what "estimate of the hidden path" means.

### Viterbi training: best guess = best path

**Initialization.** Pick a starting guess for the parameters (or start arbitrarily).

**Iteration**, until convergence:

1. Run Viterbi to find the single most likely path $\pi^*$ under the current parameters.
2. Compute $A_{kl}$, $E_k(b)$ by tallying transitions and emissions along $\pi^*$ (plus
   pseudocounts).
3. Recompute $a_{kl}, e_k(b)$ from those tallies.

This is the simple option: at every iteration you commit to one path and count exactly as in the
supervised case. The lecture flags three things worth holding onto, without resolving the first:

- Convergence to a local maximum is guaranteed — the lecture poses this as a question ("why?")
  rather than proving it, so treat it as a fact to sit with rather than one derived here.
- It does not maximize $P(x\mid\theta)$ directly — only the probability of the single best path,
  $\max_\pi P(x,\pi\mid\theta)$, which is a lower bound on $P(x\mid\theta)=\sum_\pi P(x,\pi\mid\theta)$.
- In general it performs worse than Baum-Welch, below.

### Baum-Welch: weighting over all paths

Baum-Welch is expectation-maximization (EM) applied to the HMM. The general shape of EM, independent
of HMMs:

1. Use the current model to **estimate** the missing data (the **E step**).
2. Use that estimate to **update** the model (the **M step**).
3. Repeat until convergence.

Formally, with $Q$ the distribution over hidden labels given the current parameters,

$$Q = P(\text{labels}\mid S,\ \text{params}^{t-1}) \qquad \text{(E step)}$$
$$\text{params}^t = \operatorname*{argmax}_{\text{params}} \; E_Q\big[\log P(S,\text{labels}\mid\text{params}^{t-1})\big] \qquad \text{(M step)}$$

and each iteration is guaranteed not to decrease $P(S\mid\text{model})$. EM is not specific to HMMs
— the lecture names it as the same tool behind SiPhy, $k$-means clustering and motif finding
elsewhere in the course, though none of those are worked here.

**Applied to an HMM**, the E step means: instead of committing to one path, compute — for every
position $i$ and every pair of states $k,l$ — the *posterior probability that the path used the
transition $k\to l$ at that position*, given the whole observed sequence.

Recall the forward and backward variables: $f_k(i)=P(x_1\ldots x_i,\pi_i=k)$, and
$b_l(j)=P(x_{j+1}\ldots x_N\mid\pi_j=l)$. The transition posterior is

$$P(\pi_i=k,\pi_{i+1}=l\mid x) = \frac{Q}{P(x)}, \qquad Q = P(x_1\ldots x_i,\pi_i=k,\pi_{i+1}=l,x_{i+1}\ldots x_N)$$

and $Q$ splits, by conditioning on being in state $k$ at $i$, into a piece before $i$ and a piece
from $i$ onward:

$$Q = P(\pi_{i+1}=l, x_{i+1}\ldots x_N \mid \pi_i=k)\, f_k(i)$$

and the second factor peels off one transition, one emission, then everything after — which, by the
Markov and emission-independence assumptions of the HMM, depends only on being in state $l$ at
$i+1$:

$$P(\pi_{i+1}=l,x_{i+1}\ldots x_N\mid\pi_i=k) = \underbrace{P(x_{i+2}\ldots x_N\mid\pi_{i+1}=l)}_{b_l(i+1)}\ \underbrace{P(x_{i+1}\mid\pi_{i+1}=l)}_{e_l(x_{i+1})}\ \underbrace{P(\pi_{i+1}=l\mid\pi_i=k)}_{a_{kl}}$$

so that

$$P(\pi_i=k,\pi_{i+1}=l\mid x,\theta) = \frac{f_k(i)\,a_{kl}\,e_l(x_{i+1})\,b_l(i+1)}{P(x\mid\theta)}$$

<figure>
<svg viewBox="0 0 480 190" role="img" aria-label="Forward and backward variables meeting at a single transition from state k to state l">
  <defs>
    <marker id="arrow5" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="20" y1="150" x2="460" y2="150" stroke="currentColor" stroke-width="1" stroke-opacity="0.4"/>
  <text x="60" y="170" font-size="11" text-anchor="middle" fill="currentColor">x_1 ... x_i</text>
  <text x="240" y="170" font-size="11" text-anchor="middle" fill="currentColor">x_(i+1)</text>
  <text x="420" y="170" font-size="11" text-anchor="middle" fill="currentColor">x_(i+2) ... x_N</text>
  <circle cx="180" cy="95" r="18" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="180" y="100" font-size="13" text-anchor="middle" fill="currentColor">k</text>
  <circle cx="300" cy="95" r="18" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="300" y="100" font-size="13" text-anchor="middle" fill="currentColor">l</text>
  <line x1="30" y1="95" x2="160" y2="95" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow5)"/>
  <text x="90" y="83" font-size="12" text-anchor="middle" fill="currentColor">f_k(i)</text>
  <line x1="198" y1="95" x2="280" y2="95" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow5)"/>
  <text x="240" y="70" font-size="12" text-anchor="middle" fill="currentColor">a_kl · e_l(x_(i+1))</text>
  <line x1="318" y1="95" x2="450" y2="95" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow5)"/>
  <text x="385" y="83" font-size="12" text-anchor="middle" fill="currentColor">b_l(i+1)</text>
</svg>
<figcaption>The posterior probability of using transition k→l at position i factors into three
independent pieces: the forward probability of everything up to i ending in state k, the single
transition-and-emission step, and the backward probability of everything after i+1 starting from
state l.</figcaption>
</figure>

**M step.** Summing this posterior over every position $i$ gives the *expected* number of times the
transition $k\to l$ was used — a fractional count, since the path is no longer committed to:

$$A_{kl} = \sum_i P(\pi_i=k,\pi_{i+1}=l\mid x,\theta) = \sum_i \frac{f_k(i)\,a_{kl}\,e_l(x_{i+1})\,b_l(i+1)}{P(x\mid\theta)}$$

and, by the same reasoning applied to emissions rather than transitions,

$$E_k(b) = \frac{1}{P(x)}\sum_{i\,:\,x_i=b} f_k(i)\,b_k(i)$$

The new parameters $a_{kl}, e_k(b)$ are then obtained from these expected counts by exactly the same
normalization formulas as in the supervised case. Nothing about the M step changes — only the
counts feeding it are now expectations over all paths rather than tallies along one.

**Multiple training sequences.** If training on several sequences $x^1,\ldots,x^M$, sum the expected
counts over sequences as well as positions:

$$A_{kl} = \sum_x\sum_i \frac{f_k(i)\,a_{kl}\,e_l(x_{i+1})\,b_l(i+1)}{P(x\mid\theta)}, \qquad E_k(b) = \sum_x \frac{1}{P(x)}\sum_{i\,:\,x_i=b} f_k(i)\,b_k(i)$$

### The Baum-Welch algorithm, assembled

**Initialization.** Guess the parameters (or start arbitrarily).

**Iteration**, until $P(x\mid\theta)$ stops changing appreciably:

1. Run the forward algorithm.
2. Run the backward algorithm.
3. Compute the new log-likelihood $P(x\mid\theta)$ — this is the E step.
4. Compute the expected counts $A_{kl}, E_k(b)$.
5. Recompute the parameters $a_{kl}, e_k(b)$ from those counts — this is the M step.

Each iteration is guaranteed not to decrease $P(x\mid\theta)$, by the general EM guarantee stated
above.

### Practical comments

- **Cost.** Each iteration is one forward pass and one backward pass, so the total cost is
  $(\text{\# iterations})\times O(K^2N)$ for $K$ states and a length-$N$ sequence.
- **Local, not global.** The likelihood is guaranteed to increase every iteration, but Baum-Welch is
  not guaranteed to find the *globally* best parameters — it converges to a local optimum, and which
  one depends on where you started.
- **Overtraining.** A model with too many parameters relative to the amount of training data
  overfits in exactly the way the supervised case did, only harder to notice: you never see the raw
  counts, only fractional expectations, so a parameter quietly drifting to an extreme is easy to
  miss.

## Scaling the state space: from GC content to gene structure

The same three ingredients — a generative model, scoring/decoding by forward/Viterbi, and learning
by counting or by Baum-Welch — scale to state spaces far richer than the two-state
background/pathogenicity-island model used above. What changes from task to task is only the number
of states and what each one emits:

| Task | States | Distinguishes | Emits |
| :--- | :--- | :--- | :--- |
| GC-rich region detection | 2 | GC-rich vs AT-rich | nucleotides |
| CpG-island detection | 8 (4 each, $+/-$) | CpG-rich vs CpG-poor | dinucleotides |
| Conserved-region detection | 2 | conserved vs non-conserved | level of conservation |
| Coding-exon detection | 2 | coding exon vs non-coding | nucleotide triplets |
| Coding-conservation detection | 2 | coding exon vs non-coding | $64\times64$ codon-substitution frequencies |
| Gene-structure detection (GENSCAN) | $\sim$20 | first/last/middle exon, UTRs, introns 1/2/3, intergenic, $\pm$ strand | codons, nucleotides, splice sites, start/stop codons |
| Chromatin-state detection (ChromHMM) | 40 | enhancer / promoter / transcribed / repressed / repetitive | vector of chromatin-mark frequencies |

The training machinery of this chapter is exactly what fits each row: count directly when the
labels are known, run Baum-Welch when they are not. What grows with the state count is only the
number of parameters to estimate — which is precisely why overtraining becomes a live concern for
the ~20-state and 40-state models and was barely a concern for the 2-state one.

## Sources

- `05-slides/01-introduction.md` — the six-problem master table; the framing of learning via
  transition probability $P(P_{i+1}\mid B_i)$ and emission probability $P(S\mid B), P(S\mid P)$;
  the two learning scenarios (right answer known/unknown); the supervised MLE formulas; the labelled
  path/sequence counting setup; the overfitting example and its numbers; the pseudocount formulas;
  the CpG-island $+/-$ transition tables.
- `05-slides/02-learning-case-2-when-the-right-answer-is-unknown.md` — the case-2 framing (unknown
  path) and the repeated master table.
- `05-slides/03-simple-case-viterbi-training.md` — the Viterbi training algorithm and its three
  notes; the general EM shape and its formal E-step/M-step statement, including the pointer to
  SiPhy, $k$-means and motif finding elsewhere in the course; the Baum-Welch E-step derivation of
  the transition posterior via forward and backward variables; the M-step expected-count formulas;
  the multiple-sequence extension; the assembled Baum-Welch algorithm.
- `05-slides/04-the-baum-welch-algorithm-comments.md` — time complexity, the local-optimum caveat,
  and the overtraining warning.
- `05-slides/05-examples-of-hmms-for-genome-annotation.md` — the table of HMM applications at
  increasing state-space size (GC content through GENSCAN and ChromHMM).
- No transcript or handwritten notes were supplied for this lecture; the chapter is built from the
  slide deck alone. Where the slides set up an example but left it incomplete (the labelled
  path/sequence tally table on slide 1), that is noted rather than filled in.
- Named by the lecture but not covered in this material: SiPhy (Recitation 3), $k$-means clustering
  (Lecture 8), and motif finding (Lecture 9) — all cited as further applications of EM.
- The supplied problem set, `psets/05-questions.md` ("Problem Set 5: Clustering Phylogenetic
  Trees," on Robinson–Foulds distance and tree-cluster consensus, credited to Ran
  Libeskind-Hadas), does not test the HMM-training material in this lecture, so no Exercises
  section is included here.

---

[← 4. Recap: Markov Chains and HMMs](04-recap-markov-chains-and-hmms.md) · [Contents](index.md) · [6. Gene Expression Clustering and Classification →](06-gene-expression-clustering-and-classification.md)

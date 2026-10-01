---
title: "9. Sequence Motifs and the Gibbs Sampler"
course: "MIT 7.091J"
chapter: 9
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 9. Sequence Motifs and the Gibbs Sampler

## What this covers

A sequence motif is the pattern shared by a set of binding sites — a splice site, a transcription
factor's targets, a kinase's substrates. This chapter asks two questions about motifs: how do you
describe one precisely enough to score a candidate sequence against it, and how do you *find* one
when you are only given a pile of unaligned sequences and told "there is probably something common
to all of these"? The second question is answered with a worked algorithm, the Gibbs sampler, and
the chapter spends real time on *why* a procedure built entirely out of random choices nonetheless
converges on the right answer. It assumes you can read a probability as a product over independent
positions, and are comfortable with logarithms; nothing about hidden Markov models, which the course
takes up next, is needed here.

## What is a sequence motif, and where does it come from

A motif is a pattern common to a set of DNA, RNA or protein sequences that share a biological
property — for example, all of the binding sites of a particular transcription factor, or all the
peptides phosphorylated by a particular kinase. Four sources supply the sequences that go into
building one: sequences already known to share a function, cross-linking/pulldown experiments
(ChIP-seq), *in vitro* binding or SELEX experiments (incubate recombinant protein with a random
pool of sequences and pull down what binds), and comparative genomics — align orthologous
promoters and see which sub-region is conserved. A functional readout works too: clone random
sequences upstream of a reporter gene and see which ones drive expression.

Motifs matter because they let you go from a protein's identity to its targets, or from a gene's
promoter to the factors likely to regulate it — and any model of gene expression that wants to
predict what happens when a transcription factor is knocked down or over-expressed needs an
accurate description of where that factor binds.

## Representing a motif

There is a hierarchy of representations, each more expressive — and more work to fit — than the
last.

- **Consensus sequence.** The single most common base at each position, e.g. the TATA box,
  T-A-T-A-A-A. Cheap, but real instances are usually one or two mismatches away from it, so a
  consensus alone misses most of the true sites.
- **Regular expression.** The mammalian 5' splice site is often written GTR AGT, where R means "A
  or G". This captures a fixed degeneracy at each position but no graded preference.
- **Weight matrix** (position-specific probability matrix, PSPM, or position-specific score
  matrix, PSSM). A $4 \times w$ table of the frequency of each base at each of the $w$ positions of
  the motif. This is the standard description and the rest of the chapter is built on it.
- **More complex models**, which capture dependencies between positions that a weight matrix,
  which treats positions as independent, cannot — flagged in the lecture as increasingly necessary
  but not developed further here.

### Worked example: the 5' splice site

The boundary between an exon and the following intron has a reliable motif because the junction is
known exactly from aligning cDNA to genomic sequence: positions $-3$ to $-1$ are the last three
exonic bases, and $+1$ to $+6$ are the first six intronic bases (by convention numbered from $-3$,
not from $0$). Tallying bases at each position over many introns gives a weight matrix: position
$+1$ is G with probability $\approx 1$, $+2$ is T with probability $\approx 1$ (reflecting that
introns begin almost universally with GT), and the other positions show a graded preference. The
biological reason the motif exists at all: recognition here is not by a protein but by U1 snRNA,
part of which is complementary to the consensus splice site, so the site has evolved toward
sequence that pairs well with U1.

Given a weight matrix $\Theta$ for the motif and a background model $\theta_B$ (e.g. uniform
$1/4$ for each base, if the genome is taken to be unbiased), a candidate sequence
$S = S_1 S_2 \cdots S_9$ is scored by the **odds ratio**

$$R = \frac{P(S \mid +)}{P(S \mid -)} = \frac{\Theta_{-3}(S_1)\,\Theta_{-2}(S_2)\cdots\Theta_{+6}(S_9)}{\theta_B(S_1)\,\theta_B(S_2)\cdots\theta_B(S_9)}.$$

Multiplying probabilities position by position assumes the positions act independently — the key
assumption of a weight matrix. It need not assume the matrix is *homogeneous* (different columns
can have different probabilities), only that each column's contribution doesn't depend on the
others. Dividing by the background turns a raw probability — which is always some small number
like $1/4^9$ and awkward to compare across motifs — into a ratio that says directly how much more
like the motif, versus like background, a given sequence is.

## Measuring motif strength: entropy and information content

"Exact" versus "degenerate," "strong" versus "weak" are the everyday words for motif strength; a
restriction enzyme like EcoRI is exact (cuts only GAATTC), while a TATA-binding protein is
degenerate. Shannon's statistical entropy makes this precise.

For a probability vector $p = (p_k)$ over the four bases,

$$H(p) = -\sum_{k \in \{A,C,G,T\}} p_k \log_2 p_k,$$

in bits, using log base 2. $H$ is never negative, since $\log_2 p_k \le 0$ for $p_k \in (0,1]$. By
convention $0 \log_2 0 = 0$ (the limit of $x \log_2 x$ as $x \to 0$).

Four cases worked through in lecture fix the intuition:

- A deterministic position, $p = (0,1,0,0)$ (always C): $H = 0$. No uncertainty, no entropy.
- A uniform position, $p_k = 1/4$ for all $k$: $H = -4 \cdot \tfrac14\log_2\tfrac14 = 2$ bits.
- A coin flip between two bases, $p = (\tfrac12, 0, \tfrac12, 0)$: $H = 1$ bit.
- EcoRI's site, GAATTC, where each of the six positions is deterministic: entropy $0$ at every
  position.

$H(p) = \log_2(\Omega)$ when all $\Omega$ outcomes are equally likely recovers the Boltzmann
entropy $S = k_B \ln \Omega$ from statistical mechanics up to the choice of base and constant —
Shannon's quantity is a generalization of it, which is also the reason for the name: Shannon
wanted to call his measure of uncertainty "information," found the word already overused, settled
on "uncertainty," and von Neumann told him to call it entropy instead — "in the first place your
uncertainty function has been used in statistical mechanics under that name... in the second place,
and more important, nobody knows what entropy really is, so in a debate you will always have the
advantage."

**Information** is then defined as the reduction in uncertainty a motif model gives you over the
background: if a position is background (uniform, $H = 2$ bits) and the motif model there has
entropy $H_j$,

$$I_j = H_{\text{before}} - H_{\text{after}} = 2 - H_j,$$

and if positions in the motif are independent, the information content of the whole motif adds
over positions:

$$I_{\text{motif}} = \sum_{j=1}^w I_j = 2w - H_{\text{motif}}.$$

(This additivity is *only* guaranteed under independence; it is exactly the same independence
assumption the weight matrix already makes.) Checking the four cases above against a uniform
background: the uniform position has $I = 2-2=0$; the coin-flip position has $I = 2-1=1$ bit;
EcoRI, six independent deterministic positions, has $I = 2\cdot 6 - 0 = 12$ bits.

## The motif-finding problem

Given a weight matrix, scoring a candidate site is easy. The harder problem, and the one the rest
of the chapter is about, is **finding** the motif in the first place: given a set of unaligned
sequences believed to share some motif at an unknown position and of unknown exact composition,
recover the weight matrix and the locations. Posed this way it is a **local multiple alignment**
problem — the alignment need not be global, only over the motif-width sub-region — and a motif
that is weak and degenerate can be genuinely invisible by eye in the unaligned sequences while
becoming visible once the right positions are lined up.

Three families of approach:

- **Enumerative ("dictionary").** Fix a width $k$, enumerate all $4^k$ $k$-mers, count occurrences
  in a foreground set of sequences versus a background set, and look for statistical
  over-representation. Simple and widely used, but doing $4^k$ simultaneous statistical tests
  demands a multiple-testing correction that costs power, and a precise $k$-mer is the wrong tool
  for a degenerate motif — regular expressions generalize it somewhat.
- **Probabilistic optimization**, e.g. the Gibbs sampler: a stochastic search of the space of
  possible weight matrices.
- **Deterministic optimization**, e.g. MEME: a deterministic search of the same space, by
  expectation maximization.

<figure>
<svg viewBox="0 0 420 220" role="img" aria-label="A landscape over candidate motifs, with one tall peak at the true motif and several smaller decoy peaks nearby">
  <line x1="20" y1="190" x2="400" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <text x="210" y="210" text-anchor="middle" font-size="12" fill="currentColor">space of candidate motifs</text>
  <text x="14" y="30" text-anchor="end" font-size="12" fill="currentColor">strength</text>
  <path d="M 20 185
           C 50 182, 70 160, 95 175
           C 115 185, 130 150, 150 175
           C 165 188, 180 100, 205 40
           C 225 10, 235 10, 255 40
           C 275 100, 295 185, 310 175
           C 330 150, 345 180, 365 175
           C 380 170, 390 185, 400 185"
        fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M 20 185
           C 50 182, 70 160, 95 175
           C 115 185, 130 150, 150 175
           C 165 188, 180 100, 205 40
           C 225 10, 235 10, 255 40
           C 275 100, 295 185, 310 175
           C 330 150, 345 180, 365 175
           C 380 170, 390 185, 400 185
           L 400 190 L 20 190 Z"
        fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <text x="230" y="30" text-anchor="middle" font-size="12" fill="currentColor">true motif</text>
  <text x="130" y="145" text-anchor="middle" font-size="11" fill="currentColor">decoy</text>
  <text x="335" y="145" text-anchor="middle" font-size="11" fill="currentColor">decoy</text>
</svg>
<figcaption>If the landscape of candidate motifs has one dominant peak, a random search finds it
easily; the real difficulty is when weaker, only slightly enriched decoy motifs surround it, and a
search wandering at random can get stuck on one.</figcaption>
</figure>

## Monte Carlo and the Gibbs sampling algorithm

The Gibbs motif sampler is a **Monte Carlo algorithm**: one of a class of algorithms that use
repeated random sampling, and — in the stricter sense relevant here — a randomized algorithm using
bounded resources whose answer is not guaranteed correct every run. It is contrasted with a **Las
Vegas algorithm**, which always gives a correct result or reports failure. Running the Gibbs
sampler twice on the same input can give two different answers; this is the price of the method, not
a bug to be designed around.

The underlying model: $N$ sequences $\vec{s}$ are assumed each to contain one instance of a motif
of width $W$, at an unknown location recorded in the vector $\vec{A} = (A_1, \ldots, A_N)$. Outside
the motif, each position is generated from the background $\theta_B$; inside it, position $i$ of
the motif instance is generated from column $\Theta_i$ of the weight matrix. For sequence $k$,

$$P(\vec{s}, \vec{A} \mid \Theta, \theta_B) = \prod_k \theta_{B,S_{k,1}} \cdots \theta_{B,S_{k,A_k-1}} \;\Theta_{1,S_{k,A_k}} \Theta_{2,S_{k,A_k+1}} \cdots \Theta_{W,S_{k,A_k+W-1}}\; \theta_{B,S_{k,A_k+W}} \cdots \theta_{B,S_{k,L}}.$$

This is de novo motif finding: nothing about the motif's composition is assumed in advance, only a
guessed width $W$ (from structural knowledge if available, or just a guess — motifs are often
short, so 6 or 8 is a common starting guess).

**The algorithm**, given $N$ sequences of length $L$ and guessed width $W$:

1. Choose a starting position $a_k$ in each sequence $k$ uniformly at random (at least $W$ from the
   end, so a full motif fits).
2. Choose one sequence at random, say sequence 1.
3. Build a weight matrix of width $W$ from the motif instances currently assigned in every
   sequence *except* sequence 1.
4. Slide that weight matrix along sequence 1, and for every one of the $L-W+1$ possible starting
   positions compute the likelihood of generating that sub-sequence under the motif model versus
   the background model at every other position — i.e. an odds-ratio-like score at each position.
5. Normalize these scores to a probability distribution over positions, and *sample* a new starting
   position $a_1$ from it (not argmax — a weaker-scoring position can still be chosen).
6. Choose another sequence at random (say sequence 2), and repeat steps 3–5 for it, using the
   weight matrix built from every sequence except the one just chosen.
7. Iterate until convergence — either the sampled positions stop changing, or the weight matrix
   stops changing appreciably between full passes through the sequences.

### Why random sampling converges on the real motif

This is the question the lecture spends the most time on, because the mechanism is not obvious:
the algorithm never looks at "the answer," only ever re-scores one sequence at a time against a
matrix built from the current (possibly wrong) guesses in all the others. Walk through a concrete
case: 100 sequences of length 30, motif width 6, with a strong (12-bit, EcoRI-like) motif planted
at one position in every sequence. There are $L - W + 1 = 25$ possible start positions per
sequence.

In the very first round, starting positions are uniform at random, so on average the true motif is
hit in only $100/25 = 4$ of the 100 sequences — the rest are essentially random 6-mers. The weight
matrix built from this is therefore close to uniform, but not exactly: at the first motif position,
say the true motif prefers G, roughly 4 of the 96 "wrong" sequences will have a G there by chance in
addition to the 4 "right" sequences that actually have the motif, nudging that column's G frequency
from 25% to roughly 28%. The same slight nudge happens, independently, at each of the six columns.

Is that bias enough, on its own, to make the very next sampled sequence pick out the true motif
over the other 24 candidate positions? Essentially no: a $0.28/0.25$ advantage at each of 6
positions compounds to only around $(0.28/0.25)^6 \approx 1.9$ — not even twice as likely as any
one of the other 24 positions, so chance still dominates.

What actually happens, then, is a biased random walk in the matrix's **information content**. If
the sequence picked at a given step happens to land on the true motif, the matrix's bias toward it
strengthens a little; if it lands elsewhere, the matrix drifts back toward uniform (zero
information). Plotted against iteration, information content therefore starts near zero and
fluctuates — sometimes rising a little, sometimes falling back — for a long time. But once a lucky
run of draws pushes the bias far enough that the motif's likelihood is, say, twenty times any
competing position's, the sampler picks the true motif *almost every time it is offered*, and each
correct pick strengthens the matrix further, which makes the next pick even more likely to be
correct. The result is a climb that looks flat for a long stretch and then rises sharply once a
threshold is crossed — "stumbling onto a few instances that bias the matrix, which then samples
more instances, which biases it more" (summarized in the slides). The algorithm is not directly
optimizing information content — nothing in its five steps mentions $I_{\text{motif}}$ — but the
sampling procedure has this increase as a side effect, because a matrix closer to the truth makes
the truth more likely to be resampled.

The demonstration run in lecture, with a strong planted motif, showed exactly this: a weight matrix
that starts looking essentially random, and after on the order of 100 iterations is strongly biased
toward the correct sequence and position, with the per-sequence location-probability display
(white = high, black = low) showing confident single peaks. A second run on a *weak* motif (several
sequences sharing only a loose GGC-like pattern, invisible unless pre-aligned) failed to fully
converge: the sampler locked onto a near-miss (GAGC instead of GGC in one column), because by chance
some non-motif positions looked enough like the real motif to compete with it, and the
location-probability display showed multiple competing bright spots per sequence rather than one —
visible uncertainty that never resolved.

## Features that affect whether motif finding succeeds

- **Information content of the true motif.** High-information (strong, near-deterministic) motifs
  are much easier to find: once stumbled upon, they bias the matrix sharply and convergence is
  fast. Low-information (weak, near-uniform) motifs give only a feeble signal to climb and the
  sampler may never clear the threshold.
- **Length of the sequences searched.** Shorter is better — fewer possible positions per sequence
  means less "room to hide," so a given motif instance is more likely to be sampled. Restricting
  a search for TATA to a 50-base window near a known transcription start site works far better than
  searching a 2000-base promoter.
- **Number of sequences.** More is generally better — more total opportunities to stumble onto a
  true instance — though it also changes convergence time and is subtler than it looks: cutting the
  number of sequences to speed convergence risks never finding the motif at all.
- **Match between guessed and true motif width.** The slides list the match between the
  expected and the actual length of the motif as a factor in whether the search succeeds; the
  lecture does not work through its effect.
- **Shifted motifs.** If, by chance, several sequences are first sampled at a position offset by a
  fixed number of bases from the true motif, the matrix locks onto that offset version — a real but
  wrong local optimum, less information-rich than the true motif (because the positions that would
  have been informative now fall outside the window and show up as noise). A practical fix:
  periodically test whether shifting every current assignment left or right by one or two bases
  would increase the matrix's information content, and take the shift if so.
- **Biased background composition** (e.g. a genome that is 80% A+T) is flagged as a hard case
  in general, and is addressed directly by relative entropy, below.

## Deterministic optimization: MEME

MEME runs essentially the same scoring step as the Gibbs sampler — score every candidate position
against a weight matrix built from the rest of the data — but instead of sampling a new position
proportional to its score, it deterministically takes the single highest-scoring position every
time (an instance of expectation maximization). The appeal is obvious: the answer does not depend
on a random seed, so running MEME once is enough. The cost is that *where you start* matters a
great deal, since a deterministic update has no mechanism for climbing back out of a wrong but
self-reinforcing matrix — a slight, essentially accidental bias in the initial matrix becomes a
self-fulfilling prophecy. MEME compensates by trying many different deterministic starting points
and keeping the one that scores best at the end, which costs more computation per run but removes
the need for multiple runs. The Gibbs sampler avoids this trap precisely because its randomness lets
it fall back off a weak, wrong optimum and re-explore, rather than committing to the first biased
matrix it builds.

## Scoring with a biased background: mean bit-score and relative entropy

Once a motif model $p$ and background $q$ are both known, an additive (rather than multiplicative)
score for a candidate sequence is the log-odds, $\log_2(p_k/q_k)$ summed over the sequence, which
is what a weight matrix typically stores directly. Averaging this score over instances drawn from
the motif model gives the **mean bit-score**:

$$\text{mean bit-score} = \sum_{k=1}^n p_k \log_2\!\left(\frac{p_k}{q_k}\right), \qquad n = 4^w.$$

When the background is uniform, $q_k = 1/4^w$, this reduces algebraically to
$2w - H_{\text{motif}} = I_{\text{motif}}$ — the same information content defined earlier. (The
professor left the algebra connecting the two as a short exercise, below.)

**Why information content is useful at all**: a rule of thumb (strictly true for a motif
describable as a precise regular expression, only approximately true for a general weight matrix)
is that a motif with $m$ bits of information occurs about once every $2^m$ bases of random
sequence. EcoRI's site, at 12 bits, should then occur about once every $2^{12} = 4096$ bases —
close to the roughly 4 kb fragment sizes actually seen when EcoRI is used to cut *E. coli* DNA.

When the background is *not* uniform, the mean bit-score is no longer equal to
$H_{\text{before}} - H_{\text{after}}$, and the two measures can disagree about which motif is
"stronger." In that case the mean bit-score is called **relative entropy** (also Kullback-Leibler
distance, or information for discrimination):

$$D(p \parallel q) = \sum_k p_k \log_2\!\left(\frac{p_k}{q_k}\right).$$

Worked example: take a background with $q_A = q_T = 3/8$, $q_C = q_G = 1/8$ (a 75% A+T genome), and
a motif that is deterministically C ($p_C = 1$). The original information-content formula gives
$H(q) - H(p) < 2$ bits. But relative entropy gives $D(p\|q) = \log_2(1/(1/8)) = 3$ bits. Since C is
a rare base in this background, a motif that is reliably C is in fact *stronger* evidence of a real
binding preference than the uniform-background formula credits it with — relative entropy is the
better measure of how surprising, and hence how informative, the motif really is when the
background itself is skewed.

## Exercises

1. Starting from the mean bit-score, $\displaystyle\sum_{k=1}^n p_k \log_2(p_k/q_k)$, and assuming
   a uniform background over $w$-mers, $q_k = 1/4^w$ for all $k$, show algebraically that this
   quantity equals $2w - H_{\text{motif}}$, i.e. that it coincides with the information content
   $I_{\text{motif}}$ defined from $H_{\text{before}} - H_{\text{after}}$.
2. For the restriction site recognized by a four-cutter (a precise 4-base motif) and by an
   eight-cutter (a precise 8-base motif), each against a uniform background, give the information
   content of each in bits, and use the rule of thumb (a motif with $m$ bits of information occurs
   about once every $2^m$ bases) to estimate how far apart, on average, each enzyme's sites fall in
   random sequence.

## Sources

- Slides: `lectures/09-slides/01-modeling-discovery-of-sequence-motifs.md` — definitions of a
  motif, sources and importance, examples (zinc finger, phosphorylation site, splice sites), the
  weight-matrix-with-background odds-ratio formula, Shannon entropy and information content
  slides, the Shannon/von Neumann anecdote.
- Slides: `lectures/09-slides/02-the-motif-finding-problem.md` — the unaligned/aligned sequence
  example, the three approaches to motif finding, Monte Carlo vs. Las Vegas definitions, the Gibbs
  sampler likelihood function and algorithm-in-words steps, the Gibbs summary slide, features
  affecting motif finding, MEME and WebMotifs references, mean bit-score and relative entropy
  slides (including the worked $q_A=q_T=3/8$ example).
- Transcript: `recordings/lectures/09.md` (C. Burge, Mar. 6 2014) — opening administrative remarks
  stripped. Motivation and examples for motif sources (0:00–13:00); the worked weight-matrix/odds
  ratio walkthrough for the 5' splice site (13:00–19:00); the entropy worked examples with student
  answers (20:00–32:00); the motif-finding problem and landscape analogy (32:00–39:00); the full
  Gibbs sampler walkthrough and class discussion of why it converges, including the 100-sequence/
  width-6 worked numerical example (39:00–1:05:00); the strong- and weak-motif demonstration runs
  (47:00–1:07:00); MEME comparison (1:07:00–1:10:00); features affecting motif finding and shifted
  motifs (1:10:00–1:15:00); mean bit-score, the EcoRI rule-of-thumb check, and relative entropy
  (1:15:00–1:21:16).
- Referred to but not contained in the supplied material: the NBT primers on motifs and motif
  discovery, Zvelebil & Baum (Z&B) Ch. 6, Lawrence et al., *Science* 1993 (the original Gibbs
  sampler paper), Bailey & Elkan 1995 (the MEME paper), the Fraenkel lab's WebMotifs
  (`fraenkel.mit.edu/webmotifs.html`) and Romer et al., and T. Cover, *Elements of Information
  Theory* — none of these were supplied as source files for this chapter.

---

[← 8. RNA-seq, Isoforms, and Expression Statistics](08-rna-seq-isoforms-and-expression-statistics.md) · [Contents](index.md) · [10. Markov and Hidden Markov Models →](10-markov-and-hidden-markov-models.md)

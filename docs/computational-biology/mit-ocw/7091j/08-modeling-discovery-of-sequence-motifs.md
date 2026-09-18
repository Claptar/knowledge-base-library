---
title: "8. Modeling & Discovery of Sequence Motifs"
course: "MIT 7.091J"
chapter: 8
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 8. Modeling & Discovery of Sequence Motifs

## What this covers

A regulatory protein does not bind one exact DNA sequence; it binds a family of related
sequences with a shared statistical pattern. This chapter asks two questions about that pattern:
how do you write it down and measure how strong it is, and, given a pile of sequences that share
an unknown pattern, how do you find it? It assumes only that you are comfortable with basic
probability (frequencies, independence, log-likelihood ratios) and know what a DNA or protein
sequence is; no prior exposure to information theory or to Monte Carlo methods is assumed.

## What a sequence motif is

A **sequence motif** is a pattern common to a set of DNA, RNA or protein sequences that share a
common biological property — most often, that they are all binding sites for the same protein.
The same pattern can be written down in several ways, in increasing order of how much information
they keep:

- a **consensus sequence** — the single most typical string (e.g. the majority base at each
  position),
- a **regular expression** — a pattern with wildcards and character classes,
- a **weight matrix** (also called a position-specific probability matrix, PSPM, or, once turned
  into log-odds scores, a position-specific scoring matrix, PSSM) — a full probability distribution
  over bases at each position,
- or a more elaborate model still (e.g. one with dependencies between positions).

Motifs are discovered from several kinds of evidence: sequences already known to share a function,
cross-linking/pulldown experiments, *in vitro* binding assays such as SELEX, and multiple sequence
alignments or comparative genomics. They matter because a motif lets you identify proteins, DNA or
RNA elements with a given property, infer which regulatory factors act on which genes, and build
models of gene expression.

Two worked examples of protein motifs from the lecture: the zinc finger DNA-binding domain, written
as the regular expression $\text{CX}_2\text{CX}_4\text{HX}_4\text{C}$ (Ericsson et al., *Genet.
Mol. Res.* 2006), and phosphorylation sites in the *Arabidopsis* kinase SRPK4 (de la Fuente van
Bentem et al., *NAR* 2006). On the nucleic-acid side, the three core human splicing signals — the
5' splice site, the branch site and the 3' splice site — are motifs of exactly this kind, and the
5' splice site is the running example below.

## Scoring a candidate site against the background

A weight matrix only means something in contrast to a null model of "ordinary" sequence — the
**background model**. For the 5' splice site (a 9-base window, positions $-3$ to $+6$ around the
exon–intron boundary), the lecture's toy weight matrix gives, e.g., $P_{-2}(A) = 0.6$ and
$P_{+6}(T) = 0.5$, while the background model used here is the simplest possible one: uniform and
position-independent, $P_{\text{bg}}(A) = P_{\text{bg}}(C) = P_{\text{bg}}(G) = P_{\text{bg}}(T) =
0.25$ everywhere.

Given a candidate 9-mer $S = S_1 S_2 \cdots S_9$, the natural question is which model generated it.
That is a likelihood ratio, the **odds ratio**:

$$R = \frac{P(S \mid +)}{P(S \mid -)} = \frac{P_{-3}(S_1)\,P_{-2}(S_2)\,P_{-1}(S_3) \cdots
P_{5}(S_8)\,P_{6}(S_9)}{P_{\text{bg}}(S_1)\,P_{\text{bg}}(S_2)\,P_{\text{bg}}(S_3) \cdots
P_{\text{bg}}(S_8)\,P_{\text{bg}}(S_9)}$$

Both the numerator and denominator factor into a product over positions — that is the assumption
that positions are independent given the class (motif or background), and that the background is
homogeneous (the same distribution at every position). It is a strong assumption, and it is the
one that makes the arithmetic below work; the lecture flags explicitly that the identities that
follow from it fail once positions are correlated.

## Measuring how strong a motif is

Motifs get described with a stock set of adjectives: exact/precise versus degenerate, strong
versus weak, high versus low information content, low versus high entropy. The last two pairs are
the same idea made quantitative, via Shannon entropy.

### Shannon entropy

For a distribution over the four bases, $p_k$ for $k \in \{A,C,G,T\}$, the **Shannon entropy** is

$$H(p) = -\sum_{k} p_k \log_2 p_k.$$

Logs base 2 make the units "bits". For the uniform background, $q_k = 1/4$ for all $k$,

$$H(q) = -4 \cdot \tfrac14 \log_2 \tfrac14 = -\log_2 \tfrac14 = 2 \text{ bits},$$

which is the maximum possible entropy of a 4-letter alphabet: total uncertainty about which base
comes next. Any motif distribution $p$ that is *not* uniform — any position where the protein
prefers some bases over others — has $H(p) < H(q)$: entropy falls exactly to the extent that the
distribution departs from uniform.

The name "entropy" for this quantity is a historical accident worth knowing, because it is the
reason the same word covers both a communication-theory quantity and a physical one
($S = k_B \ln \Omega$ in statistical mechanics). Shannon himself recalled being unsure what to call
his "measure of uncertainty":

> "My greatest concern was what to call it. I thought of calling it 'information', but the word
> was overly used, so I decided to call it 'uncertainty'. When I discussed it with John von
> Neumann, he had a better idea. Von Neumann told me, 'You should call it entropy, for two reasons.
> In the first place your uncertainty function has been used in statistical mechanics under that
> name, so it already has a name. In the second place, and more important, nobody knows what
> entropy really is, so in a debate you will always have the advantage.'" (1949; via Wikipedia)

### Information content

A motif position that is *low* entropy is *high* information: knowing you are looking at a real
binding site tells you a lot about what base sits there, compared to the 2 bits of total ignorance
you'd have for a random background base. Define the **information content at position $j$** as the
reduction in entropy from background to motif:

$$I_j = H_{\text{before}} - H_{\text{after}} = H(q) - H(p_j) = 2 - H_j \text{ bits}.$$

If the positions of the motif are independent of one another, the per-position information adds up:

$$I_{\text{motif}} = \sum_{j=1}^{w} I_j = 2w - H_{\text{motif}}$$

for a motif of width $w$ bases — $2w$ bits being the maximum possible (total certainty at every
position), minus however much entropy remains. As with the odds ratio, this additivity is a
consequence of the independence assumption and does not hold in general once positions are
correlated.

### Mean bit-score and a rule of thumb

The same quantity reappears as a **mean log-odds (bit-) score**. For a single $w$-mer $S$, the
bit-score is $\log_2(p_S/q_S)$; averaging over the motif's own distribution,

$$\text{mean bit-score} = \sum_{k=1}^{n} p_k \log_2\!\left(\frac{p_k}{q_k}\right), \qquad n = 4^w.$$

If the background over $w$-mers is uniform, $q_k = 1/4^w$, this again equals $2w - H_{\text{motif}}
= I_{\text{motif}}$: the same number under three names (information content, relative entropy,
mean bit-score) as long as the background is uniform.

Why bother computing it? A useful **rule of thumb**: a motif carrying $m$ bits of information will
occur roughly once every $2^m$ bases of random sequence (exactly true for a regular
expression/exact motif, only approximately true for a general weight-matrix motif). This is what
turns "information content" into something practical: it tells you how surprised to be by a match,
and hence how large a genome you can search before random noise starts producing look-alikes.

### Relative entropy, and why it beats $H_{\text{before}} - H_{\text{after}}$ for a biased background

Writing the mean bit-score as $D(p \parallel q) = \sum_k p_k \log_2(p_k/q_k)$ makes it recognisable
as the **relative entropy** (also called Kullback-Leibler divergence, or "information for
discrimination") between the motif distribution $p$ and *whatever* background $q$ actually is. It
agrees with $I_{\text{motif}} = 2w - H_{\text{motif}}$ only when $q$ is uniform. Once the real
background is not uniform, relative entropy is the better measure of information, because
$H_{\text{before}} - H_{\text{after}}$ throws away the information about *which* bases the
background favours.

Here is the lecture's example. Suppose the true background is AT-rich rather than uniform:
$q_A = q_T = 3/8$, $q_C = q_G = 1/8$. Its entropy is

$$H(q) = -2\left(\tfrac38 \log_2 \tfrac38\right) - 2\left(\tfrac18 \log_2 \tfrac18\right)
\approx 2(0.531) + 2(0.375) \approx 1.81 \text{ bits},$$

already a bit below 2 simply because the background itself is skewed. Now suppose a motif position
is *completely* determined to be C: $p_C = 1$, so $H(p) = 0$ and $H(q) - H(p) \approx 1.81 < 2$
bits. But the relative entropy is

$$D(p \parallel q) = \log_2\!\left(\frac{1}{1/8}\right) = 3 \text{ bits},$$

noticeably larger. Which number is right? Relative entropy is: fixing the position to C is far more
surprising, and far more informative, against a background where C is rare (probability $1/8$)
than the $H_{\text{before}} - H_{\text{after}}$ calculation suggests, because that calculation only
compares *total* uncertainty before and after and never asks which particular base got favoured
relative to how common it already was. Relative entropy asks exactly that, which is why it is the
right tool once the background composition is not flat.

## The motif-finding problem

Everything so far assumed you already had the weight matrix. In practice you are handed a set of
sequences believed to share a functional element — a promoter region upstream of co-regulated
genes, say — with no idea where in each sequence the shared element sits, or even exactly what it
looks like. The lecture's example is a set of roughly 40-base sequences such as

```
agggcactagcccatgtgagagggcaaggaccagcggaag
taattcagggccaggatgtatctttctcttaaaaataaca
tatcctacagatgatgaatgcaaatcagcgtcacgagctt
...
```

and the point of showing them next to a re-shuffled version of themselves — each sequence cut and
rotated so that a shared block of letters lines up in the same columns —

```
gcggaagagggcactagcccatgtgagagggcaaggacca
atctttctcttaaaaataacataattcagggccaggatgt
gtcacgagctttatcctacagatgatgaatgcaaatcagc
...
```

is that **motif finding can be posed as an alignment problem**: find, for each sequence, the offset
at which a shared window starts, so that lining every sequence up at its own offset produces a
block in which the columns look like a weight matrix rather than like background. The catch,
unlike ordinary multiple sequence alignment, is that the offsets are exactly what's unknown.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="Five sequences with a shared motif at different unknown offsets, and the same sequences after shifting each one so the motif lines up in one column">
 <text x="70" y="14" text-anchor="middle" font-size="12" fill="currentColor">unaligned</text>
 <text x="285" y="14" text-anchor="middle" font-size="12" fill="currentColor">aligned</text>
 <g stroke="currentColor" stroke-width="1.2" fill="none">
  <rect x="10" y="24" width="120" height="14"/>
  <rect x="10" y="54" width="120" height="14"/>
  <rect x="10" y="84" width="120" height="14"/>
  <rect x="10" y="114" width="120" height="14"/>
  <rect x="10" y="144" width="120" height="14"/>
 </g>
 <g fill="currentColor" fill-opacity="0.3" stroke="currentColor" stroke-width="1">
  <rect x="95" y="24" width="20" height="14"/>
  <rect x="25" y="54" width="20" height="14"/>
  <rect x="65" y="84" width="20" height="14"/>
  <rect x="105" y="114" width="20" height="14"/>
  <rect x="45" y="144" width="20" height="14"/>
 </g>
 <g stroke="currentColor" stroke-width="1.2" fill="none">
  <rect x="220" y="24" width="120" height="14"/>
  <rect x="220" y="54" width="120" height="14"/>
  <rect x="220" y="84" width="120" height="14"/>
  <rect x="220" y="114" width="120" height="14"/>
  <rect x="220" y="144" width="120" height="14"/>
 </g>
 <g fill="currentColor" fill-opacity="0.3" stroke="currentColor" stroke-width="1">
  <rect x="260" y="24" width="20" height="14"/>
  <rect x="260" y="54" width="20" height="14"/>
  <rect x="260" y="84" width="20" height="14"/>
  <rect x="260" y="114" width="20" height="14"/>
  <rect x="260" y="144" width="20" height="14"/>
 </g>
 <defs>
  <marker id="arrow-motif" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
   <polygon points="0 0, 6 3, 0 6" fill="currentColor"/>
  </marker>
 </defs>
 <line x1="140" y1="84" x2="210" y2="84" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow-motif)"/>
 <text x="175" y="78" text-anchor="middle" font-size="11" fill="currentColor">shift each row</text>
 <text x="175" y="200" text-anchor="middle" font-size="12" fill="currentColor">shaded = the motif's unknown location per sequence</text>
</svg>
<figcaption>The motif-finding problem as an alignment problem: the shaded window is the same
motif in every row, but at a different, unknown offset; finding the motif means finding the
offsets that bring the shaded windows into register.</figcaption>
</figure>

## Three approaches to motif finding

The lecture groups algorithms for this problem into three families:

- **Enumerative ("dictionary") search** — enumerate $k$-mers, or sets of $k$-mers, or regular
  expressions, and test each for statistical over-representation in the sequence set.
- **Probabilistic optimisation**, e.g. the **Gibbs sampler** — a stochastic search through the
  space of possible weight matrices (PSPMs).
- **Deterministic optimisation**, e.g. **MEME** — a deterministic search of the same space, using
  expectation-maximisation rather than random sampling.

The rest of the chapter works through the probabilistic route in detail, since it is the one the
lecture develops as a worked algorithm.

## Monte Carlo and Las Vegas algorithms

The Gibbs motif sampler is a **Monte Carlo algorithm** — in general, any class of algorithm that
relies on repeated random sampling to compute its result. More precisely: a randomised algorithm
whose resource use is bounded, but whose answer is *not* guaranteed correct every time it runs. It
is worth contrasting this with a **Las Vegas algorithm**, a randomised algorithm that always gives
a correct result, or explicitly reports failure — a guarantee Monte Carlo methods like Gibbs
sampling do not offer. As will show up below, this distinction is exactly the caveat attached to
the Gibbs sampler's output: it converges, but not necessarily to the true motif, and not
necessarily to the same one on two different runs.

## The Gibbs motif sampler

The method is due to Lawrence et al., *Science* 1993. It treats the data generatively: each of $N$
sequences is ordinary background sequence, *except* for one width-$W$ window per sequence, which
was drawn from the motif model instead. If sequence $k$'s window starts at (unknown) position
$A_k$, and $\Theta_1, \ldots, \Theta_W$ are the motif's position-specific base probabilities while
$\theta_B$ is the background model, the likelihood of everything (sequences and motif locations)
given the models is

$$P(\vec{s}, \vec{A} \mid \Theta, \theta_B) = \prod_k \theta_{B,S_{k,1}} \times \cdots \times
\theta_{B,S_{k,A_k-1}} \times \Theta_{1,S_{k,A_k}} \times \Theta_{2,S_{k,A_k+1}} \times \cdots \times
\Theta_{W,S_{k,A_k+W-1}} \times \theta_{B,S_{k,A_k+W}} \times \cdots \times \theta_{B,S_{k,L}}.$$

In words: for each sequence, multiply the background probability of every base before the motif
window, the motif's position-specific probabilities across the window itself, and the background
probability of every base after it. Neither $\Theta$ nor $\vec{A}$ is known; the algorithm searches
for both jointly by alternating between them.

### The algorithm

Given $N$ sequences of length $L$ and a chosen motif width $W$:

1. Pick a starting position $a_1, \ldots, a_N$ at random in each sequence.
2. Pick one sequence at random to leave out (say, sequence 1).
3. Build a weight matrix of width $W$ from the current sites in *every other* sequence.
4. Score every one of the $L - W + 1$ possible window positions in the held-out sequence against
   that weight matrix, giving a distribution $p = \{p_1, \ldots, p_{L-W+1}\}$ over positions.
5. Sample a new starting position $a_1$ for the held-out sequence from this distribution.
6. Pick another sequence at random to leave out (say, sequence 2), and repeat steps 3–5 for it.
7. Continue, choosing a new sequence to hold out each round, until convergence — either the sites
   stop moving ($\Delta\text{sites} = 0$) or the weight matrix stops changing ($\Delta\Theta \approx
   0$).

Each round is a leave-one-out step: build the current best guess at the motif from everyone else's
current sites, then let the held-out sequence vote on where it thinks the motif is, weighted by how
well each candidate window matches.

<figure>
<svg viewBox="0 0 360 260" role="img" aria-label="The Gibbs sampler as a cycle of four steps repeated until convergence">
 <defs>
  <marker id="arrow-gibbs" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
   <polygon points="0 0, 6 3, 0 6" fill="currentColor"/>
  </marker>
 </defs>
 <g fill="none" stroke="currentColor" stroke-width="1.3">
  <rect x="20" y="30" width="140" height="50" rx="4"/>
  <rect x="200" y="30" width="140" height="50" rx="4"/>
  <rect x="200" y="170" width="140" height="50" rx="4"/>
  <rect x="20" y="170" width="140" height="50" rx="4"/>
 </g>
 <g font-size="11" fill="currentColor" text-anchor="middle">
  <text x="90" y="51">hold out one</text>
  <text x="90" y="65">sequence</text>
  <text x="270" y="51">build weight matrix</text>
  <text x="270" y="65">from the other N-1</text>
  <text x="270" y="191">score every window in</text>
  <text x="270" y="205">the held-out sequence</text>
  <text x="90" y="191">sample a new site</text>
  <text x="90" y="205">proportional to score</text>
 </g>
 <line x1="160" y1="55" x2="195" y2="55" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow-gibbs)"/>
 <line x1="270" y1="85" x2="270" y2="165" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow-gibbs)"/>
 <line x1="195" y1="195" x2="165" y2="195" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow-gibbs)"/>
 <line x1="90" y1="165" x2="90" y2="85" stroke="currentColor" stroke-width="1.3" marker-end="url(#arrow-gibbs)"/>
 <text x="180" y="245" text-anchor="middle" font-size="12" fill="currentColor">repeat, with a new sequence held out each time, until convergence</text>
</svg>
<figcaption>One round of the Gibbs motif sampler: leave a sequence out, build the current motif
model from the rest, score the held-out sequence against it, and resample its site — then move to
a different held-out sequence and repeat.</figcaption>
</figure>

### Why it converges to a motif at all

The intuitive argument (the lecture calls this out explicitly): the algorithm works by
**stumbling** onto a few true motif instances early on, purely by chance in the random starting
positions. Those few correct instances bias the weight matrix built in step 3 toward the real
motif; a weight matrix closer to the real motif scores real motif instances in the held-out
sequence more highly, so step 5 is more likely to sample another correct site; more correct sites
bias the weight matrix further still — and so on, until the process settles down. Restated in terms
of the likelihood: each resampling step tends to increase $P(\vec{s}, \vec{A} \mid \Theta,
\theta_B)$, so the procedure is, loosely, climbing the likelihood surface defined by that formula
toward higher-probability configurations of sites and motif model together.

What it does *not* do is guarantee reaching the best configuration. Because the search is
stochastic, it is **not guaranteed to converge to the same motif on two different runs** — the
standard practice is to run the sampler several times from different random starts and compare (or
pool) the results. Subject to that caveat, the same scheme applies unchanged to DNA, RNA or protein
motifs, since nothing in steps 1–7 is specific to a 4-letter alphabet.

## What makes a motif easy or hard to find

Several factors set how well any of the above methods will do, all pointing back to the
information-content idea from earlier in the chapter:

- **Number of sequences** — more instances of the true motif to "stumble" onto and to build a
  reliable weight matrix from.
- **Length of the sequences** — longer sequences mean more background positions competing to look
  like a motif by chance.
- **Information content of the motif** — by the rule of thumb above, a motif with only a few bits
  of information is expected once every few dozen bases even in pure background, so it is
  statistically hard to tell apart from noise; a high-information motif stands out.
- **Match between the assumed motif width and its true width** — a weight matrix built at the
  wrong width cannot represent the real pattern well, whatever the search strategy.

Two specific failure modes named in the lecture: **shifted motifs**, where the algorithm converges
on a version of the true motif offset by a few bases from its actual position, and **biased
background composition**, where using the wrong (e.g. uniform) background model when the true
background is skewed distorts scoring — exactly the situation the relative-entropy example above
was built to illustrate.

## Practical tools

- **MEME** (Bailey & Elkan, 1995) is the classic deterministic alternative to Gibbs sampling: same
  underlying generative motif model, but fit by expectation-maximisation instead of stochastic
  search.
- The Fraenkel lab's **WebMotifs** runs several motif finders together — AlignACE (a method similar
  in spirit to Gibbs sampling), MDscan, MEME, Weeder and THEME — described in Romer et al.

## Sources

Both files are the reconstructed markdown of C. Burge's Lecture 9 slide deck ("7.91J/20.490J/
6.874J/HST.506J, 7.36J/20.390J/6.802J: Foundations of Computational and Systems Biology", Spring
2014, MIT OpenCourseWare, 6 March 2014), split across two source files:

- `lectures/09-slides/01-modeling-discovery-of-sequence-motifs.md` — motif definitions,
  representations, sources and importance of motifs, the zinc-finger and phosphorylation-site
  examples, the splicing-motif slide, the weight-matrix/odds-ratio slide, and the entropy /
  information-content slides (including the Shannon–von Neumann quotation, sourced on the slide to
  Wikipedia).
- `lectures/09-slides/02-the-motif-finding-problem.md` — the unaligned/aligned sequence table, the
  three approaches to motif finding, the Monte Carlo/Las Vegas distinction, the Gibbs sampler
  likelihood function and ten-step algorithm (Lawrence et al., *Science* 1993), the summary and
  "what does this accomplish" slides, the features/issues list, the MEME and WebMotifs pointers,
  and the mean bit-score / relative-entropy slides at the end of the deck.

No transcript, notes or exercise set was supplied for this lecture, so the chapter follows the
slides' own reasoning and examples without added worked problems; there is accordingly no
Exercises section.

Both source files carry their own fidelity note worth repeating here: they were reconstructed by a
model from a PDF with no text layer, and every equation in them is marked **unverified** by the
conversion process. This chapter reproduces those equations as given and does not independently
re-derive or check them against the Lawrence et al. 1993 or Bailey & Elkan 1995 papers.

Named but not contained in the supplied material (referred to by the slides but not available to
adapt from): the NBT primers on motifs and on motif discovery; Z&B (Zvelebil & Baum) Ch. 6; the
Lawrence et al. *Science* 1993 Gibbs sampler paper and the Bailey & Elkan 1995 MEME paper
themselves (only cited, not included); Romer et al. on WebMotifs; T. Cover's *Elements of
Information Theory* (pointed to for more on information theory); and the figures for several
slides that had no text content in this reconstruction — the core splicing motif diagrams, the
"motif landscape" figure, the step-by-step Gibbs sampler diagrams (Algorithm I–VII), and the
strong/weak motif example result screenshots. The lecture's own forward pointer to "For Tuesday"
(NBT primer and Z&B on HMMs, the Rabiner HMM tutorial) marks the next lecture's material and is out
of scope here.

---

[← 7. ChIP-seq Peak Calling and Reproducibility](07-chip-seq-peak-calling-and-reproducibility.md) · [Contents](index.md) · [9. Hidden Markov Models of Sequences →](09-hidden-markov-models-of-sequences.md)

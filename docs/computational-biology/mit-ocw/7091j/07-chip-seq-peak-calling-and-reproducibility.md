---
title: "7. ChIP-seq Peak Calling and Reproducibility"
course: "MIT 7.091J"
chapter: 7
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 7. ChIP-seq Peak Calling and Reproducibility

## What this covers

How do you turn raw ChIP-seq reads into a list of transcription-factor binding sites you can
trust? This chapter follows one answer end to end: a generative model of where sequencing reads
land around a binding event (GPS), the statistical test used to decide whether a candidate event
is more than background noise, a method for deciding which events replicate across two independent
experiments (the Irreproducible Discovery Rate), and an extension that folds DNA sequence motifs
into the same model (GEM). It closes with what happens when you ask whether binding events are
conserved across species. It assumes you already know what a transcription factor is, what
ChIP-seq measures, and the mechanics of the EM algorithm (E-step responsibilities, M-step
re-estimation) — the chapter uses EM as a tool rather than re-deriving it.

## The problem: reads, not binding sites

A transcription factor is a protein that binds specific DNA sequences and switches genes on or
off; a human cell has on the order of 2000 of them. ChIP-seq is the standard assay for finding
*where* a given factor binds, genome-wide: crosslink proteins to DNA in living cells, fragment the
chromatin, pull down the fragments bound by the factor of interest using an antibody, and sequence
both that enriched sample and a whole-cell-extract (WCE) control.

What comes out of the sequencer is not a binding site — it is millions of short reads, each the end
of a random DNA fragment that happened to be pulled down. A single true binding event does not
produce one read at one position; it produces a *distribution* of reads scattered around it, because
the crosslinked fragments are cut at random lengths and only one end of each fragment is sequenced.
Two consequences follow immediately. First, recovering the binding position from the read pileup is
an inference problem, not a lookup. Second, when two binding events sit close together the reads
from both mix together, and separating them means fitting more than one event to the same pile of
reads.

## What a single binding event looks like in the data

Reads on the two DNA strands behave differently. A fragment sequenced from its "+ strand" end
reports a position on one side of the true binding site; a fragment sequenced from its "− strand"
end reports a position on the other side. So a single binding event produces not one peak but two,
straddling the true site — a forward-strand pile and a reverse-strand pile, offset from each other.

<figure>
<svg viewBox="0 0 400 220" role="img" aria-label="Reads from the two strands form two offset piles straddling a single binding event">
  <line x1="20" y1="180" x2="380" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="200" y1="20" x2="200" y2="180" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <path d="M 90 180 Q 140 40 190 180 Z" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <path d="M 210 180 Q 260 40 310 180 Z" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <text x="140" y="35" text-anchor="middle" font-size="12" fill="currentColor">+ strand reads</text>
  <text x="260" y="35" text-anchor="middle" font-size="12" fill="currentColor">&#8722; strand reads</text>
  <text x="200" y="200" text-anchor="middle" font-size="12" fill="currentColor">binding site $b_j$</text>
  <text x="370" y="200" text-anchor="end" font-size="12" fill="currentColor">position</text>
</svg>
<figcaption>A single binding event does not produce a single peak of reads: forward- and
reverse-strand reads pile up on opposite sides of the true site, mirror images of one another.</figcaption>
</figure>

GPS (the model this lecture builds up) fits this shape directly rather than assuming reads cluster
symmetrically at one point. Write $r_i$ for the position of read $i$, $b_j$ for the position of
candidate binding event $j$, and let $S_i = 0$ if read $i$ is on the forward strand and $S_i = 1$ if
it is on the reverse strand. Then

$$p(r_i \mid b_j) = p(r_i \mid z_{ij} = 1) = \text{emp}\big((-1)^{S_i}(r_i - b_j)\big),$$

where $\text{emp}(d)$ is a single empirical distribution over the signed offset $d$, learned from
the data. The $(-1)^{S_i}$ term is what lets one empirical curve describe both strands: it flips the
offset for reverse-strand reads so that both strands' reads are expressed relative to the same
"same-side" distance, and $\text{emp}$ only has to capture the shape once.

## GPS: a mixture model for overlapping binding events

A genomic region rarely has just one binding event nearby. GPS handles this by treating the reads
as generated from a **mixture** of $M$ candidate binding events. Each of the $N$ observed reads is
independently drawn from one of the $M$ components:

$$p(R \mid \pi) = \prod_{n=1}^N \sum_{m=1}^M \pi_m\, p(r_n \mid m), \qquad \sum_{m=1}^M \pi_m = 1,$$

where $\pi_m$ is the mixing probability of event $m$ and $p(r_n \mid m)$ is the single-event read
distribution above, centred at $b_m$. Which event actually generated read $n$ is a latent variable
$z_n$: $z_n = m$ means read $n$ came from event $m$. The goal is the maximum-likelihood mixture,
$\pi = \arg\max_\pi p(R \mid \pi)$, and since $z_n$ is unobserved this is exactly the setting for
EM.

**E-step.** Compute the responsibility of event $m$ for read $n$ — the posterior probability that
read $n$ came from $m$ given the current $\pi$:

$$\gamma(z_n = m) = \frac{\pi_m\, p(r_n \mid m)}{\sum_{m'=1}^M \pi_{m'}\, p(r_n \mid m')}.$$

**M-step.** Re-estimate each event's weight from its effective read count $N_m = \sum_n \gamma(z_n
= m)$:

$$\hat\pi_m = \frac{N_m}{\sum_{m'} N_{m'}}.$$

Iterated to convergence from a uniform start ($\pi_j = 1/M$ initially), this is standard EM for a
mixture, and at the end $N_m$ is read off as the strength (read support) of binding event $m$.

### Why plain EM is not enough: component elimination

To find binding events you do not know in advance, you start with *many* candidate positions $M$ —
far more than the number of real events — and let the fitting procedure discard the ones that are
not supported. Plain EM does not do this: the M-step above only ever divides reads among the
existing components, so a spurious component's $\pi_m$ shrinks toward zero but essentially never
reaches it exactly. Two events 50 bp apart, fit with plain EM and no prior, tend to stay smeared
across both nearby candidate positions rather than resolving into two clean estimates.

GPS fixes this by putting a **sparse prior** directly on the mixing weights (Figueiredo and Jain,
2002):

$$p(\pi) \propto \prod_{m=1}^M \frac{1}{(\pi_m)^\alpha}, \qquad \alpha > 0,$$

which favours mixtures where a few components carry all the weight and the rest carry none. Under
this prior the M-step becomes

$$\hat\pi_m = \frac{\max(0,\, N_m - \alpha)}{\sum_{m'} \max(0,\, N_{m'} - \alpha)},$$

so any component whose effective read count $N_m$ falls below $\alpha$ is set to exactly zero and
drops out of the mixture on that iteration — "EM with component elimination." Run on synthetic
data with two true events 50 bp apart (at 500 and 550 bp), this sparse-prior EM is what lets GPS
resolve the pair, where the uniform, no-prior version does not.

The result is single-base-resolution deconvolution of closely spaced, same-factor ("homotypic")
binding events — the lecture's example is a predicted CTCF binding region that on closer inspection
contains two coordinately located CTCF motifs, recovered as two separate events rather than one
blurred peak.

## Is a predicted event real? Testing against the control

GPS's EM gives every candidate event a read count $N_m$, but read count alone does not say whether
an event is a real binding site or a chance pileup of background reads — which is exactly why the
protocol also sequences a control (WCE) sample. The significance of an event is assessed with a
one-sided binomial test comparing IP (ChIP) reads to control reads at that position: under the null
hypothesis that reads at this location are equally likely to come from either channel, so that a
read is a "coin flip" between IP and control ($P = 0.5$),

$$F(k, n, P) = \sum_{l=0}^{\lfloor k \rfloor} \binom{n}{l} P^l (1-P)^{n-l},$$

where $n$ is the total number of IP and (scale-matched) control reads at the event, and $k$ is the
scaled control read count. $F(k,n,P)$ is the probability, under the null, of seeing as few as $k$
of the $n$ reads land in the control channel — a small value is evidence the event is real, since it
means the IP channel is unexpectedly enriched relative to a fair coin.

Because this test is run at every one of many thousands of candidate events, the resulting p-values
need a multiple-testing correction before they can be used to draw a line between "significant" and
not. The lecture uses Benjamini–Hochberg: rank all p-values from most ($\text{rank}=1$) to least
significant, and convert each to a $Q$-value,

$$Q\text{-value} = P\text{-value} \times \frac{\text{Count}}{\text{Rank}},$$

where $\text{Count}$ is the total number of events tested. Events are accepted in rank order,
$1, \dots, k$, up to the last rank whose $Q$-value is still within the desired false discovery rate.

## Reproducibility across replicates: the Irreproducible Discovery Rate

A single experiment's significance test controls false positives against the null model of noise,
but it says nothing about whether an event would show up again in an independent repeat of the
experiment. The natural check is to run the assay twice and ask which events both replicates agree
on — which raises the question the rest of this section answers: given two ranked lists of
candidate events, one per replicate, how do you decide where reproducibility ends?

**Spearman correlation is not enough.** The obvious first move is to rank the $n$ detected events in
each replicate from most to least significant, giving matched ranks $x_i$ and $y_i$ for event $i$ in
lists $X$ and $Y$, and compute

$$\rho = \frac{\sum_i (x_i - \bar x)(y_i - \bar y)}{\sqrt{\sum_i (x_i - \bar x)^2 \sum_i (y_i - \bar y)^2}}.$$

This is a single summary number for the whole list. It says how correlated the two rankings are
overall, but it does not tell you *which* events, and how far down the ranked list, are still
trustworthy — and that is precisely the decision a peak caller needs to make.

**The correspondence profile.** Instead, look at how well the two rankings agree as you move down
the list together. Let $\Psi_n(t)$ be the fraction of the $n$ events that appear in the top $nt$ of
*both* $X$ and $Y$. Genuine binding events tend to be ranked consistently high in both replicates,
so among them $\Psi_n(t)$ rises close to the diagonal (agreement grows in step with $t$); once you
have moved past the genuine events into the noise, matches between the two lists become essentially
coincidental and $\Psi_n(t)$ flattens out. Its derivative $\Psi_n'(t)$ makes the transition easier to
see: high while agreement is still real, dropping once you cross into noise.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Correspondence curve rising near the diagonal for reproducible events, then flattening once ranks reach irreproducible noise">
  <line x1="40" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <line x1="170" y1="190" x2="170" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <path d="M 40 190 L 170 105 L 300 46" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="105" y="140" text-anchor="middle" font-size="12" fill="currentColor">reproducible</text>
  <text x="235" y="170" text-anchor="middle" font-size="12" fill="currentColor">irreproducible</text>
  <text x="170" y="205" text-anchor="middle" font-size="11" fill="currentColor">t*</text>
  <text x="300" y="205" text-anchor="end" font-size="12" fill="currentColor">t (top fraction ranked)</text>
  <text x="15" y="30" font-size="12" fill="currentColor">&#936;&#8345;(t)</text>
</svg>
<figcaption>The correspondence curve $\Psi_n(t)$ tracks how much of the top-$t$ fraction of each
replicate's ranked list agrees. It runs close to the diagonal while the ranks are still genuine
signal, then bends once $t$ passes the point where the events stop being reproducible.</figcaption>
</figure>

**Turning the curve into a decision.** The IDR method models the pairs of ranks in $X$ and $Y$ as
coming from a two-component mixture: a "reproducible" component in which an event's rank in the two
replicates is tightly coupled, and an "irreproducible" component in which the two ranks are
essentially independent (noise). Fitting this mixture estimates, for each event, the probability
it belongs to the irreproducible component. To report results at a chosen IDR level $\alpha$, take
the top $l$ pairs by score such that the estimated fraction of the irreproducible component among
them is $\alpha$.

Applied across nine ChIP-seq peak callers on a CTCF experiment, IDR-selected peak sets were checked
against an independent criterion — coverage of high-confidence CTCF sequence motifs — and the
number of peaks a caller could report at $\text{IDR} = 0.05$ varied a great deal between callers;
for some callers the two-component mixture was not favoured by model selection at all, meaning no
principled reproducibility cutoff could be assigned to their scores.

## GEM: letting sequence motifs inform event finding

GPS locates binding events purely from the shape of the read pileup. But a transcription factor
also has sequence preferences — the short DNA motif it physically recognises — and a real binding
event is more likely to sit at a position matching that motif than at an arbitrary position with
similar read coverage. GEM (Genome-wide Event finding and Motif discovery) couples the two: read
data plus DNA sequence are used together, with event finding biasing motif discovery and motif
discovery biasing event finding in turn.

Mechanically, this is the same mixture model as before, but the sparse prior on $\pi$ is replaced
by a **position-specific** prior that combines a uniform sparsity term with a motif-based term:

$$p(\pi) \propto \prod_{m=1}^M (\pi_m)^{-\alpha_s + \alpha_m},$$

where $\alpha_s > 0$ is the same kind of uniform sparseness parameter as GPS's $\alpha$, and
$\alpha_m$ raises the prior weight of positions that match a discovered motif. A component sitting
on a motif match needs less read support to survive component elimination than one sitting on bare
sequence.

The reported effect of adding this prior is better resolution of joint binding events and better
spatial accuracy of the predicted event position relative to the motif — checked, for instance,
against human GABP data and mouse CTCF data, and against ChIP-exo data, where motif positions serve
as an external check on where the true binding position should be. It also produces a biological
result beyond method validation: of roughly 7,500 predicted Oct4 sites, about 2,500 fall within
100 bp of a Sox2 site — evidence of a spatial constraint on how these two cooperating factors bind
together, recoverable only once binding positions are resolved precisely enough to measure the
distance between them.

## From single factors to a regulatory code

Once binding events can be called reliably for many factors, the natural next question is not about
one factor but about the system: which regulators contribute to controlling each gene, what
sequences (cis-elements) they bind, and when. This is the idea of a **transcriptional regulatory
code** — mapping, gene by gene, the set of regulators bound at its promoter, as in the draft code
assembled for yeast promoters (Harbison et al., 2004), where several regulators are typically found
together at a single promoter region.

A code assembled in one species raises an immediate question: does the same code hold in a related
species, at the orthologous gene? Comparing promoter-proximal binding of four liver-expressed
transcription factors (FOXA2, HNF1A, HNF4A and HNF6) between human and mouse found that binding at
orthologous promoters is, for the most part, **not conserved**: only a small fraction of promoters
retain binding by all of the same factors in both species, a further fraction retain binding by
some but not all, and the majority show no conserved binding event at all (Odom et al., 2007). Even
where the transcription factor and the target gene are both conserved, the fact of binding at a
given promoter frequently is not.

## Sources

- Both slide decks for MIT OCW 7.91J Lecture 7 ("ChIP-seq Analysis" / "Irreproducible Discovery
  Rate (IDR) Analysis", David K. Gifford):
  `computational-biology/mit-ocw/7091j/lectures/07-slides/01-lecture-7.md` and
  `.../02-gps-probabilistically-models-chip-seq-read-spatial-distribut.md`. No transcript, written
  notes or problem set were supplied for this lecture, so the chapter follows the slides' own
  ordering and content only.
- Both slide files are flagged by the conversion pipeline as reconstructed by a model from a PDF
  with no text layer, with "every equation... unverified" — the equations above are transcribed as
  given in the slides and should be checked against the original PDF or the papers below before
  being relied on for computation.
- The slides cite, without including, several external results referred to in passing: Kharchenko,
  Tolstorukov et al., *Nature Biotechnology* 26 (2008) on the shape of the ChIP-seq read
  distribution around a binding event; Wang and Zhang, *BMC Systems Biology* 5 (2011), SeqSite;
  Figueiredo and Jain (2002) on the sparse mixture prior and component elimination; Li, Brown et al.,
  *Annals of Applied Statistics* 5 (2011), the IDR method and its correspondence-profile figures;
  Guo, Mahony et al., *PLoS Computational Biology* 8 (2012), GEM and the Oct4/Sox2, GABP and CTCF
  results; Harbison et al., *Nature* 431 (2004), the yeast regulatory code; and Odom, Dowell et al.,
  *Nature Genetics* 39 (2007), the human–mouse liver binding comparison. None of these papers were
  supplied as source material for this chapter; the summaries above report only what the slides
  state about them.

---

[← 6. OLC and de Bruijn Assembly](06-olc-and-de-bruijn-assembly.md) · [Contents](index.md) · [8. Modeling & Discovery of Sequence Motifs →](08-modeling-discovery-of-sequence-motifs.md)

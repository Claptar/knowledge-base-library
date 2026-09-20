---
title: "4. Statistical Significance of Sequence Alignments"
course: "MIT 8.592J"
chapter: 4
source: "https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.592J](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 4. Statistical Significance of Sequence Alignments

## What this covers

This chapter asks a single question about sequence alignment: given the score $S$ that an
alignment algorithm returns, how do we know whether it reflects a real relationship between two
sequences rather than being the kind of score that turns up anyway between unrelated sequences? It
develops the answer for **gapless** local alignments in full — arriving at the Gumbel (extreme
value) distribution for the best-scoring match — and then sketches how far the same reasoning
carries once **gaps** are allowed. It assumes the basic alignment machinery (scoring matrices,
global versus local alignment, the Needleman–Wunsch and Smith–Waterman dynamic-programming
recursions) from the earlier lectures on sequence alignment that this lecture refers to but does
not repeat.

## Sequence alignment as a scoring problem

Sequence alignment tries to establish a relationship between two sequences — nucleotides for
DNA/RNA, amino acids for protein — based on common ancestry, often as a way of guessing the
function of a newly sequenced gene from what is already in a database. The *explicit* inputs are
the two sequences themselves,
$$\{a_1, a_2, \dots, a_m\} \quad \text{and} \quad \{b_1, b_2, \dots, b_n\};$$
the *implicit* inputs are folded into the scoring rule: a similarity score $s(a,b)$ for matching
element $a$ against $b$, and a cost for opening or extending a gap. A **global** alignment
(Needleman–Wunsch) finds the single best match spanning both sequences; a **local** alignment
(Smith–Waterman) instead looks for the best-matching subsequences, possibly several of them,
anywhere inside the two sequences.

Either way, the space of possible alignments is exponentially large, and what makes the problem
tractable is a recursive algorithm that builds up the best score one position at a time —
*dynamic programming* in the language of bioinformatics, a *transfer matrix* in the language of
statistical physics. Both names describe the same trick behind much older recursions, such as
building up the binomial coefficients in Pascal's triangle: the answer at a point is assembled from
the answers immediately behind it.

The output of such an algorithm is an optimal alignment and its score $S$. The question this
chapter is about is what to make of that score: is it evidence of a real relationship, or is it the
kind of score you would get anyway by chance, given how many candidate alignments a large database
offers? Answering this needs the probability that a score at least this good arises from unrelated,
random sequences. That probability can be estimated by brute force — running the same algorithm on
shuffled or randomly generated sequences — but a significant score is by definition rare, so it
sits in the tail of that distribution, exactly the part that is hardest to pin down numerically. An
analytic result is worth having if one can be found.

## Gapless alignments: the recursive score

Start with the simplest case, where no gaps are allowed. Define a matrix of alignment scores
$$S_{ij} \equiv \text{score of the best alignment ending at } a_i \text{ and } b_j.$$
Without gaps, an alignment ending at $(i,j)$ can only have come from the alignment ending at
$(i-1,j-1)$, extended by matching $a_i$ against $b_j$:
$$S_{ij} = S_{i-1,j-1} + s(a_i, b_j).$$
Laid out as a rectangle with the elements of $\vec a$ along one edge and $\vec b$ along the other,
this recursion moves along diagonals — rotate the rectangle so that $(0,0)$ sits at the top and the
two edges run down at $\pm 45^\circ$, and it looks like the binomial triangle, with $s(a_i,b_j)$
playing the role of the increment added at each step.

That rotation is worth turning into a change of coordinates. Set
$$x = j - i, \qquad t = i + j,$$
so $x$ labels a diagonal ("column") and $t$ measures depth into it. The recursion becomes
$$S(x,t) = S(x, t-2) + s(x,t):$$
the score at position $x$ evolves in "time" $t$ by adding one random increment per step, and —
because a gapless alignment never moves sideways — different columns $x$ evolve completely
independently of one another. Gaps, taken up later in the chapter, are exactly the steps that move
between columns.

## Global alignment: the easy, and limited, Gaussian case

For a global alignment, the best match is read off from whichever column $x$ has the highest score
at the far end, $t = m+n$, with the aligned subsequences recovered by tracing the recursion back.
If the two sequences are random, so are the individual step scores $s(x,t)$, and $S(x,t)$ is a sum
of a large number of them. The central limit theorem then says $S$ is Gaussian, with mean and
variance equal to the number of steps times the mean and variance of a single step — comparing an
observed score against this Gaussian is enough to judge significance for a global alignment.

The catch is visible in the two ways such a path can behave: if the mean step score $\langle s
\rangle$ is positive the path trends upward over the length of the sequence; if $\langle s \rangle$
is negative it trends downward. Either trend can hide a short, well-matched stretch sitting inside
an otherwise poor alignment — a good local match contributes only a small deviation to a long path
and gets swallowed by the overall drift. That is the motivation for local alignment.

## Local alignment and the appearance of islands

Smith–Waterman alignment sidesteps the masking problem by refusing to let the score go negative:
$$S_{ij} = \max\{S_{i-1,j-1} + s(a_i,b_j),\ 0\}, \qquad\text{or, in the diagonal coordinates,}\qquad
S(x,t) = \max\{S(x,t-2) + s(x,t-1),\ 0\}.$$
If $\langle s \rangle > 0$ this floor rarely matters. If $\langle s \rangle < 0$ — the relevant case,
since unrelated sequences typically score badly on average — the effect is to chop the path back to
zero every time it would go negative, splitting it into separate positive excursions: "islands" of
positive score in a sea of zeros.

<figure>
<svg viewBox="0 0 420 200" role="img" aria-label="A local-alignment score path reset to zero whenever it goes negative, breaking into separate positive islands of different peak heights">
  <line x1="20" y1="170" x2="405" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <text x="4" y="164" font-size="12" fill="currentColor">S = 0</text>
  <text x="395" y="188" font-size="12" fill="currentColor">t</text>
  <polyline points="40,170 55,150 70,130 85,150 100,165 110,170 130,170 150,120 170,60 190,110 205,150 215,170 235,170 250,155 265,170 300,170 315,130 330,100 345,130 360,155 375,170" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <line x1="20" y1="60" x2="405" y2="60" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="345" y="50" text-anchor="middle" font-size="12" fill="currentColor">S = max Hα</text>
  <text x="70" y="120" text-anchor="middle" font-size="12" fill="currentColor">H₁</text>
  <text x="170" y="46" text-anchor="middle" font-size="12" fill="currentColor">H₂</text>
  <text x="330" y="88" text-anchor="middle" font-size="12" fill="currentColor">H₃</text>
</svg>
<figcaption>A random local-alignment score is reset to zero whenever it would go negative, breaking
the path into separate positive islands with peak heights $H_1, H_2, \dots$; the significance
question concerns the tallest of these peaks, $S = \max_\alpha H_\alpha$, not the path as a
whole.</figcaption>
</figure>

Each island is a candidate local match, but most of them — especially in a large database — will be
there by chance. Write $H_\alpha$ for the peak height of island $\alpha$; if there are $K$ islands
in total, the best local alignment found has score
$$S = \max_{\alpha = 1, \dots, K} H_\alpha.$$
For long sequences ($m, n \gg 1$) it is reasonable that the number of islands grows with the area
of the "ocean" they live in, i.e. $K \propto mn$.

## Extreme value statistics of the best island

$S$ above is the maximum of $K$ random variables, and this is exactly what *extreme value
statistics* is about. Suppose $H_1, \dots, H_K$ are drawn independently from some density $p(H)$.
The probability that their maximum is below a threshold $S$ is the probability that *every one* of
them is below $S$:
$$P_K(S) \equiv \text{Prob}(\max_\alpha H_\alpha \le S) = \left[\int_{-\infty}^S p(H)\,dH\right]^K
= \left[1 - \int_S^\infty p(H)\,dH\right]^K.$$
For large $K$, a typical value of the maximum sits far out in the tail of $p(H)$, where
$\int_S^\infty p(H)\,dH$ is small, so
$$P_K(S) \approx \exp\left[-K\int_S^\infty p(H)\,dH\right].$$

This is where the shape of the tail of $p(H)$ enters. Suppose — this is checked directly in the
next section — that $p(H)$ decays exponentially for large $H$, $p(H) = a\,e^{-\lambda H}$. Then
$$\int_S^\infty p(H)\,dH = \frac{a}{\lambda}\,e^{-\lambda S}, \qquad
P_K(S) = \exp\left[-\frac{Ka}{\lambda}\,e^{-\lambda S}\right],$$
with density
$$p_K(S) = \frac{dP_K}{dS} = Ka\,\exp\left[-\lambda S - \frac{Ka}{\lambda}\,e^{-\lambda S}\right].$$
The exponent $\phi(S) = -\lambda S - (Ka/\lambda)\,e^{-\lambda S}$ is maximized where
$$\frac{d\phi}{dS} = -\lambda + Ka\,e^{-\lambda S^*} = 0
\quad\Longrightarrow\quad S^* = \frac{1}{\lambda}\log\!\left(\frac{Ka}{\lambda}\right),$$
the most likely value of the extreme score. Using $S^*$ to eliminate $K$ and $a$ rewrites the
density as
$$p_K(S) = \lambda\,\exp\left[-\lambda(S - S^*) - e^{-\lambda(S-S^*)}\right].$$

This is the **Gumbel**, or Fisher–Tippett, extreme value distribution. Once the two numbers $S^*$
and $\lambda$ are known, the whole distribution of the best local-alignment score is fixed. Its
shape is nothing like a Gaussian: an exponential tail above $S^*$ and a much sharper cutoff below
it. That asymmetry matters in practice, because the usual instinct — "how many standard deviations
above the mean is this score?" — is a Gaussian idea, and it gives the wrong sense of rarity for a
distribution shaped like this one.

## Finding $\lambda$: the tail of the island-height distribution

What remains is to justify the assumed exponential tail and pin down $\lambda$. The height of a
single island evolves by the same rule as before, $S(x,t) = \max\{S(x,t-2)+s(x,t-1), 0\}$, and for
randomly chosen sequence characters this is a Markov process: the probability of a jump of size $s$
is some $p_s$ (with the caveat that jumps which would take the height negative are instead absorbed
at zero). Writing this out in terms of the underlying letter frequencies $p_a, p_b$ (for instance,
in one variety of DNA, roughly 30% each for A and T and 20% each for G and C),
$$p(h,t) = \sum_s p_s\, p(h-s,\,t-2) = \sum_{a,b} p_a p_b\, p\big(h - s(a,b),\, t-2\big).$$
Solving this exactly is awkward near $h=0$, where the floor at zero distorts the transition
probabilities — but the tail at large $h$, which is all the extreme-value argument needs, is
simple. Guess an exponential steady state,
$$p^*(h) \propto e^{-\lambda h},$$
and substitute into the recursion:
$$e^{-\lambda h} = \sum_{a,b} p_a p_b\, e^{-\lambda(h - s(a,b))}.$$
The factor $e^{-\lambda h}$ cancels from both sides — confirming the ansatz — leaving an implicit
equation that fixes $\lambda$ purely from the scoring matrix and the letter frequencies:
$$\sum_{a,b} p_a p_b\, e^{\lambda\, s(a,b)} = 1.$$

This shows the *typical* island height is exponentially distributed for large $h$. The distribution
of the *peak* of an island is not quite the same thing — taking a maximum over the island's history
changes the normalization — but the maximization does not change the exponential rate $\lambda$
itself; it only enters (through a logarithm) into $S^*$. So $\lambda$ from the equation above,
together with $S^*$ from the extreme-value argument, completely fix the Gumbel distribution for
random gapless local alignments. This result is due to Karlin and collaborators in the early 1990s,
and underlies the significance scores (E-values) reported by tools such as BLAST.

## Gapped alignments

Real evolution does not just substitute one residue for another — it also inserts and deletes
material, more so between more distantly related sequences — so a useful alignment has to permit
gaps. The usual scoring choice is a cost that grows linearly with gap length, sometimes with an
extra charge just for opening a gap. Dynamic programming still handles this, but the clean
analytic argument above breaks down: the islands picture still applies in outline — a local
alignment score is still the best of many candidates — but their shape is different, and their
statistics are harder to get at directly. Empirically, though, the local gapped-alignment score is
still found to be Gumbel distributed.

Gaps enter the diagonal picture as sideways moves: a step that consumes a character from one
sequence without matching it against the other moves the alignment path from column $x$ to a
neighbouring column, rather than straight down. The resulting alignment paths still move downward
in $t$ overall but can wander sideways in between — the same kind of object as a *directed path*
elsewhere in physics, such as a flux line threading a type-II superconductor or a domain wall in a
two-dimensional magnet.

Statistical mechanics offers one route into such paths: give the alignment problem a finite
"temperature" $\beta^{-1}$, treat a score as a (negative) energy, and weight every path by a
Boltzmann factor $e^{\beta S}$. Define the constrained partition function
$$W(x,t) \equiv \sum_{\text{paths } (0,0)\to(x,t)} e^{\beta S[\text{path}]},$$
which obeys its own transfer-matrix recursion,
$$W(x,t) = e^{\beta s(x,t)} W(x, t-2) + e^{-\beta g}\big[W(x+1, t-1) + W(x-1, t-1)\big]:$$
the first term is the no-gap step down the same column, the other two are gap steps into a
neighbouring column at an energy cost $g$. Ordinary (zero-temperature) dynamic programming is
recovered in the limit $\beta \to \infty$, where the sum is dominated by whichever term is largest;
writing $W(x,t) = e^{\beta S(x,t)}$ gives
$$S(x,t) = \max\big\{\, S(x,t-2) + s(x,t),\ \ S(x+1,t-1) - g,\ \ S(x-1,t-1) - g \,\big\},$$
the gapped analogue of the Needleman–Wunsch/Smith–Waterman recursion, with the last two options
allowing a step sideways at the price of the gap cost $g$. This finite-temperature framing has been
used to obtain some analytic results for gapped alignment, though the lecture does not pursue it
further.

## Sources

- All of this chapter is drawn from the slide deck for OCW 8.592J/HST.452J *Statistical Physics in
  Biology* (Spring 2011), lecture 8, §1.5 "Sequence alignment": the introduction
  (`01-introduction.md`), §1.5.1 "Significance of gapless alignments" (`02-1-5-1-significance-of-
  gapless-alignments.md`), and §1.5.2 "Gapped alignments" (`03-1-5-2-gapped-alignments.md`). No
  transcript or written notes were supplied for this lecture, so the exposition and connective
  reasoning here follow the slides as given; the source itself is a model's reconstruction of a PDF
  with no text layer, and the note that "every equation is unverified" carries over to this
  chapter.
- The slides explicitly refer to "earlier lectures by Prof. Mirny" covering the basic sequence
  alignment machinery (dynamic programming, scoring matrices, Needleman–Wunsch, Smith–Waterman) —
  material this chapter assumes but that was not part of the supplied input.
- The result that random gapless local-alignment scores follow a Gumbel distribution is attributed
  in the slides to Karlin and collaborators, "early 1990s," without a more specific citation.
- The supplied problem set (`psets/08-questions.md`, Assignment 8, "Drift, Diffusion, and Dynamic
  Instability") covers a different topic entirely — treadmilling actin, microtubule
  growth/shrinkage, and molecular-motor models — and does not exercise the sequence-alignment
  material of this lecture, so it is not reproduced here.

---

[← 3. Absorbing States and Fixation](03-absorbing-states-and-fixation.md) · [Contents](index.md) · [5. The Charge Environment of the Cell →](05-the-charge-environment-of-the-cell.md)

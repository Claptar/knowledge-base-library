---
title: "19. Relaxation Oscillators and Scale-Free Networks"
course: "MIT 8.591J 2014"
chapter: 19
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 19. Relaxation Oscillators and Scale-Free Networks

## What this covers

This lecture answers two separate questions, joined only by being taught back to back. First: why
does combining a positive feedback loop with a negative one make a genetic oscillator both more
robust and tunable, where a loop of pure negative feedback — like the repressilator — is neither?
Second: why does a network built by two simple rules, growth and preferential attachment, end up
with a power-law degree distribution, and what does that derivation actually prove about real
biological networks? A short third section opens the question of what a fair "control" network
looks like when testing whether a network motif is over-represented.

It assumes the repressilator (three repressors in a ring, each inhibiting the next), negative
auto-regulation, the phase-line argument for why $\dot x = f(x)$ cannot oscillate, and the basic
vocabulary of random graphs: degree distribution, Erdős–Rényi graphs, and the Watts–Strogatz
small-world model.

## Why a single negative feedback loop won't oscillate

Take the sharpest possible version of a repressor turning off its own production — a step function
rather than a smooth Hill function, i.e. infinite cooperativity:

$$\dot x = \beta\,\theta(x_c - x) - \alpha x,$$

where $\theta$ switches production fully on below some critical concentration $x_c$ and fully off
above it. This does not oscillate, no matter how sharp the switch is. The reason has nothing to do
with the sharpness: $\dot x$ is written purely as a function of $x$ itself, with no $\ddot x$ term,
so this is a flow on a line. A trajectory on a line moves monotonically toward wherever the flow
points; it can never loop back around to repeat itself. Sharpening the nonlinearity changes where
the fixed point sits and how fast the trajectory approaches it, but it cannot manufacture a second
dimension for the trajectory to circle in.

Adding the mRNA explicitly — protein $x$ represses transcription of its own mRNA, and that mRNA is
translated to make more $x$ — still does not oscillate. Two variables are now in play, but this
particular loop still settles down rather than cycling.

What is missing is delay. Two ways to put it in:

- **Model the intermediate steps explicitly.** Transcription, translation, folding, and
  dimerization (if the repressor has to dimerize before it can bind DNA) all take time. A model
  that tracks each of these steps builds in an effective delay between a change in $x$ and its
  consequence, and that delay is enough to generate a limit cycle.
- **Put the delay in explicitly.** Replace $\dot x = f(x)$ with $\dot x(t) = f\big(x(t-\tau)\big)$:
  the rate of production now responds to the concentration at some earlier time $t - \tau$, not the
  current one. This is a much more explicit way of encoding the same idea, and it too can produce
  oscillations in an otherwise simple auto-regulatory loop.

The repressilator — $x$ inhibiting $y$ inhibiting $z$ inhibiting $x$, from the Elowitz paper —
works this way: the delay is distributed across the ring of three repressors rather than built into
one gene's biochemistry. It does oscillate, but imperfectly. In the reported experiment only about
40% of cells actually showed oscillations, the oscillations that did appear were noisy, and cells
desynchronized from each other fairly quickly. Worse, the period is not very tunable: try to change
the frequency — for instance by changing a degradation rate — and the amplitude collapses along
with it. This is not a defect specific to the repressilator; it is a general feature of oscillators
built entirely from negative interactions, including rings with other odd numbers of repressors
(a five-protein "pentalator," or seven, and so on all round). You can write down the model for any
of them, and in all of these cases tuning the frequency costs you the amplitude.

## Interlinked positive and negative feedback: relaxation oscillators

A 2008 *Science* paper by Jim Ferrell's group at Stanford, "Robust Tunable Biological Oscillations
from Interlinked Positive and Negative Feedback Loops," surveyed many circuit designs
computationally and made this contrast precise. The idea: instead of one loop, use two, of
different character and different speed.

- A **positive feedback loop** — some $x$ that activates itself. On its own this does not oscillate
  either; it produces bistability, two stable states rather than a cycle.
- A **negative feedback loop**, routed through another protein, layered on top.

The two loops are set to run on different time scales: the positive loop is fast, the negative loop
is slow. The fast loop locks the system into one of the two bistable states — this is what sets and
protects the *amplitude*, because "on" and "off" are fixed values rather than something that drifts
as parameters change. The slow loop is what actually drives the switching between those two states
over time, and it is the slow time scale that sets the *period*. Because amplitude and period are
now controlled by two different mechanisms, you can change one (tune the slow loop to change the
frequency) without disturbing the other. Ferrell's group found computationally that circuits built
this way could be tuned over a wide range of periods while barely losing amplitude, in sharp
contrast to the pure-negative-feedback designs, and that they were also more robust: doubling or
halving a rate parameter still left recognizable oscillations, where the purely negative designs
lost the oscillation altogether. That robustness is offered as a reason such designs might be more
evolvable, quite apart from any benefit of tunability itself.

### The circuit analogy

There is a standard electrical analogy for this separation of time scales: a battery at voltage
$V_\text{battery}$ charges a capacitor through a resistor, and a spark gap fires — discharging the
capacitor almost instantly — once the voltage across the capacitor reaches some threshold
$V_\text{th} < V_\text{battery}$.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="Voltage across a capacitor in a relaxation oscillator, charging slowly and discharging fast, at two different periods but the same amplitude">
  <defs>
    <marker id="arrow1" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="35" y1="190" x2="335" y2="190" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow1)"/>
  <line x1="40" y1="200" x2="40" y2="20" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow1)"/>
  <text x="330" y="205" text-anchor="middle" font-size="12" fill="currentColor">t</text>
  <text x="20" y="25" text-anchor="middle" font-size="12" fill="currentColor">V</text>
  <line x1="40" y1="70" x2="335" y2="70" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
  <text x="292" y="65" font-size="11" fill="currentColor">V_th</text>
  <line x1="40" y1="40" x2="335" y2="40" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.4"/>
  <text x="285" y="35" font-size="11" fill="currentColor">V_batt</text>
  <path d="M 40 190 C 55 120, 70 80, 100 70 L 100 190 C 115 120, 130 80, 160 70 L 160 190 C 190 150, 250 90, 300 70 L 300 190" fill="none" stroke="currentColor" stroke-width="1.8"/>
</svg>
<figcaption>The capacitor charges on the slow RC time scale until it reaches the spark threshold,
then discharges almost instantly. Slowing the charging rate (third cycle) stretches the period but
leaves the amplitude — fixed entirely by the threshold — unchanged.</figcaption>
</figure>

As long as $V_\text{th}$ is below $V_\text{battery}$, this fires periodically. Changing the resistor
(or capacitor) changes how fast the capacitor charges — the slow $RC$ time scale — and hence the
period, but the amplitude of each cycle is bounded by $V_\text{th}$ regardless: the spark always
fires at the same voltage. That is exactly the separation of time scales in the biological circuit:
one slow process sets *when*, one fast process sets *how far*, and they can be tuned independently.

### Built and confirmed: the Hasty oscillator

Ferrell's argument was computational. In the same year, Jeff Hasty's group (Hasty trained originally
as a high-energy theorist, then moved into experimental synthetic biology as a postdoc with Jim
Collins) built the circuit, in a *Nature* 2008 paper titled "A Fast, Robust, and Tunable Synthetic
Gene Oscillator." Using the same insight — interlinked positive and negative feedback loops, in
*E. coli* — they got beautiful oscillations in essentially every cell, tunable in period by a factor
of three or four, with periods as fast as 13 minutes. Interestingly, their model also predicted that
the same network could oscillate from negative auto-regulation alone, once the intermediate steps of
protein maturation and so on were modeled explicitly (delay again, this time arising mechanistically
rather than by design) — they built that variant too, and it also oscillated. That back-and-forth
between modeling and experiment is offered as a model for how this kind of synthetic-biology work
should go.

## Scale-free networks: the observation that needs explaining

The lecture then turned to the assigned reading, the Barabási paper proposing a mechanism for
power-law degree distributions in networks — one of the most cited papers in any field, something
like 20,000 citations by Google Scholar. Why so many? Partly timing: it appeared exactly as large
network datasets (web crawls, citation databases, and so on) were becoming available across many
fields at once, and people were already seeing the same qualitative pattern everywhere without a
clean explanation for it. A mathematician had apparently demonstrated a similar construction decades
earlier, without anything like the same impact — being first with the right idea, at the right time,
in front of the right audience, is not the same thing as being first, period. And a paper that starts
from an already-known, already-interesting observation and explains it is, in general, a much
stronger bet than one that writes down a model and hopes something interesting falls out.

The observation: in network after network, the probability that a node has $k$ edges falls off as a
power law,

$$p(k) \sim \frac{1}{k^\alpha}, \qquad \alpha \approx 2\text{–}4,$$

rather than exponentially. Examples discussed: web pages and hyperlinks (directed, $\alpha \approx
2.1$), movie stars and the movies they co-starred in (undirected, $\alpha \approx 2.3$), and articles
and their citations (directed, $\alpha \approx 3$). A power law with $\alpha$ around 3 sounds like a
fast fall-off — double $k$ and the probability drops by roughly an order of magnitude — but that is
slow compared to an exponential tail: it is exactly this slowness that lets a handful of nodes carry
a thousand edges or more, something that essentially never happens in a network whose tail decays
exponentially.

## Two models that miss it, and one that gets it

Two natural candidate explanations were set aside:

- **Erdős–Rényi random graphs** connect every pair of nodes independently with some fixed
  probability $p$. Their degree distribution is peaked and falls off exponentially above the peak —
  no hubs, nothing like the fat power-law tail. (A side note from the derivation in the paper: the
  paper states the Erdős–Rényi degree distribution as an exact Poisson; that is only the small-$p$
  approximation to the true binomial distribution, and the paper is sloppy about the distinction.)
- **Watts–Strogatz small-world networks**, built by randomly rewiring a small fraction of the edges
  of a regular ring lattice, reproduce the short average path lengths seen in real networks — the
  "six degrees of separation" or Kevin Bacon phenomenon, where almost any two actors are connected
  through a short chain of shared movies. But the small-world property (short paths) is logically
  separate from having a power-law degree distribution: rewiring a lattice gives short paths without
  giving hubs. Most known power-law networks probably also have the small-world property, if only
  because a few very highly connected nodes make good shortcuts — but that is an empirical
  observation about the examples at hand, not a proof that one property implies the other.

Barabási and Albert's model rests on exactly two assumptions — "the two things you should be able to
recapitulate on an exam":

- **Growth**: the network is not static; nodes are added over time.
- **Preferential attachment**: a new edge is more likely to attach to a node that already has many
  edges, and — in this model — with probability exactly proportional to the number of edges it
  already has ("rich get richer").

## Deriving the degree distribution

Start with $m_0$ unconnected nodes at time $0$. At each subsequent time step, add one new node and
$m$ new edges, all of them from the new node to $m$ existing nodes chosen with probability
proportional to their current degree (linear preferential attachment). So at time $t$:

$$N(t) = m_0 + t, \qquad E(t) = mt.$$

**Growth of a single node's degree.** Once node $i$ exists, its degree grows by attracting a share of
the $m$ new edges added at each subsequent time step. The probability that any one of those new
edges attaches to node $i$ is $k_i / \sum_j k_j$. Because the graph is undirected, every edge is
counted at both of its endpoints, so $\sum_j k_j = 2E(t) = 2mt$. The expected increase in $k_i$ per
time step is therefore $m$ times this probability, and treating the discrete process as continuous
in the limit of interest gives the differential equation

$$\frac{dk_i}{dt} = m \cdot \frac{k_i}{2mt} = \frac{k_i}{2t}.$$

(The factor of 2 here is not a place to be casual about constants: it comes directly from
"undirected," and it changes the exponent of $t$ that comes out below — for a directed network, where
in-edges and out-edges are tracked separately, this factor of 2 would not appear.)

This is separable: $dk_i/k_i = dt/(2t)$, so $\ln k_i = \tfrac12 \ln t + \text{const}$, giving
$k_i(t) = c\sqrt{t}$. The boundary condition is that node $i$ has exactly $m$ edges the moment it is
added, at time $t_i$: $k_i(t_i) = m$, so $c = m/\sqrt{t_i}$, and

$$k_i(t) = m\sqrt{\frac{t}{t_i}}.$$

Older nodes (small $t_i$) end up with more edges — the rich-get-richer effect, made explicit.

**From the growth law to a probability.** We want the distribution of degrees across all nodes at
time $t$, not just how one node's degree grows. Since $k_i(t)$ is a decreasing function of $t_i$, the
event "node $i$ has fewer than $k$ edges at time $t$" is exactly the event that it was added late
enough:

$$k_i(t) < k \iff t_i > \frac{m^2 t}{k^2},$$

so $P\big(k_i(t) < k\big) = P\!\left(t_i > \dfrac{m^2 t}{k^2}\right)$.

Now ask: what is the probability that a randomly chosen node (out of however many exist at time $t$)
was added before some particular time $T$? Concretely — of the $m_0 + t$ nodes present at time $t$,
the number added before time $T$ is (up to the bookkeeping choice of whether to count the initial
$m_0$ nodes, which stops mattering entirely as $t \to \infty$) roughly $T$. So

$$P(t_i \le T) \approx \frac{T}{m_0 + t}, \qquad P(t_i > T) \approx 1 - \frac{T}{m_0+t}.$$

Substituting $T = m^2 t / k^2$:

$$P\big(k_i(t) < k\big) = 1 - \frac{m^2 t/k^2}{m_0 + t}.$$

Differentiating with respect to $k$ gives the probability density directly:

$$p(k, t) = \frac{2 m^2 t}{k^3 (m_0 + t)}.$$

As $t \to \infty$ — after the network has grown enough that its structure stops changing shape — the
ratio $t/(m_0+t) \to 1$, and this settles onto a stationary distribution:

$$p(k) = \frac{2m^2}{k^3}.$$

**The degree distribution is a power law with exponent exactly 3**, independent of $m$. This is the
"crux of the climb" in the paper's derivation: the confusing part is not the differential equation
itself, but keeping straight that "the probability node $i$ was added before time $T$" is a statement
about picking a random node out of the population that currently exists, not about the specific
labels $t_i$ and $k_i$ that appear elsewhere in the calculation.

One genuinely surprising feature, flagged in the lecture: it would be natural to guess that if the
attachment probability were some nonlinear function of degree (say $\propto k^\beta$ rather than
linear in $k$) the exponent $\alpha$ would shift continuously with $\beta$. According to the paper,
that is not what happens — only exactly linear preferential attachment produces a power law at all;
away from linear, the power law is lost altogether. That leaves the range of exponents actually
observed (roughly 2.1 to 3 across different real networks) unexplained by this model alone. The
paper's own suggestion — that directed networks can have different exponents than undirected ones —
was flagged as unsatisfying, since undirected examples (the actor network, $\alpha \approx 2.3$) also
deviate from 3.

## What the derivation does and doesn't establish

Two things are worth separating carefully. The derivation shows that growth plus linear preferential
attachment is *sufficient* to produce a power-law degree distribution. It does not show that this
mechanism is *necessary*, nor that it is the only way real power-law networks could have arisen. This
distinction was flagged as a "standard logical fallacy" worth watching for in general: demonstrating
that some assumptions lead to an observed behavior is not a proof that those assumptions are what
actually produced the behavior in any particular real system. It is evidence that the mechanism is
plausible and probably a dominant contributor in many cases — not a proof about any one of them.

Is there a plausible biological instance of growth-plus-preferential-attachment? A candidate raised
in discussion: transcription networks grow by **gene duplication**. Duplicating a gene typically
duplicates its adjacent promoter region along with the coding sequence, so a transcription factor
$x$ that already regulates many targets is proportionally more likely to have one of its targets hit
by a random duplication event — the chance scales linearly with the number of targets it already
has, with no extra assumption needed to get exactly the linear preferential attachment the model
requires. This lines up with an observation about real transcription networks: it is specifically the
*out-degree* of transcription factors (how many genes a given factor regulates) that is power-law
distributed, while the *in-degree* of genes (how many transcription factors regulate a given gene) is
narrow — most genes are controlled by only a handful of factors. Gene duplication naturally targets
the out-edges (the regulated genes), which is the side of the network where the power law actually
shows up.

This is offered as a reasonably compelling mechanistic account of the growth statistics, but with
caveats stated explicitly: it says nothing about selection, and nothing about why specific network
motifs recur, and gene duplication is not the whole picture, since genomes both gain and lose genes
along a lineage — unlike the web, whose growth is presently dominated by addition rather than
deletion. Whether a birth-and-death version of the model would still recover the same distribution
was raised but not resolved in the lecture.

## Choosing a null model for network motifs

The last few minutes opened a question to be picked up in the next lecture: to ask whether a
particular network motif — a feed-forward loop, say — occurs more often in a real network than you'd
expect "by chance," you first have to fix what "by chance" means. That is the null model, and an
Erdős–Rényi random graph is not obviously the right one, for two reasons raised in discussion:

- **It does not reproduce the asymmetry actually seen.** In a real transcription network, in-degree
  and out-degree look nothing alike: out-degree (targets per transcription factor) is power-law
  distributed, in-degree (regulators per gene) is narrow. A plain Erdős–Rényi model — even a directed
  one with edges placed independently — does not reproduce that asymmetry, so comparing motif counts
  against it is comparing the real network to something that already looks different from it in an
  obvious way.
- **Biological wiring may not be "random" for mechanistic reasons that have nothing to do with
  selection.** Gene duplication itself seeds proto-motifs for free: if $x$ regulates $y$, and $y$ is
  then duplicated into $y_1$ and $y_2$, you already have $x$ regulating two genes — the beginning of
  a feed-forward-loop-like structure — without any selection pressure at all. A null model built to
  test for selection should try to strip out as much of this kind of mechanistic artifact as
  possible.

The proposed alternative is **degree-preserving randomization**. Take the real network's exact degree
sequence — every node's actual in-degree and out-degree — and generate a randomized network with the
identical degree sequence by repeatedly picking two edges at random and swapping their targets.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="A degree-preserving rewiring: two edges swap targets so every node's in- and out-degree is unchanged">
  <defs>
    <marker id="arrow2" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
      <polygon points="0,0 7,3.5 0,7" fill="currentColor"/>
    </marker>
  </defs>
  <text x="90" y="20" text-anchor="middle" font-size="12" fill="currentColor">before</text>
  <circle cx="60" cy="60" r="4" fill="currentColor"/>
  <text x="45" y="55" font-size="12" fill="currentColor">x1</text>
  <circle cx="60" cy="130" r="4" fill="currentColor"/>
  <text x="45" y="135" font-size="12" fill="currentColor">x2</text>
  <circle cx="150" cy="45" r="4" fill="currentColor"/>
  <text x="158" y="40" font-size="12" fill="currentColor">y1</text>
  <circle cx="150" cy="95" r="4" fill="currentColor"/>
  <text x="158" y="90" font-size="12" fill="currentColor">y2</text>
  <circle cx="150" cy="145" r="4" fill="currentColor"/>
  <text x="158" y="150" font-size="12" fill="currentColor">y3</text>
  <line x1="63" y1="58" x2="146" y2="46" stroke="currentColor" stroke-width="1.3" opacity="0.55" marker-end="url(#arrow2)"/>
  <line x1="63" y1="128" x2="146" y2="96" stroke="currentColor" stroke-width="1.3" opacity="0.55" marker-end="url(#arrow2)"/>
  <line x1="63" y1="62" x2="146" y2="144" stroke="currentColor" stroke-width="1.3" opacity="0.3" stroke-dasharray="3 3"/>
  <text x="260" y="20" text-anchor="middle" font-size="12" fill="currentColor">after</text>
  <circle cx="230" cy="60" r="4" fill="currentColor"/>
  <text x="215" y="55" font-size="12" fill="currentColor">x1</text>
  <circle cx="230" cy="130" r="4" fill="currentColor"/>
  <text x="215" y="135" font-size="12" fill="currentColor">x2</text>
  <circle cx="320" cy="45" r="4" fill="currentColor"/>
  <text x="300" y="40" font-size="12" fill="currentColor">y1</text>
  <circle cx="320" cy="95" r="4" fill="currentColor"/>
  <text x="300" y="90" font-size="12" fill="currentColor">y2</text>
  <circle cx="320" cy="145" r="4" fill="currentColor"/>
  <text x="300" y="150" font-size="12" fill="currentColor">y3</text>
  <line x1="233" y1="62" x2="316" y2="94" stroke="currentColor" stroke-width="1.6" marker-end="url(#arrow2)"/>
  <line x1="233" y1="128" x2="316" y2="48" stroke="currentColor" stroke-width="1.6" marker-end="url(#arrow2)"/>
  <line x1="233" y1="62" x2="316" y2="144" stroke="currentColor" stroke-width="1.3" opacity="0.3" stroke-dasharray="3 3"/>
</svg>
<figcaption>Two edges are chosen at random and their targets are swapped ($x_1\to y_1$, $x_2\to y_2$
become $x_1\to y_2$, $x_2\to y_1$); every node keeps exactly the in- and out-degree it had before —
only who connects to whom changes. Repeating this many times builds a degree-preserving null network
to compare against the real one.</figcaption>
</figure>

Comparing motif counts between the real network and many such randomizations gives a fairer test than
comparing against Erdős–Rényi: even holding the exact degree sequence fixed, a real transcription
network turns out to contain more feed-forward loops than its degree-preserving randomizations. That
gap is the beginning of an argument that feed-forward loops are selected for — but only the
beginning. Finding more of a motif than a null model predicts is suggestive evidence of selection,
never proof: the excess could still be produced by a mechanistic process (duplication again) rather
than by selection for the motif's function, and most arguments about evolutionary causes of a network
statistic are not ironclad in either direction. The honest position is that this kind of evidence
accumulates rather than settles the question outright — closer to arguing about a historical
counterfactual than proving a theorem, though laboratory evolution experiments can add real evidence
even if they cannot establish what happened millions of years ago. Quantifying the excess of
feed-forward loops, and what it does and doesn't imply, was left for the next lecture.

## Sources

All of this chapter comes from one transcript: the recording converted at
`computational-biology/mit-ocw/8591j-2014/recordings/recordings/nndqjhtuqjw.md` (MIT OCW 8.591J
Systems Biology, Fall 2014). No slides, notes, or exercises were supplied for this lecture, and
whatever was written or drawn on the board — the circuit diagrams, the node-and-edge sketches for
the Barabási–Albert derivation, the $x_1, x_2, y_1, y_2, y_3$ picture for edge-swapping — is not
captured in the source; the derivation and diagrams above are reconstructed from the spoken
description alone.

Referred to in the lecture but not contained in this transcript, and not otherwise supplied:

- The Barabási (and Albert) paper on scale-free networks itself — the week's assigned reading,
  including its appendix on in- and out-degree distributions, and the specific page (around 510)
  where the lecture flags the treatment of the Erdős–Rényi degree distribution as sloppy.
- The Elowitz repressilator paper, discussed in the previous lecture ("Thursday") and referred to
  here only in summary.
- Ferrell, J. E. et al., *Science* (2008), "Robust Tunable Biological Oscillations from Interlinked
  Positive and Negative Feedback Loops."
- Hasty, J. et al., *Nature* (2008), "A Fast, Robust, and Tunable Synthetic Gene Oscillator."
- The instructor's own News & Views piece in *Nature* summarizing the Ferrell and Hasty papers.
- The Watts–Strogatz small-world network paper.
- The pre-class reading questions about whether growth and preferential attachment are strictly
  necessary to produce a power-law network — referred to but not reproduced here.
- The continuation of the network-motif null-model discussion, deferred explicitly to the next
  lecture ("Thursday") and therefore not part of this transcript.

---

[← 18. Neutral Theory of Species Abundance](18-neutral-theory-of-species-abundance.md) · [Contents](index.md) · [20. Diffusion and Pattern Formation →](20-diffusion-and-pattern-formation.md)

---
title: "1. Feed-Forward Loops as Network Motifs"
course: "MIT 8.591J 2014"
chapter: 1
source: "https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.591J 2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 1. Feed-Forward Loops as Network Motifs

## What this covers

This lecture answers two connected questions. First: how do you tell, rigorously, that a small
wiring pattern in a regulatory network — three genes joined into a triangle of regulatory links,
say — turns up more often than pure chance would produce in a network this sparse, so that it
deserves to be called a **network motif** rather than a coincidence? Second: once the
**feed-forward loop** has been established as exactly such a motif in the *E. coli* transcription
network, what dynamical job might explain why the cell keeps re-using it? The chapter assumes the
reader already has autoregulation as a first example of a network motif, knows that gene expression
is a dynamical process with a characteristic timescale set by a protein's effective lifetime
(production balanced against dilution and degradation), and has met the idea that a signal binding
an existing protein is fast while making more of a protein by transcription is slow.

## Counting subgraphs against a null model

A regulatory network is drawn as $N$ nodes (genes or proteins) joined by $E$ directed edges (one
protein regulating another). For the *E. coli* transcription network used throughout, $N\approx
400$ and $E\approx 500$. Out of the $\sim N^2$ possible directed edges, only a tiny fraction are
actually present: $P = E/N^2 \ll 1$. That is what "sparse" means here. The mean number of edges per
node, in or out, is $\lambda = E/N \approx$ a little over one.

That average is deceptive on the outgoing side. Most proteins are not transcription factors, so to
first order they cannot directly affect anyone else's transcription and have zero outgoing edges;
a small number of transcription factors regulate many genes each. So the out-degree distribution is
heavy-tailed (a power law), and "on average, one outgoing edge per gene" describes almost no actual
gene — it is mostly genes with none, and a few genes with many.

To ask whether a subgraph is over-represented, characterize it by two numbers: little $n$, the
number of nodes, and little $g$, the number of edges. Autoregulation is $n=1,\ g=1$. The
feed-forward loop — $X$ regulates $Y$, $X$ regulates $Z$, $Y$ regulates $Z$ — is $n=3,\ g=3$; the
fact that $n=g$ here turns out to matter.

Model the network first as an **Erdős–Rényi (ER) random graph**: $N$ nodes, and each of the
possible edges present independently with probability $P$. The expected number of copies of a
given subgraph is

$$\langle N_G\rangle \approx a\,N^{n}\,P^{g},$$

where $N^n$ (using $N\gg n$) counts the ways to pick which nodes play the roles, $P^g$ is the
chance that all $g$ required edges happen to be present, and $a$ is a symmetry factor: the number
of ways of permuting the $n$ chosen nodes that give back the *same* subgraph. For the feed-forward
loop, $X$, $Y$ and $Z$ each occupy a distinguishable position (only $Y$ receives from $X$ and sends
to $Z$), so no permutation reproduces it and $a=1$. A three-node cycle where each node regulates the
next (the kind of loop seen in a repressilator) has three rotations that give the same picture, so
$a=3$.

Since $\lambda = E/N = PN$, substitute $P=\lambda/N$:

$$\langle N_G\rangle \approx a\,\lambda^{g}\,N^{\,n-g}.$$

This is the useful rewriting. Whenever $n=g$ — true of autoregulation and of the feed-forward loop
— the $N^{n-g}$ factor is $N^0=1$: the expected count of that shape does **not grow with the size
of the network**. It stays of order $a\lambda^g$, which is order one if $\lambda$ is of order one,
regardless of whether the network has 400 nodes or 4,000. So if a real network contains *dozens* of
copies of an $n=g$ subgraph, that is a real excess, not just "a bigger network has more of
everything."

## Two null models, one very different answer

For the feed-forward loop, the observed count in *E. coli* is 42. Against the ER null model
(same $N$, same sparseness $P$) the expected count is $1.7\pm1.3$ — Poisson, because independent
edges appearing at random produce a Poisson count. 42 against $1.7\pm1.3$ looks like overwhelming
evidence that the feed-forward loop is a network motif.

But the ER model only preserves the *mean* degree; it throws away the fact that a few genes are
big regulatory hubs and most have no outgoing edges at all. A sharper null model preserves each
node's exact in- and out-degree — a **degree-preserving random network** — and asks the same
question against it. Such networks are generated by repeatedly picking two edges at random and
swapping their endpoints, many times over, which leaves every node's own edge counts untouched
while randomizing who connects to whom. Against this null model, the expected feed-forward-loop
count is $7\pm5$ — much higher than the ER estimate. 42 is still well above $7\pm5$, so the loop is
still a motif, but far less dramatically than the naive ER comparison suggested; a network with, say,
15 observed loops would have looked like a motif against ER and would not against the
degree-preserving null.

Why does preserving the full degree distribution raise the expectation so much? Roughly: if $X$ is
a hub with many outgoing edges (many genes it regulates), an extra edge from any one of those
targets to any other creates a feed-forward loop — and a hub's large out-degree, preserved exactly
in this null model, creates many such opportunities that the flattened ER picture doesn't capture.
It's worth being wary of stopping at a verbal story like that one, though — a plausible-sounding
argument can be constructed for almost anything, and the only way to be sure is to run the
comparison quantitatively, as was done here.

Uri Alon's 2002 *Science* paper ran exactly this comparison, against the degree-preserving null,
across several kinds of network, not only the *E. coli* and yeast transcription networks: the
neuronal wiring diagram of *C. elegans* (feed-forward loops again over-represented), food webs
(where the feed-forward loop was *not* a motif but other subgraphs were), a class of electronic
logic circuits, and the World Wide Web link graph, which showed still other patterns. Which small
subgraphs are over-represented is a signature of what kind of computation or constraint a
particular network embodies — not a universal property of sparse networks in general.

## The coherent type-1 feed-forward loop: a sign-sensitive delay

Take the feed-forward loop with all edges activating — $X$ activates $Y$, $X$ activates $Z$, $Y$
activates $Z$ — combined at $Z$ by an **AND gate**: $Z$ is expressed only when both $X^*$ (active
$X$) and $Y^*$ are present. This is the **coherent type-1** feed-forward loop, and it is the most
common of the eight possible sign patterns a three-node feed-forward loop can have — roughly half
of the loops found in the real networks are this type.

Suppose the signal $S_y$ that activates $Y$ is present throughout, and $S_x$ (the signal acting on
$X$) is switched on and later off. $X$ protein is already present the whole time, so $S_x$ turning
on converts it to $X^*$ essentially instantly — this is just a fast binding event, not new protein
synthesis. $Y$, though, has to be *transcribed* by $X^*$ before there is any $Y$ to turn into $Y^*$
with $S_y$; that accumulation is slow, on the order of the generation time. So $Z$, needing both
$X^*$ and $Y^*$, only switches on once $Y^*$ has built up — a genuine **delay in turning on**.

When $S_x$ then goes away, $X^*$ disappears immediately (again, just unbinding). $Y^*$ is still
present in quantity — protein levels don't collapse instantly — but it doesn't matter: because the
gate is AND, losing $X^*$ alone is enough to switch $Z$ off immediately, with no need to wait for
$Y^*$ to decay. So there is delay turning on, but **no delay turning off** — a "sign-sensitive
delay element."

<figure>
<svg viewBox="0 0 480 250" role="img" aria-label="Timing diagram of the AND-gated coherent type-1 feed-forward loop showing a delayed turn-on and an immediate turn-off">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="120" y1="10" x2="120" y2="230" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>
  <line x1="220" y1="10" x2="220" y2="230" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>
  <line x1="340" y1="10" x2="340" y2="230" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>

  <text x="10" y="34" font-size="12" fill="currentColor">Sx</text>
  <path d="M40,40 L120,40 L120,20 L340,20 L340,40 L440,40" fill="none" stroke="currentColor" stroke-width="2"/>

  <text x="10" y="89" font-size="12" fill="currentColor">X*</text>
  <path d="M40,95 L120,95 L120,75 L340,75 L340,95 L440,95" fill="none" stroke="currentColor" stroke-width="2"/>

  <text x="10" y="144" font-size="12" fill="currentColor">Y*</text>
  <path d="M40,150 L120,150 L220,120 L340,120 L420,150 L440,150" fill="none" stroke="currentColor" stroke-width="2"/>

  <text x="10" y="199" font-size="12" fill="currentColor">Z</text>
  <path d="M40,205 L220,205 L220,180 L340,180 L340,205 L440,205" fill="none" stroke="currentColor" stroke-width="2"/>

  <line x1="120" y1="12" x2="220" y2="12" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr)" marker-start="url(#arr)"/>
  <text x="170" y="8" text-anchor="middle" font-size="11" fill="currentColor">turn-on delay</text>

  <text x="340" y="245" text-anchor="middle" font-size="11" fill="currentColor">Sx off, X* off, Z off — together</text>
  <text x="120" y="245" text-anchor="middle" font-size="11" fill="currentColor">Sx on</text>
</svg>
<figcaption>Reconstruction of the AND-gated coherent type-1 loop's response to a pulse of Sx with Sy
already present. X* tracks Sx exactly. Y* must accumulate by transcription before it can rise, so Z
(which needs both) switches on late — but switches off the instant X* does, regardless of how much
Y* is still around.</figcaption>
</figure>

Switching the gate to **OR** flips which transition is delayed: now $X^*$ alone is enough to
switch $Z$ on, so turning $S_x$ on produces an *immediate* rise in $Z$; but when $S_x$ turns off,
$Y^*$ — already built up — is on its own sufficient to keep $Z$ on through the OR gate until $Y^*$
itself decays away, so **turning off is now delayed** instead.

And if instead $S_x$ is held on throughout and $S_y$ is what varies, with the AND gate: $X^*$ is
guaranteed present the whole time, so that half of the AND condition is always satisfied, and $Z$'s
behaviour collapses to simple direct regulation by $Y$ alone — no delay in either direction, because
the path through $X$ has become irrelevant.

This can be tested directly by putting $X$ and $Y$ each on its own inducible promoter and reading
out $Z$ by fluorescence as the two inputs are driven independently.

## The incoherent type-1 feed-forward loop: pulse and speed

Keep the same skeleton but make $Y$ a **repressor** of $Z$ instead of an activator: $X$ activates
$Y$, $X$ activates $Z$, $Y$ represses $Z$, and the two inputs to $Z$ combine as "$X^*$ present AND
$Y^*$ absent." This is the **incoherent type-1** feed-forward loop, the second most common type
after coherent type-1.

Trace it through: when $S_x$ turns on, $X^*$ appears immediately and $Z$ starts rising right away,
since $Y$ hasn't had time to accumulate and the "$Y^*$ absent" condition is still satisfied. But
$X^*$ is simultaneously driving $Y$'s transcription; once $Y^*$ builds up past its own threshold, it
starts repressing $Z$. The result is a **pulse**: $Z$ rises, then falls back down — partially or
almost completely, depending on how strong the repression turns out to be.

Define $t_{on}$ as the time to reach half of the eventual equilibrium level $Z_{eq}$, and compare
it to the $t_{on}$ that simple regulation (X directly driving Z, with no repressor Y at all) would
give — set purely by the ordinary accumulation curve. Because $Z$ rises unimpeded at first and only
later gets pulled down once $Y^*$ has caught up, it crosses its own half-maximum earlier than the
plain accumulation curve would, so $t_{on}$ is shorter than $t_{on,\text{simple}}$: the incoherent
loop **speeds up the turn-on response**, on exactly the same logic as negative autoregulation
(overshoot early, then get reined in) — except here the reining-in comes from a second gene product
rather than the gene repressing itself. Turning off, by contrast, is governed purely by $X^*$
disappearing once $S_x$ goes away, so $t_{off}$ is unaffected.

## Comparing strategies for a fast response

Several ways of shortening a response have now been seen, and they don't all speed up the same
half of it:

- **Shortening the protein's effective lifetime** (more degradation) shortens both $t_{on}$ and
  $t_{off}$, because the whole exponential relaxation, rising and falling, runs on that lifetime.
- **Negative autoregulation** shortens $t_{on}$ only: production overshoots before the
  not-yet-accumulated repressor throttles it back to steady state, but shutting off is unaffected —
  once production stops, the protein simply decays at its ordinary lifetime.
- **The incoherent type-1 feed-forward loop**, with partial repression, also shortens $t_{on}$
  only, and for the same reason: the early unimpeded rise beats the repression to the half-maximum
  mark, but turn-off still just tracks the fixed protein lifetime.

Underlying all three is a broader limit: anything routed through transcription runs on the cell
generation time / protein lifetime — minutes to tens of minutes at best — because turning a gene on
or off is only useful once enough protein has actually appeared or gone away, and both directions
cost transcription-and-translation time. When a cell needs to process information faster than that,
it has to fall back on networks of proteins that already exist, changing protein **state** (most
classically by phosphorylation) rather than protein **concentration** — a covalent modification of
an existing pool is far faster than making new protein.

## Single-input modules and temporal programs

Many metabolic and biosynthetic pathways are literally chains of enzymes $Z_1, Z_2, \dots, Z_n$,
each converting one molecule into the next. When such a pathway needs switching on, there is an
obvious reason to want the enzymes made in the order they're used rather than all at once. A
**single-input module (SIM)** is one transcription factor $X$ (often itself autoregulated, which
helps stabilize $X$'s own level) driving all of $Z_1,\dots,Z_n$ directly, with nothing else
regulating those targets.

"$X$ regulates many targets" by itself is not surprising — a high-out-degree hub is exactly what
the heavy-tailed degree distribution already predicts, and a degree-preserving null model keeps
that. What makes the SIM a real motif is the further, non-trivial fact that the targets are
regulated *only* by $X$; that exclusivity happens more often than chance (the lecture flags this
as a case where the right null model needs more thought than the obvious degree-preserving one).

Sequencing is achieved by giving each target a different activation threshold, $K_1 < K_2 <
\dots < K_n$: as $X$ rises smoothly from zero, it crosses $K_1$ first, switching on $Z_1$, then
$K_2$, switching on $Z_2$, and so on. The genes turn on in the chosen order purely because of where
their thresholds sit, all read off a single rising input.

<figure>
<svg viewBox="0 0 400 230" role="img" aria-label="X rising then falling through three ordered thresholds, turning genes on in order but off in reverse order">
  <line x1="40" y1="160" x2="380" y2="160" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>
  <line x1="40" y1="120" x2="380" y2="120" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>
  <line x1="40" y1="80" x2="380" y2="80" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>
  <text x="384" y="164" font-size="12" fill="currentColor">K1</text>
  <text x="384" y="124" font-size="12" fill="currentColor">K2</text>
  <text x="384" y="84" font-size="12" fill="currentColor">K3</text>

  <path d="M40,200 L150,40 L270,40 L380,200" fill="none" stroke="currentColor" stroke-width="2"/>

  <circle cx="67.5" cy="160" r="3" fill="currentColor"/>
  <circle cx="95" cy="120" r="3" fill="currentColor"/>
  <circle cx="122.5" cy="80" r="3" fill="currentColor"/>
  <circle cx="297.5" cy="80" r="3" fill="currentColor"/>
  <circle cx="325" cy="120" r="3" fill="currentColor"/>
  <circle cx="352.5" cy="160" r="3" fill="currentColor"/>

  <text x="95" y="215" text-anchor="middle" font-size="12" fill="currentColor">on: Z1, Z2, Z3</text>
  <text x="325" y="215" text-anchor="middle" font-size="12" fill="currentColor">off: Z3, Z2, Z1</text>
  <text x="200" y="20" text-anchor="middle" font-size="12" fill="currentColor">X(t)</text>
</svg>
<figcaption>A single-input module's shared thresholds turn genes on in order K1, K2, K3 as X rises,
but off in the reverse order K3, K2, K1 as X falls — the last gene switched on is the first switched
off (a LIFO queue).</figcaption>
</figure>

There is a real limit on how much delay this buys: because the whole scheme runs on the timescale
of $X$'s own accumulation — the generation time — the thresholds can't be spread across much more
than about one generation's worth of dynamic range without the ordering becoming unreliable near
the top of the trajectory. A slow developmental cascade, where each gene genuinely waits for the
previous one to be transcribed before switching on the next (paying a full generation-time cost at
every step), buys much longer delays, but at proportionally much greater cost in time — appropriate
for development, not for a pathway that needs to respond within minutes.

## Getting the order right: from LIFO to FIFO

As the figure above shows, when $X$ falls back toward zero it crosses the same thresholds in the
*opposite* order: it drops below the highest threshold $K_n$ first, switching $Z_n$ off first, and
only much later drops below $K_1$, switching $Z_1$ off last. A single-input module is therefore a
**last-in-first-out (LIFO)** queue: the gene switched on last is switched off first.

For a biosynthetic pathway, LIFO is exactly the wrong order. If the *last* enzyme in the chain,
$Z_n$, disappears first while the earlier enzymes are still active, the pathway keeps feeding
molecules into the final intermediate step with nothing left to convert it onward, and the
intermediates pile up. What is wanted, for the same reason $Z_1$ was wanted before $Z_2$ on the way
up, is $Z_1$ switched off first on the way down too — a **first-in-first-out (FIFO)** queue.

A single-input module can't give FIFO, because turn-on order and turn-off order are both read off
the same variable $X$, just traversed in opposite directions. Getting FIFO needs a second,
independently tunable set of thresholds, which is exactly what a feed-forward loop supplies. In a
**multi-output feed-forward loop**, $X$ drives $Y$ as well as every $Z_i$ directly, and $Y$ also
drives every $Z_i$, combined by an OR gate at each target — so each target carries two thresholds,
$K_i$ for $X$ and $K_i'$ for $Y$. Because $Y$ has to be transcribed by $X$, it lags behind $X$, so
at the start of the response it is $X$'s thresholds $K_1<K_2<\dots<K_n$ that decide the turn-on
order. Once $X$ falls away again, it is $Y$ — still present, and now the one keeping each target on
through the OR gate — whose thresholds $K_i'$ decide when each target actually switches off. Since
the $K_i$ and $K_i'$ are independent numbers, they can be set in *opposite* order: give the target
with the lowest $X$-threshold (turned on first) the highest $Y$-threshold, so that as $Y$ falls back
down it drops below that target's threshold first too, switching it off first; give the
last-turned-on target the lowest $Y$-threshold, so it is the last one $Y$ falls below, and hence the
last one switched off. The result is FIFO: the same order in as out. This is the mechanism proposed
for the flagellar biosynthesis pathway in *E. coli*, where the components are indeed both assembled
and later shut down in the same order.

## Sources

- Transcript: `recordings/zjtvmkge8-8.md` (MIT 8.591J, Fall 2014), the lecture's entire content —
  no slides or notes were supplied for this session, so every figure here is a reconstruction of the
  logic described verbally, not a reproduction of what was actually drawn on the board.
  - Subgraph counting, sparseness, the $\langle N_G\rangle$ formula and its $N^{n-g}$ scaling:
    [00:00]–[17:26].
  - The 42 vs $1.7\pm1.3$ (ER) vs $7\pm5$ (degree-preserving) comparison, the edge-swap algorithm,
    and the hub explanation: [17:26]–[27:21].
  - Alon's 2002 *Science* paper and the other networks it examined (C. elegans, food webs,
    circuits, the web): [27:21]–[29:34].
  - Coherent type-1 feed-forward loop, AND gate, OR gate, and the $S_y$-varied case: [29:34]–[42:54].
  - Incoherent type-1 feed-forward loop, the pulse, and $t_{on}$: [42:54]–[50:55].
  - Strategies for a fast response and why transcription is inherently slow: [50:55]–[58:36].
  - Single-input modules, sequencing by thresholds, and the generation-time limit: [58:36]–[1:08:26].
  - LIFO vs FIFO, the multi-output feed-forward loop, and the flagellar biosynthesis example:
    [1:08:26]–[1:21:02].
- Named in the lecture but not supplied as source material: the assigned reading from Uri Alon's
  textbook (the chapters on network motifs and feed-forward loops, and its chapter 5 on temporal
  programs, including its worked example on gene biosynthesis ordering and the arabinose-utilization
  example of a signal acting on a transcription factor); Alon, "Network motifs: Simple Building
  Blocks of Complex Networks," *Science* (2002), cited by name and year but not itself provided; and
  a paper by Sunney Xie, assigned as reading for the next lecture and not otherwise identified in
  the transcript.

---

[Contents](index.md) · [2. Stochastic Gene Expression Bursts →](02-stochastic-gene-expression-bursts.md)

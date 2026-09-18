---
title: "6. OLC and de Bruijn Assembly"
course: "MIT 7.091J"
chapter: 6
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 6. OLC and de Bruijn Assembly

## What this covers

Whole-genome shotgun sequencing hands you millions of short, overlapping DNA reads and tells you
nothing about where in the genome each one came from. This chapter covers the resulting assembly
problem: how to reconstruct a genome from such a pile of unplaced, overlapping fragments. It builds
the idea of sequencing *coverage* and the classical Lander–Waterman estimate of how much of a genome
a given amount of sequencing will miss, then works through the two standard assembly strategies —
overlap-layout-consensus and de Bruijn-graph assembly — including the graph-theoretic shortcut (an
Eulerian walk) that makes the second one fast, and the precise reason repeated sequence breaks that
shortcut. It assumes only elementary directed-graph vocabulary, reviewed along the way, and the
Poisson approximation to a count of rare, independent events.

## Shotgun sequencing and the assembly problem

Whole-genome "shotgun" sequencing starts by copying the genome many times over and then fragmenting
each copy at random positions — "shotgun" because the breaks fall as if the DNA had been fired from
a shotgun. A genome such as

$$\texttt{GGCGTCTATATCTCGGCTCTAGGCCCTCATTTTTT}$$

is copied several times, and each copy is cut into pieces at different random places, so that the
same stretch of genome ends up sequenced more than once, as several different, overlapping
fragments (reads).

If sequencing produced so many fragments that every position were covered several times over, *and*
we additionally knew where each fragment sat, reconstruction would be trivial: lay the fragments
down at their true coordinates and read off the sequence. The real difficulty is the second
assumption failing completely — a sequencer reports only the fragment sequences, never their
genomic coordinates. Assembly is the problem of taking a large set of short, overlapping, but
*unplaced* reads and finding an ordering of them that reproduces the original sequence, using only
the fact that two reads which genuinely overlap must share a run of matching sequence at one read's
end and the other's beginning.

## Coverage, and how much of the genome we can expect to miss

*Coverage* is used in two related senses. The **average coverage** of a sequencing project is the
average number of reads covering a genome position — equivalently, the total number of sequenced
bases divided by the genome length. In one worked example, ten reads totalling 177 nucleotides were
laid down over a 35-nucleotide stretch of genome, giving an average coverage of $177/35 \approx 7\times$.
**Coverage at a position** is the local version: the number of reads that happen to overlap one
particular base. In the same example, a single marked position was covered by six of the ten reads.

<figure>
<svg viewBox="0 0 400 210" role="img" aria-label="A stretch of genome with many overlapping reads above it, and a marked position crossed by several of them">
  <line x1="40" y1="185" x2="360" y2="185" stroke="currentColor" stroke-width="2"/>
  <text x="200" y="203" text-anchor="middle" font-size="12" fill="currentColor">genome</text>
  <line x1="60" y1="40" x2="260" y2="40" stroke="currentColor" stroke-width="3"/>
  <line x1="100" y1="55" x2="300" y2="55" stroke="currentColor" stroke-width="3"/>
  <line x1="140" y1="70" x2="240" y2="70" stroke="currentColor" stroke-width="3"/>
  <line x1="170" y1="85" x2="320" y2="85" stroke="currentColor" stroke-width="3"/>
  <line x1="190" y1="100" x2="260" y2="100" stroke="currentColor" stroke-width="3"/>
  <line x1="120" y1="115" x2="210" y2="115" stroke="currentColor" stroke-width="3"/>
  <line x1="40" y1="130" x2="120" y2="130" stroke="currentColor" stroke-width="3"/>
  <line x1="260" y1="145" x2="350" y2="145" stroke="currentColor" stroke-width="3"/>
  <line x1="200" y1="25" x2="200" y2="185" stroke="orange" stroke-width="2" stroke-dasharray="4 3"/>
  <text x="200" y="16" text-anchor="middle" font-size="12" fill="currentColor">one position</text>
</svg>
<figcaption>Reads (bars) scattered at random over a stretch of genome. Coverage at the marked
position is the number of bars it crosses; the average of that count over every position is the
average coverage.</figcaption>
</figure>

Treating the number of reads landing on a given base as approximately Poisson lets this be turned
into a prediction. With $G$ the genome size, $N$ the number of reads and $L$ the read length, the
total sequenced length is $NL$, so

$$\lambda = \frac{NL}{G}$$

is the average coverage. Approximating the count of reads covering one base as $\text{Poisson}(\lambda)$,
the chance that base is covered by *no* read is the zero term of that distribution,
$\text{Poisson}(0,\lambda) = e^{-\lambda}$. Multiplying by the genome length gives the expected number
of uncovered bases,

$$\#\text{uncovered bases} \approx G e^{-\lambda},$$

and the expected number of separate gaps (maximal uncovered stretches) is estimated the same way,

$$\#\text{gaps} \approx N e^{-\lambda}.$$

This is the classical Lander–Waterman calculation: it says that pushing $\lambda$ up (sequencing
more, or sequencing longer reads) drives the uncovered fraction of the genome down exponentially,
which is why assembly projects aim for coverage well above $1\times$ — typical projects run at
$\lambda \approx 30$–$50$.

## Why overlapping reads don't quite agree

Two reads that truly come from overlapping stretches of the genome will not always match exactly:

```
TATCTCGACTCTAGGCC
||||||| ||||||||
TCTATATCTCGGCTCTAGG
```

There are two distinct reasons for a mismatch like the one marked above. The first is **sequencing
error**: the machine simply misread a base. The second is genuine **biological difference between
the two copies of a chromosome an organism carries** — humans are diploid, with one copy of each
chromosome inherited from each parent, and the two copies can differ at a site:

```
Read from Mother:        TATCTCGACTCTAGGCC
Read from Father:   TCTATATCTCGGCTCTAGG
```

Real assemblers have to reason about which explanation applies; this chapter mostly sets ploidy
aside and treats a genome as a single sequence, flagging the two places — matching reads into an
overlap graph, and calling a consensus base — where ploidy and error actually have to be confronted.

## Two strategies for assembling reads

There are two dominant approaches to turning a pile of reads into contigs, and eventually, using
information from paired reads, into longer *scaffolds*:

- **Overlap-layout-consensus (string graph) assembly** builds a graph directly from the reads
  themselves, connecting reads that overlap, eliminates redundant reads, and traces a path through
  the graph to assemble. Examples: SGA, Fermi.
- **De Bruijn-graph assembly** breaks every read into short, fixed-length substrings (*k*-mers),
  builds a graph out of those instead, and discards the original reads. Examples: Velvet, ABySS,
  SOAPdenovo.

Both end in the same place: contigs produced by either method are linked into scaffolds using read
pairs (two reads sequenced from the two ends of the same larger fragment, so their separation in the
genome is roughly known), and scaffolds are then mapped to build a genome map.

## Overlap-layout-consensus

OLC is a three-stage pipeline: **overlap**, build a graph connecting reads that overlap; **layout**,
bundle stretches of that graph into contigs; **consensus**, pick the most likely nucleotide sequence
for each contig.

### Overlap: building the graph

Finding all pairwise overlaps is the same as building a *directed graph* in which each read is a
node and a directed edge connects two reads whenever the suffix of one is similar to the prefix of
the other (as in the mismatched pair above). Recall the vocabulary: a directed graph $G(V,E)$ has a
set of vertices $V$ and a set of directed edges $E$, each edge an *ordered* pair of vertices — its
*source* and its *sink*. A vertex is drawn as a circle, an edge as an arrow between two circles.

### Layout: turning the graph into contigs

Once the overlap graph is built, many of its edges are redundant: if read $abc$ overlaps $bcd$ and
$bcd$ overlaps $cde$, an edge directly from $abc$ to $cde$ is *transitively inferrible* from the
other two and can be dropped without losing information — $abc \to bcd \to cde$ already implies it.
Removing such edges, first the ones that skip one node, then the ones that skip two, simplifies a
tangled overlap graph into much shorter chains.

Once simplified, each non-branching stretch of the graph is emitted as a contig. A short example
makes the branching case vivid: reads assembled from the phrase *"to everything there is a season,
turn, turn, turn"* produce one contig `to_every_thing_turn_` and a second contig
`turn_there_is_a_season`, because the repeated word `turn_` is a branch point the layout step cannot
resolve — it cannot tell how many times "turn" repeats or which copy connects to which neighbour.
This is an **unresolvable repeat**, and it is the single biggest obstacle to producing one contig per
chromosome rather than many short ones.

Layout also has to cope with spurious structure caused by sequencing error: a read that matches well
for a stretch and then diverges abruptly, rather than continuing to a sensible endpoint, looks like
either a real repeat boundary or a bad read. Since the divergent path ends abruptly rather than
merging back into the graph, it is reasonable to conclude it is an error and *prune* it, discarding
that branch.

### Consensus: calling the sequence

With contigs delineated, the reads that make up one contig are lined up, and the base at each column
is called by majority vote:

```
TAGATTACACAGATTACTGA  TTGATGGCGTAA CTA
TAGATTACACAGATTACTGACTTGATGGCGTAAACTA
TAG TTACACAGATTATTGACTTCATGGCGTAA CTA
TAGATTACACAGATTACTGACTTGATGGCGTAA CTA
TAGATTACACAGATTACTGACTTGATGGCGTAA CTA
                    ↓
TAGATTACACAGATTACTGACTTGATGGCGTAA CTA
```

The same two complications as before reappear here. Sequencing error means a wrong base can
outweigh the truth at low coverage. Ploidy means that a majority vote is not always well-posed at
all: if the true genotype at a site is heterozygous, say **AG**, and only about six noisy reads
cover it, "majority vote" has to decide between calling a single (wrong) consensus base and calling
a genuine two-allele site — a genuinely harder question than picking the most common letter.

### The cost of OLC

Building the overlap graph is the expensive step: every read has, in principle, to be compared
against every other read for a possible overlap. Second-generation sequencing datasets run to
hundreds of millions or billions of reads and hundreds of billions of sequenced nucleotides total,
and it is this scale — not the layout or consensus steps — that makes plain OLC assembly slow.

## De Bruijn-graph assembly

De Bruijn-graph (DBG) assembly is built on a different, cheaper notion of overlap. It is
conceptually similar to full-read overlap, but its structure has properties that make it easier to
traverse efficiently — at the cost of throwing away information that OLC keeps.

### *k*-mers and how the graph is built

A **$k$-mer** is a substring of length $k$ ("mer" from the Greek for "part"). For $S = \texttt{GGCGATTCATCG}$,
`ATTC` is a 4-mer, and the ten 3-mers of $S$ are `GGC`, `GCG`, `CGA`, `GAT`, `ATT`, `TTC`, `TCA`,
`CAT`, `ATC`, `TCG`. Write "$(k-1)$-mer" for a substring of length $k-1$: every $k$-mer has a *left*
$(k-1)$-mer (drop its last base) and a *right* $(k-1)$-mer (drop its first base) — for $k=3$,
`AAB`'s left 2-mer is `AA` and its right 2-mer is `AB`.

The construction: take every $k$-mer from the reads, split each into its left and right $(k-1)$-mer,
let $(k-1)$-mers be the *nodes* of a new graph, and for every $k$-mer draw a directed edge from its
left $(k-1)$-mer to its right $(k-1)$-mer. Each edge corresponds to exactly one $k$-mer from the
input, and it represents an overlap of length $k-2$ between two $(k-1)$-mers.

Worked over a toy two-letter alphabet, the input string `AAABBBA` yields the 3-mers `AAA`, `AAB`,
`ABB`, `BBB`, `BBA`, which split into the left/right 2-mer pairs `AA,AA`, `AA,AB`, `AB,BB`, `BB,BB`,
`BB,BA`. The resulting graph has four nodes:

<figure>
<svg viewBox="0 0 400 200" role="img" aria-label="De Bruijn graph on the 2-mers AA, AB, BB, BA built from the string AAABBBA">
  <defs>
    <marker id="arr1" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 7 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="60" cy="120" r="26" fill="orange" fill-opacity="0.25" stroke="currentColor" stroke-width="1.5"/>
  <text x="60" y="125" text-anchor="middle" font-size="13" fill="currentColor">AA</text>
  <circle cx="180" cy="60" r="26" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="180" y="65" text-anchor="middle" font-size="13" fill="currentColor">AB</text>
  <circle cx="300" cy="120" r="26" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="300" y="125" text-anchor="middle" font-size="13" fill="currentColor">BB</text>
  <circle cx="360" cy="170" r="26" fill="orange" fill-opacity="0.25" stroke="currentColor" stroke-width="1.5"/>
  <text x="360" y="175" text-anchor="middle" font-size="13" fill="currentColor">BA</text>
  <path d="M 40 100 A 22 22 0 1 1 40 140" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr1)"/>
  <text x="10" y="122" font-size="11" fill="currentColor">AAA</text>
  <line x1="80" y1="105" x2="158" y2="72" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr1)"/>
  <text x="100" y="80" font-size="11" fill="currentColor">AAB</text>
  <line x1="202" y1="72" x2="278" y2="108" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr1)"/>
  <text x="230" y="80" font-size="11" fill="currentColor">ABB</text>
  <path d="M 285 98 A 22 22 0 1 1 285 142" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr1)"/>
  <text x="240" y="120" font-size="11" fill="currentColor">BBB</text>
  <line x1="320" y1="132" x2="345" y2="155" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr1)"/>
  <text x="330" y="160" font-size="11" fill="currentColor">BBA</text>
</svg>
<figcaption>The de Bruijn graph for AAABBBA, k = 3: nodes AA and BA (shaded) are semi-balanced,
nodes AB and BB are balanced. AA → AA → AB → BB → BB → BA walks every edge once.</figcaption>
</figure>

If the input instead contained an extra repeat of `B`, e.g. `AAABBBBA`, the same construction would
add a second, parallel edge between `BB` and itself — a **multiedge** — since the $k$-mer `BBB`
would now occur twice.

For real genome assembly, each $k$-mer is additionally recorded as a "twin" pair: one node for the
$k$-mer as read, one for its reverse complement (since either DNA strand could have been
sequenced). $k$ is chosen odd so that no $k$-mer can equal its own reverse complement. Twin nodes
are usually left out of illustrations to reduce clutter — they are omitted here too.

### Eulerian walks

The reason this construction is useful is a classical graph-theory fact. A few definitions first:

- A node is **balanced** if its indegree equals its outdegree.
- A node is **semi-balanced** if indegree and outdegree differ by exactly $1$.
- A graph is **connected** if every node is reachable from some other node.
- An **Eulerian walk** is a walk that traverses every *edge* exactly once. A graph that has one is
  called **Eulerian**.

The key theorem (Jones and Pevzner, §8.8): *a directed, connected graph is Eulerian if and only if
it has at most two semi-balanced nodes and every other node is balanced.* In the toy graph above,
`AA` and `BA` are semi-balanced and `AB`, `BB` are balanced, so the graph is Eulerian — consistent
with the explicit walk `AA → AA → AB → BB → BB → BA` traversing every edge exactly once.

This matters because, with **perfect sequencing** — every length-$k$ substring of the genome
sequenced exactly once, with no errors — the de Bruijn graph built this way is *always* Eulerian,
and an Eulerian walk can be found efficiently. The reason follows directly from the balance
definitions: an interior $(k-1)$-mer occurs as a left-mer exactly as often as it occurs as a
right-mer (once for every internal occurrence in the genome), so it is balanced; the $(k-1)$-mer at
the genome's left end is only ever a left-mer, giving it one more outgoing edge than incoming, and
symmetrically the $(k-1)$-mer at the right end has one more incoming edge than outgoing — exactly
the two semi-balanced nodes the theorem allows (unless the genome is circular, in which case there
is no free end and the graph is fully balanced).

### Repeats break the correspondence

An Eulerian walk can be found efficiently, but that does not mean it is unique, and when it is not
unique, only one of the possible walks corresponds to the true genome. Consider the graph built from
`ZABCDABEFABY` with $k=3$:

<figure>
<svg viewBox="0 0 400 220" role="img" aria-label="Two cycles sharing the node AB, showing why a repeated substring produces more than one Eulerian walk">
  <defs>
    <marker id="arr2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 7 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="40" cy="110" r="20" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="40" y="115" text-anchor="middle" font-size="12" fill="currentColor">ZA</text>
  <circle cx="200" cy="110" r="24" fill="orange" fill-opacity="0.25" stroke="currentColor" stroke-width="1.5"/>
  <text x="200" y="115" text-anchor="middle" font-size="13" fill="currentColor">AB</text>
  <circle cx="360" cy="110" r="20" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="360" y="115" text-anchor="middle" font-size="12" fill="currentColor">BY</text>
  <circle cx="150" cy="40" r="18" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="150" y="45" text-anchor="middle" font-size="11" fill="currentColor">BC</text>
  <circle cx="250" cy="40" r="18" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="250" y="45" text-anchor="middle" font-size="11" fill="currentColor">CD</text>
  <circle cx="295" cy="75" r="18" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="295" y="80" text-anchor="middle" font-size="11" fill="currentColor">DA</text>
  <circle cx="150" cy="180" r="18" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="150" y="185" text-anchor="middle" font-size="11" fill="currentColor">BE</text>
  <circle cx="250" cy="180" r="18" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="250" y="185" text-anchor="middle" font-size="11" fill="currentColor">EF</text>
  <circle cx="295" cy="145" r="18" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="295" y="150" text-anchor="middle" font-size="11" fill="currentColor">FA</text>
  <line x1="60" y1="110" x2="176" y2="110" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr2)"/>
  <line x1="188" y1="93" x2="162" y2="52" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr2)"/>
  <line x1="168" y1="40" x2="232" y2="40" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr2)"/>
  <line x1="264" y1="48" x2="286" y2="63" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr2)"/>
  <line x1="283" y1="88" x2="217" y2="103" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr2)"/>
  <line x1="188" y1="127" x2="162" y2="168" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr2)"/>
  <line x1="168" y1="180" x2="232" y2="180" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr2)"/>
  <line x1="264" y1="172" x2="286" y2="157" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr2)"/>
  <line x1="283" y1="132" x2="217" y2="117" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr2)"/>
  <line x1="224" y1="110" x2="340" y2="110" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr2)"/>
</svg>
<figcaption>Node AB (shaded) is shared by two edge-disjoint cycles — BC→CD→DA and BE→EF→FA — because
the substring AB occurs three times in ZABCDABEFABY. Both orders of traversing the two loops between
entering at ZA and leaving at BY are Eulerian walks, but only one is the true genome.</figcaption>
</figure>

Two distinct Eulerian walks exist:

$$\texttt{ZA} \to \texttt{AB} \to \texttt{BE} \to \texttt{EF} \to \texttt{FA} \to \texttt{AB} \to \texttt{BC} \to \texttt{CD} \to \texttt{DA} \to \texttt{AB} \to \texttt{BY}$$

$$\texttt{ZA} \to \texttt{AB} \to \texttt{BC} \to \texttt{CD} \to \texttt{DA} \to \texttt{AB} \to \texttt{BE} \to \texttt{EF} \to \texttt{FA} \to \texttt{AB} \to \texttt{BY}$$

Both traverse every edge exactly once; only one of them matches how the two loops actually sit in
`ZABCDABEFABY`. The node `AB` is a **repeat** — it is the point where two edge-disjoint cycles meet
— and it is the repeat, not any flaw in the graph, that produces the ambiguity. This is the first
sign that finding *an* Eulerian walk is not the same as solving assembly.

### What real sequencing does to the graph

The perfect-sequencing argument for an Eulerian graph relies on assumptions that never quite hold:

- **Gaps in coverage** disconnect the graph. If a $k$-mer that should have been sequenced is
  missing, the graph built from `a_long_long_long_time` ($k=5$) splits into separate pieces — each
  piece is individually Eulerian, but the graph as a whole is not, so the assembler emits it as
  several contigs instead of one.
- **Uneven coverage** breaks the balance argument even without disconnecting anything: an extra,
  spurious copy of a $(k-1)$-mer (say, an extra `ong_t`) creates four semi-balanced nodes instead of
  two, and the theorem's condition fails.
- **Sequencing errors and real biological differences between chromosome copies** act like small
  repeats or gaps: a single substitution error (turning a copy of `long_` into `lxng_`) again
  disconnects the graph and leaves its largest component non-Eulerian.

### Cost of construction, and edge weights

Building the graph is cheap. For each $k$-mer, the construction adds one edge and up to two nodes;
if $(k-1)$-mers are encoded as hash-map keys that fit in $O(1)$ machine words, both querying and
inserting a key is $O(1)$ expected work, so one $k$-mer costs $O(1)$ expected work and $N$ reads cost
$O(N)$ overall. Timing the construction on progressively longer prefixes of the lambda phage genome
($k=14$) confirms this scaling in practice.

At typical project coverage ($\lambda \approx 30$–$50$), the same edge is added many times over —
once per occurrence of its $k$-mer. Rather than keep that many parallel edges, real implementations
keep one **weighted** edge per *distinct* $k$-mer, where the weight is the number of times that
$k$-mer occurs. This makes coverage information (how many times a given edge is supported) available
directly on the graph, which is exactly what is needed for the error-correction step below.

### Cleaning the graph up: topology-based error correction

Coverage and weight let the assembler recognise several characteristic shapes left by error, and
correct them using the graph's topology alone:

- **Errors near the end of a read** produce short, low-coverage dead-end branches — *tips* — which
  are trimmed off.
- **Errors in the middle of a read** produce a short detour that rejoins the main path a few
  $k$-mers later, forming a *bubble* of two near-identical parallel paths; the low-coverage path is
  popped, leaving the better-supported one.
- **Chimeric edges** — spurious joins with little support — are dealt with by clipping short,
  low-coverage nodes and edges outright.

### The OLC/DBG tradeoff

De Bruijn-graph assembly's main advantage is **speed and simplicity**: building it costs $O(N)$ and
avoids the all-against-all comparison that makes OLC slow. The price is information lost by chopping
every read into $k$-mers before doing anything else:

- Because reads are split immediately, a de Bruijn graph cannot resolve repeats as well as an
  overlap graph built from full-length reads can — a read that happens to span an entire repeat and
  a bit of unique sequence on each side carries information a $k$-mer window shorter than the repeat
  does not.
- Only a very specific, exact-match notion of "overlap" (sharing a $(k-1)$-mer) is considered,
  which makes handling errors more complicated than in OLC's more flexible alignment-based overlap.
- **Read coherence is lost.** Because the graph is built from $k$-mers rather than reads, some paths
  through it are consistent with the graph's edges but not with any actual input read. Recovering
  that lost information requires *threading* the original reads back through the graph afterwards.

## Evaluating an assembly: N50 and a real comparison

Assemblies are commonly summarised by their **N50**: sort the contigs (or scaffolds) by length from
longest to shortest, and find the length $L$ such that contigs of length $L$ or greater together
account for at least half the total assembled sequence. N50 is a single number that rewards long
contigs much more than a plain average length does, since a handful of very short leftover contigs
barely move it.

The following comparison, from Simpson and Durbin's SGA paper, applies one OLC assembler (SGA) and
three de Bruijn-graph assemblers (Velvet, ABySS, SOAPdenovo, at three different values of $k$) to the
same simulated *C. elegans* dataset (100 Mbase genome, 33.8 million read pairs, 100 bp reads at each
end, 250 bp insert size):

| | SGA (OLC) | Velvet (DBG, $k=61$) | ABySS (DBG, $k=67$) | SOAPdenovo (DBG, $k=59$) |
|---|---|---|---|---|
| Scaffold N50 | 26.3 kbp | 31.3 kbp | 23.8 kbp | 31.1 kbp |
| Aligned contig N50 | 16.8 kbp | 13.6 kbp | 18.4 kbp | 16.0 kbp |
| Mean aligned contig size | 4.9 kbp | 5.3 kbp | 6.0 kbp | 5.6 kbp |
| Sum aligned contig size | 96.8 Mbp | 95.2 Mbp | 98.3 Mbp | 95.4 Mbp |
| Reference bases covered | 96.2 Mbp | 94.8 Mbp | 95.9 Mbp | 95.1 Mbp |
| Reference covered by contigs $\ge$ 1 kb | 93.0 Mbp | 92.1 Mbp | 93.9 Mbp | 92.3 Mbp |
| Mismatch rate, all assembled bases | 1 / 21,545 bp | 1 / 8,786 bp | 1 / 5,577 bp | 1 / 26,585 bp |
| Mismatch rate, bases in all four assemblies | 1 / 82,573 bp | 1 / 18,012 bp | 1 / 8,209 bp | 1 / 81,025 bp |
| Contigs with split/bad alignment | 458 (4.4 Mbp) | 787 (7.2 Mbp) | 638 (9.1 Mbp) | 483 (4.4 Mbp) |
| Total CPU time | 41 h | 2 h | 5 h | 13 h |
| Max memory usage | 4.5 GB | 23.0 GB | 14.1 GB | 38.8 GB |

No single method wins on every measure: the de Bruijn-graph assemblers are much faster and lighter
here in wall-clock CPU time, but the OLC assembler (SGA) has the lowest mismatch rate and the fewest
badly-aligned contigs, at roughly ten times the CPU cost and a fraction of the memory. This is a
concrete instance of the tradeoff argued for above — de Bruijn methods win on speed, OLC wins on
accuracy of the sequence it does produce — and it is why the choice between them in practice depends
on what a project can afford. On a real human genome (NA12878, $1.2 \times 10^9$ reads, $40\times$
coverage), the same SGA assembler was reported to produce contigs covering about 95% of the
autosomes and chromosome X.

## Sources

- Slides: `lectures/06-slides/01-lecture-6.md` and
  `lectures/06-slides/02-n50---contig-scaffold-length-or-larger-that-contains-50-of-b.md`,
  MIT OCW 7.91J *Foundations of Computational and Systems Biology* (Spring 2014), Lecture 6,
  "Genome Assembly," David K. Gifford. No transcript, notes or exercise set was supplied for this
  lecture — the chapter is built entirely from the slide deck.
- The slide markdown is machine-reconstructed from a PDF with no text layer (`fidelity:
  reconstructed`); the source file itself flags that its prose is a paraphrase in places and that
  every equation is unverified against the original. The Lander–Waterman formulas and the N50 table
  above should be checked against `sources/ocw-7091j/lectures/06-slides.pdf` before being quoted
  elsewhere.
- The N50 comparison table and the NA12878 coverage figure are drawn from Simpson, J. T., and
  Durbin, R., "Efficient De Novo Assembly of Large Genomes using Compressed Data Structures,"
  *Genome Research* 22, no. 3 (2012): 549–56 — cited on the slides but not itself supplied as
  source material here.
- The Eulerian-walk theorem is attributed on the slides to Jones and Pevzner, §8.8 (not supplied).
- The graph-topology error-correction slide is credited to a presentation by Michael Schatz (not
  supplied), and the *de novo* shotgun-assembly overview diagram and the OLC/DBG pipeline diagram
  are credited respectively to Nature Education (Adams, J., 2008, and Green, E. D., *Nature Reviews
  Genetics* 2, no. 8 (2001): 573–83) and to Ben Langmead's teaching materials
  (langmead-lab.org/teaching-materials) — none of which were supplied as source material, only
  named on the slides. A flowchart and a table referenced later in the deck are marked in the
  source as removed for copyright and are not reconstructed here.

---

[← 5. Backtracking Search for Read Alignment](05-backtracking-search-for-read-alignment.md) · [Contents](index.md) · [7. ChIP-seq Peak Calling and Reproducibility →](07-chip-seq-peak-calling-and-reproducibility.md)

---
title: "6. OLC and De Bruijn Assembly"
course: "MIT 7.091J"
chapter: 6
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-10-01"
---

> **Lecture notes.** Written from the material of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 6. OLC and De Bruijn Assembly

## What this covers

How do you reconstruct a genome from a machine that only reads it in short, unordered fragments?
This chapter covers *de novo* whole-genome shotgun assembly: the pipeline from reads to contigs to
scaffolds, the coverage statistics that describe how good a read set is, and the two dominant
strategies for turning overlapping reads into sequence — overlap-layout-consensus (OLC) and
de Bruijn graph (DBG) assembly. It assumes the FM-index / Burrows-Wheeler read-indexing machinery
from the previous lecture, and basic directed-graph vocabulary (vertex, edge, indegree, outdegree),
which is reviewed briefly along the way.

## The assembly pipeline: reads to a genome map

Sequencing a genome does not read it start to finish. Contemporary short-read instruments start
from a single copy of the genome, make many copies of it, and shear those copies into fragments —
"shotgun" sequencing, because the fragmentation is as indiscriminate as buckshot. Each fragment is
read, producing a huge, unordered pile of short sequences. The job of assembly is to glue the pile
back into something resembling the original genome, by finding the overlaps that reveal which reads
sit next to which.

The standard pipeline has several stages:

- **Reads** are assembled into **contigs**, contiguous stretches of sequence believed to be
  completely covered and correctly ordered.
- Contigs are joined into **scaffolds** using the fact that each read actually comes from a *read
  pair* — both ends of a longer molecule are sequenced, so a pair can jump across a region with no
  read coverage at all, even though the sequence in that gap stays unknown.
- Scaffolds are tied to **physical locations** on chromosomes (for example using PCR-based sequence
  tag sites), producing a **genome map**.

This chapter is about the first step, reads to contigs, where the algorithmic content lives.

A genome can be assembled **de novo** — from scratch, with no prior reference — or
**reference-guided**, by mapping reads onto an existing reference genome of a related or identical
individual. Reference-guided assembly is much easier, but fails badly in the presence of large
structural variation between the individual sequenced and the reference. This lecture is about
de novo assembly, which must work without any such crutch.

## Coverage and the Lander-Waterman estimate

**Coverage** (more precisely, *average coverage*) is the average number of reads overlapping a
given base of the genome. If a genome of 35 nucleotides is covered by reads totalling 177
nucleotides, the average coverage is

$$\text{average coverage} = 177/35 \approx 7\times.$$

A different, related notion is **coverage at a position**: the number of reads that happen to span
one particular base, which varies from base to base even when the average is fixed.

Before sequencing a genome, it is useful to estimate how much of it will be left uncovered by gaps
in the read set — the **Lander-Waterman** calculation. Let $G$ be the genome size, $N$ the number of
reads, and $L$ the read length. Then

$$\lambda = \frac{NL}{G}$$

is the average coverage (reads per base). Treating the number of reads landing on a given base as
Poisson with mean $\lambda$, the probability a base is covered by *zero* reads is
$P(\text{uncovered}) \approx e^{-\lambda}$. From this, the expected number of uncovered bases is
$\approx G e^{-\lambda}$, and — reasoning that every read boundary is a candidate place for a gap —
the expected number of gaps in the assembly is $\approx N e^{-\lambda}$.

Checked against real 1000 Genomes read sets, the rule tracks some libraries well but not others:
some need noticeably more reads than predicted to reach the same coverage. The Poisson model
assumes reads land uniformly at random; real libraries have **skew** from amplification bias, which
a negative binomial model (allowing extra variance) fits better than a pure Poisson.

A separate complication, independent of coverage, is that two reads truly from overlapping
stretches of genome need not agree at every position, for two common reasons: **sequencing error**
(a wrong base call, which quality scores can help flag), and **allelic difference** — in a diploid
organism the read could come from the maternal or paternal chromosome copy, and the two can
genuinely differ. A standard reference genome ignores this and reports one haploid consensus;
assembling an actual diploid genome, keeping both parental sequences distinct, needs different,
more careful techniques.

## Two strategies for turning reads into contigs

Two families of de novo assembler dominate short-read assembly:

- **Overlap-layout-consensus (OLC)**, also called **string graph** assembly, builds a graph directly
  from the reads, eliminates redundant reads, and traces a path through the graph. Examples: SGA,
  Fermi.
- **De Bruijn graph (DBG)** assembly instead chops every read into fixed-length *k*-mers, builds a
  graph of those *k*-mers, and discards the original reads. Examples: Velvet, ABySS, SOAPdenovo.

OLC assemblers were used first, in the Human Genome Project, when reads were longer. As read
counts grew into the hundreds of millions, OLC's historical weakness — the apparent cost of finding
all pairwise overlaps — pushed people toward de Bruijn graphs, which are cheaper to build but throw
away information. That trade-off, speed versus information kept, runs through the whole lecture.

## Overlap-layout-consensus assembly

OLC has three stages: **overlap** (build a graph connecting reads that overlap), **layout**
(collapse that graph into contigs), and **consensus** (call one sequence per contig).

### Overlap: building the graph

An **overlap graph** is a directed graph $G(V, E)$: vertices $V$ (here, reads) and directed edges
$E$, each an ordered pair (source, sink). An edge is drawn whenever the suffix of one read matches
the prefix of another — the source read's tail overlaps the sink read's head. The graph can
genuinely be cyclic, either because the chromosome is circular or because a repeat in a linear
chromosome makes the overlap structure loop back on itself.

Finding every overlap by comparing all pairs of reads costs $O(N^2)$, hopeless at hundreds of
millions of reads. The efficient alternative reuses the FM-index / Burrows-Wheeler machinery from
the previous lecture: index all the reads (roughly $O(N\log N)$), then for any read, look up its
suffix or prefix directly in the index to find every overlapping read, tracing until the overlap
runs out. A further benefit of this approach (taken by Simpson et al.'s SGA) is that it never
generates the *transitive* edges described next — they are simply never produced, rather than
produced and later deleted.

### Layout: from overlap graph to contigs

The raw overlap graph is cluttered with **transitively-inferable edges**: if read $a$ overlaps $b$,
$b$ overlaps $c$, and $a$ also overlaps $c$ directly, that third edge adds no information beyond
what $a\!\to\! b\!\to\! c$ already implies, and can be removed. Repeating this — first removing edges
that skip one node, then edges that skip two — simplifies a messy graph into near-linear stretches,
from which **contigs** are emitted as the non-branching runs.

To make "layout" precise: the **shortest common superstring (SCS)** of a set of strings is the
shortest string containing every one of them as a substring. Without "shortest," satisfying
"contains every string" is trivial — concatenate them all. Minimizing length is exactly equivalent
to maximizing total overlap along a path through the overlap graph, so SCS becomes the problem of
finding the path that **minimizes total (negated) overlap cost** — an instance of the **travelling
salesman problem**, hence NP-hard. Even without weights, finding a path visiting every node once is
the **Hamiltonian path** problem, also NP-complete. So real assemblers use a **greedy heuristic**
instead: repeatedly merge the pair of strings with the largest remaining overlap. It is known to
produce an answer at most $2.5\times$ longer than the true shortest superstring — a guarantee, but
"cold comfort," since it says nothing about whether the reconstructed sequence is *correct*.

**Repeats are where greedy SCS goes wrong.** Given a genome with a repeated word and reads too short
to span it, the greedy algorithm can produce a string *shorter* than the true genome, because
identical-looking reads collapse into one copy rather than the true several. On the overlap graph,
the same failure looks like this: one path gives total overlap 39 and faithfully reproduces the
original string, but a *different* path gives strictly *larger* total overlap — a shorter,
*wrong* string. More overlap is not more correct; only reads long enough to span the repeat fix
this. A worked sentence example made the point concretely: greedy-assembling "It was the best of
times, it was the worst of times" fails until the read length reaches 13 characters.

The general shape of the problem: if a repeat sits between two stretches of unique sequence, and no
read spans all the way across it, an assembler can see where unique sequence gives way to repeat on
each side, but cannot tell how the flanks pair up or how many copies of the repeat lie between them.

<figure>
<svg viewBox="0 0 400 220" role="img" aria-label="Two unique flanks on each side of a shared repeat region, with no way to tell which left flank connects to which right flank">
  <defs>
    <marker id="arrowR" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0L10,5L0,10z" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="160" y="80" width="80" height="60" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="200" y="115" text-anchor="middle" font-size="12" fill="currentColor">repeat</text>
  <circle cx="60" cy="60" r="24" fill="none" stroke="currentColor"/>
  <text x="60" y="65" text-anchor="middle" font-size="12" fill="currentColor">U1</text>
  <circle cx="60" cy="160" r="24" fill="none" stroke="currentColor"/>
  <text x="60" y="165" text-anchor="middle" font-size="12" fill="currentColor">U2</text>
  <circle cx="340" cy="60" r="24" fill="none" stroke="currentColor"/>
  <text x="340" y="65" text-anchor="middle" font-size="12" fill="currentColor">U3</text>
  <circle cx="340" cy="160" r="24" fill="none" stroke="currentColor"/>
  <text x="340" y="165" text-anchor="middle" font-size="12" fill="currentColor">U4</text>
  <line x1="82" y1="70" x2="160" y2="95" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowR)"/>
  <line x1="82" y1="150" x2="160" y2="125" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowR)"/>
  <line x1="240" y1="95" x2="318" y2="70" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowR)"/>
  <line x1="240" y1="125" x2="318" y2="150" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowR)"/>
</svg>
<figcaption>Reads anchored in unique sequence (U1, U2) run into the shared repeat and lose their
identity there; reads anchored on the far side (U3, U4) do too. Unless a read spans the whole
repeat, nothing in the data says whether the genome goes U1&#8211;repeat&#8211;U3, U1&#8211;repeat&#8211;U4,
or some other pairing.</figcaption>
</figure>

Because roughly half the human genome is repetitive, this is close to the central difficulty of
assembly, and it is why a reference genome needs to be read in light of the read lengths used to
build it: repeat structure the reads couldn't span is not reliably resolved.

Cleaning the overlap graph also has to deal with spurious structure from sequencing error, not just
repeats: if a mismatch appears where a path exits a shared stretch, and the mismatching branch
dead-ends abruptly rather than continuing, that is evidence (not proof) that the branch is an error
rather than a genuine second copy of a repeat, and it can be pruned.

### Consensus

Once layout has produced contigs — paths through the simplified overlap graph — the reads making up
each contig are lined up, and at each position a **majority vote** decides which nucleotide (or gap)
belongs in the consensus. The complications already introduced are exactly what makes this
nontrivial: sequencing error can make a minority base look momentarily convincing, and genuine
allelic difference means the "true" answer may legitimately be two different bases at a position
with low coverage (say six reads) and a non-negligible error rate.

### A case study: the string graph assembler (SGA)

SGA, built around the FM-index, works in three passes:

1. **Error correction** — look at the *k*-mers occurring in all the reads, find rare ones near
   common ones, and correct bases that are probably sequencing errors.
2. **Assembly** — index the corrected reads with an FM-index, find overlaps directly from it,
   discard duplicate and low-quality reads, and trace the overlap graph into contigs.
3. **Scaffolding** — re-index the contigs with a fresh FM-index, map the original paired reads back
   onto them, and use pairs spanning a gap to join contigs into scaffolds.

The FM-index is built three times — correction, assembly, scaffolding — and even so, assembling a
human-sized genome this way takes days of elapsed time and thousands of CPU hours.

On real data (NA12878, $1.2\times10^9$ reads, $40\times$ coverage), SGA's contigs cover about 95% of
the autosomes and chromosome X. That falls well short of what Lander-Waterman would predict at
$40\times$ ($e^{-40}\approx 4\times10^{-18}$, i.e. essentially no uncovered bases) — the same
Poisson-versus-real-libraries mismatch noted above, compounded by the fact that uncovered bases are
only one of several ways an assembly can fail to place a base.

## De Bruijn graph assembly

The second strategy restates assembly on a different kind of graph: instead of nodes for whole
reads, it uses nodes for fixed-length substrings and routes every read through them.

### k-mers and how the graph is built

A **$k$-mer** is a substring of length $k$ ("mer" is Greek for "part"). A **$(k-1)$-mer** is a
substring of length $k-1$. Every $k$-mer has a **left** $(k-1)$-mer (its first $k-1$ characters) and
a **right** $(k-1)$-mer (its last $k-1$ characters), overlapping in $k-2$ characters.

Construction: for every $k$-mer occurring in every read, add a directed edge from its left
$(k-1)$-mer to its right $(k-1)$-mer, reusing a node if that $(k-1)$-mer is already in the graph.
Each edge stands for one $k$-mer from the input, and the graph can be built with a hash map: look up
(or insert) the left node, look up (or insert) the right node, add the edge. For genome assembly,
every $k$-mer is recorded twice — once as itself and once as its reverse complement, in "twin"
nodes — and $k$ is always odd so that no $k$-mer can be its own reverse complement (twin nodes are
omitted below to avoid clutter). If the same $k$-mer occurs more than once, its edge is added again
between the same two nodes, a **multiedge** — this is how repeats show up.

### Eulerian walks

Reconstructing a genome from this graph means finding a walk that uses every edge exactly once — an
**Eulerian walk** — since every edge is one $k$-mer and the genome is (on this idealization) the
concatenation of all of them in order. The vocabulary:

- A node is **balanced** if indegree equals outdegree; **semi-balanced** if they differ by exactly 1.
- A graph is **connected** if every node is reachable from every other.
- A directed, connected graph has an Eulerian walk iff it has **at most two semi-balanced nodes and
  all others balanced** (Jones & Pevzner, §8.8).

Take reads `AAA`, `AAB`, `ABB`, `BBB`, `BBA` ($k=3$): left/right 2-mers give `AA`→`AA`, `AA`→`AB`,
`AB`→`BB`, `BB`→`BB`, `BB`→`BA`.

<figure>
<svg viewBox="0 0 480 170" role="img" aria-label="De Bruijn graph for reads AAA, AAB, ABB, BBB, BBA, with semi-balanced nodes AA and BA at the two ends">
  <defs>
    <marker id="arrowB" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0L10,5L0,10z" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="60" cy="110" r="22" fill="none" stroke="currentColor"/>
  <text x="60" y="115" text-anchor="middle" font-size="13" fill="currentColor">AA</text>
  <circle cx="190" cy="110" r="22" fill="none" stroke="currentColor"/>
  <text x="190" y="115" text-anchor="middle" font-size="13" fill="currentColor">AB</text>
  <circle cx="320" cy="110" r="22" fill="none" stroke="currentColor"/>
  <text x="320" y="115" text-anchor="middle" font-size="13" fill="currentColor">BB</text>
  <circle cx="440" cy="110" r="22" fill="none" stroke="currentColor"/>
  <text x="440" y="115" text-anchor="middle" font-size="13" fill="currentColor">BA</text>
  <path d="M48,90 C30,50 90,50 72,90" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowB)"/>
  <line x1="82" y1="110" x2="168" y2="110" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowB)"/>
  <line x1="212" y1="110" x2="298" y2="110" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowB)"/>
  <path d="M308,90 C290,50 350,50 332,90" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowB)"/>
  <line x1="342" y1="110" x2="418" y2="110" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrowB)"/>
  <text x="60" y="150" text-anchor="middle" font-size="11" fill="currentColor">semi-balanced</text>
  <text x="440" y="150" text-anchor="middle" font-size="11" fill="currentColor">semi-balanced</text>
</svg>
<figcaption>AA has one more outgoing edge than incoming, BA one more incoming than outgoing; AB and
BB are balanced. Two semi-balanced nodes and the rest balanced means the graph is Eulerian, and the
walk AA&#8594;AA&#8594;AB&#8594;BB&#8594;BB&#8594;BA reproduces the original reads.</figcaption>
</figure>

Two independent arguments confirm this graph is Eulerian: exhibiting the walk directly, or checking
that exactly `AA` and `BA` are semi-balanced while `AB` and `BB` are balanced.

**Why perfect sequencing is always Eulerian.** Assume every length-$k$ substring of the genome is
sequenced exactly once, with no errors. Then the $(k-1)$-mer at the genome's left end is
semi-balanced with one extra outgoing edge, the one at the right end is semi-balanced with one
extra incoming edge, and every other node is balanced, because any interior $(k-1)$-mer occurs as a
*left* $(k-1)$-mer exactly as many times as it occurs as a *right* one. (If the genome is circular,
there are no ends, and the whole graph is balanced — an Eulerian *circuit*.) So under this
idealization the de Bruijn graph always has an Eulerian walk, found efficiently.

### Repeats break uniqueness here too

Having an Eulerian walk does not mean it is the only one, and only one corresponds to the true
genome. For `ZABCDABEFABY` with $k=3$, node `AB` is visited three times — a repeated 2-mer — and the
graph decomposes into two edge-disjoint directed cycles joined at `AB`. Depending which cycle is
taken first on leaving `AB`, two different Eulerian walks result:

$$\texttt{ZA}\to\texttt{AB}\to\texttt{BE}\to\texttt{EF}\to\texttt{FA}\to\texttt{AB}\to\texttt{BC}\to\texttt{CD}\to\texttt{DA}\to\texttt{AB}\to\texttt{BY}$$
$$\texttt{ZA}\to\texttt{AB}\to\texttt{BC}\to\texttt{CD}\to\texttt{DA}\to\texttt{AB}\to\texttt{BE}\to\texttt{EF}\to\texttt{FA}\to\texttt{AB}\to\texttt{BY}$$

Only one matches the real genome, and the graph itself gives no way to prefer it — the same repeat
problem seen in the overlap graph, restated on a different structure.

### What real sequencing does to the graph

Dropping perfect sequencing breaks the Eulerian property in several ways:

- **Gaps in coverage** — regions with no reads — disconnect the graph. Each component can still be
  individually Eulerian, but the whole is not, and the pieces are two contigs with an unresolved
  gap between them.
- **Coverage variation** — an extra copy of a $(k-1)$-mer relative to its neighbours — unbalances
  nodes that should have been balanced, giving more than two semi-balanced nodes.
- **Errors and allelic differences** between chromosome copies introduce spurious nodes and edges,
  again tending to disconnect the graph or break balance in the largest component.

### Efficiency

Building the graph costs $O(1)$ expected work per $k$-mer — look up or insert two nodes, add one
edge — given a hash map and $(k-1)$-mers that fit in $O(1)$ machine words. Over $N$ reads,
construction is $O(N)$, against the $O(N\log N)$ needed for the FM-index used in overlap assembly.
Timing construction on progressively longer prefixes of the lambda phage genome confirms this:
time scales roughly linearly with input size.

Typical assembly projects run at $30$–$50\times$ coverage, so the same $k$-mer can occur dozens of
times. Rather than keep parallel edges, assemblers record a **weight** on each edge — the number of
times that $k$-mer occurs — giving one weighted edge per *distinct* $k$-mer, which is both smaller
and easier to reason about, since low-weight edges become candidates for pruning as likely errors.

### Topology-based error correction

Real de Bruijn graphs need heuristic cleanup before tracing, matched to where the error shows up:
**dead-end tips** (errors at a read's end) are trimmed; **bubbles** (two parallel paths diverging at
a mid-read error and rejoining shortly after) are popped; **chimeric edges**, short low-coverage
spurious connections, are clipped. These are heuristics, and assemblers differ on exactly when to
trim, pop, or clip.

### Limitations

Splitting every read into $k$-mers immediately throws away information: **read coherence is lost**,
since some graph paths are consistent with the edges but not with any actual input read — the graph
only remembers overlaps of length $k-1$, not the reads' full length. Because only this one
fixed-length notion of overlap is considered, repeats an overlap graph could still resolve become
invisible at a shorter $k$. Some assemblers recover part of this by *threading* original reads back
through the finished graph, using them to pick the path consistent with real data rather than
trusting degree alone.

This is the central OLC/DBG trade-off: de Bruijn graphs are fast and simple, at the cost of
discarding information overlap graphs keep. With overlap-graph implementations such as SGA now
efficient enough to use at scale, that balance has shifted back toward overlap-based methods where
accuracy matters most.

## Comparing assemblers: the N50 metric

The standard summary statistic for an assembly is **N50**: the contig (or scaffold) length $L$ such
that 50% of all assembled bases lie in contigs (or scaffolds) of length $L$ or greater. Larger N50
means longer contiguous pieces and fewer gaps — it is the headline number used to tune parameters,
such as scanning a range of $k$ for a de Bruijn assembler and picking whichever maximizes N50.

A benchmark on a *C. elegans* data set (100 Mbase genome, 33.8M read pairs, 100 bp reads, 250 bp
insert) compared SGA (OLC, minimum overlap 75 bp) against three de Bruijn assemblers — Velvet
($k=61$), ABySS ($k=67$), SOAPdenovo ($k=59$):

| | SGA (OLC) | Velvet (DBG) | ABySS (DBG) | SOAPdenovo (DBG) |
| --- | --- | --- | --- | --- |
| Scaffold N50 | 26.3 kbp | 31.3 kbp | 23.8 kbp | 31.1 kbp |
| Aligned contig N50 | 16.8 kbp | 13.6 kbp | 18.4 kbp | 16.0 kbp |
| Mismatch rate (all bases) | 1/21,545 bp | 1/8,786 bp | 1/5,577 bp | 1/26,585 bp |
| Total CPU time | 41 h | 2 h | 5 h | 13 h |
| Max memory | 4.5 GB | 23.0 GB | 14.1 GB | 38.8 GB |

(From Simpson & Durbin, *Genome Research* 22(3):549–56, 2012.)

No assembler dominates every metric: the de Bruijn methods are far faster, but SGA and SOAPdenovo
have noticeably lower mismatch rates than Velvet and ABySS, and SGA uses far less memory. Different
de Bruijn assemblers also settle on different optimal $k$ despite similar data, because each has its
own heuristics for simplifying the graph — some tolerate small $k$ better, others need a larger one.

Whichever method is used, **repeats remain the underlying bottleneck**: short reads cannot resolve
repeat structure exactly, and with roughly half the human genome repetitive, this is not marginal.
A finished reference genome's repeat structure is only as trustworthy as the read lengths used to
build it. A further, currently open problem is environmental (metagenomic) sequencing, where a
sample mixes many different genomes rather than one individual's — the methods here assume a single
(possibly diploid) genome, and current read lengths have not solved the mixed case.

## Sources

- Slides: `lectures/06-slides/01-lecture-6.md` (shotgun assembly pipeline, coverage,
  Lander-Waterman, OLC and de Bruijn graph construction, Eulerian walk definitions,
  error-correction topology, the `ZABCDABEFABY` example, the SGA coverage figure after Simpson &
  Durbin 2012, and the OLC/DBG flowchart courtesy of Ben Langmead) and
  `lectures/06-slides/02-n50---contig-scaffold-length-or-larger-that-contains-50-of-b.md` (the
  *C. elegans* assembler comparison table, after Simpson, J.T. and Durbin, R., "Efficient De Novo
  Assembly of Large Genomes using Compressed Data Structures," *Genome Research* 22, no. 3 (2012):
  549–56).
- Transcript: `recordings/lectures/06.md`, timestamps 00:00–1:07:37 (David K. Gifford, MIT 7.91J
  Spring 2014). Used for the motivation, the greedy-SCS worked examples (repeated-word and
  "best of times" cases), the SCS/Hamiltonian-path/NP-hardness argument, the SGA three-pass
  description, the Poisson-vs-negative-binomial discussion of the 1000 Genomes coverage plot, and
  the closing remarks on repeats and metagenomic assembly.
- Named but not contained in the supplied material: Green, E.D., "Strategies for the Systematic
  Sequencing of Complex Genomes," *Nature Reviews Genetics* 2, no. 8 (2001): 573–83; Adams, J.,
  "Complex genomes: Shotgun sequencing," *Nature Education* 1(1) (2008); Jones, N.C. and Pevzner,
  P.A., *An Introduction to Bioinformatics Algorithms*, §8.8 (the Eulerian-walk criterion); the
  directed-graph illustration and the two "removed due to copyright restrictions" slides, whose
  content was not recoverable from the source PDF.

---

[← 5. Read Alignment with the BWT/FM Index](05-read-alignment-with-the-bwt-fm-index.md) · [Contents](index.md) · [7. ChIP-seq Peak Calling and IDR →](07-chip-seq-peak-calling-and-idr.md)

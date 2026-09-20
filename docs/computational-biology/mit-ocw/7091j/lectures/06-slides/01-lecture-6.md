---
title: Lecture 6
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/06-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/06-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture 6

## Genome Assembly

Foundations of Computational Systems Biology
David K. Gifford

---

## *de novo* whole-genome shotgun assembly

Sequence reads
$\downarrow$
Sequence contigs
$\downarrow$
Scaffolds
Read pair
Read pair
Read pair
$\downarrow$
Mapped scaffolds
$\downarrow$
Genome map

Courtesy of Nature Education. Used with permission.
Source: Green, Eric D. "Strategies for the Systematic Sequencing of Complex Genomes." *Nature Reviews Genetics* 2, no. 8 (2001): 573-83.
Adams, J. (2008) Complex genomes: Shotgun sequencing. *Nature Education* 1(1)

---

## Assembly

Whole-genome "shotgun" sequencing starts by copying and fragmenting the DNA

("Shotgun" refers to the random fragmentation of the whole genome; like it was fired from a shotgun)

Input: `GGCGTCTATATCTCGGCTCTAGGCCCTCATTTTTT`

Copy:
```
GGCGTCTATATCTCGGCTCTAGGCCCTCATTTTTT
GGCGTCTATATCTCGGCTCTAGGCCCTCATTTTTT
GGCGTCTATATCTCGGCTCTAGGCCCTCATTTTTT
GGCGTCTATATCTCGGCTCTAGGCCCTCATTTTTT
```

Fragment:
```
GGCGTCTA   TATCTCGG   CTCTAGGCCCTC   ATTTTTT
GGC   GTCTATAT   CTCGGCTCTAGGCCCTCA   TTTTTT
GGCGTC   TATATCT   CGGCTCTAGGCCCT   CATTTTTT
GGCGTCTAT   ATCTCGGCTCTAG   GCCCTCA   TTTTTT
```

---

## Assembly

Assume sequencing produces such a large # fragments that almost all genome positions are covered by many fragments...

From these:
```
               CTAGGCCCTCAATTTTT
              CTCTAGGCCCTCAATTTTT
             GGCTCTAGGCCCTCATTTTTT
            CTCGGCTCTAGCCCCTCATTTT
          TATCTCGACTCTAGGCCCTCA
          TATCTCGACTCTAGGCC
       TCTATATCTCGGCTCTAGG
   GGCGTCTATATCTCG
  GGCGTCGATATCT
 GGCGTCTATATCT
```

Reconstruct this:
$$\longrightarrow \text{GGCGTCTATATCTCGGCTCTAGGCCCTCATTTTTT}$$

---

## Assembly

...but we don't know what came from where

From these:
```
CTAGGCCCTCAATTTTT
GGCGTCTATATCT
CTCTAGGCCCTCAATTTTT
TCTATATCTCGGCTCTAGG
GGCTCTAGGCCCTCATTTTTT
CTCGGCTCTAGCCCCTCATTTT
TATCTCGACTCTAGGCCCTCA
GGCGTCGATATCT
TATCTCGACTCTAGGCC
GGCGTCTATATCTCG
```

Reconstruct this:
$$\longrightarrow \text{GGCGTCTATATCTCGGCTCTAGGCCCTCATTTTTT}$$

---

## Assembly

Key term: *coverage*. Usually it's short for *average coverage*: the average number of reads covering a position in the genome.

```
               CTAGGCCCTCAATTTTT
              CTCTAGGCCCTCAATTTTT
             GGCTCTAGGCCCTCATTTTTT
            CTCGGCTCTAGCCCCTCATTTT
          TATCTCGACTCTAGGCCCTCA             177 nucleotides
          TATCTCGACTCTAGGCC
       TCTATATCTCGGCTCTAGG
   GGCGTCTATATCTCG
  GGCGTCGATATCT
 GGCGTCTATATCT
 GGCGTCTATATCTCGGCTCTAGGCCCTCATTTTTT        35 nucleotides
```

$$\text{Average coverage} = 177 / 35 \approx 7\text{x}$$

---

## Estimating Uncovered Bases (Lander Waterman)

- $G$ – genome size
- $N$ - # of reads
- $L$ – Length of read
- $NL/G = \text{reads/base} = \lambda$ (coverage)
  - $\text{Poisson}(0, \lambda) = e^{-\lambda} =\sim \text{probability a base is not covered}$
  - # of uncovered bases $=\sim G e^{-\lambda}$
  - # of gaps $=\sim N e^{-\lambda}$

---

## Reads vs. coverage for 1000 Genomes Datasets

[Plot of Genome coverage (bases) from $0.0$ to $3.0 \cdot 10^9$ versus Reads from $0.0$ to $3.5 \cdot 10^8$]

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

---

## Assembly

Coverage could also refer to the number of reads covering a particular position in the genome:

```
               CTAGGCCCTCAATTTTT
              CTCTAGGCCCTCAATTTTT
             GGCTCTAGGCCCTCATTTTTT
            CTCGGCTCTAGCCCCTCATTTT
          TATCTCGACTCTAGGCCCTCA
          TATCTCGACTCTAGGCC
       TCTATATCTCGGCTCTAGG
   GGCGTCTATATCTCG
  GGCGTCGATATCT
 GGCGTCTATATCT
 GGCGTCTATATCTCGGCTCTAGGCCCTCATTTTTT
              |
              ^
```

$$\text{Coverage at this position} = 6$$

---

## Assembly

Say two reads truly originate from overlapping stretches of the genome. Why might there be differences?

```
TATCTCGACTCTAGGCC
||||||| ||||||||
TCTATATCTCGGCTCTAGG
          ^
```

1. Sequencing error
2. Difference between inherited copies of a chromosome
   E.g. humans are diploid; we have two copies of each chromosome, one from mother, one from father. The copies can differ:

```
Read from Mother:        TATCTCGACTCTAGGCC
                         ||||||| ||||||||        We'll mostly ignore ploidy, but
Read from Father:   TCTATATCTCGGCTCTAGG          real tools must consider it

Sequence from Mother:  TCTATATCTCGACTCTAGGCC
Sequence from Father:  TCTATATCTCGGCTCTAGGCC
```

---

## Two approaches to short read assembly

- **Overlap Layout Consensus - String Graph Assemblers**
  - Construct overlap graph directly from reads, eliminating redundant reads; trace path for assembly
  - Examples: SGA, Fermi

- **de Bruijn graph-based assemblers**
  - Construct k-mer graph from reads; original reads are discarded
  - Trace path in graph for assembly

---

## Assembly alternatives

Alternative 1: Overlap-Layout-Consensus (OLC) assembly
Alternative 2: de Bruijn graph (DBG) assembly

```
[Alternative 1]         [Alternative 2]
       |                       |
       v                       v
  +---------+           +---------------+
  | Overlap |           |Error correction|
  +---------+           +---------------+
       |                       |
       v                       v
  +---------+           +---------------+
  | Layout  |           |de Bruijn graph|
  +---------+           +---------------+
       |                       |
       v                       v
  +---------+           +---------------+
  |Consensus|           |    Refine     |
  +---------+           +---------------+
       \                       /
        \                     /
         v                   v
          +-----------------+
          |   Scaffolding   |
          +-----------------+
                   |
                   v
```

---

## Overlap Layout Consensus

```
+-----------+
|  Overlap  | ----> Build overlap graph
+-----------+
      |
      v
+-----------+
|  Layout   | ----> Bundle stretches of the overlap graph into contigs
+-----------+
      |
      v
+-----------+
| Consensus | ----> Pick most likely nucleotide sequence for each contig
+-----------+
      |
      v
```

---

## Overlaps

Finding all overlaps is like building a *directed graph* where directed edges connect overlapping nodes (reads)

```
CTCGGCTCTAGCCCCTCATTTT
 ||||||| |||||||||
 GGCTCTAGGCCCTCATTTTTT
```

Suffix of source is similar to prefix of sink

Nodes:
- `CTAGGCCCTCAATTTTT`
- `GGCGTCTATATCT`
- `CTCTAGGCCCTCAATTTTT`
- `TCTATATCTCGGCTCTAGG`
- `GGCTCTAGGCCCTCATTTTTT` $\longleftarrow$ sink
- `CTCGGCTCTAGCCCCTCATTTT` $\longrightarrow$ source
- `TATCTCGACTCTAGGCCCTCA`
- `GGCGTCGATATCT`
- `TATCTCGACTCTAGGCC`
- `GGCGTCTATATCTCG`

---

## Directed graph review

Directed graph $G(V, E)$ consists of set of vertices, $V$ and set of directed edges, $E$

Directed edge is an *ordered pair* of vertices.
First is the *source*, second is the *sink*.

Vertex is drawn as a circle

Edge is drawn as a line with an arrow connecting two circles

Vertex also called *node* or *point*
$V = \{ a, b, c, d \}$

Edge also called *arc* or *line*
$E = \{

## Layout

Picture gets clearer after removing some transitively-inferrible edges

```
      1
   +------+
   |      v
  abc -> bcd -> cde
      2      2

          |
          v

  abc -> bcd -> cde
      2      2
```

---

## Layout

Remove transitively-inferrible edges, starting with edges that skip one node:

Before:

[Graph showing nodes and directed edges before transitive reduction]

---

## Layout

Remove transitively-inferrible edges, starting with edges that skip one node:

After:

[Graph showing edges after removing skips of one node]

---

## Layout

Remove transitively-inferrible edges, starting with edges that skip one or two nodes:

After:

[Graph showing simpler chain after removing skips of one or two nodes]

Even simpler

---

## Layout

Emit *contigs* corresponding to the non-branching stretches

**Contig 1**
`to_every_thing_turn_`

**Contig 2**
`turn_there_is_a_season`

Unresolvable repeat

---

## Layout

In practice, layout step also has to deal with spurious subgraphs, e.g. because of sequencing error

```
        Possible repeat
        boundary
b [ ][ ][ ][ ][ ][ ][ ][ ][ ]     Mismatch
a [ ][ ][ ][ ][ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ][ ][ ][ ][ ]
      [ ][ ][ ][ ][ ][ ][ ][ ][ ]
        [ ][ ][ ][ ][ ][ ][ ][ ][ ]
          [ ][ ][ ][ ][ ][ ][ ][ ][ ]
               :
```

prune **b**:
a -> ...
\
 -> b (pruned)

Mismatch could be due to sequencing error or repeat. Since the path through **b** ends abruptly we might conclude it's an error and prune **b**.

---

## Overlap Layout Consensus

- **Overlap** $\checkmark$ Build overlap graph
- **Layout** $\checkmark$ Bundle stretches of the overlap graph into *contigs*
- **Consensus** Pick most likely nucleotide sequence for each contig

---

## Consensus

```
TAGATTACACAGATTACTGA  TTGATGGCGTAA CTA   | Take reads that make
TAGATTACACAGATTACTGACTTGATGGCGTAAACTA   | up a contig and line
TAG TTACACAGATTATTGACTTCATGGCGTAA CTA   | them up
TAGATTACACAGATTACTGACTTGATGGCGTAA CTA   |
TAGATTACACAGATTACTGACTTGATGGCGTAA CTA   |
  |             |  |  |           |
  v             v  v  v           v
TAGATTACACAGATTACTGACTTGATGGCGTAA CTA     Take consensus, i.e.
                                          majority vote
```

At each position, ask: what nucleotide (and/or gap) is here?

Complications: (a) sequencing error, (b) ploidy

Say the true genotype is AG, but we have a high sequencing error rate and only about 6 reads covering the position.

---

## Overlap Layout Consensus

- **Overlap** $\checkmark$ Build overlap graph
- **Layout** $\checkmark$ Bundle stretches of the overlap graph into *contigs*
- **Consensus** $\checkmark$ Pick most likely nucleotide sequence for each contig

What's the main drawback of OLC?

Building overlap graph can be *slow*.

$2^{\text{nd}}$-generation sequencing datasets are $\sim$ 100s of millions or billions of reads, hundreds of billions of nucleotides total

---

## Assembly alternatives

Alternative 1: Overlap-Layout-Consensus (OLC) assembly
Alternative 2: de Bruijn graph (DBG) assembly

```
  [ Overlap ]                 [ Error correction ]
       |                              |
       v                              v
  [ Layout ]                  [ de Bruijn graph ]
       |                              |
       v                              v
 [ Consensus ]                    [ Refine ]
       \                              /
        \                            /
         +-----> [ Scaffolding ] <--+
```

---

Flow chart removed due to copyright restrictions.

---

Table removed due to copyright restrictions.

---

## SGA contigs cover 95% of autosomes and chr X (non "N" bases)
### NA12878 $1.2 \times 10^9$ reads $40\times$ coverage

**Figure 3.** The amount of the human reference genome covered by a contig as a function of the minimum contig alignment length. For each length L on the x-axis, contig alignments less than L bp in length were filtered out and the amount of the reference genome covered by the remaining alignments was calculated.

Courtesy of Cold Spring Harbor Laboratory Press. Used with permission.
Source: Simpson, Jared T., and Richard Durbin. "Efficient De Novo Assembly of Large Genomes using Compressed Data Structures." *Genome Research* 22, no. 3 (2012): 549-56.

---

## Assembly alternatives

Alternative 1: Overlap-Layout-Consensus (OLC) assembly
Alternative 2: de Bruijn graph (DBG) assembly

```
  [ Overlap ]                 [ Error correction ]
       |                              |
       v                              v
  [ Layout ]                  [ de Bruijn graph ]
       |                              |
       v                              v
 [ Consensus ]                    [ Refine ]
       \                              /
        \                            /
         +-----> [ Scaffolding ] <--+
```

---

## De Bruijn graph assembly

A formulation conceptually similar to overlapping/SCS, but has some potentially helpful properties not shared by SCS.

---

## k-mer

"$k$-mer" is a substring of length $k$

S: `GGCGATTCATCG`
*mer*: from Greek meaning "part"

A 4-mer of S: `ATTC`

All 3-mers of S:
`GGC`
`GCG`
`CGA`
`GAT`
`ATT`
`TTC`
`TCA`
`CAT`
`ATC`
`TCG`

I'll use "$k-1$-mer" to refer to a substring of length $k - 1$

---

## De Bruijn graph

As usual, we start with a collection of reads, which are substrings of the reference genome.

`AAA`, `AAB`, `ABB`, `BBB`, `BBA`

`AAB` is a $k$-mer ($k = 3$). `AA` is its *left* $k-1$-mer, and `AB` is its *right* $k-1$-mer.

```
       AAB  3-mer
      /   \
     v     v
    AA     AB
     L      R
 AAB's left  AAB's right
   2-mer       2-mer
```

---

## De Bruijn graph

Take each length-3 input string and split it into two overlapping substrings of length 2. Call these the *left* and *right 2-mers*.

`AAABBBA`

take all 3-mers: `AAA`, `AAB`, `ABB`, `BBB`, `BBA`

form L/R 2-mers: `AA`, `AA`, `AA`, `AB`, `AB`, `BB`, `BB`, `BB`, `BB`, `BA`
L R L R L R L R L R

Let 2-mers be nodes in a new graph. Draw a directed edge from each left 2-mer to corresponding right 2-mer:

Each edge in this graph corresponds to a length-3 input string

---

## De Bruijn graph

```
        +----+
        | AB |
       /^----+----\
  AAB /  |         \ ABB
     /   |          \
+----+   |           v+----+
| AA |   |            | BA |
+----+   v            +----+
  ^ )   +----+         ^
  +-+   | BB |--------+
   AAA  +----+   BBA
         ^ )
         +-+
         BBB
```

An edge corresponds to an overlap (of length $k-2$) between two $k-1$ mers.
More precisely, it corresponds to a $k$-mer from the input.

---

## De Bruijn graph

```
        +----+
        | AB |
       /^----+----\
  AAB /  |         \ ABB
     /   |          \
+----+   |           v+----+
| AA |   |            | BA |
+----+   v            +----+
  ^ )   +----+         ^
  +-+   | BB |--------+
   AAA  +----+   BBA
        ^^ ))
        ++-+
        BBB
        BBB
```

If we add one more B to our input string: `AAABBBBA`, and rebuild the De Bruijn graph accordingly, we get a *multiedge*.

---

## Eulerian walk definitions and statements

Node is *balanced* if indegree equals outdegree

Node is *semi-balanced* if indegree differs from outdegree by 1

Graph is *connected* if each node can be reached by some other node

*Eulerian walk* visits each edge exactly once

Not all graphs have Eulerian walks. Graphs that do are *Eulerian*. (For simplicity, we won't distinguish Eulerian from semi-Eulerian.)

A directed, connected graph is Eulerian if and only if it has at most 2 semi-balanced nodes and all other nodes are balanced

Jones and Pevzner section 8.8

---

## De Bruijn graph

Back to our De Bruijn graph

`AAA`, `AAB`, `ABB`, `BBB`, `BBA`

`AA`, `AA`, `AA`, `AB`, `AB`, `BB`, `BB`, `BB`, `BB`, `BA`
L R L R L R L R L R

Is it Eulerian? **Yes**

Argument 1: `AA` $\to$ `AA` $\to$ `AB` $\to$ `BB` $\to$ `BB` $\to$ `BA`

Argument 2: `AA` and `BA` are semi-balanced, `AB` and `BB` are balanced

---

## De Bruijn graph

A procedure for making a De Bruijn graph for a genome

Assume *perfect sequencing* where each length-$k$ substring is sequenced exactly once with no errors

Pick a substring length $k$: 5

Start with each read: `a_long_long_long_time`

Take each $k$ mer and split into left and right $k-1$ mers:
```
       long_
      /     \
     v       v
   long     ong_
```

Add $k-1$ mers as nodes to De Bruijn graph (if not already there), add edge from left $k-1$ mer to right $k-1$ mer

---

## De Bruijn graph

- For genome assembly each $k$-mer is recorded in "twin" nodes – one node in the forward direction and one node in reverse complement
  - $k$ is odd so no node can be its own reverse complement
- We will not show reverse complement twin nodes to cut down on clutter

---

## De Bruijn graph

First 8 $k$-mer additions, $k = 5$

`a_long_long_long_time`

---

## De Bruijn graph

Last 5 $k$-mer additions, $k = 5$

`a_long_long_long_time`

Finished graph

---

## De Bruijn graph

With perfect sequencing, this procedure always yields an Eulerian graph. Why?

Node for $k-1$-mer from **left end** is semi-balanced with one more outgoing edge than incoming *

Node for $k-1$-mer at **right end** is semi-balanced with one more incoming than outgoing *

Other nodes are balanced since # times $k-1$-mer occurs as a left $k-1$-mer = # times it occurs as a right $k-1$-mer

\* Unless genome is circular

---

## De Bruijn graph

Assuming perfect sequencing, procedure yields graph with Eulerian walk that can be found efficiently.

We saw cases where Eulerian walk corresponds to the original superstring. Is this always the case?

---

## De Bruijn graph

**No:** graph can have multiple Eulerian walks, only one of which corresponds to original superstring

Right: graph for `ZABCDABEFABY`, $k = 3$

Alternative Eulerian walks:

`ZA` $\to$ `AB` $\to$ `BE` $\to$ `EF` $\to$ `FA` $\to$ `AB` $\to$ `BC` $\to$ `CD` $\to$ `DA` $\to$ `AB` $\to$ `BY`

`ZA` $\to$ `AB` $\to$ `BC` $\to$ `CD` $\to$ `DA` $\to$ `AB` $\to$ `BE` $\to$ `EF` $\to$ `FA` $\to$ `AB` $\to$ `BY`

These correspond to two edge-disjoint directed cycles joined by node `AB`

`AB` is a repeat: `ZABCDABEFABY`

---

## De Bruijn graph

This is the first sign that Eulerian walks can't solve all our problems

Other signs emerge when we think about how actual sequencing differs from our idealized construction

---

## De Bruijn graph

Gaps in coverage can lead to *disconnected graph*

Graph for `a_long_long_long_time`, $k = 5$:

---

## De Bruijn graph

Gaps in coverage can lead to *disconnected graph*

Graph for `a_long_long_long_time`, $k = 5$ but *omitting* `ong_t`:

Connected components are individually Eulerian, overall graph is not

---

## De Bruijn graph

Differences in coverage also lead to non-Eulerian graph

Graph for `a_long_long_long_time`, $k = 5$ but with *extra copy* of `ong_t`:

Graph has 4 **semi-balanced** nodes, isn't Eulerian

---

## De Bruijn graph

Errors and differences between chromosomes also lead to non-Eulerian graphs

Graph for `a_long_long_long_time`, $k = 5$ but with error that turns a copy of `long_` into `lxng_`

Graph is not connected; largest component is not Eulerian

---

## De Bruijn graph

How much work to build graph?

For each $k$-mer, add 1 edge and up to 2 nodes

Reasonable to say this is $O(1)$ expected work

Assume hash map encodes nodes & edges

Assume $k-1$-mers fit in $O(1)$ machine words, and hashing $O(1)$ machine words is $O(1)$ work

Querying / adding a key is $O(1)$ expected work

$O(1)$ expected work for 1 $k$-mer, $O(N)$ overall

---

## De Bruijn graph

Timed De Bruijn graph construction applied to progressively longer prefixes of lambda phage genome, $k = 14$

$O(N)$ expectation appears to work in practice, at least for this small example

---

## De Bruijn graph

In typical assembly projects, average coverage is $\sim 30 - 50$

---

## De Bruijn graph

In typical assembly projects, average coverage is $\sim 30 - 50$

Same edge might appear in dozens of copies; let's use edge *weights* instead

*Weight* = # times $k$-mer occurs

Using weights, there's one weighted edge for each *distinct* $k$-mer

Before: one edge per $k$-mer
After: one *weighted* edge per *distinct* $k$-mer

---

## Graph topology based error correction

- Errors at end of read
  - Trim off 'dead-end' tips

- Errors in middle of read
  - Pop Bubbles

- Chimeric Edges
  - Clip short, low coverage nodes

Figure adapted from presentation by Michael Schatz

---

## De Bruijn graph

What are the limitations of De Bruijn graphs?

Reads are immediately split into shorter $k$-mers; can't resolve repeats as well as overlap graph

Only a very specific type of "overlap" is considered, which makes dealing with errors more complicated.

*Read coherence is lost.* Some paths through De Bruijn graph are inconsistent with respect to input reads. Need to thread reads though De Bruijn graph to recover information lost when reads are fragmented into $k$-mers.

This is the OLC $\leftrightarrow$ DBG tradeoff

Single most important benefit of De Bruijn graph is **speed and simplicity**.

## Assembly alternatives

Alternative 1: Overlap-Layout-Consensus (OLC) assembly
Alternative 2: de Bruijn graph (DBG) assembly

```
  │                                    │
  ▼                                    ▼
┌─────────────┐                      ┌──────────────────┐
│   Overlap   │                      │ Error correction │
└──────┬──────┘                      └────────┬─────────┘
       ▼                                      ▼
┌─────────────┐                      ┌──────────────────┐
│   Layout    │                      │  de Bruijn graph │
└──────┬──────┘                      └────────┬─────────┘
       ▼                                      ▼
┌─────────────┐                      ┌──────────────────┐
│  Consensus  │                      │      Refine      │
└──────┬──────┘                      └────────┬─────────┘
       │                                      │
       └──────────────┐      ┌────────────────┘
                      ▼      ▼
                   ┌────────────┐
                   │Scaffolding │
                   └─────┬──────┘
                         ▼
```

Courtesy of Ben Langmead. Used with permission. http://www.langmead-lab.org/teaching-materials/

---

## *de novo* whole-genome shotgun assembly

Sequence reads $\downarrow$

Sequence contigs $\downarrow$

Scaffolds $\downarrow$
* Read pair
* Read pair
* Read pair

Mapped scaffolds $\downarrow$

Genome map $\downarrow\$

Courtesy of Nature Education. Used with permission.
Source: Green, Eric D. "Strategies for the Systematic Sequencing of Complex Genomes." *Nature Reviews Genetics* 2, no. 8 (2001): 573-83.

Adams, J. (2008) Complex genomes: Shotgun sequencing. Nature Education 1(1)

---

---

[Up: contents](index.md) · [N50 - contig/scaffold length or larger that contains 50% of bases →](02-n50---contig-scaffold-length-or-larger-that-contains-50-of-b.md)

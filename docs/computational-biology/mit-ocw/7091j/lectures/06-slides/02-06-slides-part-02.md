---
title: 06 slides Part 02 —
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/06-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 06 slides Part 02 —

**Source:** `lectures/06-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- ���������������������������������������� ����������

   - –�������������������������������������������������������� ����������������������������������������

   - –����������������������

- ��������������������������������

   - –����������������������������������������������������� ���������

   - –��������������������������������

11

##### Assembly alternatives

Alternative 1: Overlap-Layout-Consensus (OLC) assembly Alternative 2: de Bruijn graph (DBG) assembly


<!-- Start of picture text -->
Overlap Error correction<br>Layout de Bruijn graph<br>Consensus Refine<br>Scaffolding<br>Courtesy of Ben Langmead. Used with permission. http://www.langmead-lab.org/teaching-materials/<br><!-- End of picture text -->

12

##### Overlap Layout Consensus

**Build overlap graph Overlap** Layout Bundle stretches of the overlap graph into contigs P Consensus ick most likely nucleotide sequence for each contig

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

13

#### Overlaps

Finding all overlaps is like building a directed graph where directed edges connect overlapping nodes (reads)

   - �����������������

   - �������������

- ���������������������� ����������������������

- ������������������������

- �������������������

- �������������������

- ���������������������

- ����������������������

Suffix of source is similar to prefix of sink

���������������������

- �������������

- �����������������

- ���������������

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

14

#### Directed graph review

Directed graph G(V, E) consists of set of vertices, V and set of directed edges, E

Directed edge is an ordered pair of vertices. First is the source, second is the sink.

Vertex is drawn as a circle

Edge is drawn as a line with an arrow connecting two circles


<!-- Start of picture text -->
a b<br>c d<br><!-- End of picture text -->

Vertex also called node or point

Edge also called arc or line

V =  { a, b, c, d } E =  { (a, b), (a, c), (c, b) } Source Sink

Directed graph also called digraph

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

15

#### Overlap graph

Below: overlap graph, where an overlap is a suffix/prefix match of at least 3 characters

A vertex is a **read** , a directed edge is an overlap between suffix of source and prefix of sink

Vertices (reads): { a: ���������, b: ���������, c: ��������  } Edges (overlaps): { (a, b), (b, c) }

To keep our presentation uncluttered we will not show the treatment of read reverse complements


<!-- Start of picture text -->
a: ��������� b: ��������� c: ��������<br>3 4<br>��������� ���������<br>��������� ���������<br>��������������� �������������<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

16

#### Overlap graph

Overlap graph could contain cycles.  A cycle is a path beginning and ending at the same vertex.

7


<!-- Start of picture text -->
a: ��������� b: ��������� c: ���������<br>3 4<br><!-- End of picture text -->

These happen when the DNA string itself is circular.  E.g. bacterial genomes are often circular; mitochondrial DNA is circular.

Cycles could also be due to repetitive DNA, as we’ll see


Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

17

#### Finding overlaps

a: ��������� b: ���������

c: ��������

How do we build the overlap graph?

Assume for now an “overlap” is when a suffix of X of length ≥ _l_ exactly matches a prefix of Y, and k is the length of reads

�����������������$���������$����������

A merged FM index of all reads allows us to match read prefixes and suffixes to discover overlaps.   See SGA paper -

Efficient de novo assembly of large genomes using compressed data structures Jared T Simpson and Richard Durbin  Genome Res. 2012. 22: 549-556

SGA algorithm excludes redundant (transitive) edges A -> B -> C excludes A -> C

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

18

#### Finding overlaps

Example overlap graph with _l_ = 3 _k_ = 7

###### Edge label is overlap length


<!-- Start of picture text -->
�<br>� ������� � �������<br>�������<br>� �<br>�<br>�������<br>�<br>�<br>� ������� ������� � �<br>� �<br>������� � � ������� ������� � �������<br>�<br>�������<br><!-- End of picture text -->

Original string: ��������������������������������

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

19

##### Overlap Layout Consensus


Overlap


<!-- Start of picture text -->
Layout<br>Consensus<br><!-- End of picture text -->

Build overlap graph

**Bundle stretches of the overlap graph into contigs** Pick most likely nucleotide sequence for each contig

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

20

##### Formulating the assembly problem

Finding overlaps is important, and we’ll return to it, but our ultimate goal is to recreate (assemble) the genome

How do we formulate this problem?

First attempt: the shortest common superstring (SCS) problem

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

21

##### Shortest common superstring

Given a collection of strings S, find SCS(S): the shortest string that contains all strings in S as substrings

Without requirement of “shortest,” it’s easy: just concatenate them Example: S: ������������������������������� Concatenation: ������������������������ ~~24~~ SCS(S): ���������� ~~10~~

��� ���� ����� ������ ������� �������� ��������� ����������

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

22

##### Shortest common superstring

Can we solve it?

Imagine a modified overlap graph where each edge has cost = - (length of overlap) SCS corresponds to a path that visits every node once, minimizing total cost along path

That’s the Traveling Salesman Problem (TSP), which is NP-hard!


<!-- Start of picture text -->
S: �������������������<br>SCS(S): �������<br>���<br>����<br>�����<br>������<br>AAB<br>�������<br>-2<br>-2<br>-1<br>-1 -1<br>AAA ABB<br>-1<br>-2<br>-1 -2<br>-2<br>-2<br>BB B BBA<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

23

##### Shortest common superstring

Say we disregard edge weights and just look for a path that visits all the nodes exactly once

That’s the Hamiltonian Path problem: NP-complete Indeed, it’s well established that SCS is NP-hard


<!-- Start of picture text -->
S: �������������������<br>SCS(S): �������<br>���<br>����<br>�����<br>������<br>AAB<br>�������<br>AAA ABB<br>BB B BBA<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

24

##### Shortest common superstring

Let’s take the hint give up on finding the shortest possible superstring

Non-optimal superstrings can be found with a greedy algorithm At each step, the greedy algorithm “greedily” chooses longest remaining overlap, merges its source and sink

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

25

##### Shortest common superstring: greedy

Greedy-SCS algorithm in action ( _l_ = 1):

###### ~~Input strings~~

- ���������������������������������

- ������������������������������

- ���������������������������

- ������������������������ In red are strings that get

- ��������������������� merged before the next round

- ������������������

- ���������������

Greedy answer:

- �������������

   - �����������

- ������������� Superstring

Actual SCS:

- ����������

Rounds of merging, one merge per line. Number in first column = length of overlap merged before that round.

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

26

##### Shortest common superstring: greedy

Greedy algorithm is not guaranteed to choose overlaps yielding SCS But greedy algorithm is a good approximation; i.e. the superstring yielded by the greedy algorithm won’t be more than ~2.5 times longer than true SCS (see Gusfield, Algorithms on Strings, Trees and Sequences: Computer Science and Computational Biology, 16.17.1)

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

27

##### Shortest common superstring: greedy

Greedy-SCS algorithm in action again ( _l_ = 3):

~~Input strings~~

������������������������������������������������������������������������� ������������������������������������������������������������������ �����������������������������������������������������������

- �����������������������������������������������������

- �����������������������������������������������

- �����������������������������������������

- �����������������������������������

- �����������������������������

- �������������������������

- �������������������������

~~Superstring~~

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

28

##### Shortest common superstring: greedy

Another setup for Greedy-SCS: assemble all substrings of length 6 from string ���������������������. _l_ = 3.

����������������������������������������������������������������������� ����������������������������������������������������������������� ����������������������������������������������������������� ����������������������������������������������������� ����������������������������������������������� �����������������������������������������

����������������������������������� �����������������������������

�����������������������

������������������

������������������

We only got back: ���������������� (missing a ����� ) What happened?

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

29

##### Shortest common superstring: greedy

###### The overlap graph for that scenario ( _l_ = 3):


<!-- Start of picture text -->
�<br>�<br>�<br>������<br>� �<br>� ������<br>�<br>�<br>�<br>�<br>������ �<br>�<br>�<br>� �<br>������ � � ������<br>� ������ �<br>�<br>�<br>������<br>�<br>� �<br>�<br>� �<br>������ ������ ������<br>�<br>� �<br>�<br>�<br><!-- End of picture text -->


<!-- Start of picture text -->
Courtesy of Ben Langmead. Used with permission.<br><!-- End of picture text -->

http://www.langmead-lab.org/teaching-materials/

30

##### Shortest common superstring: greedy

The overlap graph for that scenario ( _l_ = 3):


<!-- Start of picture text -->
�<br>�<br>�<br>������<br>� �<br>� ������<br>�<br>�<br>�<br>�<br>������ �<br>�<br>�<br>� �<br>������ � � ������<br>� ������ �<br>�<br>�<br>������<br>�<br>� �<br>�<br>� �<br>������ ������ ������<br>�<br>� �<br>�<br>���������������������<br>� Total overlap: 39<br>Courtesy of Ben Langmead. Used with permission.<br><!-- End of picture text -->

http://www.langmead-lab.org/teaching-materials/

31

##### Shortest common superstring: greedy

The overlap graph for that scenario ( _l_ = 3):


<!-- Start of picture text -->
�<br>�<br>�<br>������<br>� �<br>� ������<br>�<br>�<br>�<br>�<br>������ �<br>�<br>�<br>� �<br>������ � � ������<br>� ������ �<br>�<br>�<br>������<br>�<br>� �<br>�<br>� �<br>������ ������ ������<br>�<br>� �<br>�<br>����������������<br>� Total overlap: 44 Better but<br>wrong!<br>Courtesy of Ben Langmead. Used with permission. http://www.langmead-lab.org/teaching-materials/<br><!-- End of picture text -->

32

##### Shortest common superstring: greedy

Same example, but increased the substring length from 6 to 8

������������������������������������������������������������������������������������������� ����������������������������������������������������������������������������������� ��������������������������������������������������������������������������� ������������������������������������������������������������������� ����������������������������������������������������������� ��������������������������������������������������� ������������������������������������������� �����������������������������������

���������������������������

�����������������������

�����������������������

Got the whole thing: ���������������������

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

33

##### Shortest common superstring: greedy

Why are substrings of length 8 long enough for Greedy-SCS to figure out there are 3 copies of ����?

��������������������� ��������

One length-8 substring spans all three ����s

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

34

##### Repeats

Repeats often foil assembly.  They certainly foil SCS, with its “shortest” criterion!

Reads might be too short to “resolve” repetitive sequences.  This is why sequencing vendors try to increase read length. Algorithms that don’t pay attention to repeats (like our greedy SCS algorithm) might collapse them

���������������������

collapse ����������������

The human genome is ~ 50% repetitive!

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

35

##### Repeats

Basic principle: repeats foil assembly Another example using Greedy-SCS: Input: �������������������������������������������������� Extract every substring of length _k_ , then run Greedy-SCS. Do this for various _l_ (min overlap length) and _k_ . output _l_ , _k_ 3, 5 ������������������������������������ 3, 7 ����������������������������������������� 3, 10 ���������������������������������������������� 3, 13 ��������������������������������������������������

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

36

##### Repeats

Basic principle: repeats foil assembly

Longer and longer substrings allow us to “anchor” more of the repeat to its non-repetitive context:

�������������������������������������������������������������

Often we can “walk in” from both sides.  When we meet in the middle, the repeat is resolved:

������������������������������������������������������������


Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

37

##### Repeats

Basic principle: repeats foil assembly

Yet another example using Greedy-SCS:

Input: �������������������������������������������������������������

output _l_ , _k_

3, 7 ������������������������������������������� 3, 13 �������������������������������������������������

- 3, 19 ��������������������������������������������������������� 3, 25 �������������������������������������������������������������

longer and longer substrings allow us to “reach” further into the repeat

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

38

##### Repeats

Picture the portion of the overlap graph involving repeat A ~~Repeat A~~


<!-- Start of picture text -->
L1 R1<br>L2 R2<br>Assume A is longer<br>L3 R3<br>than read length<br>L4 R4<br>Lots of overlaps<br>among reads from A<br>L1 R1<br>L2<br>R2<br>L3<br>R3<br>L4<br>R4<br>ches of<br>et<br>genome<br>Str<br>Reads<br><!-- End of picture text -->

Even if we avoid collapsing copies of A, we can’t know which paths in correspond to which paths out

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

39

#### Layout

The overlap graph is big and messy.  Contigs don’t “pop out” at us. Below: part of the overlap graph for ����������������������������������������������� _l_ = 4, _k_ = 7


<!-- Start of picture text -->
� �<br>� ������� � � � � ������� � � �<br>�<br>� �<br>� � � ������� � �<br>������� ������� � �<br>�<br>� � � ������� �������<br>������� � � �<br>� �<br>� �<br>� �<br>������� �<br>�<br>� ������� �� ������� � � � �<br>� � � ������� � � � ������� �<br>� � �<br>������� �� �� � � �������� � �������� � �� � ������� � ������� � �������� � �<br>������� � � � ������� � � ����<br>� ������� �������<br>�<br>�<br>� �<br>�<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

40

#### Layout

Picture gets clearer after removing some transitively-inferrible edges


<!-- Start of picture text -->
1<br>��� ��� ���<br>2 2<br>��� ��� ���<br>2 2<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

41

#### Layout

Remove transitively-inferrible edges, starting with edges that skip one node:


<!-- Start of picture text -->
x<br><!-- End of picture text -->


<!-- Start of picture text -->
Before:<br>� �<br>� ������� � � � � ������� � � �<br>�<br>� �<br>� � � ������� � �<br>������� ������� � �<br>�<br>� � � ������� �������<br>������� � � �<br>� �<br>� �<br>� �<br>������� �<br>�<br>� ������� �� ������� � � � �<br>� � � ������� � � � ������� �<br>� � �<br>������� �� �� � � �������� � �������� � �� � ������� � ������� � �������� �<br>������� � � � ������� � �<br>� ������� �������<br>�<br>�<br>� �<br>�<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.


<!-- Start of picture text -->
http://www.langmead-lab.org/teaching-materials/<br><!-- End of picture text -->

42

#### Layout

Remove transitively-inferrible edges, starting with edges that skip one node:


<!-- Start of picture text -->
x<br><!-- End of picture text -->


After:


<!-- Start of picture text -->
�<br>������� � �<br>� � ������� ������� � � �<br>������� � � �<br>������� � ������� � ������� ������� � ������� � ������� � � � ������� � ������� ������� � � ������� � ������� � � � �����<br>�<br>� � ������� �<br>� ������� �������<br>�������<br>�������<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

43

#### Layout

Remove transitively-inferrible edges, starting with edges that skip one or two nodes:


<!-- Start of picture text -->
x<br>x<br>After:<br>� � � � � � �<br>�<br>� ������� ������� ������� ������� ������� ������� ������� �������<br>� � � � � � � � �������<br>� �<br>������� ������� ������� ������� ������� ������� ������� ������� �<br>� � �<br>������� ������� ������� �������<br>�<br><!-- End of picture text -->

###### Even simpler

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

44

#### Layout

Emit contigs corresponding to the non-branching stretches


<!-- Start of picture text -->
Contig 1 Contig 2<br>�������������������� ����������������������<br>Unresolvable repeat<br>Courtesy of Ben Langmead. Used with permission.<br>� � ������� � ������� � ������� � ������� � ������� � ������� � ������� � ������� � ������� � ������� � ������� � ������� � ������� � ������� � ������� � �������<br>������� � ������� � ������� � ������� � ������� � ������� � ������� � ������� � ������� � ������� � ������� � ������� � ������� � ������� � � ������� �<br>� � �<br>������� ������� ������� �������<br>�<br><!-- End of picture text -->

http://www.langmead-lab.org/teaching-materials/

45

#### Layout

In practice, layout step also has to deal with spurious subgraphs, e.g. because of sequencing error


<!-- Start of picture text -->
Possible repeat<br>boundary<br>prune b<br>b<br>a Mismatch a<br>...<br><!-- End of picture text -->

Mismatch could be due to sequencing error or repeat.  Since the path through **b** ends abruptly we might conclude it’s an error and prune **b** .

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

46

##### Overlap Layout Consensus

Overlap Layout


Build overlap graph

Bundle stretches of the overlap graph into contigs

**Consensus**

**Pick most likely nucleotide sequence for each contig**

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

47

##### Consensus

������������������������������������� ������������������������������������� ������������������������������������� ������������������������������������� ������������������������������������� �������������������������������������

Take reads that make up a contig and line them up

Take consensus, i.e. majority vote

At each position, ask: what nucleotide (and/or gap) is here? Complications: (a) sequencing error, (b) ploidy

Say the true genotype is AG, but we have a high sequencing error rate and only about 6 reads covering the position.

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

48

##### Overlap Layout Consensus

Build overlap graph Overlap Layout Bundle stretches of the overlap graph into contigs Consensus Pick most likely nucleotide sequence for each contig

What’s the main drawback of OLC?

Building overlap graph can be slow.

2<sup>nd</sup> -generation sequencing datasets are ~ 100s of millions or billions of reads, hundreds of billions of nucleotides total

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

49

##### Assembly alternatives

Alternative 1: Overlap-Layout-Consensus (OLC) assembly Alternative 2: de Bruijn graph (DBG) assembly


<!-- Start of picture text -->
Overlap Error correction<br>Layout de Bruijn graph<br>Consensus Refine<br>Scaffolding<br><!-- End of picture text -->


<!-- Start of picture text -->
Courtesy of Ben Langmead. Used with permission.<br><!-- End of picture text -->

http://www.langmead-lab.org/teaching-materials/

50

Flow chart removed due to copyright restrictions.

51

Table removed due to copyright restrictions.

52

###### ����������������������������������������������������������� �����������������<sup>�</sup> ���������������������

Courtesy of Cold Spring Harbor Laboratory Press. Used with permission. Source: Simpson, Jared T., and Richard Durbin. "Efficient De Novo Assembly of Large Genomes using Compressed Data Structures." _Genome Research_ 22, no. 3 (2012): 549-56.

53

##### Assembly alternatives

Alternative 1: Overlap-Layout-Consensus (OLC) assembly Alternative 2: de Bruijn graph (DBG) assembly


<!-- Start of picture text -->
Overlap Error correction<br>Layout de Bruijn graph<br>Consensus Refine<br>Scaffolding<br><!-- End of picture text -->


<!-- Start of picture text -->
Courtesy of Ben Langmead. Used with permission.<br><!-- End of picture text -->

http://www.langmead-lab.org/teaching-materials/

54

##### De Bruijn graph assembly

A formulation conceptually similar to overlapping/SCS, but has some potentially helpful properties not shared by SCS.

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

55

##### k-mer

“k-mer” is a substring of length k S: ������������ mer: from Greek meaning “part” A 4-mer of S: ���� All 3-mers of S: ��� ���� ����� ������ ������� �������� ��������� ���������� ����������� ������������

I’ll use “k-1-mer” to refer to a substring of length k - 1

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

56

##### De Bruijn graph

As usual, we start with a collection of reads, which are substrings of the reference genome.

���, ���, ���, ���, ���

��� is a k-mer (k = 3).  �� is its left k-1-mer, and �� is its right k-1-mer.

��� 3-mer �� �� L R

���’s left 2-mer ���’s right 2-mer

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

57

##### De Bruijn graph

Take each length-3 input string and split it into two overlapping substrings of length 2.  Call these the left and right 2-mers.

�������

> take all 3-mers: ���, ���, ���, ���, ���

> form L/R 2-mers: ��, ��, ��, ��, ��, ��, ��, ��, ��, �� L R L R L R L R L R

Let 2-mers be nodes in a new graph.  Draw a directed edge from each left 2-mer to corresponding right 2-mer:


<!-- Start of picture text -->
��<br>�� ��<br>��<br><!-- End of picture text -->

Each edge in this graph corresponds to a length-3 input string

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

58

##### De Bruijn graph


<!-- Start of picture text -->
��<br>���<br>���<br>���<br>�� ��<br>�� ���<br>���<br><!-- End of picture text -->

An edge corresponds to an overlap (of length -2) between two k-1 mers. More precisely, it corresponds to a k-mer from the input.

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

59

##### De Bruijn graph


<!-- Start of picture text -->
��<br>���<br>���<br>���<br>�� ��<br>�� ���<br>���<br>���<br><!-- End of picture text -->

If we add one more B to our input string: ��������, and rebuild the De Bruijn graph accordingly, we get a multiedge.

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

60

##### Eulerian walk definitions and statements

Node is balanced if indegree equals outdegree

Node is semi-balanced if indegree differs from outdegree by 1

Graph is connected if each node can be reached by some other node Eulerian walk visits each edge exactly once

Not all graphs have Eulerian walks.  Graphs that do are Eulerian. (For simplicity, we won’t distinguish Eulerian from semi-Eulerian.)


<!-- Start of picture text -->
��<br>�� ��<br>��<br><!-- End of picture text -->

A directed, connected graph is Eulerian if and only if it has at most 2 semi-balanced nodes and all other nodes are balanced

Jones and Pevzner section 8.8

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

61

##### De Bruijn graph

Back to our De Bruijn graph


<mark>��</mark> ���, ���, ���, ���, ��� <mark>�� ��</mark> ��, ��, ��, ��, ��, ��, ��, ��, ��, �� <mark>��</mark> L R L R L R L R L R


Is it Eulerian? Yes

Argument 1:  �� → �� → �� → �� → �� → ��

Argument 2: �� and �� are semi-balanced, �� and �� are balanced

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

62

##### De Bruijn graph


<!-- Start of picture text -->
����<br>���� ����<br>����<br> where each length-kk<br>����<br>5<br>��������������������� ����<br>����� ����<br>���������<br>����<br>k-1 -1  ����<br>����<br><!-- End of picture text -->

A procedure for making a De Bruijn graph for a genome

Assume perfect sequencing where each length-kk substring is sequenced exactly once with no errors

Pick a substring length k: 5

Start with each read:

Take each k mer and split into left and right k-1 mers

Add k-1 mers as nodes to De Bruijn graph (if not already there), add edge from left k-1 -1 mer to right k-1 mer

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

63

##### De Bruijn graph


<!-- Start of picture text -->
����<br>���� ����<br>����<br>����<br>����<br><!-- End of picture text -->

- For genome assembly each k-mer is ���� recorded in “twin” nodes – one node in the forward direction and one node in reverse complement

   - k  is odd so no node can be its own reverse complement


<!-- Start of picture text -->
����<br><!-- End of picture text -->

- We will not show reverse complement twin nodes to cut down on clutter


<!-- Start of picture text -->
����<br><!-- End of picture text -->


<!-- Start of picture text -->
����<br><!-- End of picture text -->


<!-- Start of picture text -->
����<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

64

##### De Bruijn graph


<!-- Start of picture text -->
���� ���� ���� ���� ���� ���� ���� ����<br>���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ����<br>���� ���� ���� ���� ���� ���� ����<br>���� ���� ���� ���� ���� ����<br>���� ���� ���� ���� ����<br>����<br><!-- End of picture text -->

First 8 k-mer additions, k = 5 ���������������������

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

65


<!-- Start of picture text -->
De Bruijn graph<br>���� ���� ���� ���� ����<br>���� ���� ���� ���� ���� ���� ���� ���� ���� ����<br>���� ���� ���� ���� ����<br>���� ���� ���� ���� ����<br>���� ���� ���� ���� ����<br>���� ���� ���� ����<br>���� ���� ����<br>���� ����<br>Last 5 k-mer additions, k = 5<br>���������������������<br>����<br>Finished graph<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

66

##### De Bruijn graph

With perfect sequencing, this procedure always yields an Eulerian graph.  Why?

Node for k-1-mer from left end is semi-balanced with one more outgoing edge than incoming *

Node for k-1-mer at right end is semi-balanced with one more incoming than outgoing *

Other nodes are balanced since # times k-1-mer occurs as a left k-1-mer = # times it occurs as a right k-1-mer

###### * Unless genome is circular


<!-- Start of picture text -->
����<br>���� ����<br>����<br>����<br>����<br>����<br>����<br>����<br>����<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

67

##### De Bruijn graph

Assuming perfect sequencing, procedure yields graph with Eulerian walk that can be found efficiently.

We saw cases where Eulerian walk corresponds to the original superstring.  Is this always the case?


<!-- Start of picture text -->
����<br>���� ����<br>����<br>����<br>����<br>����<br>����<br>����<br>����<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

68

##### De Bruijn graph

**No** : graph can have multiple Eulerian walks, only one of which corresponds to original superstring

Right: graph for ZABCDABEFABY, k = 3

Alternative Eulerian walks:

�� → �� → �� → �� → �� → �� → �� → �� → �� → �� → ��

�� → �� → �� → �� → �� → �� → �� → �� → �� → �� → ��

These correspond to two edge-disjoint directed cycles joined by node ��

�� is a repeat: ZABCDABEFABY


<!-- Start of picture text -->
��<br>��<br>�� ��<br>��<br>�� ��<br>��<br>��<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

69

##### De Bruijn graph


<!-- Start of picture text -->
��<br>��<br>�� ��<br>��<br>�� ��<br>��<br>��<br><!-- End of picture text -->

This is the first sign that Eulerian walks can’t solve all our problems

Other signs emerge when we think about how actual sequencing differs from our idealized construction

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

70

##### De Bruijn graph

Gaps in coverage can lead to disconnected graph Graph for ���������������������, k = 5:


<!-- Start of picture text -->
����<br>���� ����<br>����<br>����<br>����<br>����<br>����<br>����<br>����<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

71

##### De Bruijn graph

Gaps in coverage can lead to disconnected graph

Graph for ���������������������, k = 5 but omitting ����� :


<!-- Start of picture text -->
���� ����<br>���� ���� ����<br>���� ����<br>���� ����<br>����<br><!-- End of picture text -->

Connected components are individually Eulerian, overall graph is not

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

72

##### De Bruijn graph

Differences in coverage also lead to nonEulerian graph

Graph for ���������������������, k = 5 but with extra copy of ����� : Graph has 4 semi-balanced nodes, isn’t Eulerian


<!-- Start of picture text -->
����<br>���� ����<br>����<br>����<br>����<br>����<br>����<br>����<br>����<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

73

##### De Bruijn graph

Errors and differences between chromosomes also lead to non-Eulerian graphs

Graph for ���������������������, k = 5 but with error that turns a copy of ����� into �����

Graph is not connected; largest component is not Eulerian


<!-- Start of picture text -->
���� ����<br>���� ���� ����<br>����<br>����<br>����<br>����<br>����<br>����<br>����<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

74

##### De Bruijn graph

How much work to build graph?


<!-- Start of picture text -->
������� �������<br>������� �������<br>������� �������<br>������� �������<br>������� �������<br><!-- End of picture text -->

For each k-mer, add 1 edge and up to 2 nodes Reasonable to say this is O(1) expected work Assume hash map encodes nodes & edges Assume k-1-mers fit in O(1) machine words, and hashing O(1) machine words is O(1) work Querying / adding a key is O(1) expected work O(1) expected work for 1 k-mer, O(N) overall

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

75

##### De Bruijn graph

Timed De Bruijn graph construction applied to progressively longer prefixes of lambda phage genome, k = 14


<!-- Start of picture text -->
O(N) expectation<br>appears to work in<br>practice, at least for this<br>small example<br>0 10000 20000 30000 40000 50000<br>Length of genome<br>0.20<br>0.15<br>0.10<br>Seconds required to build<br>0.05<br>0.00<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

76

##### De Bruijn graph

In typical assembly projects, average coverage is ~ 30 - 50


<!-- Start of picture text -->
����<br>���� ����<br>����<br>����<br>����<br>����<br>����<br>����<br>����<br><!-- End of picture text -->

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

77

##### De Bruijn graph

In typical assembly projects, average coverage is ~ 30 - 50


<!-- Start of picture text -->
����<br>����<br>��<br>���� ���� ���� ����<br>�� ��<br>���� ���� ��<br>��<br>���� ����<br>��<br>���� ����<br>��<br>���� ����<br>��<br>���� ����<br>��<br>����<br>Before: one  After: one weighted ����<br>��<br>edge per k-mer edge per distinct k-mer<br>����<br>����<br><!-- End of picture text -->

Same edge might appear in dozens of copies; let’s use edge weights instead Weight = # times k-mer occurs Using weights, there’s one weighted edge for each distinct k-mer

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

78

### ������������������������������������

- ���������������������

   - ����������������������


<!-- Start of picture text -->
B’<br>A B<br>A<br>B<br><!-- End of picture text -->

- ������������������������

   - �����������


<!-- Start of picture text -->
B’<br>A C A B* C<br>B<br><!-- End of picture text -->

- ��������������

   - ������������������������������


<!-- Start of picture text -->
A B<br>A B<br>x<br>C D<br>C D<br><!-- End of picture text -->

Figure   adapted   from   presentaFon   by   Michael   Schatz

79

##### De Bruijn graph

What are the limitations of De Bruijn graphs?

Reads are immediately split into shorter k-mers; can’t resolve repeats as well as overlap graph

Only a very specific type of “overlap” is considered, which makes dealing with errors more complicated.

Read coherence is lost.  Some paths through De Bruijn graph are inconsistent with respect to input reads.     Need to thread reads though De Bruijn graph to recover information lost when reads are fragmented into k-mers.

This is the OLC � DBG tradeoff

Single most important benefit of De Bruijn graph is speed and simplicity.

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

80

##### Assembly alternatives

Alternative 1: Overlap-Layout-Consensus (OLC) assembly Alternative 2: de Bruijn graph (DBG) assembly


<!-- Start of picture text -->
Overlap Error correction<br>Layout de Bruijn graph<br>Consensus Refine<br>Scaffolding<br><!-- End of picture text -->


<!-- Start of picture text -->
Courtesy of Ben Langmead. Used with permission.<br><!-- End of picture text -->

http://www.langmead-lab.org/teaching-materials/

81

_��������_ ��������������������� ��������

Courtesy of Nature Education. Used with permission. Source: Green, Eric D. "Strategies for the Systematic Sequencing of Complex Genomes." _Nature Reviews Genetics_ 2, no. 8 (2001): 573-83.

��������������������������������������������������������������������������

82

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [06 slides Part 03 — →](03-06-slides-part-03.md)

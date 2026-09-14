---
title: Introduction
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/compiled/compiled-compiled.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `compiled/compiled-compiled.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Computational Biology: Genomes, Networks, Evolution MIT course 6.047/6.878

Taught by Prof. Manolis Kellis

January 6, 2016

ii

CONTENTS

|**1**<br>**Intr**|**oducti**|**on to the Course**|**3**|
|---|---|---|---|
|1.1|Introd|uction and Goals<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>3|
||1.1.1|A course on computational biology . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>3|
||1.1.2|Duality of Goals: Foundations and Frontiers. . . . . . . . . . . . . . . . . .|. . . . . .<br>3|
||1.1.3|Duality of disciplines: Computation and Biology . . . . . . . . . . . . . . .|. . . . . .<br>4|
||1.1.4|Why Computational Biology? . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>4|
||1.1.5|Finding Functional Elements: A Computational Biology Question<br>. . . . .|. . . . . .<br>6|
|1.2|Final|Project - Introduction to Research In Computational Biology . . . . . . . . .|. . . . . .<br>7|
||1.2.1|Final project goals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>7|
||1.2.2|Final project milestones . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>7|
||1.2.3|Project deliverables<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>8|
||1.2.4|Project grading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>8|
|1.3|Additi|onal materials . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>9|
||1.3.1|Online Materials for Fall 2015 . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>9|
||1.3.2|Textbooks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>9|
|1.4|Crash|Course in Molecular Biology . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>9|
||1.4.1|The Central Dogma of Molecular Biology . . . . . . . . . . . . . . . . . . .|. . . . . .<br>9|
||1.4.2|DNA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>10|
||1.4.3|Transcription . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>11|
||1.4.4|RNA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>12|
||1.4.5|Translation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>13|
||1.4.6|Protein<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>14|
||1.4.7|Regulation: from Molecules to Life . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>15|
||1.4.8|Metabolism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>16|
||1.4.9|Systems Biology<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>16|
||1.4.10|Synthetic Biology. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>17|
||1.4.11|Model organisms and human biology . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>17|
|1.5|Introd|uction to algorithms and probabilistic inference<br>. . . . . . . . . . . . . . . .|. . . . . .<br>18|
||1.5.1|Probability distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>19|
||1.5.2|Graphical probabilistic models<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>19|
||1.5.3|Bayes rules: priors, likelihood, posterior . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>19|
||1.5.4|Markov Chains and Sequential Models . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>19|
||1.5.5|Probabilistic inference and learning . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>19|
||1.5.6|Max Likelihood and Max A Posteriori Estimates . . . . . . . . . . . . . . .|. . . . . .<br>19|
|**I C**|**om**|**paring Genomes**|**21**|
|**2**<br>**Seq**|**uence **|**Alignment and Dynamic Programming**|**23**|
|2.1|Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>23|


iii

_CONTENTS_

_CONTENTS_

|2.2|Aligni<br>|ng Sequences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>|. . . . . . . .<br>24<br>|
|---|---|---|---|
||2.2.1|Example Alignment<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>24|
||2.2.2|Solving Sequence Alignment . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>24|
|2.3|Proble|m Formulations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>26|
||2.3.1|Formulation 1: Longest Common Substring . . . . . . . . . . . . . . . .|. . . . . . . .<br>26|
||2.3.2|Formulation 2: Longest Common Subsequence (LCS)<br>. . . . . . . . . .|. . . . . . . .<br>27|
||2.3.3|Formulation 3: Sequence Alignment as Edit Distance. . . . . . . . . . .|. . . . . . . .<br>28|
||2.3.4|Formulation 4: Varying Gap Cost Models<br>. . . .|. . . . . . . .<br>28|
||2.3.5|Enumeration<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>29|
|2.4|Dynam|ic Programming<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>29|
||2.4.1|Theory of Dynamic Programming<br>. . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>29|
||2.4.2|Fibonacci Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>30|
||2.4.3|Sequence Alignment using Dynamic Programming . . . . . . . . . . . .|. . . . . . . .<br>32|
|2.5|The N|eedleman-Wunsch Algorithm . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>32|
||2.5.1|Dynamic programming vs. memoization . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>32|
||2.5.2|Problem Statement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>33|
||2.5.3|Index space of subproblems . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>33|
||2.5.4|Local optimality<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>33|
||2.5.5|Optimal Solution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>34|
||2.5.6|Solution Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>34|
||2.5.7|Needleman-Wunsch in practice . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>34|
||2.5.8|Optimizations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>35|
|2.6|Multip|le alignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>37|
||2.6.1|Aligning three sequences . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>37|
||2.6.2|Heuristic multiple alignment<br>. . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>38|
|2.7|Curren|t Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>39|
|2.8|Furthe|r Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>39|
|2.9<br>|Tools <br>|and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>|. . . . . . . .<br>39|
|2.10|What|Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>39|
|2.11|Appen|dix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>39|
||2.11.1|Homology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>39|
||2.11.2|Natural Selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>39|
||2.11.3|Dynamic Programming v. Greedy Algorithms . . . . . . . . . . . . . . .|. . . . . . . .<br>40|
||2.11.4|Pseudocode for the Needleman-Wunsch Algorithm . . . . . . . . . . . .|. . . . . . . .<br>41|
|**3**<br>**Rap**|**id Seq**|**uence Alignment and Database Search**|**43**|
|3.1|Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>43|
|3.2|Global|alignment vs. Local alignment vs. Semi-global alignment<br>. . . . . . . .|. . . . . . . .<br>45|
||3.2.1|Using Dynamic Programming for local alignments<br>. . . . . . . . . . . .|. . . . . . . .<br>47|
||3.2.2|Algorithmic Variations . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>47|
||3.2.3|Generalized gap penalties . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>49|
|3.3|Linear|-time exact string matching<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>49|
||3.3.1|Karp-Rabin Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>49|
|3.4|The B|LAST algorithm (Basic Local Alignment Search Tool). . . . . . . . . . .|. . . . . . . .<br>52|
||3.4.1|The BLAST algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>52|
||3.4.2|Extensions to BLAST . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>54|
|3.5|Pre-pr|ocessing for linear-time string matching . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>54|
||3.5.1|Suffix Trees . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>54|
||3.5.2|Suffix Arrays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>55|
||3.5.3|The Burrows-Wheeler Transform . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>55|
||3.5.4|Fundamental pre-processing . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>55|
||3.5.5|Educated String Matching . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>55|
|3.6|Proba|bilistic Foundations of Sequence Alignment . . . . . . . . . . . . . . . . .|. . . . . . . .<br>56|
|3.7|Curren|t Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>58|


iv

_CONTENTS_

_CONTENTS_

|3.8<br>3.9|Furthe<br>Tools|r Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . <br>and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>58<br> . . . . . .<br>59|
|---|---|---|---|
|3.10|What|Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>59|
|**4**<br>**Com**|**parat**|**ive Genomics I: Genome Annotation**|**61**|
|4.1|Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>62|
||4.1.1|Motivation and Challenge . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>62|
||4.1.2|Importance of many closely–related genomes<br>. . . . . . . . . . . . . . . . .|. . . . . .<br>63|
||4.1.3|Comparative genomics and evolutionary signatures . . . . . . . . . . . . . .|. . . . . .<br>64|
|4.2|Conse|rvation of genomic sequences . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>65|
||4.2.1|Functional elements in _Drosophila_<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>65|
||4.2.2|Rates and patterns of selection . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>65|
|4.3|Excess|Constraint<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>66|
||4.3.1|Causes of Excess Constraint . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>67|
||4.3.2|Modeling Excess Constraint . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>68|
||4.3.3|Excess Constraint in the Human Genome . . . . . . . . . . . . . . . . . . .|. . . . . .<br>69|
||4.3.4|Examples of Excess Constraint . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>71|
||4.3.5|Measuring constraint at individual nucleotides<br>. . . . . . . . . . . . . . . .|. . . . . .<br>72|
|4.4|Divers|ity of evolutionary signatures: An Overview of Selection Patterns . . . . . .|. . . . . .<br>72|
||4.4.1|Selective Pressures On Different Functional Elements. . . . . . . . . . . . .|. . . . . .<br>73|
|4.5|Protei|f<br>n–Coding Signatures<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>75|
||4.5.1|Reading–Frame Conservation (RFC) . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>76|
||4.5.2|Codon–Substitution Frequencies (CSFs) . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>77|
||4.5.3|Classification of _Drosophila_ Genome Sequences . . . . . . . . . . . . . . . .|. . . . . .<br>80|
||4.5.4|i<br>Leaky Stop Codons. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>81|
|4.6|micro|RNA (miRNA) Gene Signatures<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>84|
||4.6.1|Computational Challenge . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>84|
||4.6.2|Unusual miRNA Genes<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>85|
||4.6.3|Example: Re-examining ’dubious’ protein-coding genes<br>. . . . . . . . . . .|. . . . . .<br>87|
|4.7|Regul|atory Motifs<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>87|
||4.7.1|Computationally Detecting Regulatory Motifs. . . . . . . . . . . . . . . . .|. . . . . .<br>87|
||4.7.2|Individual Instances of Regulatory Motifs . . . . . . . . . . . . . . . . . . .|. . . . . .<br>88|
|4.8|Curre|nt Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>88|
|4.9|Furthe|r Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>88|
|4.10|Tools|and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>88|
|4.11|Biblio|graphy<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>88|
|**5**<br>**Gen**|**ome A**|**ssembly and Whole-Genome Alignment**|**89**|
|5.1|Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>91|
|5.2|Genom|e Assembly I: Overlap-Layout-Consensus Approach . . . . . . . . . . . . . .|. . . . . .<br>91|
||5.2.1|Setting up the experiment . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>91|
||5.2.2|Finding overlapping reads . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>93|
||5.2.3|Merging reads into contigs . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>94|
||5.2.4|Laying out contig graph into scaffolds<br>. . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>95|
||5.2.5|f<br>Deriving consensus sequence<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>96|
|5.3|Genom|e Assembly II: String graph methods . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>97|
||5.3.1|String graph definition and construction . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>97|
||5.3.2|i<br>Flows and graph consistency<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>99|
||5.3.3|Feasible flow<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . .<br>99|
||5.3.4|l<br>Dealing with sequencing errors . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . 100|
||5.3.5|Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . 100|
|5.4|Whole|-Genome Alignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . 100|
||5.4.1|Global, local, and ’glocal’ alignment . . . . . . . . . . . . . . . . . . . . . .|. . . . . . 100|
||5.4.2|Lagan: Chaining local alignments. . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . 101|


v

_CONTENTS_

_CONTENTS_

|5.5<br>|Gene-<br>|based region alignment<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102<br><br>|
|---|---|---|
|5.6|Mecha|nisms of Genome Evolution<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105|
||5.6.1|Chromosomal Rearrangements<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106|
|5.7|Whole|Genome Duplication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107|
|5.8|Additi|onal figures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107|
|**6**<br>**Ba**|**cterial **|**Genomics– Molecular Evolution at the Level of Ecosystems**<br>**111**|
|6.1|Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111|
||6.1.1|Evolution of microbiome research . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112|
||6.1.2|Data generation for microbiome research. . . . . . . . . . . . . . . . . . . . . . . . . . 112|
|6.2|Study|1: Evolution of life on earth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112|
|6.3|Study|2: Pediatric IBD study with Athos Boudvaros . . . . . . . . . . . . . . . . . . . . . . . 113|
|6.4|Study|3: Human Gut Ecology (HuGE) project<br>. . . . . . . . . . . . . . . . . . . . . . . . . . 114|
|6.5|Study <br>|4: Microbiome as the connection between diet and phenotype . . . . . . . . . . . . . . 118<br>f|
|6.6|Study<br>resista|5: Horizontal Gene Transfer (HGT) between bacterial groups and its effect on antibiotic<br>nce . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119|
|6.7|Study|6: Identifying virulence factors in Meningitis . . . . . . . . . . . . . . . . . . . . . . . . 119|
|6.8|Q/A .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121|
|6.9|Curren|t research directions<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122|
|6.10|Furthe|r Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122|
|6.11|Tools|and techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122|
|6.12|What|have we learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122|
|**II C**|**od**|**ing and Non-Coding Genes**<br>**125**|
|**7**<br>**Hid**|**den M**|**arkov Models I**<br>**127**|
|7.1|Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127|
|7.2|Motiva|tion: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128|
||7.2.1|We have a new sequence of DNA, now what? . . . . . . . . . . . . . . . . . . . . . . . 128|
||7.2.2|Why probabilistic sequence modeling? . . . . . . . . . . . . . . . . . . . . . . . . . . . 129|
|7.3|Marko|v Chains and HMMS: From Example To Formalizing . . . . . . . . . . . . . . . . . . . 129|
||7.3.1|Motivating Example: Weather Prediction . . . . . . . . . . . . . . . . . . . . . . . . . 129|
||7.3.2|Formalizing of Markov Chain and HMMS . . . . . . . . . . . . . . . . . . . . . . . . . 129|
|7.4|Apply|HMM to Real World: From Casino to Biology . . . . . . . . . . . . . . . . . . . . . . . 131|
||7.4.1|The Dishonest Casino . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131|
||7.4.2|Back to Biology<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134|
|7.5|Algori|thmic Settings for HMMs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137|
||7.5.1|Scoring<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137|
||7.5.2|Decoding<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138|
||7.5.3|Evaluation<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140|
|7.6|An Int|eresting Question: Can We Incorporate Memory in Our Model? . . . . . . . . . . . . . 142|
|7.7|Furthe|r Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143|
||7.7.1|Length Distributions of States and Generalized Hidden Markov Models<br>. . . . . . . . 143|
||7.7.2<br>|Conditional random fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143<br>|
|7.8|Curren|t Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143|
|7.9|Tools|and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143|
|7.10|What|Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143|
|**8**<br>**Hid**|**den M**|**arkov Models II - Posterior Decoding and Learning**<br>**145**|
|8.1|Review|of previous lecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145|
||8.1.1|Introduction to Hidden Markov Models<br>. . . . . . . . . . . . . . . . . . . . . . . . . . 145|
||8.1.2|Genomic Applications of HMMs<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146|
||8.1.3|Viterbi decoding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147|


vi

_CONTENTS_

_CONTENTS_

||8.1.4<br>Forward Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 147|
|---|---|---|
||8.1.5<br>This lecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 149|
|8.2|Posterior Decoding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 150|
||8.2.1<br>Motivation<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 150|
||8.2.2<br>Backward Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 150|
||8.2.3<br>The Big Picture<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 152|
|8.3|Encoding Memory in a HMM: Detection of CpG islands . . . . . . . . . . .|. . . . . . . . . . 153|
|8.4|Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . <br><br>|. . . . . . . . . . 155<br>|
||8.4.1<br>Supervised Learning . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 156|
||8.4.2<br>Unsupervised Learning. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 156|
|8.5|Using HMMs to align sequences with affine gap penalties<br>. . . . . . . . . .|. . . . . . . . . . 159|
|8.6|Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 160|
|8.7|Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 162|
|8.8|Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 162|
|8.9|What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 162|
|**9**<br>**Gen**|**e Identification: Gene Structure, Semi-Markov, CRFs**|**163**|
|9.1|Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 163|
|9.2|Overview of Chapter Contents<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 164|
|9.3|Eukaryotic Genes: An Introduction . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 164|
|9.4|Assumptions for Computational Gene Identification<br>. . . . . . . . . . . . .|. . . . . . . . . . 164|
|9.5|i<br>Hidden Markov Models<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 165|
|9.6|Conditional Random Fields . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 166|
|9.7|Other Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 167|
|9.8|Conclusion<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 168|
||9.8.1<br>HMM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 168|
||9.8.2<br>CRF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 168|
|9.9|Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 169|
|9.10|Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 169|
|9.11|Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 169|
|9.12|What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 169|
|**10 RN**|**A Folding**|**171**|
|10.1|Motivation and Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 172|
|10.2|Chemistry of RNA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 172|
|10.3|Origin and Functions of RNA . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 173|
||10.3.1 Riboswitches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 173|
||10.3.2 microRNAs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 173|
||10.3.3 Other types of RNA . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 174|
|10.4|RNA Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 174|
|10.5|RNA Folding Problem and Approaches. . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 176|
||10.5.1 Nussinov’s algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 177|
||10.5.2 Zuker Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 178|
|10.6|Evolution of RNA<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 181|
|10.7|Probabilistic Approach to the RNA Folding Problem . . . . . . . . . . . . .|. . . . . . . . . . 181|
||10.7.1 Application of SCFGs . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 182|
|10.8|Advanced topics<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 183|
||10.8.1 Other problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 183|
||10.8.2 Relevance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 185|
||10.8.3 Current research . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 185|
|10.9|Summary and key points. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 185|
|10.1|0Further reading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 186|


vii

_CONTENTS_

_CONTENTS_

|**11 RNA Modifications**|**189**|
|---|---|
|11.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 189|
|11.2 Post-Transcriptional Regulation . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 190|
|11.2.1 Basics of Protein Translation . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 190|
|11.2.2 Measuring Translation . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 191|
|11.2.3 Codon Evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 193|
|11.2.4 Translational Regulation . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 195|
|11.3 Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 195|
|11.4 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 195|
|11.5 Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 195|
|11.6 What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 195|
|**12 Large Intergenic non-Coding RNAs**|**197**|
|12.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 197|
|12.2 Noncoding RNAs from Plants to Mammals<br>. . . . . . . . . . . . . . . . . . . . .|. . . . . . . 198|
|12.2.1 Long non-coding RNAs<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 199|
|12.3 Practical topic: RNAseq . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 199|
|12.3.1 How it works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 199|
|12.3.2 Aligning RNA-Seq reads to genomes and transcriptomes . . . . . . . . . .|. . . . . . . 200|
|12.3.3 Calculating expression of genes and transcripts . . . . . . . . . . . . . . .|. . . . . . . 202|
|12.3.4 Differential analysis with RNA-Seq . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 203|
|12.4 Long non-coding RNAs in Epigenetic Regulation . . . . . . . . . . . . . . . . . .|. . . . . . . 204|
|12.5 Integergenic Non-coding RNAs: missing lincs in Stem/Cancer cells?<br>. . . . . . .|. . . . . . . 206|
|12.5.1 An example: XIST . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 206|
|12.6 Technologies: in the wet lab, how can we find these? . . . . . . . . . . . . . . . .|. . . . . . . 206|
|12.6.1 Example: p53 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 207|
|12.7 Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 208|
|12.8 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 208|
|12.9 Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 208|
|12.10What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 208|
|**13 Small RNA**|**209**|
|13.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 209|
|13.1.1 ncRNA classifications<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 209|
|13.1.2 Small ncRNA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 211|
|13.1.3 Long ncRNA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 211|
|13.2 RNA Interference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 212|
|13.2.1 History of discovery<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 212|
|13.2.2 Biogenesis pathways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 212|
|13.2.3 Functions and silencing mechanism . . . . . . . . . . . . . . . . . . . . . . <br>|. . . . . . . 213|
|**III Gene and Genome Regulation**|**217**|
|**14 mRNA sequencing for Expression Analysis and Transcript discovery**|**219**|
|14.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 219|
|14.2 Expression Microarrays<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 220|
|14.3 The Biology of mRNA Sequencing<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 220|
|14.4 Read Mapping - Spaced Seed Alignment . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 220|
|14.5 Reconstruction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 221|
|14.6 Quantification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 224|


viii

_CONTENTS_

_CONTENTS_

|**15 Gen**<br>15.1|**e Regulation 1 –Gene Expression Clustering**<br> Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**225**<br>. . . . 226|
|---|---|---|
||15.1.1 Clustering vs Classification<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 226|
||i<br>15.1.2 Applications<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 226|
|15.2|Methods for Measuring Gene Expression . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 227|
||15.2.1 Microarrays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 227|
||15.2.2 RNA-seq<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 228|
||15.2.3 Gene Expression Matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 229|
|15.3|Clustering Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 231|
||15.3.1 _K_-Means Clustering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 231|
||15.3.2 Fuzzy _K_-Means Clustering<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 232|
||15.3.3 _K_-Means as a Generative Model . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 233|
||15.3.4 Expectation Maximization. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 234|
||15.3.5 The limitations of the _K_-Means algorithm . . . . . . . . . . . . . . . . . . . . .|. . . . 235|
||15.3.6 Hierarchical Clustering. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 235|
||15.3.7 Evaluating Cluster Performance<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 236|
|15.4|Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 237|
|15.5|Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 237|
|15.6|Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 237|
|15.7|What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 238|
|**16 Gen**|**e Regulation 2 –Classification**|**239**|
|16.1|**i**<br> Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 239|
|16.2|Classification - Bayesian Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 240|
||16.2.1 Single Features and Bayes Rule . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 240|
||16.2.2 Collecting Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 242|
||16.2.3 Estimating Priors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 242|
||16.2.4 Multiple features and Naive Bayes . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 243|
||16.2.5 Testing a classifier . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 243|
||i<br>16.2.6 MAESTRO Mitochondrial Protein Classification . . . . . . . . . . . . . . . . .|. . . . 244|
|16.3|Classification Support Vector Machines . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 245|
||16.3.1 Kernels<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 245|
|16.4|Tumor Classification with SVMs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 247|
|16.5|i<br> Semi-Supervised Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 248|
||16.5.1 Open Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 248|
|16.6|Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 248|
|16.7|Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 248|
|16.8|Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 248|
|**17 Reg**|**ulatory Motifs, Gibbs Sampling, and EM**|**251**|
|17.1|Introduction to regulatory motifs and gene regulation<br>. . . . . . . . . . . . . . . . . .|. . . . 252|
||17.1.1 The regulatory code: Transcription Factors and Motifs . . . . . . . . . . . . . .|. . . . 252|
||17.1.2 Challenges of motif discovery . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 252|
||17.1.3 Motifs summarize TF sequence specificity . . . . . . . . . . . . . . . . . . . . .|. . . . 253|
|17.2|i<br> Expectation maximization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 254|
||17.2.1 The key idea behind EM. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 254|
||17.2.2 The E step: Estimating _Zij_ from the PWM . . . . . . . . . . . . . . . . . . . .|. . . . 255|
||<br>17.2.3 M step: Finding the maximum likelihood motif from starting positions Zij . . .|. . . . 256|
|17.3|Gibbs Sampling: Sample from joint (M,Zij) distribution . . . . . . . . . . . . . . . . .|. . . . 257|
||17.3.1 Sampling motif positions based on the Z vector . . . . . . . . . . . . . . . . . .|. . . . 257|
||17.3.2 More likely to find global maximum, easy to implement . . . . . . . . . . . . .|. . . . 257|
|17.4|De novo motif discovery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 258|
||1741Motifdiscoveryusinggenome-wideconservation<br>|258|
||..     <br>. . . . . . . . . . . . . . . . . <br>17.4.2 Validation of discovered motifs with functional datasets . . . . . . . . . . . . .|. . . . <br>. . . . 259|


ix

_CONTENTS_

_CONTENTS_

|17.5 Evolutionary signatures for instance identification. . . . . . . . . . . . . . . . . . . . . . . . . 259<br>i|
|---|
|17.6 Phylogenies, Branch length score Confidence score . . . . . . . . . . . . . . . . . . . . . . . . 259|
|i<br>17.6.1 Foreground vs. background. Real vs. control motifs. . . . . . . . . . . . . . . . . . . . 259|
|17.7 Possibly deprecated stuff below: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259|
|17.7.1 Greedy<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259|
|17.8 Comparing different Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260|
|17.9 OOPS,ZOOPS,TCM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260|
|17.10Extension of the EM Approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261|
|17.10.1ZOOPS Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261|
|17.10.2Finding Multiple Motifs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262<br>|
|17.11Motif Representation and Information Content . . . . . . . . . . . . . . . . . . . . . . . . . . 262|
|**18 Regulatory Genomics**<br>**265**|
|18.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265|
|18.1.1 History of the Field<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266|
|18.1.2 Open Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266|
|18.2 _De Novo_ Motif Discovery<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266|
|18.2.1 TF Motif Discovery<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266|
|18.2.2 Validating Discovered Motifs<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267|
|18.2.3 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267|
|18.3 Predicting Regular Targets<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268|
|18.3.1 Motif Instance Identification<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268|
|18.3.2 Validating Targets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268|
|18.4 MicroRNA Genes and Targets. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269|
|18.4.1 MiRNA Gene Discovery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269|
|18.4.2 Validating Discovered MiRNAs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269|
|18.4.3 MiRNA’s 5’ End Identification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270|
|18.4.4 Functional Motifs in Coding Regions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270|
|18.5 Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270|
|18.6 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270|
|18.7 Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270|
|18.8 What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270|
|**19 Epigenomics/Chromatin States**<br>**271**|
|19.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272|
|19.2 Epigenetic Information in Nucleosomes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273|
|19.2.1 Epigenetic Inheritance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274|
|19.3 Epigenomic Assays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275|
|19.3.1 ChIP: a method for determining where proteins bind to DNA or where histones are|
|modified . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275|
|19.3.2 Bisulfite Sequencing: a method for determining where DNA is methylated . . . . . . . 276|
|19.4 Primary data processing of ChIP data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276|
|19.4.1 Read mapping<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276|
|19.4.2 Quality control metrics<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277|
|19.4.3 Peak Calling and Selection<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279|
|19.5 Annotating the Genome Using Chromatin Signatures . . . . . . . . . . . . . . . . . . . . . . . 282|
|19.5.1 Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 283|
|19.5.2 HMMs for Chromatin State Annotation . . . . . . . . . . . . . . . . . . . . . . . . . . 283|
|19.5.3 Choosing the Number of states to model . . . . . . . . . . . . . . . . . . . . . . . . . . 284|
|19.5.4 Results<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285|
|19.5.5 Multiple Cell Types<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286|
|19.6 Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 287|
|19.7 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 288|
|19.8 Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 288|


x

_CONTENTS_

_CONTENTS_

|19.9 What|Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 288|
|---|---|---|
|**20 Networks **|**I: Inference, structure, spectral methods**|**297**|
|20.1 Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 297|
|20.1.1|Introducing Biological Networks<br>. . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 298|
|20.1.2|Interactions Between Biological Networks . . . . . . . . . . . . . . .|. . . . . . . . . . 299|
|20.1.3|Network Representation . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 299|
|20.2 Netwo|rk Centrality Measures . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 301|
|20.2.1|Degree Centrality. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 301|
|20.2.2|Betweenness Centrality<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 302|
|20.2.3|Closeness Centrality . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 303|
|20.2.4|Eigenvector Centrality . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 303|
|20.3 Linear|Algebra Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 303|
|20.3.1|Eigenvectors<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 303|
|20.3.2|Vector decomposition<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 304|
|20.3.3|Diagonal Decomposition . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 304|
|20.3.4|Singular Value Decomposition. . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 305|
|20.4 Sparse|Principal Component Analysis<br>. . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 307|
|20.4.1|Limitations of Principal Component Analysis . . . . . . . . . . . . .|. . . . . . . . . . 307|
|20.4.2|Sparse PCA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 308|
|20.5 Netwo|rk Communities and Modules<br>. . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 311|
|20.5.1|Node-Centric Communities . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 312|
|20.5.2|Group-Centric Communities. . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 313|
|20.5.3|Network-Centric Communities<br>. . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 313|
|20.6 Netwo|rk Diffusion Kernels . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 319|
|20.7 Neural|Networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 321|
|20.7.1|Feed-forward nets<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 321|
|20.7.2|Back-propagation . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 321|
|20.7.3|Deep Learning<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 322|
|20.8 Open I|ssues and Challenges . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 323|
|20.9 Curren|t Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 324|
|20.10Furthe|r Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 324|
|20.11Tools|and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 325|
|20.12What|Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 325|
|**21 Regulator**|**y Networks: Inference, Analysis, Application**|**327**|
|21.1 Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 327|
|21.1.1|Introducing Biological Networks<br>. . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 328|
|21.1.2|Interactions Between Biological Networks . . . . . . . . . . . . . . .|. . . . . . . . . . 329|
|21.1.3|Studying Regulatory Networks . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 329|
|21.2 Struct|ure Inference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 330|
|21.2.1|Key Questions in Structure Inteference. . . . . . . . . . . . . . . . .|. . . . . . . . . . 330|
|21.2.2|Abstract Mathematical Representations for Networks<br>. . . . . . . .|. . . . . . . . . . 330|
|21.3 Overvi|ew of the PGM Learning Task . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 331|
|21.3.1|Parameter Learning for Bayesian Networks<br>. . . . . . . . . . . . . .|. . . . . . . . . . 331|
|21.3.2|Learning Regulatory Programs for Modules . . . . . . . . . . . . . .|. . . . . . . . . . 333|
|21.3.3|Conclusions in Network Inference . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 333|
|21.4 Applic|ations of Networks<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 333|
|21.4.1|Overview of Functional Models . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 333|
|21.4.2|Functional Prediction for Unannotated Nodes . . . . . . . . . . . . .|. . . . . . . . . . 334|
|21.5 Struct|ural Properties of Networks. . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 336|
|21.5.1|Degree distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 336|
|21.5.2|Network motifs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 337|
|21.6 Netwo|rk clustering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . 338|


xi

_CONTENTS_

_CONTENTS_

|21.6.1|An algebraic view to networks<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 339|
|---|---|---|
|21.6.2|The spectral clustering algorithm . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 341|
|**22 Chromatin**|**Interactions**|**345**|
|22.1 Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 345|
|22.1.1|What’s already known . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 346|
|22.1.2|What we don’t know . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 346|
|22.1.3|Why do we study it? . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 347|
|22.2 Releva|nt terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 347|
|22.2.1 <br>|Nuclear lamina . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . <br>|. . . . . . . . 347|
|22.2.2|Lamina Associated Domains(LADs)<br>. . . . . . . . . . . . . . . . . . . .|. . . . . . . . 347|
|22.2.3|Histones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 347|
|22.2.4|Chromatin<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 347|
|22.2.5|Chromosome territories (CT) . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 348|
|22.2.6|Gross folding principles<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 348|
|22.3 Molecu|lar Methods for Studying Nuclear Genome Organization . . . . . . . . .|. . . . . . . . 348|
|22.3.1|Methods for measuring DNA-Nuclear Lamina interactions . . . . . . . .|. . . . . . . . 348|
|22.3.2|Measuring DNA-DNA contacts . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 350|
|22.4 Mappi|ng Genome-Nuclear Lamina Interactions (LADs)<br>. . . . . . . . . . . . .|. . . . . . . . 352|
|22.4.1|Interpreting DamID Data . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 353|
|22.4.2|Interpreting Hi-C Data<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 354|
|22.5 Compu|tational Methods for Studying Nuclear Genome Organization . . . . . .|. . . . . . . . 355|
|22.5.1|Sources of Bias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 355|
|22.5.2|Bias Correction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 355|
|22.5.3|3D-modeling of 3C-based data<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 356|
|22.6 Archit|ecture of Genome Organization<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 356|
|22.6.1|Multiple cell types influence on determining architecture . . . . . . . . .|. . . . . . . . 356|
|22.6.2|Inter-species comparison of lamina associations . . . . . . . . . . . . . .|. . . . . . . . 356|
|22.6.3|A-T Content Rule<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 357|
|22.7 Mecha|nistic Understanding of Genome Architecture<br>. . . . . . . . . . . . . . .|. . . . . . . . 358|
|22.7.1|Understanding Mitosis and LADs . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 358|
|22.7.2|Modeling<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 358|
|22.8 Curren|t Research Directions:<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 359|
|22.8.1|LADs<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 359|
|22.8.2|TADs and Other Compartments: . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 359|
|22.8.3|Other/Miscellaneous:. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 359|
|22.9 Furthe|r Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 360|
|22.10Availa|ble Tools and Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 360|
|22.11What|Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 360|
|**23 Introduct**|**ion to Steady State Metabolic Modeling**|**361**|
|23.1 Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 361|
|23.1.1|What is Metabolism?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 362|
|23.1.2|Why Model Metabolism?<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 362|
|23.2 Model|Building . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 362|
|23.2.1|Chemical Reactions<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 362|
|23.2.2|Steady-State Assumption . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 363|
|23.2.3|Reconstructing Metabolic Pathways<br>. . . . . . . . . . . . . . . . . . . .|. . . . . . . . 364|
|23.3 Metab|olic Flux Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 364|
|23.3.1|Mathematical Representation . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 364|
|23.3.2|Null Space of S . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 365|
|23.3.3|Constraining the Flux Space<br>. . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 366|
|23.3.4|Linear Programming . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 366|
|23.4 Applic|ations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 368|


xii

_CONTENTS_

_CONTENTS_

|23.4.1 _In Silico_ Detection Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 368<br><br>|
|---|
|23.4.2 Quantitative Flux _In Silico_ Model Predictions<br>. . . . . . . . . . . . . . . . . . . . . . 369|
|23.4.3 Quasi Steady State Modeling (QSSM) . . . . . . . . . . . . . . . . . . . . . . . . . . . 370|
|23.4.4 Regulation via Boolean Logic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 371|
|23.4.5 Coupling Gene Expression with Metabolism . . . . . . . . . . . . . . . . . . . . . . . . 373<br>|
|23.4.6 Predicting Nutrient Source<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 374|
|23.5 Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 377|
|23.6 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 377|
|23.7 Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 377|
|23.8 What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 377|
|**24 The ENCODE project: Systematic experimentation and integrative genomics**<br>**379**|
|24.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 379|
|24.2 Experimental Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 380|
|24.3 Computational Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 381|
|24.4 Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 383|
|24.5 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 384|
|24.6 Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 384|
|24.7 What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 384|
|**25 Pharmacogenomics**<br>**387**|
|25.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 387|
|25.2 Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 387|
|25.3 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 387|
|25.4 Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 387|
|25.5 What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 387|
|**26 Synthetic Biology**<br>**389**|
|26.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 389|
|26.2 Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 391|
|26.3 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 392|
|26.4 Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 392|
|26.5 What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 393|
|**IV Phylogenomics and Population Genomics395**|
|**27 Molecular Evolution and Phylogenetics**<br>**397**|
|27.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 398|
|27.2 Basics of Phylogeny<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 398|
|27.2.1 Trees. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 398|
|27.2.2 Traits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 399|
|27.2.3 Methods for Tree Reconstruction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 400|
|27.3 Distance Based Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 402|
|27.3.1 From alignment to distances<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 402|
|27.3.2 Distances to Trees . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 407|
|27.4 Character-Based Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 411|
|27.4.1 Scoring<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 412|
|27.4.2 Search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 417|
|27.5 Possible Theoretical and Practical Issues with Discussed Approach . . . . . . . . . . . . . . . 419|
|27.6 Towards final project . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 419|
|27.6.1 Project Ideas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 419|
|27.6.2ProjectDatasets.......................................419|
|<br>27.7 What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 420|


xiii

_CONTENTS_

_CONTENTS_

|**28 Phylogenomics II**|**421**|
|---|---|
|28.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 422|
|28.2 Inferring Orthologs/Paralogs, Gene Duplication and Loss<br>. . . . . . . . . . . . . . .|. . . . . 422|
|28.2.1 Species Tree. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 422|
|28.2.2 Gene Tree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 423|
|28.2.3 Gene Family Evolution<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 423|
|28.2.4 Reconciliation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 423|
|28.2.5 Interpreting Reconciliation Examples. . . . . . . . . . . . . . . . . . . . . . .|. . . . . 427|
|28.3 Reconstruction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 428|
|28.3.1 Species Tree Reconstruction . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 428|
|28.3.2 Improving Gene Tree Reconstruction and Learning Across Gene Trees . . . .|. . . . . 429|
|28.4 Modeling Population and Allele Frequencies . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 430|
|28.4.1 The Wright-Fisher Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 430|
|28.4.2 The Coalescent Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 432|
|28.4.3 The Multispecies Coalescent Model . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 434|
|28.5 SPIDIR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 434|
|28.5.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 434|
|28.5.2 Method and Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 436|
|28.6 Ancestral Recombination Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 437|
|28.6.1 The Sequentially Markov Coalescent . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 437|
|28.7 Conclusion<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 437|
|28.8 Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 438|
|28.9 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 438|
|28.10Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 438|
|28.11What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 438|
|**29 Population History**|**439**|
|29.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 439|
|29.2 Quick Survey of Human Genetic Variation . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 440|
|29.3 African and European Gene Flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 441|
|29.4 Gene Flow on the Indian Subcontinent . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 442|
|29.4.1 Almost All Mainland Indian Groups are Mixed . . . . . . . . . . . . . . . . .|. . . . . 442|
|29.4.2 Population structure in India is different from Europe . . . . . . . . . . . . .|. . . . . 444|
|29.4.3 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 444|
|29.5 Gene Flow Between Archaic Human Populations . . . . . . . . . . . . . . . . . . . .|. . . . . 445|
|29.5.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 445|
|29.5.2 Evidence of Gene Flow between Humans and Neanderthals . . . . . . . . . .|. . . . . 445|
|29.5.3 Gene Flow between Humans and Denisovans<br>. . . . . . . . . . . . . . . . . .|. . . . . 446|
|29.5.4 Analysis of High Coverage Archaic Genomes<br>. . . . . . . . . . . . . . . . . .|. . . . . 447|
|29.5.5 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 447|
|29.6 European Ancestry and Migrations . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 448|
|29.6.1 Tracing the Origins of European Genetics . . . . . . . . . . . . . . . . . . . .|. . . . . 448|
|29.6.2 Migration from the Steppe<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 449|
|29.6.3 Screening for Natural Selection . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 449|
|29.7 Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 449|
|29.7.1 Techniques for Studying Population Relationships<br>. . . . . . . . . . . . . . .|. . . . . 449|
|29.7.2 Extracting DNA from Neanderthal Bones . . . . . . . . . . . . . . . . . . . .|. . . . . 451|
|29.7.3 Reassembling Ancient DNA . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 452|
|29.8 Research Directions<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 452|
|29.9 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . 453|


xiv

_CONTENTS_

_CONTENTS_

|**30 Population Genetic Variation**<br>30.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|**455**<br> . . . . 456|
|---|---|
|30.2 Population Selection Basics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 456|
|30.2.1 Polymorphisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 456|
|30.2.2 Allele and Genotype Frequencies . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 457|
|30.2.3 Ancestral State of Polymorphisms<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 460|
|30.2.4 Measuring Derived Allele Frequencies<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . . 461|
|30.3 Genetic Linkage. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . <br>fi|. . . . 462|
|30.3.1 Correlation Coefficient _r_<sup>2</sup><br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 463|
|fi<br>30.4 Natural Selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 463|
|30.4.1 Genomics Signals of Natural Selection . . . . . . . . . . . . . . . . . . . . . . .|. . . . 464|
|30.5 Human Evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 467|
|30.5.1 A History of the Study of Population Dynamics. . . . . . . . . . . . . . . . . .|. . . . 467|
|30.5.2 Understanding Disease . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 470|
|30.5.3 Understanding Recent Population Admixture . . . . . . . . . . . . . . . . . . .|. . . . 471|
|30.6 Current Research . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 472|
|30.6.1 HapMap project<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 472|
|30.6.2 1000 genomes project<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 472|
|30.7 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . <br>|. . . . 472|
|**V Medical Genomics**|**475**|
|**31 Medical Genetics – The Past to the Present**|**477**|
|31.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 477|
|31.2 Goals of investigating the genetic basis of disease . . . . . . . . . . . . . . . . . . . . .|. . . . 478|
|31.2.1 Personalized genomic medicine . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 478|
|31.2.2 Informing therapeutic development . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 478|
|31.3 Mendelian Traits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 479|
|31.3.1 Mendel<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 479|
|31.3.2 Linkage Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 479|
|31.4 Complex Traits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 482|
|31.5 Genome-wide Association Studies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 482|
|31.5.1 Events Enabling Genome-wide Association Studies<br>. . . . . . . . . . . . . . .|. . . . 483|
|31.5.2 Quality Controls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 484|
|31.5.3 Testing for Association. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 484|
|31.5.4 Interpretation: How can GWAS inform the biology of disease?<br>. . . . . . . . .|. . . . 486|
|31.5.5 Bottom-up<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 486|
|31.5.6 Top-down . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 487|
|31.5.7 Comparison with Linkage Analysis . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 487|
|31.5.8 Challenges of Non-coding Variants . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 487|
|31.5.9 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 488|
|31.6 Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 488|
|31.7 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 489|
|31.8 Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 489|
|31.9 What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 489|
|**32 Variation 2: : Quantitative trait mapping, eQTLs, molecular trait variation**|**493**|
|32.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 493|
|32.2 eQTL Basics<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 494|
|32.2.1 Cis-eQTLs<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 494|
|32.2.2 Trans-eQTLs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 495|
|32.3 Structure of an eQTL Study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 495|
|32.3.1 Considerations for Expression Data. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 496|


xv

_CONTENTS_

_CONTENTS_

|32.3.2 Considerations for Genomic Data . . . . . . . . . . . . . . . . . . . . . . <br>|. . . . . . . . 496<br>|
|---|---|
|32.3.3 Covariate Adjustment . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 496|
|32.3.4 Points to Consider . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 497|
|32.4 Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 497|
|32.4.1 Quantifying Trait Variation . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 497|
|32.4.2 New Applications. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . <br>|. . . . . . . . 498|
|32.5 What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 498|
|32.6 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 498|
|32.7 Tools and Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 499|
|**33 Missing Heretibility**|**505**|
|33.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 505|
|33.2 Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 505|
|33.3 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 505|
|33.4 Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 505|
|33.5 What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 505|
|**34 Personal Genomes, Synthetic Genomes, Computng in C vs. Si**|**507**|
|34.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 507|
|34.2 Reading and Writing Genomes<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 507|
|34.3 Personal Genomes<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 508|
|34.4 Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 509|
|34.5 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 509|
|34.6 Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 509|
|34.7 What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 509|
|**35 Personal Genomics**|**511**|
|35.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 511|
|35.2 Epidemiology: An Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 512|
|35.3 Genetic Epidemiology<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 513|
|35.4 Molecular Epidemiology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 514|
|35.4.1 meQTLs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 515|
|35.4.2 EWAS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 516|
|35.5 Causality Modeling and Testing . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 516|
|35.5.1 Polygenic Risk Prediction . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 517|
|35.6 Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 518|
|35.7 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 518|
|35.8 Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 518|
|35.9 What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 518|
|**36 Cancer Genomics**|**519**|
|361Intrdtin|519|
|. ouco . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .|
|36.2 Characterization<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 519|
|36.3 Interpretation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 521|
|36.4 Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 521|
|36.5 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 522|
|36.6 Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 522|
|36.7 What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 522|
|**37 Genome Editing**|**523**|
|37.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 523|
|37.1.1 What is **C**RISPR/Cas?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 523|
|37.1.2 Why is CRISPR/Cas important to us? . . . . . . . . . . . . . . . . . . . <br>|. . . . . . . . 523|
|37.1.3Cas-9<br>.....................................|........524|
|<br>                                     <br>37.2 Current Research Directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|<br> . . . . . . . . 524|


xvi

_CONTENTS_

_CONTENTS_

|37.2.1 Improvement of Cas-9 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 524|
|---|
|37.2.2 Current research being done with CRISPR/Cas-9. . . . . . . . . . . . . . . . . . . . . 524|
|37.3 Further Reading<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 525|
|37.4 Tools and Techniques<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 525|
|37.5 What Have We Learned?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 525|


xvii

_CONTENTS_

_CONTENTS_

xviii

_CONTENTS_

History of the Course

_CONTENTS_

## **Preface and Acknowledgements**

These notes summarize the material taught in the MIT course titled “Computational Biology: Genomes, Networks, Evolution”, also cross-listed with Harvard, HST, HSPH and BU over the years. The course was listed as MIT course 6.047/6.878 in 2007-2011 (and under the temporary numbers 6.085/6.095/6.895 in Fall 2005-2006, and 6.096 in Spring 2005). It was cross-listed with MIT/Harvard Health Sciences and Technology (HST) course HST.507 in 2007-2011, Boston University Biological Engineering course BE-562 in 2008 and 2009, and Harvard School of Public Health course IMI231 in 2009-2011.

The course was originally developed by Prof. Manolis Kellis at MIT, with advice from **Silvio Micali** . It was first taught in Spring Spring 2005 as a half-course extension to the Introduction to Algorithms Course (6.046), and as an independent full-credit course in Fall 2005-2011. The course was co-lectured with Prof. **Piotr Indyk** in Fall 2005-2006, who contributed to the material on hashing and dimentionality reduction techniques. It was co-taugh with Prof. **James Galagan** in Fall 2007-2009 who contributed to the lectures on expression clustering, supervised learning and metabolic modelling, and who continued teaching the course independently at BU.

The material in the course has benefited tremendously from courses by **Bonnie Berger** at MIT, whose course “Introduction to Computational Biology (18.417)” was co-taught by Manolis Kellis as a student in Fall 2001, and **Serafim Batzoglou** at Stanford whose course “Computational Genomics (CS262)” was an inspiration for clarity and style and a source of figures and diagrams for the early chapters on alignment and HMMs. Lastly, the material in the course also benefited from two books used extensively in the course in the last several years, titled “Biological Sequence Analysis” by **Durbin, Eddy, Drogh, and Mitchison** , and “Bioinformatics Algorithms” by **Jones and Pevzner** .

The material of several chapters was initially developed by guest lecturers who are experts in their field and contributed new material, figures, slides, organization, and thoughts in the form of one or more lectures. Without them, the corresponding chapters would not have been possible. They are: **Pardis Sabeti** (Population Genetic Variation), **Mark Daly** (Medical Genetics), **David Reich** (Population History), **Eric Alm** (Bacterial Genomics), **John Rinn** (Long Non-Coding RNAs), **James Galagan** (Steady State modeling), **Matt Rasmussen** (Phylogenomics), **Mike Lin** (Gene finding), **Stefan Washietl** (RNA folding), **Jason Ernst** (Epigenomics), **Sushmita Roy** (Regulatory Networks), **Pouya Kheradpour** (Regulatory Genomics).

The Teaching Assistants who taught recitations and help develop the course problem sets have been **Reina Reimann** (Spring 2005), **Pouya Kheradpour** (Fall 2005), **Matt Rasmussen** and **Mike Lin** (Fall 2006), **Mike Lin** and **David Sontag** (Fall 2007), **Matt Rasmussen** and **Pouya Kheradpour** (Fall 2008), **Ed Reznik** and **Bob Altshuler** (Fall 2009), **Matt Edwards** (Fall 2010), and **Melissa Gymrek** (Fall 2011). The notes were originally compiled in a uniform format **Anna Shcherbina** (Fall 2011).

The current and past members of the **MIT CompBio Lab** ( `http://compbio.mit.edu/people.html` ), who have taught me as they grew into experts in their own fields. They are: Matt Rasmussen, Mike Lin, Pouya Kheradpour, Alexander Stark, Xiaohui Xie, Jason Ernst, Sushmita Roy, Luke Ward, Chris Bristow, Abdoulaye Diallo, David Hendrix, Loyal Goff, Stefan Washietl, Daniel Marbach, Mukul Bansal, Matthew Eaton, Irwin Jungreis, Rachel Sealfon, Bob Altshuler, Jessica Wu, Angela Yen, Soheil Feizi, Luis Barrera, Ben Holmes, Anna Ayuso, Wouter Meuleman, Ferhat Ay, Rogerio Candeias, Patrick Meyer, Tom Morgan, Wes Brown, Will Gibson, Rushil Goel, Luisa Di Stefano, Stephan Ossowski, Aviva Presser, Erez Lieberman, Joshua Grochow, Yuliya Kodysh, Leopold Parts, Ameya Deoras, Matt Edwards, Adrian Dalca.

The students taking the class and contributing to the scribe notes are:

- Spring 2005: Dan Arlow, Arhab Battacharyya, Punyashloka Biswal, Adam Bouhenguel, Dexter Chan, Shuvo Chatterjee, Tiffany Dohzen, Lyric Doshy, Robert Figueiredo, Edena Gallagher, Josh Grochow, Aleksas Hauser, Blanca Himes, George Huo, Xiaoming Jia, Scott Johnson, Steven Kannan, Faye Kasemset, Jason Kelly, Daniel Kim, Yuliya Kodysh, Nate Kushman, Lucy Mendel, Jose Pacheco, Sejal Patel, Haiharan Rahul, Gireeja Ranade, Sophie Rapoport, Aditya Rastogi, Shubhangi Saraf, Oded Shaham, Walter Stiehl, Kevin Stolt, James Sun, Xin Sun, Kah Tai, Kah Tay, Chester Tse, Verlik Tzanov, Brian Wu

- Fall 2005: Ebad Ahmed, Christophe Falling, Michael Farry, Elaine Gee, Luke Hutchison, Michael Lin, Grigore Pintilie, Asfandyar Qureshi, Matthew Rasmussen, Alexandru Salcianu, Zeeshan Syed, Hayden

1

_CONTENTS_

History of the Course

_CONTENTS_

#### Taylor, Velin Tzanov, Grant Wang

- Fall 2006: Mats Ahlgren, Zhu Ailing, Bob Altshuler, Nada Amin, Shay Artzi, Solomon Bisker, Allen Bryan, Sumeet Gupta, Adam Kiezun, Richard Koche, Mieszko Lis, Ryan Newton, Michael O’Kelly, Chris Reeder, Jonathan Rhodes, Michael Schnall-Levin, Alex Tsankov, Tarak Upadhyaya, Kush Varshney, Sam Volchenboum, Jon Wetzel, Amy Williams

- Fall 2007: Anton Aboukhalil, Matthew Belmonte, Ellenor Brown, Brad Cater, Alal Eran, Guilherme Fujiwara, Saba Gul, Kate Hoff, Shannon Iyo, Eric Jonas, Peter Kruskall, Michael Lee, Ben Levick, Fulu Li, Alvin Liang, Joshua Lim, Chit-Kwan Lin, Po-Ru Loh, Kevin Modzelewski, Georgis Papachristoudis, Michalis Potamias, Emmanuel Santos, Alex Schwendner, Maryam Shanechi, Timo Somervuo, James Sun, Xin Sun, Robert Toscano, Qingqing Wang, Ning Xie, Qu Zhang, Blaine Ziegler

- Fall 2008: Burak Alver, Tural Badirkhanli, Arnab Bhattacharyya, Can Cenik, Clara Chan, Lydia Chilton, Arkajit Dey, Ardavan Farjadpour, Jeremy Fineman, Bernhard Haeupler, Arman Hajati, Ethan Heilman, Joe Herman, Irwin Jungreis, Arjun Manrai, Nilah Monnier, Christopher Rohde, Rachel Sealfon, Daniel Southern, Paul Steiner, David Stiebel, Mengdi Wang

- Fall 2009: Layla Barkal, Michael Bennie, David Charlton, Guoliang Chew, John Dong, Matthew Edwards, Eric Eisner, Subha Gollakota, Nathan Haseley, Allen Lin, Christopher McFarland, Michael Melgar, Anrae Motes, Anand Oza, Elizabeth Perley, Brianna Petrone, Arya Tafvizi Zavareh, Yi-Chieh Wu, Angela Yen, Morteza Zadimoghaddam, Chelsea Zhang, James Zou

- Fall 2010: Minjeong Ahn, Andreea Bodnari, Wesley Brown, Jenny Cheng, Bianca Dumitrascu, Sam Esfahani, Amer Fejzic, Talitha Forcier, Maria Frendberg, Dhruv Garg, Rushil Goel, Melissa Gymrek, Benjamin Holmes, Wui Ip, Isaac Joseph, Geza Kovacs, Gleb Kuznetsov, Adam Marblestone, Alexander Mccauley, Sheida Nabavi, Jacob Shapiro, Andrew Shum, Ashutosh Singhal, Mark Smith, Mashaal Sohail, Eli Stickgold, Tahin Syed, Lance Wall, Albert Wang, Fulton Wang, Jerry Wang

- Fall 2011: Asa Adadey, Leah Alpert, Ahmed Bakkar, Rebecca Bianco, Brett Boval, Kelly Brock, Peter Carr, Efrain Cermeno, Alex Chernyakhovsky, Diana Chien, Akashnil Dutta, Temuge Enkhbaatar, Maha Farhat, Alec Garza-Galindo, Fred Grober, Gabriel Ha, Marc Hafner, Neel Hajare, Timothy Helbig, Ivan Imaz, Yarden Katz, Gwang Ko, David Ku, Yu-Chi Kuo, Dan Landay, Yinqing Li, Mark Mimee, Selene Mota, Hyun Ji Noh, Chrisantha Perera, Aleksey Pesterev, Michael Quintin, Maria Rodriguez, Megan Roytman, Abhishek Sarkar, Angela Schwarz, Meriem Sefta, Anna Shcherbina, Mindy Shi, Noam Shoresh, Eric Soderstrom, Ying Qi Soh, Sarah Spencer, Derrick Sund, Ruqi Tang, Zenna Tavares, Arvind Thiagarajan, Paul Tillberg, Christos Tzamos, Leonardo Urbina, Manasi Vartak, Nathan Villagaray-Carski, Sajith Wickramasekara, Thomas Willems, Maxim Wolf, Lok Sang Wong, Iris Xu, Johannes Yeh, Deniz Yorukoglu, Boyang Zhao.

- Fall 2013: Maria Alexis, Polina Binder, Jake Bograd-Denton, Orhan Tunc Celiker, Hyunghoon Cho, Brian Cleary, David Danko, Vivek Dasari, Dalesh Dharamshi, Atray Dixit, Joseph Driscoll, John Froberg, Themistoklis Gouleakis, Carissa Jansen, Yuta Kato, Hanna Levitin, Brendan Liu, Quanquan Liu, Yang Li, Julianna Mello, Hayden Metsky, Peter Nguyen, Luke O’Connor, Alexander Pagan, Sebastian Palacios, Peter Palmedo, Jr., Staphany Park, Nicole Power, Emma Seropian, Meena Subramaniam, Nirvan Tyagi, Joseph Vitti, Timothy Wall, Deena Wang, James Weis, Iris Xu, Haoyang Zeng, Sidi Zhang

- Fall 2014: Abdulaziz Alghunaim, Sahar Alkhairy, Benjamin Bauchwitz, Tristan Bepler, Silvia Canas Duarte, Kevin Chen, Michael Coulombe, Lei (Jerry) Ding, Gabriel Filsinger, Matthew Fox, Kristjan Kaseniit, Joseph Kim, David Lazar, William Leiserson, Jenny Lin, Kathy Lin, Yunpeng Liu, Nicolai Ludvigsen, Eric Mazumdar, Hilary Mulholland, Pavel Muravyev, Muneeza Patel, Divya Pillai, Cl´ement Pit-Claudel, Adam Sealfon, Ha Kyung (Kris) Shin, Aradhana Sinha, Daniel Sosa, Yi-Shiuan Tung, Margaret Walker, Sarah Walker, Yuhao Wang, Hui Ting Grace Yeo, Catherine Yun

- Fall 2015: Jonathan Li, Jesse Tordoff, Thrasyvoulos Karydis, Heather Sweeney, Eric Bartell, Anastasiya Belyaeva, Justin Gullingsrud, Cara Weisman, Robert Hunt, Alex Genshaft, Ge Liu, Richard

2

_CONTENTS_

History of the Course

_CONTENTS_

Hsu, Karthik Murugadoss, Sagar Indurkhya, Max Shen, Kevin Tian, Alvin Shi, Connor Duffy, Narek Dshkhunyan, Joyce Hong, Gil Goldshlager, Sophia Liu, Aurora Alvarez-Buylla, Giri Anand, Tejas Sundaresan, Nolan Kamitaki, Bryce Hwang, Hunter Gatewood, Misha Jamy, Nadia Wallace, Carles Boix, Ava Soleimany, Brock Wooldridge, Sadik Yildiz, Anne Kim, Divya Shanmugam, Deniz Aksel, Molly Schmidt, Jonahtan Uesato, Joseph Cunningham, Suganya Sridharma, Oleksandr Chaykovskyy, Eunice Wu, Sam Johnson, Ye Tao

3

_CONTENTS_

History of the Course

_CONTENTS_

4

## CHAPTER **ONE**

## INTRODUCTION TO THE COURSE

### **Figures**

|1.1|In this computational biology problem, we are provided with a sequence of bases, and wish<br>to locate genes and regulatory motifs.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|6|
|---|---|---|
|1.2|The double-helix structure of DNA. Nucleotides are in the center, and the sugar-phosphate<br>backbone lies on the outside.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|11|
|1.3|DNA is packed over several layers of organization into a compact chromosome.<br>. . . . . .|12|
|1.4|RNA is produced from a DNA template during transcription. A “bubble” is opened in the||
||DNA, allowing the RNA polymerase to enter and place down bases complementary to the<br>DNA.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|13|
||(a)<br>Transcription initiation<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|13|
||(b)<br>Transcription elongation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|13|
||(c)<br>Transcription termination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|13|
|1.5|This codon table shows which of the 20 amino acid each of the 3-nucleotide codons in<br>mRNA are translated into. In red are the stop codons, which terminate translation.<br>. . .|14|
|1.6|Operon Lac illustrates a simple biological regulatory system. In the presence of glucose,<br>genes to lactose metabolism are turn out because glucose inactives an activator protein. In<br>the absence of lactose, a repressor protein also turns out the operon. Lactose metabolism<br>genes are expressed only in the presence of lactose and absence of glucose. . . . . . . . . .|15|
|1.7|Metabolic pathways and regulation can be studied by Computational biology.<br>Models<br>are made from genome scale information and used to predict metabolic function and to<br>metabolic engineering. An example of biological engineering is modifying bacteria genome<br>to overproduce artemesenin, an antibiotic used to treat malaria. . . . . . . . . . . . . . . .|16|


## **1.1 Introduction and Goals**

### **1.1.1 A course on computational biology**

These lecture notes are aimed to be taught as a term course on computational biology, each 1.5 hour lecture covering one chapter, coupled with bi-weekly homework assignments and mentoring sessions to help students accomplish their own independent research projects. The notes grew out of MIT course 6.047/6.878, and very closely reflect the structure of the corresponding lectures.

### **1.1.2 Duality of Goals: Foundations and Frontiers**

There are two goals for this course. The first goal is to introduce you to the **foundations** of the field of computational biology. Namely, introduce the fundamental biological problems of the field, and learn the algorithmic and machine learning techniques needed for tackling them. This goes beyond just learning how to

5

6.047/6.878 Lecture 01: Introduction and Administrative Details

use the programs and online tools that are popular any given year. Instead, the aim is for you to understand the underlying principles of the most successful techniques that are currently in use, and provide you with the capacity to design and implement the next generation of tools. That is the reason why an introductory algorithms class is set as a pre-req; the best way to gain a deeper understanding for the algorithms presented is to implement them yourself.

The second goal of the course is to tackle the research **frontiers** of computational biology, and that’s what all the advanced topics and practical assignments are really about. We’d actually like to give you a glimpse of how research works, expose you to current research directions, guide you to find the problems most interesting to you, and help you become an active practitioner in the field. This is achieved through guest lectures, problem sets, labs, and most importantly a term-long independent research **project** , where you carry out your independent research.

The **modules** of the course follow that pattern, each consisting of lectures that cover the foundations and the frontiers of each topic. The foundation lectures introduce the classical problems in the field. These problems are very well understood and elegant solutions have already been found; some have even been taught for well over a decade. The frontiers portion of the module cover advanced topics, usually by tackling central questions that still remain open in the field. These chapters frequently include guest lectures by some of the pioneers in each area speaking both about the general state of the field as well as their own lab’s research.

The **assignments** for the course follow the same foundation/frontiers pattern. Half of the assignments are going to be about working out the methods with pencil on paper, and diving deep into the algorithmic and machine learning notions of the problems. The other half are actually going to be practical questions consisting of programming assignments, where real data sets are provided. You will analyze this data using the techniques you have learned and interpret your results, giving you a real hands on experience. The assignments build up to the final project, where you will propose and carry out an original research project, and present your findings in conference format. Overall, the assignments are designed to give you the opportunity to apply computational biology methods to real problems in biology.

### **1.1.3 Duality of disciplines: Computation and Biology**

In addition to aiming to cover both foundations and frontiers, the other important duality of this course is between computation and biology.

From the **biological** perspective of the course, we aim to teach topics that are fundamental to our understanding of biology, medicine, and human health. We therefore shy away from any computationallyinteresting problems that are biologically-inspired, but not relevant to biology. We’re not just going to see something in biology, get inspired, and then go off into computer science and do a lot of stuff that biology will never care about. Instead, our goal is to work on problems that can make a significant change in the field of biology. We’d like you to publish papers that actually matter to the biological community and have real biological impact. This goal has therefore guided the selection of topics for the course, and each chapter focuses on a fundamental biological problem.

From the **computational** perspective of the course, being after all a computer science class, we focus on exploring general techniques and principles that are certainly important in computational biology, but nonetheless can be applied in any other fields that require data analysis and interpretation. Hence, if what you want is to go into cosmology, meteorology, geology, or any such, this class offers computational techniques that will likely become useful when dealing with real-world data sets related to those fields.

### **1.1.4 Why Computational Biology?**

#### `lecture1_transcript.html#Motivations`

There are many reasons why Computational Biology has emerged as an important discipline in recent years, and perhaps some of these lead you to pick up this book or register for this class. Even though we have our own opinion on what these reasons are, we have asked the students year after year for their own view on what has enabled the field of Computational Biology to expand so rapidly in the last few years. Their responses fall into several broad themes, which we summarize here.

6

6.047/6.878 Lecture 01: Introduction and Administrative Details

1. Perhaps the most fundamental reason why computational approaches are so well-suited to the study of biological data is that at their core, biological systems are **fundamentally digital in nature** . To be blunt, humans are not the first to build a digital computer – our ancestors _are_ the first digital computer, as the earliest DNA-based life forms were already storing, copying, and processing digital information encoded in the letters A,C,G, and T. The major evolutionary advantage of a digital medium for storing genetic information is that it can persist across thousands of generations, while analog signals would be diluted from generation to generation from basic chemical diffusion.

2. Besides DNA, many other aspects of biology are digital, such as **biological switches** , which ensure that only two discrete possible states are achieved by feedback loops and metastable processes, even though these are implemented by levels of molecules. Extensive feedback loops and other diverse regulatory circuits implement discrete decisions through otherwise unstable components, again with design principles similar to engineering practice, making our quest to understand biological systems from an engineering perspective more approachable.

3. Sciences that heavily benefit from data processing, such as Computational Biology, follow a virtuous cycle involving the data available for processing. The more that can be done by processing and analyzing the available data, the more funding will be directed into developing technologies to obtain, process and analyze even more data. New technologies such as sequencing, and high-throughput experimental techniques like microarray, yeast two-hybrid, and ChIP-chip assays are creating **enormous and increasing amounts of data** that can be analyzed and processed using computational techniques. The $1000 and $100 genome projects are evidence of this cycle. Over ten years ago, when these projects started, it would have been ludicrous to even imagine processing such massive amounts of data. However, as more potential advantages were devised from the processing of this data, more funding was dedicated into developing technologies that would make these projects feasible.

4. The ability to process data has greatly improved in the recent years, owing to: 1) the massive computational power available today (due to Moore’s law, among other things), and 2) the advances in the algorithmic techniques at hand.

5. Optimization approaches can be used to solve, via computational techniques, that are otherwise intractable problems.

6. **Running time & memory** considerations are critical when dealing with huge datasets. An algorithm that works well on a small genome (for example, a bacteria) might be too time or space inefficient to be applied to 1000 mammalian genomes. Also, combinatorial questions dramatically increase algorithmic complexity.

7. Biological datasets can be **noisy** , and filtering signal from noise is a computational problem.

8. **Machine learning** approaches are useful to make inferences, classify biological features, & identify robust signals.

9. As our understanding of biological systems deepens, we have started to realize that such systems cannot be analyzed in isolation. These systems have proved to be intertwined in ways previously unheard of, and we have started to shift our analyses to techniques that consider them all as a whole.

10. It is possible to use computational approaches to find correlations in an unbiased way, and to come up with conclusions that transform biological knowledge and facilitate active learning. This approach is called **data-driven discovery** .

11. Computational studies can **predict** hypotheses, mechanisms, and theories to explain experimental observations. These falsifiable hypotheses can then be tested experimentally.

12. Computational approaches can be used not only to analyze existing data but also to **motivate data collection** and suggest useful experiments. Also, computational filtering can narrow the experimental search space to allow more focused and efficient experimental designs.

7

6.047/6.878 Lecture 01: Introduction and Administrative Details

13. Biology has **rules** : Evolution is driven by two simple rules: 1) random mutation, and 2) brutal selection. Biological systems are constrained to these rules, and when analyzing data, we are looking to find and interpret the emerging behavior that these rules generate.

14. **Datasets can be combined** using computational approaches, so that information collected across multiple experiments and using diverse experimental approaches can be brought to bear on questions of interest.

15. Effective **visualizations** of biological data can facilitate discovery.

16. Computational approaches can be used to **simulate & model** biological data.

17. Computational approaches can be more **ethical** . For example, some biological experiments may be unethical to perform on live subjects but could be simulated by a computer.

18. Large scale, systems engineering approaches are facilitated by computational technique to obtain global views into the organism that are too complex to analyze otherwise.

### **1.1.5 Finding Functional Elements: A Computational Biology Question**

```
lecture1_transcript.html#Codons
```

Several computational biology problems refer to finding biological signals in DNA data (e.g. coding regions, promoters, enhancers, regulators, ...).


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 1.1: In this computational biology problem, we are provided with a sequence of bases, and wish to locate genes and regulatory motifs.

We then discussed a specific question that computational biology can be used to address: how can one find functional elements in a genomic sequence? Figure 1.1 shows part of the sequence of the yeast genome. Given this sequence, we can ask:

- **Q:** What are the genes that encode proteins?

- **A:** During translation, the start codon marks the first amino acid in a protein, and the stop codon indicates the end of the protein. However, as indicated in the “Extracting signal from noise” slide, only a few of these ATG sequences in DNA actually mark the start of a gene which will be expressed as protein. The others are “noise”; for example, they may have been part of introns (non-coding sequences which are spliced out after transcription).

8

6.047/6.878 Lecture 01: Introduction and Administrative Details

- **Q:** How can we find features (genes, regulatory motifs, and other functional elements) in the genomic sequence?

- **A:** These questions could be addressed either experimentally or computationally. An experimental approach to the problem would be creating a knockout, and seeing if the fitness of the organism is affected. We could also address the question computationally by seeing whether the sequence is conserved across the genomes of multiple species. If the sequence is significantly conserved across evolutionary time, it’s likely to perform an important function.

There are caveats to both of these approaches. Removing the element may not reveal its function–even if there is no apparent difference from the original, this could be simply because the right conditions have not been tested. Also, simply because an element is not conserved doesn’t mean it isn’t functional. (Also, note that “functional element” is an ambiguous term. Certainly, there are many types of functional elements in the genome that are not protein-encoding. Intriguingly, 90-95% of the human genome is transcribed (used as a template to make RNA). It isn’t known what the function of most of these transcribed regions are, or indeed if they are functional).

## **1.2 Final Project - Introduction to Research In Computational Biology**

```
lecture1_transcript.html#FinalProject
```

### **1.2.1 Final project goals**

An important component of being a computational biologist is the ability to carry out independent research in the area. The skills for a successful researcher differ from one person to the next, but in the process of teaching this course, we have identified several aspects that are all needed, and laid out activities for a term-long project, that enable students to carry out their independent research.

The project mirrors real world scientific process: come up with an idea _→_ frame it _→_ propose it _→_ revise it _→_ carry it out _→_ present your results. Students are expected to think critically about their own project, and also evaluate peer research proposals, and lastly respond to feedback from their peers.

Students are expected to use real data and present their results in conference format. The ultimate goal is publishable research. Students are encouraged to talk with the course staff while formulating a final project idea, look head through the various chapters and modules, and get an idea of what areas will interest you most.

### **1.2.2 Final project milestones**

Instead of waiting until the end of the term to begin brainstorming or provide feedback, we begin project activities with the first problem set, to identify problems of interest and types of projects, find partners, speak with current students and postdocs in computational biology that can serve as mentors, and lay out a research plan in the style of an NIH proposal to identify potential pitfalls early and address them or work around them before they become a bottleneck.

By setting up several incremental progress milestones throughout the term, coupled with mentoring and feedback throughout the semester, we have achieved consistent progress in previous years, which can be useful to students taking on a new project at any stage of their career. Research projects from this course in the past have been used as the starting point for a published paper, have led to Masters and PhD theses, and earned awards both academically and in conferences.

The timeline for the final project is as follows:

1. **Set-up:** a brief overview of your experience and interest. Due 9/29

2. **Brainstorming:** a list of initial project ideas and partners. Due 10/6

3. **Proposal:** submit a project proposal in the form of an NIH proposal. Due 10/20

9

6.047/6.878 Lecture 01: Introduction and Administrative Details

4. **Proposal presentation:** present slides to class and mentors on the proposal. Due 10/23

5. **Review:** review and critique 3 peer proposals. Due 10/30

6. **Midterm Progress Report:** write outline of final report. Due 11/19

7. **Final Project Report:** write report in conference paper format. Due 12/6

8. **Final Class Presentation:** 10min conference talk. Due 12/10

There will be Friday mentoring sessions before each portion of the final project is due, and you are encouraged to find a mentor at the first few sessions who is actively interested in your project and could help you more frequently. The mentoring sessions can be helpful in identifying if unexpected results are the result of a bug or are instead a discovery.

Make sure you start working on the project even while waiting for peer reviews, so that you will have 4-5 weeks to complete the research itself.

### **1.2.3 Project deliverables**

The final project will include the following two deliverables:

1. A written presentation, due Mon at 8pm, last week of classes. The written presentation can contain the following elements:

   - Who did what (to reflect trend in publications)

   - The overall project experience

   - Your discoveries

   - What you learned from the experience (introspection)

2. An oral presentation, due Thursday after the written presentation. This allows students three days to prepare the oral presentation.

### **1.2.4 Project grading**

Selecting a project that will be successful can be difficult. To help students optimize for a successful project, we let them know in advance the grading scheme, designed to maximize the project impact by being original, challenging, and relevant to the field, but of course the grade is ultimately dependent on the overall achievement and the clarity of presentation.

Briefly, the grading equation for the final project is:

min( _O, C, R_ ) _× A_ + _P_

where

**Originality** - unoriginal computational experiments don’t get published

**Challenge** - the project needs to be sufficiently difficult

**Relevance** - it needs to be from biology, can’t just reuse something from another field

**Achievement** - if you don’t accomplish anything you won’t get a good grade

- **Presentation** - even if you’ve achieved a good project you have to be able to present it so everyone knows that, and make it look easy. The presentation should show how the project is _O_ , _C_ , and _R_ .

- Originality, Challenge, Relevance are each out of 5 points, Achievement and Presentation are each out of

- 10.

10

6.047/6.878 Lecture 01: Introduction and Administrative Details

## **1.3 Additional materials**

### **1.3.1 Online Materials for Fall 2015**

```
lecture1_transcript.html#Handouts
```

In addition to these _static_ notes, the course has several online resources:

- The course calendar on Google Calendar. You can add ”6.047 Lectures”, a public calendar.

- The NB note-taking system for annotating these notes `http://nb.mit.edu/`

### **1.3.2 Textbooks**

`lecture1_transcript.html#CourseInformation` The following three (optional) reference textbooks are recommended for the class.

1. Richard Durbin, Sean R. Eddy, Anders Krogh and Graeme Mitchison, Biological Sequence Analysis: Probabilistic Models of Proteins and Nucleic Acids.

2. Neil Jones and Pavel Pevzner, An Introduction to Bioinformatics Algorithms.

3. Richard Duda, Peter Hart, David Stork, Pattern Classification.

Each book has a different advantage. The first book is a classic one. It is heavy in math and covers much of what is in class. The book is focused on sequence alignment. As part of sequence alignment theory, the book approaches Hidden Markov Models (HMM), pairwise and multiple alignment methods, phylogenetic trees as well as a short background in probability theory.

The second book intends to balance between mathematical rigor and biological relevance. According to the author, it is a good book for undergrad students. The book includes a table that associates algorithms to biological problems.

The third book is about machine learning. It takes more of an engineering approach. It includes machine learning theory, neural network and, as the name suggests, pattern recognition.

## **1.4 Crash Course in Molecular Biology**

For the primarily computational students, we provide a brief introduction to the key notions of molecular biology that we will encounter throughout the term.

### **1.4.1 The Central Dogma of Molecular Biology**

`lecture1_transcript.html#CentralDogma` _DNA → RNA → Protein_

The central dogma of molecular biology describes how genetic information is stored and interpreted in the cell: The genetic code of an organism is stored in DNA, which is transcribed into RNA, which is finally translated into protein. Proteins carry out the majority of cellular functions such as motility, DNA regulation, and replication.

Though the central dogma holds true in most situations, there are a number of notable exceptions to the model. For instance, retroviruses are able to generate DNA from RNA via reverse-transcription. In addition, some viruses are so primitive that they do not even have DNA, instead only using RNA to protein.

11

6.047/6.878 Lecture 01: Introduction and Administrative Details

## **_Did You Know?_**

The central dogma is sometimes **incorrectly** interpreted too strongly as meaning that DNA only stores immutable information from one generation to the next that remains identical within a generation, RNA is only used as a temporary information transfer medium, and proteins are the only molecule that can carry out complex actions.

Again, there are many exceptions to this interpretation, for example:

- Somatic mutations can alter the DNA within a generation, and different cells can have different DNA content.

- Some cells undergo programmed DNA alterations during maturation, resulting in different DNA content, most famously the B and T immunity while blood cells

- Epigenetic modifications of the DNA can be inherited from one generation to the next

- RNA can play many diverse roles in gene regulation, metabolic sensing, and enzymatic reactions, functions that were previously thought to be reserved to proteins.

- Proteins themselves can undergo conformational changes that are epigenetically inherited notably prion states that were famously responsible for mad cow disease

### **1.4.2 DNA**

<mark>DNA</mark> _→_ RNA _→_ Protein

#### **DNA function**

The DNA molecule stores the genetic information of an organism. DNA contains regions called genes, which encode for proteins to be produced. Other regions of the DNA contain regulatory elements, which partially influence the level of expression of each gene. Within the genetic code of DNA lies both the data about the proteins that need to be encoded, and the control circuitry, in the form of regulatory motifs.

#### **DNA structure**

DNA is composed of four **nucleotides** : A( **adenine** ), C( **cytosine** ),T ( **thymine** ), and G ( **guanine** ). A and G are purines, which have two rings, while C and T are pyrimidines, with one ring. A and T are connected by two hydrogen bonds, while C and G are connected by three bonds. Therefore, the A-T pairing is weaker than the C-G pairing. (For this reason, the genetic composition of bacteria that live in hot springs is 80% G-C). `lecture1_transcript.html#Complementarity`

The two DNA strands in the double helix are **complementary** , meaning that if there is an A on one strand, it will be bonded to a T on the other, and if there is a C on one strand, it will be bonded to a G on the other. The DNA strands also have **directionality** , which refers to the positions of the pentose ring where the phosphate backbone connects. This directionality convention comes from the fact that DNA and RNA polymerase synthesize in the 5’ to 3’ direction. With this in mind, we can say that that the DNA strands are **anti-parallel** , as the 5’ end of one strand is adjacent to the 3’ end of the other. As a result, DNA can be read both in the 3’ to 5’ direction and the 5’ to 3’ direction, and genes and other functional elements can be found in each. By convention, DNA is written from 5’ to 3’. The 5’ and 3’ directions refer to the positions on the pentose ring where the phosphate backbone connects.

Base pairing between nucleotides of DNA constitutes its primary and secondary structure. In addition to DNA’s secondary structure, there are several extra levels of structure that allow DNA to be tightly compacted and influence gene expression (Figure 3). The tertiary structure describes the twist in the DNA ladder that forms a helical shape. In the quaternary structure, DNA is tightly wound around small proteins called histones. These DNA-histone complexes are further wound into tighter structures seen in chromatin.

Before DNA can be replicated or transcribed into RNA, the chromatin structure must be locally “unpacked”. Thus, gene expression may be regulated by modifications to the chromatin structure, which make it

12

6.047/6.878 Lecture 01: Introduction and Administrative Details


© Zephyris on wikipedia. Some rights reserved. License: CC BY-SA. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 1.2: The double-helix structure of DNA. Nucleotides are in the center, and the sugar-phosphate backbone lies on the outside.

easier or harder for the DNA to be unpacked. This regulation of gene expression via chromatin modification is an example of epigenetics.

#### **DNA replication**

The structure of DNA, with its weak hydrogen bonds between the bases in the center, allows the strands to easily be separated for the purpose of DNA replication (the capacity for DNA strands to be separated also allows for transcription, translation, recombination, and DNA repair, among others). This was noted by Watson and Crick as “It has not escaped our notice that the specific pairing that we have postulated immediately suggests a possible copying mechanism for the genetic material.” In the replication of DNA, the two complementary strands are separated, and each of the strands are used as templates for the construction of a new strand.

DNA polymerases attach to each of the strands at the origin of replication, reading each existing strand from the 3’ to 5’ direction and placing down complementary bases such that the new strand grows in the 5’ to 3’ direction. Because the new strand must grow from 5’ to 3’, one strand (the leading strand) can be copied continuously, while the other (the lagging strand) grows in pieces which are later glued together by DNA ligase. The end result is 2 double-stranded pieces of DNA, where each is composed of 1 old strand, and 1 new strand; for this reason, DNA replication is semiconservative.

Many organisms have their DNA broken into several chromosomes. Each chromosome contains two strands of DNA, which are complementary to each other but are read in opposite directions. Genes can occur on either strand of DNA. The DNA before a gene (in the 5’ region) is considered “upstream” whereas the DNA after a gene (in the 3’ region) is considered “downstream”.

### **1.4.3 Transcription**

```
lecture1_transcript.html#Transcription
```

DN <mark>A</mark> _<mark>→</mark>_ <mark>R</mark> NA _→_ Protein

13

6.047/6.878 Lecture 01: Introduction and Administrative Details


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Qiu, Jane. "Epigenetics: Unfinished Symphony." _Nature_ 441, no. 7090 (2006): 143-45.

Figure 1.3: DNA is packed over several layers of organization into a compact chromosome.

#### **mRNA generation**

Transcription is the process by which RNA is produced using a DNA template. The DNA is partially unwound to form a “bubble”, and RNA polymerase is recruited to the transcription start site (TSS) by regulatory protein complexes. RNA polymerase reads the DNA from the 3’ to 5’ direction and placing down complementary bases to form messenger RNA (mRNA). RNA uses the same nucleotides as DNA, except Uracil is used instead of Thymine.

#### **Post-transcriptional modifications**

mRNA in eukaryotes experience post-translational modifications, or processes that edit the mRNA strand further. Most notably, a process called splicing removes **introns** , intervening regions which don’t code for protein, so that only the coding regions, the **exons** , remain. Different regions of the primary transcript may be spliced out to lead to different protein products (alternative splicing). In this way, an enormous number of different molecules may be generated based on different splicing permutations.

In addition to splicing, both ends of the mRNA molecule are processed. The 5’ end is capped with a modified guanine nucleotide. At the 3’ end, roughly 250 adenine residues are added to form a poly(A) tail.

### **1.4.4 RNA**

```
lecture1_transcript.html#RNA
```

DNA _→_ <mark>RNA</mark> _→_ Protein

RNA is produced when DNA is transcribed. It is structurally similar to DNA, with the following major differences:

1. The nucleotide uracil (U) is used instead of DNA’s thymine (T).

2. RNA contains ribose instead of deoxyribose (deoxyribose lacks the oxygen molecule on the 2’ position found in ribose).

3. RNA is single-stranded, whereas DNA is double-stranded.

RNA molecules are the intermediary step to code a protein. RNA molecules also have catalytic and regulatory functions. One example of catalytic function is in protein synthesis, where RNA is part of the ribosome.

There are many different types of RNA, including:

14

6.047/6.878 Lecture 01: Introduction and Administrative Details


<!-- Start of picture text -->
(a) Transcription initiation<br>(b) Transcription elongation<br>(c) Transcription termination<br>Courtesy of Forluvoft on wikipedia. Images in the public domain.<br><!-- End of picture text -->

Figure 1.4: RNA is produced from a DNA template during transcription. A “bubble” is opened in the DNA, allowing the RNA polymerase to enter and place down bases complementary to the DNA.

1. **mRNA** (messenger RNA) contains the information to make a protein and is translated into protein sequence.

2. **tRNA** (transfer RNA) specifies codon-to-amino-acid translation. It contains a 3 base pair anti-codon complementary to a codon on the mRNA, and carries the amino acid corresponding to its anticodon attached to its 3’ end.

3. **rRNA** (ribosomal RBA) forms the core of the ribosome, the organelle responsible for the translation of mRNA to protein.

4. **snRNA** (small nuclear RNA) is involved in splicing (removing introns from) pre- mRNA, as well as other functions.

Other functional kinds of RNA exist and are still being discovered. Though proteins are generally thought to carry out essential cellular functions, RNA molecules can have complex three-dimensional structures and perform diverse functions in the cell.

According to the “RNA world” hypothesis, early life was based entirely on RNA. RNA served as both the information repository (like DNA today) and the functional workhorse (like protein today) in early organisms. Protein is thought to have arisen afterwards via ribosomes, and DNA is thought to have arisen last, via reverse transcription.

### **1.4.5 Translation**

```
lecture1_transcript.html#Translation
```

DNA _→_ RNA _<mark>→</mark>_ <mark>P</mark> rotein

#### **Translation**

Unlike transcription, in which the nucleotides remained the means of encoding information in both DNA and RNA, when RNA is translated into protein, the primary structure of the protein is determined by the

15

6.047/6.878 Lecture 01: Introduction and Administrative Details

sequence of amino acids of which it is composed. Since there are 20 amino acids and only 4 nucleotides, 3-nucleotides sequences in mRNA, known as codons, encode for each of the 20 amino acids.

Each of the 64 possible 3-sequences of nucleotides (codon) uniquely specifies either a particular amino acid, or is a stop codon that terminates protein translation (the start codon also encodes methionine). Since there are 64 possible codon sequences, the code is degenerate, and some amino acids are specified by multiple encodings. Most of the degeneracy occurs in the 3rd codon position.

#### **Post-translational modifications**

Like mRNA, protein also undergo further modifications that affect its structure and function. One type of post-translational modification (PTM) involves introducing new functional groups to the amino acids. Most notably, phosphorylation is the process by which a phosphate group is added onto an amino acid which can activate or deactivate the protein entirely. Another type of PTM is cleavage of peptide bonds. For example, the hormone insulin is cleaved twice following the formation of disulfide bonds within the original protein.


Figure 1.5: This codon table shows which of the 20 amino acid each of the 3-nucleotide codons in mRNA are translated into. In red are the stop codons, which terminate translation.

### **1.4.6 Protein**

#### DNA _→_ RNA _→_ <mark>Protein</mark>

Protein is the molecule responsible for carrying out most of the tasks of the cell, and can have many functions, such as enzymatic, contractile, transport, immune system, signal and receptor to name a few. Like RNA and DNA, proteins are polymers made from repetitive subunits. Instead of nucleotides, however, proteins are composed of amino acids.

Each amino acid has special properties of size, charge, shape, and acidity. As such, additional structure emerges beyond simply the sequence of amino acids (the primary structure), as a result of interactions between the amino acids. As such, the three-dimensional shape, and thus the function, of a protein is determined by its sequence. However, determining the shape of a protein from its sequence is an unsolved problem in computational biology.

16

6.047/6.878 Lecture 01: Introduction and Administrative Details

### **1.4.7 Regulation: from Molecules to Life**

```
lecture1_transcript.html#Regulation
```

Not all genes are expressed at the same time in a cell. For example, cells would waste energy if they produced lactose transporter in the absence of lactose. It is important for a cell to know which genes it should expresses and when. A regulatory network is involved to control expression level of genes in a specific circumstance.

Transcription is one of the steps at which protein levels can be regulated. The promoter region, a segment of DNA found upstream (past the 5’ end) of genes, functions in transcriptional regulation. The promoter region contains motifs that are recognized by proteins called transcription factors. When bound, transcription factors can recruit RNA polymerase, leading to gene transcription. However, transcription factors can also participate in complex regulatory interactions. There can be multiple binding sites in a promotor, which can act as a logic gate for gene activation. Regulation in eukaryokes can be extremely complex, with gene expression affected not only by the nearby promoter region, but also by distant enhancers and repressors.

We can use probabilistic models to identify genes that are regulated by a given transcription factor. For example, given the set of motifs known to bind a given transcription factor, we can compute the probability that a candidate motif also binds the transcription factor (see the notes for precept #1). Comparative sequence analysis can also be used to identify regulatory motifs, since regulatory motifs show characteristic patterns of evolutionary conservation.

The lac operon in E. coli and other bacteria is an example of a simple regulatory circuit. In bacteria, genes with related functions are often located next to each other, controlled by the same regulatory region, and transcribed together; this group of genes is called an operon. The lac operon functions in the metabolism of the sugar lactose, which can be used as an energy source. However, the bacteria prefer to use glucose as an energy source, so if there is glucose present in the environment the bacteria do not want to make the proteins that are encoded by the lac operon. Therefore, transcription of the lac operon is regulated by an elegant circuit in which transcription occurs only if there is lactose but not glucose present in the environment.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 1.6: Operon Lac illustrates a simple biological regulatory system. In the presence of glucose, genes to lactose metabolism are turn out because glucose inactives an activator protein. In the absence of lactose, a repressor protein also turns out the operon. Lactose metabolism genes are expressed only in the presence of lactose and absence of glucose.

17

6.047/6.878 Lecture 01: Introduction and Administrative Details


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 1.7: Metabolic pathways and regulation can be studied by Computational biology. Models are made from genome scale information and used to predict metabolic function and to metabolic engineering. An example of biological engineering is modifying bacteria genome to overproduce artemesenin, an antibiotic used to treat malaria.

### **1.4.8 Metabolism**

#### `lecture1_transcript.html#`

Live organisms are made from self-organizing building blocks. Energy source is necessary for organize blocks. The basic mechanism involved in building blocks is degrading small molecules to get energy to build big molecules. The process of degrading molecules to release energy is called catabolism and the process of using energy to assemble more complex molecules is called anabolism. Anabolism and catabolism are both metabolic processes. Metabolism regulates the flow of mass and energy in order to keep an organism in a state of low entropy.

Enzymes are a critical component of metabolic reactions. The vast majority of (but not all!) enzymes are proteins. Many biologically critical reactions have high activation energies, so that the uncatalyzed reaction would happen extremely slowly or not at all. Enzymes speed up these reactions, so that they can happen at a rate that is sustainable for the cell. In living cells, reactions are organized into metabolic pathways. A reaction may have many steps, with the products of one step serving as the substrate for the next. Also, metabolic reactions often require an investment of energy (notably as a molecule called ATP), and energy released by one reaction may be captured by a later reaction in the pathway. Metabolic pathways are also important for the regulation of metabolic reactionsif any step is inhibited, subsequent steps may lack the substrate or the energy that they need to proceed. Often, regulatory checkpoints appear early in metabolic pathways, since if the reaction needs to be stopped, it is obviously better to stop it before much energy has been invested.

### **1.4.9 Systems Biology**

#### `lecture1_transcript.html#SystemsBiology`

Systems biology strives to explore and explain the behavior that emerges from the complex interactions among the components of a biological system. One interesting recent paper in systems biology is “Metabolic gene regulation in a dynamically changing environment” (Bennett et al., 2008). This work makes the assumption that yeast is a linear, time invariant system, and runs a signal (glucose) through the system to observe the response. A periodic response to low-frequency fluctuations in glucose level is observed, but there is little response to high-frequency fluctuations in glucose level. Thus, this study finds that yeast acts as a low-pass filter for fluctuations in glucose level.

18

6.047/6.878 Lecture 01: Introduction and Administrative Details

### **1.4.10 Synthetic Biology**

```
lecture1_transcript.html#SyntheticBiology
```

Not only can we use computational approaches to model and analyze biological data collected from cells, but we can also design cells that implement specific logic circuits to carry out novel functions. The task of designing novel biological systems is known as synthetic biology.

A particularly notable success of synthetic biology is the improvement of artemesenin production. Artemesenin is a drug used to treat malaria. However, artemisinin was quite expensive to produce. Recently, a strain of yeast has been engineered to synthesize a precursor to artemisinic acid at half of the previous cost.

### **1.4.11 Model organisms and human biology**

Diverse model organisms exist for all aspects of human biology. Importance of using model organisms at appropriate level of complexity.

Note: In this particular book, we’ll focus on human biology, and we’ll use examples from baker’s yeast _Saccharomyces cerevisiae_ , the fruitfly _Drosophila melanogaster_ , the nematode worm _Coenorhabditis elegans_ , and the house mouse _Mus musculus_ . We’ll deal with bacterial evolution only in the context of metagenomics of the human microbiome.

19

6.047/6.878 Lecture 01: Introduction and Administrative Details

## **1.5 Introduction to algorithms and probabilistic inference**

1. We will quickly review some basic probability by considering an alternate way to represent motifs: a _position weight matrix_ (PWM). We would like to model the fact that proteins may bind to motifs that are not fully specified. That is, some positions may require a certain nucleotide (e.g. `A` ), while others positions are free to be a subset of the 4 nucleotides (e.g. `A` or `C` ). A PWM represents the set of all DNA sequences that belong to the motif by using a matrix that stores the probability of finding each of the 4 nucleotides in each position in the motif. For example, consider the following PWM for a motif with length 4:

||1|2|3|4|
|---|---|---|---|---|
|A|0.6|0.25|0.10|1.0|
|G|0.4|0.25|0.10|0.0|
|T|0.0|0.25|0.40|0.0|
|C|0.0|0.25|0.40|0.0|


We say that this motif can generate sequences of length 4. PWMs typically assume that the distribution of one position is not influenced by the base of another position. Notice that each position is associated with a probability distribution over the nucleotides (they sum to 1 and are nonnegative).

2. We can also model the _background distribution_ of nucleotides (the distribution found across the genome):

|A<br>0.1|
|---|
|G<br>0.4|
|T<br>0.1|
|C<br>0.4|


Notice how the probabilities for A and T are the same and the probabilities of G and C are the same. This is a consequence of the complementarity DNA which ensures that the overall composition of A and T, G and C is the same overall in the genome.

3. Consider the sequence _S_ = GCAA.

   - The probability of the motif generating this sequence is _P_ ( _S|M_ ) = 0 _._ 4 _×_ 0 _._ 25 _×_ 0 _._ 1 _×_ 1 _._ 0 = 0 _._ 01. The probability of the background generating this sequence _P_ ( _S|B_ ) = 0 _._ 4 _×_ 0 _._ 4 _×_ 0 _._ 1 _×_ 0 _._ 1 = 0 _._ 0016.

4. Alone this isn’t particularly interesting. However, given fraction of sequences that are generated by the motif, e.g. _P_ ( _M_ ) = 0 _._ 1, and assuming all other sequences are generated by the background ( _P_ ( _B_ ) = 0 _._ 9) we can compute the probability that the motif generated the sequence using Bayes’ Rule:


20

6.047/6.878 Lecture 01: Introduction and Administrative Details

- **1.5.1 Probability distributions**

- **1.5.2 Graphical probabilistic models**

- **1.5.3 Bayes rules: priors, likelihood, posterior**

- **1.5.4 Markov Chains and Sequential Models**

- **1.5.5 Probabilistic inference and learning**

- **1.5.6 Max Likelihood and Max A Posteriori Estimates**

## **Bibliography**

- [1] lec1test. lec1test, lec1test.

21

6.047/6.878 Lecture 01: Introduction and Administrative Details

22

---

[Up: contents](index.md) · [Part I →](02-part-i.md)

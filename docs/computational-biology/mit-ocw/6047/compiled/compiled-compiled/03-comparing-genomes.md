---
title: Comparing Genomes
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/compiled/compiled-compiled.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Comparing Genomes

**Source:** `compiled/compiled-compiled.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

23

## CHAPTER **TWO**

## SEQUENCE ALIGNMENT AND DYNAMIC PROGRAMMING

Guilherme Issao Fujiwara, Pete Kruskal (2007) Arkajit Dey, Carlos Pards (2008) Victor Costan, Marten van Dijk (2009) Andreea Bodnari, Wes Brown (2010) Sarah Spencer (2011) Nathaniel Parrish (2012) Cl´ement Pit-Claudel (2014) Jesse Tordoff, Thrasyvoulos Karydis (2015)

### **Figures**

|2.1|Sequence alignment of Gal10-Gal1 between four yeast strains. Asterisks mark conserved<br>nucleotides. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|25|
|---|---|---|
|2.2|Evolutionary changes of a genetic sequence<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|25|
|2.3|Aligning human to mouse sequences is analogous to tracing . . . . . . . . . . . . . . . . .|26|
|2.4|Example of longest common substring . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|27|
|2.5|Example of longest common subsequence formulation. . . . . . . . . . . . . . . . . . . . .|27|
|2.6|Cost matrix for matches and mismatches. . . . . . . . . . . . . . . . . . . . . . . . . . . .|28|
|2.7|Examples of Finonacci numbers in nature are ubiquitous.<br>. . . . . . . . . . . . . . . . . .|30|
|2.8|The recursion tree for the fib procedure showing repeated subproblems. The size of the<br>tree is _O_(_φ_(_n_)), where _φ_ is the golden ratio. . . . . . . . . . . . . . . . . . . . . . . . . . .|31|
|2.9|(Example) Initial setup for Needleman-Wunsch . . . . . . . . . . . . . . . . . . . . . . . .|35|
|2.10|(Example) Half-way through the second step of Needleman-Wunsch<br>. . . . . . . . . . . .|35|
|2.11|(Example) Tracing the optimal alignment . . . . . . . . . . . . . . . . . . . . . . . . . . .|36|
|2.12|Bounded dynamic programming example<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|36|
|2.13|Recovering the sequence alignment with _O_(_m_+_n_) space<br>. . . . . . . . . . . . . . . . . .|37|
|2.14|Ortholog and paralog sequences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|40|


## **2.1 Introduction**

Sequence alignment is a powerful tool capable of revealing the patterns and functions of genes. If two genetic regions are similar or identical, sequence alignment can demonstrate the conserved elements or differences between them. Evolution has preserved two broad classes of functional elements in the genome. Such preserved elements between species are often homologs<sup>1</sup> – either orthologous or paralogous sequences (refer to Appendix 2.11.1). Both classes of conserved elements can help demonstrate the function or evolutionary history of a gene sequence. Primarily solved using computational methods (most frequently dynamic

> 1Homologous sequences are genomic sequences descended from a common ancestor.

25

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming

programming), sequence alignment is a fast and powerful way to find similarities among genes or genomes. These notes discuss the sequence alignment problem, the technique of dynamic programming, and a specific solution to the problem using this technique.

## **2.2 Aligning Sequences**

Sequence alignment represents the method of comparing two or more genetic strands, such as DNA or RNA. These comparisons help with the discovery of genetic commonalities and with the (implicit) tracing of strand evolution. There are two main types of alignment:

- Global alignment: an attempt to align every element in a genetic strand, most useful when the genetic strands under consideration are of roughly equal size. Global alignment can also end in gaps.

- Local alignment: an attempt to align regions of sequences that contain similar sequence motifs within a larger context.

### **2.2.1 Example Alignment**

Within orthologous gene sequences, there are islands of conservation, or relatively large stretches of nucleotides that are preserved between generations. These conserved regions typically imply functional elements and vice versa. As an example, we considered the alignment of the Gal10-Gal1 intergenic region for four different yeast species, the first cross-species whole genome alignment (Figure 2.1). As we look at this alignment, we note that some areas are more similar than others, suggesting that these areas have been conserved through evolution. In particular, we note some small conserved motifs such as CGG and CGC, which in fact are functional elements in the binding of Gal4[8].<sup>2</sup> This example highlights how evolutionary data can help locate functional areas of the genome: per-nucleotide levels of conservation denote the importance of each nucleotide, and exons are among the most conserved elements in the genome.

We have to be cautious with our interpretations, however, because conservation does sometimes occur by random chance. In order to extract accurate biological information from sequence alignments we have to separate true signatures from noise. The most common approach to this problem involves modeling the evolutionary process. By using known codon substitution frequencies and RNA secondary structure constraints, for example, we can calculate the probability that evolution acted to preserve a biological function. See Chapter **??** for an in-depth discussion of evolutionary modeling and functional conservation in the context of genome annotation.

### **2.2.2 Solving Sequence Alignment**

Genomes change over time, and the scarcity of ancient genomes makes it virtually impossible to compare the genomes of living species with those of their ancestors. Thus, we are limited to comparing just the genomes of living descendants. The goal of sequence alignment is to infer the ‘edit operations’ that change a genome by looking only at these endpoints.

We must make some assumptions when performing sequence alignment, if only because we must transform a biological problem into a computationally feasible one and we require a model with relative simplicity and tractability. In practice, sequence evolution is mostly due to nucleotide mutations, deletions, and insertions (Figure 2.2). Thus, our sequence alignment model will only consider these three operations and will ignore other realistic events that occur with lower probability (e.g. duplications).<sup>3</sup>

1. A nucleotide **mutation** occurs when some nucleotide in a sequence changes to some other nucleotide during the course of evolution.

2. A nucleotide **deletion** occurs when some nucleotide is deleted from a sequence during the course of evolution.

> 2Gal4 in fact displays a particular structure, comprising two arms that each bind to the same sequence, in reversed order.

> 3Interestingly, modeling decisions taken to improve tractability do not necessarily result in diminished relevance; for example, accounting for directionality in the study of chromosome inversions yields polynomial-time solutions to an otherwise NP problem.[6]

26

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming


<!-- Start of picture text -->
© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

Figure 2.1: Sequence alignment of Gal10-Gal1 between four yeast strains. Asterisks mark conserved nucleotides.

3. A nucleotide **insertion** occurs when some nucleotide is added to a sequence during the course of evolution.


<!-- Start of picture text -->
ancestral!<br>A! C! G! T! C! A! T! C! A!<br>sequence<br>mutation!<br>A! C! G! T! G� A! T! C! A!<br>deletion!<br>A! G! T! G! T! C! A!<br>A! G! T! G! T! C! A!<br>insertion!<br>T! A! G! T! G! T! C! A!<br>derived! T! A! G! T! G! T! C! A!<br>sequence<br><!-- End of picture text -->

Figure 2.2: Evolutionary changes of a genetic sequence

Note that these three events are all reversible. For example, if a nucleotide N mutates into some nucleotide M, it is also possible that nucleotide M can mutate into nucleotide N. Similarly, if nucleotide N is deleted, the event may be reversed if nucleotide N is (re)inserted. Clearly, an insertion event is reversed by a corresponding deletion event.

This reversibility is part of a larger design assumption: time-reversibility. Specifically, any event in our model is reversible in time. For example, a nucleotide deletion going forward in time may be viewed as a nucleotide insertion going backward in time. This is useful because we will be aligning sequences which both exist in the present. In order to compare evolutionary relatedness, we will think of ourselves following one sequence backwards in time to a common ancestor and then continuing forward in time to the other sequence. In doing so, we can avoid the problem of not having an ancestral nucleotide sequence.

Note that time-reversibility is useful in solving some biological problems but does not actually apply to

27

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming


Figure 2.3: Aligning human to mouse sequences is analogous to tracing backward from the human to a common ancestor, then forward to the mouse

biological systems. For example, CpG<sup>4</sup> may incorrectly pair with a TpG or CpA during DNA replication, but the reverse operation cannot occur; hence this transformation is not time-reversible. To be very clear, time-reversibility is simply a design decision in our model; it is not inherent to the biology<sup>5</sup> .

We also need some way to evaluate our alignments. There are many possible sequences of events that could change one genome into another. Perhaps the most obvious ones minimize the number of events (i.e., mutations, insertions, and deletions) between two genomes, but sequences of events in which many insertions are followed by corresponding deletions are also possible. We wish to establish an optimality criterion that allows us to pick the ‘best’ series of events describing changes between genomes.

We choose to invoke Occam’s razor and select a maximum parsimony method as our optimality criterion. That is, in general, we wish to minimize the number of events used to explain the differences between two nucleotide sequences. In practice, we find that point mutations are more likely to occur than insertions and deletions, and certain mutations are more likely than others[11]. Our parsimony method must take these and other inequalities into account when maximizing parsimony. This leads to the idea of a substitution matrix and a gap penalty, which are developed in the following sections. Note that we did not need to choose a maximum parsimony method for our optimality criterion. We could choose a probabilistic method, for example using Hidden Markov Models (HMMs), that would assign a probability measure over the space of possible event paths and use other methods for evaluating alignments (e.g., Bayesian methods). Note the duality between these two approaches: our maximum parsimony method reflects a belief that mutation events have low probability, thus in searching for solutions that minimize the number of events we are implicitly maximizing their likelihood.

## **2.3 Problem Formulations**

In this section, we introduce a simple problem, analyze it, and iteratively increase its complexity until it closely resembles the sequence alignment problem. This section should be viewed as a warm-up for Section 2.5 on the Needleman-Wunsch algorithm.

### **2.3.1 Formulation 1: Longest Common Substring**

As a first attempt, suppose we treat the nucleotide sequences as strings over the alphabet A, C, G, and T. Given two such strings, S1 and S2, we might try to align them by finding the longest common substring between them. In particular, these substrings cannot have gaps in them.

As an example, if S1 = ACGTCATCA and S2 = TAGTGTCA (refer to Figure 2.4), the longest common substring between them is GTCA. So in this formulation, we could align S1 and S2 along their longest common substring, GTCA, to get the most matches. A simple algorithm would be to try aligning S1 with different offsets of S2 and keeping track of the longest substring match found thus far. Note that this algorithm is quadratic in the length of the shortest sequence, which is slower than we would prefer for such a simple problem.

> 4p denotes the phosphate backbone in a DNA strand

> 5This is an example where understanding the biology helps the design greatly, and illustrates the general principle that success in computational biology requires strong knowledge of the foundations of both CS and biology. Warning: computer scientists who ignore biology will work too hard.

28

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming


Figure 2.4: Example of longest common substring formulation

### **2.3.2 Formulation 2: Longest Common Subsequence (LCS)**

Another formulation is to allow gaps in our subsequences and not just limit ourselves to substrings with no gaps. Given a sequence X = ( _x_ 1 ,.., _xm_ ), we formally define _Z_ = ( _z_ 1 _, . . . , zk_ ) to be a subsequence of X if there exists a strictly increasing sequence _i_ 1 _< i_ 2 _< . . . < ik_ of indices of X such that for all _j_ , 1 _≤ j ≤ k_ , we have _xij_ = _zj_ (CLRS 350-1).

In the longest common subsequence (LCS) problem, we’re given two sequences X and Y and we want to find the maximum-length common subsequence Z. Consider the example of sequences S1 = ACGTCATCA and S2 = TAGTGTCA (refer to Figure 2.5). The longest common subsequence is AGTTCA, a longer match than just the longest common substring.


Figure 2.5: Example of longest common subsequence formulation

29

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming

### **2.3.3 Formulation 3: Sequence Alignment as Edit Distance**

#### **Formulation**

The previous LCS formulation is close to the full sequence alignment problem, but so far we have not specified any cost functions that can differentiate between the three types of edit operations (insertion, deletions, and substitutions). Implicitly, our cost function has been uniform, implying that all operations are equally likely. Since substitutions are much more likely, we want to bias our LCS solution with a cost function that prefers substitutions over insertions and deletions.

We recast sequence alignment as a special case of the classic Edit-Distance<sup>6</sup> problem in computer science (CLRS 366). We add varying penalties for different edit operations to reflect biological occurrences. One biological reasoning for this scoring decision is the probabilities of bases being transcribed incorrectly during polymerization. Of the four nucleotide bases, A and G are purines (larger, two fused rings), while C and T are pyrimidines (smaller, one ring). Thus DNA polymerase<sup>7</sup> is much more likely to confuse two purines or two pyrimidines since they are similar in structure. The scoring matrix in Figure 2.6 models the considerations above. Note that the table is symmetric - this supports our time-reversible design.


Figure 2.6: Cost matrix for matches and mismatches

Calculating the scores implies alternating between the probabilistic interpretation of how often biological events occur and the algorithmic interpretation of assigning a score for every operation. The problem is to the find the least expensive (as per the cost matrix) operation sequence which can transform the initial nucleotide sequence into the final nucleotide sequence.

#### **Complexity of Edit Distance**

All algorithms to solve the edit distance between two strings operate in near-polynomial time. In 2015, Backurs and Indyk [ **?** ] published a proof that edit distance cannot be solved faster than _O_ ( _n_<sup>2</sup> ) in the general case. This result depends on the Strong Exponential Time Hypothesis (SETH), which states that NP-complete problems cannot be solved in subexponential time in the worse case.

### **2.3.4 Formulation 4: Varying Gap Cost Models**

Biologically, the cost of creating a gap is more expensive than the cost of extending an already created gap. Thus, we could create a model that accounts for this cost variation. There are many such models we could use, including the following:

- **Linear gap penalty:** Fixed cost for all gaps (same as formulation 3).

- **Affine gap penalty:** Impose a large initial cost for opening a gap, then a small incremental cost for each gap extension.

- **General gap penalty:** Allow any cost function. Note this may change the asymptotic runtime of our algorithm.

> 6Edit-distance or Levenshtein distance is a metric for measuring the amount of difference between two sequences (e.g., the Levenshtein distance applied to two strings represents the minimum number of edits necessary for transforming one string into another).

> 7DNA polymerase is an enzyme that helps copy a DNA strand during replication.

30

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming

- **Frame-aware gap penalty:** Tailor the cost function to take into account disruptions to the coding frame (indels that cause frame-shifts in functional elements generally cause important phenotypic modifications).

### **2.3.5 Enumeration**

Recall that in order to solve the Longest Common Substring formulation, we could simply enumerate all possible alignments, evaluate each one, and select the best. This was because there were only _O_ ( _n_ ) alignments of the two sequences. Once we allow gaps in our alignment, however, this is no longer the case. It is a known issue that the number of all possible gapped alignments cannot be enumerated (at least when the sequences are lengthy). For example, with two sequences of length 1000, the number of possible alignments exceeds the number of atoms in the universe.

Given a metric to score a given alignment, the simple brute-force algorithm enumerates all possible alignments, computes the score of each one, and picks the alignment with the maximum score. This leads to the question, ‘How many possible alignments are there?’ If you consider only NBAs<sup>8</sup> _n > m_ , the number of alignments is


This number grows extremely fast, and for values of _n_ as small 30 is too big ( _>_ 10<sup>17</sup> ) for this enumeration strategy to be feasible. Thus, using a better algorithm than brute-force is a necessity.

## **2.4 Dynamic Programming**

Before proceeding to a solution of the sequence alignment problem, we first discuss dynamic programming, a general and powerful method for solving problems with certain types of structure.

### **2.4.1 Theory of Dynamic Programming**

Dynamic programming may be used to solve problems with:

1. **Optimal Substructure** : The optimal solution to an instance of the problem contains optimal solutions to subproblems.

2. **Overlapping Subproblems** : There are a limited number of subproblems, many/most of which are repeated many times.

Dynamic programming is usually, but not always, used to solve optimization problems, similar to greedy algorithms. Unlike greedy algorithms, which require a greedy choice property to be valid, dynamic programming works on a range of problems in which locally optimal choices do not produce globally optimal results. Appendix 2.11.3 discusses the distinction between greedy algorithms and dynamic programming in more detail; generally speaking, greedy algorithms solve a smaller class of problems than dynamic programming. In practice, solving a problem using dynamic programming involves two main parts: Setting up dynamic programming and then performing computation. Setting up dynamic programming usually requires the following 5 steps:

1. Find a ’matrix’ parameterization of the problem. Determine the number of dimensions (variables).

2. Ensure the subproblem space is polynomial (not exponential). Note that if a small portion of subproblems are used, then memoization may be better; similarly, if subproblem reuse is not extensive, dynamic programming may not be the best solution for the problem.

3. Determine an effective transversal order. Subproblems must be ready (solved) when they are needed, so computation order matters.

> 8Non-Boring Alignments, or alignments where gaps are always paired with nucleotides.

31

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming

4. Determine a recursive formula: A larger problem is typically solved as a function of its subparts.

5. Remember choices: Typically, the recursive formula involves a minimization or maximization step. Moreover, a representation for storing transversal pointers is often needed, and the representation should be polynomial.

Once dynamic programming is setup, computation is typically straight-forward:

1. Systematically fill in the table of results (and usually traceback pointers) and find an optimal score.

2. Traceback from the optimal score through the pointers to determine an optimal solution.

### **2.4.2 Fibonacci Numbers**


<!-- Start of picture text -->
Rabbits per generation Leaves per height<br>Romanesque spirals Nautilus size Coneflower spirals Leaf ordering<br><!-- End of picture text -->

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 2.7: Examples of Finonacci numbers in nature are ubiquitous.

The Fibonacci numbers provide an instructive example of the benefits of dynamic programming. The Fibonacci sequence is recursively defined as _F_ 0 = _F_ 1 = 1 _, Fn_ = _Fn−_ 1 + _Fn−_ 2 for _n ≤_ 2. We develop an algorithm to compute the _n_<sup>th</sup> Fibonacci number, and then refine it first using memoization and later using dynamic programming to illustrate key concepts.

#### **The Na¨ıve Solution**

The simple top-down approach is to just apply the recursive definition. Listing 1 shows a simple Python implementation.

1 `# Assume n is a non -negative integer.`

- 2 `def fib(n):`

3 `if n == 0 or n == 1:`

- 4 `return 1`

5 `else :`

6 `return fib(n - 1) + fib(n - 2)`

Listing 2.1: Python implementation for computing Fibonacci numbers recursively.

But this top-down algorithm runs in exponential time. That is, if _T_ ( _n_ ) is how long it takes to compute the _n_<sup>th</sup> Fibonacci number, we have that _T_ ( _n_ ) = _T_ ( _n −_ 1) + _T_ ( _n −_ 2) + _O_ (1), so _T_ ( _n_ ) = _O_ ( _φ_<sup>_n_</sup> )<sup>9</sup> . The problem is that we are repeating work by solving the same subproblem many times.

> 9 _φ_ is the **golden ratio** , i.e. <u>1+2</u> _~~<u>√</u>~~_ <u>5</u>

32

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming


Figure 2.8: The recursion tree for the fib procedure showing repeated subproblems. The size of the tree is _O_ ( _φ_ ( _n_ )), where _φ_ is the golden ratio.

#### **The Memoization Solution**

A better solution that still utilizes the top-down approach is to memoize the answers to the subproblems. Listing 2 gives a Python implementation that uses memoization.

1 `# Assume n is a non -negative integer.` 2 `fibs = {0: 1, 1: 1} # stores subproblem answers`

3 `def fib(n):`

- 4 `if n not in fibs:`

5 `x = fib(n - 2)` 6 `y = fib(n - 1)` 7 `fibs[n] = x + y` 8 `return fibs[n]`

Listing 2.2: Python implementation for computing Fibonacci numbers using memoization.

Note that this implementation now runs in _T_ ( _n_ ) = _O_ ( _n_ ) time because each subproblem is computed at most once.

#### **The Dynamic Programming Solution**

For calculating the _n_<sup>th</sup> Fibonacci number, instead of beginning with _F_ ( _n_ ) and using recursion, we can start computation from the bottom since we know we are going to need all of the subproblems anyway. In this way, we will omit much of the repeated work that would be done by the na¨ıve top-down approach, and we will be able to compute the _n_<sup>th</sup> Fibonacci number in _O_ ( _n_ ) time.

As a formal exercise, we can apply the steps outlined in section 2.4.1:

1. **Find a ’matrix’ parameterization:** In this case, the matrix is one-dimensional; there is only one parameter to any subproblem _F_ ( _x_ ).

2. **Ensure the subproblem space is polynomial:** Since there are only _n −_ 1 subproblems, the space is polynomial.

3. **Determine an effective transversal order:** As mentioned above, we will apply a bottom-up transversal order (that is, compute the subproblems in ascending order).

4. **Determine a recursive formula:** This is simply the well-known recurrance _F_ ( _n_ ) = _F_ ( _n−_ 1)+ _F_ ( _n−_ 2).

5. **Remember choices:** In this case there is nothing to remember, as no choices were made in the recursive formula.

Listing 3 shows a Python implementation of this approach.

33

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming

- 1 `# Assume n is a non -negative integer`

- 2 `def fib(n):`

- 3 `x = y = 1`

- 4 `for i in range (1, n):`

- 5 `x, y = y, x + y`

- 6 `return x`

Listing 2.3: Python implementation for computing Fibonacci numbers iteratively using dynamic programming.

This method is optimized to only use constant space instead of an entire table since we only need the answer to each subproblem once. But in general dynamic programming solutions, we want to store the solutions to subproblems in a table since we may need to use them multiple times without recomputing their answers. Such solutions would look somewhat like the memoization solution in Listing 2, but they will generally be bottom-up instead of top-down. In this particular example, the distinction between the memoization solution and the dynamic programming solution is minimal as both approaches compute all subproblem solutions and use them the same number of times. In general, memoization is useful when not all subproblems will be computed, while dynamic programming saves the overhead of recursive function calls, and is thus preferable when all subproblem solutions must be calculated<sup>10</sup> . Additional dynamic programming examples may be found online [7].

### **2.4.3 Sequence Alignment using Dynamic Programming**

We are now ready to solve the more difficult problem of sequence alignment using dynamic programming, which is presented in depth in the next section. Note that the key insight in solving the sequence alignment problem is that alignment scores are additive. This allows us to create a matrix _M_ indexed by _i_ and _j_ , which are positions in two sequences _S_ and _T_ to be aligned. The best alignment of _S_ and _T_ corresponds with the best path through the matrix _M_ after it is filled in using a recursive formula.

By using dynamic programming to solve the sequence alignment problem, we achieve a provably optimal solution, that is far more efficient than brute-force enumeration.

## **2.5 The Needleman-Wunsch Algorithm**

We will now use dynamic programming to tackle the harder problem of general sequence alignment. Given two strings S =( _S_ 1 _, . . . , Sn_ ) and T =( _T_ 1 _, . . . , Tm_ ), we want to find the longest common subsequence, which may or may not contain gaps. Rather than maximizing the length of a common subsequence we want to compute the common subsequence that optimizes the score as defined by our scoring function. Let d denote the gap penalty cost and s(x; y) the score of aligning a base x and a base y. These are inferred from insertion/deletion and substitution probabilities which can be determined experimentally or by looking at sequences that we know are closely related. The algorithm we will develop in the following sections to solve sequence alignment is known as the Needleman-Wunsch algorithm.

### **2.5.1 Dynamic programming vs. memoization**

Before we dive into the algorithm, a final note on memoization is in order. Much like the Fibonacci problem, the sequence alignment problem can be solved in either a top-down or bottom-up approach.

In a _top-down recursive approach_ we can use memoization to create a potentially large dictionary indexed by each of the subproblems that we are solving (aligned sequences). This requires _O_ ( _n_<sup>2</sup> _m_<sup>2</sup> ) space if we index each subproblem by the starting and end points of the subsequences for which an optimal alignment needs to be computed. The advantage is that we solve each subproblem at most once: if it is not in the dictionary, the problem gets computed and then inserted into dictionary for further reference.

In a _bottom-up iterative approach_ we can use dynamic programming. We define the order of computing sub-problems in such a way that a solution to a problem is computed once the relevant sub-problems have

> 10In some cases dynamic programming is virtually the only acceptable solution; this is the case in particular when dependency chains between subproblems are long: in this case, the memoization-based solution recurses too deeply, and causes a stack overflow

34

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming

been solved. In particular, simpler sub-problems will come before more complex ones. This removes the need for keeping track of which sub-problems have been solved (the dictionary in memoization turns into a matrix) and ensures that there is no duplicated work (each sub-alignment is computed only once).

Thus in this particular case, the only practical difference between memoization and dynamic programming is the cost of recursive calls incurred in the memoization case (space usage is the same).

### **2.5.2 Problem Statement**

Suppose we have an optimal alignment for two sequences _S_ 1 _...n_ and _T_ 1 _...m_ in which _Si_ matches _Tj_ . The key insight is that this optimal alignment is composed of an optimal alignment between ( _S_ 1 _, . . . , Si−_ 1) and ( _T_ 1 _, . . . , Tj−_ 1<sup>)andanoptimalalignmentbetween(</sup><sup>_S_</sup> _i_ +1 _, . . . ., Sn_ ) and ( _Tj_ +1 _, . . . ., Tm_ ). This follows from a cut-and-paste argument: if one of these partial alignments is suboptimal, then we cut-and-paste a better alignment in place of the suboptimal one. This achieves a higher score of the overall alignment and thus contradicts the optimality of the initial global alignment. In other words, every subpath in an optimal path must also be optimal. Notice that the scores are additive, so the score of the overall alignment equals the addition of the scores of the alignments of the subsequences. This implicitly assumes that the sub-problems of computing the optimal scoring alignments of the subsequences are independent. We need to biologically motivate that such an assumption leads to meaningful results.

### **2.5.3 Index space of subproblems**

We now need to index the space of subproblems. Let _Fi,j_ be the score of the optimal alignment of ( _S_ 1 _, . . . , Si_ ) and ( _T_ 1 _, . . . , Tj_ ). The space of subproblems is _{Fi,j, i ∈_ [0 _, |S|_ ] _, j ∈_ [0 _, |T |_ ] _}_ . This allows us to maintain an ( _m_ + 1) _×_ ( _n_ + 1) matrix F with the solutions (i.e. optimal scores) for all the subproblems.

### **2.5.4 Local optimality**

We can compute the optimal solution for a subproblem by making a locally optimal choice based on the results from the smaller sub-problems. Thus, we need to establish a recursive function that shows how the solution to a given problem depends on its subproblems. And we use this recursive definition to fill up the table F in a bottom-up fashion.

We can consider the 4 possibilities (insert, delete, substitute, match) and evaluate each of them based on the results we have computed for smaller subproblems. To initialize the table, we set _F_ 0 _,j_ = _−j · d_ and _Fi,_ 0 = _−i · d_ since those are the scores of aligning ( _T_ 1 _, . . . , Tj_ ) with _j_ gaps and ( _S_ 1 _, . . . ., Si_ ) with _i_ gaps (aka zero overlap between the two sequences). Then we traverse the matrix column by column computing the optimal score for each alignment subproblem by considering the four possibilities:

- Sequence S has a gap at the current alignment position.

- Sequence T has a gap at the current alignment position.

- There is a mutation (nucleotide substitution) at the current position.

- There is a match at the current position.

We then use the possibility that produces the maximum score. We express this mathematically by the recursive formula for _Fi,j_ :

35

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming


_Termination_ `:` _Bottom right_

After traversing the matrix, the optimal score for the global alignment is given by _Fm,n_ . The traversal order needs to be such that we have solutions to given subproblems when we need them. Namely, to compute _Fi,j_ , we need to know the values to the left, up, and diagonally above _Fi,j_ in the table. Thus we can traverse the table in row or column major order or even diagonally from the top left cell to the bottom right cell. Now, to obtain the actual alignment we just have to remember the choices that we made at each step.

### **2.5.5 Optimal Solution**

Paths through the matrix _F_ correspond to optimal sequence alignments. In evaluating each cell _Fi,j_ we make a choice by selecting the maximum of the three possibilities. Thus the value of each (uninitialized) cell in the matrix is determined either by the cell to its left, above it, or diagonally to the left above it. A match and a substitution are both represented as traveling in the diagonal direction; however, a different cost can be applied for each, depending on whether the two base pairs we are aligning match or not. To construct the actual optimal alignment, we need to traceback through our choices in the matrix. It is helpful to maintain a pointer for each cell while filling up the table that shows which choice was made to get the score for that cell. Then we can just follow our pointers backwards to reconstruct the optimal alignment.

### **2.5.6 Solution Analysis**

The runtime analysis of this algorithm is very simple. Each update takes _O_ (1) time, and since there are _mn_ elements in the matrix F, the total running time is _O_ ( _mn_ ). Similarly, the total storage space is _O_ ( _mn_ ). For the more general case where the update rule is more complicated, the running time may be more expensive. For instance, if the update rule requires testing all sizes of gaps (e.g. the cost of a gap is not linear), then the running time would be _O_ ( _mn_ ( _m_ + _n_ )).

### **2.5.7 Needleman-Wunsch in practice**

Assume we want to align two sequences S and T, where

S = AGT

T = AAGC

The first step is placing the two sequences along the margins of a matrix and initializing the matrix cells. To initialize we assign a 0 to the first entry in the matrix and then fill in the first row and column based on the incremental addition of gap penalties, as in Figure 2.9 below. Although the algorithm could fill in the first row and column through iteration, it is important to clearly define and set boundaries on the problem.

The next step is iteration through the matrix. The algorithm proceeds either along rows or along columns, considering one cell at time. For each cell three scores are calculated, depending on the scores of three adjacent matrix cells (specifically the entry above, the one diagonally up and to the left, and the one to the left). The maximum score of these three possible tracebacks is assigned to the entry and the corresponding pointer is also stored. Termination occurs when the algorithm reaches the bottom right corner. In Figure 2.10 the alignment matrix for sequences S and T has been filled in with scores and pointers.

36

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming


<!-- Start of picture text -->
-  A G T  Initialization:<br>-  0  -2  -4  -6<br>• Top left: 0<br>• M( i ,0)=M( i -1,0) - 2  gap�<br>• M(0, j )=M(0, j -1) - 2  gap�<br>A -2<br>Update Rule:<br>M( i , j )=max{<br>A -4<br>G -6  }<br>Termination:<br>C  -8<br><!-- End of picture text -->

Figure 2.9: (Example) Initial setup for Needleman-Wunsch


Figure 2.10: (Example) Half-way through the second step of Needleman-Wunsch

The final step of the algorithm is optimal path traceback. In our example we start at the bottom right corner and follow the available pointers to the top left corner. By recording the alignment decisions made at each cell during traceback, we can reconstruct the optimal sequence alignment from end to beginning and then invert it. Note that in this particular case, multiple optimal pathways exist (Figure 2.11). A pseudocode implementation of the Needleman-Wunsch algorithm is included in Appendix 2.11.4

### **2.5.8 Optimizations**

The dynamic algorithm we presented is much faster than the brute-force strategy of enumerating alignments and it performs well for sequences up to 10 kilo-bases long. Nevertheless, at the scale of whole genome alignments the algorithm given is not feasible. In order to align much larger sequences we can make modifications to the algorithm and further improve its performance.

#### **Bounded Dynamic Programming**

One possible optimization is to ignore Mildly Boring Alignments (MBAs), or alignments that have too many gaps. Explicitly, we can limit ourselves to stay within some distance W from the diagonal in the matrix

37

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming


Figure 2.11: (Example) Tracing the optimal alignment

F of subproblems. That is, we assume that the optimizing path in F from _F_ 0 _,_ 0 to _Fm,n_ is within distance W along the diagonal. This means that recursion (2.2) only needs to be applied to the entries in F within distance W around the diagonal, and this yields a time/space cost of _O_ (( _m_ + _n_ ) _W_ ) (refer to Figure 2.12).


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 2.12: Bounded dynamic programming example

Note, however, that this strategy is heuristic and no longer guarantees an optimal alignment. Instead it attains a lower bound on the optimal score. This can be used in a subsequent step where we discard the recursions in matrix F which, given the lower bound, cannot lead to an optimal alignment.

#### **Linear Space Alignment**

Recursion (2.2) can be solved using only linear space: we update the columns in F from left to right during which we only keep track of the last updated column which costs _O_ ( _m_ ) space. However, besides the score

38

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming

_Fm,n_ of the optimal alignment, we also want to compute a corresponding alignment. If we use trace back, then we need to store pointers for each of the entries in F, and this costs _O_ ( _mn_ ) space.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 2.13: Recovering the sequence alignment with _O_ ( _m_ + _n_ ) space

It is also possible to find an optimal alignment using only linear space! The goal is to use divide and conquer in order to compute the structure of the optimal alignment for one matrix entry in each step. Figure 2.13 illustrates the process. The key idea is that a dynamic programming alignment can proceed just as easily in the reverse direction, starting at the bottom right corner and terminating at the top left. So if the matrix is divided in half, then both a forward pass and a reverse pass can run at the same time and converge in the middle column. At the crossing point we can add the two alignment scores together; the cell in the middle column with the maximum score must fall in the overall optimal path.

We can describe this process more formally and quantitatively. First compute the row index _u ∈ {_ 1 _, . . . , m}_ that is on the optimal path while crossing the<sup>_<u>n</u>_</sup> 2 th column. For 1 _≤ i ≤ m_ and _<u>n</u>_ 2<sup>_≤j≤n_</sup> let _Ci,j_ denote the row index that is on the optimal path to _Fi,j_ while crossing the<sup>_<u>n</u>_</sup> 2 th column. Then, while we update the columns of F from left to right, we can also update the columns of C from left to right. So, in _O_ ( _mn_ ) time and _O_ ( _m_ ) space we are able to compute the score _Fm,n_ and also _Cm,n_ , which is equal to the row index _u ∈{_ 1 _, . . . , m}_ that is on the optimal path while crossing the<sup>_<u>n</u>_</sup> 2 th column.

Now the idea of divide and conquer kicks in. We repeat the above procedure for the upper left _u ×_<sup>_<u>n</u>_</sup> 2 submatrix of F and also repeat the above procedure for the lower right ( _m − u_ ) _×_<sup>_<u>n</u>_</sup> 2<sup>submatrixofF.This</sup> can be done using _O_ ( _m_ + _n_ ) allocated linear space. The running time for the upper left submatrix is _O_ (<sup>_<u>un</u>_</sup> 2<sup>)</sup> and the running time for the lower right submatrix is _O_ (<sup><u>(</u></sup><sup>_m−_</sup> 2<sup>_u_</sup><sup><u>)</u></sup><sup>_n_</sup> ), which added together gives a running time of _O_ (<sup>_<u>mn</u>_</sup> 2<sup>) =</sup><sup>_O_(</sup><sup>_mn_).</sup>

We keep on repeating the above procedure for smaller and smaller submatrices of F while we gather more and more entries of an alignment with optimal score. The total running time is _O_ ( _mn_ )+ _O_ (<sup>_<u>mn</u>_</sup> 2<sup>)+</sup><sup>_O_(</sup><sup>_<u>mn</u>_</sup> 4 )+ _..._ = _O_ (2 _mn_ ) = _O_ ( _mn_ ). So, without sacrificing the overall running time (up to a constant factor), divide and conquer leads to a linear space solution (see also Section **??** on Lecture 3).

## **2.6 Multiple alignment**

### **2.6.1 Aligning three sequences**

Now that we have seen how to align a pair of sequences, it is natural to extend this idea to _multiple_ sequences. Suppose we would like to find the optimal alignment of 3 sequences. How might we proceed?

39

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming

Recall that when we align two sequences _S_ and _T_ , we choose the maximum of three possibilities for the final position of the alignment (sequence _T_ aligned against a gap, sequence _S_ aligned against a gap, or sequence _S_ aligned against sequence _T_ ):


For three sequences _S_ , _T_ , and _U_ , there are seven possibilities for the final position of the alignment. That haveis, thereall threeare threesequencesways toalignedhave tw(�<sup>3</sup> 1o� gaps+ ��32<sup>in</sup> +<sup>the</sup> ��33<sup>final</sup> = 7).<sup>position,</sup> The update<sup>three</sup> rule<sup>ways</sup> is now:<sup>tohaveonegap,andonewayto</sup>


where _s_ is the function describing gap, match, and mismatch scores.

This approach, however, is exponential in the number of sequences we are aligning. If we have k sequences of length _n_ , computing the optimal alignment using a k-dimensional dynamic programming matrix takes _O_ ((2 _n_ )<sup>_k_</sup> ) time (the factor of 2 results from the fact that a k-cube has 2<sup>_k_</sup> vertices, so we need to take the maximum of 2<sup>_k_</sup> _−_ 1 neighboring cells for each entry in the score matrix). As you can imagine, this algorithm quickly becomes impractical as the number of sequences increases.

### **2.6.2 Heuristic multiple alignment**

One commonly used approach for multiple sequence alignment is called _progressive multiple alignment_ . Assume that we know the evolutionary tree relating each of our sequences. Then we begin by performing a pairwise alignment of the two most closely-related sequences. This initial alignment is called the _seed alignment_ . We then proceed to align the next closest sequence to the seed, and this new alignment replaces the seed. This process continues until the final alignment is produced.

In practice, we generally do not know the evolutionary tree (or _guide tree_ ), this technique is usually paired with some sort of clustering algorithm that may use a low-resolution similarity measure to generate an estimation of the tree.

While the running time of this heuristic approach is much improved over the previous method (polynomial in the number of sequences rather than exponential), we can no longer guarantee that the final alignment is optimal.

Note that we have not yet explained how to align a sequence against an existing alignment. One possible approach would be to perform pairwise alignments of the new sequence with each sequence already in the seed alignment (we assume that any position in the seed alignment that is already a gap will remain one). Then we can add the new sequence onto the seed alignment based on the best pairwise alignment (this approach was previously described by Feng and Doolittle[4]). Alternatively, we can devise a function for scoring the alignment of a sequence with another alignment (such scoring functions are often based on the pairwise sum of the scores at each position).

Design of better multiple sequence alignment tools is an active area of research. Section 2.9 details some of the current work in this field.

40

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming

## **2.7 Current Research Directions**

## **2.8 Further Reading**

## **2.9 Tools and Techniques**

Lalign finds local alignments between two sequences. Dotlet is a browser-based Java applet for visualizing the alignment of two sequences in a dot-matrix.

The following tools are available for multiple sequence alignment:

- Clustal Omega - A multiple sequence alignment program that uses seeded guide trees and HMM profile-profile techniques to generate alignments.[10]

- MUSCLE - MUltiple Sequence Comparison by Log-Expectation[3]

- T-Coffee - Allows you to combine results obtained with several alignment methods[2]

- MAFFT - (Multiple Alignment using Fast Fourier Transform) is a high speed multiple sequence alignment program[5]

- Kalign - A fast and accurate multiple sequence alignment algorithm[9]

## **2.10 What Have We Learned?**

## **2.11 Appendix**

### **2.11.1 Homology**

One of the key goals of sequence alignment is to identify homologous sequences (e.g., genes) in a genome. Two sequences that are homologous are evolutionarily related, specifically by descent from a common ancestor. The two primary types of homologs are orthologous and paralogous (refer to Figure 2.14<sup>11</sup> ). Other forms of homology exist (e.g., xenologs), but they are outside the scope of these notes.

_Orthologs_ arise from speciation events, leading to two organisms with a copy of the same gene. For example, when a single species A speciates into two species B and C, there are genes in species B and C that descend from a common gene in species A, and these genes in B and C are orthologous (the genes continue to evolve independent of each other, but still perform the same relative function).

_Paralogs_ arise from duplication events within a species. For example, when a gene duplication occurs in some species A, the species has an original gene B and a gene copy B<sup>_′_</sup> , and the genes B and B<sup>_′_</sup> are paralogus. Generally, orthologous sequences between two species will be more closely related to each other than paralogous sequences. This occurs because orthologous typically (although not always) preserve function over time, whereas paralogous often change over time, for example by specializing a gene’s (sub)function or by evolving a new function. As a result, determining orthologous sequences is generally more important than identifying paralogous sequences when gauging evolutionary relatedness.

### **2.11.2 Natural Selection**

The topic of natural selection is a too large topic to summarize effectively in just a few short paragraphs; instead, this appendix introduces three broad types of natural selection: positive selection, negative selection, and neutral selection.

- _Positive selection_ occurs when a trait is evolutionarily advantageous and increases an individual’s fitness, so that an individual with the trait is more likely to have (robust) offspring. It is often associated with the development of new traits.

> 11R.B. - BIOS 60579

41

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 2.14: Ortholog and paralog sequences

- _Negative selection_ occurs when a trait is evolutionarily disadvantageous and decreases an individual’s fitness. Negative selection acts to reduce the prevalence of genetic alleles that reduce a species’ fitness. Negative selection is also known as purifying selection due to its tendency to ’purify’ genetic alleles until only the most successful alleles exist in the population.

- _Neutral selection_ describes evolution that occurs randomly, as a result of alleles not affecting an individual’s fitness. In the absence of selective pressures, no positive or negative selection occurs, and the result is neutral selection.

### **2.11.3 Dynamic Programming v. Greedy Algorithms**

Dynamic programming and greedy algorithms are somewhat similar, and it behooves one to know the distinctions between the two. Problems that may be solved using dynamic programming are typically optimization problems that exhibit two traits:

#### 1. **optimal substructure** and

#### 2. **overlapping subproblems** .

Problems solvable by greedy algorithms require both these traits as well as (3) the **greedy choice property** . When dealing with a problem “in the wild,” it is often easy to determine whether it satisfies (1) and (2) but difficult to determine whether it must have the greedy choice property. It is not always clear whether locally optimal choices will yield a globally optimal solution.

For computational biologists, there are two useful points to note concerning whether to employ dynamic programming or greedy programming. First, if a problem may be solved using a greedy algorithm, then it may be solved using dynamic programming, while the converse is not true. Second, the problem structures that allow for greedy algorithms typically do not appear in computational biology.

To elucidate this second point, it could be useful to consider the structures that allow greedy programming to work, but such a discussion would take us too far afield. The interested student (preferably one with a mathematical background) should look at matroids and greedoids, which are structures that have the greedy choice property. For our purposes, we will simply state that biological problems typically involve entities that are highly systemic and that there is little reason to suspect sufficient structure in most problems to employ greedy algorithms.

42

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming

### **2.11.4 Pseudocode for the Needleman-Wunsch Algorithm**

The first problem in the first problem set asks you to finish an implementation of the Needleman-Wunsch (NW) algorithm, and working Python code for the algorithm is intentionally omitted. Instead, this appendix summarizes the general steps of the NW algorithm (Section 2.5) in a single place.

Problem: Given two sequences S and T of length m and n, a substitution matrix vU of matching scores, and a gap penalty G, determine the optimal alignment of S and T and the score of the alignment. Algorithm:

1. Create two _m_ + 1 by _n_ + 1 matrices A and B. A will be the scoring matrix, and B will be the traceback matrix. The entry ( _i, j_ ) of matrix A will hold the score of the optimal alignment of the sequences _S_ [1 _, . . . , i_ ] and _T_ [1 _, . . . , j_ ], and the entry ( _i, j_ ) of matrix B will hold a pointer to the entry from which the optimal alignment was built.

2. Initialize the first row and column of the score matrix A such that the scores account for gap penalties, and initialize the first row and column of the traceback matrix B in the obvious way.

3. Go through the entries ( _i, j_ ) of matrix A in some reasonable order, determining the optimal alignment of the sequences _S_ [1 _, . . . , i_ ] and _T_ [1 _, . . . , j_ ] using the entries ( _i −_ 1 _, j −_ 1), ( _i −_ 1 _, j_ ), and ( _i, j −_ 1). Set the pointer in the matrix B to the corresponding entry from which the optimal alignment at ( _i, j_ ) was built.

4. Once all entries of matrices A and B are completed, the score of the optimal alignment may be found in entry ( _m, n_ ) of matrix A.

5. Construct the optimal alignment by following the path of pointers starting at entry ( _m, n_ ) of matrix B and ending at entry (0 _,_ 0) of matrix B.

## **Bibliography**

- [1] Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein. _Introduction to Algorithms_ . The MIT Press, London, third edition, 1964.

- [2] Paolo Di Tommaso, Sebastien Moretti, Ioannis Xenarios, Miquel Orobitg, Alberto Montanyola, Jia-Ming Chang, Jean-Fran¸cois Taly, and Cedric Notredame. T-Coffee: a web server for the multiple sequence alignment of protein and RNA sequences using structural information and homology extension. _Nucleic Acids Research_ , 39(Web Server issue):W13–W17, 2011.

- [3] Robert C Edgar. MUSCLE: multiple sequence alignment with high accuracy and high throughput. _Nucleic acids research_ , 32(5):1792–7, January 2004.

- [4] D F Feng and R F Doolittle. Progressive sequence alignment as a prerequisite to correct phylogenetic trees. _Journal of Molecular Evolution_ , 25(4):351–360, 1987.

- [5] Kazutaka Katoh, George Asimenos, and Hiroyuki Toh. Multiple alignment of DNA sequences with MAFFT. _Methods In Molecular Biology Clifton Nj_ , 537:39–64, 2009.

- [6] John D. Kececioglu and David Sankoff. Efficient bounds for oriented chromosome inversion distance. In _Proceedings of the 5th Annual Symposium on Combinatorial Pattern Matching_ , CPM ’94, pages 307–325, London, UK, UK, 1994. Springer-Verlag.

- [7] Manolis Kellis. Dynamic programming practice problems. http://people.csail.mit.edu/bdean/6.046/dp/, September 2010.

- [8] Manolis Kellis, Nick Patterson, Matthew Endrizzi, Bruce Birren, and Eric S Lander. Sequencing and comparison of yeast species to identify genes and regulatory elements. _Nature_ , 423(6937):241–254, 2003.

- [9] Timo Lassmann and Erik L L Sonnhammer. Kalign–an accurate and fast multiple sequence alignment algorithm. _BMC Bioinformatics_ , 6(1):298, 2005.

43

6.047/6.878 Lecture 2: Sequence Alignment and Dynamic Programming

- [10] Fabian Sievers, Andreas Wilm, David Dineen, Toby J Gibson, Kevin Karplus, Weizhong Li, Rodrigo Lopez, Hamish McWilliam, Michael Remmert, Johannes S¨oding, Julie D Thompson, and Desmond G Higgins. Fast, scalable generation of high-quality protein multiple sequence alignments using Clustal Omega. _Molecular Systems Biology_ , 7(539):539, 2011.

- [11] Zhaolei Zhang and Mark Gerstein. Patterns of nucleotide substitution, insertion and deletion in the human genome inferred from pseudogenes. _Nucleic Acids Research_ , 31(18):5338–5348, 2003.

44

## CHAPTER **THREE**

RAPID SEQUENCE ALIGNMENT AND DATABASE SEARCH

Heather Sweeney (Sep 20, 2015) Eric Bartell (Sep 20, 2015) Kathy Lin (Sep 11, 2014) Maria Rodriguez (Sep 13, 2011) Rushil Goel (Sep 16, 2010) Eric Eisner -Guilhelm Richard (Sep 17, 2009) Tural Badirkhnali (Sep 11, 2008)

### **Figures**

|3.1|Global Alignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>44|
|---|---|---|
|3.2|Global Alignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>45|
|3.3|Local Alignment<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>46|
|3.4|Local alignments to detect rearrangements . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>46|
|3.5|Semi-global Alignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>46|
|3.6|Bounded-space computation . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>48|
|3.7|Linear-space computation for optimal alignment score<br>. . . . . . . . . . . .|. . . . . . . .<br>48|
|3.8|Space-saving optimization for finding the optimal alignment . . . . . . . . .|. . . . . . . .<br>48|
|3.9|Divide and Conquer<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>49|
|3.10|Naive Karp-Rabin algorithm<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>50|
|3.11|Final Karp-Rabin algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>51|
|3.12|Pigeonhole Principle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>52|
|3.13|The BLAST Algorithm<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>53|
|3.14|Educated String Matching . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>56|
|3.15|Final String Matching . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>56|
|3.16|Nucleotide match scores . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>57|
|3.17|BLOSUM62 matrix for amino acids. . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>58|


## **3.1 Introduction**

In the previous chapter, we used dynamic programming to compute sequence alignments in _O_ ( _n_<sup>2</sup> ). In particular, we learned the algorithm for global alignment, which matches complete sequences with one another at the nucleotide level. We usually apply this when the sequences are known to be homologous (i.e. the sequences come from organisms that share a common ancestor).

The biological significance of finding sequence alignments is to be able to infer the most likely set of evolutionary events such as point mutations/mismatches and gaps (insertions or deletions) that occurred in order to transform one sequence into the other. To do so, we first assume that the set of transformations with

45

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search

the lowest cost is the most likely sequence of transformations. By assigning costs to each transformation type (mismatch or gap) that reflect their respective levels of evolutionary difficulty, finding an optimal alignment reduces to finding the set of transformations that result in the lowest overall cost.

We achieve this by using a dynamic programming algorithm known as the Needleman-Wunsch algorithm. Dynamic programming uses optimal substructures to decompose a problem into similar sub-problems. The problem of finding a sequence alignment can be nicely expressed as a dynamic programming algorithm since alignment scores are additive, which means that finding the alignment of a larger sequence can be found by recursively finding the alignments of smaller subsequences. The scores are stored in a matrix, with one sequence corresponding to the columns and the other sequence corresponding to the rows. Each cell represents the transformation required between two nucleotides corresponding to the cell’s row and column. An alignment is recovered by tracing back through the dynamic programming matrix (shown below). The dynamic programming approach is preferable to a greedy algorithm that simply chooses the transition with minimum cost at each step because a greedy algorithm does not guarantee that the overall result will give the optimal or lowest-cost alignment.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 3.1: Global Alignment

To summarize the Needleman-Wunsch algorithm for global alignment:

- We compute scores corresponding to each cell in the matrix and record our choice (memoization) at that step i.e. which one of the top, left or diagonal cells led to the maximum score for the current cell. We are left with a matrix full of optimal scores at each cell position, along with pointers at each cell reflecting the optimal choice that leads to that particular cell.

- We can then recover the optimal alignment by tracing back from the cell in the bottom right corner (which contains the score of aligning one complete sequence with the other) by following the pointers reflecting locally optimal choices, and then constructing the alignment corresponding to an optimal path followed in the matrix.

- The runtime of Needleman-Wunsch algorithm is _O_ ( _n_<sup>2</sup> ) since for each cell in the matrix, we do a finite amount of computation. We calculate 3 values using already computed scores and then take the maximum of those values to find the score corresponding to that cell, which is a constant time ( _O_ (1)) operation.

- To guarantee correctness, it is necessary to compute the cost for every cell of the matrix. It is possible that the optimal alignment may be made up of a bad alignment (consisting of gaps and mismatches) at the start, followed by many matches, making it the best alignment overall. These are the cases that traverse the boundary of our alignment matrix. Thus, to guarantee the optimal global alignment, we need to compute every entry of the matrix.

Global alignment is useful for comparing two sequences that are believed to be homologous. It is less useful for comparing sequences with rearrangements or inversions or aligning a newly-sequenced gene against reference genes in a known genome, known as database search. In practice, we can also often restrict the alignment space to be explored if we know that some alignments are clearly sub-optimal.

This chapter will address other forms of alignment algorithms to tackle such scenarios. It will first introduce the Smith-Waterman algorithm for local alignment for aligning subsequences as opposed to complete sequences, in contrast to the Needleman-Wunsch algorithm for global alignment. Later on, an overview will be given of hashing and semi-numerical methods like the Karp-Rabin algorithm for finding the longest

46

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search

(contiguous) common substring of nucleotides. These algorithms are implemented and extended for inexact matching in the BLAST program, one of the most highly cited and successful tools in computational biology. Finally, this chapter will go over BLAST for database searching as well as the probabilistic foundation of sequence alignment and how alignment scores can be interpreted as likelihood ratios.

Outline:

1. **Introduction**

   - Review of global alignment (Needleman-Wunsch)

2. **Global alignment vs. Local alignment vs. Semi-global alignment**

   - Initialization, termination, and update rules for Global alignment (Needleman-Wunsch) vs. Local alignment (Smith-Waterman) vs. Semi-global alignment

   - Varying gap penalties, algorithmic speedups

3. **Linear-time exact string matching**

   - Karp-Rabin algorithm and semi-numerical methods

   - Hash functions and randomized algorithms

4. **The BLAST algorithm and inexact matching**

   - Hashing with neighborhood search

   - Two-hit blast and hashing with combs

5. **Pre-processing for linear-time string matching**

   - Fundamental pre-processing

   - Suffix Trees

   - Suffix Arrays

   - The Burrows-Wheeler Transform

6. **Probabilistic foundations of sequence alignment**

   - Mismatch penalties, BLOSUM and PAM matrices

   - Statistical significance of an alignment score

## **3.2 Global alignment vs. Local alignment vs. Semi-global alignment**

A **global alignment** is defined as the _end-to-end_ alignment of two strings _s_ and _t_ .

A **local alignment** of string _s_ and _t_ is an alignment of _substrings_ of _s_ with substrings of _t_ .

In general are used to find regions of high local similarity. Often, we are more interested in finding local alignments because we normally do not know the boundaries of genes and only a small domain of the gene may be conserved. In such cases, we do not want to enforce that other (potentially non-homologous) parts of the sequence also align. Local alignment is also useful when searching for a small gene in a large chromosome or for detecting when a long sequence may have been rearranged (Figure 4).

A **semi-global alignment** of string s and t is an alignment of a substring of s with a substring of t. This form of alignment is useful for overlap detection when we do not wish to penalize starting or ending gaps. For finding a semi-global alignment, the important distinctions are to initialize the top row and leftmost column to zero and terminate end at either the bottom row or rightmost column.

The algorithm is as follows:

47

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search


Figure 3.2: Global Alignment


Figure 3.3: Local Alignment


Figure 3.4: Local alignments to detect rearrangements


Figure 3.5: Semi-global Alignment

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

_Initialization_ `:` _F_ ( _i,_ 0) = 0 _F_ (0 _, j_ ) = 0  _F_ ( _i −_ 1 _, j_ ) _− d Iteration_ `:` _F_ ( _i, j_ ) = max _F_ ( _i, j −_ 1) _− d_   _F_ ( _i −_ 1 _, j −_ 1) + _s_ ( _xi, yj_ ) _Termination_ `:` _Bottom row or Right column_

48

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search

### **3.2.1 Using Dynamic Programming for local alignments**

In this section we will see how to find local alignments with a minor modification of the Needleman-Wunsch algorithm that was discussed in the previous chapter for finding global alignments.

To find global alignments, we used the following dynamic programming algorithm (Needleman-Wunsch algorithm):


For finding local alignments we only need to modify the Needleman-Wunsch algorithm slightly to start over and find a new local alignment whenever the existing alignment score goes negative. Since a local alignment can start anywhere, we initialize the first row and column in the matrix to zeros. The iteration step is modified to include a zero to include the possibility that starting a new alignment would be cheaper than having many mismatches. Furthermore, since the alignment can end anywhere, we need to traverse the entire matrix to find the optimal alignment score (not only in the bottom right corner). The rest of the algorithm, including traceback, remains unchanged, with traceback indicationg an end at a zero, indicating the start of the optimal alignment.

These changes result in the following dynamic programming algorithm for local alignment, which is also known as the :


### **3.2.2 Algorithmic Variations**

Sometimes it can be costly in both time and space to run these alignment algorithms. Therefore, this section presents some algorithmic variations to save time and space that work well in practice.

One method to save time, is the idea of bounding the space of alignments to be explored. The idea is that good alignments generally stay close to the diagonal of the matrix. Thus we can just explore matrix cells within a radius of _k_ from the diagonal. The problem with this modification is that this is a heuristic and can lead to a sub-optimal solution as it doesn’t include the boundary cases mentioned at the beginning of the chapter. Nevertheless, this works very well in practice. In addition, depending on the properties of the scoring matrix, it may be possible to argue the correctness of the bounded-space algorithm. This algorithm requires _O_ ( _k ∗ m_ ) space and _O_ ( _k ∗ m_ ) time.

We saw earlier that in order to compute the optimal solution, we needed to store the alignment score in each cell as well as the pointer reflecting the optimal choice leading to each cell. However, if we are only interested in the _optimal alignment score_ , and not the actual alignment itself, there is a method to compute the solution while saving space. To compute the score of any cell we only need the scores of the cell above, to the left, and to the left-diagonal of the current cell. By saving the previous and current column in which we are computing scores, the optimal solution can be computed in linear space.

If we use the principle of divide and conquer, we can actually find the _optimal alignment_ with linear space. The idea is that we compute the optimal alignments from both sides of the matrix i.e. from the left to the right, and vice versa. Let _u_ = _⌊_<sup>_<u>n</u>_</sup> 2<sup>_⌋_.Saywecanidentify</sup><sup>_v_suchthatcell(</sup><sup>_u, v_)isontheoptimal</sup>

49

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search


Figure 3.6: Bounded-space computation


Figure 3.7: Linear-space computation for optimal alignment score © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

alignment path. That means _v_ is the row where the alignment crosses column _u_ of the matrix. We can find the optimal alignment by concatenating the optimal alignments from (0,0) to ( _u, v_ ) plus that of ( _u, v_ ) to ( _m, n_ ), where _m_ and _n_ is the bottom right cell (note: alignment scores of concatenated subalignments using our scoring scheme are additive. So we have isolated our problem to two separate problems in the the top left and bottom right corners of the DP matrix. Then we can recursively keep dividing up these subproblems to smaller subproblems, until we are down to aligning 0-length sequences or our problem is small enough to apply the regular DP algorithm. To find _v_ the row in the middle column where the optimal alignment crosses we simply add the incoming and outgoing scores for that column.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 3.8: Space-saving optimization for finding the optimal alignment

One drawback of this divide-and-conquer approach is that it has a longer runtime. Nevertheless, the runtime is not dramatically increased. Since _v_ can be found using one pass of regular DP, we can find _v_ for each column in _O_ ( _mn_ ) time and linear space since we don’t need to keep track of traceback pointers for this step. Then by applying the divide and conquer approach, the subproblems take half the time since we only need to keep track of the cells diagonally along the optimal alignment path (half of the matrix of the previous step) That gives a total run time of _O_ ( _mn_ (1 + 2<sup><u>1</u>+</sup><sup><u>1</u></sup> 4 + _. . ._ )) = _O_ (2 _MN_ ) = _O_ ( _mn_ ) (using the sum of geometric series), to give us a quadratic run time (twice as slow as before, but still same asymptotic behavior). The total time will never exceed 2 _MN_ (twice the time as the previous algorithm). Although the runtime is increased by a constant factor, one of the big advantages of the divide-and-conquer approach is that the space is dramatically reduced to _O_ ( _N_ ).

50

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 3.9: Divide and Conquer

- **Q:** Why not use the bounded-space variation over the linear-space variation to get both linear time and linear space?

- **A:** The bounded-space variation is a heuristic approach that can work well in practice but does not guarantee the optimal alignment.

### **3.2.3 Generalized gap penalties**

Gap penalties determine the score calculated for a subsequence and thus affect which alignment is selected. The normal model is to use a where each individual gap in a sequence of gaps of length _k_ is penalized equally with value _p_ . This penalty can be modeled as _w_ ( _k_ ) = _k ∗ p_ .

Depending on the situation, it could be a good idea to penalize differently for, say, gaps of different lengths. One example of this is a in which the incremental penalty decreases quadratically as the size of the gap grows. This can be modeled as _w_ ( _k_ ) = _p_ + _q ∗ k_ + _r ∗ k_<sup>2</sup> . However, the trade-off is that there is also cost associated with using more complex gap penalty functions by substantially increasing runtime. This cost can be mitigated by using simpler approximations to the gap penalty functions. The is a fine intermediate: you have a fixed penalty to start a gap and a linear cost to add to a gap; this can be modeled as _w_ ( _k_ ) = _p_ + _q ∗ k_ .

You can also consider more complex functions that take into consideration the properties of protein coding sequences. In the case of protein coding region alignment, a gap of length mod 3 can be less penalized because it would not result in a frame shift.

## **3.3 Linear-time exact string matching**

While we have looked at various forms of alignment and algorithms used to find such alignments, these algorithms are not fast enough for some purposes. For instance, we may have a 100 nucleotide sequence which we want to search for in the whole genome, which may be over a billion nucleotides long. In this case, we want an algorithm with a run-time that depends on the length of query sequence, possibly with some pre-processing on the database, because processing the entire genome for every query would be extremely slow. For such problems, we enter the realm of randomized algorithms where instead of worrying about the worst-case performance, we are more interested in making sure that the algorithm is linear in the expected case. When looking for exact(consecutive) matches of a sequence, the Karp-Rabin algorithm interprets such a match numerically. There are many other solutions to this problem and some of them that can ensure the problem is linear in the worst case such as: the Z-algorithm, Boyer-Moore and Knuth-Morris-Pratt algorithm, algorithms based on suffix trees, suffix arrays, etc. (discussed in the “Lecture 3 addendum” slides)

### **3.3.1 Karp-Rabin Algorithm**

This algorithm tries to match a particular pattern to a string, which is the basic principle of database search. The problem is as follows: in text _T_ of length _n_ we are looking for pattern _P_ of length _m_ . Strings are mapped to numbers to enable fast comparison. A naive version of the algorithm involves mapping the string _P_ and

51

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search

_m_ -length substrings of _T_ sinto numbers _x_ and _y_ , respectively, sliding x along T at every offset until there is a match of the numbers.


Figure 3.10: Naive Karp-Rabin algorithm

However, one can see that the algorithm, as stated, is in fact non-linear for two reasons:

1. Computing each _yi_ takes more than constant time (it is in fact linear if we naively compute each number from scratch for each subsequence)

2. Comparing _x_ and _yi_ can be expensive if the numbers are very large which might happen if the pattern to be matched is very long

To make the algorithm faster, we first modify the procedure for calculating _yi_ in constant time by using the previously computed number, _yi −_ 1. We can do this using some bit operations: a subtraction to remove the high-order bit, a multiplication to shift the characters left, and an addition to append the low-order digit. For example, in Figure 10, we can compute _y_ 2 from _y_ 1 by

- removing the highest order bit: 23590 mod 10000 = 3590

- shifting left: 3590 _∗_ 10 = 35900

- adding the new low-order digit: 35900 + 2 = 35902

Our next issue arises when we have very long sequences to compare. This causes our calculations to be with very large numbers, which becomes no longer linear time. To keep the numbers small to ensure efficient comparison, we do all our computations modulo p (a form of hashing), where _p_ reflects the word length available to us for storing numbers, but is small enough such that the comparison between _x_ and _yi_ is doable in constant time.

: Using a function to map data values to a data set of fixed size.

Because we are using hashing, mapping to the space of numbers modulo _p_ can result in spurious hits due to hashing collisions, and so we modify the algorithm to deal with such spurious hits by explicitly verifying reported hits of the hash values. Hence, the final version of the Karp-Rabin algorithm is:

To compute the expected runtime of Karp-Rabin, we must factor in the expect cost of verification. If we can show the probability of spurious hits is small, the expected runtime is linear.

#### **Questions:**

- **Q:** What if there are more than 10 characters in the alphabet?

- **A:** In such a case, we can just modify the above algorithm by including more digits i.e. by working in a base other than 10, e.g. say base 256. But in general, when hashing is used, strings are mapped into a space of numbers and hence the strings are interpreted numerically.

- **Q:** How do we apply this to text?

52

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search


Figure 3.11: Final Karp-Rabin algorithm

- **A:** A hash function is used that changes the text into numbers that are easier to compare. For example, if the whole alphabet is used, letters can be assigned a value between 0 and 25, and then be used similar to a string of numbers.

- **Q:** Why does using modulus decrease the computation time?

- **A:** Modulus can be applied to each individual part in the computation while preserving the answer. For instance: imagine our current text is ”314152” and word length is 5. After making our first computation on ”31415”, we move our frame over to make our second computation, which is: 14152 = (31415 _−_ 3 _∗_ 10000) _∗_ 10 + 2( _mod_ 13) = (7 _−_ 3 _∗_ 3) _∗_ 10 + 2( _mod_ 13) = 8( _mod_ 13)

This computation can be done now in linear time.

- **Q:** Are there provisions in the algorithm for inexact matches?

- **A:** The above algorithm only works when there are regions of exact similarity between the query sequence and the database. However, the BLAST algorithm, which we look at later, extends the above ideas to include the notion of searching in a biologically meaningful neighborhood of the query sequence to account for some inexact matches. This is done by searching in the database for not just the query sequence, but also some variants of the sequence up to some fixed number of changes.

In general, in order to reduce the time for operations on arguments like numbers or strings that are really long, it is necessary to reduce the number range to something more manageable. Hashing is a general solution to this and it involves mapping keys _k_ from a large universe _U_ of strings/numbers into a hash of the key _h_ ( _k_ ) which lies in a smaller range, say [1 _...m_ ]. There are many hash function that can be used, all with different theoretical and practical properties. The two key properties that we need for hashing are:

1. Reproducibility if _x_ = _y_ , then _h_ ( _x_ ) = _h_ ( _y_ ). This is essential for our mapping to make sense.

2. Uniform output distribution This implies that regardless of the input distribution, the output distribution is uniform. i.e. if _x_ ! = _y_ , then _P_ ( _h_ ( _x_ ) = _h_ ( _y_ )) = 1 _/m_ , irrespective of the input distribution. This is a desirable property to reduce the chance of spurious hits.

An interesting idea that was raised was that it might be useful to have locality sensitive hash functions from the point of view of use in neighborhood searches, such that points in U that are close to each other are mapped to nearby points by the hash function. The notion of Random projections, as an extension of the BLAST algorithm, is based on this idea. Also, it is to be noted that modulo doesnt satisfy property 2 above because it is possible to have input distributions (e.g. all multiples of the number vis--vis which the

53

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search

modulo is taken) that result in a lot of collisions. Nevertheless, choosing a random number as the divisor of the modulo can avoid many collisions.

Working with hashing increases the complexity of analyzing the algorithm since now we need to compute the expected run time by including the cost of verification. To show that the expected run time is linear, we need to show that the probability of spurious hits is small.

## **3.4 The BLAST algorithm (Basic Local Alignment Search Tool)**

The BLAST algorithm looks at the problem of sequence database search, wherein we have a query, which is a new sequence, and a target, which is a set of many old sequences, and we are interested in knowing which (if any) of the target sequences is the query related to. One of the key ideas of BLAST is that it does not require the individual alignments to be perfect; once an initial match is identified, we can fine-tune the matches later to find a good alignment which meets a threshold score. Also, BLAST exploits a distinct characteristic of database search problems: most target sequences will be completely unrelated to the query sequence, and very few sequences will match.

However, correct (near perfect) alignments will have long substrings of nucleotides that match perfectly. E.g. if we looking for sequences of length 100 and are going to reject matches that are less than 90% identical, we need not look at sequences that do not even contain a consecutive stretch of less than 10 matching nucleotides in a row. We base this assumption on the : if m items are put in n containers and m _>_ n, at least 2 items must be put in one of the n containers.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

#### Figure 3.12: Pigeonhole Principle

In addition, in biology, functional DNA is more likely to be conserved, and therefore the mutations that we find will not actually be distributed randomly, but will be clustered in nonfunctional regions of DNA while leaving long stretches of functional DNA untouched. Therefore because of the pigeonhole principle and because highly similar sequences will have stretches of similarity, we can pre-screen the sequences for common long stretches. This idea is used in BLAST by breaking up the query sequence into W-mers and pre-screening the target sequences for all possible _W − mers_ by limiting our seeds to be _W − mers_ in the neighborhood that meet a certain threshold.

The other aspect of BLAST that allows us to speed up repeated queries is the ability to preprocess a large database of DNA off-line. After preprocessing, searching for a sequence of length _m_ in a database of length _n_ will take only _O_ ( _m_ ) time. The key insights that BLAST is based on are the ideas of hashing and neighborhood search that allows one to search for _W − mers_ , even when there are no exact-matches.

### **3.4.1 The BLAST algorithm**

The steps are as follows:

1. Split query into overlapping words of length _W_ (the _W -mers_ )

2. Find a “neighborhood” of similar words for each word (see below)

54

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search

3. Lookup each word in the neighborhood in a hash table to find the location in the database where each word occurs. Call these the _seeds_ , and let _S_ be the collection of seeds.

4. Extend the seeds in _S_ until the score of the alignment drops off below some threshold _X_ .

5. Report matches with overall highest scores


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 3.13: The BLAST Algorithm

The pre-processing step of BLAST makes sure that all substrings of _W_ nucleotides will be included in our database (or in a hash table). These are called the _W -mers_ of the database. As in step 1, we first split the query by looking at all substrings of W consecutive nucleotides in the query. To find the neighborhood of these _W -mers_ , we then modify these sequences by changing them slightly and computing their similarity to the original sequence. We generate progressively more dissimilar words in our neighborhood until our similarity measure drops below some threshold _T_ . This affords us flexibility to find matches that do not have exactly _W_ consecutive matching characters in a row, but which do have enough matches to be considered similar, i.e. to meet a certiain threshold score.

Then, we look up all of these words in our hash table to find seeds of _W_ consecutive matching nucleotides. We then extend these seeds to find our alignment using the Smith-Waterman algorithm for local alignment, until the score drops below a certain threshold _X_ . Since the region we are considering is a much shorter segment, this will not be as slow as running the algorithm on the entire DNA database.

It is also interesting to note the influence of various parameters of BLAST on the performance of the algorithm vis-a-vis run-time and sensitivity:

- **W** Although large _W_ would result in fewer spurious hits/collisions, thus making it faster, there are also tradeoffs associated, namely: a large neighborhood of slightly different query sequences, a large hash table, and too few hits. On the other hand, if _W_ is too small, we may get too many hits which pushes runtime costs to the seed extension/alignment step.

- **T** If T is higher, the algorithm will be faster, but you may miss sequences that are more evolutionarily distant. If comparing two related species, you can probably set a higher T since you expect to find more matches between sequences that are quite similar.

- **X** Its influence is quite similar to _T_ in that both will control the sensitivity of the algorithm. While _W_ and _T_ affect the total number of hits one gets, and hence affect the runtime of the algorithm dramatically, setting a really stringent _X_ despite less stringent _W_ and _T_ , will result runtime costs from trying unnecessary sequences that would not meet the stringency of _X_ . So, it is important to match the stringency of _X_ with that of _W_ and _T_ to avoid unnecessary computation time.

55

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search

### **3.4.2 Extensions to BLAST**

- **Filtering** Low complexity regions can cause spurious hits. For instance, if our query has a string of copies of the same nucleotide e.g. repeats of AC or just G, and the database has a long stretch of the same nucleotide, then there will be many many useless hits. To prevent this, we can either try to filter out low complexity portions of the query or we can ignore unreasonably over-represented portions of the database.

- **Two-hit BLAST** The idea here is to use double hashing wherein instead of hashing one long _W -mer_ , we will hash two small W-mers. This allows us to find small regions of similarity since it is much more likely to have two smaller _W -mers_ that match rather than one long _W -mer_ . This allows us to get a higher sensitivity with a smaller W, while still pruning out spurious hits. This means that we’ll spend less time trying to extend matches that don’t actually match. Thus, this allows us to improve speed while maintaining sensitivity.

- **Q:** For a long enough W, would it make sense to consider more than 2 smaller _W -mers_ ?

- **A:** It would be interesting to see how the number of such _W -mers_ influences the sensitivity of the algorithm. This is similar to using a comb, described next.

- **Combs** This is the idea of using non-consecutive _W -mers_ for hashing. Recall from your biology classes that the third nucleotide in a triplet usually doesnt actually have an effect on which amino acid is represented. This means that each third nucleotide in a sequence is less likely to be preserved by evolution, since it often doesnt matter. Thus, we might want to look for _W -mers_ that look similar except in every third codon. This is a particular example of a comb. A comb is simply a bit mask which represents which nucleotides we care about when trying to find matches. We explained above why 110110110 . . . (ignoring every third nucleotide) might be a good comb, and it turns out to be. However, other combs are also useful. One way to choose a comb is to just pick some nucleotides at random. Rather than picking just one comb for a projection, it is possible to randomly pick a set of such combs and project the W-mers along each of these combs to get a set of lookup databases. Then, the query string can also be projected randomly along these combs to lookup in these databases, thereby increasing the probability of finding a match. This is called Random Projection. Extending this, an interesting idea for a final project is to think of different techniques of projection or hashing that make sense biologically. One addition to this technique is to analyze false negatives and false positives, and change the comb to be more selective. Some papers that explore additions to this search include Califino-Rigoutsos’93, Buhler’01, and Indyk-Motwani’98.

- **PSI-BLAST** Position-Specific Iterative BLAST create summary profiles of related proteins using BLAST. After a round of BLAST, it updates the score matrix from the multiple alignment, and then runs subsequent rounds of BLAST, iteratively updating the score matrix. It builds a Hidden Markov Model to track conservation of specific amino acids. PSI-BLAST allows detection of distantly-related proteins.

## **3.5 Pre-processing for linear-time string matching**

The hashing technique at the core of the BLAST algorithm is a powerful way of string for rapid lookup. A substantial time is invested to process the whole genome, or a large set of genomes, _in advance_ of obtaining a query sequence. Once the query sequence is obtained, it can be similarly processed and its parts searched against the indexed database in linear time.

In this section, we briefly describe four additional ways of pre-processing a database for rapid string lookup, each of which has both practical and theoretical importance.

### **3.5.1 Suffix Trees**

Suffix trees provide a powerful tree representation of substrings of a target sequence T, by capturing all suffixes of T in a radix tree.

56

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search

**Representation of a sequence in a suffix tree**

#### **Searching a new sequence against a suffix tree**

#### **Linear-time construction of suffix trees**

### **3.5.2 Suffix Arrays**

For many genomic applications, suffix trees are too expensive to store in memory, and more efficient representations were needed. Suffix arrays were developed specifically to reduce the memory consumption of suffix trees, and achieve the same goals with a significantly reduced space need.

Using suffix arrays, any substring can be found by doing a binary search on the ordered list of suffixes. By thus exploring the prefix of every suffix, we end up searching all substrings.

### **3.5.3 The Burrows-Wheeler Transform**

An even more efficient representation than suffix trees is given by the Burrows-Wheeler Transform (BWT), which enables storing the entire hashed string in the same number of characters as the original string (and even more compactly, as it contains frequent homopolymer runs of characters that can be more easily compresed). This has helped make programs that can run even more efficiently.

We first consider the BWT matrix, which is an extension of a suffix array, in that it contains not only all suffixes in sorted (lexicographic) order, but it appends to each suffix starting at position _i_ the prefix ending at position _i −_ 1, each row thus containing a full rotation of the original string. This enables all the suffix-array and suffix-tree operations, of finding the position of suffixes in time linear in the query string.

The key difference from Suffix Arrays is space usage, where instead of storing all suffixes in memory, which even for suffix arrays is very expensive, only the last column of the BWT matrix is stored, based on which the original matrix can be recovered.

An auxiliary array can be used to speed things even further and avoid having to repeat operations of finding the first occurrence of each character in the modified suffix array.

Lastly, once the positions of 100,000s of substrings are found in the modified string (the last column of the BTW matrix), these coordinates can be transformed to the original positions, saving runtime by amortizing the cost of the transformation across the many many reads.

The BWT has had a very strong impact on short-string matching algorithms, and nearly all the fastest read mappers are currently based on the Burrows-Wheeler Transform.

### **3.5.4 Fundamental pre-processing**

This is a variation of processing that has theoretical interest but has found relatively little practical use in bioinformatics. It relies on the Z vector, that contains at each position _i_ the length of the longest prefix of a string that also matches the substring starting at _i_ . This enables computing the _L_ and _R_ (Left and Right) vectors that denote the end of the longest duplicate substrings that contains the current position _i_ .

### **3.5.5 Educated String Matching**

The Z algorithm enables an easy computation of both the Boyer-Moore and the Knuth-Morris-Pratt algorithms for linear-time string matching. These algorithms use information gathered at every comparison

57

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search

when matching strings to improve string matching to _O_ ( _n_ ).

The naive algorithm is as follows: it compares its string of length m character by character to the sequence. After comparing the entire string, if there are any mismatches, it moves to the next index and tries again. This completes in _O_ ( _m ∗ n_ ) time.

One improvement to this algorithm is to discontinue the current comparison if a mismatch is found. However, this still completes in _O_ ( _m ∗ n_ ) time when the string we are comparing matches the entire sequence.


#### Figure 3.14: Educated String Matching

The key insight comes from learning from the internal redundancy in the string to compare, and using that to make bigger shifts down the target sequence. When a mistake is made, all bases in the current comparison can be used to move the frame considered for the next comparison further down. As seen below, this greatly reduces the number of comparisons required, decreasing runtime to _O_ ( _n_ ).


Figure 3.15: Final String Matching

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

## **3.6 Probabilistic Foundations of Sequence Alignment**

As described above, the BLAST algorithm uses a scoring (substitution) matrix to expand the list of _W -mers_ in order to look for and determine an approximately matching sequence during seed extension. Also, a scoring matrix is used in evaluating matches or mismatches in the alignment algorithms. But how do we construct this matrix in the first place? How do you determine the value of _s_ ( _xi, yj_ ) in global/local alignment?

The idea behind the scoring matrix is that the score of alignment should reflect the probability that two similar sequences are homologous i.e. the probability that two sequences that have a bunch of nucleotides in common also share a common ancestry. For this, we look at the likelihood ratios between two hypotheses.

1. **Hypothesis 1:** – That the alignment between the two sequence is due to chance and the sequences are, in fact, unrelated.

2. **Hypothesis 2:** – That the alignment is due to common ancestry and the sequences are actually related.

Then, we calculate the probability of observing an alignment according to each hypothesis. _Pr_ ( _x, y|U_ ) is the probability of aligning _x_ with _y_ assuming they are unrelated, while _Pr_ ( _x, y|R_ ) is the probability of the

58

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search


Figure 3.16: Nucleotide match scores

alignment, assuming they are related. Then, we define the alignment score as the log of the likelihood ratio between the two:


Since a sum of logs is a log of products, we can get the total score of the alignment by adding up the scores of the individual alignments. This gives us the probability of the whole alignment, assuming each individual alignment is independent. Thus, an additive matrix score exactly gives us the probability that the two sequences are related, and the alignment is not due to chance. More formally, considering the case of aligning proteins, for unrelated sequences, the probability of having an n-residue alignment between _x_ and _y_ is a simple product of the probabilities of the individual sequences since the residue pairings are independent. That is,


For related sequences, the residue pairings are no longer independent so we must use a different joint probability, assuming that each pair of aligned amino acids evolved from a common ancestor:


Then, the likelihood ratio between the two is given by:


Since we eventually want to compute a sum of scores and probabilities require add products, we take the log of the product to get a handy summation:

59

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search


Thus, the substitution matrix score for a given pair _a, b_ is give by


The above expression is then used to crank out a substitution matrix like the BLOSUM62 for amino acids. It is interesting to note that the score of a match of an amino acid with itself depends on the amino acid itself because the frequency of random occurrence of an amino acid affects the terms used in calculating the likelihood ratio score of alignment. Hence, these matrices capture not only the sequence similarity of the alignments, but also the chemical similarity of various amino acids.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 3.17: BLOSUM62 matrix for amino acids

## **3.7 Current Research Directions**

## **3.8 Further Reading**

BLAST related algorithms: Califino-Rigoutsos’93, Buhler’01, and Indyk-Motwani’98

60

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search

## **3.9 Tools and Techniques**

## **3.10 What Have We Learned?**

In this section we explored alignment algorithms beyond global alignment. We began by reviewing our use of dynamic programming to solve global alignment problems using the Needleman-Wunsch algorithm. We then the explored alternatives of local (Smith-Waterman) and semi-global alignments. We then discussed using hash function to match exact strings in linear time (Karp-Rabin) as well as doing a neighborhood search, investigating similar sequences in probabilistic linear time (pigeonhole principle, combs, 2-hit blast, random projections). We have also addressed using pre-processing for linear time string matching, as well as the probabilistic background for sequence alignment.

## **Bibliography**

61

6.047/6.878 Lecture 3 - Rapid Sequence Alignment and Database Search

62

## CHAPTER **FOUR**

## COMPARATIVE GENOMICS I: GENOME ANNOTATION

#### Quanquan Liu (2013),

Mark Smith, Yarden Katz (Partially adapted from notes by:

Angela Yen, Christopher Robde, Timo Somervuo and Saba Gul)

### **Figures**

|4.1|Exon conservation from mammals to fish. . . . . . . . . . . . . . . . . . . . . . . . . . . .|64|
|---|---|---|
|4.2|Comparative identification of functional elements in 12 _Drosophila_ species. . . . . . . . . .|66|
|4.3|A comparison between two genomic regions with different selection rates _ω_. . . . . . . . .|66|
|4.4|Unusual patterns of substitution<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|67|
|4.5|Increase in power to detect small constrained elements . . . . . . . . . . . . . . . . . . . .|68|
|4.6|HOXB5 conservation across mammalian species.<br>. . . . . . . . . . . . . . . . . . . . . . .|69|
|4.7|Modeling mutations using rate matrices. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|69|
|4.8|Measuring genome–wide excess constraint. . . . . . . . . . . . . . . . . . . . . . . . . . . .|70|
|4.9|Detecting functional elements from their evolutionary signature. **A** Distribution of con-<br>straint for the whole genome against ancestral repeats (background). **B**Difference between<br>whole genome and background constraint. **C** Discovery of functional elements from excess<br>constraint. Novel elements are shown in red. **D** Enrichment of elements for regions of<br>excess constraint. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|71|
|4.10|Coverage depth across different sets of elements.<br>. . . . . . . . . . . . . . . . . . . . . . .|72|
|4.11|Different mutation patterns in protein–coding and non–protein–coding regions. . . . . . .|72|
|4.12|Evolutionary signatures of protein-coding genes . . . . . . . . . . . . . . . . . . . . . . . .|73|
|4.13|RNA with secondary stem–loop structure<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|74|
|4.14|Silent point mutations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|75|
|4.15|Protein-coding vs. non-protein-coding conserved regions . . . . . . . . . . . . . . . . . . .|76|
|4.16|Reading frame conservation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|77|
|4.17|Rejected open reading frame. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|78|
|4.18|Null and alternate model rate matrices.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|79|
|4.19|Probability that a region is protein-coding . . . . . . . . . . . . . . . . . . . . . . . . . . .|80|
|4.20|Prediction of new genes and exons using evolutionary signatures. . . . . . . . . . . . . . .|81|
|4.21|OPRL1 neurotransmitter: a novel translational read–through candidate. . . . . . . . . . .|82|
|4.22|Stop codon suppression interpretations.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|83|
|4.23|Z–curve for _Caki_. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|83|
|4.24|miRNA hairpin structure. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|84|
|4.25|miRNA characteristic conservation pattern. . . . . . . . . . . . . . . . . . . . . . . . . . .|84|
|4.26|Novel miRNA Evidence 1. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|85|
|4.27|Novel miRNA Evidence 2. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|85|


63

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation

|4.28 miRNA detection decision tree. . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .<br>86|
|---|---|
|4.29 CG31044 and CG33311 Transcripts.<br>. . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .<br>87|
|4.30 TAATTA regulatory motif.<br>. . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . .<br>87|


## **4.1 Introduction**

In this chapter we will explore the emerging field of comparative genomics, primarily through examples of multiple species genome alignments (work done by the Kellis lab.) One approach to the analysis of genomes is to infer important gene functions through applying an understanding of evolution to search for expected evolutionary patterns. Another approach is to discover evolutionary trends by studying genomes themselves. Taken together, evolutionary insight and large genomic datasets offer great potential for discovery of novel biological phenomena.

A recurring theme of this work is to take a global computational approach to analyzing elements of genes and RNAs encoded in the genome and use it to find interesting new biological phenomena. We can do this by seeing how individual examples “diverge” or differ from the average case. For example, by examining many protein–coding genes, we can identify features representative of that class of loci. We can then come up with highly accurate tests for distinguishing protein–coding from non–protein–coding genes. Often, these computational tests, based on thousands of examples, will be far more definitive than conventional low– throughput wet lab tests. (Such tests can include mass spectrometry to detect protein products, in cases where we want to know if a particular locus is protein coding.)

### **4.1.1 Motivation and Challenge**

As the cost of genome sequencing continues to drop, the availability of sequenced genome data has exploded. However, analysis of the data has not kept up, while there are many interesting biological phenomena lying undiscovered in the endless strings of ATGCs. The goal of comparative genomics is to leverage the vast amounts of information available to look for biological patterns.

As the name suggests, comparative genomics does not focus on one specific set of genomes. The problem with purely focusing on the single genome level is that key evolutionary signatures are missed. Comparative genomics solves this problem by comparing genomes from many species that evolved from a common ancestor. As evolution changes a species’s genome, it leaves behind traces of its presence. We will see later in this chapter that evolution discriminates between portions of a genome on the basis of biological function. By exploiting this correlation between evolutionary fingerprints and the biological role of a genomic subsequence, comparative genomics is able to direct wet lab research to interesting portions of the genome and discover new biological <u>phenomena.</u>

## **_FAQ_**

- **Q:** Why do mutations only accumulate in certain regions of the genome, whereas other regions are conserved?

- **A:** In non-functional regions of DNA, accumulated mutations are kept because they do not disturb the function of the DNA. In functional regions, these mutations can lead to decreased fitness; these mutations are then discarded from the species by natural selection.

We can glean much information about evolution through studying genomics, and, similarly, we can learn about the genome through studying evolution. For example, from the principle of “survival of the fittest,” we can compare related species to discover which portions of the genome are functional elements. The evolutionary process introduces mutations into any genome. In non-functional regions of DNA, accumulated mutations are kept because they do not disturb the function of the DNA. However, in functional regions, accumulated mutations often lead to decreased fitness. Thus, these fitness-decreasing mutations are not likely to perpetuate to future generations. As time progresses, evolutionarily unfit organisms are likely to

64

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation

not survive and their genes thin out. By comparing surviving species’ genomes with their ancestors’ genomes, we can see which portions constitute functional elements and which constitute “junk DNA.”

To date various important biological markers and phenomena have been discovered through comparative genomics methods. For example, CRISPRs (Clustered Regularly Interspaced Short Palindromic Repeats), found in bacteria and archaea, were first discovered through comparative genomics. Follow–up experiments revealed that they provide adaptive immunity to plasmids and phages. Another example, which we will look at later in this chapter, is the phenomenon of stop–codon read–through, where stop codons are occasionally ignored during the process of translation phase of protein biosynthesis. Without comparative genomics to guide them, experimentalists might have ignored both of these features for many years.

Without a system for interpreting and identifying important features in genomes, all of the DNA sequences on earth are just a meaningless sea of data. However, we cannot ignore the importance of both computer science and biology in comparative genomics. Without knowledge of biology, one might miss the signatures of synonymous substitutions or frame shift mutations. On the other hand, ignoring computational approaches would lead to an inability to parse ever larger datasets emerging from sequencing centers. Comparative genomics require rare multidisciplinary skills and insight.

This is a particularly exciting time to enter the field of comparative genomics, because the field is mature enough that there are tools and data available to make discoveries. But it is young enough that important findings will likely continue to be made for many years.

### **4.1.2 Importance of many closely–related genomes**

In order to resolve significant biological features we need both sufficient similarity to enable comparison and sufficient divergence to identify signatures of change over evolutionary time. This is difficult to achieve in a pairwise comparison. We improve the resolution of our analysis by extending analysis to many genomes simultaneously with some clusters of similar organisms and some dissimilar organisms. A simple analogy is one of observing an orchestra. If you place a single microphone, it will be difficult to decipher the signal coming from the entire system, because it will be overwhelmed by the local noise from the single point of observation, the nearest instrument. If you place many microphones distributed across the orchestra at reasonable distances, then you get a much better perspective not only on the overall signal, but also on the structure of the local noise. Similarly, by sequencing many genomes across the tree of life we are able to distinguish the biological signals of functional elements from the noise of neutral mutations. This is because nature selects for conservation of functional elements across large phylogenetic distances while constantly introducing noise through mutagenic processes operating at shorter time scales.

In this chapter, we will assume that we already have a complete genome–wide alignment of multiple closely–related species, spanning both coding and non–coding regions. In practice, constructing complete genome assemblies and whole–genome alignments is a very challenging problem; that will be the topic of the next chapter.

## **_FAQ_**

- **Q:** Why is there more resolving power when the evolutionary distance or branch length between species increases?

- **A:** If we are comparing two species like human and chimp that are very close to each other, we expect to see little to no mutations. This gives us little discriminative power because we see no difference between the number of mutations in functional elements vs. the number of mutations in non-functional elements. However, as we increase the evolutionary time between species, we expect to see more mutations, but what we actually see are a notable decrease in the observed number of mutations in certain regions of the genome. We can conclude that these regions are functional regions. Therefore, our confidence in perceived functional elements increases as branch length increases.

65

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation

## **_FAQ_**

- **Q:** Why is it better to have many closely related species for the same branch length rather than one distantly related species?

- **A:** As branch length increases between distantly related species, even functional elements are not conserved. Furthermore, reliably aligning genes from distantly related relatives of the same species is difficult if not impossible using current technology such as BLAST.

### **4.1.3 Comparative genomics and evolutionary signatures**

Given a genome-wide alignment, we can subsequently analyze the level of conservation of functional elements in each of the genomes considered. Using the UCSC genome browser, one may see a level of conservation for every gene in the human genome derived from aligning the genomes of many other species. In Figure 4.1 below, we see a DNA sequence represented on the x–axis, while each “row” represents a different species. The y–axis within each row represents the amount of conservation for that species in that part of the chromosome (though other species that are not shown were also used to calculate conservation). Higher bars correspond with greater conservation.

From this figure, we can see that there are blocks of conservation separated by regions that are not conserved. The 12 exons (highlighted by red rectangles) are mostly conserved across species, but sometimes, certain exons are missing; for example, zebrafish is missing exon 9. However, we also see that there is a spike in some species (as circled in red) that do not correspond to a known protein coding gene. This tells us that some intronic regions have also been evolutionarily conserved, since DNA regions that do not code for proteins can still be important as functional elements, such as RNA, microRNA, and regulatory motifs. By observing how regions are conserved, instead of just looking at the amount of conservation, we can observe ‘evolutionary signatures’ of conservation for different functional elements.

The pattern of mutation/insertion/deletion can help us distinguish different types of functional elements in the genome. Different functional elements are under different selective pressures and by considering which selective pressures each element is under, we can develop evolutionary signatures characteristic of each function. For example, we see the difference in evolutionary signatures as exhibited by protein-coding genes as opposed to regulatory motifs...etc.


<!-- Start of picture text -->
© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

Figure 4.1: Exons (boxed in red) are deeply conserved from mammals to fish. Other elements are also strongly conserved, such as the circled peak near the center of the graph. This may be a regulatory element found in mammals but not in aves or fish.

66

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation

## **_FAQ_**

- **Q:** Given an alignment of genes from multiple species, what can you measure to determine the level of conservation of a specific gene(s)?

- **A:** One simple method is just to look at the alignment score for each gene. If one wants to distinguish between highly conserved protein coding segments from non-protein coding segments, one may also look at codon conservation. However, in both of these approaches, we have to consider the position of each species being compared in the phylogenetic tree. A pairwise comparison score that is lower between two species separated by a greater distance in the phylogenetic tree than the pairwise score between two closely related species would not necessarily imply lower conservation.

## **4.2 Conservation of genomic sequences**

### **4.2.1 Functional elements in** **_Drosophila_**

In a 2007 paper<sup>1</sup> , Stark et al. identified evolutionary signatures of different functional elements and predicted function using conserved signatures. One important finding is that across evolutionary time, genes tend to remain in a similar location. This is illustrated by Figure 4.2, which shows the result of a multiple alignment on orthologous segments of genomes from twelve _Drosophila_ species. Each genome is represented by a horizontal blue line, where the top line represents the reference sequence. Grey lines connect orthologous functional elements, and it is clear that their <u>positions</u> are <u>generally</u> conserved across the different species.

## **_FAQ_**

- **Q:** Why is it significant that the position of orthologous elements is conserved?

- **A:** The fact that positions are conserved is what allows us to make comparisons across species. Otherwise, we would not be able to align non-coding regions reliably.

Drosophila is a great species to study because, in fact, the separation of fruit flies is greater than that of mammals. This brings us to an interesting side-note, that of which species to select when looking at conservation signatures. You don’t want to have very similar species (such as humans and chimpanzees, which share 98% of the genome), because it would be difficult to distinguish regions that are different from ones that are the same. When comparing species to humans, the right level of conservation to look at is the mammals. Specifically, most research done in this field is done using 29 eutherian mammals (placental mammals, no marsupials or monotremes) to study. Another things to take into account is branch-length differences between two species. Your ideal subjects of study would be a few closely related (short branchlength) species, to avoid problems of interpretation that arise with a long branch-length mutations, such as back-mutations.

### **4.2.2 Rates and patterns of selection**

Now that we have established that there is structure to the evolution of genomic sequences, we can begin analyzing specific features of the conservation. For this section, let us consider genomic data at the level of individual nucleotides. Later on in this chapter we will see that we can also analyze amino acid sequences.

We may estimate the intensity of a constraint of selection _ω_ by making a probabilities model of the substitution rate inferred from genome alignment data. Using a Maximum Likelihood (ML) estimation of _ω_ can provide us with the rate of selection _ω_ as well as the log odds score that the rate is non-natural.

> 1 `http://www.nature.com/nature/journal/v450/n7167/abs/nature06340.html`

67

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation


<!-- Start of picture text -->
© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

Figure 4.2: Comparative identification of functional elements in 12 _Drosophila_ species. Grey lines indicate the alignment of orthologous regions. Color indicates direction of transcription.

One property that this measures that we may consider is the rate of nucleotide substitution in a genome. Figure 4.3 shows two nucleotide sequences from a collection of mammals. One of the sequences is subject to normal rates of change, while the other demonstrates a reduced rate. Hence we may hypothesize that the latter sequence is subject to a greater level of evolutionary constraint, and may represent a more biologically important section of the genome.


<!-- Start of picture text -->
© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

Figure 4.3: A comparison between two genomic regions with different selection rates _ω_ . The sequence on the left demonstrates normal rates of mutation, while the sequence on the right shows a high conservation level, as evidenced by the reduced number of mutations.

We can further detect unusual patterns of selection _π_ by looking at a probabilistic model of a stationary distribution that is different from the background distribution. The ML estimation of _π_ provides us with the Probability Weight Matrix (PWM) for each k-mer in the genome as well as the log odds score for substitutions that are unusual (e.g. one base changing to one and only one other base). As one may see from Figure 4.4, specific letters matter because some bases selectively change to one (or two other bases), and the specific base it changes to may suggest what the function of the sequence may be.

We can increase our detection power of constraint elements by looking at more species, as shown in Figure 4.5 where we see a dramatic increase in the power to detect small constrained elements.

## **4.3 Excess Constraint**

In most regions of the genome where we see conservation across species, we expect there to be at least some amount of _synonymous_ substitution. These are “silent” nucleotide substitutions that modify a codon in such a way that the amino acid it encodes is unchanged. In a 2011 paper<sup>2</sup> , Lindblad–Toh et al. studied

> 2 `http://www.nature.com/nature/journal/v478/n7370/full/nature10530.html`

68

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.4: This sequence displays an unusual substitution rate of substituting C with G and vice versa.

evolutionary constraint in the human genome by doing comparative analysis of 29 mammalian species. They found that among the 29 genomes, the average nucleotide site showed 4.5 substitutions per site.

Given such a high average substitution rate, we do not expect to see perfect conservation across all regions that are conserved. For example, ignoring all other effects, the probability of a 12–mer remaining fixed across all 29 species is less than 10<sup>_−_25</sup> . Thus, regions which are nearly perfectly conserved across multiple species stand out as being unique and worthy of further study. One such region is shown in Figure 4.6.

### **4.3.1 Causes of Excess Constraint**

The question is what evolutionary pressures cause certain regions to be so perfectly conserved? The following were all mentioned in class as possibilities:

- Could it be that there is a special structure of DNA shielding this area from mutation?

- Is there some special error correcting machinery that sits at this spot?

- Can the cell use the methylation state of the two copies of DNA as an error correcting mechanism? This mechanism would rely on the fact that the new copy of DNA is unmethylated, and therefore the DNA replication machinery could check the new copy against the old methylated copy.

- Maybe the next generation can’t survive if this region is mutated?

Another possible explanation is that selection is occurring to conserve specific codons. Some codons are more efficient than others: for example, higher abundant proteins that need rapid translation might select codons that give the most efficient translation rate, while other proteins might select for codons that give less efficient translation.

Still, these regions seem too perfectly conserved to be explained by codon usage alone. What else can explain excess constraint? There must be some degree of accuracy needed at the nucleotide level that keeps these sequences from diverging.

It could be that we are looking at the same region in two species that have only recently diverged or that there is a specific genetic mechanism protecting this area. However, it is more likely that so much conservation is a sign of protein coding regions that simultaneously encode other functional elements. For example, the HOXB5 gene shows obvious excess constraint, and there is evidence that the 5’ end of the HOXB5 ORF encodes both protein and an RNA secondary structure.

69

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.5: By increasing the number of mammals studied, we see an increase in the constrained k-mers and base pairs that are detectable.

Regions that encode more than one type of functional element are under overlapping selective pressures. There might be pressure in the protein coding space to keep the amino acid sequence corresponding to this region the same, combined with pressure from the RNA space to keep a nucleotide sequence that preserves the RNA’s secondary structure. As a result of these two pressures to keep codons for the same amino acids and to produce the same RNA structure, the region is likely to show much less tolerance for any synonymous substitution patterns.

The process of estimating evolutionary constraint from genomic alignment data across multiple species follows the steps below:

- Count the number of edit operations (i.e. the number of substitutions and/or deletions/insertions)

- Estimate the number of mutations including back-mutations

- Incorporate information about the neighborhood elements of the conserved element by looking at ”conservation windows”

- Estimate the probability of a constrained “hidden state” through using Hidden Markov Models

- Use phylogeny to estimate tree mutation rate (i.e. reject substitutions that should occur along the tree)

- Allow different portions of the tree to have different mutation rates

### **4.3.2 Modeling Excess Constraint**

To better study region of excess constraint, we develop mathematical models to systematically measure the amount of synonymous and non-synonymous conservation of different regions. We will measure two rates: codon and nucleotide conservation.

To represent the null model, we can build rate matrices (4 _×_ 4 in the nucleotide case and 64 _×_ 64 for the codon case) that give the rates of substitutions between either codons or nucleotides for a unit time. We estimate the rates in the null model by looking at a ton of data and estimating the probabilities of each type of substitution. See Figure 4.18a in 4.5.2 for an example of a null matrix for the codon case.

- _λs_ : the rate of synonymous substitutions

70

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.6: Many genomic regions, such as HOXB5, show more conservation than we would expect in normal conserved coding regions. Among the 29 species under study, all but 7 of them had the exact same nucleotide sequence. The green areas are areas that have undergone evolutionary mutations.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information,see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.7: We can model mutations using rate matrices, as shown here for nucleotide substitutions on the left and codon substitutions on the right. In each matrix, the cell in the _m_ th row and _n_ th column represents the likelihood that the _m_ th symbol will mutate into the _n_ th symbol. The darker the color, the less likely the mutation.

• _λn_ : the rate of nonsynonymous substitutions

For example, if _λs_ = 0 _._ 5, then the rate of synonymous substitutions is half of what is expected from the null model in that region. We can then evaluate the statistical significance of the rate estimates we obtain, and find regions where the rate of substitution is much lower than expected.

Using a null model here helps us account for biases in alignment coverage of certain codons and also accounts for the possibility of codon degeneracy, in which case we would expect to see a much higher rate of substitutions. We will learn how to combine such models with phylogenic methods when we talk about phylogenic trees and evolution later on in the course.

Applying this model shows that the sequences in the first translated codons, cassette exons (exons that are present in one mRNA transcript but absent in an isoform of the transcript), and alternatively spliced regions have especially low rates of synonymous substitutions.

### **4.3.3 Excess Constraint in the Human Genome**

In this section, we will examine the problem of determining the total proportion of the human genome under excess constraint. In particular, we will revisit the work of Lindblad–Toh et al. (2011), which compared 29 mammalian genomes. They measured conservation levels throughout the genome by applying the process described in the previous section to 50–mers. By considering only 50–mers which were part of ancestral repeats, it is possible to determine a background level of conservation. We can imagine that the intensities of conservation among the 50–mers are distributed according to a hidden probability distribution, as illustrated in Figure 4.8. In the figure, the background curve represents the distribution of constraint in the absence

71

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation

of special mechanisms for excess constraint, as determined by looking at ancestral repeats, while the signal (foreground) curve represents the actual distribution of the genome. The signal curve has more conservation overall due to the purifying effects of natural selection.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.8: Measuring genome–wide excess constraint. See accompanying text for explanation.

We may wish to investigate specific regions of the genome which are under excess constraint by setting a threshold level of conservation and examining regions which are more conserved. In the illustration, this corresponds to considering all 50–mers which fall to the right of one of the orange lines. We see that while this method does indeed give us regions under excess constraint, it also gives us false positives. This is because even in the absence of purifying selection and other effects, certain regions will be heavily conserved, simply due to random chance. Setting the threshold higher, such as by using the dotted orange line as our threshold, reduces the proportion of false positives (FP) to true positives (TP), while also lowering the number of true positives detected, thus trading higher specificity for lower sensitivity.

However, not all hope is lost. It is possible to empirically measure both the background (BG) and foreground (FG) signal curves, as described above. Once that is done, the area of the region between them, which is shaded in gray in Figure 4.8, can be determined by integration. This area represents the proportion of the genome which is under excess constraint. Because the curves overlap, we cannot detect all conserved elements but we can estimate the total amount of excess constraint. This number of estimated constraint turns out to be about 5% of the human genome, depending on how large a window is used. Those regions are likely to all be functional, but since about 1.5% of the human genome is protein–coding, we can infer that the remaining 3.5% consists of functional, non–coding elements, most of which probably play regulatory roles.

We have seen that evolutionary constraint over the whole genome can be estimated by evaluating genomic constraint against a background distribution. Lindblad-Toh et al. (2011) compare genome conservation across 29 mammals against a background calculated from ancestral repeat elements to find regions with excess constraint (Figure 4.9A and B). Annotation of evolutionarily constrained bases reveals that the majority of discovered regions are intergenic and intronic and demonstrates that going from four (HMRD) to 29 mammalian genomes increases the power of this analysis primarily in non-coding regions (Figure 4.9C). The most constrained regions in the genome are coding regions (Figure 4.9D).

As shown in Figure 4.9, the increase from HMRD to a 29 genome alignment vastly improves the power

72

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.9: Detecting functional elements from their evolutionary signature. **A** Distribution of constraint for the whole genome against ancestral repeats (background). **B** Difference between whole genome and background constraint. **C** Discovery of functional elements from excess constraint. Novel elements are shown in red. **D** Enrichment of elements for regions of excess constraint.

of this analysis. However, while the amount of intergenic elements detected increased significantly, detection is still limited by the fact that non-functional elements have much lower species coverage depth in multiple alignments than functional regions (Figure 4.10). For example, ancestral repeats (AR, _µ_ = 11 _._ 4) have a much lower average coverage depth than exons ( _µ_ = 20 _._ 9). On one hand, this shows evidence of selection against insertions and deletions in functional elements, which are not examined in the analysis of base constraint. On the other, it also complicates the analysis of evolutionary constraint, as such work must then handle varying coverage across the genome.

### **4.3.4 Examples of Excess Constraint**

Examples of excess constraint have been found in the following cases:

- Most Hox genes show overlapping constraint regions. In particular, as mentioned above the first 50 amino acids of HOXB5 are almost completely conserved. In addition, HOXA2 shows overlapping regulatory modules. These two loci encode developmental enhancers, providing a mechanism for tissue specific expression.

- ADAR: the main regulator of mRNA editing, has a splice variant where a low synonymous substitution rate was found at a resolution of 9 codons.

- BRCA1: Hurst and Pal (2001) found a low rate of synonymous substitutions in certain regions of BRCA1, the main gene involved in breast cancer. They hypothesized that purifying selection is occurring in these regions. (This claim was refuted by Schmid and Yang (2008) who claim this phenomenon is the artifact of a sliding window analysis).

- THRA/NR1D1: these genes, also involved in breast cancer, are part of a dual coding region that codes for both genes and is highly conserved.

73

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.10: Coverage depth across different sets of elements.

- SEPHS2: has a hairpin involved in selenocysteine recoding. Because this region must select codons to both conserve the protein’s amino acid sequence and the nucleotides to keep the same RNA secondary structure, it shows excess constraint.

### **4.3.5 Measuring constraint at individual nucleotides**

By measuring evolutionary constraint at individual nucleotides instead of blocks of the sequence, we may find individual transcription factor binding sites, position-specific bias within motif instances, and reveal motif consensus among most species. Specifically, we can detect SNPs that disrupt conserved regulatory motifs and determine the level of evolution by looking at every nucleotide in the gene. By looking at nucleotides individually, we can find SNPs that are important in the function of a specific sequence.

## **4.4 Diversity of evolutionary signatures: An Overview of Selection Patterns**

Independently of the substitution rate, we may also consider the pattern of substitutions in a particular nucleotide subsequence. Consider a sequence of nucleotides which encodes a protein. Due to tRNA wobble, a mutation in the third nucleotide of a codon is less likely to affect the final protein than a mutation in the other positions. Hence we expect to see a pattern of increased substitutions on the third position when looking at protein–coding subsequences of the genome. This is indeed verified experimentally, as shown in Figure 4.11.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.11: Different mutation patterns in protein–coding and non–protein–coding regions. Asterisks indicate that the nucleotide was conserved across all species. Note that within the protein–coding exon, nucelotides 1 and 2 of each codon tend to be conserved, while codon 3 is allowed to vary more, which is consistent with the phenomenon of wobble.

74

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation

## **_FAQ_**

- **Q:** In Figure 4.11, we also see nucleotide substitutions in groups of three or sixes. Why is this the case?

- **A:** Insertions and deletions in groups of threes and sixes also contribute to preserving the reading frame. If all the nucleotides are deleted in one codon, the rest of the codons are unaffected during amino acid translation. However, if we delete a number of nucleotides that is not a multiple of three (i.e. we only delete part of some codon), then the translation of the rest of the codons become nonsensical since the reading frame has been shifted.

In Figure 4.12, we can see one more feature of protein-coding genes. The boundaries of conservation are very distinct and they lie near splice sites. Periodic mutations (in multiples of three) begin to occur after the splice site boundary.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.12: In addition to reading frame conservation and substitutions every third nucleotide, we also see sharp conservation boundaries that pinpoint splice sites.

As we can see with detecting protein-coding genes, it is not only important to consider the substitution rate but also the pattern of substitutions. By observing how regions are conserved, instead of just looking at the amount of conservation, we can observe ‘evolutionary signatures’ of conservation for different functional elements.

### **4.4.1 Selective Pressures On Different Functional Elements**

Different functional elements have different selective pressures (due to their structure and other characteristics); some changes (insertions, deletions, or mutations) that can be extremely harmful to one functional element may be innocuous to another. By figuring out what the “signatures” are for different elements, we can more accurately annotate a region by observing the patterns of conservation it shows.

Such a pattern is called an **evolutionary signature** : a pattern of change that is tolerated within elements that still preserve their function. An evolutionary signature is different from the degree of conservation in that you tolerate mutation, but only specific types of mutations in specific places. Evolutionary signatures arise because evolution and natural selection are acting on different levels in certain functional elements. For instance, in a protein-coding gene evolution is acting on the level of amino acids, and so natural selection willl not filter out nucleotide changes which do not affect the amino acid sequence. Whereas a structural RNA will have pressure to preserve nucleotide pairs, but not necessarily individual nucleotides.

75

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation

Importantly, the pattern of conservation has a distinct phylogenetic structure. More similar species (mammals) group together with shared conserved domains that fish lack, suggesting a mammalian specific innovation, perhaps for regulatory elements not shared by fish. Meanwhile, some features are globally conserved, suggesting a universal significance, such as protein coding. Initial approximate annotation of protein coding regions in the human genome was possible using the simple heuristic that if it was conserved from human to fish it likely served as a protein coding region.

An interesting idea for a final project would be to map divergences in the multiple alignment and call these events “births” of new coding elements. By focusing on a particular element (say microRNAs) one could identify periods of innovation and isolate portions of a phylogenetic tree enriched for certain classes of these elements.

The rest of the chapter will focus on quantifying the degree to which a sequence follows a given pattern. Kellis compared the process of evolution to exploring a fitness landscape, with the fitness score of a particular sequence constrained by the function it encodes. For example, protein coding genes are constrained by selection on the translated product, so synonymous substitutions in the third base pair of a codon are tolerated.

Below is a summary of the expected patterns followed by various functional elements:

- Protein–coding genes exhibit particular frequencies of codon substitution as well as reading frame conservation. This makes sense because the significance of the genes is the proteins they code for; therefore, changes that result in the same or similar amino acids can be easily tolerated, while a tiny change that drastically changes the resulting protein can be considered disastrous. In addition to the error correction of the mismatch repair system and DNA polymerase itself, the redundancy of the genetic code provides an additional level of intrinsic error correction/tolerance.

- Structural RNA is selected based on the secondary sequence of the transcribed RNA, and thus requires compensatory changes. For example, some RNA has a secondary stem–loop structure such that sections of its sequence bind to other sections of its sequence in its “stem”, as shown in figure 4.13.


Courtesy of Sakurambo on wikipedia. Image in the public domain.

Figure 4.13: RNA with secondary stem–loop structure

Imagine that a nucleotide (A) and its partner (T) bind to each other in the stem, and then (A) mutates to a (C). This would ruin the secondary structure of the RNA. To correct this, either the (C) would mutate back to an (A), or the (T) would mutate to a (G). Then the (C)-(G) pair would maintain the secondary structure. This is called a compensatory mutation. Therefore, in RNA structures, the amount of change to the secondary structure (e.g. stem–loop) is more important than the amount of change in the primary structure (just the sequence). Understanding the effects of changes in RNA structure requires knowledge of the secondary structure. The likely secondary structure of an RNA can be determined by modeling the stability of many possible conformations and choosing the most likely conformation.

- MicroRNA is a molecule that is ejected from the nucleus into the cytoplasm. Their characteristic trait is that they also have the hairpin (stem–loop) structure illustrated in Figure 4.13, but a section of the stem is complementary to a portion of mRNA. When microRNA binds its complementary sequence to the respective portion of mRNA, it degrades the mRNA. This means that it is a post–transcriptional regulator, since it’s being used to limit the

76

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation

production of a protein (translation) after transcription. MicroRNA is conserved differently than structural RNA. Due to its binding to an mRNA target, the region of binding is much more conserved to maintain target specificity.

- Finally, regulatory motifs are conserved in sequence (to bind particular interacting protein partners) but not necessarily in location. Regulatory motifs can move around since they only need to recruit a factor to a particular region. Small changes (insertions and deletions) that preserve the consensus of the motif are tolerated, as are changes upstream and downstream that move the location of the motif.

When trying to understand the role of conservation in functional class prediction, an important question is how much of observed conservation can be explained by known patterns. Even after accounting for “random” conservation, roughly 60% of non–random conservation in the fly genome was not accounted for — that is, we couldn’t identify it as a protein–coding gene, RNA, microRNA, or regulatory motif. The fact that they remain conserved however suggests a functional role. That so much conserved sequence remains poorly understood underscores that many exciting questions remain to be answered. One final project for 6.047 in the past was using clustering (unsupervised learning) to account for the other conservation. It developed into an M.Eng project, and some clusters were identified, but the function of these clusters was, and is, still unclear. It’s an open problem!

## **4.5 Protein–Coding Signatures**

In slide 12, we see three examples of conservation: an intronic sequence with poor conservation, a coding region with high conservation, and a non–coding region with high conservation, meaning it is probably a functional element. As we saw at the beginning of this section, the important characteristic of protein– coding regions to remember is that codons (triples of nucleotides) code for amino acids, which make up proteins. This results in the evolutionary signature of protein–coding regions, as shown in slide 13: (i) reading–frame conservation and (ii) codon–substitution patterns. The intuition for this signature is relatively straightforward.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.14: Some point mutations to DNA sequence do not change protein translation

Firstly, reading frame conservation makes sense, since an insertion or deletion of one or two nucleotides will “shift” how all the following codons are read. However, if an insertion or deletion happens in a multiple of 3, the other codons will still be read in the same way, so this is a less significant change. Secondly, it makes sense that some mutations are less harmful than others, since different triplets can code for the same amino acids (a conservative substitution, as evident from the matrix below), and even mutations that result in a different amino acid may be evolutionarily neutral if the substitutions occur with similar amino acids in a domain of the protein where exact amino acid properties are not required. These distinctive patterns allow us to “color” the genome and clearly see where the exons are, as shown in Figure 4.15.

When using these patterns in distinguishing evolutionary signatures, we have to make sure to consider the ideas below:

77

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.15: By coloring the types of insertions/deletions/substitutions that occur on a sequence, we can see patterns or evolutionary signatures that distinguish a protein-coding conserved region from a non-proteincoding conserved region.

- Quantify the distinctiveness of all 64<sup>2</sup> possible codon substitutions by considering synonymous (frequent in protein-coding sequences) and nonsense (more frequent in non-coding than coding sequences) regions.

- Model the phylogenetic relationship among the species: multiple apparent substitutions may be explained by one evolutionary event.

- Tolerate uncertainty in the input such as unknown ancestral sequences and gaps in alignment (missing data).

- Report the certainty or uncertainty of the result: quantify the confidence that a given alignment is protein-coding using various units such as p-value, bits, decibans...etc.

### **4.5.1 Reading–Frame Conservation (RFC)**

Now that we know about this pattern of conservation in protein coding genes, we can develop methods to determine if a gene is protein-coding or if it is not.

By scoring the pressure to stay in the same reading frame we can quantify how likely a region is to be protein–coding or not. As shown in slide 20, we can do this by having a target sequence (Scer, the genome of _S. cerevisiae_ ), and then aligning a selecting sequence (Spar, _S. paradoxus_ ) to it and calculating what proportion of the time the selected sequence matches the target sequence’s reading frame.

Since we don’t know where the reading frame starts in the selected sequence, we align three times to try all possible offsets:

(Sparf1 _,_ Sparf2 _,_ Sparf3)

From these, we choose the alignment where the selected sequence is most often in sync with the target sequence. For example, we can begin numbering the nucleotides “1, 2, 3...etc.” until we reach a gap that we do not number. Or we can start numbering the nucleotides “2, 3, 1...etc.” where each triplet of “1,2,3” represents a codon.

78

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation

Finally, for the best alignment, we calculate the percentage of nucleotides that are out of frame — if it is above a cutoff, this selected species “votes” that this region is a protein–coding region , and if it is low, this species “votes” that this is an intergenic region. The “votes” are tallied from all the species to sum to the RFC score.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.16: Two alignments showing conservation pattern differences between gene and intergenic sequences. Red boxes represent gaps that shift the coding frame, and gray boxes are non-frame-shifting gaps (in multiples of three). Green regions are conserved, and yellow ones are mutated. Note the pattern of “match, match, mismatch” in the protein-coding sequence that indicates synonymous mutations.

This method is not robust to sequencing error. We can compensate for these errors by using a smaller scanning window and observing local reading frame conservation.

The method was shown to have 99.9% specificity and 99% sensitivity when applied to the yeast genome. When applied to 2000 hypothetical ORFs (open reading frames, or proposed genes)<sup>3</sup> in yeast, it rejected 500 of these putative protein coding genes as not being protein coding.

Similarly, 4000 hypothetical genes in the human genome were rejected by this method. This model created a specific hypothesis (that these DNA sequences were unlikely to code for proteins) that has subsequently been supported with experimental confirmation that the regions do not code for proteins in vivo.<sup>4</sup>

This represents an important step forward for genome annotation, because previously it was difficult to conclude that a DNA sequence was non–coding simply from lack of evidence. By narrowing the focus and creating a new null hypothesis (that the gene in question appears to be a non–coding gene) it became much easier to not only accept coding genes, but to reject non–coding genes with computational support. During the discussion of reading frame conservation in class, we identified an exciting idea for a final project which would be to look for the birth of new functional proteins resulting from frame shift mutations.

### **4.5.2 Codon–Substitution Frequencies (CSFs)**

The second signature of protein coding regions, the codon substitution frequencies, acts on multiple levels of conservation. To explore these frequencies, it is helpful to remember that codon evolution can be modeled

> 3Kellis M, Patterson N, Endrizzi M, Birren B, Lander E. S. 2003. Sequencing and comparison of yeast species to identify genes and regulatory elements. Science. 423: 241–254.

> 4Clamp M et al. 2007. Distinguishing protein–coding and noncoding genes in the human genome. PNAS. 104: 19428–19433.

79

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.17: Red boxes represent frame-shifting gaps, and gaps in multiples of three are uncolored. Conserved and mutated regions are green and yellow, respectively.

by conditional probability distributions (CPDs) — the likelihood of a descendant having a codon _b_ where an ancestor had codon _a_ an amount of time _t_ ago.

The most conservative event is exact maintenance of the codon. A mutation that codes for the same amino acid may be conservative but not totally synonymous, because of species specific codon usage biases. Even mutations that alter the identity of the amino acid might be conservative if they code for amino acids with similar biochemical properties.

We use a CPD in order to capture the net effect of all of these considerations. To calculate these CPDs, we need a “rate” matrix, _Q_ , which measures the exchange rate for a unit time; that is, it indicates how often codon _a_ in species 1 is substituted for codon _b_ in species 2, for a unit branch length. Then, by using _e_<sup>_Qt_</sup> , we can estimate the frequency of substitution at time _t_ .

When the CPD is considered in conjunction with the topology of a network graph representing the evolutionary tree, it has a approximately (2 _L −_ 2) _·_ 64<sup>2</sup> parameters, where _L_ is the number of leaves in the tree (species in the evolutionary phylogeny). This number of parameters is derived from the number of entries in _Q_ and the number of independent branch lengths, _t_ . Estimates of these parameters can be determined by MLE from training data.

The CPD is defined in terms of _e_<sup>_Qt_</sup> as follows:


The intuition, is that as time increases, the probability of substitutions increase, while at the “initial” time ( _t_ = 0), _e_<sup>_Qt_</sup> is the identity matrix, since every codon is guaranteed to be itself. But how do we get the rate matrix?

- _Q_ is “learned” from the sequences, by using Expectation–Maximization, for example. Many known protein-coding sequences are used as training data (or non-coding regions when generating that model).

- Given the parameters of the model, we can use Felsenstein’s algorithm[1] to compute the probability of any alignment, while taking into account phylogeny, given the substitution model (the E–step).

_Likelihood_ ( **_Q_** ) = Pr(Training Data; **_Q_** _, t_ ) (4.2)

- Then, given the alignments and phylogeny, we can choose the parameters (the rate matrix: _Q_ , and branch lengths: _t_ ) that maximize the likelihood of those alignments in the M–step; for example, to estimate Q, we can count the number of times one codon is substituted for another in the alignment. The argument space consists of thousands of possibilities for _Q_ and _t_ . This space is represented by **Q** . _Q_ ˆ is the parameter that maximizes the likelihood:


Other maximization strategies include: expectation maximization, gradient ascent, simulated annealing, spectral decomposition. Branch length, _t_ , can be optimized using the same method simultaneously.

80

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation

## **_FAQ_**

- **Q:** How does the branch length contribute to determining the rate matrix?

- **A:** The branch lengths specify how much “time” passed between any two nodes. The rate matrix describes the relative frequencies of codon substitutions per **unit branch length** .

With two estimated rate matrices, the calculated probabilities of any given alignment is different for _P r_ <u>(</u> _Leaves_ <u>;</u> _<u>Qc,t</u>_ <u>)</u> each matrix. Now, we can compare the likelihood ratio, , that the alignment came from a _P r_ ( _Leaves_ ; _QN ,t_ ) protein-coding region as opposed to coming from a non-protein-coding region.


<!-- Start of picture text -->
(a) Rate matrix QN estimated from (b) Rate matrix Qc estimated from<br>non–coding regions known coding regions.<br><!-- End of picture text -->

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.18: Rate matrices for the null and alternate models. A lighter color means substitution is more likely.

Now that we know how to obtain our model, we note that, given the specific pattern of codon substitution frequencies for protein–coding, we want two models so that we can distinguish between coding and non– coding regions. Figures 4.18a and 4.18b show rate matrices for intergenic and genic regions, respectively. A number of salient features present themselves in the codon substitution matrix (CSM) for genes. Note that the main diagonal element has been removed, because the frequency of a triplet being exchanged for itself will obviously be much higher than any other exchange. Nevertheless,

1. it is immediately obvious that there is a strong diagonal element in the protein coding regions.

2. We also note certain high–scoring off diagonal elements in the coding CSM: these are substitutions that are close in function rather than in sequence, such as 6–fold degenerate codons or very similar amino acids.

3. We also note dark vertical stripes, which indicate these substitutions are especially unlikely. These columns correspond to stop codons, since substitutions to this triplet would significantly alter protein function, and thus are strongly selected against.

On the other hand, in the matrix for intergenic regions, the exchange rates are more uniform. In these regions, what matters is the _mutational proximity_ , i.e. the edit distance or number of changes from one sequence to another. Genetic regions are dictated by _selective proximity_ , or the similarity in amino acid sequence of the protein resulting from the gene.

Now that we have the two rate matrices for the two regions, we can calculate the probabilities that each matrix generated the genomes of the two species. This can be done by using Felsenstein’s algorithm, and adding up the “score” for each pair of corresponding codons in the two species. Finally, we can calculate the likelihood ratio that the alignment came from a coding region to a non–coding region by dividing the two

81

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation

scores — this demonstrates our confidence in our annotation of the sequence. If the ratio is greater than 1, we can guess that it is a coding region, and if it is less than 1, then it is a non–coding region. For example, in Figure 4.16, we are very confident about the respective classifications of each region.

It should be noted, however, that although the “coloring” of the sequences confirms our classifications, the likelihood ratios are calculated independently of the ‘coloring,’ which uses our knowledge of synonymous or conservative substitutions. This further implies that this method automatically infers the genetic code from the pattern of substitutions that occurs, simply by looking at the high scoring substitutions. In species with a different genetic code, the patterns of codon exchange will be different; for example, in Candida albumin, the CTG codes for serine (polar) rather than leucine (hydrophobic), and this can be deduced from the CSMs. However, no knowledge of this is required by the method; instead, we can deduce this _a posteriori_ from the CSM.

In summary, we are able to distinguish between non–coding and coding regions of the genome based on their evolutionary signatures, by creating two separate 64 by 64 _rate matrices_ : one measuring the rate of codon substitutions in coding regions, and the other in non–coding regions. The rate matrix gives the exchange rate of codons or nucleotides over a unit time.

We used the two matrices to calculate two probabilities for any given alignment: the likelihood that it came from a coding region and the likelihood that it came from a non–coding region. Taking the _likelihood ratio_ of these two probabilities gives a measure of confidence that the alignment is protein–coding as demonstrated in Figure 4.19. Using this method we can pick out regions of the genome that evolve according to the protein coding signature.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.19: As we can see in the figure that the likelihood ratio is positive for sequences that are likely to be protein coding and negative for sequences that are not likely to be protein coding.

We will see later how to combine this likelihood ratio approach with phylogenetic methods to find evolutionary patterns of protein coding regions.

However, this method only lets us find regions that are selected at the translational level. The key point is that here we are measuring for only protein coding selection. We will see today how we can look for other conserved functional elements that exhibit their own unique signatures.

### **4.5.3 Classification of** **_Drosophila_ Genome Sequences**

We have seen that using these RFC and CSF metrics allows us to classify exons and introns with extremely high specificity and sensitivity. The classifiers that use these measures to classify sequences can be implemented using a HMM or semi–Markov conditional random field (SMCRF). CRFs allow the integration of diverse features that do not necessarily have a probabilistic nature, whereas HMMs require us to model ev-

82

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation

erything as transition and emission probabilities. CRFs will be discussed in an upcoming lecture. One might wonder why these more complex methods need to be implemented, when the simpler method of checking for conservation of the reading frame worked well. The reason is that in very short regions, insertions and deletions will be very infrequent, even by chance, so there won’t be enough signal to make the distinction between protein–coding and non–protein–coding regions. In the figure below, we see a DNA sequence along the x–axis, with the rows representing an annotated gene, amount of conservation, amount of protein–coding evolutionary signature, and the result of Viterbi decoding using the SMCRF, respectively.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.20: Evolutionary signatures can predict new genes and exons. The star denotes a new exon, which was predicted using the three comparative genomics tests, and later verified using cDNA sequencing.

This is one example of how utilization of the protein–coding signature to classify regions has proven very successful. Identification of regions that had been thought to be genes but that did not have high protein– coding signatures allowed us to strongly reject 414 genes in the fly genome previously classified as CGid–only genes, which led FlyBase curators to delete 222 of them and flag another 73 as uncertain. In addition, there were also definite false negatives, as functional evidence existed for the genes under examination. Finally, in the data, we also see regions with both conversation, as well as a large protein–coding signature, but had not been previously marked as being parts of genes, as in Figure 4.20. Some of these have been experimentally tested and have been show to be parts of new genes or extensions of existing genes. This underscores the utility of computational biology to leverage and direct experimental work.

### **4.5.4 Leaky Stop Codons**

Stop codons (TAA, TAG, TGA in DNA and UAG, UAA, UGA in RNA) typically signal the end of a gene. They clearly reflect translation termination when found in mRNA and release the amino acid chain from the ribosome. However, in some unusual cases, translation is observed beyond the first stop codon. In instances of single read–through, there is a stop codon found within a region with a clear protein–coding signature followed by a second stop–codon a short distance away. An example of this in the human genome is given in Figure 4.21. This suggests that translation continues through the first stop codon. Instances of double read–through, where two stop codons lie within a protein coding region, have also been observed. In these instances of stop codon suppression, the stop codon is found to be highly conserved, suggesting that these skipped stop codons play an important biological role.

Translational read–through is conserved in both flies, which have 350 identified proteins exhibiting stop codon read–through, and humans, which have 4 identified instances of such proteins. They are observed mostly in neuronal proteins in adult brains and brain expressed proteins in Drosophila.

The kelch gene exhibits another example of stop codon suppression at work. The gene encodes two ORFs with a single UGA stop codon between them. Two proteins are translated from this sequence, one from the first ORF and one from the entire sequence. The ratio of the two proteins is regulated in a tissue–specific manner. In the case of the kelch gene, a mutation of the stop codon from UGA to UAA results in a loss of function, suggesting that tRNA suppression is the mechanism behind stop codon suppression.

83

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.21: OPRL1 neurotransmitter: one of the four novel translational read–through candidates in the human genome. Note that the region after the first stop codon exhibits an evolutionary signature similar to that of the coding region before the stop codon, indicating that the stop codon is “suppressed”.

An additional example of stop codon suppression is Caki, a protein active in the regulation of neurotransmitter release in _Drosophila_ . Open reading frames (ORFs) are DNA sequences which contain a start and stop codon. In Caki, reading the gene in the first reading frame (Frame 0) results in significantly more ORFs than reading in Frame 1 or Frame 2 (a 440 ORF excess). Figure 4.22 lists twelve possible interpretations for the ORF excess. However, because the excess is observed only in Frame 0, only the first 4 interpretations are likely:

- Stop–codon readthrough: the stop codon is suppressed when the ribosome pulls in tRNA that pairs incorrectly with the stop codon.

- Recent nonsense: Perhaps some recent nonsense mutation is causing stop codon readthrough.

- A to I editing: Unlike we previously thought, RNA can still be edited after transcription. In some case the A base is changed to an I, which can be read as a G. This could change a TGA stop codon to a TGG, which encodes an amino acid. However, this phenomenon is only found in a couple of cases.

- Selenocysteine, the “21st amino acid”: Sometimes when the TGA codon is read by a certain loop which leads to a specific fold of the RNA, it can be decoded as selenocysteine. However, this only happens in four fly proteins, so can’t explain all of stop codon suppression.

Among these four, three of them (recent nonsense, A to I editing, and selenocysteine) account for only 17 of the cases. Hence, it seems that read–through must be responsible for most if not all of the remaining cases. In addition, biased stop codon usage is observed hence ruling out other processes such as alternative splicing (where RNA exons following transcription are reconnected in multiple ways leading to multiple proteins) or independent ORFs.

Read–through regions can be determined in a single species based on their pattern of codon usage. The Z–curve as shown in Figure 4.23 measures codon usage patterns in a region of DNA. From the figure, one can observe that the read–through region matches the distribution before the regular stop codon. After the second stop however, the region matches regions found after regular stops.

Another suggestion offered in class was the possibility of ribosome slippage, where the ribosome skips some bases during translation. This might cause the ribosome to skip past a stop codon. This event occurs in bacterial and viral genomes, which have a greater pressure to keep their genomes small, and therefore can use this slipping technique to read a single transcript in each different reading frame. However, humans and flies are not under such extreme pressure to keep their genomes small. Additionally, we showed above that the excess we observe beyond the stop codon is frame specific to frame 0, suggesting that ribosome slipping is not responsible.

Cells are stochastic in general and most processes tolerate mistakes at low frequencies. The system isn’t perfect and stop codon leaks happen. However, the following evidence suggests that stop codon read–through is not random but instead subject to regulatory control:

- Perfect conservation of read–through stop codons is observed in 93% of cases, which is much higher than the 24% found in background.

- Increased conservation is observed upstream of the read–through stop codon.

84

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation


Figure 4.22: Various interpretations of stop codon suppression. See text for explanation.


Figure 4.23: Z–curve for _Caki_ . Note that the codon usage in the read through region is similar to that in the region before the first stop codon.

- Stop codon bias is observed. TGAC is the most frequent sequence found at the stop codon in read–

85

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation

through and the least frequent found at normal terminated stop codons. It is known to be a “leaky” stop codon. TAAA is found almost universally only in non–read–through instances.

- Unusually high numbers of GCA repeats observed through read–through stop codons.

- Increased RNA secondary structure is observed following transcription suggesting evolutionarily conserved hairpins.

## **4.6 microRNA (miRNA) Gene Signatures**

One example of functional genomic regions subject to high levels of conservation are sequences encoding microRNAs (miRNAs). miRNAs are RNA molecules that bind to complementary sequences in the 3’ untranslated region of targeted mRNA molecules, causing gene silencing.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.24: The hairpin structure of a microRNA. Note that miRNA* denotes the strand on the opposite side of the hairpin, which has the same sequence as the mRNA molecules that are suppressed by the miRNA.

How do we find evolutionary signatures for miRNA genes and their targets, and can we use these to gain new insights on their biological functions? We will see that this is a challenging task, as miRNAs leave a highly conserved but very subtle evolutionary signal.

### **4.6.1 Computational Challenge**

Predicting the location of miRNA genes and their targets is a computationally challenging problem. We can look for “hairpin” regions, where we find nucleotide sequences that are complementary to each other and predict a hairpin structure. But out of 760,355 miRNA–like hairpins found in the cell, only 60–100 were true miRNAs. So to make any test that will give us regions statistically likely to be miRNAs, we need a test with 99.99% specificity.

Figure 4.25 is an example of the conservation pattern for miRNA genes. You can see the two hairpin structures conserved in the red and blue regions, with a region of low conservation in the middle. This pattern is characteristic of miRNAs.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.25: Characteristic conservation pattern of miRNAs. The number of asterisks below a nucleotide indicates the number of species where it is conserved. The blue and red highly conserved regions represent the complementary strands of the miRNA, as in figure 4.24.

By analyzing evolutionary and structural features specific to miRNA, we can use combinations of these features to pick out regions of miRNAs with _>_ 4,500-fold enrichment compared to random hairpins. The following are examples of features that help pick out miRNAs:

86

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation

- miRNAs bind to highly conserved target motifs in the 3’ UTR

- miRNAs can be found in introns of known genes


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.26: Novel miRNA in intron

- miRNAs have a preference for the positive strand of DNA and for transcription factors

- miRNAs are typically not found in exonic and repetitive elements of the genome (counter-example in Figure 4.29).

- Novel miRNAs may cluster with known miRNAs, especially if they are in the same family or have a common origin


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.27: Novel and Known miRNA clustered.

These features of miRNA-coding regions can be grouped into structural families, enabling classifiers to be built based on known RNAs in each family. Energy considerations for RNA structure can be used to support this classification into families. Within each family, orthologous conservation(genes in different species for same function with common ancestral gene) and paralogous conservation (duplicated genes within same species that evolved to serve different functions) occurs.

|**Evolutionary**|**Structural**|
|---|---|
|Correlation with conservation profile|Hairpin stability (MFE z-score)|
|MFE of the consensus fold|Number of asymmetric loops|
|Structure conservation index|Number of symmetric loops|


We can combine several features into one test by using a decision tree, as illustrated in Figure 4.28. At each node of the tree, a test is applied which determines which branch will be followed next. The tree is traversed starting from the root until a terminal node is reached, at which point the tree will output a classification. A decision tree can be trained using a body of classified genome subsequences, after which it can be used to predict whether new subsequences are miRNAs or not. In addition, many decision trees can be combined into a “random forest,” where several decision trees are trained. When a new nucleotide sequence needs to be classified, each tree votes on whether or not it is an miRNA, and then the votes are aggregated to determine the final classification.

Applying this technique to the fly genome showed 101 hairpins above the 0.95 cutoff, rediscovering 60 of 74 of known miRNAs, predicting 24 novel miRNAs that were experimentally validated, and finding an additional 17 candidates that showed evidence of diverse function.

### **4.6.2 Unusual miRNA Genes**

The following four “surprises” were found when looking at specific miRNA genes:

87

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation


Figure 4.28: A possible decision tree for miRNA detection. The features used in this tree are minimum free energy, conservation profile correlation, structure conservation index, number of loops, and stability.

- Surprise 1 Both strands might be expressed and functional. For instance, in the miR–iab–4 gene, expression of the sense and antisense strands are seen in distinct embryonic domains. Both strands score _>_ 0.95 for miRNA prediction.

- Surprise 2 Some miRNAs might have multiple 5’ ends for a single miRNA arm, giving evidence for an imprecise start site. This could give rise to multiple mature products, each potentially with its own functional targets.

- Surprise 3 High scoring miRNA* regions (the star arm is complementary to the actual miRNA sequence) are very highly expressed, giving rise to regions of the genome that are both highly expressed and contain functional elements.

- Surprise 4 Both miR–10 and miR–10* have been shown to be very important Hox regulators, leading to the prediction that miRNAs could be “master Hox regulators”. Pages 10 and 11 of the first set of lecture 5 slides show the importance of miRNAs that form a network of regulation for different Hox genes.

88

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation

### **4.6.3 Example: Re-examining ’dubious’ protein-coding genes**

Two genes, CG31044 and CG33311 were independently rejected because their conservation patterns did not match those characteristic of a protein evolutionary signatures (see Section 4.5). They were identified as precursor miRNA based on genomic properties and high expression levels (Lin et al.). This is a rare example of miRNA being found in previously exonic sequences and illustrates the challenge of identifying miRNA evolutionary signatures.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 4.29: Existing annotations and transcription levels in ’dubious’ protein-coding regions.

## **4.7 Regulatory Motifs**

Another class of functional element that is highly conserved across many genomes contains _regulatory motifs_ . A regulatory motif is a highly conserved sequence of nucleotides that occurs many times throughout the genome and serves some regulatory function. For instance, these motifs might characterize enhancers, promoters, or other genomic elements.


Figure 4.30: TAATTA is a hexamer that appears as a conserved element throughout the genome in many different functional elements, including here. It is an example of a regulatory motif.

### **4.7.1 Computationally Detecting Regulatory Motifs**

Computational methods have been developed to measure conservation of regulatory motifs across the genome, and to find new unannotated motifs _de novo_ . Known motifs are often found in regions with high conservation, so we can increase our testing power by testing for conservation, and then finding signatures for regulatory motifs.

Evaluating the pattern of conservation for known motifs versus the “null model” of regions without motifs gives the following signature:

|Conservation within:<br>Gal4|(known motif region)|Controls|
|---|---|---|
|All intergenic regions|13%|2%|
|Intergenic: coding|13%: 3%|2%:7%|
|Upstream: downstream|12: 0|1:1|


89

6.047/6.878 Lecture 4: Comparative Genomics I: Genome Annotation

So as we can see, regions with regulatory motifs show a much higher degree of conservation in intergenic regions and upstream of the gene of interest.

To discover novel motifs, we can use the following pipeline:

- Pick a motif “seed” consisting of two groups of three non–degenerate characters with a variable size gap in the middle.

- Use a conservation ratio to rank the seed motifs

- Expand the seed motifs to fill in the bases around the seeds using a hill climbing algorithm.

- Cluster to remove redundancy.

Discovering motifs and performing clustering has led to the discovery of many motif classes, such as tissue specific motifs, function specific motifs, and modules of cooperating motifs.

### **4.7.2 Individual Instances of Regulatory Motifs**

To look for expected motif regions, we can first calculate a _branch–length score_ for a region suspected to be a regulatory motif, and then use this score to give us a confidence level of how likely something is to be a real motif.

The branch length score (BLS) sums evidence for a given motif over branches of a phylogenetic tree. Given the pattern of presence or absence of a motif in each species in the tree, this score evaluates the total branch length of the sub–tree connecting the species that contain the motif. If all species have the motif, the BLS is 100%. Note more distantly related species are given higher scores, since they span a longer evolutionary distance. If a predicted motif has spanned such a long evolutionary time frame, it is likely it is a functional element rather than just a region conserved by random chance.

To create a null model, we can choose control motifs. The null model motifs should be chosen to have the same composition as the original motif, to not be too similar to each other, and to be dissimilar from known motifs. We can get a confidence score by comparing the fraction of motif instances to control motifs at a given BLS score.

## **4.8 Current Research Directions**

## **4.9 Further Reading**

1. For more on constraint calculations and identification, refer to Lindblad-Toh’s et. al.’s “A high-resolution map of human evolutionary constraint using 29 mammals”.

2. For more on translational read–through and evolutionary signature, refer to Lin et. al.’s “Revisiting the protein-coding gene catalog of Drosophila melanogaster using 12 fly genomes”.

## **4.10 Tools and Techniques**

1. For sequence alignment of proteins, see http://mafft.cbrc.jp/alignment/software/.

2. For prediction of genes through frameshifts in prokaryotes, see GeneTack.

## **4.11 Bibliography**

## **Bibliography**

- [1] Joseph Felsenstein. Evolutionary trees from dna sequences: A maximum likelihood approach. _Journal of Molecular Evolution_ , 17:368–376, 1981. 10.1007/BF01734359.

90

## CHAPTER **FIVE**

## GENOME ASSEMBLY AND WHOLE-GENOME ALIGNMENT

Melissa Gymrek, Liz Tsai, Rebecca Taft (2012), Keshav Dhandhania (2012), Joe Vitti (2013), Matt Fox (2014)

### **Figures**

|5.1|We can use evolutionary signatures to find genomic functional elements, and in turn can<br>study mechanisms of evolution by looking at patterns of genomic variation and change.<br>.|91|
|---|---|---|
|5.2|Here is a quick look at a few platforms that can be used to read genomes. . . . . . . . . .|92|
|5.3|Shotgun sequencing involves randomly shearing a genome into small fragments so they can<br>be sequenced, and then computationally reassembling them into a continuous sequence.<br>.|93|
|5.4|Constructing a sequence from read overlap. . . . . . . . . . . . . . . . . . . . . . . . . . .|93|
|5.5|We can visualize the process of merging fragments into contigs by letting the nodes in a<br>graph represent reads and edges represent overlaps. By removing the transitively inferable<br>edges (the pink edges in this image), we are left with chains of reads ordered to form contigs|. 94|
|5.6|Overcollapsed contigs are caused by repetetive regions of the genome which cannot be<br>distinguished from one another during sequencing. Branching patterns of alignment that<br>arise during the process of merging fragments into contigs are a strong indication that one<br>of the regions may be overcollapsed.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|95|
|5.7|In this graph connecting contigs, repeated region X has indegree and outdegree equal to<br>2. The target seqence shown at the top can be inferred from the links in the graph. . . . .|95|
|5.8|Mate pairs help us determine the relative order of contigs in order to link them into into<br>supercontigs.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|96|
|5.9|We derive the multiple alignment consensus sequence by weighted voting at each base. . .|96|
|5.10|Constructing a string graph. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|97|
|5.11|Constructing a string graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|97|
|5.12|Example of string graph undergoing removal of transitive edges.. . . . . . . . . . . . . . .|98|
|5.13|Example of string graph undergoing chain collapsing. . . . . . . . . . . . . . . . . . . . . .|98|
|5.14|_Left:_ Flow resolution concept. _Right:_ Flow resolution example. . . . . . . . . . . . . . . .|99|
|5.15|The Needleman-Wunsch algorithm for alignments of 2 and 3 genomes. . . . . . . . . . . .|101|
|5.16|We can save time when performing a global alignment by first finding all the local align-<br>ments and then chaining them together along the diagonal with restricted dynamic pro-<br>gramming. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|101|
|5.17|Glocal alignment allows for the possibility of duplications, inversion, and translocations. .|102|
|5.18|The steps to run the SLAGAN algorithm are A. Find all the local alignments, B. Build a<br>rough homology map, and C. globally align the consistent parts using the regular LAGAN<br>algorithm<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|103|
|5.19|Using the concepts of glocal alignment, we can discover inversions, translocations, and<br>other homologous relations between different species such as human and mouse. . . . . . .|103|
|5.20|Graph of _S. cerevisae_ and _S. bayanus_ gene correspondence.<br>. . . . . . . . . . . . . . . . .|104|


91

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment

|5.21 Illustration of gene correspondence for _S.cerevisiae_ Chromosome VI (250-300bp).<br>.|. . .<br>104|
|---|---|
|5.22 Dynamic view of a changing gene.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>105|
|5.23 Mechanisms of chromosomal evolution. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>106|
|5.24 Moving further back in evolutionary time for Saccharomyces.<br>. . . . . . . . . . . . .|. . .<br>107|
|5.25 Gene Correspondence for _S.cerevisiae_ chromosomes and _K.waltii_ scaffolds.<br>. . . . .|. . .<br>108|
|5.26 Gene interleaving shown by sister regions in _K.waltii_ and _S.cerevisae_ . . . . . . . . .|. . .<br>108|
|5.27 S-LAGAN results.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>109|
|5.28 S-LAGAN results for IGF locus.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . <br>5.29 S-LAGAN results for IGF locus.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>109<br>. . .<br>109|


92

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment

## **5.1 Introduction**

In the previous chapter, we saw the importance of comparative genomics analysis for discovering functional elements. In “part IV” of this book, we will see how we can use comparative genomics for studying gene evolution across species and individuals. In both cases however, we assumed that we had access to complete and aligned genomes across multiple species.

In this chapter, we will study the challenges of genome assembly and whole-genome alignment that are the foundations of whole-genome comparative genomics methodologies. First, we will study the core algorithmic principles underlying many of the most popular genome assembly methods available today. Second, we will study the problem of whole-genome alignment, which requires understanding mechanisms of genome rearrangement (e.g. segmental duplication and other translocations). The two problems of genome assembly and whole-genome alignment are similar in nature, and we close by discussing some of the parallels between them.


Figure 5.1: We can use evolutionary signatures to find genomic functional elements, and in turn can study mechanisms of evolution by looking at patterns of genomic variation and change.

## **5.2 Genome Assembly I: Overlap-Layout-Consensus Approach**

Many areas of research in computational biology rely on the availability of complete whole-genome sequence data. Yet the process to sequence a whole genome is itself non-trivial and an area of active research. The problem lies in the fact that current genome-sequencing technologies cannot continuously read from one end of a long genome sequence to the other; they can only accurately sequence small sections of base pairs (ranging from 100 to a few thousand, depending on the method), called _reads_ . Therefore, in order to construct a sequence of millions or billions of base pairs (such as the human genome), computational biologists must find ways to combine smaller reads into larger, continuous DNA sequences. FIrst, we will examine aspects of the experiemental setup for the overlap-layout-consensus approach, and then we will move forward to learning about how to combine reads and learn information from them

### **5.2.1 Setting up the experiment**

The first challenge that must be tackled when setting up this experiment is that we need to start with many copies of each chromosome in order to use this approach. This number is on the order of 10<sup>5</sup> . It is important to note that the way we obtain these copies is very important and will affect our outcomes later on as it many of the comparisons we make will depend on consistent data. The first way that we may think to get this much data is to amplify a given genome. However, amplification does damage which will throw off our algorithms in later steps and cause worse results. Another possible method would be to inbreed the genome to get many copies of each chromosome. If you are looking to get rid of polymorphism, this

93

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment

may be a good technique, but we also lose valuable data from the polymorphic sites when we inbreed. A suggested method for obtaining this data is to use one individual, though the organism would need to be rather large. We could also use techniques such as progeny of one or progeny of two to get as few versions of each chromosome as possible. This will get high sequencing depth on each chromosome, which is the reason we want all chromosomes to be as similar as possible.

Next, let’s look as how we could decide on our read lengths given current technology. Looking at (Figure 5.2), we can see that a cost-benefit analysis must be done to decide which platform to use on a given project. With current technology, we commonly use HiSeq2500 with a read length of about 250, though this is rapidly changing.


Figure 5.2: Here is a quick look at a few platforms that can be used to read genomes.

Finally, let’s look at a few sequences that cause trouble when using platforms with short reads. Sequences with high GC content (e.g. GGCGGCGATC), low GC content (e.g. AAATAATCAA), or low complexity (e.g. ATATATATA) can cause trouble with short reads. This is still an active area of research, but some possible explanations include Polymerase slippage and DNA denaturing too easily or not easily enough.

This section will examine one of the most successful early methods for computationally assembling a genome from a set of DNA reads, called shotgun sequencing (Figure 5.3). Shotgun sequencing involves randomly shearing multiple copies of the same genome into many small fragments, as if the DNA were shot with a shotgun. Typically, the DNA is actually fragmented using either sonication (brief bursts from an ultrasound) or a targeted enzyme designed to cleave the genome at specific sequence motifs. Both of these methods can be tuned to create fragments of varying sizes.

After the DNA has been amplified and fragmented, the technique developed by Frederick Sanger in 1977 called chain-termination sequencing (also called Sanger sequencing) is used to sequence the fragments. In brief, fragments are extended by DNA polymerase until a dideoxynucleotriphosphate is incorporated; these special nucleotides cause the termination of a fragment’s extension. The length of the fragment therefore becomes a proxy for where a given ddNTP was added in the sequence. One can run four separate reactions, each with a different ddNTP (A, G, C, T) and then run out the results on a gel in order to determine the relative ordering of bases. The result is many sequences of bases with corresponding per-base quality scores, indicating the probability that each base was called correctly. The shorter fragments can be fully sequenced, but the longer fragments can only be sequenced at each of their ends since the quality diminishes significantly

94

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 5.3: Shotgun sequencing involves randomly shearing a genome into small fragments so they can be sequenced, and then computationally reassembling them into a continuous sequence.

after about 500-900 base pairs. These paired-end reads are called _mate pairs_ . In the rest of this section, we discuss how to use the reads to construct much longer sequences, up to the size of entire chromosomes.

### **5.2.2 Finding overlapping reads**

To combine the DNA fragments into larger segments, we must find places where two or more reads overlap, i.e. where the beginning sequence of one fragment matches the end sequence of another fragment. For example, given two fragments such as ACGTTGACCGCATTCGCCATA and GACCGCATTCGCCATACGGCATT, we can construct a larger sequence based on the overlap: ACGTTGACCGCATTCGCCATACGGCATT (Figure 5.4).


Figure 5.4: Constructing a sequence from read overlap

One method for finding matching sequences is the Needleman-Wunsch dynamic programming algorithm, which was discussed in chapter 2. The Needleman-Wunsch method is impractical for genome assembly, however, since we would need to perform millions of pairwise-alignments, each taking _O_ ( _n_<sup>2</sup> ) time, in order to construct an entire genome from the DNA fragments.

A better approach is to use the BLAST algorithm (discussed in chapter 3) to hash all the _k_ -mers (unique sequences of length _k_ ) in the reads and find all the locations where two or more reads have one of the _k_ -mers in common. This allows us to achieve _O_ ( _k_<sup>_n_</sup> ) efficiency rather than _O_ ( _n_<sup>2</sup> ) pairwise comparisons. _k_ can be any number smaller than the size of the reads, but varies depending on the desired sensitivity and specificity. By adjusting the read length to span the repetitive regions of the genome, we can correctly resolve these regions

95

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment

and come very close to the ideal of a complete, continuous genome. One popular overlap-layout-consensus assembler called Arachne uses _k_ = 24 [2].

Given the matching _k_ -mers, we can align each of the corresponding reads and discard any matches that are less than 97% similar. We do not require that the reads be identical since we allow for the possibility of sequencing errors and heterozygosity (i.e., a diploid organism like a human may have two different variants at a polymorphic site).

### **5.2.3 Merging reads into contigs**

Using the techniques described above to find overlaps between DNA fragments, we can piece together larger segments of continuous sequences called _contigs_ . One way to visualize this process is to create a graph in which all the nodes represent reads, and the edges represent overlaps between the reads (Figure 5.5). Our graph will have _transitive overlap_ ; that is, some edges will connect disparate nodes that are already connected by intermediate nodes. By removing the transitively inferable overlaps, we can create a chain of reads that have been ordered to form a larger contig. These graph transformations are discussed in greater depth in section 5.3.1 below. In order to get a better understanding of the size of contigs, we calculate something known as _N50_ . Because measures of contig length tend to be highly sensitive to the smallest contig cutoff, N50 is calculated as the length-weighted median. For a human, N50 is usually close to 125 kb.


Figure 5.5: We can visualize the process of merging fragments into contigs by letting the nodes in a graph represent reads and edges represent overlaps. By removing the transitively inferable edges (the pink edges in this image), we are left with chains of reads ordered to form contigs.

In theory, we should be able to use the above approach to create large contigs from our reads as long as we have adequate coverage of the given region. In practice, we often encounter large sections of the genome that are extremely repetitive and as a result are difficult to assemble. For example, it is unclear exactly how to align the following two sequences: ATATATAT and ATATATATAT. Due to the extremely low information content in the sequence pattern, they could overlap in any number of ways. Furthermore, these repetitive regions may appear in multiple locations in the genome, and it is difficult to determine which reads come from which locations. Contigs made up of these ambiguous, repetitive reads are called _overcollapsed contigs_ .

In order to determine which sections are overcollapsed, it is often possible to quantify the depth of coverage of fragments making up each contig. If one contig has significantly more coverage than the others, it is a likely candidate for an overcollapsed region. Additionally, several unique contigs may overlap one contig in the same location, which is another indication that the contig may be overcollapsed (Figure 5.6).

96

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 5.6: Overcollapsed contigs are caused by repetetive regions of the genome which cannot be distinguished from one another during sequencing. Branching patterns of alignment that arise during the process of merging fragments into contigs are a strong indication that one of the regions may be overcollapsed.

After fragments have been assembled into contigs up to the point of a possible repeated section, the result is a graph in which the nodes are contigs, and the edges are links between unique contigs and overcollapsed contigs (Figure 5.7).


<!-- Start of picture text -->
© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

Figure 5.7: In this graph connecting contigs, repeated region X has indegree and outdegree equal to 2. The target seqence shown at the top can be inferred from the links in the graph.

### **5.2.4 Laying out contig graph into scaffolds**

Once our fragments are assembled into contigs and contig graphs, we can use the larger mate pairs to link contigs into _supercontigs_ or _scaffolds_ . Mate pairs are useful both to orient the contigs and to place them in the correct order. If the mate pairs are long enough, they can often span repetitive regions and help resolve the ambiguities described in the previous section (Figure 5.8).

97

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 5.8: Mate pairs help us determine the relative order of contigs in order to link them into into supercontigs.

Unlike contigs, supercontigs may contain some gaps in the sequence due to the fact that the mate pairs connecting the contigs are only sequenced at the ends. Since we generally know how long a given mate pair is we can estimate how many base pairs are missing, but due to the randomness of the cuts in shotgun sequencing, we may not have the data available to fill in the exact sequence. Filling in every single gap can be extremely expensive, so even the most completely assembled genomes usually contain some gaps.

### **5.2.5 Deriving consensus sequence**

The goal of genome assembly is to create one continuous sequence, so after the reads have been aligned into contigs, we need to resolve any differences between them. As mentioned above, some of the overlapping reads may not be identical due to sequencing errors or polymorphism. We can often determine when there has been a sequencing error when one base disagrees with all the other bases aligned to it. Taking into account the quality scores on each of the bases, we can usually resolve these conflicts fairly easily. This method of conflict resolution is called weighted voting (Figure 5.9). Another alternative is to ignore the frequencies of each base and take the maximum quality letter as the consensus. Sometimes, you will want to keep all of the bases that form a polymorphic set because it can be important information. In this case, we would be unable to use these methods to derive a consensus sequence.


Figure 5.9: We derive the multiple alignment consensus sequence by weighted voting at each base.

In some cases, it is not possible to derive a consensus if, for example, the genome is heterozygous and there are equal numbers of two different bases at one location. In this case, the assembler must choose a representative.

## **_Did You Know?_**

Since polymorphism can significantly complicate the assembly of diploid genomes, some researchers induce several generations of inbreeding in the selected species to reduce the amount of heterozygosity before attempting to sequence the genome.

98

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment

In this section, we saw an algorithm to do genome assembly given reads. However, this algorithm works well when the reads are 500 - 900 bases long or more, which is typical of Sanger sequencing. Alternate genome assembly algorithms are required is the reads we get from our sequencing methods are much shorter.

## **5.3 Genome Assembly II: String graph methods**

Shotgun sequencing, which is a more modern and economic method of sequencing, gives reads that around 100 bases in length. The shorter length of the reads results in a lot more repeats of length greater than that of the reads. Hence, we need new and more sophisticated algorithms to do genome assembly correctly.

### **5.3.1 String graph definition and construction**

The idea behind string graph assembly is similar to the graph of reads we saw in section 5.2.2. In short, we are constructing a graph in which the nodes are sequence data and the edges are overlap, and then trying to find the most robust path through all the edges to represent our underlying sequence.

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 5.10: Constructing a string graph.

Starting from the reads we get from Shotgun sequencing, a string graph is constructed by adding an edge for every pair of overlapping reads. Note that the vertices of the graph denote junctions, and the edges correspond to the string of bases. A single node corresponds to each read, and reaching that node while traversing the graph is equivalent to reading all the bases upto the end of the read corresponding to the node. For example, in figure 5.10, we have two overlapping reads A and B and they are the only reads we have. The corresponding string graph has two nodes and two edges. One edge doesn’t have a vertex at its tail end, and has A at its head end. This edge denotes all the bases in read A. The second edge goes from node A to node B, and only denotes the bases in B-A (the part of read B which is not overlapping with A). This way, when we traverse the edges once, we read the entire region exactly once. In particular, notice that we do not traverse the overlap of read A and read B twice.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 5.11: Constructing a string graph

99

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment

There are a couple of subtleties in the string graph (figure 5.11) which need mentioning:

- We have two different colors for nodes since the DNA can be read in two directions. If the overlap is between the reads as is, then the nodes receive same colors. And if the overlap is between a read and the complementary bases of the other read, then they receive different colors.

- Secondly, if A and B overlap, then there is ambiguity in whether we draw an edge from A to B, or from B to A. Such ambuigity needs to be resolved in a consistent manner at junctions caused due to repeats.


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 5.12: Example of string graph undergoing removal of transitive edges.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 5.13: Example of string graph undergoing chain collapsing.

After constructing the string graph from overlapping reads, we:-

- _Remove transitive edges:_ Transitive edges are caused by transitive overlaps, i.e. A overlap B overlaps C in such a way that A overlaps C. There are randomized algorithms which remove transitive edges in O(E) expected runtime. In figure 5.12, you can see the an example of removing transitive edges.

100

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment

- _Collapse chains:_ After removing the transitive edges, the graph we build will have many chains where each node has one incoming edge and one outgoing edge. We collapse all these chains to a single edge. An example of this is shown in figure 5.13.

### **5.3.2 Flows and graph consistency**

After doing everything mentioned above we will get a pretty complex graph, i.e. it will still have a number of junctions due to relatively long repeats in the genome compared to the length of the reads. We will now see how the concepts of flows can be used to deal with repeats.

First, we estimate the weight of each edge by the number of reads we get corresponds to the edge. If we have double the number of reads for some edge than the number of DNAs we sequenced, then it is fair to assume that this region of the genome gets repeated. However, this technique by itself is not accurate enough. Hence sometimes we may make estimates by saying that the weight of some edge is _≥_ 2, and not assign a particular number to it.


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 5.14: _Left:_ Flow resolution concept. _Right:_ Flow resolution example.

We use reasoning from flows in order to resolve such ambiguities. We need to satisfy the flow constraint at every junction, i.e. the total weight of all the incoming edges must equal the total weight of all the outgoing edges. For example, in the figure 5.14 there is a junction with an incoming edge of weight 1, and two outgoing edges of weight _≥_ 0 and _≥_ 1. Hence, we can infer that the weights of the outgoing edges are exactly equal to 0 and 1 respectively. A lot of weights can be inferred this way by iteratively applying this same process throughout the entire graph.

### **5.3.3 Feasible flow**

Once we have the graph and the edge weights, we run a min cost flow algorithm on the graph. Since larger genomes may not a have unique min cost flow, we iteratively do the following:

- Add _ϵ_ penalty to all edges in solution

- Solve flow again - if there is an alternate min cost flow it will now have a smaller cost relative to the previous flow

- Repeat until we find no new edges

101

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment

After doing the above, we will be able to label each edge as one of the following

- _Required:_ edges that were part of all the solutions

- _Unreliable:_ edges that were part of some of the solutions

- _Not required:_ edges that were not part of any solution

### **5.3.4 Dealing with sequencing errors**

There are various sources of errors in the genome sequencing procedure. Errors are generally of two different kinds, local and global.

Local errors include insertions, deletions and mutations. Such local errors are dealt with when we are looking for overlapping reads. That is, while checking whether reads overlap, we check for overlaps while being tolerant towards sequencing errors. Once we have computed overlaps, we can derive a consensus by mechanisms such as removing indels and mutations that are not supported by any other read and are contradicted by at least 2.

Global errors are caused by other mechasisms such as two different sequences combining together before being read, and hence we get a read which is from different places in the genome. Such reads are called chimers. These errors are resolved while looking for a feasible flow in the network. When the edge corresponding to the chimer is in use, the amount of flow going through this edge is smaller compared to the flow capacity. Hence, the edge can be detected and then ignored.

Each step of the algorithm is made as robust and resilient to sequencing errors as possible. And the number of DNAs split and sequenced is decided in a way so that we are able to construct most of the DNA (i.e. fulfill some quality assurance such as 98% or 95%).

### **5.3.5 Resources**

Some popular genome assemblers using String Graphs are listed below

- Euler (Pevzner, 2001/06) : Indexing _→_ deBruijn graphs _→_ picking paths _→_ consensus

- Valvel (Birney, 2010) : Short reads _→_ small genomes _→_ simplification _→_ error correction

- ALLPATHS (Gnerre, 2011) : Short reads _→_ large genomes _→_ jumping data _→_ uncertainty

## **5.4 Whole-Genome Alignment**

Once we have access to whole-genome sequences for several different species, we can attempt to align them in order to infer the path that evolution took to differentiate these species. In this section we discuss some of the methods for performing whole-genome alignments between multiple species.

### **5.4.1 Global, local, and ’glocal’ alignment**

The Needleman-Wunsch algorithm discussed in chapter 2 is the best way to generate an optimal alignment between two or more genome sequences of limited size. At the level of whole genomes, however, the _O_ ( _n_<sup>2</sup> ) time bound is impractical. Furthermore, in order to find an optimal alignment between _k_ different species, the time for the Needleman-Wunsch algorithm is extended to _O_ ( _n_<sup>_k_</sup> ). For genomes that are millions of bases long, this run time is prohibitive (Figure 5.15).

102

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 5.15: The Needleman-Wunsch algorithm for alignments of 2 and 3 genomes.

One alternative is to use an efficient local alignment tool such as BLAST to find all of the local alignments, and then chain them together along the diagonal to form global alignments. This approach can save a significant amount of time, since the process of finding local alignments is very efficient, and then we only need to perform the time-consuming Needleman-Wunsch algorithm in the small rectangles between local alignments (Figure 5.16).


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 5.16: We can save time when performing a global alignment by first finding all the local alignments and then chaining them together along the diagonal with restricted dynamic programming.

Another novel approach to whole genome alignment is to extend the local alignment search to include inversions, duplications and translocations. Then we can chain these elements together using the least-cost transformations between sequences. This approach is commonly called glocal alignment, since it seeks to combine the best of local and global alignment to create the most accurate picture of how genomes evolve over time (Figure 5.17).

### **5.4.2 Lagan: Chaining local alignments**

LAGAN is a popular software toolkit that incorporates many of the above ideas and can be used for local, global, glocal, and multiple alignments between species.

103

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 5.17: Glocal alignment allows for the possibility of duplications, inversion, and translocations.

The regular LAGAN algorithm consists of finding local alignments, chaining local alignments along the diagonal, and then performing restricted dynamic programming to find the optimal path between local alignments.

Multi-LAGAN uses the same approach as regular LAGAN but generalizes it to multiple species alignment. In this algorithm, the user must provide a set of genomes and a corresponding phylogenetic tree. MultiLAGAN performs pairwise alignment guided by the phylogenetic tree. It first compares highly related species, and then iteratively compares more and more distant species.

Shuffle-LAGAN is a glocal alignment tool that finds local alignments, builds a rough homology map, and then globally aligns each of the consistent parts (Figure 5.18). In order to build a homology map, the algorithm chooses the maximum scoring subset of local alignments based on certain gap and transformation penalties, which form a non-decreasing chain in at least one of the two sequences. Unlike regular LAGAN, all possible local alignment sequences are considered as steps in the glocal alignment, since they could represent translocations, inversions and inverted translocations as well as regular untransformed sequences. Once the rough homology map has been built, the algorithm breaks the homologous regions into chunks of local alignments that are roughly along the same continuous path. Finally, the LAGAN algorithm is applied to each chunk to link the local alignments using restricted dynamic programming.

By running Shuffle-LAGAN or other glocal alignment tools, we can discover inversions, translocations, and other homologous relations between different species. By mapping the connections between these rearrangements, we can gain insight into how each species evolved from the common ancestor (Figure 5.19).

## **5.5 Gene-based region alignment**

An alternative way for aligning multiple genomes anchors genomic segments based on the genes that they contain, and uses the correspondence of genes to resolve corresponding regions in each pair of species. A nucleotide-level alignment is then constructed based on previously-described methods in each multiplyconserved region.

Because not all regions have one-to-one correspondence and the sequence is not static, this is more difficult: genes undergo divergence, duplication, and losses and whole genomes undergo rearrangements. To help overcome these challenges, researchers look at the amino-acid similarity of gene pairs across genomes and the locations of genes within each genome.

104

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment


<!-- Start of picture text -->
© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

Figure 5.18: The steps to run the SLAGAN algorithm are A. Find all the local alignments, B. Build a rough homology map, and C. globally align the consistent parts using the regular LAGAN algorithm


Figure 5.19: Using the concepts of glocal alignment, we can discover inversions, translocations, and other homologous relations between different species such as human and mouse.

105

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 5.20: Graph of _S. cerevisae_ and _S. bayanus_ gene correspondence.

Gene correspondence can be represented by a weighted bipartite graph with nodes representing genes with coordinates and edges representing weighted sequence similarity (Figure 5.20). Orthologous relationships are one-to-one matches and paralogous relationships are one-to-many or many-to-many matches. The graph is first simplified by eliminating spurious edges and then edges are selected based on available information such as blocks of conserved gene order and protein sequence similarity.

The Best Unambiguous Subgroups (BUS) algorithm can then be used to resolve the correspondence of genes and regions. BUS extends the concept of best-bidirectional hits and uses iterative refinement with an increasing relative threshold. It uses the complete bipartite graph connectivity with integrated amino acid similarity and gene order information.

## **_Did You Know?_**

A bipartite graph is a graph whose vertices can be split into two disjoint sets U and V such that every edge connects a vertex in U to a vertex in V.


<!-- Start of picture text -->
© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

Figure 5.21: Illustration of gene correspondence for _S.cerevisiae_ Chromosome VI (250-300bp).

106

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment

In the example of a correctly resolved gene correspondence of _S.cerevisiae_ with three other related species, more than 90% of the genes had a one-to-one correspondence and regions and protein families of rapid change were identified.

## **5.6 Mechanisms of Genome Evolution**

Once we have alignments of large genomic regions (or whole genomes) across multiple related species, we can begin to make comparisons in order to infer the evolutionary histories of those regions.

Rates of evolution vary across species and across genomic regions. In _S. cerevisiae_ , for example, 80% of ambiguities are found in 5% of the genome. Telomeres are repetitive DNA sequences at the end of chromosomes which protect the ends of the chromosomes from deterioration. Telomere regions are inherently unstable, tending to undergo rapid structural evolution, and the 80% of variation corresponds to 31 of the 32 telomeric regions. Gene families contained within these regions such as HXT, FLO, COS, PAU, and YRF show significant evolution in number, order, and orientation. Several novel and protein-coding sequences can be found in these regions. Since very few genomic rearrangements are found in _S. cerevisiae_ aside from the telomeric regions, regions of rapid change can be identified by protein family expansions in chromosome ends.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 5.22: Dynamic view of a changing gene.

Geness evolve at different rates. For example as illustrated in Figure 5.22, on one extreme, there is YBR184W in yeast which shows unusually low sequence conservation and exhibits numerous insertions and deletions across species. On the other extreme there is MatA2, which shows perfect amino acid and nucleotide conservation. Mutation rates often also vary by functional classification. For example, mitochondrial ribosomal proteins are less conserved than ribosomal proteins.

107

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment

The fact that some genes evolve more slowly in one species versus another may be due to factors such as longer life cycles. Lack of evolutionary change in specific genes, however, suggests that there are additional biological functions which are responsible for the pressure to conserve the nucleotide sequence. Yeast can switch mating types by switching all their A and _α_ genes and MatA2 is one of the four yeast mating-type genes (MatA2, Mat _α_ 2, MatA1, Mat _α_ 1). Its role could potentially be revealed by nucleotide conservation analysis.

Fast evolving genes can also be biologically meaningful. Mechanisms of rapid protein change include:

- Protein domain creation via stretches of Glutamine (Q) and Asparagine (N) and protein-protein interactions,

- Compensatory frame-shifts which enable the exploration of new reading frames and reading/creation of RNA editing signals,

- Stop codon variations and regulated read-through where gains enable rapid changes and losses may result in new diversity

- Inteins, which are segments of proteins that can remove themselves from a protein and then rejoin the remaining protein, gain from horizontal transfers of post-translationally self-splicing inteins.

We now look at differences in gene content across different species ( _S.cerevisiae_ , _S.paradoxus_ , _S.mikatae_ , and _S.bayanus_ .) A lot can be revealed about gene loss and conversion by observing the positions of paralogs across related species and observing the rates of change of the paralogs. There are 8-10 genes unique to each genome which are involved mostly with metabolism, regulation and silencing, and stress response. In addition, there are changes in gene dosage with both tandem and segment duplications. Protein family expansions are also present with 211 genes with ambiguous correspondence. All in all however, there are few novel genes in the different species.

### **5.6.1 Chromosomal Rearrangements**

These are often mediated by specific mechanisms as illustrated for Saccharomyces in Figure5.23.

[Matt Fox]Fig11 _ChromEvolImageissuperblurryasfarasIcansee.Whereeverthiswasfound, itshouldbereplacedwithahigherqualityversion, orremovedifthatisimpossible._


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 5.23: Mechanisms of chromosomal evolution.

108

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment

Translocations across dissimilar genes often occur across transposable genetic elements (Ty elements in yeast for example). Transposon locations are conserved with recent insertions appearing in old locations and long terminal repeat remnants found in other genomes. They are evolutionarily active however (for example with Ty elements in yeast being recent), and typically appear in only one genome. The evolutionary advantage of such locationally conserved transposons may lie in the possibility of mediating reversible arrangements. Inversions are often flanked by tRNA genes in opposite transcriptional orientation. This may suggest that they originate from recombination between tRNA genes.

## **5.7 Whole Genome Duplication**


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 5.24: Moving further back in evolutionary time for Saccharomyces.

As you trace species further back in evolutionary time, you have the ability to ask different sets of questions. In class, the example used was _K. waltii_ , which dates to about 95 millions years earlier than _S.cerevisiae_ and 80 million years earlier than _S.bayanus_ .

Looking at the dotplot of _S.cerevisiae_ chromosomes and _K.waltii_ scaffolds, a divergence was noted along the diagonal in the middle of the plot, whereas most pairs of conserved region exhibit a dot plot with a clear and straight diagonal. Viewing the segment at a higher magnification (Figure 5.25), it seems that _S.cerevisiae_ sister fragments all map to corresponding _K.waltii_ scaffolds.

Schematically (Figure 5.26) sister regions show gene interleaving. In duplicate mapping of centromeres, sister regions can be recognized based on gene order. This observed gene interleaving provides evidence of complete genome duplication.

## **5.8 Additional figures**

109

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment


<!-- Start of picture text -->
© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

Figure 5.25: Gene Correspondence for _S.cerevisiae_ chromosomes and _K.waltii_ scaffolds.


<!-- Start of picture text -->
© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

Figure 5.26: Gene interleaving shown by sister regions in _K.waltii_ and _S.cerevisae_

## **Bibliography**

- [1] Embl allextron database - cassette exons.

- [2] Batzoglou S et al. Arachne: a whole-genome shotgun assembler. _Genome Res_ , 2002.

- [3] Manolis Kellis. Lecture slides 04: Comparative genomics i. September 21,2010.

- [4] Manolis Kellis. Lecture slides 05.1: Comparative genomics ii. September 23, 2010.

- [5] Manolis Kellis. Lecture slides 05.2: Comparative genomics iii, evolution. September 25,2010.

- [6] Nikolaus Rajewsky Kevin Chen. The evolution of gene regulation by transcription factors and micrornas. _Nature Reviews Genetics_ , 2007.

110

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment


<!-- Start of picture text -->
S-LAGAN RESULTS (TODO: AXIS LABELS/UNITS??)<br><!-- End of picture text -->


Figure 5.27: S-LAGAN results.


<!-- Start of picture text -->
S-LAGAN (IGF REGION)<br>S-LAGAN (IGF REGION)<br><!-- End of picture text -->

Figure 5.28: S-LAGAN results for IGF locus.


Figure 5.29: S-LAGAN results for IGF locus.

   - © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- [7] Douglas Robinson and Lynn Cooley. Examination of the function of two kelch proteins generated by stop codon suppression. _Development_ , 1997.

- [8] Stark. Discovery of functional elements in 12 drosophila genomes using evolutionary signatures. _Nature_ , 2007.

111

6.047/6.878 Lecture 5: Genome Assembly and Whole-Genome Alignment

- [9] Angela Tan. Lecture 15 notes: Comparative genomics i: Genome annotation. November 4, 2009.

112

## CHAPTER **SIX**

BACTERIAL GENOMICS– MOLECULAR EVOLUTION AT THE LEVEL OF ECOSYSTEMS

Guest Lecture by Eric Alm Scribed by Deniz Yorukoglu (2011)

### **Figures**

|6.1|A tree of life displaying rates of gene birth, duplication, loss, and horizontal gene transfer<br>at each branching point. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|113|
|---|---|---|
|6.2|Rates of new gene birth, duplication, loss and horizontal gene transfer during Archean||
||Gene Expansion<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|114|
|6.3|Abundance levels of different bacterial groups in control patients, Crohn’s disease patients<br>and patients with ulcerative colitis. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|115|
|6.4|Gut bacterial abundances plotted through time for the two donors participating in HuGE<br>project.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|116|
|6.5|Description of how to read a horizon plot. . . . . . . . . . . . . . . . . . . . . . . . . . . .|116|
|6.6|Horizon plot of Donor B in HuGE study. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|117|
|6.7|Horizon plot of Donor A in HuGE study.. . . . . . . . . . . . . . . . . . . . . . . . . . . .|118|
|6.8|Day-to-day bacterial abundance correlation matrices of Donor A and Donor B. . . . . . .|118|
|6.9|Rate of horizontal gene transfer between different bacterial groups taken from non-human<br>sites, human sites, same site within human, and different sites within human. . . . . . . .|120|
|6.10|Rate of horizontal gene transfer between bacterial groups sampled from the same continent<br>and from different continents. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|120|
|6.11|Rate of horizontal gene transfer between different human and non-human sites (top right)<br>and the percentage of antiboitic resistance genes among horizonta gene transfers (bottom<br>left). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|121|


## **6.1 Introduction**

With the magnitude and diversity of bacterial populations in human body, human microbiome has many common properties with natural ecosystems researched in environmental biology. As a field with a large number of quantitative problems to tackle, bacterial genomics offers an opportunity for computational biologist to be actively involved in the progress of this research area.

There are approximately 10<sup>14</sup> microbial cells in an average human gut, whereas there are only 10<sup>13</sup> human cells in a human body in total. Furthermore, there are 10<sup>12</sup> external microbial cells living on our skin. From a cell count perspective, this corresponds to 10 times more bacterial cells in our body than our own cells. From a gene count perspective, there are 100 times more genes belonging to the bacteria living in/on us than to our own cells. For this reason, these microbial communities living in our bodies are an integral part of

113

6.047/6.878 Lecture 6: Bacterial Genomics – Molecular Evolution at the Level of Ecosystems

what makes us human and we should research upon these genes that are not directly encoded in our genome, but still have a significant effect on our physiology.

### **6.1.1 Evolution of microbiome research**

Earlier stages of microbiome research were mostly based on data collection and analysis of surveys of bacterial groups present in a particular ecosystem. Apart from collecting data, this type of research also involved sequencing of bacterial genomes and identification of gene markers for determining different bacterial groups present in the sample. The most commonly used marker for this purpose is 16S rRNA gene, which is a section of the prokaryotic DNA that codes for ribosomal RNA. Three main features of 16S gene that makes it a very effective marker for microbiome studies are: (1) its short size ( _∼_ 1500 bases) that makes it cheaper to sequence and analyze, (2) high conservation due to exact folding requirements of the ribosomal RNA it encodes for, and (3) its specificity to prokaryote organisms that allows us to differentiate from contaminant protist, fungal, plant and animal DNAs.

A further direction in early microbial research was inferring rules from generated datasets upon microbial ecosystems. These studies investigated initially generated microbial data and tried to understand rules of microbial abundance in different types of ecosystems and infer networks of bacterial populations regarding their co-occurrence, correlation and causality with respect to one another.

A more recent type of microbial research takes a predictive approach and aims to model the change of bacterial populations in an ecosystem through time making use of differential equations. For example, we can model the rate of change for the population size of a particular bacterial group in human gut as an ordinary differential equation (ODE) and use this model to predict the size of the population at a future time point by integrating over the time interval.

We can further model change of bacterial populations with respect to multiple parameters, such as time and space. When we have enough data to represent microbial populations temporally and spatially, we can model them using partial differential equations (PDEs) for making predictions using multivariate functions.

### **6.1.2 Data generation for microbiome research**

Data generation for microbiome research usually follows the following work-flow: (1) a sample of microbial ecosystem is taken from the particular site being studied (e.g. a patient’s skin or a lake), (2) the DNAs of the bacteria living in the sample are extracted, (3) 16S rDNA genes are sequenced, (4) conserved motifs in some fraction of the 16S gene (DNA barcodes) are clustered into **operational taxonomic units** (OTUs), and (5) a vector of abundance is constructed for all species in the sample. In microbiology, bacteria are classified into OTUs according to their functional properties rather than species, due to the difficulty in applying the conventional species definition to the bacterial world.

In the remainder of the lecture, a series of recent studies that are related to the field of bacterial genomics and human microbiome studies are described.

## **6.2 Study 1: Evolution of life on earth**

This study [2] is inspired from a quote by Max Delbruck: ”Any living cell carries with it the experience of a billion years of experimentation by its ancestors”. In this direction, it is possible to find evidence in the genomes of living organisms for ancient environmental changes with large biological impacts. For instance, the oxygen that most organisms currently use would have been extremely toxic to almost all life on earth before the accumulation of oxygen via oxygenic photosynthesis. It is known that this event happened approximately 2.4 billion years ago and it caused a dramatic transformation of life on earth.

A dynamic programming algorithm was developed in order to infer gene birth, duplication, loss and horizontal gene transfer events given the phylogeny of species and phylogeny of different genes. **Horizontal gene transfer** is the event in which bacteria transfer a portion of their genome to other bacteria from different taxonomic groups.

Figure 6.1 shows an overview of these inferred events in a phylogenetic tree focusing on prokaryote life. In each node, the size of the pie chart represents the amount of genetic change between two branches and each colored slice stands for the rate of a particular genetic modification event. Starting from the root of the

114

6.047/6.878 Lecture 6: Bacterial Genomics – Molecular Evolution at the Level of Ecosystems

tree, we see that almost the entire pie chart is represented by newly born genes represented by red. However, around 2.5 billion years ago green and blue slices become more prevalent, which represent rate of horizontal gene transfer and gene duplication events.


© Lawrence David. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 6.1: A tree of life displaying rates of gene birth, duplication, loss, and horizontal gene transfer at each branching point.

In Figure 6.2, a large spike can be seen during Archean eon representing large amount of genetic change on earth occurring during this particular time period. This study looked for enzymatic activity of genes that were born in this eon different from the genes that were already present. On the right hand side of Figure 6.2, logarithmic enrichment levels of different metabolites are displayed. Most enriched metabolites produced by these genes were discovered to be functional in oxidation reduction and electron transport. Overall, this study suggests that life invented modern electron transport chain around 3.3 billion years ago and around 2.8 billion years ago organisms evolved to use the same proteins that are used for producing oxygen also to breathe oxygen.

## **6.3 Study 2: Pediatric IBD study with Athos Boudvaros**

In some diseases such as Inflammatory Bowel Disease (IBD); if the disease is not diagnosed and monitored closely, the results can be very severe, such as the removal of the patient’s colon. On the other hand, currently existing most reliable diagnosis methods are very invasive (e.g. colonoscopy). An alternative approach for diagnosis can be abundance analysis of the microbial sample taken from the patients’ colon. This study aims to predict the disease state of the subject from bacterial abundances in stool samples taken from the patient.

> 105 samples were collected for this study among the patients of Dr. Athos Boudvaros; some of them

115

6.047/6.878 Lecture 6: Bacterial Genomics – Molecular Evolution at the Level of Ecosystems


Courtesy of Macmillan Publishers Limited. Used with permission. Source: David, Lawrence A., and Eric J. Alm. "Rapid Evolutionary Innovation during an Archaean Genetic Expansion." _Nature_ 469, no. 7328 (2011): 93-96.

Figure 6.2: Rates of new gene birth, duplication, loss and horizontal gene transfer during Archean Gene Expansion

displaying IBD symptoms and others different diseases (control group). In Figure 6.3, each row block represents a set of bacterial groups at a taxonomic level (phylum level at the top and genus level at the bottom) and each column block represents a different patient group: control patients, Crohn’s disease (CD), and ulcerative colitis (UC). The only significant single biomarker was E. Coli, which is not seen in control and CD patients but seen in about a third of the UC patients. There seems to be no other single bacterial group that gives significant classification between the patient groups from these abundance measures.

Since E. Coli abundance is not a clear-cut single bacterial biomarker, using it as a diagnostic tool would yield low accuracy classification. On the other hand, we can take the entire bacterial group abundance distribution and feed them into a random forest and estimate cross-validation accuracy. After the classification method was employed, it was able to tell with 90% accuracy if the patient is diseased or not. This suggests that it is a competitive method with respect to other non-invasive diagnotic approaches which are generally highly specific but not sensitive enough.

One key difference between control and disease groups is the decrease in the diversity of the ecosystem. This suggests that the disease status is not controlled by a single germ but the overall robustness and the resilience of the ecosystem. When diversity in the ecosystem decreases, the patient might start showing disease symptoms.

## **6.4 Study 3: Human Gut Ecology (HuGE) project**

This study aims to identify more than three hundred dietary and environmental factors affecting human microbiome. The factors, which were regularly tracked by an iPhone App, were the food the subject ate, how much they slept, the mood they were in etc. Moreover, stool samples were taken from the subjects every day for a year in order to perform sequence analysis of the bacterial group abundances for a specific day

116

6.047/6.878 Lecture 6: Bacterial Genomics – Molecular Evolution at the Level of Ecosystems


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 6.3: Abundance levels of different bacterial groups in control patients, Crohn’s disease patients and patients with ulcerative colitis.

relevant to a particular environmental factor. The motivation behind carrying out this study is that, it is usually very hard to get a strong signal between bacterial abundances and disease status. Exploring dietary effects on human microbiome might potentially elucidate some of these confounding factors in bacterial abundance analysis. However, this study analyzed dietary and environmental factors on only two subjects’ gut ecosystems; inferring statistically significant correlations with environmental factors would require large cohorts of subjects.

Figure 6.4 shows abundance levels of different bacterial groups in the gut of the two donors throughout the experiment. One key point to notice is that within an individual, the bacterial abundance is very similar through time. However, bacterial group abundances in the gut significantly differ from person to person.

One statistically significant dietary factor that was discovered as a predictive marker for bacterial population abundances is fiber consumption. It was inferred that fiber consumption is highly correlated with the abundance of bacterial groups such as Lachnospiraceae, Bifidobacteria, and Ruminococcaceae. In Donor B, 10g increase in fiber consumption increased the overall abundance of these bacterial groups by 11%.

In Figure 6.6 and Figure 6.7, a horizon plot of the two donors B and A are displayed respectively. A legend to read these horizon plots is given in Figure 6.5. For each bacterial group the abundance-time graph is displayed with different colors for different abundance layers, segments of different layers are collapsed into the height of a single layer displaying only the color with the highest absolute value difference from the normal abundance, and finally the negative peaks are switched to positive peaks preserving their original color.

In Figure 6.6, we see that during the donor’s trip to Thailand, there is a significant change in his gut bacterial ecosystem. A large number of bacterial groups disappear (shown on the lower half of the horizon plot) as soon as the donor starts living in Thailand. And as soon as the donor returns to U.S., the abundance

117

6.047/6.878 Lecture 6: Bacterial Genomics – Molecular Evolution at the Level of Ecosystems

Figures from the David lab removed due to copyright restrictions.

Figure 6.4: Gut bacterial abundances plotted through time for the two donors participating in HuGE project.

Figures from the David lab removed due to copyright restrictions.

Figure 6.5: Description of how to read a horizon plot.

levels of these bacterial groups quickly return back to their normal levels. Moreover, some bacterial groups that are normally considered to be pathogens (first 8 groups shown on top) appears in the donor’s ecosystem almost as soon as the donor moves to Thailand and mostly disappears when he returns back to United States. This indicates that environmental factors (such as location) can cause major changes in our gut ecosystem

118

6.047/6.878 Lecture 6: Bacterial Genomics – Molecular Evolution at the Level of Ecosystems

Figures from the David lab removed due to copyright restrictions.

Figure 6.6: Horizon plot of Donor B in HuGE study.

while the environmental factor is present but can disappear after the factor is removed.

In Figure 6.7, we see that after the donor is infected with salmonella, a significant portion of his gut ecosystem is replaced by other bacterial groups. A large number of bacterial groups permanently disappear during the infection and other bacterial groups replace their ecological niches. In other words, the introduction of a new environmental factor takes the bacterial ecosystem in the donor’s gut from one equilibrium point to a completely different one. Even though the bacterial population mostly consists of salmonella during the infection, before and after the infection the bacterial count stays more or less the same. The scenario that happened here is that salmonella drove some bacterial groups to extinction in the gut and similar bacterial groups took over their empty ecological niches.

In Figure 6.8, p-values are displayed for day-to-day bacterial abundance correlation levels for Donor A and B. In Donor A’s correlation matrix, there is high correlation within the time interval _a_ corresponding to pre-infection and within the time interval _b_ corresponding to post-infection. However, between _a_ and _b_ there is almost no correlation at all. On the other hand, in the correlation matrix of donor B, we see that pre-Thailand and post-Thailand time intervals, _c_ , have high correlation within and between themselves. However, the interval _d_ that correspond to the time period of Donor B’s trip to Thailand, we see relatively little correlation to _c_ . This suggests that the perturbations in the bacterial ecosystem of Donor B wasn’t enough to cause a permanent shift of the abundance equilibrium as in the case with Donor A due to salmonella infection.

119

6.047/6.878 Lecture 6: Bacterial Genomics – Molecular Evolution at the Level of Ecosystems

Figures from the David lab removed due to copyright restrictions.

Figure 6.7: Horizon plot of Donor A in HuGE study.


Courtesy of Lawrence David. Used with permission.

Figure 6.8: Day-to-day bacterial abundance correlation matrices of Donor A and Donor B.

## **6.5 Study 4: Microbiome as the connection between diet and phenotype**

In a study by Mozaffarian et al. [4] more than a hundred thousand patients were analyzed with the goal of discovering the effect of diet and lifestyle choices on long-term weight gain and obesity. This study built a model to predict the patients’ weights based on the types and amounts of food they consumed over a certain period of time. They found out that fast-food type of food (processed meats, potato chips, sugar-sweetened

120

6.047/6.878 Lecture 6: Bacterial Genomics – Molecular Evolution at the Level of Ecosystems

beverages) were were most highly correlated with obesity. On the other hand, consumption level of yogurt was inversely correlated with obesity.

Further experiments with mouse and human cohorts showed that, within both control group and fast-food group, increased consumption of yogurt leads to weight loss. In the experiment with mice, some female mice were given Lactobacillus reuteri (a group of bacteria found in yogurt) and allowed to eat as much regular food or fast-food they wanted to. This resulted in significant weight loss in the group of mice that were given the purified bacterial extract.

An unexpected phenotypical effect of organic yogurt consumption was discovered to be shinier coat of the mice and dogs that were given yogurt as part of their diet. A histological analysis of the skin biopsy of the control and yogurt fed mice proves that the mice that were fed the bacteria in yogurt had hair follicles that are active, leading to active development of healthier and shiny coat and hair.

## **6.6 Study 5: Horizontal Gene Transfer (HGT) between bacterial groups and its effect on antibiotic resistance**

A study by Hehemann et al. [3] discovered a specific gene that digests a type of sulfonated carbohydrate that is only found in seaweed sushi wrappers. This gene is found in the gut microbes of Japanese people but not North Americans. The study concluded that this specific gene has transferred at some point in history from the algae itself to the bacteria living on it and then to the gut microbiome of a Japanese person by horizontal gene transfer. This study also suggests that, even though some bacterial group might live in our gut for our entire lives, they can gain new functionalities throughout our lives by picking up new genes depending on the type of food that we eat.

In this direction, a study in Alm’s Laboratory investigated around 2000 bacterial genomes published in [1] with the aim of detecting genes that are 100% similar but belong to bacteria in different taxonomic groups. Any gene that is exactly the same between different bacterial groups would indicate a horizontal gene transfer event. In this study, around 100000 such instances were discovered.

When looked at specific environments, it was discovered that the bacteria isolated from humans share genes mostly with other bacteria isolated from human sites. If we focus on more specific sites; we see that bacterial genomes isolated from human gut share genes mostly with with other bacteria that are isolated from gut, and bacterial genomes isolated from human skin shared gene mostly with other isolated from human skin. This finding suggests that independent from the phylogeny of the bacterial groups, ecology is the most important factor determining the amount of gene transfer instances between bacterial groups.

In Figure 6.9, we see that between different bacterial groups taken from human that has at least 3% 16S gene distance, there is around 23% chance that they will share an identical gene in their genome. Furthermore, there is more than 40% chance that they share an identical gene if they are sampled from the same site as well.

On the other hand, Figure 6.10 shows that geography is a weak influence on horizontal gene transfer. Bacterial populations sampled from the same continent and different continents had little difference in terms of the amount of horizontal gene transfer detected.

Figure 6.11 shows a color coded matrix of the HGT levels between various human and non-human environments; top-right triangle representing the amount of horizontal gene transfers and the bottom-left triangle showing the percentage of antibiotic resistance (AR) genes among the transferred genes. In the top-right corner, we see that there is a slight excess of HGT instances between human microbiome and bacterial samples taken from farm animals. And when we look at the corresponding percentages of antibiotic resistance genes, we see that more than 60% of the transfers are AR genes. This result shows the direct effect of feeding subtherapeutic antibiotics to livestock on the emergence of antibiotic resistance genes in the bacterial populations living in human gut.

## **6.7 Study 6: Identifying virulence factors in Meningitis**

Bacterial meningitis is a disease that is caused by very diverse bacteria that are able to get into the blood stream and cross the blood-brain barrier. This study aimed to investigate the virulence factors that can turn

121

6.047/6.878 Lecture 6: Bacterial Genomics – Molecular Evolution at the Level of Ecosystems

Figures removed due to copyright restrictions. See similar figures in this journal article: Smillie, Chris S. et al. "Ecology drives a global network of gene exchange connecting the human microbiome." Nature 480, no. 7376 (2011): 241-244.

Figure 6.9: Rate of horizontal gene transfer between different bacterial groups taken from non-human sites, human sites, same site within human, and different sites within human.

Figures removed due to copyright restrictions. See similar figures in this journal article: Smillie, Chris S. et al. "Ecology drives a global network of gene exchange connecting the human microbiome." Nature 480, no. 7376 (2011): 241-244.

Figure 6.10: Rate of horizontal gene transfer between bacterial groups sampled from the same continent and from different continents.

bacteria into a type that can cause meningitis.

The study involved 70 bacterial strains isolated from meningitis patients, comprising 175172 genes in total. About 24000 of these genes had no known function. There could be some genes among these 24000

122

6.047/6.878 Lecture 6: Bacterial Genomics – Molecular Evolution at the Level of Ecosystems


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Smillie, Chris S., et al. "Ecology Drives a Global Network of Gene Exchange Connecting the Human Microbiome." _Nature_ 480, no. 7376 (2011): 241-4.

Figure 6.11: Rate of horizontal gene transfer between different human and non-human sites (top right) and the percentage of antiboitic resistance genes among horizonta gene transfers (bottom left).

that might be leading to meningitis causing bacteria and might be good drug targets. Moreover, 82 genes were discovered to be involved in horizontal gene transfer. 69 of these had known functions and 13 of them belonged to the 24000 genes that we do not have any functional information. Among the genes with known function, some of them were related to AR, detoxification, and also some were related to known virulence factors such as hemalysin that lets the bacteria live in the blood stream and adhesin that helps the bacteria latch onto the vein and potentially cross blood brain barrier.

## **6.8 Q/A**

Q: Do you think after some time Donor A in Study 3 will have its bacterial ecosystem return back to its original pre-infection state?

A: The salmonella infection caused certain niches to be wiped out from the bacterial ecosystem of Donor A which were then filled in by similar type of bacteria and reached to a different ecosystem at a new equilibrium. Since these niches are dominated by the new groups of bacteria, it would not be possible for the previous bacterial groups to replace them without a large-scale change in his gut ecosystem.

Q: Is the death of certain bacterial groups in the gut during salmonella infection caused directly by the infection or is it an immune response to cure the disease?

A: It can be both, but it is very hard to tell from the data in Study 3 since it is only a data point that corresponds to the event that we can observe. A future study that tries to figure out what is happening in our immune system during the infection can be observed by drawing blood from the patients during the infection.

123

6.047/6.878 Lecture 6: Bacterial Genomics – Molecular Evolution at the Level of Ecosystems

Q: Is there a particular connection between an individual’s genome and the dominant bacterial groups in the bacterial ecosystem? Would twins show more similar bacterial ecosystems?

A: Twins in general have similar bacterial ecosystems independent from whether they live together or are separated. Even though this seems to be a genetic factor at first, monozygotic and dizygotic twins have the exact same effect, as well as displaying similarity to their mothers’ bacterial ecosystem. The reason for this is that starting from birth there is a period of time in which the bacterial ecosystem is programmed. The similarity effect between twins is based on this more than genetic factors.

## **6.9 Current research directions**

A further extension to HuGE study could observe mice gut microbiome during a salmonella infection and observe the process of some bacterial groups being driven to extinction and other types of bacteria replacing the ecological niches that are emptied by them. A higher resolution observation of this phenomenon in mice could illuminate how bacterial ecosystems shift from one equilibrium to another.

## **6.10 Further Reading**

- Overview of Human Microbiome Project: `http://commonfund.nih.gov/hmp/overview.aspx`

- Lawrence A. David and Eric J. Alm. (2011). Rapid evolutionary innovation during an Archaean genetic expansion. _Nature_ , 469(7328):93-96.

- A tutorial on 16S rRNA gene and its use in microbiome research: `http://greengenes.lbl.gov/ cgi-bin/JD_Tutorial/nph-Tutorial_2Main2.cgi`

- Dariush Mozaffarian, Tao Hao, Eric B. Rimm, Walter C. Willett, and Frank B. Hu. (2011). Changes in diet and lifestyle and long-term weight gain in women and men. _The New England journal of medicine_ , 364(25):2392-2404.

- JH Hehemann, G Correc, T Barbeyron, W Helbert, M Czjzek, and G Michel. (2010). Transfer of carbohydrate- active enzymes from marine bacteria to japanese gut microbiota. _Nature_ , 464(5):908-12.

- The Human Microbiome Jumpstart Reference Strains Consortium. (2010). A Catalog of Reference Genomes from the Human Microbiome. _Science_ , 328(5981):994-999

## **6.11 Tools and techniques**

## **6.12 What have we learned?**

In this lecture, we learned about the field of bacterial genomics in general and how bacterial ecosystems can be used to verify major environmental changes at early stages of evolution (Study 1), can act as a noninvasive diagnostic tool (Study 2), are temporarily or permanently affected by different environmental and dietary factors (Study 3), can act as the link between diet and phenotype (Study 4), can cause antibiotic resistance genes to be carried between different species’ microbiome through horizontal gene transfer (Study 5), and can be used to identify significant virulence factors in disease states (Study 6).

## **Bibliography**

- [1] The Human Microbiome Jumpstart Reference Strains Consortium. A Catalog of Reference Genomes from the Human Microbiome. _Science_ , 328(5981):994–999, May 2010.

- [2] Lawrence A. David and Eric J. Alm. Rapid evolutionary innovation during an Archaean genetic expansion. _Nature_ , 469(7328):93–96, January 2011.

124

6.047/6.878 Lecture 6: Bacterial Genomics – Molecular Evolution at the Level of Ecosystems

- [3] JH Hehemann, G Correc, T Barbeyron, W Helbert, M Czjzek, and G Michel. Transfer of carbohydrateactive enzymes from marine bacteria to japanese gut microbiota. _Nature_ , 464(5):908–12, 2010 Apr 8.

- [4] Dariush Mozaffarian, Tao Hao, Eric B. Rimm, Walter C. Willett, and Frank B. Hu. Changes in diet and lifestyle and long-term weight gain in women and men. _The New England journal of medicine_ , 364(25):2392–2404, June 2011.

125

6.047/6.878 Lecture 6: Bacterial Genomics – Molecular Evolution at the Level of Ecosystems

126

---

[← Part I](02-part-i.md) · [Up: contents](index.md) · [Part II →](04-part-ii.md)

---
title: Takis exercises Part 01 —
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Takis exercises Part 01 —

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the Dark Ages, Harvard, Dartmouth, and Yale admitted only male students. Assume that, at that time, 80 percent of the sons of Harvard men went to Harvard and the rest went to Yale, 40 percent of the sons of Yale men went to Yale, and the rest split evenly between Harvard and Dartmouth; and of the sons of Dartmouth men, 70 percent went to Dartmouth, 20 percent to Harvard, and 10 percent to Yale. (i) Find the probability that the grandson of a man from Harvard went to Harvard. (ii) Modify the above by assuming that the son of a Harvard man always went to Harvard. Again, find the probability that the grandson of a man from Harvard went to Harvard.

Solution. We first form a Markov chain with state space S = {H, D, Y } and the following transition probability matrix :


Note that the columns and rows are ordered: first H, then D, then Y . Recall: the ij<sup>th</sup> entry of the matrix P<sup>n</sup> gives the probability that the Markov chain starting in state i will be in state j after n steps. Thus, the probability that the grandson of a man from Harvard went to Harvard is the upper-left element of the matrix


It is equal to .7 = .8<sup>2</sup> + .2 × .3 and, of course, one does not need to calculate all elements of P<sup>2</sup> to answer this question.

If all sons of men from Harvard went to Harvard, this would give the following matrix for the new Markov chain with the same set of states:


The upper-left element of P<sup>2</sup> is 1, which is not surprising, because the offspring of Harvard men enter this very institution only.

2.

Consider an experiment of mating rabbits. We watch the evolution of a particular

> 1More or less

> 2Most of them

> 3Some of these exercises are taken verbatim from Grinstead and Snell; some from other standard sources; some are original; and some are mere repetitions of things explained in my lecture notes.

> 4The subject covers the basic theory of Markov chains in discrete time and simple random walks on the integers

> 5Thanks to Andrei Bejan for writing solutions for many of them

1

gene that appears in two types, G or g. A rabbit has a pair of genes, either GG (dominant), Gg (hybrid–the order is irrelevant, so gG is the same as Gg) or gg (recessive). In mating two rabbits, the offspring inherits a gene from each of its parents with equal probability. Thus, if we mate a dominant (GG) with a hybrid (Gg), the offspring is dominant with probability 1/2 or hybrid with probability 1/2. Start with a rabbit of given character (GG, Gg, or gg) and mate it with a hybrid. The offspring produced is again mated with a hybrid, and the process is repeated through a number of generations, always mating with a hybrid.

(i) Write down the transition probabilities of the Markov chain thus defined. (ii) Assume that we start with a hybrid rabbit. Let µn be the probability distribution of the character of the rabbit of the n-th generation. In other words, µn(GG), µn(Gg), µn(gg) are the probabilities that the n-th generation rabbit is GG, Gg, or gg, respectively. Compute µ1, µ2, µ3. Can you do the same for µn for general n?

Solution. (i) The set of states is S = {GG, Gg, gg} with the following transition probabilities:


We can rewrite the transition matrix in the following form:


(ii) The elements from the second row of the matrix P<sup>n</sup> will give us the probabilities for a hybrid to give dominant, hybrid or recessive species in (n − 1)<sup>th</sup> generation in this experiment, respectively (reading this row from left to right). We first find


so that


Actually the probabilities are the same for any i ∈ N. If you obtained this result before 1858 when Gregor Mendel started to breed garden peas in his monastery garden and analysed the offspring of these matings, you would probably be very famous because it definitely looks like a law! This is what Mendel found when he crossed mono-hybrids.

2

In a more general setting, this law is known as Hardy-Weinberg law. As an exercise, show that


Try!

---

[Up: contents](index.md) · [Takis exercises Part 02 — →](02-takis-exercises-part-02.md)

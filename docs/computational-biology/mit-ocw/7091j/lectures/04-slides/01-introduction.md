---
title: Introduction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/04-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/04-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

7.91 / 7.36 / 20.490 / 20.390 / 6.874 / 6.801 / HST.506

C. Burge Lecture #6 Feb 13, 2014

Comparative Genomics

1

Global Alignment of Protein Sequences (NW, SW, PAM, BLOSUM)

- Global sequence alignment (Needleman-Wunch-Sellers)

- Gapped local sequence alignment (Smith-Waterman)

- Substitution matrices for protein comparison

Background: Z&B Chapters 4,5 (esp. pp. 119-125)

2


### DNA Sequence Evolution

Generation **_n-1_** (grandparent)

- 5’ TGGCATGCACCCTGTAAGTCAATATAAATGGCTACGCCTAGCCCATGCGA 3’ |||||||||||||||||||||||||||||||||||||||||||||||||| 3’ ACCGTACGTGGGACATTCAGTTATATTTACCGATGCGGATCGGGTACGCT 5’


Generation **_n_** (parent)

- 5’ TGGCATGCACCCTGTAAGTCAATATAAATGGCTATGCCTAGCCCATGCGA 3’ |||||||||||||||||||||||||||||||||||||||||||||||||| 3’ ACCGTACGTGGGACATTCAGTTATATTTACCGATACGGATCGGGTACGCT 5’

Generation **_n+1_** (child)


- 5’ TGGCATGCACCCTGTAAGTCAATATAAATGGCTATGCCTAGCCCGTGCGA 3’ |||||||||||||||||||||||||||||||||||||||||||||||||| 3’ ACCGTACGTGGGACATTCAGTTATATTTACCGATACGGATCGGGCACGCT 5’

Images of The Simpsons © FOX. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

3

###### Markov Model (aka Markov Chain)

Stochastic Process:

- a random process  or

<u>Classical Definition</u>

- a sequence of Random Variables

A discrete stochastic process X1, X2, X3, … which has the Markov property:

- P(Xn+1 = j | X1=x1, X2=x2, … Xn=xn) = P(Xn+1 = j | Xn=xn )

(for all xi, all j, all n)


###### <u>In words:</u>

A random process which has the property that the future (next state) is conditionally independent of the past given the present (current state)

Andrey Markov, a Russian mathematician (1856 - 1922)

Image is in the public domain.

4

#### Markov Model Example


<!-- Start of picture text -->
Grandpa<br>Simpson<br>Grandma<br>Simpson<br>Past<br>Homer<br>Marge<br>Present<br>Future<br><!-- End of picture text -->

Genotype at the Apolipoprotein locus (alleles A and a) in successive generations of boxed Simpson lineage forms a Markov model

This is because, e.g., Bart’s genotype is conditionally independent of Grandpa Simpson’s genotype given his father Homer’s genotype:

P(Bart = a/a | Grandpa = A/a & Homer = a/a) = P(Bart = a/a | Homer = a/a)


<!-- Start of picture text -->
Bart<br><!-- End of picture text -->

Images of The Simpsons © FOX. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

5

### Review:

### Vector/Matrix Notation for Markov Chains

###### to:

A        C       G       T **Assuming no selection** _PAA PAC PAG PAT_ ⎛ ⎞ _Sn_ = base at generation _n_ ⎜ _PCA PCC PCG PCT_ ⎟ _P_ = ⎜ ⎟ _PGA PGC PGG PGT_ ⎜ ⎜ ⎟ ⎟ _Pij_<sup>=</sup><sup>_P_(</sup> _Sn_ +1 = _j_ | _Sn_<sup>=</sup><sup>_i_)</sup> ⎝ _PTA PTC PTG PTT_ ⎠

> <sup>r</sup> _n q q_  _n_ =( _q A_ , _qC_ , _qG_ , _qT_ ) = vector of prob’s of bases at gen. _n_ r _n_ +1 r _nn_ ++ _kk n n_ +1<sup>r</sup> _n k_ = = _P_ Handy relations: _q q_  _qq P_  _n q q_  _q q_ r  _n_

> What happens after a long time?       i.e. what is lim _q_  _Pn_<sup>=</sup> ?<sup>_r_</sup> _n_ →∞

6

## **PAM matrix derivation**

**Aa,b Ma,b = mutation prob. matrix Ma,b =** Λ **mb Aa,b = observed subs of a,b** Σ **Ai,b mb = mutability of b i fb    = frequency of b** **_Set scale factor_** Λ **_so that_** Λ **= a scaling constant**

Σ **fb Mb,b = 0.99** i.e. chance of mutating is ~ 1% **b**

**_This gives a probability matrix for an evolutionary distance of 1 PAM.  Use matrix multiplication to calculate prob. matrices for other PAM distances, e.g., 20, 40, 60, 120, 250._**

**substitution scores for evolutionary distance d:**

**d sa,b = 2 log2 (Ma,b /fb)              Recall: matrix multiplication**

7

---

[Up: contents](index.md) · [Issues with PAM Series? →](02-issues-with-pam-series.md)

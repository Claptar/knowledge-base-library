---
title: 7.2 Entropy as a measure of unpredictability
source: https://www.stat.berkeley.edu/~aldous/205B/entropy_chapter.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/entropy_chapter.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7.2 Entropy as a measure of unpredictability

**Source:** [`entropy_chapter.pdf`](https://www.stat.berkeley.edu/~aldous/205B/entropy_chapter.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For a probability distribution over numbers – Binomial or Poisson, Normal or Exponential – the mean or standard distribution are examples of “statistics” – numbers that provide partial information about the distribution. Consider instead a probability distribution over an arbitrary finite set _S_ . Simple concrete examples we have in mind for _S_ are

(i) Relative frequencies of given names (Table 7.1)<sup>1</sup> .

(ii) Relative frequencies of letters in the English language (Figure 7.2)

Table 7.1: 2013 U.S. births given names.

|Rank|Male name|Percent of total males|Female name|Percent of total females|
|---|---|---|---|---|
|1|Noah|0.9043%|Sophia|1.1039%|
|2|Liam|0.8999%|Emma|1.0888%|
|3|Jacob|0.8986%|Olivia|0.9562%|
|4|Mason|0.8793%|Isabella|0.9161%|
|5|William|0.8246%|Ava|0.7924%|
|6|Ethan|0.8062%|Mia|0.6844%|


(iii) Relative frequencies of words in the English language.

> 1The extensive such data from the Social security site is an interesting source for student projects.

_7.2. ENTROPY AS A MEASURE OF UNPREDICTABILITY_

105

Figure 7.2: Relative frequencies of letters in the English language (from Wikipedia)


(iv) Relative frequencies of phrases in the English language<sup>2</sup> .

For a probability distribution **p** = ( _ps, s 2 S_ ) on such sets _S_ it does not make sense to talk about _mean_ or _standard deviation_ . But it does make sense to devise statistics that involve only the _unordered_ set of values _{ps}_ , and the particular statistic relevant to this lecture is


which is called the _entropy_ of the probability distribution **p** . This terminology is confusing, patly because “entropy” is often used for what is properly called _entropy rate_ (section 7.4), and partly because of the only indirectly related notion of _entropy_ in statistical physics.

A basic fact is that the uniform distribution on an _n_ -element set has entropy = log _n_ whereas the “degenerate” distribution concentrated at a single element has entropy zero. The entropy statistic serves to place a distribution on the spectrum from degenerate to uniform; entropy is of described as “amount of randomness” but for our purposes is better regarded as a measure of _unpredictability_ . Note that many other statistics serve the same general purpose, as discussed further in Lecture xxx under the phrase diversity statistic.

> 2See the Google Books Ngram Viewer, which has various interesting uses. To see usage of _data_ as singular or plural, compare frequencies of “the data is” and “the data are”.

_CHAPTER 7. CODING AND ENTROPY_

106

A good way to interpret the numerical value of _E_ ( **p** ) is via the “e↵ective number” _N_ e↵ – the number<sup>3</sup> such that the uniform distribution on _N_ e↵ elements has the same statistic. See section xxx for an illustration concerning the changes over time in the diversity of given names (Table 7.1).

**Entropy in physics.** The reader has likely seen a statement of the second law of thermodynamics in a verbal form such as

the total entropy of any isolated thermodynamic system increases over time, approaching a maximum value

and the informal description of entropy as a measure of _disorder_ . When expressed in mathematical terms one can indeed see connections between this physics formulation of _entropy_ and our definition of _E_ ( **p** ), but this connection is not particularly helpful for an introductory treatment of the topic of this lecture.

---

[← 7.1 Introduction](01-7-1-introduction.md) · [Up: contents](index.md) · [7.3 Coding, compression and encryption →](03-7-3-coding-compression-and-encryption.md)

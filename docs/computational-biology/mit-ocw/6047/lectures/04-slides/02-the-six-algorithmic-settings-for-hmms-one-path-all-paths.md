---
title: The six algorithmic settings for HMMs One path All paths
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/04-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The six algorithmic settings for HMMs One path All paths

**Source:** `lectures/04-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1.  Scoring x, one path

P(x,π)

Prob of a path, emissions

3. Viterbi decoding

- π* = argmaxπ P(x,π)

- Most likely path

5. Supervised learning, given π Λ* = argmaxΛ P(x,π|Λ)

6. Unsupervised learning. Λ* = argmaxΛ maxπP(x,π|Λ) Viterbi training, best path

2.  Scoring x, all paths

P(x) = Σπ P(x,π)

Prob of emissions, over all paths

4.  Posterior decoding

- π^ = {πi | πi=argmaxk ΣπP(πi=k|x)}

Path containing the most likely state at any time point.

6.  Unsupervised learning

   - Λ* = argmaxΛ ΣπP(x,π|Λ)

Baum-Welch training, over all paths

13

## **Examples of HMMs**

The dishonest casino The dishonest genome … and many more

14

## **Example: The Dishonest Casino**

##### A casino has two dice:

- Fair die

   - P(1) = P(2) = P(3) = P(5) = P(6) = 1/6

- Loaded die

   - P(1) = P(2) = P(3) = P(4) = P(5) = 1/10 P(6) = 1/2

Casino player switches between fair and loaded die on average once every 20 turns

##### **<u>Game:</u>**

1. You bet $1

2. You roll (always with a fair die)

3. Casino player rolls (maybe with fair die, maybe with loaded die)

4. Highest number wins $2

Slide credit: Serafim Batzoglou

15

## **The dishonest casino model**


<!-- Start of picture text -->
0.05<br>0.95  0.95<br>Hidden<br>Fair  Loaded<br>(model)<br>0.05<br>P(1|Fair) = 1/6  P(1|L) = 1/10<br>P(2|Fair) = 1/6  P(2|L) = 1/10<br>Observed  P(3|Fair) = 1/6  P(3|L) = 1/10<br>P(4|Fair) = 1/6  P(4|L) = 1/10<br>(world)<br>P(5|Fair) = 1/6  P(5|L) = 1/10<br>P(6|Fair) = 1/6  P(6|L) = 1/2<br>Slide credit: Serafim Batzoglou<br><!-- End of picture text -->

16

## **The dishonest genome model**


<!-- Start of picture text -->
0.85<br>0.15  0.95<br>Hidden<br>Virus  “Self”<br>(model)<br>0.05<br>P(A|Virus) = 1/6  P(A|Self) = 1/4<br>Observed  P(T|Virus) = 1/6  P(T|Self) = 1/4<br>P(C|Virus) = 1/3  P(C|Self) = 1/4<br>(world)<br>P(G|Virus) = 1/3  P(G|Self) = 1/4<br>Slide credit: Serafim Batzoglou<br><!-- End of picture text -->

17

## **Examples of HMMs for genome annotation**

|**Application**|**Detection**<br>**of GC-rich**<br>**regions**|**Detection**<br>**of**<br>**conserved**<br>**regions**|**Detection**<br>**of protein-**<br>**coding**<br>**exons**|**Detection**<br>**of protein-**<br>**coding**<br>**conservatio**<br>**n**|**Detection**<br>**of protein-**<br>**coding**<br>**gene**<br>**structures**|**Detection**<br>**of**<br>**chromatin**<br>**states**|
|---|---|---|---|---|---|---|
|**Topology /**<br>**Transitions**|2 states,<br>different<br>nucleotide<br>composition|2 states,<br>different<br>conservation<br>levels|2 states,<br>different tri-<br>nucleotide<br>composition|2 states,<br>different<br>evolutionary<br>signatures|~20 states,<br>different<br>composition/<br>conservation<br>, specific<br>structure|40 states,<br>different<br>chromatin<br>mark<br>combination<br>s|
|**Hidden**<br>**States /**<br>**Annotation**|GC-rich / AT-<br>rich|Conserved /<br>non-<br>conserved|Coding exon<br>/ non-coding<br>(intron or<br>intergenic)|Coding exon<br>/ non-coding<br>(intron or<br>intergenic)|First/last/mid<br>dle coding<br>exon,UTRs,<br>intron1/2/3,<br>intergenic,<br>*(+/- strand)|Enhancer /<br>promoter /<br>transcribed /<br>repressed /<br>repetitive|
|**Emissions /**<br>**Observatio**<br>**ns**|Nucleotides|Level of<br>conservation|Triplets of<br>nucleotides|Nucleotide<br>triplets,<br>conservation<br>levels|Codons,<br>nucleotides,<br>splice sites,<br>start/stop<br>codons|Vector of<br>chromatin<br>mark<br>frequencies<br>18|


## **Running the model:  Probability of a sequence**


<!-- Start of picture text -->
L  L  L  L  L  L  L  L  L  L<br>.95  .95  .95  .95  .95  .95  .95  .95  .95  1<br>1/2  F  F  F  F  F  F  F  F  F  F<br>1/6  1/6  1/6  1/6  1/6  1/6  1/6  1/6  1/6  1/6<br><!-- End of picture text -->


What is the joint probability of observing x and a specific path π: π = Fair, Fair, Fair, Fair, Fair, Fair, Fair, Fair, Fair, Fair and rolls x   =   1   ,   2,     1,     5,     6,      2,     1,     6,     2,      4 Joined probability P(x,π)=P(x|π)P(π)=P(emissions|path)*P(path)

emission      transition       emission     transition         emission p = ½  P(1 | Fair) P(Fairi+1 | Fairi) P(2 | Fair) P(Fair | Fair) … P(4 | Fair) = ½  (1/6)<sup>10</sup>  (0.95)<sup>9</sup>

= 5.2  10<sup>-9</sup>

**Why is p so small?**

Slide credit: Serafim Batzoglou

19

## **Running the model:  Probability of a sequence**


<!-- Start of picture text -->
.95  .95  .95  .95  .95  .95  .95  .95  .95<br>1/2  L  L  L  L  L  L  L  L  L  L  1<br>F  F  F  F  F  F  F  F  F  F<br>1/10  1/10  1/10  1/10  1/2  1/10  1/10  1/2  1/10  1/10<br>What is the likelihood of<br><!-- End of picture text -->

π = Load, Load, Load, Load, Load, Load, Load, Load, Load, Loaded and rolls

x   =     1   ,   2,      1,      5,        6,       2,       1,       6,       2,      4

emission        transition       emission     transition         emission p = ½  P(1 | Load) P(Loadi+1 | Loadi) P(2 | Load) P(Load|Load) … P(4 | Fair) = ½  (1/10)<sup>8</sup>  (1/2)<sup>2</sup> (0.95)<sup>9</sup> = 7.9  10<sup>-10</sup> **Compare the two!**

Slide credit: Serafim Batzoglou

20


<!-- Start of picture text -->
Comparing the two paths<br>.95  .95  .95  .95  .95  .95  .95  .95  .95<br>1/2  L  L  L  L  L  L  L  L  L  L  1<br>1/10  1/10  1/10  1/10  1/2  1/10  1/10  1/2  1/10  1/10<br>1/6  1/6  1/6  1/6  1/6  1/6  1/6  1/6  1/6  1/6<br>.95  .95  .95  .95  .95  .95  .95  .95  .95  1<br>1/2  F  F  F  F  F  F  F  F  F  F<br>Two sequence paths:<br><!-- End of picture text -->

P( x, all-Fair )       = 5.2  10<sup>-9</sup> (very small)

P( x, all-Loaded ) = 7.9  10<sup>-10</sup> (very very small)

Likelihood ratio:

P( x, all-Fair ) is 6.59 times more likely than P( x, all-Loaded )

It is 6.59 times more likely that the die is fair all the way, than loaded all the way.

Slide credit: Serafim Batzoglou

21

## **What about partial runs and die switching**


<!-- Start of picture text -->
L  L  L  L  L  .95  L  .95  L  .95  L  L  L<br>.05<br>.05<br>.95  .95  .95  .95  1<br>1/2  F  F  F  F  F  F  F  F  F  F<br>1/6  1/6  1/6  1/6  1/2  1/10  1/10  1/2  1/6  1/6<br>What is the likelihood of<br><!-- End of picture text -->

π = Fair, Fair, Fair, Fair, Load, Load, Load, Load, Fair, Fair and rolls x   =   1   ,   2,     1,     5,      6,       2,      1,       6,      2,      4 emission      transition       emission     transition         emission p = ½  P(1 | Fair) P(Fairi+1 | Fairi) P(2 | Fair) P(Fair | Fair) … P(4 | Fair) = ½  (1/10)<sup>2</sup>  (1/2)<sup>2</sup>  (1/6)<sup>5</sup>  (0.95)<sup>7</sup>  (0.05)<sup>2</sup> = 2.8  10<sup>-10</sup>

#### **Much less likely, due to high cost of transitions**

22

## **Model comparison**

Let the sequence of rolls be: x = 1, 6, 6, 5, 6, 2, 6, 6, 3, 6

Now, what is the likelihood  = F, F, …, F? ½  (1/6)<sup>10</sup>  (0.95)<sup>9</sup> = 0.5  10<sup>-9</sup> , same as before

What is the likelihood  = L, L, …, L? ½  (1/10)<sup>4</sup>  (1/2)<sup>6</sup> (0.95)<sup>9</sup> = 0.5  10<sup>-7</sup>

So, it is 100 times more likely the die is loaded

**Model evaluation**

23

---

[← Lecture 4 Modeling Biological Sequences using Hidden Markov Models](01-lecture-4-modeling-biological-sequences-using-hidden-markov.md) · [Up: contents](index.md) · [The six algorithmic settings for HMMs One path All paths →](03-the-six-algorithmic-settings-for-hmms-one-path-all-paths.md)

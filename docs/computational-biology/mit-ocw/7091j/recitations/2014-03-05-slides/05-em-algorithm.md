---
title: EM algorithm
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# EM algorithm

**Source:** `recitations/2014-03-05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

-The previous formulation works pretty well, but distributes the binding events π to _too many_ nonzero components

- For example, it might assign equal binding weight of 0.0033 to three

- adjacent nucleotides when we know there was a binding event starting at only one of them which should have weight 0.01 with the other two being 0.

- Solution: introduce a sparse prior, which penalizes the a nucleotide for

- having nonzero π component - the likelihood is multiplied by this prior to get calculate a posterior likelihood. If α is chosen within an appropriate range, this can force nearby components to 0 while allowing one nucleotide in the neighborhood to have nonzero component in the π that maximizes the posterior likelihood.


<!-- Start of picture text -->
N M M<br>Likelihood of<br>= =<br>observed reads  p ( R | π) π m p ( rn | m ,) π m 1<br>∏∑ ∑<br>n =1 m =1 m =1<br>A sparse prior  on mixture components (binding events)<br>M 1<br>π ∝ α > 0<br>p ( ) ,<br>α<br>∏<br>m =1 (π m ) (Figueiredo and Jain, 2002)<br><!-- End of picture text -->

13

## GEM: Genome-wide Event-finding and Motif discovery

- If we know the motif(s) that the protein binds to, incorporating this information can inform where binding sites are, which can strongly improve spatial resolution

   - Even if unknown ahead of time, we can try to learn the motif(s) from overrepresented _k_ mers around the predicted binding sites


<!-- Start of picture text -->
Biases binding event<br>predictions towards<br>2<br>G E M<br>motif positions<br>Event  Motif<br>finding  discovery<br>Bias motif<br>1<br>discovery towards<br>binding sites<br>Binding events and<br>explanatory DNA motifs<br><!-- End of picture text -->

14

## How significant are resulting peaks?

- Compute a scaling factor between control and IP reads using the read counts from the non-peak regions

- Then, for each binding event (nonzero π element), calculate the P-value for observing the number of ChIP reads under the null hypothesis that there was no binding event (i.e., reads equally likely in control and IP since both are background):

Under null hypothesis, reads should be equally distributed between control and IP. In reality, we observe more reads in IP and fewer in control.

P-value: if the _n_ reads near the binding site were randomly distributed between the control and IP, what’s the probability of observing _k_ or fewer reads in the control?

15

---

[← EM algorithm](04-em-algorithm.md) · [Up: contents](index.md) · [Multiple Hypothesis Correction →](06-multiple-hypothesis-correction.md)

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

######

1.  Scoring x, one path

2.  Scoring x, all paths

P(x,π)

- P(x) = Σπ P(x,π)

  Prob of emissions, over all paths

Prob of a path, emissions

3. Viterbi decoding

   4.  Posterior decoding

- π* = argmaxπ P(x,π)

- π^ = {πi | πi=argmaxk ΣπP(πi=k|x)}

Most likely path

Path containing the most likely state at any time point.

5. Supervised learning, given π Λ* = argmaxΛ P(x,π|Λ)

   6.  Unsupervised learning

      - Λ* = argmaxΛ ΣπP(x,π|Λ)

6. Unsupervised learning. Λ* = argmaxΛ maxπP(x,π|Λ) Viterbi training, best path

Baum-Welch training, over all paths

39

## **Examples of HMMs for genome annotation**

|**Application**|**Detection**<br>**of GC-rich**<br>**regions**|**Detection**<br>**of**<br>**conserved**<br>**regions**|**Detection**<br>**of protein-**<br>**coding**<br>**exons**|**Detection**<br>**of protein-**<br>**coding**<br>**conservatio**<br>**n**|**Detection**<br>**of protein-**<br>**coding**<br>**gene**<br>**structures**|**Detection**<br>**of**<br>**chromatin**<br>**states**|
|---|---|---|---|---|---|---|
|**Topology /**<br>**Transitions**|2 states,<br>different<br>nucleotide<br>composition|2 states,<br>different<br>conservation<br>levels|2 states,<br>different tri-<br>nucleotide<br>composition|2 states,<br>different<br>evolutionary<br>signatures|~20 states,<br>different<br>composition/<br>conservation<br>, specific<br>structure|40 states,<br>different<br>chromatin<br>mark<br>combination<br>s|
|**Hidden**<br>**States /**<br>**Annotation**|GC-rich / AT-<br>rich|Conserved /<br>non-<br>conserved|Coding exon<br>/ non-coding<br>(intron or<br>intergenic)|Coding exon<br>/ non-coding<br>(intron or<br>intergenic)|First/last/mid<br>dle coding<br>exon,UTRs,<br>intron1/2/3,<br>intergenic,<br>*(+/- strand)|Enhancer /<br>promoter /<br>transcribed /<br>repressed /<br>repetitive|
|**Emissions /**<br>**Observatio**<br>**ns**|Nucleotides|Level of<br>conservation|Triplets of<br>nucleotides|64x64 matrix<br>of codon<br>substitution<br>frequencies|Codons,<br>nucleotides,<br>splice sites,<br>start/stop<br>codons|Vector of<br>chromatin<br>mark<br>frequencies<br>40|


## **What have we learned ?**

- Modeling sequential data

- Recognize a **_type_** of sequence, genomic, oral, verbal, visual, etc…

- • Definitions

   - Markov Chains

   - Hidden Markov Models (HMMs)

- Examples of HMMs

   - Recognizing GC-rich regions, preferentially-conserved elements, coding exons, protein-coding gene structures, chromatin states

- Our first computations

   - Running the model:  know model  generate sequence of a ‘type’

   - Evaluation:  know model, emissions, states  p?

   - Viterbi: know model, emissions  find optimal path

   - Forward: know model, emissions  total p over all paths

- Next time:

   - Posterior decoding

   - Supervised learning

   - Unsupervised learning:  Baum-Welch, Viterbi training

41

MIT OpenCourseWare http://ocw.mit.edu

6.047 / 6.878 / HST.507 Computational Biology Fall 2015

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← The six algorithmic settings for HMMs One path All paths](04-the-six-algorithmic-settings-for-hmms-one-path-all-paths.md) · [Up: contents](index.md)

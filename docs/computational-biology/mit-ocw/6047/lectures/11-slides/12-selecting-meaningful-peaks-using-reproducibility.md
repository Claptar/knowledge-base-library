---
title: Selecting meaningful peaks using reproducibility
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Selecting meaningful peaks using reproducibility

**Source:** `lectures/11-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Use peak ranks in replicate experiments IDR: Irreproducible Discovery Rate

<u>http://anshul.kundaje.net/projects/idr</u>

46 <u>A. Kundaje, Q. Li , B. Brown, J. Rozowsky, S. Wilder, M. Gerstein, I. Dunham, E. Birney, P. Bickel</u>

## How to combine two replicates

###### Replicate 1

Replicate 2


• Challenge:

– Replicates show small differences in peak heights

– Many peaks in common, but many are unique

• Problem with simple solutions:

– Union: too lenient, keeps garbage from both

– Intersection: too stringent, throws away good peaks

– Sum: does not exploit independence of two datasets

47

###### **IDR idea: Exploit peak rank similarity in replicates**


<!-- Start of picture text -->
IDR Cutoff<br><!-- End of picture text -->

         - © Source unknown. All rights reserved. This content is excluded from our Creative

         - Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- Key idea: True peaks will be highly ranked in both replicates

      - Keep going down rank list, until ranks are no longer correlated

      - This cutoff could be different for the two replicates

   - The actual peaks included may differ between replicates

      - Adaptively learn optimal peak calling threshold

   - **F** DR threshold of 10%  10% of peaks are false (widely used)

• **I** DR threshold of 10%  10% of peaks are not reproducible

48

The IDR model: A two component mixture model

• Looking only at ranks means that the marginals are uniform, so all the information is encoded in the joint distribution.

• Model the joint distribution of ranks as though it came from a two component Gaussian mixture model:

~  _x_    _N_ ( , _y_ ) _pN_ (  ,  , , ,  ) 1( _p_ ) (0,1,1,0,0)

• This can be fit via an EM-like algorithm.

49

###### **IDR leads to higher consistence between peak callers**

###### **IDR = Irreproducible Discovery Rate FDR = False Discovery Rate**


<!-- Start of picture text -->
 (at IDR = 1% cutoff)<br> (at FDR = 1% cutoff)<br># peaks called by SPP  # peaks called by SPP<br># peaks called by MACS<br># peaks called by MACS<br><!-- End of picture text -->

      - © Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

   - Compare number of peaks found by two different peak callers

   - IDR thresholds are far more robust and comparable than FDR

- FDR only relies on enrichment over input, IDR exploits replicates

50

###### **What if we don’t have good replicates?**


      - © Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

   - IDR pipeline uses replicates when they are available

   - IDR pipeline also evaluates each replicate individually

      - Pooling strategy to generate pseudo-replicates

- Can pin-point ‘bad’ replicates that may lead to low reproducibility

- Can estimate IDR thresholds when replicates are not available

51

## Only one good replicate: Pseudo-replicates


<!-- Start of picture text -->
Rescued<br>datasets<br><!-- End of picture text -->

   - © Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- IDR pipeline can be used to rescue datasets with only one good replicate (using pseudo-replicates)

- • IDR pipeline can also be used to call optimal thresholds on a dataset with a single replicate (e.g. when there isn’t enough material to perform multiple reps) 52

52

###### **Goals for today: Computational Epigenomics**

1. Introduction to Epigenomics – Overview of epigenomics, Diversity of Chromatin modifications

   - Antibodies, ChIP-Seq, data generation projects, raw data

2. Primary data processing: Read mapping, Peak calling – Read mapping: Hashing, Suffix Trees, Burrows-Wheeler Transform

– Quality Control, Cross-correlation, Peak calling, IDR (similar to FDR)

3. Discovery and characterization of chromatin states

   - A multi-variate HMM for chromatin combinatorics

   - Promoter, transcribed, intergenic, repressed, repetitive states

4. Model complexity: selecting the number of states/marks – Selecting the number of states, selecting number of marks

– Capturing dependencies and state-conditional mark independence

5. Learning chromatin states jointly across multiple cell types – Stacking vs. concatenation approach for joint multi-cell type learning

– Defining activity profiles for linking enhancer regulatory networks

(Future: Chromatin states to interpret disease-associated variants)

53

###### **Chromatin signatures for genome annotation**


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Qiu, Jane. "Epigenetics: Unfinished Symphony." Nature 441, no. 7090 (2006): 143-145.

- **Challenges**

   - Dozens of marks

   - Complex combinatorics

   - • Diversity and dynamics

- **Histone code hypothesis** • Distinct function for distinct combinations of marks?

   - Both additive and combinatorial effects

- **How do we find biologically relevant ones?**

   - Unsupervised approach

   - Probabilistic model

   - Explicit combinatorics

54

###### **Summarize multiple marks into chromatin states**


###### **Chromatin state track summary**


- © WashU Epigenome Browser. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

WashU Epigenome Browser

**_ChromHMM: multi-variate hidden Markov model_**

55

### Multivariate HMM for Chromatin States


<!-- Start of picture text -->
Enhancer  Transcription<br>Start Site  Transcribed Region  DNA<br>Observed<br>chromatin<br>marks. Called<br>based on a  K4me1  K4me3  K4me3  K4me1  K36me3  K36me3  K36me3 K36me3<br>poisson<br>distribution  K27ac  K4me1<br>Most likely<br>Hidden State  1  2  3  4  6  6  6  6  6  5  5  5<br>High Probability Chromatin Marks in State<br>0.8<br>0.8<br>200bp  1:  4:  0.7<br>intervals  K4me1  K27ac  K4me1  All probabilities are<br>learned from the data<br>2:  0.9  0.8<br>5:<br>K4me3  K4me1<br>3:  0.9  6:  0.9<br>K4me3  K36me3<br>Ernst and Kellis<br>Nature Biotech 2010<br><!-- End of picture text -->

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Ernst, Jason and Manolis Kellis. "Discovery and characterization of chromatin states for systematic annotation of the human genome." Nature Biotechnology 28, no. 8 (2010): 817-825.

56

---

[← Peak Calling](11-peak-calling.md) · [Up: contents](index.md) · [Design Choice →](13-design-choice.md)

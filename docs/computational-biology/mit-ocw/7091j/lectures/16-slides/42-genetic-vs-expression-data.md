---
title: Genetic vs. Expression Data
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Genetic vs. Expression Data

**Source:** `lectures/16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

|**Perturbation**|**Differentially**<br>**expressed**<br>**genes**|**Genetic**<br>**hits**|**Number of**<br>**overlapping**<br>**genes**|
|---|---|---|---|
|**Growth arrest**<br>**(Hydroxyurea)**|**59**|**86**|**0**|
|**DNA damage (MMS)**|**198**|**1448**|**43**|
|**Protein biosynthesis block**<br>**(Cycloheximide)**|**20**|**164**|**0**|
|**ER stress (Tunicamycin)**|**200**|**127**|**5**|
|**ATP synthesis block**<br>**(Arsenic)**|**828**|**50**|**9**|
|**Fatty acid metabolism**<br>**(oleate)**|**269**|**103**|**9**|
|<br>**Gene inactivation**<br>**(24 datasets, median shown)**|**27**|**130**|**0**|


**Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity Nature Genetics Published online: 22 February 2009**

##### **For 156 perturbations:**

**Genetic Data Enriched for:** • **Transcriptional regulation** • **Signal transduction**


**Expression Data Enriched for: Metabolic Processes e.g., organic acid metabolic process, oxidoreducatse activities**

**Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity Nature Genetics Published online: 22 February 2009**


<!-- Start of picture text -->
DNA Damage<br><!-- End of picture text -->


<!-- Start of picture text -->
DNA Damage<br>Sliding clamp checkpoint<br>Cell cycle DNA repair<br>arrest<br><!-- End of picture text -->

**Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity Nature Genetics Published online: 22 February 2009**


<!-- Start of picture text -->
DNA Damage<br><!-- End of picture text -->


<!-- Start of picture text -->
DNA Damage<br><!-- End of picture text -->


<!-- Start of picture text -->
MEC1 = ATM<br>RAD53 = CHK2<br>Cell cycle DNA repair<br>arrest<br><!-- End of picture text -->

**Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity Nature Genetics Published online: 22 February 2009**


**Interactome TF ChIP-chip & Sequence Analysis**

**Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity Nature Genetics Published online: 22 February 2009**

###### **Test case: Perturbing pheromone response pathway**

Perturbing Ste5


20 genes rescue mating phenotype (SGD)


12 genes differentially expressed (Rosetta compendium)


<!-- Start of picture text -->
Dig1 Ste12<br><!-- End of picture text -->

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity Nature Genetics Published online: 22 February 2009**


<!-- Start of picture text -->
Δste5: Naïve approach<br>Paths limited to length 3<br>Genetic Data<br><!-- End of picture text -->


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.


<!-- Start of picture text -->
Expression Data<br><!-- End of picture text -->

**193 nodes, 778 edges**

**Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity Nature Genetics Published online: 22 February 2009**

###### Maximize the connectivity via reliable paths


<!-- Start of picture text -->
p=0.1<br>p=0.9<br><!-- End of picture text -->


Goal: find paths that maximize product of Pij Assign probabilities using a Bayesian approach based on reliability of underlying data type: Myers, C.L. et al. Genome Biology (2005).

Jansen, R. et al. Science (2003).

**Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity Nature Genetics Published online: 22 February 2009**

###### Maximize the connectivity via reliable paths


<!-- Start of picture text -->
Source<br>Minimum cost flow<br>Flow<br>p=0.1<br>p=0.9<br>Low High<br>probability probability<br>Sink<br>FLOW<br><!-- End of picture text -->

**Minimum cost flow problem** Flow

**Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity Nature Genetics Published online: 22 February 2009**

###### Maximize the connectivity via reliable paths


<!-- Start of picture text -->
Source<br>Minimum cost flow problem<br>Flow<br>p=0.1<br>p=0.1<br>p=0.9<br>Low High<br>probability probability<br>Proteins ranked by their incoming<br>flow:<br>Sink<br>Less  More<br>important important<br>FLOW<br><!-- End of picture text -->

**Minimum cost flow problem** Flow

###### Maximize the connectivity via reliable paths


<!-- Start of picture text -->
Source<br>Minimum cost flow problem<br>Maximize flow: source to sink<br>p=0.1 Minimize cost (eij) =ij) =) = fij ij  *(-log Pijij)<br>p=0.1<br>min (∑cost(eij) –γ*∑ fSj)∑cost(eij) –γ*∑ fSj)ij) –γ*∑ fSj)) –γ*∑ fSj)–γ*∑ fSj)γ*∑ fSj)*∑ fSj)Sj))<br>p=0.9<br>fij = flow through eij<br>cij = capacity of eij= 1 for all eij<br>Proteins ranked by their incoming<br>flow:<br>Sink<br>FLOW<br><!-- End of picture text -->

**Minimum cost flow problem** Maximize flow: source to sink

- Minimize cost (eij) =ij) =) = fij ij *(-log Pijij) min (∑cost(eij) –γ*∑ fSj)∑cost(eij) –γ*∑ fSj)ij) –γ*∑ fSj)) –γ*∑ fSj)–γ*∑ fSj)γ*∑ fSj)*∑ fSj)Sj))

Less More important important

###### **Test case: Perturbing pheromone response pathway**


<!-- Start of picture text -->
Dig1 Ste12<br><!-- End of picture text -->

###### Perturbing Ste5


20 genes rescue mating phenotype (SGD)


12 genes differentially expressed

(Rosetta compendium)

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity Nature Genetics Published online: 22 February 2009**

###### **Genetic Data**

###### Enriched for pheromone response p<10<sup>-18</sup>


<!-- Start of picture text -->
CLN3 STE20 FAR1 CDC25 STE7 STE11 STE4 STE18 STE2 HOG1 AKR1 CDC36 CDC39 HSP82<br>CDC28 CLB2 CLN2 STE5 GPA1 SKO1 SIN4 SSN8 IQG1 RPD3<br>KSS1 FUS3 CMD1<br>SWI6 XBP1 STE12 DIG1 TEC1 TUP1 HAP5 SDS3 SIN3 SWI1<br>YLR<br>AGA1­ SST2­ KAR4­ GPA1­ FUS3­ TEC1­ STE2­ STE6­ FUS1+<br>042C­ Expression<br>Data<br>49 nodes, 96 edges<br>Predicted genes<br>Importance<br><!-- End of picture text -->

---

[← ‘Omic data don’t agree](41-omic-data-don-t-agree.md) · [Up: contents](index.md) · [Network Models →](43-network-models.md)

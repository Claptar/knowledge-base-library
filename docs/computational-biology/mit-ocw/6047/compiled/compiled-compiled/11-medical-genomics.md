---
title: Medical Genomics
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/compiled/compiled-compiled.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Medical Genomics

**Source:** `compiled/compiled-compiled.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

477

CHAPTER

**THIRTYONE**

## MEDICAL GENETICS – THE PAST TO THE PRESENT

Guest Lecture by Mark J. Daly (PhD) Scribed by Anna Ayuso, Abhishek Sarkar (2011), Joel Brooks (2012), Grace Yeo (2014)

### **Figures**

|31.1 Examples of diseases and quantitative traits which have genetic components . . . . . . . .|478|
|---|---|
|31.2 The drug development process<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|479|
|31.3 A pedigree which shows the inheritance of some trait . . . . . . . . . . . . . . . . . . . . .|480|
|31.4 Representing a particular pattern of inheritance as an inheritance vector . . . . . . . . . .|481|
|31.5 Discovery of genes for different disease types versus time . . . . . . . . . . . . . . . . . . .|482|
|31.6 Different types of genetic variation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|483|
|31.7 Thresholds for GWAS significance at the blue line and red lines for a study by the IBDGC<br>on Crohn’s disease. The blue line represents a p-value of 5e-8 and the red line represents<br>approximately 7.2e-8.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|485|
|31.8 (A) Manhattan plot and (B) Q-Q plot for GWAS of Crohn’s disease . . . . . . . . . . . .|485|
|31.9 Evaluating Disease Network Significance . . . . . . . . . . . . . . . . . . . . . . . . . . . .|487|


## **31.1 Introduction**

Mark J. Daly, Ph.D., is an Associate Professor at the Massachusetts General Hospital/Harvard Medical School and an Associate Member of the Broad Institute. This lecture explains how statistical and computational methods can aid researchers in understanding, diagnosing, and treating disease. Association mapping is the process identifying genetic variation which can explain phenotypic variation, which is particularly important for understanding disease phenotypes (e.g., susceptibility). Historically, the method of choice for solving this problem was linkage analysis. However, advances in genomic technology have allowed for a more powerful method called genome-wide association.

479

6.047/6.878 Lecture 24: Medical Genetics – The Past to the Present

More recent advances in technology and genomic data have allowed for novel integrative analyses which can make powerful predictions about diseases. Any discussion about the basis of disease must consider both genetic and environmental effects. However, it is known that many traits, for example those in Figure 31.1, have significant genetic components. Formally, the _heritability_ of a phenotype is the proportion of variation in that phenotype which can be explained by genetic variation. The traits in Figure 31.1 are all at least 50% heritable. Accurately estimating heritability involves statistical analyses on samples with highly varied levels of shared genetic variation (e.g., twins, siblings, relatives, and unrelated). Studies on the heritability of Type 2 diabetes, for example, have shown that given you have diabetes, the risk to the person sitting next to you (an unrelated person) increases by 5–10%; the risk to a sibling increases by 30%; and the risk to an identical twin increases by 85%–90%.

## **31.2 Goals of investigating the genetic basis of disease**

Having established that there is a genetic component to disease traits, how can this research help meet outstanding medical challenges? There are two main ways:

### **31.2.1 Personalized genomic medicine**

Variants can be used in genetic screens to test for increased risk for the disease trait and provide individualized medical insights. A large number of companies are now providing personalized genomic services through screening for cancer recurrence risk, genetic disorders (including prenatal screening), and common disease. Individualized genomic medicine can help identify likelihood to benefit from specific therapeutic interventions, or can predict adverse drug responses.

### **31.2.2 Informing therapeutic development**

Identifying genetic variants which explain the disease trait contributes to our ability to understand the mechanism (the biochemical pathways, etc.) by which the disease manifests. This allows us to engineer drugs that are more effective at targeting the causal pathways in disease. This is of particular interest


Figure 31.1: Examples of diseases and quantitative traits which have genetic components

480

6.047/6.878 Lecture 24: Medical Genetics – The Past to the Present


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 31.2: The drug development process

because our current drug development process makes it difficult to develop drugs for certain disorders. For example, in the last 50 years, no truly novel compounds have been developed to treat various psychiatric disorders such as schizophrenia. The identification of genetically associated genes can help identify targets to start drug development.

Figure 31.2 depicts the cycle of drug development. The drug development process starts with hypothesizing a possible target of interest that might be related to a disease. After biochemical evaluations and drug development, the target is tested in model organisms. If the drug is effective in model organisms, it is tested in humans through clinical trials. However, the vast majority of drugs which make it through this process end up being ineffective in treating the disease for which they were originally designed. This result is mainly a consequence of faulty target selection as the basis of the disease in question. Statins are a prominent example of highly effective drugs developed after work on understanding the genetic basis of the disease trait they are targeted at. Dr. Michael Brown and Dr. Joseph Goldstein won the Nobel Prize in Physiology or Medicine in 1985 for their work on the regulation of LDL cholesterol metabolism [5]. They were able to isolate the cause of extreme familial hypercholesterolemia (FH), a Mendelian disorder, to mutations of a single gene encoding an LDL receptor. Moreover, they were able to identify the biochemical pathway which was affected by the mutation to create the disease condition. Statins target that pathway, making them useful not only to individuals suffering from FH, but also as an effective treatment for high LDL cholesterol in the general population.

## **31.3 Mendelian Traits**

### **31.3.1 Mendel**

Gregor Mendel identified the first evidence of inheritance in 1865 using plant hybridization. He recognized discrete units of inheritance related to phenotypic traits, and noted that variation in these units, and therefore variations in phenotypes, was transmissible through generations. However, Mendel ignored a discrepancy in his data: some pairs of phenotypes were not passed on independently. This was not understood until 1913, when linkage mapping showed that genes on the same chromosome are passed along in tandem unless a meiotic cross-over event occurs. Furthermore, the distance between genes of interest describes the probability of a recombination event occuring between the two loci, and therefore the probability of the two genes being inherited together ( **linkage** ).

481

6.047/6.878 Lecture 24: Medical Genetics – The Past to the Present


Figure 31.3: A pedigree which shows the inheritance of some trait

### **31.3.2 Linkage Analysis**

Historically, researchers have used the idea of linkage through **linkage analysis** to determine genetic variants which explain phenotypic variation. The goal is to determine which variants contribute to the observed pattern of phenotypic variation in a _pedigree_ . Figure 31.3 shows an example pedigree in which squares are male individuals, circles are female individuals, couples and offspring are connected, and individuals in red have the trait of interest.

Linkage analysis relies on the biological insight that genetic variants are not independently inherited (as proposed by Mendel). Instead, meiotic recombination happens a limited number of times (roughly once per chromosome), so many variants _cosegregate_ (are inherited together). This phenomenon is known as _linkage disequilibrium_ (LD).

As the distance between two variants increases, the probability a recombination occurs between them increases. Thomas Hunt Morgan and Alfred Sturtevant developed this idea to produce **linkage maps** which could not only determine the order of genes on a chromosome, but also their relative distances to each other. The Morgan is the unit of genetic distance they proposed; loci separated by 1 centimorgan (cM) have 1 in 100 chance of being separated by a recombination. Unlinked loci have 50% chance of being separated by a recombination (they are separated if an odd number of recombinations happens between them). Since we usually do not know _a priori_ which variants are causal, we instead use _genetic markers_ which capture other variants due to LD. In 1980, David Botstein proposed using _single nucleotide polymorphisms_ (SNPs), or mutations of a single base, as genetic markers in humans [4]. If a particular marker is in LD with the actual causal variant, then we will observe its pattern of inheritance contributing to the phenotypic variation in the pedigree and can narrow down our search.

The statistical foundations of linkage analysis were developed in the first part of the 20th century. Ronald Fisher proposed a genetic model which could reconcile Mendelian inheritance with continuous phenotypes such as height [10]. Newton Morton developed a statistical test called the **LOD score** (logarithm of odds) to test the hypothesis that the observed data results from linkage [26]. The null hypothesis of the test is that the _recombination fraction_ (the probability a recombination occurs between two adjacent markers) _θ_ = 1 _/_ 2 (no linkage) while the alternative hypothesis is that it is some smaller quantity. The LOD score is essentially a log-likelihood ratio which captures this statistical test:


The algorithms for linkage analysis were developed in the latter part of the 20th century. There are two main classes of linkage analysis: _parametric_ and _nonparametric_ [34]. Parametric linkage analysis relies on a model (parameters) of the inheritance, frequencies, and penetrance of a particular variant. Let _F_ be the set of founders (original ancestors) in the pedigree, let _gi_ be the genotype of individual _i_ , let Φ _i_ be

482

6.047/6.878 Lecture 24: Medical Genetics – The Past to the Present


Figure 31.4: Representing a particular pattern of inheritance as an inheritance vector

the phenotype of individual _i_ , and let _f_ ( _i_ ) and _m_ ( _i_ ) be the father and mother of individual _i_ . Then, the likelihood of observing the genotypes and phenotypes in the pedigree is:


The time required to compute this likelihood is exponential in both the number of markers being considered and the number of individuals in the pedigree. However, Elston and Stewart gave an algorithm for more efficiently computing it assuming no inbreeding in the pedigree [8]. Their insight was that conditioned on parental genotypes, offspring are conditionally independent. In other words, we can treat the pedigree as a Bayesian network to more efficiently compute the joint probability distribution. Their algorithm scales linearly in the size of the pedigree, but exponentially in the number of markers.

There are several issues with parametric linkage analysis. First, individual markers may not be _informative_ (give unambiguous information about inheritance). For example, homozygous parents or genotyping error could lead to uninformative markers. To get around this, we could type more markers, but the algorithm does not scale well with the number of markers. Second, coming up with model parameters for a Mendelian disorder is straightforward. However, doing the same for non-Mendelian disorders is non-trivial. Finally, estimates of LD between markers are not inherently supported.

Nonparametric linkage analysis does not require a genetic model. Instead, we first infer the inheritance pattern given the genotypes and the pedigree. We then determine whether the inheritance pattern can explain the phenotypic variation in the pedigree.

Lander and Green formulated an HMM to perform the first part of this analysis [20]. The states of this HMM are _inheritance vectors_ which specify the result every meiosis in the pedigree. Each individual is represented by 2 bits (one for each parent). The value of each bit is 0 or 1 depending on which of the grand-parental alleles is inherited. Figure 31.4 shows an example of the representation of two individuals in an inheritance vector.

Each step of the HMM corresponds to a marker; a transition in the HMM corresponds to some bits of the inheritance vector changing. This means the allele inherited from some meiosis changed, i.e. that a recombination occurred. The transition probabilities in the HMM are then a function of the recombination fraction between adjacent markers and the Hamming distance (the number of bits which differ, or the number of recombinations) between the two states. We can use the forward-backward algorithm to compute posterior probabilities on this HMM and infer the probability of every inheritance pattern for every marker.

This algorithm scales linearly in the number of markers, but exponentially in the size of the pedigree. The number of states in the HMM is exponential in the length of the inheritance vector, which is linear in the size of the pedigree. In general, the problem is known to be NP-hard (to the best of our knowledge, we cannot do better than an algorithm which scales exponentially in the input) [28]. However, the problem is important not

483

6.047/6.878 Lecture 24: Medical Genetics – The Past to the Present


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Glazier, Anne M., et al. "Finding Genes that Underlie Complex Traits." _Science_ 298, no. 5602 (2002): 2345-9.

Figure 31.5: Discovery of genes for different disease types versus time

only in this context, but also in the contexts of _haplotype inference_ or _phasing_ (assigning alleles to homologous chromosomes) and _genotype imputation_ (inferring missing genotypes based on known genotypes). There have been many optimizations to make this analysis more tractable in practice [1, 11, 12, 15–18, 21, 23].

Linkage analysis identifies a broad genomic region which correlates with the trait of interest. To narrow down the region, we can use fine-resolution genetic maps of recombination breakpoints. We can then identify the affected gene and causal mutation by sequencing the region and testing for altered function.

## **31.4 Complex Traits**

Linkage analysis has proven to be highly effective in studying the genetic basis of Mendelian (single gene) diseases. In the past three decades, thousands of genes have been identified as contributing to Mendelian diseases. We have identified the genetic basis of disease such as sickle cell anemia, cystic fibrosis, muscular dystrophy, and severe forms of common diseases such as diabetes and hypertension. For these diseases, mutations are severe and obvious; the environment, behavior, and chance have little effect. Figure 31.5 shows this explosion in published associations.

However, most diseases (and many other traits of interest) are not Mendelian. These **complex traits** arise from the interactions of many genes and possibly the environment and behavior. A canonical complex trait is human height: it is highly heritable, but environmental factors can affect it. Recently, researchers have identified hundreds of variants which are associated with height [2, 25].

Linkage analysis is not a viable approach to find these variants. The first complex trait mapping occured in 1920 by Altenburg and Muller and involved the genetic basis of truncated wing in _D. Melanogaster_ . The polygenicity, or distribution of a complex trait across a large number of genes, provides a fundamental challenge to determining which genes are associated with a phenotype. In complex traits, instead of one gene determining a disease or trait (as in Mendelian inheritance), many genes each exert a small influence. The effect of all of these genes, as well as environmental influences, combine to determine an individual outcome. Furthermore, most common diseases work this way. This is due to the fact that selection agains each individual genotypic difference is very small, because there is no one difference that is causal for the disease. This way, complex traits ”survive” evolution, because they are not targets for selection.

484

6.047/6.878 Lecture 24: Medical Genetics – The Past to the Present


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 31.6: Different types of genetic variation

## **31.5 Genome-wide Association Studies**

In the 1990s, researchers proposed a methodology called **genome-wide association** to systematically correlate markers with traits. These studies sample large pools of cases and controls, measure their genotypes at on the order of one million markers, and try to correlate variation (SNPs, CNVs, indels) in their genotypes with their variation in phenotype, tracking disease through the population, instead of pedigrees.

### **31.5.1 Events Enabling Genome-wide Association Studies**

Genome-wide association studies (GWASs) are possible due to three advances.

First, advances in our understanding of the genome and the creation of genomic resources have allowed us to better understand and catalogue variation in the genome. From this data, we have realized the key biological insight that humans are one of the least genetically diverse species. On the order of tens of millions of SNPs are shared between different human subpopulations. For any particular region of the genome, we observe only a limited number of **haplotypes** (allele combinations which are inherited together). This is due to the fact that as a species, we are relatively new, and mutations have not caught up with our rapid growth. Because of this high redundancy, we only need to measure a fraction of all the variants in the human genome in order to capture them all with LD. We can then adapt the algorithms for inferring inheritance patterns in linkage analysis to impute genotypes for the markers which we did not genotype. Furthermore, genome resources allow us to carefully choose markers to measure and to make predictions based on markers which show statistically significant association. We now have the reference sequence of the human genome (allowing for alignments, genotype and SNP calling) and HapMap, a comprehensive catalog of SNPs in humans. We also have genome-wide annotations of genes and regulatory elements.

Second, advances in genotyping technology such as microarrays and high-throughput sequencing have given us the opportunity to compare the genomes of those affected with various phenotypes to controls. They are also the easiest and cheapest to measure using these technologies. Although there are many types of variation in the human genome (Figure 31.6 shows some examples), SNPs are the vast majority. Additionally, to account for the other types of variants, recently DNA microarrays have been developed to detect copy-number variation in addition to SNPs, after which we can impute the unobserved data.

The third advance is a new expectation of collaboration between researchers. GWASs rely on large sample sizes to increase the _power_ (probability of a true positive) of statistical tests. The explosion in the number of published GWASs has allowed for a new type of **meta-analysis** which combines the results of several

485

6.047/6.878 Lecture 24: Medical Genetics – The Past to the Present

GWASs for the same phenotype to make more powerful associations. Meta-analysis accounts for various technical and population-genetic biases in individual studies. Researchers who conduct GWASs are expected to collaborate with others who have conducted GWASs on the same trait in order to show replicability of results. By pooling together the data, we also have more confidence in the reported associations, and the genes that are discovered may lead to the recognition of key pathways and processes.

## **_Did You Know?_**

Modified from the Wellcome Trust Sanger Institute: Crohn’s disease and Ulcerative Colitis have been focuses for complex disease genetics, and the massive collaborative efforts of the International Inflammatory Bowel Disease Genetics Consortium (IIBDGC) strengthen the success of the research. With approximately 40,000 DNA samples from patients with IBD and 20,000 healthy controls, the IIBDGC have discovered 99 definite IBD loci. In all, the 71 Crohn’s disease and 47 UC loci account for 23 % and 16% of disease heritability respectively. Key insights into disease biology have already [ **?** ] resulted from gene discovery (e.g. autophagy in Crohn’s disease, defective barrier function in UC and IL23 signalling in IBD and immune-mediated disease generally). It is anticipated that of the many novel drug targets identified by gene discovery, a few will ultimately result in improved therapeutics for these devastating conditions. Improved diagnostics, prognostics and therapeutics are all goals, with a view to **personalized therapy** (the practice of using an individual’s genetic profile as a guide for treatment decisions) in future.

### **31.5.2 Quality Controls**

The main problem in conducting GWASs is eliminating confounding factors, but best practices can be used to support quality data.

First, there is genotyping error, which is common enough to require special treatment regardless of which technology is used. This is a technical quality control, and to account for such errors, we use thresholds on metrics like minor allele frequency and deviation from **Hardy–Weinberg equilibrium** and throw out SNPs which do not meet the criteria.

Second, systematic genetic differences between human subpopulations require a genetic quality control. There are several methods to account for this **population substructure** , such as genomic control [7], testing for Mendelian inconsistencies, structured association [30], and principal component analysis [27, 29].

Third, covariates such as environmental and behavioral effects or gender may skew the data. We can account for these by including them in our statistical model.

### **31.5.3 Testing for Association**

After performing the quality controls, the statistical analysis involved in GWAS is fairly straightforward, with the simplest tests being **single marker regression** or a **chi-square test** . In fact, association results requiring arcane statistics/complex multi-marker models are often less reliable.

First, we assume the effect of each SNP is independent and additive to make the analysis tractable. For each SNP, we perform a hypothesis test whose null hypothesis is that the observed variation in the genotype at that SNP across the subjects does not correlate with the observed variation in the phenotype across the subjects. Because we perform one test for each SNP, we need to deal with the **multiple testing problem** . Each test has some probability of giving a false positive result, and as we increase the number of tests, the

486

6.047/6.878 Lecture 24: Medical Genetics – The Past to the Present


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 31.7: Thresholds for GWAS significance at the blue line and red lines for a study by the IBDGC on Crohn’s disease. The blue line represents a p-value of 5e-8 and the red line represents approximately 7.2e-8.

probability of getting a false positive in any of them increases. Essentially, with linkage, p = 0.001 (.05/ 50 chromosomal arms) would be considered potentially significant, but GWAS involves performing O(10e6) tests that are largely independent. Each study would have hundreds of p _<_ 0.001 purely by statistical chance, with no real relationship to disease. There are several methods to account for multiple testing such as Bonferroni correction and measures such as the false discovery rate [3] and the irreproducible discovery rate [22]. Typically, **genome-wide significance** is set at p = 5*10e-8 (= .05/1 million tests), first proposed by Risch and Merikangas (1996) []. In 2008, three groups [] published empirically derivaed estimates based on dense genome-wide maps of common DNA and estimated appropriate dense-map numbers to be in the range of 2.5 to 7.2e-8. These can be visualized in Figure 31.7. Because of these different thresholds, it’s important to look at multiple studies to validate associations, as even with strict quality control there can be artifiacts that can affect one every thousand or ten thousand SNPs and escape notice. Additionally, strict genomewide significance is generally not dramatically exceeded, if it’s reached at all, in a single study.

In addition to reporting SNPs which show the strongest associations, we typically also use _Manhattan plots_ to show where these SNPs are located in the genome and _quantile-quantile (Q-Q) plots_ to detect biases which have not been properly accounted for. A Manhattan plot is a scatter plot of log-transformed p-values against genomic position (concatenating the chromosomes). In Figure 31.8A, the points in red are those which meet the significance threshold. They are labeled with candidate genes which are close by. A Q-Q plot is a scatter plot of log-transformed observed p-values against log-transformed expected p-values. We use uniform quantiles as the expected p-values: assuming there is no association, we expect p-values to be uniformly distributed. Deviation from the diagonal suggests p-values are more significant than would be expected. However, early and consistent deviation from the diagonal suggests too many p-values are too significant, i.e. there is some bias which is confounding the test. In Figure 31.8B, the plot shows observed test statistic against expected test statistic (which is equivalent). Considering all markers includes the **Major Histocompatability Complex (MHC)** , which is the region associated with immune response. This region has a unique LD structure which confounds the statistical analysis, as is clear from the deviation of the black points from the diagonal (the gray area). Throwing out the MHC removes much of this bias from the results (the blue points).

GWAS identifies markers which correlate with the trait of interest. However, each marker captures a neighborhood of SNPs which it is in LD with, making the problem of identifying the causal variant harder. Typically, the candidate gene for a marker is the one which is closest to it. From here, we have to do further study to identify the relevance of the variants which we identify. However, this remains a challenging problem for a few reasons:

487

6.047/6.878 Lecture 24: Medical Genetics – The Past to the Present


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 31.8: (A) Manhattan plot and (B) Q-Q plot for GWAS of Crohn’s disease

- Regions of interest identified by association often implicate multiple genes

- Some of these associations are nowhere near any protein coding segments and do no thave an obviously functional allele as their origin

- Linking these regions to underlying biological pathways is difficult

### **31.5.4 Interpretation: How can GWAS inform the biology of disease?**

Our primary goal is to use these found associations to understand the biology of disease in an actionable manner, as this will help guide therapies in order to treat these diseases. Most associations do not identify specific genes and causal mutations, but rather are just pointers to _small regions_ with causal influences on disease. In order to develop and act on a therapeutic hypothesis, we must go much further, and answer these questions:

- Which <mark>gene</mark> is connected to disease?

- What <mark>biological</mark> process is thereby implicated?

- What is the <mark>cellular context</mark> in which that process acts and is relevant to disease?

- What are the specific <mark>functional alleles</mark> which perturb the process and promote or protect from disease?

This can be approached in one of two manners: the _bottom-up_ approach, or the _top-down_ approach.

### **31.5.5 Bottom-up**

The **bottom-up** approach is used to investigate a particular gene that has a known association with a disease, and investigate it’s biological importance within a cell. Kuballa et al.[19] were able to use this bottom-up approach to learn that a particular risk variant associated with Crohn’s Disease leads to impairment of

488

6.047/6.878 Lecture 24: Medical Genetics – The Past to the Present


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 31.9: Evaluating Disease Network Significance

autophagy of certain pathogens. Furthermore, the authors were able to create a mouse model of the same risk variant found in humans. Identifying biological implications of risk variants at the cellular level and creating these models is invaluable as the models can be directly used to test new potential treatment compounds.

### **31.5.6 Top-down**

In contrast, the **top-down** approach involves looking at _all_ known associations, utilizing the complete set of GWAS results, and trying to link them to shared biological processes/pathways implicated in disease pathogenesis. This approach is based on the idea that many of the associated genes with a disease share relevant biological pathways. This is commonly done by taking existing networks like protein-protein interaction networks, and layering the associated genes on top of them. However, these resulting disease networks may not be significant due to bias in both the discovery of associations and the experimental bias of the data that the associations are being integrated with. This significance can be estimated by permuting the labels for the nodes in the network many times, and then computing how rare the level of connectivity is for the given disease network. This process is illustrated in Figure 31.9. As genes connected in the network should be co-expressed, it has been shown that these disease networks can be further validated from gene-expression profiling[14].

### **31.5.7 Comparison with Linkage Analysis**

It is important to note GWAS captures more variants than linkage analysis. Linkage analysis identifies rare variants which have negative effects, and linkage studies are used when pedigrees of related individuals with phenotypic information is available. They can identify rare alleles that are present in smaller numbers of families, usually due to a founder mutatios and have been used to identify mutations such as BRCA1, associated with breast cancer. Alternatively, association studies are used for this purpose and also to find more common genetic changes that confer smaller influences in susceptibility, such as rare variants which have protective effects. Linkage analysis cannot identify these variants because they are anti-correlated with disease status. Furthermore, linkage analysis relies on the assumption that a single variant explains the disease, an assumption that does not hold for complex traits such as disease. Instead, we need to consider many markers in order to explain the genetic basis of these traits.

489

6.047/6.878 Lecture 24: Medical Genetics – The Past to the Present

### **31.5.8 Challenges of Non-coding Variants**

While genomic medicine promises novel discoveries in disease mechanisms, target genes, therapeutics, and personalized medicine, several challenges remain, including that 90+% of hits are non-coding.

To fix this, the non-coding genome has been annotated through ENCODE/Roadmap and enhancers have been linked to regulators and target genes. Once each GWAS locus is expanded using SNP linkage desiquilibrium (LD) it can be used to recognize relevant cell types, driver transcription factors, and target genes. These leads to a linking of traits to their relevant cell and tissue types.

### **31.5.9 Conclusions**

We have learned several lessons from GWAS. First, fewer than one-third of reported associations are coding or obviously functional variants. Second, only some fraction of associated non-coding variants are significantly associated to expression level of a nearby gene. Third, many are associated to regions with no nearby coding gene. Finally, the majority of reported variants are associated to multiple autoimmune or inflammatory diseases. These revelations indicate that there are still many mysteries lurking in the genome waiting to be discovered.

## **31.6 Current Research Directions**

One current challenge in medical genetics is that of translation. In particular, we are concerned if GWAS can inform the development of new therapeutics. GWAS studies have been successful in identifying diseaseassociated loci. However, they provide little information about the causal alleles, pathways, complexes or cell types that are involved. Nevertheless, many known druggable targets are associated with GWAS hits. We therefore expect that GWAS has great potential in guiding therapeutic development.

A new tool in our search for greater insight into genetic perturbations is **next generation sequencing** (NGS). NGS has made sequencing an individual’s genome a much less costly and time-consuming task. NGS has several uses in the context of medical genetics, including exome/genome sequencing of rare and severe diseases, as well as exome/genome sequencing for the completion of allelic architecture at GWAS locis. However, NGS has in turn brought about new challenges in computation and interpretation.

One application of NGS to the study of human disease is in the identification and characterization of loss of function (LoF) variants. LoF variants disrupt the reading frame of protein-coding genes, and are therefore expected to be of scientific and clinical interest. However, the identification of these variants is complicated by errors in automated variant-calling and gene annotation. Many putative LoF variants are therefore likely to be false positives. In 2012, MacArthur et al. set out to describe a stringent set of LoF variants. Their results suggest that the typical human genomes contain about 100 LoF variants. They also presented a method to prioritize candidate genes as a function of their functional and evolutionary characteristics [24].

The MacArthur lab is also involved in an ongoing effort by the Exome Aggregation Consortium to assemble a catalog of human protein-coding variation for data mining. Currently, the catalog includes sequencing data from over 60,000 individuals. Such data allows for the identification of genes that are significantly lacking in functional coding variation. This is important because genes under exceptional constraint are expected to be deleterious. Based on this principle, Samocha et al. were able to identify 1000 genes involved in autism spectrum disorders that were significantly lacking in functional coding variation.

490

6.047/6.878 Lecture 24: Medical Genetics – The Past to the Present

This was done using a statistical framework that described a model of de novo mutation [32]. Similarly, De Rubeis et al. were able to identify 107 genes under exceptional evolutionary constraint that occurred in 5% of autistic subjects. Many of these genes were found to encode proteins involved in transcription and splicing, chromatin remodelling and synaptic function, thus advancing our understanding of the disease mechanism of these variants.

NGS can also be used to study rare and severe diseases, such as in the case of the DGAT1 mutation. In a study by Haas et al., exome sequencing was used to identify a rare splice site mutation in the DGAT1 gene. This had resulted in congenital diarrheal disorders in the children of a family of Ashkenazi Jewish descent [13]. In this case, sequencing not only had therapeutical applications for the surviving child but also provided insight into an ongoing DGAT1 inhibition clinical trial.

While NGS allows us to study highly penetrant variants that result in severe Mendelian diseases, there are also genetic studies that deliver hypotheses for intervention. One example of this is the discovery of SCN9A. The complete loss-of-function of SCN9A, also known as NaV1.7, results in congenital indifference to pain. This has resulted in the development of novel analgesics with efficacy exceeding that of morphine, as in the case of _µ_ -SLPTX-Ssm6a, a selective NaV1.7 inhibitor [35]. Another example is the loss-of-function variant of PCSK9, which lowers LDL and protects against coronary artery disease. This has led to the development of PCSK9 inhibitor REGN727, which has been shown to be safe and effective in phase 1 clinical trails [6].

NGS is also important for fine-mapping loci identified in GWAS studies. For example, GWAS studies from 2010 looking at Crohn’s disease implicated a region on chromosome 15 containing multiple genes. After fine-mapping, the International Inflammatory Bowel Disease Genetics Consortium (IIBDGC) was able to refine the association to a SMAD3 noncoding functional elements. Another example is a study by Farh et al. that looked at candidate causal variants for 21 autoimmune diseases. They showed that 90% of causal variants are non-coding, but only 10-20% alter transcription factor binding motifs, implying that current gene regulatory models cannot explain the mechanism of these variants [9]. Finally, a study by Rivas et al. that analyzed a deep resequencing of GWAS loci associated with inflammatory bowel disease found not only new risk factors but also protective variants. For example, a protective splice variant in CARD9 that causes premature truncation of protein was shown to strongly protect against the development of Crohn’s disease [31].

## **31.7 Further Reading**

## **31.8 Tools and Techniques**

- HapMap, a thorough catalog of human SNPs.

- PLINK, an open-source C/C++ GWAS tool set that can analyze large data sets with hundreds of thousands of markers genotyped for thousands of individuals to examine potential pathways.

- GRASS (Gene set Ridge regression in Association Studies), summarizes the genetic structure for each gene as eigenSNPs and uses group ridge regression to select representative eigenSNPs for each gene, assessing their association with disease risk and reducing the high dimensionality of GWAS data.

- GWAMA (Genome-Wide Association Meta-Analysis), performs meta-analysis of GWAS of dichotomous phenotypes or quantitative traits.

491

6.047/6.878 Lecture 24: Medical Genetics – The Past to the Present

## **31.9 What Have We Learned?**

In the past several decades, we have made huge advances in developing techniques to investigate the genetic basis of disease. Historically, we have used linkage analysis to find causal variants for Mendelian disease with great success. More recently, we have used genome-wide association studies to begin investigating more complex traits with some success. However, more work is needed in developing methods to interpret these GWAS and identifying causal variants and their role in disease mechanism. Improving our understanding of the genetic basis of disease will us develop more effective diagnoses and treatments.

## **Bibliography**

- [1] G.R. Abe¸casis, S.S. Cherny, W.O. Cookson, and L.R. Cardon. Merlin—rapid analysis of dense genetic maps using sparse gene flow trees. _Nature Genetics_ , 30(1):97–101, 2002.

- [2] H.L. Allen et al. Hundreds of variants clustered in genomic loci and biological pathways affect human height. _Nature_ , 467(7317):832–838, 2010.

- [3] Y. Benjamini and Y. Hochberg. Controlling the false discovery rate: A practical and powerful approach to multiple testing. _Journal of the Royal Statistical Society_ , 57:289–300, 1995.

- [4] D. Botstein, R.L. White, M. Skolnick, and R.W. Davis. Construction of a genetic linkage map in man using restriction fragment length polymorphisms. _American Journal of Human Genetics_ , 32:314–331, 1980.

- [5] M.S. Brown and J.L. Goldstein. A receptor-mediated pathway for cholesterol homeostasis. _Science_ , 232(4746):34–47, 1986.

- [6] Jonathan C. Cohen, Eric Boerwinkle, Thomas H. Mosley, and Helen H. Hobbs. Sequence variations in _PCSK9,_ low LDL, and protection against coronary heart disease. 354(12):1264–1272.

- [7] B. Devlin and K. Roeder. Genomic control for association studies. _Biometrics_ , 55:997–1004, 1999.

- [8] R.C. Elston and J. Stewart. A general model for the genetic analysis of pedigree data. _Human Heredity_ , 21:”523–542”, 1971.

- [9] Kyle Kai-How Farh, Alexander Marson, Jiang Zhu, Markus Kleinewietfeld, William J. Housley, Samantha Beik, Noam Shoresh, Holly Whitton, Russell J. H. Ryan, Alexander A. Shishkin, Meital Hatan, Marlene J. Carrasco-Alfonso, Dita Mayer, C. John Luckey, Nikolaos A. Patsopoulos, Philip L. De Jager, Vijay K. Kuchroo, Charles B. Epstein, Mark J. Daly, David A. Hafler, and Bradley E. Bernstein. Genetic and epigenetic fine mapping of causal autoimmune disease variants.

- [10] Sir R.A. Fisher. The correlation between relatives on the supposition of Mendelian inheritance. _Transactions of the Royal Society of Edinburgh_ , 52:399–433, 1918.

- [11] D.F. Gudbjartsson, K. Jonasson, M.L. Frigge, and A. Kong. Allegro, a new computer program for multipoint linkage analysis. _Nature Genetics_ , 25(1):12–13, 2000.

- [12] D.F Gudbjartsson, T. Thorvaldsson, A. Kong, G. Gunnarsson, and A. Ingolfsdottir. Allegro version 2. _Nature Genetics_ , 37(10):1015–1016, 2005.

- [13] Joel T. Haas, Harland S. Winter, Elaine Lim, Andrew Kirby, Brendan Blumenstiel, Matthew DeFelice, Stacey Gabriel, Chaim Jalas, David Branski, Carrie A. Grueter, Mauro S. Toporovski, Tobias C. Walther, Mark J. Daly, and Robert V. Farese. DGAT1 mutation is linked to a congenital diarrheal disorder. 122(12):4680–4684.

492

6.047/6.878 Lecture 24: Medical Genetics – The Past to the Present

- [14] X. Hu, H. Kim, E. Stahl, R. Plenge, M. Daly, and S. Raychaudhuri. Integrating autoimmune risk loci with gene-expression data identifies specific pathogenic immune cell subsets. _The American Journal of Human Genetics_ , 89(4):496–506, 2011.

- [15] R.M. Idury and R.C. Elston. A faster and more general hidden markov model algorithm for multipoint likelihood calculations. _Human Heredity_ , 47:197–202, 1997.

- [16] A. Ingolfsdottir and D. Gudbjartsson. Genetic linkage analysis algorithms and their implementation. In Corrado Priami, Emanuela Merelli, Pablo Gonzalez, and Andrea Omicini, editors, _Transactions on Computational Systems Biology III_ , volume 3737 of _Lecture Notes in Computer Science_ , pages 123–144. Springer Berlin / Heidelberg, 2005.

- [17] L. Kruglyak, M.J. Daly, M.P. Reeve-Daly, and E.S. Lander. Parametric and nonparametric linkage analysis: a unified multipoint approach. _American Journal of Human Genetics_ , 58:1347–1363, 1996.

- [18] L. Kruglyak and E.S. Lander. Faster multipoint linkage analysis using fourier transforms. _Journal of Computational Biology_ , 5:1–7, 1998.

- [19] P. Kuballa, A. Huett, J.D. Rioux, M.J. Daly, and R.J. Xavier. Impaired autophagy of an intracellular pathogen induced by a crohn’s disease associated atg16l1 variant. _PLoS One_ , 3(10):e3391, 2008.

- [20] E.S. Lander and P. Green. Construction of multilocus genetic linkage maps in humans. _Proceedings of the National Academy of Sciences_ , 84(8):2363–2367, 1987.

- [21] E.S. Lander, P. Green, J. Abrahamson, A. Barlow, M.J. Daly, S.E. Lincoln, and L. Newburg. Mapmaker: An interactive computer package for constructing primary genetic linkage maps of experimental and natural populations. _Genomics_ , 1(2):174–181, 1987.

- [22] Q. Li, J.B. Brown, H. Huang, and P.J. Bickel. Measuring reproducibility of high-throughput experiments. _Annals of Applied Statistics_ , 5:1752–1797, 2011.

- [23] E.Y. Liu, Q. Zhang, L. McMillan, F.P. de Villena, and W. Wang. Efficient genome ancestry inference in complex pedigrees with inbreeding. _Bioinformatics_ , 26(12):i199–i207, 2010.

- [24] D.G. MacArthur, S. Balasubramanian, A. Frankish, N. Huang, J. Morris, K. Walter, L. Jostins, L. Habegger, J.K. Pickrell, S.B. Montgomery, et al. A systematic survey of loss-of-function variants in human protein-coding genes. _Science_ , 335(6070):823–828, 2012.

- [25] B.P. McEvoy and P.M. Visscher. Genetics of human height. _Economics & Human Biology_ , 7(3):294 – 306, 2009.

- [26] N.E. Morton. Sequential tests for the detection of linkage. _The American Journal of Human Genetics_ , 7(3):277–318, 1955.

- [27] N. Patterson, A. Price, and D. Reich. Population structure and eigenanalysis. _PLoS Genetics_ , 2:e190, 2006.

- [28] A. Piccolboni and D. Gusfield. On the complexity of fundamental computational problems in pedigree analysis. _Journal of Computational Biology_ , 10:763–773, October 2003.

- [29] A. Price et al. Principal components analysis corrects for stratification in genome-wide association studies. _Nature Genetics_ , 38:904–909, 2006.

- [30] J. Pritchard, M. Stephens, N. Rosenberg, and P. Donnelly. Association mapping in structured populations. _American Journal of Human Genetics_ , 67:170–181, 2000.

- [31] M.A. Rivas, M. Beaudoin, A. Gardet, C. Stevens, Y. Sharma, C.K. Zhang, G. Boucher, S. Ripke, D. Ellinghaus, N. Burtt, et al. Deep resequencing of gwas loci identifies independent rare variants associated with inflammatory bowel disease. _Nature genetics_ , 2011.

493

6.047/6.878 Lecture 24: Medical Genetics – The Past to the Present

- [32] Kaitlin E Samocha, Elise B Robinson, Stephan J Sanders, Christine Stevens, Aniko Sabo, Lauren M McGrath, Jack A Kosmicki, Karola Rehnstrm, Swapan Mallick, Andrew Kirby, Dennis P Wall, Daniel G MacArthur, Stacey B Gabriel, Mark DePristo, Shaun M Purcell, Aarno Palotie, Eric Boerwinkle, Joseph D Buxbaum, Edwin H Cook, Richard A Gibbs, Gerard D Schellenberg, James S Sutcliffe, Bernie Devlin, Kathryn Roeder, Benjamin M Neale, and Mark J Daly. A framework for the interpretation of de novo mutation in human disease. 46(9):944–950.

- [33] Evan A. Stein, Scott Mellis, George D. Yancopoulos, Neil Stahl, Douglas Logan, William B. Smith, Eleanor Lisbon, Maria Gutierrez, Cheryle Webb, Richard Wu, Yunling Du, Therese Kranz, Evelyn Gasparino, and Gary D. Swergold. Effect of a monoclonal antibody to PCSK9 on LDL cholesterol. 366(12):1108–1118.

- [34] T. Strachan and A.P. Read. _Human Molecular Genetics_ . Wiley-Liss, New York, 2 edition, 1999.

- [35] S. Yang, Y. Xiao, D. Kang, J. Liu, Y. Li, E. A. B. Undheim, J. K. Klint, M. Rong, R. Lai, and G. F. King. Discovery of a selective NaV1.7 inhibitor from centipede venom with analgesic efficacy exceeding morphine in rodent pain models. 110(43):17534–17539.

494

CHAPTER

**THIRTYTWO**

VARIATION 2: : QUANTITATIVE TRAIT MAPPING, EQTLS, MOLECULAR TRAIT VARIATION

Tim Wall, Brendan Liu, Lei Ding (2014), Tejas Sundaresan, Giri Anand (2015)

### **Figures**

|32.1 Non-coding vs. Coding Variation and Explanation of Traits . . . . . . . . . . . . . . .|. .<br>502|
|---|---|
|32.2 A comparison of eQTL and GWAS approaches. . . . . . . . . . . . . . . . . . . . . . .|. .<br>503|
|32.3 cis-eQTL regulating gene transcription directly. [3] . . . . . . . . . . . . . . . . . . . .|. .<br>503|
|32.4 trans-eQTL regulating gene transcription indirectly. [3]<br>. . . . . . . . . . . . . . . . .|. .<br>503|
|32.5 eQTL Study Approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>503|
|32.6 Effects of the search radius and MAF on the number of eQTLs detected . . . . . . . .|. .<br>503|
|32.7 The effects of technical and population variance on expression level assays . . . . . . .|. .<br>503|
|32.8 The decision parameters researchers must make when conducting an eQTL study . . .|. .<br>504|
|32.9 An example eQTL Study on asthma . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>504|


## **32.1 Introduction**

Differences in gene coding regions across different organisms do not completely explain the phenotypic variation we see. For example, although the phenotypic difference is high between humans and chimpanzees and low between different squirrel species, there is more genetic variation among the squirrel species [1]. These observations lead us to conclude that there must be more than just gene-coding variation that accounts for phenotypic variation; specifically, non-coding variation also influences how genes are expressed, and consequently influences the phenotype of an organism. In fact, previous research has shown that most genetic variation occurs in non-coding regions [2]. Furthermore, most expression patterns have been found to be heritable traits.

Understanding how variation in non-coding regions affects co-regulating genes would allow us not only to

495

6.047/6.878 Lecture 25B: <u>Quantitative</u> trait mapping, eQTLs, molecular trait variation

understand but also control the expression of these and other related genes. This is especially relevant to the control of undesirable trait expressions like complex, polygenic diseases (Figure 32.1). In Mendelian disease, the majority of disease risk is predicted by coding variation, whereas in polygenic diseases the vast majority of causal variation is found outside of coding regions. This suggests that variation in the regulation of gene expression may play a greater role than genotypic variation in these polygenic diseases. Thus, the study of these trait associated variants is a step in the direction of understanding how genetic sequences both code for and control the expression of such diseases and their associated phenotypes.

eQTLs ( _expression quantitative trait loci_ ) encapsulate the idea of non-coding regions influencing mRNA expression introduced above: we can define an eQTL as a region of variants in a genome that are quantitatively correlated with the expression of another gene encoded by the organism. Usually, we will see that certain SNPs in certain non-coding regions will either enhance or disrupt the expression of a certain gene. The field of identifying, analyzing, and interpreting eQTLs in the genome has grown immensely over the last couple of years with hundreds of research papers being published.

There are four main mechanisms for how eQTLs influence the expression of their associated genes:

1. Altered transcription factor binding

2. Histone modifications

3. Alternative splicing of mRNA

4. miRNA silencing

## **_FAQ_**

- **Q:** What is the difference between an eQTL study and a GWAS?

- **A:** There are two fundamental differences. The first is in the nature of the phenotype being examined. In an eQTL, the phenotype checked is usually on a lower level of biological abstraction (normalized gene expression levels) instead of a more higher-level, sometimes visible phenotype used in GWAS, such as ”black hair”). Secondly, in GWAS, usually because the phenotype being correlated with various SNPs is a higher-level phenotype, we very rarely see tissue-specific GWAS. However, in eQTLs, the expression patterns of mRNA could vary greatly between tissue-types within the same individual, and eQTL studies for a specific tissue-type, such as neuron and glial cells, can be performed (Figure 32.2)

## **32.2 eQTL Basics**

### **32.2.1 Cis-eQTLs**

The use of whole genome eQTL analysis has separated eQTLs into two distinct types of manifestation. The first is a **cis-eQTL** (Figure 32.3) in which the position of the eQTL maps near the physical position of the gene. Because of proximity, cis-eQTL effects tend to be much stronger, and thus can be more easily detected by GWAS and eQTL studies. Often, these function as promoters of certain polymorphisms, affect methylation and chromatin conformation (thus increasing or decreasing access to transcription), and can

496

6.047/6.878 Lecture 25B: <u>Quantitative</u> trait mapping, eQTLs, molecular trait variation

manifest as insertions and deletions to the genome. Cis-eQTLs are generally classified as variants that lie within 1 million base pairs of the gene of interest. However, this is indeed an arbitrary cutoff and can be altered by an order of magnitude, for instance.

### **32.2.2 Trans-eQTLs**

The second distinct type of eQTL is a **trans-eQTL** (Figure 32.4). A trans-eQTL does not map near the physical position of the gene it regulates. Its functions are generally more indirect in their effect on the gene expression (not directly boosting or inhibiting transcription but rather, affecting kinetics, signaling pathways, etc.). Since such effects are harder to determine explicitly, they are harder to find in eQTL analysis; in addition, such networks can be extremely complex, further limiting trans-eQTL analysis. However, eQTL analysis has led to the discovery of **trans hotspots** which refer to loci that have widespread transcriptional effects [11].

Perhaps the biggest surprise of eQTL research is that, despite the location of trans hotspots and cis-eQTLs, no major trans loci for specific genes have been found in humans [12]. This is probably attributed the current process of whole genome eQTL analysis itself. As useful and widespread whole genome eQTL analysis is, we find that genome-wide significance occurs at _p_ = 5 _×_ 10<sup>_−_8</sup> with multiple testing on about 20 _,_ 000 genes. Thus, studies generally use an inadequate sample size to determine the significance of many trans-eQTL associations, which start with priors of very low probability to begin with as compared to cis-eQTLs [4]. Further, the bias reduction methods described in earlier sections deflate variance, which is integral to capture the microtrait associations inherent in trans loci. Finally, non-normal distributions limit the statistical significance of associations between trans-eQTLs and gene expression[4]. This has been slightly remedied by the use of cross-phenotype meta-analysis (CPMA)[5] which relies on the summary statistics from GWAS rather than individual data. This cross-trait analysis is effective because trans-eQTLs affect many genes and thus have multiple associations originating from a single marker. Sample CPMA code can be found in _Tools and Resources_ .

However, while trans loci have not been found, trans-acting _variants_ have been found. Since it can be inferred trans-eQTLs affect many genes, CPMA and ChIP-Seq can be used to detect such cross-trait variants. Indeed, 24 different significant trans-acting transcription factors were determined from a group of 1311 trans-acting SNP variants by observing allelic effects on populations and target gene interactions/connections.

## **32.3 Structure of an eQTL Study**

The basic approach behind an eQTL study is to consider each gene’s expression as a quantitative multi-factor trait and regress on principal components that explain the variance in expression. First, cells of the tissue of interest are extracted and their RNA extracted. Expression of proteins of interest is measured either by microarray or by RNA-seq analysis. Expression levels of each gene are regressed on genotypes, controlling for biological and technical noise, such that


Where _Yi_ is the gene expression of gene _i_ , _Xi_ is a vector containing the allelic composition of each SNP associated with the gene (and can take on values 0, 1, or 2 given a reference allele), _α_ and _β_ are column vectors containing the regression coefficients, and _ϵi_ is the residual error (See Figure 32.5) [9]. In concept,

497

6.047/6.878 Lecture 25B: <u>Quantitative</u> trait mapping, eQTLs, molecular trait variation

such a study is extremely simple. In practice, there are hundreds of potential confounders and statistical uncertainties which must be accounted for at every step of the process. However, the same regression model can be used to account for these covariates.

Figure 32.9 contains an example eQTL study conducted on asthma. The key result from the study is the linear model in the upper right: we can see as the genotype tends more towards the ”A” variant, the target gene expression decreases.

### **32.3.1 Considerations for Expression Data**

Quantifying expression of genes is fraught with experimental challenges. For a more detailed discussion of these issues, see Chapter 14. One important consideration for this type of expression analysis is the **SNPunder-probe effect** : probe sequences that map to regions with common variants provide inconsistent results due to the effect of variation within the probe itself on binding dynamics. Thus, experiments repeated with multiple sets of probes will produce a more reliable result. Expression analysis should also generally exclude **housekeeping genes** , which are not differentially regulated across members of a population and/or cell types, since these would only dilute the statistical power of the study.

### **32.3.2 Considerations for Genomic Data**

There are two main considerations for the analysis of genomic data: the minor allele frequency and the search radius. The **search radius** determines the generality of the effect being considered: an infinite search radius corresponds to a full-genome cis and trans-eQTL scan, while smaller radii restrict the analysis to cis-eQTLs. The **minor allele frequency** (MAF) determines the cutoff under which a SNP site is not considered: it is a major determinant of the statistical power of the study. A higher MAF cutoff generally leads to higher statistical power, but MAF and search radius interact in nonlinear ways to determine the number of significant alleles detected (see Figure 32.6).

### **32.3.3 Covariate Adjustment**

There are many possible statistical confounders in an eQTL study, both biological and technical. Many biological factors can affect the observed expression of any given mRNA in an individual; this is exacerbated by the impossibility of controlling the testing circumstances of the large population samples needed to achieve significance. Population stratification and genomic differences between racial groups are additional contributing factors. Statistical variability also exists on the technical side. Even samples run on the same machine at different times show markedly different clustering of expression results. (Figure 32.7).

Researchers have successfully used the technique of **Principal Component Analysis** (PCA) to separate the effects of these confounders. PCA can produce new coordinate axes along which SNP-associated gene expression data has the highest variance, thereby isolating unwanted sources of consistent variation (see Chapter 20.4 for a detailed description of Principal Component Analysis). After extracting the principal components of the gene expression data, we can extend the linear regression model to account for these confounders and produce a more accurate regression.

498

6.047/6.878 Lecture 25B: <u>Quantitative</u> trait mapping, eQTLs, molecular trait variation

## **_FAQ_**

- **Q:** Why is PCA an appropriate statistical tool to use in this setting and why do we need it?

- **A:** Unfortunately, our raw data has several biases and external factors that will make it difficult to infer good eQTLs. However, we can think of these biases as being independent influences on the datasets that create artificial variance in the expression levels we see, confounding the factors that give rise to actual variance. Using PCA, we can decompose and identify these variances into their principal components, and filter them out appropriately. Also, due to the complex nature of the traits being analyzed, PCA can help reduce the dimensionality of the data and thereby facilitate computational analysis.

## **_FAQ_**

- **Q:** How do we decide how many principal components to use?

- **A:** This is a tough problem; one possible solution would be to try a different number of principal components and examine the eQTLs found afterwards - very this number for future tests by seeing whether the outputted eQTLs are viable. Note that it would be difficult to ”optimize” different parameters for the eQTL study because each dataset will have an optimal number of principal components, a best value for MAF, etc...

### **32.3.4 Points to Consider**

The following are some points to consider when conducting an eQTL study.

- The optimal strategy for eQTL discovery in a specific dataset out of all different ways to conduct normalization procedures, non-specific gene filtering, search radius selection, and minor allele frequency cutoffs may not be transferable to another eQTL study. Many scientists overcome this using _greedy tuning_ of these parameters, running the eQTL study iteratively until a maximum number of significant eQTLs are found.

- It is important to note that eQTL studies only find _correlation_ between genetic markers and gene expression patterns, and do not imply causation.

- When conducting an eQTL study, note that most significant eQTLs are found within a few kb of the regulated gene.

- Historically, it has been found that most eQTL studies are about 30-40% reproducible, and this is a relic of how the dataset is structured and the different normalization and filtering strategies the respective researchers use. However, eQTLs that are found in two or more cohorts consistently follows similar expression influence within each of the cohorts.

- Many eQTLs are tissue-specific; that is, their influence in gene expression could occur in one tissue but not in another, and a possible explanation of this is the co-regulation of a single gene by multiple eQTLs that is dependent on one gene having multiple alleles.

499

6.047/6.878 Lecture 25B: <u>Quantitative</u> trait mapping, eQTLs, molecular trait variation

## **32.4 Current Research Directions**

### **32.4.1 Quantifying Trait Variation**

Because the study of eQTLs is a study in the level of expression of a gene, the primary step towards conducting an informative study is picking traits that have varying levels of expression rather than binary expression. Examples of such quantitatively viable traits are body mass index (BMI) and height. In the late 1980’s and early 1990’s, the first studies of gene expression through genome-wide mapping studies were initiated by Damerval and de Vienne [8] [6]. However, their use of 2-D electrophoresis for protein separation was inefficient and not thoroughly reliable as it introduced a lot of noise and could not be systematically and quantitatively summarized. It was only in the early 2000s when the introduction of high-throughput arraybased methods to measure mRNA incidence accelerated the successful use of this method, first highlighted in a study by Brem [10].

### **32.4.2 New Applications**

There are two directions that eQTL studies are headed. First, there is a rush to use whole genome eQTL analysis to validate associations among variances in the human population such as differences in gene expression among ethnic groups, as the statistical power for being able to do so is beginning to reach the threshold of significance. A second direction of research seeks to dislocate genetic associations with varying phenotypes and and population differences based on a non-genetic basis. These non-genetic factors include environment, cell line preparation, and batch effects.

## **32.5 What Have We Learned?**

In summary, most causal variation for complex polygenic diseases that we have discovered so far is noncoding. Moreover, phenotypic differences between species are not well explained by coding variation, while gene expression is highly heritable between generations. Thus, it is proposed that genetic control of expression levels are a crucial factor in determining phenotypic variance.

eQTLs are SNP variant loci that are correlated with gene expression levels. They come in one of two forms. Cis-eQTLs are sites whose loci map to near the affected genes, are relatively easy to detect due to their proximity, and generally have clear mechanisms of action. Trans-eQTLs map to distance areas of the genome, are more difficult to detect, and their mechanisms are not as direct.

eQTL studies combine a whole-genome approach similar to GWAS with a expression assay, either microarray or RNA-seq. Expression levels of each gene are correlated by linear regression with genotypes after using PCA to extract confounding factors. Determining the optimal parameters for MAF, search radius, and confounder normalization is an open research question. Applications of eQTLs include the identification of disease-associated variants as well as variants associated with population subspecies and the genetic and environmental variance that gives rise to complex traits,

500

6.047/6.878 Lecture 25B: <u>Quantitative</u> trait mapping, eQTLs, molecular trait variation

## **32.6 Further Reading**

The following is a very good introductory literature review on eQTLs, including their history and current applications:

#### **The role of regulatory variation in complex traits and disease**

Frank W. Albert and Leonid Kruglyak

_Nature Reviews Genetics 16_ 2015

There are also some research papers that are trailblazers in what is current in eQTL studies. One such paper is informative on the occurrence of DNA methylation affecting gene expression in the human brain. Another is a study on changes in expression during development in the nematode C. elegans, using age as a covariate during eQTL mapping:

1. **Abundant quantitative trait loci exist for DNA methylation and gene expression in human brain**

Gibbs JR, van der Brug MP, Hernandez DG, Traynor BJ, Nalls MA, et al.

_PLOS Genet 6_ 2010

2. **The effects of genetic variation on gene expression dynamics during development** Francesconi, M. and Lehner, B. _Nature 505_ 2013

In addition, eQTL variants have recently been found to be implicated in diseases such as Crohn’s disease and multiple sclerosis [4].

As mentioned in Section 4.2, there have also been a recent surge in studies applying eQTL studies to delineating differences among human subpopulations and characterizing the contributions of the environment toward trait variation:

1. **Common genetic variants account for differences in gene expression among ethnic groups** Spielman RS, Bastone LA, Burdick JT, Morley M, Ewens WJ, Cheung VG. _Nature Genetics_ 2007

2. **Gene-expression Variation Within and Among Human populations** Storey JD, Madeoy J, Strout JL, Wurfel M, Ronald J, Akey JM _The American Journal of Human Genetics_ 2007

3. **Population genomics of human gene expression [12]**

   - Stranger BE,Nica AC, Forrest MS, et. al.

_The American Journal of Human Genetics_ 2007

4. **Evaluation of genetic Variation Contributing to Differences in Gene expression between populations**

Zhang W, Duan S, Kistner EO, Bleibel WK, Huang RS, Clark TA, Chen TX, Schweitzer AC, Blume JE, Cox NJ, Dolan ME _The American Journal of Human genetics_ 2008

5. **A Genome-Wide Gene Expression Signature of Environmental Geography in Leukocytes of Moroccan Amazighs**

   - Idaghdour Y, Storey JD, Jadallah SJ, Gibson G _PLoS_ 2008

6. **On the design and analysis of gene expression studies in human populations** Joshua M Akey, Shameek Biswas, Jeffrey T Leek, John D Storey _Nature Genetics_ 2007

501

6.047/6.878 Lecture 25B: <u>Quantitative</u> trait mapping, eQTLs, molecular trait variation

## **32.7 Tools and Resources**

- The Costapas Lab distributes code to calculate CPMA from GWAS association p-values which can be found here: http://www.cotsapaslab.info/index.php/software/cpma/

- The Pritchard lab has several resources (found here: http://eqtl.uchicago.edu/Home.html) for eQTL research and gene regulation including:

   - DNase-seq data from 70 YRI lymphoblastoid cell lines

   - Downloading positions of transcription factor binding sites inferred in the HapMap lymphoblastoid cell lines by CENTIPEDE

   - Raw and mapped RNA-Seq data from Pickrell et al.

   - Assorted scripts for identifying sequencing reads covering genes, polyadenylation sites and exonexon junctions

   - Data and meQTL results for Illumina27K methylation data in HapMap lymphoblastoid cell lines.

   - Files to ignore areas of the genome that are prone to causing false positives in ChIP-seq and other sequencing based functional assays

   - Browser for eQTLs identified in recent studies in multiple tissues

- The Wellcome Trust Sanger Institute has developed packaged database and web services ( _Genevar_ ) that are designed to help integrative analysis and visualization of SNP-gene associations in eQTL studies. This information can be found here: http://www.sanger.ac.uk/resources/software/genevar/

- The Wellcome Trust Sanger Institute has also developed databases that contain information relevant to eQTL studies such as finding and identifying all functional elements in the human genome sequence and maintaining automatic annotation on selected eukaryotic genomes. This information can be found here: http://www.sanger.ac.uk/resources/databases/.

- Finally, the NIH is progressing on the Genotype-Tissue Expansion Projext (GTEx). Currently, the project stands at 35 tissues from 50 donors; the aim is to acquire and analyze 20,000 tissues from 900 donors, with the hope of gathering even more data for further genetic analyses, especially for eQTL and trans-eQTL analyses that require larger sample sizes.

## **Bibliography**

- [1] King, Mary-Claire and Wilson, A.C. (April 1975) _Evolution at Two Levels in Humans and Chimpanzees_ Science Vol.188 No. 4184

- [2] 1000 Genomes Project Consortium. Nature. 2010; 467:1061-73.

- [3] Cheung Vivien G. and Spielman Richard S. (2009) _Genetics of Human Gene Expression: Mapping DNA Variants that Influence Gene Expression_ Nature Reviews Genetics

- [4] C. Cotsapas, _Regulatory variation and eQTLs_ . 2012 Nov 1.

- [5] C. Cotsapas, BF Voight, E Rossin, K Lage, BM Neale, et al. (2011) _Pervasive Sharing of Genetic Effects in Autoimmune Disease._ PLoS Genet 7(8):e1002254. doi:10.1371/journal.pgen.1002254

- [6] Damerval C, Maurice A, Josse JM, de Vienne D (May 1994). _Quantitative Trait Loci Underlying Gene Product Variation: A Novel Perspective for Analyzing Regulation of Genome Expression_ Genetics 137 (1): 289301.PMC 1205945. PMID 7914503.

- [7] Dimas AS , et. al. (Sept. 2009) _Common regulatory variation impacts gene expression in a cell typedependent manner._ Science 325(5945):1246-50. 2 Epub 2009 Jul 30.

502

6.047/6.878 Lecture 25B: <u>Quantitative</u> trait mapping, eQTLs, molecular trait variation

- [8] D. de Vienne, A. Leonardi, C. Damerval (Nov 1988). _Genetic aspects of variation of protein amounts in maize and pea._ Electrophoresis 9 (11): 742750. doi:10.1002/elps.1150091110. PMID 3250877.

- [9] Shengjie Yang, Yiyuan Liu, Ning Jiang, Jing Chen, Lindsey Leach, Zewei Luo, Minghui Wang. _Genomewide eQTLs and heritability for gene expression traits in unrelated individuals_ . BMC Genomics 15(1): 13. 2014 Jan 9.

- [10] Rachel B. Brem and Leonid Kruglyak. _The landscape of genetic complexity across 5,700 gene expression traits in yeast._ PNAS 102(5): 15721577. 23 Nov 2004.

- [11] Michael Morley, Cliona M. Molony, Teresa M. Weber, James L. Devlin, Kathryn G. Ewens, Richard S. Spielman, Vivian G. Cheung. _Genetic analysis of genome-wide variation in human gene expression._ Nature 430: 743-747. 12 Aug 2004.

- [12] Barbara E Stranger, Alexandra C Nica, Matthew S Forrest, Antigone Dimas, Christine P Bird, Claude Beazley, Catherine E Ingle, Mark Dunning, Paul Flicek, Daphne Koller, Stephen Montgomery, Simon Tavar, Panos Deloukas, Emmanouil T Dermitzakis. _Population genomics of human gene expression._ Nature Genetics 39: 1217 - 1224. 16 Sep 2007.

503

6.047/6.878 Lecture 25B: <u>Quantitative</u> trait mapping, eQTLs, molecular trait variation


<!-- Start of picture text -->
coding_variation_disease.png<br><!-- End of picture text -->

Figure 32.1: Non-coding vs. Coding Variation and Explanation of Traits

504

6.047/6.878 Lecture 25B: <u>Quantitative</u> trait mapping, eQTLs, molecular trait variation

```
eQTL_network.png
```

Figure 32.2: A comparison of eQTL and GWAS approaches. Figure 32.3: cis-eQTL regulating gene transcription directly. [3]

Figure 32.4: trans-eQTL regulating gene transcription indirectly. [3]

Figure 32.5: eQTL Study Approach

Figure 32.6: Effects of the search radius and MAF on the number of eQTLs detected

Figure 32.7: The effects of technical and population variance on expression level assays

505

6.047/6.878 Lecture 25B: <u>Quantitative</u> trait mapping, eQTLs, molecular trait variation

Figure 32.8: The decision parameters researchers must make when conducting an eQTL study

Figure 32.9: An example eQTL Study on asthma

506

CHAPTER

**THIRTYTHREE**

MISSING HERETIBILITY

- **33.1 Introduction**

- **33.2 Current Research Directions**

- **33.3 Further Reading**

- **33.4 Tools and Techniques**

- **33.5 What Have We Learned?**

507

6.047/6.878 Lecture 25: Missing Heretibility

508

CHAPTER

**THIRTYFOUR**

PERSONAL GENOMES, SYNTHETIC GENOMES, COMPUTNG IN C VS. SI

Guest Lecture by George Church Scribed by Lawson Wong (2011)

## **34.1 Introduction**

George Church discussed a variety of topics that have motivated his past and present research. He first discussed about reading and writing genomes, including his own involvement in the development of sequencing and the Human Genome Project. In that latter half, he discussed about his more recent endeavor, the Personal Genome Project, which he initiated in 2005.

## **34.2 Reading and Writing Genomes**

As a motivation, consider the following question: Is there any technology that is not biologically motivated or inspired? Biology and our observations of it influence our lives pervasively. For example, within the energy sector, biomass and bioenergy has always existed and is increasingly becoming the focus of attention. Even in telecommunications, the potential of quantum-level molecular computing is promising, and is expected to be a major player in the future.

Church has been involved in molecular computing in his own research, and claims that once harnessed, it has great advantages over their current silicon counterparts. For example, molecular computing can provide at least 10% greater efficiency per Joule in computation. More profound perhaps is its potential effect on data storage. Current data storage media (magnetic disk, solid-state drives, etc.) is much less (billions times) dense than DNA. The limitation of DNA as data storage is that it has a high error rate. Church is currently involved in a project exploring reliable storage through the use of error correction and other techniques.

509

6.047/6.878 Lecture 26: Personal Genomes, Synthetic Genomes, Computing in C vs. Si

In a 2009 Nature Biotechnology review article [1], Church explores the potential for efficient methods to read and write to DNA. He observes that in the past decade there has been a 10 _×_ exponential curve in both sequencing and oligo synthesis, with double-stranded synthesis lagging behind but steadily increasing. Compared to the 1 _._ 5 _×_ exponential curve for VLSI (Moore’s Law), the increase on the biological side is more dramatic, and there is no theoretical argument yet for why the trend should taper off. In summary, there is great potential for genome synthesis and engineering.

## **_Did You Know?_**

George Church was an early pioneer of genome sequencing. In 1978, Church was able to sequence plasmids at $10 per base. By 1984, together with Walter Gilbert, he developed the first direct genomic sequencing method [3]. With this breakthrough, he helped initiate the Human Genome Project in 1984. This proposal aimed to sequence an entire human haploid genome at $1 per base, requiring a total budget of $3 billion. This quickly played out into the well-known race between Celera and UCSC-Broad-Sanger. Although the latter barely won in the end, their sequence had many errors and gaps, whereas Celera’s version was much higher quality. Celera initially planned on releasing the genome in 50 kb fragments, which researchers could perform alignments on, much like BLAST. Church once approached Celera’s founder, Craig Venter, and received a promise to obtain the entire genome on DVD after release. However, questioning the promise, Church decided instead to download the genome directly from Celera by taking advantage of the short fragment releases. Using automated crawl and download scripts, Church managed to download the entire genome in 50 kb fragments within three days!

## **34.3 Personal Genomes**

In 2005, George Church initiated the Personal Genome Project [2]. Now that sequencing costs have rapidly decreased to the point that we can currently get the entire diploid human genome for $4000 (compare to $3 billion for a haploid human genome in the Human Genome Project), personal genome and sequence information is becoming increasingly affordable.

One important application for this information is in personalized medicine. Although many diseases are still complicated to predict, diagnose, and study, we currently already have a small list of diseases that are highly predictable from genome data. Examples include phenylketonuria (PKU), BRCA-mutation-related breast cancer, and hypertrophic cardiomyopathy (HCM). Many of these and similar diseases are uncertain (sudden onset without warning symptoms) and not normally checked for (due to their relative rareness). As such, they are particularly suitable as targets for personalized medicine by personal genomes, because genomic data provide accurate information that otherwise cannot be obtained. Already, there are over 2500 diseases (due to _∼_ 6000 genes) that are highly predictable and medically actionable, and companies such as 23andMe are exploring these opportunities.

As a final remark on the subject, Church remarked on some of his personal philosophy regarding personalized medicine. He finds many people reluctant to obtain their genomic information, and attributes this to a negative view among the general public toward GWAS and personalized medicine. He thinks that the media focuses too much on the failure of GWAS. The long-running argument against personalized medicine is that we should focus first on common diseases and variants before studying rare events. Church counterargues that in fact there is no such thing as a common disease. Phenomena such as high blood pressure or high cholesterol only count as symptoms; many ‘common diseases’ such as heart disease and cancer have many subtypes and finer categories. All along, lumping these diseases into one large category only has the benefit of teaching medical students and to sell pharmaceuticals (e.g., statins, which have fared well commercially but only benfit very few). Church argues that lumping implies a loss of statistical power, and is only useful if it is actually meaningful. Ultimately, everyone dies due to their own constellation of genes and diseases,

510

6.047/6.878 Lecture 26: Personal Genomes, Synthetic Genomes, Computing in C vs. Si

so Church sees that splitting (personalized genomics) is the way to proceed.

Personal genomics provide information for planning and research. As a business model, it is analogous to an insurance policy, which provides risk management. As an additional benefit however, the information received allows for early detection, and consequences may even be avoidable. Access to genomic information allows one to make more informed decisions.

## **34.4 Current Research Directions**

## **34.5 Further Reading**

Personal Genome Project: `http://www.personalgenomes.org/`

## **34.6 Tools and Techniques**

## **34.7 What Have We Learned?**

## **Bibliography**

- [1] Peter A. Carr and George M. Church. Genome engineering. _Nature biotechnology_ , 27(12):1151–1162, December 2009.

- [2] G. M. Church. The Personal Genome Project. _Molecular Systems Biology_ , 1(1):msb4100040–E1– msb4100040–E3, December 2005.

- [3] G. M. Church and W. Gilbert. Genomic sequencing. _Proceedings of the National Academy of Sciences of the United States of America_ , 81(7):1991–1995, April 1984.

511

6.047/6.878 Lecture 26: Personal Genomes, Synthetic Genomes, Computing in C vs. Si

512

CHAPTER

## **THIRTYFIVE**

## PERSONAL GENOMICS

Deniz Aksel, Molly Schmidt, Jonathan Uesato

### **Figures**

|35.1 Factors that contribute to the probability of getting a disease. Each relationship shown<br>represents correlation except for the link between genome and disease. Correlation does<br>not mean causality, but we can use the genome to resolve causality.<br>. . . . . . . . . . . .|512|
|---|---|
|35.2 SNPs associated with Mendelian diseases often lie in coding regions whereas those asso-<br>ciated with polygenic diseases are usually found in non-coding regions. This is because<br>large effect variants, protein coding variants, associated with Mendelian diseases are at low<br>frequencies due to selection. Common variants associated with polygenic diseases, tend to<br>have a lower effect, so selection does not play as big of a role. . . . . . . . . . . . . . . . .|513|
|35.3 The multiple factors and datasets in determining the role of methylation on disease states,<br>and methods for linking these datasets.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|515|
|35.4 Modeling Human Disease<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|517|
|35.5 Polygenic Risk Prediction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|518|


## **35.1 Introduction**

Personalized genomics focuses on the analysis of individuals'genomes and their predispositions for diseases rather than looking at the population level. Personalized medicine is only possible with information about genetics along with information about many other factors such as age, nutrition, lifestyle, or epigenetic markers (such as methylation). To make personalized medicine more of a reality, we need to learn more about the causes and patterns of diseases in populations and individuals.

513

6.047/6.878 Lecture 29: Personal Genomics

## **35.2 Epidemiology: An Overview**


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 35.1: Factors that contribute to the probability of getting a disease. Each relationship shown represents correlation except for the link between genome and disease. Correlation does not mean causality, but we can use the genome to resolve causality.

Epidemiology is the study of patterns, causes, and effects of health and disease conditions in defined populations. In order to talk about epidemiology, we need to first understand some basic definitions and terms: **Morbidity level** is how sick an individual is whereas mortality is whether an individual is dead or not. The **incidence** is a rate which describes the number of new cases/people with a disease that appears during a period of time. The **prevalence** is the total steady state number of cases in the population. The **attributable risk** is the difference in rate of a disease between those exposed to the disease and those not exposed to the disease. **Population burden** refers to the years of potential life lost (YPLL), quality-adjusted or disability-adjusted life year (QALY/DALY). **Syndrome** refers to co-occurring signs or symptoms of a disease that are observed. The **prevention challenge** is to determine a disease and its cause and understand whether, when, and how to intervene.

In order to determine disease causes, studies must be designed according to certain principles of experimental design. These principles include control, randomization, replication, grouping, orthogonality, and combinatorics. Control groups are needed so that comparison to a baseline can be done.The placebo effect is real, so having a control group is necessary. The people who get the putative treatment being tested must also be random so that there is no bias. The study needs to be replicated as well in order to control for variability in the initial sample. (This is similar to the winners curse. Someone may win a race because they did outstanding in that particular round and surpassed their personal average, but in the next round they probably will regress back to performing close to their average.) Understanding variation between different subgroups may also play a large role in the outcomes of experiments. These may include subgroups based on age, gender, or demographics. One subgroup of the population may be contributing in a more profound way then they rest, so looking at each subgroup specifically is important. Orthogonality, or the combination of all factors and treatments, and combinatorics, factorial design, must also be taken into account when designing an experiment. With disease studies in particular, ethics when dealing with human subjects must be taken into account. There are legal and ethical constraints which are overseen by review boards. Clinical trials must be performed either blind (patient does not know if they are getting treatment or not) or double-blind (doctor also doesnt know). A patient who knows if they have gotten a treatment may change their habits causing bias, or a doctor who knows a patient got the treatment may treat them differently or analyze their results differently. Both considerations need to be taken into account to lower the bias that may cause different results of a clinical trial.

**Example** An example of the need for a randomized control trial is the treatment of ebola. A treatment must be distributed randomly to individuals being treated in different hospitals and it must be blind. If

514

6.047/6.878 Lecture 29: Personal Genomics

someone believes they are getting the vaccine, they may alter their habits to protect themselves which may affect the outcome. If only patients of one hospital get the vaccine, there is a possibility that the effects seen are just from that hospital being more careful.

## **_FAQ_**

- **Q:** In poorly designed experiments, is there one aspect that is most commonly overlooked?

- **A:** The most commonly missed is subgroup structure. It is sometimes not obvious what the different subgroups could be. To help with this, researchers can look at general properties of a predictor by trying to cluster cases and controls independently and visualize the clustering. If there is substructure other than case/control in the clustering, researchers can look for variables within each cluster to see what is driving substructure.

## **35.3 Genetic Epidemiology**

Genetic epidemiology focuses on the genetic factors contributing to disease. Genome-Wide association studies (GWAS), previously described in depth, identify genetic variants that are associated with a particular disease while ignoring everything else that may be a factor. With the decrease of whole genome sequencing, these types of studies are becoming much more frequent.


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 35.2: SNPs associated with Mendelian diseases often lie in coding regions whereas those associated with polygenic diseases are usually found in non-coding regions. This is because large effect variants, protein coding variants, associated with Mendelian diseases are at low frequencies due to selection. Common variants associated with polygenic diseases, tend to have a lower effect, so selection does not play as big of a role.

In genetic epidemiology there are many genetic factors that you can test to identify diseases in a particular individual. You can look at family risk alleles which are inherited with a common trait in specific genes or variants. You can study monogenic, actionable protein-coding mutations which are the most understood, would have the highest impact, and would be the easiest to interpret. There is the possibility of testing all coding SNPs (single nucleotide polymorphisms) with a known disease association. There are debates over whether a patient needs to or would want to know this information sometimes especially if the disease is not

515

6.047/6.878 Lecture 29: Personal Genomics

treatable. A person’s quality of life may decrease just from knowing they may have the untreatable disease even if no symptoms are exhibited. You can also test all coding and non-coding associations from GWAS, all common SNPs regardless of association to any disease, or the whole genome.

## **_Did You Know?_**

23andMe is a personal genomics company that offers saliva-based direct-to-consumer genome tests. 23andMe gives consumers raw genetic data, ancestry-related results, and estimates of predisposition for more than 90 traits and conditions. In 2010, the FDA notified several genetic testing companies, including 23andMe, that their genetic tests are considered medical devices and federal approval is required to market them. In 2013, the FDA ordered 23andMe to stop marketing its Saliva Collection Kit and Personal Genome Service (PGS) as 23andMe had not demonstrated that they have “analytically or clinically validated the PGS for its intended uses” and the “FDA is concerned about the public health consequences of inaccurate results from the PGS device” [ **?** ]. The FDA expressed concerns over both false negative and false positive genetic risk results, saying that a false positive may cause consumers to undergo surgery, intensive screening, or chemoprevention in the case of BRCA-related risk, for example, while a false negative may prevent consumers from getting the care they need. In class, we discussed whether people should be informed about potential risk alleles they may carry. Often, people may misunderstand the probabilities provided to them and either underestimate or overestimate how concerned they should be. The argument was also raised that people should not be told they are at risk if there is nothing current medicine and technology can do to mitigate the risk. If people are going to be informed about a risk, the risk should be actionable; i.e. they should be able to do something about it, instead of just live in worry, as that added stress may cause other health problems for them.

Not only is there the choice of what to test, there is the question of when to test someone for a particular condition. Diagnostic testing occurs after symptoms are displayed in order to confirm a hypothesis or distinguish between different possibilities of having a condition. You can also test predictive risk which occurs before symptoms are even shown by a patient. You may test newborns in order to intervene early or even do pre-natal testing via an ultrasound, maternal serum, probes or chorionic villus sampling. In order to test which disorders you may pass on to your child, you can do pre-conception testing. You can also do carrier testing to determine if you are a carrier of a particular mutant allele that may run in your family history. Testing genetics and biomarkers can be tricky because it can be unknown if the genetics or biomarker seen is causing the disease or is a consequence of having the disease.

To interpret disease associations, we need to use epigenomics and functional genomics. The genetic associations are still only probabilistic: if you have a genetic variant, there is still a possibility that you will not get the disease. Based on Bayesian statistics however, the posterior probability increases if the prior increases. As we find more and more associations and variants, the predictive value will increase.

## **35.4 Molecular Epidemiology**

Molecular Epidemiology involves looking at the molecular biomarkers of a disease state. This includes looking at gene expression profiles, DNA methylation patterns i.e. epigenomics, and chromatin structure and organization in specific cell types. In earlier chapters, we discussed the link between gene expression (as RNA or proteins) and SNPs in the context of eQTL studies. As a reminder, eQTLs (expression quantitative trait loci) seek linear correlations between gene expression levels and different variants of a genetic locus.

516

6.047/6.878 Lecture 29: Personal Genomics

This section will focus on understanding the the role of **epigenomic markers** as molecular indicators of a disease. It is important to understand that multiple factors, and thus multiple datasets come into play in understanding the epigenomic basis of disease: methylaytion patterns of sample patients (M), genomic information (G) for the same individuals, enviornmental data (E, covering covariates like age, gender, smoking habits etc.), and phenotype quantifications (P, can capture multiple phenotypic markers, for example in Alzheimer’s Disease, the number of neuronal plaques per patient). Furthermore, we need to understand the various interconnections and dependencies between these data sets to make meaningful conclusions about the influence of methylation for a certain disease.

To remove experimental, technical or environmental covariants, we rely on either known, or ICA (Independent component analysis)-inferred corrections. To link genetic data to methylation patterns, we look for meQTLs (methylation quantitative trati loci), which is equivalent to eQTLs. Molecular phenotypes such as expression level or methylation level are also quantitative traits. Finally, to link methylation patterns with diseases, we implement EWAS (Epigenome-wide association studies).


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 35.3: The multiple factors and datasets in determining the role of methylation on disease states, and methods for linking these datasets.

### **35.4.1 meQTLs**

The discovery of meQTLs follows a process that is highly similar to the methodology used for discovering eQTLs. To discover cis-meQTLs (i.e. meQTLs where the effect on methylation is proximal to the tested locus) we select a genomic window, and use a linear model to test whether or not we see a correlation between methylation and SNP variants in that region. We test to see if the correlation is significant via an F-test, where our null hypothesis is that the additional model complexity introduced via the genomic information does not explain a significant portion of variation in methylation patterns. Other methods of discovering meQTLs include permutation and Linear Mixed Models (LMM).

**Example** An example of using meQTLs in discovering the connection between methylation, genotype, and disease is the Memory and Aging Project. 750 elderly people enrolled in the project many years ago and

517

6.047/6.878 Lecture 29: Personal Genomics

today, they have mostly died and given their brain to science. The genotype and methylation of the dorsal lateral prefrontal cortex were determined in order to study the connection between methylation and the phenotype of Alzheimer’s and how the genotype may affect the methylation profile. SNP data, methylation, environmental factors (such as age, gender, sample batch, smoking status, etc..), and phenotype were taken into account. First covariants needed to be discovered and excluded to make sure the results obtained are not due to confounding factors. This is done by decomposing the matrix of methylation data by doing ICA. This enables the discovery of variables that are driving the most variability in the trait. The batch sample and cell mixture can have the biggest effect in the variation between individuals. After this is corrected for, linear models, permutation tests, and linear mixed models are used to determine cis-meQTLs–how much the genotype explains the methylation level.

### **35.4.2 EWAS**

Epigenome-Wide Genome Studies (EWAS) aim to find connections between the methylation pattern of a patient and their phenotype. Much like GWAS, EWAS relies on linear models and p-value testing for finding linkages between epigenomic profiles and disease states. Together with meQTLs, EWAS can also potentially shine light on whether a given methylation pattern is the cause or result of a disease. Ideally, the idea is to be able to generate models that allow us to predict disease states (phenotypes) based on methylation.

There are some drawbacks to EWAS. First, the variance in methylation patterns due to phenotype is typically very small, making it difficult to link epigenomic states to disease states, similar to seeking a needle in a haystack. To improve this situation, we need to control for other sources of variance in our methylation data, such as gender, age etc. Gender, for example, incorporates a large variance for the case of Alzheimer’s Disease. We additionally need to account for variance due to genotype (in the form of meQTLs). Additionally, variability across samples is a major issue in collecting methylation data for EWAS[ **?** ]. As different cell types in the same individual will have different epigenomic signatures, it is important that relevant tissue samples are collected, and the data is corrected for the different cell/tissue types involved in a study.

## **35.5 Causality Modeling and Testing**

A central question for personal genomics is the question of which markers are causal of disease. For example, one might ask whether methylation at a certain loci, or a certain histone modification, increases a person’s risk for a certain disease. This question is difficult because we need to separate spurious correlations from causal effects - for example, it is possible that a mutation elsewhere in the genome causes the disease, and also increases the chance of observing a particular marker, but that the marker has no causal effect on the disease. In this case, we would find a correlation between the disease phenotype and the presence of the marker despite the lack of any causal effect.

The key insight that allows us to determine causal effects, as opposed to mere correlations, is the observation that while the genotype may influence a person’s risk for a particular disease, the disease will not modify a person’s genotype. This allows us to use genotype as an instrumental variable for methylation. This limits the number of possible models so that we can statistically test which model is most consistent with the observed data.

518

6.047/6.878 Lecture 29: Personal Genomics

There are three possibilities for modeling complex human diseases: the independent associations model, the interaction model, and the causal pathway model, depicted in Figure 35.4. We will use the example of studying the causal relationship between methylation at a certain loci and disease to demonstrate how to test for a causal effect.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

#### Figure 35.4: Modeling Human Disease

Under the independent associations model, the data should contain no correlation between the genotype and the disease, which distinguishes this model from the interaction and causal pathway models. However, there will be correlations between each of the factors and the disease separately. Thus, this model is straightforward to test for. An example of this would be two independent risk genes.

Under the interaction model, factor Bs effect on a disease may vary depending on the value for A. For example, a drugs effect on someone can be different based on their genotype. To test for this, we determine the statistical significance of the effect of the interaction term, _β_ 2, in the regression _D_ = _β_ 0 _A_ + _β_ 1 _B_ + _β_ 2 _A∗B_ + _c_ . If there is a significant interaction effect, we can isolate the separate effects by stratifyng across different levels of A.

The causal pathway model is a little more complex. If we notice a correlation between a risk factor and a disease, we may wonder whether there is a direct link between risk factor A and a disease, or does the risk factor A affect risk factor B which then affects the disease. In the case that risk factor A only has an effect on the disease through B, we will observe that after conditioning upon B, the correlation between A and D disappears, that is, B “mediates” this interaction. In reality, the effect of A on a disease is usually only partially mediated through B, so we can instead look for if the effect size of A on the disease is decreased when B is observed.

### **35.5.1 Polygenic Risk Prediction**

One of the most central questions of personal genomics is prediction of genetic predispositions to various genetic traits, using multiple genes to inform our predictions. The basic approach is explained in Figure 35.5. First, the data set is divided into a training and test set, and in the training cohort, we select which SNPs are most important and their appropriate weightings. Then we use the test set to evaluate the accuracy of our predictions. Finally, we use this model to predict genetic predispositions for the target cohort by using the confidences we determined from the test set.

519

6.047/6.878 Lecture 29: Personal Genomics


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 35.5: Polygenic Risk Prediction

## **35.6 Current Research Directions**

- **35.7 Further Reading**

- **35.8 Tools and Techniques**

## **35.9 What Have We Learned?**

In this section we have learned about the basics of epidemiology, both genetic and molecular. We have learned techniques of designing an epidemiological experiment and how and when to use genetic screens for identifying diseases. Lastly, we focused on resolving causality vs. correlation between epigenetic markers and diseases using genetics as an instrument variable.

## **Bibliography**

520

CHAPTER

**THIRTYSIX**

CANCER GENOMICS

Pasha Muravyev (2014)

## **36.1 Introduction**

What is cancer? Cancer represents a group of diseases or tumors that trigger abnormal cell growth and have the potential to spread to many parts of the body. A cancer usually starts with mutations in one or more ”driver genes” which are genes that can drive tumorigenesis. These mutations are called driver events, meaning that they provide a selective fitness advantage for the individual; other mutations that don’t provide a fitness advantages are called passenger mutations.

The main objective of cancer genomics is to generate a comprehensive catalog of cancer genes and pathways. Many cancer genome projects have been started within the last ten years (mainly due to the drop in genome sequencing costs); for example, the Cancer Genome Atlas was started in 2006 with the aim of analyzing 20-25 tumor types with 500 tumor / normal pairs each via a large number of experiments (SNP arrays, whole-exome sequencing, RNA seq, and others). The ICGC (international cancer genome consortium) is a bigger, umbrella organization that organizes similar projects around the world with the end goal of studying 50 tumor types with 500 tumor/normal types each.

## **36.2 Characterization**

For each tumor, our aim is to obtain a complete, base-level characterization of that tumor, its evolutionary history and the mechanisms that shaped it. We can use _massivelyparallelsequencing_ to get the base level genome characterization, but this approach brings with it some associated challenges.

521

6.047/6.878 Lecture 24: Cancer Genomics

1. Massive amounts of data The main challenge with increased amounts of data is an increase in the computational power required to analyze this data, as well as storage costs associated with keeping track of all of the sequenced genomes. There also needs to be an analysis pipeline (automated, standardized, reproducible) to have consistent findings across the different characterization efforts. Finally, we need to come up with new ways of visualizing and reporting on large scale data.

2. Sensitivity / Specificity Cancer characterization starts with the proper identification of SNP mutations present in cancer cells, and maximal removal of false positive reads. When selecting tumor samples, the extracted DNA is a mix of normal genomes and complex tumor genomes. The mutational allelic fraction (the fraction of DNA molecules from a locus that carry a mutation), is used to study significance of a mutation and its prevalence in the cancer subtype. This fraction depends on the purity, local copy number, multiplicity of the tumor sample, and the cancer cell fraction (CCF, amount of cancer cells that carry the mutation). Clonal mutations are carried by all cancer cells, and sub-clonal mutations are carried by a subset of the tumor cells.

As well as detecting the presence of clonal and subclonal mutations, proper analysis requires removal of false positive mutagenic events. Two types of false positives include sequencing errors and germline mutations. Sequencing errors can come from misread bases, sequencing artifacts, and misaligned reads, while germline mutations usually occur in predicable places in the genome (1000/MB known, 10-20/MB novel). By having multiple reads of the same sequence the likelihood of repeated errors in sequencing drops rapidly, and by knowing where in the genome a germline mutation is likely, a filter can correct for the additional false positive probability. The overall sensitivity of detecting single nucleotide variations depends on the frequency of background mutations and the number of alternative reads.

A third type of false positive can come from cross patient contamination if the tumor sample contains DNA from another person. ContEst is a method to accurately detect contamination by comparison to a SNP array.

A mutation caller is a classifier asking at every genomic locus, Is there a mutation here?. These classifiers are evaluated using many Receiver Operators Characteristic (ROC) curves, which depend on the allele fraction, coverage of tumor and normal sample, and sequencing and alignment noise. MuTect is a highly sensitive Somatic Mutation Caller. The MuTect pipeline is as follows: Tumor and normal samples are passed into a variant detection statistic (which compares the variant model to the null hypothesis), which is passed through site-based filters (proximal gap, strand bias, poor mapping, triallelic site, clustered position, observed in control), then compared to a panel of normal samples, and finally classified as candidate variants. MuTect can detect low allele fraction mutations and is thus suited for studying impure and heterogenous tumors.

3. Discovering mutational processes

Instead of detecting the presence of mutations in cancer genes, a different approach could be to discover if there were specific patterns among mutations in the cancer samples. A ”Lego plot” is a way to visualize patterns of mutations, in which the heights of each of the colors represents frequencies of the 6 types of base pair substitutions, and the frequency of each is plotted relative to the 16 different contexts this mutation could occur in (neighboring nucleotides). The specific types of mutagenic events in each type of cancer can be plotted and analyzed. As an example, a novel mutation pattern (AA ¿ AC) is found in esophageal cancer. Cancers can be grouped by these specific mutational spectra. Dimensionality reductions using non-negative Matrix Factorization (NMF) of lego plot data can be used to identify fundamental spectral signatures.

4. Estimating purity, ploidy and cancer cell functions

522

6.047/6.878 Lecture 24: Cancer Genomics

As well as detecting mutations in cancer cells, removing false positives, and detecting patterns of mutations, a proper characterization of each tumor sample is required. Because of heterogeneity and sample impurities, estimating the purity, absolute copy number and cancer cell fraction (CCF) of the tumor sample being sequenced is needed to get correct total number and prevalence of the mutated alleles.

5. Tumor heterogeneity and evolution

Samples can have large distributions of point mutations and copy number alterations, but a Bayesian clustering algorithm can help identify the mutations and copy number alterations in distinct subpopulations.

## **36.3 Interpretation**

The fundamental challenge in interpreting the sequencing results lies in differentiating driver mutations from passenger mutations. In order to accomplish this, we need to model the background mutational processes of the analyzed sequences and identify pathways/regions with more mutations than would have been predicted solely by the background model. Those regions then become our candidate cancer genes.

However, we run into the potential issue of selecting an incorrect background model or we can encounter systematic artifacts in mutation calling. In this case, we have to go back to the drawing board and attempt to come up with a better background model before we can proceed with candidate gene idetification.

Many tools have been developed in an effort to accurately detect candidate cancer genes and pathways (sub-networks) including NetSig, GISTIC, and MutSig. NetSig is used to identify clusters of mutated genes in protein-protein interaction networks. GISTIC can be used to score regions according to frequency and amplitude of copy-number events. MutSig: is used to score genes according to number and types of mutations. The main analysis steps in finding candidate cancer genes are 1) estimation of the background mutation rate (which varies across samples, 2) calculate p-values based on statistical models, and 3) correct for multiple testing hypothesis (N genes).

As sample size and or mutation rate increases, the significant gene list for cancer genes increases and contains many fishy genes. One major breakthrough to reduce fishy genes has been the proper modeling of background mutations. Standard tools use consistent background rate (rates for CpG, C/G, A/T, indel) while ignoring heterogeneity across samples, additional sequence contexts, and the genome. But it was discovered that the mutation rate across cancer varies ¿1000 fold, mutation rate is lower in highly expressed genes, and the frequency of somatic mutations correlates with DNA replication time. There are more mutations in areas of the genome that replicate later than those which divide early. MutSigCV is a tool which corrects for this variation in background mutation rates.

## **36.4 Current Research Directions**

There are a few holes in the current library of cancer genes including those which appear in intergenic regions. Classification of pan-cancer mutations is thought to be required in order to find more non-coding mutations.

523

6.047/6.878 Lecture 24: Cancer Genomics

## **36.5 Further Reading**

1. http://www.broadinstitute.org/cancer/cga/mutect

2. http://www.broadinstitute.org/cancer/cga/ABSOLUTE

## **36.6 Tools and Techniques**

## **36.7 What Have We Learned?**

The drop in sequencing costs over the last ten years has led to a need for automized analysis pipelines and more computational / storage power to handle the vast flood of data being generated by a multitude of parallel sequencing efforts. Two major tasks of cancer genome projects going forward can be roughly grouped into two areas: characterization and interpretation.

For characterization, there seems to still a need for a systematic benchmark of analysis methods (one example is ROC curves - curves that illustrate the performance of a classifier with a varying discrimination threshhold). We saw that cancer mutation rates tend to vary more than 1,000-fold across different tumor types. We also learned that clonal and subclonal mutations could be used for studying tumor evolution and heterogeneity.

Running a significance analysis on the sequencing results identified a long-tailed distribution of significantly mutated genes. Since we’re dealing with a long tail distribution, we can increase the predictive power of our models and detect more cancer genes by integrating multiple sources of evidence. However we have to take into account that mutation rates differ according to the original sample, gene, and category from each study.

## **Bibliography**

524

CHAPTER

**THIRTYSEVEN**

GENOME EDITING

## **37.1 Introduction**

### **37.1.1 What is CRISPR/Cas?**

The **C** RISPR/Cas system is the prokaryotic immune system. When a virus or other foreign attacker attempts to infect a prokaryotic cell and inject its own DNA into a prokaryote’s genome, the prokaryote’s CRISPR/Cas system is responsible from removing the foreign DNA. How does it do this? The CRISPR/Cas system has two parts, CRISPR and Cas. The CRISPR part (a CRISPR array), is responsible for ”remembering” the foreign DNA, while the Cas part (Cas proteins), is responsible for cutting out the recogined foreign DNA. A CRIPSR array is made up of segments of short spacer DNA, which are the results of previous exposure to foreign DNA. These spacer DNA are transcribed to RNAs, which can be used to match the foregin DNA that the spacer DNA was built from. These RNA are then picked up by Cas proteins. When a Cas protein picks up a particular RNA, it becomes sensitive to the matching DNA sequences. The next time the same foreign DNA is inserted into the prokaryote, the Cas proteins sensitive to it will match the foreign DNA and cut it out of the genome, causing it to become inactive.

### **37.1.2 Why is CRISPR/Cas important to us?**

Because nature is giving us an effective way of editing a genome! In order to accurately edit a genome, it is important to be able to cut a sequence at precisely the targeted location. Once a cut is made, repair mechanism can go in and make a modification at the target site. The CRISPR/Cas system is a naturally occurring time tested method of doing making alterations to DNA sequences.

Currently, the ability of researchers to perturb and interrogate the genome is lagging behind the current level

525

6.047/6.878 Lecture 9: Genome Editing

of techniques for reading. CRISPR provides an effective way to write to the genome that we are capable of reading, allowing us to determine what variations in the genetic code give rise to diseases of interest.

### **37.1.3 Cas-9**

The CRISPR/Cas-9 system is a system that has been of particular interest. Cas-9 is a endonuclease that can trigger gene repair by making cuts at specific target sites, guided by a 20-nucleotide sgRNA. When a target site that is complementary to the guide sgRNA is found and is followed by a NGG PAM region, the Cas-9 protein will cut the DNA at that target site. By programming Cas-9 with specific sgRNA, it can be programmed to create double stranded breaks at specific targets, while the PAM region plays a role in prevent targeting of its own genome. Cas-9 has been shown to be much more efficient at targeting than more established methods. Unfortunately, one drawback of Cas-9 is that it might make cuts at off-target sites that aren’t fully complementary to the RNA guide, which makes it a challenge for accurate genome editing.

## **37.2 Current Research Directions**

### **37.2.1 Improvement of Cas-9**

Recent research has produced a variant of Cas-9 that greatly improves the specificity of Cas-9, reducing the likeliness of offsite errors.

### **37.2.2 Current research being done with CRISPR/Cas-9**

The recent improvement of Cas-9 has opened new pathways of research. For example, it can be used to analyze the functions of specific genes by using CRISPR/Cas-9 to remove just that gene and observing the effect of the removal. One example of an application of this is in the study of melanoma cancer cells.

Vemurafenib is a FDA approved drug for treating melanoma, and has been shown to be effective on melanoma cells that have a V600E BRAF mutation by interrupting the BRAF pathway and inducing programmed cell death.

Unfortunately, in many cases the cancer will become resistant to the drug by creating alternative survival pathways. CRISPR/Cas-9 can be used to determine the genes that allow the cancer cells to develop alternative pathways. By programming Cas-9 proteins to target every gene individually and tagging the proteins so it is possible to determine which protein affected which cell, it is possible to determine the genes that are required for survival.

526

6.047/6.878 Lecture 9: Genome Editing

## **37.3 Further Reading**

- **37.4 Tools and Techniques**

## **37.5 What Have We Learned?**

CRISPR/Cas-9 produces double stranded breaks in DNA, and has two main components:

20bp DNA

PAM

## **Bibliography**

527

6.047/6.878 Lecture 9: Genome Editing

528

MIT OpenCourseWare http://ocw.mit.edu

6.047 Computational Biology Fall 2015

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Part V](10-part-v.md) · [Up: contents](index.md)

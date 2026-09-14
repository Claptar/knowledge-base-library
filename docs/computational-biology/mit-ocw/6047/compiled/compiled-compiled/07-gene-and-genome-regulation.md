---
title: Gene and Genome Regulation
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/compiled/compiled-compiled.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Gene and Genome Regulation

**Source:** `compiled/compiled-compiled.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

219

CHAPTER

**FOURTEEN**

MRNA SEQUENCING FOR EXPRESSION ANALYSIS AND TRANSCRIPT DISCOVERY

Guest lecture by Manuel Garber

### **Figures**

|14.1 Figure 1: Expression microarray process . . . . . . . . . . . . . . . . . . . . . . . . . . . .|220|
|---|---|
|14.2 Spaced k-mer method of mapping reads to reference genome . . . . . . . . . . . . . . . . .|221|
|14.3 Box 1: How Do We Calculate qMS?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|222|
|14.4 Figure 3: Reconstruction works by determining, for a particular window, the probability of<br>observing that number of reads (top left) given the uniform distribution of the total reads<br>(bottom left). This probability follows the Poisson distribution. . . . . . . . . . . . . . . .|222|
|14.5 Figure 4: Process for reconstructing genome based on reads, using the scan distribution .|223|
|14.6 Figure 5: Alternative isoforms present a challenge for reconstruction, which must depend<br>on exon junction spanning reads<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|223|
|14.7 Box 2: The Scripture Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|224|


## **14.1 Introduction**

The purpose of mRNA sequencing (RNA-seq) is to measure the levels of mRNA transcripts for every gene in a given cell. mRNA sequencing was a daunting task, and requires approximately 40 million aligned reads in order to accurately measure mRNA transcripts.This did not become possible until 2009, when next-generation sequencing technologies became more advanced and efficient.

In this chapter, we will explore the different techniques for using mRNA sequencing data to aid in gene and transcript discovery as well as in expression analysis.

221

6.047/6.878 Lecture 11: mRNA sequencing for Expression Analysis and Transcript discovery

## **14.2 Expression Microarrays**

Prior to the development of mRNA sequencing technology, mRNA levels were measured using expression microarrays. These microarrays function by inserting a DNA probe on a slide and measuring the levels transcripts that undergo complimentary hybridization with the DNA, a process that could analyze expression on a gene by gene basis (Figure 1).


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 14.1: Figure 1: Expression microarray process

However, this technology has several limitations: it cannot distinguish mRNA isoforms, it cannot analyze on the sequence, or digital level, it can only measure known transcripts, and the expression measurements become less reliable for highly saturated transcript levels.

## **14.3 The Biology of mRNA Sequencing**

The first step in mRNA sequencing is to lyse the cells of interest. This creates a mass of proteins, nucleotides, and other molecules which are then filtered through so that only RNA (or specifically mRNA) molecules remain. The resulting transcripts are then fragmented into reads 200-1000 base pairs long and undergo a reverse transcription reaction to build a strand-specific DNA library. Finally, both ends of these DNA fragments are sequenced. After establishing these sequenced reads, the computational part of RNA-Seq can be divided into three parts: read mapping, reconstruction, and quantification.

## **14.4 Read Mapping - Spaced Seed Alignment**

The idea behind read mapping is to align the sequenced reads to a reference genome. Sequence alignment algorithms discussed in earlier chapters will not work for this case due to the scale of the problem. The goal is to align millions of reads to the genome and would take too long if each was aligned individually. Instead, we will introduce the Spaced Seed Alignment approach. This process begins by using the reference genome to creating a hash table of 8-mers, which do not have to be contiguous. The positions of these stored spaced seeds are mapped to the hash table. Using these spaced 8-mers, each read is then compared with each possible position in the reference genome and scored based on the number of base pair matches (Figure 2).

More accurately, for each position, it is possible to calculate the score using the equation _qMS_ = _−_ 10 log10(1 _− P_ ( _i|G, q_ )), where _P_ ( _i|G, q_ ) represents the probability that the read, q, is mapped to position i of reference genome G. More details on deriving this score can be found in Figure 13.2.

It is possible to adjust the parameters of this method in order to alter the sensitivity, speed, and memory

222

6.047/6.878 Lecture 11: mRNA sequencing for Expression Analysis and Transcript discovery


Figure 14.2: Spaced k-mer method of mapping reads to reference genome

of the algorithm. Using smaller k-mer seeds allows for less precise base pair matching (greater sensitivity), but requires more matches to be attempted. Smaller seeds take up less memory, while larger seeds run faster.

There exist methods other than the one described above to perform this alignment. The most popular of which is the Burrows-Wheeler approach. The Burrows-Wheeler transform is an even more efficient algorithm for mapping reads and will be discussed in a later chapter. It is able to speed up the process of finding matches in the large genome by reordering the genome in a very specific permutation. This allows reads to be matched solely as a function of the length of the read and not the genome. As better sequencing technology allows for larger read lengths, more algorithms will need to be developed to handle the extra processing.

Unlike ChIP-Seq, a similar technology, RNA-seq is more complex. This is because the read mapper needs to worry about small exons interspersed between large introns and be able to find both sides of an exon. This complexity can be overcome by using the above mentioned spaced seed matching technique, and detecting when two k-mers from the same read are separated by a long distance. This would signal a possible intron and can be fixe by then extending the k-mers to fill in gaps (SNO methods). Another method is to base the alignment on contiguous reads, which are further fragmented into 20-30 bp regions. These regions are remapped, and the positions with two or more different alignments are marked as splice junctions. Exon-first aligners are faster than the previous methods, but come at a cost: they fail to differentiate psuedogenes, prespliced genes, and transposed genes.

## **14.5 Reconstruction**

Reconstruction of reads is a largely statistical problem. The goal is to determine a score for each fixed-sized window in the genome. This score represents the probability of seeing the observed number of reads given the window size. In other words, is the number of reads in a particular window unlikely given the genome? The expected number of reads per window is derived from a uniform distribution based on the total number of reads (Figure 3). This score is modeled by a Poisson distribution.

However, this score must account for the problem of multiple testing hypotheses, due to the approximately 150 million expected bases. One option for dealing with this is the Bonferroni correction, where the nominal

223

6.047/6.878 Lecture 11: mRNA sequencing for Expression Analysis and Transcript discovery

Figure 14.3: Box 1: How Do We Calculate qMS?


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 14.4: Figure 3: Reconstruction works by determining, for a particular window, the probability of observing that number of reads (top left) given the uniform distribution of the total reads (bottom left). This probability follows the Poisson distribution.

p-value = n * p-value. This method leads to low sensitivity, due to its very conservative nature. Another option is to permute the reads observed in the genome, and find the maximum number of reads seen on a single base. This allows for a max count distribution model, but the process is very slow. The scan distribution speeds up this process by computing a closed form for max count distribution to account for dependency of overlapping windows (Figure 4). The probability of observing k reads on a window of size w in a genome of size L given a total of N reads can be approximated by [slide is not clear].

224

6.047/6.878 Lecture 11: mRNA sequencing for Expression Analysis and Transcript discovery


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 14.5: Figure 4: Process for reconstructing genome based on reads, using the scan distribution

Choosing a window size is also an important decision, as genes exist at different expression levels and span different orders of magnitude. Small windows are better at detecting punctuate regions, while larger windows can detect longer spans of moderate enhancement. In most cases, windows of different sizes are used to pick up signals of varying size.

Transcript reconstruction can be seen as a segmentation problem, with several challenges. As mentioned above, genes are expressed at different levels, over several orders of magnitude. In addition, the reads used for reconstruction are obtained from both mature and immature mRNA, the latter still containing introns. Finally, many genes have multiple isoforms, and the short nature of reads makes it difficult to differentiate between these different transcripts. A computational tool called Scripture uses a priori knowledge of fragment connectivity to detect transcripts.

Alternative isoforms can only be detected via exon junction spanning reads, which contain the ends of an exon. Longer reads have a greater chance of spanning these junctions (Figure 5). Scripture works by modeling the reads using graph structure, where bases are connected to neighbor bases, as well as splice neighbors. This process differs from the string graph technique, because it focuses on whole genome, and does not map overlapping sequences directly. When sliding the window, Scripture can jump across splice junctions yet still examine alternative isoforms. From this oriented connectivity graph, the program identifies segments across the graph, and looks for significant segments (Box 2).


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 14.6: Figure 5: Alternative isoforms present a challenge for reconstruction, which must depend on exon junction spanning reads

Direct transcript assembly is another method of reconstruction (as opposed to genome-guided methods like Scripture). Transcript assembly methods are able to reconstruct transcripts from organisms without a reference sequence, while genome-guided approaches are ideal for annotating high quality genomes and expanding the catalog of expressed transcripts. Hybrid approaches are used for lesser quality transcripts or transcriptomes that have underwent major rearrangements, such as those of cancer cells. Popular transcript

225

6.047/6.878 Lecture 11: mRNA sequencing for Expression Analysis and Transcript discovery

assembly tools include Oasis, Trans-ABySS, and Trinity. Another popular genome-guided software is Cufflinks. Regardless of methodology or software type, any sequencing experiment that produces more genome coverage will experience better transcript reconstruction.

Figure 14.7: Box 2: The Scripture Method


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

## **14.6 Quantification**

The goal of the quantification step is to score regions in the genome based on the number of reads. Recall that each transcript is fragmented into many smaller reads. Therefore, it is insufficient to simply count the number of reads per region, as this value would be influenced by (1) expression rates and (2) length of transcript. The higher the expression rate of a transcript the more reads we will have for it. Similarly, the longer a transcript is, the more reads we will have. This issue can be solved by normalizing the number of reads by the length of the transcript and the total number of reads in the experiment. This provides the RPKM value, or reads per kilobase of exonic sequence per million mapped reads.

This method is robust for genes with only one isoform. However, there is the possibility of overlap between conflicting variants of a transcript. When multiple transcript variants are involved, this problem is known as differential expression analysis. There are a few different methods for handling this complexity. The exon intersection model scores only the constituent exons. The exon union model simply scores based on a merged transcript, but can easily be biased based on the relative ratios of each isoform. A more thorough model is the transcript expression model, which assigns unique reads to different isoforms.

226

CHAPTER

**FIFTEEN**

GENE REGULATION 1 –GENE EXPRESSION CLUSTERING

Ge Liu(2015) Shau-Chieh Hsu (2015) Franck Dernoncourt (2012) Arvind Thiagarajan (2011) Tahin Syed (2010) Barrett Steinberg and Brianna Petrone (2009) Mia Y. Qia (2008)

### **Figures**

|15.1 Clustering compared to classification. In clustering we group observations into clusters<br>based on how near they are to one another.<br>In classification we want a rule that will<br>accurately assign labels to new points. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|226|
|---|---|
|15.2 Gene expression values from microarray experiments can be represented as heat maps to<br>visualize the result of data analysis.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|228|
|15.3 RNA-Seq reads mapping to a gene (_c-fos_) and its splice junctions. Densities along exon<br>represent read densities mapping to exons (in log10), arcs correspond to junction reads,<br>where arc width is drawn in proportion to number of reads in that junction. The gene is<br>downregulated in Sample 2 compared to Sample 1. . . . . . . . . . . . . . . . . . . . . . .|228|
|15.4 Transforming Figure 4 to a heatmap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|229|
|15.5 Gene expression level in log value comparison with reference sample<br>. . . . . . . . . . . .|229|
|15.6 A sample matrix of gene expression values, represented as a heatmap and with hierarchal<br>clusters. [1] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|230|
|15.7 Using gene expression matrix to infer more about a disease and gene segment . . . . . . .|230|
|15.8 The k-means clustering algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|231|
|15.9 Examples of final cluster assignments of fuzzy _k_-means using _k_= 4 with centroids, correct<br>clusters, and most probable assigned clusters marked as crosses, shapes of points, and<br>colors respectively. Note that the original data set is non-Gaussian. . . . . . . . . . . . . .|232|
|15.10_K_-Means as a Generative Model. Samples were drawn from normal distributions. . . . . .|233|
|15.11_K_-Means as an expectation maximization (EM) algorithm.<br>. . . . . . . . . . . . . . . . .|234|
|15.12Comparison of clustering, HMM and motif discovery with respect to expectation minimiza-<br>tion (EM) algorithm. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|234|


227

6.047/6.878 Lecture 13: Gene Expression Clustering

|15.13Hierarchical Clustering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|236|
|---|---|
|15.14Distance Metrics for Hierarchical Clustering. Clockwise from top left: minimum, maxi-||
|mum, average distance and centroid distance. . . . . . . . . . . . . . . . . . . . . . . . . .|236|
|15.15Calculation of probability that you have more than _r_ +’s in a randomly selected cluster. .|237|


## **15.1 Introduction**

In this chapter, we consider the problem of discerning similarities or patterns within large datasets. Finding structure in such data sets allows us to draw conclusions about the process as well as the structure underlying the observations. We approach this problem through the application of clustering techniques. The following chapter will focus on classification techniques.

### **15.1.1 Clustering vs Classification**

One important distinction to be made early on is the difference between classification and clustering. **Classification** is the problem of identifying to which of a set of categories (sub-populations) a new observation belongs, on the basis of a training set of data containing observations or instances whose category membership is known. The training set is used to learn rules that will accurately assign labels to new observations. The difficulty is to find the most important features (feature selection).

In the terminology of machine learning, classification is considered an instance of supervised learning, i.e. learning where a training set of correctly-identified observations is available. The corresponding unsupervised procedure is known as **clustering** or cluster analysis, and involves grouping data into categories based on some measure of inherent similarity, such as the distance between instances, considered as vectors in a multidimensional vector space. The difficulty is to identify the structure of the data. Figure 15.1 illustrates the difference between clustering and classification.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 15.1: Clustering compared to classification. In clustering we group observations into clusters based on how near they are to one another. In classification we want a rule that will accurately assign labels to new points.

228

6.047/6.878 Lecture 13: Gene Expression Clustering

### **15.1.2 Applications**

Clustering was originally developed within the field of artificial intelligence. Being able to group similar objects, with full implications of generality implied, is indeed a fairly desirable attribute for an artificial intelligence, and one that humans perform routinely throughout life. As the development of clustering algorithms proceeded apace, it quickly becomes clear that there was no intrinsic barrier involved in applying these algorithms to larger and larger datasets. This realization led to the rapid introduction of clustering to computational biology and other fields dealing with large datasets.

Clustering has many applications to computational biology. For example, let’s consider expression profiles of many genes taken at various developmental stages. Clustering may show that certain sets of genes line up (i.e. show the same expression levels) at various stages. This may indicate that this set of genes has common expression or regulation and we can use this to infer similar function. Furthermore, if we find a uncharacterized gene in such a set of genes, we can reason that the uncharacterized gene also has a similar function through guilt by association.

Chromatin marks and regulatory motifs can be used to predict logical relationships between regulators and target genes in a similar manner. This sort of analysis enables the construction of models that allow us to predict gene expression. These models can be used to modify the regulatory properties of a particular gene, predict how a disease state arose, or aid in targeting genes to particular organs based on regulatory circuits in the cells of the relevant organ.

Computational biology deals with increasingly large and open-access datasets. One such example is the ENCODE project [2]. Launched is 2003, the goal of ENCODE is to build a comprehensive list of functional elements in the human genome, including elements that act at the protein and RNA levels, and regulatory elements that control cells and circumstances in which a gene is active. ENCODE data are now freely and immediately available for the entire human genome: `http://genome.ucsc.edu/ENCODE/` . Using all of this data, it is possible to make functional predictions about genes through the use of clustering.

## **15.2 Methods for Measuring Gene Expression**

The most intuitive way to investigate a certain phenotype is to measure the expression levels of functional proteins present at a given time in the cell. However, measuring the concentration of proteins can be difficult, due to their varying locations, modifications, and contexts in which they are found, as well as due to the incompleteness of the proteome. mRNA expression levels, however, are easier to measure, and are often a good approximation. By measuring the mRNA, we analyze regulation at the transcription level, without the added complications of translational regulation and active protein degradation, which simplifies the analysis at the cost of losing information. In this chapter, we will consider two techniques for generating gene expression data: microarrays and RNA-seq.

### **15.2.1 Microarrays**

Microarrays allow the analysis of the expression levels of thousands of preselected genes in one experiment. The basic principle behind microarrays is the hybridization of complementary DNA fragments. To begin, short segments of DNA, known as probes, are attached to a solid surface, commonly known as a gene chip. Then, the RNA population of interest, which has been taken from a cell, is reverse transcribed to cDNA (complementary DNA) via reverse transcriptase, which synthesizes DNA from RNA using the poly-A tail as a primer. For intergenic sequences which have no poly-A tail, a standard primer can be ligated to the ends

229

6.047/6.878 Lecture 13: Gene Expression Clustering

of the mRNA. The resulting DNA has more complementarity to the DNA on the slide than the RNA. The cDNA is than washed over the chip and the resulting hybridization triggers the probes to fluoresce. This can be detected to determine the relative abundance of the mRNA in the target, as illustrated in figure 15.2.


<!-- Start of picture text -->
Genes<br>Experiments<br>© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

Figure 15.2: Gene expression values from microarray experiments can be represented as heat maps to visualize the result of data analysis.

Two basic types of microarrays are currently used. Affymetrix gene chips have one spot for every gene and have longer probes on the order of 100s of nucleotides. On the other hand, spotted oligonucleotide arrays tile genes and have shorter probes around the tens of bases.

There are numerous sources of error in the current methods and future methods seek to remove steps in the process. For instance, reverse transcriptase may introduce mismatches, which weaken interaction with the correct probe or cause cross hybridization, or binding to multiple probes. One solution to this has been to use multiple probes per gene, as cross hybridization will be different for each gene. Still, reverse transcription is necessary due to the secondary structure of RNA. The structural stability of DNA makes it less probable to bend and not hybridize to the probe. The next generation of technologies, such as RNA-Seq, sequences the RNA as it comes out of the cell, essentially probing every base of the genome.

### **15.2.2 RNA-seq**


<!-- Start of picture text -->
RNA-Seq reads mapped to gene body and splice junctions<br>4.0<br>2.0<br>0.0<br>4.0<br>2.0<br>0.0<br>c-fos<br>chr12<br>© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br>Sample 1<br>Sample 2<br>RNA-Seq read density (log)10<br><!-- End of picture text -->

Figure 15.3: RNA-Seq reads mapping to a gene ( _c-fos_ ) and its splice junctions. Densities along exon represent read densities mapping to exons (in log10), arcs correspond to junction reads, where arc width is drawn in proportion to number of reads in that junction. The gene is downregulated in Sample 2 compared to Sample 1.

RNA-Seq, also known as whole transcriptome shotgun sequencing, attempts to perform the same function that DNA microarrays have been used to perform in the past, but with greater resolution. In particular, DNA microarrays utilize specific probes, and creation of these probes necessarily depends on prior knowledge of the genome and the size of the array being produced. RNA-seq removes these limitations by simply sequencing all of the cDNA produced in microarray experiments. This is made possible by next-generation sequencing

230

6.047/6.878 Lecture 13: Gene Expression Clustering

technology. The technique has been rapidly adopted in studies of diseases like cancer [4]. The data from RNA-seq is then analyzed by clustering in the same manner as data from microarrays would normally be analyzed.

### **15.2.3 Gene Expression Matrices**

Microarrays and RNA-seq are frequently used to compare the gene expression profiles of cells under various conditions. The amount of data generated from these experiments is enormous. Microarrays can analyze thousands of genes, and RNA-seq can, in principle, analyze every gene that is actively expressed. The expression level of each of those genes is measured across a variety of conditions, including time courses, stages of development, phenotypes, healthy vs. sick, and other factors.

To understand what the heatmap of a gene expression matrix (Figure 15.4) convey, we have to first understand what the expression data matrix tells us. By using microarrays and RNA-seq, we can obtain gene expression level in quantitative form in an experiment. If we have multiple experiments, we can construct a value matrix (Figure 15.5) representing a log value of (T/R), where T is the gene expression level in test sample and R is the gene expression level in reference sample.

The Expression Matrix removed due to copyright restrictions.

Figure 15.4: Transforming Figure 4 to a heatmap

If we visualize the matrix as a heatmap, then we obtain the following new colored-matrix:


Figure 15.5: Gene expression level in log value comparison with reference sample

These matrices can be clustered hierarchically showing the relation between pairs of genes, pairs of pairs, and so on, creating a dendrogram in which the rows and columns can be ordered using optimal leaf ordering algorithms.

231

6.047/6.878 Lecture 13: Gene Expression Clustering


Image in the public domain. This graph was generated using the program Cluster from Michael Eisen, which is available from http://rana.lbl.gov/EisenSoftware.htm, with data extracted from the StemBase database of gene expression data.

Figure 15.6: A sample matrix of gene expression values, represented as a heatmap and with hierarchal clusters. [1]

By revealing the hidden structure of a long segment of genome, we obtain great insight of what a fragment of gene does, and subsequently understand more about the root cause of an unknown disease.


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Alizadeh, Ash A., Michael B. Eisen, et al. "Distinct Types of Diffuse Large B-cell Lymphoma Identified by Gene Expression Profiling." _Nature_ 403, no. 6769 (2000): 503-11.

Figure 15.7: Using gene expression matrix to infer more about a disease and gene segment

This predictive and analytical power is increased due to the ability of biclustering the data; that is, clustering along both dimensions of the matrix. The matrix allows for the comparison of expression profiles of genes, as well as comparing the similarity of different conditions such as diseases. A challenge, though, is the curse of dimensionality. As the space of the data increases, the clustering of the points diminishes. Sometimes, the data can be reduced to lower dimensional spaces to find structure in the data using clustering to infer which points belong together based on proximity.

Interpreting the data can also be a challenge, since there may be other biological phenomena in play. For

232

6.047/6.878 Lecture 13: Gene Expression Clustering

example, protein-coding exons have higher intensity, due to the fact that introns are rapidly degraded. At the same time, not all introns are junk and there may be ambiguities in alternative splicing. There are also cellular mechanisms that degrade aberrant transcripts through non-sense mediated decay.

## **15.3 Clustering Algorithms**

To analyze the gene expression data, it is common to perform clustering analysis. There are two types of clustering algorithms: partitioning and agglomerative. Partitional clustering divides objects into nonoverlapping clusters so that each data object is in one subset. Alternatively, agglomerative clustering methods yield a set of nested clusters organized as a hierarchy representing structures from broader to finer levels of detail.

### **15.3.1** **_K_ -Means Clustering**

The _k_ -means algorithm clusters _n_ objects based on their attributes into _k_ partitions. This is an example of partitioning, where each point is assigned to exactly one cluster such that the sum of distances from each point to its correspondingly labeled center is minimized. The motivation underlying this process is to make the most compact clusters possible, usually in terms of a Euclidean distance metric.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 15.8: The k-means clustering algorithm

The k-means algorithm, as illustrated in figure 15.8, is implemented as follows:

1. Assume a fixed number of clusters, _k_

2. _Initialization_ : Randomly initialize the k means _µk_ associated with the clusters and assign each data point _xi_ to the nearest cluster, where the distance between _xi_ and _µk_ is given by _di,k_ = ( _xi − µk_ )<sup>2</sup> .

3. _Iteration_ : Recalculate the centroid of the cluster given the points assigned to it: _µk_ ( _n_ + 1) = � _|xx_<sup>_k_</sup> _<u>i</u> | xi_<sup>_∈k_</sup>

where _xk_ is the number of points with label k. Reassign data points to the k new centroids by the given distance metric. The new centers are effectively calculated to be the average of the points assigned to each cluster.

4. _Termination_ : Iterate until convergence or until a user-specified number of iterations has been reached. Note that the iteration may be trapped at some local optima.

233

6.047/6.878 Lecture 13: Gene Expression Clustering

There are several methods for choosing _k_ : simply looking at the data to identify potential clusters or iteratively trying values for _n_ , while penalizing model complexity. We can always make better clusters by increasing _k_ , but at some point we begin overfitting the data.

We can also think of _k_ -means as trying to minimize a cost criterion associated with the size of each cluster, where the cost increases as the clusters get less compact. However, some points can be almost halfway between two centers, which doesn’t fit well with the binary belonging _k_ -means clustering.

### **15.3.2 Fuzzy** **_K_ -Means Clustering**

In fuzzy clustering, each point has a probability of belonging to each cluster, rather than completely belonging to just one cluster. Fuzzy k-means specifically tries to deal with the problem where points are somewhat in between centers or otherwise ambiguous by replacing distance with probability, which of course could be some function of distance, such as having probability relative to the inverse of the distance. Fuzzy k-means uses a weighted centroid based on those probabilities. Processes of initialization, iteration, and termination are the same as the ones used in k-means. The resulting clusters are best analyzed as probabilistic distributions rather than a hard assignment of labels. One should realize that k-means is a special case of fuzzy k-means when the probability function used is simply 1 if the data point is closest to a centroid and 0 otherwise.


Figure 15.9: Examples of final cluster assignments of fuzzy _k_ -means using _k_ = 4 with centroids, correct clusters, and most probable assigned clusters marked as crosses, shapes of points, and colors respectively. Note that the original data set is non-Gaussian.

The fuzzy k-means algorithm is the following:

1. Assume a fixed number of clusters _k_

2. _Initialization_ : Randomly initialize the _k_ means _µk_ associated with the clusters and compute the probability that each data point _xi_ is a member of a given cluster _k_ , _P_ (point _xi_ has label _k|xi, k_ ).

3. _Iteration_ : Recalculate the centroid of the cluster as the weighted centroid given the probabilities of membership of all data points _xi_ :


And recalculate updated memberships _P_ ( _µk_<sup>_|x_</sup> _i_<sup>)(therearedifferentwaystodefinemembership,here</sup>

234

6.047/6.878 Lecture 13: Gene Expression Clustering

is just one example):


4. _Termination_ : Iterate until membership matrix converges or until a user-specified number of iterations has been reached (the iteration may be trapped at some local maxima or minima)

The _b_ here is the weighting exponent which controls the relative weights places on each partition, or the degree of fuzziness. When _b− >_ 1, the partitions that minimize the squared error function is increasingly hard (non-fuzzy), while as _b− > ∞_ the memberships all approach _k_<sup><u>1</u></sup> , which is the fuzziest state. There is no theoretical evidence of how to choose an optimal _b_ , while the empirical useful values are among [1 _,_ 30], and in most of the studies, 1 _._ 5 ⩽ _b_ ⩽ 3 _._ 0 worked well.

### **15.3.3** **_K_ -Means as a Generative Model**

A generative model is a model for randomly generating observable-data values, given some hidden parameters. While a generative model is a probability model of all variables, a discriminative model provides a conditional model only of the target variable(s) using the observed variables.

In order to make _k_ -means a generative model, we now look at it in a probabilistic manner, where we assume that data points in cluster _k_ are generated using a Gaussian distribution with the mean on the center of cluster and a variance of 1, which gives _P_ ( _xi|µk_<sup>)=</sup> _~~√~~_ <u>12</u> _π_<sup>_exp{−_</sup><sup><u>(</u></sup><sup>_xi−_</sup> 2<sup>_<u>µk</u>_</sup><sup><u>)2</u></sup> _}_ . This gives a stochastic representation of the data, as shown in figure 15.10. Now this turns to a maximum likelihood problem, which, we will show in below, is exactly equivalent to the original _k_ -means algorithm mentioned above.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 15.10: _K_ -Means as a Generative Model. Samples were drawn from normal distributions.

In the generating step, we want to find a most likely partition, or assignment of label, for each _xi_ given the mean _µk_ . With the assumption that each point is drawn independently, we could look for the maximum likelihood label for each point separately:


This is totally equivalent to finding the nearest cluster center in the original _k_ -means algorithm.

In the Estimation step, we look for the maximum likelihood estimate of the cluster mean _µk_ , given the partitions (labels):


Note that the solution of this problem is exactly the centroid of the _xi_ , which is the same procedure as the original _k_ -means algorithm.

235

6.047/6.878 Lecture 13: Gene Expression Clustering

Unfortunately, since k-means assumes independence between the axes, covariance and variance are not accounted for using _k_ -means, so models such as oblong distributions are not possible. However, this issue can be resolved when generalize this problem into expectation maximization problem.

### **15.3.4 Expectation Maximization**

K-means can be seen as an example of EM (expectation maximization algorithms), as shown in figure 15.11 where expectation consists of estimation of hidden labels, _Q_ , and maximizing of expected likelihood occurs given data and _Q_ . Assigning each point the label of the nearest center corresponds to the E step of estimating the most likely label given the previous parameter. Then, using the data produced in the E step as observation, moving the centroid to the average of the labels assigned to that center corresponds to the _M_ step of maximizing the likelihood of the center given the labels. This case is analogous to Viterbi learning. A similar comparison can be drawn for fuzzy _k_ -means, which is analogous to Baum-Welch from HMMs. Figure 15.12 compares clustering, HMM and motif discovery with respect to expectation minimization algorithm.

It should be noted that using the EM framework, the _k_ means approach can be generalized to clusters of oblong shape and varying sizes. With _k_ means, data points are always assigned to the nearest cluster center. By introducing a covariance matrix to the Gaussian probability function, we can allow for clusters of different sizes. By setting the variance to be different along different axes, we can even create oblong distributions.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 15.11: _K_ -Means as an expectation maximization (EM) algorithm.


Figure 15.12: Comparison of clustering, HMM and motif discovery with respect to expectation minimization (EM) algorithm.

EM is guaranteed to converge and guaranteed to find the best possible answer, at least from an algorithmic

236

6.047/6.878 Lecture 13: Gene Expression Clustering

point of view. The notable problem with this solution is that the existence of local maxima of probability density can prevent the algorithm from convergin to the global maximum. One approach that may avoid this complication is to attempt multiple initializations to better determine the landscape of probabilities.

### **15.3.5 The limitations of the** **_K_ -Means algorithm**

The _k_ -means algorithm has a few limitations which are important to keep in mind when using it and before choosing it. First of all, it requires a metric. For example, we cannot use the _k_ -means algorithm on a set of words since we would not have any metric.

The second main limitation of the _k_ -means algorithm is its sensitivity to noise. One way to try to reduce the noise is to run a principle component analysis beforehand. Another way is to weight each variable in order to give less weight to the variables affected by significant noise: the weights will be calculated dynamically at each iteration of the algorithm K-means [3].

The third limitation is that the choice of initial centers can influence the results. There exist heuristics to select the initial cluster centers, but none of them are perfect.

Lastly, we need to know a priori the number of classes. As we have seen, there are ways to circumvent this problem, essentially by running several times the algorithm while varying k or using the rule of thumb _k ≈_ � _n/_ 2 if we are short on the computational side. `http://en.wikipedia.org/wiki/Determining_ the_number_of_clusters_in_a_data_set` summarizes well the different techniques to select the number of clusters. Hierarchical clustering provides a handy approach to choosing the number of cluster.

### **15.3.6 Hierarchical Clustering**

While the clustering discussed thus far often provide valuable insight into the nature of various data, they generally overlook an essential component of biological data, namely the idea that similarity might exist on multiple levels. To be more precise, similarity is an intrinsically hierarchical property, and this aspect is not addressed in the clustering algorithms discussed thus far. Hierarchical clustering specifically addresses this in a very simple manner, and is perhaps the most widely used algorithm for expression data. As illustrated in figure 15.13, it is implemented as follows:

1. _Initialization_ : Initialize a list containing each point as an independent cluster.

2. _Iteration_ : Create a new cluster containing the two closest clusters in the list. Add this new cluster to the list and remove the two constituent clusters from the list.

One key benefit of using hierarchical clustering and keeping track of the times at which we merge certain clusters is that we can create a tree structure that details the times at which we joined every cluster, as can be seen in figure 15.13. Thus, to get a number of clusters that fits your problem, you simply cut at a cut-level of your choice as in figure 15.13 and that gives you the number of clusters corresponding to that cut-level. However, be aware that one potential pitfall with this approach is that at certain cut-levels, elements that are fairly close in space (such as e and b in figure 15.13), might not be in the same cluster.

Of course, a method for determining distances between clusters is required. The particular metric used varies with context, but (as can be seen in figure 15.14 some common implementations include the maximum,

237

6.047/6.878 Lecture 13: Gene Expression Clustering


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 15.13: Hierarchical Clustering

minimum, and average distances between constituent clusters, and the distance between the centroids of the clusters.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 15.14: Distance Metrics for Hierarchical Clustering. Clockwise from top left: minimum, maximum, average distance and centroid distance.

Noted that when choosing the closest clusters, calculating all pair-wise distances is very time and space consuming, therefore a better scheme is needed. One possible way of doing this is : 1) define some bounding boxes that divide the feature space into several subspaces 2) calculate pair-wise distances within each box 3)shift the boundary of the boxes in different directions and recalculate pair-wise distances 4) choose the closest pair based on the results in all iterations.

### **15.3.7 Evaluating Cluster Performance**

The validity of a particular clustering can be evaluated in a number of different ways. The overrepresentation of a known group of genes in a cluster, or, more generally, correlation between the clustering and confirmed biological associations, is a good indicator of validity and significance. If biological data is not yet available, however, there are ways to assess validity using statistics. For instance, robust clusters will appear from clustering even when only subsets of the total available data are used to generate clusters. In addition, the statistical significance of a clustering can be determined by calculating the probability of a particular distribution having been obtained randomly for each cluster. This calculation utilizes variations on the hypergeometric distribution. As can be seen from figure 15.15, we can do this by calculating the probability that we have more than _r_ +’s when we pick _k_ elements from a total of _N_ elements. `http://en.wikipedia.org/wiki/Cluster_analysis#Evaluation_of_clustering_results` gives several formula to assess the quality of the clustering.

238

6.047/6.878 Lecture 13: Gene Expression Clustering


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 15.15: Calculation of probability that you have more than _r_ +’s in a randomly selected cluster.

## **15.4 Current Research Directions**

The most significant problems associated with clustering now are associated with scaling existing algorithms cleanly with two attributes: size and dimensionality. To deal with larger and larger datasets, algorithms such as canopy clustering have been developed, in which datasets are coarsely clustered in a manner intended to pre-process the data, following which standard clustering algorithms (e.g. _k_ -means) are applied to subdivide the various clusters. Increase in dimensionality is a much more frustrating problem, and attempt to remedy this usually involve a two stage process in which appropriate relevant subspaces are first identified by appropriate transformations on the original space and then subjected to standard clustering algorithms.

## **15.5 Further Reading**

- Trevor Hastie, Robert Tibshirani, and Jerome Friedman. The Elements of Statistical Learning: Data Mining, Inference, and Prediction. Second Edition, February 2009. Found online at `http://www-stat. stanford.edu/~tibs/ElemStatLearn/download.html`

- Numerical Recipes: The Art of Scientific Computing (3rd ed.). New York: Cambridge University Press.

- McLachlan, G.J. and Basford, K.E. (1988) ”Mixture Models: Inference and Applications to Clustering”, Marcel Dekker.

- Bezdek, J. C., Ehrlich, R., Full, W. (1984). FCM: The fuzzy c-means clustering algorithm. Computers and Geosciences, 10(2), 191-203.

- `http://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-clustering-1.html`

- `http://compbio.uthsc.edu/microarray/lecture1.html`

## **15.6 Resources**

- Cluster 3.0: open source clustering software that implements the most commonly used clustering methods for gene expression data analysis.

239

6.047/6.878 Lecture 13: Gene Expression Clustering

- MATLAB: K-means clustering: `http://www.mathworks.com/help/stats/kmeans.html` ; Fuzzy C- means clustering: `http://www.mathworks.com/help/fuzzy/fcm.html` ; Hierarchical Clustering: `http: //www.mathworks.com/help/stats/linkage.html`

- Orange is a free data mining software suite (see module orngClustering for scripting in Python): `http://bonsai.hgc.jp/~mdehoon/software/cluster/software.htm`

- R (see Cluster Analysis and Finite Mixture Models)

- SAS CLUSTER

## **15.7 What Have We Learned?**

To summarize, in this chapter we have seen that:

- In _clustering_ , we identify structure in unlabeled data. For example, we might use clustering to identify groups of genes that display similar expression profiles.

   - Partitioning clustering algorithms, construct non-overlapping clusters such that each item is assigned to exactly one cluster. Example: k-means

   - Agglomerative clustering algorithms construct a hierarchical set of nested clusters, indicating the relatedness between clusters. Example: hierarchical clustering

   - By using clustering algorithms, we can reveal hidden structure of a gene expression matrix, which gives us valuable clues for understanding the mechanism of complicated diseases and categorizing different diseases

- In _classification_ , we partition data into known labels. For example, we might construct a classifier to partition a set of tumor samples into those likely to respond to a given drug and those unlikely to respond to a given drug based on their gene expression profiles. We will focus on classification in the next chapter.

## **Bibliography**

- [1] http://en.wikipedia.org/wiki/File:Heatmap.png.

- [2] http://genome.ucsc.edu/ENCODE/.

- [3] J.Z. Huang, M.K. Ng, Hongqiang Rong, and Zichen Li. Automated variable weighting in k-means type clustering. _Pattern Analysis and Machine Intelligence, IEEE Transactions on_ , 27(5):657 –668, may 2005.

- [4] Christopher A. Maher, Chandan Kumar-Sinha, Xuhong Cao, Shanker Kalyana-Sundaram, Bo Han, Xiaojun Jing, Lee Sam, Terrence Barrette, Nallasivam Palanisamy, and Arul M. Chinnaiyan. Transcriptome sequencing to detect gene fusions in cancer. _Nature_ , 458(7234):97–101, Mar 05 2009.

240

CHAPTER

**SIXTEEN**

GENE REGULATION 2 –CLASSIFICATION

Arvind Thiagarajan Fulton Wang Salil Desai David Charlton Kevin Modzelewski Robert Toscano

## **16.1 Introduction**

In the previous chapter we looked at _clustering_ , which provides a tool for analyzing data without any prior knowledge of the underlying structure. As we mentioned before, this is an example of “unsupervised” learning. This chapter deals with **supervised learning** , in which we are able to use pre-classified data to construct a model by which to classify more datapoints. In this way, we will use existing, known structure to develop rules for identifying and grouping further information.

There are two ways to do classification. The two ways are analogous to the two ways in which we perform motif discovery: HMM, which is a generative model that allows us to actually describe the probability of a particular designation being valid, and CRF, which is a discriminative method that allows us to distinguish between objects in a specific context. There is a dichotomy between generative and discriminative approaches. We will use a Bayesian approach to classify mitochondrial proteins, and SVM to classify tumor samples.

In this lecture we will look at two new algorithms: a generative classifier, Nave Bayes, and a discriminative classifier, Support Vector Machines (SVMs). We will discuss biological applications of each of these models, specifically in the use of Nave Bayes classifiers to predict mitochondrial proteins across the genome and the use of SVMs for the classification of cancer based on gene expression monitoring by DNA microarrays. The salient features of both techniques and caveats of using each technique will also be discussed.

Like with clustering, classification (and more generally supervised learning) arose from efforts in Artificial

241

6.047/6.878 Lecture 14: Gene Regulation 2: Classification

Intelligence and Machine Learning. Furthermore, much of the motivating infrastructure for classification had already been developed by probability theorists prior to the advent of either AI or ML.

## **16.2 Classification - Bayesian Techniques**

Consider the problem of identifying mitochondrial proteins. If we look at the human genome, how do we determine which proteins are involved in mitochondrial processes, or more generally which proteins are targeted to the mitochondria1?<sup>1</sup> This is particularly useful because if we know the mitochondrial proteins, we can study how these proteins mediate disease processes and metabolic functions. The classification method we will look considers 7 features for all human proteins:

1. targeting signal

2. protein domains

3. co-expression

4. mass spectrometry

5. sequence homology

6. induction

7. motifs

Our overall approach will be to determine how these features are distributed for both mitochondrial and non-mitochondrial proteins. Then, given a new protein, we can apply probabilistic analysis to these seven features to decide which class it most likely falls into.

### **16.2.1 Single Features and Bayes Rule**

Let’s just focus on one feature at first. We must first assume that there is a class dependent distribution for the features. We must first derive this distribution from real data. The second thing we need is the a priori chance of drawing a sample of particular class before looking at the data. The chance of getting a particular class is simply the relative size of the class. Once we have these probabilities, we can use Bayes rule to get the probability a sample is in a particular class given the data(this is called the posterior). We have forward generative probabilities, and use Bayes rules to perform the backwards inference. Note that it is not enough to just consider the probability the feature was drawn from each class dependent distribution, because if we knew a priori that one class(say class A) is much more common than the other, then it should take overwhelming evidence that the feature was drawn from class B’s distribution for us to believe the feature was indeed from class B. The correct way to find what we need based on both evidence and prior knowledge is to use Bayes Rule:


> 1Mitochondria is the energy producing machinery of cell. Very early in life, the mitochondria was engulfed by the predecessor to modern day eukaryotes, and now, we have different compartments in our cells. So the mitochonria has its own genome, but it is very depleted from its own ancestral genome - only about 11 genes remain. But there are hundreds are genes that make the mitochondria work, and these proteins are encoded by genes transcribed in the nucleus, and then transported to the mitochondria. So the goal is to figure out which proteins encoded in the genome are targeted to the mitochondria. This is important because there are many diseases associated with the mitochonria, such as aging.

242

6.047/6.878 Lecture 14: Gene Regulation 2: Classification

- **Posterior** : _P_ (Class _|_ feature)

- **Prior** : _P_ (Class)

- **Likelihood** : _P_ (feature _|_ Class)

This formula gives us exactly the connection we need to flip known feature probabilities into class probabilities for our classifying algorithm. It lets us integrate both the likelihood we derive from our observations and our prior knowledge about how common something is. In the case of mtDNA, for example, we can estimate that mitochondrial DNA makes up something like 1500/21000 (i.e. less than 10%) of the human genome. Therefore, applying Bayes rule, our classifier should only classify a gene as mitochondrial if there is a **very strong likelihood based on the observed features** , since the prior probability that any gene is mitochondrial is so low.

With this rule, we can now form a maximum likelihood rule for predicting an objects class based on an observed feature. We want to choose the class that has the highest probability given the observed feature, so we will choose Class1 instead of Class2 if:


Notice that _P_ (feature) appears on both sides, so we can cancel that out entirely, and simply choose the class with the highest value of _P_ (feature _|_ Class) _P_ (Class).

Another way of looking at this is as a discriminant function: By rearranging the formulas above and taking the logarithm, we should select Class1 instead of Class2 precisely when


In this case the use of logarithms provide distinct advantages:

1. Numerical stability

2. Easier math (its easier to add the expanded terms than multiply them)

3. Monotonically increasing discriminators.

This discriminant function does not capture the penalties associated with misclassification (in other words, is one classification more detrimental than other). In this case, we are essentially minimizing the number of misclassifications we make overall, but not assigning penalties to individual misclassifications. From examples discussed in class and in the problem set - if we are trying to classify a patient as having cancer or not, it could be argued that it is far more harmful to misclassify a patient as being healthy if they have cancer than to misclassify a patient as having cancer if they are healthy. In the first case, the patient will not be treated and would be more likely to die, whereas the second mistake involves emotional grief but no greater chance of loss of life. To formalize the penalty of misclassification we define something called a loss function, _Lkf_ , which assigns a loss to the misclassification of an object as class j when the true class is class k (a specific example of a loss function was seen in Problem Set 2).

243

6.047/6.878 Lecture 14: Gene Regulation 2: Classification

### **16.2.2 Collecting Data**

The preceding tells us how to handle predictions if we already know the exact probabilities corresponding to each class. If we want to classify mitochondrial proteins based on feature _X_ , we still need ways of determining the probabilities _P_ (mito), _P_ (not mito), _P_ ( _X|_ mito) and _P_ ( _X|_ not mito). To do this, we need a training set: a set of data that is already classified that our algorithm can use to learn the distributions corresponding to each class. A **high-quality training set** (one that is both large and unbiased) is the most important part of any classifier. An important question at this point is, how much data do we need about known genes in order to build a good classifier for unknown genes? This is a hard question whose answer is not fully known. However, there are some simple methods that can give us a good estimate: when we have a fixed set of training data, we can keep a holdout set that we dont use for our algorithm, and instead use those (known) data points to test the accuracy of our algorithm when we try to classify them. By trying different sizes of training versus _holdout_ set, we can check the accuracy curve of our algorithm. Generally speaking, we have enough training data when we see the accuracy curve flatten out as we increase the amount of training data (this indicates that additional data is likely to give only a slight marginal improvement). The holdout set is also called the test set, because it allows us to test the generalization power of our classifier.

Supposing we have already collected our training data, however, how should we model _P_ ( _X|Class_ )? There are many possibilities. One is to use the same approach we did with clustering in the last lecture and model the feature as a Gaussian then we can follow the maximum likelihood principle to find the best center and variance. The one used in the mitochondrial study is a simple density estimate: for each feature, divide the range of possibilities into a set of bins (say, five bins per feature). Then we use the given data to estimate the probability of a feature falling into each bin for a given class. The principle behind this is again maximum likelihood, but for a multinomial distribution rather than a Gaussian. We may choose to discretize a otherwise continuous distribution because estimating a continuous distribution can be complex.

There is one issue with this strategy: what if one of the bins has zero samples in it? A probability of zero will override everything else in our formulas, so that instead of thinking this bin is merely unlikely, our classifier will believe it is _impossible_ . There are many possible solutions, but the one taken here is to apply the _Laplace Correction_ : add some small amount (say, one element) into each bin, to draw probability estimates slightly towards uniform and account for the fact that (in most cases) none of the bins are truly impossible. Another way to avoid having to apply the correction is to choose bins that are not too small so that bins will not have zero samples in them in practice. If you have many many points, you can have more bins, but run the risk of overfitting your training data.

### **16.2.3 Estimating Priors**

We now have a method for approximating the feature distribution for a given class, but we still need to know the relative probability of the classes themselves. There are **three general approaches** :

1. Estimate the priors by counting the relative frequency of each class in the training data. This is prone to bias, however, since data available is often skewed disproportionately towards less common classes (since those are often targeted for special study). If we have a high-quality (representative) sample for our training data, however, this works very well.

2. Estimate from expert knowledge—there may be previous estimates obtained by other methods independent of our training data, which we can then use as a first approximation in our own predictions. In other words, you might ask experts what the percentage of mitochondrial proteins are.

3. Assume all classes are equally likely we would typically do this if we have no information at all about the true frequencies. This is effectively what we do when we use the maximum likelihood principle:

244

6.047/6.878 Lecture 14: Gene Regulation 2: Classification

our clustering algorithm was essentially using Bayesian analysis under the assumption that all priors are equal. This is actually a strong assumption, but when you have no other data, this is the best you can do.

For classifying mitochondrial DNA, we use method (2), since some estimates on the proportions of mtDNA were already known. But there is an complication there are more than 1 features.

### **16.2.4 Multiple features and Naive Bayes**

In classifying mitochondrial DNA, we were looking at 7 features and not just one. In order to use the preceding methods with multiple features, we would need not just one bin for each individual feature range, but one for each combination of features if we look at two features with five ranges each, thats already 25 bins. All seven features gives us almost 80,000 bins and we can expect that most of those bins will be empty simply because we dont have enough training data to fill them all. This would cause problems because zeroes cause infinite changes in the probabilities of being in one class. Clearly this approach wont scale well as we add more features, so we need to estimate combined probabilities in a better way.

The solution we will use is to **assume the features are independent** , that is, that once we know the class, the probability distribution of any feature is unaffected by the values of the other features. This is the Nave Bayes Assumption, and it is almost always false, but it is often used anyway for the combined reasons that it is very easy to manipulate mathematically and it is often close enough to the truth that it gives a reasonable approximation. (Note that this assumption does not say that all features are independent: if we look at the overall model, there can be strong connections between different features, but the assumption says that those connections are divided by the different classes, and that within each individual class there are no further dependencies.) Also, if you know that some features are coupled, you could learn the joint distribution in only some pairs of the features.

Once we assume independence, the probability of combined features is simply the product of the individual probabilities associated with each feature. So we now have:

_P_ ( _f_ 1 _, f_ 2 _, K, fN |_ Class) = _P_ ( _f_ 1 _|_ Class) _P_ ( _f_ 2 _|_ Class) _KP_ ( _fN |_ Class)

Where _f_ 1 represents feature 1. Similarly, the discriminant function can be changed to the multiplication of the prior probabilities:


### **16.2.5 Testing a classifier**

A classifier should always be tested on data not contained in its training set. We can imagine in the worst case an algorithm that just memorized its training data and behaved randomly on anything else a classifier that did this would perform perfectly on its training data, but that indicates nothing about its real performance on new inputs. This is why its important to use a test, or holdout, set as mentioned earlier. However, a simple error rate doesnt encapsulate all of the possible consequences of an error. For a simple binary classifier (an object is either in or not in a single target class), there are the following for types of errors:

1. True positive (TP)

245

6.047/6.878 Lecture 14: Gene Regulation 2: Classification

2. True negative (TN)

3. False positive (FP)

4. False negative (FN)

The frequency of these errors can be encapsulated in performance metrics of a classifier which are defined as,

1. _Sensitivity_ what fraction of objects that are in a class are correctly labeled as that class? That is, what fraction have true positive results? High sensitivity means that elements of a class are very likely to be labeled as that class. Low sensitivity means there are too many false negatives.

2. _Specificity_ what fraction of objects not in a class are correctly labeled as not being in that class? That is, what fraction have true negative results? High specificity means that elements labeled as belonging to a class are very likely to actually belong to it. Low specificity means there are too many false positives.

In most algorithms there is a **tradeoff between sensitivity and specificity** . For example, we can reach a sensitivity of 100% by labeling everything as belonging to the target class, but we will have a specificity of 0%, so this is not useful. Generally, most algorithms have some probability cutoff they use to decide whether to label an object as belonging to a class (for example, our discriminant function above). Raising that threshold increases the specificity but decreases the sensitivity, and decreasing the threshold does the reverse. The MAESTRO algorithm for classifying mitochondrial proteins (described in this lecture) achieves 99% specificity and 71% sensitivity.

### **16.2.6 MAESTRO Mitochondrial Protein Classification**

They find a class dependent distribution for each feature by creating several bins and evaluating the proportion of mitochondrial and non mitochondrial proteins in each bin. This lets you evaluate the **usefulness of each feature** in classification. You end up with a bunch of medium strength classifiers, but when you combine them together, you hopefully end up with a stronger classifier. Calvo et al. [1] sought to construct high-quality predictions of human proteins localized to the mitochondrion by generating and integrating data sets that provide complementary clues about mitochondrial localization. Specifically, for each human gene product _p_ , they assign a score _si_ ( _p_ ), using each of the following seven genome-scale data sets targeting signal score, protein domain score, cis-motif score, yeast homology score, ancestry score, coexpression score, and induction score (details of each of the meaning and content of each of these data sets can be found in the manuscript). Each of these scores _s_ 1 _− S_ 7 can be used individually as a weak genome-wide predictor of mitochondrial localization. Each methods performance was assessed using large gold standard curated training sets - 654 mitochondrial proteins _T_ mito maintained by the MitoP2 database1 and 2,847 nonmitochondrial proteins _T_ mito annotated to localize to other cellular compartments. To improve prediction accuracy, the authors integrated these eight approaches using a nave Bayes classifier that was implemented as a program called MAESTRO. So we can take several weak classifiers, and combine them to get a stronger classifier.

When MAESTRO was applied across the human proteome, 1451 proteins were predicted as mitochondrial proteins and 450 novel proteins predictions were made. As mentioned in the previous section The MAESTRO algorithm achieves a 99% specificity and a 71% sensitivity for the classification of mitochondrial proteins, suggesting that even with the assumption of feature independence, Nave Bayes classification techniques can prove extremely powerful for large-scale (i.e. genome-wide) scale classification.

246

6.047/6.878 Lecture 14: Gene Regulation 2: Classification

## **16.3 Classification Support Vector Machines**

The previous section looked at using probabilistic (or generative) models for classification, this section looks at using discriminative techniques in essence, can we run our data through a function to determine its structure? Such discriminative techniques avoid the inherent cost involved in generative models which might require more information than is actually necessary.

Support vector machine techniques essentially involve drawing a vector thats perpendicular to the line(hyperplane) separating the training data. The approach is that we look at the training data to obtain a separating hyperplane so that two classes of data lie on different sides of the hyperplane. There are, in general, many hyperplanes that can separate the data, so we want to draw the hyperplane that separates the data the most - we wish to choose the line that maximizes the distance from the hyperplane to any data point. In other words, the SVM is a maximum margin classifier. You can think of the hyperplane being surrounded with margins of equal size on each side of the line, with no data points inside the margin on either side. We want to draw the line that allows us to draw the largest margin. Note that once the separating line and margin are determined, some data points will be right on the boundary of the margin. These are the data points that keep us from expanding the margin any further, and thus determine the line/margin. Such points are called the support vectors. If we add new data points outside the margin or remove points that are not support vectors, we will not change the maximum margin we can achieve with any hyperplane.

the Supposepoint � _|w_ that _<u>b</u> |_ �. theThenvectora pointperpendicular _x_ is classifiedto theas beinghyperplanein theispositivew, and classthat theif _w_ hyperplane _∗ x_ is greaterpassesthanthrough _b_ , and negative otherwise. It can be shown that the optimal w, that is, the hyperplane that achieves the maximum margin, can actually be written as a linear combination of the data vectors Σ _ai ∗ xi_ . Then, to classify a new data point x, we need to take the dot product of w with x to arrive at a scalar. Notice that this scalar, Σ _ai ∗_ ( _xi ∗ x_ ) only depends on the dot product between x and the training vectors _xi_ s. Furthermore, it can be shown that finding the maximum margin hyperplane for a set of (training) points amounts to maximizing a linear program where the objective function only depends on the dot product of the training points with each other. This is good because it tells us that the complexity of solving that linear program is independent of the of dimension of the data points. If we precompute the pairwise dot products of the training vectors, then it makes no difference what the dimensionality of the data is in regards to the running time of solving the linear program.

### **16.3.1 Kernels**

We see that SVMs are dependent only on the dot product of the vectors. So, if we call our transformation _φ_ ( _v_ ), for two vectors we only care about the value of _φ_ ( _v_ 1) _· φ_ ( _v_ 2) The trick to using kernels is to realize that for certain transformations _φ_ , there exists a function _K_ ( _v_ 1 _, v_ 2), such that:


In the above relation, the right-hand side is the dot product of vectors with very high dimension, but the left-hand side is the function of two vectors with lower dimension. In our previous example of mapping _x →_ ( _x, y_ = _x_<sup>2</sup> ), we get


Now we did not actually apply the transformation _φ_ , we can do all our calculations in the lower dimensional space, but get all the power of using a higher dimension.

247

6.047/6.878 Lecture 14: Gene Regulation 2: Classification

Example kernels are the following:

1. Linear kernel: _K_ ( _v_ 1 _, v_ 2) = _v_ 1 _· v_ 2 which represents the trivial mapping of _φ_ ( _x_ ) = _x_

2. Polynomial kernel: _K_ ( _v_ 1 _, v_ 2) = (1 + _v_ 1 _· v_ 2)<sup>_n_</sup> which was used in the previous example with _n_ = 2.

3. Radial basis kernel: _K_ ( _v_ 1 _, v_ 2) = exp( _−β|v_ 1 _− v_ 2 _|_<sup>2</sup> ) This transformation is actually from a point _v_ 1 to a function (which can be thought of as being a point in Hilbert space) in an infinite-dimensional space. So what were actually doing is transforming our training set into functions, and combining the to get a decision boundary. The functions are Gaussians centered at the input points.

4. Sigmoid kernel: _K_ ( _v_ 1 _, v_ 2) = tanh[ _β_ ( _v_ 1<sup>_Tv_2+</sup><sup>_r_)] Sigmoid kernels have been popular for use in SVMs due</sup> to their origin in neural networks (e.g. sigmoid kernel functions are equivalent to two-level, perceptron neural networks). It has been pointed out in previous work (Vapnik 1995) that the kernel matrix may not be positive semi-definite for certain values of the parameters _µ_ and _r_ . The sigmoid kernel has nevertheless been used in practical applications [2].

Here is a specific example of a kernel function. Consider the two classes of one-dimensional data:

_{−_ 5 _, −_ 4 _, −_ 3 _,_ 3 _,_ 4 _,_ 5 _}and{−_ 2 _, −_ 1 _,_ 0 _,_ 1 _,_ 2 _}_

This data is clearly not linearly separable, and the best separation boundary we can find might be _x > −_ 2 _._ 5. Now consider applying the transformation . The data can now be written as new pairs,

_{−_ 5 _, −_ 4 _, −_ 3 _,_ 3 _,_ 4 _,_ 5 _} →{_ ( _−_ 5 _,_ 25) _,_ ( _−_ 4 _,_ 16) _,_ ( _−_ 3 _,_ 9) _,_ (3 _,_ 9) _,_ (4 _,_ 16) _,_ (5 _,_ 25) _}_

and

_{−_ 2 _, −_ 1 _,_ 0 _,_ 1 _,_ 2 _} →{_ ( _−_ 2 _, −_ 4) _,_ ( _−_ 1 _,_ 1) _,_ (0 _,_ 0) _,_ (1 _,_ 1) _,_ (2 _,_ 4) _}_

This data is separable by the rule _y >_ 6 _._ 5, and in general the more dimensions we transform data to the more separable it becomes.

An alternate way of thinking of this problem is to transform the classifier back in to the original lowdimensional space. In this particular example, we would get the rule _x_<sup>2</sup> _<_ 6 _._ 5 , which would bisect the number line at two points. In general, the higher dimensionality of the space that we transform to, the more complicated a classifier we get when we transform back to the original space.

One of the caveats of transforming the input data using a kernel is the risk of overfitting (or overclassifying) the data. More generally, the SVM may generate so many feature vector dimensions that it does not generalize well to other data. To avoid overfitting, cross-validation is typically used to evaluate the fitting provided by each parameter set tried during the grid or pattern search process. In the radial-basis kernel, you can essentially increase the value of _β_ until each point is within its own classification region (thereby defeating the classification process altogether). SVMs generally avoid this problem of over-fitting due to the fact that they maximize margins between data points.

When using difficult-to-separate training sets, SVMs can incorporate a cost parameter _C_ , to allow some flexibility in separating the categories. This parameter controls the trade-off between allowing training errors and forcing rigid margins. It can thereby create a _soft_ margin that permits some misclassifications. Increasing the value of _C_ increases the cost of misclassifying points and forces the creation of a more accurate model that may not generalize well.

248

6.047/6.878 Lecture 14: Gene Regulation 2: Classification

Can we use just any function as our kernel? The answer to this is provided by Mercers Condition which provides us an analytical criterion for choosing an acceptable kernel. Mercers Condition states that a kernel _K_ ( _x, y_ ) is a valid kernel if and only if the following holds For any _g_ ( _x_ ) such that � _g_ ( _x_ )<sup>2</sup> _dx_ is finite, we have:

#### �� _K_ ( _x, y_ ) _g_ ( _x_ ) _g_ ( _y_ ) _dxdy ≥_ 0[3]

In all, we have defined SVM discriminators and shown how to perform classification with appropriate kernel mapping functions that allow performing computations on lower dimension while being to capture all the information available at higher dimensions. The next section describes the application of SVMs to the classification of tumors for cancer diagnostics.

## **16.4 Tumor Classification with SVMs**

A generic approach for classifying two types of acute leukemias acute myeloid leukemia (AML) and acute lymphoid leukemia (ALL) was presented by Golub et al. [4]. This approach centered on effectively addressing three main issues:

1. Whether there were genes whose expression pattern to be predicted was strongly correlated with the class distinction (i.e. can ALL and AML be distinguished)

2. How to use a collection of known samples to create a “class predictor” capable of assigning a new sample to one of two classes

3. How to test the validity of their class predictors

They addressed (1) by using a “neighbourhood analysis” technique to establish whether the observed correlations were stronger than would be expected by chance. This analysis showed that roughly 1100 genes were more highly correlated with the AML-ALL class distinction than would be expected by chance. To address (2) they developed a procedure that uses a fixed subset of “informative genes” (chosen based on their correlation with the class distinction of AML and ALL) and makes a prediction based on the expression level of these genes in a new sample. Each informative gene casts a “weighted vote” for one of the classes, with the weight of each vote dependent on the expression level in the new sample and the degree of that genes correlation with the class distinction. The votes are summed to determine the winning class. To address (3) and effectively test their predictor by first testing by cross-validation on the initial data set and then assessing its accuracy on an independent set of samples. Based on their tests, they were able to identify 36 of the 38 samples (which were part of their training set!) and all 36 predictions were clinically correct. On the independent test set 29 of 34 samples were strongly predicted with 100% accuracy and 5 were not predicted.

A SVM approach to this same classification problem was implemented by Mukherjee et al.[5]. The output of classical SVM is a binary class designation. In this particular application it is particularly important to be able to reject points for which the classifier is not confident enough. Therefore, the authors introduced a confidence interval on the output of the SVM that allows for rejection of points with low confidence values. As in the case of Golub et al.[4] it was important for the authors to infer which genes are important for the classification. The SVM was trained on the 38 samples in the training set and tested on the 34 samples in the independent test set (exactly in the case of Golub et al.). The authors results are summarized in the following table (where _|d|_ corresponds to the cutoff for rejection).

These results a significant improvement over previously reported techniques, suggesting that SVMs play an important role in classification of large data sets (as those generated by DNA microarray experiments).

249

6.047/6.878 Lecture 14: Gene Regulation 2: Classification

## **16.5 Semi-Supervised Learning**

In some scenarios we have a data set with only a few labeled data points, a large number of unlabeled data points and inherent structure in the data. This type of scenario both clustering and classification do not perform well and a hybrid approach is required. This semi-supervised approach could involve the clustering of data first followed by the classification of the generated clusters.

### **16.5.1 Open Problems**

## **16.6 Current Research Directions**

## **16.7 Further Reading**

- Richard O. Duda, Peter E. Hart, David G. Stork (2001) Pattern classification (2nd edition), Wiley, New York

- See previous chapter for more books and articles.

## **16.8 Resources**

- Statistical Pattern Recognition Toolbox for Matlab.

- See previous chapter for more tools

## **Bibliography**

- [1] Calvo, S., Jain, M., Xie, X., Sheth, S.A., Chang, B., Goldberger, O.A., Spinaz- zola, A., Zeviani, M., Carr, S.A., and Mootha, V.K. (2006). Systematic identifi- cation of human mitochondrial disease genes through integrative genomics. Nat. Genet. 38, 576582.

- [2] Scholokopf, B., et al., 1997. Comparing support vector machines with Gaussian kernels to radial basis function classifiers. IEEE Transactions on Signal Processing.

- [3] Christopher J.C. Burges. A tutorial on support vector machines for pattern recognition. _Data Mining and Knowledge Discovery_ , 2:121–167, 1998.

- [4] T. R. Golub, D. K. Slonim, P. Tamayo, C. Huard, M. Gaasenbeek, J. P. Mesirov, H. Coller, M. L. Loh, J. R. Downing, M. A. Caligiuri, and C. D. Bloomfield. Molecular classification of cancer: class discovery and class prediction by gene expression monitoring. _Science_ , 286:531–537, 1999.

- [5] S. Mukherjee, P. Tamayo, D. Slonim, A. Verri, T. Golub, J. P. Mesirov, and T. Poggio. Support vector machine classification of microarray data. Technical report, AI Memo 1677, Massachusetts Institute of Technology, 1998.

250

6.047/6.878 Lecture 14: Gene Regulation 2: Classification

|**Genes**|**Rejects**|**Errors**|**Confidence level**|_|d|_|
|---|---|---|---|---|
|7129|3|0|93%|0.1|
|40|0|0|93%|0.1|
|5|3|0|92%|0.1|


251

6.047/6.878 Lecture 14: Gene Regulation 2: Classification

252

CHAPTER

## **SEVENTEEN**

REGULATORY MOTIFS, GIBBS SAMPLING, AND EM

Jenny Lin (2014) Maria Alexis (2013) James Yeung (2012) Yinqing Li and Arvind Thiagarajan (2011) Bianca Dumitrascu and Neal Wadhwa (2010) Joseph Lane (2009) Brad Cater and Ethan Heilman (2008)

### **Figures**

|17.1 Transcription factors binding to DNA at a motif site . . . . . . . . . . . . . . . . . . . . .|253|
|---|---|
|17.2 Example Profile Matrix<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|254|
|17.3 Examples of the Z matrix computed<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|255|
|17.4 Selecting motif location: the greedy algorithm will always pick the most probable location<br>for the motif. The EM algorithm will take an average while Gibbs Sampling will actually<br>use the probability distribution given by _Z_ to sample a motif in each step . . . . . . . . .|255|
|17.5 Sample position weight matrix<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|256|
|17.6 Gibbs Sampling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|258|
|17.7 Using motif seeds to find degenerate motifs<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|259|
|17.8 Examples of the Z matrix computed via EM, Gibbs Sampling, and the Greedy Algorithm|260|
|17.9 Selecting motif location: the greedy algorithm will always pick the most probable location<br>for the motif. The EM algorithm will take an average while Gibbs Sampling will actually<br>use the probability distribution given by _Z_ to sample a motif in each step . . . . . . . . .|260|
|17.10Sequences with zero, one or two motifs.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|262|
|17.11Entropy is maximized when both heads and tails have an equal chance of occurring . . . .|263|
|17.12The height of each stack represents the number of bits of information that Gibbs sampling<br>or EM told us about the postion in the motif . . . . . . . . . . . . . . . . . . . . . . . . .|263|
|17.13lexA binding site assuming low G-C content and using K-L distance<br>. . . . . . . . . . . .|264|


253

6.047/6.878 Lecture 15: Regulatory Motifs, Gibbs Sampling, and EM

## **17.1 Introduction to regulatory motifs and gene regulation**

We have already explored the areas of dynamic programming, sequence alignment, sequence classification and modeling, hidden Markov models, and expectation maximization. In the following chapter, we will look at how these techniques are also useful in identifying novel motifs and elucidating their functions.

### **17.1.1 The regulatory code: Transcription Factors and Motifs**

Motifs are short (6-8 bases long), recurring patterns that have well- defined biological functions. Motifs include DNA patterns in enhancer regions or promoter motifs, as well as motifs in RNA sequences such as splicing signals. As we have discussed, genetic activity is regulated in response to environmental variations. Motifs are responsible for recruiting Transcription Factors, or regulatory proteins, to the appropriate target gene. Motifs can also be recognized by microRNAs, which bind to motifs given through complementarity; nucleosomes, which recognize motifs based on their GC content; and other RNAs, which use a combination of DNA sequence and structure. Once bound, they can activate or repress the expression of the associated gene.

Transcription factors (TFs) can use several mechanisms in order to control gene expression, including acetylation and deacetylation of histone proteins, recruitment of cofactor molecules to the TF-DNA complex, and stabilization or disruption of RNA-DNA interfaces during transcription. They often regulate a group of genes that are involved in similar cellular processes. Thus, genes that contain the same motif in their upstream regions are likely to be related in their functions. In fact, many regulatory motifs are identified by analyzing the regions upstream of genes known to have similar functions.

Motifs have become exceedingly useful for defining genetic regulatory networks and deciphering the functions of individual genes. With our current computational abilities, regulatory motif discovery and analysis has progressed considerably and remains at the forefront of genomic studies.

### **17.1.2 Challenges of motif discovery**

Before we can get into algorithms for motif discovery, we must first understand the characteristics of motifs, especially those that make motifs somewhat difficult to find. As mentioned above, motifs are generally very short, usually only 6-8 base pairs long. Additionally, motifs can be degenerate, where only the nucleotides at certain locations within the motif affect the motif’s function. This degeneracy arises because transcription factors are free to interact with their corresponding motifs in manners more complex than a simple complementarity relation. As seen in 17.1, many proteins interact with the motif not by opening up the DNA to check for base complementarity, but instead by scanning the spaces, or grooves, between the two sugar phosphate backbones. Depending on the physical structure of the transcription factor, the protein may only be sensitive to the difference between purines and pyrimidines or weak and strong bases, as opposed to identifying specific base pairs. The topology of the transcription factor may even make it such that certain nucleotides aren’t interacted with at all, allowing those bases to act as wildcards.

This issue of degeneracy within a motif poses a challenging problem. If we were only looking for a fixed k-mer, we could simply search for the k-mer in all the sequences we are looking at using local alignment

254

6.047/6.878 Lecture 15: Regulatory Motifs, Gibbs Sampling, and EM


Figure 17.1: Transcription factors binding to DNA at a motif site

© Garland Publishing. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

tools. However, the motif may vary from sequence to sequence. Because of this, a string of nucleotides that is known to be a regulatory motif is said to be an _instance_ of a motif because it represents one of potentially many different combinations of nucleotides that fulfill the function of the motif.

In our approaches, we make two assumptions about the data. First, we assume that there are no pairwise correlations between bases, i.e. that each base is independent of every other base. While such correlations do exist in real life, considering them in our analysis would lead to an exponential growth of the parameter space being considered, and consequently we would run the risk of overfitting our data. The second assumption we make is that all motifs have fixed lengths; indeed, this approximation simplifies the problem greatly. Even with these two assumptions, however, motif finding is still a very challenging problem. The relatively small size of motifs, along with their great variety, makes it fairly difficult to locate them. In addition, a motif’s location relative to the corresponding gene is far from fixed; the motif can be upstream or downstream, and the distance between the gene and the motif also varies. Indeed, sometimes the motif is as far as 10 _k_ to 10 _M_ base pairs from the gene.

### **17.1.3 Motifs summarize TF sequence specificity**

Because motif instances exhibit great variety, we generally use a Position Weight Matrix (PWM) to characterize the motif. This matrix gives the frequency of each base at each location in the motif. The figure below shows an example PWM, where _pck_ corresponds to the frequency of base _c_ in position _k_ within the motif, with _pc_ 0 denoting the distribution of bases in non-motif regions.

We now define the problem of motif finding more rigorously. We assume that we are given a set of co-regulated and functionally related genes. Many motifs were previously discovered by doing footprint

255

6.047/6.878 Lecture 15: Regulatory Motifs, Gibbs Sampling, and EM


Figure 17.2: Example Profile Matrix

experiments, which isolate sequences bound by specific transcription factors, and therefore more likely to correspond to motifs. There are several computational methods that can be used to locate motifs:

1. Perform a local alignment across the set of sequences and explore the alignments that resulted in a very high alignment score.

2. Model the promoter regions using a Hidden Markov Model and then use a generative model to find non-random sequences.

3. Reduce the search space by applying prior knowledge for what motifs should look like.

4. Search for conserved blocks between different sequences.

5. Examine the frequency of kmers across regions highly likely to contain a motif.

6. Use probabilistic methods, such as EM, Gibbs Sampling, or a greedy algorithm

Method 5, using relative kmer frequencies to discover motifs, presents a few challenges to consider. For example, there could be many common words that occur in these regions that are in fact not regulatory motifs but instead different sets of instructions. Furthermore, given a list of words that could be a motif, it is not certain that the most likely motif is the most common word; for instance, while motifs are generally overrepresented in promoter regions, transcription factors may be unable to bind if an excess of motifs are present. One possible solution to this problem might be to find kmers with maximum relative frequency in promoter regions as compared to background regions. This strategy is commonly performed as a post processing step to narrow down the number of possible motifs.

In the next section, we will talk more about these probabilistic algorithms as well as methods to use kmer frequency for motif discovery. We will also come back to the idea of using kmers to find motifs in the context of using evolutionary conservation for motif discovery.

## **17.2 Expectation maximization**

### **17.2.1 The key idea behind EM**

We are given a set of sequences with the assumption that motifs are enriched in them. The task is to find the common motif in those sequences. The key idea behind the following probabilistic algorithms is that if

256

6.047/6.878 Lecture 15: Regulatory Motifs, Gibbs Sampling, and EM

we were given motif starting positions in each sequence, finding the motif PWM would be trivial; similarly, if we were given the PWM for a particular motif, it would be easy to find the starting positions in the input sequences. Let _Z_ be the matrix in which _Zij_ corresponds to the probability that a motif instance starts at position _j_ in sequence _i_ (a graphical of the probability distributions summarized in _Z_ is shown in Figure 17.8). These algorithms therefore rely on a basic iterative approach: given a motif length L and an initial matrix _Z_ , we can use the starting positions to estimate the motif, and in turn use the resulting motif to re-estimate the starting positions, iterating over these two steps until convergence on a motif.


<!-- Start of picture text -->
© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

Figure 17.3: Examples of the Z matrix computed

### **17.2.2 The E step: Estimating** _Zij_ **from the PWM**


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 17.4: Selecting motif location: the greedy algorithm will always pick the most probable location for the motif. The EM algorithm will take an average while Gibbs Sampling will actually use the probability distribution given by _Z_ to sample a motif in each step

- **Step 1: Initialization** The first step in EM is to generate an initial probability weight matrix (PWM). The PWM describes the frequency of each nucleotide at each location in the motif. In 17.5, there is an example of a PWM. In this example, we assume that the motif is eight bases long.

If you are given a set of aligned sequences and the location of suspected motifs within them, then finding the PWM is accomplished by computing the frequency of each base in each position of the suspected motif. We can initialize the PWM by choosing starting locations randomly.

We refer to the PWM as _pck_ , where _pck_ is the probability of base _c_ occurring in position _k_ of the motif. Note: if there is 0 probability, it is generally a good idea to insert pseudo- counts into your probabilities. The PWM is also called the profile matrix. In addition to the PWM, we also keep a background distribution _pck,k_ =0, a distribution of the bases not in the motif.

- **Step 2: Expectation** In the expectation step, we generate a vector _Zij_ which contains the probability of the motif starting in position _j_ in sequence _i_ . In EM, the _Z_ vector gives us a way of classifying all of the nucleotides in the sequences and tell us whether they are part of the motif or not. We can calculate _Zij_ using Bayes’ Rule. This simplifies to:

   - _P r_<sup>_t_</sup> <u>(</u> _Xi_<sup>_<u>|Z</u>_</sup> _ij_<sup><u>)</u></sup><sup>_P rt_</sup><sup><u>(</u></sup><sup>_Z_</sup> _ij_<sup>=1)</sup>

   - _Z_<sup>_t_</sup> _ij_<sup>=</sup> Σ<sup>_L_</sup> _k_ =1<sup>_−W_+1</sup> _P r_<sup>_t_</sup> ( _Xi|Zij_ =1) _P r_<sup>_t_</sup> ( _Zik_ =1)

257

6.047/6.878 Lecture 15: Regulatory Motifs, Gibbs Sampling, and EM


Figure 17.5: Sample position weight matrix


where _Pr_<sup>_t_</sup> ( _Xi|Zij_ = 1) = _Pr_ ( _Xi|Zij_ = 1 _, p_ ) is defined as

This is the probability of sequence _i_ given that the motif starts at position _j_ . The first and last products correspond to the probability that the sequences preceeding and following the candidate motif come from some background probability distribution whereas the middle product corresponds to the probability that the candidate motif instance came from a motif probability distribution. In this equation, we assume that the sequence has length _L_ and the motif has length _W_ .

### **17.2.3 M step: Finding the maximum likelihood motif from starting positions Zij**

- **Step 3: Maximization** Once we have calculated _Z_<sup>_t_</sup> , we can use the results to update both the PWM and the background probability distribution. We can update the PWM using the following equation


**Step 4: Repeat** Repeat steps 2 and 3 until convergence.

258

6.047/6.878 Lecture 15: Regulatory Motifs, Gibbs Sampling, and EM

One possible way to test whether the profile matrix has converged is to measure how much each element in the PWM changes after step maximization. If the change is below a chosen threshold, then we can terminate the algorithm. EM is a deterministic algorithm and is entirely dependent on the initial starting points because it uses an average over the full probability distribution. It is therefore advisable to rerun the algorithm with different intial starting positions to try reduce the chance of converging on a local maximum that is not the global maximum and to get a good sense of the solution space.

## **17.3 Gibbs Sampling: Sample from joint (M,Zij) distribution**

### **17.3.1 Sampling motif positions based on the Z vector**

Gibbs sampling is similar to EM except that it is a stochastic process, while EM is deterministic. In the expectation step, we only consider nucleotides within the motif window in Gibbs sampling. In the maximization step, we sample from _Zij_ and use the result to update the PWM instead of averaging over all values as in EM.

- **Step 1: Initialization** As with EM, you generate your initial PWM with a random sampling of initial starting positions. The main difference lies in the Maximization step. During EM, the algorithm creates the sequence motif by considering all possible starting points of the motif. During Gibbs, the algorithm picks a single starting point of the motif with the probability of the starting points Z.

- **Step 2: Remove** Remove one sequence, _Xi_ , from your set of sequences. You will change the starting location of for this particular sequence.

- **Step 3: Update** Using the remaining set of sequences, update the PWM by counting how often each base occurs in each position, adding pseudocounts as necessary.

- **Step 4: Sample** Using the newly updated PWM, compute the score of each starting point in the sequence _Xi_ . To generate each score, _Zij_ , the following formula is used:


This is simply the probability that the sequence was generated using the motif PWM divided by the probability that the sequence was generated using the background PWM.

Select a new starting position for _Xi_ by randomly choosing a position based on its _Zij_ .

- **Step 5: Iterate** Loop back to Step 2 and iterate the algorithm until convergence.

### **17.3.2 More likely to find global maximum, easy to implement**

Because Gibbs updates its sequence motif during Maximization based of a single sample of the Motif rather than every sample weighted by their scores, Gibbs is less dependent on the starting PWM. EM is much more likely to get stuck on a local maximum than Gibbs because of this fact. However, this does not mean that Gibbs will always return the global maximum. Gibbs must be run multiple times to ensure that you have found the global maximum and not the local maximum.Two popular implementations of Gibbs Sampling applied to this problem are AlignACE and BioProspector. A more general Gibbs Sampler can be found in

259

6.047/6.878 Lecture 15: Regulatory Motifs, Gibbs Sampling, and EM

the program WinBUGS. Both AlignACE and BioProspector use the aforementioned algorithm for several choices of initial values and then report common motifs. Gibbs sampling is easier to implement than E-M, and in theory, it converges quickly and is less likely to get stuck at a local optimum. However, the search is less systematic.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 17.6: Gibbs Sampling

## **17.4 De novo motif discovery**

As discussed in beginning of this chapter, the core problem for motif finding is to define the criteria for what is a valid motif and where they are located. Since most motifs are linked to important biological functions, one could subject the organism to a variety of conditions in hope of triggering these biological functions. One could then search for differentially expressed genes, and then use those genes as a basis for which genes are functionally related and thus likely to be controlled by the same motif instance. However, this technique not only relies on prior knowledge of interesting biological functions to probe for, but is also subject to biases in the experimental procedure. Alternatively, one could use ChIP-seq to search for motifs, but this method relies on not only having a known Transcription Factor of interest, but also requires developing antibodies to recognize said Transcription Factor, which can be costly and time consuming.

Ideally one would be able to discover motifs de novo, or without relying on an already known gene set or Transcription Factor. While this seems like a difficult problem, it can in fact be accomplished by taking advantage of genome-wide conservation. Because biological functions are usually conserved across species and have distinct evolutionary signatures, one can align sequences from close species and search specifically in conserved regions (also known as Island of Conservation) in order to increase the rate of finding functional motifs.

### **17.4.1 Motif discovery using genome-wide conservation**

Conservation islands often overlap known motifs, so doing genome-wide scans through evolutionary conserved regions can help us discover motifs, de novo. However, not all conserved regions will be motifs; for instance, nucleotides surrounding motifs may also be conserved even though they are not themselves part of a motif. Distinguishing motifs from background conserved regions can be done by looking for enrichments which will select more specifically for kmers involved in regulatory motifs. For instance, one can find regulatory motifs by searching for conserved sequences enriched in intergenic regions upstream of genes as compared to control

260

#### 6.047/6.878 Lecture 15: Regulatory Motifs, Gibbs Sampling, and EM

regions such as coding sequences, since one would expect motifs to be enriched in or around promoters of genes. One can also expand this model to find degenerate motifs: we can look for conservation of smaller, non-degenerate motifs separated by a gap of variable length, as shown in the figure below. We can also extend this motif through a greedy search in order to get closer to find the local maximum likelihood motif. Finally, evolution of motifs can also reveal which motifs are degenerate; since a particular motif is more likely to be degenerate if it is often replaced by another motif throughout evolution, motif clustering can reveal which kmers are likely to correspond to the same motif.

In fact, the strategy has its biological relevance. In 2003, Professor Kellis argued that there must be some selective pressure to cause a particular sequence to be occur on specific places. His PhD. thesis on the topic can be found at the following location: �������������������������������������������������������������

images/Fig18_ConservationForTFMotifDiscovery.png

Figure 17.7: Using motif seeds to find degenerate motifs

### **17.4.2 Validation of discovered motifs with functional datasets**

These predicted motifs can then be validated with functional datasets. Predicted motifs with at least one of the following features are more likely to be real motifs: -enrichment in co-regulated genes. One can extend this further to larger gene groups; for instance, motifs have been found to be enriched in genes expressed in specific tissues -overlap with TF binding experiments -enrichment in genes from the same complex -positional biases with respect to the transcription start site (TSS): motifs are enriched in gene TSS’s -upstream vs. downstream of genes, inter- vs. intra-genic positonal biases: motifs are generally depleted in coding sequences -similarity to known transcription factor motifs: some, but not all, discovered motifs may match known motifs (however, not all motifs are conserved and _known_ motifs may not be exactly correct)

## **17.5 Evolutionary signatures for instance identification**

## **17.6 Phylogenies, Branch length score Confidence score**

### **17.6.1 Foreground vs. background. Real vs. control motifs.**

## **17.7 Possibly deprecated stuff below:**

### **17.7.1 Greedy**

While the greedy algorithm is not used very much in practice, it is important know how it functions and mainly its advantages and disadvantages compared to EM and Gibbs sampling. The Greedy algorithm works just like Gibbs sampling except for a main difference in Step 4. Instead of randomly choosing selecting a new starting location, it always picks the starting location with the highest probability.

261

6.047/6.878 Lecture 15: Regulatory Motifs, Gibbs Sampling, and EM

This makes the Greedy algorithm slightly faster than Gibbs sampling but reduces its chances of finding a global maximum considerably. In cases where the starting location probability distribution is fairly evenly distributed, the greedy algorithm ignores the weights of every other starting position other than the most likely.

## **17.8 Comparing different Methods**

The main difference between Gibbs, EM, and the Greedy algorithm lies in their maximization step after computing their _Z_ matrix. Examples of the Z matrix are graphically represented below.THis _Z_ matrix is then used to recompute theoriginal profile matrix until convergence. Some examples of this matrix are graphically represented by 17.8


<!-- Start of picture text -->
© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

Figure 17.8: Examples of the Z matrix computed via. EM, Gibbs Sampling, and the Greedy Algorithm

Intuitively, the greedy algorithm will always pick the most probable location for the motif. The EM algorithm will take an average of all values while Gibbs Sampling will actually use the probability distribution given by _Z_ to sample a motif in a step.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 17.9: Selecting motif location: the greedy algorithm will always pick the most probable location for the motif. The EM algorithm will take an average while Gibbs Sampling will actually use the probability distribution given by _Z_ to sample a motif in each step

## **17.9 OOPS,ZOOPS,TCM**

The different types of sequence model make differing assumptions about how and where motif occurrences appear in the dataset. The simplest model type is OOPS (One-Occurence-Per-Sequence) since it assumes that there is exactly one occurrence per sequence of the motif in the dataset. This is the case we have analyzed in the Gibbs sampling section. This type of model was introduced by Lawrence & Reilly (1990) [2], when they describe for the first time a generalization of OOPS, called ZOOPS (Zero-or-One-Occurrence-Per-Sequence), which assumes zero or one motif occurrences per dataset sequence. Finally, TCM (Two-Component Mixture)

262

6.047/6.878 Lecture 15: Regulatory Motifs, Gibbs Sampling, and EM

models assume that there are zero or more non-overlapping occurrences of the motif in each sequence in the dataset, as described by Baily & Elkan (1994). [1] Each of these types of sequence model consists of two components, which model, respectively, the motif and non-motif (background) positions in sequences. A motif is modelled by a sequence of discrete random variables whose parameters give the probabilities of each of the different letters (4 in the case of DNA, 20 in the case of proteins) occurring in each of the different positions in an occurrence of the motif. The background positions in the sequence are modelled by a single discrete random variable.

## **17.10 Extension of the EM Approach**

### **17.10.1 ZOOPS Model**

The approach presented before (OOPS) relies on the assumption that every sequence is characterized by only one motif (e.g., there is exactly one motif occurrence in a given sequence). The ZOOPS model takes into consideration the possibility of sequences not containing motifs.

In this case let _i_ be a sequence that does not contain a motif. This extra information is added to our previous model using another parameter _λ_ to denote the prior probability that any position in a sequence is the start of a motif. Next, the probability of the entire sequence to contain a motif is _λ_ = ( _L − W_ + 1) _∗ λ_

#### **The E-Step**

The E-step of the ZOOPS model calculates the expected value of the missing information–the probability that a motif occurrence starts in position _j_ of sequence _Xi_ . The formulas used for the three types of model are given below.


where _λ_<sup>_t_</sup> is the probablity that sequence i has a motif, _Pr_<sup>_t_</sup> ( _Xi|Qi_ = 0) is the probablity that _Xi_ is generated from a sequence i that does not contain a motif

#### **The M-Step**

The M-step of EM in MEME re-estimates the values for _λ_ using the preceding formulas. The math remains the same as for OOPS, we just update the values for _λ_ and _γ_


The model above takes into consideration sequences that do not have any motifs. The challenge is to also take into consideration the situation in which there is more than one motif per sequence. This can be

263

6.047/6.878 Lecture 15: Regulatory Motifs, Gibbs Sampling, and EM

accomplished with the more general model TCM. TCM (two-component mixture model) is based on the assumption that there can be zero, one, or even two motif occurrences per sequence.


Figure 17.10: Sequences with zero, one or two motifs.

### **17.10.2 Finding Multiple Motifs**

All the above sequence model types model sequences containing a single motif (notice that TCM model can describe sequences with multiple occurences of the same motif). To find multiple, non-overlapping, different motifs in a single dataset, one incorporates information about the motifs already discovered into the current model to avoid rediscovering the same motif. The three sequence model types assume that motif occurrences are equally likely at each position _j_ in sequences _xi_ . This translates into a uniform prior probability distribution on the missing data variables _Zij_ . A new prior on each _Zij_ had to be used during the E-step that takes into account the probability that a new width-W motif occurrence starting at position _Xij_ might overlap occurrences of the motifs previously found. To help compute the new prior on _Zij_ we introduce variables _Vij_ where _Vij_ = 1 if a width-W motif occurrence could start at position _j_ in the sequence _Xi_ without overlapping an occurrence of a motif found on a previous pass. Otherwise _Vij_ = 0.


## **17.11 Motif Representation and Information Content**

Instead of a Profile Matrix, we can also represent Motifs using information theory. In information theory, information about a certain event is communicated through a message. The amount of information carried by a message is measured in bits. We can determine the bits of information carried by a message by observing the probability distribution of the event described in the message. Basically, if we dont know anything about the outcome of the event, the message will contain a lot of bits. However, if we are pretty sure how the event is going to play out, and the message only confirms our suspicions, the message carries very few bits of information. For example, The sentence 0un will rise tomorrow” is not very surprising, so the information of that sentence if quite low.. However, the sentence 0un will not rise tomorrow” is very surprising and it has high information content. We can calculate the specific amount of information in a given message with the equation: _−_ log _p_ .

Shannon Entropy is a measure of the expected amount of information contained in a message. In other words, it is the information contained by a message of every event that could possibly occur weighted by each events probability. The Shannon entropy is given by the equation:

264

6.047/6.878 Lecture 15: Regulatory Motifs, Gibbs Sampling, and EM


Entropy is maximum when all events have an equal probability of occurring. This is because Entropy tells us the expected amount of information we will learn. If each even has the same chance of occurring we know as little as possible about the event, so the expected amount of information we will learn is maximized. For example, a coin flip has maximal entropy only when the coin is fair. If the coin is not fair, then we know more about the event of the coin flip, and the expected message of the outcome of the coin flip will contain less information.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 17.11: Entropy is maximized when both heads and tails have an equal chance of occurring

We can model a motif by how much information we have of each position after applying Gibs Sampling or EM. In the following figure, the height of each letter represents the number of bits of information we have learned about that base. Higher stacks correspond to greater certainty about what the base is at that position of the motif while lower stacks correspond to a higher degree of uncertainty. With four codons to choice from, the Shannon Entropy of each position is 2 bits. Another way to look at this figure is that the height of a letter is proportional to the frequency of the base at that position.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 17.12: The height of each stack represents the number of bits of information that Gibbs sampling or EM told us about the postion in the motif

There is a distance metric on probability distributions known as the Kullback-Leibler distance. This allows us to compare the divergence of the motif distribution to some true distribution. The K-L distance is given by


265

6.047/6.878 Lecture 15: Regulatory Motifs, Gibbs Sampling, and EM

In Plasmodium, there is a lower G-C content. If we assume a G-C content of 20%, then we get the following representation for the above motif. C and G bases are much more unusual, so their prevalence is highly unusual. Note that in this representation, we used the K-L distance, so that it is possible for the stack to be higher than 2.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 17.13: lexA binding site assuming low G-C content and using K-L distance

## **Bibliography**

- [1] Timothy L. Bailey. Fitting a mixture model by expectation maximization to discover motifs in biopolymers. In _Proceedings of the Second International Conference on Intelligent Systems for Molecular Biology_ , pages 28–36. AAAI Press, 1994.

- [2] C E Lawrence and A A Reilly. An expectation maximization (em) algorithm for the identification and characterization of common sites in unaligned biopolymer sequences. _Proteins_ , 7(1):41–51, 1990.

266

CHAPTER

## **EIGHTEEN**

REGULATORY GENOMICS

Lecturer: Pouya Kheradpour Scribe: Maria Frendberg

### **Figures**

|18.1 Challenges in Regulatory Genomics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>266|
|---|


## **18.1 Introduction**

Every cell has the same DNA, but they all have different expression patterns due to the temporal and spatial regulation of genes. Regulatory genomics explains these complex gene expression patterns. The regulators we will be discussing are:

- _Transcription Factor (TF)_ - Regulates transcription of DNA to mRNA. TFs are proteins which bind to DNA before transcription and either increase or decrease transcription. We can determine the specificity of a TF through experimental methods using protein or antibodies. We can find the genes by their similarity to know TFs.

- _Micro RNA (miRNA)_ - Regulates translation of mRNA to Proteins. miRNAs are RNA molecules which bind to mRNA after transcription and can reduce translation. We can determine the specificity of an miRNA through experimental methods, such as cloning, or computational methods, using conservation and structure.

267

6.047/6.878 Lecture 16 Regulatory Genomics

### **18.1.1 History of the Field**

### **18.1.2 Open Problems**

Both TFs and miRNAs are regulators and we can find them through both experimental and computational methods. We will discuss some of these computational methods, specifically the use of evolutionary signatures. These regulators bind to specific patterns, called motifs. We can predict the motifs to which a regulator will bind using both experimental and computational methods. We will be discussing identification of miRNAs through evolutionary and structural signatures and the identification of both TFs and miRNAs through de novo comparative discovery, which theoretically can find all motifs. Given a motif, it is difficult to find the regulator which binds to it.

A target is a place where a factor binds. There are many sequence motifs, however many will not bind; only a subset will be targets. Targets for a specified regulator can be determined using experimental methods. In Lecture 11, methods for finding a motif given a target were discussed. We will also discuss finding targets given a motif.


Figure 18.1: Challenges in Regulatory Genomics

## **18.2** **_De Novo_ Motif Discovery**

### **18.2.1 TF Motif Discovery**

Transcription Factors influence the expression of target genes as either activators or repressors by binding to the DNA near genes. This binding is guided by TF sequence specificity. The closer the DNA is to the base preference, the more likely it is that the factor will bind. These motifs can be found both computationally and experimentally. There are three main approaches for discovering these motifs.

> • _Co-Regulation_ - In Lecture 11, we discussed a co-regulation type of discovery of motifs by finding sequences which are likely to have the motif bound. We can then use enumerative approaches or

268

6.047/6.878 Lecture 16 Regulatory Genomics

alignment methods to find these motifs in the upstream regions. We can apply similar techniques to experimental data where you know where motif is bound.

- _Factor Centric_ - There are also factor centric methods for discovering motifs. These are mostly experimental methods which require a protein or antibody. Examples include SELEX, DIP-Chip, and PBMs. All of these methods are in vitro.

- _Evolutionary_ - Instead of focusing on only one factor, evolutionary methods focus on all factors. We can begin by looking at a single factor and determining which properties we can exploit. There are certain sequences which are preferentially conserved (conservation islands). However, these are not always motifs and instead can be due to chance or non-motif conservation. We can then look at many regions, find more conserved motifs, and determine which ones are more conserved overall. By testing conservation in many regions across many genomes, we increase the power. These motifs have certain evolutionary signatures that help us to identify them: motifs are more conserved in intergenic regions than in coding regions, motifs are more likely to be upstream from a gene than downstream. This is a method for taking a known motif and testing if it is conserved.

We now want to find everything that is more conserved than expected. This can be done using a hill climbing approach. We begin by enumerating the motif seeds, which are typically in 3-gap-3 form. Then, each of these seeds is scored and ranked using a conservation ratio corrected for composition and small counts. These seeds are then expanded to fill unspecified bases around the seed using hill climbing. Through these methods, it is possible to arrive at the same, or very similar seeds in different manners. Thus, our final step consists of clustering the seeds using sequence similarity to remove redundancy.

A final method that we can use is recording the frequency with which one sequence is replaced by another in evolution. This produces clusters of k-mers that correspond to a single motif.

### **18.2.2 Validating Discovered Motifs**

There are many ways that we can validate discovered motifs. Firstly, we expect them to match real motifs, which does happen significantly more often than with random motifs. However, this is not a perfect agreement, possibly due to the fact that many known motifs are not conserved and that known motifs are biased and may have missed real motifs. Positional bias. Biased towards TSS,

Motifs also have functional enrichments. If a specific TF is expressed in a tissue, then we expect the upstream region will have that factor’s motif. This also reveals modules of cooperating motifs. We also see that most motifs are avoided in ubiquitously expressed genes, so that they are not randomly turned on and off.

### **18.2.3 Summary**

There are disadvantages to all of these approaches. Both TF and region-centric approaches are not comprehensive and are biased. TF centric approaches require a transcription factor or antibody, take lots of time and money, and also have computational challenges. De novo discovery using conservation is unbiased, but it can’t match motifs to factors and requires multiple genomes.

269

6.047/6.878 Lecture 16 Regulatory Genomics

## **18.3 Predicting Regular Targets**

### **18.3.1 Motif Instance Identification**

Once potential motifs are discovered, the next step is to discover which motif matches are real. This can be done by both experimental and computational methods.

- _Experimental_ - Instances can be identified experimentally using ChIP-Chip and ChIP-Deq methods. Both of these are in vivo methods. This is done by cross linking cells. DNA is first broken into sections. Then the protein and its antibody or tagged protein is added, which binds to various sequences. These bound sequences are now pulled out and cross linking is reversed. This allows us to determine where in the genome the factor was bound. This has a high false positive rate because there are many instances where a factor binds, but is not functional. This is a very popular experimental methods, but it is limited by the availability of antibodies, which are difficult to get for many factors.

- _Computational_ - Computation approaches. There are also many computational approaches to identify instances. Single genome approaches use motif clustering. They look for many matches to increase power and are able to find regulatory regions (CRMs). However, they miss instances of motifs that occur alone and require a set of specific factors that act together. Multi-genome approaches, known as phylogentic footprinting, face many challenges. They begin by aligning many sequences, but even in functional motifs, sequences can move, mutate, or be missing. The approach taken by Kheradpour handles this by not requiring perfect conservation (by using a branch length score) and by not requiring an exact alignment (by searching within a window).

Branch Length Scores (BLS) are computed by taking a motif match and searching for it in other species. Then, the smallest subtree containing all species with a motif match is found. The percentage of total tree is the BLS. Calculating the BLS in this way allows for mutations permitted by motif degeneracy, misalighment and movement within a window, and missing motifs in dense species trees.

This BLS is then translated into a confidence score. This enables us to evaluate the likelihood of a given score and to account for differences in motif composition and length. We calculate this confidence score by counting all motif instances and control motifs at each BLS. We then want to see which fraction of the motif instances seem to be real. The confidence score is then signal/(signal+noise). The control motifs used in this calculation are produced by producing 100 shuffles of the original motif, and filtering the results by requiring that they match the genome with +/- 20% of the original motif. These are then sorted based on their similarity to known motifs and clustered. At most one motif is taken from each cluster, in increasing order of similarity, to produce our control motifs.

### **18.3.2 Validating Targets**

Similar to motif discovery, we can validate targets by seeing where they fall in the genome. Confidence selects for TF motif instances in promoters and miRNA motifs in 3’ UTRs, which is what we expect. TFs can occur on either strand, whereas miRNA must fall on only one strand. Thus, although there is no preference for TFs, miRNA are found preferentially on the plus strand.

Another method of validating targets is by computing enrichments. This requires having a background and foreground set of regions. These could be a promoter of co-regulated genes vs all genes or regions bound by a factor vs other intergenic regions. Enrichment is computed by taking the fraction of motif

270

6.047/6.878 Lecture 16 Regulatory Genomics

instances inside the foreground vs the fraction of bases in the foreground. Composition and conservation level are corrected for with control motifs. These fractions can be made more conservative using a binomial confidence interval.

Targets can then be validated by comparing to experimental instances found using ChIP-Seq. This shows the conserved CTCF motif instances are highly enriched in ChIP-Seq sites. Increasing confidence also increases enrichment. Using this, many motif instances are verified. ChIP-Seq does not always find functional motifs, so these results can further be verified by comparing to conserved bound regions. This finds that enrichment in intersections is dramatically higher. This shows where factors are binding that have an effect worthwhile conserving in evolution. These two approaches are complementary and are even more effective when used together.

## **18.4 MicroRNA Genes and Targets**

### **18.4.1 MiRNA Gene Discovery**

MiRNAs are post-transcriptional regulators that bind to mRNAs to silence a gene. They are an extremely important regulator in development. These are formed when a miRNA gene is transcribed from the genome. The resulting strand forms a hairpin at some point. This is processed, trimmed and exported to the cytoplasm. Then, another protein trims the hairpin and one half is incorporated into a RISK complex. By doing this, it is able to tell the RISK complex where to bind, which determines which gene is turned off. The second strand is usually discarded. It is a computational problem to determine which strand is which. The computational problem here is how to find the genes which correspond to these miRNAs.

The first problem is finding hairpins. Simply folding the genome produces approximately 760,000 hairpins, but there are only 60 to 200 true miRNAs. Thus we need methods to help improve specificity. Structural features, including folding energy, loops (number, symmetry), hairpin length and symmetry, substructures and pairings, can be considered, however, this only increases specificity by a factor of 40. Thus structure alone cannot predict miRNAs. Evolutionary signatures can also be considered. MiRNA show characteristic conservation properties. Hairpins consist of a loop, two arms and flanking regions. In most RNA, the loop is the most well conserved due to the fact that it is used in binding. In miRNA, however, the arms are more conserved because they determine where the RISK complex will bind. This increases specificity by a factor of 300. Both these structural features and conservation properties can be combined to better predict potential miRNAs.

These features are combined using machine learning, specifically random forests. This produces many weak classifiers (decision trees) on subsets of positives and negatives. Each tree then votes on the final classification of a given miRNA. Using this technique allows us to reach the desired sensitivity (increased by 4,500 fold).

### **18.4.2 Validating Discovered MiRNAs**

Discovered miRNAs can be validated by comparing to known miRNAs. An example given in class shows that 81% of discovered miRNAs were already known to exist, which shows that these methods perform well. The putative miRNAs have yet to be tested, however this can be difficult to do as testing is done by cloning.

Region specificity is another method for validating miRNAs. In the background, hairpins are fairly evenly

271

6.047/6.878 Lecture 16 Regulatory Genomics

distributed between introns, exons, intergenic regions, and repeats and transposons. Increasing confidence in predictions causes almost all miRNAs to fall in introns and intergenic regions, as expected. These predictions also match sequencing reads.

This also produced some genomic properties typical of miRNAs. They have a preference for transcribed strand. This allows them to piggyback in intron of real gene, and thus not require a separate transcription. They also clustering with known and predicted miRNAs. This indicates that they are in the same family and have a common orgin.

### **18.4.3 MiRNA’s 5’ End Identification**

The first seven bases determine where an miRNA binds, thus it is important to know exactly where clevage occurs. If this clevage point is wrong by even two bases, the miRNA will be predicted to bind to a completely different gene. These clevage points can be discovered computationally by searching for highly conserved 7-mers which could be targets. These 7-mers also correlate to a lack of anti-targets in ubiquitously expressed genes. Using these features, structural features and conservational features, it is possible to take a machine learning approach (SVMs) to predict clevage site. Some miRNAs have no single high scoring position, and these also show imprecise processing in the cell. If the star sequence is highly scored, then it tends to be more expressed in the cell also.

### **18.4.4 Functional Motifs in Coding Regions**

Each motif type has distinct signatures. DNA is strand symmetric, RNA is strand-specific and frameinvariant, and Protein is strand-specific and frame-biased. This frame-invariance can be used as a signature. Each frame can then be evaluated separately. Motifs due to di-codon usage biases are conserved in only one frame offset while motifs due to RNA-level regulation are conserved in all three frame offsets. This allows the ability to distinguish overlapping pressures.

## **18.5 Current Research Directions**

## **18.6 Further Reading**

- **18.7 Tools and Techniques**

## **18.8 What Have We Learned?**

## **Bibliography**

272

CHAPTER

## **NINETEEN**

## EPIGENOMICS/CHROMATIN STATES

### **Figures**

- 19.1 A. There is a wide diversity of modifications in the epigenome. Some regions of DNA are compactly wound around histones, making the DNA inaccessible and the genes inactive. Other regions have more accessible DNA and thus active genes. Epigenetic factors can bind to the tails of these histones to modify these properties. B. Histone modifications provide information about what types of proteins are bound to the DNA and what the function of the region is. In this example, The histone modifications allow for an enhancer region (potentially over 100 kilo bases away) to interact with the promoter region. [6] . . 290

- 19.2 The method of chromatin immunoprecipitation [5]. The steps in this figure correspond to the six steps of the procedure. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290

- 19.3 (Top) In the Burrows-Wheeler forward transformation rotations are generated and sorted. The last column of the sorted list (bolded) consists of the transformed string. (Bottom)In the Burrows-Wheeler reverse transformation the transformed string is sorted, and two columns are generated: one consisting of the original string and the other consisting of the sorted. These effectively form two columns from the rotations in the forward transformation. This process is repeated until the complete rotations are generated. . . . . . . . . . 291

- 19.4 To use input DNA as a control, one can run the ChIP experiment as normal while simultaneously running the same experiment (with same DNA) without an antibody. This generates a background signal for which we can correct. . . . . . . . . . . . . . . . . . . . 291

- 19.5 In the figure above each column is a color-coded histogram that encodes the fraction of all mapped reads that have base score Q (y-axis) at each position(x-axis). A low average per base score implies greater probability of mismappings. We typically reject reads whose average score Q is less than 10. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 292

- 19.6 A sample signal track. Here, the red signal is derived from the number of reads that mapped to the genome at each position for a ChIP-seq experiment with the target H3K36me3. The signal gives a level of enrichment of the mark. . . . . . . . . . . . . . . . . . . . . . . . . . 292

- 19.7 Sample signal tracks for both the true experiment and the background (control). Regions are considered to have statistically significant enrichment when the true experiment signal values are well above the background signal values. . . . . . . . . . . . . . . . . . . . . . . 292

- 19.8 Example of the data and the annotation from the HMM model. The bottom section shows the raw number of reads mapped to the genome. The top section shows the annotation from the HMM model. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293

273

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

- 19.9 Emission probabilities for the final model with 51 states. The cell corresponding to mark _i_ and state _k_ represents the probability that mark _i_ is observed in state _k_ . . . . . . . . . . 294

- 19.10Transition probabilities for the final model with 51 states. The transition probability increases from green to red. Spatial relationships between neighboring chromatin states and distinct sub-groups of states are revealed by clustering the transition matrix. Notably, the matrix is sparse, so indicating that most are not possible. . . . . . . . . . . . . . . . . 295

- 19.11Chromatin state definition and functional interpretation. [7] a. Chromatin mark combinations associated with each state. Each row shows the specific combination of marks associated with each chromatin state and the frequencies between 0 and 1 with which they occur in color scale. These correspond to the emission probability parameters of the HMM learned across the genome during model training. b. Genomic and functional enrichments of chromatin states, including fold enrichment in different part of the genome (e.g. transcribed regions, TSS, RefSeq 5 end or 3end of the gene etc), in addition to fold enrichment for evolutionarily conserved elements, DNaseI hypersensitive sites, CpG islands, etc. All enrichments are based on the posterior probability assignments. c. Brief description of biological state function and interpretation (chr, chromatin; enh, enhancer). . . . . . . . . 296

## **19.1 Introduction**

The human body contains approximately 210 different cell types, but each cell type shares the same genomic sequence. In spite of having the same genetic code, cells not only develop into distinct types from this same sequence, but also maintain the same cell type over time and across divisions. This information about the cell type and the state of the cell is called _epigenomic_ information. The epigenome (“epi” means above in Greek, so epigenome means above genome) is the set of chemical modifications or marks that influence gene expression and are transferred across cell divisions and, in some limited cases, across generations of organisms.

As shown in Figure 19.1, epigenomic information in a cell is encoded in diverse ways. For example, methylation of DNA (e.g. at CpG dinucleotides) can alter gene expression. Similarly, positioning of nucleosomes (unit of packing of DNA) determines which parts of DNA are accessible for transcription factors to bind to and other enzymes. Almost two decades of work have revealed hundreds of post translational modifications of histone tails. Since an extremely large number of histone modification states are possible for any given histone tail, the ”histone code hypothesis” has been proposed. This hypothesis states that particular combinations of histone modifications encode information. Although a controversial hypothesis, it has guided the epigenetics field. The core of epigenetics is understanding how chemical modifications to chromatin (be they DNA methylation, histone modifications or chromatin architecture) are established and how the cell ”interprets” this information to establish and maintain gene expression states.

In this chapter we will explore the experimental and computational techniques used to uncover chromatin states within a cell type. We will learn how chromatin immunoprecipitation can be used to infer the regions of the genome bound by a protein or interest, and a common algorithm (the Burrows-Wheeler) transform can be used to rapidly map large numbers of short sequencing reads to a reference genome. From this we then abstract a level and use a hidden Markov model (HMM) to segment the genome into regions which share similar chromatin states. We will close by showing how these comprehensive maps of chromatin states can be compared across cell types and can be used to provide information on how cell states are established and maintained and the impact of genetic variation on gene expression.

274

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

## **19.2 Epigenetic Information in Nucleosomes**

In order to fit two meters of DNA into a 5-20 _µm_ diameter cell nucleus and arrange the DNA for easy access to transcriptional machinery, DNA is packaged into chromatin. Nucleosomes form the unit of this packaging. A nucleosome is composed of DNA approximately 150-200 bp long wrapped around an octamer consisting of two copies each of histone proteins H2A, H2B, H3, and H4 (and occasionally a linker histone H1 or H5). While the structure and importance of higher-level packaging of nucleosomes is less known, the lower-level arrangement and modification of nucleosomes is very important to transcriptional regulation and the development of different cell types. Histone proteins H3 and H4 are the most highly conserved proteins in the eukaryotic domain of life.

Nucleosomes encode epigenetic information in two main ways: chromatin accessibility and histone modifications.

First, the nucleosomes’ positions on the DNA determine which parts of DNA are accessible. Nucleosomes are often positioned at the promoters of inactive genes. To initiate transcription of a gene, transcription factors (TFs) and the RNA polymerase complex have to bind to its promoter. Therefore, when a gene becomes active, the nucleosomes located at its promoter are often removed from the promoter to allow RNA polymerase to initiate transcription. Hence, nucleosome positioning on the DNA is stable, yet mutable. This property of stability and mutability is a prerequisite for any form of epigenetic information because cells need to maintain the identity of a particular cell type, yet still be able to change their epigenetic state to respond to environmental circumstances.

Chromatin accessibility can also be modulated by transcribed RNA (specifically, “enhancer RNA,” or eRNA) floating around the nucleus. In particular, Mousavi et al. found in 2013 that eRNAs, which are transcribed at extragenic enhancer regions, enhance RNA pol II occupancy (which is rate-limited by chromatin accessibility) and deployment of other transcriptional machinery, leading to enhanced expression of distal target genes [9].

Second, histones contain unstructured tails protruding from the globular core domains that comprise the nucleosome octamer. These tails can undergo post-translational modification such as methylation, acetylation and phosphorylation, each of which affect gene expression. Some proteins involved in transcriptional regulation bind specifically to particular histone modifications or combinations of modifications, and recruit yet more transcription factors which enhance or repress expression of nearby genes. Thus, the “histone code hypothesis” posits that different combinations of histone modifications at specific genomic loci encode biological function via differential transcriptional regulation. In this model, histone modifications are analogous to different readers marking sections of a book with different-colored post-it notes – histone modifications allow the same genome to be interpreted (i.e., transcribed) differently at different times and in different tissues. There are over 100 distinct histone modifications that have been found experimentally. Six of the most well-characterized histone modifications, along with the typical signature widths of their appearances in the genome and their putative associated regulatory elements, are listed in Table 19.1. Note that all of these modifications are on lysines in H3 and H4. Modifications of H3 and H4 are most well-characterized because H3 and H4 are the most highly conserved histones (making modifications of those histones more likely to have conserved regulatory function) and because good antibodies exist for all of the commonly-observed modifications of those histones.

Histone modifications are so commonly-referenced that a shorthand has been developed to identify them. This shorthand consists of the name of the histone protein, the amino acid residue on its tail that has been modified and the type of modification made to this residue. To illustrate, the fourth residue from the N-terminus of histone H3, lysine, is often methylated at the promoters of active genes. This modification is described as H3K4me3 (if methylated thrice). The first part of the shorthand corresponds to the histone protein, in this case H3; K4 corresponds to the 4th residue from the end, in this case a lysine, and me3

275

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

corresponds to the actual modification, the addition of 3 methyl groups in this case.

|Histone Modification|Signature|Associated Regulatory Element|
|---|---|---|
|H3K4me1|(wide) focal|active promoters/enhancers|
|H3K4me3|(wide) focal|active promoters/enhancers|
|H3K9me3|wide|repressed regions|
|H3K27ac|focal|active promoters/enhancers|
|H3K27me3|wide|repressed regions|
|H3K36me3|wide|transcribed regions|


Table 19.1: Six of the most well-characterized histone modifications along with their typical signature widths and putative associated regulatory elements. “Focal” indicates that each instance of the histone modification has a relatively narrow signature in the genome (peak width _<_ 5kb) whereas “wide” indicates wide signatures.

One example of epigenetic modifications influencing biological function is often seen in enhancer regions of the genome. Often these enhancer regions are far away from the genes and promoters that they regulate. The enhancer is able to come into contact with a specific promoter by histone modification (acetylation and methylation). This causes the DNA to fold upon itself to bring the promoter, enhancer, and recruited transcription factors into contact, activating the previously repressed promoter. This system can be very dynamic such that less than a minute after histone modification the cell will show signs of epigenetic influence, while other modifications (mainly those during development) will show themselves in a slower manner. This is also an example how how certain types of modifications of the histones can help us to predict enhancer regions.

It is possible for more than one histone modification to be present at a given genomic locus, and histone modifications thereby can act cooperatively and competitively. It is even possible for the two copies of a given histone protein within the same nucleosome to have different modifications (though usually the histone modification “writers” will localize together, thereby creating the same modification on both copies within the nucleosome). Thus, it is necessary to simultaneously take into account all histone modifications in a genomic region in order to accurately call the chromatin state of that region. As described in Section , with the completion of the Roadmap Epigenome Project in 2015, a robust hidden Markov model (with histone modifications as emissions and chromatin states as hidden states) can be used to do so.

## **_Did You Know?_**

The simplest organisms that have epigenetic modifications are yeasts. Yeast is a single celled organism; thus, epigenetic modifications are not responsible for cell differentiation. As organisms become more complex they tend to have more epigenetic modifications.

### **19.2.1 Epigenetic Inheritance**

The extent to which epigenetic/epigenomic features are heritable is poorly understood and is therefore the subject of much debate and ongoing investigation. In organisms that reproduce sexually, most epigenetic modifications are lost during meiosis and/or at fertilization, but some modifications are sometimes maintained. Additionally, biases exist in the ways in which paternal versus maternal epigenetic marks are removed or remodeled during this process. In particular, maternal DNA methylation is often retained at fertilization, whereas paternal DNA is almost always completely demethylated. Furthermore, for unknown reasons, some genomic elements, such as centromeric satellites, are more likely to evade epigenetic reset. In cases where epigenomic erasure does not occur completely at meiosis and fertilization, trans-generational epigenetic inheritance can occur. See generally [4].

Another mechanism likely to be governed by epigenetic inheritance is the phenomenon of parental im-

276

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

printing. In parental imprinting, certain autosomal genes are expressed if and only if they are inherited from an individual’s mother, and other automsomal genes are expressed if and only if they are inherited from an individual’s father. Examples are the Igf2 gene in mice (only expressed if inherited from the father) and the H19 gene in mice (only expressed if inherited from the mother). There are no changes in the DNA sequence of these genes, but extra methyl groups are observed on certain nucleotides within the inactivated copy of the gene. The mechanisms and causality of this imprinting are poorly understood.

## **19.3 Epigenomic Assays**

### **19.3.1 ChIP: a method for determining where proteins bind to DNA or where histones are modified**

Given the importance of epigenomic information in biology, great efforts have been made to study signals that quantify this information. One common method for epigenomic mark measurement is called chromatin immunoprecipitation (ChIP). **ChIP technology** yields fragments of DNA whose location in the genome denote the positions of a particular histone modification or transcription factor. The procedures of ChIP are described as follows and are depicted in Figure 19.2:

1. Cells are exposed to a cross-linking agent such as formaldehyde, which causes covalent bonds to form between DNA and its bound proteins (e.g., histones with specific modifications).

2. Genomic DNA is isolated from the cell nucleus.

3. Isolated DNA is sheared by sonication or enzymes.

4. Antibodies are grown to recognize a specific protein, such as those involved in histone modification. The antibodies are grown by exposing the proteins of interest to mammals, such as goats or rats, whose immune response then causes the production of the desired antibodies.

5. Antibodies are added to the solution to immunoprecipitate and purify the complexes.

6. The cross-linking between the protein and DNA is reversed and the DNA fragments specific to the epigenetic marks are purified.

After a ChIP experiment, we have short sequences of DNA that correspond to places where histones were bound to the DNA. To identify the location of these DNA fragments in the genome, one can hybridize them to known DNA segments on an array or gene chip and visualize them with fluorescent marks; this method is known as ChIP-chip. Alternatively, one can do massive parallel next-generation sequencing of these fragments; this is known as **ChIP-seq** . The latter approach, ChIP-seq, is a newer approach that is used much more frequently. It is preferred because it has a wider dynamic range of detection and avoids problems like cross-hybridization in ChIP-chip.

Each sequence tag is 30 base pairs long. These tags are mapped to unique positions in the reference genome of 3 billion bases. The number of reads depending on sequencing depth, but typically there are on the order of 10 million mapped reads for each ChIP-seq experiment.

There is a fairly standard pipeline used to infer the enrichment of the protein of interest at each site in the genome given a set of short sequencing reads from a ChIP-seq experiment. First, the DNA fragments must be mapped to the DNA (called read mapping). Next, we must determine which regions of the genome have statistically significant enrichment of the protein of interest (called peak calling). After these preprocessing

277

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

steps, we can build different supervised and unsupervised models to study chromatin states and their relation to biological function. We look at each of these steps in turn.

### **19.3.2 Bisulfite Sequencing: a method for determining where DNA is methylated**

DNA methylation was the first epigenomic modification to be discovered and is an important transcriptional regulator in that the methylation of cytosine residues in CpG dinucleotides results in “silencing,” or repression, of transcription. Bisulfite sequencing is a method by which DNA is treated with bisulfite before sequencing, allowing the precise determination of the nucleotides at which the DNA had been methylated. Bisulfite treatment converts unmethylated cytosine residues to uracil, but does not affect methylated cytosines. Thus, genomic DNA can be sequenced with or without bisulfite treatment, and the sequences can be compared, and the sites at which cytosine has not been converted to uracil in the treated DNA (or, equivalently, sites at which there is bisulfite-generated difference between the treated and untreated sequences) are sites at which cytosine was methylated. This analysis assumes complete conversion of unmethylated cytosine residues to uracil, so incomplete conversion can result in false positives (i.e., nucleotides identified as methylated but which in fact were not methylated) [11].

## **19.4 Primary data processing of ChIP data**

### **19.4.1 Read mapping**

The problem of **read mapping** seeks to assign a given read to the best matching location in the reference genome. Given the large number of reads and the size of human genome, one common requirement of all read mapping algorithms is that they be efficient in both space and time. Furthermore, they must allow mismatches due to sequencing errors and SNPs.

Based on previous lectures, we know various ways to perform mapping of reads: sequence alignment ( _O_ ( _mn_ ) time) and hash-based approaches such as BLAST, for example. Other approaches exist as well: linear time string matching ( _O_ ( _m_ + _n_ ) time) and suffix trees and suffix arrays ( _O_ ( _m_ ) time). However, a problem with all these techniques is that they have a large memory requirement (often _O_ ( _mn_ )). Instead, state-of-the-art techniques based on the Burrows-Wheeler transformation [1] are used. These run in _O_ ( _m_ ) time and require just _O_ ( _n_ ) space.

The **Burrows-Wheeler transform** originally arose from the need to compress information. It takes a long string and rearranges it in a way that has adjacent repeating letters. This string can be compressed because, for example, instead of writing 100 A’s the computer can now just indicate that there are 100 A’s in a row. The Burrows-Wheeler transform also has some other special properties that we will exploit to search in sublinear time.

The Burrows-Wheeler transform creates a unique transformed string that is shorter than the original string. It also can be reversed easily to generate the original string, so no information is lost. The transformed string is in sorted order, which allows for easy searching. The details of Burrows-Wheeler transformation are described below and are illustrated in Figure 19.3.

First, we produce a transform from an original string by the following steps. In particular, we produce a transform of the reference genome.

278

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

1. For a given reference genome, add a special character at the beginning and end of the string (e.g., “BANANA” becomes `^BANANA@` ). Then generate all the rotations of this string (e.g., one such rotation would be `NANA@^BA` ).

2. Sort the rotations lexicographically — i.e., in alphabetical order — with special characters sorted last.

3. Only keep the last column of the sorted list of rotations. This column contains the transformed string

Once a Burrows-Wheeler transform has been computed, it is possible to reverse the transform to compute the original string. This can be done with the procedure in Figure **??** . Briefly, the reverse transformation works as follows: given the transformed string, sort the string characters in alphabetical order; this gives the first column in the transform. Combine the last column with the first to get pairs of characters from the original rotations. Sort the pairs and repeat.

By using sorting pointers rather than full strings, it is possible to generate this transform of the reference genome using a space that is linear in its size. Furthermore, even with a very large number of reads, it is only necessary to do the transform one in a forward direction. After counting the reads in the transformed space, it is then only necessary to do the reverse transform once to map the counts to genome coordinates.

In particular, from the Burrows-Wheeler transform we observe that all occurrences of the same suffix are effectively next to each other rather than scattered throughout the genome. Moreover, the _i_<sup>_th_</sup> occurrence of a character in the first column corresponds to the _i_<sup>_th_</sup> occurrence in the last column. Searching for substrings using the transform is also easy. Suppose we are looking for the substring “ANA” in the given string. Then the problem of search is reduced to searching for a prefix “ANA” among all possible sorted suffixes (generated by rotations). The last letter of the substring (“A”) is first searched for in the first letters of the sorted rotations. Then, the one-letter rotations of these matches are considered; the last two letters of the substring (“NA”) are searched for among the first two letters of these one-letter rotations. This process can be continued with increasing length suffixes to find the substring as a prefix of a rotation. Specifically, each read is searched for and is found as a prefix of a rotation of the reference genome; this gives the position of the read in the genome. By doing a reverse transform, it is possible to find the genomic coordinates of the mapped reads.

Note that this idea is no faster in theory than hashing, but it can be faster in practice because it uses a smaller memory footprint.

### **19.4.2 Quality control metrics**

As with all experimental data, ChIP methods contain biases and their output may be of varied quality. As a result, before processing the data, it is necessary to control for these biases, to determine which reads in the data achieve a certain level of quality, and to set target thresholds on the quality of the data set as a whole. In this section we will describe these **quality control** problems and metrics associated with them.

#### **QC1: Use of input DNA as control**

First, the reads given by ChIP are _not_ uniformly scattered in the genome. For example, accessible regions of the genome can be fragmented more easily, leading to non-uniform fragmentation. To control for this bias, we can run the ChIP experiment on the same portion of DNA without using an antibody. This yields input DNA, which can then be fragmented and mapped to give a signal track that can be thought of as a background — i.e., reads we would expect by chance. (Indeed, even in the background we do not see

279

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

uniformity.) Additionally, we have a signal track for the true experiment, which comes from the chromoimmunoprecipitated DNA. Shown in Figure 19.4

#### **QC2: Read-level sequencing quality score threshold**

When sequencing DNA, each base pair is associated with a quality score. Thus, the reads given by ChIPseq contain quality scores on the base pair level, where lower quality scores imply a greater probability of mismappings. We can easily use this information in a preprocessing step by simply rejecting any reads whose average quality score falls below some threshold (e.g., only use reads where Q, the average quality score, is greater than 10). Shown in Figure 19.5

#### **QC3: Fraction of short reads mapped**

Each read that passes the above quality metric may map to exactly one location in the genome, to multiple locations, or to no locations at all. When reads map to multiple locations, there are a number of approaches for handling this:

- A conservative approach: We do not assign the reads to any location because we are so uncertain. Con: we can lose signal

- A probabilistic approach: We fractionally assign the reads to all locations. Con: can add artifacts (unreal peaks)

- A sampling approach: We only select one location at random for a read. Chances are, across many reads, we will assign them uniformly. Con: can add artifacts (unreal peaks)

- An EM approach: We can map reads based on the density of unambiguous reads. That is, many unique reads that map to a region give a high prior probability that a read maps to that region. Note: we must make the assumption that the densities are constant within each region

- A paired-end approach: Because we sequence both ends of a DNA fragment, if we know the mapping of the read from one end, we can determine the mapping of the read at the other end even if it is ambiguous.

Either way, there will likely be reads that do not map to the genome. One quality control metric would be considering the fraction of reads that map; we may set a target of 50%, for instance. Similarly, there may be regions to which no reads map. This may be due to a lack of assembly coverage or too many reads mapping to the region; we treat unmappable regions as missing data.

#### **QC4: Cross-correlation analysis**

An additional quality control that is cross-correlation analysis. If single-end reads are employed, the a DNA binding protein will generate a peak of reads mapping to the forward strand offset a distance roughly equal to the DNA fragment length from a peak of reads mapping to the reverse strand. A similar pattern is generated from paired end reads, in which read ends fall into two groups with a given offset, one read end will map to the forward strand and the other to the reverse strand. The average fragment length can be inferred by computing the correlation between the number of reads mapping to the forward strand and number of

280

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

reads mapping to the reverse strand as a function of distance between the forward and reverse reads. The correlation will peak at the mean fragment length.

The cross-correlation analysis also provides information on the quality of the ChIP-seq data set. Input DNA should not contain any real peaks, but often shows a strong cross-correlation at a distance equal to the read length. This occurs because some reads map uniquely in between regions that are unmappable. If a read can map uniquely at position x in between two unmappable regions on the forward strand, then a read can also map uniquely to the reverse strand at position x + r -1, where r is the read length. Reads that map in this manner generate the strong cross- correlation at distance equal to the read length in the input DNA. If a ChIP-seq experiment was unsuccessful and did not significantly enrich for the protein of interest, then a large component of the reads will be similar to the unenriched input, which will produce a peak in the cross-correlation at read length. Thus, the strength of the cross-correlation at read length relative to the strength at fragment length can be used to evaluate the quality of the ChIP-seq data set. Acceptable ChIP-seq libraries should have a cross-correlation at fragment length at least as high as at read-length, and the higher the ratio between the fragment-length cross-correlation and the read-length cross-correlation, the better.

#### **QC5: Library Complexity**

As a final quality control metric, we can consider the complexity of the library, or the fraction of reads that are non-redundant. In a region with signal, we might expect reads to come from all positions in that region; however, we sometimes see that only a small number of positions in a region have reads mapping to them. This may be the result of an amplification artifact in which a single read amplifies much more than it should. Consequently, we consider the non-redundant fraction of a library:

No. of distinct unique-mapping reads

NRF = No. of unique mapping reads

This value measures the complexity of the library. Low values indicate low complexity, which may occur, for example, when there is insufficient DNA or one DNA fragment is over-sequenced. When working with at least 10 million uniquely mapped reads, we typically set a target of at least 0.8 for the NRF.

### **19.4.3 Peak Calling and Selection**

After reads are aligned, signal tracks as shown in Figure 19.6 can be generated. This data can be ordered into a long histogram spanning the length of the genome, which corresponds to the number of reads (or degree of fluorescence in the case of ChIP-chip) found at each position in the genome. More reads (or fluorescence) suggests a stronger presence of the epigenetic marker of interest at this particular location.

In particular, to generate these signal tracks we transform the read counts into a normalized intensity signal. First, we can use the strand cross-correlation analysis to estimate the fragment length distribution _f_ . Since we now know _f_ , as well as the length of each read, we can extend each read (typically just 36 bp) from the 5’ to 3’ direction so that its length equals the average fragment length. Then, rather than just summing the intensity of each base in the original reads, we can sum the intensity of each base in the extended reads from both strands. In other words, even though we only sequence a small read, we are able to use information about an entire segment of which that read is a part. We can do this same operation on the control data. This yields signal tracks for both the true experiment and the control, as shown in Figure 19.7.

To process the data, we are first interested in using these signal tracks to discover regions (i.e., discrete intervals) of enrichment. This is the goal of **_peak calling_** . There are many programs that perform peak

281

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

calling with different approaches. For example, MACS uses a local Poission distribution as its statistical model, whereas PeakSeq uses a conditional binomial model.

One way to model the read count distribution is with a Poisson distribution. We can estimate the expected read count, _λ_ local from the control data. Then,


Thus, the Poisson _p_ -value for a read count _x_ is given by Pr(count _≥ x_ ). We specify a threshold _p_ -value (e.g., 0.00001) below which genomic regions are considered peaks.

We can transform this _p_ -value into an empirical false discovery rate, or eFDR, by swapping the ChIP (true) experiment data with the input DNA (control) tracks. This would yield the locations in the genome where the background signal is higher than the ChIP signal. For each _p_ -value, we can find from both the ChIP data and the control data. Then, for each _p_ -value, the eFDR is simply the number of control peaks divided by the number of ChIP peaks. With this, we can then choose which peaks to call based on an eFDR threshold.

A major problem that arises is that no single universal eFDR or _p_ -value threshold can be used. Ideal thresholds depend on a range of factors, including the ChIP, the sequencing depth, and the ubiquity of the target factor. Furthermore, small changes in the eFDR threshold can yield very large changes in the peaks that are discovered. An alternative measure is the Irreproducible Discovery Rate, or IDR, and this measure avoids these FDR-specific issues.

#### **Irreducible Discovery Rate (IDR)**

A major drawback of using traditional statistical methods to evaluate the significance of ChIP-seq peaks is that FDR and p-value-based approaches make particular assumptions regarding the relationship between enrichment and significance. Evaluating the significance of ChIP peaks using IDR rather than a p-value or FDR is advantageous because it allows us to leverage the information present in biological replicates to call peaks without setting a threshold for significance. IDR-based approaches rely upon the idea that real signal is likely to be reproducible between replicates, whereas noise should not be reproducible. Using IDR to call significant peaks returns peaks that satisfy a given threshold for significance. To determine which peaks are significant via IDR, the peaks in each biological replicate are ranked based on their enrichment in descending order.The top N peaks in each replicate are then compared against each other, and the IDR for a given replicate is the fraction of peaks present in the top N peaks in the replicate that are not present in the other replicates (i.e, the fraction of peaks that are not reproducible between replicates). To develop more mathematical intuition, the following (entirely optional) subsection will rigorously introduce the concept of the IDR.

#### **Mathematical Derivation of the IDR**

Since the IDR utilizes ranks, this mean that the marginal distributions are uniform, and the information is mostly encoded in the joint distributions of the ranks across biological replicates. Specifically, when the marginal distributions are uniform, we can model the joint distributions through a **copula** model. Simply put, a copula is a multivariate probability distribution in which the marginal probability of each variable is uniform. **Skar’s Theorem** states that there exists at least one copula function which allows us to express the joint in terms of the dependence of the marginal distributions.


282

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

Where _Cx_ is the copula function and the _F_ ( _x_ ) is the cumulative distribution for a variable _x_ . Given this information, we can set a Bernoulli distribution _Ki ∼_ Bern( _πi_ ) that denotes whether the _i_ th peak is from the consistent set or the spurious set. We can derive _z_ 1 = ( _z_ 1 _,_ 1 _, z_ 1 _,_ 2) if _Ki_ = 1 or _z_ 0 = ( _z_ 0 _,_ 1 _, z_ 0 _,_ 2) if _Ki_ = 0 (where _z_ 0 _,i_ means that it’s from the spurious set in biological replicate _i_ ). Using this, we can model the _z_ 1 _,_ 1 and _z_ 0 _,_ 1 models as the following:


We can utilize two different models to model whether it comes from the spurious set (denoted by 0), or the real set (1). If the real set, we have _µ_ 1 _>_ 0 and 0 _< ρ_ 1 _<_ 1, whereas in the null set we have _µ_ 0 = 0, and _σ_ 0<sup>2= 1.Wecanmodelavariable</sup><sup>_ui,_1and</sup><sup>_ui,_2withthefollowingformulas:</sup>


Where Φ is the normal cumulative distribution function. Then, let the observed _xi,_ 1 = _F_<sup>_−_1</sup> ( _ui,_ 1) and _xi,_ 2 = _F_<sup>_−_1</sup> ( _ui,_ 2), where _F_ 1 and _F_ 2 are the marginal distributions of the two coordinates. Thus, for a signal _i_ , we have:


We can express _h_ 0 and _h_ 1 with the following normal distributions, similar to the _z_ 1 and _z_ 2 that were defined above:


We _P_ ( _K_ can _i_ = 1now _|_ ( _x_ infer _i,_ 1 _, x_ the _i,_ 2);parameters _θ_ ˆ). Thus, we _θ_ = (can _µ_ define1 _, ρ_ 1 _, σ_ the1 _, π_ 0local), usingirreproduciblea EM algorithm,discoverywhereratetheas:inference is based on


So to control the IDR at some level _α_ , we can rank ( _xi,_ 1 _, xi,_ 2) by their IDR values. We can then select ( _x_ ( _i_ ) _,_ 1 _, x_ ( _i_ ) _,_ 2) _, i_ = 1 _. . . l_ , where


IDR is analogous to a FDR control in this copula mixture model. This subsection summarizes the information provided in this lecture: `https://www.biostat.wisc.edu/~kendzior/STAT877/SK_2.pdf` . The original paper, along with an even more detailed formulation of IDR, can be found in Li et al. [10]

#### **Advantages and use cases of the IDR**

IDR analysis can be performed with increasing N, until the desired IDR is reached (for example, N is increased until IDR=0.05, meaning that 5% of the top N peaks are not reproducible). Note that N can be

283

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

different for different replicates of the same experiment, as some replicates may be more reproducible than others due to either technical or biological artifacts.

IDR is also superior to simpler approaches to use the reproducibility between experiments to define significance. One approach might be to take the union of all peaks in both replicates as significant, however; this method will accept both real peaks and the noise in each data set. Another approach is to take the intersection of peaks in both replicates, that is, only count peaks present in both data sets as significant. While this method will very effectively eliminate spurious peaks, it is likely to miss many genuine peaks. IDR can be thought of as combining both these approaches, as it accepts all peaks, regardless as to whether they are reproducible, so long as the peaks have sufficient enrichment to fall within the segment of the data with an overall irreproducibility rate above a given threshold. Another advantage to IDR is that it can still be performed even if biological replicates are not available, which can often be the case for ChIP experiments performed in rare cell types. Psuedo-replicates can be generated from a single data set by randomly assigning half the reads to one pseudo-replicate and half to another pseudo-replicate.

#### **Interpreting Chromatin Marks**

We now move onto techniques for interpreting chromatin marks. There are many ways to analyze epigenomic marks, such as aggregating chromatin signals (e.g., H3K4me3) on known feature types (e.g., promoters of genes with high or low expression levels) and performing supervised or unsupervised machine learning methods to derive epigenomic features that are predictive of different types of genomics elements such as promoters, enhancers or large intergenic non-coding RNAs. In particular, in this lecture, we examine in detail the analysis of chromatin marks as done in [7].

## **19.5 Annotating the Genome Using Chromatin Signatures**

The histone code hypothesis suggests that chromatin-DNA interactions are guided by **combinatorial histone modifications** . These combinatorial modifications, when taken together, can in part determine how a region of DNA is interpreted by the cell (i.e. as a transcription factor binding domain, a splice site, an enhancer region, an actively expressed gene, a repressed gene, or a non functional region). We are interested in interpreting this “code” (i.e. determining from histone marks at a region whether the region is a transcription start site, enhancer, promoter, etc.). With an understanding of the combinatorial histone marks, we can annotate the genome into functional regions and predict novel enhancers, promoters, genes, etc. The challenge is that there are dozens of marks and they exhibit complex combinatorial effects.

Stated another way, DNA can take on a series of (hidden) states (coding, noncoding, etc). Each of these states emits a specific combination of epigenetic modifications (H3K4me3, H3K36me3, etc) that the cell recognizes. We want to be able to predict these hidden, biologically relevant states from observed epigenetic modifications.

In this section, we explore a technique for interpreting the “code” and its application to a specific dataset [7], which measured 41 chromatin marks across the human genome.

284

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

### **19.5.1 Data**

Data for this analysis consisted of 41 chromatin marks including acetylations, methylations, H2AZ, CTCF and PollI in CD4 T cells. First, the genome was divided into 200 bp non-overlapping bins in which the binary absence or presence of each of the 41 chromatin marks was determined. This data was processed using **data binarization** , in which each mark in each interval is assigned a value of 0 or 1 depending on whether the enrichment of the mark’s signal in that interval exceeds a threshold. Specifically, let _Cij_ be the number of reads detected by ChIP-seq for mark _i_ , mapping to the 200bp bin _j_ . Let _λi_ be the average number of reads mapping to a bin for mark _i_ . The mark _i_ is determined to be present in bin _j_ if _P_ ( _X > Cij_ ) is less than the accepted threshold of 10<sup>_−_4</sup> where X is a Poisson random variable with mean _λi_ and absent otherwise. The threshold is user defined, similar to a Poisson p-value. In order words, the read enrichment for a specific bin has to be significantly greater than a random process of putting reads into bins. An example for chromatin states around the CAPZA2 gene on chromosome 7 is shown in Figure 19.8. So in this way, for each mark _i_ , we can label each bin _j_ with a 1 if the mark is present and a 0 if it isn’t. Looking at the data as a whole, we can think of it as large binary matrix, where each row corresponds to a mark and each column corresponds to a bin (which is simply a 200bp region of the genome).

Additional data used for analysis included gene ontology data, SNP data, expression data, and others.

### **19.5.2 HMMs for Chromatin State Annotation**

Our goal is to identify biologically meaningful and spatially coherent combinations of chromatin marks. Remember that we broke the genome up into 200bp blocks, so by spatially coherent we mean that if we have a genomic element that is longer than 200bps, we expect the combination of chromatin marks to be consistent on each 200bp bin in the region. We’ll call these biologically meaningful and spatially coherent combinations of chromatin marks **chromatin states** . In previous lectures, we’ve seen HMMs applied to genome annotation for genes and CpG islands. We would like to apply the same ideas to this situation, but in this case, we don’t know the hidden states a priori (e.g. CpG island region or not), we’d like to learn them _de novo_ . This model can capture both the functional ordering of different states (e.g from promoter to transcribed regions) and the spreading of certain chromatin domains across the genomes. To summarize, we want to learn an HMM where the hidden states of the HMM are chromatin states.

As we learned previously, even if we don’t know the emission probabilities and transition probabilities of an HMM, we can use the Baum-Welch training algorithm to learn the maximum likelihood values for those parameters. In our case, we have an added difficulty, we don’t even know how many chromatin states exist! In the following subsections, we’ll expand on how the data is modeled and how we can choose the number of states for the HMM.

#### **Emission of a Vector**

In HMMs from previous lectures, each state emitted either a single nucleotide or a single string of nucleotides at a time. In the HMM for this problem, each state emits a combination of epigenetic marks. Each combination can be represented as an _n_ -dimensional vector where _n_ is the number of chromatin marks being analyzed ( _n_ = 41 for our data). For example, assuming you have four possible epigenetic modifications: H3K4me3, H2BK5ac, Methyl-C, and Methyl-A, a sequence containing H3K4me3 and Methyl-C could be presented as the vector (1, 0, 1, 0). One could imagine many different probability distributions on binary _n_ -vectors and for simplicity, we assume that the marks are independent and modeled as Bernoulli random variables. So we are assuming the marks are independent given the hidden state of the HMM (note that this is not the same as assuming the marks are independent).

285

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

If there are _n_ input marks, each state _k_ has a vector ( _pk_ 1 _, .., pkn_ ) of probabilities of observing marks 1 to _n_ . Since the probability is modeled as a set of independent Bernoulli random variables, the probability of observing a set of marks given that we are in the hidden state _k_ equals the product of the probabilities of observing individual marks. For example if _n_ = 4, the observed marks at bin _j_ were (1 _,_ 0 _,_ 1 _,_ 0) and we were in state _k_ , then the likelihood of that data is _pk_ 1(1 _− pk_ 2) _pk_ 3(1 _− pk_ 4).

The learned emission probabilities for the data are shown in Figure 19.9.

#### **Transition Probabilities**

Recall that the transition probabilities represent the frequency of transitioning from one hidden state to another hidden state. In this case, our hidden states are chromatin states. The transition matrix for our data is shown in Figure 19.10. As seen from the figure, the matrix is sparse, indicating that only a few of the possible transitions actually occur. The transition matrix reveals the spatial relationships between neighboring states. Blocks of states in the matrix reveal sub-groups of states and from these higher level blocks, we can see transitions between these meta-states.

### **19.5.3 Choosing the Number of states to model**

As with most machine learning algorithms, increasing the complexity of the model (e.g. the number of hidden states) will allow it to better fit training data. However, the training data is only a limited sample of the true population. As we add more complexity, at some point we are fitting patterns in the training data that only exist due to limited sampling, so that the model will not generalize to the true population. This is called **over-fitting** training data; we should stop adding complexity to the model before it fits the noise in the training data.

**Bayesian Information Criterion (BIC)** is a common technique for optimizing the complexity of a model that balances increased fit to the data with complexity of the model. Using BIC, we can visualize the increasing power of the HMM as a function of the number of states. Generally, one will choose a value for _k_ (the number of states) such that the addition of more states has relatively little benefit in terms of predictive power gain. However, there is a tradeoff between model complexity and model interpretability that BIC cannot help with. The optimal model according to BIC is likely to have more states than an ideal model because we are willing to trade some predictive power for a model with fewer states that can be interpreted biologically. The human genome is so big and the chromatin marks so complex that statistically significant differences are easy to find, yet many of these differences are not biologically significant.

To solve this problem, we start with a model with more hidden states than we believe are necessary and prune hidden states as long as all states of interest in the larger model are adequately captured. The Baum-Welch algorithm (and EM in general) is sensitive to the initial conditions, so we try several random initializations in our learning. For each number of hidden states from 2 - 80, we generate three random initializations of the parameters and train the model using Baum-Welch. The best model according to BIC had 79 states and states were then iteratively removed from this set of 79 states.

As we mentioned earlier, Baum-Welch is sensitive to the initial parameters, so when we pruned states, we used a nested initialization rather than a randomized initialized for the pruned model. Specifically, states were greedily removed from the BIC-optimal 79 state model. The state to be removed was the state that such that all states from the 237 randomly initialized models were well captured. When removing a state, the emission probabilities would be removed and any state transitioning to the removed state would have that transition probability uniformly redistributed to the remaining states. This was used as the initialization to

286

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

the Baum-Welch training. The number of states for a model to analyze can then be selected by choosing the model trained from such nested initialization with the smallest number of states that sufficiently captures all states offering distinct biological interpretations. The resulting final model had 51 states.

We can also check model fit by looking at how the data violates model assumptions. Given the hidden state, the HMM assumes that each mark is independent. We can test how well the data conforms to this assumption by plotting the dependence between marks. This can reveal states that fit well and those that do not. In particular, repetitive states reveal a case where the model does not fit well. As we add more states, the model is better able to fit the data and hence fit the dependencies. By monitoring the fit on individual states that we are interested in, we can control the complexity of the model.

### **19.5.4 Results**

This multivariate HMM model resulted in a set of 51 biologically relevant chromatin states. However, there were no one-to-one relationship between each state and known classes of genomic elements (e.g. introns, exons, promoters, enhancers, etc) Instead, multiple chromatin states were often associated with one genomic element. Each chromatin state encoded specific biological relevant information about its associated genomic element. For instance, three different chromatin states were associated with transcription start site (TSS), but one was associated with TSS of highly expressed genes, while the other two were associated with TSS of medium and lowly expressed genes respectively. Such use of epigenetic markers greatly improved genome annotation, particularly when combined with evolutionary signals discussed in previous lectures. The 51 chromatin states can be divided in five large groups. The properties of these groups are described as follows and further illustrated in 19.11:

#### 1. **Promoter-Associated States (1-11):**

These chromatin states all had high enrichment for promoter regions. 40-89% of each state was within 2 kb of a RefSeq TSS. compared to 2.7% genome-wide. These states all had a high frequency of H3K4me3, significant enrichments for DNase I hypersensitive sites, CpG islands, evolutionarily conserved motifs and bound transcription factors. However, these states differed in the levels of associated marks such as H3K79me2/3, H4K20me1, acetylations etc. These states also differed in their functional enrichment based on Gene Ontology (GO). For instance, genes associated with T cell activation were enriched in state 8 while genes associated with embryonic development were enriched in state 4. Additionally, among these promoter states there were distinct positional enrichments. States 1-3 peaked both upstream and downstream of TSS; states 4-7 were concentrated right over TSS whereas states 8-11 peaked between 400 bp and 1200 bp downstream of TSS. This suggests that chromatin marks can recruit initiation factors and that the act of transcript can reinforce these marks. The distinct functional enrichment also suggests that the marks encode a history of activation.

#### 2. **Transcription-Associated States (12-28):**

This was the second largest group of chromatin states and included 17 transcription-associated states. There are 70-95% contained in annotated transcribed regions compared to 36% for rest of genome. These states were not predominantly associated with a single mark but rather they were defined by a combination of seven marks - H3K79me3, H3K79me2, H3K79me1, H3K27me1, H2BK5me1, H4K20me1 and H3K36me3. These states have subgroups associated with 5’-proximal or 5’-distal locations. Some of these states were associated with spliced exons, transcription start sites or end sites. Of interest, state 28, which was characterized by high frequency for H3K9me3, H4K20me3, and H3K36me3, showed a high enrichment in zinc-finger genes. This specific combination of marks was previously reported as marking regions of KAP1 binding, a zinc-finger specific co-repressor.

3. **Active Intergenic States (29-39):**

287

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

These states were associated with several classes of candidate enhancer regions and insulator regions and were associated with higher frequencies for H3K4me1, H2AZ, several acetylation marks but lower frequencies of methylation marks. Moreover, the chromatin marks could be used to distinguish active from less active enhancers. These regions were usually away from promoters and were outside of transcribed genes. Interestingly, several active intergenic states showed a significant enrichment for disease SNPs, or single nucleotide polymorphism in genome-wide association study (GWAS). For instance, a SNP (rs12619285) associated with plasma eosinophil count levels in inflammatory diseases was found to be located in the chromatin state 33, which was enriched for GWAS hits. In contrast, the surrounding region of this SNP was assigned to other chromatin states with no significant GWAS association. This can shed light on the possible functional significance of disease SNPs based on its distinct chromatin states.

4. **Large-Scale Repressed States (40-45):**

These states marked large-scale repressed and heterochromatic regions, representing 64% of the genome. H3K27me3 and H3K9me3 were two most frequently detected marks in this group.

5. **Repetitive States (46-51):**

These states showed strong and distinct enrichments for specific repetitive elements. For instance, state 46 had a strong sequence signature of low-complexity repeats such as (CA)n, (TG)n, and (CATG)n. States 48-51 showed seemingly high frequencies for many modification but also enrichment in reads from non-specific antibody control. The model was thus able to also capture artifacts resulting from lack of coverage for additional copies of repeat elements.

Since many of the chromatin states were described by multiple marks, the contribution of each mark to a state was quantified. Varying subsets of chromatin marks were tested to evaluate their potential for distinguishing between chromatin states. In general, increasing subsets of marks were found to converge to an accurate chromatin state when marks were chosen greedily.

The predictive power of chromatin states for discovery of functional elements consistently outperformed predictions based on individual marks. Such unsupervised model using epigenomic mark combination and spatial genomic information performed as well as many supervised models in genome annotation. It was shown that this HMM model based on chromatin states was able to reveal previously unannotated promoters and transcribed regions that were supported by independent experimental evidence. When chromatin marks were analyzed across the whole genome, some of the properties observed were satellite enriched states (47-51) enriched in centromere, the zinc-finger enriched state (state 28) enriched on chromosome 19 etc. Thus, such genome-wide annotation based on chromatin states can help better interpret biological data and potentially discover new classes of functional elements in the genome.

### **19.5.5 Multiple Cell Types**

All of the above work was done in a single cell type (CD4+ T cells). Since epigenomic markers vary over time, across cell types, and environmental circumstances, it is important to consider the dynamics of the chromatin states across different cell types and experimental conditions. The ENCODE project [3] in the Brad Bernstein Chromatin Group has measured 9 different chromatin marks in nine human cell lines. In this case, we want to a learn a single set of chromatin marks for all of the data. There are two approaches to this problem: concatenation and stacking. For concatenation, we could combine all of the 9 cell lines as if they were a single cell line. By concatenating the different cell lines, we ensure that a common set of state definitions are learned. We can do this here because the profiled marks were the same in each experiment. However, if we profiled different marks for different cell lines, we need to use another approach. Alternatively, we can align the 9 cell lines and treat all of the marks as a super-vector. This allows us to learn cell line specific activity states, for example there might be a state for ES-specific enhancers (in that

288

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

state there would be enhancer marks in ES, but no marks in other cell types). Unfortunately, this greatly increases the dimension of the vectors emitted by the HMM, which translates to an increase in the model complexity needed to adequately fit the data.

Suppose we had multiple cell types where we profiled different marks and we wanted to concatenate them. One approach is to learn independent models and then combine them. We could find corresponding states by matching emission vectors that are similar or by matching states that appear at the same places in the genome. A second approach is to treat the missing marks as missing data. The EM framework allows for unspecified data points, so as long as pairwise relationships are observed between marks in some cell type, we can use EM. Lastly, we can predict the missing chromatin marks based on the observed marks using maximum-likelihood as in the Viterbi algorithm. This is a less powerful approach if the ultimate goal is chromatin state learning because we are only looking at the most likely state instead of averaging over all possibilities as in the second approach.

In the case with 9 marks in 9 human cell lines, the cell lines were concatenated and a model with 15 states was learned [8]. Each cell type was analyzed for class enrichment. It was shown that some chromatin states, such as those encoding active promoters were highly stable across all cell types. Other states, such as those encoding strong enhancers, were highly enriched in a cell-type specific manner, suggesting their roles in tissue specific gene expression. Finally, it was shown that there was significant correlation between the epigenetic marks on enhancers and the epigenetic marks on the genes they regulate, even though these can be thousands of base pairs away. Such chromatin state model has proven useful in matching enhancers to their respective genes, a problem that has been largely unsolved in modern biology. Thus, chromatin states provide a means to study the dynamic nature of chromatin across many cell types. In particular, we can see the activity of a particular region of the genome based on the chromatin annotation. It also allows us to summarize important information contained in 2.4 billion reads in just 15 chromatin states.

A 2015 _Nature_ publication by the Epigenome Roadmap Project has shown produced an unparalleled reference for human epigenomics signatures across over a hundred different tissues [2]. In their analysis, they make use of several of the concepts we have discussed in-depth in this chapter, such as a 15-state or 18-state ChromHMM model to annotate the epigenome. Training over a 111 data sets allowed for greater robustness to the HMM models discussed earlier. The Roadmap project explored many interesting directions in their paper, and interested readers are strongly encouraged to read over this publication. Interesting conclusions include that H3K4-me1 associated states are the most tissue-specific chromatin marks, and that bivalent promoters and repressed states were also the most highly variable annotations across different tissue types. For enhancers, the Roadmap project found that a significant amount of disease-related SNPs are associated with annotated enhancer regions. Active exploration of this connection is ongoing in the Computational Biology Group at MIT.

## **19.6 Current Research Directions**

Several large-scale data production efforts such as ENCODE, modENCODE and Epigenome Roadmap projects are currently in progress and therefore there are several opportunities to computationally analyze this new data. Epigenomic data is also being used to study how behavior can alter your genome. There are studies being done that look at diet and exercise and their effects on disease susceptibility.

Another interesting area of research is the analysis of epigenetic changes in disease. Current research in the Computational Biology Group at MIT is looking at the link between chromatin states and Alzheimer’s disease. A selection of papers in epigenetics-disease linkage has been provided below.

289

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

## **19.7 Further Reading**

There are several interesting papers that are looking at chromatin states and epigenetics in general. Several urls are listed below to begin your exploration:

1. `http://www.nature.com/nmeth/journal/v8/n9/full/nmeth.1673.html`

2. `http://www.nature.com/nature/journal/v473/n7345/full/nature09906.html`

3. `http://www.nature.com/nbt/journal/v28/n8/abs/nbt.1662.html`

4. `http://www.nytimes.com/2012/09/09/opinion/sunday/why-fathers-really-matter.html?_r=1`

5. `http://www.nature.com/doifinder/10.1038/nature14248`

These are a few selected publications that deal with epigenetics and disease.

1. `http://www.nature.com/nature/journal/v429/n6990/full/nature02625.html`

2. `http://www.sciencedirect.com/science/article/pii/S2211124712003725`

3. `http://www.nature.com/nbt/journal/v28/n10/pdf/nbt.1685.pdf`

## **19.8 Tools and Techniques**

ChromHMM is the HMM described in the text. It is available free for download with instructions and examples at: `http://compbio.mit.edu/ChromHMM/` .

Segway is another method for analyzing multiple tracks of functional genomics data. It uses a dynamic Bayesian network (HMMs are a particular type of dynamic Bayesian network) which enables it to analyze the entire genome at 1-bp resolution. The downside is that it is much slower than ChromHMM. It is available free for download here: `http://noble.gs.washington.edu/proj/segway/` .

## **19.9 What Have We Learned?**

In this lecture, we learned how chromatin marks can be used to infer biologically relevant states. The analysis in [7] presents a sophisticated method to apply previously learned techniques such as HMMs to a complex problem. The lecture also introduced the powerful Burrows-Wheeler transform that has enabled efficient read mapping.

## **Bibliography**

- [1] Langmead B, Trapnell C, Pop M, and Salzberg S. Ultrafast, memory-efficient alignment of short DNA sequences to the human genome. _Genome Biology_ , 10(3), 2009.

290

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

- [2] Roadmap Epigenomics Consortium, Kundaje A, Meuleman W, et al. Integrative analysis of 111 reference human epigenomes. _Nature_ , 518(7539):317–330, 2015.

- [3] The ENCODE Project Consortium. An integrated encyclopedia of DNA elements in the human genome. _Nature_ , 489(7414):57–74, 2012.

- [4] Heard E and Martienssen RA. Transgenerational epigenetic inheritance: Myths and mechanisms. _Cell_ , 157(1):95–109, 2014.

- [5] Mardis ER. ChIP-seq: welcome to the new frontier. _Nature Methods_ , 4(8):614–614, 2007.

- [6] Herz H-M, Hu D, and Shilatifard A. Enhancer malfunction in cancer. _Molecular Cell_ , 53(6):859–866, 2014.

- [7] Ernst J and Kellis M. Discovery and characterization of chromatin states for systematic annotation of the human genome. _Nature Biotechnology_ , 28:817–825, 2010.

- [8] Ernst J, Kheradpour P, Mikkelsen TS, et al. Mapping and analysis of chromatin state dynamics in nine human cell types. _Nature_ , 473(7345):43–49, 2011.

- [9] Mousavi K, Zare H, Dell’orso S, Grontved L, et al. eRNAs promote transcription by establishing chromatin accessibility at defined genomic loci. _Molecular Cell_ , 51(5):606–17, 2013.

- [10] Qunhua Li, James B. Brown, Haiyan Huang, and Peter J. Bickel. Measuring reproducibility of highthroughput experiments. _The Annals of Applied Statistics_ , 5(3):1752–1779, 2011.

- [11] Li Y and Tollefsbol TO. DNA methylation detection: Bisulfite genomic sequencing analysis. _Methods Molecular Biology_ , 791:11–21, 2011.

291

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

Courtesy of National Institutes of Health. Image in the public domain.

Courtesy of Elsevier, Inc. Used with permission. Source: Herz, Hans-Martin, Deqing Hu, et al. "Enhancer Malfunction in Cancer." _Molecular Cell_ 53, no. 6 (2014): 859-66.

Figure 19.1: A. There is a wide diversity of modifications in the epigenome. Some regions of DNA are compactly wound around histones, making the DNA inaccessible and the genes inactive. Other regions have more accessible DNA and thus active genes. Epigenetic factors can bind to the tails of these histones to modify these properties. B. Histone modifications provide information about what types of proteins are bound to the DNA and what the function of the region is. In this example, The histone modifications allow for an enhancer region (potentially over 100 kilo bases away) to interact with the promoter region. [6]


Courtesy of Nature Publishing Group. Used with permission. Source: Mardis, Elaine R. "ChIP-seq: Welcome to the New Frontier." _Nature Methods_ 4, no. 8 (2007): 613.

Figure 19.2: The method of chromatin immunoprecipitation [5]. The steps in this figure correspond to the six steps of the procedure.

292

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 19.3: (Top) In the Burrows-Wheeler forward transformation rotations are generated and sorted. The last column of the sorted list (bolded) consists of the transformed string. (Bottom)In the Burrows-Wheeler reverse transformation the transformed string is sorted, and two columns are generated: one consisting of the original string and the other consisting of the sorted. These effectively form two columns from the rotations in the forward transformation. This process is repeated until the complete rotations are generated.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 19.4: To use input DNA as a control, one can run the ChIP experiment as normal while simultaneously running the same experiment (with same DNA) without an antibody. This generates a background signal for which we can correct.

293

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 19.5: In the figure above each column is a color-coded histogram that encodes the fraction of all mapped reads that have base score Q (y-axis) at each position(x-axis). A low average per base score implies greater probability of mismappings. We typically reject reads whose average score Q is less than 10.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 19.6: A sample signal track. Here, the red signal is derived from the number of reads that mapped to the genome at each position for a ChIP-seq experiment with the target H3K36me3. The signal gives a level of enrichment of the mark.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 19.7: Sample signal tracks for both the true experiment and the background (control). Regions are considered to have statistically significant enrichment when the true experiment signal values are well above the background signal values.

294

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Ernst, Jason, and Manolis Kellis. "Discovery and Characterization of Chromatin States for Systematic Annotation of the Human Genome." _Nature Biotechnology_ 28, no. 8 (2010): 817-25.

Figure 19.8: Example of the data and the annotation from the HMM model. The bottom section shows the raw number of reads mapped to the genome. The top section shows the annotation from the HMM model.

295

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites


© Macmillan Publishers Limited. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Ernst, Jason, and Manolis Kellis. "Discovery and Characterization of Chromatin States for Systematic Annotation of the Human Genome." _Nature Biotechnology_ 28, no. 8 (2010): 817-25.

Figure 19.9: Emission probabilities for the final model with 51 states. The cell corresponding to mark _i_ and state _k_ represents the probability that mark _i_ is observed in state _k_ .

296

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites


Figure 19.10: Transition probabilities for the final model with 51 states. The transition probability increases from green to red. Spatial relationships between neighboring chromatin states and distinct sub-groups of states are revealed by clustering the transition matrix. Notably, the matrix is sparse, so indicating that most are not possible.

297

6.047/6.878 Lecture 17: Epigenomics/Chromatin Sites


Figure 19.11: Chromatin state definition and functional interpretation. [7] a. Chromatin mark combinations associated with each state. Each row shows the specific combination of marks associated with each chromatin state and the frequencies between 0 and 1 with which they occur in color scale. These correspond to the emission probability parameters of the HMM learned across the genome during model training. b. Genomic and functional enrichments of chromatin states, including fold enrichment in different part of the genome (e.g. transcribed regions, TSS, RefSeq 5 end or 3end of the gene etc), in addition to fold enrichment for evolutionarily conserved elements, DNaseI hypersensitive sites, CpG islands, etc. All enrichments are based on the posterior probability assignments. c. Brief description of biological state function and interpretation (chr, chromatin; enh, enhancer).

298

CHAPTER

**TWENTY**

## NETWORKS I: INFERENCE, STRUCTURE, SPECTRAL METHODS

### **Figures**

|20.1 Interactions between biological networks.. . . . . . . . . . . . . . . . . . . . . . . . . . . .|299|
|---|---|
|20.2 Representation of different types of networks. . . . . . . . . . . . . . . . . . . . . . . . . .|300|
|20.3 A simple network on 3 nodes. The adjacency matrix of this graph is given in equation (21.1|).301|
|20.4 Wigner semicircle law<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|306|
|20.5 Structural inference using SVD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|307|
|20.6 Eigen-gene decomposition using PCA<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|308|
|20.7 Least squares solution of linear regression. Left: 2-D case, right: 3-D case . . . . . . . . .|309|
|20.8 PCA in a regression framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|310|
|20.9 PCA vs SPCA<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|311|
|20.10The iterative classification algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|311|
|20.11Prediction of gene function using associations . . . . . . . . . . . . . . . . . . . . . . . . .|312|
|20.12An example network containing a 4-clique . . . . . . . . . . . . . . . . . . . . . . . . . . .|312|
|20.13A network with 8 nodes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|317|
|20.14What other distance metrics are useful? . . . . . . . . . . . . . . . . . . . . . . . . . . . .|319|
|20.15Illustration of a random walk . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|320|
|20.16Illustration of a neural network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|321|
|20.17A flowchart of the DeepBind procedure (taken from the DeepBind paper). Five sequences<br>are being processed in parallel by the model. The model convolves the sequences (we can<br>think of the deepbind model as a filter scanning through the sequencs), recitifies and pools<br>them in order to produce a feature vector which is then passed through a deep neural<br>network. The output from the deepnet is compared against the desired output and the<br>error is back-propagated through the pipeline. . . . . . . . . . . . . . . . . . . . . . . . . .|323|
|20.18An illustration of the calibration, training and testing procedure used by the DeepBind<br>method (taken from the DeepBind paper).<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|323|
|20.19An illustration (taken from the Srivastava et al. paper) of a thinned net produced after the<br>dropout procedure was applied. The units that have been crossed out have been dropped.|324|
|20.20A plot (taken from the Srivastava et al. paper) illustrating that the classification error rate<br>decreases noticeably when the dropout procedure is applied. . . . . . . . . . . . . . . . . .|325|


299

6.047/6.878 Lecture 12B: Networks I

## **20.1 Introduction**

Molecular and cellular biology describe a hugely diverse system of interacting components that is capable of producing intricate and complex phenomena. Interactions within the proteome describe cellular metabolism, signaling cascades, and response to the environment. Networks are a valuable tool to assist in representing, understanding, and analyzing the complex interactions between biological components. Living systems can be viewed as a composition of multiple layers that each encode information about the system. Some important layers are:

1. Genome: Includes coding and non-coding DNA. Genes defined by coding DNA are used to build RNA, and Cis-regulatory elements regulate the expression of these genes.

2. Epigenome: Defined by chromatin configuration. The structure of chromatin is based on the way that histones organize DNA. DNA is divided into nucleosome and nucleosome-free regions, forming its final shape and influencing gene expression.<sup>1</sup>

3. Transcriptome RNAs (ex. mRNA, miRNA, ncRNA, piRNA) are transcribed from DNA. They have regulatory functions and manufacture proteins.

4. Proteome Composed of proteins. This includes transcription factors, signaling proteins, and metabolic enzymes.

Each layer consists of a network of interactions. For example, mRNAs and miRNAs interact to regulate the production of proteins. Layers can also interact with each other, forming a network between networks. For example, a long non-coding RNA called Xist produces epigenomic changes on the X-chromosome to achieve dosage compensation through X-inactivation.

### **20.1.1 Introducing Biological Networks**

Five example types of biological networks:

**Regulatory Network** – set of regulatory interactions in an organism.

   - Nodes represent regulators (ex. transcription factors) and associated targets.

   - Edges represent regulatory interaction, directed from the regulatory factor to its target. They are signed according to the positive or negative effect and weighted according to the strength of the reaction.

- **Metabolic Network** – connects metabolic processes. There is some flexibility in the representation, but an example is a graph displaying shared metabolic products between enzymes.

   - Nodes represent enzymes.

> 1More in the epigenetics lecture.

300

6.047/6.878 Lecture 12B: Networks I

Figure 20.1: Interactions between biological networks.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- Edges represent regulatory reactions, and are weighted according to the strength of the reaction. Edges are undirected.

**Signaling Network** – represents paths of biological signals.

- Nodes represent proteins called signaling receptors.

- Edges represent transmitted and received biological signals, directed from transmitter to receiver. Edges are directed and unweighted.

**Protein Network** – displays physical interactions between proteins.

   - Nodes represent individual proteins.

   - Edges represent physical interactions between pairs of proteins. These edges are undirected and unweighted.

- **Coexpression Network** – describes co-expression functions between genes. Quite general; represents functional rather than physical interaction networks, unlike the other types of nets. Powerful tool in computational analysis of biological data.

   - Nodes represent individual genes.

   - Edges represent co-expression relationships. These edges are undirected and unweighted.

Today, we will focus exclusively on regulatory networks. Regulatory networks control context-specific gene expression, and thus have a great deal of control over development. They are worth studying because they are prone to malfunction and are associated with disease.

### **20.1.2 Interactions Between Biological Networks**

Individual biological networks (that is, layers) can themselves be considered nodes in a larger network representing the entire biological system. We can, for example, have a signaling network sensing the environment governing the expression of transcription factors. In this example, the network would display that TFs govern the expression of proteins, proteins can play roles as enzymes in metabolic pathways, and so on.

The general paths of information exchange between these networks are shown in figure 21.1a.

301

6.047/6.878 Lecture 12B: Networks I

Figure 20.2: Representation of different types of networks.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

### **20.1.3 Network Representation**

In figure 20.2 we show a number of these networks and their visualizations as graphs. However, how did we decide on these particular networks to represent the underlying biological models? Given a large biological dataset, how can we understand dependencies between biological objects and what is the best way to model these dependencies? Below, we introduce several approaches to network representation. In practice, no model is perfect. Model choice should balance biological knowledge and computability for reasonably efficient analysis.

Networks are typically described as graphs. Graphs are composed of 1. nodes, which represent objects; and 2. edges, which represent connections or interactions between nodes. There are three main ways to think about biological networks as graphs.

**Probabilistic Networks** – also known as graphical models. They model a probability distribution between nodes.

   - Modeling joint probability distribution of variables using graphs.

   - Some examples are Bayesian Networks (directed), Markov Random Fields (Undirected). More on Bayesian networks in the later chapters.

- **Physical Networks** – In this scheme we usually think of nodes as physically interacting with each other and the edges capture that interaction.

   - Edges represent physical interaction among nodes.

   - Example: physical regulatory networks.

**Relevance Network** – Model the correlation between nodes.

- Edge weights represent node similarities.

- Example: functional regulatory networks.

#### **Networks as Graphs**

Computer scientists consider subtypes of graphs, each with different properties for their edges and nodes.

302

6.047/6.878 Lecture 12B: Networks I

Figure 20.3: A simple network on 3 nodes. The adjacency matrix of this graph is given in equation (21.1).


<!-- Start of picture text -->
1 2<br>3<br><!-- End of picture text -->

- **Weighted graph** : Edges have an associated weight. Weights are generally positive. When all the weights are 1, then we call it an **unweighted graph** .

- **Directed graphs** : Edges possess directionality. For example _A → B_ is not the same as _A ← B_ . When the edges do not have direction, we call it an **undirected graph** .

- **Multigraphs (pseudographs)** : When we allow more than one edge to go between two nodes (more than two if it’s directed) then we call it a multigraph. This can be useful for modeling multiple interactions between two nodes each with different weights for example.

- **Simple graph** : All edges are undirected and unweighted. Multiple edges between nodes and self-edges are forbidden.

#### **Matrix Representation of Graphs**

**Adjacency matrix** One way to represent a network is using the so-called _adjacency matrix_ . The adjacency matrix of a network with _n_ nodes is an _n × n_ matrix _A_ where _Aij_ is equal to one if there is an edge between nodes _i_ and _j_ , and 0 otherwise. For example, the adjacency matrix of the graph represented in figure 21.6b is given by:


If the network is weighted (i.e., if the edges of the network each have an associated weight), the definition of the adjacency matrix is modified so that _Aij_ holds the weight of the edge between _i_ and _j_ if the edge exists, and zero otherwise.

Another convenience that comes with the adjacency matrix representation is that when we have a binary matrix (unweighted graph) then the sum of row _i_ gives us the **degree** of node _i_ . In an undirected graph, the degree of a node is the number of edges it has. Since every entry in the row tells us whether node _i_ is connected to another node, by summing all these values we know how many nodes is node _i_ connected to, thus we get the degree.

## **20.2 Network Centrality Measures**

We discussed in the previous chapter how we can take a biological network and model it mathematically. Now as we visualize these graphs and try to understand them we need some measure for the importance of a node/edge to the structural characteristics of the system. There are many ways to measure the importance (what we refer to as centrality) of a node. In this chapter we will explore these ideas and investigate their significance.

303

6.047/6.878 Lecture 12B: Networks I


<!-- Start of picture text -->
3. Linear Algebra Review<br>–<br>Eigenvector and singular vector decomposition<br>–<br>Low rank approximations, Wigner semicircle law<br>4. Sparse Principle Component Analysis<br>– Lasso and Elastic lasso<br><!-- End of picture text -->

### **20.2.1 Degree Centrality**

The first idea about centrality is measure importance by the degree of a node. This is probably one of the most intuitive centrality measures as it’s very easy to visualize and reason about. The more edges you have connected to you, the more important to the network you are.

Let’s explore a simple example and see how the go about finding these centralities. We have the following graph


<!-- Start of picture text -->
A<br>B C<br>D E<br><!-- End of picture text -->

And our goal is to find the degree centrality of every node in the graph. To proceed, we first write out the adjacency matrix for this graph. The order for the edges is A, B, C, D, E


Previously we discussed how to find the degree for a node given an adjacency matrix. We sum along every row of the adjacency matrix.


Now _D_ is a vector with the degree of every node. This vector gives us a relative centrality measures for nodes in this network. We can observe that node _B_ has the highest degree centrality.

Although this metric gives us a lot of insight, it has its limitations. Imagine a situation where there is one node that connects two parts of the network together. The node will have a degree of 2, but it is much more important than that.

304

6.047/6.878 Lecture 12B: Networks I

### **20.2.2 Betweenness Centrality**

Betweenness centrality gives us another way to think about importance in a network. It measures the number of shortest paths in the graph that pass through the node divided by the total number of shortest paths. In other words, this metric computes all the shortest paths between every pair of nodes and sees what is the percentage of that passes through node _k_ . That percentage gives us the centrality for node _k_ .

- Nodes with high betweenness centrality control information flow in a network.

- Edge betweenness is defined in a similar fashion.

### **20.2.3 Closeness Centrality**

In order to properly define closeness we need to define the term **farness** . Distance between two nodes is the shortest paths between them. The farness of a node is the sum of distances between that node and all other nodes. And the closeness of a node is the inverse of its farness. In other words, it is the normalized inverse of the sum of topological distances in the graph.

The most central node is the node that propagates information the fastest through the network.

The description of closeness centrality makes it similar to the degree centrality. Is the highest degree centrality always the highest closeness centrality? No. Think of the example where one node connects two components, that node has a low degree centrality but a high closeness centrality.

### **20.2.4 Eigenvector Centrality**

The eigenvector centrality extends the concept of a degree. The best to think of it is the average of the centralities of it’s network neighbors. The vector of centralities can be written as:


where _A_ is the adjacency matrix. The solution to the above equation is going to be the **eigenvector** corresponding to the **principle component** (largest eigenvalue).

The following section includes a review of linear algebra concepts including eigenvalue and eigenvectors.

## **20.3 Linear Algebra Review**

Our goal of this section is to remind you of some concepts you learned in your linear algebra class. This is not meant to be a detailed walk through. If you would want to learn more about any of the following concepts, I recommend picking up a linear algebra book and reading from that section. But this will serve as a good reminder and noting concepts that are important for us in this chapter.

305

6.047/6.878 Lecture 12B: Networks I

### **20.3.1 Eigenvectors**

Given a square matrix _A_ , ( _m × m_ ), the eigenvector _v_ is the solution to the following equation.


In other words, if we multiply the matrix by that vector, we only change our position parallel the vector (we get back a scaled version of the vector _v_ ).

And _λ_ (how much the vector _v_ is scaled) is called the **eigenvalue** .

So how many eigenvalues are there at most? Let’s take the first steps to solving this equation.


that has non-zero solutions when _|A − λI|_ = 0. That is an _m_ -th order equation in _λ_ which can have at most _m_ distinct solutions. Remember that those solutions can be complex, even though _A_ is real.

### **20.3.2 Vector decomposition**

Since the eigenvectors form the set of all bases they fully represent the column space. Given that, we can decompose any arbitrary vector _x_ to a combination of eigenvectors.


Thus when we multiply a vector with a matrix _A_ , we can rewrite it in terms of the eigenvectors.


So the action of _A_ on _x_ is determined by the eigenvalues of and eigenvectors. And we can observe that small eigenvalues have a small effect on the multiplication.

306

6.047/6.878 Lecture 12B: Networks I

## **_Did You Know?_**

- For symmetric matrices, eigenvectors for distinct eigenvalues are orthogonal.

- All eigenvalues of a real symmetric matrix are real.

- All eigenvalues of a positive semidefinite matrix are non-negative.

### **20.3.3 Diagonal Decomposition**

Also known as Eigen Decomposition. Let _S_ be a square _m × m_ matrix with _m_ linearly independent eigenvectors (a non-defective matrix).

Then, there exist a decomposition (matrix digitalization theorem)


Where the columns of _U_ are the eigenvectors of _S_ . And Λ is a diagonal matrix with eigenvalues in its diagonal.

### **20.3.4 Singular Value Decomposition**

Oftentimes, singular value decomposition (SVD) is used for the more general case of factorizing an _m × n_ non-square matrix:


where **U** is a _m×m_ matrix representing orthogonal eigenvectors of **AA**<sup>_T_</sup> , **V** is a _n×n_ matrix representing orthogonal eigenvectors of **A**<sup>_T_</sup> **A** and **Σ** is a _m × n_ matrix representing square roots of the eigenvalues of **A**<sup>_T_</sup> **A** (called singular values of **A** ):


The SVD of any given matrix can be calculated with a single command in Matlab and we will not cover the technical details of computing it. Note that the resulting “diagonal” matrix **Σ** may not be full-rank, i.e. it may have zero diagonals, and the maximum number of non-zero singular values is min( _m, n_ ).

For example, let


307

6.047/6.878 Lecture 12B: Networks I

thus _m_ = 3 _, n_ = 2. Its SVD is


Typically, the singular values are arranged in decreasing order.

SVD is widely utilized in statistical, numerical analysis and image processing techniques. A typical application of SVD is optimal low-rank approximation of a matrix. For example if we have a large matrix of data ,e.g. 1000 by 500, and we would like to approximate it with a lower-rank matrix without much loss of information, formulated as the following optimization problem:


where the subscript _F_ denotes Frobenius norm _||_ **A** _||F_ = ~~�~~ <u>�</u> _i_ <u>�</u> _j_<sup>_|aij|_</sup> 2<sup>.Usually</sup><sup>_k_ismuchsmallerthan</sup> _r_ . The solution to this problem is the SVD of **X** , **UΣV**<sup>_T_</sup> , with the smallest _r − k_ singular values in **Σ** set to zero:


Such an approximation can be shown to have an error of _||_ **A** _−_ **A** _k||F_ = _σk_ +1. This is also known as the Eckart-Young theorem.

A common application of SVD to network analysis is using the distribution of singular values of the adjacency matrix to assess whether our network looks like a random matrix. Because the distribution of the singular values (Wigner semicircle law) and that of the largest eigenvalue of a matrix (Tracy-Widom distribution) have been theoretically derived, it is possible to derive the distribution of eigenvalues (singular values in SVD) of an observed network (matrix), and calculate a _p_ -value for each of the eigenvalues. Then we need only look at the significant eigenvalues (singular values) and their corresponding eigenvectors (singular vectors) to examine significant structures in the network. The following figure shows the distribution of singular values of a random Gaussian unitary ensemble (GUE, see this Wikipedia link for definition and properties `http://en.wikipedia.org/wiki/Random_matrix` ) matrix, which form a semi-circle according to Wigner semicircle law (Figure 20.4).

An example of using SVD to infer structural patterns in a matrix or network is shown in Figure 20.5. The top-left panel shows a structure (red) added to a random matrix (blue background in the heatmap), spanning the first row and first three columns. SVD detects this by the identification of a large singular value (circled in red on singular value distribution) and corresponding large row loadings ( _U_ 1) as well as three large column loadings ( _V_ 1). As more structures are added to the network (top-right and bottom panels), they can be discovered using SVD by looking at the next largest singular values and corresponding row/column loadings, etc..

308

6.047/6.878 Lecture 12B: Networks I


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 20.4: Wigner semicircle law

## **20.4 Sparse Principal Component Analysis**

### **20.4.1 Limitations of Principal Component Analysis**

When analyzing microarray-based gene expression data, we are often dealing with data matrices of dimensions _m × n_ where _m_ is the number of arrays and _n_ is the number of genes. Usually _n_ is in the order of thousands and _m_ is in the order of hundreds. We would like to identify the most important features (genes) that best explain the expression variation, or patterns, in the dataset. This can be done by performing PCA on the expression matrix:


This is in essence an SVD of the expression matrix **E** that rotates and scales the feature space so that expression vectors of each gene in the new orthogonal coordinate system are as uncorrelated as possible, where **E** is the _m_ by _n_ expression matrix, **U** is the _m_ by _m_ matrix of left singular vectors (i.e. principal components), or “eigen-genes”, **V** is the _n_ by _n_ matrix of right singular vectors, or “eigen-arrays”, and **D** is a diagonal matrix of singular values, or “eigen-expressions” of eigen-genes. This is illustrated in Figure 20.6.

In PCA, each principal component (eigen-gene, a column of **U** ) is a linear combination of _n_ variables (genes), which corresponds to a loading vector (column of **V** ) where the loadings are coefficients corresponding to variables in the linear combination.

However, a straightforward application of PCA to expression matrices or any large data matrices can be problematic because the principal components (eigen-genes) are linear combinations of _all n_ variables (genes), which is difficult to interpret in terms of functional relevance. In practice we would like to use a combination of as few genes as possible to explain expression patterns, which can be achieved by a sparse version of PCA.

309

6.047/6.878 Lecture 12B: Networks I


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 20.5: Structural inference using SVD

### **20.4.2 Sparse PCA**

Sparse PCA (SPCA) modifies PCA to constrain the principal components (PCs) to have sparse loadings, thus reducing the number of explicitly used variables (genes in microarray data, etc.) and facilitating interpretation. This is done by formulating PCA as a linear regression-type optimization problem and imposing sparsity constraints.

A linear regression problem takes a set of input variables **x** = (1 _, x_ 1 _, ..., xp_ ) and response variables **y** = **x** _β_ + _ϵ_ where _β_ is a row vector of regression coefficients ( _β_ 0 _, β_ 1 _, ..., βp_ )<sup>_T_</sup> and _ϵ_ is the error. The regression model for _N_ observations can be written in matrix form:


The goal of the linear regression problem is to estimate the coefficients _β_ . There are several ways to do this, and the most commonly used methods include the least squares method, the Lasso method and the elastic net method.

**Least Squares** method minimizes the residual sum of squared error:

310

6.047/6.878 Lecture 12B: Networks I


Figure 20.6: Eigen-gene decomposition using PCA


where _RSS_ ( _β ≡_<sup>�</sup><sup>_N_</sup> _i_ =1<sup>(</sup><sup>_yi−Xiβ_)2(</sup><sup>_Xi_isthe</sup><sup>_i_thinstanceofinputvariables</sup><sup>**x**).Thisisillustratedin</sup> Figure 20.7 for the 2-D and 3-D cases, where either a regression line or hyperplane is produced.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 20.7: Least squares solution of linear regression. Left: 2-D case, right: 3-D case

**Lasso** method not only minimizes the sum of residual errors but at the same time minimizes a Lasso penalty, which is proportional to the L-1 norm of the coefficient vector _β_ :


where _L_ 1( _β_ ) = _λ_<sup>�</sup> _pj_ =1<sup>_|βj|,λ≥_0.TheidealpenaltyforSparsePCAisthe</sup><sup>_L_0normwhichpenalizes</sup> each non-zero element by 1, while zero elements are penalized by 0. However, the _L_ 0 penalty function is non-convex and the best solution for exploring the exponential space (number of possible combinations of non-zero elements) is NP-hard. The _L_ 1 norm provides a convex approximation to the _L_ 0 norm. The Lasso regression model in essence continuously shrinks the coefficients toward zero as much as possible, producing a sparse model. It automatically selects for the smallest set of variables that explain variations in the data. However, the Lasso method suffers from the problem that if there exists a group of highly correlated variables it tends to select only one of these variables. In addition, Lasso selects at most _N_ variables, i.e. the number of selected variables is limited by sample size.

**Elastic Net** method removes the group selection limitation of the Lasso method by adding a ridge constraint:

311

6.047/6.878 Lecture 12B: Networks I


where _L_ 2( _β_ ) = _λ_ 2 � _pj_ =1<sup>_|βj|_2</sup><sup>_,λ_2</sup><sup>_≥_0.Intheelasticnetsolution,agroupofhighlycorrelatedvariables</sup> will be selected once one of them is included.

All of the added penalty terms above arise from the theoretical framework of regularization. We skip the mathematics behind the technique and point to an online concise explanation and tutorial of regularization at `http://scikit-learn.org/stable/modules/linear_model.html` .

PCA can be reconstructed in a regression framework by viewing each PC as a linear combination of the _p_ variables. Its loadings can thus be recovered by regressing PC on the _p_ variables (Figure 20.8). Let **X** = **UDV**<sup>_T_</sup> . _∀i_ , denote _Yi_ = _UiDii_ , then _Yi_ is the _i_ th principal component of **X** . We state without proving the following theorem that confirms the correctness of reconstruction:

**Theorem 20.4.1.** _∀λ >_ 0 _, suppose β_ ˆ _ridge is the ridge estimate given by_


_and let_ **v** ˆ = _|ββ_ ˆ<sup>ˆ</sup> _ridridgege|_<sup>_,then_</sup><sup>**v**ˆ =</sup><sup>_Vi._</sup>


Figure 20.8: PCA in a regression framework

Note that the ridge penalty does not penalize the coefficients but rather ensure the reconstruction of the PCs. Such a regression problem cannot serve as an alternative to na¨ıve PCA as it uses exactly its results **U** in the model, but it can be modified by adding the Lasso penalty to the regression problem to penalize for the absolute values of coefficients:


where **X** = **UDV**<sup>_T_</sup> and _∀i_ , _Yi_ = _UiDii_ is the _i_ th principal component of **X** . The resulting _β_ when scaled by its norm are exactly what SPCA aims at - sparse loadings:


312

6.047/6.878 Lecture 12B: Networks I

with _XVi ≈ Yi_ being the _i_ th sparse principal component.

Here we give a simulated example dataset and compare the recovery of hidden factors using PCA and SPCA. We have 10 variables for which to generate data points: **X** = ( _X_ 1 _, ..., X_ 10), and a model of 3 hidden factors _V_ 1, _V_ 2 and _V_ 3 is used to generate the data:


From these data we expect two significant structures to arise from a sparse PCA model, each governed by hidden factors _V_ 1 and _V_ 2 respectively ( _V_ 3 is merely a linear mixture of the two). Indeed, as shown in Figure 20.9, by limiting the number of variables used, SPCA correctly recovers the PCs explaining the effects of _V_ 1 and _V_ 2 while PCA does not distinguish well among the mixture of hidden factors.


Figure 20.9: PCA vs SPCA

## **20.5 Network Communities and Modules**

Is it possible to use networks to infer the labels of unlabeled nodes, or data? Assuming that some of the data is labeled in a network, we can use the idea that networks capture relational information through a “Guilt by association” methodology. Simply put, we can look at the labeled “friends” of a node in a network to infer the label of a new node. Even though the “Guilt By Association” way of reasoning is a logical fallacy and insufficient in legal court settings, it is often helpful to predict labels (e.g. gene functions) for nodes in a network by looking at the labels of a node’s neighbors. Essentially, a node connected to many nodes with the same label is likely to have that label too. In terms of biological networks where nodes represent genes, and edges represent interactions (regulation, co-expression, protein-protein interactions etc., see Figure 20.11), it is possible to predict function of an unannotated gene based on the functions of the genes that the query gene is connected to. It is easy to see that we can immediately apply this into an iterative algorithm, where we start with a set of labeled nodes and unlabeled nodes, and we iteratively update relational attributes

313

6.047/6.878 Lecture 12B: Networks I

and then re-infer labels of nodes. We iterate until all nodes are labeled. This is known as the iterative classification algorithm.


Figure 20.10: The iterative classification algorithm

“Guilt By Association” implies a notion of association. The definition of association we implicitly considered above is a straightforward definition where we consider all the nodes directly connected to a particular node. Can we give a better definition of association? Considering this question, we arrive naturally at the idea of communities, or modules, in graphs. The term community attempts to capture the notion of a region in a graph with densely connected nodes, linked to other regions in the graph with a sparse number of edges. Graphs like these, with densely connected subgraphs, are often termed as modular. Note that there is no consensus upon the exact definition of communities. For practical use, the definition of communities should be biologically motivated and informed by prior knowledge about the system being modeled. In biology, regulatory networks are often modular, with genes in each densely connected subgraph sharing similar functions and co-regulation. However, broad categories of communities have been developed based on different topological features. They can be roughly divided into 4 categories: node-centric, group-centric, network-centric and hierarchy-centric communities. Here we examine a commonly used criterion for each of the first three types and briefly walk through some well-known algorithms that detect these communities.


Figure 20.11: Prediction of gene function using associations

### **20.5.1 Node-Centric Communities**

Node-centric community criteria usually require that _each node_ in a group satisfies certain properties. A frequently used node-centric community definition is the **clique** , which is a maximum complete subgraph in which all nodes are adjacent to each other. Figure 20.12 shows an example of a clique (nodes 5,6 7 and 8) in a network.

Exactly finding the maximum clique in a network is NP-hard, thus it is very computationally expensive to implement a straightforward algorithm for clique-finding. Heuristics are often used to limit time complexity by trading a certain fraction of accuracy. A commonly used heuristic for maximum clique finding is based on the observation that in a clique of size _k_ , each node maintains degree of at least _k −_ 1. We therefore can apply the following pruning procedure:

• Sample a sub-network from the given network and find a clique in the subnetwork using an efficient

314

6.047/6.878 Lecture 12B: Networks I


Figure 20.12: An example network containing a 4-clique

(e.g. greedy) approach

- Suppose the identified clique has size _k_ , to find a larger clique, all nodes with degree less than or equal to _k −_ 1 are removed

- Repeat until network is small enough

In practice many nodes will be pruned as social media networks and many forms of biological networks follow a power law distribution of node degrees that results in large numbers of nodes with low degrees.

Take the network in Figure 20.12 for an example of such a clique finding procedure. Suppose we sampled a subnetwork with nodes numbered 1 to 9 and found a clique _{_ 1 _,_ 2 _,_ 3 _}_ of size 3. In order to find a clique with size larger than 3, we iteratively remove al nodes with degree _≤_ 2, i.e. nodes _{_ 2 _,_ 9 _}_ , _{_ 1 _,_ 3 _}_ and 4 will be sequentially removed. This leaves us with the 4-clique _{_ 5 _,_ 6 _,_ 7 _,_ 8 _}_ .

### **20.5.2 Group-Centric Communities**

Group-centric community criteria consider connections _within a group_ as a whole, and the group has to satisfy certain properties without zooming into node-level, e.g. the group edge density must exceed a given threshold. We call a subgraph _Gs_ ( _Vs, Es_ ) a _γ − dense_ **quasi-clique** if


where the denominator is the maximum number of edges in the network. With such a definition, a similar strategy to the heuristic we discussed for finding maximum cliques can be adopted:

- Sample a subnetwork and find a maximal _γ − dense_ quasi-clique (e.g. of size _|Vs|_

- 2 _<u>|Es</u>_<sup>_<u>|</u>_</sup>

- Remove nodes with degree less than the average degree ( _< |Vs|γ ≤ |Vs|−_ 1<sup>)</sup>

- Repeat until network is small enough

315

6.047/6.878 Lecture 12B: Networks I

### **20.5.3 Network-Centric Communities**

Network-centric definitions seek to partition _the entire network_ into several disjoint sets. Several approaches exist for such a goal, as listed below:

- Markov clustering algorithm [6]: The Markov Clustering Algorithm (MCL) works by doing a random walk in the graph and looking at the steady-state distribution of this walk. This steady-state distribution allows to cluster the graph into densely connected subgraphs.

- Girvan-Newman algorithm [2]: The Girvan-Newman algorithm uses the number of shortest paths going through a node to compute the _essentiality_ of an edge which can then be used to cluster the network.

- Spectral partitioning algorithm

In this section we will look in detail at the spectral partitioning algorithm. We refer the reader to the references [2, 6] for a description of the other algorithms.

The spectral partitioning algorithm relies on a certain way of representing a network using a matrix. Before presenting the algorithm we introduce an important description of a network - its Laplacian matrix.

**Laplacian matrix** For the clustering algorithm that we will present later in this section, we will need to count the number of edges between the two different groups in a partitioning of the network. For example, in Figure 21.6a, the number of edges between the two groups is 1. The _Laplacian matrix_ which we will introduce now comes in handy to represent this quantity algebraically. The Laplacian matrix _L_ of a network on _n_ nodes is a _n × n_ matrix _L_ that is very similar to the adjacency matrix _A_ except for sign changes and for the diagonal elements. Whereas the diagonal elements of the adjacency matrix are always equal to zero (since we do not have self-loops), the diagonal elements of the Laplacian matrix hold the _degree_ of each node (where the degree of a node is defined as the number of edges incident to it). Also the off-diagonal elements of the Laplacian matrix are set to be _−_ 1 in the presence of an edge, and zero otherwise. In other words, we have:


For example the Laplacian matrix of the graph of figure 21.6b is given by (we emphasized the diagonal elements in bold):


**Some properties of the Laplacian matrix** The Laplacian matrix of any network enjoys some nice properties that will be important later when we look at the clustering algorithm. We briefly review these here.

The Laplacian matrix _L_ is always **symmetric** , i.e., _Li,j_ = _Lj,i_ for any _i, j_ . An important consequence of this observation is that all the eigenvalues of _L_ are real (i.e., they have no complex imaginary part). In fact one can even show that the eigenvalues of _L_ are all nonnegative<sup>2</sup> The final property that we mention

> 2One way of seeing this is to notice that _L_ is diagonally dominant and the diagonal elements are strictly positive (for more details the reader can look up “diagonally dominant” and “Gershgorin circle theorem” on the Internet).

316

6.047/6.878 Lecture 12B: Networks I

about _L_ is that all the rows and columns of _L_ sum to zero (this is easy to verify using the definition of _L_ ). This means that the smallest eigenvalue of _L_ is always equal to zero, and the corresponding eigenvector is _s_ = (1 _,_ 1 _, . . . ,_ 1).

**Counting the number of edges between groups using the Laplacian matrix** Using the Laplacian matrix we can now easily count the number of edges that separate two disjoint parts of the graph using simple matrix operations. Indeed, assume that we partitioned our graph into two groups, and that we define a vector _s_ of size _n_ which tells us which group each node _i_ belongs to:


Then one can easily show that the total number of edges between group 1 and group 2 is given by the quantity 4<sup><u>1</u></sup> _s_<sup>_T_</sup> _Ls_ where _L_ is the Laplacian of the network.

To see why this is case, let us first compute the matrix-vector product _Ls_ . In particular let us fix a node _i_ say in group 1 (i.e., _si_ = +1) and let us look at the _i_ ’th component of the matrix-vector product _Ls_ . By definition of the matrix-vector product we have:


We can decompose this sum into three summands as follows:


Using the definition of the Laplacian matrix we easily see that the first term corresponds to the degree of _i_ , i.e., the number of edges incident to _i_ ; the second term is equal to the negative of the number of edges connecting _i_ to some other node in group 1, and the third term is equal to the number of edges connecting _i_ to some node ingroup 2. Hence we have:


Now since any edge from _i_ must either go to group 1 or to group 2 we have


Thus combining the two equations above we get:


Now to get the total number of edges between group 1 and group 2, we simply sum the quantity above over all nodes _i_ in group 1:


We can also look at nodes in group 2 to compute the same quantity and we have:


317

6.047/6.878 Lecture 12B: Networks I

Now averaging the two equations above we get the desired result:


where _s_<sup>_T_</sup> is the row vector obtained by transposing the column vector _s_ .

**The spectral clustering algorithm** We will now see how the linear algebra view of networks given in the previous section can be used to produce a “good” partitioning of the graph. In any good partitioning of a graph the number of edges between the two groups must be relatively small compared to the number of edges within each group. Thus one way of addressing the problem is to look for a partition so that the number of edges between the two groups is minimal. Using the tools introduced in the previous section, this problem is thus equivalent to finding a vector _s ∈{−_ 1 _,_ +1 _}_<sup>_n_</sup> taking only values _−_ 1 or +1 such that<sup><u>1</u></sup> 4 _s_<sup>_T_</sup> _Ls_ is minimal, where _L_ is the Laplacian matrix of the graph. In other words, we want to solve the minimization problem:


If _s_<sup>_∗_</sup> is the optimal solution, then the optimal partioning is to assign node _i_ to group 1 if _si_ = +1 or else to group 2.

This formulation seems to make sense but there is a small glitch unfortunately: the solution to this problem will always end up being _s_ = (+1 _, . . . ,_ +1) which corresponds to putting all the nodes of the network in group 1, and no node in group 2! The number of edges between group 1 and group 2 is then simply zero and is indeed minimal!

To obtain a meaningful partition we thus have to consider partitions of the graph that are nontrivial. Recall that the Laplacian matrix _L_ is always symmetric, and thus it admits an eigendecomposition:


where Σ is a diagonal matrix holding the nonnegative eigenvalues _λ_ 1 _, . . . , λn_ of _L_ and _U_ is the matrix of eigenvectors and it satisfies _U_<sup>_T_</sup> = _U_<sup>_−_1</sup> .

The cost of a partitioning _s ∈{−_ 1 _,_ +1 _}_<sup>_n_</sup> is given by


where _α_ = _U_<sup>_T_</sup> _s_ give the decomposition of _s_ as a linear combination of the eigenvectors of _L_ : _s_ =<sup>�</sup> _ni_ =1<sup>_αiui_.</sup>

Recall also that 0 = _λ_ 1 _≤ λ_ 2 _≤· · · ≤ λn_ . Thus one way to make the quantity above as small as possible (without picking the trivial partitioning) is to concentrate all the weight on _λ_ 2 which is the smallest nonzero eigenvalue of _L_ . To achieve this we simply pick _s_ so that _α_ 2 = 1 and _αk_ = 0 for all _k̸_ = 2. In other words, this corresponds to taking _s_ to be equal to _u_ 2 the second eigenvector of _L_ . Since in general the eigenvector _u_ 2 is not integer-valued (i.e., the components of _u_ 2 can be different than _−_ 1 or +1), we have to convert first

318

6.047/6.878 Lecture 12B: Networks I


Figure 20.13: A network with 8 nodes.

the vector _u_ 2 into a vector of +1’s or _−_ 1’s. A simple way of doing this is just to look at the signs of the components of _u_ 2 instead of the values themselves. Our partition is thus given by:


To recap, the spectral clustering algorithm works as follows:

#### **Spectral partitioning algorithm**

- Input: a network

- Output: a partitioning of the network where each node is assigned either to group 1 or group 2 so that the number of edges between the two groups is small

1. Compute the Laplacian matrix _L_ of the graph given by:


2. Compute the eigenvector _u_ 2 for the second smallest eigenvalue of _L_ .

3. Output the following partition: Assign node _i_ to group 1 if ( _u_ 2) _i ≥_ 0, otherwise assign node _i_ to group 2.

We next give an example where we apply the spectral clustering algorithm to a network with 8 nodes.

**Example** We illustrate here the partitioning algorithm described above on a simple network of 8 nodes given in figure 21.7. The adjacency matrix and the Laplacian matrix of this graph are given below:


319

6.047/6.878 Lecture 12B: Networks I

Using the `eig` command of Matlab we can compute the eigendecomposition _L_ = _U_ Σ _U_<sup>_T_</sup> of the Laplacian matrix and we obtain:


We have highlighted in bold the second smallest eigenvalue of _L_ and the associated eigenvector. To cluster the network we look at the sign of the components of this eigenvector. We see that the first 4 components are negative, and the last 4 components are positive. We will thus cluster the nodes 1 to 4 together in the same group, and nodes 5 to 8 in another group. This looks like a good clustering and in fact this is the “natural” clustering that one considers at first sight of the graph.

## **_Did You Know?_**

The mathematical problem that we formulated as a motivation for the spectral clustering algorithm is to find a partition of the graph into two groups with a minimimal number of edges between the two groups. The spectral partitioning algorithm we presented does not always give an optimal solution to this problem but it usually works well in practice.

Actually it turns out that the problem as we formulated it can be solved exactly using an efficient algorithm. The problem is sometimes called the **minimum cut** problem since we are looking to cut a minimum number of edges from the graph to make it disconnected (the edges we cut are those between group 1 and group 2). The minimum cut problem can be solved in polynomial time in general, and we refer the reader to the Wikipedia entry on _minimum cut_ [9] for more information. The problem however with minimum cut partitions it that they usually lead to partitions of the graph that are not balanced (e.g., one group has only 1 node, and the remaining nodes are all in the other group). In general one would like to impose additional constraints on the clusters (e.g., lower or upper bounds on the size of clusters, etc.) to obtain more realistic clusters. With such constraints, the problem becomes harder, and we refer the reader to the Wikipedia entry on _Graph partitioning_ [8] for more details.

320

6.047/6.878 Lecture 12B: Networks I

## **_FAQ_**

- **Q:** How to partition the graph into more than two groups?

- **A:** In this section we only looked at the problem of partitioning the graph into two clusters. What if we want to cluster the graph into more than two clusters? There are several possible extensions of the algorithm presented here to handle _k_ clusters instead of just two. The main idea is to look at the _k_ eigenvectors for the _k_ smallest nonzero eigenvalues of the Laplacian, and then to apply the _k_ -means clustering algorithm appropriately. We refer the reader to the tutorial [7] for more information.

## **20.6 Network Diffusion Kernels**

Earlier, we defined a distance metric between two nodes as the weighted shortest path. This simple distance metric is sufficient for many purposes, but it notably does not use any information about the overall graph structure. Often times, defining distance based on the number of possible paths between two nodes, weighted by the plausibility or likelihood of taking such paths, gives a better representation of the actual system we are modeling. We explore alternative distance metrics in this section.


Figure 20.14: What other distance metrics are useful?

Diffusion kernel matrices help capture the global network structure of graphs, informing a more complex definition of distance.

Let _A_ be our regular adjacency matrix. _D_ is the diagonal matrix of degrees. We can define _L_ , the Laplacian matrix, as follows:


We then define a diffusion kernel _K_ as


Where _β_ is the diffusion parameter. Note that we are taking a matrix exponential and not an element-wise exponential, which is based on the Taylor series expansion as follows:


321

6.047/6.878 Lecture 12B: Networks I


So what does the matrix _K_ represent? There are multiple ways to interpret _K_ , we will list the most relevant to us below:

**Random Walks** – One way to interpret _K_ as the results of a random walk. Let’s assume we have a graph and at the node of interest, we have a probability distribution over the edges representing that probability that we move along that edge. Like the figure below:


Figure 20.15: Illustration of a random walk

_β_ is the transition probability along a specific edge. And there is also a probability that we don’t move (represented here as a self loop). Note that for the probability distribution to be valid it must sum up to 1.

If we have the setup above, then _Kij_ is equal to the probability of the walk that started at _i_ being at _j_ after infinite time steps. To derive that result, we can write our graph as a Markov model and take the limit as _t →∞_

**Stochastic Process** – Another way we can interpret the diffusion kernel is through a stochastic process.

- for each node _i_ , consider a random variable _Zi_ ( _t_ )

- let _Zi_ ( _t_ ) be zero-mean with some defined variance.

- covariance for _Zi_ ( _t_ ) and _Zj_ ( _t_ ) is zero (independent to each other).

- each variable sends a fraction to the neighbors


let the time evolution operator _T_ ( _t_ ) be


then the covariance is equal to


Then as we take ∆ _t →_ 0 we get


322

6.047/6.878 Lecture 12B: Networks I

## **20.7 Neural Networks**

Neural networks came out modeling the brain and the nervous system in an attempt to achieve brain-like learning. They are highly parallel and by learning simple concepts we can achieve very complex behaviors. In relevance to this book, they also have proved to be very good biological models (not surprising giving where they came about).

### **20.7.1 Feed-forward nets**

In a neural network we map the input to the output passing through hidden states that are parametrized by learning.


Figure 20.16: Illustration of a neural network

- Information flow is unidirectional

- Data is presented to Input layer

- Passed on to Hidden Layer

- Passed on to Output layer

- Information is distributed

- Information processing is parallel

### **20.7.2 Back-propagation**

Back-propagation is one of the most influential results for training neural nets and allowing us to easily deal with multi-layer networks.

- Requires training set (input / output pairs)

- Starts with small random weights

323

6.047/6.878 Lecture 12B: Networks I

- Error is used to adjust weights (supervised learning)

It basically performs gradient descent on the error landscape trying to minimize the error. Thus, back propagation can be slow.

### **20.7.3 Deep Learning**

Deep learning is a collection of statistical machine learning techniques used to learn feature hierarchies. Often based on artificial neural networks. Deep neural networks have more than one hidden layer. Each successive layer in a neural network uses features in the previous layer to learn more complex features. One of the (relevant) aims of deep learning methods is to perform hierarchical feature extraction. This makes deep learning an attractive approach to modeling hierarchical generative processes as are commonly found in systems biology.

#### **Example: DeepBind (Alipanahi et al. 2015)**

DeepBind[1] is a machine learning tool developed by Alipanahi et al. to predict the sequence specificities of DNA- and RNA-binding proteins using deep learning based methods.

The authors point out three difficulties encountered when training models of sequence of specificities on the large volumes of sequence data produced by modern high-throughput technologies: (a) the data comes in qualitatively different forms, including protein binding microarrays, RNAcompete assays, ChIPseq and HT-SELEX, (b) the quantity of data is very large (typical experiments measure ten to a hundred thousand sequences and (c) each data acquisition technology has it’s own formats and error profile and thus an algorithm is needed that is robust to these unwanted effects.

The DeepBind method is able to resolve these difficulties by way of (a) parallel implementation on a graphics processing unit, (b) tolerating a moderate degree of noise and mis-classified training data and (c) train predictive model in an automatic fashion while avoiding the need for hand-tuning. The following figures illustrate aspects of the Deep Bind pipeline.

To address the concern of overfitting, the authors used several regularizers, including dropout, weight decay and early stopping.

#### **Dropout: Prevention of Over-Fitting**

Dropout[5] is a technique for addressing the problem of overfitting on the training data in the context of large networks. Due to the multiplication of gradients in the computation of the chain rule, hidden unit weights are co-adapted which can lead to overfitting. One way to avoid co-adaption of hidden unit weights is to simply drop units (randomly). A beneficial consequence of dropping units is that larger neural networks are more computationally intensive to train.

However, this approach take a little longer with respect to training. Furthermore, tuning step-size is a bit of a challenge. The authors provide an Appendix, in which they (in part (A)) provide a helpful “Practical Guide for Training Dropout Networks.” They note that typical values for the dropout parameter _p_ (which

324

6.047/6.878 Lecture 12B: Networks I


Figure 20.17: A flowchart of the DeepBind procedure (taken from the DeepBind paper). Five sequences are being processed in parallel by the model. The model convolves the sequences (we can think of the deepbind model as a filter scanning through the sequencs), recitifies and pools them in order to produce a feature vector which is then passed through a deep neural network. The output from the deepnet is compared against the desired output and the error is back-propagated through the pipeline.


Figure 20.18: An illustration of the calibration, training and testing procedure used by the DeepBind method (taken from the DeepBind paper).

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Alipanahi, Babak, Andrew Delong, et al. "Predicting the Sequence Specificities of DNA-and RNA-binding Proteins by Deep Learning." _Nature Biotechnology_ (2015).

determines the probability that a node will be dropped) are between 0.5 and 0.8 for hidden layers and 0.8 for input layers.

## **20.8 Open Issues and Challenges**

Some of the challenges regarding the previous covered topics are

- **Validation** How do we know the network structure is right?

- How do we know if the network function is right?

- Measuring and modeling protein expression

- Understanding the evolution of regulatory networks

- Mostly it is intractable to compute joint distributions so we focus on marginal distributions.

325

6.047/6.878 Lecture 12B: Networks I

Figures of neural nets before and after dropout removed due to copyright restrictions. Source: Srivastava, Nitish et al. "Dropout: A simple way to prevent neural networks from overfitting." The Journal of Machine Learning Research 15, no. 1 (2014): 1929-1958.

Figure 20.19: An illustration (taken from the Srivastava et al. paper) of a thinned net produced after the dropout procedure was applied. The units that have been crossed out have been dropped.

- Often we have a very large number of regulators or targets making some of the problems require simplifying assumption to be able to make it tractable.

## **20.9 Current Research Directions**

## **20.10 Further Reading**

To learn more about the topics discussed in this chapter, you can look for following key terms.

- Probabilistic graphical models

- Network Completion

- Non-negative matrix factorization

- Network Alignment

- Network Integration

326

6.047/6.878 Lecture 12B: Networks I

Figures of neural nets before and after dropout removed due to copyright restrictions. Source: Srivastava, Nitish et al. "Dropout: A simple way to prevent neural networks from overfitting." The Journal of Machine Learning Research 15, no. 1 (2014): 1929-1958.

Figure 20.20: A plot (taken from the Srivastava et al. paper) illustrating that the classification error rate decreases noticeably when the dropout procedure is applied.

## **20.11 Tools and Techniques**

## **20.12 What Have We Learned?**

- Networks come in various types and can be represented in probabilistic and algebraic views

- Different centrality measures gauge the importance of nodes/edges from different aspects

- PCA and SVD are useful for uncovering structural patterns in the network by performing matrix decomposition

- Sparse PCA improves upon PCA by selecting a few most representative variables in the data and more accurately recovers community structure

- Network communities have a variety of definitions, each of which has specific algorithms designed for community detection

- Neural networks and deep learning networks are supervised learning machines that capture complex patterns in data.

## **Bibliography**

- [1] B. Alipanahi, A. Delong, M.T. Weirauch, and B.J. Frey. Predicting the sequence specificities of dna and rna-binding proteins by deep learning. _Nature Biotechnology_ , 33:831–838, 2015.

- [2] M. Girvan and M.E.J. Newman. Community structure in social and biological networks. _Proceedings of the National Academy of Sciences_ , 99(12):7821–7826, 2002.

- [3] O. Hein, M. Schwind, and W. K¨onig. Scale-free networks: The impact of fat tailed degree distribution on diffusion and communication processes. _Wirtschaftsinformatik_ , 48(4):267–275, 2006.

327

6.047/6.878 Lecture 12B: Networks I

- [4] T.I. Lee, N.J. Rinaldi, F. Robert, D.T. Odom, Z. Bar-Joseph, G.K. Gerber, N.M. Hannett, C.T. Harbison, C.M. Thompson, I. Simon, et al. Transcriptional regulatory networks in saccharomyces cerevisiae. _Science Signalling_ , 298(5594):799, 2002.

- [5] N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov. Dropout: A simple way to prevent neural networks from overfitting. _Journal of Machine Learning Research_ , 15:1929–1958, 2014.

- [6] S.M. van Dongen. _Graph clustering by flow simulation_ . PhD thesis, University of Utrecht, The Netherlands, 2000.

- [7] U. Von Luxburg. A tutorial on spectral clustering. _Statistics and computing_ , 17(4):395–416, 2007.

- [8] Wikipedia. Graph partitioning. `http://en.wikipedia.org/wiki/Graph_partitioning` , 2012.

- [9] Wikipedia. Minimum cut. `http://en.wikipedia.org/wiki/Minimum_cut` , 2012.

328

CHAPTER

## **TWENTYONE**

REGULATORY NETWORKS: INFERENCE, ANALYSIS, APPLICATION

Guest Lecture by Sushmita Roy (2010) / Soheil Feizi (2012) Scribed by Ben Holmes (2010) / Hamza Fawzi and Sara Brockmueller (2012)

### **Figures**

|21.3|The solid symbols give the in-degree distribution of genes in the regulatory network of _S._<br>_cerevisiae_ (the in-degree of a gene is the number of transcription factors that bind to the<br>promoter of this gene). The open symbols give the in-degree distribution in the comparable<br>random network. Figure taken from [4].<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|336|
|---|---|---|
|21.4|Scale-free vs. random Erd˝os-Renyi networks . . . . . . . . . . . . . . . . . . . . . . . . . .|337|
|21.5|Network motifs in regulatory networks: Feed-forward loops involved in speeding-up re-<br>sponse of target gene. Regulators are represented by blue circles and gene promoters are<br>represented by red rectangles (figure taken from [4])<br>. . . . . . . . . . . . . . . . . . . . .|338|
|21.6|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|339|
|21.7|A network with 8 nodes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|342|


## **21.1 Introduction**

Living systems are composed of multiple layers that encode information about the system. The primary layers are:

1. Epigenome: Defined by chromatin configuration. The structure of chromatin is based on the way that histones organize DNA. DNA is divided into nucleosome and nucleosome-free regions, forming its final shape and influencing gene expression.<sup>1</sup>

> 1More in the epigenetics lecture.

329

6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application

2. Genome: Includes coding and non-coding DNA. Genes defined by coding DNA are used to build RNA, and Cis-regulatory elements regulate the expression of these genes.

3. Transcriptome RNAs (ex. mRNA, miRNA, ncRNA, piRNA) are transcribed from DNA. They have regulatory functions and manufacture proteins.

4. Proteome Composed of proteins. This includes transcription factors, signaling proteins, and metabolic enzymes.

Interactions between these components are all different, but understanding them can put particular parts of the system into the context of the whole. To discover relationships and interactions within and between layers, we can use networks.

### **21.1.1 Introducing Biological Networks**

Biological networks are composed as follows:

**Regulatory Net** – set of regulatory interactions in an organism.

- Nodes are regulators (ex. transcription factors) and associated targets.

- Edges correspond to regulatory interaction, directed from the regulatory factor to its target. They are signed according to the positive or negative effect and weighted according to the strength of the reaction.

**Metabolic Net** – connects metabolic processes. There is some flexibility in the representation, but an example is a graph displaying shared metabolic products between enzymes.

- Nodes are enzymes.

- Edges correspond to regulatory reactions, and are weighted according to the strength of the reaction.

**Signaling Net** – represents paths of biological signals.

- Nodes are proteins called signaling receptors.

- Edges are transmitted and received biological signals, directed from transmitter to receiver.

**Protein Net** – displays physical interactions between proteins.

   - Nodes are individual proteins.

   - Edges are physical interactions between proteins.

- **Co-Expression Net** – describes co-expression functions between genes. Quite general; represents functional rather than physical interaction networks, unlike the other types of nets. Powerful tool in computational analysis of biological data.

   - Nodes are individual genes.

   - Edges are co-expression relationships.

Today, we will focus exclusively on regulatory networks. Regulatory networks control context-specific gene expression, and thus have a great deal of control over development. They are worth studying because they are prone to malfunction and causing disease.

330

6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

(a) Interactions between biological networks.

### **21.1.2 Interactions Between Biological Networks**

Individual biological networks (that is, layers) can themselves be considered nodes in a larger network representing the entire biological system. We can, for example, have a signaling network sensing the environment governing the expression of transcription factors. In this example, the network would display that TFs govern the expression of proteins, proteins can play roles as enzymes in metabolic pathways, and so on.

The general paths of information exchange between these networks are shown in figure 21.4.

### **21.1.3 Studying Regulatory Networks**

In general, networks are used to represent dependencies among variables. Structural dependencies can be represented by the presence of an edge between nodes - as such, unconnected nodes are conditionally independent. Probabilistically, edges can be assigned a ”weight” that represents the strength or the likelihood of the interaction. Networks can also be viewed as matrices, allowing mathematical operations. These frameworks provides an effective way to represent and study biological systems.

These networks are particularly interesting to study because malfunctions can have a large effect. Many diseases are caused by rewirings of regulatory networks. They control context specific expression in development. Because of this, they can be used in systems biology to predict development, cell state, system state, and more. In addition, they encapsulate much of the evolutionary difference between organisms that are genetically similar.

To describe regulatory networks, there are several challenging questions to answer.

- **Element Identification** What are the elements of a network? Elements constituting regulatory networks were identified last lecture. These include upstream motifs and their associated factors.

- **Network Structure Analysis** How are the elements of a network connected? Given a network, structure analysis consists of examination and characterization of important properties. It can be done biological networks but is not restricted to them.

- **Network Inference** How do regulators interact and turn on genes? This is the task of identifying gene edges and characterizing their actions.

- **Network Applications** What can we do with networks once we have them? Applications include predicting function of regulating genes and predicting expression levels of regulated genes.

331

6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application

## **21.2 Structure Inference**

### **21.2.1 Key Questions in Structure Inteference**

- **How to choose network models?** A number of models exist for representing networks, a key problem is choosing between them based on data and predicted dynamics.

- **How to choose learning methods?** Two broad methods exist for learning networks. Unsupervised methods attempt to infer relationships for unalabeled datapoints and will be described in sections to come. Supervised methods take a subset of network edges known to be regulatory, and learn a classifier to predict new ones.<sup>2</sup>

- **How to incorporate data?** A variety of data sources can be used to learn and build networks including Motifs, ChIP binding assays, and expression. Data sources are always expanding; expanding availability of data is at the heart of the current revolution in analyzing biological networks.

### **21.2.2 Abstract Mathematical Representations for Networks**

Think of a network as a function, a black box. Regulatory networks for example, take input expressions of regulators and spit out output expression of targets. Models differ in choosing the nature of functions and assigning meaning to nodes and edges.

- **Boolean Network** This model discretizes node expression levels and interactions. Functions represented by edges are logic gates.

- **Differential Equation Model** These models capture network dynamics. Expression rate changes are function of expression levels and rates of change of regulators. For these it can be very difficult to estimate parameters. Where do you find data for systems out o equilibrium?

- **Probabilistic Graphical Model** These systems model networks as a joint probability distribution over random variables. Edges represent conditional dependencies. Probabilistic graphical models (PGMs) are focused on in the lecture.

#### **Probabilistic Graphical Models**

Probabilistic graphical models (PGMs) are trainable and able to deal with noise and thus they are good tools for working with biological data.<sup>3</sup> In PGMs, nodes can be transcription factors or genes and they are modeled by random variables. If you know the joint distribution over these random variables, you can build the network as a PGMs. Since this graph structure is a compact representation of the network, we can work with it easily and accomplish learning tasks. Examples of PGMS include:

- **Bayesian Network** Directed graphical technique. Every node is either a parent or a child. Parents fully determine the state of children but their states may not be available to the experimenter. The network structure describes the full joint probablility distribution of the network as a product of individual distributions for the nodes. By breaking up the network into local potentials, computational complexity is drastically reduced.

> 2Supervised methods will not be addressed today.

> 3These are Dr. Roys models of choice for dealing with biological nets.

332

6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application

- **Dynamic Bayesian Network** Directed graphical technique. Static bayesian networks do not allow cyclic dependencies but we can try to model them with bayesian networks allowing arbitrary dependencies between nodes at different time points. Thus cyclic dependencies are allowed as the network progresses through time and the network joint probability itself can be described as a joint over all times.

- **Markov Random Field** Undirected graphical technique. Models potentials in terms of cliques. Allows modelling of general graphs including cyclic ones with higher order than pairwise dependencies.

- **Factor Graph** Undirected graphical technique. Factor graphs introduce “factor” nodes specifying interaction potentials along edges. Factor nodes can also be introduced to model higher order potentials than pairwise.

It is easiest to learn networks for Bayesian models. Markov random fields and factor graphs require determination of a tricky partition function. To encode network structure, it is only necessary to assign random variables to TFs and genes and then model the joint probability distribution.

Bayesian networks provide compact representations of JPD

The main strength of Bayesian networks comes from the simplicity of their decomposition into parents and children. Because the networks are directed, the full joint probability distribution decomposes into a product of conditional distributions, one for each node in the network.<sup>4</sup>

#### **Network Inference from Expression Data**

Using expression data and prior knowledge, the goal of network inference is to produce a network graph. Graphs will be undirected or directed. Regulatory networks for example will often be directed whil expression nets for example will be undirected.

## **21.3 Overview of the PGM Learning Task**

We have to learn parameters from the data we have. Once we have a set of parameters, we have to use parametrizations to learn structure. Wewill focus on score based approaches to network building, defining a score to be optimized as a metric for network construction.

### **21.3.1 Parameter Learning for Bayesian Networks**

- **Maximum Likelihood** Chooses parameters to maximize the likelihood of the available data given the model.

In maximum likelihood, compute data likelihood as scores of each ran- dom variable given parents and note that scores can be optimized in- dependently. Depending on the choice of a model, scores

> 4Bayesian networks are parametrized by _θ_ according to our specific choice of network model. With different choices of random variables, we will have different options for parametrizations, _θ_ and therefore different learning tasks: **Discrete** Random variables suggest simple _θ_ corresponding to parameter choices for a multinomial distribution.

> **Continuous** Random variables may be modelled with _θ_ corresponding to means and covariances of gaussians or other continuous distribution.

333

6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application

will be max- imized in different manners. For gaussian distriubution it is possible to simply compute parameters optimizing score. For more complicated model choices it may be necessary to do gradient descent.

- **Bayesian Parameter Estimation** Treats _θ_ itself as a random variable and chooses the parameters maximizing the posterior probability. These methods require a fixed structure and seek to choose internal parameters maximizing score.

#### **Structure Learning**

We can compute best guess parametrizations of structured networks. How do we find structures themselves?

Structure learning proceeds by comparing likelihood of ML parametrizations across different graph structures and in order to seek those structures realizing optimal of ML score.

A Bayesian framework can incorporate prior probabilities over graph structures if given some reason to believe a-priori that some structures are more likely than others.

To perform search in structure learning, we will inevitably have to use a greedy approach because the space of structures is too large to enumerate. Such methods will proceed by an incremental search analogous to gradient descent optimization to find ML parametrizations.

A set of graphs are considered and evaluated according to ML score. Since local optima can exist, it is good to seed graph searches from multiple starting points.

Besides being unable to capture cyclic dependencies as mentioned above, Bayesian networks have certain other limitations.

- **Indirect Links** Since Bayesian networks simply look at statistical dependencies between nodes, it is easy for them to be tricked into putting edges where only indirect relations are in fact present.

- **Neglected Interactions** Especially when structural scores are locally optimized, it is possible that significant biological interactions will be missed entirely. Coexpressed genes may not share proper regulators.

**Slow Speed** Bayesian methods so far discussed are too slow to work effectively whole-genome data.

#### **Excluding Indirect Links**

- **How to eliminate indirect links?** Information theoretic approaches can be used to remove extraneous links by pruning network structures to remove redundant information. Two methods are described.

- **ARACNE** For every triplet of edges, a mutual information score is computed and the ARACNE algorithm excludes edges with the least information subject to certain thresholds above which minimal edges are kept.

- **MRNET** Maximizes dependence between regulators and targets while minimizing the amount of redundant information shared between regulators by stripping edges corresponding to regulators with low variance.

Alternately it is possible to simply look at regulatory motifs and eliminate regulation edges not predicted by common motifs.

334

6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application

### **21.3.2 Learning Regulatory Programs for Modules**

- **How to fix omissions for coregulated genes?** By learning parameters for regulatory models instead of individual genes, it is possible to exploit the tendency of coexpressed genes to be regulated similarly. Similar to the method of using regulatory motifs to prune redundant edges, by modeling modules at once, we reduce network edge counts while increasing data volume to work with.

With extensions, it is possible to model cyclic dependencies as well. Module networks allow clustering revisitation where genes are reassigned to clusters based on how well hey are predicted by a regulatory program for a module.

Modules however cannot accomodate genes sharing module membership. divide and conquer for speeding up learning

- **How to speed up learning?** Dr. Roy has developed a method to break the large learning problem into smaller tasks using a divide and conquer technique for undirected graphs. By starting with clusters it is possible to infer regulatory networks for individual clusters then cross edges, reassign genes, and iterate.

### **21.3.3 Conclusions in Network Inference**

Regulatory networks are important but hard to construct in general. By exploiting modularity, it is often possible to find reliable structures for graphs and subgraphs.<sup>5</sup>

Many extensions are on the horizon for regulatory networks. These include inferring causal edges from expression correlations, learning how to share genes between clusters, and others.

## **21.4 Applications of Networks**

Using linear regression and regression trees, we will try to predict expression from networks. Using collective classification and relaxation labeling, we will try to assign function to unknown network elements.

We would like to use networks to:

1. predict the expression of genes from regulators.

   - In expression prediction, the goal is to parametrize a relationship giving gene expression levels from regulator expression levels. It can be solved in various manners including regression and is related to the problem of finding functional networks.

2. predict functions for unknown genes.

### **21.4.1 Overview of Functional Models**

One model for prediction is a conditional gaussian: a simple model trained by linear regression. A more complex prediction model is a regression tree trained by nonlinear regression.

> 5Dr. Roy notes that many algorithms are available for running module network inference with various distributions. Neural net pacakges and Bayesian packages among others are available.

335

6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application

#### **Conditional Gaussian Models**

Conditional gaussian models predict over a continuous space and are trained by a simple linear regression to maximize likelihood of data. They predict targets whose expression levels are means of gaussians over regulators.

Conditional gaussian learning takes a structured, directed net with targets and regulating transcription factors. You can estimate gaussian parameters, _µ_ , _σ_ from the the data by finding parameters maximizing likelihood - after a derivative, the ML approach reduces to solving a linear equation.

From a functional regulatory network derived from multiple data sources<sup>6</sup> ,Dr, Roy trained a gaussian model for prediction using time course expression data and tested it on a hold-out testing set. In comparisons to predictions by a modle trained from a random network, found out that the network predicted substantially better than random.

The linear model used makes a strong assumption on linearity of interaction. This is probably not a very accurate assumption to make but it appears to work to some extent with the dataset tested.

#### **Regression Tree Models**

Regression tree models allow the modeler to use a multimodal distribtion incorporating nonlinear dependencies between regulator and target gene expression. The final structure of a regression tree describes expression grammar in terms of a series of choices made at regression tree nodes. Because targets can share regulatory programs, notions of recurring motifs may be incorporated. Regression trees are rich models but tricky to learn. regression trees in predicting expression

In practice, prediction works its way down a regression tree given regulator expression levels. Upon reaching the leaf nodes of the regression tree, a prediction for gene expression is made.

### **21.4.2 Functional Prediction for Unannotated Nodes**

Given a network with an incomplete set of labels, the goal of function annotation is to predict labels for unknown genes. We will use methods falling under the broad category of guilt by association. If we know nothing about a node but that its neighbors are involved in a function, assign that function to the unknown node.

Association can include any notion of network relatedness discussed above such as co-expression, proteinprotein interactions and co-regulation. Many methods work, two will be discussed: collective classification and relaxation classification; both of which work for regulatory networks encoded as undirected graphs.

#### **Collective Classification**

View functional prediction as a classification problem: Given a node, what is its regulatory class?.

> 6data sources included chromatin, physical binding, expression, motif

336

6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application


<!-- Start of picture text -->
(a) Fly development.<br><!-- End of picture text -->

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

In order to use the graph structure in the prediction problem, we capture properties of the neighborhood of a gene in relational attribute. Since all points are connected in a network, data points are no longer independently distributed - the prediction problem becomes substantially harder than a standard classification problem.

Iterative classification is a simple method with which to solve the classification problem. Starting with an initial guess for unlabeled genes it infers labels iteratively, allowing changed labels to influence node label predictions in a manner similar to gibbs sampling<sup>7</sup>

Relaxation labeling is another approach originally developed to trac terrorist networks. The model uses a suspicion score where nodes are labeled with a suspiciousness according to the suspiciousness of its neighbors. The method is called relaxation labeling because it gradually settles on to a solution according to a learning parameter. It is another instance of iterative learning where genes are assigned probabilities of having a given function.

#### **Regulatory Networks for Function Prediction**

For pairs of nodes, compute a regulatory similarity – the interaction quantity – equal to the size of the intersection of their regulators divided by the size of their union. Having this interaction similarity in the form of an undirected graph over netowrk targets, can use clusters derived from a network in final functional classification.

The model is successful in predicting invaginal disk and neural system development. The blue line in Fig. 21.2a shows the score of every gene predicting its participation in neural system development.

Co-expression an co-regulation can be used side by side to augment the set of genes known to particiapte in neural system development.

> 7see the previous lecture by Manolis describing motif discovery

337

6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application

## **21.5 Structural Properties of Networks**

Much of the early work on networks was done by scientists outside of biology. Physicists looked at internet and social networks and described their properties. Biologists observed that the same properties were also present in biological networks and the field of biological networks was born. In this section we look at some of these structural properties shared by the different biological networks, as well as the networks that arise in other disciplines as well.

### **21.5.1 Degree distribution**


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 21.3: The solid symbols give the in-degree distribution of genes in the regulatory network of _S. cerevisiae_ (the in-degree of a gene is the number of transcription factors that bind to the promoter of this gene). The open symbols give the in-degree distribution in the comparable random network. Figure taken from [4].

In a network, the _degree_ of a node is the number of neighbors it has, i.e., the number of nodes it is connected to by an edge. The _degree distribution_ of the network gives the number of nodes having degree _d_ for each possible value of _d_ = 1 _,_ 2 _,_ 3 _, . . ._ . For example figure 21.3 gives the degree distribution of the _S. cerevisiae_ gene regulatory network. It was observed that the degree distribution of biological networks follow a power law, i.e., the number of nodes in the network having degree _d_ is approximately _cd_<sup>_−γ_</sup> where _c_ is a normalization constant and _γ_ is a positive coefficient. In such networks, most nodes have a small number of connections, except for a few nodes which have very high connectivity.

This property –of power law degree distribution– was actually observed in many different networks across different disciplines (e.g., social networks, the World Wide Web, etc.) and indicates that those networks are not “random”: indeed random networks (constructed from the Erd˝os-Renyi model) have a degree distribution that follows a Poisson distribution where almost all nodes have approximately the same degree and nodes with higher or smaller degree are very rare [6] (see figure 21.4).

Networks that follow a power law degree distribution are known as **scale-free networks** . The few nodes in a scale-free network that have very large degree are called _hubs_ and have very important interpretations. For example in gene regulatory networks, hubs represent transcription factors that regulate a very large number of genes. Scale-free networks have the property of being highly resilient to failures of “random” nodes, however they are very vulnerable to coordinated failures (i.e., the network fails if one of the hub nodes fails, see [1] for more information).

338

6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application


© Carlos Castillo. Some rights reserved. License: CC BY-SA. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- (a) Scale-free graph vs. a random graph (figure taken from [10]) .


(b) Degree distribution of scale-free network vs. random network (figure taken from [3]).

© Vieweg Verlag. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Hein, Oliver, et al. "Scale-free Networks." _Wirtschaftsinformatik_ 48, no. 4 (2006): 267-75.

Figure 21.4: Scale-free vs. random Erd˝os-Renyi networks

In a regulatory network, one can identify four levels of nodes:

1. Influential, master regulating nodes on top. These are hubs that each indirectly control many targets.

2. Bottleneck regulators. Nodes in the middle are important because they have a maximal number of direct targets.

3. Regulators at the bottom tend to have fewer targets but nonetheless they are often biologically essential!

4. Targets.

### **21.5.2 Network motifs**

Network motifs are subgraphs of the network that occur significantly more than random. Some will have interesting functional properties and are presumably of biological interest.

Figure 21.5 shows regulatory motifs from the yeast regulatory network. Feedback loops allow control of regulator levels and feedforward loops allow acceleration of response times among other things.

339

6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Lee, Tong Ihn et al. "Transcriptional Regulatory Networks in Saccharomyces Cerevisiae." _Science_ 298, no. 5594 (2002): 799-804.

Figure 21.5: Network motifs in regulatory networks: Feed-forward loops involved in speeding-up response of target gene. Regulators are represented by blue circles and gene promoters are represented by red rectangles (figure taken from [4])

## **21.6 Network clustering**

An important problem in network analysis is to be able to **cluster** or **modularize** the network in order to identify subgraphs that are densely connected (see e.g., figure 21.6a). In the context of gene interaction networks, these clusters could correspond to genes that are involved in similar functions and that are coregulated.

There are several known algorithms to achieve this task. These algorithms are usually called _graph partitioning algorithms_ since they partition the graph into separate modules. Some of the well-known algorithms include:

- Markov clustering algorithm [5]: The Markov Clustering Algorithm (MCL) works by doing a random walk in the graph and looking at the steady-state distribution of this walk. This steady-state distribution allows to cluster the graph into densely connected subgraphs.

- Girvan-Newman algorithm [2]: The Girvan-Newman algorithm uses the number of shortest paths going through a node to compute the _essentiality_ of an edge which can then be used to cluster the network.

- Spectral partitioning algorithm

In this section we will look in detail at the spectral partitioning algorithm. We refer the reader to the references [2, 5] for a description of the other algorithms.

The spectral partitioning algorithm relies on a certain way of representing a network using a matrix. Before presenting the algorithm we will thus review how to represent a network using a matrix, and how to extract information about the network using matrix operations.

340

#### 6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. (a) A partition of a network into two groups.


<!-- Start of picture text -->
1 2<br>3<br>(b) A simple network on 3 nodes. The adja-<br>cency matrix of this graph is given in equation<br>(21.1) .<br><!-- End of picture text -->

Figure 21.6

### **21.6.1 An algebraic view to networks**

**Adjacency matrix** One way to represent a network is using the so-called _adjacency matrix_ . The adjacency matrix of a network with _n_ nodes is an _n × n_ matrix _A_ where _Ai,j_ is equal to one if there is an edge between nodes _i_ and _j_ , and 0 otherwise. For example, the adjacency matrix of the graph represented in figure 21.6b is given by:


If the network is weighted (i.e., if the edges of the network each have an associated weight), the definition of the adjacency matrix is modified so that _Ai,j_ holds the weight of the edge between _i_ and _j_ if the edge exists, and zero otherwise.

**Laplacian matrix** For the clustering algorithm that we will present later in this section, we will need to count the number of edges between the two different groups in a partitioning of the network. For example, in Figure 21.6a, the number of edges between the two groups is 1. The _Laplacian matrix_ which we will introduce now comes in handy to represent this quantity algebraically. The Laplacian matrix _L_ of a network on _n_ nodes is a _n × n_ matrix _L_ that is very similar to the adjacency matrix _A_ except for sign changes and for the diagonal elements. Whereas the diagonal elements of the adjacency matrix are always equal to zero (since we do not have self-loops), the diagonal elements of the Laplacian matrix hold the _degree_ of each node (where the degree of a node is defined as the number of edges incident to it). Also the off-diagonal elements of the Laplacian matrix are set to be _−_ 1 in the presence of an edge, and zero otherwise. In other words, we have:


For example the Laplacian matrix of the graph of figure 21.6b is given by (we emphasized the diagonal elements in bold):


341

6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application

**Some properties of the Laplacian matrix** The Laplacian matrix of any network enjoys some nice properties that will be important later when we look at the clustering algorithm. We briefly review these here.

The Laplacian matrix _L_ is always **symmetric** , i.e., _Li,j_ = _Lj,i_ for any _i, j_ . An important consequence of this observation is that all the eigenvalues of _L_ are real (i.e., they have no complex imaginary part). In fact one can even show that the eigenvalues of _L_ are all nonnegative<sup>8</sup> The final property that we mention about _L_ is that all the rows and columns of _L_ sum to zero (this is easy to verify using the definition of _L_ ). This means that the smallest eigenvalue of _L_ is always equal to zero, and the corresponding eigenvector is _s_ = (1 _,_ 1 _, . . . ,_ 1).

**Counting the number of edges between groups using the Laplacian matrix** Using the Laplacian matrix we can now easily count the number of edges that separate two disjoint parts of the graph using simple matrix operations. Indeed, assume that we partitioned our graph into two groups, and that we define a vector _s_ of size _n_ which tells us which group each node _i_ belongs to:


Then one can easily show that the total number of edges between group 1 and group 2 is given by the quantity<sup><u>1</u></sup> 4 _s_<sup>_T_</sup> _Ls_ where _L_ is the Laplacian of the network.

To see why this is case, let us first compute the matrix-vector product _Ls_ . In particular let us fix a node _i_ say in group 1 (i.e., _si_ = +1) and let us look at the _i_ ’th component of the matrix-vector product _Ls_ . By definition of the matrix-vector product we have:


We can decompose this sum into three summands as follows:


Using the definition of the Laplacian matrix we easily see that the first term corresponds to the degree of _i_ , i.e., the number of edges incident to _i_ ; the second term is equal to the negative of the number of edges connecting _i_ to some other node in group 1, and the third term is equal to the number of edges connecting _i_ to some node ingroup 2. Hence we have:


Thus combining the two equations above we get:


Now to get the total number of edges between group 1 and group 2, we simply sum the quantity above over all nodes _i_ in group 1:


> 8One way of seeing this is to notice that _L_ is diagonally dominant and the diagonal elements are strictly positive (for more details the reader can look up “diagonally dominant” and “Gershgorin circle theorem” on the Internet).

342

6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application

We can also look at nodes in group 2 to compute the same quantity and we have:


Now averaging the two equations above we get the desired result:


where _s_<sup>_T_</sup> is the row vector obtained by transposing the column vector _s_ .

### **21.6.2 The spectral clustering algorithm**

We will now see how the linear algebra view of networks given in the previous section can be used to produce a “good” partitioning of the graph. In any good partitioning of a graph the number of edges between the two groups must be relatively small compared to the number of edges within each group. Thus one way of addressing the problem is to look for a partition so that the number of edges between the two groups is minimal. Using the tools introduced in the previous section, this problem is thus equivalent to finding a vector _s ∈{−_ 1 _,_ +1 _}_<sup>_n_</sup> taking only values _−_ 1 or +1 such that<sup><u>1</u></sup> 4<sup>_sT Ls_isminimal,where</sup><sup>_L_istheLaplacian</sup> matrix of the graph. In other words, we want to solve the minimization problem:


If _s_<sup>_∗_</sup> is the optimal solution, then the optimal partioning is to assign node _i_ to group 1 if _si_ = +1 or else to group 2.

This formulation seems to make sense but there is a small glitch unfortunately: the solution to this problem will always end up being _s_ = (+1 _, . . . ,_ +1) which corresponds to putting all the nodes of the network in group 1, and no node in group 2! The number of edges between group 1 and group 2 is then simply zero and is indeed minimal!

To obtain a meaningful partition we thus have to consider partitions of the graph that are nontrivial. Recall that the Laplacian matrix _L_ is always symmetric, and thus it admits an eigendecomposition:


where Σ is a diagonal matrix holding the nonnegative eigenvalues _λ_ 1 _, . . . , λn_ of _L_ and _U_ is the matrix of eigenvectors and it satisfies _U_<sup>_T_</sup> = _U_<sup>_−_1</sup> .

The cost of a partitioning _s ∈{−_ 1 _,_ +1 _}_<sup>_n_</sup> is given by


where _α_ = _U_<sup>_T_</sup> _s_ give the decomposition of _s_ as a linear combination of the eigenvectors of _L_ : _s_ =<sup>�</sup> _ni_ =1<sup>_αiui_.</sup>

343

6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 21.7: A network with 8 nodes.

Recall also that 0 = _λ_ 1 _≤ λ_ 2 _≤· · · ≤ λn_ . Thus one way to make the quantity above as small as possible (without picking the trivial partitioning) is to concentrate all the weight on _λ_ 2 which is the smallest nonzero eigenvalue of _L_ . To achieve this we simply pick _s_ so that _α_ 2 = 1 and _αk_ = 0 for all _k̸_ = 2. In other words, this corresponds to taking _s_ to be equal to _u_ 2 the second eigenvector of _L_ . Since in general the eigenvector _u_ 2 is not integer-valued (i.e., the components of _u_ 2 can be different than _−_ 1 or +1), we have to convert first the vector _u_ 2 into a vector of +1’s or _−_ 1’s. A simple way of doing this is just to look at the signs of the components of _u_ 2 instead of the values themselves. Our partition is thus given by:


To recap, the spectral clustering algorithm works as follows:

#### **Spectral partitioning algorithm**

- Input: a network

- Output: a partitioning of the network where each node is assigned either to group 1 or group 2 so that the number of edges between the two groups is small

1. Compute the Laplacian matrix _L_ of the graph given by:


2. Compute the eigenvector _u_ 2 for the second smallest eigenvalue of _L_ .

3. Output the following partition: Assign node _i_ to group 1 if ( _u_ 2) _i ≥_ 0, otherwise assign node _i_ to group 2.

We next give an example where we apply the spectral clustering algorithm to a network with 8 nodes.

344

6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application

**Example** We illustrate here the partitioning algorithm described above on a simple network of 8 nodes given in figure 21.7. The adjacency matrix and the Laplacian matrix of this graph are given below:


Using the `eig` command of Matlab we can compute the eigendecomposition _L_ = _U_ Σ _U_<sup>_T_</sup> of the Laplacian matrix and we obtain:


We have highlighted in bold the second smallest eigenvalue of _L_ and the associated eigenvector. To cluster the network we look at the sign of the components of this eigenvector. We see that the first 4 components are negative, and the last 4 components are positive. We will thus cluster the nodes 1 to 4 together in the same group, and nodes 5 to 8 in another group. This looks like a good clustering and in fact this is the “natural” clustering that one considers at first sight of the graph.

## **_Did You Know?_**

The mathematical problem that we formulated as a motivation for the spectral clustering algorithm is to find a partition of the graph into two groups with a minimimal number of edges between the two groups. The spectral partitioning algorithm we presented does not always give an optimal solution to this problem but it usually works well in practice.

Actually it turns out that the problem as we formulated it can be solved exactly using an efficient algorithm. The problem is sometimes called the **minimum cut** problem since we are looking to cut a minimum number of edges from the graph to make it disconnected (the edges we cut are those between group 1 and group 2). The minimum cut problem can be solved in polynomial time in general, and we refer the reader to the Wikipedia entry on _minimum cut_ [9] for more information. The problem however with minimum cut partitions it that they usually lead to partitions of the graph that are not balanced (e.g., one group has only 1 node, and the remaining nodes are all in the other group). In general one would like to impose additional constraints on the clusters (e.g., lower or upper bounds on the size of clusters, etc.) to obtain more realistic clusters. With such constraints, the problem becomes harder, and we refer the reader to the Wikipedia entry on _Graph partitioning_ [8] for more details.

345

6.047/6.878 Lecture 18: Regulatory Networks: Inference, Analysis, Application

## **_FAQ_**

- **Q:** How to partition the graph into more than two groups?

- **A:** In this section we only looked at the problem of partitioning the graph into two clusters. What if we want to cluster the graph into more than two clusters? There are several possible extensions of the algorithm presented here to handle _k_ clusters instead of just two. The main idea is to look at the _k_ eigenvectors for the _k_ smallest nonzero eigenvalues of the Laplacian, and then to apply the _k_ -means clustering algorithm appropriately. We refer the reader to the tutorial [7] for more information.

## **Bibliography**

- [1] R. Albert. Scale-free networks in cell biology. _Journal of cell science_ , 118(21):4947–4957, 2005.

- [2] M. Girvan and M.E.J. Newman. Community structure in social and biological networks. _Proceedings of the National Academy of Sciences_ , 99(12):7821–7826, 2002.

- [3] O. Hein, M. Schwind, and W. K¨onig. Scale-free networks: The impact of fat tailed degree distribution on diffusion and communication processes. _Wirtschaftsinformatik_ , 48(4):267–275, 2006.

- [4] T.I. Lee, N.J. Rinaldi, F. Robert, D.T. Odom, Z. Bar-Joseph, G.K. Gerber, N.M. Hannett, C.T. Harbison, C.M. Thompson, I. Simon, et al. Transcriptional regulatory networks in saccharomyces cerevisiae. _Science Signalling_ , 298(5594):799, 2002.

- [5] S.M. van Dongen. _Graph clustering by flow simulation_ . PhD thesis, University of Utrecht, The Netherlands, 2000.

- [6] M. Vidal, M.E. Cusick, and A.L. Barabasi. Interactome networks and human disease. _Cell_ , 144(6):986– 998, 2011.

- [7] U. Von Luxburg. A tutorial on spectral clustering. _Statistics and computing_ , 17(4):395–416, 2007.

- [8] Wikipedia. Graph partitioning, 2012.

- [9] Wikipedia. Minimum cut, 2012.

- [10] Wikipedia. Scale-free network, 2012.

346

CHAPTER

## **TWENTYTWO**

## CHROMATIN INTERACTIONS

Silvia Canas; Vivek Dasari

### **Figures**

|22.1 Chromosome Territories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|346|
|---|---|
|22.2 1) ChIP and DamID only identify regions that have come into close contact with the<br>nuclear lamina. 2) 3C-based methods identify all DNA-DNA interactions, regardless of<br>whether they are in the periphery of the nucleus or not<br>. . . . . . . . . . . . . . . . . . .|348|
|22.3 ChIP Method of Measurement<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|349|
|22.4 DamID Method of Measurement<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|350|
|22.5 3C-based methods for identifying chromatin interactions . . . . . . . . . . . . . . . . . . .|350|
|22.6 Method for generating Hi-C data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|352|
|22.7 ChIA-PET protocol<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|352|
|22.8 Lamina Associated Domains (LADs) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|353|
|22.9 Matrix representing Hi-C read count . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|354|
|22.10Image depicting sources of bias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|355|
|22.11Chromosome Territories in 3D<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|356|
|22.12A core chromosome architecture is evident. About 70% of regions are constitutive (cLAD/-<br>ciLAD) and 30% of regions are facultative (fLAD) . . . . . . . . . . . . . . . . . . . . . .|357|
|22.13AT regions are indicators for constitutive regions . . . . . . . . . . . . . . . . . . . . . . .|357|
|22.14LADs Through The (Single) Cell Cycle (Kind et al, Cell 2013)<br>. . . . . . . . . . . . . . .|358|
|22.15Loop Extrusion as a Mechanism of Chromosome Orientation<br>. . . . . . . . . . . . . . . .|358|


## **22.1 Introduction**

In recent years, many subtle and previously disregarded mechanisms for fine genetic regulation have been discovered. Aside from direct regulation by proteins, these mechanisms include the involvement of nonprotein coding regions of the genome, epigenomic factors such histone modifications, and diverse RNA

347

6.047/6.878 Lecture 30: Chromatin Interactions

switches. The spatial organization of chromatin inside the nucleus, chromatin modifier complexes and its functional consequences have also become an area of interest. In this chapter, we will delve into the study of 3D chromatin structures, starting with the state of art in this field, the most relevant terminology and current methods. Specially we will focus on the study of DNA regions located by peripheral regions of the nucleus (thus in close contact with the nuclear lamina) Finally, we will discuss the computational methods involved in studying nuclear genome organization.

### **22.1.1 What’s already known**

DNA is locally compacted in nucleosomes, by wrapping around histone octamers. Each nucleosome comprises about 147 bps packed in 1.67 lef-handed superhelical turns. DNA is globally compacted as chromosomes (during cell division and mitosis). Chromosomes have been dyed with different colors, and it has been shown that some chromosomes have radial preferences within the cell nucleus, even when the cell is not actively undergoing division and the chromosomes are not condensed. That is, some chromosomes prefer to stay near the center of the nucleus while others tend towards the periphery. These are known as chromosome territories (CT). The territories of homologous chromosomes usually do not lie not near one another. It is also know that there is an overarching nuclear ’architecture’ that is observable, conserved even between different cell types.


Figure 22.1: Chromosome Territories

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Cremer, Thomas, and Christoph Cremer. "Chromosome Territories, Nuclear Architecture and Gene Regulation in Mammalian Cells." N _ature Reviews Genetics_ 2, no. 4 (2001): 292-301.

### **22.1.2 What we don’t know**

While local organization (nucleosome packaging) and global organization (chromosome condensation) of DNA are somehow understood, the intermediate structures of DNA are not yet well characterized - many speculated states have only been observed in vitro. The positioning of genomic regions in the nucleus on a sub-chromosomal level, for example the specific 3D conformation of a certain chromosomal region containing several genes, is also largely unknown.

While it is known that chromosomes retain some general architecture during the entire cell cycle, it is unknown how that location is maintained and how different chromosomes continue to interact over the couse of the entire cell cycle.

348

6.047/6.878 Lecture 30: Chromatin Interactions

Together, although we do understand certain parts of the function of chromosomes, we do not have a complete mechanistic understanding of this process.

### **22.1.3 Why do we study it?**

In general, we are interested in understanding the functional characteristics of genomic regions and the molecular mechanisms encoded within, which might have implications in human diseases. Particularly, it has been shown that genes that are encoded in spatially neighboring regions are likely to be co-regulated. Also, the DNA packed inside the nucleus is the equivalent of wrapping 20 km of 20 _µ_ m thick thread in something the size of a tennis ball, which would reach from Kendall Square to Harvard and back over 6 and a half times! Isnt this amazing??

## **22.2 Relevant terminology**

### **22.2.1 Nuclear lamina**

The nuclear lamina is a dense network of proteins and filaments that lies on the inner surface of the inner nuclear membrane. Its functions include: Maintenance of the nuclear stability, interact with nuclear pore complexes, and organization of the chromatin by directly interacting and binding with it. The protein meshwork is predominantly made up of lamin proteins.

### **22.2.2 Lamina Associated Domains(LADs)**

Lamina associated domains(LADs) are the portions of the chromatin that interact with the nuclear lamina. Mapping the interactions of the chromatin and the nuclear lamina provides insight towards mapping chromosome folding. While not much is known about LADs, it is known that these regions are closely related to both high gene expression and low gene density, an interesting combination. Additionally LADs are associated with CTCFs, promoters, and CPG islands along its borders.

### **22.2.3 Histones**

Histones are highly alkaline proteins found eukaryotes that comprise the core of nucleosomes, packaging and ordering the nuclear DNA. An octamer form by 2 copies of the core histones H2A, H2B, H3, and H4 forms the nucleosome, which acts as a spool for DNA to wind around.

### **22.2.4 Chromatin**

Chromatin is a complex form by DNA, proteins and RNA that generates the global architecture of DNA in eukaryote nuclei. Its main functions involve DNA packaging, reinforcing the DNA macromolecule to allow mitosis, preventing DNA damage, and regulating gene expression and DNA replication Most of the

349

6.047/6.878 Lecture 30: Chromatin Interactions

mechanisms underlying the formation and regulation of the structure of chromatin are largely unknown; however, during cell division, chromatin organizes by way of chromosomes.

### **22.2.5 Chromosome territories (CT)**

Chromosomes are not randomly distributed throughout the nucleus. Chromosomes occupy specific regions of the nucleus. These regions are called chromosome territories.

### **22.2.6 Gross folding principles**

## **22.3 Molecular Methods for Studying Nuclear Genome Organization**

There are two main types of methods for investigating the three-dimensional structure of chromatin in the nucleus.

- The first set of methods, ChIP and DamID, are methods that measure DNA-’landmark’ interactions. That is, they measure interactions of genome loci with relatively fixed nuclear landmarks, and only regions of the genome that come into contact with the nuclear lamina will be identified.

- The second set of methods, the 3C-based methods, are those that measure DNA-DNA interactions. Any two regions of DNA that interact may be identified, regardless of whether they are near the interior or periphery of the nucleus.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 22.2: 1) ChIP and DamID only identify regions that have come into close contact with the nuclear lamina. 2) 3C-based methods identify all DNA-DNA interactions, regardless of whether they are in the periphery of the nucleus or not

### **22.3.1 Methods for measuring DNA-Nuclear Lamina interactions**

The following methods, ChIP and DamID, both examine regions of DNA the specifically come in contact with the nuclear lamina.

350

6.047/6.878 Lecture 30: Chromatin Interactions

#### **ChIP: Chromatin Immuno Precipitation**

ChIP is a method for detecting regions of DNA that are bound to proteins of interest. Proteins bound with DNA are cross-linked in place with formaldehyde. The protein-DNA complexes are pulled-down using affinity chromatography, mainly using specific antibodies that target the protein of interest. The recovered complexes are then dessassociated, cross-links are broken, and the DNA that was bound to the proteins is fragmented and analyzed. DNA fragments can be then analyzed using sequencing (ChiP-Seq) or microarrays (ChiP-Chip). However, a big challenge associated with the various ChIP techniques is that it can be difficult to get a high-affinity antibody. To study the 3D structure of DNA within the nucleus, ChIP-Seq can be used with antibodies that targed lamina proteins.

#### **DamID: DNA adenine methyltransferase IDentification**

DamID is used to map the binding sites of Chromatin-binding proteins. In the DamID method, DNA adenine methyltransferase ( _Dam_ ) from _E. coli_ is fused to the LaminB1 protein (the Dam enzyme hangs off the end of the protein and is thus in the vicinity for interactions). In _E. coli_ , the _Dam_ enzyme methylates the adenine in the sequence GATC; bacterial genomes contain proteins with functions like Dam to protect their own DNA from digestion by restriction enzymes, or as part of their DNA repair systems. As this process doesnt naturally occur in eukaryotes, the methylated adenines in a region can thus be attributed to an interaction with the protein fused with Dam, thereby implying that that particular region came into close contact with the nuclear lamina. As a control, unfused _Dam_ can be expressed at low levels. This results in a sparse distribution of methylated adenine for which the precise position of the methylated adenines can be used to infer variation in DNA accessibility. The methylated adenine are determined using disulphide PCR assays or other PCR technique sensitive to methylations in the template DNA. In one of those assays, the genome can digested by DpnI, which only cuts methylated GATC sequences. Adapter sequences are then ligated to the ends of these digested pieces, and PCR is run using primers matching the adapters. Only the regions occurring between proximal GATC positions are amplified. The final measurement is the log of the ratio between test and control lamina assocation: positive values are preferentially lamina-associated, and are thus identified as LADs. One advantage of using DamID over ChIP is that DamID does not require a specific antibody which may be difficult to find. However, a disadvantage of using DamID is that the fusion protein must be made and expressed.


Figure 22.3: ChIP Method of Measurement Courtesy of Anthony P. Fejes. Used with permission.

351

6.047/6.878 Lecture 30: Chromatin Interactions


Figure 22.4: DamID Method of Measurement Courtesy of Bas van Steensel. Used with permission.

## **_FAQ_**

- **Q:** How close does DNA have to come to DamID to be methylated?

- **A:** It doesn’t have to bind directly to the lamina, but it does have to come pretty close. DamID has a range of about 1.5kb.

### **22.3.2 Measuring DNA-DNA contacts**

All of the following methods are based on Chromosome Conformation Capturing (3C) with certain modifications.


Figure 22.5: 3C-based methods for identifying chromatin interactions

> © Cold Spring Harbor Laboratory Press. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: de Wit, Elzo and Wouter de Laat. "A decade of 3C Technologies: Insights into Nuclear Organization." _Genes & Development_ 26, no. 1 (2012): 11-24.

352

6.047/6.878 Lecture 30: Chromatin Interactions

#### **3C**

Chromosome Conformation Capturing (3C) is a method that detects which genomic loci are in close vicinity to other loci within the nucleus. Similar to the ChIP method, a cross-linking agent is used freeze proteins bound to DNA in place and forming protein-DNA complexes. The DNA can be then be digested by a restriction enzyme after allowing the bound protein to disassociate. Typically an enzyme with a 6 bps long recognition site that leaves sticky ends, like _HindIII_ , is used. The generated fragments are then induce to self-ligate (Using very low concentration of DNA to prevent the ligation of the fragment with another random fragment). The result is a pool of linear DNA fragments, known as the 3C library, that may be analyzed via PCR by designing primers specifically for the interaction of interest. 3C can be described as a ’one vs one’ method, because the primers used are specifically target to amplify the product of the interaction between 2 regions of interest.

#### **Circularized Chromatin Conformation Capture (4C)**

4C methods can be described as a ’one vs all’ because for a single region of interest, we can examine all its interactions with all other regions in the genome. 4C works similarly to 3C with the main difference being the restriction enzyme used. In 4C, a common cutter is employed to generate more and smaller fragments. These fragments are then again ligated. Some smaller fragments may be excluded, but the result is a circularized fragment of DNA. Primers can be designed to amplify the ’unknown’ fragment of DNA so that all interactions with the region of interest are identified.

#### **Carbon-Copy Chromosome Conformation Capture (5C)**

5C is a ’many vs many’ method and allows the identification of interactions between many regions of interest and many other regions, also of interest, to be analyzed at once. 5C works similarly to 3C. However, after obtaining the 3C library, multiplex ligation-mediated amplification (LMA) is performed. LMA is a method in which multiple targets are amplified. The resulting 5C library may be analyzed on a microarray or high-throughput sequencing.

#### **Hi-C**

Hi-C can be described as an ’all vs all’ method because it identifies all chromatin interactions. Hi-C works by labeling all DNA fragments with biotin before ligation, which marks all the ligation junctions. Magnetic beads are then used to purify the biotin-marked junctions. This Hi-C library may then be fed into next generation sequencing.

#### **ChIP-loop**

ChIP-loop can be described as a ’one vs one’ method, because similar to 3C, only an interaction between two regions of interest may be identified. ChIP-loop is a hybrid between ChIP and the 3C methods. DNA-protein complexes are first cross-linked and digested. Then, as in ChIP, the protein of interest and the DNA bound to it are pulled down using an antibody. The protocol then proceeds as in 3C: the free ends of the fragments are ligated, the cross-linking are reversed, and sequencing can proceed using primers designed specifically for a ’one vs one’ interaction.

353

6.047/6.878 Lecture 30: Chromatin Interactions


Figure 22.6: Method for generating Hi-C data

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Lieberman-Aiden, Erez, et al. "Comprehensive Mapping of Long-range Interactions Reveals Folding Principles of the Human Genome." _Science_ 326, no. 5950 (2009): 289-93.

#### **ChIA-PET**

Chromatin Interception Analysis by Paired-End Tag Sequencing, or ChIA-PET, combines the ChIP and 3C methodologies to determine long-range chromatin interactions genome-wide. It can be described as a ’all vs all’ method, because although a single protein of interest must be identified, any interactions will be identified. In ChIA-PET, DNA-protein complexes are cross-linked, as in previously discussed methods. However, sonication is then used to break up chromatin, and to reduce non-specific interactions. As in the ChIP protocol, an antibody is used to pull down regions of DNA bound to a protein of interest. Two different oligonucleotide linkers are then ligated to the free ends of the DNA. These linkers both have _MmeI_ cut sites. The linkers are then ligated together so that the free ends are connected, after which the fragments are digested with _MmeI_ . _MmeI_ cuts 20 nt downstream of its recognition sequence, so the result of the digestion is the linker bordered by the sequence of interest on either side. This is a ’tag-linker-tag’ structure, and the fragments are known as PETs. The PETs may be sequenced and mapped back to the genome to determine regions of interacting DNA.


Figure 22.7: ChIA-PET protocol

Courtesy of the authors. License: CC BY. Source: Li, Guoliang, et al. "Software ChIA-PET tool for Comprehensive Chromatin Interaction Analysis with Paired-end Tag Sequencing." _Genome Biology_ 11 (2010): R22.

## **22.4 Mapping Genome-Nuclear Lamina Interactions (LADs)**

In this section, we will present how the DamID and Hi-C methods were used to map lamina-associated domains in the genome.

354

6.047/6.878 Lecture 30: Chromatin Interactions

### **22.4.1 Interpreting DamID Data**

The DamID method (described in section 3) was used to identify regions of DNA that interacted with the lamin <u>protein</u> at the nuclear lamina.

## **_Did You Know?_**

DamID experiments typically run for 24 hours and the methylation is irreversible. The results The reare also the average over millions of cells. Therefore, DamID is not suitable for exact time related positioning of the genome, though single cell studies may soon make address this issue!

_Dam f usionprotein_ sults of the DamID experiment were plotted as _log_ 2 _Dam only_ , as done in the figure below (black peaks). For the LaminB1 fusion experiment, positive regions (underlined in yellow in the figure below) indicate regions which preferentially associate with the nuclear lamina. These positive regions are defined as Lamina Associated Domains, or LADs. Approximately 1300 LADs were discovered in human


Figure 22.8: Lamina Associated Domains (LADs)

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

fibroblasts. They were surprisingly large, ranging from about 0.1Mb - 10Mb, with a median size of 5Mb.

## **_FAQ_**

- **Q:** In this representation is a value of 0 significant?

- **A:** No, there is definitely a point where we do not know where the real 0 is. Instead, we can try to make a good estimate of where the 0 value should be, in order to see relative preference (the interior vs exterior of the nucleus)

After LADs have been identified, we can align their boundaries to discover various interesting features such as known gene densities or gene expression levels to the data to build our LAD model. Experiments have shown that LADs are characterized by low gene density and gene expression levels. It was noticed that the LAD boundaries are very sharply defined. By aligning the start positions of many LADs, it was discovered that the borders are <u>particularly</u> marked by CpG islands, outward <u>pointing promoters,</u> and CTCF binding

## **_FAQ_**

**Q:** Why CTCF binding sites? What’s so important about them? sites.

- **A:** That’s the question! Perhaps they help maintain LADs. They could perhaps prevent the LADs from ’spreading’.

355

6.047/6.878 Lecture 30: Chromatin Interactions

## **_FAQ_**

**Q:** How does organization relate to polyclonal expression?

- **A:** Certainly something going on; however, polyclonal repression works on a smaller scale than LAD. It occurs outside of LADs, as an additional repression mechanism

### **22.4.2 Interpreting Hi-C Data**

Hi-C data was collected, and the read were mapped back to the genome. The read counts were compiled into a matrix _O_ (shown below for chromosome 14) where the element _Oi,j_ indicates the number of reads corresponding to an interaction between positions _i_ and _j_ . A strong diagonal is clearly present, and indicates that regions that are close together in 1D are also likely to interact in 3D. Errors in Hi-C data interpretation may occur when the assumptions of the technique are violated: for example, the assumption that the reference genome is correct, which may not be true in the case of a cancerous cell. The matrix was then


Figure 22.9: Matrix representing Hi-C read count

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Lieberman-Aiden, Erez, et al. "Comprehensive Mapping of Long-range Interactions Reveals Folding Principles of the Human Genome." Science 326, no. 5950 (2009): 289-93.

normalized to account genetic distance between two regions, and a matrix indicating which interactions are enriched or depleted in the data. In order to compare the data in the matrix, which is two dimensional, to genomic data sets, which are one dimensional, Principal Component Analysis (PCA) must be used. After PCA, functional characterization of the data is possible. Hi-C identified two global types of regions:

- Type A, which is characterized by open chromatin, gene richness, and active chromatin marks.

- Type B, which is characterized by closed chromatin, and is gene poor.

Both types of regions are primarily self-interacting and interactions between the two types are infrequent. Hi-C also confirmed the presence of chromosome territories, as there were far more intra-chromosomal rather than inter-chromosomal interactions.

356

6.047/6.878 Lecture 30: Chromatin Interactions

## **22.5 Computational Methods for Studying Nuclear Genome Organization**

### **22.5.1 Sources of Bias**


Figure 22.10: Image depicting sources of bias

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Lieberman-Aiden, Erez, et al. "Comprehensive Mapping of Long-range Interactions Reveals Folding Principles of the Human Genome." Science 326, no. 5950 (2009): 289-93.

The three steps that could potentially introduce biases include: Digestion, Ligation, and Sequencing. Digestion efficiency is a function of the restriction enzymes used and therefore some regions of the genome could be less prone to be digested as their distribution of the particular recognition site could be really sparse. Also, some regions could be enriched in the recognition site and thereby will be over-represented in the results. One solution for this is using many different restriction enzymes and compare the results. Ligation efficiency is a function of the fragment lengths. Depending on how the restriction enzymes cut the sequence, some ends may be more or less likely to ligate together. Finally, sequencing efficiency is a function of the composition of the sequence. Some DNA strands will be more difficult to sequence, based on GC richness and presence of repeats, which will introduce bias.

### **22.5.2 Bias Correction**

To minimize ligation bias, non-specific ligation products are removed. Since non-specific ligation products typically have far-away restriction sites, they introduce much larger fragments. In addition, the influence of fragment size on ligation efficiency( _Flen_ ( _alen, blen_ )), the influence of G/C content on amplification and sequencing( _Fgc_ ( _agc, bgc_ )), and the influence of sequence uniqueness on mappability( _M_ ( _a_ ) _∗ M_ ( _b_ )) can all be accounted for and corrected with the equation:


Alternatively, the sources of bias can be less explicitly represented by the following equation:


where the sum of all relative contact probabilities _Ti,j_ for each bin equals 1. The biases are only assumed to be multiplicative. This is solved by matrix balancing, or proportional fitting by an iterative correction algorithm.

357

6.047/6.878 Lecture 30: Chromatin Interactions

### **22.5.3 3D-modeling of 3C-based data**

3D-modeling can reveal many general principles of genome organization. Current models are generated using a combination of inter-locus interactions and known spatial distances between nuclear landmarks. However, a lot of uncertainty remains in current 3D-models because the data is gathered from millions of cells. The practical problems affecting 3D-modeling are due to the large amount of data necessary to construct models and the different dynamics between an individual cell and a population, which lead to unstable models. Next generation modeling is trending towards using single cell genomics.


Figure 22.11: Chromosome Territories in 3D

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Kalhor, Reza, et al. "Genome Architectures Revealed by Tethered Chromosome Conformation Capture and Population-based Modeling." _Nature Biotechnology_ 30, no. 1 (2012): 90-98.

## **22.6 Architecture of Genome Organization**

### **22.6.1 Multiple cell types influence on determining architecture**

Embryonic stem cells (ESC), Neural Progenitor Cells (NPC), and Astrocytes(AC) are all isogenic cell types (they all start as embryonic stem cells). Embryonic stem cells are constantly dividing and are completely undifferentiated; they generate the neural progenitor cells, which are still dividing but less so, and are only halfway differentiated. The neural progenitor cells then generate the completely differentiated astrocytes. It was discovered that during this differentiation process, some areas switched from being Lamina Associated Domains to being interior domains. In the embryonic stem cells, there is very little transcription. However, transcription goes up as the cells become more and more differentiated. This matches the localization of the domains from being primarily associated with the lamina (and thus not expressed) to being localized to the interior. Even though these cell types each have very different properties, a DamID map shows a high level of similarity between the three isogenic cells as well as an independent fibroblast cell. Hidden Markov Models were employed to identify the Lamina Associated Domains between the cells. A core chromosome architecture was found with about 70% of the chromosome being constitutive (cLad/ ciLAD) and 30% of the chromosome being facultative(fLAD).

### **22.6.2 Inter-species comparison of lamina associations**

To determine lamina associations between species, a mouse and a human were used. A genome wide alignment was constructed between a mouse and a human. For each genomic region in the mouse, the best reciprocal region was matched in the human. Then the human genome was re-mapped, and used to reconstruct a

358

6.047/6.878 Lecture 30: Chromatin Interactions


© Cold Spring Harbor Laboratory Press. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Meuleman, Wouter, et al. "Constitutive Nuclear Lamina–genome Interactions are Highly Conserved and Associated with A/T-rich Sequence." _Genome Research_ 23, no. 2 (2013): 270-80.

Figure 22.12: A core chromosome architecture is evident. About 70% of regions are constitutive (cLAD/ciLAD) and 30% of regions are facultative (fLAD)

mouse genome. DamID data was projected onto this map and there was 83% concordance between the two genomes (91% for the constitutive regions; 67% for the facultative regions).

### **22.6.3 A-T Content Rule**

A-T content has been found to be a strong predictor for lamina association within core architecture. Additional support for this prediction is that the LAD-structure that makes up the core architecture is similar to an isochore structure (a large uniform region of DNA).


Figure 22.13: AT regions are indicators for constitutive regions

> © Cold Spring Harbor Laboratory Press. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Meuleman, Wouter, et al. "Constitutive Nuclear Lamina–genome Interactions are Highly Conserved and Associated with A/T-rich Sequence." _Genome Research_ 23, no. 2 (2013): 270-80.

359

6.047/6.878 Lecture 30: Chromatin Interactions

## **22.7 Mechanistic Understanding of Genome Architecture**

### **22.7.1 Understanding Mitosis and LADs**

Organization of chromosomes, particularly in spatial relation to other parts of the chromosome, is not well understood during the mitotic process. The conformation of cells is thought to conform to two different states. Highly compartmentalized and cell-type specific conformations are almost entirely limited to interphase. During the transition into metaphase, chromosomes enter a locus and tissue-independent folding state.

During the mitotic process, approximately 30% of LADs are positioned along the cellular periphery. This positioning, however, reflects protein-lamina contact at intermittent intervals, however, the cells are restricted to the periphery of the cells. During mitotic division, this laminar positioning is stochastically inherited by child cells.


Figure 22.14: LADs Through The (Single) Cell Cycle (Kind et al, Cell 2013) Courtesy of Elsevier, Incorporate, Used with permission. Source: Kind, Jop, et al. "Single-cell Dynamics of Genome-nuclear Lamina Interactions." _Cell_ 153, no. 1 (2013): 178-92.

### **22.7.2 Modeling**

Three dimensional modeling will be increasingly important in understanding the chromosomal interactions. Current techniques have modeled the yeast genome and the _α_ -globin locus (Duan _et al._ Nature (2010), Bau _et al._ Nature SMB (2011)). From modeling studeis it has become clear that we cannot generate a direct relationship between contact probability and spatial distance (i.e. contact probability != spatial distance).

Modelling, however, is an inverse problem, it is harder to go one way than the other. Specifically, it is easier to go from protein structure to a protein contact map than vice versa. Similarly, chromosomal structure is a hard problem, even if we have a contact mapping.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 22.15: Loop Extrusion as a Mechanism of Chromosome Orientation

360

6.047/6.878 Lecture 30: Chromatin Interactions

## **22.8 Current Research Directions:**

### **22.8.1 LADs**

- (a) 30% of the genome is variable between cell types, how are we able to differentiate these differences

- (b) How do lamina and LADs interact? Is there an attractions between LADs and these domains, or is it based on repulsion of the interior

- (c) Why and how are the genes along the periphery of LADs repressed.

### **22.8.2 TADs and Other Compartments:**

- (a) What is the biological basis of compartments, is there some multifaceted component of the compartments?

- (b) How do cohesins work? Are cohesin-extrusion pairs enough to explain all domains?

- (c) Enhancer-promoter loops are confined to specific domains? Are these dynamic components/are they architectural loops mediated by CTCF?

### **22.8.3 Other/Miscellaneous:**

- (a) How do we relate the different chromosomal components (i.e. LADs, TADs, polycomb domain, replication origins, histone modifications, gene expression)?

- (b) Evolutionary basis of genomic architecture: was there an evolutional pressure and when did the folding principles emerge?

- (c) In chromosomal changes do localizations or changes in expression happen first?

## **_Did You Know?_**

This question has (partially) been addressed! In investigating cells that go through multiple rounds of differentiation, it has been observed that some regions will localize to the lamina in the first differentiation but won’t become repressed until the second differentiation!

#### **Body Guard Hypothesis**

The body guard hypothesis was proposed in 1975 by Hsu TC. It suggests that inactive DNA is localized to the periphery of the nucleus so that it can ’guard’ the important, active regions of DNA from foreign dangers like viruses or free radicals. Attempts to test the hypothesis by introducing artificial DNA damage have produced circumstantial results, and the question remains open. **Single Cell Experiments**

It is known that cells retain their original organization after mitosis, as shown by chromosome staining experiments. However, recent experiments have shown that there may be a large difference in organization between the parent and daughter cells. Certain global properties, like chromosome territories, are conserved,

361

6.047/6.878 Lecture 30: Chromatin Interactions

but organization at a finer detail may greatly differ. Single cell experimentation is an emerging technique that may be able to address this open question.

## **_FAQ_**

- **Q:** Has anyone tried increasing expression of a gene in the middle of a LAD? What happened?

- **A:** It’s unclear if there is a specific example of this, however several related studies have been conducted. Researchers have tried to ’tether’ a region of DNA to the nuclear lamina to see if it spontaneously becomes deactivated. However, the results were inconclusive as in half of the cases the region would become inactive and in the other half it wouldn’t! So far these types of manipulations haven’t yielded much, but it was found that if a protein-devoid segment of DNA was digested and mixed with highly purified lamina proteins, the bound fragments reveal a very similar pattern as the LADs. This tells us that lamina directly binds to DNA. However, this does seem to vary between species.

## **22.9 Further Reading**

## **22.10 Available Tools and Techniques**

## **22.11 What Have We Learned?**

362

CHAPTER

## **TWENTYTHREE**

INTRODUCTION TO STEADY STATE METABOLIC MODELING

Guest Lecture by James Galagan Scribed by Meriem Sefta (2011) Jake Shapiro, Andrew Shum, and Ashutosh Singhal (1910) Molly Ford Dacus and Anand Oza (1909) Christopher Garay (1908)

### **Figures**

|23.1 The process leading to and including the citric acid cycle. . . . . . . . . . . . . . . . .|. .<br>363|
|---|---|
|23.2 Adding constraints to extreme pathways.<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>366|
|23.3 Maximizing two functions with linear programming.<br>. . . . . . . . . . . . . . . . . . .|. .<br>367|
|23.4 Removing a reaction is the same as removing a gene from the stoichiometric matrix. .|. .<br>368|
|23.5 Constraining the feasible solution space may create a new optimal flux.<br>. . . . . . . .|. .<br>369|
|23.6 Model of Coljin et. al [3] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>374|
|23.7 Basic flow in predicting state of a metabolic system under varing drug treatments. . .|. .<br>375|
|23.8 Applying expression data set allows constraining of cone shape. . . . . . . . . . . . . .|. .<br>375|
|23.9 Results of nutrient source prediction experiment. . . . . . . . . . . . . . . . . . . . . .|. .<br>376|


## **23.1 Introduction**

Metabolic modeling allows us to use mathematical models to represent complex biological systems. This lecture discusses the role of modeling the steady state of biological systems in understanding the metabolic capabilities of organisms. We also briefly discuss how well steady state models are able to replicate in-vitro experiments.

363

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling

### **23.1.1 What is Metabolism?**

According to Matthews and van Holde, metabolism is the totality of all chemical reactions that occur in living matter. This includes catabolic reactions, which are reactions that lead to the breakdown of molecules into smaller components, and anabolic reactions, which are responsible for the creation of more complex molecules (e.g. proteins, lipids, carbohydrates, and nucleic acids) from smaller components. These reactions are responsible for the release of energy from chemical bonds and the storage of this energy. Metabolic reactions are also responsible for the transduction and transmission of information (for example, via the generation of cGMP as a secondary messenger or mRNA as a substrate for protein translation).

### **23.1.2 Why Model Metabolism?**

An important application of metabolic modeling is in the prediction of drug effects. An important subject of modeling is the organism Mycobacterium tuberculosis [15]. The disruption of the mycolic acid synthesis pathways of this organism can help control TB infection. Computational modeling gives us a platform for identifying the best drug targets in this system. Gene knockout studies in _Escherichia coli_ have allowed scientists to determine which genes and gene combinations affect the growth of this important model organism [6]. Both agreements and disagreements between models and experimental data can help us assess our knowledge of biological systems and help us improve our predictions about metabolic capabilities. In the next lecture, we will learn the importance of incorporating expression data into metabolic models. In addition, a variety of infectious disease processes involve metabolic changes at the microbial level.

## **23.2 Model Building**

An overarching goal of metabolic modeling is the ability to take a schematic representation of a pathway and change that it into a mathematical formula modeling the pathway. For example, converting the following pathway into a mathematical model would be incredible useful.

### **23.2.1 Chemical Reactions**

In metabolic models, we are concerned with modeling chemical reactions that are catalyzed by enzymes. Enzymes work by acting on a transition state of the enzyme-substrate complex that lowers the activation energy of a chemical reaction. The diagram on slide 5 of page 1 of the lecture slides demonstrates this phenomenon. A typical rate equation (which describes the conversion of the substrates S of the enzyme reaction into its products P) can be described by a Michaelis-Menten rate law:


In this equation, V is the rate of the equation as a function of substrate concentration [S]. It is clear that the parameters _Km_ and _Vmax_ are necessary to characterize the equation.

The inclusion of multiple substrates, products, and regulatory relationships quickly increases the number of parameters necessary to characterize such equations. The figures on slides 1, 2, and 3 of page 2 of the lecture notes demonstrate the complexity of biochemical pathways. Kinetic modeling quickly becomes

364

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling


Figure 23.1: The process leading to and including the citric acid cycle.

© Pearson. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Matthews, C. K., et al. "Biochemistry." (2000).

infeasible: the necessary parameters are difficult to measure, and also vary across organisms [10]. Thus, we are interested in a modeling method that would allow us to use a small number of precisely determined parameters. To this end, we recall the basic machinery of stoichiometry from general chemistry. Consider the chemical equation _A_ +2 _B →_ 3 _C_ , which says that one unit of reactant A combines with 2 units of reactant B to form 3 units of reactant C. The rate of formation of the compound X is given by the time derivative of [X]. Note that C forms three times as fast as A. Therefore, due to the stoichiometry of the reaction, we see that the reaction rate (or reaction flux) is given by


This will be useful in the subsequent sections. We must now state the simplifying assumptions that make our model tractable.

### **23.2.2 Steady-State Assumption**

The steady state assumption assumes that there is no accumulation of any metabolite in the system. This allows us to represent reactions entirely in terms of their chemistry (i.e. the stoichiometric relationships between the components of the enzymatic reaction). Note that this does not imply the absence of flux

365

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling

through any given reaction. Rather, steady-state actually implies two assumptions that are critical to simplify metabolic modeling. The first is that the internal metabolite concentrations are constant, and the second is that fluxes, ie input and output fluxes, are also constant.

An analogy is a series of waterfalls that contribute water to pools. As the water falls from one pool to another, the water levels do not change even though water continues to flow (see page 2 slide 5). This framework prevents us from being hindered by the overly complicated transient kinetics that can result from perturbations of the system. Since we are usually interested in long-term metabolic capabilities (functions on a scale longer than milliseconds or seconds), the steady state dynamics may give us all the information that we need.

The steady-state assumption makes the ability to generalize across species and reuse conserved pathways in models much more feasible. Reaction stochiometries are often conserved across species, since they involve only conservation of mass. The biology of enzyme catalysis, and the parameters that characterize it, are not similarly conserved. These include species-dependent parameters such as the activation energy of a reaction, substrate affinity of an enzyme, and the rate constants for various reactions. However, none of these are required for steady-state modeling.

It is also of interest to note that, since time constants for metabolic reactions are usually in the order of milliseconds, most measurement technologies used today are not able to capture these extremely fast dynamics. This is the case of metabolomics mass spectrometry based measurements for example. In this method, the amounts of all the internal metabolites in a system are measured at a given point in time, but measurements can be taken at best every hour. In the majority of circumstances, all that is ever measured is steady state.

### **23.2.3 Reconstructing Metabolic Pathways**

There are several databases that can provide the information necessary to reconstruct metabolic pathways in silico. These databases allow reaction stoichiometry to be accessed using Enzyme Commission numbers. Reaction stochiometries are the same in all the organisms that utilize a given enzyme. Among the databases of interest are ExPASy [5], MetaCyc [16], and KEGG [14]. These databases often contain pathways organized by function that can be downloaded in SBML format, making pathway reconstruction very easy for wellcharacterized pathways.

## **23.3 Metabolic Flux Analysis**

Metabolic flux analysis (MFA) is a way of computing the distribution of reaction fluxes that is possible in a given metabolic network at steady state. We can place constraints on certain fluxes in order to limit the space described by the distribution of possible fluxes. In this section, we will develop a mathematical formulation for MFA. Once again, this analysis is independent of the particular biology of the system; rather, it will only depend on the (universal) stoichiometries of the reactions in question.

### **23.3.1 Mathematical Representation**

Consider a system with _m_ metabolites and _n_ reactions. Let _xi_ be the concentration of substrate i, so that the rate of change of the substrate concentration is given by the time derivative of _xi_ . Let _x_ be the column vector

366

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling

(with _m_ components) with elements _xi_ . For simplicity, we consider a system with m = 4 metabolites A, B, C, and D. This system will consist of many reactions between these metabolites, resulting in a complicated balance between these compounds.

Once again, consider the simple reaction _A_ + 2 _B →_ 3 _C_ . We can represent this reaction in vector form as (-1 -2 3 0). Note that the first two metabolites (A and B) have negative signs, since they are consumed in the reaction. Moreover, the elements of the vector are determined by the stoichiometry of the reaction, as in Section 2.1. We repeat this procedure for each reaction in the system. These vectors become the columns of the stoichiometric matrix S. If the system has m metabolites and n reactions, S will be a m n matrix. Therefore, if we define v to be the n-component column vector of fluxes in each reaction, the vector _Sv_ describes the rate of change of the concentration of each metabolite. Mathematically, this can be represented as the fundamental equation of metabolic flux analysis:

> _<u>dx</u>_ = _Sv dt_

The matrix S is an extraordinarily powerful data structure that can represent a variety of possible scenarios in biological systems. For example, if two columns c and d of S have the property that _c_ = _d_ , the columns represent a reversible reaction. Moreover, if a column has the property that only one component is nonzero, it represents in exchange reaction, in which there is a flux into (or from) a supposedly infinite sink (or source), depending on the sign of the nonzero component.

We now impose the steady state assumption, which says that the left size of the above equation is identically zero. Therefore, we need to find vectors v that satisfy the criterion _Sv_ = 0. Solutions to this equation will determine feasible fluxes for this system.

### **23.3.2 Null Space of S**

The feasible flux space of the reactions in the model system is defined by the null space of S, as seen above. Recall from elementary linear algebra that the null space of a matrix is a vector space; that is, given two vectors y and z in the nullspace, the vector _ay_ + _bz_ (for real numbers a, b) is also in the null space. Since the null space is a vector space, there exists a basis _bi_ , a set of vectors that is linearly independent and spans the null space. The basis has the property that for any flux _v_ in the null space of _S_ , there exist real numbers _αi_ such that


How do we find a basis for the null space of a matrix? A useful tool is the singular value decomposition (SVD) [4]. The singular value decomposition of a matrix S is defined as a representation _S_ = _UEV ∗_ , where _U_ is a unitary matrix of size _m_ , _V_ is a unitary matrix of size _n_ , and _E_ is a _mxn_ diagonal matri _x_ , with the (necessarily positive) singular values of S in descending order. (Recall that a unitary matrix is a matrix with orthonormal columns and rows, i.e. _U ∗ U_ = _UU ∗_ = _I_ the identity matrix). It can be shown that any matrix has an SVD. Note that the SVD can be rearranged into the equation _Sv_ = _σu_ , where _u_ and _v_ are columns of the matrices U and V and is a singular value. Therefore, if _σ_ = 0, v belongs to the null space of S. Indeed, the columns of V that correspond to the zero singular values form an orthonormal basis for the null space of S. In this manner, the SVD allows us to completely characterize the possible fluxes for the system.

367

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling

### **23.3.3 Constraining the Flux Space**

The first constraint mentioned above is that all steady-state flux vectors must be in the null space. Also negative fluxes are not thermodynamically possible. Therefore a fundamental constraint is that all fluxes must be positive. (Within this framework we represent reversible reactions as separate reactions in the stoichiometric matrix S having two unidirectional fluxes.)

These two key constraints form a system that can be solved by convex analysis. The solution region can be described by a unique set of Extreme Pathways. In this region, steady state flux vectors v can be described as a positive linear combination of these extreme pathways. The Extreme Pathways, represented in slide 25 as vectors _bi_ , circumscribe a convex flux cone. Each dimension is a rate for some reaction. In slide 25, the z-dimension represents the rate of reaction for _v_ 3 . We can recognize that at any point in time, the organism is living at a point in the flux cone, i.e. is demonstrating one particular flux distribution. Every point in the flux cone can be described by a possible steady state flux vector, while points outside the cone cannot.

One problem is that the flux cone goes out to infinity, while infinite fluxes are not physically possible. Therefore an additional constraint is capping the flux cone by determining the maximum fluxes of any of our reactions (these values correspond to our _Vmax_ parameters). Since many metabolic reactions are interior to the cell, there is no need to set a cap for every flux. These caps can be determined experimentally by measuring maximal fluxes, or calculated using mathematical tools such as diffusivity rules.

We can also add input and output fluxes that represent transport into and out of our cells ( _Vin_ and _Vout_ ). These are often much easier to measure than internal fluxes and can thus serve to help us to generate a more biologically relevant flux space. An example of an algorithm for solving this problem is the simplex algorithm [1]. Slides 24-27 demonstrate how constraints on the fluxes change the geometry of the flux cone. In reality, we are dealing with problems in higher dimensional spaces.


<!-- Start of picture text -->
© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

Figure 23.2: Adding constraints to extreme pathways.

### **23.3.4 Linear Programming**

Linear programming is a generic solution that is capable of solving optimization problems given linear constraints. These can be represented in a few different forms.

**Canonical Form** :

368

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling

- Maximize: _c_<sup>_T_</sup> _x_

- Subject to: _Ax ≤ b_

**Standard Form** :

- Maximize Σ _ci ∗ xi_

- Subject to _aijXi ≤ biforalli, j_

- Non-negativity constraint: _Xi ≥_ 0

A concise and clear introduction to Linear Programming is available here: `http://www.purplemath. com/modules/linprog.htm` The constraints described throughout section 3 give us the linear programming problem described in lecture. Linear programming can be considered a first approximation and is a classic problem in optimization. In order to try and narrow down our feasible flux, we assume that there exists a fitness function which is a linear combination of any number of the fluxes in the system. Linear programming (or linear optimization) involves maximizing or minimizing a linear function over a convex polyhedron specified by linear and non-negativity constraints.


Figure 23.3: Maximizing two functions with linear programming.

We solve this problem by identifying the flux distribution that maximizes an objective function:

The key point in linear programming is that our solutions lie at the boundaries of the permissible flux space and can be on points, edges, or both. By definition however, an optimal solution (if one exists) will lie at a point of the permissible flux space. This concept is demonstrated on slide 30. In that slide, _A_ is the stoichiometric matrix, _x_ is the vector of fluxes, and _b_ is a vector of maximal permissible fluxes.

Linear programs, when solved by hand, are generally done by the Simplex method. The simplex method sets up the problem in a matrix and performs a series of pivots, based on the basic variables of the problem statement. In worst case, however, this can run in exponential time. Luckily, if a computer is available, two other algorithms are available. The ellipsoid algorithm and Interior Point methods are both capable of solving any linear program in polynomial time. It is interesting to note, that many seemingly difficult problems can be modeled as linear programs and solved efficiently (or as efficiently as a generic solution can solve a specific problem).

In microbes such as E. coli, this objective function is often a combination of fluxes that contributes to biomass, as seen in slide 31. However, this function need not be completely biologically meaningful.

369

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling

For example, we might simulate the maximization of mycolates in _M. tuberculosis_ , even though this isnt happening biologically. It would give us meaningful predictions about what perturbations could be performed in vitro that would perturb mycolate synthesis even in the absence of the maximization of the production of those metabolites.Flux balance analysis (FBA) was pioneered by Palssons group at UCSD and has since been applied to E. coli, M. tuberculosis, and the human red blood cell [ **?** ].

## **23.4 Applications**

### **23.4.1** **_In Silico_ Detection Analysis**

With the availability of such a powerful tool like FBA, more questions naturally arise. For example, are we able to predict gene knockout phenotype based on their simulated effects on metabolism? Also, why would we try to do this, even though other methods, like protein interaction map connective, exist? Such analysis is actually necessary, since other methods do not take into direct consideration the metabolic flux or other specific metabolic conditions.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 23.4: Removing a reaction is the same as removing a gene from the stoichiometric matrix.

Knocking out a gene in an experiment is simply modeled by removing one of the columns (reactions) from the stochiometric matrix. (A question during class clarified that a single gene can knock out multiple columns/reactions.) Thereby, these knockout mutations will further constrain the feasible solution space by removing fluxes and their related extreme pathways. If the original optimal flux was outside is outside the new space, then new optimal flux is created. Thus the FBA analysis will produce different solutions. The solution is a maximal growth rate, which may be confirmed or disproven experimentally. The growth rate at the new solution provides a measure of the knockout phenotype. If these gene knockouts are in fact lethal, then the optimal solution will be a growth rate of zero.

Studies by Edwards, Palsson (1900) explore knockout phenotype prediction use to predict metabolic changes in response to knocking out enzymes in E. coli, a prokaryote [ **?** ]. In other words, an in silico metabolic model of E.coli was constructed to simulate mutations affecting the glycolysis, pentose phosphate, TCA, and electron transport pathways (436 metabolites and 719 reactions included). For each specific condition, the optimal growth of mutants was compared to non-mutants. The in vivo and in silico results were then compared, with 86% agreement. The errors in the model indicate an underdeveloped model (lack of knowledge). The authors discuss 7 errors not modeled by FBA, including mutants inhibiting stable RNA synthesis and producing toxic intermediates.

370

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 23.5: Constraining the feasible solution space may create a new optimal flux.

### **23.4.2 Quantitative Flux** **_In Silico_ Model Predictions**

Can models quantitatively predict fluxes, growth rate? We demonstrate the ability of FBA to give quantitative predictions about growth rate and reaction fluxes given different envi- ronmental conditions. More specifically, prediction refers to externally measurable fluxes as a function of controlled uptake rates and environmental conditions. Since FBA maximizes an objective function, resulting in a specific value for this function, we should in theory be able to extract quantitative information from the model.

An early example by Edwards, Ibarra, and Palsson (1901), predicted the growth rate of E. coli in culture given a range of fixed uptake rates of oxygen and two carbon sources (acetate and succinate), which they could control in a batch reactor [6]. They assumed that E. coli cells adjust their metabolism to maximize growth (using a growth objective function) under given environmental conditions and used FBA to model the metabolic pathways in the bacterium. The input to this particular model is acetate and oxygen, which is labeled as _VIN_ .

The controlled uptake rates fixed the values of the oxygen and acetate/succinate input fluxes into the network, but the other fluxes were calculated to maximize the value of the growth objective.

The growth rate is still treated as the solution to the FBA analysis. In sum, optimal growth rate is predicted as a function of uptake constraints on oxygen versus acetate and oxygen versus succinate. The basic model is a predictive line and may be confirmed in a bioreactor experimentally by measuring the uptake and growth from batch reactors (note: experimental uptake was not constrained, only measured).

This model by Palsson was the first good proof of principle in silico model. The authors quantitative growth rate predictions under the different conditions matched very closely to the experimentally observed growth rates, implying that E. coli do have a metabolic network that is designed to maximize growth. It had good true positive and true negative rates. The agreement between the predictions and experimental results is very impressive for a model that does not include any kinetic information, only stoichiometry. Prof. Galagan cautioned, however, that it is often difficult to know what good agreement is, because we dont know the significance of the size of the residuals. The organism was grown on a number of different nutrients. Therefore, the investigators were able to predict condition specific growth. Keep in mind this worked, since only certain genes are necessary for some nutrients, like fbp for gluconeogenesis. Therefore, knocking out fbp will only be lethal when there is no glucose in the environment, a specific condition that resulted in a growth solution when analyzed by FBA.

371

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling

### **23.4.3 Quasi Steady State Modeling (QSSM)**

We’re now able describe how to use FBA to predict time-dependent changes in growth rates and metabolite concentrations using quasi steady state modeling. The previous example used FBA to make quantitative growth predictions under specific environmental conditions (point predictions). Now, after growth and uptake fluxes, we move on to another assumption and type of model.

Can we use a steady state model of metabolism to predict the time-dependent changes in the cell or environments? We do have to make a number of quasi steady state assumptions (QSSA):

1. The metabolism adjusts to the environmental/cellular changes more rapidly than the changes themselves

2. The cellular and environmental concentrations are dynamic, but metabolism operates on the condition that the concentration is static at each time point (steady state model).

Is it possible to use QSSM to predict metabolic dynamics over time? For example, if there is less acetate being taken in on a per cell basis as the culture grows, then the growth rate must slow. But now, QSSA assumptions are applied. That is, in effect, at any given point in time, the organism is in steady state.

What values does one get as a solution to the FBA problem? There are fluxes the growth rate. We are predicting rate and fluxes (solution) where VIN/OUT included. Up to now we assumed that the input and output are infinite sinks and sources. To model substrate/growth dynamics, the analysis is performed a bit differently from prior quantitative flux analysis. We first divide time into slices _δt_ . At each time point _t_ , we use FBA to predict cellular substrate uptake ( _Su_ ) and growth ( _g_ ) during interval _δt_ . The QSSA means these predictions are constant over _δt_ . Then we integrate to get the biomass (B) and substrate concentration (Sc) at the next time point _t_ + _δt_ . Therefore, the new VIN is calculated each time based on points _δt_ in-between time. Thus we can predict the growth rate and glucose and acetate uptake (nutrients available in the environment). The four step analysis is:

1. The concentration at time t is given by the substrate concentration from the last step plus any additional substrate provided to the cell culture by an inflow, such as in a fed batch.

2. The substrate concentration is scaled for time and biomass (X) to determine the substrate availability to the cells. This can exceed the maximum uptake rate of the cells or be less than that number.

3. Use the flux balance model to evaluate the actual substrate uptake rate, which may be more or less than the substrate available as determined by step 2.

4. The concentration for the next time step is then calculated by integrating the standard differential equations:


The additional work by Varma et al. (1994) specifies the glucose uptake rate a priori [17]. The model simulations work to predict time-dependent changes in growth, oxygen uptake, and acetate secretion. This

372

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling

converse model plots uptake rates versus growth, while still achieving comparable results in vivo and in silico. The researchers used quasi steady state modeling to predict the time-dependent profiles of cell growth and metabolite concentrations in batch cultures of _E. coli_ that had either a limited initial supply of glucose (left) or a slow continuous glucose supply (right diagram). A great fit is evident.

The diagrams above show the results of the model predictions (solid lines) and compare it to the experimental results (individual points). Thus, in _E. coli_ , quasi steady state predictions are impressively accurate even with a model that does not account for any changes in enzyme expression levels over time. However, this model would not be adequate to describe behavior that is known to involve gene regulation. For example, if the cells had been grown on half-glucose/half-lactose medium, the model would not have been able to predict the switch in consumption from one carbon source to another. (This does occur experimentally when _E. coli_ activates alternate carbon utilization pathways only in the absence of glucose.)

### **23.4.4 Regulation via Boolean Logic**

There is a number of levels of regulation through which metabolic flux is controlled at the metabolite, transcriptional, translational, post-translational levels. FBA associated errors may be explained by incorporation of gene regulatory information into the models. One way to do this is Boolean logic. The following table describes if genes for associated enzymes are on or off in presence of certain nutrients (an example of incorporating _E. coli_ preferences mentioned above):

|ON|ON|
|---|---|
|no glucose(0)|acetate present(1)|
|ON|OFF|
|glucose present(1)|acetate present(1)|


Therefore, one may think that the next step to take is to incorporate this fact into the models. For example, if we have glucose in the environment, the acetate processing related genes are off and therefore absent from the S matrix which now becomes dynamic as a result of incorporation of regulation into our model. In the end, our model is not quantitative. The basic regulation then describes that if one nutrientprocessing enzyme is on, the other is off. Basically it is a bunch of Boolean logic, based on presence of enzymes, metabolites, genes, etc. These Boolean style assumptions are then used at every small change in time dt to evaluate the growth rate, the fluxes, and such variables. Then, given the predicted fluxes, the _VIN_ ,the _VOUT_ , and the system states, one can use logic to turn genes off and on, effectively a _δS_ per _δt_ . We can start putting together all of the above analyses and come up with a general approach in metabolic modeling. We can tell that if glycolysis is on, then gluconeogenesis must be off.

The first attempt to include regulation in an FBA model was published by Covert, Schilling, and Palsson in 1901 [7]. The researchers incorporated a set of known transcriptional regulatory events into their analysis of a metabolic regulatory network by approximating gene regulation as a Boolean process. A reaction was said to occur or not depending on the presence of both the enzyme and the substrate(s): if either the enzyme that catalyzes the reaction (E) is not expressed or a substrate (A) is not available, the reaction flux will be zero:

rxn = IF (A) AND (E)

Similar Boolean logic determined whether enzymes were expressed or not, depending on the currently expressed genes and the current environmental conditions. For example, transcription of the enzyme (E) occurs only if the appropriate gene (G) is available for transcription and no repressor (B) is present:

373

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling

#### trans = IF (G) AND NOT (B)

The authors used these principles to design a Boolean network that inputs the current state of all relevant genes (on or off) and the current state of all metabolites (present or not present), and outputs a binary vector containing the new state of each of these genes and metabolites. The rules of the Boolean network were constructed based on experimentally determined cellular regulatory events. Treating reactions and enzyme/metabolite concentrations as binary variables does not allow for quantitative analysis, but this method can predict qualitative shifts in metabolic fluxes when merged with FBA. Whenever an enzyme is absent, the corresponding column is removed from the FBA reaction matrix, as was described above for knockout phenotype prediction. This leads to an iterative process:

1. Given the initial states of all genes and metabolites, calculate the new states using the Boolean network;

2. perform FBA with appropriate columns deleted from the matrix, based on the states of the enzymes, to determine the new metabolite concentrations;

3. repeat the Boolean network calculation with the new metabolite concentrations; etc. The above model is not quantitative, but rather a pure simulation of turning genes on and off at any particular time instant.

On a few metabolic reactions, there are rules about allowing organism to shift carbon sources (C1, C2).

An application of this method from the study by Covert et al.[7] was to simulate diauxic shift, a shift from metabolizing a preferred carbon source to another carbon source when the preferred source is not available. The modeled process includes two gene products, a regulatory protein RPc1, which senses (is activated by) Carbon 1, and a transport protein Tc2, which transports Carbon 2. If RPc1 is activated by Carbon 1, Tc2 will not be transcribed, since the cell preferentially uses Carbon 1 as a carbon source. If Carbon 1 is not available, the cell will switch to metabolic pathways based on Carbon 2 and will turn on expression of Tc2.

The Booleans can represent this information:

#### RPc1 = IF(Carbon1) Tc2 = IF NOT(RPc1)

Covert et al. found that this approach gave predictions about metabolism that matched results from experimentally induced diauxic shift. This diauxic shift is well modeled by the in silico analysis see above figure. In segment A, C1 is used up as a nutrient and there is growth. In segment B, there is no growth as C1 has run out and C2 processing enzymes are not yet made, since genes have not been turned on (or are in the process), thus the delay of constant amount of biomass. In segment C, enzymes for C2 turned on and the biomass increases as growth continues with a new nutrient source. Therefore, if there is no C1, C2 is used up. As C1 runs out, the organism shifts metabolic activity via genetic regulation and begins to take up C2. Regulation predicts diauxie, the use of C1 before C2. Without regulation, the system would grow on both C1 and C2 together to max biomass.

So far we have discussed using this combined FBA-Boolean network approach to model regulation at the transcriptional/translational level, and it will also work for other types of regulation. The main limitation is for slow forms of regulation, since this method assumes that regulatory steps are completed within a single time interval (because the Boolean calculation is done at each FBA time step and does not take into account previous states of the system). This is fine for any forms of regulation that act at least as fast as transcription/translation. For example, phosphorylation of enzymes (an enzyme activation process) is very fast and can be modeled by including the presence of a phosphorylase enzyme in the Boolean network.

374

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling

However, regulation that occurs over longer time scales, such as sequestration of mRNA, is not taken into account by this model. This approach also has a fundamental problem in that it does not allow actual experimental measurements of gene expression levels to be inputted at relevant time points.

We do not need our simulations to artificially predict whether certain genes are on or off. Microarray expression data allows us to determine which genes are being expressed, and this information can be incorporated into our models.

### **23.4.5 Coupling Gene Expression with Metabolism**

In practice, we do not need to artificially model gene levels, we can measure them. As discussed previousky, it is possible to measure the expressions levels of all the mRNAs in a given sample. Since mRNA expression data correlates with protein expression data, it would be extremely useful to incorporate it into the FBA. Usually, data from microarray experiments is clustered, and unknown genes are hypothesised to have function similar to the function of those known genes with which they cluster. This analysis can be faulty, however, as genes with similar actions may not always cluster together. Incorporating microarray expression data into FBA could allow an alternate method of interpretation of the data. Here arises a question, what is the relationship between gene level and flux through a reaction?

Say the reaction _A → B_ is catalyzed by an enzyme. If a lot of A present, increased expression of the gene for the enzyme causes increased reaction rate. Otherwise, increasing gene expression level will not increase reaction rate. However, the enzyme concentration can be treated as a constraint on the maximum possible flux, given that the substrate also has a reasonable physiological limit.

The next step, then, is to relate the mRNA expression level to the enzyme concentration. This is more difficult, since cells have a number of regulatory mechanisms to control protein concentrations independently of mRNA concentrations. For example, translated proteins may require an additional activation step (e.g. phosphorylation), each mRNA molecule may be translated into a variable number of proteins before it is degraded (e.g. by antisense RNAs), the rate of translation from mRNA into protein may be slower than the time intervals considered in each step of FBA, and the protein degradation rate may also be slow. Despite these complications, the mRNA expression levels from microarray experiments are usually taken as upper bounds on the possible enzyme concentrations at each measured time point. Given the above relationship between enzyme concentration and flux, this means that the mRNA expression levels are also upper bounds on the maximum possible fluxes through the reactions catalyzed by their encoded proteins. The validity of this assumption is still being debated, but it has already performed well in FBA analyses and is consistent with recent evidence that cells do control metabolic enzyme levels primarily by adjusting mRNA levels. (In 1907, Professor Galagan discussed a study by Zaslaver et al. (1904) that found that genes required in an amino acid biosynthesis pathway are transcribed sequentially as needed [2]). This is a particularly useful assumption for including microarray expression data in FBA, since FBA makes use of maximum flux values to constrain the flux balance cone.

Colijn et al. address the question of algorithmic integration of expression data and metabolic networks [3]. They apply FBA to model the maximum flux through each reaction in a metabolic network. For example, if microarray data is available from an organism growing on glucose and from an organism growing on acetate, significant regulatory differences will likely be observed between the two datasets. _Vmax_ tells us what the maximum we can reach. Microarray detects the level of transcripts, and it gives an upper boundary of _Vmax_ .

In addition to predicting metabolic pathways under different environmental conditions, FBA and microarray experiments can be combined to predict the state of a metabolic system under varying drug treatments. For example, several TB drugs target mycolic acid biosynthesis. Mycolic acid is a major cell wall constituent. In a 1904 paper by Boshoff et al., researchers tested 75 drugs, drug combinations, and growth conditions to

375

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling


Figure 23.6: Model of Coljin et. al [3]

Courtesy of the authors. License: CC BY.

Source: Colijn, Caroline, et al. "Interpreting Expression Data with Metabolic Flux Models: Predicting Mycobacterium Tuberculosis Mycolic acid Production." _PLoS Computational Biology_ 5, no. 8 (2009): e1000489.

see what effect different treatments had on mycolic acid synthesis [9]. In 1905, Raman et al. published an FBA model of mycolic acid biosynthesis, consisting of 197 metabolites and 219 reactions [13].

The basic flow of the prediction was to take a control expression value and a treatment expression value for a particular set of genes, then feed this information into the FBA and measure the final effect on the treatment on the production of mycolic acid. To examine predicted inhibitors and enhancers, they examined significance, which examines whether the effect is due to noise, and specificity, which examines whether the effect is due to mycolic acid or overall supression/enhancement of metabolism. The results were fairly encouraging. Several known mycolic acid inhibitors were identified by the FBA. Interesting results were also found among drugs not specifically known to inhibit mycolic acid synthesis. 4 novel inhibitors and 2 novel enhancers of mycolic acid synthesis were predicted. One particular drug, Triclosan, appears to be an enhancer according to the FBA model, whereas it is currently known as an inhibitor. Further study of this particular drug would be interesting. Experimental testing and validation are currently in progress.

Clustering may also be ineffective in identifying function of various treatments. Predicted inhibitors, and predicted enhancers of mycolic acid synthesis are not clustered together. In addition, no labeled training set is required for FBA-based algorithmic classification, whereas it is necessary for supervised clustering algorithms.

### **23.4.6 Predicting Nutrient Source**

Now, we get the idea of predicting the nutrient source that an organism may be using in an environment, by looking at expression data and looking for associated nutrient processing gene expression. This is easier, since we cant go into the environment and measure all chemical levels, but we can get expression data rather easily. That is, we try to predict a nutrient source through predictions of metabolic state from expression data, based on the assumption that organisms are likely to adjust metabolic state to available nutrients. The nutrients may then be ranked by how well they match the metabolic states.

The other way around could work too. Can I predict a nutrient given a state? Such predictions could be useful for determining the nutrient requirements of an organism with an unknown natural environment, or for determining how an organism changes its environment. (TB, for example, is able to live within the environment of a macrophage phagolysosome, presumably by altering the environmental conditions in the

376

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling


Figure 23.7: Basic flow in predicting state of a metabolic system under varing drug treatments phagolysosome and preventing its maturation.)

Courtesy of the authors. License: CC BY.

Source: Colijn, Caroline, et al. "Interpreting Expression Data with Metabolic Flux Models: Predicting Mycobacterium Tuberculosis Mycolic Acid Production." _PLoS Computational Biology_ 5, no. 8 (2009): e1000489.

We can use FBA to define a space of possible metabolic states and choose one. The basic steps are to:

- Start with max flux cone (representing best growth with all nutrients available in environment). Find optimal flux for each nutrient.

- Apply expression data set (still not knowing nutrient). This will allow you to constrain the cone shape and figure out the nutrient, which is represented as one with the closest distance to optimal solution.


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 23.8: Applying expression data set allows constraining of cone shape.

In Figure 8, you may see that the first cone has a number of optimals, so the real nutrient is unknown. However, after expression data is applied, the cone is reshaped. It has only one optimal, which is still in feasible space and thereby must be that nutrient you are looking for.

As before, the measured expression levels provide constraints on the reaction fluxes, altering the shape

377

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling

of the flux-balance cone (now the expression-constrained flux balance cone). FBA can be used to determine the optimal set of fluxes that maximize growth within these expression constraints, and this set of fluxes can be compared to experimentally-determined optimal growth patterns under each environmental condition of interest. The difference between the calculated state of the organism and the optimal state under each condition is a measure of how sub-optimal the current metabolic state of the organism would be if it were in fact growing under that condition.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Figure 23.9: Results of nutrient source prediction experiment.

Expression data from growth and metabolism may then be applied to predict the carbon source being used. For example, consider E. coli nutrient product. We can simulate this system for glucose versus acetate. The color indicates the distance from the constrained flux cone to the optimal flux solution for that nutrient combo (same procedure described above). Then, multiple nutrients may be ranked, prioritized according to expression data. Unpublished data from Desmond Lun and Aaron Brandes provide an example of this approach.

They used FBA to predict which nutrient source E. coli cultures were growing on, based on gene expression data. They compared the known optimal fluxes (the optimal point in flux space) for each nutrient condition to the allowed optimal flux values within the expression-constrained flux-balance cone. Those nutrient conditions with optimal fluxes that remained within (or closest to) the expression-constrained cone were the most likely possibilities for the actual environment of the culture.

Results of the experiment are shown in Figure 9, where each square in the results matrices is colored based on the distance between the optimal fluxes for that nutrient condition and the calculated optimal fluxes based on the expression data. Red values indicate large distances from the expression-constrained flux cone and blue values indicate short distances from the cone. In the glucose-acetate experiments, for example, the results of the experiment on the left indicate that low acetate conditions are the most likely (and glucose was the nutrient in the culture) and the results of the experiment on the right indicate that low glucose/medium acetate conditions are the most likely (and acetate was the nutrient in the culture). When 6 possible nutrients were considered, the model always predicted the correct one, and when 18 possible nutrients were considered, the correct one was always one of the top 4 ranking predictions. These results suggest that it is possible to use expression data and FBA modeling to predict environmental conditions from information about the metabolic state of an organism.

This is important because TB uses fatty acids in macrophages in immune systems. We do not know which ones exactly are utilized. We can figure out what the TB sees in its environment as a food source and proliferation factor by analyzing what related nutrient processing genes are turned on at growth phases and such. Thereby we can figure out the nutrients it needs to grow, allowing for a potential way to kill it off by not supplying such nutrients or knocking out those particular genes.

It is easier to get expression data to see flux activity than see whats being used up in the environment by

378

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling

analyzing the chemistry on such a tiny level. Also, we might not be able to grow some bacteria in lab, but we can solve the problem by getting the expression data from the bacteria growing in a natural environment and then seeing what it is using to grow. Then, we can add it to the laboratory medium to grow the bacteria successfully.

## **23.5 Current Research Directions**

## **23.6 Further Reading**

- Becker, S. A. and B. O. Palsson (1908). Context-Specific Metabolic Networks Are Consistent with Experiments. PLoS Computational Biology 4(5): e1000082.

   - If gene expression lower than some threshold, turn the gene off in the model.

- Shlomi, T., M. N. Cabili, et al. (1908). Network-based prediction of human tissue-specific metabolism. Nat Biotech 26(9): 1003-1010.

   - Nested optimization problem.

   - First, standard FBA

   - Second, maximize the number of enzymes whose predicted flux activity is _consistent with their measured expression level_

## **23.7 Tools and Techniques**

- Kegg

- BioCyc

- Pathway Explorer ( `pathwayexplorer.genome.tugraz.at` )

- Palssons group at UCSD ( `http://gcrg.ucsd.edu/` )

- `www.systems-biology.org`

- Biomodels database ( `www.ebi.ac.uk/biomodels/` )

- JWS Model Database ( `jjj.biochem.sun.ac.za/database/index.html` )

## **23.8 What Have We Learned?**

## **Bibliography**

[1]

- [2] Zaslaver A, Mayo AE, Rosenberg R, Bashkin P, Sberro H, Tsalyuk M, Surette MG, and Alon U. Justin-time transcription program in metabolic pathways. _Nat. Gen_ , 36:486–491, 2004.

379

6.047/6.878 Lecture 19: Introduction to Steady State Metabolic Modeling

- [3] Caroline Coljin. Interpreting expression data with metabolic flux models: Predicting mycobacterium tuberculosis mycolic acid production. _PLoS Computational Biology_ , 5(8), Aug 2009.

- [4] Price N. D., Reed J. L., Papin J.A, Famili I., and Palsson B.O. Analysis of metabolic capabilities using singular value decomposition of extreme pathway matrices. _Biophys J._ , 84(2):794–804, Feb 2003.

- [5] Gasteiger E., Gattiker A., Hoogland C. andIvanyi I., Appel R.D., , and Bairoch A. Expasy: The proteomics server for in-depth protein knowledge and analysis. _Nucleic Acids Res_ , 31(13):3784–3788.

- [6] J.S. Edwards, R. U. Ibarra, and B.O. Palsson. In silico predictions of e coli metabolic capabilities are consis ent with experimental data. _Nat Biotechnology_ , 19:125–130, 2001.

- [7] Covert M et al. Regulation of gene expression in flux balance models of metabolism. _Journal of Theoretical Biology_ , 213:73–88, Nov 2001.

- [8] J. Forster, I. Famili, B.O. Palsson, and J. Nielsen. Large-scale evaluation of in silico gene deletions in saccharomyces cerevisiae. _OMICS_ , 7(2):193–202, 2003. PMID: 14506848.

- [9] Boshoff H.I., Myers T.G., Copp B.R., McNeil M.R., Wilson M.A., and Bary C.E. The transcriptional response of mycobacterium tuberculosis to inhibitors of metabolism: novel insights into drug mechanisms of action. _J Biol Chem_ , 279:40174–40184, Sep 2004.

- [10] Holmberg. On the practical identifiability of microbial-growth models incorporating michaelis-menten type nonlinearities. _Mathematical Biosciences_ , 62(1):23–43, 1982.

- [11] Edwards J.S. and Palsson B.O. volume 97, pages 5528–5533. Proceedings of the National Academy of Sciences of the United States of America, May 2000. PMC25862.

- [12] Edwards J.S., Covert M., , and Palsson B. Metabolic modeling of microbes: the flux balance approach. _Environmental Microbiology_ , 4(3):133–140, 2002.

- [13] Raman Karthik, Preethi Rajagopalan, and Nagasuma Chandra. Flux balance analysis of mycolic acid pathway: Targets for anti-tubercular drugs. _PLoS Computational Biology_ , 1, Oct 2005.

- [14] Kanehisa M., Goto S., Kawashima S., and Nakaya. From genomics to chemical genomics: new developments in kegg. _Nucleic Acids Res._ , 34, 2006.

- [15] Jamshidi N. and Palsson B. Investigating the metabolic capabilities of mycobacterium tuberculosis h37rv using the in silico strain inj661 and proposing alternative drug targets. _BMC Systems Biology_ , 26, 2007.

- [16] Caspi R., Foerster H., Fulcher C.A., Kaipa P., Krummenacker M., Latendresse M., Paley S., Rhee S.Y., Shearer A.G., Tissier C., Walk T.C. ZhangP., and Karp P. The metacyc database of metabolic pathways and enzymes and the biocyc collection of pathway/genome databases. _Nucleic Acids Res_ , 36(Suppl), 2008.

- [17] A. Varma and B. O. Palsson. Stoichiometric flux balance models quantitatively predict growth and metabolic by-product secretion in wild-type escherichia coli w3110. _Applied and Environmental Microbiology_ , 60:3724–3731, Oct 1994.

380

CHAPTER

## **TWENTYFOUR**

THE ENCODE PROJECT: SYSTEMATIC EXPERIMENTATION AND INTEGRATIVE GENOMICS

### **Figures**

|24.1 Snapshot of ENCODE project experiment matrix.<br>. . . . . . . . . . . . . . . . . . . . . .|380|
|---|---|
|24.2 Overview of Chip-seq [3] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|381|
|24.3 ENCODE uniform Processing Pipeline . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|382|
|24.4 Shifting forward and reverse strand signals, Cross Correlation plot<br>. . . . . . . . . . . . .|382|
|24.5 IDR to assess reproducibility of CHIP-seq datasets. Scatter plots display signal scores of<br>peaks that overlap in each replicate pair. (A,B) results for high quality replicate. (C)<br>Estimated IDR for varying rank thresholds. [1] . . . . . . . . . . . . . . . . . . . . . . . .|383|


## **24.1 Introduction**

The human genome was sequenced in 2003, an important step in understanding the blueprint of life. However, before this information can be fully utilized, the location, identity, and function of all proteinencoding and non-protein-encoding genes must be determined. Moreover, the human genome has many other functional elements, ranging from promotors, regulatory sequences, and other factors that determine chromatin structure. These must also be determined to fully understand the human genome.

The ENCODE (Encyclopedia of DNA Elements) project aims to solve these problems by delineating all functional elements of the human genome . To accomplish this goal, a consortium was formed to guide the project. The consortium aimed to advance and develop technologies for annotating the human genome with higher accuracy, completeness, and cost-effectiveness,

381

6.047/6.878 Lecture 28: Systematic experimentation and integrative <u>genomics</u>

along with more standardization.They also aimed to develop a series of computational techniques to parse and analyze the data obtained.

To accomplish this goal, a pilot project was launched. The ENCODE pilot project aimed to study 1% of the human genome in depth, roughly from 2003 to 2007. From 2007 to 2012, the ENCODE project ramped up to annotate the entire genome. Finally, from 2012 onwards, the ENCODE project aims further increases in all dimensions: deeper sequencing, more assays, more transcription factors, etc.

This chapter will describe some of the experimental and computational techniques used in the ENCODE project.

## **24.2 Experimental Techniques**

The ENCODE project used a wide range of experimental techniques, ranging from RNA-seq, CAGE-seq, Exon Arrays, MAINE-seq, Chromatin ChIP-seq, DNase-seq, and many more.


Figure 24.1: Snapshot of ENCODE project experiment matrix.

© ENCODE Project. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

One of the most important techniques used was ChIP-seq (chromatin immunoprecipitation followed by sequencing). The first step in a ChIP experiment is to target DNA fragments associated with a specific protein. This is done by using an anti-body that targets the specific protein and is used to immunoprecipitate the DNA-protein complex. The final step is to assay the DNA. This will determine the sequences bound to the proteins.

ChIP-seq has several advantages over previous techniques (e.g. ChIP-chip). For example, ChIP-seq has single nucleotide resolution and its alignability increases with read length. However, ChIP-seq has several disadvantages. Sequencing errors tend to increase substantially near the end of reads. Also, with low number of reads, sensitivity and specificity tend to decrease when detecting enriched regions. Both of these problems arise when processing the data and many of the computational techniques seek to rectify this.

382

6.047/6.878 Lecture 28: Systematic experimentation and integrative <u>genomics</u>


Figure 24.2: Overview of Chip-seq [3]

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Park, Peter J. "ChIP–seq: Advantages and Challenges of a Maturing Technology." _Nature Reviews Genetics_ 10, no. 10 (2009): 669-80.

## **24.3 Computational Techniques**

This section will focus on techniques on processing raw data from the ENCODE project. Before ENCODE data can be analyzed (e.g. for motif discovery, co-association analysis, signal aggregation over elements, etc), the raw data must be processed.

Even before the data is processed, some quality control is applied. Quality control is needed for several reasons. Even without anti-bodies, reads are not uniformly-scattered. The biological reasons include nonuniform fragmentation of the genome, open chromatin regions fragmenting easier, and repetitive sequences over-collapsed in assembled genomes. The ENCODE project corrected for these biases in several ways. Portions of the DNA were removed before the ChIP step, removing large portions of unwanted data. Control experiments were also conducted without the use of anti-bodies. Finally, fragment input DNA sequence reads were used as a background.

Because of inherent noise in the ChIP-seq process, some reads will be of lower quality. Using a read quality metric, reads below a threshold were thrown out.

Shorter reads (and to a lesser extent, longer reads) can map to exactly one location (uniquely mapping), multiple locations (repetitive mapping), or no locations at all (unmappable) in the genome. There are many potential ways to deal with repetitive mapping, ranging from probabilistically spreading the read to use an EM approach. However, since the ENCODE project aims to be as correct as possible, it does not assign repetitive reads to any location.

383

6.047/6.878 Lecture 28: Systematic experimentation and integrative <u>genomics</u>


Figure 24.3: ENCODE uniform Processing Pipeline

© ENCODE Project. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

If a sample does not contain sufficient DNA and/or if it is over-sequenced, you will simply be repeatedly sequencing PCR duplicates of a restricted pool of distinct DNA fragments. This is known a low-complexity library and is not desirable. To solve this problem, a histogram with the number of duplicates is created and samples with a low non-redundant fraction (NRF) are thrown out.

ChIP-seq randomly sequences from one end of each fragment, so to determine which reads came from which segment, typically strand cross-correlation analysis is used [Fig. 04]. To accomplish this, the forward and and reverse strand signals are calculated. Then, they are sequentially shifted towards each other. At every step, the correlation is calculated. At the fragment length offset _f_ , the correlation peaks. _f_ is the length at which ChIP DNA is fragmented. Using further analysis, we can determine that we should have a high absolute cross-correlation at fragment length, and high fragment length cross-correlation relative to read-length cross-correlation. The RSC (Relative Strand Correlation) should be greater than 1.


Figure 24.4: Shifting forward and reverse strand signals, Cross Correlation plot


Once quality control is applied, the data is further processed to determine actual areas of enrichment. To accomplish this, the ENCODE project used a modified version of peak calling. There are many existing peak

384

6.047/6.878 Lecture 28: Systematic experimentation and integrative <u>genomics</u>

calling algorithms, but the ENCODE project used MACS and PeakSeq, as they are deterministic. However, it is not possible to set a uniform p-value or false discovery rate (FDR) constant. The FDR and p-value depends on ChIP and input sequencing depth, the binding ubiquity of the factor, and is highly unstable. Moreover, different tools require different values.

The ENCODE project uses replicates (of the same experiment) and combines the data to find more meaningful results. Simple solutions have major issues: taking the union of the peaks keeps garbage from both, the intersection is too stringent and throws away good peaks, and taking the sum of the data does not exploit the independence of the datasets. Instead, the ENCODE project uses the independent discovery rate (IDR). The key idea is that true peaks will be highly ranked in both replicates. Thus, to find significant peaks, the peaks are considered in rank order, until ranks are no longer correlated.


Courtesy of Cold Spring Harbor Laboratory Press. License: CC BY-NC. Source: Landt, Stephen G., et al. "ChIP-seq Guidelines and Practices of the ENCODE and ModENCODE Consortia." _Genome Research_ 22, no. 9 (2012): 1813-31.

Figure 24.5: IDR to assess reproducibility of CHIP-seq datasets. Scatter plots display signal scores of peaks that overlap in each replicate pair. (A,B) results for high quality replicate. (C) Estimated IDR for varying rank thresholds. [1]

The cutoff could be different for the two replicates and actual peaks included may differ between replicates. It is modeled as a Gaussian mixture model, which can be fit via an EM-like algorithm. Using IDR leads to higher consistence between peak callers. This is because FDR only relies on enrichment over input, IDR exploits replicates. Also, using sampling methods, if there is only one replicate, the IDR pipeline can still be used with pseudo-replicates.

## **24.4 Current Research Directions**

The ENCODE project is still ongoing. Using saturation techniques, we believe we only have discovered a maximum 50% of elements. This number is likely to be lower due to inaccessible cell types and other factors. Also, several cell types are extremely rare and difficult to access, so sequencing data from these cell types is another challenge.

In computational frontiers, the ENCODE project has produced an enormous amount of raw data. Similar to how the full sequence of the human genome unleashed a series of computational projects, the ENCODE data can be used for a variety of computational projects.

385

6.047/6.878 Lecture 28: Systematic experimentation and integrative <u>genomics</u>

## **24.5 Further Reading**

The Nature site with ENCODE papers is available at `http://www.nature.com/encode/` .

The official ENCODE portal is `http://encodeproject.org/ENCODE/` .

To browse ENCODE data, visit `http://encodeproject.org/cgi-bin/hgHubConnect` .

Data processing tools for ENCODE data are available at `http://encodeproject.org/ENCODE/analysis. html` .

## **24.6 Tools and Techniques**

ENCODE data mining, `http://genome.ucsc.edu/cgi-bin/hgTables?db=hg18&hgta_group=regulation& hgta_track=wgEncodeHudsonalphaChipSeq`

ENCODE data visualization, `http://genome.ucsc.edu/cgi-bin/hgTracks?hgS_doOtherUser=submit& hgS_otherUserName=Kate&hgS_otherUserSessionName=encodePortalSession`

Software and resources for rnalyzing ENCODE data, `http://genome.ucsc.edu/ENCODE/analysisTools. html`

Software tools used to create the ENCODE resource, `http://genome.ucsc.edu/ENCODE/encodeTools. html`

## **24.7 What Have We Learned?**

This chapter provides an overview the ENCODE project which aims to annotate the entire human genome. It collects DNA sequences using various experimental techniques such as CHIP-seq, RNA-seq, and CAGE-seq. After the data has been obtained it needs to be processed before attempting analysis. The data goes through a number of steps; quality control, peak calling, IDR processing, and blacklist filtering. Once the accuracy of the data has been ensured other analysis can be done in the form of motif discovery, co-association analysis, and signal aggregation over elements.

## **Bibliography**

> [1] S G Landt, G K Marinov, A Kundaje, P Kheradpour, F Pauli, S Batzoglou, B E Bernstein, P Bickel, J B Brown, P Cayting, Y Chen, G DeSalvo, C Epstein, K I Fisher-Aylor, G Euskirchen, M Gerstein, J Gertz, A J Hartemink, M M Hoffman, V R Iyer, Y L Jung, S Karmakar, M Kellis, P V Kharchenko, Q Li, T Liu, X S Liu, L Ma, A Milosavljevic, R M Myers, P J Park, M J Pazin, M D Perry, D Raha, T E Reddy, J Rozowsky, N Shoresh, A Sidow, M Slattery, J A Stamatoyannopoulos, M Y Tolstorukov,

386

6.047/6.878 Lecture 28: Systematic experimentation and integrative <u>genomics</u>

K P White, S Xi, P J Farnham, J D Lieb, B J Wold, and M Snyder. ChIP-seq guidelines and practices of the ENCODE and modENCODE consortia. _Genome Research_ , 22(9):1813–1831, 2012.

- [2] Philippe Lefran¸cois, Ghia M Euskirchen, Raymond K Auerbach, Joel Rozowsky, Theodore Gibson, Christopher M Yellman, Mark Gerstein, and Michael Snyder. Efficient yeast ChIP-Seq using multiplex short-read DNA sequencing. _BMC Genomics_ , 10(1):37, 2009.

- [3] P J Park. ChIP-seq: advantages and challenges of a maturing technology. _Nature reviews. Genetics_ , 10(10):669–680, October 2009.

387

6.047/6.878 Lecture 28: Systematic experimentation and integrative <u>genomics</u>

388

CHAPTER

**TWENTYFIVE**

PHARMACOGENOMICS

- **25.1 Introduction**

- **25.2 Current Research Directions**

- **25.3 Further Reading**

- **25.4 Tools and Techniques**

- **25.5 What Have We Learned?**

- **Bibliography**

389

6.047/6.878 Lecture 31: Pharmacogenomics

390

CHAPTER

## **TWENTYSIX**

## SYNTHETIC BIOLOGY

### **Figures**

|26.1 The layers of abstraction in robotics compared with those in biology (credit to Ron Weiss).|390|
|---|---|
|26.2 The repressilator genetic regulator network. . . . . . . . . . . . . . . . . . . . . . . . . . .|390|
|26.3 Fluorescence of a single cell with the repressilator circuit over a period of 10 hours. . . . .|390|
|26.4 Cost of synthesizing a base pair versus US dollar . . . . . . . . . . . . . . . . . . . . . . .|391|
|26.5 An example of a BioCompiler program and the process of actualizing it (credit to Ron Weiss|)392|
|26.6 An example of combining BioBrick Pieces taken from`http://2006.igem.org/wiki/index.`<br>`php/Standard_Assembly` . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|393|


## **26.1 Introduction**

A cell is like robot in that it needs to be able to sense it surroundings and internal state, perform computations and make judgments, and complete a task or function. The emerging discipline of synthetic biology aims to make control of biological entities such as cells and proteins similar to designing a robot. Synthetic biology combines technology, science, and engineering to construct biological devices and systems for useful purposes including solutions to world problems in health, energy, environment and, security.

Synthetic biology involves every level of biology, from DNA to tissues. Synthetic biologist aims to create layers of biological abstraction like those in digital computers in order to create biological circuits and programs efficiently. One of the major goals in synthetic biology is development of a standard and welldefined set of tools for building biological systems that allows the level of abstraction available to electrical engineers building complex circuits to be available to synthetic biologists.

Synthetic biology is a relatively new field. The size and complexity of synthetic genetic circuits has so far been small, on the order of six to eleven promoters. Synthetic genetic circuits remain small in total size

391

6.047/6.878 Lecture 32: Synthetic Biology

Figure 26.1: The layers of abstraction in robotics compared with those in biology (credit to Ron Weiss).


Courtesy of EMBO and Nature Publishing Group. Used with permission. Source: Andrianantoandro, Ernesto, et al. "Synthetic Biology: New Engineering Rules for an Emerging Discipline." _Molecular Systems Biology_ 2, no. 1 (2006).

(10<sup>3</sup> - 10<sup>5</sup> base pairs) compared to size of the typical genome in a mammal or other animal (10<sup>5</sup> - 10<sup>7</sup> base pairs) as well.

One of the first milestones in synthetic biology occurred in 2000 with the repressilator. The repressilator [2] is a synthetic genetic regulatory network which acts like an electrical oscillator system with fixed time periods. A green fluorescent protein was expressed within _E. coli_ and the fluorescence was measured over time. Three genes in a feedback loop were set up so that each gene repressed the next gene in the loop and was repressed by the previous gene.

Figure 26.2: The repressilator genetic regulator network.


Courtesy of Timreid on wikipedia; in the public domain.

Figure 26.3: Fluorescence of a single cell with the repressilator circuit over a period of 10 hours.


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Elowitz, Michael B., and Stanislas Leibler. "A Synthetic Oscillatory Network of Transcriptional Regulators." _Nature_ 403, no. 6767 (2000): 335-8.

The repressilator managed to produce periodic fluctuations in fluorescence. It served as one of the first triumphs in synthetic biology. Other achievements in the past decade include programmed bacterial population control, programmed pattern formation, artificial cell-cell communication in yeast, logic gate creation by chemical complementation with transcription factors, and the complete synthesis, cloning, and assembly of a bacterial genome.

392

6.047/6.878 Lecture 32: Synthetic Biology

## **26.2 Current Research Directions**

Encoding functionality in DNA is one way synthetic biologists program cells. As the price of sequencing and synthesis of DNA continues to decrease, coding DNA strands has become more feasible. In fact, the number of base pairs that can be synthesized per US$ has increased exponentially, akin to Moore’s Law.

Figure 26.4: Cost of synthesizing a base pair versus US dollar


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Carr, Peter A. and George M. Church. "Genome Engineering." N _ature Biotechnology_ 27, no. 12 (2009): 1151-62.

This has made the process of designing, building, and testing biological circuits much faster and cheaper. One of the major research areas in synthetic biology is the creation of fast, automated synthesis of DNA molecules and the creation of cells with the desired DNA sequence. The goal of creating a such a system is speeding up the design and debugging of making a biological system so that synthetic biological systems can be prototyped and tested in a quick, iterative process.

Synthetic biology also aims to develop abstract biological components that have standard and well-defined behavior like a part an electrical engineer might order from a catalogue. To accomplish this, the Registry of Standard Biological Parts ( `http://partsregistry.org` ) [4] was created in 2003 and currently contains over 7000 available parts for users. The research portion of creating such a registry includes the classification and description of biological parts. The goal is to find parts that have desirable characteristics such as:

**Orthogonality** Regulators should not interfere with each other. They should be independent.

**Composability** Regulators can be fused to give composite function.

**Connectivity** Regulators can be chained together to allow cascades and feedback.

**Homogeneity** Regulators should obey very similar physics. This allows for predictability and efficiency.

Synthetic biology is still developing, and research can still be done by people with little background in the field. The International Genetically Modified Machine (iGEM) Foundation ( `http://igem.org` ) [3] created the iGEM competition where undergraduate and high school students compete to design and build biological systems that operate within living cells. The student teams are given a kit of biological parts at the beginning of the summer and work at their own institutions to create biological system. Some interesting projects include:

393

6.047/6.878 Lecture 32: Synthetic Biology

- **Arsenic Biodetector** The aim was to develop a bacterial biosensor that responds to a range of arsenic concentrations and produces a change in pH that can be calibrated in relation to arsenic concentration. The team’s goal was to help many under-developed countries, in particular Bangladesh, to detect arsenic contamination in water. The proposed device was intended be more economical, portable and easier to use in comparison with other detectors.

- **BactoBlood** The UC Berkeley team worked to develop a cost-effective red blood cell substitute constructed from engineered E. coli bacteria. The system is designed to safely transport oxygen in the bloodstream without inducing sepsis, and to be stored for prolonged periods in a freeze-dried state.

- **E. Chromi** The Cambridge team project strived to facilitate biosensor design and construction. They designed and characterised two types of parts - Sensitivity Tuners and Colour Generators – E. coli engineered to produce different pigments in response to different concentrations of an inducer. The availability of these parts revolutionized the path of future biosensor design.

## **26.3 Further Reading**

## **26.4 Tools and Techniques**

Synthetic biology combines many fields, and the techniques used are not particular to synthetic biology. Much like the process of solving other engineering problems, the process of creating a useful biological system has designing, building, testing, and improving phases. Once a design or statement of the desired properties of a biological system are created, the problem becomes finding the proper biological components to build such a system.

BioCompiler [1] is a tool developed to allow the programming of biological circuits using a high-level programming language. One can write programs in a language similar to LISP and compile their program into a biological circuit. BioCompiler uses a process similar to that of a compiler for a programming language. It uses a human-written program as a high-level description of the genetic circuit, then generates a formal description of the program. From there, it looks up abstract genetic regulatory network pieces that can be combined to create the genetic circuit and goes through its library of DNA parts to find appropriate sequences to match the functionality of the abstract genetic regulatory network pieces. Assembly instructions can then be generated for creating cells with the appropriate genetic regulatory network.

Figure 26.5: An example of a BioCompiler program and the process of actualizing it (credit to Ron Weiss)

Flow chart removed due to copyright restrictions.

394

6.047/6.878 Lecture 32: Synthetic Biology

BioBrick standard biologic parts ( `biobricks.org` )are another tool used in synthetic biology. Similar to the parts in the Registry of Standard Biological Parts, BioBrick standard biological parts are DNA sequences of defined structure and function. Each BioBrick part is a DNA sequence held together in a circular plasmid. At either end of the BioBrick contains a known and well-defined sequence with restriction enzymes that can cut open the plasmid at known positions. This allows for the creation of larger BioBrick parts by chaining together smaller ones. Some competitors in the iGEM competition used BioBrick systems to develop an _E. coli_ line that produced scents such as banana or mint.

Figure 26.6: An example of combining BioBrick Pieces taken from `http://2006.igem.org/wiki/index. php/Standard_Assembly`


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

## **26.5 What Have We Learned?**

Synthetic biology is an emerging disciplines that aims to create useful biological systems to solve problems in energy, medicine, environment, and many more fields. Synthetic biologists attempt to use abstraction to enable them to build more complex systems from simpler ones in a similar way to how a software engineer or an electrical engineer would make a computer program or a complex circuit. The Registry of Standard Biological Parts and BioBrick standard biological parts aim to characterize and standardize biological pieces just as one would a transistor or logic gate to enable abstraction. Tools such as BioCompiler allow people to describe a genetic circuit using a high-level language and actually build a genetic circuit with the described functionality. Synthetic biology is still new, and research can be done by those unfamiliar with the field, as demonstrated by the iGEM competition.

## **Bibliography**

- [1] J. Beal and J. Bachrach. Cells are plausible targets for high-level spatial languages, 2008.

- [2] M. Elowitz and S. Leibler. A synthetic oscillatory network of transcriptional regulators. _Nature_ , 403:335– 338, 2000.

- [3] iGEM. igem: Synthetic biology based on standard parts, December 2012.

- [4] Registry of Standard Biological Parts. Registry of standard biological parts, December 2012.

395

6.047/6.878 Lecture 32: Synthetic Biology

396

---

[← Part III](06-part-iii.md) · [Up: contents](index.md) · [Part IV →](08-part-iv.md)

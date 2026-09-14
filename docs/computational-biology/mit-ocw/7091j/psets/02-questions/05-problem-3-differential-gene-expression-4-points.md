---
title: Problem 3. Differential gene expression (4 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/02-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 3. Differential gene expression (4 points)

**Source:** `psets/02-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You are analyzing RNA-seq data to identify differentially expressed genes between two treatment conditions. You have three biological replicates in each of the two conditions for a total of 6 samples, and you process and sequence each of the samples separately.

- **(A) (1 pts)** Imagine you first pool the sequencing results for each of the conditions, resulting in two pools. What kind of variation have you lost the ability to observe, and why might this variation be important?

This is performing analysis without any replicates. If we observe a difference between the conditions, we are unable to know if this difference is due to differential expression between the different conditions or due to baseline variation between the replicates (just due to technical or biological variation).

5

- **(B) (3 pts)** Devise an improved analysis strategy for these six samples and identify the sources of variation it can detect. Identify how you would estimate the mean-dispersion function for use in a negative binomial model of variation.

Don’t pool the sequencing results together. Now, since we have replicates for each condition, we can compute an empirical dispersion value per gene, rather than estimating dispersion from genes which have similar expression levels across conditions (under the assumption that the condition effect is minimal for these genes). This allows us to detect technical/biological variation among samples within the same condition as well as variation in excess of that due to differential expression between the two conditions.

**Problem 4. RNA Isoform quantification (3 points)**


Consider the gene structure in the above figure.

Exon numbers and sizes in nucleotides are indicated. The transcript can initiate at either of the arrows shown, and exons 2 and/or 3 can be spliced out.

- **(A) (1 pt.)** How many possible isoforms of this gene could exist?

6 isoforms

- **(B) (1 pt.)** For each isoform, list the junction spanning RNA-seq reads that would support it.

|**Isoform**|**Reads**|
|---|---|
|1-4|Only1-4spanningreads|
|1-2-4|1-2, and 2-4 spanning reads|
|1-3-4|1-3 and 3-4 spanning reads|
|1-2-3-4|1-2,2-3,and 3-4spanningreads|
|2-4|Only 2-4 spanning reads|
|2-3-4|2-3and 3-4spanningreads|


6

- **(C) (1 pt.)** Assuming single ended reads, what is the shortest read length that would guarantee the ability to unambiguously identify all isoforms of this gene if we require that a junction read must have minimum overlap of 5bp with each exon?

260bp – the 150bp of exon 2, 100bp of exon 3, and 5bp overlap with exons 1 and 4

---

[← Problem 2. Library Complexity (5 points)](04-problem-2-library-complexity-5-points.md) · [Up: contents](index.md) · [Problem 5. de Bruijn graphs (5 points) →](06-problem-5-de-bruijn-graphs-5-points.md)

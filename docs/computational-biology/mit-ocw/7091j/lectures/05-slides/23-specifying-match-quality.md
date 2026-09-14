---
title: Specifying match quality
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Specifying match quality

**Source:** `lectures/05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Bowtie supports a Maq*-like alignment policy – ≤ N mismatches allowed in first L bases on left end – Sum of mismatch qualities may not exceed E – N, L and E configured with **`-n`** , **`-l`** , **`-e`**

– E.g.:

<mark>G</mark> C <mark>C A T</mark> A <mark>C G</mark> G <mark>G C</mark> T <mark>A G C</mark> C If N < 2 <mark>40</mark> 40 <mark>35 40 40</mark> 40 <mark>40 30</mark> 30 <mark>20 15</mark> 15 <mark>40 25 5</mark> 5 If E < 45 If L < 9 and N < 2 L=12 E=50, N=2

- PHRED score = -10log(p)     Where p is probability of error

- Li H, Ruan J, Durbin R: Mapping short DNA sequencing reads and calling variants using mapping quality scores. Genome Res 2008.

Courtesy of Ben Langmead. Used with permission.

44

**http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt**

#### Bowtie can match starting from the left to limit backtracking

- But how to match left-to-right?

- Double indexing:

– Reverse read and use “mirror index”: index for reference with sequence reversed


**Forward Index**


###### **Mirror Index**


**G C C A T A C G G A T T A G C C**

**No backtracks allowed**


**C C G A T T A G G C A T A C C G**

**No backtracks allowed**

45

Courtesy of Ben Langmead. Used with permission.

#### Time to build a BWT/FM index

- Bowtie employs a indexing algorithm* that can trade flexibly between memory usage and running time

- For human genome (NCBI 36.3) on 2.4 GHz AMD Opteron:


<!-- Start of picture text -->
Physical  Actual peak<br>memory  memory<br>Target footprint Wall clock time<br>16 GB 14.4 GB 4h:36m<br>8 GB 5.84 GB 5h:05m<br>4 GB 3.39 GB 7h:40m<br>2 GB 1.39 GB 21h:30m<br><!-- End of picture text -->

- Kärkkäinen J: Fast BWT in small space by blockwise suffix sorting. Theor Comput Sci 2007, 387(3):249-257.

Courtesy of Ben Langmead. Used with permission.

46

**http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt**

#### 35bp read alignment performance

||CPU time|Wall clock<br>time|Reads<br>per hour|Peak<br>virtual<br>memory<br>footprint|Speedup|
|---|---|---|---|---|---|
|Bowtie, 1 thread (server)|18m:19s|18m:46s|28.3 M|**1,353 MB**|-|
|Bowtie, 2 threads (server)|20m:34s|10m:35s|**50.1 M**|**1,363 MB**|**1.77x**|
|Bowtie, 4 threads (server)|23m:09s|6m:01s|**88.1 M**|**1,384 MB**|**3.12x**|


- Bowtie uses POSIX threads to exploit multi-processor computers – Reads are distributed across parallel threads – Threads synchronize when fetching reads, outputting results, etc. – Index is shared by all threads, so footprint does not increase substantially as # threads increases

- Table shows performance results for Bowtie v0.9.6 on 4-core Server with 1, 2, 4 threads

Courtesy of Ben Langmead. Used with permission.

47

**http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt**

#### Paired read alignment in BWA


<!-- Start of picture text -->
Left Read<br><!-- End of picture text -->

**Unobserved**

**Right Read**


**Insert size (only estimate known)**

**Sequencing instrument identifies read pairs (also called mate pairs) in its output file First, align Left and Right Reads  (they can only be oriented with respect to a genome sequence) If one read fails to align uniquely, use Smith-Waterman for the unaligned read in proximal sequence to the aligned read**

48

#### Considerations for read alignment

**Uniquely aligning reads vs. “multimaped” reads in output Desired mismatch tolerance Desired processing for paired reads**

49

# **FIN**

50

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Backtracking](22-backtracking.md) · [Up: contents](index.md)

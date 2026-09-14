---
title: Cross-correlation analysis
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Cross-correlation analysis

**Source:** `lectures/11-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Exploiting  forward and reverse reads Fragment-length peak Phantom read-length peak

33

#### **ChIP-seq: exploiting forward and reverse reads**

**(Chromatin immunoprecipitation followed by sequencing)**


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Park, Peter J. "ChIP–seq: advantages and challenges of a maturing technology." Nature Reviews Genetics 10, no. 10 (2009): 669-680.

Multiple IP fragments are obtained corresponding to each binding event

Ends of the fragments are sequenced i.e. “Short-reads/tags”

- Typically ~36 bp, 50 bp, 76 bp or 101 bp

###### Single-end (SE) sequencing

- Randomly sequence one of the ends of each fragment

Paired-end (PE) sequencing

- sequence both ends of each fragment

- Canonical “stranded mirror distribution of <u>short-reads” after mapping reads to genome</u>

- Heaps of reads on the **+ strand** and **– strand** separated by a distance ~= fragment length

34

## **Strand cross-correlation (CC) analysis**

<u>f</u> f = fragment length


<!-- Start of picture text -->
c<br>b<br>d<br>a<br>f<br>strand shift (s)<br>cross-correlation<br><!-- End of picture text -->


<!-- Start of picture text -->
f<br>(a)<br>(b)<br>(c)<br>(d)<br><!-- End of picture text -->

**_s = f/2 + f/2_**

1. Calculate forward and reverse strand signals 2. Shift both by specified offset towards each other

3. Calculate correlation of two signals at that shift

4. Correlation peaks at **fragment length** offset **_f_**

**_f_** is the length at which ChIP DNA is fragmented

35

### **Cross-correlation at** **_read_ vs.** **_fragment_ length**


<!-- Start of picture text -->
C Cf<br>fragment<br>read<br>CCr<br>min ( CC )<br>r = read length<br>f  = fragment length<br><!-- End of picture text -->

strand shift (s)

- Sign of a good dataset:

   - High absolute cross-correlation at _fragment_ length (NSC)

   - High _fragment_ length CC relative to _read_ length CC (RSC)

36

##### **Where does** **_read_ cross-correlation come from?**


<!-- Start of picture text -->
Mappable<br>region<br>x<br>x+r-1<br>Unmappable  Unmappable<br><!-- End of picture text -->

- Input dataset (no ChIP) shows ‘phantom’ peak at **_read_** length only

- Due to read mappability:

   - If position ‘x’ is uniquely mappable on + strand

   - Then position ‘x+r-1’ is uniquely mappable on – strand

- _Fragment_ -length peak should always dominate the read-length peak

37

### **Example of good, medium, bad CC datasets**


<!-- Start of picture text -->
CCf<br>CCr<br>min ( CC )<br>strand shift  strand shift<br>Highly quality  Medium quality<br>cross-correlation<br><!-- End of picture text -->


<!-- Start of picture text -->
strand shift<br><!-- End of picture text -->


<!-- Start of picture text -->
Low quality<br><!-- End of picture text -->


For highly enriched datasets, fragment length cross-correlation peak should be able to beat read-length phantom peak

RSC should be > 1

38

###### **Goals for today: Computational Epigenomics**

1. Introduction to Epigenomics – Overview of epigenomics, Diversity of Chromatin modifications

   - Antibodies, ChIP-Seq, data generation projects, raw data

2. Primary data processing: Read mapping, Peak calling – Read mapping: Hashing, Suffix Trees, Burrows-Wheeler Transform

– Quality Control, Cross-correlation, Peak calling, IDR (similar to FDR)

3. Discovery and characterization of chromatin states

   - A multi-variate HMM for chromatin combinatorics

- Promoter, transcribed, intergenic, repressed, repetitive states

- 4. Model complexity: selecting the number of states/marks – Selecting the number of states, selecting number of marks

- – Capturing dependencies and state-conditional mark independence

- 5. Learning chromatin states jointly across multiple cell types – Stacking vs. concatenation approach for joint multi-cell type learning

- – Defining activity profiles for linking enhancer regulatory networks

- (Future: Chromatin states to interpret disease-associated variants)

39

---

[← Quality control metrics](09-quality-control-metrics.md) · [Up: contents](index.md) · [Peak Calling →](11-peak-calling.md)

---
title: Searching for an Exact Match
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Searching for an Exact Match

**Source:** `lectures/11-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

P is the input substring

e.g. Searching for OLIS In MANOLISKELLIS **For simplicity** (here):

C[c] – is how many characters occur before c lexographically in the genome

- only exact matches

Occ(c,k)  is the number of occurrence of the character c before index _k_ in the far right column

- Show entire matrix

**In practice** : only pointers

###### OLIS

###### OLIS

###### OLIS

###### OLIS

`1. $MANOLISKELLIS`

      `1. $MANOLISKELLIS`

   `1. $MANOLISKELLIS`

`1. $MANOLISKELLIS`

`2. ANOLISKELLIS$M`

      `2. ANOLISKELLIS$M`

   `2. ANOLISKELLIS$M`

`2. ANOLISKELLIS$M`

`3. ELLIS$MANOLISK`

      `3. ELLIS$MANOLISK`

   `3. ELLIS$MANOLISK`

`3. ELLIS$MANOLISK`

`4. IS$MANOLISKELL`

```
4. IS$MANOLISKELL
```

   `4. IS$MANOLISKELL`

`4. IS$MANOLISKELL`


`5. ISKELLIS$MANOL`

```
5. ISKELLIS$MANOL
```

   `5. ISKELLIS$MANOL`

`5. ISKELLIS$MANOL`

`6. LIS$MANOLISKEL`

```
6. LIS$MANOLISKEL
7. LISKELLIS$MANO
8. LLIS$MANOLISKE
```

   `6. LIS$MANOLISKEL`

`6. LIS$MANOLISKEL`

      `7. LISKELLIS$MANO`

   `7. LISKELLIS$MANO`

`7. LISKELLIS$MANO`

```
8. LLIS$MANOLISKE
9. KELLIS$MANOLIS
10.MANOLISKELLIS$
11.NOLISKELLIS$MA
12.OLISKELLIS$MAN
13.S$MANOLISKELLI
14.SKELLIS$MANOLI
```

   `8. LLIS$MANOLISKE`

`8. LLIS$MANOLISKE`

```
9. KELLIS$MANOLIS
```

   `9. KELLIS$MANOLIS`

`9. KELLIS$MANOLIS`

```
10.MANOLISKELLIS$
11.NOLISKELLIS$MA
12.OLISKELLIS$MAN
13.S$MANOLISKELLI
14.SKELLIS$MANOLI
```

   - `10.MANOLISKELLIS$`

- `10.MANOLISKELLIS$`

   - `11.NOLISKELLIS$MA`

- `11.NOLISKELLIS$MA`

- `12.OLISKELLIS$MAN`

```
12.OLISKELLIS$MAN
13.S$MANOLISKELLI
14.SKELLIS$MANOLI
```

```
13.S$MANOLISKELLI
14.SKELLIS$MANOLI
```

Pseudocode from Langmead et al, 2009. Example by Jason Ernst.

22

## Hashing vs. Burrows Wheeler Transform


<!-- Start of picture text -->
Multi-seed<br>hashing<br>BWT<br>Burrows-<br>Wheeler<br>Transform<br>Today: How does the BW<br>transform actually work?<br><!-- End of picture text -->

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Trapnell, Cole and Steven L. Salzberg. "How to map billions of short reads onto genomes." Nature Biotechnology 27, no. 5 (2009): 455.

23

#### Key properties of Burrows-Wheeler Transform

- **Very little memory usage. Same as input (or less)**

   - Don’t represent matrix, or strings, just pointers

   - Encode: Simply sort pointers. Decode: follow pointers

- **Original application: string compression (bZip2)**

   - Runs of letters compressed into (letter, runlength) pairs

- **Bioinformatics applications: substring searching** – Achieve similar run time as hash tables, suffix trees

   - But: very memory efficient  practical speed gains

- **Mapping 100,000s of reads: only transform once**

   - Pre-process once; read counts in transformed space.

   - Reverse transform once, map counts to genome coords

24

###### **Goals for today: Computational Epigenomics**

1. Introduction to Epigenomics – Overview of epigenomics, Diversity of Chromatin modifications

- Antibodies, ChIP-Seq, data generation projects, raw data

- 2. Primary data processing: Read mapping, Peak calling – Read mapping: Hashing, Suffix Trees, Burrows-Wheeler Transform

- – Quality Control, Cross-correlation, Peak calling, IDR (similar to FDR)

- 3. Discovery and characterization of chromatin states

   - A multi-variate HMM for chromatin combinatorics

- Promoter, transcribed, intergenic, repressed, repetitive states

- 4. Model complexity: selecting the number of states/marks – Selecting the number of states, selecting number of marks

- – Capturing dependencies and state-conditional mark independence

- 5. Learning chromatin states jointly across multiple cell types – Stacking vs. concatenation approach for joint multi-cell type learning

- – Defining activity profiles for linking enhancer regulatory networks

- (Future: Chromatin states to interpret disease-associated variants)

25

---

[← How would you do it](07-how-would-you-do-it.md) · [Up: contents](index.md) · [Quality control metrics →](09-quality-control-metrics.md)

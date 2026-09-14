---
title: Introduction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/06-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/06-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 6 Genome Assembly

Foundations of Computational Systems Biology David K. Gifford

1

_��������_ ��������������������� ��������

Courtesy of Nature Education. Used with permission. Source: Green, Eric D. "Strategies for the Systematic Sequencing of Complex Genomes." _Nature Reviews Genetics_ 2, no. 8 (2001): 573-83.

��������������������������������������������������������������������������

2

#### Assembly

Whole-genome “shotgun” sequencing starts by copying and fragmenting the DNA

(“Shotgun” refers to the random fragmentation of the whole genome; like it was fired from a shotgun)

Input: ����������������������������������� Copy: ����������������������������������� ����������������������������������� ����������������������������������� ����������������������������������� Fragment: ����������������������������������������� ����������������������������������������� ����������������������������������������� �����������������������������������������

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

3

#### Assembly

Assume sequencing produces such a large # fragments that almost all genome positions are covered by many fragments...

����������������������������������� ����������������������������������� ����������������������������������� ��������������������������������� Reconstruct ����������������������������� this ������������������������� ����������������������� ��������������� ������������� �������������

From these

�����������������������������������

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

4

#### Assembly

...but we don’t know what came from where

Reconstruct this


����������������� ������������� ������������������� ������������������� ��������������������� ���������������������� ��������������������� ������������� ����������������� ���������������

�����������������������������������

From these

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

5

#### Assembly

Key term: coverage.  Usually it’s short for average coverage: the average number of reads covering a position in the genome.

����������������������������������� ����������������������������������� ����������������������������������� ��������������������������������� ����������������������������� 177 nucleotides ������������������������� ����������������������� ��������������� ������������� ������������� ����������������������������������� 35 nucleotides

35 nucleotides

Average coverage = 177 / 35 ≈ 7x

Courtesy of Ben Langmead. Used with permission. http://www.langmead-lab.org/teaching-materials/

6

������������������������� �����������������

• ���������������

- ��������������

• ������������������

- ��������������������λ   (���������

   - –�����������λ�����<sup>−λ</sup> =∼����������������������������������

–���������������������������<sup>�λ</sup>

- –���������������<sup>�λ</sup>

7

### ������������������������������������ ��������


<!-- Start of picture text -->
© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

8

#### Assembly

Coverage could also refer to the number of reads covering a particular position in the genome:

����������������������������������� ����������������������������������� ����������������������������������� ��������������������������������� ����������������������������� ������������������������� ����������������������� ��������������� ������������� ������������� �����������������������������������

Coverage at this position = 6

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

9

#### Assembly

Say two reads truly originate from overlapping stretches of the genome.  Why might there be differences?

������������������������� ����������������������� �����������������������

1. Sequencing error

2. Difference between inhereted copies of a chromosome E.g. humans are diploid; we have two copies of each chromosome, one from mother, one from father.  The copies can differ:

Read from Mother:������������������������� ����������������������� Read from Father:�����������������������

We’ll mostly ignore ploidy, but real tools must consider it

Sequence from Mother: ��������������������� Sequence from Father: ���������������������

Courtesy of Ben Langmead. Used with permission.

http://www.langmead-lab.org/teaching-materials/

10

---

[Up: contents](index.md) · [06 slides Part 02 — →](02-06-slides-part-02.md)

---
title: Overlapping Fields
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/01-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Overlapping Fields

**Source:** `lectures/01-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Computational Systems Informatics Biology Biology Biology Bioinformatics (Methods/Tools for Using Computational/ Study of Molecular and Management and Modeling/Analytical Cellular Systems Analysis of Information/ Approaches to Data) Address Biological Questions (Development of Methods for Analysis of Biological Data) Study of Living Things

The 1970s and Earlier - Sequence Databases, Similarity Matrices and Molecular Evolution


How do protein sequences evolve?

How should similarity between two proteins be scored to most accurately detect homology?

- First protein sequence databases / protein family classification

- PAM matrices for protein sequence comparisons (still used!)

###### Margaret Dayhoff

This photograph is in the public domain.

What can molecular sequences tell us about organismal evolution?


- Molecular classification of life


- Molecular clocks

- Use of ribosomal RNA to infer phylogeny

- Discovery of third 'domain' of life - Archaea

###### Carl Woese

© NARA/U. of Illinois 306-PS-E-77--S743. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Russ Doolittle

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

8

#### The 1980s: Sequence Alignment/Search

Which specific residues/positions in a pair of proteins are homologous?

• Smith-Waterman alignment algorithm

Photographs of scientists removed due to copyright restrictions.

What RNA secondary structure has

minimum folding free energy?

- Nussinov algorithm

- Zuker algorithm

How to rapidly and reliably find homologs to a query sequence in a sequence database?

- FastA and BLAST algorithms and associated statistics

Photographs of scientists removed due to copyright restrictions.

9

#### Al Gore Learns to Search PubMed


**_NCBI Director David Lipman (far left) coaches Vice President Gore (seated) as he searches PubMed. NIH Director Harold Varmus (center) and NLM Director Donald Lindberg (far right) look on._**

Photograph by the National Center for Biotechnology Information; in the public domain.

10

The ‘90s: HMMs, Ab Initio Protein Structure Prediction, Genomics, Comparative Genomics

How to identify domains in a protein? How to identify genes in a genome? Hidden Markov Models as a framework for such problems

How to study gene expression globally, infer gene function from expression?

- Microarrays and clustering

How to predict protein function by comparing genomes?

- gene fusions, phylogenetic profiling, etc.

How to predict protein structure directly from primary sequence?

- Rosetta algorithm

Photographs of scientists removed due to copyright restrictions.

11

#### The 2000s Part 1: The human genome is sequenced, assembled, annotated

###### genomics becomes fashionable

Photograph of genome-project pioneers removed due to copyright restrictions. See the photograph on nature.com.

Photograph of Craig Venter removed due to copyright restrictions.

Photographs of Jim Kent removed due to copyright restrictions.

© Mayo Foundation for Medical Education and Research. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Photographs of Ewan Birney removed due to copyright restrictions.

12

#### The 2000s Part 2: Biological Experiments Become High-Throughput, Computational Biology Becomes more Biological

Massively parallel data collection - transcriptomics, proteomics, interactomics, metagenomics

Using sequence and array data to address fundamental questions about transcription, splicing, microRNAs, translation, epigenetics, protein structure/function, development, evolution, disease, etc.

Courtesy of Marc Vidal. Used with permission.

Integrated computational/experimental approaches

Rise of bioimage informatics


Courtesy of Donald G. Moerman and Benjamin D. Williams. License: CC-BY. Source: Moerman, D. G. and Williams, B. D. "Sarcomere Assembly in C. Elegans Muscle" (January 16, 2006), WormBook, ed. The C. elegans Research Community, WormBook.

13

Photograph of Eric Davidson removed due to copyright restrictions.


Computational model of the gene regulatory netowrk controlling sea-urchin embryonic development removed due to copyright restrictions. See the image here.

Courtesy of Charles Ettensohn. Used with permission.

###### The 2000s Part 3 Systems Biology

Models of gene and protein networks in development, disease, etc.


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

14

#### The 2000s Part 4: Synthetic Biology & Biological Engineering

Design of regulatory networks using biological components


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Elowitz, Michael B., and Stanislas Leibler. "A Synthetic Oscillatory Network of Transcriptional Regulators." _Nature_ 403, no. 6767 (2000): 33S-8.


15

#### Late 2000s / Early 2010s


**Next-gen sequencing finds applications across biology** Genome sequencing Transcriptome sequencing Protein-DNA intrxns (ChIP-seq) Protein-RNA intrxns (CLIP-seq)

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Metzker, Michael L. "Sequencing Technologies-the Next Generation. " _Nature Reviews Genetics_ 11, no. 1 (2009): 31-46.

###### Metzker NRG 2010

Translatome Methylome Open chromatome

Photograph of Barbara Wold removed due to copyright restrictions.

16

#### For those who would like a proper history of the field


Photograph of Hallam Stevens removed due to copyright restrictions.


© University of Chicago Press. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Stevens, Hallam." Life Out of Sequence: A Data-Driven History of Bioinformatics<sup>."</sup> _University of Chicago Press_ , 2013.

17

###### **Online Access**

All course materials, including copies of lecture slides, will be distributed via course website :

###### **Auditors/Listeners**

The class may be audited only by permission of one of the instructors. Please meet us after class and tell us who you are and why you want to audit. Students are strongly encouraged to take the course for credit.

18

### A look at the syllabus

**Topics:**

Genomic Analysis I  (CB) Genomic Analysis II – 2<sup>nd</sup> Gen Sequencing (DG) Modeling Biological Function (CB) Proteomics (EF) Regulatory Networks (EF, DG + DL) Computational Genetics (DG)

Guest lectures: Doug Lauffenburger (signaling networks), Ron Weiss (synth bio), George Church (genetics/genomics)

Topics will include a discussion of motivating questions, experimental methods and the interplay between experiment and computation

19

#### Motivating Questions

What instructions are encoded in our (and other) genomes? How are chromosomes organized?

What genes are present?

What regulatory circuitry is encoded?

Can the transcriptome be predicted from the genome? Can the proteome be predicted from the transcriptome? Can protein function be predicted from sequence?

Can evolutionary history be reconstructed from sequence?

20

#### Motivating Questions

What would you need to measure if you wanted to discover the causes of disease? the mechanisms of existing drugs? the metabolic pathways in a micro-organism?

What kind of modeling would help you use these data to design new therapies? re-engineer organisms for new purposes?

What can we currently measure?

What does each type of data mean individually?

How do we integrate the data to understand the system?

21

### Course Schedule, Part I


22

### Course Schedule, Part II


23

#### **Is this the right course for me?**

Other alternatives are available, some more specialized:

7.57 Quantitative Biology for Graduate Students (only for bio grad students)

               - 7.81 Systems Biology (Gore)

- 6.581/20.482 Foundations of Algorithms and Computational Techniques in Systems Biology (Tidor, White)

   - 6.047/6.878 Computational Biology: Genomes, Networks, Evolution (Kellis)

            - 6.502/6.582/HST.949 Molecular Simulations (Stultz)

         - 6.877/HST.949 Computational Evolutionary Biology (Berwick)

      - 18.417 Introduction to Computational Molecular Biology (Waldispuhl)

         - 18.418 Topics in Computational Molecular Biology (Berger)

10.555J Bioinformatics: Principles, Methods and Applications (Stephanopoulos, Rigoutsos)

24

###### **Text Book**

The following text is recommended (not required) for this course is available through Amazon and at the COOP and will be on reserve at Hayden library

###### <u>Understanding Bioinformatics, Zvelebil & Baum (Garland Science)</u>

This text contains helpful background information for some of the lectures and relevant chapters or sections will be mentioned from time to time. However, we have also selected the following texts as particularly useful in selected areas, if you are looking for further information. …

###### **Basic Probability and Statistics**

A primer covering basic concepts in probability and statistics that are useful for this class is available at the class web site. The workbook is designed for students to complete at their own pace, and/or to use as a reference. It includes explanatory material and many examples drawn from biology. Students who have less background in these areas or need a refresher are strongly encouraged to read the primer and do the examples. Your TAs will be able to answer questions about this material throughout the semester.

25

###### **Homework**

Five written or computer-based homework assignments will be posted on the course web site. These are designed to promote deeper understanding of the principles and algorithms discussed in class and to provide hands-on experience with bioinformatics tools _._

Your score for the homework portion of the course will be based on a maximum of 100 points, but the total points available on the homeworks will be 120. This means that you can miss one homework (or a portion of one homework) and still do fairly well on this component if you have done well on the other homeworks. For example, a student who obtained perfect marks on 4 of 5 homeworks, each valued at 24 points would get 96 points for the homework component of the course, almost as good as a student who completed all 5 homeworks, earning 90% of points on each, since 0.9 x 120 = 108, which would earn the maximum score of 100. Because of this, no make-up <u>assignments will be offered. Of course, it is still to your advantage to do all five homeworks, as this will help you to</u> learn the material in more depth, help prepare you for exams, etc. Please note that the point values of individual homeworks may vary somewhat from the 24 point average value, depending on their length and level of difficulty.

The dates that the assignments are due are included in the syllabus below. Homework must be turned in to the appropriate box outside of the Biology education office (68-120), or submitted on-line, by the assigned time to be eligible for full credit.

###### **Late assignments**

Assignments are due at noon on the dates indicated on the syllabus. Assignments received electronically, or in the appropriate box outside the Biology Education Office (68-120), within 24h of the time they are due will be eligible for 50% credit. If necessary, you may turn in your written portion and your programming portion separately. For example, if you turn in your written portion on time and your programming by the late due date, your written work will be eligible for full points but the programming will be eligible for only 50% of points. You may not further sub-divide your submissions. Because answer keys will be posted, no homework will be accepted after the extended deadline.

26

###### <u>Collaboration on Problem Sets</u>

The goal of the problem sets is to reinforce the material and sometimes to explore a topic in greater depth. You may talk with other students about the problems and work on them together. However, you should write up your own solutions. Copying someone else's solutions will not improve your understanding of the material and is not acceptable. Duplicate or nearly identical <u>homeworks from different students will receive a score of zero. This has happened. We notice.</u> Don’t let it happen to you!

###### Collaboration on Programming in Problem Sets

You must write your own code on problem sets. You may discuss the programming problems with other students. The following two simple rules should make it clear what is not permitted: do not copy or reuse code from any source (except the sample code provided) do not share your code with anyone else in the class.

###### **Intellectual Honesty**

We hope and trust that academic misconduct will not occur during this course. We nevertheless want to emphasize that we will be rigorous in our enforcement of Institute rules. It is the policy of the Biology Department to keep a record of all cases of academic misconduct and to forward cases to the Dean of Undergraduate and Student Affairs.

27

#### **Recitations**

Three recitation sections will be offered each week. Times will be determined on the first day of class. These will be led by the TAs and will provide students an opportunity to ask questions about material presented in lecture, the readings or the homeworks. Recitations are required for 6.874, optional for other versions. However, if you are having difficulty in the class, you are _strongly_ encouraged to attend regularly.

28

###### **Python Instruction**

The homework assignments will include problems that involve writing programs in the scripting language Python. Python is widely used for bioinformatics and computational biology. Programming will not be taught in lecture, but because some students may have little or no programming experience, hands-on tutorials in Python will be offered by the teaching assistants during the first and second weeks of classes. Also, you may ask questions related to programming assignments at weekly recitations. Be sure to attend recitation if you are struggling with the programming assignments.

There will be an "Intro to Python" session, targeting those with little or no previous programming experience.

Please bring a laptop if you have one.

- "Notes outlining the materials covered in these sessions, as well as short exercises "designed to help you get up to speed (NOT for credit), are posted on course website . "You are encouraged to look at these materials, especially "Starting Python Programming” before attending the introductory sessions.

29

###### **Project Component** (7.91/20.490/6.874/HST.506 only)

Students registered for one of the graduate versions of this course will also complete a computational biology research project during the semester.

There are 6 student assignments related to project component:

- 1) Submit background/interests for posting to course website

- 2) Choose Teams and submit Project Title and 1 Paragraph Summary

- 3) Submit Specific Aims (1 page)

- 4) Submit Research Strategy (2 pages)

- 5) Submit Final Written report (~5 pages)

- 6) Oral presentations <u>Due dates for these assignments are listed on the course syllabus.</u>

This Project component of this course is designed to give you practice in applying computational methods to contemporary problems in biology. Students design and carry out projects working in a group (maximum: 5 students, unless approved by instructor) or by themselves. We suggest that you choose people to work with who have skills complementary to yours.

30


31

###### **Exams/Grading/Honesty**

###### **Exams**

There will be two 80-minute exams (non cumulative). Exam dates are noted on the calendar below. Students are expected to take the exams at the scheduled times.  There is no final exam.

|**Grading**|
|---|
|Undergraduate versions of course (6.802, 7.36, 20.390):|
|Homework (out of max 100 points):<br>36%|
|Exams<br>62%|
|Peer Review<br>2%|


|Graduate Bio/BE/HST versions of course (7.91, 20.490, HST.506<br>):|
|---|
|Homework (out of max 100 points):<br>30%|
|Exams<br>48%|
|Project<br>20%|
|Peer Review<br>2%|


|Graduate EECS version of course (6.874):|
|---|
|Homework (out of max 100 points):<br>25%|
|Exams<br>48%|
|Project<br>20%|
|Extra AI-related problems<br>5%|
|Peer Review<br>2%|


An additional 1% extra credit may be awarded for exceptional class participation.

32

### Topic 1 - Announcements

###### **PSet**

- PSet1 will be posted tonight. **Due: Thurs Feb 20 @ noon**

- <sup>involves basic molecular biology, probability/statistics</sup>

- Pset2 will be posted soon. <u>Look at the programming problem to give you a feeling for the level of programming that will be needed.</u>

###### **Probability/Stats**

- For review of basic probability/statistics concepts related to the course, see Statistics Primer (posted)

###### **Sequencing Technologies**

- Read Metzker review (posted)

###### **Reading on Sequence Alignment / Statistics**

- Over the next several days, read Chapters 4, 5 of Z&B for background on sequence alignment

33

### Genomic Analysis I

Sequencing Technologies (L1/L2)

Metzker 2010

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Metzker, Michael L. "Sequencing Technologies-the Next Generation." _Nature Reviews Genetics_ 11, no. 1 (2009): 31-46.


Sequence search/statistics with BLAST (L2) (local ungapped sequence alignment)


-λx]

P(S > x) = 1 - exp[-KMN e

34


<!-- Start of picture text -->
Global Sequence Alignment (L3)<br>Gap  V  D  S  C  Y<br>Gap  0 4 -8  -16  -24  -32  -40<br>-3  -8<br>-8<br>V  -8  4  -4  -12  -20  -28<br>3<br>E  -16  -6  7 2  -1  -9  -17<br>S  -24  -14  -6  9  1  -7<br>L  -32  -22  -14  1  3<br>0<br>C  -40  -30  -22  -7  13  3<br>Y  -48  -38  -30  -15  5  23<br><!-- End of picture text -->


© Cold Spring Harbor Laboratory Press. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Figure 1B of Friedman, Robin C., Kyle Kai-How Farh, et al. "Most Mammalian mRNAs are Conserved Targets of MicroRNAs." _Genome R esearch_ 19, no. 1 (2009): 92-10S.

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Comparative Genomic Analysis of Gene Regulation (L4)

35

### Modeling Biological Function

###### Modeling & Discovery of Sequence Motifs (L9)


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.


Markov & Hidden Markov Models of Genomic and Protein Features (L10)

Courtesy of CIS Journal. Used with permission.

Source: Hashad, Attalah, Khalaed Kamal, et al. "Improving Virus C type 4 Interferon using Bioinformatics Techniques." (PDF) _Journal of Emerging Trends in Computing and Information �ciences�_ no. 6 (2012): 88S-9S.

36

RNA Secondary Structure - Biological Functons & Predicton (L11)

© Washington University. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

37

---

[← Plan for Today](02-plan-for-today.md) · [Up: contents](index.md) · [Genomic Analysis Module Next Generation Sequencing →](04-genomic-analysis-module-next-generation-sequencing.md)

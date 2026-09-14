---
title: '3. HMMs for GC-rich regions: State durations and limitations'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/psets/01-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. HMMs for GC-rich regions: State durations and limitations

**Source:** `psets/01-questions.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

An important use of HMMs is to decode or parse a genome into its biological components: exons, introns, regulatory regions, etc. In this problem, we will examine how the accuracy of HMM predictions is affected by certain inherent properties of the model.

In this problem, we will use GC content (the fraction of letters that are a C or a G) to classify the genome into high-GC regions (on average 60% G or C) and Low-GC regions (on average 60% A or T). These have different melting temperatures, different replication times across the cell cycle, and different gene density. They have also been hypothesized to have different evolutionary origins (see _isochores_ ), but this hypothesis remains controversial.

Our simple model requires only two states. We have provided a program, `viterbi.py` , which you will complete and use to decode several artificial genomes, and then compare the resulting predictions of HighGC and Low-GC regions to a provided (correct) annotation. More details about this program are included at the end of the problem.

- (a) In most HMMs, the self-loop transition probabilities _akk_ are large, while the transition probabilities between different states _akl_ are small. Once a Markov chain with these transition probabilities enters state _k_ , it tends to stay in state _k_ for a while. The _state duration_ is the total number of consecutive steps at which the Markov chain stays in the same state, before switching to another state (e.g. transitioning into state _k_ and then transitioning out to a different state is a state duration of 1). What is the expected (mean) state duration of state _k_ as a function of the transition probability _akk_ ? What is the distribution of state durations _P_ ( _Dk_ = _d_ )?

- (b) Complete the implementation of the Viterbi algorithm in `viterbi.py` . Based on the HMM parameters hard-coded into the program, what are the expected state durations for High-GC and Low-GC regions? Apply the finished program to the data file `hmmgen` , which was generated using the same HMM, and verify that your program achieves _∼_ 83% accuracy.

- (c) Now apply your program to the files `mystery1` , `mystery2` , and `mystery3` . How do the (correct) state duration distributions in the mystery sequences differ and what do they have in common? What accuracy levels does your HMM achieve on these sequences? How does each Viterbi-predicted state duration distribution differ from the correct distribution? (You do not need to include the plots in your solutions.)

- (d) Would re-training the HMM parameters according to the procedure described in lecture, using the correct annotations as training data, improve the accuracy of the Viterbi annotation for the mystery sequences? Why or why not?

   - (Extra credit) Try to make the decoder perform better by adjusting the hard-coded model parameters. If you succeed, can you explain why?

- (e) As you are now aware, the length distribution of genomic elements can strongly affect the predictive accuracy of an HMM used to decode them. Unfortunately, most elements in real genomes do not follow the length distribution you derived in part (a). By reading the following paper (or any other sources), describe how the gene finder GENSCAN addresses this issue. How is it possible, algorithmically, to use state duration distributions that differ from the one you derived in part (a)? Burge C, Karlin S. Prediction of complete gene structures in human genomic DNA. _J Mol Bio_ 268(1):78-94, 1997.

Details about `viterbi.py`

3

**6.047/6.878/HST.507 Fall 2015**

**Problem Set 1**

Note that like in problem set 1, the plotting portion of this code relies on gnuplot. Therefore, you should run this on athena after running “add gnu” if you want plotting to work.

The nearly complete program `viterbi.py` performs the following:

   - Reads in a data file containing a DNA sequence and an authoritative (correct) annotation, consisting of a string of pluses and minuses, specifying where the High-GC and Low-GC regions are, respectively.

   - Calculates the base composition of the High-GC and Low-GC regions, calculates the mean length of High-GC and Low-GC regions, and plots a histogram of the lengths of the High-GC and Low-GC regions. (All with respect to the authoritative annotation.)

   - Performs Viterbi decoding on the DNA sequence, using a hard-coded HMM designed to detect High-GC and Low-GC regions. (This is the part you will complete.)

   - Calculates the base composition of the High-GC and Low-GC regions, calculates the mean length of High-GC and Low-GC regions, and plots a histogram of the lengths of the High-GC and Low-GC regions. (All with respect to the Viterbi annotation.)

   - Calculates the accuracy of the Viterbi decoding, defined as the percentage of predicted plus and minus states that match the authoritative annotation.

4. **Final project preparation** This course aims to both introduce you to the field of computational biology, and to enable you to become active members of its research community. This involves being able to plan, set up, carry out, and report your independent research, which will be the goal of the final project. While the bulk of the work for the final project will be carried out during the second half of the term, it is important to begin thinking about possible projects early on.

To begin the process of identifying a good project that matches your background and your interest, this part of the first problem set asks you to begin that process by writing a paragraph or two on each of the following questions:

- (a) **Skill set:** Detail your academic background, and in particular, your computational/algorithmic training and your biological knowledge/experience. We encourage you to select a project that matches your skills, and benefits from your strengths. Certainly, you will learn new areas and new applications of your skills, but you are more likely to accomplish a successful project if you think carefully about your strengths, and perhaps identify partners that complement your background early on.

- (b) **Research experience:** Outline your previous research experience, if any. This can be in any field and can be either independent research or class-related research. Think back at the projects you have accomplished over the years, list them here, and give a brief description of the kind of skills that you gained in accomplishing them.

- (c) **Interests:** What areas of computational biology do you find the most interesting for your own research? Read ahead on the syllabus, and find the lecture topics that seem most interesting to you for a final project. You can find more information about each of these topics on the web, or by pulling up the slides for these lectures from previous years. Stepping back and taking a look at the whole term ahead of time will help you pick a topic without biasing yourself to only consider early lectures.

- (d) **Project types:** Think ahead about the type of project you might prefer, for example: algorithmic, theoretical, tool-building, analysis, or method development. This can help you identify areas that are more inclined to the type of project that youre looking for, and also pair up with partners that share similar interests, or complementary interests on the same topic.

A unique aspect of computational biology is how collaborative the field is. In order to learn more about your classmates, identify potential partners for the final project, and potentially even collaborators that will come in handy for the longer term, we ask you to fill out the information above (or an abbre­ viated version thereof) in an MS Word document and upload it with your homework. We have pro­ vided a template `StudentProfileTemplate.doc` . Note that these summaries will be shared among

Athena is MIT's UNIX-based computing environment. OCW does not provide access to it.

4

**6.047/6.878/HST.507 Fall 2015**

**Problem Set 1**

your classmates (if you are uncomfortable with this, please contact the course staff). Name your pro­ file `LastnameFirstname` ~~`P`~~ `rofile.doc` . There will be more files that complement this through the term, so maintaining a consistent naming scheme is important.

5

MIT OpenCourseWare http://ocw.mit.edu

6.047 / 6.878 / HST.507 Computational Biology Fall 2015

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← CGT[AATC]AGA](03-cgt-aatc-aga.md) · [Up: contents](index.md)

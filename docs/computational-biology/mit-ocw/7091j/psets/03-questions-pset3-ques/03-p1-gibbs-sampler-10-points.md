---
title: P1. Gibbs Sampler (10 Points).
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/03-questions-pset3-ques.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# P1. Gibbs Sampler (10 Points).

**Source:** `psets/03-questions-pset3-ques.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You are studying longevity in two species, A and B.  A study was recently published showing that a transcription factor called AGE is involved in regulating many aging- and stress-related pathways in both species A and B.  AGE is known to affect transcription by binding to the promoters of its target genes.  You have a list of aging-related genes whose expression changed (as measured by RNA-seq) in _age_ ( _-_ ) mutants relative to wild-type in species A.  From a similar experiment, you obtained a list of genes whose expression changed in _age(-)_ in species B.  You want to look at the promoters of these genes to see if you can find any enriched sequence motif that might be a recognition site for AGE.  You have two lists of sequences – seqsA.fa contains the 30bp upstream from the AGE target genes in A, and seqsB.fa contains 30bp upstream from the AGE target genes in B.  To do this analysis, you will implement a Gibbs sampler!  Once you are done modifying the script for parts A-D, please submit your completed <u>gibbsSampler.py script to the Homework Submissions dropbox on the course website.</u>

**(A – 6 points)** Download the skeleton code gibbsSampler.py.  The script requires two inputs: the name of a FASTA file containing sequences believed to share a common motif, and the length of the motif.  The main function run is called at the very bottom of the script; the argument x passed to run(x) is the number of iterations of the Gibbs sampler that will be run (initially set to 1).

You can run the script with the sequences from A as the input file and motif length 7 by running

% python gibbsSampler.py seqsA.fa 7

The skeleton code should run without errors, though it will mostly be telling you that various subfunctions haven’t been implemented yet.  Now fill out the skeleton code so that it successfully implements the Gibbs Sampler. Though you can use whatever approach you find best when completing the script, you may find the suggestions in GibbsSamplerHelp.txt helpful to walk you through which sub-functions you need to complete.

Once you’ve completed the code, set your Gibbs Sampler to run 1000 iterations and run it on the seqsA.fa file.  Run the algorithm several (~10) times and pick the highest scoring run.  For that run, report the background distribution, final weight matrix, motif score and relative entropy (you can just copy and paste from the output of the script as long as your solution is in readable table form; .doc provided on course website if helpful).  Also, plot the relative entropy of the motif after each iteration.  What is the shape of this graph?  What is the consensus motif?  (Hint: the highest scoring motif has a score over 600).

**(B – 1 point)** Weight matrices are not very visually informative for understanding a motif – Sequence Logos are more human friendly.  Run your code again, using the printToLogo() function provided in the code to print out the final motifs for each sequence after the 1000 iterations are complete (you may want to comment out the other outputs).  Go to http://weblogo.berkeley.edu/logo.cgi and paste the list of aligned motifs into the input box and hit Create Logo (note that the number of bits of information at each position doesn’t take into account the background distribution of the sequences).  Try this at least 3 different times with different runs of your Gibbs sampler, and print off or include a screenshot of each logo as well as the relative entropy and final score of that logo.  Compare the results of your various runs. Briefly explain what types of differences you observe and why the Gibbs sampler returns these different motifs.

**(C – 2 points)** We now want to look for motifs in species B.  Run the algorithm for length 7 and seqsB.fa several times and report the background distribution, final weight matrix, motif score and relative entropy (you don’t need to plot RelEnt at every iteration) from a representative run. How does the relative entropy of the motif in species B compared to species A?  Does this mean that the AGE motif is easier or harder to find in species B?  Why?

**(D – 1 point)** Assuming there was still one occurrence of the motif in every sequence, what would happen if we increased the lengths of the sequences we are searching through?  Run your Gibbs sampler on seqsAext.fa, which contains sequences of length 90 instead of 30.  Run it several times and plot the relative entropy as a function of the number of iterations for a high scoring run.  How is this plot different from part (a)?  Can you explain the difference?

---

[← Python Scripts](02-python-scripts.md) · [Up: contents](index.md) · [P2. RNA secondary structure prediction (5 points). →](04-p2-rna-secondary-structure-prediction-5-points.md)

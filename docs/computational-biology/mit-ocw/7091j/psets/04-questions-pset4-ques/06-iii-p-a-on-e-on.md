---
title: (iii) P(A = ON | E = ON)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/04-questions-pset4-ques.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# (iii) P(A = ON | E = ON)

**Source:** `psets/04-questions-pset4-ques.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

4

**(C – 1 point)** For the rest of this problem, you will be using the Python module Pebl (<sup>https://code.google.com/p/pebl-project</sup> <u>/), which provides an environment for learning the</u> structure of a Bayesian network. Just like PyRosetta, Pebl has been installed on Athena, and we will provide instructions for how to complete this problem on Athena’s Dialup Service. You are, of course, free to download Pebl yourself and complete the problem locally.

Log on to Athena’s Dialup Service:

ssh <your Kerberos username>@athena.dialup.mit.edu

Before running any Python scripts, use the following command to add the Athena Pebl module to your PYTHONPATH:�

export PYTHONPATH=/afs/athena/course/20/20.320/pythonlib/lib/python2.7/site-packages/

If you forget to do this, you will get

ImportError: No module named pebl

when you try to run the provided scripts. Additional information about Pebl and its modules can be found here: https://pythonhosted.org/pebl/apiref.html#apiref.

You will also need to get the .zip containing the files for this problem in the course folder:

cd /afs/athena/course/7/7.91/sp_2014 cp bayesNetworks.zip ~ cd ~ unzip bayesNetworks.zip cd bayesNetworks

We have provided you with a small subset of the microarray data that were published in a 2000 paper (Gasch _et al._ - http://www.ncbi.nlm.nih.gov/pubmed/11102521 ). Gasch _et al_ . explored gene expression changes in _S. cerevisiae_ in response to a variety of environmental stresses, such as heat shock and oxidative stress. We have given you geneExprData.txt,� which contains data for 12 of the genes included in the study, observed under these various stress conditions.

We have also provided a simple script learnNetwork.py which will learn the network structure that best explains these data, using Pebl’s greedy learner algorithm (see https://pythonhosted.org/pebl/learner/greedy.html). From the folder containing geneExprData.txt, run the script:

python learnNetwork.py geneExprData.txt network1

If you’ve done this correctly, a new folder called network1 will be created in your current directory on Athena, containing an .html file and two more folders data and lib.��If you are at an Athena workstation, you can open and view the .html directly. If you’ve ssh’ed into Athena from your own computer, you will need to copy the entire outFolderName to your local computer using scp:

5

<in a new Terminal on your computer, cd into your local computer’s directory where you want to download the files> scp –r <your Kerberos username>@athena.dialup.mit.edu:~/bayesNetworks/network1 .

Now click on the .html file to open it. Include a printout of the top scoring network with your write-up or upload a photo of it to the course website online dropbox. What is its log score?

**(D – 1 point)** We have provided another data file, exprDataMisTCP1.txt,�which is the same as geneExprData.txt except the data for tcp1 has been removed.

- (i) Before using Pebl to calculate the network, make a quick guess about how the network might change in response to removing the tcp1 data.

(ii) Now, use the learnNetwork.py script to learn a network for exprDataMisTCP1.txt:�

python learnNetwork.py exprDataMisTCP1.txt network2

Again, if you ssh’ed into Athena, you will need to copy the network2 folder locally in order to view it:

<in a new Terminal on your computer, cd into your local computer’s directory where you want to download the PDF>

scp –r <your Kerberos username>@athena.dialup.mit.edu:~/bayesNetworks/network2 .

Include a printout of the top scoring network with your write-up or upload a photo of it to the course website online dropbox. According to this network, which node(s) does the expression of mcx1depend on? Is this consistent with your guess above? Briefly suggest a reason why you might be observing this network in response to loss of tcp1 data.

6

---

[← (ii) P(E = ON | A = ON)](05-ii-p-e-on-a-on.md) · [Up: contents](index.md) · [P2 – Refining Protein Structures in PyRosetta (7 points) →](07-p2-refining-protein-structures-in-pyrosetta-7-points.md)

---
title: P1 - Bayesian Networks (7 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/04-questions-pset4-ques.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `psets/04-questions-pset4-ques.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# P1 - Bayesian Networks (7 points)

## PROBLEM SET 4. Bayesian Networks, Refining Protein Structures in PyRosetta, Mutual information of protein residues (21 Points)

Due: Thursday, April 17th at noon.

### Python Scripts
All Python scripts must work on athena using /usr/athena/bin/python. You may not assume availability of any third party modules unless you are explicitly instructed so. You are advised to test your code on Athena before submitting. Please only modify the code between the indicated bounds, with the exception of adding your name at the top, and remove any print statements that you added before submission.

Electronic submissions are subject to the same late homework policy as outlined in the syllabus and submission times are assessed according to the server clock. Any Python programs you add code to must be submitted electronically, as .py files on the course website using appropriate filename for the scripts as indicated in the problem set or in the skeleton scripts provided on course website.

---

You are given two different Bayesian network structures 1 and 2, each consisting of 5 binary random variables A, B, C, D, E. Each variable corresponds to a gene, whose expression can be either "ON" or "OFF".

**Network 1**
(Directed graph with edges: $A \to C$, $A \to E$, $B \to D$, $C \to E$, $D \to E$)

**Network 2**
(Directed graph with edges: $A \to B$, $A \to C$, $A \to D$, $B \to D$, $D \to E$)

**(A – 2 points)** In class, we covered the chain rule of probability for Bayes Nets, which allows us to factor the joint probability over all the variables into terms of conditional probabilities. For each of the following cases, factor P(A,B,C,D,E) according to the independencies specified and give the **minimum number of parameters required to fully specify the distribution**.

(i) A,B,C,D,E are all mutually independent

(ii) A,B,C,D,E follow the independence assumptions of **Network #1** above

(iii) A,B,C,D,E follow the independence assumptions of **Network #2** above

(iv) no independencies

---

**(B – 3 points)** Using **Network #2** and the probabilities given below, calculate the probability of the following:

$$P(A = \text{ON}) = 0.6$$

$$P(B = \text{ON} \mid A) = \begin{cases} 0.1, & A = \text{OFF} \\ 0.95, & A = \text{ON} \end{cases}$$

$$P(C = \text{ON} \mid A) = \begin{cases} 0.8, & A = \text{OFF} \\ 0.5, & A = \text{ON} \end{cases}$$

$$P(D = \text{ON} \mid A, B) = \begin{cases} 0.1 & A = \text{OFF}, B = \text{OFF} \\ 0.9 & A = \text{ON}, B = \text{OFF} \\ 0.3 & A = \text{OFF}, B = \text{ON} \\ 0.95 & A = \text{ON}, B = \text{ON} \end{cases}$$

$$P(E = \text{ON} \mid D) = \begin{cases} 0.8, & D = \text{OFF} \\ 0.1, & D = \text{ON} \end{cases}$$

(i) P(A=ON, B=ON, C=ON, D=ON, E=ON)

(ii) P(E = ON | A = ON)

---

(iii) P(A = ON | E = ON)

---

**(C – 1 point)** For the rest of this problem, you will be using the Python module Pebl (https://code.google.com/p/pebl-project/), which provides an environment for learning the structure of a Bayesian network. Just like PyRosetta, Pebl has been installed on Athena, and we will provide instructions for how to complete this problem on Athena's Dialup Service. You are, of course, free to download Pebl yourself and complete the problem locally.

Log on to Athena's Dialup Service:

```
ssh <your Kerberos username>@athena.dialup.mit.edu
```

Before running any Python scripts, use the following command to add the Athena Pebl module to your `PYTHONPATH`:

```
export PYTHONPATH=/afs/athena/course/20/20.320/pythonlib/lib/python2.7/site-packages/
```

If you forget to do this, you will get
```
ImportError: No module named pebl
```
when you try to run the provided scripts. Additional information about Pebl and its modules can be found here: https://pythonhosted.org/pebl/apiref.html#apiref.

You will also need to get the .zip containing the files for this problem in the course folder:

```
cd /afs/athena/course/7/7.91/sp_2014
cp bayesNetworks.zip ~
cd ~
unzip bayesNetworks.zip
cd bayesNetworks
```

We have provided you with a small subset of the microarray data that were published in a 2000 paper (Gasch et al. - http://www.ncbi.nlm.nih.gov/pubmed/11102521). Gasch et al. explored gene expression changes in *S. cerevisiae* in response to a variety of environmental stresses, such as heat shock and oxidative stress. We have given you `geneExprData.txt`, which contains data for 12 of the genes included in the study, observed under these various stress conditions.

We have also provided a simple script `learnNetwork.py` which will learn the network structure that best explains these data, using Pebl's greedy learner algorithm (see https://pythonhosted.org/pebl/learner/greedy.html). From the folder containing `geneExprData.txt`, run the script:

```
python learnNetwork.py geneExprData.txt network1
```

If you've done this correctly, a new folder called `network1` will be created in your current directory on Athena, containing an `.html` file and two more folders `data` and `lib`. If you are at an Athena workstation, you can open and view the `.html` directly. If you've ssh'ed into Athena from your own computer, you will need to copy the entire `outFolderName` to your local computer using `scp`:

---

```
<in a new Terminal on your computer, cd into your local computer's directory where you want to download the files>
scp -r <your Kerberos username>@athena.dialup.mit.edu:~/bayesNetworks/network1 .
```

Now click on the `.html` file to open it. Include a printout of the top scoring network with your write-up or upload a photo of it to the course website online dropbox. What is its log score?

**(D – 1 point)** We have provided another data file, `exprDataMisTCP1.txt`, which is the same as `geneExprData.txt` except the data for tcp1 has been removed.

(i) Before using Pebl to calculate the network, make a quick guess about how the network might change in response to removing the tcp1 data.

(ii) Now, use the `learnNetwork.py` script to learn a network for `exprDataMisTCP1.txt`:

```
python learnNetwork.py exprDataMisTCP1.txt network2
```

Again, if you ssh'ed into Athena, you will need to copy the `network2` folder locally in order to view it:

```
<in a new Terminal on your computer, cd into your local computer's directory where you want to download the PDF>
scp -r <your Kerberos username>@athena.dialup.mit.edu:~/bayesNetworks/network2 .
```

Include a printout of the top scoring network with your write-up or upload a photo of it to the course website online dropbox. According to this network, which node(s) does the expression of mcx1 depend on? Is this consistent with your guess above? Briefly suggest a reason why you might be observing this network in response to loss of tcp1 data.

---

---

[Up: contents](index.md) · [P2 – Refining Protein Structures in PyRosetta (7 points) →](02-p2-refining-protein-structures-in-pyrosetta-7-points.md)

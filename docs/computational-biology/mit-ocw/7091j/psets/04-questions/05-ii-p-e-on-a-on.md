---
title: (ii) P(E = ON | A = ON)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/04-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# (ii) P(E = ON | A = ON)

**Source:** `psets/04-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- B, D, and E are conditionally independent of C given A, so C drops out. Therefore, we

- sum over the 4 {B, D} <u>possibilities:</u>

**P(E** = **ON| A** = **ON)** = ∑ **P(E** = **ON|D)P(D | A** = **ON,B)P(B | A** = **ON) B,D** = **{ON,OFF}**

|B|D|P(B|A=ON)|P(D|A=ON,B)|P(E=ON|D)|P(E=ON, B, D|A=ON)|
|---|---|---|---|---|---|
|ON|ON|0.95|0.95|0.1|0.09025|
|ON|OFF|0.95|0.05|0.8|0.038|
|OFF|ON|0.05|0.9|0.1|0.0045|
|OFF|OFF|0.05|0.1|0.8|0.004|


Summing over the last column, we obtain P(E=ON | A = ON) = 0.13675.

3

(iii) P(A = ON | E = ON)

By Bayes’ rule,

_P_ ( _A_ = _ON_ | _E_ = _ON_ ) =<sup>_P_</sup><sup><u>(</u></sup><sup>_E_=</sup><sup>_ON_|</sup><sup>_A_=</sup><sup>_ON_</sup><sup><u>)</u></sup><sup>_P_</sup><sup><u>(</u></sup><sup>_A_=</sup><sup>_ON_</sup><sup><u>)</u></sup> _P_ ( _E_ = _ON_ ) _P_ <u>(</u> _E_ = _ON_ | _A_ = _ON_ <u>)</u> _P_ <u>(</u> _A_ = _ON_ <u>)</u> = _P_ ( _E_ = _ON_ | _A_ = _ON_ ) _P_ ( _A_ = _ON_ ) + _P_ ( _E_ = _ON_ | _A_ = _OFF_ ) _P_ ( _A_ = _OFF_ )

We already have P(E=ON | A=ON) from (ii), so we just need P(E=ON | A=OFF):

|B|D|P(B|A=OFF)|P(D|A=OFF,B)|P(E=ON|D)|P(E=ON,B,D|A=OFF)|
|---|---|---|---|---|---|
|ON|ON|0.1|0.3|0.1|0.003|
|ON|OFF|0.1|0.7|0.8|0.056|
|OFF|ON|0.9|0.1|0.1|0.009|
|OFF|OFF|0.9|0.9|0.8|0.648|


Summing over the last column, we obtain P(E=ON | A=OFF) = 0.716.  Therefore

**<u>(0.13675)(0.6)</u> P(A** = **ON|E** = **ON)** = = **0.2227** **<u>(0.13675)(0.6)</u>** + **<u>(0.716)(0.4)</u>**

4

**(C – 1 point)** For the rest of this problem, you will be using the Python module Pebl (https://code.google.com/p/pebl-project/), which provides an environment for learning the structure of a Bayesian network. Just like PyRosetta, Pebl has been installed on Athena, and we will provide instructions for how to complete this problem on Athena’s Dialup Service. You are, of course, free to download Pebl yourself and complete the problem locally.

Log on to Athena’s Dialup Service:

ssh <your Kerberos username>@athena.dialup.mit.edu

Before running any Python scripts, use the following command to add the Athena Pebl module to your PYTHONPATH:

export PYTHONPATH=/afs/athena/course/20/20.320/pythonlib/lib/python2.7/site-packages/

If you forget to do this, you will get

ImportError: No module named pebl

when you try to run the provided scripts. Additional information about Pebl and its modules can be found here: https://pythonhosted.org/pebl/apiref.html#apiref .

You will also need to get the .zip containing the files for this problem in the course folder:

cd /afs/athena/course/7/7.91/sp_2014 cp bayesNetworks.zip ~ cd ~ unzip bayesNetworks.zip cd bayesNetworks

We have provided you with a small subset of the microarray data that were published in a 2000 paper (Gasch _et al._ - http://www.ncbi.nlm.nih.gov/pubmed/11102521). Gasch _et al_ . explored gene expression changes in _S. cerevisiae_ in response to a variety of environmental stresses, such as heat shock and oxidative stress. We have given you geneExprData.txt, which contains data for 12 of the genes included in the study, observed under these various stress conditions.

We have also provided a simple script learnNetwork.py which will learn the network structure that best explains these data, using Pebl’s greedy learner algorithm (see https://pythonhosted.org/pebl/learner/greedy.html). From the folder containing geneExprData.txt, run the script:

python learnNetwork.py geneExprData.txt network1

If you’ve done this correctly, a new folder called network1 will be created in your current directory on Athena, containing an .html file and two more folders data and lib. If you are at an Athena workstation, you can open and view the .html directly. If you’ve ssh’ed into Athena from your own computer, you will need to copy the entire outFolderName to your local computer using scp:

5

<in a new Terminal on your computer, cd into your local computer’s directory where you want to download the files>

scp –r <your Kerberos username>@athena.dialup.mit.edu:~/bayesNetworks/network1 .

Now click on the .html file to open it. Include a printout of the top scoring network with your write-up or upload a photo of it to the Stellar online dropbox. What is its log score?

Log score = -1966.216


6

**(D – 1 point)** We have provided another data file, exprDataMisTCP1.txt, which is the same

as geneExprData.txt except the data for tcp1 has been removed.

- (i) Before using Pebl to calculate the network, make a quick guess about how the network might change in response to removing the tcp1 data.

We might assume that we will simply see edges from tcp1’s parents going directly to mcx1. In other words, mcx1 expression would depend only on cct8 and cct4.

- (ii) Now, use the learnNetwork.py script to learn a network for exprDataMisTCP1.txt:

python learnNetwork.py exprDataMisTCP1.txt network2

- Again, if you ssh’ed into Athena, you will need to copy the network2 folder locally in order to view it:

<in a new Terminal on your computer, cd into your local computer’s directory where you want to download the PDF> scp –r <your Kerberos username>@athena.dialup.mit.edu:~/bayesNetworks/network2 .

Include a printout of the top scoring network with your write-up or upload a photo of it to the Stellar online dropbox. According to this network, which node(s) does the expression of mcx1 depend on? Is this consistent with your guess above? Briefly suggest a reason why you might be observing this network in response to loss of tcp1 data.

7


When we lose the tcp1 data, we obtain a network in which mcx1 depends on a number of other nodes, not just the parents of tcp1. Losing tcp1, brought together diverse sources of information, makes all the relationships between mcx1 and ancestors of tcp1 more noisy, and makes it harder to tell which are real and which aren’t – in this case, it appears that a number of them have some contribution to the value of mcx1.

8

---

[← (i) P(A=ON, B=ON, C=ON, D=ON, E=ON)](04-i-p-a-on-b-on-c-on-d-on-e-on.md) · [Up: contents](index.md) · [P2 – Refining Protein Structures in PyRosetta (7 points) →](06-p2-refining-protein-structures-in-pyrosetta-7-points.md)

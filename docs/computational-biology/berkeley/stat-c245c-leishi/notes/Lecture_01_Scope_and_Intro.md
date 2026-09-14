---
title: 'PH240C: Scope and Introduction'
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_01_Scope_and_Intro.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_01_Scope_and_Intro.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PH240C: Scope and Introduction

**Source:** [`notes/Lecture_01_Scope_and_Intro.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_01_Scope_and_Intro.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Jingshen Wang 09/01/2021


1

## **Class Policy**

###### Homework assignments (65%):

- Biweekly

- The lowest score will be dropped in the final grade, and one late homework (24 hour) is allowed.

- It is encouraged to discuss the problem sets with others, but everyone needs to turn in a unique personal write-up.

- Final project write-up and presentation(35%): take home, open books, open notes.

2

## **Labs**

- Supervised Learning (classical approaches)

1. GLM/SVM (09/08)

Please fill in the lab time change pool!

2. Kernel-based Methods (09/15)

3. Metric Learning (09/22)

###### **3 Labs**

4. Tree-based Methods (09/29, 10/06)

- Semi-supervised Learning (10/13)

1. Neural Networks (10/20)

###### **1 Labs**

2. Deep Neural Networks (10/27)

- Causal Inference and Clinical Trials

1. Nature’s Experiments: Mendelian Randomization (11/10) 2. Bayesian Inference and Design of Experiments (11/17) 3. Adaptive Clinical Trial and Reinforcement Learning (12/01)

###### **2 Labs**

## **What is Machine Learning?**


<!-- Start of picture text -->
‣ The concept of ML is not<br>new<br><!-- End of picture text -->

‣Arthur Samuel (1959): Machine Learning is the field of study that gives the computer the ability to learn without being explicitly programmed


<!-- Start of picture text -->
?<br><!-- End of picture text -->

4

## **Change Points of ML — Image Recognition**

The trained  deep convolutional neural network provides much more accurate prediction than the previous methods

5

## **What does it mean for medicine and healthcare?**

Studies relied on Deep Learning have showcased its ability to

‣ Diagnose some types of skin cancer

‣ Identify specific heart-rhythm abnormality like cardiologists ‣ Interpret medical scans or pathology slides like highly qualified radiologists

‣ Diagnose various eye disease as well as ophthalmologist

‣ ….

Nevertheless, machine learning methods need to be powered by big data

6

## **One example**


7

### **Geographic Information System of a Human Being**


8

## **Where do Data Come from?**


<!-- Start of picture text -->
Patients have symptoms, acute illness, etc.<br>Encounter with health professionals<br>Examination, history, diagnostics<br>Diagnosis<br>Interventions including drug prescribing<br>Paperless records<br>EMR Claims and billing for insurance<br>Research Data Base: Electronic Health Record Data<br><!-- End of picture text -->

9

## **Electronic Health Record Data**

EHR stands for electronic health record. According to Wikipedia:

‣ EHR is the systematized collection of patient and population electronically-stored health information in a digital format. ‣These records can be shared across different health care settings. Records are shared through network-connected, enterprise-wide information systems or other information networks and exchanges.

10

## **Reality in EHR data**


Lab Results


Doctors’ Diagnosis (NLP)


Need to be linked

Baseline Biomarkers

11

## **What do we want to learn/gain from data?**


12

## **What do we want to learn/gain from data?**

###### **Learning objects in this class:**

1. Disease risk (early) prediction/diagnosis — Supervised Learning

2. Utilize massive undiagnosed patient information to improve prediction — Semi-supervised Learning

3. Guide future clinical decisions — causal inference and clinical trial design

13

## **We need tools to achieve these goals**

###### **Supervised Learning (classical approaches)**

1. GLM/SVM

2. Kernel-based Methods

3. Metric Learning

4. Tree-based Methods

**Example 1. The prime example: house price prediction**

- Suppose we have data about

- (1) Features  — square footage, number of rooms, features, whether a house has a garden or not _X_ (2) Labels/Outcomes  — the prices of these houses _Y_ By leveraging data coming from thousands of houses, we can train a supervised machine learning model to predict a new house’s price based on the examples observed by the model.

14

## **Example: Text as data**

##### **Example 2. Text as data**

Can you tell who wrote the following sentences? Jane Austen from _Pride and Prejudice_ or J. K. Rowling from _Harry Potter_ ?

“The thought of the confined creature was so dreadful to him…”

“…was as if something turned over, and the point of view altered…”

15

## **Examples: Text as data (predictors)**


##### You will work on these text data in your labs with your GSI, and make predictions on your own

16

## **Example: Disease risk prediction**

**Example 3. Disease risk prediction** We are given massive biobank data for patients with stroke history that contain information:

1. _Y_ ∈{0,1}: if the patient has developed Alzheimer’s disease at the time of recruit

2. _X_ ∈ℝ<sup>_p_</sup> : covariates information including individual lifestyles (insomnia, current smoking status, beef lover, etc.), baseline biomarker information (gender, age, education, and family AD history), and genetic information (SNPs)

Goal:

1. Predict which patients that are at high risk of developing AD (why important?)

2. Find any lifestyle factors can reduce the risk of AD How about the other patients that are not diagnosed? Can we use their information to improve our prediction?

17

## **Semi-supervised Learning**

###### **Semi-supervised Learning**

In medical record database, we often encounter the following scenario:

1. Labeled data { _Yi_ , _Xi_ }<sup>_n_</sup> _i_ =1 — _Yi_ ∈{0,1} represents if the patient is diagnosed with certain disease at the time of recruit, and _Xi_ ∈ℝ<sup>_p_</sup> represents patient all available information

2. Unlabeled data — represents unlabeled patient information { _Xj_ }<sup>_n_+</sup><sup>_N_</sup> _Xj_ ∈ℝ<sup>_p_</sup> _j_ = _n_ +1

Question: Can we improve the prediction results given massive amount of unlabeled data? If so, when?

18

#### **Learning objectives in the first half of the semester**

##### **Supervised Learning (classical approaches)**

1. GLM/SVM (09/08)

2. Kernel-based Methods (09/15)

3. Metric Learning (09/22)

4. Tree-based Methods (09/29, 10/06)

**Semi-supervised Learning (10/13)**

And then?

19

## **Alzheimer’s disease: a little more detail..**


Alzheimer’s disease is a neurodegenerative disease often characterized by dementia, accumulation of beta-amyloid ( _Aβ_ ) plaques and tau proteins on neurons, and brain inflammation and atrophy.

20

## **Neural Networks (1)**

###### **Collective force of synapses**


<!-- Start of picture text -->
X 1 ⋅ w 1<br>Synapse1<br>X 1 ∈{0,1}<br>w<br>The weight  models the<br>synaptic connection, either<br>strong or weak<br>⋮<br>Synapse n Xn  ⋅ wn<br>Xn  ∈{0,1}<br><!-- End of picture text -->

Measure the influence of the synapses—decide whether or not the whole axon is stimulated

###### **Output**


<!-- Start of picture text -->
n 1<br> if  ∑ n<br>i =1 wiXi  > threshold<br>Decide if  wiXi  > threshold<br>∑<br>0<br> if  ∑ n<br>i =1 Z  = { i =1 wiXi  ≤ threshold<br><!-- End of picture text -->

###### **Three elements in a neural network:**

1. Each synapse has some influence on the final output

2. Cumulative influence simulate the axon

3. Synaptic weight

21

## **Neural Networks (2)**


<!-- Start of picture text -->
Inputs<br>(A simple?) Brain<br>Synapse1<br>Z 1<br>X 1 ∈{0,1} w 1<br>w 2<br>T 32<br>Tn<br>⋮<br>⋮ T 1<br>wn<br>Zm<br>Synapse n<br>Xn  ∈{0,1}<br><!-- End of picture text -->

**Neural Network (NN)** A NN learns the functional form of


where we need to adjust the weights _wi_ and the thresholds  so that what we get out is _Ti_ the outcome . _Zj_

22

## **Example: Disease risk prediction with NN**

**Example 3. Disease risk prediction (revisit)** We are given massive biobank data for patients with stroke history that contain information:

1. _Y_ ∈{0,1}: if the patient has developed Alzheimer’s disease at the time of recruit

2. _X_ ∈ℝ<sup>_p_</sup> : covariates information including individual lifestyles (insomnia, current smoking status, beef lover, etc.), baseline biomarker information (gender, age, education, and family AD history), and genetic information (SNPs)

To have binary input, we can transform the covariates into dummy variables. Can we still obtain the effect of certain lifestyle on lowering the disease risk?

23

## **Deep Neural Networks**


24

## **Deep Neural Networks**


25

## **Challenges in Research**


1. MD Anderson taps IBM Watson to power "Moon Shots" mission aimed at ending cancer, starting with Leukemia

2. Big data insights to help accelerate translation of cancer-fighting knowledge to cutting edge medical practices


3. Link to the news: https://www.ibm.com/products/clinical-decision-support-oncology

4. IBM’s Watson supercomputer recommended ‘unsafe and incorrect’ cancer treatments, internal documents show

How to make machine learning methods more trustworthy?

26

## **Learning objectives**

1. Neural Networks (10/20)

- Convolutional Networks, Recurrent Networks, and their applications in medical research

2. Deep Neural Networks (10/27)

###### **Observational data**

1. Disease risk prediction — supervised learning (including NN and DNN), semi-supervised learning

2. Learning effective treatments for different patients

**?**

1. Will you trust the findings from

   - observational data?

2. If not, what can we do?

3. How can we guide future clinical decisions?

27

## **Effect of Smoking on Life Expectancy?**


28

## **What hinders our understanding?**


<!-- Start of picture text -->
Confounding factors<br>Smokers tend to drink more heavily and have<br>a less healthy diet<br>Randomized experiment is not feasible<br>Smoking cannot be randomly assigned to<br>individual — neither practical nor ethical<br>Reverse Causation<br>When people become ill, they tend to give up<br>smoking. This wrongly suggests smoking worsen<br>health.<br><!-- End of picture text -->


<!-- Start of picture text -->
Smoking<br><!-- End of picture text -->


<!-- Start of picture text -->
Shortened<br>Life Expectancy<br><!-- End of picture text -->

29

## **Last learning objectives**

###### Causal Inference and Clinical Trials

1. Nature’s Experiments: Mendelian Randomization (11/10)

2. Bayesian Inference and Design of Experiments (11/17)

3. Adaptive Clinical Trial and Reinforcement Learning (12/01)

###### **Observational data**

1. Disease risk prediction — supervised learning (including NN and DNN), semi-supervised learning

2. Learning effective treatments for different patients

###### **Causal Inference**

1. Randomized control trials (RCT) can help us to verify our finds from observation study

2. When RCT is not available, we may rely on Nature’s experiment (Mendelian Randomization)


<!-- Start of picture text -->
Reinforcement<br><!-- End of picture text -->

30

## **Mendelian Randomization: Popularity**


31

## **Mendelian Randomization**

###### **Randomly** inherited genes are **not** associated with any confounding factors


<!-- Start of picture text -->
Smokers who carry one version of<br>CHRNA5 tend to smoke less heavily<br>than those who carry a different version<br>Shortened Life<br>Smoking<br>Expectancy<br>Different variant of CHRNA5 in non-<br>smokers has no effect on life expectancy<br><!-- End of picture text -->


<!-- Start of picture text -->
CHRNA5<br><!-- End of picture text -->

32

## **Labs**

- Supervised Learning (classical approaches)

1. GLM/SVM (09/08)

Please fill in the lab time change pool!

2. Kernel-based Methods (09/15)

3. Metric Learning (09/22)

###### **3 Labs**

4. Tree-based Methods (09/29, 10/06)

- Semi-supervised Learning (10/13)

1. Neural Networks (10/20)

###### **1 Labs**

2. Deep Neural Networks (10/27)

- Causal Inference and Clinical Trials

1. Nature’s Experiments: Mendelian Randomization (11/10) 2. Bayesian Inference and Design of Experiments (11/17) 3. Adaptive Clinical Trial and Reinforcement Learning (12/01)

###### **2 Labs**

---

[Up: contents](../index.md)

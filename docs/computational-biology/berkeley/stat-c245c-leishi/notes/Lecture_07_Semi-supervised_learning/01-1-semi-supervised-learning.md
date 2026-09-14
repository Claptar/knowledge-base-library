---
title: 1 Semi-supervised Learning
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_07_Semi-supervised_learning.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_07_Semi-supervised_learning.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Semi-supervised Learning

**Source:** [`notes/Lecture_07_Semi-supervised_learning.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_07_Semi-supervised_learning.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **1.1 Overview**

As the name suggests, semi-supervised learning is a machine learning method that stands between unsupervised and supervised learning, and can also be called as classification with labelled and unlabelled data (or partially labelled data). Semi-supervised learning has tremendous practical value. In many tasks, there is a paucity of labelled data. The labels _Y_ may be difficult to obtain because they require human annotators, special devices, or expensive and slow experiments. For example,

- In speech recognition, an instance _X_ is a speech utterance, and the label _Y_ is the corresponding transcript. For example, here are some detailed phonetic transcript of words as they are spoken:

film _⇒_ f ih_n uh_gl_n m _._

Accurate transcription by human expert annotators can be extremely time consuming: it took as long as 400 hours to transcribe 1 hour of speech at the phonetic level for a recordings of randomly paired participants discussing various topics such as social, economic, political, and environmental issues Godfrey et al. (1992).

- In spam filtering, an instance _X_ is an email, and the label _Y_ is the user’s judgment (spam or ham). In this situation, the bottleneck is an average user’s patience to label a large number of emails.

- In healthcare, given the vast accessibility of electronic health record data, labeled disease status are rather sparse. How to use the labelled disease status to infer the unlabelled patients is of vital interest (Ford et al., 2016).

While labelled data pair is difficult to obtain in these examples, unlabelled data _X_ are available in large quantity and easy to collect: speech utterance can be recorded from radio broadcasts. Semi-supervised learning is attractive because it can potentially utilize both labeled and un labeled data to achieve better performance than supervised learning. From a different perspective, semi-supervised learning may achieve the same level of performance as supervised learning, but with fewer labelled instances. This reduces the annotation effort, which leads to reduced cost.

Semi-supervised learning also provides a computational model of how humans learn from labelled and unlabeled data. Consider the task of concept learning in children, which is similar to classification: an instance x is an object (e.g., an animal), and the label y is the corresponding concept (e.g., dog). Young

1


Figure 1: A simple example to demonstrate how semi-supervised learning is possible.

children receive labeled data from teachers (e.g., Daddy points to a brown animal and says “dog!”). But more often they observe various animals by themselves without receiving explicit labels. It seems self-evident that children are able to combine labeled and unlabeled data to facilitate concept learning. The study of semi-supervised learning is therefore an opportunity to bridge machine learning and human learning.

### **1.2 Why semi-supervised learning can be helpful?**

At first glance, it might seem paradoxical that one can learn anything about a classifier from unlabeled data. After all, a classifier _f_ is about the mapping from the instance _X_ to the label _Y_ , yet unlabeled data do not provide any example of such a mapping. The answer lies in the assumptions one makes about the _link between the distribution of unlabeled data and the target label_ .

Figure 1 shows a simple example of semi-supervised learning. Let each instance be represented by a one-dimensional attribute _X ∈_ R. They are two classes _Y ∈{−_ 1 _,_ 1 _}_ . Consider the following two scenarios:

1. In supervised learning, we are only given two labeled training instance ( _X_ 1 _, Y_ 1) = ( _−_ 1 _, −_ 1) and ( _X_ 2 _, Y_ 2) = (1 _,_ 1). The best decision boundary is at _x_ = 0.

2. In addition, we are also given a large number of unlabeled instances, shown as green dots in the figure. The correct class labels for these unlabeled examples are unknown. However, we observe that they form two groups. If we **assume** that subjects in each class form a coherent group (for example the conditional distribution P( _X|Y_ = 1) has finite variance), this unlabeled data gives us more information. Specifically, it seems that the two labeled instances are not the most prototypical examples for the two considered classes. The semi-supervised estimate of the decision boundary should be between the two groups instead at _x ≈_ 0 _._ 4.

If our assumption is true, then using both labeled and unlabeled data gives us a more reliable estimate of the decision boundary. Intuitively, the distribution of unlabeled data helps to find a good division of the attribute space, and then the few labeled data then provide actual labels. Of course, this is merely one assumption considered in an ocean of literature on semi-supervised learning.

### **1.3 Inductive and transductive semi-supervised learning**

We now move forward with introducing two slightly different semi-supervised leaning setups, namely inductive and transductive semi-supervised learning. Recalled that in supervised learning, the training sample is

2

fully labeled, so one is always interested in the performance on future test data. In semi-supervised classification, however, the training sample contains some unlabeled data. Therefore, there are two distinct goals:

1. Inductive semi-supervised learning. Given a training sample with labeled part _{_ ( _Xi, Yi_ ) _}_<sup>_n_</sup> _i_ =1<sup>,and</sup> unlabeled part _{Xj}_<sup>_N_</sup> _j_ = _n_ +1<sup>,inductivesemi-supervisedlearninglearnsaclassifierthatpredictswellon</sup> **future** data, beyond _{Xj}_<sup>_N_</sup> _j_ = _n_ +1<sup>.</sup>

2. Transductive learning. Given a training sample with labeled part _{_ ( _Xi, Yi_ ) _}_<sup>_n_</sup> _i_ =1<sup>,andunlabeledpart</sup> _{Xj}_<sup>_N_</sup> _j_ = _n_ +1<sup>,transductivesemi-supervisedlearninglearnsaclassifierthatpredictswellon</sup><sup>**unlabeled**</sup> data _{Xj}_<sup>_N_</sup> _j_ = _n_ +1<sup>.</sup>

There is an interesting analogy: inductive semi-supervised learning is like an in-class exam, where the questions are not known in advance, and a student needs to prepare for all possible questions; in contrast, transductive learning is like a take-home exam, where the student knows the exam questions and needs not prepare beyond those.

### **1.4 Self-training models**

Self-training is characterized by the fact that the learning process uses its own predictions to teach itself. For this reason, it is also called self-teaching or bootstrapping (not to be confused with the statistical procedure with the same name). Self-training can be either inductive or transductive, depending on the problem:

1. Input labeled data _{_ ( _Xi, Yi_ ) _}_<sup>_n_</sup> _i_ =1<sup>andunlabeleddata</sup><sup>_{Xj}N_</sup> _j_ = _n_ +1

2. Define the initial labeled set as _L_ = _{_ 1 _, . . . , n}_ and the initial unlabeled set as _U_

3. Repeat the following steps that iteratively update the labeled set and the unlabeled set:

   - (a) Train _f_ from the data points in _L_ using supervised learning

   - (b) Apply _f_ to the unlabeled instances in _U_

   - (c) Remove a subset _S_ that is confidently labeled from _U_

   - (d) Add _{_ ( _Xi, f_ ( _Xi_ )) _|Xi ∈ S}_ to _L_

The main idea is to first train a classifier on labeled data. The function _f_ is then used to predict the labels for the unlabeled data. A subset _S_ of the unlabeled data, together with their predicted labels, are then selected to augment the labeled data. Typically, _S_ consists of a few unlabeled instances with the most confidence _f_ predictions. The function _f_ is then re-trained on the now larger set of labeled data, and the procedure repeats. This procedure looks quite intuitive, but it also relies on the **assumption** that the labeled dataset prediction results tend to be correct, at least for the high confidence ones. This is likely to be the case when the classes from well-separated clusters.

The major advantages of self-training are its simplicity, and the choice of the classifier for _f_ in Step 3(b) is left completely open. For example, the classifier can be a simple kNN algorithm, or a very complicated classifier. The self-training procedure “wraps” around the classifier without changing its inner workings. The disadvantage is also clear: the early mistake an algorithm makes can be reinforced by keep generating incorrectly labeled data. Re-training with wrongly classified data will lead to an even worse _f_ in the next iteration.

A concrete example of self-training, we now introduce an algorithm with a simple example:

3


Figure 2: Semi-supervised learning algorithm with a 1-nearest-neighbour classifier.

1. Input labeled data _{_ ( _Xi, Yi_ ) _}_<sup>_n_</sup> _i_ =1<sup>,unlabeleddata</sup><sup>_{Xj}N_</sup> _j_ = _n_ +1<sup>andadistancefunction</sup><sup>_d_(</sup><sup>_·_)</sup>

2. Define the initial labeled set as _L_ = _{_ 1 _, . . . , n}_ and the initial unlabeled set as _U_

3. Repeat the following steps until _U_ is empty:

   - (a) Select _X_ = arg min min _X ′∈L d_ ( _X, X_<sup>_′_</sup> ) _X∈U_

   - (b) Set _f_ ( _X_ ) to be the labels of _X_ ’s nearest instance in _L_

   - (c) Remove _X_ from _U_ , and add _{X, f_ ( _X_ ) _}_ to L.

See a simple illustrative example in Figure 2.

### **1.5 Semi-supervised learning in healthcare**

Suppose we have patient cohorts from two large hospitals. Our goal is to predict the status for bipolar disorder, a heritable mental disorder characterized by mood swings between mania and depression. Similar attributes are collected at both sites including age, gender, race, count of the diagnostic code for bipolar disorder and count of the major depressive disorder or depression. At one site, clinical investigators have manually labelled the binary disease status for _n_ patients, and the other site, we have access to _N − n_ additional patient attributes. In this example, we focus on transductive learning as its goal is more aligned with healthcare at large.

To have a concrete statistical model, suppose the labeled data are denoted as _{_ ( _Xi, Yi_ ) _}_<sup>_n_</sup> _i_ =1<sup>,andthe</sup> unlabeled data are denoted as _{Xj}_<sup>_N_</sup> _j_ = _n_ +1<sup>.Here</sup><sup>_Xi∈_R</sup><sup>_p_capturestheattributesand</sup><sup>_Yi∈{−_1</sup><sup>_,_1</sup><sup>_}_isthe</sup> corresponding label. We use _Si_ to denote whether a data point _i_ is labeled:


Again, semi-supervised learning only improves the prediction accuracy under certain assumption. From our motivating example, we assume that given a set of attributes _Xi_ = _x_ either from labeled or unlabeled

4

dataset, the probability of _Yi_ = 1 does not change, i.e.,


In other words, we assume that there is an underlying true status of patients disease profile regardless of whether his/her label is missing (when will this assumption be violated?). Nevertheless, given the patient information is collected across different locations, their baseline profile may differ accrediting to whether they are labeled or not. Thus, it is reasonable to expect that there is a covariate shift between two sites:


Our goal here is to accurate predict the disease status for unlabeled patients, i.e., we aim to find a classifier _f_ 0( _·_ ) that minimizes the empirical risk conditional on the data are unlabelled:


We can further start from the class of linear classifiers, then the problem can be simplified into


Note that different from supervised learning approaches used in previous lectures, _Yj_ is unobserved and the expectation function cannot be replaced by its sample analogue. Fortunately, under covariate shift, we have


Hence, as long as we can approximate the covariate shift between the labeled and unlabeled data, we may try to find w0 by minimizing the following objective function


Now the question remains is how to approximate the covariates shift especially when we have access to many attributes. What ideas do you have?

Multiple researchers have informally noted that semi-supervised learning does not always help. Little is written about it, except a few papers like Cozman et al. (2003); ELWORTHY (1994). This is presumably due to “publication bias,” that negative results tend not to be published. A deeper understanding of when semi-supervised learning works merits further study.

5

---

[Up: contents](index.md) · [References →](02-references.md)

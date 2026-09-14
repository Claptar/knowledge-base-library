---
title: 2 Online streaming data analysis with continuous outcomes
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_11_Streaming_Data_Analyses_in_Electronic_Medical_Record_Data.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_11_Streaming_Data_Analyses_in_Electronic_Medical_Record_Data.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Online streaming data analysis with continuous outcomes

**Source:** [`notes/Lecture_11_Streaming_Data_Analyses_in_Electronic_Medical_Record_Data.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_11_Streaming_Data_Analyses_in_Electronic_Medical_Record_Data.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We start with a simple (may be unrealistic, but always good to start with something simple and then generalize) scenario that we can update the health system on a daily basis Suppose in a streaming data environment, we have access to a continuous outcome variable _yit_ and a vector of attributes _xit ∈_ R<sup>_p_</sup> observed at _t_ = 1 _, . . . , m_ for subject _i_ = 1 _, . . . , n_ . Typically, medical practitioner might be interested in

1. How do outcome measures change over time? Is there a pattern associated with it?

2. How do the outcome measure depend on the covariates over time?

For example, the severity of a disease often depends on the patient’s nutritional status, age, gender and family income, and these information might be observed once every few month. Naturally, the dependence of the outcome variable, severity of disease on the covariates is of interest.

In classical statistics, we would work with a linear model that assumes


The problem of such a modelling assumption is that it restricts the flexibility of our analysis. For example, in a situation that _yit_ measures the patients CD4 counts in HIV patients, and _xit_ measures the transportation

2

cost to travel to the clinic for picking up medication. We would expect the influence of transportation cost on the CD4 count changing over time when COVID hits.

A natural alternative of this linear model is to replace the constant _β_ with _βt_ so that the coefficient is allowed to change over time:


Traditionally speaking, such a dynamic changing coefficient model is referred to as the varying coefficient model. If we have the data for the patient entire trajectory (Wu et al., 1998), we may simply estimate the coefficient through


where _K_ ( _·_ ) is a kernel function in a nonparametric sense and is a non-negative real-valued integrable function. Typically, it is desirable to define the kernel function that satisfies two constraints:

1. Normalization: �R<sup>_K_(</sup><sup>_u_)d</sup><sup>_u_= 1</sup>

2. Symmetry: _K_ ( _−u_ ) = _K_ ( _u_ ) for all values of _u_

Think about why we put down these two constraints in practice? And the resulting estimator has the form:


where _Ki_ ( _t_ ; _h_ ) = Diag ( _Ki_ 1( _t_ ; _h_ ) _, . . . , Ki,_ ( _t_ ; _h_ )). However, in an online learning environment, at time point _t_ , we cannot expect to have access to the patient future data. Such an estimate is thus not feasible in practice. This motivate us to consider a one-sided kernel function instead of the traditional kernel function:


Incorporating the weighting function _λ_<sup>_t−j_</sup> into the loss function enables us to dynamically down weight the observations far away from the current time updating time point _t_ . Although such a weighting scheme is just one choice among a broad class of weighting functions, its benefit will be apparent in the following derivations. Recall our task in the streaming data environment is to find scalable, it admits a recursive expression which allows to sequentially update the previous batch estimator _β_<sup>�</sup> _t−_ 1 when the new data batch arrives:


3


Figure 2: Example of changes shown in Gama et al. (2014).

And the prediction interval for future patient can be constructed by


Thus, such a recursive form allows us to conduct online statistical (predictive?) inference. Nevertheless, finding an optimal tuning parameter _λ_ is not an easy task in practice. Intuitively, what kind of _λ_ appeals e to you?

### **2.1 Connection with existing machine learning literature**

In a recent ML survey, Gama et al. (2014) has discussed the issues of online learning when “concept drift” happens. Formally, because data is expected to evolve over time, especially in dynamically changing environment, where non-stationary is typically, its underlying distribution can change dynamically over time. Suppose between time point _t_ 0 and _t_ 1, there exist an attribute such that the joint distribution of ( _X, y_ ) change over time, that is


where _pt_ ( _·, ·_ ) denotes the joint distribution at time _t_ 0 between the set of attribute variable _X_ and the target variable _y_ . Changes in data can thus be characterized as changes in the component of this relation. In the literature, there are two types of drift:

1. Real concept drift refers to the changes in _p_ ( _y|X_ ).

2. Virtual drift happens if the distribution of the incoming data changes, i.e., _p_ ( _X_ ).

There are, of course, different kind of drift/changes may happen over time. For example, Figure 2 demonstrates different types of changes. Does the introduce model setup cover these changes? If not, how would you propose to change this model?

---

[← 1 An example with HIV care engagement in electronic medical record data](02-1-an-example-with-hiv-care-engagement-in-electronic-medical.md) · [Up: contents](index.md) · [3 More challenging online streaming data analysis in healthcare with binary outcomes →](04-3-more-challenging-online-streaming-data-analysis-in-healthc.md)

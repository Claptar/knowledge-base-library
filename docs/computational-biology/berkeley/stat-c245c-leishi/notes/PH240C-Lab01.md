---
title: PH240C LAB 01
source: https://leishi-rocks.github.io/courses/ph240c/notes/PH240C-Lab01.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/PH240C-Lab01.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PH240C LAB 01

**Source:** [`notes/PH240C-Lab01.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/PH240C-Lab01.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Sep 14, 2021


Agenda:

- <u>About the labs</u>

- <u>Final project policy</u>

- <u>Review of lectures + More on GLM</u>

- <u>Computation aspects</u>

- <u>Homework 1 hints</u>


## **About the labs…**

- GSI: Lei Shi, 2nd year Ph.D. in Biostats

- Schedule: Biweekly


- Mode: Hybrid + Recorded, but encourage in-person participation

- What will we do in labs?

   - Review lectures and walk little bit further

   - More interesting topics and examples

   - Homework hints!


## **Final project policy**

- Final project write-up and presentation takes up 35% of the final grade

- Presentation date: Dec 08

- Teams: 1 or 2 persons. Larger group size needs permission.

- Topic: Analyze data using modern statistical learning algorithms.

   - Highly recommend: finding your own data(from your projects or asking companies for help) If not possible you could use our assigned data too.


## **Review of the lectures**

• Classification: We have data ( _Xi_ , _Yi_ ) from some unknown distribution . _F Yi_ ∈{0,1} are binary.


- We hope to find a classifier _h_ ∈ℋ to minimize the generalization risk .

- _R_ ( _h_ , _F_ ) = _EF_ (1{ _Y_ ≠ _h_ ( _X_ )})


## **Review of the lectures**

- Logistic regression:


_E_ ( _Y_ ∣ _X_ ) = _μ_ ( _X_ ) ∈[0,1], _Y_ ∣ _X_ ∼ Bernoulli( _μ_ ( _X_ )) . exp( _X_ ′ _<u>β</u>_ ) Choosing _μ_ ( _X_ ) = expit( _X_ ′ _β_ ) = gives logistic regression. 1 + exp( _X_ ′ _β_ )

- Given the data, We obtain an estimator  with maximum likelihood estimation _β_

- • The classifier is then given by


<!-- Start of picture text -->
 that separates the<br><!-- End of picture text -->

## **Review of the lectures**

- Support vector machines: find hyperplane 𝒜 that separates the training data and maximize the minimal margin

- • Mathematically we solve optimization:


- In many cases we cannot find or deliberately avoid separating plane by introducing soft constraints:


<!-- Start of picture text -->
β<br><!-- End of picture text -->

## **More on logistic regression**

- If we have high dimensional covariates, we want a sparse  (a _β_ parsimonious and more interpretable model)

- Example: use gene expression levels(thousands of covariates) to predict certain disease.

- LASSO on GLM: Adding _ℓ_ 1 penalty on the log likelihood:


- + _λ_ ∥ _b_ ∥1


## **Computation aspects**

- Logistic regression can be solved with Newton-Raphson.

- SVM can be solved by quadratic programming(QP).

   - A Kernel trick can be applied to adapt to nonlinear classifiers. Here’s a link for <u>SVM in R.</u>

- We have existing R packages for GLM(stats, glmnet) and SVM(e1071).

- See our R code file: glm_svm.r.

- Test classification reference:

   1. <u>Text classification with tidy data principles</u>

   2. <u>Practicing sentiment analysis with Harry Potter</u>


## **Homework 1 hints**

- Problem 1: Predicting GPA


- Recall how to predict a success probability with a logistic model

- • <u>Here “odds” means odds ratios!</u>

- Build an equation and solve for _X_ 1. Please give the numerical result(i.e. no logs or exps).


## **Homework 1 hints**

- Problem 2: SVM


- <u>Graph paper not required. Three regions related to a hyperplane.</u> How to determine the signs:

   - A dumb try always works

   - Geometric interpretation

- Recall what is margin. Consider how to calculate distance between paralleled planes.

- Use the hyperplane!

- Two ways of calculating slack variable here:

   - A hinge loss interpretation from wikipedia: SVM

   - For slack variables the inequalities in the constraints can be attained


## **Homework 1 hints**

- Problem 3: Heart disease data


- SVM functions and different kernels

- Try your hand!

---

[Up: contents](../index.md)

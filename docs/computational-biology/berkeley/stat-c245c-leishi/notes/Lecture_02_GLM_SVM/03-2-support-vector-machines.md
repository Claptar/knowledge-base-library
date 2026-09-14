---
title: 2 Support Vector Machines
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_02_GLM_SVM.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_02_GLM_SVM.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Support Vector Machines

**Source:** [`notes/Lecture_02_GLM_SVM.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_02_GLM_SVM.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## **2.1 Hyperplane, margin and maximal margin classifiers**

Motivated by the interpretation of logistic regression, given a training sample _S_ , it seems that we would have found a good fit to the data if we can find _β_ so that _x_<sup>_′_</sup> _β ≫_ 0 whenever _y_ = 1, and _x_<sup>_′_</sup> _β ≪_ 0 whenever _y_ = 0. Because this would reflect a very confidence (and maybe correct) set of classifications for the training sample. This seems to be a nice goal to aim for. To simplify notations, in this section, we change the label set _Y ∈{_ 0 _,_ 1 _}_ to _Y ∈{−_ 1 _,_ 1 _}_ .

Consider a very simple example in the following Figure 2, in which X (green cross) represent positive outcomes, and red circles represent negative outcomes. The classifier _h_ 1has larger margin than the classifier _h_ 2, and the classifier _h_ 2 is called the “maximal margin classifier.” In plot C, _h_ 3 is the maximal margin classifier. Nevertheless, _h_ 3 may give false prediction given the yellow cross. This suggests the maximal margin classifier is sensitive to the presence of outliers. The decision boundary is specified by _{x_ : _x − a_ = 0 _}_ . We predict the outcome to be 1 (low risk) when _x > a_ and we predict the outcome to be _−_ 1 (high risk) when _x < a_ .

When we are using a margin to determine the location of a threshold _a_ , then we are using a maximal margin classifier–Support Vector Machine (SVM)– to classify observations. We will formally discuss SVM in the next section.

Now we have informally introduced margin and maximal margin classifiers, let’s now define the margin of a given hyper-plane rigorously. A hyperplane is defined through _β_ = ( _a, β_ 1 _, . . . , βd_ )<sup>_′_</sup> as a set of points so that


and the margin _γ_ is defined as the distance from the hyperplane to the closest point across both classes. Given a hyperplane, to decide the margin, we need to


Figure 2: One-dimensional classification problem and the definition of margin.

first calculate the distance of a point _x_ to the hyperplane _A_ . For simplicity, we define w = ( _β_ 1 _, . . . , βd_ )<sup>_′_</sup> .

**Distance between a point** _x ∈_ R<sup>_d_</sup> **to the hyperplane** _A_ Consider some point _x_ , and let _d_ be the vector from _A_ to _x_ of the minimum length. Our goal is to calculate the length of _d_ ( _l_ 2 norm of _d_ ). Let _x_<sup>`p`</sup> be the projection of _x_ onto _A_ . Since _d_ is parallel to w, we can write


Since _x_<sup>`p`</sup> , it satisfies _a_ + _x_<sup>`p`</sup><sup>_′_</sup> w = 0. Therefore,


4

The length of _d_ :


Now, given training covariates _{Xi}_<sup>_n_</sup> _i_ =1<sup>and a hyperplane</sup><sup>_A_,the</sup><sup>_mar-_</sup> _gin_ of _A_ with respect to _S_ is defined as:


By definition, the margin and hyperplane are scale invariant: _γ_ ( _c·_ w _, c·a_ ) = _γ_ (w _, a_ ), for any _c̸_ = 0.

## **2.2 Maximal Margin Classifier-SVM**

The name SVM comes from the fact that the observations on the edge and within the margin are called _Support Vectors_ . We will circle back for a more precise definition of support vectors at the end of the section. See a two-dimensional illustration in Figure 4.. We can formulate our search for the maximum margin separating hyperplane as a constrained

Figure 3: Distance between a and within the margin are called _Support Vectors_ . We will circle back point _x ∈_ R<sup>2</sup> to the hyperplane for a more precise definition of support vectors at the end of the section. _A_ . See a two-dimensional illustration in Figure 4.. We can formulate our search for the maximum margin separating hyperplane as a constrained optimization problem. The objective is to maximize the margin under the constraint that all data points must lie on the correct side of the hyperplane:


Or equivalently:


Because the hyperplane is scale invariant, we can fix the scale of _b_ and w such that


This suggests we can further relax our objective function to


We can further show that the optimal solution of the above problem is equivalent to (How?)


5


We’ve now transformed the problem into a form that can be efficiently solved. The above is an optimization problem with a convex quadratic objective and only linear constraints. Its solution gives us the optimal margin classifier. This optimization problem can be solved using commercial quadratic programming (QP) code.


Figure 4: Support Vector Machine in 2-dimensions.

**Support vectors** For the optimal solution of the above problem, some training points will have tight constraints (why?), i.e.,


We refer to these training points as support vectors. Support vectors are special because they are the training points that define the maximum margin of the hyperplane to the data set _S_ . Thus, they determine the shape of the hyperplane. If you were to move one of them and retrain the SVM, the resulting hyperplane would change.

## **2.3 SVM with soft constraints**

In the previous section, we discussed SVM under the constraint that no mis-classification is allowed. Let’s circle back to the example given in Figure 2.C and

compare the classifier _h_ 3 and _h_ 4:

1. Classifier _h_ 3: no mis-classification error, but predict the high risk patient (yellow cross) as low risk

2. Classifier _h_ 4: miss classify one low risk patient as high risk, but correctly predict the high risk patient profile

Which classifier would you prefer if you were a doctor?

In some cases, we would deliberately make mistakes so that our algorithm can detect high risk patients with a higher accuracy. Motivated by this consideration, we can revise the SVM with so-called “soft constraints.” In addition, in practice,when there exists no separating hyperplane between the two classes, soft constraints can be helpful as well.

The soft constraints are done by the introduction of slack variables:


The slack variables _ξi_ ’s allow the input _xi_ to move closer to the hyperplane, but there is a penalty in the objective function for such slackness. _C_ is a tuning parameter: If _C_ is very large, the SVM becomes very

6

strict and tries to get all points on one side of the hyperplane. If _C_ is very small, the SVM becomes very loose and may “sacrifice” some points to obtain a simpler solution.

Two questions before ending this lecture:

1. If we do not want to misclassify any high-risk patient, what options do we have?

2. How can we revise the current algorithm so that SVM can work with the problem presented in Figure 5?


Figure 5: Can SVM be used to predict the drug-effective outcome?

7

---

[← 1 Logistic Regression](02-1-logistic-regression.md) · [Up: contents](index.md)

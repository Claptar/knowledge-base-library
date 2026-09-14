---
title: PH240C Homework 1
source: https://leishi-rocks.github.io/courses/ph240c/hw/Homework-1.pdf
source_file: sources/berkeley-stat-c245c-leishi/hw/Homework-1.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PH240C Homework 1

**Source:** [`hw/Homework-1.pdf`](https://leishi-rocks.github.io/courses/ph240c/hw/Homework-1.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Due: Septerm 22nd in class

September 9, 2021

1. Suppose we fit logistic regression to predict the probability a PH240C student gets an A in the class, from two variables. The variable are average hours of study per week ( _X_ 1) and GPA in other statistics courses taken ( _X_ 2). The model estimates _β_ 0 = _−_ 4 _, β_ 1 = 0 _._ 05 _, β_ 2 = 1. (Note: these are made up numbers! Do not try to predict your grades with them. 10 points per question.)

   - (a) Predict the probability of getting an A for a student who studies 5 hours a week and has a GPA of 3.5 in other statistics courses.

   - (b) What are the odds that this student will get an A?

   - (c) How many hours a week does this student need to study for the model to predict a 50% chance of getting an A?

2. For this question, please use graph paper; you can print it for free from many websites, for example, www.printfreegraphpaper.com. (15 points per question)

   - (a) Draw the hyperplane defined by 2 _X_ 1 _−_ 2 _X_ 2 _−_ 1 = 0. Indicate the set of points satisfying 2 _X_ 1 _−_ 2 _X_ 2 _−_ 1 _>_ 0 with a “+” sign, and the set of points satisfying 2 _X_ 1 _−_ 2 _X_ 2 _−_ 1 _<_ 0 with a “ _−_ ” sign.

   - (b) Suppose your hyperplane is the optimal separating hyperplane for an SVM classifier fitted to some data, with the margin _m_ = _√_ 2. Draw the margin lines.

   - (c) What class label (+ or _−_ , as defined above) does this SVM predict for the following points: (1,4); (1,1); (2, -5); (2, -1); (4,2)?

   - (d) Suppose these five points were part of the training data, and their true labels, given in the same order, are _−_ , _−_ , +, +, _−_ . Calculate the corresponding slack values ( _ξi_ ’s) for each of the five points.

3. Using the dataset “heart ~~d~~ isease.csv” which contains a dataset of heart disease patients from the Cleveland Clinic:

   - Chest-pain type. Type of chest-pain experienced by the individual: 1 = typical angina, 2 = atypical angina, 3 = non-angina pain, 4 = asymptomatic angina

   - Fasting Blood Sugar. Fasting blood sugar level relative to 120 mg/dl: 0 = fasting blood sugar _≤_ 120 mg/dl, 1 = fasting blood sugar _>_ 120 mg/dl

   - Resting ECG. Resting electrocardiographic results: 0 = normal, 1 = ST-T wave abnormality, 2 = left ventricle hyperthrophy

   - Exercise Induced Angina: 0 = no, 1 = yes

1

- ST Depression Induced by Exercise Relative to Rest: ST Depression of subject

- Peak Exercise ST Segment: 1 = Up-sloaping, 2 = Flat, 3 = Down-sloaping

- Thal: Form of thalassemia: 3 = normal, 6 = fixed defect, 7 = reversible defect

- Diagnosis of Heart Disease: Indicates whether subject is suffering from heart disease or not: 0 = absence, 1 = heart disease present

The goal is to learn a binary classifier for hear disease using support vector machines. Please consider at least three different choices of kernel function (linear, Gaussian, polynomial) to produce the corresponding classifiers. What are important predictors in the model? How would you quantify them?

2

---

[Up: contents](../index.md)

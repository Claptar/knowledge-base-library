---
title: PH240C Homework 2
source: https://leishi-rocks.github.io/courses/ph240c/hw/Homework-2.pdf
source_file: sources/berkeley-stat-c245c-leishi/hw/Homework-2.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PH240C Homework 2

**Source:** [`hw/Homework-2.pdf`](https://leishi-rocks.github.io/courses/ph240c/hw/Homework-2.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## Due: October 19th at 7pm to your GSI

October 6, 2021

1. (20pt) This question concerns classification trees.

   - (a) Sketch the tree corresponding to the partition of the predictor space shown. The class labels inside the boxes on the diagram indicate the majority of _Y_ within each region. Label each split on your tree and indicate class label assigned to each terminal node.


<!-- Start of picture text -->
X2 < −1.55|<br>Green<br>X2 < 1.25<br>1<br>Red<br>Green X1 < 2.25<br>1<br>Red<br>Red<br>X1 < −1.8<br>1<br>−1 0 1 2 3<br>X1<br>1 −1<br>3<br>2<br>X2 1<br>0<br>−1<br><!-- End of picture text -->

   - (b) Sketch a diagram similar to the one in part (a) for the tree shown below. Divide the predictor space into regions, and indicate the class label (1 or -1) for each region.

   - (c) Use the tree in (b) to classify the observation ( _X_ 1 _, X_ 2) = (2 _,_ 1). Trace and present the corresponding path through the tree above and write down your prediction below.

2. (35pt) This question uses the `crabs` data, available through the R package `MASS` . The data contain five size-related measurements on two different species of crabs, blue and orange, with 50 male and 50 female crabs of each species measured. Set the random seed to 6789 and randomly select 80% of the data as your training data. Make sure you select the same number of observations from each species/sex combination. Set the remaining 20% aside to use as test data.

   - (a) Train a classification tree to predict Species from the five numerical measurements and sex, selecting the optimal size by cross-validation but using no more than 10 splits. Plot the tree. Comment on which variables are used by the tree. Compute training and test errors.

1

   - (b) Train random forests on the data, using _m_ = 5 randomly selected predictors at each split, and 1000 trees total. Make a variable importance plot and compare with your results for a single tree. Compute training and test errors.

   - (c) Fit AdaBoost to the data. Plot the training and test errors as a function of the number of trees _M_ constructed by boosting, for a range of values of _M_ up to 1000. Report training ansd test errors for a value of _M_ of your choice, and explain why you chose that _M_ .

   - (d) Comment on which method appears to perform best for this dataset, and whether the results are consistent across methods.

3. (20 pt) Load the dataset in “dataHW2.Rda”, build a classifier based on learnt supervised learning methods. Report your findings. The score you get for this question is 20 pt times the prediction accuracy of your classifier.

2

---

[Up: contents](../index.md)

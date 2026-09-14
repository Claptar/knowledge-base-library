---
title: Data importing and preprocessing
source: https://leishi-rocks.github.io/courses/ph240c/hw/hw1-sol.pdf
source_file: sources/berkeley-stat-c245c-leishi/hw/hw1-sol.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Data importing and preprocessing

**Source:** [`hw/hw1-sol.pdf`](https://leishi-rocks.github.io/courses/ph240c/hw/hw1-sol.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

```
data<-read.csv("heart_disease.csv")
data<-data%>%filter(Thalassemia!="?")%>%droplevels()
name_lst<-c("Chest_Pain_Type","Fasting_Blood_Sugar","Resting_ECG",
"Exercise_Induced_Angina","ST_Depression_Exercise",
"Peak_Exercise_ST_Segment","Thalassemia")
factor_lst<-c("Chest_Pain_Type","Fasting_Blood_Sugar","Resting_ECG",
"Exercise_Induced_Angina","Peak_Exercise_ST_Segment")
x<-data%>%select(all_of(name_lst))
x[factor_lst]<-lapply(x[factor_lst],factor)
y<-as.factor(data$Diagnosis_Heart_Disease)
data_run<-data.frame(y,x)
```

**Linear SVM** :

```
svm.linear<-svm(y~.,data=data_run,kernel="linear")
summary(svm.linear)
##
##Call:
##svm(formula=y~.,data=data_run,kernel="linear")
##
##
##Parameters:
##SVM-Type:C-classification
##SVM-Kernel:linear
##cost:1
##
##NumberofSupportVectors:137
##
##(6968)
##
##
##NumberofClasses:2
##
##Levels:
##01
support.index<-svm.linear$index
coefs<-svm.linear$coefs
w<-data.frame(value=t(svm.linear$SV)%*%coefs)
w
```

|`##`||`value`|
|---|---|---|
|`## `|`Chest_Pain_Type1`|`0.769309770`|
|`## `|`Chest_Pain_Type2`|`-0.001731588`|
|`## `|`Chest_Pain_Type3`|`0.155706830`|
|`## `|`Chest_Pain_Type4`|`-0.923285012`|
|`## `|`Fasting_Blood_Sugar1`|`-0.065955421`|
|`## `|`Resting_ECG1`|`0.000000000`|
|`## `|`Resting_ECG2`|`-0.529802769`|


3

```
##Exercise_Induced_Angina1-0.548814524
##ST_Depression_Exercise-0.532332166
##Peak_Exercise_ST_Segment2-0.483938860
##Peak_Exercise_ST_Segment30.274404461
##Thalassemia6.0-0.693203452
##Thalassemia7.0-1.169822820
```

We measure the importance of the variables according to the magnitude of the svm coefficients. Based on the output, Thalassemia 7.0, chest pain type 1 and 4(corresponding to typical angina and asymptomatic angina), Thalassemia 6.0 seem to have a more important affect on heart disease.

Of course coefficients might not be a good quantification of variable importance: the linear SVM model might not be correct, and the coefficients might not be statistically significant.

---

[← Question 3](03-question-3.md) · [Up: contents](index.md) · [Gaussian SVM →](05-gaussian-svm.md)

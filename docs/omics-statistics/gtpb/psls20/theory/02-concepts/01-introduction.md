---
title: Introduction
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/02-concepts.Rmd
source_file: sources/gtpb-psls20/theory/02-concepts.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`theory/02-concepts.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/02-concepts.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

```r
knitr::opts_chunk$set(include = TRUE, comment = NA, echo = TRUE,
                      message = FALSE, warning = FALSE)
library(tidyverse)
library(NHANES)
```

```r
if ("pi"%in%ls()) rm("pi")
kopvoeter<-function(x,y,angle=0,l=.2,cex.dot=.5,pch=19,col="black")
{
angle=angle/180*pi
points(x,y,cex=cex.dot,pch=pch,col=col)
lines(c(x,x+l*cos(-pi/2+angle)),c(y,y+l*sin(-pi/2+angle)),col=col)
lines(c(x+l/2*cos(-pi/2+angle),x+l/2*cos(-pi/2+angle)+l/4*cos(angle)),c(y+l/2*sin(-pi/2+angle),y+l/2*sin(-pi/2+angle)+l/4*sin(angle)),col=col)
lines(c(x+l/2*cos(-pi/2+angle),x+l/2*cos(-pi/2+angle)+l/4*cos(pi+angle)),c(y+l/2*sin(-pi/2+angle),y+l/2*sin(-pi/2+angle)+l/4*sin(pi+angle)),col=col)
lines(c(x+l*cos(-pi/2+angle),x+l*cos(-pi/2+angle)+l/2*cos(-pi/2+pi/4+angle)),c(y+l*sin(-pi/2+angle),y+l*sin(-pi/2+angle)+l/2*sin(-pi/2+pi/4+angle)),col=col)
lines(c(x+l*cos(-pi/2+angle),x+l*cos(-pi/2+angle)+l/2*cos(-pi/2-pi/4+angle)),c(y+l*sin(-pi/2+angle),y+l*sin(-pi/2+angle)+l/2*sin(-pi/2-pi/4+angle)),col=col)
}

par(mar=c(0,0,0,0),mai=c(0,0,0,0))
plot(0,0,xlab="",ylab="",xlim=c(0,10),ylim=c(0,10),col=0,xaxt="none",yaxt="none",axes=FALSE)
rect(0,6,10,10,border="red",lwd=2)
text(.5,8,"population",srt=90,col="red",cex=2)
symbols (3, 8, circles=1.5, col="red",add=TRUE,fg="red",inches=FALSE,lwd=2)
set.seed(330)
grid=seq(0,1.3,.01)

for (i in 1:50)
{
	angle1=runif(n=1,min=0,max=360)
	angle2=runif(n=1,min=0,max=360)
	radius=sample(grid,prob=grid^2*pi/sum(grid^2*pi),size=1)
	kopvoeter(3+radius*cos(angle1/180*pi),8+radius*sin(angle1/180*pi),angle=angle2)
}
text(7.5,8,"Cholesterol in population",col="red",cex=1.2)

rect(0,0,10,4,border="blue",lwd=2)
text(.5,2,"sample",srt=90,col="blue",cex=2)
symbols (3, 2, circles=1.5, col="red",add=TRUE,fg="blue",inches=FALSE,lwd=2)
for (i in 0:2)
	for (j in 0:4)
{

	kopvoeter(2.1+j*(3.9-2.1)/4,1.1+i)
}
text(7.5,2,"Cholesterol in sample",col="blue",cex=1.2)

arrows(3,5.9,3,4.1,col="black",lwd=3)
arrows(7,4.1,7,5.9,col="black",lwd=3)
text(1.5,5,"EXP. DESIGN (1)",col="black",cex=1.2)
text(8.5,5,"ESTIMATION &\nINFERENCE (3)",col="black",cex=1.2)
text(7.5,.5,"DATA EXPLORATION &\nDESCRIPTIVE STATISTICS (2)",col="black",cex=1.2)
```

### Experimental Design (1)
   - Researcher determines the **population** to which they wants to generalize their conclusions.
   - Financial and logistic limitations $\rightarrow$ **representative sample** from population

### Data analysis (2 & 3)
   - **Data-Exploration en Descriptive Statistics (2)**: explore, visualize, summarize, gain insight, check assumptions
   - **Statistical Inference (3)**: Generalize what we observe in the sample towards the population so that we can draw general conclusions on the biological process we study. We need statistical models to analyze the data, and, to quantify and report on variability and uncertainty.

---

## Example

- National Health and Nutrition Examination Survey (NHANES)
- American demografic study
- Large number of physical, demographic, nutritional, life style and health characteristics

```r
library(NHANES)
knitr::kable(  NHANES[c(1,4,5,6,7,8),c(1,3,20,23,34,72)]
,format = "markdown")
```

---

## Variables

- We measure *variables* on subjects in the sample
- A Variable is a charactistic e.g. Direct cholesterol, Age, Gender,, ...
- It varies from subject tot subject in the population and thus also within the sample as well as from sample to sample.

### *Types* of variables

1. *Qualitative variables*: a limited number of outcome categories, non-numeric.
	-  *nominal variables*: no natural ordening, e.g. gender, blood group, eye color, ...
	-  *ordinal variables*: ordening, e.g. BMI class, smoking status (1: never smoked, 2: stopped smoking, 3: smoker)

2. *Numeric variables*:
   	- *discrete variables*: counts e.g. number of parners in life span, ...
	- *continuous variables*: can (in theory) take each possible value between certain limits e.g. Age, Weight, BMI, fluorescence measurement in ELISA assay

	- Often dichotomised to turn it in a nominal qualitative variable $\rightarrow$ information loss

---

## Population

- Aim of scientific study: make general statements on a process at the level of the population.
- E.g. assess if the cholesterol level is on average different between males and females who are elder than 25.

$\rightarrow$ assess cholesterol level in population above 25.

- Population in statistics is a theoretical concept
	  - It is in continuous evolution/change
	  - Often interest to generalize conclusions to future subject $\rightarrow$ so population cannot be entirely observed at the present.
  	- Can typically be considered to be infinite.

- Population has to be clearly defined!

*Inclusion criteria* are characteristics a subject/experimental unit must have to belong to the population, e.g.

- age above 25
- normal BMI
- ...

*Exclusion criteria* characteristics that the subject/experimental unit is not allowed to have to belong to the population, e.g.

- pregnancy in study on new type of drug
- diabetes, history of hard drugs, low health status when the aim is to delineate a range of normal values of blood pressure in a population of healthy individuals
- ...

---

---

[Up: contents](index.md) · [Random Variables →](02-random-variables.md)

---
title: About Stat 210A
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/syllabus.html
source_file: sources/berkeley-stat210a/fall-2025/syllabus.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# About Stat 210A

**Source:** [`syllabus.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/syllabus.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

### What is the theory of statistics? {.anchored anchor-id="what-is-the-theory-of-statistics"}

Statistics is the study of methods that use data to understand the world. Statistical methods are used throughout the natural and social sciences, in machine learning and artificial intelligence, and in engineering. Despite the ubiquitous use of statistics, its practitioners are perpetually accused of not actually understanding what they are doing. Statistics theory is, broadly speaking, the subject of what exactly we are doing when we apply statistical methods.

While there are many possible ways to analyze data, most (but certainly not all) statistical methods are based on **statistical modeling:** treating the data as a realization of some *random* data-generating process with attributes, usually called *parameters*, that are *a priori* unknown. The goal of the **analyst**, then, is to use the data to draw accurate inferences about these parameters and/or to make accurate predictions about future data. If the modeling has been done well (a very big “if”) then these unknown parameters will correspond well to whatever real-world questions initially motivated the analysis. Applied statistics courses like Stat 215A and B delve deeply into questions about how to ensure that the statistical modeling exercise successfully captures something interesting about reality.

In this course we will instead focus on how the analyst can use the data most effectively within the context of a given mathematical setup. We will discuss the structure of statistical models, how to evaluate the quality of a statistical method, how to design good methods for new settings, and the philosophy of Bayesian vs frequentist modeling frameworks. We will cover estimation, confidence intervals, and hypothesis testing, in parametric and nonparametric methods, in finite samples and asymptotic regimes.

### Topics {.anchored anchor-id="topics"}

Statistical decision theory (frequentist and Bayesian), exponential families, point estimation, hypothesis testing, resampling methods, estimating equations and maximum likelihood, empirical Bayes, large-sample theory, high-dimensional testing, multiple testing and selective inference.

### Prerequisites {.anchored anchor-id="prerequisites"}

The course prerequisites are linear algebra, analysis, probability, and statistics. See the [course FAQ](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/faq.html) for more details if you are unsure about your level of preparation.

### Relationship of Stat 210A to other Berkeley courses {.anchored anchor-id="relationship-of-stat-210a-to-other-berkeley-courses"}

Stat 210A focuses on *classical* statistical contexts: inference in finite samples and in fixed-dimensional asymptotic regimes. Stat 210B (for which 210A is a prerequisite) is more technical and covers topics like empirical process theory and high-dimensional statistics.

Berkeley’s graduate course on Statistical Learning Theory (CS 281A / Stat 241A) is also very popular and has some overlap in its topics. Roughly speaking, it is more tilted toward “machine learning”: it spends more time on topics in predictive modeling (i.e. classification and regression, which are covered in Stat 215A), optimization, and signal processing, but spends less time on inferential questions and (I believe) does not cover topics like hypothesis testing, confidence intervals, and causal inference. Both courses cover estimation and exponential families.

---

[← Course information](01-course-information.md) · [Up: contents](index.md) · [References →](03-references.md)

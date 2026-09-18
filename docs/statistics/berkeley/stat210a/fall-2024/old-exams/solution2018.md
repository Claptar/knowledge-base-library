---
title: Solution2018
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2018.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2018.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`old-exams/solution2018.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2018.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Solution2018

Student ID:

## Final Examination: QUESTION BOOKLET

Prof. William Fithian

Fall 2018

• Do NOT open this question booklet until you are told to do so.

• Write your Student ID number at the top of this page.

• Write your solutions in this booklet.

• No electronic devices are allowed during the exam.

• Be neat! If we can’t read it, we can’t grade it.

• You can treat any results from lecture or homework as “known,” and use them in your work without rederiving them, but do make clear what result you’re using. You do not need to explicitly check regularity conditions for the theorems from class that required them.

• For a multi-part problem, you may treat the results of previous parts as given (if you don’t prove the result for part (a), you can still use it to solve part (b)).

• I have starred some parts which I believe are the most difficult, and which I expect most students won’t necessarily be able to solve in the time allotted. They are generally not worth more points than the less difficult parts, so don’t waste too much time on them until you’re happy with your answers to the latter.

• Be careful to justify your reasoning and answers. We are primarily interested in your understanding of concepts, so show us what you know.

• Good luck!

---

## 1. A curved Gaussian family (20 points, 4 points / part). Some useful facts for this problem:

• Recall that the Gaussian density function for $Z \sim N(\mu, \sigma^2)$ is
$$\frac{1}{\sqrt{2\pi\sigma^2}} \exp\left\{ -\frac{(x - \mu)^2}{2\sigma^2} \right\}$$

Suppose that
$$X_1, \ldots, X_n = \begin{pmatrix} X_{1,1} \\ X_{1,2} \end{pmatrix}, \ldots, \begin{pmatrix} X_{n,1} \\ X_{n,2} \end{pmatrix} \stackrel{\text{i.i.d.}}{\sim} N_2(\mu(\theta), I_2),$$
for $\theta \in \mathbb{R}$ and $\mu(\theta) = \begin{pmatrix} \theta \\ \theta^2 \end{pmatrix}$.

(a) Show that $T(X) = \sum_i X_i \in \mathbb{R}^2$ is a minimal sufficient statistic but is not complete

---

[Up: contents](../index.md)

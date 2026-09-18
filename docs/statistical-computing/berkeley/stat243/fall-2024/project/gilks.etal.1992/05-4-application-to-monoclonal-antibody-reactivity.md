---
title: 4. Application to Monoclonal Antibody Reactivity
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/project/gilks.etal.1992.pdf
source_file: sources/berkeley-stat243/fall-2024/project/gilks.etal.1992.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`project/gilks.etal.1992.pdf`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/project/gilks.etal.1992.pdf) — berkeley-stat243 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4. Application to Monoclonal Antibody Reactivity

We have applied adaptive rejection sampling to a Gibbs sampling analysis of monoclonal antibody reactivity. The data that we examine originate from flow cytometry experiments in which 13 monoclonal antibodies were tested against 15 normal and malignant human cell types. The data form part of a much larger study designed to discover antigens involved in small cell lung cancers (Souhami *et al.*, 1991). Each of the 13 antibodies studied here is known to react with cells expressing the neural cell adhesion molecule (NCAM), a molecule which is expressed on the surface of normal peripheral nerve cells, but which also appears on malignant small cell lung cancer cells. In normal nerve cells the molecule is thought to attach the nerve to other cells, thereby fixing it in position; in malignant cells its role is as yet unclear. The NCAM molecule is also present, in varying densities, on other normal and malignant cell types (e.g. brain cells and neuroblastoma cells) but is absent on many cell types.

The recognition of an antigen (a molecule expressed on the surface of a cell) by an antibody depends on the fraction antibody binding (FAB) portion of the antibody being the correct shape to lock on to the antigen. Since different monoclonal antibodies recognizing the same antigen will in general have slightly differently shaped FAB portions, we might expect such antibodies to differ somewhat in their ability to bind to the antigen. The purpose of the analysis presented here is to quantify the nature and extent of this variability. Lack of variability could indicate that the NCAM molecule has only one epitope (molecular feature) accessible to antibody.

## 4.1. Model

In each flow cytometry experiment, reactivity was measured as the percentage of cells reacting with antibody. Percentages were reported rounded to the nearest integer. Let $y_{ijr}$ denote the percentage reactivity recorded in the $r\text{th}$ experiment testing antibody $i$ against target cell type $j$ (for $i = 1, \dots, I$; $j = 1, \dots, J$; $r = 1, \dots, n_{ij}$). We might proceed by ignoring the rounding and constructing a linear model of $\text{logit}(y_{ijr}/100)$, where $\text{logit}(x)$ denotes $\log\{x/(1 - x)\}$. However, with these data the rounding is important, as there are many (rounded) reactivities of 0.0 or 100.0. Therefore, instead we suppose that $y_{ijr}$ is related to an underlying logistic distribution with location parameter $\mu_{ij}$ and scale parameter $\tau_y$ as follows:
$$[y_{ijr} \mid \mu_{ij}, \tau_y] = \frac{1}{1 + \exp\{-\tau_y(b_{ijr} - \mu_{ij})\}} - \frac{1}{1 + \exp\{-\tau_y(a_{ijr} - \mu_{ij})\}} \tag{7}$$
where
$$\begin{aligned}
a_{ijr} &= \text{logit}\left(\frac{y_{ijr} - 0.5}{100}\right) && \text{if } y_{ijr} > 0, \\
&= -\infty && \text{if } y_{ijr} = 0,
\end{aligned}$$
and
$$\begin{aligned}
b_{ijr} &= \text{logit}\left(\frac{y_{ijr} + 0.5}{100}\right) && \text{if } y_{ijr} < 100, \\
&= +\infty && \text{if } y_{ijr} = 100.
\end{aligned}$$

For the location parameter we specify
$$\mu_{ij} = \beta_0 + \beta_{1j} + \beta_{2i}. \tag{8}$$
This model specifies a basic pattern of reactivity $(\beta_0 + \beta_{1j})$ across cell types, reflecting different densities of cell surface expression of the NCAM molecule. The basic pattern is adjusted to allow for differences in affinity for the NCAM molecule ($\beta_{2i}$).

To complete the model we need to specify priors for $\beta_0$, $\beta_{1j}$, $\beta_{2i}$ and $\tau_y$. We set
$$[\beta_0 \mid \alpha_0, \tau_0] \sim N(\alpha_0, \tau_0^{-1}), \tag{9}$$
$$[\beta_{1j} \mid \tau_1] \sim N(0, \tau_1^{-1}), \tag{10}$$
$$[\beta_{2i} \mid \tau_2] \sim N(0, \tau_2^{-1}), \tag{11}$$
$$[\tau_y \mid \rho_y, \lambda_y] \sim G(\rho_y, \lambda_y), \tag{12}$$
where $N(\alpha, \tau^{-1})$ denotes a normal distribution with mean $\alpha$ and variance $\tau^{-1}$, and $G(\rho, \lambda)$ denotes a gamma distribution with index parameter $\rho$ and scale parameter $\lambda$. We set $\alpha_0 = -1.0$, $\tau_0 = 0.1$, $\rho_y = 2.0$ and $\lambda_y = 4.0$ to give fairly flat priors for $\beta_0$ and $\tau_y$. We do not fix the remaining hyperparameters $\tau_1$ and $\tau_2$, as the data contain information about them: indeed, these hyperparameters are the focus of this analysis. Instead we specify fairly flat hyperpriors
$$[\tau_k \mid \rho_k, \lambda_k] \sim G(\rho_k, \lambda_k) \tag{13}$$
for $k = 1, 2$, setting $\rho_k = 2.0$ and $\lambda_k = 4.0$.

## 4.2. Gibbs Sampling

To estimate the hierarchical model (7)–(13) by Gibbs sampling the full conditional distribution for each free model parameter is required. The full conditional for $\beta_0$ is
$$[\beta_0 \mid\ ] \propto \exp\left\{-\frac{1}{2} \tau_0 (\beta_0 - \alpha_0)^2\right\} \prod_{ijr} \left[\frac{1}{1 + \exp\{-\tau_y(b_{ijr} - \mu_{ij})\}} - \frac{1}{1 + \exp\{-\tau_y(a_{ijr} - \mu_{ij})\}}\right] \tag{14}$$
where each data point contributes one term to the product. Expressions similar to expression (14) also hold for the full conditional distributions of $\beta_{1j}$, $\beta_{2i}$ and $\tau_y$ (with suitable restrictions on the subscripts of the product operator and, for $\tau_y$, the first term in expression (14) being replaced by the gamma prior (12)).

The full conditional distribution for $\beta_0$ in expression (14) does not simplify; thus sampling $\beta_0$ could be time consuming. Fortunately, each of the many terms in expression (14) is concave on the logarithmic scale with respect to $\beta_0$, and so adaptive rejection sampling can be used. Similar considerations apply to the full conditionals for $\beta_{1j}$, $\beta_{2i}$ and $\tau_y$.

The full conditional for $\tau_1$ is straightforward:
$$[\tau_1 \mid\ ] \sim G\left(\rho_1 + \frac{1}{2} J, \, \lambda_1 + \frac{1}{2} \sum_{j=1}^J \beta_{1j}^2\right) \tag{15}$$
with a similar expression for the full conditional for $\tau_2$.

We performed 1000 iterations of the Gibbs sampler. At each iteration, for each of the parameters $\beta_0$, $\beta_{1j}$, $\beta_{2i}$ and $\tau_y$, we used the 15th and 85th centiles of the sampling density $s_k(x)$ from the previous iteration as starting values for adaptive rejection sampling.

## 4.3. Results

For each of the parameters sampled by adaptive rejection sampling, on average only three evaluations of $h(x)$ were required at each iteration (including the two starting evaluations), and on only 5% of iterations were more than four evaluations of $h(x)$ required.

Convergence in distribution was achieved within 10 iterations. Therefore the posterior summaries in Table 3 were based on iterations 11–1100. The results suggest that there is substantial variability in the expression of NCAM among targets ($\tau_1^{-1}$), but relatively little variability in antibody affinity for the NCAM molecule ($\tau_2^{-1}$). There is some evidence that antibody 12 has low affinity to NCAM as the 90% support interval for $\beta_{2,12}$ does not cover 0.

---

[← 3. Adaptive Rejection Sampling and Gibbs Sampling](04-3-adaptive-rejection-sampling-and-gibbs-sampling.md) · [Up: contents](index.md) · [5. Conclusions →](06-5-conclusions.md)

---
title: Risk of the James-Stein estimator
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/jamesstein.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/jamesstein.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Risk of the James-Stein estimator

**Source:** [`reader/jamesstein.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/jamesstein.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

We are now ready to calculate the risk of the James--Stein estimator $\delta_{JS}(X) = \left(1 - \frac{d-2}{\|X\|^2}\right)X$. We can drop the assumption $\sigma^2 = $, under the assumption $\sigma^2 = 1$ (for general $\sigma^2$, we should replace the numerator $d-2$ with $(d-2)\sigma^2$. Then ).

Proceeding as before, we have
$$
h(X) = \frac{d-2}{\|X\|^2}X \Rightarrow \|h(X)\|^2 = \frac{(d-2)^2}{\|X\|^2},
$$
Applying the quotient rule we have
$$Dh(X)_{ii} = (d-2)\frac{\partial}{\partial X_i} \frac{X_i}{\sum_j X_j^2} = (d-2)\frac{\|X\|^2 - 2X_i^2}{\|X\|^4},$$
and summing over the coordinates gives
$$\text{tr}(Dh(X)) = (d-2) \frac{d\|X\|^2 - 2\|X\|^2}{\|X\|^4} = -\frac{(d-2)^2}{\|X\|^2}.$$
We thereby obtain the estimator
$$
\widehat{\text{MSE}}(X) = d + \frac{(d-2)^2}{\|X\|^2} - 2\frac{(d-2)^2}{\|X\|^2} = d - \frac{(d-2)^2}{\|X\|^2}.
$$
Taking expectations, we obtain
$$
\text{MSE}(\theta; \delta_{\text{JS}}) = d - (d-2)^2\EE_\theta\left[\frac{1}{\|X\|^2}\right].
$$
Note this is always strictly less than $d$, which is the MSE of $\delta_0(X) = X$.

If $\theta = 0$ then $\|X\|^2 \sim \chi_d^2$ and we can apply our previous result to obtain
$$
\text{MSE}(0; \delta_{\text{JS}}) = d - (d-2)^2\frac{1}{d-2} = 2.
$$
Thus, even though we are estimating $d$ parameters, our total MSE does not rise with $d$, because we will shrink harder and harder toward zero the larger $d$ gets. This is fairly remarkable.

On the other hand, suppose $\|\theta\|^2 \to \infty$. Then $\EE_\theta \|X\|^2 \to \infty$ and the improvement $(d-2)^2/\EE_\theta\|X\|^2$ will be driven to $0$.

Note that, for more general $\sigma^2$, the James--Stein estimator is $\left(1-\frac{(d-2)\sigma^2}{\|X\|^2}\right)X$. Then we have
$$h(X) = \sigma^2\frac{d-2}{\|X\|^2} \Rightarrow \|h(X)\|^2 = \sigma^4 \frac{(d-2)^2}{\|X\|^2}, \quad \text{tr} Dh(X) = \sigma^2 \frac{(d-2)^2}{\|X\|^2},$$
leading to the estimator $\widehat{\text{MSE}}(X) = \sigma^2 d - \sigma^4\frac{(d-2)^2}{\|X\|^2}$, and plugging in $\EE_0 1/\|X\|^2 = 1/(d-2)\sigma^2$, the MSE at $\theta=0$ is $2\sigma^2$.

### Final thoughts

A few more notes: first, $\delta_{JS}(X)$ also inadmissible, since $\delta_{+}(X) = (1 - \frac{d-2}{\|X\|^2})_+ X$ is strictly better since we never benefit from using a shrinkage parameter $\zeta > 1$.

A practically more useful version of James--Stein shrinks toward the central value $\overline{X}$:

$$\delta_{JS+, i}(X) = \overline{X} + (1 - \frac{d-3}{V^2})_+ (X_i - \overline{X})$$
This estimator dominates $\delta(X) = X$ for $d \geq 4$.

Taken to its logical extreme, the James--Stein estimator seems to imply absurd things: should all scientists at
Berkeley, across all different fields, pool their estimates to calculate a James--Stein estimator even if their different estimation problems have nothing to do with each other, as long as they are estimating Gaussian location parameters? The overall MSE for all of the estimates really would be better.

To avoid this conclusion we might note that even when the overall MSE is improved, the MSE for a single coordinate can certainly get worse. For example, if $\theta_1 = 10$ but $\theta_2=\theta_3=\cdots=\theta_{1000}=0$, it's likely that we'll overshrink our estimate of $\theta_1$ toward $0$ in order to do well on the other coordinates. So people who believe their estimands are larger than average wouldn't want to participate in this scheme.

---

[← Stein's Unbiased Risk Estimator](02-stein-s-unbiased-risk-estimator.md) · [Up: contents](index.md)

---
title: Inference via Expectation–Maximization
source: https://doi.org/10.64898/2026.03.04.709349/
source_file: sources/papers/caskey-rich-2026-cellsweep/caskey-rich-2026-cellsweep.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `caskey-rich-2026-cellsweep.pdf` from [papers/caskey-rich-2026-cellsweep](https://doi.org/10.64898/2026.03.04.709349/) — papers · caskey-rich-2026-cellsweep, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Inference via Expectation–Maximization

We introduce a latent variable $\boldsymbol{z}_{i,g}^s$ representing the number of UMI counts for
barcode $i$ and feature $g$ that originated from source $s \in \{A, M, P_1, \ldots, P_K\}$. The
observed counts are constrained by:

$$\boldsymbol{C}_{i,g} = \sum_s \boldsymbol{z}_{i,g}^s. \qquad (10)$$

The likelihood is

$$L(\theta) = \frac{T_i!}{\prod_{s,g}\boldsymbol{z}_{i,g}^s!}\prod_{s,g}(\boldsymbol{w}_{i,g}^s)^
{\boldsymbol{z}_{i,g}^s} \sim \prod_{i,g,s}(\boldsymbol{w}_{i,g}^s)^{\boldsymbol{z}_{i,g}^s}, \qquad
(11)$$

where $\theta = \{\{\alpha_i\},\beta,\{\boldsymbol{p}^k\},\boldsymbol{a},\boldsymbol{m}\}$ and

- $\boldsymbol{w}_{i,g}^A = (1-\beta)\alpha_i \boldsymbol{a}_g$;
- $\boldsymbol{w}_{i,g}^M = \beta \boldsymbol{m}_g$;
- $\boldsymbol{w}_{i,g}^{P_k} = (1-\beta)(1-\alpha_i)\gamma_i^k \boldsymbol{p}_g^k$.

**E-step.** In the expectation step, the latent counts are replaced by their expected values given
the observed counts and current parameters:

$$\boldsymbol{C}_{i,g}^{(s)} = \mathbb{E}[\boldsymbol{z}_{i,g}^s \mid \boldsymbol{C}_{i,g},
\theta^{(t)}] = \boldsymbol{C}_{i,g}\cdot\frac{\boldsymbol{w}_{i,g}^s}{\sum_{s'}
\boldsymbol{w}_{i,g}^{s'}}. \qquad (12)$$

This can be interpreted as decomposing each observed count into fractional contributions from
each source.

**M-step.** The expected complete-data log-likelihood is

$$Q(\theta) = \sum_{i,g,s}\boldsymbol{C}_{i,g}^{(s)}\log \boldsymbol{w}_{i,g}^s, \qquad (13)$$

and parameters are updated by maximizing $Q$ with respect to each group.

Updating cell-type profiles:

$$\boldsymbol{p}_g^k = \frac{\sum_i \boldsymbol{C}_{i,g}^{(P_k)}}{\sum_{i,g'}
\boldsymbol{C}_{i,g'}^{(P_k)}}. \qquad (14)$$

Updating barcode contamination: We update the barcode-specific ambient fraction $\alpha_i$ from
the expected ambient and cell-assigned counts:

$$\alpha_i = \frac{\sum_g \boldsymbol{C}_{i,g}^{(A)}}{\sum_g \boldsymbol{C}_{i,g}^{(A)} +
\sum_{g,k}\boldsymbol{C}_{i,g}^{(P_k)}}. \qquad (15)$$

We do not update $\alpha_i$ for barcodes that were pre-classified as non-cellular: for such
barcodes we keep $\alpha_i = 1$ (i.e. 100% ambient, excluding the global bulk component).

Updating the global bulk fraction:

$$\beta = \frac{\sum_{i,g}\boldsymbol{C}_{i,g}^{(M)}}{\sum_{i,g}\boldsymbol{C}_{i,g}}. \qquad
(16)$$

**Two-stage optimization and handling of extreme ambient fractions.** CellSweep employs a
two-stage optimization procedure designed to stabilize inference in the presence of barcodes that
are poorly explained by their assigned cell-type profiles. Optimization begins with a burn-in
phase, during which convergence is assessed exclusively via stabilization of the log-likelihood.
This allows the algorithm to rapidly enter a stable basin of the likelihood surface before
enforcing stricter parameter-based stopping criteria.

During burn-in, per-barcode ambient fractions are capped at $\alpha_i \le 0.9$. Barcodes that
reach this cap are temporarily excluded from contributing to updates of the cell-type profiles
$p_k$, preventing nearly ambient barcodes from biasing early profile estimates. Only these capped
barcodes are permitted to update their cell-type assignments during burn-in, using a hard
maximum-likelihood criterion over existing profiles. After convergence of the log-likelihood, the
ambient cap is removed, cell-type assignments are fixed, and final optimization proceeds until
convergence of the model parameters. In practice, this procedure substantially reduces the
prevalence of extreme $\alpha_i \to 1$ solutions while preserving global clustering structure and
stabilizing estimation of the cell-type profiles.

**Repulsion-modified update for cell-type profiles.** During the burn-in phase, CellSweep
modifies the standard EM update for cell-type expression profiles to discourage solutions in
which inferred cell-type profiles align closely with the ambient profile. Rather than maximizing
the expected complete-data log-likelihood alone, the cell-type profiles are updated by solving a
penalized optimization problem that explicitly disfavors similarity to the ambient profile.

For a given cell-type profile $p \in \Delta^{G-1}$, the burn-in update is defined as the solution
to

$$\max_{p \in \Delta^{G-1}}\left[\sum_{g=1}^{G}\tilde C_g^{(P)}\log p_g - \rho M \sum_{g=1}^{G}
a_g p_g\right],$$

where $\tilde C_g^{(P)}$ denotes the expected number of counts assigned to the cell-type component
for feature $g$, $M = \sum_g \tilde C_g^{(P)}$ is the total expected mass of the profile, $a$ is
the fixed ambient expression profile, and $\rho > 0$ controls the strength of the repulsion. This
modified objective biases early updates away from explaining background signal as biological
variation. After the burn-in phase, the repulsion term is disabled and standard EM updates are
recovered exactly, ensuring that final estimates correspond to a stationary point of the original
likelihood.

**Inferring the Ambient Profile without Non-Cellular Barcodes.** In situations with few or no
non-cellular barcodes, the ambient pool can instead be viewed as a mixture of cell-type profiles.
Conceptually, ambient contamination arises from lysed or damaged cells, so the global ambient
profile should lie within the convex hull of the cell-type expression profiles $\{p^k\}$.

We therefore parameterize the ambient profile as a mixture of the $K$ cell-type expression
distributions,

$$a = \sum_{k=1}^{K} u^k p^k, \qquad (17)$$

such that $u^k$ satisfies $\sum_k u^k = 1$ and $u^k > 0$.

We initialize these mixture weights using the initial soft membership assignments $\gamma_n^k$.
Specifically, we set

$$u^k = \frac{\sum_n \gamma_n^k}{\sum_{k'=1}^{K}\sum_n \gamma_n^{k'}}, \qquad (18)$$

which corresponds to the estimated relative abundance of each cell type in the dataset. This
choice ensures that the initial ambient profile resembles the global expression distribution
implied by the initial clustering, while remaining flexible enough to adapt during subsequent
updates.

Allowing the ambient profile to be updated renders the two-step optimization strategy used in the
default model ineffective. In the default setting, the ambient profile is fixed and therefore acts
as a stable anchor against which signal can be distinguished from noise. When the ambient profile
is allowed to change, the inferred structure of the noise co-evolves with the cell-type profiles,
so it no longer provides a consistent reference direction for separating signal from background.
In this regime, repulsion and cell-type reassignment become unstable because similarity to
ambient is itself moving during training. For this reason, the alternative model omits both the
repulsion term and cell-type reassignment.

**Updating the ambient mixture weights.** When non-cellular barcodes are unavailable, the ambient
mixture weights $\{u^k\}$ are refined using a nested expectation–maximization procedure. Let $A_g$
denote the expected number of counts assigned to the ambient component for feature $g$,
aggregated across all barcodes. Given the current estimate of the ambient profile $a$ and the
cell-type profiles $\{p^k\}$, we compute the posterior responsibility of each cell type for
generating ambient counts at each feature,

$$r_{k,g} = \frac{u^k p_g^k}{a_g}, \qquad (19)$$

These responsibilities are then used to update the mixture weights,

$$u^k \propto \sum_g r_{k,g} A_g, \qquad (20)$$

followed by normalization to enforce $\sum_k u^k = 1$. The ambient profile is subsequently
recomputed as

$$a \leftarrow \sum_{k=1}^{K} u^k p^k, \qquad (21)$$

This inner update is repeated for three iterations to refine the ambient mixture weights without
fully optimizing the ambient profile within each outer EM step. This approach provides a stable
compromise between flexibility and computational efficiency, allowing the ambient profile to adapt
while avoiding oscillatory behavior.

## Recovering Denoised Counts

After convergence, the cleaned data matrix is returned by subtracting the expected noise counts
from the observed counts:

$$\hat{\boldsymbol{C}}_{i,g} = \max\{0, \boldsymbol{C}_{i,g} - \boldsymbol{C}_{i,g}^{(A)} -
\boldsymbol{C}_{i,g}^{(M)}\}. \qquad (22)$$

When integer counts are required, stochastic rounding is used to preserve unbiasedness and
per-barcode totals.

---

[← Initial Parameter Estimates](06-initial-parameter-estimates.md) · [Up: contents](index.md) · [References →](08-references.md)

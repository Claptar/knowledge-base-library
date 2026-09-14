---
title: The Gibbs sampler
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-computation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/bayes-computation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# The Gibbs sampler

**Source:** [`reader/bayes-computation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-computation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

There exist a multitude of MCMC algorithms, but we will focus on one that goes well with the hierarchical models we were discussing in the last lecture.

## Directed Graphical Models

One special class of models that come up often in Bayesian modeling is **directed graphical models**. For a random vector $Z=(Z_1,\ldots,Z_d)$ and directed graph $G=(V,E)$ on vertex set $\{1,\ldots,d\}$, we say the density $p$ is a directed graphical model if it can be factored as
$$
p(z) = \prod_{i=1}^d p_i(z_i \mid z_{\text{Pa}(i)}),
$$
where $\text{Pa}(i)$ is the set of "parent vertices" that point to $i$, that is $\text{Pa}(i)=\{j:\; j\to i \in E\}$.

One example of a graphical model is the first $T$ steps of a Markov chain, whose distribution we can factor as
$$
\pi_0(x^{(0)}) \prod_{t=1}^{T} Q(x^{(t)} \mid x^{(t-1)}),
$$
giving the following graph:
```ojs
//| label: fig-markov
//| fig-cap: "Markov chain graphical model"
//| echo: false

{
  const width = 700;
  const height = 200;
  const nodeRadius = 25;

  const svg = d3.create("svg")
      .attr("width", width)
      .attr("height", height);

  // Define nodes for Markov chain - ellipsis is now a node
  const nodes = [
    {id: "x0", x: 100, y: 100, label: "X⁽⁰⁾"},
    {id: "x1", x: 220, y: 100, label: "X⁽¹⁾"},
    {id: "x2", x: 340, y: 100, label: "X⁽²⁾"},
    {id: "dots", x: 460, y: 100, label: "⋯"},
    {id: "xT", x: 580, y: 100, label: "X⁽ᵀ⁾"}
  ];

  const links = [
    {source: nodes[0], target: nodes[1]},
    {source: nodes[1], target: nodes[2]},
    {source: nodes[2], target: nodes[3]},
    {source: nodes[3], target: nodes[4]}
  ];

  // Helper function to calculate arrow endpoints with spacing
  function getArrowCoordinates(source, target, radius, spacing) {
    const dx = target.x - source.x;
    const dy = target.y - source.y;
    const distance = Math.sqrt(dx * dx + dy * dy);
    const unitX = dx / distance;
    const unitY = dy / distance;

    return {
      x1: source.x + unitX * (radius + spacing),
      y1: source.y + unitY * (radius + spacing),
      x2: target.x - unitX * (radius + spacing),
      y2: target.y - unitY * (radius + spacing)
    };
  }

  // Define larger arrowhead marker
  svg.append("defs").append("marker")
      .attr("id", "arrowhead")
      .attr("viewBox", "0 0 10 10")
      .attr("refX", 10)
      .attr("refY", 5)
      .attr("markerWidth", 8)
      .attr("markerHeight", 8)
      .attr("orient", "auto")
    .append("path")
      .attr("d", "M 0 0 L 10 5 L 0 10 z")
      .attr("fill", "#333");

  // Draw arrows with spacing from nodes
  svg.selectAll("line")
      .data(links)
      .join("line")
      .attr("x1", d => {
        const coords = getArrowCoordinates(d.source, d.target, nodeRadius, 3);
        return coords.x1;
      })
      .attr("y1", d => {
        const coords = getArrowCoordinates(d.source, d.target, nodeRadius, 3);
        return coords.y1;
      })
      .attr("x2", d => {
        const coords = getArrowCoordinates(d.source, d.target, nodeRadius, 3);
        return coords.x2;
      })
      .attr("y2", d => {
        const coords = getArrowCoordinates(d.source, d.target, nodeRadius, 3);
        return coords.y2;
      })
      .attr("stroke", "#333")
      .attr("stroke-width", 2)
      .attr("marker-end", "url(#arrowhead)");

  // Draw nodes (excluding the ellipsis node)
  svg.selectAll("circle")
      .data(nodes.filter(d => d.id !== "dots"))
      .join("circle")
      .attr("cx", d => d.x)
      .attr("cy", d => d.y)
      .attr("r", nodeRadius)
      .attr("fill", "white")
      .attr("stroke", "#333")
      .attr("stroke-width", 2);

  // Add labels
  svg.selectAll("text.label")
      .data(nodes)
      .join("text")
      .attr("class", "label")
      .attr("x", d => d.x)
      .attr("y", d => d.y + 5)
      .attr("text-anchor", "middle")
      .style("font-size", "18px")
      .text(d => d.label);

  return svg.node();
}
```

The Gaussian hierarchical model
$$
\begin{aligned}
\tau^2 &\sim \lambda_0\\
\theta_i &\simiid N(0,\tau^2), \quad \text{ for } i = 1,\ldots,d\\
X_i \mid \theta &\simind N(\theta_i,1)
\end{aligned}
$$
is another example, with the following graph:

```ojs
//| label: fig-dgm
//| fig-cap: "Hierarchical directed graphical model"
//| echo: false

{
  const width = 600;
  const height = 400;
  const nodeRadius = 25;

  const svg = d3.create("svg")
      .attr("width", width)
      .attr("height", height);

  // Define nodes - tau is centered horizontally
  const nodes = [
    {id: "tau", x: 300, y: 70, label: "τ²"},
    {id: "theta1", x: 175, y: 180, label: "θ₁"},
    {id: "theta2", x: 250, y: 180, label: "θ₂"},
    {id: "thetam", x: 400, y: 180, label: "θₘ"},
    {id: "x1", x: 175, y: 290, label: "X₁"},
    {id: "x2", x: 250, y: 290, label: "X₂"},
    {id: "xm", x: 400, y: 290, label: "Xₘ"}
  ];

  const links = [
    {source: nodes[0], target: nodes[1]},
    {source: nodes[0], target: nodes[2]},
    {source: nodes[0], target: nodes[3]},
    {source: nodes[1], target: nodes[4]},
    {source: nodes[2], target: nodes[5]},
    {source: nodes[3], target: nodes[6]}
  ];

  // Helper function to calculate arrow endpoints with spacing
  function getArrowCoordinates(source, target, radius, spacing) {
    const dx = target.x - source.x;
    const dy = target.y - source.y;
    const distance = Math.sqrt(dx * dx + dy * dy);
    const unitX = dx / distance;
    const unitY = dy / distance;

    return {
      x1: source.x + unitX * (radius + spacing),
      y1: source.y + unitY * (radius + spacing),
      x2: target.x - unitX * (radius + spacing),
      y2: target.y - unitY * (radius + spacing)
    };
  }

  // Define larger arrowhead marker
  svg.append("defs").append("marker")
      .attr("id", "arrowhead")
      .attr("viewBox", "0 0 10 10")
      .attr("refX", 10)
      .attr("refY", 5)
      .attr("markerWidth", 8)
      .attr("markerHeight", 8)
      .attr("orient", "auto")
    .append("path")
      .attr("d", "M 0 0 L 10 5 L 0 10 z")
      .attr("fill", "#333");

  // Draw arrows with spacing from nodes
  svg.selectAll("line")
      .data(links)
      .join("line")
      .attr("x1", d => {
        const coords = getArrowCoordinates(d.source, d.target, nodeRadius, 3);
        return coords.x1;
      })
      .attr("y1", d => {
        const coords = getArrowCoordinates(d.source, d.target, nodeRadius, 3);
        return coords.y1;
      })
      .attr("x2", d => {
        const coords = getArrowCoordinates(d.source, d.target, nodeRadius, 3);
        return coords.x2;
      })
      .attr("y2", d => {
        const coords = getArrowCoordinates(d.source, d.target, nodeRadius, 3);
        return coords.y2;
      })
      .attr("stroke", "#333")
      .attr("stroke-width", 2)
      .attr("marker-end", "url(#arrowhead)");

  // Add dots in middle layer
  svg.append("text")
      .attr("x", 325)
      .attr("y", 185)
      .attr("text-anchor", "middle")
      .style("font-size", "24px")
      .text("⋯");

  // Add dots in bottom layer
  svg.append("text")
      .attr("x", 325)
      .attr("y", 295)
      .attr("text-anchor", "middle")
      .style("font-size", "24px")
      .text("⋯");

  // Draw nodes
  svg.selectAll("circle")
      .data(nodes)
      .join("circle")
      .attr("cx", d => d.x)
      .attr("cy", d => d.y)
      .attr("r", nodeRadius)
      .attr("fill", "white")
      .attr("stroke", "#333")
      .attr("stroke-width", 2);

  // Add labels
  svg.selectAll("text.label")
      .data(nodes)
      .join("text")
      .attr("class", "label")
      .attr("x", d => d.x)
      .attr("y", d => d.y + 5)
      .attr("text-anchor", "middle")
      .style("font-size", "18px")
      .text(d => d.label);

  return svg.node();
}
```

The graphical model form implies that we can write the joint distribution of the parameters and data as
$$
\lambda_0(\tau^2)\cdot \prod_{i=1}^d \lambda(\theta_i \mid \tau^2) p_{\theta_i}(x_i),
$$
giving one factor for each node.

## Gibbs sampler

The Gibbs sampler is an MCMC algorithm that's especially convenient for (sparsely connected) directed graphical models. We give the algorithm in terms of a parameter vector $\theta = (\theta_1,\ldots,\theta_d)$, which we would like to sample from the posterior $\lambda(\theta \mid X)$. Let $\theta_{-j} = (\theta_1,\ldots,\theta_{j-1},\theta_{j+1},\ldots,\theta_d)$ denote the vector with the $j$th coordinate removed.

**Gibbs Sampler Algorithm:**

::: {style="margin-left: 2em;"}
Initialize $\theta = \theta^{(0)}$

For $t = 1, 2, \ldots, T$:
:::

::: {style="margin-left: 4em;"}
For $j=1,\ldots, d$:
:::

::: {style="margin-left: 6em;"}
Resample $\theta_j \sim \lambda(\theta_j \mid \theta_{-j}, X)$
:::

::: {style="margin-left: 4em;"}
Record $\theta^{(t)}= \theta$.
:::

::: {style="margin-left: 2em;"}
Return $\theta^{(0)},\theta^{(1)},\ldots,\theta^{(T)}$.
:::

By the instruction "Resample $\theta_j$," we mean hold $\theta_{-j}$ fixed and replace $\theta_j$ with a fresh draw from its conditional distribution given the rest.

!!! tip "Tip"
There are two common variations on the inner loop where we update the $d$ coordinates of $\theta$ one-by-one in order. We could instead either update the $d$ coordinates in a random order, or update a single random coordinate $J^{(t)}\sim \text{Unif}\{1,\ldots,d\}$.

Another variation is that it can sometimes be convenient to update blocks of covariates at a time; e.g. we could resample the pair $(\theta_1,\theta_2)$ from their joint distribution given $(\theta_3,\ldots,\theta_d)$ and $X$.
:::

**Proposition:** The posterior $\pi(\theta) = \lambda(\theta\mid X)$ is stationary for the Gibbs sampler algorithm.

*Proof:* The Gibbs sampler transition kernel is a composition of $d$ distinct transition kernels $Q_1,\ldots,Q_d$ corresponding to the $d$ steps of the inner for loop. We begin by showing that $\pi$ is stationary for each $Q_j$. Thus, if $\theta \sim \pi$ and $\zeta \mid \theta \sim Q_j(\cdot \mid \theta)$, we need to show that (marginally) $\zeta \sim \pi$ as well.

Because $\zeta_{-j} = \theta_{-j}$ almost surely, they must have the same distribution. Moreover, $\theta_j \mid \theta_{-j}$ is drawn from the distribution $\lambda(\theta_j \mid \theta_{-j}, X)$ by assumption, and $\zeta_j \mid \theta_{-j}$ is also drawn from $\lambda(\theta_j \mid \theta_{-j}, X)$ by construction of the Gibbs sampler algorithm. Hence, $\zeta \sim \lambda(\theta \mid X)$ as well.

Thus, we see that $pi$ is a stationary distribution for each $Q_j$; but then it follows that it is stationary for the composition of such kernels too. Define $\theta^{(t,0)}=\theta^{(t)}$, then $\theta^{(t,1)}$ to be the value after updating $\theta_1$ via $Q_1$, and so on up to $\theta^{(t,d)}=\theta^{(t+1)}$. We have shown that, if $\theta^{(t,j-1)} \sim \pi$, then $\theta^{(t,j)}\sim\pi$ as well, for every $j$; it follows that if $\theta^{(t)}=\theta^{(t,0)} \sim \pi$, then $\theta^{(t+1)}=\theta^{(t,d)}\sim \pi$ as well; hence $\pi$ is stationary for the "full-update" kernel $Q$ that specifies the distribution of $\theta^{(t+1)}$ given $\theta^{(t)}$.$\blacksquare$

If $\lambda(\theta\mid X) > 0$ on $\Theta$, and $\Theta^\circ$ is a connected subset of $\RR^d$, then the Gibbs sampler is irreducible (because we can get from anywhere to anywhere else by making tiny moves following a smooth path through the interior) and aperiodic (because there's a positive probability density on staying in the same place). If $\Theta$ is disconnected, however, the Gibbs sampler may not be irreducible: for example, if $\Theta = (-1,0)^2 \cup (0,1)^2 \in \RR^2$ (or if that is the support of the posterior), then there is no way to move between the two connected components by changing one coordinate at a time.

## Computational advantages of the Gibbs sampler

The great advantage of the Gibbs sampler when we have a graphical model is that, when we update $\theta_j$, all of the factors that *do not* involve $\theta_j$ cancel out of the numerator and the denominator. For example, in our hierarchical Gaussian model, when we update $\theta_j$ we have simply
$$
\lambda(\theta_j \mid \tau^2,\theta_{-j},X)
= \frac{\lambda(\theta_j \mid \tau^2) p_{\theta_j}(X_j)}{\int \lambda(\zeta \mid \tau^2)p_\zeta(X_j) \,d\zeta}.
$$
As we have set up the problem, this posterior distribution is very simple: we are back to the simple Bayes problem with a conjugate prior $\theta\sim N(0,\tau^2)$ and we just need to sample $\theta_j \sim N\left(\frac{\tau^2}{1+\tau^2}X_i, \frac{\tau^2}{1+\tau^2}\right)$.

Even if we did not get a lot of cancellations, or couldn't appeal to a simple conjugate prior update, a single Gibbs step would still be computationally tractable because the integral is only one-dimensional.

---

[← Markov chains](02-markov-chains.md) · [Up: contents](index.md) · [MCMC in practice →](04-mcmc-in-practice.md)

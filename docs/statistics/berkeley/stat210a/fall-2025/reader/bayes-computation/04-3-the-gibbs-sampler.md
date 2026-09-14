---
title: 3 The Gibbs sampler
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-computation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/bayes-computation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 The Gibbs sampler

**Source:** [`reader/bayes-computation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-computation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

There exist a multitude of MCMC algorithms, but we will focus on one that goes well with the hierarchical models we were discussing in the last lecture.

## <span class="header-section-number">3.1</span> Directed Graphical Models {.anchored number="3.1" anchor-id="directed-graphical-models"}

One special class of models that come up often in Bayesian modeling is **directed graphical models**. For a random vector <span class="math inline">\$Z=(Z\_1,\\ldots,Z\_d)\$</span> and directed graph <span class="math inline">\$G=(V,E)\$</span> on vertex set <span class="math inline">\$\\{1,\\ldots,d\\}\$</span>, we say the density <span class="math inline">\$p\$</span> is a directed graphical model if it can be factored as <span class="math display">\\$$ p(z) = \\prod\_{i=1}^d p\_i(z\_i \\mid z\_{\\text{Pa}(i)}), \\$$</span> where <span class="math inline">\$\\text{Pa}(i)\$</span> is the set of “parent vertices” that point to <span class="math inline">\$i\$</span>, that is <span class="math inline">\$\\text{Pa}(i)=\\{j:\\; j\\to i \\in E\\}\$</span>.

One example of a graphical model is the first <span class="math inline">\$T\$</span> steps of a Markov chain, whose distribution we can factor as <span class="math display">\\$$ \\pi\_0(x^{(0)}) \\prod\_{t=1}^{T} Q(x^{(t)} \\mid x^{(t-1)}), \\$$</span> giving the following graph:

``` {.sourceCode .js .code-with-copy}
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

<figure class="quarto-float quarto-float-fig figure">
<div aria-describedby="fig-markov-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
<div id="ojs-cell-1" data-nodetype="expression">

</div>
</div>
<figcaption>Figure 1: Markov chain graphical model</figcaption>
</figure>

The Gaussian hierarchical model <span class="math display">\\$$ \\begin{aligned} \\tau^2 &\\sim \\lambda\_0\\\\ \\theta\_i &\\simiid N(0,\\tau^2), \\quad \\text{ for } i = 1,\\ldots,d\\\\ X\_i \\mid \\theta &\\simind N(\\theta\_i,1) \\end{aligned} \\$$</span> is another example, with the following graph:

``` {.sourceCode .js .code-with-copy}
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

<figure class="quarto-float quarto-float-fig figure">
<div aria-describedby="fig-dgm-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
<div id="ojs-cell-2" data-nodetype="expression">

</div>
</div>
<figcaption>Figure 2: Hierarchical directed graphical model</figcaption>
</figure>

The graphical model form implies that we can write the joint distribution of the parameters and data as <span class="math display">\\$$ \\lambda\_0(\\tau^2)\\cdot \\prod\_{i=1}^d \\lambda(\\theta\_i \\mid \\tau^2) p\_{\\theta\_i}(x\_i), \\$$</span> giving one factor for each node.

## <span class="header-section-number">3.2</span> Gibbs sampler {.anchored number="3.2" anchor-id="gibbs-sampler"}

The Gibbs sampler is an MCMC algorithm that’s especially convenient for (sparsely connected) directed graphical models. We give the algorithm in terms of a parameter vector <span class="math inline">\$\\theta = (\\theta\_1,\\ldots,\\theta\_d)\$</span>, which we would like to sample from the posterior <span class="math inline">\$\\lambda(\\theta \\mid X)\$</span>. Let <span class="math inline">\$\\theta\_{-j} = (\\theta\_1,\\ldots,\\theta\_{j-1},\\theta\_{j+1},\\ldots,\\theta\_d)\$</span> denote the vector with the <span class="math inline">\$j\$</span>th coordinate removed.

**Gibbs Sampler Algorithm:**

Initialize <span class="math inline">\$\\theta = \\theta^{(0)}\$</span>

For <span class="math inline">\$t = 1, 2, \\ldots, T\$</span>:

For <span class="math inline">\$j=1,\\ldots, d\$</span>:

Resample <span class="math inline">\$\\theta\_j \\sim \\lambda(\\theta\_j \\mid \\theta\_{-j}, X)\$</span>

Record <span class="math inline">\$\\theta^{(t)}= \\theta\$</span>.

Return <span class="math inline">\$\\theta^{(0)},\\theta^{(1)},\\ldots,\\theta^{(T)}\$</span>.

By the instruction “Resample <span class="math inline">\$\\theta\_j\$</span>,” we mean hold <span class="math inline">\$\\theta\_{-j}\$</span> fixed and replace <span class="math inline">\$\\theta\_j\$</span> with a fresh draw from its conditional distribution given the rest.

Tip

There are two common variations on the inner loop where we update the <span class="math inline">\$d\$</span> coordinates of <span class="math inline">\$\\theta\$</span> one-by-one in order. We could instead either update the <span class="math inline">\$d\$</span> coordinates in a random order, or update a single random coordinate <span class="math inline">\$J^{(t)}\\sim \\text{Unif}\\{1,\\ldots,d\\}\$</span>.

Another variation is that it can sometimes be convenient to update blocks of covariates at a time; e.g. we could resample the pair <span class="math inline">\$(\\theta\_1,\\theta\_2)\$</span> from their joint distribution given <span class="math inline">\$(\\theta\_3,\\ldots,\\theta\_d)\$</span> and <span class="math inline">\$X\$</span>.

**Proposition:** The posterior <span class="math inline">\$\\pi(\\theta) = \\lambda(\\theta\\mid X)\$</span> is stationary for the Gibbs sampler algorithm.

*Proof:* The Gibbs sampler transition kernel is a composition of <span class="math inline">\$d\$</span> distinct transition kernels <span class="math inline">\$Q\_1,\\ldots,Q\_d\$</span> corresponding to the <span class="math inline">\$d\$</span> steps of the inner for loop. We begin by showing that <span class="math inline">\$\\pi\$</span> is stationary for each <span class="math inline">\$Q\_j\$</span>. Thus, if <span class="math inline">\$\\theta \\sim \\pi\$</span> and <span class="math inline">\$\\zeta \\mid \\theta \\sim Q\_j(\\cdot \\mid \\theta)\$</span>, we need to show that (marginally) <span class="math inline">\$\\zeta \\sim \\pi\$</span> as well.

Because <span class="math inline">\$\\zeta\_{-j} = \\theta\_{-j}\$</span> almost surely, they must have the same distribution. Moreover, <span class="math inline">\$\\theta\_j \\mid \\theta\_{-j}\$</span> is drawn from the distribution <span class="math inline">\$\\lambda(\\theta\_j \\mid \\theta\_{-j}, X)\$</span> by assumption, and <span class="math inline">\$\\zeta\_j \\mid \\theta\_{-j}\$</span> is also drawn from <span class="math inline">\$\\lambda(\\theta\_j \\mid \\theta\_{-j}, X)\$</span> by construction of the Gibbs sampler algorithm. Hence, <span class="math inline">\$\\zeta \\sim \\lambda(\\theta \\mid X)\$</span> as well.

Thus, we see that <span class="math inline">\$pi\$</span> is a stationary distribution for each <span class="math inline">\$Q\_j\$</span>; but then it follows that it is stationary for the composition of such kernels too. Define <span class="math inline">\$\\theta^{(t,0)}=\\theta^{(t)}\$</span>, then <span class="math inline">\$\\theta^{(t,1)}\$</span> to be the value after updating <span class="math inline">\$\\theta\_1\$</span> via <span class="math inline">\$Q\_1\$</span>, and so on up to <span class="math inline">\$\\theta^{(t,d)}=\\theta^{(t+1)}\$</span>. We have shown that, if <span class="math inline">\$\\theta^{(t,j-1)} \\sim \\pi\$</span>, then <span class="math inline">\$\\theta^{(t,j)}\\sim\\pi\$</span> as well, for every <span class="math inline">\$j\$</span>; it follows that if <span class="math inline">\$\\theta^{(t)}=\\theta^{(t,0)} \\sim \\pi\$</span>, then <span class="math inline">\$\\theta^{(t+1)}=\\theta^{(t,d)}\\sim \\pi\$</span> as well; hence <span class="math inline">\$\\pi\$</span> is stationary for the “full-update” kernel <span class="math inline">\$Q\$</span> that specifies the distribution of <span class="math inline">\$\\theta^{(t+1)}\$</span> given <span class="math inline">\$\\theta^{(t)}\$</span>.<span class="math inline">\$\\blacksquare\$</span>

If <span class="math inline">\$\\lambda(\\theta\\mid X) &gt; 0\$</span> on <span class="math inline">\$\\Theta\$</span>, and <span class="math inline">\$\\Theta^\\circ\$</span> is a connected subset of <span class="math inline">\$\\RR^d\$</span>, then the Gibbs sampler is irreducible (because we can get from anywhere to anywhere else by making tiny moves following a smooth path through the interior) and aperiodic (because there’s a positive probability density on staying in the same place). If <span class="math inline">\$\\Theta\$</span> is disconnected, however, the Gibbs sampler may not be irreducible: for example, if <span class="math inline">\$\\Theta = (-1,0)^2 \\cup (0,1)^2 \\in \\RR^2\$</span> (or if that is the support of the posterior), then there is no way to move between the two connected components by changing one coordinate at a time.

## <span class="header-section-number">3.3</span> Computational advantages of the Gibbs sampler {.anchored number="3.3" anchor-id="computational-advantages-of-the-gibbs-sampler"}

The great advantage of the Gibbs sampler when we have a graphical model is that, when we update <span class="math inline">\$\\theta\_j\$</span>, all of the factors that *do not* involve <span class="math inline">\$\\theta\_j\$</span> cancel out of the numerator and the denominator. For example, in our hierarchical Gaussian model, when we update <span class="math inline">\$\\theta\_j\$</span> we have simply <span class="math display">\\$$ \\lambda(\\theta\_j \\mid \\tau^2,\\theta\_{-j},X) = \\frac{\\lambda(\\theta\_j \\mid \\tau^2) p\_{\\theta\_j}(X\_j)}{\\int \\lambda(\\zeta \\mid \\tau^2)p\_\\zeta(X\_j) \\,d\\zeta}. \\$$</span> As we have set up the problem, this posterior distribution is very simple: we are back to the simple Bayes problem with a conjugate prior <span class="math inline">\$\\theta\\sim N(0,\\tau^2)\$</span> and we just need to sample <span class="math inline">\$\\theta\_j \\sim N\\left(\\frac{\\tau^2}{1+\\tau^2}X\_i, \\frac{\\tau^2}{1+\\tau^2}\\right)\$</span>.

Even if we did not get a lot of cancellations, or couldn’t appeal to a simple conjugate prior update, a single Gibbs step would still be computationally tractable because the integral is only one-dimensional.

---

[← 2 Markov chains](03-2-markov-chains.md) · [Up: contents](index.md) · [4 MCMC in practice →](05-4-mcmc-in-practice.md)

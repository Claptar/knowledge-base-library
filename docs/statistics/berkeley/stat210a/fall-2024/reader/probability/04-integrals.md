---
title: Integrals
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/probability.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/probability.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Integrals

**Source:** [`reader/probability.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/probability.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

One very nice thing about measures is that they let us define integrals of (nice enough) real-valued functions on $\cX$ with respect to the measure $\mu$, meaning the integral is "weighted" in a way that assigns total weight $\mu(A)$ to each set $A$. We will use the notation $\int f(x)\,\,d\mu(x)$, or just $\int f \,d\mu$.

To construct this integral, we begin by defining it for indicator functions, and then extend to more general functions by linearity and limits, in a few steps:

First, for an indicator function $1_A(x) = 1\{x \in A\}$ of a set $A \in \cF$, it is straightforward to define the integral as $\int 1_A \,d\mu = \mu(A)$ (note if $A \notin \cF$ this does not work, but we are only defining the integral for a class of "nice" functions determined by our $\sigma$-field)

Next, consider a *simple function* $f(x) = \sum_{i=1}^\infty c_i 1_{A_i}(x)$, with all $c_i \geq 0$ and $A_i \in \cF$. Because the integral should be linear, we should have

$$
\int f\,d\mu = \sum_{i=1}^\infty c_i \int 1_{A_i}\,d\mu = \sum_{i=1}^\infty c_i \mu(A_i)
$$

Third, we can extend to all sufficiently nice non-negative functions by approximating them from below with a series of simple functions:

$$
\int f\,d\mu = \lim_{n=1}^\infty \int f_n\,d\mu.
$$

For example, we could take the sequence of simple functions $$f_n(x) = \sum_{k=0}^{\infty} k 2^{-n} 1_{A_{n,k}}(x),\quad \text{ where } A_{n,k} = \left\{x:\; f(x) \in \left[k 2^{-n}, (k+1) 2^{-n}\right)\right\},$$ as illustrated in the picture below.

```ojs
//| echo: false

// Import libraries using require
Plot = require("@observablehq/plot")
d3 = require("d3")

// Define the Gaussian function
function gaussian(x, mu = 0, sigma = 1) {
  return (1 / (sigma * Math.sqrt(2 * Math.PI))) *
    Math.exp(-0.5 * Math.pow((x - mu) / sigma, 2));
}

// Define our function f(x) = 3g(x-4) + 5g(x-7)
function f(x) {
  return 3 * gaussian(x - 4, 0, 1) + 4.8 * gaussian(x - 7, 0, 1);
}

// Create a slider for 'c'
viewof c = Inputs.range([0, 4], {step: 1, label: "n"})

// Generate x values
xValues = d3.range(-2, 13, 0.01)

// Calculate y values
data = xValues.map(x => ({x, y: f(x)}))

// Calculate Lebesgue sets with multiple intervals
function calculateLebesgueSets(data, c) {
  const maxY = d3.max(data, d => d.y);
  const sets = d3.range(0, Math.ceil(maxY * Math.pow(2, c))).map(k => {
    const lower = k * Math.pow(2, -c);
    const upper = (k + 1) * Math.pow(2, -c);
    const points = data.filter(d => d.y > lower && d.y <= upper);

    if (points.length > 0) {
      // Identify distinct intervals
      const intervals = [];
      let currentInterval = [points[0]];
      for (let i = 1; i < points.length; i++) {
        if (points[i].x - points[i-1].x <= 0.011) { // Allow small gaps
          currentInterval.push(points[i]);
        } else {
          intervals.push(currentInterval);
          currentInterval = [points[i]];
        }
      }
      intervals.push(currentInterval);

      return {
        k,
        lower,
        upper,
        intervals: intervals.map(interval => ({
          xMin: d3.min(interval, d => d.x),
          xMax: d3.max(interval, d => d.x),
          points: interval
        }))
      };
    }
    return null;
  }).filter(set => set !== null);

  return sets;
}

lebesgueSets = calculateLebesgueSets(data, c)

// Create the plot
plot = Plot.plot({
  marks: [
    Plot.line(data, {x: "x", y: "y", stroke: "gray", strokeWidth: 1}),
    Plot.dot(lebesgueSets.flatMap(set => set.intervals.flatMap(int => int.points)), {
      x: "x",
      y: "y",
      fill: d => d3.schemeCategory10[lebesgueSets.findIndex(s => s.intervals.some(int => int.points.includes(d))) % 10],
      r: 2
    }),
    Plot.rectY(lebesgueSets.flatMap(set =>
      set.intervals.map(int => ({
        x1: int.xMin,
        x2: int.xMax,
        y1: 0,
        y2: set.lower,
        color: set.k
      }))
    ), {
      x1: "x1",
      x2: "x2",
      y1: "y1",
      y2: "y2",
      fill: d => d3.schemeCategory10[d.color % 10],
      fillOpacity: 0.2,
      stroke: d => d3.schemeCategory10[d.color % 10],
      strokeOpacity: 0.5
    })
  ],
  y: {
    domain: [0, d3.max(data, d => d.y) * 1.1],
    label: "f(x)"
  },
  x: {
    domain: [-2, 13],
    label: "x"
  },
  style: {
    backgroundColor: "white"
  },
  width: 800,
  height: 500
})
```

Finally, we can write any real-valued function as the sum of its positive and negative parts, $f(x) = f^+(x) - f^-(x)$, where $f^+(x) = \max\{f(x), 0\}$ and $f^-(x) = \max\{-f(x), 0\}$. Then both $f^+$ and $f^-$ have non-negative (possibly infinite) integrals. Then we simply take

$$
\int f\,d\mu = \int f^+\,d\mu - \int f^-\,d\mu \in [-\infty, \infty],
$$

calling the difference undefined if the integrals of both $f^+$ and $f^-$ are infinite.

As a result, we have $\int f\,d\mu$ for any function $f$ whose positive and negative parts can both be approximated from below by simple functions. Note that we have left out some important details in this presentation (for example we have not characterized which functions $f$ are nice enough to be approximated well by simple functions) but these details are unimportant for this class. The important thing to know is that to any measure $\mu$ there corresponds a well-defined integral $\int \cdot \,d\mu$, which behaves as we would expect it to.

We can now return to our previous examples of measures and ask what the corresponding integrals are:

**Example 1, continued (Counting measure):** An integral with respect to $\#$ just adds up all the values of $f(x)$:

$$
\int f\,d\# = \sum_{x\in \cX} f(x)
$$

**Example 2, continued (Lebesgue measure):** An integral with respect to the Lebesgue measure is called a *Lebesgue integral*, which is essentially just the usual integral you are used to from calculus class:

$$
\int f\,d\lambda = \int\cdots \int f(x) \,d x_1 \cdots \,d x_n.
$$

The Lebesgue integral extends the Riemann integral to a more general class of functions, in the sense that if the Riemann integral of $f$ is defined then the Lebesgue integral is also well defined and the two integrals coincide. But the Lebesgue integral is also well-defined for functions like $f(x) = 1\{x \in \mathbb{Q}\}$, for which the Riemann integral is not well-defined (**Exercise:** what is the Lebesgue integral of $1\{x \in \mathbb{Q}\}$?)

**Example 3, continued (Gaussian measure):** Note that $P_Z(A)$ is defined as the (Lebesgue) integral of $1_A(x)\phi(x)$. By extension, the integral of $f$ with respect to $P_Z$ is the Lebesgue integral of $f(x) \phi(x)$, which is nothing more than the expectation of $f(Z)$:

$$
\int f\,d P_Z = \int_{-\infty}^\infty f(x) \phi(x) \,d x = \EE[f(Z)].
$$

---

[← Measures](03-measures.md) · [Up: contents](index.md) · [Densities →](05-densities.md)

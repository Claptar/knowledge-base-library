---
title: Integrals
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/probability.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/probability.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/probability.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/probability.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Integrals

One very nice thing about measures is that they let us define integrals of (nice enough) real-valued functions on $\cX$ with respect to the measure $\mu$, meaning the integral is “weighted” in a way that assigns total weight $\mu(A)$ to each set $A$. We will use the notation $\int f(x)\,\,d\mu(x)$, or just $\int f \,d\mu$.

To construct this integral, we begin by defining it for indicator functions, and then extend to more general functions by linearity and limits, in a few steps:

First, for an indicator function $1_A(x) = 1\{x \in A\}$ of a set $A \in \cF$, it is straightforward to define the integral as $\int 1_A \,d\mu = \mu(A)$ (note if $A \notin \cF$ this does not work, but we are only defining the integral for a class of “nice” functions determined by our $\sigma$-field)

Next, consider a *simple function* $f(x) = \sum_{i=1}^\infty c_i 1_{A_i}(x)$, with all $c_i \geq 0$ and $A_i \in \cF$. Because the integral should be linear, we should have

$$
\int f\,d\mu = \sum_{i=1}^\infty c_i \int 1_{A_i}\,d\mu = \sum_{i=1}^\infty c_i \mu(A_i)
$$

Third, we can extend to all sufficiently nice non-negative functions by approximating them from below with a series of simple functions:

$$
\int f\,d\mu = \lim_{n=1}^\infty \int f_n\,d\mu.
$$

For example, we could take the sequence of simple functions

$$
f_n(x) = \sum_{k=0}^{\infty} k 2^{-n} 1_{A_{n,k}}(x),\quad \text{ where } A_{n,k} = \left\{x:\; f(x) \in \left[k 2^{-n}, (k+1) 2^{-n}\right)\right\},
$$

 as illustrated in the picture below.

``` {.sourceCode .js .code-with-copy}
phi = (x) => (1 / Math.sqrt(2 * Math.PI)) * Math.exp(-0.5 * x * x)

// Define our target function f(x) = 3*phi(x-4) + 5*phi(x-7)
f = (x) => 3 * phi(x - 4) + 5 * phi(x - 7)

// Slider for n value
viewof n = Inputs.range([0, 5], {value: 2, step: 1, label: "n"})

// Calculate c_n = 2^(-n)
c_n = Math.pow(2, -n)

// Define the simple function f_n(x) - f(x) rounded down to nearest multiple of c_n
f_n = (x) => {
  const fValue = f(x);
  return Math.floor(fValue / c_n) * c_n;
}

// Create data points for both functions
data = {
  const xMin = 0;
  const xMax = 11;
  const numPoints = 1000;
  const dx = (xMax - xMin) / (numPoints - 1);

  return Array.from({length: numPoints}, (_, i) => {
    const x = xMin + i * dx;
    return {
      x: x,
      f_original: f(x),
      f_simple: f_n(x)
    };
  });
}

// Create the plot
Plot.plot({
  width: 800,
  height: 400,
  marginTop: 60,
  marginLeft: 100,
  marginBottom: 100,
  marginRight: 120,
  style: {
    fontSize: "18px"
  },
  x: {
    domain: [0, 11],
    label: "x",
    labelAnchor: "center",
    labelOffset: 60
  },
  y: {
    domain: [0, Math.max(...data.map(d => d.f_original)) * 1.1],
    label: "f(x)",
    labelAnchor: "center",
    labelOffset: 70
  },
  marks: [
    Plot.line(data, {x: "x", y: "f_original", stroke: "steelblue", strokeWidth: 2}),
    Plot.line(data, {x: "x", y: "f_simple", stroke: "red", strokeWidth: 2}),
    Plot.ruleY([0]),
    Plot.text([`Approximating a smooth function from below with simple functions`], {
      x: 5.5,
      y: Math.max(...data.map(d => d.f_original)) * 1.15,
      fontSize: 18,
      fontWeight: "bold",
      textAnchor: "middle"
    }),
    // Legend with colored lines
    Plot.lineX([{x: 9.2, y: Math.max(...data.map(d => d.f_original)) * 0.95},
                {x: 9.8, y: Math.max(...data.map(d => d.f_original)) * 0.95}], {
      x: "x", y: "y",
      stroke: "steelblue",
      strokeWidth: 2
    }),
    Plot.text(["f(x)"], {
      x: 10,
      y: Math.max(...data.map(d => d.f_original)) * 0.95,
      fontSize: 16,
      fill: "black",
      textAnchor: "start"
    }),
    Plot.lineX([{x: 9.2, y: Math.max(...data.map(d => d.f_original)) * 0.88},
                {x: 9.8, y: Math.max(...data.map(d => d.f_original)) * 0.88}], {
      x: "x", y: "y",
      stroke: "red",
      strokeWidth: 2
    }),
    Plot.text([`fₙ(x)`], {
      x: 10,
      y: Math.max(...data.map(d => d.f_original)) * 0.88,
      fontSize: 16,
      fill: "black",
      textAnchor: "start"
    })
  ]
})
```

Old version:

Finally, we can write any real-valued function as the sum of its positive and negative parts, $f(x) = f^+(x) - f^-(x)$, where $f^+(x) = \max\{f(x), 0\}$ and $f^-(x) = \max\{-f(x), 0\}$. Then both $f^+$ and $f^-$ have non-negative (possibly infinite) integrals. Then we simply take

$$
\int f\,d\mu = \int f^+\,d\mu - \int f^-\,d\mu \in [-\infty, \infty],
$$

calling the difference undefined if the integrals of both $f^+$ and $f^-$ are infinite.

As a result, we have $\int f\,d\mu$ for any function $f$ whose positive and negative parts can both be approximated from below by simple functions. Note that we have left out some important details in this presentation (for example we have not characterized which functions $f$ are nice enough to be approximated well by simple functions) but these details are unimportant for this class. The important thing to know is that to any measure $\mu$ there corresponds a well-defined integral $\int \cdot \,d\mu$, which behaves as we would expect it to.

We can now return to our previous examples of measures and ask what the corresponding integrals are:

**Example 1, continued (Counting measure):** An integral with respect to $#$ just adds up all the values of $f(x)$:

$$
\int f\,d# = \sum_{x\in \cX} f(x)
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

---
title: Integrals
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/probability.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/probability.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Integrals

**Source:** [`units/reader/probability.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/probability.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

One very nice thing about measures is that they let us define integrals of (nice enough) real-valued functions on <span class="math inline">\$\\cX\$</span> with respect to the measure <span class="math inline">\$\\mu\$</span>, meaning the integral is “weighted” in a way that assigns total weight <span class="math inline">\$\\mu(A)\$</span> to each set <span class="math inline">\$A\$</span>. We will use the notation <span class="math inline">\$\\int f(x)\\,\\,d\\mu(x)\$</span>, or just <span class="math inline">\$\\int f \\,d\\mu\$</span>.

To construct this integral, we begin by defining it for indicator functions, and then extend to more general functions by linearity and limits, in a few steps:

First, for an indicator function <span class="math inline">\$1\_A(x) = 1\\{x \\in A\\}\$</span> of a set <span class="math inline">\$A \\in \\cF\$</span>, it is straightforward to define the integral as <span class="math inline">\$\\int 1\_A \\,d\\mu = \\mu(A)\$</span> (note if <span class="math inline">\$A \\notin \\cF\$</span> this does not work, but we are only defining the integral for a class of “nice” functions determined by our <span class="math inline">\$\\sigma\$</span>-field)

Next, consider a *simple function* <span class="math inline">\$f(x) = \\sum\_{i=1}^\\infty c\_i 1\_{A\_i}(x)\$</span>, with all <span class="math inline">\$c\_i \\geq 0\$</span> and <span class="math inline">\$A\_i \\in \\cF\$</span>. Because the integral should be linear, we should have

<span class="math display">\\$$ \\int f\\,d\\mu = \\sum\_{i=1}^\\infty c\_i \\int 1\_{A\_i}\\,d\\mu = \\sum\_{i=1}^\\infty c\_i \\mu(A\_i) \\$$</span>

Third, we can extend to all sufficiently nice non-negative functions by approximating them from below with a series of simple functions:

<span class="math display">\\$$ \\int f\\,d\\mu = \\lim\_{n=1}^\\infty \\int f\_n\\,d\\mu. \\$$</span>

For example, we could take the sequence of simple functions <span class="math display">\\$$f\_n(x) = \\sum\_{k=0}^{\\infty} k 2^{-n} 1\_{A\_{n,k}}(x),\\quad \\text{ where } A\_{n,k} = \\left\\{x:\\; f(x) \\in \\left\[k 2^{-n}, (k+1) 2^{-n}\\right)\\right\\},\\$$</span> as illustrated in the picture below.

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

Finally, we can write any real-valued function as the sum of its positive and negative parts, <span class="math inline">\$f(x) = f^+(x) - f^-(x)\$</span>, where <span class="math inline">\$f^+(x) = \\max\\{f(x), 0\\}\$</span> and <span class="math inline">\$f^-(x) = \\max\\{-f(x), 0\\}\$</span>. Then both <span class="math inline">\$f^+\$</span> and <span class="math inline">\$f^-\$</span> have non-negative (possibly infinite) integrals. Then we simply take

<span class="math display">\\$$ \\int f\\,d\\mu = \\int f^+\\,d\\mu - \\int f^-\\,d\\mu \\in \[-\\infty, \\infty$$, \\\]</span>

calling the difference undefined if the integrals of both <span class="math inline">\$f^+\$</span> and <span class="math inline">\$f^-\$</span> are infinite.

As a result, we have <span class="math inline">\$\\int f\\,d\\mu\$</span> for any function <span class="math inline">\$f\$</span> whose positive and negative parts can both be approximated from below by simple functions. Note that we have left out some important details in this presentation (for example we have not characterized which functions <span class="math inline">\$f\$</span> are nice enough to be approximated well by simple functions) but these details are unimportant for this class. The important thing to know is that to any measure <span class="math inline">\$\\mu\$</span> there corresponds a well-defined integral <span class="math inline">\$\\int \\cdot \\,d\\mu\$</span>, which behaves as we would expect it to.

We can now return to our previous examples of measures and ask what the corresponding integrals are:

**Example 1, continued (Counting measure):** An integral with respect to <span class="math inline">\$\\#\$</span> just adds up all the values of <span class="math inline">\$f(x)\$</span>:

<span class="math display">\\$$ \\int f\\,d\\# = \\sum\_{x\\in \\cX} f(x) \\$$</span>

**Example 2, continued (Lebesgue measure):** An integral with respect to the Lebesgue measure is called a *Lebesgue integral*, which is essentially just the usual integral you are used to from calculus class:

<span class="math display">\\$$ \\int f\\,d\\lambda = \\int\\cdots \\int f(x) \\,d x\_1 \\cdots \\,d x\_n. \\$$</span>

The Lebesgue integral extends the Riemann integral to a more general class of functions, in the sense that if the Riemann integral of <span class="math inline">\$f\$</span> is defined then the Lebesgue integral is also well defined and the two integrals coincide. But the Lebesgue integral is also well-defined for functions like <span class="math inline">\$f(x) = 1\\{x \\in \\mathbb{Q}\\}\$</span>, for which the Riemann integral is not well-defined (**Exercise:** what is the Lebesgue integral of <span class="math inline">\$1\\{x \\in \\mathbb{Q}\\}\$</span>?)

**Example 3, continued (Gaussian measure):** Note that <span class="math inline">\$P\_Z(A)\$</span> is defined as the (Lebesgue) integral of <span class="math inline">\$1\_A(x)\\phi(x)\$</span>. By extension, the integral of <span class="math inline">\$f\$</span> with respect to <span class="math inline">\$P\_Z\$</span> is the Lebesgue integral of <span class="math inline">\$f(x) \\phi(x)\$</span>, which is nothing more than the expectation of <span class="math inline">\$f(Z)\$</span>:

<span class="math display">\\$$ \\int f\\,d P\_Z = \\int\_{-\\infty}^\\infty f(x) \\phi(x) \\,d x = \\EE\[f(Z)$$. \\\]</span>

---

[← Measures](04-measures.md) · [Up: contents](index.md) · [Densities →](06-densities.md)

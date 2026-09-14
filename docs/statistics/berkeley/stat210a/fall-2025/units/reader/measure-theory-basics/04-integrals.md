---
title: Integrals
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/measure-theory-basics.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/measure-theory-basics.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Integrals

**Source:** [`units/reader/measure-theory-basics.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/measure-theory-basics.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

One very nice thing about measures is that they let us define integrals of (nice enough) real-valued functions on <span class="math inline">\$\\cX\$</span> with respect to the measure <span class="math inline">\$\\mu\$</span>, meaning the integral is “weighted” in a way that assigns total weight <span class="math inline">\$\\mu(A)\$</span> to each set <span class="math inline">\$A\$</span>. We will use the notation <span class="math inline">\$\\int f(x)\\,\\td\\mu(x)\$</span>, or just <span class="math inline">\$\\int f \\td\\mu\$</span>.

To construct this integral, we begin by defining it for indicator functions, and then extend to more general functions by linearity and limits, in a few steps:

First, for an indicator function <span class="math inline">\$1\_A(x) = 1\\{x \\in A\\}\$</span> of a set <span class="math inline">\$A \\in \\cF\$</span>, it is straightforward to define the integral as <span class="math inline">\$\\int 1\_A \\td\\mu = \\mu(A)\$</span> (note if <span class="math inline">\$A \\notin \\cF\$</span> this does not work, but we are only defining the integral for a class of “nice” functions determined by our <span class="math inline">\$\\sigma\$</span>-field)

Next, consider a *simple function* <span class="math inline">\$f(x) = \\sum\_{i=1}^\\infty c\_i 1\_{A\_i}(x)\$</span>, with all <span class="math inline">\$c\_i \\geq 0\$</span> and <span class="math inline">\$A\_i \\in \\cF\$</span>. Because the integral should be linear, we should have

<span class="math display">\\$$ \\int f\\td\\mu = \\sum\_{i=1}^\\infty c\_i \\int 1\_{A\_i}\\td\\mu = \\sum\_{i=1}^\\infty c\_i \\mu(A\_i) \\$$</span>

Third, we can extend to all sufficiently nice non-negative functions by approximating them from below with a series of simple functions:

<span class="math display">\\$$ \\int f\\td\\mu = \\lim\_{i=1}^\\infty \\int f\_i\\td\\mu. \\$$</span>

This idea is illustrated in the picture below:

<figure class="figure">
<p><img src="images/Screenshot%202023-08-23%20at%2011.16.18%20PM.png" class="img-fluid figure-img" /></p>
<figcaption>Approximating a non-negative function from below by a series of simple (piecewise constant) functions. The red function is an indicator, the blue function is a simple function, and the dashed orange function is a simple function that approximates the orange curve.</figcaption>
</figure>

Finally, we can write any real-valued function as the sum of its positive and negative parts, <span class="math inline">\$f(x) = f^+(x) - f^-(x)\$</span>, where <span class="math inline">\$f^+(x) = \\max\\{f(x), 0\\}\$</span> and <span class="math inline">\$f^-(x) = \\max\\{-f(x), 0\\}\$</span>. Then both <span class="math inline">\$f^+\$</span> and <span class="math inline">\$f^-\$</span> have non-negative (possibly infinite) integrals. Then we simply take

<span class="math display">\\$$ \\int f\\td\\mu = \\int f^+\\td\\mu - \\int f^-\\td\\mu \\in \[-\\infty, \\infty$$, \\\]</span>

calling the difference undefined if the integrals of both <span class="math inline">\$f^+\$</span> and <span class="math inline">\$f^-\$</span> are infinite.

As a result, we have <span class="math inline">\$\\int f\\td\\mu\$</span> for any function <span class="math inline">\$f\$</span> whose positive and negative parts can both be approximated from below by simple functions. Note that we have left out some important details in this presentation (for example we have not characterized which functions <span class="math inline">\$f\$</span> are nice enough to be approximated well by simple functions) but these details are unimportant for this class. The important thing to know is that to any measure <span class="math inline">\$\\mu\$</span> there corresponds a well-defined integral <span class="math inline">\$\\int \\cdot \\td\\mu\$</span>, which behaves as we would expect it to.

We can now return to our previous examples of measures and ask what the corresponding integrals are:

**Example 1, continued (Counting measure):** An integral with respect to <span class="math inline">\$\\#\$</span> just adds up all the values of <span class="math inline">\$f(x)\$</span>:

<span class="math display">\\$$ \\int f\\td\\# = \\sum\_{x\\in \\cX} f(x) \\$$</span>

**Example 2, continued (Lebesgue measure):** An integral with respect to the Lebesgue measure is called a *Lebesgue integral*, which is essentially just the usual integral you are used to from calculus class:

<span class="math display">\\$$ \\int f\\td\\lambda = \\int\\cdots \\int f(x) \\td x\_1 \\cdots \\td x\_n. \\$$</span>

The Lebesgue integral extends the Riemann integral to a more general class of functions, in the sense that if the Riemann integral of <span class="math inline">\$f\$</span> is defined then the Lebesgue integral is also well defined and the two integrals coincide. But the Lebesgue integral is also well-defined for functions like <span class="math inline">\$f(x) = 1\\{x \\in \\mathbb{Q}\\}\$</span>, for which the Riemann integral is not well-defined (**Exercise:** what is the Lebesgue integral of <span class="math inline">\$1\\{x \\in \\mathbb{Q}\\}\$</span>?)

**Example 3, continued (Gaussian measure):** Note that <span class="math inline">\$P\_Z(A)\$</span> is defined as the (Lebesgue) integral of <span class="math inline">\$1\_A(x)\\phi(x)\$</span>. By extension, the integral of <span class="math inline">\$f\$</span> with respect to <span class="math inline">\$P\_Z\$</span> is the Lebesgue integral of <span class="math inline">\$f(x) \\phi(x)\$</span>, which is nothing more than the expectation of <span class="math inline">\$f(Z)\$</span>:

<span class="math display">\\$$ \\int f\\td P\_Z = \\int\_{-\\infty}^\\infty f(x) \\phi(x) \\td x = \\EE\[f(Z)$$. \\\]</span>

---

[← Measures](03-measures.md) · [Up: contents](index.md) · [Densities →](05-densities.md)

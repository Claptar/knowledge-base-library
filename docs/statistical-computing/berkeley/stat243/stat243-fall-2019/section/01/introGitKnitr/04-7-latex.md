---
title: 7) LaTeX
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/01/introGitKnitr.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/01/introGitKnitr.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 7) LaTeX

**Source:** [`section/01/introGitKnitr.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/01/introGitKnitr.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Rmarkdown files render LaTeX through an external generator. This means that you can
write any math equations or LaTeX syntax within a specific chunk, and install the
required LaTeX libraries outside of R, and it will be rendered properly.

Inline code chunks are setoff with single dollar signs, ie `$\beta$` is rendered
as $\beta$. This is great for small equations, Greek letters, and references to variables.

LaTeX chunks can also be significantly more complicated. Independent chunks are
setoff with double dollar signs, ie `$$ Complex LaTeX Thing $$`, such as the following
equation:
$$
D(\theta_l,T_x) = \left\{
         \begin{array}{ll}
             \theta_{l[0]}^{'}=\theta_l 								& \quad i = 0 \\
             \theta_{l[i+1]}^{'} = \theta_{l[i]}^{'} *F(\overline{L_{[t-i-T_x]}})	& \quad i \leq T_l
         \end{array}
     \right.
$$

---

[← 6) Code chunks](03-6-code-chunks.md) · [Up: contents](index.md) · [Submitting problem sets →](05-submitting-problem-sets.md)

---
title: 'Model-based Inference: The Z-Test'
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/02-randomization-tests/lab.md
source_file: sources/berkeley-stat158/spring-2026/labs/02-randomization-tests/lab.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Model-based Inference: The Z-Test

**Source:** [`labs/02-randomization-tests/lab.md`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/labs/02-randomization-tests/lab.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

9.  Before we conduct our z-test, we should be explicit about our
    hypothesis and assumptions. Answer the following questions in brief,
    but complete sentences.

**Q:** What is the null hypothesis of our z-test in the context of our
specific problem? Is it different from that of the permutation test?
**A:**\
\
\
\

**Q:** What assumptions are required by the z-test?\
**A:**\
\
\
\

Note that though we are working with binary data, the proportion of 1's
can often be well approximated by a normal distribution, particularly
with larger sample sizes. Thus a z-test is still valid in such settings.

10. Fortunately, `R` has a built-in function, called `prop.test`, that
    conducts a two-sample z-test on such binary data. Run the test on
    the Many Labs data in the chunk below and report the p-value. Be
    sure to add `correct = FALSE.` in the arguments.

::: cell
``` {.r .cell-code}
# conduct a two-sample z-test
# ex: prop.test((p1, p2), (n1, n2), correct = FALSE)
```
:::

Run this on your own collected data as well.

::: cell
``` {.r .cell-code}
# conduct a two-sample z-test
```
:::

**Q:** What can you conclude from the above two test results?\
**A:**\
\
\
\

**Q:** What do you think this tells you about the power of the z-test
and the normal approximation?\
**A:**\
\
\
\

---

[← Non-parametric Methods: Randomization Tests](06-non-parametric-methods-randomization-tests.md) · [Up: contents](index.md)

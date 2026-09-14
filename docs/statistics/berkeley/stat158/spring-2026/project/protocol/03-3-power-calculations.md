---
title: 3. Power Calculations
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/project/protocol.pdf
source_file: sources/berkeley-stat158/spring-2026/project/protocol.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. Power Calculations

**Source:** [`project/protocol.pdf`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/project/protocol.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

See the lab assignment on power for details about how to calculate power for a more complicated design. Note that the effect sizes (i.e. parameter values) should be set to the smallest value that would be scientifically meaningful to you. Ideally, you would obtain power of roughly 0.7-0.95 for all of your tests. If your power curve suggests you a sample size that is not feasible for this experiment, you can pick the largest feasible sample size even if that means you will have lower power.

If you find that the number of samples is surprisingly small then bump it up to a larger number that is still feasible. For example, if it suggests only 3 blocks for a blocking design, that is probably surprisingly small, particularly if blocks are subjects. However, if you are running a factorial with a large number of treatment

1

combinations (e.g. 12+ combinations), then 𝑛= 3 replications would imply a lot of individual observations (36+), so that’s not surprisingly small.

If you get surprisingly small 𝑛, there are two common problems that might be causing it, so look more closely before you finish: 1) You defined the effects you want to be able to detect as very far apart. While not always an error, if the effect size you defined was not realistic for what you could reasonably hope to see if the alternative was true, then your power analysis is not going to provide relevant guidance for obtaining a practically interesting answer to your research question. 2) You have done the power calculations incorrectly.

---

[← 2. Estimate 𝜎2 for Power Calculations](02-2-estimate-𝜎2-for-power-calculations.md) · [Up: contents](index.md) · [4. Final assignments of treatments →](04-4-final-assignments-of-treatments.md)

---
title: 'Example: Gene-level tests'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/stagewiseTesting.pdf
source_file: sources/statomics-sga21/docs/stagewiseTesting.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Example: Gene-level tests

**Source:** [`docs/stagewiseTesting.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/stagewiseTesting.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
all hypotheses null genes<br>1% 5% 10% 1% 5% 10%<br>False discovery rate cut-off<br>0.10<br>0.05<br>Empirical false discovery proportion<br>0.01<br><!-- End of picture text -->

11 / 17


<!-- Start of picture text -->
However, we lose resolution on the<br><!-- End of picture text -->

Example transcript level analysis: control FDR on gene level by aggregated testing

A simple strategy would be to

> 1 Aggregate p-values across hypotheses (i.e. omnibus test)

> 2 Control FDR on level _αI_ on the aggregated p-values

12 / 17

Example transcript level analysis: control FDR on gene level by aggregated testing

A simple strategy would be to

> 1 Aggregate p-values across hypotheses (i.e. omnibus test)

> 2 Control FDR on level _αI_ on the aggregated p-values Additionally takes advantage of aggregated tests with higher sensitivity


<!-- Start of picture text -->
B<br><!-- End of picture text -->

However, we **lose resolution on the biology**

12 / 17

---

[← Example](09-example.md) · [Up: contents](index.md) · [Solution: Stage-wise testing procedure: aggregate and split evidence →](11-solution-stage-wise-testing-procedure-aggregate-and-split-ev.md)

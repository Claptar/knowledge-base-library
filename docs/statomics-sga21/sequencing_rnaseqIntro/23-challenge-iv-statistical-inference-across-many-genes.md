---
title: 'Challenge IV: Statistical inference across many genes'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Challenge IV: Statistical inference across many genes

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Contrasts on the treatment effects

We will first derive all contrasts that are also investigated in the original manuscript, using our extended model where we are allowing for an interaction effect between treatment and time.

The mean model is
$$ \log(\mu_{gi}) = \beta_{g0} + \beta_{g1} x_{DPN} + \beta_{g2} x_{OHT} + \beta_{g3} x_{48h} + \beta_{g4} x_{pat2} + \beta_{g5} x_{pat3} + \beta_{g6} x_{pat4} + \\ \beta_{g7} x_{DPN:48h} + \beta_{g8} x_{OHT:48h}. $$

The intercept corresponds to the log average gene expression in the control group at 24h for patient 1.

**DPN 24h vs control 24h.**
The respective means are
$$\log \mu_{g,DPN,24h} = \beta_{g0} + \beta_{g1},$$
$$\log \mu_{g,con,24h} = \beta_{g0}.$$
And their difference is
$$ \delta_g = \beta_{g1}. $$

**DPN 48h vs control 48h.**
The respective means are
$$\log \mu_{g,DPN,48h} = \beta_{g0} + \beta_{g1} + \beta_{g3} + \beta_{g7},$$
$$\log \mu_{g,con,48h} = \beta_{g0} + \beta_{g3}.$$
And their difference is
$$ \delta_g = \beta_{g1} + \beta_{g7}. $$

**OHT 24h vs control 24h.**
The respective means are
$$\log \mu_{g,OHT,24h} = \beta_{g0} + \beta_{g2} ,$$
$$\log \mu_{g,con,24h} = \beta_{g0}.$$
And their difference is
$$ \delta_g = \beta_{g2}. $$

**OHT 48h vs control 48h.**
The respective means are
$$\log \mu_{g,OHT,48h} = \beta_{g0} + \beta_{g2} + \beta_{g3} + \beta_{g8},$$
$$\log \mu_{g,con,48h} = \beta_{g0} + \beta_{g3}.$$
And their difference is
$$ \delta_g = \beta_{g2} + \beta_{g8}. $$

However, we can also assess the interaction effects: is the time effect different between DPN and OHT treatment versus the control? And how about the DPN vs OHT treatments?

**DPN vs control interaction.**
The time effect for each condition is
$$ \delta_{DPN} = \log \mu_{g,DPN,48h} - \log \mu_{g,DPN,24h} = \beta_{g3} + \beta_{g7},$$
$$ \delta_{con} = \log \mu_{g,con,48h} - \log \mu_{g,con,24h} = \beta_{g3}. $$
So the interaction effect is
$$\delta_{DPN-con} = \beta_{g7}.$$

**OHT vs control interaction.**
The time effect for each condition is
$$ \delta_{OHT} = \log \mu_{g,OHT,48h} - \log \mu_{g,OHT,24h} = \beta_{g3} + \beta_{g8},$$
$$ \delta_{con} = \log \mu_{g,con,48h} - \log \mu_{g,con,24h} = \beta_{g3}. $$
So the interaction effect is
$$\delta_{DPN-con} = \beta_{g8}.$$

**OHT vs DPN interaction.**
The time effect for each condition is
$$ \delta_{OHT} = \log \mu_{g,OHT,48h} - \log \mu_{g,OHT,24h} = \beta_{g3} + \beta_{g8},$$
$$ \delta_{DPN} = \log \mu_{g,DPN,48h} - \log \mu_{g,DPN,24h} = \beta_{g3} + \beta_{g7},$$
So the interaction effect is
$$\delta_{OHT-DPN} = \beta_{g8} - \beta_{g7}.$$

Let's implement all of these in a contrast matrix.

```r
L <- matrix(0, nrow = ncol(fit$coefficients), ncol = 7)
rownames(L) <- colnames(fit$coefficients)
colnames(L) <- c("DPNvsCON24", "DPNvsCON48",
                 "OHTvsCON24", "OHTvsCON48",
                 "DPNvsCONInt", "OHTvsCONInt",
                 "OHTvsDPNInt")

---

[← All defaults](22-all-defaults.md) · [Up: contents](index.md) · [DPN vs control at 24h →](24-dpn-vs-control-at-24h.md)

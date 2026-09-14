---
title: Stage-wise testing procedure1
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/stagewiseTesting.pdf
source_file: sources/statomics-sga21/docs/stagewiseTesting.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stage-wise testing procedure1

**Source:** [`docs/stagewiseTesting.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/stagewiseTesting.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## 1 **Screening Stage:**


Assess the screening hypothesis _Hg_<sup>_S_/globalnullhypothesisfor</sup> all genes/proteins in the set _G_ .

Apply the Benjamini Hochberg (BH) FDR procedure to the screening p-values at FDR level _α_ . Let _R_ be the number of rejected screening hypotheses.

- 2 **Confirmation Stage:** For all _R_ genes/proteins that pass the screening stage.


Let _αII_ = _Rα/G_ be FDR-adjusted significance level from the first stage.

Adopt a multiple testing procedure to assess all _ng_ hypotheses while controlling the within gene error rate at the adjusted level _αII_ .

> 1Heller et al. 2009, Bioinformatics.

14 / 17

DGE experiments with complex designs


Our procedure correctly controls the FDR at gene-level The omnibus test enriches for genes with interaction effects While maintaining equivalent power for main effects


<!-- Start of picture text -->
Conventional Conventional Conventional<br>Stage-wise Stage-wise Stage-wise<br>1% 5% 10% 1% 5% 10% 1% 5% 10%<br>False discovery rate cut-off<br>0.6<br>0.65<br>0.10<br>0.5 0.60<br>0.55<br>OFDR 0.4<br>0.05<br>Power main effect<br>Power interaction effect 0.50<br>0.3<br>0.45<br>0.01<br><!-- End of picture text -->

15 / 17

Stage-wise testing unlocks powerful transcript-level analysis


Naturally unites high gene-level power with transcript-level resolution of the results Equal or better power at transcript level Better FDR control


<!-- Start of picture text -->
Drosophila Human<br>gene-level<br>tx-level<br>tx-level stage-wise<br>gene-level<br>tx-level<br>tx-level stage-wise<br>0.0 0.1 0.2 0.3 0.4 0.0 0.1 0.2 0.3 0.4<br>False Discovery Proportion False Discovery Proportion<br>1.0 1.0<br>0.8 0.8<br>0.6 0.6<br>0.4 0.4<br>True Positive Rate True Positive Rate<br>0.2 0.2<br>0.0 0.0<br><!-- End of picture text -->

16 / 17

Van den Berge _et al. Genome Biology_ (2017) 18:151 DOI 10.1186/s13059-017-1277-0


**METHOD**

**Open Access**

stageR: a general stage-wise method for controlling the gene-level false discovery rate in differential expression and differential transcript usage

Koen Van den Berge<sup>1,2</sup> , Charlotte Soneson<sup>3,4</sup> , Mark D. Robinson<sup>3,4</sup> and Lieven Clement<sup>1,2*</sup>

### **Abstract**

RNA sequencing studies with complex designs and transcript-resolution analyses involve multiple hypotheses per gene; however, conventional approaches fail to control the false discovery rate (FDR) at gene level. We propose stageR, a two-stage testing paradigm that leverages the increased power of aggregated gene-level tests and allows post hoc assessment for significant genes. This method provides gene-level FDR control and boosts power for testing interaction effects. In transcript-level analysis, it provides a framework that performs powerful gene-level tests while maintaining biological interpretation at transcript-level resolution. The procedure is applicable whenever individual hypotheses can be aggregated, providing a unified framework for complex high-throughput experiments.

**Keywords:** RNA-sequencing, Stage-wise testing, Differential transcript usage, Differential expression

17 / 17

---

[← Stage-wise testing procedure1](12-stage-wise-testing-procedure1.md) · [Up: contents](index.md)

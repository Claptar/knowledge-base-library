---
title: Single cell transc riptomics
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/stagewiseTesting.pdf
source_file: sources/statomics-sga21/docs/stagewiseTesting.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Single cell transc riptomics

**Source:** [`docs/stagewiseTesting.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/stagewiseTesting.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
Cell  Barcoding & Library Sequence Transcriptome<br>Suspension Construction<br>Collect RT Remove OilPool<br>10x Barcoded Cells Oil<br>Gel Beads Enzyme<br>Single CellGEMs 10x BarcodedcDNA 10x BarcodedcDNA<br>Transcriptome profile for each individual cell<br><!-- End of picture text -->


<!-- Start of picture text -->
Cell 1<br>Gene 1  …  Gene  3 0000<br>Cell 10000<br>Gene 1  …  Gene 30000<br><!-- End of picture text -->

6 / 17


Kang et al. Nat. Biotechnol. 2018 36(1):89-94

peripheral blood mononuclear cells from 8 individuals Stimulated vs control _>_ 29000 cells


<!-- Start of picture text -->
Stimulated Control<br>NK cells NK cells<br>FCGR3A+ Monocytes FCGR3A+ Monocytes<br>CD8 T cells CD8 T cells<br>CD4 T cells CD4 T cells<br>CD14+ Monocytes CD14+ Monocytes<br>B cells B cells<br><!-- End of picture text -->

7 / 17


peripheral blood mononuclear cells from 8 individuals Stimulated vs control _>_ 29000 cells Two channels of 10x genomics chip Two lanes of hiseq run Demultiplexing individuals via SNPs

Kang et al. Nat. Biotechnol. 2018 36(1):89-94

7 / 17


DE stimulated vs control in each cell type (6 tests/gene) Different stimulus effect across cell types (15 tests/gene)


<!-- Start of picture text -->
Kang et al. Nat. Biotechnol. 2018 36(1):89-94<br><!-- End of picture text -->

7 / 17

Many hypotheses per gene/protein in contemporary high throughput studies

Transcript-level analysis, single cell experiments and complex designs result in multiple hypotheses of interest per gene/protein. The conventional strategy

- 1 assess each hypothesis separately

- 2 on FDR level _α_

- 3 provide the biologist with list of top-genes for every contrast

8 / 17

Many hypotheses per gene/protein in contemporary high throughput studies

Transcript-level analysis, single cell experiments and complex designs result in multiple hypotheses of interest per gene/protein. The conventional strategy

- 1 assess each hypothesis separately

- 2 on FDR level _α_

- 3 provide the biologist with list of top-genes for every contrast

- However,


Shortlist of interesting genes when we assess multiple hypotheses per gene/protein? Post-hoc tests for each hypothesis within a gene/protein if omnibus null hypothesis is rejected?


Gene/protein-level FDR control required because downstream analysis and validation is done at the gene/protein-level.

8 / 17

---

[← Single cell transcriptomics](06-single-cell-transcriptomics.md) · [Up: contents](index.md) · [Simulation study conventional analysis in sequencing applications →](08-simulation-study-conventional-analysis-in-sequencing-applica.md)

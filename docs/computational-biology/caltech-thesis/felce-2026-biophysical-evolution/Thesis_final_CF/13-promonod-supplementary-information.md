---
title: PROMONOD SUPPLEMENTARY INFORMATION
source: https://thesis.library.caltech.edu/17880/
source_file: sources/felce-2026-biophysical-evolution/Thesis_final_CF.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROMONOD SUPPLEMENTARY INFORMATION

**Source:** `Thesis_final_CF.pdf` from [felce-2026-biophysical-evolution](https://thesis.library.caltech.edu/17880/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **B.1 Stationary distribution of mRNA and protein via generating function methods**

The generating functions, as defined in Equations 3.3-3.4 evolve as follows:


When _𝑏_ → 0 _, 𝐹_ ( _𝑧𝑢_ ) ≈ 1 + _𝑏𝑧𝑢_ , and this reduces to the constitutive model. For the steady-state solution, we set<sup>_𝜕_</sup> _𝜕𝑡_<sup>_<u>𝜙</u>_= 0 and solve the resulting first order PDE using the</sup> method of characteristics (Courant and Hilbert, 1962). We write all the variables as functions of _𝑠_ , i.e., _𝜙_ ( _𝑢_ ˜ _𝑢_ ( _𝑠_ ) _, 𝑢_ ˜ _𝑠_ ( _𝑠_ ) _, 𝑢_ ˜ _𝑝_ ( _𝑠_ ) _, 𝑡_ ( _𝑠_ )), giving the characteristic ODEs:


and


For the bursty model with geometrically distributed burst sizes, we have _𝑀_ ( _𝑢_ ) = 1− _<u>𝑏𝑢𝑏𝑢</u>_<sup>.We have immediately that</sup>

126


In summary, we need to solve the following:


### **B.2 Solving probability distribution numerically**

We used Runge-Kutta 4 (Runge, 1895) to numerically integrate these equations.

### **B.3 Biological data analysis Data processing**

We obtained our sequencing data from the following human PBMC datasets:

- 10k Human PBMCs Stained with TotalSeq™-B Human TBNK Cocktail, Chromium GEM-X Single Cell 3’ Universal 3’ Gene Expression dataset analyzed using Cell Ranger 8.0.0 (2024, March 13) (Genomics, 2024)

- 10K Human PBMCs, Gene Expression with a Panel of TotalSeq™-B Antibodies, analyzed using Cell Ranger 3.0.0, (2018, November 19) (Genomics, 2018)

The raw RNA-seq fastq files were processed with `kb-python` (Sullivan et al., 2025); we used the `nac` workflow with the appropriate 10x technology string. The call for processing the 2024 dataset is shown as an example here:

```
kbcount\
```

```
--overwrite\
--h5ad\
--workflow=nac\
```

- `-i /home/cfelce/proMonod/data/ref/human/GRCh38.110/index.idx \`

- `-g /home/cfelce/proMonod/data/ref/human/GRCh38.110/t2g.txt \`

- `-x 10xv4 \`

127

- `-o /home/cfelce/proMonod/data/RNA_S2 \`

- `-c1 /home/cfelce/proMonod/data/ref/human/GRCh38.110/cdna.txt \`

- `-c2 /home/cfelce/proMonod/data/ref/human/GRCh38.110/nascent.txt \`

- `-m 16G \`

```
--verbose\
```

```
--filterbustools\
```

```
10k_Human_PBMC_TotalSeqB_3p_gemx_fastqs/gex/
```

```
10k_Human_PBMC_TotalSeqB_3p_gemx_gex1_S2_L001_R1_001.fastq.gz\
```

```
10k_Human_PBMC_TotalSeqB_3p_gemx_fastqs/gex/
```

```
10k_Human_PBMC_TotalSeqB_3p_gemx_gex1_S2_L001_R2_001.fastq.gz\
10k_Human_PBMC_TotalSeqB_3p_gemx_fastqs/gex/
```

```
10k_Human_PBMC_TotalSeqB_3p_gemx_gex1_S2_L002_R1_001.fastq.gz\
10k_Human_PBMC_TotalSeqB_3p_gemx_fastqs/gex/
```

```
10k_Human_PBMC_TotalSeqB_3p_gemx_gex1_S2_L002_R2_001.fastq.gz\
10k_Human_PBMC_TotalSeqB_3p_gemx_fastqs/gex/
```

```
10k_Human_PBMC_TotalSeqB_3p_gemx_gex1_S2_L003_R1_001.fastq.gz
10k_Human_PBMC_TotalSeqB_3p_gemx_fastqs/gex/
```

```
10k_Human_PBMC_TotalSeqB_3p_gemx_gex1_S2_L003_R2_001.fastq.gz
10k_Human_PBMC_TotalSeqB_3p_gemx_fastqs/gex/
```

```
10k_Human_PBMC_TotalSeqB_3p_gemx_gex1_S2_L004_R1_001.fastq.gz
10k_Human_PBMC_TotalSeqB_3p_gemx_fastqs/gex/
```

```
10k_Human_PBMC_TotalSeqB_3p_gemx_gex1_S2_L004_R2_001.fastq.gz
```

Some proteins, or protein complexes, corresponded to multiple RNA transcripts in the data. The identifications in Table B.1 (10x, 2024) and Table B.2 (10x, 2018), were used to map protein counts to RNA counts. The cells were clustered using Leiden clustering (see the scripts at `https://github.com/pachterlab/ FFP_2025` ), and subsetted to monocytes for the 10x, 2024 dataset, and to a group of T-cells for the 10x, 2018 dataset.

### **Fitted parameters**

We fit the bursty transcription with translation model, with Poissonian count sampling, described in the main text, Section 3.3. Note that, since we fit only spliced RNA and protein counts, the technical sampling rate for unspliced counts only affected the method of moments initialization values.

We show the optimal biological parameters for each fit in Table B.3, along with

128

|**Protein**|**Subunits (alternate forms)**|**Ensembls**|
|---|---|---|
|CD3 (complex)|CD3_𝛾_(x1)<br>CD3_𝛿_(x1)<br>CD3_𝜖_(x2)|ENSG00000160654<br>ENSG00000167286<br>**ENSG0000019885**|
|CD4|-|ENSG00000010610|
|CD8|CD8a<br>(CD8b)|ENSG00000153563<br>(ENSG00000172116)|
|CD11C|-|ENSG00000140678|
|CD14|-|ENSG00000170458|
|CD16|CD16a<br>(CD16b)|ENSG00000203747<br>(ENSG00000162747)|
|CD19|-|ENSG00000177455|
|CD56|-|ENSG00000149294|
|CD45|-|ENSG00000081237<br>(ENSG00000262418)|


Table B.1: Proteins (complexes) with their constituent subunits or alternative forms, and the corresponding Ensembl IDs, for the 10x 2024 dataset. Where alternate forms are given in parentheses, the non-parenthesized Ensembl ID was used. Where subchains of a complex are shown, the bolded ensembl was used.

the technical parameters used (capture rates _𝜆𝑢,𝑠,𝑝_ for unspliced, spliced and protein counts respectively), and the initialization method used for fitting.

### **References**

- Courant, Richard and David Hilbert (1962). _Methods of Mathematical Physics, Volume II_ . Wiley-Interscience.

- Genomics, 10x (Nov. 2018). _10k PBMCs from a Healthy Donor - Gene Expression with a Panel of TotalSeq-B Antibodies Universal 3’ Gene Expression_ . 10x Genomics Datasets. Version Cell Ranger v3.0.0. Dataset analyzed using Cell Ranger v3.0.0. url: `https://www.10xgenomics.com/datasets/10- k- pbm-cs-from-a-healthy-donor-gene-expression-and-cell-surfaceprotein-3-standard-3-0-0` .

- (Oct. 2024). _10k Human PBMCs Stained with TotalSeq-B Human TBNK Cocktail, Chromium GEM-X Single Cell 3’ Gene Expression_ . 10x Genomics Datasets. Version Cell Ranger v8.0.0. Dataset analyzed using Cell Ranger v8.0.0. url: `https://www.10xgenomics.com/datasets/10k-human-pbmcs-stainedwith-totalseq-B-human-TBNK-cocktail-GEM-X` .

129

|**Gene Symbol**|**Ensembl ID**|
|---|---|
|PTPRC|ENSG00000081237|
|FCGR3A|ENSG00000203747|
|CD247|ENSG00000198821|
|CD3E|ENSG00000198851|
|CD3D|ENSG00000167286|
|CD3G|ENSG00000160654|
|FUT4|ENSG00000196371|
|NCAM1|ENSG00000149294|
|CD4|ENSG00000010610|
|IGHG1|ENSG00000211896|
|IGHG2|ENSG00000211893|
|ISG20|ENSG00000172183|
|CD19|ENSG00000177455|
|PDCD1|ENSG00000188389|
|CD8A|ENSG00000153563|
|TIGIT|ENSG00000181847|
|IL7R|ENSG00000168685|
|CD14|ENSG00000170458|


Table B.2: Final one-to-one mapping, used for the 10x 2018 dataset, between protein (gene) symbols and Ensembl IDs.

- Runge, C. (June 1895). “Ueber Die Numerische Auflösung von Differentialgleichungen”. In: _Mathematische Annalen_ 46.2, pp. 167–178. issn: 1432-1807. doi: `10.1007/BF01446807` .

- Sullivan, Delaney K. et al. (2025). “kallisto, bustools and kb-python for quantifying bulk, single-cell and single-nucleus RNA-seq”. In: _Nature Protocols_ 20.3, pp. 587–607. doi: `10.1038/s41596-024-01057-0` .

130

||**2024, CD14**|**2024, CD45**|**2018, IL7R**|
|---|---|---|---|
|**Cell Type**|Monocytes|Monocytes|T-cell cluster|
|**log10****_b_**|3.04|1.96|4.2|
|**log10****_β_**|-0.403|-0.993|-0.665|
|**log10****_γ_**|1.77|-0.406|1.31|
|**log10****_kp_**|3.5|-1.14|1.24|
|**log10****_γp_**|-0.634|-0.862|-0.764|
|**log10****_λu_**|0.0|-|0.0|
|**log10****_λs_**|0.0|-1|-2.0|
|**log10****_λp_**|-2.5|0|-2.5|
|**Initialization**|Moments estimate|10 random restarts|Moments estimate|


Table B.3: Optimal biophysical parameters for each of the fits shown in the main text, and the corresponding technical capture rates. The cell type and initialization method for the fit are also given.

131

_A p p e n d i x C_

---

[← ATAC SUPPLEMENTARY INFORMATION](12-atac-supplementary-information.md) · [Up: contents](index.md) · [MECHANISMS OF GENE EXPRESSION EVOLUTION: SUPPLEMENTARY INFORMATION →](14-mechanisms-of-gene-expression-evolution-supplementary-inform.md)

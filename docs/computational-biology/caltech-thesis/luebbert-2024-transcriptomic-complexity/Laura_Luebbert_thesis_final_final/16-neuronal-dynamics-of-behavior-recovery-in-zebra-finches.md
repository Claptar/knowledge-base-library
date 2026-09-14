---
title: Neuronal Dynamics of Behavior Recovery in Zebra Finches
source: https://thesis.library.caltech.edu/16368/
source_file: sources/luebbert-2024-transcriptomic-complexity/Laura_Luebbert_thesis_final_final.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Neuronal Dynamics of Behavior Recovery in Zebra Finches

**Source:** `Laura_Luebbert_thesis_final_final.pdf` from [luebbert-2024-transcriptomic-complexity](https://thesis.library.caltech.edu/16368/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

#### **Preamble**

Here, single-cell RNA sequencing is used to investigate the neuronal dynamics underlying the recovery of a learned behavior after chronically silencing inhibitory neurons in zebra finches. Beyond the challenges of studying a non-model organism described in the previous subchapter, this analysis was further complicated by the experimental design comparing two conditions. Here, I am only including the relevant single-cell RNA sequencing results and methods from the published paper.

Zsofia Torok, **Laura Luebbert** , Jordan Feldman, Alison Duffy, Alexander A. Nevue, Shelyn Wongso, Claudio V. Mello, Adrienne Fairhall, Lior Pachter, Walter G. Gonzalez, Carlos Lois (2023). Recovery of a learned behavior despite partial restoration of neuronal dynamics after chronic inactivation of inhibitory neurons. _bioRxiv_ . <u>https://doi.org/10.1101/2023.05.17.541057</u>

#### **Summary**

Maintaining motor skills is crucial for an animal’s survival, enabling it to endure diverse perturbations throughout its lifespan, such as trauma, disease, and aging. What mechanisms orchestrate brain circuit reorganization and recovery to preserve the stability of behavior despite the continued presence of a disturbance? To investigate this question, we chronically silenced inhibitory neurons, which altered brain activity and severely perturbed a complex learned behavior for around two months, after which it was precisely restored. Electrophysiology recordings revealed abnormal offline dynamics resulting from chronic inhibition loss, while subsequent recovery of the behavior occurred despite partial normalization of brain activity. Single-cell RNA sequencing revealed that chronic silencing of interneurons leads to elevated levels of microglia and MHC I. These experiments demonstrate that the adult brain can overcome extended periods of drastic abnormal activity. The reactivation of mechanisms employed during learning, including offline neuronal dynamics and upregulation of MHC I and microglia, could facilitate the recovery process following perturbation of the adult brain. These findings indicate that some forms of brain plasticity may persist in a dormant state in the adult brain until they are recruited for circuit restoration.

#### **Introduction**

Maintaining the ability to precisely execute motor behavior throughout life, despite perturbations due to trauma, disease, or aging, is crucial for reproduction and survival. To reliably execute behaviors, brain circuits require a balance of excitation and inhibition (E/I balance) to maintain physiological activity patterns. Loss of E/I balance causes abnormal patterns of neuronal activity, which can result in diseases such as epilepsy<sup>1,2</sup> . Given its importance, brain circuits strive to restore E/I balance once disturbed<sup>3</sup> . However, the


<!-- Start of picture text -->
83<br><!-- End of picture text -->


**Graphical Abstract** Schematic overview of the experiments performed in this study. To investigate how a complex motor behavior recovers after chronic loss of inhibitory tone, we blocked the function of zebra finch HVC inhibitory neurons by bilateral stereotaxic injection of an AAV viral vector into HVC. Throughout various timepoints in this perturbation paradigm, we recorded song behavioral data, electrophysiological measurements (chronic and acute within HVC), and measured changes in gene expression at single-cell resolution.

mechanisms orchestrating circuit reorganization and recovery of E/I balance during the continued presence of a perturbation remain poorly understood.

Zebra finches produce a highly stereotyped song with minimal variability over extended periods of time<sup>4</sup> , underpinned by temporally precise neural activity<sup>5</sup> . This species thus provides an optimal model to simultaneously track abnormal brain activity, its effect on behavior, and changes to both over time. It serves as an excellent model for studying chronic E/I imbalance and accompanying changes over time at the behavioral, neuronal, and transcriptomic levels.

84

Here, we genetically block inhibitory neurons in HVC (proper name), a premotor brain nucleus of the male zebra finch involved in song production, to chronically perturb the E/I balance. HVC contains two main types of excitatory neurons that project to two main downstream targets: nucleus X (proper name) and nucleus RA (robust nucleus of the arcopallium). In addition, HVC includes several types of inhibitory neurons whose axons do not leave HVC; thus, they act locally within HVC<sup>5</sup> . Juvenile male zebra finches learn their song from their fathers during the “critical period” and once learned, produce a highly stereotypical song for the rest of their lives<sup>6</sup> . Previous work has shown that inhibition plays a role during development to close the critical period and protect learned components of the song in juvenile animals<sup>7</sup> . Acutely blocking interneuron signaling in adult animals by chemicals leads to abnormal behaviors that quickly return to normal once the chemical is washed out<sup>8</sup> . However, it is not known how long-term disruption of inhibitory neurons affects neuronal dynamics, and whether behaviors can recover after such drastic perturbation.

#### **Results**

To investigate how a complex motor behavior recovers after chronic loss of inhibitory tone, we blocked the function of HVC inhibitory neurons in adult male zebra finches by bilateral stereotaxic injection of an AAV viral vector into HVC. The AAV viral vector carried the light chain of tetanus toxin (TeNT), driven by the human dlx5 promoter, which is selectively active in inhibitory neurons<sup>9</sup> . TeNT blocks the release of neurotransmitters from presynaptic terminals, thereby preventing neurons from communicating with their postsynaptic partners<sup>10</sup> . Thus, expression of TeNT does not directly alter the ability of neurons to fire action potentials, but effectively mutes them. As a control, a second group of animals was injected with an AAV carrying the green fluorescent protein NeonGreen driven by the ubiquitous promoter CAG. Throughout various time points in this perturbation paradigm, we recorded song behavioral data, obtained electrophysiological measurements (chronic and acute within HVC), and measured changes in gene expression at single-cell resolution (Graphical Abstract).

#### **Single-cell RNA sequencing suggests mechanisms of neuronal plasticity driven by microglia and MHC class I genes during song perturbation**

To investigate cellular mechanisms that might underlie the observed changes in neuronal activity and behavior at the transcriptomic level, we performed single-cell RNA sequencing (scRNAseq) of HVC from control (n=2) and TeNT-treated (n=2) adult male zebra finches at 25 dpi, around the time of peak song distortion. HVC from both hemispheres of all four birds were dissected based on retrograde tracer fluorescence and dissociated to prepare single-cell suspensions, which were indexed and pooled. This allowed the construction of a combined dataset, containing results from all organisms and conditions, without the need for batch correction (Supplementary Figure 4.1, Supplementary Table 4.1). Following quality control, we retained a total of 35,804 singlecell profiles spanning four individuals, consisting of two control and two TeNT-treated animals.

85


Figure legend on next page.

86

**Figure 4.3** Transcriptomic changes at single-cell resolution in HVC at 25 days after chronic loss of inhibitory neurons through viral expression of tetanus toxin (TeNT). Single-cell RNA sequencing of the HVCs of control (n=2) and TeNT-treated (n=2) animals was performed at 25 days post-injection (dpi). **A** Heatmap showing min-max scaled expression of cell type marker genes for each cell type (data from both control and TeNT-treated animals). **B** Log-fold change in total number of cells per cell type between TeNTtreated and control animals. **C** Volcano plot showing statistical significance over magnitude of change of differentially expressed genes between TeNT-treated and control animals across all cell types. Dotted lines indicate fold change = 1.5 and p value = Bonferroni corrected alpha of 0.05. A list of all differentially expressed genes can be found here: https://github.com/lauraluebbert/TL_2023. **D** Violin plots of normalized counts of major histocompatibility complex 1 α chain-like (MHC1) (ENSTGUG00000017273.2) and beta 2 microglobulin-like (B2M) (ENSTGUG00000004607.2) genes in control (n=2, blue) and TeNT-treated (n=2, red) animals per cell cluster. A star indicates a significant increase in gene expression in TeNT-treated animals compared to control (p < 0.05 and fold change > 1.5).

While cell type abundance was highly concordant between replicates of the same condition (Supplementary Figure 4.1, Figure 4.3 A), we found that animals treated with TeNT we found that animals treated with TeNT displayed a three-fold increase in the number of microglia (Figure 4.3 B). This increase in microglia was likely not due to an inflammatory reaction caused by the surgical procedure or the AAV injection because control animals also received a viral injection with a highly similar construct. Thus, we hypothesize that the increase in microglia in TeNT-treated animals is a consequence of the chronic muting of inhibitory neurons.

Several studies have shown that microglia play a role in synaptic plasticity during early brain development and learning in mammals<sup>32–35</sup> . These prior observations in combination with our findings suggest that microglia might participate in the synaptic reorganization triggered by circuit perturbation. We performed in situ hybridization (ISH) using a probe against RGS10, a gene expressed in microglia, during song degradation at 25 dpi and after recovery at 90 dpi. At 25 dpi, the number of microglia increased in TeNT-treated animals compared to control (Figure 4.4 A, Supplementary Figure 4.2 A and B), and returned to control levels by 90 dpi, when the song had recovered.

To further investigate the hypothesis that microglia are associated with circuit reorganization involved in neuronal plasticity, we counted the number of microglial cells in HVC at different times during song learning in naive (untreated), juvenile birds using ISH. The number of microglia in the HVC of juveniles was higher during the early stages of the song learning period (30-50 days post-hatching (dph)), compared to 70 dph, after the song became more stereotypic (Figure 4.4 B, Supplementary Figure 4.2 C and D).

Furthermore, scRNAseq analysis revealed a significant increase in the expression of the α chain of major histocompatibility complex class I (MHC I) and β2-microglobulin (B2M) across several neuronal cell types in TeNT-treated animals (Figure 4.3 C and D) and confirmed the increases in MHC I by ISH (Figure 4.4 C, Supplementary Figure 4.2 E and F). MHC class I molecules are heterodimers that consist of two polypeptide chains, α and

87


**Figure 4.4** _In situ_ hybridization of microglia marker gene RGS10 in adult male control, TeNT-treated and juvenile male HVC & MHC1 gene in adult male control and TeNT-treated HVC. **A** Histological sections of HVC (in control and TeNT-treated animals at 25 and 90 dpi) after _in situ_ hybridization of RNA probes for RGS10 (a gene marker for microglia). **B** Histological sections of HVC in naive juvenile males (at 20, 50, and 75 days post-hatching (dph)) after _in situ_ hybridization of RNA probes for RGS10. **C** Histological sections of HVC (from control and TeNT-treated animals at 25 and 90 dpi) after _in situ_ hybridization of RNA probes for MHC1. Black/darker dots indicate enzyme reactions resulting in successful probe localization and suggest target gene expression.

B2M, and are involved in antigen presentation for T cells<sup>36</sup> . This increase in MHC I and B2M is likely triggered by the genetic silencing of inhibitory neurons, and not due to an inflammatory response because it was not observed in control animals injected with a control virus. MHC I and B2M have been observed in previous studies to be highly

88

expressed in neurons during brain development<sup>37,38</sup> , consistent with a hypothetical role in synaptic plasticity<sup>39,40</sup> . Here we observe that MHC I and B2M are upregulated in response to perturbation of neuronal activity in a fully formed circuit, indicating their possible role in the restoration of brain function.

#### **Discussion**

The brain requires a balance between excitation and inhibition to maintain physiological activity patterns and enable reliable behaviors. We found that chronic muting of inhibitory neurons in a pre-motor circuit severely disrupts a learned motor behavior for an extended period of time (30-90 days). Even after several weeks of perturbed brain activity, the brain circuit is able to regain function and recover the behavior, despite failing to restore some aspects of its neuronal dynamics. We propose that the return to control-like offline voltage deflections and the precision of local neuronal activity during alpha oscillations during these deflections are key components that accompany the behavioral recovery. Our observations indicate a putative relationship between activity dynamics offline and the restoration of circuit function. Furthermore, our data suggest that microglia and MHC I may be involved in changes caused by chronic perturbation of neuronal activity. These experiments reveal that the adult brain can overcome extended periods of E/I imbalance, potentially by processes that occur offline. The reactivation of mechanisms typically employed during juvenile learning, including night replay and activation of MHC I and microglia, could facilitate the recovery process following perturbation in the adult brain. This indicates that some forms of circuit plasticity may persist throughout adulthood, entering a dormant state until their activation is required for circuit restoration.

#### **Methods**

#### _Animals_

All procedures involving zebra finches were approved by the Institutional Animal Care and Use Committee of the California Institute of Technology. All birds used in the current study were bred in our own colony and housed with multiple conspecific cage mates of mixed genders and ages until used for experiments. Before any experiments, adult male birds (>120 days post-hatching (dph)) were singly housed in sound isolation cages with a 14/10 hr light/dark cycle for >5 days until they habituated to the new environment and started singing. Thereafter, birds were kept in isolation until the end of the experiment.

#### _Behavioral recordings_

Adult male zebra finches’ (n=30, 130-890 dph) undirected songs were recorded 24/7 in sound-isolated chambers for 10-14 days before any manipulation to get a baseline of their song. Recordings were done with microphones (Audio-technica, AT831b) that are connected to an amplifier M-TRACK 8 and recording software Sound Analysis Pro 2011 at 44100 Hz. Animals were housed in these chambers and continuously recorded for the duration of the experiments.

#### _Viral vectors_

AAV-TeNT contained the promoter from the human dlx5 gene driving expression of the light chain of tetanus toxin fused to EGFP with a PEST domain. AAV9-dlx-TeNT was

89

obtained from the Duke viral core facility. The control virus used was AAV9-CAGNeonGreen, where CAG drives the expression of NeonGreen which is a GFP variant.

#### _Stereotaxic injection_

Birds were anesthetized with isoflurane (0.5% for initial induction, 0.2% for maintenance) and head-fixed on a stereotaxic apparatus. First, to inject a retrograde tracer in area X, craniotomies were made bilaterally and fluorescent tracers (fluoro-ruby 10%, 100-300 nL) were injected through a glass capillary (tip size ~25 μm) into the corresponding nuclei (coordinates from dorsal sinus in mm - area X: Anteroposterior (AP) 3.3-4.2, Mediolateral (ML) 1.5-1.6, Deep (D): 3.5-3.8). To deliver the virus (AAV) into HVC, a second surgery was performed 7-10 days after retrograde tracer injection. By then, HVC was strongly labeled by fluorescence and visible through a fluorescent stereoscope. AAVs diffuse extensively (~500 µm), and a single injection (~100 nL) in the center of HVC was sufficient to label enough cells. All injections in HVC were performed at ~20 nL/min to minimize physical damage. At the end of every surgery, craniotomies were covered with Kwik-Sil, and the skin incision was closed with Gluture.

#### _Chronic electrophysiology recordings_

Animals (n=4, 300-700 dph) were implanted in the right hemisphere HVC with 4 by 4 electrode arrays (Neuronexus A4x4-3mm-50/100-125-703-CM16LP) based on retrograde fluorescent labeling of HVC (just as for viral injections). Post-perfusion histology images were obtained to locate the electrode array within HVC for each animal (Supplementary Figure 4.3). Electrode implantation occurred within the same surgery as the viral injection.

This procedure follows the same surgical steps as the viral delivery protocol, until the point of electrode implantation. A small opening was cut on the dura (just big enough to fit the electrode array) to lower the electrodes manually. The reference and ground were a gold screw pin placed into the cerebellum. The skin was removed from the surface of the skull for the majority of the surface, in order to secure the implant. Before implantation, the skull and the craniotomies were cleaned with saline and dried and the skull was prepared according to the protocol of the C&B Metabond cement system. Post implantation we covered the craniotomies with kwik-sil. Once hardened, we covered the whole skull, and the part of the electrode still exposed, with metabond. The head stage (Intan RHD Part # C3335) was connected to the probe before implantation and securely metabonded to the connection between the probe and head stage in order to prevent detachment when the bird is moving. SPI interface cables (Intan Part #C3203, #C3213) were connected to the acquisition board (Open Ephys). Data was recorded at 30,000 Hz with the Open Ephys software system. Animals were freely moving with a passive counterweight-based commutator system.

#### _Acute electrophysical recordings_

Animals (n=10, 140-250 dph) went through the same surgical procedure as described for a stereotaxic viral injection. However, at the end of the surgery the skin was removed from the skull, and the whole skull was pre-treated and covered in metabond except for the craniotomies over HVC that were covered with kwik-cast until the day of the acute

90

recording session. Shortly before the recording session, a head-bar was glued on top of the frontal surface of the metabonded skull to allow the head-fixation of the bird for the recording session. Then, the kwik-cast was removed from the craniotomy over HVC (left or right hemisphere or both depending on the animal) and a small incision was made in the dure over HVC, which was identified by the retrograde tracer previously injected. The ground was placed into the cerebellum. Then the high-density silicone probe (Neuropixel) was lowered with a motorized arm over hours for 2.6-3 mm deep into the brain. The head stage and acquisition board was connected to the computer and data was recorded with the Open Ephys software. Once the probe settled in the brain, we had 4 distinct recording sessions. Post-perfusion histology images were obtained to locate electrode array within HVC for each animal (Supplementary Figure 4.4). Recording sessions: lights on silence (10 min), followed by playback of the bird’s own song (3-10 min); lights-off silence (10 min), followed by playback of the bird’s own song (3-10 min); microinjection of 100 nL 250 µM Gabazine (Hellobio, HB0901), followed by the same protocol of lights-off and on without Gabazine.

#### _Single-cell RNA sequencing Animals_

All of the work described in this study was approved by California Institute of Technology and Oregon Health & Science University’s Institutional Animal Care and Use Committee and is in accordance with NIH guidelines. Zebra finches ( _Taeniopygia guttata_ ) were obtained from our own breeding colony or purchased from local breeders.

#### _Dissociation and cDNA generation_

Animals were anesthetized with a mix of ketamine-xylazine (0.02 mL / 1 gram) and quickly decapitated, then the brain was placed into a carbogenated (95% O2, 5% CO2) NMDGACSF petri dish on ice. The brains were dissected on a petri dish with NMDG-ACSF surrounded by ice under an epifluorescent microscope guided by the fluoro-ruby retrograde tracing from Area X to HVC.

We used the commercially available Worthington Papain Dissociation system with some minor changes and add-on steps. We followed all the steps included in the Worthington protocol with a final concentration of 50 U/mL of papain. To match the intrinsic osmolarity of neurons in zebra finches we used NMDG-ACSF (~310 mOsm) instead of the EBSS for post-dissection and STOP solution. Another modification was to add 20 µL of 1 mg/mL Actinomycin D (personal communication from Allan-Hermann Pool; 47) into 1 mL of the post-dissection medium and the STOP solution in which trituration occurred. Papain digestion occurred for an hour on a rocking surface with constant carbogenation in a secondary container above the sample vial at RT. We performed trituration with increasingly smaller diameter glass pasteur pipettes. Trituation was performed inside the papain solution. Then, once the tissue was fully dissociated, we centrifuged the samples at 300 g RT for 5 minutes and resuspended them in STOP solution. Next, we used a 40 µm Falcon cell strainer pre-wet with the STOP solution and centrifuged again at 300 g RT for 5 min. Finally, we resuspended the cell pellet in 60µl of STOP solution and proceeded to barcoding and cDNA synthesis. The cell barcoding, cDNA synthesis, and library

91

generation protocol were performed according to the Chromium v3.1 next GEM single cell 3’ reagent kits by Jeff Park in the Caltech sequencing facility. Sequencing was performed on an Illumina Novaseq S4 sequencer with 2x150 bp reads.

#### _Generation of count matrices_

The reference genome GCA_003957565.2 (Black17, no W) was retrieved from Ensembl on March 20, 2021 (http://ftp.ensembl.org/pub/release-104/gtf/taeniopygia_guttata/). We quantified the gene expression in each of the four datasets using the kallisto-bustools workflow<sup>48</sup> . The reference index was built using the kb-python (v0.26.3) ref command and the above-mentioned reference genome. Subsequently, the WRE sequence was manually added to the cdna and t2g files generated by kallisto-bustools to allow the identification of transgenic cells. The count matrix was generated for each dataset using the kallisto-bustools count function. The resulting count matrices were compared to those generated by the 10X Cell Ranger pipeline (v6.0.1) and kallisto-bustools count with multimapping function. For all four datasets, kallisto-bustools mapped approximately 10% more reads than Cell Ranger (Supplementary Figure 4.5). No increase in confidently mapped reads was observed when using the multimapping function, indicating that reads align confidently to one gene in the reference genome (Supplementary Figure 4.5).

#### _Quality control and filtering_

The datasets were filtered separately based on the expected number of cells and their corresponding minimum number of UMI counts (Supplementary Figure 4.6). Following quality control based on apoptosis markers and library saturation plots (Supplementary Figure 4.6), the count matrices were concatenated and normalized using log(CP10k + 1) for downstream dimensionality reduction and visualization using Scanpy’s (v1.9.1)<sup>49</sup> normalize_total with target sum 10,000 and log1p. Gene names and descriptions for Ensembl IDs without annotations were obtained using gget (v0.27.3)<sup>50</sup> .

#### _Dimensionality reduction and normalization_

The concatenated data was mapped to a lower dimensional space by PCA applied to the log-normalized counts filtered for highly variable genes using Scanpy’s highly_variable_genes. Next, we computed nearest neighbors and conducted Leiden clustering<sup>51</sup> using Scanpy.

Initially, this approach was performed on the control and TeNT datasets separately. This resulted in the identification of 19 clusters in the control data and 22 clusters in the TeNT data (Supplementary Figure 4.6). For both conditions, equal contribution from both datasets indicated that there was minimal batch effect, as expected since the data was sequenced in a pooled sequencing run. We also performed batch correction using scVI<sup>52</sup> which did not change the contribution of each dataset per cluster. As a result, we continued the analysis using the data that was not batch-corrected with scVI.

Next, we concatenated all four datasets and followed the approach described above. This resulted in the identification of 21 Leiden clusters, which we also refer to as cell types (Figure 4.3 A). Each cluster was manually annotated with a cell type based on the

92

expression of previously established marker genes<sup>53</sup> . The cell type annotation was validated by the top 20 differentially expressed genes extracted from each cluster using Scanpy’s rank_genes_groups (P values were computed using a t-test and adjusted with the Bonferroni method for multiple testing) (Supplementary Figure 4.1). Clusters identified as glutamatergic neurons were further broken down into HVC-X- and HVC-RA-projecting glutamatergic neurons using previously established marker genes (data not shown; also see <u>https://github.com/lauraluebbert/TL_2023). We found that reclustering all cells labeled as</u> glutamatergic neurons using the Leiden algorithm did not yield different results and we therefore continued with the initial clusters (data not shown). All results discussed in this paper were confirmed by both jointly and separately clustering the experimental conditions.

#### _Comparative analysis of clusters and conditions_

Differentially expressed genes between clusters were identified using Scanpy’s rank_genes_groups (p values were computed using a t-test and adjusted with the Bonferroni method for multiple testing, and confirmed by comparison to P values generated with Wilcoxon test with Bonferroni correction).

In the violin plots, unless otherwise indicated, a star indicates a p value < 0.05 and a fold change > 1.5 difference in mean gene expression between the indicated conditions (p value computed with scipy.stats’ (v1.7.0) ttest_ind and adjusted with the Bonferroni method for multiple testing).

#### _In situ hybridization Animals_

All of the work described in this study was approved by the California Institute of Technology and Oregon Health & Science University’s Institutional Animal Care and Use Committee and is in accordance with NIH guidelines. Zebra finches ( _Taeniopygia guttata_ ) were obtained from our own breeding colony or purchased from local breeders. Developmental gene expression in HVC in the 20-, 50-, and 75-days post-hatch (dph) male and female zebra finches was assessed as previously described<sup>54</sup> . The sex of birds was determined by plumage and gonadal inspection. Birds were sacrificed by decapitation, bisected in the sagittal plane and flash-frozen in Tissue-Tek OCT (Sakura-Finetek), and frozen in a dry ice/isopropyl alcohol slurry. Brains of TeNT-manipulated finches were coronally blocked anterior to the tectum and flash frozen in Tissue-Tek (Sakura). All brains were sectioned at 10 µm on a cryostat and mounted onto charged slides (Superfrost Plus, Fisher).

#### _In situ hybridization_

_In situ_ hybridization was performed as previously described<sup>55,56</sup> . Briefly, DIG-labeled riboprobes were synthesized from cDNA clones for RGS10 (CK312091) and LOC100231469 (class I histocompatibility antigen, F10 alpha chain; DV951963). Slides containing the core of HVC were hybridized overnight at 65°C. Following high stringency washes, sections were blocked for 30 min and then incubated in an alkaline phosphatase conjugated anti-DIG antibody (1:600, Roche). Slides were then washed and developed

93

overnight in BCIP/NBT chromogen (Perkin Elmer). To minimize experimental confounds between animals, sections for each gene were fixed together in 3% paraformaldehyde, hybridized with the same batch of probe, and incubated in chromogen for the same duration.

Sections were imaged under consistent conditions on a Nikon E600 microscope with a Lumina HR camera and imported into ImageJ for analysis. We quantified the expression level of the gene as measured by optical density and the number of cells expressing the gene per unit area, as previously described 54. Optical density was measured by taking the average pixel intensity of a 300x300 pixel square placed over the center of HVC. This value was normalized to the average background level of the tissue. To quantify the number of labeled cells, we established a threshold of expression that was 2.5x the background level. Binary filters (Close-, Open) were applied and the number of particles in the same 300x300 pixel square was quantified.

#### _Histology_

After cardiac perfusion with room temperature 3.2% PFA in 1xPBS we let the brains fix for 2-4 hours at room temperature. After each hemisphere of the brain was sectioned sagittally with a vibratome at 70-100 µm thickness. The brain slices containing HVC were collected and incubated at 4 C overnight with the primary rabbit anti-GFP (AB3080P, EMD Milipore) (blocked in 10% donkey serum in 0.2% Triton 1xPBS). On the second day, the brains were washed in 0.05% Triton 1xPBS and incubated for 2 hours in the dark at room temperature in the secondary goat anti-rabbit 488 (ab150077). Next, the brain slices were washed and mounted in Fluoromount (Sigma). Confocal images were taken with the LSM800.

#### _Data and Code Availability_

Data generated in this study have been deposited in Caltech DATA and can be found at the following DOIs: <u>https://doi.org/10.22002/ednra-nn006</u> and <u>https://doi.org/10.22002/3ta8v-gj982. Please do not hesitate to contact the authors for data</u> or code requests. The code used for the analysis of the single-cell RNA sequencing data can be found here: <u>https://github.com/lauraluebbert/TL_2023. The code used for the</u> analysis of the chronic electrophysiology data can be found here: <u>https://github.com/jordan-feldman/Torok2023-ephys.</u>

94


**Supplementary Figure 4.1** Heatmap of top 5 differentially expressed genes per annotated cell type/cluster obtained by single-cell RNA sequencing of HVC from control and TeNT-treated birds at 25 dpi. Differentially expressed genes between clusters were identified using Scanpy’s rank_genes_groups (p values were computed using a t-test and were adjusted with the Bonferroni method for multiple testing. They were then confirmed by comparison to p values generated with the nonparametric Wilcoxon test with Bonferroni correction). The heatmap depicts the min-max scaled expression for each gene.

95


**Supplementary Figure 4.2** Quantification of the _in situ_ hybridization against microglia marker gene RGS10 in adult male control, TeNT-treated and juvenile male HVC; and MHC1 in adult male control, TeNT-treated animals. **A-B** Quantification of the _in situ_ hybridization for RGS10 between control (n=4 animals) and TeNTtreated animals at 25 dpi (n=4) and 90 dpi (n=4). **C-D** Quantification of the _in situ_ hybridization for RGS10 between juvenile males at 20, 50, and 70 days post-hatching (dph) (n=4). **E-F** Quantification of the _in situ_ hybridization for MHC1 between control (n=4) and TeNT-treated animals at 25 (n=4) and 90 dpi (n=4). Error bars represent standard deviation.

96


**Supplementary Figure 4.3** Histology of electrode array location in HVC in the chronically implanted animals. The white dotted line outlines HVC. Some sections display missing tissue due to the removal of the electrodes after perfusion of the animals. The stronger cyan signal indicates glial scar formation around the electrode array, which provides an approximation of the location of the electrodes.

97


**Supplementary Figure 4.4** Histology to confirm the high-density silicone electrode location in the acute head-fixed animal recordings. The red trace represents the electrode location. The green trace represents the second electrode location in animals that were recorded twice, 40 days apart. The white labels represent the animal IDs. “LH” and “RH” stands for left and right hemisphere, respectively.

98


**Supplementary Figure 4.5** Comparison of different pre-processing methods for the HVC single-cell RNA sequencing datasets. **A** Number of cells retained after quality control for each dataset and alignment method. **B** Mean UMI counts per cell for each dataset and pre-processing method. **C** Percentage of reads confidently mapped to transcriptome for each pre-processing method.

99

Figure legend on next page.

100

**Supplementary Figure 4.6** Quality control of the single-cell RNA sequencing HVC datasets from control and TeTN-treated animals at 25 days post-injection (dpi). **A** “Knee plots” showing the set of barcodes (top row) and number of genes detected (bottom row) over UMI counts. The dashed lines depict the quality filtering cutoff. **B-C** Barplot depicting the fraction of cells from each replicate per cluster for control (B) and TeNT (C), normalized (by dividing) to the total number of cells in each replicate. Control and TeNT datasets were clustered separately using the Leiden algorithm. The equal distribution of replicates across the clusters suggests that technical effects do not dominate the clusters. Thus, we did not perform batch correction. The numbers on top of the bars indicate the total number of cells in each cluster. **D** Barplot depicting the fraction of cells from each dataset in the cell type clusters obtained after jointly clustering the control and TeNT datasets. The numbers on top of the bars indicate the total number of cells in each cluster.


**Supplementary Table 4.1** Overview of single-cell RNA sequencing datasets.

101

#### **References**

1. Dehghani, N., Peyrache, A., Telenczuk, B., Le Van Quyen, M., Halgren, E., Cash, S.S., Hatsopoulos, N.G., and Destexhe, A. (2016). Dynamic Balance of Excitation and Inhibition in Human and Monkey Neocortex. _Sci. Rep._ 6, 23176.

2. Fritschy, J.-M. (2008). Epilepsy, E/I balance and GABA(A) receptor plasticity. Front. Mol. Neurosci. 1, 5.

3. Cossart, R., Bernard, C., and Ben-Ari, Y. (2005). Multiple facets of GABAergic neurons and synapses: multiple fates of GABA signalling in epilepsies. _Trends Neurosci._ 28, 108–115.

4. Nottebohm, F., Stokes, T.M., and Leonard, C.M. (1976). Central control of song in the canary, Serinus canarius. _J. Comp. Neurol._ 165, 457–486.

5. Kozhevnikov, A.A., and Fee, M.S. (2007). Singing-related activity of identified HVC neurons in the zebra finch. _J. Neurophysiol._ 97, 4271–4283.

6. Brainard, M.S., and Doupe, A.J. (2002). What songbirds teach us about learning. _Nature_ 417, 351–358.

7. Vallentin, D., Kosche, G., Lipkind, D., and Long, M.A. (2016). Neural circuits. Inhibition protects acquired song segments during vocal learning in zebra finches. _Science_ 351, 267–271.

8. Kosche, G., Vallentin, D., and Long, M.A. (2015). Interplay of inhibition and excitation shapes a premotor neural sequence. _J. Neurosci._ 35, 1217–1227.

9. Dimidschstein, J., Chen, Q., Tremblay, R., Rogers, S.L., Saldi, G.-A., Guo, L., Xu, Q., Liu, R., Lu, C., Chu, J., et al. (2016). A viral strategy for targeting and manipulating interneurons across vertebrate species. _Nat. Neurosci._ 19, 1743–1749.

10. Link, E., Edelmann, L., Chou, J.H., Binz, T., Yamasaki, S., Eisel, U., Baumert, M., Südhof, T.C., Niemann, H., and Jahn, R. (1992). Tetanus toxin action: inhibition of neurotransmitter release linked to synaptobrevin proteolysis. _Biochem. Biophys. Res. Commun._ 189, 1017–1023.

11. Vu, E.T., Mazurek, M.E., and Kuo, Y.C. (1994). Identification of a forebrain motor programming network for the learned song of zebra finches. _J. Neurosci._ 14, 6924– 6934.

12. Yu, A.C., and Margoliash, D. (1996). Temporal hierarchical control of singing in birds. _Science_ 273, 1871–1875.

13. Glaze, C.M., and Troyer, T.W. (2006). Temporal structure in zebra finch song: implications for motor coding. _J. Neurosci._ 26, 991–1005.

14. Brainard, M.S., and Doupe, A.J. (2000). Interruption of a basal ganglia–forebrain circuit prevents plasticity of learned vocalizations. _Nature_ 404, 762–766.

15. Olveczky, B.P., Andalman, A.S., and Fee, M.S. (2005). Vocal experimentation in the juvenile songbird requires a basal ganglia circuit. _PLoS Biol._ 3, e153.

16. Kao, M.H., Doupe, A.J., and Brainard, M.S. (2005). Contributions of an avian basal ganglia–forebrain circuit to real-time modulation of song. _Nature_ 433, 638–643.

17. Markowitz, J.E., Liberti, W.A., 3rd, Guitchounts, G., Velho, T., Lois, C., and Gardner, T.J. (2015). Mesoscopic patterns of neural activity support songbird cortical sequences. _PLoS Biol._ 13, e1002158.

   - 102

18. Brown, D.E., 2nd, Chavez, J.I., Nguyen, D.H., Kadwory, A., Voytek, B., Arneodo, E.M., Gentner, T.Q., and Gilja, V. (2021). Local field potentials in a pre-motor region predict learned vocal sequences. _PLoS Comput. Biol._ 17, e1008100.

19. Crandall, S.R., Adam, M., Kinnischtzke, A.K., and Nick, T.A. (2007). HVC neural sleep activity increases with development and parallels nightly changes in song behavior. _J. Neurophysiol._ 98, 232–240.

20. Dave, A.S., and Margoliash, D. (2000). Song replay during sleep and computational rules for sensorimotor vocal learning. _Science_ 290, 812–816.

21. Elmaleh, M., Kranz, D., Asensio, A.C., Moll, F.W., and Long, M.A. (2021). Sleep replay reveals premotor circuit structure for a skilled behavior. _Neuron_ 109, 3851– 3861.e4.

22. Hahnloser, R.H.R., Kozhevnikov, A.A., and Fee, M.S. (2006). Sleep-related neural activity in a premotor and a basal-ganglia pathway of the songbird. _J. Neurophysiol._ 96, 794–812.

23. Shank, S.S., and Margoliash, D. (2009). Sleep and sensorimotor integration during early vocal learning in a songbird. _Nature_ 458, 73–77.

24. Wang, B., Torok, Z., Duffy, A., Bell, D., Wongso, S., Velho, T., Fairhall, A., and Lois, C. (2022). Unsupervised Restoration of a Complex Learned Behavior After LargeScale Neuronal Perturbation. _bioRxiv_ , 2022.09.09.507372. 10.1101/2022.09.09.507372.

25. Jun, J.J., Steinmetz, N.A., Siegle, J.H., Denman, D.J., Bauza, M., Barbarits, B., Lee, A.K., Anastassiou, C.A., Andrei, A., Aydın, Ç., et al. (2017). Fully integrated silicon probes for high-density recording of neural activity. _Nature_ 551, 232–236.

26. Steinmetz, N.A., Koch, C., Harris, K.D., and Carandini, M. (2018). Challenges and opportunities for large-scale electrophysiology with Neuropixels probes. _Curr. Opin. Neurobiol_ . 50, 92–100.

27. Fisher, R.S., Scharfman, H.E., and deCurtis, M. (2014). How can we identify ictal and interictal abnormal activity? _Adv. Exp. Med. Biol._ 813, 3–23.

28. Lubenov, E.V., and Siapas, A.G. (2009). Hippocampal theta oscillations are travelling waves. _Nature_ 459, 534–539.

29. Buzsáki, G. (1986). Hippocampal sharp waves: their origin and significance. _Brain Res._ 398, 242–252.

30. Hulse, B.K., Lubenov, E.V., and Siapas, A.G. (2017). Brain State Dependence of Hippocampal Subthreshold Activity in Awake Mice. _Cell Rep._ 18, 136–147.

31. Joo, H.R., and Frank, L.M. (2018). The hippocampal sharp wave–ripple in memory retrieval for immediate use and consolidation. _Nat. Rev. Neurosci._ 19, 744–757.

32. Lenz, K.M., and Nelson, L.H. (2018). Microglia and Beyond: Innate Immune Cells As Regulators of Brain Development and Behavioral Function. _Front. Immunol._ 9, 698.

33. Li, Q., and Barres, B.A. (2018). Microglia and macrophages in brain homeostasis and disease. _Nat. Rev. Immunol._ 18, 225–242.

34. Thion, M.S., Ginhoux, F., and Garel, S. (2018). Microglia and early brain development: An intimate journey. _Science_ 362, 185–189.

35. Parkhurst, C.N., Yang, G., Ninan, I., Savas, J.N., Yates, J.R., 3rd, Lafaille, J.J., Hempstead, B.L., Littman, D.R., and Gan, W.-B. (2013). Microglia promote learning-

103

dependent synapse formation through brain-derived neurotrophic factor. _Cell_ 155, 1596–1609.

36. Simpson, E. (1988). Function of the MHC. _Immunol. Suppl._ 1, 27–30.

37. Elmer, B.M., and McAllister, A.K. (2012). Major histocompatibility complex class I proteins in brain development and plasticity. _Trends Neurosci._ 35, 660–670.

38. Chacon, M.A., and Boulanger, L.M. (2013). MHC class I protein is expressed by neurons and neural progenitors in mid-gestation mouse brain. _Mol. Cell. Neurosci._ 52, 117–127.

39. Shatz, C.J. (2009). MHC class I: an unexpected role in neuronal plasticity. _Neuron_ 64, 40–45.

40. Lazarczyk, M.J., Kemmler, J.E., Eyford, B.A., Short, J.A., Varghese, M., Sowa, A., Dickstein, D.R., Yuk, F.J., Puri, R., Biron, K.E., et al. (2016). Major Histocompatibility Complex class I proteins are critical for maintaining neuronal structural complexity in the aging brain. _Sci. Rep._ 6, 26199.

41. Tchernichovski, O., Nottebohm, F., Ho, C.E., Pesaran, B., and Mitra, P.P. (2000). A procedure for an automated measurement of song similarity. _Anim. Behav._ 59, 1167– 1176.

42. Goffinet, J., Brudner, S., Mooney, R., and Pearson, J. (2021). Low-dimensional learned feature spaces quantify individual and group differences in vocal repertoires. _Elife_ 10. 10.7554/eLife.67855.

43. Sainburg, T., Thielk, M., and Gentner, T.Q. (2020). Finding, visualizing, and quantifying latent structure across diverse animal vocal repertoires. _PLoS Comput. Biol_ . 16, e1008228.

44. Yeganegi, H., Luksch, H., and Ondracek, J.M. (2019). Hippocampal-like network dynamics underlie avian sharp wave-ripples. _bioRxiv_ , 825075. 10.1101/825075.

45. Shan, K.Q., Lubenov, E.V., and Siapas, A.G. (2017). Model-based spike sorting with a mixture of drifting t-distributions. _J. Neurosci._ Methods 288, 82–98.

46. Pachitariu, M., Steinmetz, N., Kadir, S., Carandini, M., and Harris, K.D. (2016). Kilosort: realtime spike-sorting for extracellular electrophysiology with hundreds of channels. _bioRxiv_ , 061481. 10.1101/061481.

47. Pool, A.-H., Wang, T., Stafford, D.A., Chance, R.K., Lee, S., Ngai, J., and Oka, Y. (2020). The cellular basis of distinct thirst modalities. _Nature_ 588, 112–117.

48. Melsted, P., Sina Booeshaghi, A., Gao, F., Beltrame, E., Lu, L., Hjorleifsson, K.E., Gehring, J., and Pachter, L. (2019). Modular and efficient pre-processing of single-cell RNA-seq. _bioRxiv_ , 673285. 10.1101/673285.

49. Wolf, F.A., Angerer, P., and Theis, F.J. (2018). SCANPY: large-scale single-cell gene expression data analysis. _Genome Biol._ 19, 15.

50. Luebbert, L., and Pachter, L. (2023). Efficient querying of genomic reference databases with gget. _Bioinformatics_ 39. 10.1093/bioinformatics/btac836.

51. Traag, V.A., Waltman, L., and van Eck, N.J. (2019). From Louvain to Leiden: guaranteeing well-connected communities. _Sci. Rep._ 9, 5233.

52. Lopez, R., Regier, J., Cole, M.B., Jordan, M.I., and Yosef, N. (2018). Deep generative modeling for single-cell transcriptomics. _Nat. Methods_ 15, 1053–1058.

104

53. Colquitt, B.M., Merullo, D.P., Konopka, G., Roberts, T.F., and Brainard, M.S. (2021). Cellular transcriptomics reveals evolutionary identities of songbird vocal circuits. _Science_ 371. 10.1126/science.abd9704.

54. Zemel, B.M., Nevue, A.A., Dagostin, A., Lovell, P.V., Mello, C.V., and von Gersdorff, H. (2021). Resurgent Na+ currents promote ultrafast spiking in projection neurons that drive fine motor control. _Nat. Commun._ 12, 6762.

55. Carleton, J.B., Lovell, P.V., McHugh, A., Marzulla, T., Horback, K.L., and Mello, C.V. (2014). An optimized protocol for high-throughput in situ hybridization of zebra finch brain. _Cold Spring Harb. Protoc._ 2014, 1249–1258.

56. Nevue, A.A., Lovell, P.V., Wirthlin, M., and Mello, C.V. (2020). Molecular specializations of deep cortical layer analogs in songbirds. _Sci. Rep._ 10, 18767.

105

_C h a p t e r 5_

---

[← Challenges and Solutions](15-challenges-and-solutions.md) · [Up: contents](index.md) · [TRANSCRIPTOMICS IN HEALTHCARE – PART I →](17-transcriptomics-in-healthcare-part-i.md)

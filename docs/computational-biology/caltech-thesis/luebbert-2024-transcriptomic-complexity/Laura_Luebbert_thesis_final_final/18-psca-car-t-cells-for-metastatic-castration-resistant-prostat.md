---
title: 'PSCA-CAR T cells for Metastatic Castration-resistant Prostate Cancer: A Phase
  1 Trial'
source: https://thesis.library.caltech.edu/16368/
source_file: sources/luebbert-2024-transcriptomic-complexity/Laura_Luebbert_thesis_final_final.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PSCA-CAR T cells for Metastatic Castration-resistant Prostate Cancer: A Phase 1 Trial

**Source:** `Laura_Luebbert_thesis_final_final.pdf` from [luebbert-2024-transcriptomic-complexity](https://thesis.library.caltech.edu/16368/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

#### **Preamble**

This chapter describes the results obtained through single-cell RNA sequencing of the CAR T product, peripheral blood, and solid tumor tissue derived from 12 prostate cancer patients at varying time points of CAR T therapy using two different sequencing technologies, single-cell gene expression and V(D)J immune repertoire sequencing, resulting in a total of 64 multiplexed datasets and over 25 billion sequencing reads which I analyzed in parallel, revealing significant differences in the immune landscape dynamics and identifying relevant time points for clonotype expansion. Below, I am only including the relevant single-cell RNA sequencing results and methods from the published paper.

Tanya B. Dorff, M. Suzette Blanchard, Lauren N. Adkins, **Laura Luebbert,** Neena Leggett, Stephanie N. Shishido, Alan Macias, Marissa Del Real, Gaurav Dhapola, Colt Egelston, John P. Murad, Reginaldo Rosa, Jinny Paul, Ammar Chaudhry, Hripsime Martirosyan, Ethan Gerdts, Jamie R. Wagner, Tracey Stiller, Dileshni Tilakawardane, Sumanta Pal, Robert E. Reiter, Catalina Martinez, Elizabeth L. Budde, Massimo D’Apuzzo, Peter Kuhn, Lior Pachter, Stephen J. Forman, Saul J. Priceman (2024). PSCACAR T cell therapy for metastatic castration-resistant prostate cancer: a phase 1 trial. _Under review._

#### **Summary**

Despite recent therapeutic advances, metastatic castration-resistant prostate cancer (mCRPC) remains lethal. Chimeric antigen receptor (CAR) T cell therapies have demonstrated durable remissions in hematological malignancies and are of interest for patients with mCRPC. We report results from a phase 1, first-in-human study of prostate stem cell antigen (PSCA)-directed CAR T cells in patients with mCRPC screened for tumor PSCA expression. The starting dose level was 100 million (M) CAR T cells without lymphodepletion (LD), followed by incorporation of LD with 100M CAR T cells. The primary endpoints were safety and dose-limiting toxicities (DLTs). No DLTs were observed at DL1, with a DLT of grade 3 cystitis encountered at DL2, resulting in addition of a new cohort using a reduced LD regimen + 100M CAR T cells (DL3). No DLTs were observed in DL3. Cytokine release syndrome (CRS) of grade 1 or 2 occurred in 5 of 14 treated patients. PSA declines (>30%) occurred in 4 of 14 patients, as well as radiographic improvements. Dynamic changes indicating activation of peripheral blood endogenous and CAR T cell subsets, TCR repertoire diversity, and changes in the tumor immune microenvironment were observed in a subset of patients. Limited persistence of CAR T cells was observed beyond 28 days post infusion. In summary, CAR T cells targeting PSCA

106

demonstrate bioactivity at a single dose of 100M, supporting future clinical studies evaluating multiple infusions to achieve higher total dose and combinatorial approaches are needed to improve durable therapeutic outcomes.

#### **Introduction**

Metastatic castration-resistant prostate cancer (mCRPC) is a lethal disease, causing more than 30,000 deaths in American men each year (1). Immunotherapy has largely been unsuccessful; both vaccine-based strategies such as GVAX and Prost-VAC (2,3) and immune checkpoint inhibition with CTLA-4 and PD-1 inhibitors (4,5) have shown limited activity. The only immunotherapy proven to prolong survival in mCRPC is sipuleucel-T, which is an autologous cellular immunotherapy with ex-vivo incubation of dendritic cells leading to activation against prostate acid phosphatase (6). However, significant improvements are needed for immunotherapies to effectively target mCRPC.

Reasons for lack of immunotherapy response in prostate cancer are multi-fold, including strong immunosuppression in advanced prostate cancer (7)  that limits both trafficking and effector T cell function in the local tumor microenvironment. Despite this, there are unique tumor-associated antigens in mCRPC which are commonly and robustly expressed including prostate stem cell antigen (PSCA) and prostate specific membrane antigen (PSMA), which could be leveraged as targets for powerful cellular immunotherapy modalities. The dramatic successes of chimeric antigen receptor (CAR) T cell therapies in hematological malignancies have inspired the clinical development of CAR T cell therapies for the treatment of mCRPC.

PSCA is highly expressed in prostate cancer, and increases with advanced disease states, particularly in the setting of bone metastases (8). Using xenograft and syngeneic tumor models, we demonstrated safety and efficacy of second generation PSCA-CAR T cells with 4-1BB costimulation in eradicating bone metastatic prostate cancer (9). Here, we report results of our first-in-human phase 1 clinical trial to evaluate the safety and bioactivity of PSCA-CAR T cells in mCRPC patients.

#### **Results**

#### _Clinical trial design and patient characteristics_

City of Hope conducted a single center, first-in-human, phase 1 clinical trial to evaluate safety and bioactivity of PSCA-directed CAR T cells in patients with metastatic castrationresistant prostate cancer (NCT03873805). The primary endpoints were safety and doselimiting toxicities (DLT). The secondary endpoints were persistence of CAR T cells to 28 days post infusion (defined as CAR T cells comprising at least 7.5 copies/μg of DNA of total CD3 cells), expansion of CAR T cells (Max log10 copies/μg of genomic DNA, disease response (PSA decline, RECIST) and survival described as percent of participants alive at 6 months. Exploratory endpoints were phenotypes and frequencies of immune cell subsets in the peripheral blood pre- and post-therapy, serum cytokine profile before and after CAR T infusion to assess potential CRS toxicity and CAR T cell effector function, phenotype of tumor-infiltrating lymphocytes, gene expression (by RNA-seq) of CTCs, cfDNA in

107


<!-- Start of picture text -->
a<br>b<br>Subjects consented and screened<br>for PSCA expression by IHC<br>(n = 58)<br>Low PSCA expression (n = 4)<br>Patient decision to pursue other<br>treatment or deterioration in status<br>(n = 32)<br>Subjects enrolled and leukapheresis<br>(n = 22)<br>Withdrew consent after amendment<br>reducing LD (n = 1)<br>Patient deterioration in status, did not<br>meet eligibility (n = 7)<br>Subjects received CAR T cell infusion<br>(n = 14)<br>Cohorts<br>DL1: 100M<br>PSCA-CAR T cells<br>(n = 3)<br>DL2: LD + 100M<br>PSCA-CAR T cells<br>(n = 6)<br>DL3: Reduced LD + 100M<br>PSCA-CAR T cells<br>(n = 5)<br><!-- End of picture text -->

**Figure 5.1** Clinical trial design and CONSORT diagram. **(a)** Illustration of clinical trial design including subject screening, leukapheresis, PSCA-CAR T cell manufacturing, pre-infusion biopsy (BX), peripheral blood (PB) sample collection prior to lymphodepletion (LD), bone scan and CT imaging, Flu/Cy LD, PSCACAR T cell infusion, serial PB sample collection timepoints from day 0 to day 28, post-infusion bone scan and CT imaging, post-infusion BX, and long-term follow up (LTFU). **(b)** CONSORT diagram detailing subjects consented and screened for PSCA expression by immunohistochemistry (IHC) (n = 58), subjects enrolled and leukapheresis (n = 22), subjects received CAR T cell infusion (n = 14). Dose level (DL) cohorts including DL1 (100 million (M) PSCA-CAR T cells, n = 3), DL2 (Flu/Cy LD + 100M PSCA-CAR T cells, n = 6), and DL3 (Reduced Flu/Cy LD + 100M PSCA-CAR T cells, n = 5).

peripheral blood by whole exome sequencing, and CAR immunogenicity (anti-PSCA-CAR antibodies).

108

The clinical trial design is summarized in Figure 5.1a. Fifty-eight subjects were screened for PSCA expression by immunohistochemistry, twenty-two subjects underwent leukapheresis and CAR T cell manufacturing, and fourteen subjects were treated from August 2019 to July 2022 (Figure 5.1b CONSORT diagram). The first subject was prescreened (tissue testing) 5/23/19, first subject enrolled (leukapheresis) 7/30/19, and last subject treated (CAR T cell infusion) 7/25/22; the trial is closed. The median age of subjects on study was 62 for dose level (DL)1, 70 for DL2, and 69 for DL3. All subjects received prior androgen receptor signaling inhibitors, either enzalutamide (71%), abiraterone (79%), or both (64%) and a majority of patients received cabazitaxel (57%), docetaxel (86%), or both (57%) prior to CAR T cell infusion. Baseline PSA (median) ranged from 16.5 to 235.3.

#### _CAR T cell product manufacturing and characterization_

The PSCA-CAR construct comprised the anti-PSCA humanized scFv (A11 clone), �CH2 extracellular spacer, CD4 transmembrane domain, 4-1BB intracellular co-stimulatory domain, and CD3γ cytolytic domain as previously published (9). Briefly, CAR T cell manufacturing included depletion of CD14+ and CD25+ cells, CD3/28 bead stimulation, transduction with lentivirus at multiplicity of infection of 0.1, removal of beads at day 7-9, followed by expansion for a total of 12-17 days in IL-2 and IL-15 cytokines. There were no manufacturing failures, with a median CAR percentage of 86.8% in the final released product. Thawed products were characterized by flow cytometry for expression of CD4/CD8 , CD19 (for CD19t transduction marker) expression, and Fc (PSCA-CAR) expression, as well as T cell subsets demonstrating a dominant Tcm/Tem phenotype. Two products fell outside the pre-specified woodchuck post-transcriptional regulatory element (WPRE) copy number (<5), and FDA approval was granted to proceed with infusion. Median time from leukapheresis to infusion of the product was 73 days (range 34 to 182); delays were primarily due to protocol mandated holds on accrual during toxicity assessments and protocol amendments, waiting for confirmatory PSCA staining from onstudy biopsies, as well as seeking regulatory approval for the use of product out of parameters (as specified above). Six patients received bridging therapy: cabazitaxel (4), cabazitaxel + carboplatin (1), enzalutamide (1).

#### _Treatment response_

PSA declines from before treatment to day 28 after CAR T cell infusion were seen in 1 of 3 subjects in DL1, 3 of 6 subjects in DL2, and 3 of 5 subjects in DL3. Waterfall plot of the maximum PSA change from before CAR T cell infusion to day 28 shows 4 of 14 subjects with PSA declines >30% (Figure 5.2a). Of these, only 1 subject maintained PSA decline >30% beyond 28 days. In DL1, 1 of 3 subjects treated experienced a transient PSA response; notably this subject had evidence of early neuroendocrine (NE) expression in the on-study biopsy but still retained strong PSCA expression, and RECIST response was PD. Post-treatment biopsy revealed further NE transformation (data not shown). The first

109


<!-- Start of picture text -->
a<br>150 DL1<br>DL2<br>100 DL3<br>50<br>0<br>-50<br>-100<br>b<br>Death<br>Lost to follow-up<br>PI decision<br>Required disallowed therapy<br>Survival post progression<br>Stable disease<br>CAR T cell infusion to eval<br>Lymphodepletion<br>0 3 6 9 12 15 18 21 24 27 30 33<br>Months<br>c 1 month<br>Before infusion after infusion<br>143.95<br>27.91<br>15.75<br>6.65 5.12 2.16 1.72<br>-5.00<br>Change from baseline (%) -14.48 -17.86<br>-42.67 -43.39<br>-52.73<br>-94.58<br>DL3<br>DL2<br>DL1<br>UPN394 (DL3)<br><!-- End of picture text -->

**Figure 5.2** Treatment response following PSCA-CAR T cell infusion. **(a)** PSA waterfall plot showing best PSA response in the 28 days following CAR T cell infusion at each dose level (DL). **(b)** Swimmer’s plot depicting response to treatment and follow up for each subject on study. **(c)** Computed tomography (CT) scan of a patient (UPN394) in DL3 showing liver metastases before infusion and disease response 1 month after infusion of PSCA-CAR T cells.

subject treated in DL2 (with lymphodepletion) achieved a >90% PSA decline in the first 28 days post CAR T cell infusion. The response in this subject is characterized in greater detail below.

Rates of stable disease by RECIST were DL1: 0%, DL2 67%, and DL3 60%. Swimmer plots for treated subjects are shown in Figure 5.2b, with a 33%, 67%, and 40% 6-month survival rate in DL1, DL2, and DL3, respectively. The first subject treated in DL3 achieved radiographic improvement in liver metastatic burden but did not achieve PSA response (Figure 5.2c). One subject with bone only disease who exhibited stable disease in DL3 requested and received a 2<sup>nd</sup> infusion of 100M CAR T cells about 6 months following initial infusion. He experienced transient relief of cancer-related pain after the 2<sup>nd</sup> infusion.

We also evaluated treatment response by circulating tumor cell (CTC) quantification in the peripheral blood of treated subjects on study using high-definition single cell analysis (HDSCA) (10). Cytokeratin (CK)positive cells were detected in the peripheral blood of 100% of treated subjects. Overall, there were marked declines in mean CK+ cells from baseline to 28 days after CAR T cell infusion in both of the LD cohorts (DL2 and DL3), but not in DL1.

Somatic DNA sequencing results were available for 8 subjects and 2 subjects had germline testing results (no overlap between somatic and germline tested patients). Of the 8 with somatic testing, the highest tumor mutational burden was 10.5, all others were deemed low.


110

111

**Figure 5.3** Patient with biochemical and radiographic response with associated immune landscape changes. **(a)** PSA response in UPN388 on DL2 before and through the 28 days following PSCA-CAR T cell infusion and at day 90. **(b)** bone scintigraphy (anterior-posterior view) for bone metastases detection before and 1 month after PSCA-CAR T cell infusion in the same patient. Red asterisks denote representative bone metastases. **(c)** High-definition single cell analysis (HDSCA) of circulating tumor cells (CTCs) in the bone marrow before and 1 month after infusion of PSCA-CAR T cells. Quantification of CK+ cells per mL is shown in grey box. **(d)** Immunofluorescence images of bone metastasis biopsy samples from before (top) and 1 month after PSCA-CAR T cell infusion (bottom), evaluating expression of pan-cytokeratin (pan-CK) (tumor cells), PDL1, CD3 (T cells), CD8 (effector cells), and Granzyme B (GzmB). Indicated areas of tumor and stromal regions, and arrows indicate residual tumor cells in post-infusion sample. Images shown are representative of the whole evaluable tissue region on slide. **(e)** Computed tomography (CT) scan of pancreatic lesion in UPN388 before and 1 month after PSCA-CAR T cell infusion. Red circles denote pancreatic lesion around stent. Measured size of lesion before infusion, 40.2 mm x 24.8 mm. Lesion regressed 1 month after infusion and was not measurable. **(f)** scRNAseq analysis of CD3+ T cell subsets in the infused product and in the peripheral blood T cells at indicated timepoints post-T cell infusion. **(g)** Single cell analysis of TCRa/b repertoire diversity in the peripheral blood T cells at indicated timepoints post-T cell infusion. Top 40 clonotypes with greatest fractions at day 28. Legend in Figure 5.4e.

PTEN loss was noted in 3 of these subjects, one of whom experienced the greatest PSA decline on study (Figure 5.2a). In DL3, the subject with radiographic improvement in liver metastases had a genomic alteration in CDK12, and he had progressed on prior immune checkpoint inhibitor therapy.

#### _Patient with biochemical and radiographic response_

One participant, a subject in DL2, experienced a >90% PSA decline following CAR T cell infusion, from 64.2 ng/mL before LD and CAR T cells to 3.5 ng/mL at day 28 after CAR T cell infusion (Figure 5.3a). Radiographic improvement was seen in this subject’s soft tissue metastasis (Figure 5.3b) though RECIST assessment was SD due to the presence of bone metastases. Changes in serum cytokines in this patient demonstrate pronounced but transient induction of inflammatory factors, including IFNy, IL-6, GM-CSF, IP-10, and MIG. Serum chemistry showed mild increases in CRP (max 81 mg/L), ferritin (max 555 ng/mL), ALT/AST (<1.5 x ULN), LDH (max 365 U/L), and alkaline phosphatase (max 192) following CAR T cell infusion. This corresponded to grade 2 CRS with T max 39.1 on day 4, 38.8 on day 5 and tocilizumab was administered on day 6 due to persistent rigors without fever; all aforementioned labs subsequently trended down by day 21.  CTC assessment with cytokeratin positivity were significantly reduced, both in bone marrow (Figure 5.3c) and in peripheral blood samples, from baseline to 28 days after CAR T infusion. The post-CAR T cell infusion bone metastasis biopsy showed reductions in PSCA+ disease, Ki67+ expression, along with greater infiltration of CD3+ and cytotoxic CD8+ T cells by immunofluorescence staining (Figure 5.3d). Few residual tumor cells in the post-treatment biopsy were observed and were associated with increased granzyme B+ and PD-L1+ areas, suggestive of an active anti-tumor immune response. Quantification of immunofluorescence staining showed increased CD8+ and PD-L1+ areas in this subject, with variable results from other subjects analyzed. Interestingly, UPN388 also had a biopsy proven prostate cancer metastasis in the pancreas which necessitated stent placement prior to study entry; this completely resolved after CAR T cell infusion (Figure 5.3e).

112


113

**Figure 5.4** Single cell analysis of CD3+ T cell subsets and TCRα/β repertoire diversity in the peripheral blood. **(a)** scRNAseq analysis of CD3+ T cell subsets in the infused product and in the peripheral blood T cells at indicated timepoints post-T cell infusions of UPN375. **(b)** Single cell analysis of TCRα/β repertoire diversity in the peripheral blood T cells of UPN375 at indicated timepoint post-T cell infusion. **(c-d)** Same as (a-b) for UPN394. **(e)** Legend for Figure 5.3g. **(f)** Legend for Figure 5.4b. **(g)** Legend for Figure 5.4d.

#### _Immune landscape changes in patient with biochemical response_

Endogenous and CAR T cell populations in peripheral blood were further characterized by flow cytometry, as well as by single cell RNA sequencing (scRNAseq) and TCR repertoire analysis in this patient. Initial assessment of T cell subsets in peripheral blood pre- and post- LD and CAR T cell infusion in this patient showed dynamic changes in naïve (Tn), central memory Tcm), effector memory (Tem), and terminally differentiated effector memory (Temra) cells over time. Greater re-emergence of CD8+ Tcm and Tem cells were observed by day 28 post-CAR T cell infusion. CD8+ CAR T cells expanded with this phenotype by day 14 in this patient. Interestingly, CAR+ and endogenous non-CAR T cells showed increased PD1 expression (and smaller increases in LAG3 and TIM3) over the 28 days following treatment, which is associated with an activation and/or exhaustive phenotype. Peripheral blood CAR T cells showed elevated expression of CX3CR1, which has been correlated with response to immunotherapy with anti-PD1 immune checkpoint blockade (10). Few CX3CR1-positive T cells were observed in the product prior to infusion. Similar results in CAR+ and endogenous non-CAR T cells in the peripheral blood were observed in a patient in DL3, but not in DL1. scRNAseq corroborated these data, with increased effector CD8+ T cell subsets including CX3CR1+ CD8+ T cells in patients (Figure 5.3f and Figure 5.4a, c). Single cell TCR a/b repertoire analysis of endogenous T cells in peripheral blood demonstrated emerging and expanded clones by day 28 post-CAR T cell infusion in patients (Figure 5.3g, Figure 5.4b, d, e-g, and Figure 5.5), which contracted at days 90 in UPN388, suggesting TCR clonal diversity changes following therapy. Collectively, these data suggest that LD + PSCA-CAR T cell therapy can induce biochemical and radiographic response along with changes in the immune landscape and TCR repertoire.


**Figure 5.5** TCR repertoire diversity in peripheral blood T cells. Number of cells per clonotype at day 0 versus day 28 following therapy in UPN388 **(a)** , UPN375 **(b)** , and UPN394 **(c)** .

114

#### **Discussion**

CAR T cell therapy has achieved durable response rates for patients with refractory hematological malignancies (16-18), creating enthusiasm in translating this therapy to patients with solid tumors. Our study evaluated PSCA-directed CAR T cells in patients with mCRPC. We observed biochemical and radiographic responses in patients following LD and PSCA-CAR T cell infusion. The dose-limiting toxicity was cystitis, which was likely an on-target/ off-tumor effect (19) with contribution from cyclophosphamide LD (20). Reducing the cyclophosphamide dose avoided high grade cystitis events in DL3 while retaining similar peripheral blood expansion of CAR T cells, although small number of patients limits the statistical power to exclude a difference. In this heavily pretreated population, encouraging anti-cancer responses were seen. Our findings are limited by the small number of subjects accrued. Accrual to a phase 1 trial with tissue pre-screening requirement, holds to accrual during DLT assessment periods and enrollment of heavily pre-treated patients was by nature slow, and many patients did not proceed with treatment if disease progression occurred in a way that led to ineligibility, including some who had undergone leukapheresis. The relatively lengthy process may have excluded patients with more aggressive disease or borderline performance status. This highlights the importance of streamlining enrollment in phase 2 to reduce enrollment bias and overall study cost by improving the rate of infusion of manufactured CAR T cell product.  This study validates PSCA as a viable CAR T cell therapeutic target and provides encouraging early clinical data to support further studies, focused on extending CAR T cell persistence, which, with the use of novel dosing and/or combinatorial strategies is hoped to lead to improved responses in patients.

Both activity and toxicity of CAR T were impacted by the addition of LD, though the role of LD in facilitating CAR T cell activity in solid tumors is likely different than the role it plays in hematological malignancies. Preconditioning with LD promoted greater peripheral blood CAR T cell expansion and serum cytokine levels which manifested in greater objective anti-cancer response in DL2 and DL3. These phase 1 trial results validate our recent preclinical studies, which found that increased efficacy of CAR T cells following administration of cyclophosphamide was associated with enhanced T cell infiltration into tumors along with antigen presenting cell (i.e., dendritic cell) infiltration and reduced myeloid suppressive features compared to CAR T cell therapy alone (21). Notably, lower dose cyclophosphamide (300 mg/m2) still yielded greater CAR T cell bioactivity than absence of LD, while it did reduce the toxicities compared to cyclophosphamide dosed at 500 mg/m2; similar findings have been documented in hematological malignancies (22). Given the critical role of LD, an important avenue of investigation will be to study different LD regimens for optimal changes in the tumor immune microenvironment. Preclinically, gene ontology enrichment analysis identified T cell migration and IFNγ production as key processes enhanced by cyclophosphamide pre-treatment (21) and these can be used as endpoints of preclinical exploration. Metronomic dosing strategies of cyclophosphamide and alternative LD regimens warrant evaluation since the traditional high dose IV 3-day LD regimen adopted from hematological malignancy CAR T cell trials may not be equivalently translated for solid tumors. Taxanes and platinum agents have shown potential

115

for modulation of the tumor immune microenvironment and for solid tumor CAR T cell therapy (23,24) and bendamustine is also emerging as a potentially valuable LD agent (22).

DLTs were only seen after the addition of LD in this trial, mirroring the toxicity experience of the PSMA-targeted TGFβ dominant negative CAR T cell trial, in which DLT were only encountered after LD chemotherapy was added (25). In the PSMA-targeting TGFβinsensitive armored CAR T cell trial the dose of CAR T cells was reduced after high grade toxicity occurred (sepsis and macrophage activation syndrome/ hemophagocytic lymphohistiocytosis – MAS/HLH). Our approach of incorporating LD prior to CAR T cell dose escalation allowed for earlier appearance of DLTs during the trial. Therefore, reducing LD and maintaining CAR T cell dose resulted in continued evidence of anticancer efficacy with a lower toxicity profile. CRS onset was slightly delayed with PSCA CAR T cell therapy compared to the experience in hematological malignancies (26), with median onset at 4 days post infusion in this study. Tocilizumab was administered in 3 patients primarily for relief of fever and chills, with no grade 3 CRS events, and no hypotension or hypoxia events noted. Unlike other CAR T cell trials in mCRPC (25, 27,28), no high-grade neurologic toxicity nor MAS/HLH events occurred though it is unclear whether the PSCA target or this particular CAR cell construct underly this observation. Overall, the favorable toxicity profile of PSCA-CAR T cell therapy enables the currently accruing phase 1b trial (NCT05805371) to proceed with entirely outpatient dosing in the context of close clinical monitoring.

While PSCA CAR T expansion was robust with objective measures of disease-modifying activity including PSA decline, reduction in CTCs, and radiographic improvements, there was a lack of CAR T cell persistence that corresponded to the lack of durable remission. Innovative strategies will be needed to enhance CAR T cell persistence and prolong the anti-cancer efficacy. Armoring CAR T cells with modifications such as the TGFbdominant negative approach with PSMA targeting showed efficacy but at the cost of fatal toxicities, perhaps due to uncontrolled over-expansion (25). Over-expansion was also potentially the cause of fatal toxicity with the strategy employed by the Go-CART agent, in which rimiducid was administered in pulses to stimulate proliferation (28). Alternative strategies to improve persistence of CAR T cells may include enriching for T naïve/stem/memory cells (29) and incorporating agents into the CAR T cell manufacturing process to improve T cell fitness, including AKT inhibitors (30, 31). Allogeneic cell therapy approaches may further modify therapeutic activity (32) while also increasing feasibility by shortening time to treatment, which was a factor in the high drop-out rate observed in this trial. In order to avoid high-grade toxicity and to prolong the presence of infused T cells, our phase 1b strategy will administer multiple smaller doses of PSCA-CAR T cells rather than escalating to a larger single dose. Preclinical models of cystitis can be leveraged to study potential prevention or early intervention strategies, which could make it feasible to escalate the PSCA-CAR T cell dose in future trial iterations.

Tumor antigen heterogeneity with neuroendocrine transformation was noted in one patient in this study and may be a more general resistance mechanism in heavily-treated mCRPC patients. Treatment-emergent neuroendocrine transformation is reported to occur more

116

commonly in mCRPC recently since the introduction of powerful androgen receptor pathway inhibitors (33) Thus, treating patients with mCRPC earlier in the disease course may be necessary to achieve durable responses. Alternatively, dual targeting to include proteins expressed on the de-differentiated CRPC cell populations such as CEA or DLL3 (34) may be required. T cell exhaustion may have contributed to the limited duration of activity, as indicated by upregulation of PD1 in peripheral CAR T cells. Anecdotal experiences suggest that CAR T cells lose function in the setting of high tumor volumes, and immune checkpoint inhibitor therapy may rescue incomplete CAR T cell responses (35) which may have contributed to the long-term survival of a patient who received pembrolizumab as part of a clinical trial after participation in the phase 1 PSCA-CAR T study (Figure 5.2).

In summary, our first-in-human phase 1 trial evaluating PSCA-CAR T cell therapy showed bioactivity and early evidence of clinical effectiveness, though on-target toxicity of cystitis impacted intended CAR T cell dose escalation. Reduced LD dose mitigated toxicity while still enhancing CAR T cell expansion compared to no LD. Future studies will explore multi-dose and combinatorial strategies to improve persistence with the goal of increasing clinical activity in patients with mCRPC.

#### **Methods**

_Trial design and patients_

This was a single-center phase 1 trial aimed at evaluating safety and feasibility of intravenously administered, lentivirally transduced PSCA-CAR T cells in patients with mCRPC, with a total of three dose level (DL) cohorts. The primary endpoints were safety and dose-limiting toxicities (DLT). The secondary endpoints were persistence of CAR T cells to 28 days post infusion (defined as CAR T cells comprising at least 7.5 copies/μg of DNA of total CD3 cells), expansion of CAR T cells (Max log10 copies/μg of genomic DNA, disease response (PSA decline, RECIST) and survival described as percent of participants alive at 6 months. Exploratory endpoints were phenotypes and frequencies of immune cell subsets in the peripheral blood pre- and post-therapy, phenotype of tumorinfiltrating lymphocytes, gene expression (by RNA-seq) of CTCs, cfDNA in peripheral blood by whole exome sequencing, CAR immunogenicity (anti-PSCA-CAR antibodies) and serum cytokine profile before and after CAR T cell infusion to assess potential CRS toxicity and CAR T cell effector function.

The trial was conducted in accordance with the United States Food and Drug Administration (FDA) and International Conference on Harmonization Guidelines for Good Clinical Practice, the Declaration of Helsinki and applicable institutional review board requirements (study protocol approved by the City of Hope Institutional Review Board). Only subjects with male sex were enrolled due to prostate cancer presenting only in this sex group. After IND was obtained and institutional review board approved the protocol, subjects provided written informed consent in a two-step process. Many patients pre-screened (tissue PSCA testing) but did not proceed with leukapheresis due to lengthy wait times with limited slot availability and accrual pauses during DLT evaluation periods. The trial was registered with clinicaltrials.gov (NCT <mark>03873805)</mark> . The City of Hope Data

117

Safety Monitoring Board monitored the conduct of this study to ensure the safety of enrolled and treated subjects, and the validity and integrity of the acquired data.

A starting dose of 100 million (M) PSCA-CAR T cells was selected based on experience with other CAR T cell trials and anticipated effective dose. The first 3 subjects on Dose level (DL) 1 at 100M CAR T cells without fludarabine and cyclophosphamide (Flu/Cy) preconditioning lymphodepletion (LD), and the first 3 subjects on DL2 at 100M CAR T cells with LD were staggered through the dose-limiting toxicity (DLT) period.  All further subjects were accrued to dose levels (DLs) in cohorts of 3. After evaluation of the data from the completed DLT period (28 days) the protocol management team met to determine whether it was safe to escalate to the next DL, with rules following the TEQR design of Blanchard and Longmate (11) with an equivalence range of 0.20-0.35 and a too toxic level of 0.51. The first cohort received 100M CAR T cells without LD; the subsequent cohorts would all receive LD with plans to escalate the dose of CAR T cells from 100M to 300M to 600M, and the option to de-escalate the dose to 50M if LD plus 100M CAR T cells was not tolerated.

Lymphodepletion (LD) chemotherapy: standard regimen of cyclophosphamide 500 mg/m2 IV on days -5 to -3 and fludarabine 30 mg/m2 IV on days -5 to -3 was employed in DL2; this was reduced due to DLT, and DL3 subjects received cyclophosphamide 300 mg/m2 IV on days -5 to -3 with the same dose schedule of fludarabine. Prophylactic G-CSF was not utilized, but G-CSF could be added for neutropenia if the treating physician felt it was indicated, as well as all other standard supportive measures such as antiemetics.

In order to attempt to exclude patients unlikely to benefit due to lack of tumor PSCA expression, all potential subjects signed a pre-screening consent form so that archived tissue could be tested for PSCA by immunohistochemistry (IHC) staining. Subjects were required to have at least moderate PSCA expression in their prostate primary or metastatic biopsy tissue to enroll in the study, although due to lack of a validated assay there was no pre-specified cut-off. All subjects enrolled had PSCA expression in >30% of tumor cells (Figure 5.1a CONSORT diagram). An on-study biopsy was performed, and for soft tissue metastases confirmation of PSCA staining was required (this was not required for bone metastases due to inadequate calibration of the IHC assay on bone material); repeat biopsy of the same metastatic area was performed during the day 28 assessment period.

Patients with mCRPC were eligible if they had experienced disease progression on at least one androgen receptor pathway inhibitor, e.g. abiraterone, enzalutamide. Prior taxane chemotherapy was allowed but not required.  Creatinine clearance > 50 mL/min were required, as well as AST/ALT < 5 x ULN and bilirubin < 2.0 mg/dL. Electrocardiogram was required to show no acute abnormalities requiring intervention and echocardiogram was required to document a left ventricular ejection fraction of > 40%. Patients with clinically significant cardiac arrhythmias or central nervous system disease were excluded. Patients with HIV, active hepatitis B or C, or uncontrolled active infection were excluded. Eligibility was confirmed prior to leukapheresis and again prior to start of treatment (DL1: CAR T and DL 2 or DL 3: LD).

118

#### _CAR T cell manufacturing_

Following screening and enrollment into the trial, subjects underwent leukapheresis at City of Hope’s Michael Amini Transfusion Medicine Center. Autologous PBMC were immunomagnetically depleted of CD14+ and CD25+ cells, then stimulated with CD3/CD28 DynaBeads and subjected to transduction with PSCA(dCH2)BBζ/CD19t lentivirus (multiplicity of infection = 0.1) followed by T cell expansion for 10-16 days until the freezing process. Cells were manufactured in the City of Hope Center for Biomedicine and Genetics (CBG) GMP facility; details are provided in the clinical protocol (see Supplemental Materials).

#### _Flow cytometry_

Peripheral blood samples were obtained from subjects prior to and at various timepoints for 28 days following CAR T cell infusion, as well as day 60, 90, and q12 weeks after day 90 to evaluate CAR T cell expansion/persistence. Peripheral blood samples were lysed using BD PharmLyse (15 min at RT) and quenched using RPMI containing 10% FBS. Cells were resuspended in FACS buffer (Hank’s balanced salt solution without Ca2+, Mg2+, or phenol red (HBSS−/−, Life Technologies) containing 2% FBS and 1 × AA). Cells were incubated with Fc block (BD Biosciences) for 5 min at RT and then incubated with fluorescence-labelled antibodies for 15 min at RT in the dark. Unless otherwise stated, antibodies were used at a dilution of 1:100. Cell viability was determined using 4′, 6- diamidino-2-phenylindole (DAPI, Sigma, Cat: D8417). For samples run on the Cytek Aurora, samples were thawed, counted using a Muse cell counter (1 milion cells) and were stained in a two-step process.  Before staining, the cells were Fc Blocked with BD Pharmingen™ Human BD Fc Block™ (BD Biosciences) for 20 min on ice, washed, spun, and resuspended in the first master mix. The first master mix included 1 antibody, PDL1 PE-Fire810 (Biolegend), in FACS buffer.  Following incubation on ice for 20 minutes, cells were washed twice with FACS Buffer and then stained with a 23-antibody master mix. The second master mix was prepared using FACS Buffer with Brilliant Buffer Plus (BD Horizon). After incubation, the cells were washed twice with FACS Buffer and finally resuspended in FACS buffer with 7-AAD (Invitrogen). Flow cytometry was performed on a MACSQuant Analyzer 10 (Miltenyi Biotec) or Cytek Aurora 3, and data were analyzed with FlowJo software (v10.8.1, TreeStar) or OMIQ software (Dotmatics).

#### _Single cell transcriptomics and TCR repertoire analysis_

Single cell RNA and TCR libraries were prepared using 10x Genomics Chromium Single Cell Immune Profiling Solution Kit and workflow (10×Genomics Inc.). Cells were thawed, washed twice, and resuspended in RPMI containing 10% FBS to a final concentration of 100–1000 cells per μl as determined by Cell Countess. Samples with unique donor identities were pooled together and processed for a targeted cell recovery of 10,000 cells. Single cell RNA-seq and TCR-seq libraries were assessed for quality and quantified using the Agilent 2100 Bioanalyzer System and Qubit 3.0 Fluorometer. Single cell RNA libraries were sequenced on an Illumina NovaSeq to a minimum sequencing depth of 25,000 reads per cell using read lengths of 26 bp read 1, 8 bp i7 index, 98 bp read 2. The single-cell TCR libraries were sequenced on an Illumina HiSeq and NovaSeq to a minimum sequencing depth of 5,000 reads per cell using read lengths of 150 bp read 1, 8 bp i7 index, 150 bp

119

read 2. DNA was extracted from each sample donor’s CAR T cell product using the DNeasy Blood and Tissue Kit (Qiagen) and recommended protocol for Purification of Total DNA from Animal Blood or cells. Isolated DNA was genotyped with Infinium Omni5-4 Beadchip Array at City of Hope’s Integrative Genomics Core.

A full description of the methods and code used to process and analyse the single-cell RNA seq data is available at: <u>https://github.com/pachterlab/DBALLSMRDMCMGWSTPMBDKPFP_2023.</u>

#### **Acknowledgements**

This study was funded by a 2017 Prostate Cancer Foundation Challenge Award (S.J.P., S.J.F.) and an NCI SPORE Award (P50CA092131). Studies reported in this publication were also supported by the Doug and Rhonda Collier Foundation fund, the Fiterman Family Foundation fund, and the Borstein Foundation fund. Work performed in the GMP facility and the COH Pathology Core supported by the National Cancer Institute of the National Institutes of Health under grant number P30CA033572. We thank the Analytical Pharmacology Core Facility (APCF) for their assistance in performing correlatives assays, and the T Cell Therapeutics Research Laboratories (TCTRL) and the Center for Biomedicine and Genetics (CBG) for CAR T cell manufacturing and product release. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes.

#### **Competing Interests**

T.B.D. is a consultant for AstraZeneca and Janssen. S.J.P. and S.J.F. are scientific advisors to and receive royalties from Mustang Bio. S.J.P. is also a scientific advisor and/or receives royalties from Imugene Ltd, Adicet Bio, Port Therapeutics, and Celularity. S.J.P. and S.J.F. are listed as co-inventors on a patent on chimeric antigen receptors targeted to PSCA, which is owned by the City of Hope. All other authors declare that they have no competing interests.

#### **Data availability statement**

All required clinical data have been uploaded to clinicaltrials.gov. All requests for raw and analyzed data and materials should be addressed to the corresponding authors and will be reviewed by the institution to verify whether the request is subject to any intellectual property or confidentiality obligations. Patient data may be subject to patient confidentiality. Any data and materials that can be shared will be released via a material transfer agreement.

#### **Code availability statement**

A description of the methods and the code used to process and analyze the single-cell RNA seq and TCR seq data is available at:

<u>https://github.com/pachterlab/DBALLSMRDMCMGWSTPMBDKPFP_2023.</u> Full access the TCR and single cell RNA seq can be accessed via: <u>https://www.dropbox.com/scl/fo/rhgr2y28az1e2h0avaj0l/h?rlkey=6a4wlnus0png19mb80 g42uja1&dl=0 (password: coh_128781)</u>

120

#### **Obtaining biologic materials statement**

Chimeric antigen receptor T cells (CAR T cells) were manufactured at City of Hope in the GMP facility, with materials and processes approved by FDA IND. These are provided (administered) only to individual patients enrolled on the trial.

#### **References**

1. Siegel RL, Miller KD, Fuchs HE, Jemal A. Cancer Statistics, 2021. _CA Cancer J Clin_ 2021; 71:7-33.

2. Higano CS, Corman JM, Smith DC, Centeno AS, Steidle CP, Gittleman M, _et al._ Phase 1-2 dose-escalation study of a GM-CSF-secreting, allogeneic, cellular immunotherapy for metastatic hormone-refractory prostate cancer. _Cancer_ 2008; 113:975-84.

3. Gulley JL, Borre M, Vogelzang NJ, Ng S, Agarwal N, Parker CC, et al. Phase III trial of PROSTVAC in asymptomatic or minimally symptomatic metastatic castrationresistant prostate cancer. _J Clin Oncol_ 2019; 37:1051-61.

4. Antonarakis ES, Piulats JM, Gross-Goupil M, Goh J, Ojamaa K, Hoimes CJ _, et al._ Pembrolizumab for Treatment-Refractory Metastatic Castration-Resistant Prostate Cancer: Multicohort, Open-Label Phase II KEYNOTE-199 Study. _J Clin Oncol_ 2020;38(5):395-405 doi 10.1200/JCO.19.01638.

5. Kwon ED, Drake CG, Scher HI, Fizazi K, Bossi A, van den Eertwegh AJ _, et al._ Ipilimumab versus placebo after radiotherapy in patients with metastatic castrationresistant prostate cancer that had progressed after docetaxel chemotherapy (CA184043): a multicentre, randomised, double-blind, phase 3 trial. _Lancet Oncol_ 2014;15(7):700-12 doi 10.1016/S1470-2045(14)70189-5

6. Kantoff PW, Higano CS, Shore ND, Berger ER, Small EJ, Penson DF _, et al._ SipuleucelT immunotherapy for castration-resistant prostate cancer. _N Engl J Med_ 2010;363(5):411-22 doi 10.1056/NEJMoa1001294

7. Dorff TB, Narayan V, Forman SJ, Zang PD, Fraietta JA, June CH, Haas NB, Priceman SJ. Novel redirected T-cell immunotherapies for advanced prostate cancer. _Clin Cancer Res_ 2022; 28:576-84.

8. Gu Z, Thomas G, Yamashiro J, Shintaku IP, Dorey F, Raitano A, _et al._ Prostate stem cell antigen (PSCA) expression increases with high gleason score, advanced stage and bone metastasis in prostate cancer. _Oncogene_ 2000; 19:1288-96.

9. Priceman SJ, Gerdts EA, Tilakawardane D, Kennewick KT, Murad JP, _et al._ Costimulatory signaling determines tumor antigen sensitivity and persistence of CAR T cells targeting PSCA + metastatic prostate cancer. _Oncoimmunology_ 2017; 7:e1380764

10. Yamauchi T, Hoki T, Oba T, Jain V, Chen H, Attwood K, _et al._ T cell CX3CR1 expression as a dynamic blood-based biomarker of response to immune checkpoint inhibitors. _Nat Commun_ 2021; 12:1402 doi: 10.1038/s41467-021-21619-0.

11. Blanchard MS, Longmate JA. Toxicity equivalence range design (TEQR): a practical phase I design. _Contemp Clin Trials_ 2011; 32:114-21.

   - 121

12. Chai S, Matsumoto N, Storgard R, Peng C-C, Aparicio A, Ormseth B, _et al._ Plateletcoated circulating tumor cells are a predictive biomarker in patinets with metastatic castrate-resistant prostate cancer. _Mol Cancer Res_ 2021; 19:2036-45

13. Shishido SN, Sayeed S, Courcobubetis G, Djaladat H, Miranda G, Pienta KJ, _et al._ Characterization of cellular and acellular analytes from pre-cystectomy liquid biopsies in patients newly diagnosed with primary bladder cancer. _Cancers_ 2022; 14:758. Doi: 10.3390/cancers14030758

14. Setayesh SM, Hart O, Naghdloo A, Hga N, Nieva J, Lu J, Hwang S, _et al._ Multianalyte liquid biopsy to aid the diagnostic workup of breast cancer. _NPJ Breast Cancer_ 2022; 8:112. Doi:10.1038/s41523-022-00480-4.

15. Shishido SN, Ghoreifi A, Sayeed S, Courcobetis G, Huang A, Ye B, _et al._ Liquid biopsy landscape in patinets with primary upper tract urothelial carcinoma. _Cancers_ 2022; 14:3007. Doi:10.3390/cancers14123007.

16. Neelapu SS, Locke FL, Bartlett NL, Lekakis LJ, Miklos DB, _et al._ <mark>Axicabtagene ciloleucel CAR T-cell therapy in refractory large B-cell lymphoma.</mark> _<mark>N. Engl. J. Med.</mark>_ <mark>2017;</mark> **<mark>377</mark>** <mark>:2531–2544</mark>

17. Maude SL, Laetsch TW, Buechner J, Rives S, Boyer M, _et al._ <mark>Tisagenlecleucel in children and young adults with B-cell lymphoblastic leukemia.</mark> _<mark>N. Engl. J. Med.</mark>_ <mark>2018;</mark> **<mark>378</mark>** <mark>:439–448</mark>

18. Schuster SJ, Svoboda J, Chong EA, Nasta SD, Mato AR, _et al_ _<mark>.</mark>_ <mark>Chimeric antigen receptor T cells in refractory B-cell lymphomas.</mark> _<mark>N. Engl. J. Med.</mark>_ <mark>2017;</mark> **<mark>377</mark>** <mark>:2545–2554</mark>

19. Cheng L, Reiter RE, Jin Y, Sharon H, Wieder J, Lane TF _, et al._ Immunocytochemical analysis of prostate stem cell antigen as adjunct marker for detection of urothelial transitional cell carcinoma in voided urine specimens. _J Urol_ 2003; **169** (6):2094-100 doi 10.1097/01.ju.0000064929.43602.17.

20. Almalag HM, Alasmari SS, Alrayes MH, Binhameed MA, Alsudairi RA, _et al._ Incidence of hemorrhagic cystitis after cyclophosphamide therapy with or without mesna: a cohort study and comprehensive literature review _. J Oncol Pharm Pract_ 2021; 27:340-9. Doi: 10.1177/1078155220920690. city

21. Murad JP, Tilakawardane D, Park AK, Lopez LS, Young CA, Gibosn J _et al._ Preconditioning modifies the TME t enhance solid tumor CAR T cell efficacy and endogenous protective immunity. _Mol ther_ 2021; 29:2335-49.

22. Amini L, Silbert SK, Maude SL, Nastoupil LJ, Ramos CA, _et al._ Preparing for CAR T cell therapy: patient selection, bridging therapies and lymphodepletion. _Nat Rev Clin Oncol_ 2022; 19:342-55.

23. Alzubi J, Dettmer-Monaco V, Kuehle J, Thorausch N, Seidl M, Taromi S _, et al._ PSMADirected CAR T Cells Combined with Low-Dose Docetaxel Treatment Induce Tumor Regression in a Prostate Cancer Xenograft Model. _Mol Ther Oncolytics_ 2020; **18** :22635 doi 10.1016/j.omto.2020.06.014

   - 122

24. Kershaw MH, Devaud C, John LB, Westwood JA, Darcy PK. Enhancing immunotherapy using chemotherapy and radiation to modify the tumor microenvironment. _Oncoimmunology_ 2012; e25962.

25. Narayan V, Barber-Rtenberg JS, Jung I-Y, Lacey SF, Rech AJ, _et al._ PSMA-targeting TGFb-insensitive armored CAR T cells in metastatic castration-resistant prostate cancer: a phase 1 trial. _Nat Med_ 2022; 28:7224-34.

26. Maude, SL, _et al.,_ Managing cytokine release syndrome associated with novel T cellengaging therapies. _Cancer_ J, 2014. **20** (2): p. 119-22

27. Slovin SF, Dorff TB, Falchook GS, Wei XX, Gao X, McKay RR, _et al._ Phase 1 study of P-PSMA-101 CAR-T cells in patients with metastatic castration-resistant prostate cancer. _J Clin Oncol_ 2022; supp (abstr 98).

28. <mark>Stein MN, Teply BA, Gergis U, Strickland D, Senesac J, Bayle H,</mark> _<mark>et al.</mark>_ <mark>Early results form a phase 1, multicenter trial of PSCA-specific GoCAR T cells (BPX-601) in patients with metastatic castration-resistant prostate cancer (mCRPC).</mark> _<mark>J Clin Oncol</mark>_ <mark>2023; 41 (supp) abstr 140</mark>

29. Aldoss I, Khaled SK, Wang X, Palmer J, Wang Y, Wagner JR, Clark MC, _et al._ Favorable activity and safety profile of memory-enriched CD19-targeted chimeric antigen receptor T-cell therapy in adults with high-risk relapsed/refractory ALL. _Clin Cancer Res_ 2023; 29:742-53.

30. Urak R, walter M, Lim L< Wong CLW, Budde LE, Thomas S, Forman SJ, Wang X. Ex vivo Akt inhibitiorn promotes the generation of potent CD19 CAR T cells for adoptime immunotherapy. J IMmunother Cancer 2017; 5:26 doi:10.1186/s40425-0170227-4

31. Mehra V, Agliardi G, Pinto JDA, Shafat MS, Garai AC, Green L, _et al._ AKT inhibition generates potent polyfunctional clinical grade AUTO1 CAR T-cells, enhancing function and survival. _J Immunother Cancer_ 2023; 11:e007002. Doi:10.1136/jitc2023-007002.

32. Depil S, Duchateau P, Grupp SA, Mufti G, Poirot L. ‘Off the shelf; allogeneic CAR T cells: development and challenges. _Nat Rev Drug Discov_ 2020; 19:185-99.

33. Liu S, Alabi BR, Yin Q, Stoyanova T. Molecular mechanisms underlying the development of neuroendocrine prostate cancer. Semin Cancer Biol 2022; 86:57-68.

34. <mark>DeLucia DC, Cardillo TM, Ang L, Labrecque MP, Zhang A, Hopkins JE</mark> _<mark>et al.</mark>_ <mark>Regulation of CEACAM5 and therapeutic efficacy of an anti-CEACAM5-SN38 antibody-drug conjugate in neuroendocrine prostate cancer.</mark> _<mark>Clin Cancer Res</mark>_ <mark>2021; 27:759-774</mark>

35. Adusumilli PS, Zauderer MG, Riviere I, Solomon SB, Rusch VW, O’Cearbhaill RE, _et al._ A phase I trial of regional mesothelin-targeted CAR T-cell therapy in patients with malignant pleural disease, in combination with the anti-PD-1 antibody agent pembrolizumab. _Cancer Discovery_ 2021; 11:2748-63.

123

TRANSCRIPTOMICS IN HEALTHCARE – PART II

---

[← TRANSCRIPTOMICS IN HEALTHCARE – PART I](17-transcriptomics-in-healthcare-part-i.md) · [Up: contents](index.md) · [Laura Luebbert thesis final final Part 19 — →](19-laura-luebbert-thesis-final-final-part-19.md)

---
title: Model size is fairly insensitive to size penalty
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/17-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Model size is fairly insensitive to size penalty

**Source:** `lectures/17-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

#### **Objective function = Fit of data (MSE) + α Size**


<!-- Start of picture text -->
200<br>0.2<br>160<br>Substantial number of<br>0.15<br>120<br>scaffold arcs not supported<br>by hepatocyte data<br>80 0.1<br>40 0.05<br>0<br>0<br>-7  -5  -3 -1<br>0  10  10  10 10<br>Size penalty !<br>f<br>!MSE<br>!Size S<br>!Objective function<br><!-- End of picture text -->

##### **selected model-size penalty, for maximal predictive capability**

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

21

**_Models can only be partially identified -- thus model families are best outcome_**

**Frequency of Arc Distribution for Error Tolerance-Related (** **_i.e._ , beyond exptl uncertainty) Model Families**


<!-- Start of picture text -->
arc<br>frequency<br><!-- End of picture text -->


<!-- Start of picture text -->
*<br>*<br>0% identifiability<br><!-- End of picture text -->

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

22

### **_Trade-off between False Negatives and False Positives_**

- **Receiver Operating Characteristic (ROC) curve [ratio of true positives (1-false negatives) vs. false positives] for different values of the size penalty α**

- **Optimal choice of size penalty (α=10**<sup>**-5**</sup> **) corresponds to most predictive model**

- **Extended model (** **_i.e._ , with added arcs) decreases false negatives but increases false positives**


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

23


- **_Model Validation_**

- **_-- successful_ a priori**

- **_predictions of new test data_**

      - ! **Used trained model to** **_a priori_ predict effects of ligand combinations,**

      - **additional inhibitors, and inhibitor combinations**

   - ! **New test data predicted to within ~11% error,**

   - **comparable to ~9% for original training data**


<!-- Start of picture text -->
0  0.5  1<br>Agree                            Disagree<br><!-- End of picture text -->

- ! **Can identify loci needing more detailed inquiry**

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

24

- **_Extension to comparison among hepatocellular lines -- phosphoproteomic data_**

© American Association for Cancer Research. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Saez-Rodriguez, Julio, Leonidas G. Alexopoulos, et al. "Comparing Signaling Networks Between Normal and Transformed Hepatocytes Using Discrete Logical Models." _Cancer Research_ 71, no. 16 (2011): 5400-11.

25

### **_Demonstration of benefit of cell type-specific models_**

### **_Demonstration of capability to identify particular points inviting further study_**


© American Association for Cancer Research. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Saez-Rodriguez, Julio, Leonidas G. Alexopoulos, et al. "Comparing Signaling Networks Between Normal and Transformed Hepatocytes Using Discrete Logical Models." _Cancer Research_ 71, no. 16 (2011): 5400-11.

26


### **_Best-Fit Boolean Logic Model Families for Primaries versus_**

   - **_Lines_**

- **Arc width corresponds to**

- **proportion of best-fit models bearing it**

- **Black arcs – all models in**

- **both primaries and HCC lines**

- **Blue arcs – most or all**

- **primary models**

- **Red arcs – most or all HCC**

- **line models**

- **Gray arcs deleted from**

- **original scaffold**

- **Dashed arc added to**

- **account for especially recalcitrant data**

© American Association for Cancer Research. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Saez-Rodriguez, Julio, Leonidas G. Alexopoulos, et al. "Comparing Signaling Networks Between Normal and Transformed Hepatocytes Using Discrete Logical Models." _Cancer Research_ 71, no. 16 (2011): 5400-11.

27


**_Best-Fit Boolean Logic Model Families for Primaries versus Lines_**

- **~90% of original scaffold**

- **interactions were found in at least one best-fit model across families for all cell types**

- **but only <10% were found**

- **both in most primary cell models and cell line models** • **multiple pathways are identifiable as dysregulated from normal to tumor lines**

© American Association for Cancer Research. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Saez-Rodriguez, Julio, Leonidas G. Alexopoulos, et al. "Comparing Signaling Networks Between Normal and Transformed Hepatocytes Using Discrete Logical Models." Cancer Research 71, no. 16 (2011): 5400-11.

28


**_Model permits novel insights concerning drug actions_**

**Dashed arc added to fit data generated in presence of IKK inhibitor TPCA1 – two potential explanations:**

- **IKK activity suppresses**

- **STAT3 activity downstream of JAK2;** **_or_**

- **TPCA1 has off-target**

- **effect on JAK2**

© American Association for Cancer Research. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Saez-Rodriguez, Julio, Leonidas G. Alexopoulos, et al. "Comparing Signaling Networks Between Normal and Transformed Hepatocytes Using Discrete Logical Models." _Cancer Research_ 71, no. 16 (2011): 5400-11.

29

**_Experimental validation of model prediction that putative IKK inhibitor TPCA1 hits JAK2 as an off-target substrate_**

#### **_(whereas BMS-345541 does not)_**


© American Association for Cancer Research. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Saez-Rodriguez, Julio, Leonidas G. Alexopoulos, et al. "Comparing Signaling Networks Between Normal and Transformed Hepatocytes Using Discrete Logical Models." _Cancer Research_ 71, no. 16 (2011): 5400-11.

**…perhaps providing an explanation for why TPCA1 has been found to be more efficacious for airway inflammation treatment than other IKK inhibitors**

30


- **_Best-Fit Boolean Logic Model Families_**

- **_-- comparison among HCC Lines_**

   - **cell-type specificity of**

   - **network operation is thus explicitly characterized – not only contrasting primaries to tumor lines but also disparities between different tumor lines**

© American Association for Cancer Research. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Saez-Rodriguez, Julio, Leonidas G. Alexopoulos, et al. "Comparing Signaling Networks Between Normal and Transformed Hepatocytes Using Discrete Logical Models." _Cancer Research_ 71, no. 16 (2011): 5400-11.

31

### **_Cell types can be quantitatively clustered with respect to common edges -- reasonable similarity to transcriptomic result_**


- © American Association for Cancer Research. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Saez-Rodriguez, Julio, Leonidas G. Alexopoulos, et al. "Comparing Signaling Networks Between Normal and Transformed Hepatocytes Using Discrete Logical Models." _Cancer Research_ 71, no. 16 (2011): 5400-11.

32

### **_Detailed Primary-vs-Lines Comparison_**

   - **8 edges are**

   - **strongly disparate between primary**

   - **hepatocytes and the HCC lines**

- © American Association for Cancer Research. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Saez-Rodriguez, Julio, Leonidas G. Alexopoulos, et al. "Comparing Signaling Networks Between Normal and Transformed Hepatocytes Using Discrete Logical Models." _Cancer Research_ 71, no. 16 (2011): 5400-11.

33

### **_Detailed Primary-vs-Lines Comparison – insights gained_**

- **Whereas EGFR leads to**

- **ERK activation in all cell types, HSP27 is**

- **significantly activated**

- **downstream of ERK only in primaries**

- • **In the lines, HSP27 was**

- **activated more mildly and via p38 instead of via ERK**

**(Literature: HCC tumor progression is associated with decreased HSP27 activation -- despite HSP27 over-expression)**

- © American Association for Cancer Research. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Saez-Rodriguez, Julio, Leonidas G. Alexopoulos, et al. "Comparing Signaling Networks Between Normal and Transformed Hepatocytes Using Discrete Logical Models." _Cancer Research_ 71, no. 16 (2011): 5400-11.

34

### **_Detailed Primary-vs-Lines Comparison – insights gained_**

• **In primaries Ikb phosphorylation requires TNFa-NIK and activation of PI3K-JNK (via TGFa or Ins), whereas in lines only TNFa-NIK is required (Literature: HCC tumor progression is associated with looser control over NFkBmediated survival signals)**

© American Association for Cancer Research. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Saez-Rodriguez, Julio, Leonidas G. Alexopoulos, et al. "Comparing Signaling Networks Between Normal and Transformed Hepatocytes Using Discrete Logical Models." _Cancer Research_ 71, no. 16 (2011): 5400-11.

35

### **_Detailed Primary-vs-Lines Comparison – insights gained_**

• **GSK3 phosphorylation by Akt (leading to nuclear activation of pro-mitotic factors) is induced by Insulin in lines but not in primaries**

**(Literature: IRS1 is overexpressed in HCC, potentially shifting Insulininduced signaling from IRS2-mediated metabolism to proliferation)**

- © American Association for Cancer Research. All rights reserved. This content is excluded from our

Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Saez-Rodriguez, Julio, Leonidas G. Alexopoulos, et al. "Comparing Signaling Networks Between Normal and Transformed Hepatocytes Using Discrete Logical Models." _Cancer Research_ 71, no. 16 (2011): 5400-11.

36

### **_These same three pathways have been implicated in_** **_<u>combination kinase therapy for HCC</u>_**

###### **IKK Akt**


<!-- Start of picture text -->
p38<br><!-- End of picture text -->


© American Association for Cancer Research. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Pritchard, Justin R., Benjamin D. Cosgrove, et al. "Three-kinase Inhibitor Combination Recreates Multipathway Effects of a Geldanamycin Analogue on Hepatocellular Carcinoma Cell Death." _Molecular Cancer Therapeutics_ 8, no. 8 (2009): 2183-92.

37


- **_Constrained Fuzzy_**

- **_Logic_** � **_Framework_**

- **_allows Analog Model rather than Digital_**


Courtesy of Morris et al. License: CC-BY.

Source: Morris, Melody K., Julio Saez-Rodriguez, et al. "Training Signaling Pathway Maps to Biochemical Data with Constrained Fuzzy Logic: Quantitative Analysis of Liver Cell Responses to Inflammatory Stimuli." _PLoS Computational Biology_ 7, no. 3 (2011): e1001099.

38

### **_HepG2 Constrained Fuzzy Logic Network Model (again consensus family)_**


<!-- Start of picture text -->
Extracellular<br>cues<br>TNF! IL1a  LPS  TGF! IGF1  IL6<br>0.38 ± 0.09<br>0.32 ± 0.13  0.5 ± 0<br>0.13 ± 0.08<br>0.41 ± 0.04  0.06 ± 0.01<br>0.2 ± 0.08  *<br>TRAF6  Ras  PI3K<br>0.41 ± 0.17<br>0.11 ±  0.05<br>*<br>MAP3K7  MAP3K1  Akt  MEK1/2<br>Protein<br>signals<br>MKK4  IKK<br>JNK1/2  p38<br>0.49 ± 0.15<br>0.8 ± 0.16<br>MSK1/2  p90RSK mTOR<br>0.38 ± 0.16<br>0.49 ± 0.16  0.34 ± 0.18<br>0.28 ± 0.11<br>c-Jun  Hsp27  p53  I"B  Gsk3  HistH3 CREB IRS1s p70s6  STAT3<br>Courtesy of Morris et al. License: CC-BY.<br>Source: Morris, Melody K., Julio Saez-Rodriguez, et al. "Training Signaling Pathway Maps to Biochemical Data<br>with Constrained Fuzzy Logic: Quantitative Analysis of Liver Cell Responses to Inflammatory Stimuli."<br>PLoS Computational Biology 7, no. 3 (2011): e1001099.<br>0.68 ± 0.18<br>0.18 ± 0.08<br>0.38 ±<br>0.17<br>0.57 ± 0.19<br>0.2 ± 0.08<br>0.43 ±<br>0.11<br>0.6 ± 0.15<br>0.59 ± 0.17<br>0.68 ±<br>0.15<br>0.37 ±0.13<br>0.3 ±0.07<br>0.62 ±<br>0.2<br>0.66 ±0.14<br>0.45<br>0.75 ± 0.18<br>0.5 ± 0.17<br>0.19 ± 0.05  0.6 ± 0.13<br><!-- End of picture text -->

**_Intensity of arc = likelihood of connection_**

**_Numerical descriptor = upstream-downstream effect strength_**

**_*_**<sup>**_= new arcs not identified by Boolean model_**</sup>

39

### **_Example Results for Quantitative Cell Circuit Logic -- downstream_** � **_child_** � **_node versus upstream_** � **_parent_** � **_nodes_**

**Red points: experimental values Gray points: averaged-model predictions : averaged-model predictions Gold points: individual model predictions : individual model predictions**


<!-- Start of picture text -->
Gray points: averaged-model predictions : averaged-model predictions<br>1.2 Gold points: individual model predictions : individual model predictions<br>1 TNF! IL1a  LPS  TGF! IGF1  IL6<br>0.38 ±  0.09<br>0.32 ±  0.13  0.5 ±  0<br>0.13 ±  0.08<br>0.8 0.41 ±  0.04  0.06 ±  0.01<br>0.2 ±  0.08  TRAF6  Ras PI3K<br>0.6 0.41 ±  0.17<br>0.11 ±  0.05<br>0.4 MAP3K7  MAP3K1  Akt  MEK1/2<br>0.2<br>MKK4  IKK<br>0<br>-0.2 JNK1/2  p38<br>1 0.9 0.8 1 0.49 ±  0.15 0.8 ±  0.16<br>0.7 0.6 0.8 0.9 MSK1/2 p90RSK  mTOR<br>0.5 0.4 0.5 0.6 0.7 0.49 ±  0.16  0.34 ±  0.18  0.38 ±  0.16<br>0.3 0.4 0.28 ±  0.11<br>MEK1/2 0.2 0.2 0.3 c-Jun  Hsp27  p53  I"B  Gsk3  HistH3 CREB  IRS1s  p70s6 STAT3<br>0.1<br>0.1 0 0 p38<br>0.68 ±  0.18<br>0.18 ±  0.08<br>0.38 ±  0.17<br>0.57 ±  0.19<br>0.2 ±  0.08<br>0.43 ±  0.11<br>0.6 ±  0.15<br>0.59 ±  0.17  0.68 ±  0.15<br>0.37 ±  0.13<br>0.3 ±  0.07<br>0.62 ±  0.2<br>0.66 ±  0.14<br>0.45<br>0.75 ±  0.18<br>0.5 ±  0.17<br>0.19 ±  0.05  0.6 ±  0.13<br>CREB<br><!-- End of picture text -->

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Courtesy of Morris et al. License: CC-BY.

Source: Morris, Melody K., Julio Saez-Rodriguez, et al. "Training Signaling Pathway Maps to Biochemical Data with Constrained Fuzzy Logic: Quantitative Analysis of Liver Cell Responses toInflammatory Stimuli." _PLoS Computational Biology_ 7, no. 3 (2011): e1001099.

**New test data fell within one standard deviation of predictions across all conditions**

40

### **_Model family precision generally presages accuracy_**


Courtesy of Morris et al. License: CC-BY.

Source: Morris, Melody K., Julio Saez-Rodriguez, et al. "Training Signaling Pathway Maps to Biochemical Data with Constrained Fuzzy Logic: Quantitative Analysis of Liver Cell Responses to Inflammatory Stimuli." _PLoS Computational Biology_ 7, no. 3 (2011): e1001099.

41

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Central Topic: Regulation of Mammalian Cell Behavior by Receptor-Mediated Signaling](01-central-topic-regulation-of-mammalian-cell-behavior-by-recep.md) · [Up: contents](index.md)

---
title: 'Central Topic: Regulation of Mammalian Cell Behavior by Receptor-Mediated
  Signaling'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/17-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Central Topic: Regulation of Mammalian Cell Behavior by Receptor-Mediated Signaling

**Source:** `lectures/17-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**_extracellular behavior ligand ‘response’ ‘cues’ (phenotype)_**

**_‘signals’ [‘execution’– transcription / translation, metabolism / synthesis, cytoskeleton / motors]_**

Courtesy of Elsevier, Inc., http://www.sciencedirect.com. Used with permission. Source: Hanahan, Douglas, and Robert A. Weinberg. "The Hallmarks of Cancer." C _ell_ 100, no. 1 (2000): 57-70.

2

**_Objective: Learn how cell signaling network operation – in multi-pathway manner -- differs between normal and disease state or among various individuals_**

**cell / tissue phenotypic behavior**


<!-- Start of picture text -->
or among various individuals<br>environmental context<br>altered<br>behavior of<br>cellular<br>� machines �<br>and<br>� circuits �<br>DNA<br>dynamic<br>mRNA<br>sequence protein  protein<br>expression<br>levels operations<br>gene<br>variations /<br>mutations<br><!-- End of picture text -->

3

### **_Example: Myriad -- and highly diverse -- genetic alterations (amplifications, deletions, mutations) across pancreatic tumors… (as well as in breast, colon, brain)_**


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Jones, Siân, Xiaosong Zhang, et al. "Core Signaling Pathways in Human Pancreatic Cancers Revealed by Global Genomic Analyses." _Science_ 321, no. 5897 (2008): 1801-6.

4

[Jones et al., <u>Science</u> (2008) ] !

### **_…but diverse mutations lead to dysregulation of a limited set of key pathways at protein level_**

- © American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Jones, Siân, Xiaosong Zhang, et al. "Core Signaling Pathways in Human Pancreatic Cancers Revealed by Global Genomic Analyses." _Science_ 321, no. 5897 (2008): 1801-6.

[Jones et al., <u>Science</u> (2008) ] !

5

### **_…but diverse mutations lead to dysregulation of a limited set of key pathways at protein level_**

- © American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Jones, Siân, Xiaosong Zhang, et al. "Core Signaling Pathways in Human Pancreatic Cancers Revealed by Global Genomic Analyses." _Science_ 321, no. 5897 (2008): 1801-6.

[Jones et al., <u>Science</u> (2008) ] !

6


**_Cell Signaling_** � **_Circuitry_** �

**Need to advance from** **<u>Metaphor</u>**


<!-- Start of picture text -->
to<br><!-- End of picture text -->

**<u>Model</u>**

- © Scientific American Library. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- Varmus, H., and R. A. Weinberg. "The Genetic Elements Governing Cancer: Tumor Suppressor Genes." _Genes and The Biology of Cancer_ (1993): 101-9.

**Varmus & Weinberg, Genes & the Biology of Cancer [1993]**

7

### **_Spectrum of Computational Modeling Methods_**

**SPECIFIED**

**ABSTRACTED**


<!-- Start of picture text -->
differential<br>equations<br><!-- End of picture text -->

**Boolean/fuzzy logic, decision trees Bayesian networks mutual** **_mechanisms_ information** **_logic_ regression, clustering** **_influences topology relationships_**

- **_prior knowledge_** � **_needed_**

8

### **_Pathway / Interactome Databases hold substantial prior knowledge_**

##### **_<u>Pathway Databases (Nodes)</u>_**

|**Database**|**Pathways**|**Relevant**|**No. Genes**|**Format**|
|---|---|---|---|---|
|GeneGO|700+|55|804|Table|
|PANTHER|165|14|1,025|SBML|
|CellMap (NetPATH)|20|12|625|BioPAX / SIF|
|Reactome|1081|4|173|BioPAX / SIF|
|NCI-PID|104|28|459|BioPAX / SIF|
|KEGG|1000+|8|564|-|
|**_SUMMARY_**||**_120_**|**_2,054_**||


##### **_Interactome Databases (Edges)_**

|**Database**|**Type**|**No. Edges**|**Graph type**|
|---|---|---|---|
|i2D v1.71|Protein-Protein (Exp)|11,327|Undirected|
|STRING|Integrated Text mining|35,033|Mixture|
|GeneGo|Curated|11,994|Directed, Signed|
|Cell Map|Curated|12,933|Mixture|
|NCI-PID|Curated|14,58|Mixture|
|Reactome|Curated|6,930|Mixture|
|**_SUMMARY_**||**_68,067_**|**_Mixture_**|


© Respective copyright holders. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

9

**_Pathway / Interactome Databases hold substantial_** � **_prior knowledge_** � **_for integrative analysis of multi-pathway network effects; but, there is need to move forward from illustration to prediction_** **_<u>Shortcomings:</u>_**

**_<u>Shortcomings:</u>_**


<!-- Start of picture text -->
EREG HBEGF<br>Node Source  ERBB4 •  Typically diverse with<br>≥ 2  respect to specificity and<br>GeneGo  context – i.e.,<br>KEGG<br>NCI-PID<br>cell type, genomic content,<br>NetPATH<br>and/or environmental<br>PANTHER<br>Reactome  conditions<br><!-- End of picture text -->

- **_Do not readily permit_**

- � **_input-output_** � **_calculation of network operating behavior, and thus difficult to relate to phenotype and/or interventions_**


<!-- Start of picture text -->
© source unknown. All rights reserved. This content is excluded from our Creative<br><!-- End of picture text -->


<!-- Start of picture text -->
Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->


- © Respective copyright holders. All rights reserved. This content is excluded from our Creative

10

Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

### **_<u>Central Goal:</u>_**

**_Establish methodology for converting from qualitative cell pathway topology_** � **_maps_** � **_to quantitatively computable network models_**

**_<u>Approach:</u>_**

**_Employ logic-based modeling framework, to train qualitative_** � **_prior knowledge_** � **_maps to quantitative empirical data for system context and multi-pathway comparisons of interest_**

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

11

**_More Detailed Insights from Stronger Modeling Analysis -- integrating empirical data with prior knowledge using network logic approach_**

**Generic Pathway Map (** **_e.g._ , Ingenuity) nodes (=compounds), signed directed edges (activation +, inhibition -)**

**Network Logic Model Boolean operators: AND / OR / NOT**


<!-- Start of picture text -->
A  B  C<br>�!<br>+  +  +<br>F<br>E<br>+<br>+<br>�! G<br>+<br><!-- End of picture text -->


<!-- Start of picture text -->
A  B  C<br>NOT<br>AND  AND<br>F<br>E  OR<br>NOT<br>G<br>S<br><!-- End of picture text -->

12

#### **_Example Study: Comparative Hepatocytic Cell Signaling Network Operation in Inflammation Context_**


<!-- Start of picture text -->
hepatocellular lines hepatocellular lines<br>Primary Hepatocytes  HepG2  Huh7  Hep3B  FocusFocus<br>[7 ligands +<br>control]<br>X [7 inhibitors<br>+ control]<br>X 17 signals<br>= ~ 1000<br>measurements<br>for each<br>cell-type and<br>time-point and<br>replicate<br><!-- End of picture text -->

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

13

#### **_Multi-Pathway Phosphoproteomic Data – primary human hepatocytes, HepG2 hepatocellular line_**


<!-- Start of picture text -->
TRANSIENT  LATE<br>NO RESPONSE  SUSTAINED<br><!-- End of picture text -->

###### **Time-points: 0, 30 min, 3 hrs**

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

###### **-- also cell death, proliferation index, and production of ~50 cytokines for each condition**

14

**_Example Database Pathway Map from literature curation, for network responses to our cytokine and growth factor treatments_**


<!-- Start of picture text -->
from  Ingenuity<br>supplemented by<br>some literature<br>knowledge for key<br>receptors<br>-- 82 nodes,<br>116 edges<br><!-- End of picture text -->

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

15

### **_Training Prior Pathway Map Knowledge on Context-Specific Empirical Signaling Data_**


<!-- Start of picture text -->
TNF EGF<br>EGF TNF<br>Define Pathway Map Perform  870<br>TNFR EGFR<br>from literature/Database Experiments<br>Ikb<br>PI3K<br>IKKab<br>0<br>Import Map Import Data<br>Ikb AKT<br>EGF TNF<br>1<br>TNF EGF Process Map Process Data Ikb<br>Compress & Remove non-observables<br>Normalize between 0,1<br>TNFR EGFR<br>Filter noise, saturation 0<br>Create Boolean Scaffold<br>IKKab PI3K DataRail EGF TNF<br>1<br>Ikb AKT Choose Submap  CellNetOptimizer Ikb<br>0<br>TNF EGF<br>AND OR Compare  TNF EGF<br>experiment - simulation<br>IKKab TNFR EGFR<br>Evaluate model<br>Ikb PI3K<br>Sum deviations + Size<br>OR<br>TNF EGF<br>X X X NO YES Analyze IKKab AKT<br>AND OR STOP?<br>resulting model<br>Ikb<br>IKKab<br>© source unknown. All rights reserved. This content is excluded from our Creative<br>Ikb<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br>Deviation<br><!-- End of picture text -->


<!-- Start of picture text -->
Automated Development of Logic Network Models<br>from Fit of Generic Pathway Map to Experimental Data<br>as an Optimization Problem<br>Objective  θ = θ f + α ⋅θ S<br>Function<br>Fit to data  Relative   Size of model<br>n<br>S M importance<br>θ S =  ν  kPk<br>θ f = ∑∑( BiklM − BiklE )2  Fit vs. Size  ∑<br>k =1<br>l =1  K =1  ∈ ∈ {0,1}{0,1} ∈ [0,1)<br><!-- End of picture text -->

         - © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

   - ! **minimize Objective Function (** **_θ)_ across model variants (P),**

      - ! **trading off model-data error and model size;**

   - ! α **ascertained by Pareto optimum for false-positive vs falsenegative trade-offs**

- ! **obtain family of best-fit models (within 1% of Objective Function optimum)**

17

### **_Automated Development of Logic Network Models from Fit of Generic Pathway Map to Experimental Data as an Optimization Problem_**

#### **Genetic Algorithm**

**1. Initialize a population of model variants (from Ingenuity scaffold or from random scaffolds)**

**2. Evaluate objective function (model-vs-data error plus modelsize penalty) for each individual in the population**

**3. Generate next generation of population using Elite Survival, Fitness Selection, Mutation, and Crossover**

**4. Assess whether stop criterion is fulfilled, or iterate back to step 2**

**5. Model pruning to reduce model size without detriment to model-vs-data error**

**6. 100 runs for each value of model-size penalty** α

18


### **_Illustration for HepG2 cell line_**

- **_improvement in data fit from best-fit original scaffold model_**

- **_to best-fit trained model_**

**Training data fit to ~9% error, substantially improved from original scaffold model fit of >45% error**

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see  http://ocw.mit.edu/help/faq-fair-use/.

19


**_Illustration for HepG2 cell line – consensus model from fit of empirical data to initial prior knowledge scaffold -- additional arcs needed to improve model fit, support in literature though not in prior knowledge scaffold -- arcs present in other cell line models but not in HepG2_**

Courtesy of EMBO and Nature Publishing Group. License: CC-BY-NC-SA.

Source: Saez `‐` Rodriguez, Julio, Leonidas G. Alexopoulos, et al. "Discrete Logic Modelling as a Means to Link Protein Signalling Networks with Functional Analysis of Mammalian Signal Transduction." _Molecular Systems Biology_ 5, no. 1 (2009).

20

---

[Up: contents](index.md) · [Model size is fairly insensitive to size penalty →](02-model-size-is-fairly-insensitive-to-size-penalty.md)

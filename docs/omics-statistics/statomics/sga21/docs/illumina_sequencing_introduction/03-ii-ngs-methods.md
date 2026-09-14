---
title: II. NGS Methods
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/illumina_sequencing_introduction.pdf
source_file: sources/statomics-sga21/docs/illumina_sequencing_introduction.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# II. NGS Methods

**Source:** [`docs/illumina_sequencing_introduction.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/illumina_sequencing_introduction.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

NGSplatformsenable a wide varietyofmethods, allowingresearcherstoask virtuallyanyquestionrelated tothe genome, transcriptome, orepigenome ofanyorganism. Sequencingmethodsdifferprimarilybyhow the DNAorRNAsamplesare obtained (eg, organism, tissue type, normalvs. affected, experimentalconditions, etc)and bythe data analysisoptions used. Afterthe sequencinglibrariesare prepared, the actualsequencingstage remainsfundamentallythe same, regardless ofthe method. There are variousstandard librarypreparationkitsthat offerprotocolsforwhole-genome sequencing(WGS), RNAsequencing(RNA-Seq), targeted sequencing(suchasexome sequencingor16Ssequencing), custom-selected regions, protein-bindingregions, and more. Althoughthe numberofNGSmethodsisconstantlygrowing, a briefoverview of the most commonmethodsispresented here.

### a. Genomics

#### Whole-Genome Sequencing

Microarray-based, genome-wide associationstudies(GWAS)have beena commonapproachforidentifyingdisease associationsacrossthe whole genome. While GWASmicroarrayscaninterrogate overfour millionmarkerspersample, the most comprehensive method ofinterrogatingthe 3.2 billionbasesofthe humangenome isWGS. The rapid drop in sequencingcost and the abilityofWGStoproduce large volumesofdata rapidlymake it a powerfultoolforgenomics research. While WGSiscommonlyassociated withsequencinghumangenomes, the scalable, flexible nature ofthe method makesit equallyusefulforsequencinganyspecies, suchasagriculturallyimportant livestock, plant genomes, ordiseaserelated microbialgenomes. Thisbroad utilitywasdemonstrated duringthe recent E. colioutbreak inEurope in2011, which prompted a rapid scientific response. Usingthe latest NGSsystems, researchersquicklysequenced the bacterialstrain, enablingthemtotrack the originsand transmissionofthe outbreak aswellasidentifygenetic mutationsconferringthe increased virulence.<sup>13</sup>

#### Exome Sequencing

Exome sequencingisa widely-used targeted sequencingmethod. The exome representslessthan2% ofthe human genome, but containsmost ofthe knowndisease-causingvariants, makingwhole-exome sequencing(WES)a costeffective alternative toWGS.<sup>14</sup> WithWES, the protein-codingportionofthe genome isselectivelycaptured and sequenced. It canefficientlyidentifyvariantsacrossa wide range ofapplications, includingpopulationgenetics, genetic disease, and cancerstudies.

> †With dual flow cell mode enabled.

For Research Use Only. Not for use in diagnostic procedures.

#### De novoSequencing

De novosequencingreferstosequencinga novelgenome where there isnoreference sequence available foralignment. Sequence readsare assembled ascontigsand the coverage qualityofde novosequence data dependsonthe size and continuityofthe contigs(ie, the numberofgapsinthe data). Anotherimportant factoringeneratinghigh-qualityde novo sequencesisthe diversityofinsert sizesincluded inthe library. Combiningshort-insert paired-end and long-insert mate pair sequencesisthe most powerfulapproachformaximalcoverage acrossthe genome (Figure 7). The combinationofinsert sizesenablesdetectionofthe widest range ofstructuralvariant typesand isessentialforaccuratelyidentifyingmore complex rearrangements. The short-insert reads, sequenced at higherdepths, canfillingapsnot covered bythe longinserts, which are oftensequenced at lowerread depths. Therefore, usinga combined approachresultsinhigherqualityassemblies. In parallelwithNGStechnologyimprovements, manyalgorithmic advanceshave emerged insequence assemblersforshortread data. Researcherscanperformhigh-qualityde novoassemblyusingNGSreadsand publiclyavailable short-read assemblytoolswithexistingcomputerresourcesinthe laboratory.


Figure 7: Mate Pairs and De novoAssembly —Using a combination of short and long insert sizes with paired-end sequencing results in maximal coverage of the genome for de novo assembly.

#### Targeted Sequencing

Withtargeted sequencing, a subset ofgenesorregionsofthe genome are isolated and sequenced. Targeted sequencing allowsresearcherstofocustime, expenses, and data analysisonspecific areasofinterest and enablessequencingat much highercoverage levels. Forexample, a typicalWGSstudyachievescoverage levelsof30–50× pergenome, while a targeted resequencingproject caneasilycoverthe target regionat 500–1000× orhigher. Thishighercoverage allowsresearchersto identifyrare variants, variantsthat would be toorare and tooexpensive toidentifywithWGSorCE-based sequencing.

Targeted sequencingpanelscanbe purchased withfixed, preselected content orcanbe customdesigned. Awide variety oftargeted sequencinglibraryprep kitsare available, includingkitswithprobe setsfocused onspecific areasofinterest such ascancer, cardiomyopathy, orautism. Customprobe setsare available throughDesignStudio™Software enabling researcherstotarget regionsofthe genome relevant tospecific researchinterests. Customtargeted sequencingisidealfor examininggenesinspecific pathways, orforfollow-up studiesfromGWASorWGS. Illumina currentlysupportstwomethods fortargeted sequencing, target enrichment and amplicongeneration(Figure 8).

Target enrichment capturesbetween10 kb–62 Mb regions, dependingonthe libraryprep kit parameters. Amplicon sequencingallowsresearcherstosequence 16–1536 targetsat a time, spanning2.4–652.8 kb oftotalcontent, depending onthe libraryprep kit used. Thishighlymultiplexed approachenablesa wide range ofapplicationsfordiscovery, validation, or screeningofgenetic variants. Ampliconsequencingisusefulfordiscoveryofrare somatic mutationsincomplexsamples(eg, canceroustumorsmixed withgermline DNA).<sup>15,16</sup> Anothercommonampliconapplicationissequencingthe bacterial 16S rRNAgene acrossmultiple species, a widelyused method forphylogenyand taxonomystudies, particularlyindiverse metagenomic samples.<sup>17</sup>


Formore informationonIllumina targeted, WGS, exome, orde novosequencingsolutions, visit www.illumina.com/applications/sequencing/dna_sequencing.html.

For Research Use Only. Not for use in diagnostic procedures.


Figure 8: Target Enrichment and Amplicon Generation Workflows —With target enrichment, specific regions of interest are captured by hybridization to biotinylated probes, then isolated by magnetic pulldown. Amplicon sequencing involves the amplification and purification of regions of interest using highly multiplexed PCR oligos sets.

For Research Use Only. Not for use in diagnostic procedures.

### b. Transcriptomics

LibrarypreparationmethodsforRNA-Seq typicallybeginwithtotalRNAsample preparationfollowed bya ribosome removal step. The totalRNAsample isthenconverted tocDNAbefore standard NGSlibrarypreparation. RNA-Seq focused on mRNA, smallRNA, noncodingRNA, ormicroRNAscanbe achieved byincludingadditionalisolationorenrichment steps before cDNAsynthesis(Figure 9).


Figure 9: A Complete View of Transcriptomics with NGS —A broad range of methods for transcriptomics with NGS have emerged over the past 10 years including total RNA-Seq, mRNA-Seq, small RNA-Seq, and targeted RNA-Seq.

#### Total RNA and mRNA Sequencing

Transcriptome sequencingisa majoradvance inthe studyofgene expressionbecause it allowsa snapshot ofthe whole transcriptome ratherthana predetermined subset ofgenes. Whole-transcriptome sequencingprovidesa comprehensive view ofa cellulartranscriptionalprofile at a givenbiologicalmoment and greatlyenhancesthe powerofRNAdiscovery methods. Aswithanysequencingmethod, analmost unlimited dynamic range allowsidentificationand quantificationofboth commonand rare transcripts. Additionalcapabilitiesinclude aligningsequencingreadsacrosssplice junctions, and detectionofisoforms, noveltranscripts, and gene fusions. Librarypreparationkitsthat support precise detectionofstrand orientationare available forbothtotalRNA-Seq and mRNA-Seq methods.

#### Targeted RNA Sequencing

Targeted RNAsequencingisa method formeasuringtranscriptsofinterest fordetectingdifferentialexpression, allelespecific expression, detectionofgene-fusions, isoforms, cSNPs, and splice junctions. Illumina TruSeq<sup>®</sup> Targeted RNA SequencingKitsinclude preconfigured, experimentallyvalidated panelsfocused onspecific cellularpathwaysordisease statessuchasapoptosis, cardiotoxicity, NFκB pathway, and more. Customcontent canbe designed and ordered for analysisofspecific genesofinterest. Targeted RNAsequencingisa powerfulmethod forthe investigationofspecific pathwaysofinterest orforthe validationofgene expressionmicroarrayorwhole-transcriptome sequencingresults.

#### Small RNA and Noncoding RNASequencing

Small, noncodingRNA, ormicroRNAsare short, 18–22 bp nucleotidesthat playa role inthe regulationofgene expression oftenasgene repressorsorsilencers. The studyofmicroRNAshasgrownastheirrole intranscriptionaland translational regulationhasbecome more evident.<sup>18,19</sup>


Formore informationregardingIllumina solutionsforsmallRNA(noncodingRNA), targeted RNA, totalRNA, and mRNAsequencing, visit www.illumina.com/applications/sequencing/rna.html.

For Research Use Only. Not for use in diagnostic procedures.

### c. Epigenomics

While genomicsinvolvesthe studyofheritable oracquired alterationsinthe DNAsequence, epigeneticsisthe studyof heritable changesingene activitycaused bymechanismsotherthanDNAsequence changes. Mechanismsofepigenetic activityinclude DNAmethylation, smallRNA–mediated regulation, DNA–proteininteractions, histone modification, and more.

#### Methylation Sequencing

Acriticalfocusinepigeneticsisthe studyofcytosine methylation(5mC)statesacrossspecific areasofregulation, suchas promotorsorheterochromatin. Cytosine methylationcansignificantlymodifytemporaland spatialgene expressionand chromatinremodeling.<sup>20</sup> While there are manymethodsforthe studyofgenetic methylation, methylationsequencing leveragesthe advantagesofNGStechnologyand genome-wide analysiswhile assessingmethylationstatesat the singlenucleotide level. Twomethylationsequencingmethodsare widelyused: whole-genome bisulfite sequencing(WGBS)and reduced representationbisulfite sequencing (RRBS). WithWGBS, sodiumbisulfite chemistryconvertsnonmethylated cytosinestouracils, whichare thenconverted tothyminesinthe sequence readsordata output. InRRBS, DNAisdigested withMspI, a restrictionenzyme unaffected bymethylationstatus. Fragmentsinthe 100–150 bp size range are isolated to enrichforCpG and promotorcontainingDNAregions. Sequencinglibrariesare thenconstructed usingthe standard NGS protocols.


Formore informationonmethylationsequencingsolutions, visit

www.illumina.com/techniques/sequencing/methylation-sequencing.html

#### ChIP Sequencing

Protein–DNAorprotein–RNAinteractionshave a significant impact onmanybiologicalprocessesand disease states. These interactionscanbe surveyed withNGSbycombiningchromatinimmunoprecipitation (ChIP)assaysand NGSmethods. ChIP-Seq protocolsbeginwiththe chromatinimmunoprecipitationstep (ChIPprotocolsvarywidelyastheymust be specific tothe species, tissue type, and experimentalconditions).


Formore informationonChIP-Seq, visit

www.illumina.com/techniques/sequencing/dna-sequencing/chip-seq.html.

#### Ribosome Profiling

Ribosome profilingisa method based ondeep sequencingofribosome protected–mRNAfragments. Purificationand sequencingofthese fragmentsprovidesa “snapshot” ofallthe ribosomesactive ina cellat a specific time point. This informationcandetermine what proteinsare beingactivelytranslated ina cell, and canbe usefulforinvestigatingtranslational control, measuringgene expression, determiningthe rate ofproteinsynthesis, orpredictingproteinabundance. Ribosome profilingenablessystematic monitoringofcellulartranslationprocessesand predictionofproteinabundance. Determining what regionsofa transcript are beingtranslated canhelp define the proteome ofcomplexorganisms. WithNGS, ribosome profilingallowsdetailed and accurate invivoanalysisofproteinproduction.


Tolearnmore about Illumina ribosome profiling, visit

www.illumina.com/applications/sequencing/rna.html.

For Research Use Only. Not for use in diagnostic procedures.

---

[← I. Welcome to Next-Generation Sequencing](02-i-welcome-to-next-generation-sequencing.md) · [Up: contents](index.md) · [III. Illumina DNA-to-Data NGS Solutions →](04-iii-illumina-dna-to-data-ngs-solutions.md)

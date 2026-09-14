---
title: 'Detectors: electron multiplier amplification'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/proteomics_data_analysis.pdf
source_file: sources/statomics-sga21/docs/proteomics_data_analysis.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Detectors: electron multiplier amplification

**Source:** [`docs/proteomics_data_analysis.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/proteomics_data_analysis.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
single ion in<br>40V<br>20V<br>80V<br>60V<br>120V<br>100V<br>10 6 electrons out<br><!-- End of picture text -->

Different variations of electron multiplier (EM) detectors are used, and these are the most common type of detector. An EM relies on several Faraday cup dynodes with increasing charges to produce an electron cascade from a few incident ions.


6

The primary principle in quantification is that detector signal relates to quantity


<!-- Start of picture text -->
Make each sample distinguishable<br>introduce mass differences between the samples<br>perform distinct experimental runs for each sample<br>Measure the intensity of the signal for each analyte in each sample<br>Statistically process the accumulated information<br>1/2 1/1 2/1<br><!-- End of picture text -->


Not all peptides ionise equally, so we cannot compare signal strength across peptides


<!-- Start of picture text -->
protein peptide MS1 signal<br><!-- End of picture text -->


7

As intensities become more extreme, the detector response starts to level off


Gevaert, Proteomics, 2007


At the same time, the measurement error increases as the ratio deviates from 1/1


<!-- Start of picture text -->
Vaudel, Proteomics, 2010<br><!-- End of picture text -->


8

And these effects remain quite visible, even on modern instruments (Orbitrap)


Raw data processing is somewhat imprecise, with expected errors on the order of 10%

Mass spectrometer specific processing required

Sets the dynamic range lower limit (S/N)

5-10% error in the final ratios due to peak-picker are often seen


<!-- Start of picture text -->
100,00%<br>80,00%<br>60,00%<br>40,00%<br>20,00%<br>0,00 %<br>117,09 117,095 117,1 117,105 117,11 117,115 117,12 117,125 117,13<br>m/z<br>Black: 0,02 Da<br>Blue: 0,04 Da<br>Red: 0,08 Da<br>Vaudel, Proteomics, 2010<br>Normalized intensity<br><!-- End of picture text -->


<!-- Start of picture text -->
30000<br>25000<br>20000<br>15000<br>10000<br>5000<br>0<br>503,73 503,74 503,75 503,76 503,77<br>m/z<br>Non-adapted shape -> +10% error<br>Intensity<br><!-- End of picture text -->


9

Different model options are available in tools or libraries for MS peak detection

Decon2LS


Vaudel, Proteomics, 2010


There’s actually more to a peak than just m/z


<!-- Start of picture text -->
OpenMS TOPPView<br>Vaudel, Proteomics, 2010<br><!-- End of picture text -->

10

Serum proteins are degraded over time, even with the best sampling tubes


<!-- Start of picture text -->
Yi, J Prot Res, 2007<br><!-- End of picture text -->


Our open modification search engine ionbot shows that modifications are also an issue

|**Protein name**|**Protein accession**|**Number of modifications**|
|---|---|---|
|Glyceraldehyde-3-phosphate dehydrogenase|P04406|166|
|Pyruvate kinase PKM|P14618|139|
|Fructose-bisphosphate aldolase A|P04075|122|
|Alpha-enolase|P06733|121|
|Triosephosphate isomerase|P60174|117|
|Phosphoglycerate kinase|P00558|111|


**_Mods found across all six proteins, between 50 and 278 distinct peptides_**

carbamyl, carbamidomethyl, formyl, acetyl, oxidation, methyl, thiazolidine, amidine, dehydrated, dicarbamidomethyl, dioxidation, succinyl, ammonia-loss, ethyl, carboxymethyl, guanidinyl, gg, cation:fe[iii]

https://ionbot.cloud Source data presented to ionbot from Kim _et al_ ., Nature, 2014


11

**Amino acids, peptides, and proteins Mass spectrometry basics**

**MS/MS spectra and identification**

**Database search algorithms in three phases Sequencial search algorithms Decoys and false discovery rate calculation Protein inference: bad, ugly, and not so good**


<!-- Start of picture text -->
Identification relies on fragmentation<br><!-- End of picture text -->


<!-- Start of picture text -->
source detector<br>ion selector fragment<br>mass analyzer<br>fragmentation<br><!-- End of picture text -->

Tandem-MS is accomplished by using two mass analyzers in series (tandem). A single ion trap can also perform tandem-MS. The first mass analyser performs the function of ion selector, by selectively allowing only ions of a given _m/z_ to pass through. The second mass analyzer is situated after fragmentation is triggered (see next slides) and is used in its normal capacity as a mass analyzer for the fragments.


12

Peptides subjected to fragmentation analysis can yield several types of fragment ions


<!-- Start of picture text -->
x3 y3 z3 x2 y2 z2 x1 y1 z1<br>R1 R2 R3 R4<br>NH2 C CO N C CO N C CO N C COOH<br>H H H H H H H<br>a1 b1 c1 a2 b2 c2 a3 b3 c3<br><!-- End of picture text -->

There are several other ion types that can be annotated, as well as ‘internal fragments’. The latter are fragments that no longer contain an intact terminus. These are harder to use for ‘ladder sequencing’, but can still be interpreted.


This nomenclature was coined by **Roepstorff and Fohlmann** _(Biomed. Mass Spec_ ., 1984) and **Klaus Biemann** _(Biomed. Environ. Mass Spec_ ., 1988) and is commonly referred to as ‘Biemann nomenclature’. Note the link with the Roman alphabet.

In an ideal world, the peptide sequence will produce directly interpretable ion ladders

# L E N N A R T


<!-- Start of picture text -->
intensity<br>LENNAR<br>RT<br>NART NNART<br>LEN LENNART<br>LENNA LENNART<br>ART<br>ENNART<br>T LENN<br>L<br>LE<br>L E N N A R T<br>m/z<br><!-- End of picture text -->

13

Real spectra usually look quite a bit worse, which introduces ambiguity in interpretation


<!-- Start of picture text -->
N<br>intensity<br>LE /EL N NA / AN<br>[EL] [AN]<br>[EI] [QG]<br>[E[IL]] [KG]<br>[QN]<br>[KN] NART<br>LEN<br>LENN A RT<br>LENNA LENNART<br>ART<br>T<br>LE<br>m/z<br><!-- End of picture text -->

**Amino acids, peptides, and proteins Mass spectrometry basics MS/MS spectra and identification Database search algorithms in three phases Sequencial search algorithms Decoys and false discovery rate calculation Protein inference: bad, ugly, and not so good**


14


<!-- Start of picture text -->
Database search engines match experimental<br>spectra to known peptide sequences<br>database  peptide seq. theoretical spectra peptide scores<br>1) YSFVATAER  34<br>in silico in silico scoring 2) YSFVSAIR     12<br>digest MS/MS function 3) FFLIGGGGK 12<br>…<br>protein inference<br>experimental spectra<br>Three popular algorithms illustrate<br>the three types of scoring systems<br>SEQUEST (UWashington, Thermo Fisher Scientific)<br>Intensity-based scoring system<br>MASCOT (Matrix Science) / Andromeda (Jürgen Cox)<br>Peak counting-based scoring system<br>X!Tandem (The Global Proteome Machine Organization)<br>Hybrid scoring system<br><!-- End of picture text -->

15


<!-- Start of picture text -->
SEQUEST is the original search engine,<br>and is based on ion intensity matching<br><!-- End of picture text -->


<!-- Start of picture text -->
Can be used for MS/MS (PFF) identifications<br>Based on a cross-correlation score (includes peak height)<br>Published core algorithm (patented, licensed to Thermo), Eng,  JASMS  1994<br>Provides preliminary (Sp) score, rank, cross-correlation score (XCorr),<br>and score difference between the top tow ranks (deltaCn, Cn)<br>Thresholding is up to the user, and is commonly done  per  charge state<br>Many extensions exist to perform a more automatic validation of results<br><!-- End of picture text -->


<!-- Start of picture text -->
The correlation score ( Ri ) is calculated<br>as the matched ion intensity<br>���<br>�𝑅𝑖<br>����<br>Int<br>R2<br>m/z<br>Int<br>� R1<br>m/z<br>𝑅� = �𝑥� �𝑦(���)<br>��� Int<br>R0<br>m/z<br>Int<br>R-1<br>m/z<br>Int<br>R-2<br>Eng, JASMS 1994 m/z<br>Yılmaz, Proteome Bioinformatics (MMB), Springer, 2017<br><!-- End of picture text -->

16

The cross-correlation score ( _Xcorr_ ) is _R0_ calibrated by the average random correlation


<!-- Start of picture text -->
���<br>XCorr = 𝑅� − 150 1 � 𝑅𝑖<br>����/��<br>Frequency<br>[R-75, R75]/R0 R0<br>correlation<br>score<br>Eng, JASMS 1994<br>Yılmaz, Proteome Bioinformatics (MMB), Springer, 2017<br><!-- End of picture text -->

The best theoretical match is then compared to the second-best theoretical match


<!-- Start of picture text -->
XCorr 1   XCorr  2<br>deltaCn =<br>XCorr 1<br>Int<br>Int<br>XCorr1 XCorr2<br>m/z<br>m/z<br>Eng, JASMS 1994<br>Yılmaz, Proteome Bioinformatics (MMB), Springer, 2017<br><!-- End of picture text -->

17

But the advent of high-throughput proteomics showed issues with user-defined thresholding


<!-- Start of picture text -->
MacCoss et al., Anal. Chem. 2002<br>Peng et al., J. Prot. Res.. 2002<br><!-- End of picture text -->

Mascot is an equally recognized search engine, but is based on peak counting

Very well established search engine, Perkins, _Electrophoresis_ 1999 Can do MS (PMF) and MS/MS (PFF) identifications Based on the MOWSE score, Unpublished core algorithm (trade secret) Predicts an _a priori_ threshold score that identifications need to pass From version 2.2, Mascot allows integrated decoy searches Provides rank, score, threshold and expectation value per identification Customizable confidence level for the threshold score


18


<!-- Start of picture text -->
Through Andromeda,<br>we understand MASCOT<br><!-- End of picture text -->


<!-- Start of picture text -->
n  = number of theoretical peaks<br>k  = number of matched peaks (within a given fragment tolerance)<br>p  = probability of finding a single, matched peak by chance<br>p is calculated by dividing the number of highest intensity peaks (q)<br>by a mass-window size (100 Da)<br>q  is limited by a maximum value, and is optimized for maximum  s<br>based on  peak counting  instead of intensity sums<br>Cox, J Prot Res, 2011<br>Yılmaz, Proteome Bioinformatics (MMB), Springer, 2017<br><!-- End of picture text -->

X!Tandem introduces a hybrid score, based on both peak counting and ion intensity


<!-- Start of picture text -->
A successful open source search engine, Craig and Beavis,  RCMS  2003<br>Can be used for MS/MS (PFF) identifications<br>Based on a hyperscore ( Pi  is either 0 or 1):  HyperScore  n Ii * Pi  * Nb !* Ny !<br> i  0 <br>Relies on a hypergeometric distribution (hence hyperscore)<br>Published core algorithm, and is freely available<br>Provides hyperscore and expectancy score (the discriminating one)<br>X!Tandem is fast and can handle modifications in an iterative fashion<br>Has rapidly gained popularity as (auxiliary) search engine<br><!-- End of picture text -->


19

X!Tandem’s significance calculation for scores can be seen as a general template


<!-- Start of picture text -->
60 4<br>3.5<br>50<br>3<br>40 2.5<br>30 2<br>1.5<br>20<br>1<br>10 0.5<br>0 0<br>0 20 40 60 80 100 20 25 30hyperscore35 40 45 50<br>hyperscore<br>6 significance<br>4 threshold<br>2<br>0<br>-2<br>-4<br>-6<br>-8 E-value=e -8.2<br>-10<br>0 20 40 60 80 100 Adapted from: Brian Searle, ProteomeSoftware,<br>hyperscore http://www.proteomesoftware.com/XTandem_edited.pdf<br># results<br>log(# results)<br>log(# results)<br><!-- End of picture text -->

The influence of various parameter changes on database size is clearly visible


<!-- Start of picture text -->
Verheggen, Mass Spec Reviews, 2017<br><!-- End of picture text -->


20

And the effect on identification rate is correspondingly obvious


<!-- Start of picture text -->
Verheggen, Mass Spec Reviews, 2017<br><!-- End of picture text -->


The main search engines in use are Mascot, Andromeda, SEQUEST and X!Tandem


<!-- Start of picture text -->
Verheggen, Mass Spec Reviews, 2017<br><!-- End of picture text -->


21

Among the up-and-coming engines, Comet, MS-GF+ and MS-Amanda are most notable


Verheggen, Mass Spec Reviews, 2017


SearchGUI makes it very easy for you to run multiple free search engines


<!-- Start of picture text -->
Vaudel, Proteomics, 2011<br><!-- End of picture text -->


22


<!-- Start of picture text -->
PeptideShaker is your gateway to the results<br><!-- End of picture text -->


Vaudel, Nature Biotechnology, 2015


**Amino acids, peptides, and proteins Mass spectrometry basics MS/MS spectra and identification Database search algorithms in three phases Sequencial search algorithms Decoys and false discovery rate calculation Protein inference: bad, ugly, and not so good**


23

_S_ equence tags are as old as SEQUEST, and still have a role to play today


<!-- Start of picture text -->
sequence tag<br>1079.61 - SD[IL] - 303.20<br>The concept of sequence tags was introduced by Mann and Wilm<br>Mann, Analytical Chemistry, 1994<br><!-- End of picture text -->

---

[← Mass resolution is an important characteristic for identification and quantification](02-mass-resolution-is-an-important-characteristic-for-identific.md) · [Up: contents](index.md) · [GutenTag, DirecTag, TagRecon →](04-gutentag-directag-tagrecon.md)

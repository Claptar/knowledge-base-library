---
title: GutenTag, DirecTag, TagRecon
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/proteomics_data_analysis.pdf
source_file: sources/statomics-sga21/docs/proteomics_data_analysis.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# GutenTag, DirecTag, TagRecon

**Source:** [`docs/proteomics_data_analysis.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/docs/proteomics_data_analysis.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
Tabb,  Anal. Chem.  2003, Tabb,  JPR  2008, Dasari,  JPR  2010<br>Recent implementations of the sequence tag approach<br>Refine hits by peak mapping in a second stage to resolve ambiguities<br>Rely on a empirical fragmentation model<br>Published core algorithms, DirecTag and TagRecon freely available<br>GutenTag/DirecTag extracts tags, TagRecon matches tags to database<br>Very useful to retrieve unexpected peptides (modifications, variations)<br>Entire workflows exist (e.g., combination with IDPicker)<br><!-- End of picture text -->


24

GutenTag: two stage, hybrid tag searching


<!-- Start of picture text -->
Tabb, Analytical Chemistry, 2003<br><!-- End of picture text -->


_De novo_ sequencing tries to read the entire peptide sequence from the spectrum


<!-- Start of picture text -->
Example of a manual de novo of an MS/MS spectrum<br>No more database necessary to extract a sequence!<br>Algorithms References<br>Lutefisk Dancik 1999, Taylor 2000<br>Sherenga Fernandez-de-Cossio 2000<br>PEAKS Ma 2003, Zhang 2004<br>PepNovo Frank 2005, Grossmann 2005<br>RapidNovor Ma 2015<br>… …<br><!-- End of picture text -->


25

**Amino acids, peptides, and proteins Mass spectrometry basics MS/MS spectra and identification Database search algorithms in three phases Sequencial search algorithms Decoys and false discovery rate calculation Protein inference: bad, ugly, and not so good**


<!-- Start of picture text -->
All hits, good and bad together,<br>form a distribution of scores<br>Nesvizhskii, J Proteomics, 2010<br><!-- End of picture text -->

26

If we know how scores for bad hits distribute, we can distinguish good from bad by score


The separation is not perfect, which leads to the calculation of a local false discovery rate


<!-- Start of picture text -->
local false discovery rate<br>(posterior error probability; PEP)<br><!-- End of picture text -->


27

Decoy databases are false positive factories, assumed to deliver representative bad hits


<!-- Start of picture text -->
Three main types of decoy DB’s are used:<br>- Reversed databases ( easy )<br>LENNARTMARTENS   SNETRAMTRANNEL<br>- Shuffled databases ( slightly more difficult )<br>LENNARTMARTENS   NMERLANATERTTN (for instance)<br>- Randomized databases ( as difficult as you want it to be )<br>LENNARTMARTENS   GFVLAEPHSEAITK (for instance)<br><!-- End of picture text -->


<!-- Start of picture text -->
The concept is that each peptide identified from the decoy database is an incorrect<br>identification. By counting the number of decoy hits, we can estimate the number of<br>false positives in the original database,  provided that the decoys have similar<br>properties as the forward sequences.<br><!-- End of picture text -->

With the help of the scores of decoy hits, we can assess the score distribution of bad hits


<!-- Start of picture text -->
local false discovery rate<br>(posterior error probability; PEP)<br>score<br>Käll, Journal of Proteome Research, 2008<br><!-- End of picture text -->

28

Setting a threshold classifies all hits as either bad or good, which inevitably leads to errors


<!-- Start of picture text -->
False Negative True Negative<br>False Positive<br>True Positive<br><!-- End of picture text -->

**Amino acids, peptides, and proteins Mass spectrometry basics MS/MS spectra and identification Database search algorithms in three phases Sequencial search algorithms Decoys and false discovery rate calculation Protein inference: bad, ugly, and not so good**


29


<!-- Start of picture text -->
Protein inference is a question of conviction<br>peptides a b c d<br>proteins<br>prot X x x<br>Minimal set prot Y x<br>Occam { prot Z x x x<br>peptides a b c d<br>proteins<br>prot X x x<br>Maximal set<br>prot Y x<br>anti-Occam { prot Z x x x<br>peptides  a b c d<br>proteins<br>prot X (-) x x<br>Minimal set with prot Y (+) x<br>maximal annotation { prot Z (0) x x x<br>true Occam?<br>Martens, Molecular Biosystems, 2007<br><!-- End of picture text -->


<!-- Start of picture text -->
The complexity of protein inference is<br>linked to the information ratio of a database<br><!-- End of picture text -->


<!-- Start of picture text -->
Tryptic cleavage, 1 allowed missed cleavage,<br>Mass limits from 600 to 4000 Da.<br>Barsnes, Amino Acids, 2013<br><!-- End of picture text -->


30

In real life, protein inference issues will be mainly bad, often ugly, and occasionally good


Protein inference can create issues in quantification due to degenerate peptides


_A nice example of the mess of degenerate peptides in quantification_


<!-- Start of picture text -->
Colaert, Proteomics, 2010<br><!-- End of picture text -->


31

---

[← Detectors: electron multiplier amplification](03-detectors-electron-multiplier-amplification.md) · [Up: contents](index.md)

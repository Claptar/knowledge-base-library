---
title: P3. Mutual information of protein residues (7 points).
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/04-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# P3. Mutual information of protein residues (7 points).

**Source:** `psets/04-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this problem, you will explore the mutual information of amino acid residues in a Multiple Sequence Alignment (MSA) of the Cys/Met metabolism PLP-dependent enzyme family (http://pfam.sanger.ac.uk/family/PF01053#tabview=tab0). Skeleton code is provided in mutual_info.py in Problem3.zip on Stellar. The full MSA, which you should use for all of your answers, is cys_met.fasta. However, we have also provided you with a smaller file containing the first ~1000 lines of the MSA (which you can use when developing and testing your code to cut down on the run-time) as cys_met_shortened.fasta.

**(A – 2 points)** Open mutual_info.py and scan to the bottom (after

if __name__ == "__main__":) to get a feeling for what functions are executed and what each function returns.

First, we’ll calculate the information content at each position of the alignment. What is maximum information possible at one position (in bits), and what is the formula for information that you will implement?

Maximum information possible: 4.32 bits. There are 20 possible states (amino acids) – the maximum Shannon entropy (which is also the maximum information possible - realized if only one state occurs with probability 1 and the other 19 with probability 0) is log2(20)≈4.32 bits.

Formula for information at a position: 4.32 + ��aa=l<sup>P</sup> aa<sup>log</sup> 2<sup>P</sup> aa<sup>, where P</sup> aa<sup>is the probability of</sup> amino acid aa.

Now, complete the part_A_get_information_content() function in mutual_info.py, and plot the information content at each position (see the code for more specific details). The code can be run with the following command:

python mutual_info.py cys_met.fasta

What is the maximum information content, and what is the first position at which this maximum information is attained?

The maximum information content at any position is 4.318 bits, and it is attained at position 1658 (well-represented position 367).

If you have matplotlib installed (you also can upload your code to Athena, which has matplotlib installed), you can uncomment

plot_info_content_list(info_content_list), which will make 2 plots of the information content at each position (one relative to the original MSA positions and a condensed version relative to the well-represented position numbers); otherwise, make a plot of the information content at each position with a tool of your choice. Upload one of the 2 plots (or your own custom one) to the Stellar electronic dropbox or include a printout of it with your write-up.

15


<!-- Start of picture text -->
Information scatterplot<br>4.32<br>3.92<br>4<br>3.53<br>3.14<br>3<br>2.74<br>2.35<br>2<br>1.96<br>1.56<br>1 1.17<br>0.78<br>0 0.38<br>0 50 100 150 200 250 300 350<br>Well-represented Position<br>Information scatterplot<br>4.32<br>3.92<br>4<br>3.53<br>3.14<br>3<br>2.74<br>2.35<br>2<br>1.96<br>1.56<br>1 1.17<br>0.78<br>0 0.38<br>0 200 400 600 800 1000 1200 1400 1600<br>Original MSA Position<br>Information<br>Information<br><!-- End of picture text -->

16

**(B – 3 points)** Now let’s calculate the mutual information between all pairs of wellrepresented positions in the alignment. Complete the function

get_MI_at_pairs_of_positions() to get the mutual information at each pair of positions, and plot the mutual information at each pair of positions (if you have matplotlib installed, you can uncomment the

plot_mutual_information_dict(mutual_information_dict) function provided to make 2 heatmap plots, one relative to the original MSA positions, and a condensed one relative to the “well-represented” position number).

What is the maximum mutual information, and at what pair of positions is this value achieved? Upload the heatmap plot with the well-represented positions to the Stellar Problem Set 4 electronic dropbox or include a printout of it with your write-up.

The maximum mutual information is 1.212, and it is attained between positions (339, 1131) of the original MSA (well-represented position #s (50, 229)).

The condensed heatmap of mutual information for position pairs indexed relative to the “well­ represented positions”:


<!-- Start of picture text -->
Mutual information heatmap<br>1.21<br>350<br>1.09<br>0.97<br>300<br>0.85<br>250<br>0.73<br>200<br>0.61<br>0.48<br>150<br>0.36<br>100<br>0.24<br>50<br>0.12<br>0 0.00<br>0 50 100 150 200 250 300 350<br>Well-represented Position 1<br>Well-representedPosition2<br><!-- End of picture text -->

17

The heatmap of mutual information for position pairs indexed relative to positions in the original multiple sequence alignment:


<!-- Start of picture text -->
Mutual information heatmap<br>1.21<br>1600<br>1.09<br>1400<br>0.97<br>1200 0.85<br>0.73<br>1000<br>0.61<br>800<br>0.48<br>600 0.36<br>0.24<br>400<br>0.12<br>200<br>0.00<br>200 400 600 800 1000 1200 1400 1600<br>Original MSA Position 1<br>OriginalMSAPosition2<br><!-- End of picture text -->

18

**(C – 2 points)** Now’s lets see if we can make sense of why the positions with the highest mutual information are as such. Complete the function

part_c_get_highest_MI_block_of_10() to find the 10 consecutive well-represented positions with the highest average mutual information. If your function is implemented successfully, the code will subsequently print out the human sequence (including gaps and intervening non-well-represented positions) corresponding to this block. What is it?

N---R--L-R--F--L--Q--------------------------------------------------------------N-SL

The human entry (CGL_HUMAN/19-395) in the multiple sequence alignment cys_met.fasta corresponds to 1QGN (Figures 1-5) in the paper “New methods to measure residues coevolution in proteins” by Gao et al. BMC Bioinformatics 2011, **12** :206 (http://www.biomedcentral.com/content/pdf/1471-2105-12-206.pdf). By matching the printedout, gapped sequence in the MSA human entry to the ungapped human sequence (Isoform 1 of http://www.uniprot.org/uniprot/P32929), determine which positions of the human protein correspond to the highest MI block. Are these positions in any of the figures from the paper? Based on the structure of the enzyme, why would you expect these positions to have high mutual information?

As a reminder, be sure that your final answers are for cys_met.fasta (not cys_met_shortened.fasta).

By matching the “NRLRFLQNSL” residues with the Uniprot ungapped human sequence, we see that these are residues 234-243. In particular, the first “L” corresponds to human protein residue 236, which is the red residue in Figure 4 of the Gao et al. paper. The structure in that figure shows that residue 236 is close proximity to many other residues in the tertiary structure. Thus, if residue 236 mutates, we expect compensatory changes in the nearby residues to accommodate the new geometry of the site, explaining why residue 236 covaries and has high mutual information with others nearby in the protein.

19

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology

Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Energy of Metropolis Algorithm, kT=53782](07-energy-of-metropolis-algorithm-kt-53782.md) · [Up: contents](index.md)

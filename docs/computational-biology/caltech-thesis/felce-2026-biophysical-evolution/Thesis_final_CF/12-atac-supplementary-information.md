---
title: ATAC SUPPLEMENTARY INFORMATION
source: https://thesis.library.caltech.edu/17880/
source_file: sources/felce-2026-biophysical-evolution/Thesis_final_CF.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# ATAC SUPPLEMENTARY INFORMATION

**Source:** `Thesis_final_CF.pdf` from [felce-2026-biophysical-evolution](https://thesis.library.caltech.edu/17880/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **A.1 Site Inhomogeneity**

We consider the mean chromatin openness values at each ATAC-seq peak site within the six-site loci we selected from each dataset. For a single ATAC-seq peak region _𝑥_ , we have a mean openness value, ⟨ _𝑥_ ⟩, given by:


where _𝑁𝑐_ is the number of cells in the dataset, and _𝑥𝑖_ denotes the openess value (0 or 1) of the chromatin measured at site _𝑥_ in cell _𝑖_ .

Figures A.1-A.3 show the mean site openness values at each site, within each locus, for all three datasets. These results indicate that, even within a single six-site locus, different ATAC-seq peak regions have significantly different average openness measurements.

### **A.2 Transition Matrix Generalization**

The transition matrix given for a two-gene system in the main text can be extended naturally to a gene locus with an arbitrary number of chromatin sites. We allow transitions only to states which are accessible from the current state by changing the openness value of a single site, with transition rates _𝑘_ o _𝑛,𝑖_ for site _𝑖_ , and _𝑘_ o _𝑓𝑓_ for all sites. To express the preference for aligned adjacent site cooperation, we multiply these transition rates by a factor of _𝜖_<sup>−</sup><sup>_𝑛_m</sup><sup>_𝑖𝑠_</sup> , where _𝑛_ m _𝑖𝑠_ represents the number of ‘misaligned’ adjacent gene pairs in the current state.

For example, a DNA locus with three adjacent chromatin sites, and the chromatinstate basis given in the state matrix, _𝑆_ , of Equation 2.29, would have the following chromatin-state transition matrix, _𝐻_ :

105


<!-- Start of picture text -->
0.8 1:25028504-25036643 1:30743207-30761867 1:145983069-146000218<br>0.6<br>0.4<br>0.2<br>0.0<br>0.8 1:154997426-155013274 10:69043845-69054726 11:67400339-67415716<br>0.6<br>0.4<br>0.2<br>0.0<br>0.8 12:6942980-6959950 12:122871161-122881442 12:123442812-123452591<br>0.6<br>0.4<br>0.2<br>0.0<br>0.8 13:99214272-99224403 14:103332058-103345829 15:63494909-63508612<br>0.6<br>0.4<br>0.2<br>0.0<br>0.8 16:17341686-17350658 17:58317153-58342599 18:77059667-77072738<br>0.6<br>0.4<br>0.2<br>0.0<br>0.8 19:1257621-1273894 19:2079885-2093092 19:14400888-14417383<br>0.6<br>0.4<br>0.2<br>0.0<br>0.8 19:14505302-14520514 2:207498455-207506138 3:71485753-71494710<br>0.6<br>0.4<br>0.2<br>0.0<br>0.8 3:111538813-111547156 4:38661545-38676163 6:136782339-136790129<br>0.6<br>0.4<br>0.2<br>0.0<br>0.8 7:50302133-50316776 7:158809395-158820068 9:73147538-73156846<br>0.6<br>0.4<br>0.2<br>0.0<br>0.8 9:92961693-92971408 9:93031575-93043792 X:119681908-119694232<br>0.6<br>0.4<br>0.2<br>0.0<br>1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6<br>Site Index Within Each Locus<br>Mean Openness of Each Site Across Cells<br><!-- End of picture text -->

Figure A.1: The mean chromatin openness for the six adjacent ATAC-seq peak sites at each of the 30 loci from the PBMC dataset.

106


<!-- Start of picture text -->
0.4 h1:24920478-24933424 h16:84597423-84606983 h17:46138409-46146960<br>0.3<br>0.2<br>0.1<br>0.0<br>0.4 h22:41935274-41948163 h4:112279148-112288953 h6:389478-402258<br>0.3<br>0.2<br>0.1<br>0.0<br>0.4 h9:131724747-131739897 m4:132071452-132082226 m6:47627213-47654930<br>0.3<br>0.2<br>0.1<br>0.0<br>0.4 1 2m6:108801688-1088152803 4 5 6 1 2 m7:15930224-159461503 4 5 6 1 2m8:124126700-1241412463 4 5 6<br>0.3<br>0.2<br>0.1<br>0.0<br>0.4 m8:127307518-1273203231 2 3 4 5 m9:32606386-326200706<br>0.3<br>0.2<br>0.1<br>0.0<br>1 2 3 4 5 6 1 2 3 4 5 6<br>Site Index Within Each Locus<br>Mean Openness of Each Site Across Cells<br><!-- End of picture text -->

Figure A.2: The mean chromatin openness for the six adjacent ATAC-seq peak sites at each of the 14 loci from the human-mouse mixture dataset.

||<br><br><br>|�<br>−Σ000|_𝑘_on_,_1|_𝑘_on_,_2|_𝑘_on_,_3|0|0|0|0<br>|�|
|---|---|---|---|---|---|---|---|---|---|---|
||<br>1<br>_𝜖_<sup>−1</sup><br>_𝜖_<sup>−2</sup><br><br>|�����<br>_𝑘_off<br>_𝑘_off|−Σ100<br>0|0<br>−Σ010|0<br>0|_𝑘_on_,_2<br>_𝑘_on_,_1|_𝑘_on_,_3<br>0|0<br>_𝑘_on_,_3|0<br>0<br>|������|
|dia|<br>_𝜖_<sup>−1</sup><br><br>|��<br>_𝑘_off|0|0|−Σ001|0|_𝑘_on_,_1|_𝑘_on_,_2|0<br>|���|
|g|<br>_𝜖_<sup>−1</sup><br><br><br>|��<br>0|_𝑘_off|_𝑘_off|0|−Σ110|0|0|_𝑘_on_,_3<br>|���<br>,|
||<br>_𝜖_<sup>−2</sup><br><sup>−1</sup><br><br>|���<br>0|_𝑘_off|0|_𝑘_off|0|−Σ101|0|_𝑘_on_,_2<br>|���|
||<br>_𝜖_<br>1<br><br>|���<br>0|0|_𝑘_off|_𝑘_off|0|0|−Σ011|_𝑘_on_,_1<br>|���|
||<br><br><br>|�<br>0|0|0|0|_𝑘_off|_𝑘_off|_𝑘_off|−Σ111<br><br><br>|�<br>(A.2)|


107


<!-- Start of picture text -->
1:172134032-172157528 11:120119474-120131466 13:83802715-83809701<br>0.6<br>0.4<br>0.2<br>0.0<br>15:27783188-27795411 15:85551572-85565581 7:101099140-101110619<br>0.6<br>0.4<br>0.2<br>0.0<br>1 2 3 4 5 6 9:43990069-44006338 1 2 3 4 5 6<br>0.6<br>0.4<br>0.2<br>0.0<br>1 2 3 4 5 6<br>Site Index Within Each Locus<br>Mean Openness Across Cells<br><!-- End of picture text -->

Figure A.3: The mean chromatin openness for the six adjacent ATAC-seq peak sites at each of the 7 loci from the mouse cortex dataset.

where Σ _𝛼_ is the decay rate of state _𝛼_ , and is equal to the sum of the remaining values in the row (Σ000 = _𝑘_ o _𝑛,_ 3+ _𝑘_ o _𝑛,_ 2+ _𝑘_ o _𝑛,_ 1, Σ001 = _𝑘_ o _𝑓𝑓_ + _𝑘_ o _𝑛,_ 2+ _𝑘_ o _𝑛,_ 1, etc.), such that each row sums to zero. The first matrix is the diagonal of a vector _𝜖_ ˜, where each entry _𝜖_ ˜ _𝛼_ is equal to _𝜖_<sup>−</sup><sup>_𝑛_m</sup><sup>_𝑖𝑠_</sup> , where _𝑛_ m _𝑖𝑠_ is the number of opposite openness adjacent chromatin sites in state _𝛼_ . This generalization allows biophysical gene-state switching between similar configurations, at rates which encode the preference of neighboring DNA regions to have the same openness value, and can be extended straightforwardly to loci of arbitrary length.

### **A.3 RNA Transcript Count Moments**

To find moments concerning the _𝑖_<sup>t</sup><sup>_ℎ_</sup> species, we differentiate Equation 2.9 with respect to _𝑧_<sup>_𝑖_</sup> . This allows us to find conditional means, _𝜇_ ˜<sup>_𝑖_</sup> _𝛼_<sup>,whichrepresentthe</sup> expected number of transcripts of species _𝑖_ , given that the system is in chromatinstate _𝛼_ . From the definition of _𝐺𝛼_ given in Equation 2.8, we note that:


where P _𝛼_ is defined to be the probability that the system is in chromatin-state _𝛼_ . We define the vector **P** to be the vector with the P _𝛼_ as compenents. Noting that

108

**_G_** = **P** for **_z_** = **1** , setting the LHS of Equation 2.9 to zero and taking a derivative with respect to _𝑧_<sup>_𝑖_</sup> , we reach steady-state conditional means given by:


where Π<sup>ˆ</sup> is the diagonal matrix of **_π_** , and _𝐵_<sup>ˆ</sup> _𝑖_ is the diagonal matrix of the _𝑖_<sup>t</sup><sup>_ℎ_</sup> column of B. For our model of transcription, in index notation, this becomes:


where no summation over _𝛼_ is implied. **_µ_ ˜**<sup>**_i_**</sup> is the vector whose components _𝛼_ are defined in Equation A.3.

For the unconditional means, _𝜇_<sup>_𝑖_</sup> =<sup>�</sup> _𝛼_<sup>Πˆ˜</sup><sup>_𝜇𝑖_</sup> _𝛼_<sup>, we find:</sup>


where, for ease of this and future calculations, we define:


We also make use of the Neumann series approximation for the matrix inverse, for a matrix _𝐻_<sup>˜</sup> with spectral radius less than one:


where for our purposes we define _𝐻_<sup>˜</sup> via:


109

for a scalar, _𝑑_<sup>_𝑖_</sup> . Then, if the spectral radius of _𝐻_<sup>_𝑇_</sup> / _𝑑_<sup>_𝑖_</sup> _<_ 1, we have:


Recalling the symmetry of _𝐻_<sup>_𝑇_</sup> and hence _𝐻_<sup>˜</sup> , we have:


Inserting the Neumann expansion for _𝑀_<sup>_𝑖_</sup> in Equation A.6, and using the symmetry in Equation A.11, we see that:


For correlations between species, we use the equation:


noting that here and in what follows, we require _𝑖_ ≠ _𝑗_ . Differentiating Equation 2.9 twice, we get, in steady state:


where ( ˜ _𝜇_<sup>_𝑖𝑗_</sup> ) _𝛼_ = ⟨ _𝑚_<sup>_𝑖_</sup> _𝑚_<sup>_𝑗_</sup> ⟩ _𝛼_ is the conditional expectation of the product of transcripts i and j given gene state _𝛼_ .

Solving for the mean product vector over gene states, we get:


110

Convolving this with the steady-state probability distribution for states, we can find the unconditional expectation value of the product of two genes. Subtracting the product of the means of each gene, we arrive at the correlation between the two gene counts.

The unconditional mean product is given by:


with _𝑀_<sup>_𝑖𝑗_</sup> as defined above (A.7).

Converting into index notation and using the relation between B and S (A.5), we find:


Using another symmetry argument related to A.11 (see Appendix A.3), this is always equivalent to:


Note that, since to zeroth order in _𝐻_<sup>˜</sup> , (i.e. in the limit of very slow switching, _𝑘_ o _𝑓𝑓 , 𝑘_ o _𝑛_ ≪ _𝑑_<sup>_𝑖_</sup> _, 𝑑_<sup>_𝑗_</sup> and _𝜖_ not too small), we have:


giving, to zeroth order in _𝐻_<sup>˜</sup> :

111


as expected.

From Equation A.16 and the expansion of _𝑀_<sup>_𝑖_</sup> , in the case of bounded _𝐻_<sup>˜</sup> we have the exact expression for the covariance:


If _𝐻_<sup>˜</sup> is not bounded, the series will not converge and we need to return to the expression in Equation A.17.

Note that, due to the structure of _𝐻_<sup>˜</sup> , the first-order term in _𝐻_<sup>˜</sup> always evaluates to zero (see Appendix A.11). We also show that both terms in the sum are identical, except for factors of _𝑑_<sup>_𝑖,𝑗_</sup> , giving:


Again, we see that for switching which is slow compared to the RNA decay rates, i.e. _𝐻<<_ ˜ _𝐼_ for all entries of the matrix, Cov( _𝑚_<sup>_𝑖_</sup> _𝑚_<sup>_𝑗_</sup> ) ∼ _𝑑_<sup>_<u>𝑏𝑖𝑖𝑏</u>_</sup> _𝑑_<sup>_𝑗𝑗_Cov(</sup><sup>_𝜎𝑖𝜎𝑗_),asex-</sup> pected. Following the procedure above, we now consider the variance of transcript _𝑖_ . Defining _𝜇_ ˜ ≡ _𝜇_<sup>_𝑖_</sup> −( _𝜇_<sup>_𝑖_</sup> )<sup>2</sup> , we have:


112

where we have defined matrix _𝑀_<sup>[2</sup><sup>_𝑖_]</sup> via _𝑀_<sup>[2</sup><sup>_𝑖_]</sup> ≡(2 _𝑑_<sup>_𝑖_</sup> _𝐼_ − _𝐻_<sup>_𝑇_</sup> )<sup>−1</sup> , and used the explicit decompositions of _𝐵_<sup>ˆ</sup> and Π<sup>ˆ</sup> . For the third equality we have used the argument in section A.3, to give the relation:


For the case of bounded _𝐻_<sup>˜</sup> , this becomes:


### **A.4 Correlation Propagation**

We define site-site correlations for accessibility and transcript count respectively via:


We define f, the ratio between these quantities via:


Returning to matrix notation, and dropping the assumption of bounded _𝐻_<sup>˜</sup> , we recall the transcript covariances and variances:


113


Compare these with the gene-state covariances and variances:


where the variance is obtained by setting _𝑖_ = _𝑗_ in this expression. An expression for f is obtained by taking the appropriate ratios of these moments:


We show the value of f for a two-gene system with varying _𝑘_ o _𝑛,_ 1 _, 𝑘_ o _𝑛,_ 2 and two sets of remaining parameters in Figure A.4. The other parameters are: _𝑏_ 1 = _𝑏_ 2 = 10 _, 𝑑_ 1 = _𝑑_ 2 = 1, and _𝜖_ = 0 _._ 7 _, 𝑘_ o _𝑓𝑓_ = 30; _𝜖_ = 0 _._ 5 _, 𝑘_ o _𝑓𝑓_ = 0 _._ 5 for the left and right panels respectively.

Since RNA counts are downstream of chromatin dynamics and add an additional layer of stochasticity, we might expect that f would be constrained within the range: 0 _< 𝑓<_ 1. Whilst the left panel in Figure A.4 shows a parameter regime where this constraint is observed, the right panel provides an example where _𝑓>_ 1. The intuition behind this surprising result is explored further in section A.5.

### **A.5 Illustrative Toy Systems**

Here we consider illustrative toy systems where the fraction, f, of transcript correlation to gene-state correlation, falls outside of the naively expected range, 0 _< 𝑓<_ 1. To emphasize how this can be achieved, we demonstrate the behavior of two different two-gene systems.

114


Figure A.4: Ratio, _𝑓_ , between gene-gene correlations at the transcript and at the chromatin level, calculated for different values of _𝑘_ o _𝑛,_ 1 _, 𝑘_ o _𝑛,_ 2 in a two-gene system. The other parameters are, **Top:** _𝜖_ = 0 _._ 7, _𝑘_ o _𝑓𝑓_ = 30, _𝑏_ 1 = _𝑏_ 2 = 10, _𝑑_ 1 = _𝑑_ 2 = 1; **Bottom:** _𝜖_ = 0 _._ 5, _𝑘_ o _𝑓𝑓_ = 0 _._ 5, _𝑏_ 1 = _𝑏_ 2 = 10, _𝑑_ 1 = _𝑑_ 2 = 1.

115


Figure A.5: Simple toy systems for which the value of _𝑓_ falls outside of the naively expected range. The states ( _𝑖, 𝑗_ ) correspond to the openness of sites _𝑖_ and _𝑗_ in that state, where 0 _,_ 1 indicate closed and open chromatin respectively. The arrows between chromatin states represent allowed transitions, and their weights correspond to the rates of these transitions. **Left:** A system with | _𝑓_ | _>_ 1. **Right:** A system with _𝑓<_ 0, i.e. reversed correlations between the transcript and chromatin-state levels.

The first system, although un-biological (including instantaneous changes of two genes at the same time), shows how Markov state transitions combined with constitutive transcript production can give transcript correlations without any correlations in the underlying chromatin openness. This corresponds to an infinite value of | _𝑓_ |.

The chromatin-state structure of this imagined system is shown in the left panel of Figure A.5, where the chromatin-states are labeled ( _𝑖, 𝑗_ ), for _𝑖, 𝑗_ = 0 _,_ 1 depending on the openness of each of the two chromatin sites. The arrows in the diagram represent transitions between chromatin configurations, and their weight represents the rate of each transition.

We could encode such a system using the following transition matrix:


with _𝛿<_ 1, which has a uniform stationary distribution. However, due to the structure of the graph in Figure A.5, whilst there is no correlation between the openness of genes 0 and 1 in the steady state, there is clearly a correlation between their time averaged histories. This is because, if, for instance, gene 1 is on, that

116

indicates that the system is in the lower half of the state graph diagram, making it more likely that it has also been in the lower half for its recent history. This means that knowing that gene 1 is on increases the probability that gene 2 has been on in the system’s recent history. In our gene model, this corresponds to a correlation between transcript numbers, despite there being no correlation between the openness of genes 1 and 2 in steady state. The correlations resulting from simulations of this system are shown on the top row of Figure A.6. Whilst correlations between transcripts are always significant and positive, the correlations between sites are around zero, resulting in _𝑓_ values with large magnitude.

The second example system, (no longer including un-biological transitions), has reversed sign correlations (i.e. _𝑓<_ 0). We consider chromatin-state evolution defined by the transition matrix:


for _𝛿<_ 1 _, 𝜒>_ 1, and illustrated in the right hand panel of Figure A.5. The correlations observed for such a system from simulations are shown in the bottom row of Figure A.6. Whilst the correlations between transcripts are significant and positive as in the previous example, due to slow transitions from the (0 _,_ 0) state, there is a negative correlation between site openness values, due to the relative stability of the (1 _,_ 0) and (0 _,_ 1) states.

### **A.6 Noise**

We consider binomial dropout with probability _𝑝_ d _𝑟𝑜𝑝_ applied independently at each site in a locus. Figure A.7 shows how this affects various distributions over three-site configurations in the Ising-like model we have described. In the case of uncorrelated (including uniformly distributed) sites, the binomial dropout effects all configurations with the same total number of open sites equally. However, for the case of correlated neighbors, ( _𝜖<_ 1), the effect of dropout varies even between configurations with the same total number of open sites. For example, between _𝑝_ d _𝑟𝑜𝑝_ = 0 _._ 1 and _𝑝_ d _𝑟𝑜𝑝_ = 0 _._ 5, the probability of the (0 _,_ 1 _,_ 0) configuration is reduced less than the (0 _,_ 0 _,_ 1) and (1 _,_ 0 _,_ 0) configurations. This is because the (0 _,_ 1 _,_ 0) configura-

117


<!-- Start of picture text -->
20<br>0.26<br>10<br>0.25<br>0<br>0.24<br>10<br>0.23<br>20<br>-0.03 -0.02 -0.01 0.00 0.01 0.02 -0.03 -0.02 -0.01 0.00 0.01 0.02<br>Site Openness Correlations Site Openness Correlations<br>1<br>0.12<br>2<br>0.11<br>3<br>0.10<br>4<br>0.09<br>5<br>0.08<br>6<br>0.07<br>7<br>-0.07 -0.06 -0.05 -0.04 -0.03 -0.02 -0.01 0.00 -0.07 -0.06 -0.05 -0.04 -0.03 -0.02 -0.01 0.00<br>Site Openness Correlations Site Openness Correlations<br>Correlation Fraction, f<br>Transcript Number Correlations<br>Correlation Fraction, f<br>Transcript Number Correlations<br><!-- End of picture text -->

Figure A.6: Correlations for simulated toy systems, with analytic solutions shown as dotted lines. **Left** : Transcript correlations versus site openness correlations. **Right:** Correlation ratio, f, versus site openness correlations. **Top:** First toy system described, with | _𝑓_ | _>_ 1. **Bottom:** Second toy system described, with _𝑓<_ 0. The parameters used were: _𝛿_ = 0 _._ 1 _, 𝜒_ = 1 _._ 2 _, 𝑘_ = 1 _, 𝑏_ 1 = _𝑏_ 2 = 2 _, 𝑑_ 1 = _𝑑_ 2 = 0 _._ 5, and results shown are for 5,000 simulated cells.

tion ‘receives’ probability from both the (1 _,_ 1 _,_ 0) and (0 _,_ 1 _,_ 1) configurations under dropout, which are favored by a factor 1/ _𝜖_ compared to the (1 _,_ 0 _,_ 1) configuration.

### **A.7 Model Fitting**

Fits at the first 5 loci in dataset 1 are included in Figure A.8. The models are as described in the main text, and the parameters were fitted using Python’s `differential_evolution` package. The algorithm was run 10 times per locus per model, to verify that the method converged closely to the same parameters each time. We also fit a locus from the 10x PBMC data using MCMC (see Figure A.9). The parameters found by the `differential_evolution` algorithm matched the most

118


Figure A.7: The effect of binomial dropout on various three-site distributions. **Top:** Uniform distribution. **Middle:** Distribution from Ising model transition matrix with independent sites. Parameters: _𝑘_ o _𝑛_ = 1 for all sites, _𝑘_ o _𝑓𝑓_ = 1 _._ 5, _𝜖_ = 1. **Bottom:** Distribution from Ising model transition matrix with correlated adjacent sites. Parameters: _𝑘_ o _𝑛_ = 1 for all sites, _𝑘_ o _𝑓𝑓_ = 1 _._ 5, _𝜖_ = 0 _._ 5.

119

likely values from the MCMC results. The Bayesian Information Criteria (BIC) for the fits at each locus are shown in the main text. The BIC is defined as:


where _𝑘_ is the number of parameters in the model, _𝑛_ is the number of data-points, and _𝐿_<sup>ˆ</sup> is the likelihood of the data under the fitted parameters.

### **A.8 snATAK Input**

For pre-processing using snATAK, we used the technology string (argument option -x): `0,0,0:-1,0,0:1,0,0,2,0,0` , where files 0, 1, and 2 correspond to the R2, R1, and R3 FASTQ files respectively. This technology string indicates that the cell barcodes are found in the R2 file, that there are no UMIs for these ATAC-seq data, and that the paired-end reads are found in files R1 and R3. The entirety of each file is used. Note that for the whitelist we used the reverse complement of the whitelist provided by 10x.

### **A.9 Nearest-Neighbor Correlations**

For each pair of adjacent ATAC-seq peak sites in the loci we selected, we calculated the Pearson correlation coefficient between the two sites in the pair. The sample Pearson correlation coefficient between two variables x and y is defined via:


where n is the size of the sample of joint observations of x and y, and ⟨⟩ denotes the sample averages of the enclosed quantities across all cells. In this case, we are considering each pair of adjacent sites, ( _𝑥, 𝑦_ ), which have openness values 0 or 1. Each cell in the dataset gives another joint observation of the value of the sites. For a pair of sites, we consider the number of observations across cells of each possible openness configuration, ((0 _,_ 0) _,_ (0 _,_ 1) _,_ (1 _,_ 0) _,_ (1 _,_ 1)), and label the proportion of such observations _𝑝_ 00, _𝑝_ 01, _𝑝_ 10, and _𝑝_ 11 respectively. Note that, since the openness values at sites _𝑥_ and _𝑦_ take binary values, we have:

120


<!-- Start of picture text -->
6-Parameter Model Observed Frequency 8-Parameter Model<br>0.6<br>Chrom 1:25028504-25036643<br>0.4<br>0.2<br>0.0<br>0.25 Chrom 1:30743207-30761867<br>0.20<br>0.15<br>0.10<br>0.05<br>0.00<br>Chrom 1:145983069-146000218<br>0.3<br>0.2<br>0.1<br>0.0<br>Chrom 1:154997426-155013274<br>0.4<br>0.3<br>0.2<br>0.1<br>0.0<br>Chrom 10:69043845-69054726<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0.0<br>Chromatin Configuration<br>000000000100000010001000000001100000000110001100001010000101100100100010010000000011101000001001001110100001100110000111101100101010 000000000100000010001000000001100000000110001100001010000101100100100010010000000011101000001001001110100001100110000111101100101010<br>000000000010100000001010001000100010101000101010000001000011100001010000010010001011100011001001101011011010101001110000011000110010 000000000010100000001010001000100010101000101010000001000011100001010000010010001011100011001001101011011010101001110000011000110010<br>000000000010000110000100010010010000001000001010000011000001010110010100001110000111001100100010011010100000000101010011010001011000 000000000010000110000100010010010000001000001010000011000001010110010100001110000111001100100010011010100000000101010011010001011000<br>001000000000011000010000001001001010000001000010101000001100011001011010001011000100100000010001010010011100101001111000000011001110 001000000000011000010000001001001010000001000010101000001100011001011010001011000100100000010001010010011100101001111000000011001110<br>000000010000100000001000000010011000110000000001010010001010011010101000010001100010111000001001000100000011011001101010110010001100 000000010000100000001000000010011000110000000001010010001010011010101000010001100010111000001001000100000011011001101010110010001100<br>Probability of Configuration: ()P<br><!-- End of picture text -->

Figure A.8: Six and eight-parameter model fits to 5 loci in the human PBMC dataset. The scatter plots show the analytic distribution at the best fitting parameters, and the bar chart shows the empirical distribution.

121


Figure A.9: MCMC methods used to fit the eight-parameter model on locus 11:67400339-67415716 of the PBMC dataset. The most probable parameter values matched with those found using the global minimization algorithm. 512 walkers were used, with initial values of _𝑘_ o _𝑛,𝑖_ = 1 for all sites, _𝜖_ = 1 and _𝑝_ d _𝑟𝑜𝑝_ = 0 _._ 7. The parameters were fit in log-space.


From Equation A.36, we then have:


We calculate the Pearson coefficient in this way from each pair of adjacent sites in the selected loci. We can also calculate the average openness of the pair of sites, via:


122

### **A.10 Positive Outlier: Locus 10:69043845-69054726**

In the PBMC dataset, locus 10:69043845-69054726 shows a significantly larger BIC difference in favor of the eight-parameter model than any other locus. The fits of each model are shown in the bottom row of Figure A.8. Figure A.1 (the middle of the second row) also shows that this locus seems to have mean openness values that are correlated between neighboring sites.

### **A.11 Symmetries Transition Matrix Symmetry**

Let us consider terms of the form:


Recalling that _𝐻_<sup>˜</sup> ∝ _𝐻_<sup>_𝑇_</sup> , we note that the components _𝐻_<sup>˜</sup> _𝛼𝛽_ are only non-zero for states which are connected (denoted _𝛼_ ∼ _𝛽_ ), meaning that _𝛼_ can be reached from _𝛽_ by flipping the openness of a single site. Recall also that _𝑆𝛼_<sup>_𝑖_</sup> = 0 _,_ 1 indicates that site _𝑖_ is closed/open in state _𝛼_ . Since _𝑆𝛼_<sup>_𝑖_</sup> and _𝑆𝛽_<sup>_𝑗_</sup> must both be 1 for non-zero contributions to A.40, and _𝛼_ ∼ _𝛽_ , we can re-write Expression A.40 as:


This is because, unless _𝑆𝛽_<sup>_𝑖_</sup> and _𝑆𝛼_<sup>_𝑗_</sup> are both zero, the multiplier within the parentheses evaluates to 1. But, as discussed above, for _𝛽_ ∼ _𝛼_ , we cannot have _𝑆𝛼_<sup>_𝑖_</sup> = _𝑆𝛽_<sup>_𝑗_</sup> = 1, and _𝑆𝛽_<sup>_𝑖_</sup> = _𝑆𝛼_<sup>_𝑗_</sup> = 0, since this would require both sites _𝑖_ and _𝑗_ to change openness value between states _𝛼_ and _𝛽_

We can think of the multiplier within the parentheses of Expression A.41 as dividing the expression into the different possible transitions between connected states. The first term represents transitions between states where both sites _𝑖_ and _𝑗_ are open in both _𝛼_ and _𝛽_ , the second from _𝑖_ closed and _𝑗_ open to both open, and the last from both open to _𝑖_ open and _𝑗_ closed. Then, noting that **_π_** is the steady-state vector of the Markovian transition matrix _𝐻_<sup>_𝑇_</sup> , we have that:

123


allowing us to re-write the final term of Equation A.41 as:


where in the last line we have simply relabeled the indices (note the symmetry of the relation _𝛽_ ∼ _𝛼_ ). This allows us to re-write the total expression in A.41 as:


where the first equality comes from the fact that _𝑆𝛼_<sup>_𝑖_</sup> _𝑆𝛼_<sup>_𝑗_</sup> selects for transitions into states with both sites _𝑖_ and _𝑗_ open. The connected origin states _𝛽_ must either have both states _𝑖_ and _𝑗_ open, or exactly one of the _𝑖_ and _𝑗_ sites open. Hence the sum in terms of _𝑆𝛽_<sup>_𝑖,𝑗_</sup> expresses all of the non-zero transitions between states _𝛽_ and _𝛼_ , making the expression redundant with the specification that all _𝛽_ ∼ _𝛼_ , (i.e. the multiplier in parentheses must evaluate to 1, similarly to before). The second equality comes from the symmetry of _𝐻_<sup>˜</sup> (A.11), and the fact that only _𝐻_<sup>˜</sup> _𝛼𝛽_ are only non-zero for _𝛽_ ∼ _𝛼_ (or alternatively from the definition of **_π_** ).

Thus we have shown that:


124

### **Inverse Matrix Symmetry**

We consider the inverse matrix defined via:


Note that, by the definition of M:


and that, also:


Considering the RHS of Equation A.48 component-wise, and summing over _𝛼_ , we note that:


where for the last equality we have used the symmetry of _𝐻_<sup>˜</sup> :


Then, equating this with the component-wise version of Equation A.47, we arrive at:


as desired. □

125

_A p p e n d i x B_

---

[← FUTURE DIRECTIONS](11-future-directions.md) · [Up: contents](index.md) · [PROMONOD SUPPLEMENTARY INFORMATION →](13-promonod-supplementary-information.md)

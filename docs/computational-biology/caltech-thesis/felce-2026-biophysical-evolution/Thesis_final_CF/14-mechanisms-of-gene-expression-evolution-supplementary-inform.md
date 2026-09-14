---
title: 'MECHANISMS OF GENE EXPRESSION EVOLUTION: SUPPLEMENTARY INFORMATION'
source: https://thesis.library.caltech.edu/17880/
source_file: sources/felce-2026-biophysical-evolution/Thesis_final_CF.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# MECHANISMS OF GENE EXPRESSION EVOLUTION: SUPPLEMENTARY INFORMATION

**Source:** `Thesis_final_CF.pdf` from [felce-2026-biophysical-evolution](https://thesis.library.caltech.edu/17880/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **C.1 Data processing**

### **Pre-processing**

For this study we use single-cell RNA-seq data from Jiao et al. Jiao et al., 2024, extracted from the spleen of seven different species. We processed the data using kallisto Sullivan et al., 2025 to obtain spliced and unspliced count matrices, and filtered out low UMI cells. An example kallisto call is given here:

```
kbcount--verbose-i./frog/index.idx-g./frog/t2g_mm10.txt
```

- `-x 10xv2 -o ./frog/output -t 24 -m 8G -c1 ./frog/cdna_t2c.txt -c2 ./frog/intron_t2c.txt --workflow=nac --filter bustools --strand=unstranded --sum=cell ../SRR16490736_1.fastq ../SRR16490736_2.fastq,`

with example output summary:

- `"n_targets": 76913,`

- `"n_bootstraps": 0,`

- `"n_processed": 289062079,`

- `"n_pseudoaligned": 190915538,`

- `"n_unique": 35185121,`

- `"p_pseudoaligned": 66.0,`

- `"p_unique": 12.2,`

```
"kallisto_version":"0.50.1",
```

- `"index_version": 13,`

- `"start_time": "Wed Jun 12 15:04:30 2024"`

After clustering the data from each species by cell-type, we excluded the fish sample from further analysis because of an indistinct and low-count T-cell cluster, leaving six remaining species, which were filtered for T-cells.

132

### **Fitting biophysical parameters**

We searched for genes which had orthologs in all six species using Ensembl BioMart Kinsella et al., 2011. We then fit transcriptional rates for these genes in each species separately using Monod Gorin and Pachter, 2023, using the bursty transcription model with Poisson technical noise. After fitting with Monod, which filters some genes, and removing genes without a fitted ortholog in all six species, we were left with 167 genes. An example of the Monod run is given below:

```
fitmodel=cme_toolbox.CMEModel(’Bursty’,’Poisson’)
filt_param={’min_means’:[0.01,0.01],’max_maxes’:[350,350],
’min_maxes’:[1,3]}
```

```
lb=[-1.0,-1.8,-1.8]
ub=[4.2,2.5,3.5]
#samp_lb,samp_ub=[-8,-3],[-5,0]
samp_lb,samp_ub=[-11,-6],[-5,0]
```

```
grid=[6,7]
```

- `fitted_adata = inference.perform_inference(combined_adata, fitmodel, n_genes=5000, seed=5, phys_lb=lb, phys_ub=ub, gridsize=grid, samp_lb=samp_lb, samp_ub=samp_ub, filt_param=filt_param, gradient_param={‘max_iterations’:5, ‘init_pattern’:’moments’,‘num_restarts’:1}, dataset_string=dataset_string, viz=True,num_cores=32)`

The output of this procedure is a per-gene burst size, _𝑏_ , splicing rate _𝛽_ , and decay rate, _𝛾_ , with the rates given in units of the transcription initiation rate, _𝑘_ , all in log space. We then subtracted the mean of each parameter across genes from each species, and used the resulting values as the traits for the phylogenetic analysis.

### **Phylogenetic tree**

For the phylogenetic tree, we used the following tree, from TimeTree Kumar et al., 2022, in Newick format:

```
(Frog:351.68654000,(Pig:94.00000000,((Rat:11.64917000,
```

133

```
Mouse:11.64917000)’14’:75.55083000(Human:28.82000000,
Macaque:28.82000000)’13’:58.38000000)’25’:6.80000000)
’37’:257.68654000);
```

### **C.2 Two-dimensional evolution model**

### **Phylogenetic model derivation from fitness landscape**

Following Cope et al. Cope, Schraiber, and Pennell, 2025, we consider a fitness function of the form:


Since transcriptional rates are the mechanisms by which cells control the level of transcription, we assume that mutations can affect _𝑏_ and _𝛾_ independently. This corresponds to setting _𝑐_ = 0 in the model from Cope et al. Cope, Schraiber, and Pennell, 2025. Then, using their expression for the evolution matrix, (their _𝐹_ ), we have:


We then consider two different models. In the first model, we assume that selection acts first on the decay rate, _𝛾_ , and then on the mean spliced RNA value, _𝜇𝑠_ , via adaptation of the burst size, _𝑏_ . This is equivalent to setting _𝜙𝛾_ = 0 and _𝜙𝑏_ = 1, recalling that, in log space, log _𝜇𝑠_ = log _𝑏_ − log _𝛾_ . Note that, since the unspliced mean, _𝜇𝑢_ , is given by<sup>_<u>𝑏</u>_</sup> _𝛽_<sup>,and the spliced mean is given by</sup><sup>_<u>𝜇</u>_</sup> _𝛾_<sup>_<u>𝑢𝛽</u>_,the splicing rate</sup><sup>_𝛽_</sup> does not influenced the mean spliced counts, _𝜇𝑠_ (recall that rates are in fitted in units of the transcriptional initiation rate). In this model, we also relabel _𝑉𝑏_ → _𝑉𝜇_ and _𝜃𝑏_ → _𝜃 𝜇_ , to emphasize that the pressure on _𝑏_ to adjust is equivalent to selection pressure on the mean spliced RNA level. So we have, for the fist, _𝛾_ -constrained model:


134

For the _𝛾_ -constrained model, _𝐻_ becomes:


and _𝜔_ =<sup>_𝑉𝜇_</sup> _𝑉𝛾_<sup>.Inthis</sup><sup>_𝛾_-constrainedmodel,wefurtherassumethat</sup><sup>_𝑉𝛾_≪</sup><sup>_𝑉𝜇_,such</sup> that we can neglect terms O _𝜔_ <u>1</u> , giving: � �


For our second model, we assume that _𝑏_ is tightly constrained, and _𝛾_ is more free to vary and adjust to the optimum mean RNA level. This corresponds to setting _𝜙𝑏_ = 0 and _𝜙𝛾_ = 1. The fitness function then becomes:


where we have relabeled _𝑉𝛾_ → _𝑉𝜇_ and _𝜃𝛾_ →− _𝜃 𝜇_ (note the change of sign in the first term has no effect due to the squaring). This gives, as above:


For this, _𝑏_ -constrained, model, _𝜔_ ≡<sup>_𝑉𝑏_</sup> _𝑉𝜇_<sup>, and we assume</sup><sup>_𝑉𝑏_≪</sup><sup>_𝑉𝜇_, giving:</sup>


We compare these models with a fully independent model (diagonal _𝐻_ ), as well as more generic models. For all models, we fit a diagonal matrix for the stochastic term:

135


which depends on the relative mutation rates of _𝑏_ and _𝛾_ .

Recall Cope et al. also have:


where, again, we have switched to our notation. Since either _𝜙𝑏_ or _𝜙𝛾_ is zero in each of our models, the denominator is always equal to one. In particular, we have:


for the first and second models respectively. We then assume that the logarithms of _𝑏_ and _𝛾_ evolve along the tree according to


as in the independent case, where now


and _𝐻_ , **_X_**<sup>ˆ</sup> and Σ are as specified above. Note that the selection matrix _𝐻_ is the only structural difference between the two models.

### **Evolutionary parameter inference**

We fit a mixture model where a fraction _𝑝_ w _𝑛_ of genes are assumed to be drawn from a white-noise distribution. The rest of the genes are assumed to be generated from the relevant phylogenetic model, described in C.2.

136

The evolutionary parameters in _𝐻_ and Σ are assumed constant across genes, but the optimal values _𝜃 𝜇, 𝜃𝑏,𝛾_ are allowed to vary per gene, and are assumed to be drawn from a normal distribution centered at _𝜃_<sup>¯</sup><sup>_𝑃_</sup> _𝜇_<sup>and</sup><sup>_𝜃_¯</sup> _𝑏,𝛾_<sup>_𝑃_respectively, where the</sup><sup>_𝑃_denotes</sup> the population of optima over genes. The standard deviations of these populations of optima are also fit as part of the likelihood maximization ( _𝜏𝑏,𝛾_<sup>_𝑃, 𝜏_</sup> _𝜇_<sup>_𝑃_).Wethen</sup> analytically integrate over the possible values of _𝜃 𝜇_ and _𝜃𝑏,𝛾_ .

The white-noise distribution is a two-dimensional Gaussian with mean **_X_**<sup>**ˆ**</sup> , with the values of _𝜃 𝜇, 𝜃𝑏,𝛾_ assumed to be drawn from the same distributions as for the phylogenetic model, and diagonal covariance matrix with entries _𝜎𝑤𝑛_<sup>_𝑏,𝛾_.Since</sup> we analytically integrate over possible values of _𝜃𝑏,𝛾_ , this amounts to a new twodimensional Gaussian distribution with means _𝜃_<sup>¯</sup><sup>_𝑃_</sup> _𝜇_<sup>and</sup><sup>_𝜃_¯</sup> _𝑏,𝛾_<sup>_𝑃_, with covariance matrix</sup> given by Cov( **_X_**<sup>**ˆ**</sup> ) (see section C.5).

Overall, this gives an 11-parameter model, with 4 evolutionary parameters, 3 whitenoise parameters (the two standard deviations and the mixture probability _𝑝𝑤𝑛_ ), and 4 optima distribution parameters. The likelihood of the data under the full model is optimized using `optimx` Nash and Varadhan, 2011.

### **Simulation results: Two-dimensional model**

For the model comparison, we simulate 100 datasets under each of hypotheses 1 and 2 (decay rate and burst size-driven), using PCMBase Mitov et al., 2020. We draw random sets of true parameters for each simulation uniformly between the bounds. We then fit the simulated datasets using the procedure described above. The results for the decay-rate-constrained model are shown in Figure C.1, and the results for the burst-size-constrained model are shown in Figure C.2.

We also performed a model comparison by simulating data under both models, and fitting both datasets under each model. We show the distribution of AIC differences in favor of the correct model in Figure C.3. We show the corresponding accuracy of differentiating between models using the AIC value in Figure C.4. This is given by the fraction of model fits with AIC differences above each cutoff which would be attributed to the correct model.

### **Data fit details**

We include the fitted parameter values for the two-parameter _𝐻_ , two-dimensional OU model in Table C.1. Note that the burst-size-constrained model hits the upper bound for _𝑝_ wn, the probability for each gene to be pure noise in our mixture model.

137


<!-- Start of picture text -->
αb αγ σb σγ<br>10.0 10.0<br>2.0<br>1.5 2 7.5 7.5<br>1.0 5.0 5.0<br>1<br>0.5 2.5 2.5<br>0.0 0 0.0 0.0<br>0.5 1.0 1.5 2.0 0.5 1.0 1.5 2.0 0.0 2.5 5.0 7.5 10.0 0.0 2.5 5.0 7.5 10.0<br>σbwn σγwn pwn θ P µ<br>15 1.0<br>20 0.6<br>0.5<br>15 10 0.4<br>10 0.0<br>5 0.2<br>5 −0.5<br>0 0 0.0<br>0.0 2.5 5.0 7.5 10.0 0.0 2.5 5.0 7.5 10.0 0.0 0.2 0.4 0.6 −0.050−0.025 0.000 0.025 0.05<br>τPµ θ P γ τPγ<br>6<br>1.0 2.0<br>4 0.5 1.5<br>1.0<br>0.0<br>2<br>0.5<br>−0.5<br>0 0.0<br>0.950 0.975 1.000 1.025 1.050 −0.050−0.025 0.000 0.025 0.050 0.950 0.975 1.000 1.025 1.050<br>True<br>Estimated<br><!-- End of picture text -->

Figure C.1: Fitted vs true parameters for the decay-rate-constrained model.

Table C.1: Two-dimensional OU model fitted parameters

|Model|_𝛼𝑏_|_𝛼𝛾_|_𝜎𝑏_|_𝜎𝛾_|_𝑝_wn|AIC|
|---|---|---|---|---|---|---|
|_𝛾_-constrained|31.5|2.33|0.923|1.06|0.149|2124|
|_𝑏_-constrained|0.022|3.56|3.01|0.169|0.900|3186|
|Independent|1.36|1.59|0.651|0.831|0.329|2726|


### **dN/dS calculations**

To look at the signatures of selection for the 167 genes in our dataset across the six species phylogeny, we computed dN/dS values. We adopted a standard bioinformatic pipeline, using protein and cDNA sequences from Ensembl Dyer et al., 2024, protein alignment using MAFFT Katoh and Standley, 2013, codon based alignment with Pal2Nal Suyama, Torrents, and Bork, 2006 and dN/dS calculations using CODEML from PAML Yang, 2007; Álvarez-Carretero, Kapli, and Yang, 2023. Out of 167 genes, we obtained values for 159 gene ortholog groups which we plotted based on the bins of gene expression, shown in Figure C.5.

138


<!-- Start of picture text -->
αb αγ σb σγ<br>2.5 10.0<br>2.0 9<br>2 7.5<br>1.5 6<br>5.0<br>1 1.0<br>3 2.5<br>0.5<br>0 0 0.0<br>0.5 1.0 1.5 2.0 0.5 1.0 1.5 2.0 2.5 5.0 7.5 10.0 0.0 2.5 5.0 7.5 10.0<br>σbwn σγwn pwn θ P µ<br>10.0 10.0 0.6<br>1.0<br>7.5 7.5<br>0.4 0.5<br>5.0 5.0<br>0.0<br>0.2<br>2.5 2.5 −0.5<br>0.0 0.0 −1.0<br>2.5 5.0 7.5 10.0 0.0 2.5 5.0 7.5 10.0 0.0 0.2 0.4 0.6 −0.050−0.025 0.000 0.025 0.05<br>τPµ θ P b τPb<br>5<br>4 0.5 2<br>3<br>2 0.0 1<br>1<br>−0.5<br>0 0<br>0.950 0.975 1.000 1.025 1.050 −0.050−0.025 0.000 0.025 0.0500.950 0.975 1.000 1.025 1.050<br>True<br>Figure C.2: Fitted vs true parameters for the burst-size-constrained model.<br>∆AIC for simulation under model 1 ∆AIC for simulation under model 2<br>40<br>40<br>30<br>30<br>20<br>20<br>10 10<br>0 0<br>0 100 200 300 400 >500 0 100 200 300 400 >500<br>∆AIC = AIC(model 2) − AIC(model 1) ∆AIC = AIC(model 1) − AIC(model 2)<br>(a) (b)<br>Estimated<br>Count Count<br><!-- End of picture text -->

Figure C.3: Distributions of AIC differences in favor of the correct model, for datasets simulated under the decay-rate-constrained model **(a)** and the burst-sizeconstrained model **(b)** , fitted under both models.

### **C.3 Independent evolution model**

We also considered the simple case where, for each gene, the biophysical parameters, _𝑏_ , _𝛽_ , and _𝛾_ , evolve independently. We assume that each gene also evolves

139


<!-- Start of picture text -->
Correct identification vs AIC cutoff Correct identification vs AIC cutoff: Simulated model 2<br>100 100<br>98<br>98<br>96<br>96<br>94<br>94<br>92<br>0 25 50 75 100 0 25 50 75 100<br>AIC cutoff AIC cutoff<br>(a) (b)<br>% correctly identified % correctly identified<br><!-- End of picture text -->

Figure C.4: Accuracy of model identifications made at various AIC cutoffs, for datasets simulated under the decay-rate-constrained model **(a)** and the burst-sizeconstrained model **(b)** , fitted under both models. Accuracy is defined as the fraction of model fits with AIC differences above each cutoff that would be attributed to the correct model.

independently, but that all genes evolve according to the same evolutionary dynamics Chaix et al., 2008 Cope, Schraiber, and Pennell, 2025. This amounts to a shared selection matrix, _𝐻_ , and mutation matrix, Σ, in the OU evolution equation:


where **_X_** is given by the logarithms of the three biophysical rates,


The assumed independence of the biophysical rates is enforced by diagonality of _𝐻_ and Σ. We therefore define parameter-specific selections rates, _𝛼_ , and stochastic standard deviations, _𝜎_ , via:


140


<!-- Start of picture text -->
*<br>ns<br>0.4<br>ns<br>0.3<br>0.2<br>0.1<br>0.0<br>low medium high<br>Expression levels<br>Omega (dN/dS)<br><!-- End of picture text -->

Figure C.5: dN/dS values for 159 genes across the six species tree, binned by expression level

If we assume that the root value is drawn from the stationary distribution, we have that:


Each gene is assumed to have its own optimum value, given by _𝜃𝑔_ , drawn from a normal distribution, _𝑁_ ( _𝜃, 𝜏_<sup>¯2</sup> ). The parameters of this normal distribution are optimized during fitting, and the hyper-prior is specified along with the priors for the other model parameters. We can integrate over the possible values of _𝜃𝑔_ for each gene, to give a new variance-covariance matrix given by:


141

Since initial fits gave high values for the diagonal elements of _𝐻_ (indicating low phylogenetic signal for many genes), we fitted a mixture model, following Chaix et al. Chaix et al., 2008. For the ‘outlier’ distribution, we used a white-noise (wn) (normal) distribution, centered at _𝜃_<sup>¯</sup> , with variance _𝜎_ w<sup>2</sup> _𝑛_<sup>+</sup><sup>_𝜏_2, to represent a process of</sup> rapid mean-reversion with negligible phylogenetic signal. As in Chaix et al., 2008, we then optimized for a total likelihood given by:


where LLi _𝑛_ is the likelihood of the original model. We implemented this via an MCMC in rstan. The simulation results for MCMC fits to the selection strength, standard deviations, and white noise probabilities are shown in Figure C.6.


Figure C.6: Estimated vs true parameters for simulated data under the independent model described in Section C.3. The mean posterior values for the MCMC, are plotted against the known, simulated parameters. The red points showed poor convergence.

142

### **Independent model results**

We applied the model to the data described in Section C.1. The posterior distributions for the most significant parameters are shown in Figure C.7. The posteriors for all of the parameters are shown in Figure C.8.


Figure C.7: Posterior distributions for the selection strength ( _𝛼_ ) and the mutation strength ( _𝜎_ ), for the independent evolution of the logarithms of the biophysical parameters: burst size ( _𝑏_ , red), splicing rate ( _𝛽_ , blue), and decay rate ( _𝛾_ , green).

### **C.4 Three-parameter** _𝐻_ **models**

We also investigated models of the above form, but with the off-diagonal _𝐻_ terms allowed to vary from the corresponding diagonal value. This is equivalent to allowing _𝜙𝑏_ and _𝜙𝛾_ respectively to differ from one (see Section C.2). This gives selection matrices:


and _𝑋_<sup>ˆ</sup> values:


143


Figure C.8: Posterior distributions for the selection strength ( _𝛼_ ) and mutation strength ( _𝜎_ ) in the independent OU model. The mixture model probability, _𝑝_ w _𝑛_ , the white-noise distribution standard deviation, _𝜎_ w _𝑛_ , and the parameters of the assumed underlying distribution for the gene optima and white-noise means ( _𝜃_<sup>¯</sup><sup>_𝑃_</sup> _, 𝜏_<sup>_𝑃_</sup> ) are also shown. These are the parameters governing the independent evolution of the logarithms of the biophysical parameters: burst size ( _𝑏_ , red), splicing rate ( _𝛽_ , blue), and decay rate ( _𝛾_ , green).

for the two models respectively. The other details of the models were identical to Section C.2. Although these models had better AIC scores than those discussed in the main text, because of the required additional parameter, and the superior interpretability of the two-dimensional models, we have discussed those more at length.

### **Simulations results: three-parameter models**

As for the two-parameter _𝐻_ case, we simulate 100 datasets under each of hypotheses 1 and 2 (decay rate and burst size-driven), this time with the extra _𝜙𝑏,𝛾_ parameters. The results for the three-parameter decay-rate-constrained model are shown in Figure C.9, and the results for the three-parameter burst-size-constrained model are shown in Figure C.10.

As before, we perform a simulated model comparison for the three-parameter _𝐻_ case. We show the distribution of AIC differences in favor of the true simulated model in Figure C.11. We show the corresponding accuracy of differentiating

144


<!-- Start of picture text -->
αb αγ q σb<br>2 12.5<br>30<br>10.0<br>20 1<br>20 7.5<br>5.0<br>10 10 0<br>2.5<br>0 0 −1 0.0<br>0 5 10 15 20 0 5 10 15 20 −1 0 1 2 0.0 2.5 5.0 7.5 10.0<br>σγ σbwn σγwn pwn<br>10.0 15<br>0.6<br>9<br>7.5<br>6 10 0.4<br>5.0<br>2.5 3 5 0.2<br>0.0 0 0 0.0<br>0.0 2.5 5.0 7.5 10.0 0.0 2.5 5.0 7.5 10.0 0.0 2.5 5.0 7.5 10.0 0.0 0.2 0.4 0.6<br>θ P b τPb θ P γ τPγ<br>2.5<br>2.0<br>1.0<br>0.3 2.0<br>1.5<br>0.5 1.5<br>0.0 1.0<br>0.0 1.0<br>−0.3 0.5 −0.5 0.5<br>0.0 0.0<br>−0.6<br>−0.050−0.025 0.000 0.025 0.0500.950 0.975 1.000 1.025 1.050 −0.050−0.025 0.000 0.025 0.050 0.950 0.975 1.000 1.025 1.05<br>True<br>Estimated<br><!-- End of picture text -->

Figure C.9: Fitted vs true parameters for the decay-rate-constrained, three-parameter _𝐻_ model.

between models using the AIC value in Figure C.12.

### **Data fits: three-parameter models**

We include the fitted parameter values for the three-parameter _𝐻_ models in Table C.2. Note that the AIC is again much better for the decay-rate-constrained model, and _𝑝_ wn goes to the upper bound in the burst-size-constrained model.

Table C.2: Three-parameter model fitted parameters

|Model|_𝛼𝑏_|_𝛼𝛾_|_𝜙𝑏,𝛾_|_𝜎𝑏_|_𝜎𝛾_|_𝑝_wn|AIC|
|---|---|---|---|---|---|---|---|
|_𝛾_-constrained|130.2|4.21|0.717|2.20|1.33|0.226|1972|
|_𝑏_-constrained|1.91|4.68|1.84|0.567|0.00676|0.9|3166|


### **C.5 Theta integration**

For a vector of traits (e.g. ( _𝑏_ , _𝛽_ , _𝛾_ )), we consider the distribution of values for a single species given a constant optimum, _𝜃_ . We define:

145


<!-- Start of picture text -->
αb αγ q σb<br>50 40 2<br>40 30<br>1 10<br>30<br>20<br>20<br>0 5<br>10 10<br>0 0 −1 0<br>0 5 10 15 20 0 5 10 15 20 −1 0 1 2 0.0 2.5 5.0 7.5 10.0<br>σγ σbwn σγwn pwn<br>10.0 10.0 15<br>0.75<br>7.5 7.5<br>10<br>5.0 5.0 0.50<br>5<br>2.5 2.5 0.25<br>0.0 0.0 0 0.00<br>0.0 2.5 5.0 7.5 10.0 0.0 2.5 5.0 7.5 10.0 0.0 2.5 5.0 7.5 10.0 0.0 0.2 0.4 0.6<br>θ P b τPb θ P γ τPγ<br>0.8 1.5<br>0.6<br>0.4 1.0 0.4<br>1.0<br>0.2<br>0.0<br>0.0 0.5 0.5<br>−0.4<br>−0.2<br>0.0 0.0<br>−0.050−0.025 0.000 0.025 0.050 0.950 0.975 1.000 1.025 1.050 −0.050−0.025 0.000 0.025 0.050 0.950 0.975 1.000 1.025 1.05<br>True<br>Figure C.10: Fitted vs true parameters for the burst-size-constrained, three-<br>parameter  𝐻 model.<br>∆AIC  for simulation under model 1, with three−parameter H ∆AIC  for simulation under model 2, with three−parameter H<br>20<br>20<br>10 10<br>0 0<br>0 100 200 300 400 0 100 200 300 400 >500<br>∆AIC = AIC(model 2) − AIC(model 1) ∆AIC = AIC(model 1) − AIC(model 2)<br>(a) (b)<br>Estimated<br>Count Count<br><!-- End of picture text -->

Figure C.11: Distributions of AIC differences in favor of the simulated model for datasets simulated under the three-parameter _𝐻_ versions of the decay-rateconstrained model ( **left** ) and the burst-size-constrained model ( **right** ), fitted under both models.

146


<!-- Start of picture text -->
Correct identification vs AIC cutoff: Simulated model 1 Correct identification vs AIC cutoff: Simulated model 2<br>100 100<br>90<br>90<br>80<br>70 80<br>0 25 50 75 100 0 25 50 75 100<br>AIC cutoff AIC cutoff<br>(a) (b)<br>% correctly identified % correctly identified<br><!-- End of picture text -->

Figure C.12: Accuracy of model identifications made at various AIC cutoffs for datasets simulated under the three-parameter _𝐻_ versions of the decay-rateconstrained model ( **left** ) and the burst-size-constrained model ( **right** ), fitted under both models. The accuracy is defined as the fraction of model fits with AIC differences above each cutoff which would be attributed to the correct model.


where _𝐻_<sup>ˆ</sup> is the selection matrix. As in the one-trait case, we have:


Then, using the OU equation:


where **_dW_** is a vector whose components are independent instantiations of the random variable, dW (Wiener process), and correlations between changes in the different variables of **_x_** _𝑡_ can be introduced via off-diagonal elements in 𝚺. This gives:


147

where, for the second equality, we have used the commutation of _𝑒_<sup>_𝐻𝑡_ˆ</sup> and _𝐻_<sup>ˆ</sup> . Using the convenient properties of the matrix exponential, we can solve this via:


for _𝑠_ our dummy time variable. Then, by the definition of **_f_** , (and the commutation of _𝐻_<sup>ˆ</sup> with itself and its inverse), we have:


Note that in the limit _𝑡_ →∞, for positive definite _𝐻_<sup>ˆ</sup> , the first term vanishes, and we are left with a linear sum of the independent normal random variables, _𝑑𝑊𝑠_ , which make up **_dW_** _𝑠_ . Since each component of **_x_** _𝑡_ is a linear comination of the _𝑑𝑊_ values, the vector **_x_** _𝑡_ has a multivariate normal distribution. We can proceed to calculate the moments of this distribution. We find, for a single tip, _𝑖_ , at time _𝑡_ = _𝑡𝑖_ ,


since E( **_dWt_** ) = **0** for all _𝑡_ , and **_θ_** and _𝐻_<sup>ˆ</sup> are fixed parameters of the system. We now consider the variance-covariance of the different traits at a single tip. We use Greek indices to indicate the different traits at a tip, (and Latin indices to indicate the tip (extant species)). Since **_x_ 0** and the stochastic path integral are independent random variables (and the middle term is constant), we have:


First we focus on the **_x_ 0** term. By simple properties of matrices we have:

148


for _𝑉_<sup>ˆ</sup> _𝑥_ 0 the variance-covariance matrix for **_x_ 0** . Then we focus on the integral term. As above, the expectations of all components of **_dW_** are zero. For generic traits _𝛼_ and _𝛽_ we therefore have:


Since each individual _𝑑𝑊𝑠_ is assumed independent from the last, and has zero expectation, we have:


For notes on solving this, see Jonathan Goodman, NYU n.d. Next, we consider the covariance between traits _𝛼_ and _𝛽_ , between two _different_ species _𝑖_ and _𝑗_ . We have:


Recall that the stationary variance satisfies:

149


We have already shown that the stationary distribution is multivariate Gaussian. If **_x_ 0** is drawn from this distribution, it will therefore be distributed via:


and the entire process is also multivariate normal given by:


using again that _𝐻_<sup>ˆ−1</sup> and _𝑒_<sup>−</sup><sup>_𝐻𝑡_ˆ</sup> commute to calculate the mean, and _𝑉_<sup>ˆ</sup> is the full covariance matrix. If **_θ_** is another random variable chosen independently from a prior, and the previous distribution of **_x_** _𝑡_ is in fact **_x_** _𝑡_ | **_θ_** , we consider again:


Since the last term is linear combinations of the same _𝑑𝑊_ , it is clearly multivariate normal, and independent from the other two terms. **_θ_** is drawn from a normal prior, _𝑁_ ( _𝜇𝜃, 𝑉_<sup>ˆ</sup> _𝜃_ ). This determines the distribution of the r.v. **_x_ 0** . This distribution is determined by imagining the stationary version of the equation, where _𝑡_ →∞:


This stationary distribution clearly would be multivariate normal with expectation **_θ_** and some stationary variance _𝑉_<sup>ˆ</sup> s _𝑡𝑎𝑡_ , which depends on the model parameters. To show that **_x_ 0** is multivariate normal with **_θ_** , consider the sum of the two variables. Consider **_x_ 0** = **_θ_** + _𝜖_ , with _𝜖_ ∼ _𝑁_ (0 _, 𝑉_<sup>ˆ</sup> s _𝑡𝑎𝑡_ ). For deterministic _𝛼, 𝛽_ and _independent_ **_θ_** and _𝜖_ , we have _𝛼_ **_x_ 0** + _𝛽_ **_θ_** = ( _𝛼_ + _𝛽_ ) **_θ_** + _𝛼_ **_ϵ_** . Clearly, the whole of **_x_** _𝑡_ is still a multivariate normal random variable. The expected value is given by:

150


where we have used that E( **_dW_** ) = **0** . Considering **_θ_** as a random variable changes the variance-covariance matrix of the distribution, since now we have to consider:


retaining the separation of this term from the integral term, since the two are independent. Considering the decomposition above, we get:


Considering this, trait-component-wise, we have:


Since the integral term is unchanged, this simply represents summing the original variance-covariance matrix with the variance-covariance matrix for **_θ_** . Since the **_x_ 0** and **_θ_** values are common between species, the components of Cov _𝑖𝑗𝛼𝛽_ , between

151

different species _𝑖_ and _𝑗_ , will also pick up these same covariance terms. This will give the full, overall formula:


This allows us to effectively integrate over a Gaussian prior on the optima, by using the prior distribution covariance in _𝑉_<sup>ˆ</sup> _𝜃_ , and considering a new Gaussian distribution for **_xt_** with a covariance given by Eq. C.43.

152

---

[← PROMONOD SUPPLEMENTARY INFORMATION](13-promonod-supplementary-information.md) · [Up: contents](index.md)

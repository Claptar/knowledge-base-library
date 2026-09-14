---
title: 9.4 Logistische regressie
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-categorisch.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-categorisch.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 9.4 Logistische regressie

**Source:** [`chap-categorisch.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-categorisch.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

In de statistische literatuur bestaat ook een raamwerk voor het modelleren van binaire data (vb. kanker vs geen kanker): *logistische regressie-modellen*. Net zoals we bij het regressiemodel voor Normale continue gegevens hebben gezien in Hoofdstuk [6](../chap-linReg/index.md), [7](../chap-anova/index.md) en [10](../chap-glm/index.md), laten logistische regressie modellen toe om binaire gegevens te modelleren a.d.h.v. continue en/of dummy variabelen.

De modellen veronderstellen dat de observaties voor subject <span class="math inline">\$i=1,\\ldots,n\$</span> onafhankelijk zijn en een Bernoulli verdeling volgen. Het logaritme van de odds wordt dan gemodelleerd d.m.v. een lineair model, ook wel lineaire predictor genoemd: <span class="math display">\\$$\\begin{equation} \\left\\{ \\begin{array}{ccl} Y\_i&\\sim&B(\\pi\_i)\\\\\\\\ \\log \\frac{\\pi\_i}{1-\\pi\_i}&=&\\beta\_0 + \\beta\_1X\_{i1} + \\ldots + \\beta\_p X\_{ip} \\end{array}\\right. \\end{equation}\\$$</span>

### <span class="header-section-number">9.4.1</span> Categorische predictor

We illustreren logistische regressie aan de hand van het borstkanker voorbeeld waar we bestuderen of de BRCA 1 variant geassocieerd is met het krijgen van borstkanker (zie Sectie [9.3.2](index.md)).

Net zoals in de anova context, kunnen we een factor in het regressieraamwerk introduceren door gebruik te maken van dummy variabelen. We zullen hierbij 1 dummy variable minder nodig hebben dan er groepen zijn.

Voor het BRCA 1 voorbeeld zijn dus twee dummy variabelen nodig en kunnen we de data dus modelleren met onderstaande lineaire predictor:

<span class="math display">\\$$\\begin{eqnarray\*} \\log \\frac{\\pi\_i}{1-\\pi\_i} &=& \\beta\_0+\\beta\_1 x\_{i1} +\\beta\_2 x\_{i2} \\end{eqnarray\*}\\$$</span>

Waarbij de predictoren dummy-variabelen zijn: <span class="math display">\\$$x\_{i1} = \\left\\{ \\begin{array}{ll} 1 & \\text{ als subject \$i\$ heterozygoot is, Pro/Leu variant} \\\\ 0 & \\text{ als subject \$i\$ homozygoot is, (Pro/Pro of Leu/Leu variant)} \\end{array}\\right. .\\$$</span> en <span class="math display">\\$$x\_{i2} = \\left\\{ \\begin{array}{ll} 1 & \\text{ als subject \$i\$ homozygoot is in de Leucine mutatie: Leu/Leu variant} \\\\ 0 & \\text{ als subject \$i\$ niet homozygoot is in de Leu/Leu variant} \\end{array}\\right. .\\$$</span>

Homozygositeit in het wild type allel Pro/Pro wordt voor dit model de **referentiegroep**.

Het model wordt als volgt in R gefit:

``` {.sourceCode .r}
brcaLogit <- glm(cancer~variant,data=brca,family=binomial)
summary(brcaLogit)
```

    ##
    ## Call:
    ## glm(formula = cancer ~ variant, family = binomial, data = brca)
    ##
    ## Deviance Residuals:
    ##    Min      1Q  Median      3Q     Max
    ## -1.379  -1.286   1.017   1.017   1.073
    ##
    ## Coefficients:
    ##                Estimate Std. Error z value Pr(>|z|)
    ## (Intercept)     0.25131    0.08175   3.074  0.00211 **
    ## variantpro/leu  0.13802    0.11573   1.193  0.23302
    ## variantleu/leu  0.21197    0.18915   1.121  0.26243
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ##
    ## (Dispersion parameter for binomial family taken to be 1)
    ##
    ##     Null deviance: 1863.9  on 1371  degrees of freedom
    ## Residual deviance: 1861.9  on 1369  degrees of freedom
    ## AIC: 1867.9
    ##
    ## Number of Fisher Scoring iterations: 4

Het intercept is de log-odds op kanker in de referentieklasse (Pro/Pro) en de hellingstermen zijn log odds ratio’s tussen de behandeling en de referentieklasse: <span class="math display">\\$$\\begin{eqnarray\*} \\log \\text{ODDS}\_\\text{Pro/Pro}&=&\\beta\_0\\\\\\\\ \\log \\text{ODDS}\_\\text{Pro/Leu}&=&\\beta\_0+\\beta\_1\\\\\\\\ \\log \\text{ODDS}\_\\text{Leu/Leu}&=&\\beta\_0+\\beta\_2\\\\\\\\ \\log \\frac{\\text{ODDS}\_\\text{Pro/Leu}}{\\text{ODDS}\_\\text{Pro/Pro}}&=&\\log \\text{ODDS}\_\\text{Pro/Leu}-\\log ODDS\_{Pro/Pro}\\\\ &=&\\beta\_0+\\beta\_1-\\beta\_0=\\beta\_1\\\\\\\\ \\log \\frac{\\text{ODDS}\_\\text{Leu/Leu}}{\\text{ODDS}\_\\text{Pro/Pro}}&=&\\beta\_2 \\end{eqnarray\*}\\$$</span>

De analyse laat dus toe om de resultaten onmiddellijk te interpreteren in termen van Odds’es en Odds-ratio’s!

Net zoals bij een ANOVA analyse bij een continue response, kan de anova functie worden gebruikt voor het testen of er een associatie is tussen het voorkomen van kanker en de genetische variant.

``` {.sourceCode .r}
anova(brcaLogit,test="Chisq")
```

    ## Analysis of Deviance Table
    ##
    ## Model: binomial, link: logit
    ##
    ## Response: cancer
    ##
    ## Terms added sequentially (first to last)
    ##
    ##
    ##         Df Deviance Resid. Df Resid. Dev Pr(>Chi)
    ## NULL                     1371     1863.9
    ## variant  2   2.0562      1369     1861.9   0.3577

De <span class="math inline">\$\\chi^2\$</span>-test in het logistische regressiemodel geeft eveneens aan dat er geen significante associatie is tussen de uitkomst (voorkomen van kanker) en de factor ( de genetische variant van het BRCA gen) (<span class="math inline">\$p=\$</span> 0.358). De p-waarde is bijna equivalent aan de p-waarde van de <span class="math inline">\$\\chi^2\$</span>-test uit de vorige sectie.

Als er een significante associatie was geweest, dan hadden we post-hoc tests kunnen uitvoeren om te evalueren welke odds ratio’s verschillend zijn. Voor het BRCA1 voorbeeld zouden we uiteraard geen post-hoc testen uitvoeren omdat de globale <span class="math inline">\$\\chi^2\$</span>-test voor het testen van associatie niet significant is. We illustreren de post-hoc analyse toch zodat jullie over de code beschikken voor het uitvoeren van de analyses.

``` {.sourceCode .r}
library(multcomp)
posthoc=glht(brcaLogit,linfct=mcp(variant = "Tukey"))
posthocTests=summary(posthoc)
posthocTests
```

    ##
    ##   Simultaneous Tests for General Linear Hypotheses
    ##
    ## Multiple Comparisons of Means: Tukey Contrasts
    ##
    ##
    ## Fit: glm(formula = cancer ~ variant, family = binomial, data = brca)
    ##
    ## Linear Hypotheses:
    ##                        Estimate Std. Error z value Pr(>|z|)
    ## pro/leu - pro/pro == 0  0.13802    0.11573   1.193    0.449
    ## leu/leu - pro/pro == 0  0.21197    0.18915   1.121    0.493
    ## leu/leu - pro/leu == 0  0.07395    0.18922   0.391    0.917
    ## (Adjusted p values reported -- single-step method)

``` {.sourceCode .r}
posthocBI=confint(posthoc)
posthocBI
```

    ##
    ##   Simultaneous Confidence Intervals
    ##
    ## Multiple Comparisons of Means: Tukey Contrasts
    ##
    ##
    ## Fit: glm(formula = cancer ~ variant, family = binomial, data = brca)
    ##
    ## Quantile = 2.3265
    ## 95% family-wise confidence level
    ##
    ##
    ## Linear Hypotheses:
    ##                        Estimate lwr      upr
    ## pro/leu - pro/pro == 0  0.13802 -0.13123  0.40727
    ## leu/leu - pro/pro == 0  0.21197 -0.22809  0.65203
    ## leu/leu - pro/leu == 0  0.07395 -0.36627  0.51417

Door middel van de `confint` functie worden BI’s verkregen op de log-odds ratios die gecorrigeerd zijn voor multiple testing. Deze kunnen als volgt worden teruggetransformeerd naar odds ratios:

``` {.sourceCode .r}
OR=exp(posthocBI$confint)
OR
```

    ##                   Estimate       lwr      upr
    ## pro/leu - pro/pro 1.148000 0.8770178 1.502711
    ## leu/leu - pro/pro 1.236111 0.7960560 1.919426
    ## leu/leu - pro/leu 1.076752 0.6933150 1.672248
    ## attr(,"conf.level")
    ## [1] 0.95
    ## attr(,"calpha")
    ## [1] 2.326533

De odds ratios die worden bekomen met het logistisch regressiemodel zijn exact gelijk aan de odds ratios die we zouden bekomen op basis van Tabel [9.2](index.md): vb. <span class="math inline">\$\\text{OR}\_\\text{Leu/Leu-Pro/Pro}=89\\times 266/(56\\times 342)=\$</span> 1.236.

Merk op dat de statistische besluitvorming bij logistische modellen beroep doet op asymptotische theorie. Ze is dus enkel correct voor grote steekproeven.

### <span class="header-section-number">9.4.2</span> Continue predictor

Om het toxicologisch effect van een stof te kwantificeren worden dierproeven uitgevoerd waarbij dieren bij verschillende concentraties van de stof worden blootgesteld voor een bepaalde tijd. In dit voorbeeld wordt koolstofdisulfide (CS<span class="math inline">\$\_2\$</span>) bestudeerd in proeven met kevers. De centrale onderzoeksvraag is of de concentratie van CS<span class="math inline">\$\_2\$</span> een effect heeft op de mortaliteit (i.e. kans op sterven) van de kevers?

**Design** In 32 onafhankelijk experimenten wordt een kever blootgesteld aan één van 8 concentraties (mg/l) van CS<span class="math inline">\$\_2\$</span> voor een gegeven periode. De uitkomst van het experiment is: de kever sterft (<span class="math inline">\$y=1\$</span>) of de kever overleeft (<span class="math inline">\$y=0\$</span>). Een R object met de data is opgeslagen in de file `kevers.rda` in de dataset folder.

``` {.sourceCode .r}
load("dataset/kevers.rda")
head(kevers)
```

    ##    dosis status
    ## 1 169.07      1
    ## 2 169.07      0
    ## 3 169.07      0
    ## 4 169.07      0
    ## 5 172.42      1
    ## 6 172.42      0

``` {.sourceCode .r}
table(kevers$dosis,kevers$status)
```

    ##
    ##          0 1
    ##   169.07 3 1
    ##   172.42 3 1
    ##   175.52 3 1
    ##   178.42 2 2
    ##   181.13 1 3
    ##   183.69 0 4
    ##   186.1  0 4
    ##   188.39 0 4

We bouwen nu een logistisch regressiemodel waarbij we de log odds modelleren in functie van de dosis <span class="math inline">\$x\_i\$</span>: <span class="math display">\\$$\\log \\frac{\\pi\_i}{1-\\pi\_i}=\\beta\_0+\\beta\_1 \\times x\_i.\\$$</span>

``` {.sourceCode .r}
keverModel<-glm(status~dosis,data=kevers,family=binomial)
summary(keverModel)
```

    ##
    ## Call:
    ## glm(formula = status ~ dosis, family = binomial, data = kevers)
    ##
    ## Deviance Residuals:
    ##     Min       1Q   Median       3Q      Max
    ## -1.7943  -0.7136   0.2825   0.5177   2.1670
    ##
    ## Coefficients:
    ##             Estimate Std. Error z value Pr(>|z|)
    ## (Intercept) -53.1928    18.0046  -2.954  0.00313 **
    ## dosis         0.3013     0.1014   2.972  0.00296 **
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ##
    ## (Dispersion parameter for binomial family taken to be 1)
    ##
    ##     Null deviance: 42.340  on 31  degrees of freedom
    ## Residual deviance: 26.796  on 30  degrees of freedom
    ## AIC: 30.796
    ##
    ## Number of Fisher Scoring iterations: 5

Het intercept heeft als betekenis de log odds op mortaliteit wanneer er geen <span class="math inline">\$\\text{CS}\_2\$</span> gas wordt toegediend. Het duidt op een heel erg lage odds op sterfte (<span class="math inline">\$\\pi/(1-\\pi)=\\exp(-53.2)\$</span>) en dus op een kans die nagenoeg nul is. We verwachten inderdaad dat de kevers niet zullen sterven als we geen gas gebruiken in het experiment. Merk op dat de interpretatie van het intercept echter wel op een heel sterke extrapolatie berust gezien de minimum dosis in de dataset 169.07 mg/l bedroeg.

De geschatte odds ratio voor het effect van dosis op de mortaliteitskans is <span class="math inline">\$\\exp(0.3013)=1.35\$</span>. Dus bij een toename van de dosis CS<span class="math inline">\$\_2\$</span> met 1 mg/l, is de odds ratio voor de mortaliteit <span class="math inline">\$1.35\$</span>. We besluiten dat dit effect heel significant is (<span class="math inline">\$p=\$</span> 0.003). Een toename in de CS<span class="math inline">\$\_2\$</span> dosis doet de kans op sterven toenemen.

Figuur [9.6](index.md) toont de geschatte probabiliteit in functie van de dosis die werd gefit a.d.h.v. het regressiemodel. De figuur werd bekomen met onderstaande R code. We kunnen predicties voor nieuwe dosissen berekenen d.m.v. de `predict` functie. Het argument `type="response"` geeft aan dat we de predicties op de probabiliteitsschaal wensen. Wanneer we dat niet specifiëren genereert het model predictie op de log odds schaal.

``` {.sourceCode .r}
dosisGrid=seq(min(kevers$dosis),max(kevers$dosis),.1)
piHat=predict(keverModel,newdata=data.frame(dosis=dosisGrid),type="response")

plot(dosisGrid, piHat, type="l",ylim=c(0,1), xlab="dosis", ylab="Prob(dood)")

#omdat we meerdere observaties hebben voor elke dosis,
#zullen we berekenen hoeveel kevers er leefden voor elke dosis
#en dat uitzetten in de grafiek
#zodat de ruwe gegevens ook worden weergegeven.
tabKevers=table(kevers)
text(as.double(rownames(tabKevers)),0,labels=tabKevers[,1])
text(as.double(rownames(tabKevers)),1,labels=tabKevers[,2])
```

<span id="fig:keversFit"></span> <img src="Statistiek_2019_2020_files/figure-html/keversFit-1.png" style="width:100.0%" alt="Fit van het logistische regressiemodel voor de kevers data. Het aantal kevers die dood/levend was per dosis is weergegeven met een cijfer." />

Figuur 9.6: Fit van het logistische regressiemodel voor de kevers data. Het aantal kevers die dood/levend was per dosis is weergegeven met een cijfer.

### References {#references}

Rogovin, Konstantin A., Anastasiya M. Khrushchova, Olga N. Shekarova, Nina A. Vasilieva, and Nina Yu Vasilieva. 2017. “Females Choose Gentle, but Not Healthy or Macho Males in Campbell Dwarf Hamsters (Phodopus Campbelli Thomas 1905).” *Current Zoology* 63 (5): 545–54. doi:[10.1093/cz/zow090](https://doi.org/10.1093/cz/zow090).

------------------------------------------------------------------------

1.  Wees voorzichtig als je een binomiaalcoëfficient met een zakrekenmachine berekent. Teller en noemer kunnen snel zeer groot worden. Om (afrondings)fouten te vermijden moet men de uitdrukking eerst zoveel mogelijk vereenvoudigen.[↩](index.md)

2.  Indien de partnerkeuze niet geassocieerd zou zijn van de omgeving, verwachten we dat deze kansen (<span class="math inline">\$\\pi\_1\$</span> en <span class="math inline">\$\\pi\_2\$</span>) gelijk zijn op populatieniveau. Als we een associatie verwachten, met name partnerkeuze wordt beïnvloed door omgeving, dan zouden we verwachten dat vele hamsters zouden “switchen” van partnervoorkeur als ze uit een andere omgeving komen. De observaties waarbij geswitch wordt van partner worden discordante paren genoemd[↩](index.md)

3.  Inderdaad, vermits de variantie onder de nulhypothese exact gekend is, moet er geen correctie worden uitgevoerd voor het schatten van de variantie en kunnen we de z-test gebruiken.[↩](index.md)

4.  heterozygoot Pro/Leu of homozygoot Pro/Pro[↩](index.md)

5.  Indien de ene kwalitatieve variabele 2 waarden aanneemt, bvb, succes of faling, dan kan deze toets gebruikt worden om na te gaan of de kans op succes verschilt tussen strata van de andere kwalitatieve variabele.[↩](index.md)

---

[← 9.3 Toets voor associatie tussen 2 kwalitatieve variabelen](03-9-3-toets-voor-associatie-tussen-2-kwalitatieve-variabelen.md) · [Up: contents](index.md)

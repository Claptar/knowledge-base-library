---
title: '7.3 Post hoc analyse: Meervoudig Vergelijken van Gemiddelden'
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-anova.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-anova.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 7.3 Post hoc analyse: Meervoudig Vergelijken van Gemiddelden

**Source:** [`chap-anova.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-anova.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">7.3.1</span> Naïeve methode {#naïeve-methode}

In het eerste deel van dit hoofdstuk hebben we een <span class="math inline">\$F\$</span>-test besproken die gebruikt kan worden voor het testen van

<span class="math display">\\$$ H\_0: \\mu\_1=\\cdots = \\mu\_g \\text{ versus } H\_1: \\text{niet } H\_0.\\$$</span> Dus als de nulhypothese verworpen wordt, dan wordt besloten dat er minstens twee gemiddelden verschillen van elkaar. De methode stelt ons echter niet in staat om te identificeren welke gemiddelden van elkaar verschillen.

Een eerste, maar naïeve benadering van het probleem bestaat erin om de nulhypothese op te splitsen in partiële hypotheses <span class="math display">\\$$H\_{0jk}: \\mu\_j=\\mu\_k \\text{ versus } H\_{1jk}: \\mu\_j \\neq \\mu\_k\\$$</span> en deze partiële hypotheses te testen met two-sample <span class="math inline">\$t\$</span>-testen. Voor het vergelijken van groep <span class="math inline">\$j\$</span> met groep <span class="math inline">\$k\$</span> wordt de klassieke two-sample <span class="math inline">\$t\$</span>-test onder de veronderstelling van homoscedasticiteit gegeven door <span class="math display">\\$$T\_{jk} = \\frac{\\bar{Y}\_j-\\bar{Y}\_k}{S\_p\\sqrt{\\frac{1}{n\_j}+\\frac{1}{n\_k}}} \\sim t\_{n-2}\\$$</span> waarin <span class="math inline">\$S\_p^2\$</span> de gepoolde variantieschatter is, <span class="math display">\\$$S\_p^2 = \\frac{(n\_j-1)S\_j^2 + (n\_k-1)S\_k^2}{n\_j+n\_k-2}\\$$</span> met <span class="math inline">\$S\_j^2\$</span> en <span class="math inline">\$S\_k^2\$</span> de steekproefvarianties van respectievelijk de uitkomsten uit groep <span class="math inline">\$j\$</span> en <span class="math inline">\$k\$</span>.

In een ANOVA context wordt echter verondersteld dat in **alle** <span class="math inline">\$g\$</span> groepen de variantie van de uitkomsten dezelfde is (de residuele variantie <span class="math inline">\$\\sigma^2\$</span>). Indien we dus <span class="math inline">\$S\_p^2\$</span> gebruiken, dan is dit niet de meest efficiënte schatter omdat deze niet van alle data gebruik maakt<a href="#fn48" id="fnref48" class="footnoteRef"><sup>48</sup></a>. We kunnen dus efficiëntie winnen door MSE te gebruiken. Ter herinnering, MSE kan geschreven worden als <span class="math display">\\$$\\text{MSE}= \\sum\_{j=1}^g \\frac{(n\_j-1)S\_j^2}{n-g}.\\$$</span> De <span class="math inline">\$t\$</span>-testen voor het twee-aan-twee vergelijken van alle gemiddelden worden dus best gebaseerd op <span class="math display">\\$$T\_{jk} = \\frac{\\bar{Y}\_j-\\bar{Y}\_k}{\\text{MSE}\\sqrt{\\frac{1}{n\_j}+\\frac{1}{n\_k}}} \\sim t\_{n-g}.\\$$</span>

We zullen hier eerst demonstreren dat het werken met <span class="math inline">\$m\$</span>-testen op het <span class="math inline">\$\\alpha\$</span> significantieniveau een foute aanpak is die de kans op een type I fout niet onder controle kan houden. Dit zal aanleiding geven tot een meer algemene definitie van de type I fout.

Alvorens de denkfout in de naïeve aanpak te demonsteren via simulaties, tonen we hoe de naïeve benadering in zijn werk zou gaan voor het prostacycline voorbeeld.

``` {.sourceCode .r}
with(prostacyclin,pairwise.t.test(prostac,dose,"none"))
```

    ##
    ##  Pairwise comparisons using t tests with pooled SD
    ##
    ## data:  prostac and dose
    ##
    ##    10      25
    ## 25 0.34927 -
    ## 50 2e-05   0.00031
    ##
    ## P value adjustment method: none

Deze output toont de tweezijdige <span class="math inline">\$p\$</span>-waarden voor het testen van alle partiële hypotheses. We zouden hier kunnen besluiten dat het gemiddelde prostacycline niveau extreem significant verschillend is tussen de hoge en de lage dosis groep en tussen de hoge en de matige dosis groep (beide <span class="math inline">\$p&lt;&lt;0.001\$</span>). Verder is het gemiddelde prostacycline niveau niet significant verschillend is tussen de matige en de lage dosis groep.

In onderstaande R code wordt een simulatiestudie opgezet (herhaalde steekproefname).

1.  We simuleren uit een ANOVA model met <span class="math inline">\$g=3\$</span> groepen.
2.  De gemiddelden in het ANOVA model zijn gelijk aan elkaar, zodat de nulhypothese <span class="math display">\\$$H\_0: \\mu\_1=\\mu\_2=\\mu\_3\\$$</span> opgaat.
3.  Voor iedere gesimuleerde dataset zijn er <span class="math inline">\$m=3\$</span> paarsgewijze two-sample <span class="math inline">\$t\$</span>-testen
4.  Zodra minstens één van de <span class="math inline">\$p\$</span>-waarden kleiner is dan het significantieniveau <span class="math inline">\$\\alpha=5\\%\$</span>, wordt de nulhypothese <span class="math inline">\$H\_0: \\mu\_1=\\mu\_2=\\mu\_3\$</span> verworpen omdat er minstens twee gemiddelden verschillend zijn volgens de <span class="math inline">\$t\$</span>-testen.
5.  We rapporteren de relatieve frequentie van het verwerpen van de globale nulhypothese, meer bepaald de kans op een type I fout van de test voor <span class="math inline">\$H\_0: \\mu\_1=\\mu\_2=\\mu\_3\$</span>.

``` {.sourceCode .r}
g<-3 # aantal behandelingen (g=3)
ni<-12 # aantal herhalingen in iedere groep
n<-g*ni # totaal aantal observaties
alpha<-0.05 # significantieniveau van een individuele test
N=10000 #aantal simulaties
set.seed(302) #seed zodat resultaten exact geproduceerd kunnen worden
trt=factor(rep(1:g,ni)) #factor
cnt<-0 #teller voor aantal foutieve verwerpingen
for(i in 1:N) {
if (i%%1000==0) cat(i,"/",N,"\n")
y <- rnorm(n)
tests<-pairwise.t.test(y,trt,"none")
verwerp<-min(tests$p.value,na.rm=T)<alpha
if(verwerp) cnt<-cnt+1
}
```

    ## 1000 / 10000
    ## 2000 / 10000
    ## 3000 / 10000
    ## 4000 / 10000
    ## 5000 / 10000
    ## 6000 / 10000
    ## 7000 / 10000
    ## 8000 / 10000
    ## 9000 / 10000
    ## 10000 / 10000

``` {.sourceCode .r}
cnt/N
```

    ## [1] 0.1209

De simulatiestudie toont aan dat de kans op een type I fout gelijk is aan 12.1%, wat meer dan dubbel zo groot is dan de vooropgestelde <span class="math inline">\$\\alpha=5\\%\$</span>. Als we de simulatiestudie herhalen met <span class="math inline">\$g=5\$</span> groepen (i.e. m=g(g-1)/2=10 paarsgewijze <span class="math inline">\$t\$</span>-testen) dan vinden we <span class="math inline">\$28.0\\%\$</span> in plaats van de gewenste <span class="math inline">\$5\\%\$</span>. Deze simulaties illustreren het probleem van **multipliciteit** (Engels: *multiplicity*): de klassieke <span class="math inline">\$p\$</span>-waarden mogen enkel met het significantieniveau <span class="math inline">\$\\alpha\$</span> vergeleken worden, indien het besluit op exact één <span class="math inline">\$p\$</span>-waarde gebaseerd is. Hier wordt het finale besluit (aldanniet verwerpen van <span class="math inline">\$H\_0: \\mu\_1=\\cdots =\\mu\_g\$</span>) gebaseerd op <span class="math inline">\$m=g\\times(g-1)/2\$</span> <span class="math inline">\$p\$</span>-waarden, met <span class="math inline">\$g\$</span> het aantal groepen.

In de volgende sectie breiden we het begrip van type I fout uit en introduceren we enkele oplossingen om met multipliciteit om te gaan.

### <span class="header-section-number">7.3.2</span> Family-wise error rate

Wanneer <span class="math inline">\$m&gt;1\$</span> toetsen worden aangewend om 1 beslissing te vormen, is het noodzakelijk te corrigeren voor het risico op vals positieve resultaten<a href="#fn49" id="fnref49" class="footnoteRef"><sup>49</sup></a>. Meeste procedures voor meervoudig toetsen gaan ervan uit dat *alle <span class="math inline">\$m\$</span> nulhypotheses waar* zijn. Er wordt dan geprobeerd om het *risico op minstens 1 vals positief resultaat* te controleren op **experimentgewijs significantieniveau <span class="math inline">\$\\alpha\_E\$</span>**, typisch <span class="math inline">\$\\alpha\_E=0.05\$</span>. In de engelstalige literatuur wordt het experimentgewijs significantieniveau *family-wise error rate (FWER)* genoemd.

#### <span class="header-section-number">7.3.2.1</span> Bonferroni correctie

Bij het uitvoeren van <span class="math inline">\$m\$</span> onafhankelijke toetsen met elk significantieniveau <span class="math inline">\$\\alpha\$</span>, is <span class="math display">\\$$\\begin{eqnarray\*} \\alpha\_E&=&\\text{P}\[\\text{minstens 1 Type I fout}$$\\\\ &=&1-(1-\\alpha)^m \\leq m\\alpha \\end{eqnarray\*}\\\]</span>

- Als we 5 toetsen uitvoeren op het 5% significantieniveau is FWER <span class="math inline">\$\\approx 25\\%\$</span>.
- Door ze op het 1% significantieniveau uit te voeren, bekomen we FWER <span class="math inline">\$\\approx 5\\%\$</span>.

De Bonferroni correctie houdt de FWER begrensd op <span class="math inline">\$\\alpha\_E\$</span> door <span class="math display">\\$$\\alpha=\\alpha\_E/m\\$$</span> te kiezen voor het uitvoeren van de <span class="math inline">\$m\$</span> paarsgewijze vergelijkingen. Als alternatieve methode kunnen we ook

1.  *aangepaste p-waarden* rapporteren zodat we deze met het experimentgewijze <span class="math inline">\$\\alpha\_E\$</span> niveau kunnen vergelijken: <span class="math display">\\$$\\tilde{p}=min(m\\times p,1)\\$$</span>
2.  <span class="math inline">\$(1-\\alpha\_E/m)100\\%\$</span> betrouwbaarheidsintervallen rapporteren.

Het gebruik van aangepaste p-waarden heeft als voordeel dat de lezer deze zelf kan interpreteren en hij/zij een maat kan geven voor de significantie op het experimentsgewijs significantie niveau. Merk op dat we de aangepaste p-waarden begrenzen op <span class="math inline">\$\\tilde{p}=1\$</span> omdat p-waarden kansen zijn en steeds tussen 0 en 1 dienen te liggen.

Onderstaande R code geeft de resultaten (gecorrigeerde <span class="math inline">\$p\$</span>-waarden) na correctie met de methode van Bonferroni.

``` {.sourceCode .r}
with(prostacyclin,pairwise.t.test(prostac,dose, data = prostacyclin, p.adjust.method="bonferroni"))
```

    ##
    ##  Pairwise comparisons using t tests with pooled SD
    ##
    ## data:  prostac and dose
    ##
    ##    10      25
    ## 25 1.00000 -
    ## 50 6e-05   0.00094
    ##
    ## P value adjustment method: bonferroni

De conclusies blijven hetzelfde behalve dat de FWER nu gecontroleerd is <span class="math inline">\$\\alpha=5\\%\$</span> en de <span class="math inline">\$\\tilde{p}\$</span>-waarden een factor 3 groter zijn.

Dezelfde analyse kan uitgevoerd worden met het `multcomp` R package dat speciaal werd ontwikkeld voor multipliciteit in lineaire modellen.

``` {.sourceCode .r}
library(multcomp)
model1.mcp<-glht(model1,linfct=mcp(dose="Tukey"))
summary(model1.mcp,test=adjusted("bonferroni"))
```

    ##
    ##   Simultaneous Tests for General Linear Hypotheses
    ##
    ## Multiple Comparisons of Means: Tukey Contrasts
    ##
    ##
    ## Fit: lm(formula = prostac ~ dose, data = prostacyclin)
    ##
    ## Linear Hypotheses:
    ##              Estimate Std. Error t value Pr(>|t|)
    ## 25 - 10 == 0    8.258      8.698   0.949 1.000000
    ## 50 - 10 == 0   43.258      8.698   4.974 5.98e-05 ***
    ## 50 - 25 == 0   35.000      8.698   4.024 0.000943 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## (Adjusted p values reported -- bonferroni method)

Om Bonferroni aangepaste betrouwbaarheidsintervallen te verkrijgen moeten we eerst zelf functie definiëren in R om bonferroni kritische waarde te bepalen. We noemen deze functie `calpha_bon_t`.

``` {.sourceCode .r}
calpha_bon_t<-function(object,level) abs(qt((1-level)/2/nrow(object$linfct), object$df))
confint(model1.mcp,calpha=calpha_bon_t)
```

    ##
    ##   Simultaneous Confidence Intervals
    ##
    ## Multiple Comparisons of Means: Tukey Contrasts
    ##
    ##
    ## Fit: lm(formula = prostac ~ dose, data = prostacyclin)
    ##
    ## Quantile = 2.5222
    ## 95% confidence level
    ##
    ##
    ## Linear Hypotheses:
    ##              Estimate lwr      upr
    ## 25 - 10 == 0   8.2583 -13.6790  30.1957
    ## 50 - 10 == 0  43.2583  21.3210  65.1957
    ## 50 - 25 == 0  35.0000  13.0626  56.9374

We zullen nu het effect van de Bonferroni correctie opnieuw nagaan via simulaties.

``` {.sourceCode .r}
g<-3 # aantal behandelingen (g=3)
ni<-12 # aantal herhalingen in iedere groep
n<-g*ni # totaal aantal observaties
alpha<-0.05 # significantieniveau van een individuele test
N=10000 #aantal simulaties
set.seed(302) #seed zodat resultaten exact geproduceerd kunnen worden
trt=factor(rep(1:g,ni)) #factor
cnt<-0 #teller voor aantal foutieve verwerpingen
for(i in 1:N) {
if (i%%1000==0) cat(i,"/",N,"\n")
y <- rnorm(n)
tests<-pairwise.t.test(y,trt,"bonferroni")
verwerp<-min(tests$p.value,na.rm=T)<alpha
if(verwerp) cnt<-cnt+1
}
```

    ## 1000 / 10000
    ## 2000 / 10000
    ## 3000 / 10000
    ## 4000 / 10000
    ## 5000 / 10000
    ## 6000 / 10000
    ## 7000 / 10000
    ## 8000 / 10000
    ## 9000 / 10000
    ## 10000 / 10000

``` {.sourceCode .r}
cnt/N
```

    ## [1] 0.0457

We vinden dus een FWER van 4.6% (een beetje conservatief). Wanneer we de simulaties doen voor <span class="math inline">\$g=5\$</span> groepen, vinden we een FWER van <span class="math inline">\$4.1\\%\$</span> (conservatiever). Door de Bonferroni correctie is de kans op minstens één vals positief resultaat <span class="math inline">\$&lt; \\alpha\_E\$</span>. Hoewel de FWER wordt gecontroleerd door de Bonferroni methode, kan een verlies aan power worden verwacht aangezien het werkelijke niveau lager is dan het vooropgestelde 5% experimentsgewijs significantieniveau.

#### <span class="header-section-number">7.3.2.2</span> Methode van Tukey

De methode van Tukey is een minder conservatieve methode voor het uitvoeren van post hoc testen. De implementatie benadert de nuldistributie van de posthoc test d.m.v. simulaties. De resultaten kunnen daarom lichtjes verschillen wanneer je de posthoc analyse opnieuw uitvoert.
De details van de methode vallen buiten het bestek van deze cursus. Via de implementatie in het multcomp package kunnen we opnieuw aangepaste p-waarden verkrijgen en aangepaste betrouwbaarheidsintervallen voor alle <span class="math inline">\$m\$</span> paarsgewijze testen. We hoeven zelf geen functies te definiëren voor het verkrijgen van Tukey gecorrigeerde BIs.

``` {.sourceCode .r}
model1.mcp<-glht(model1,linfct=mcp(dose="Tukey"))
summary(model1.mcp)
```

    ##
    ##   Simultaneous Tests for General Linear Hypotheses
    ##
    ## Multiple Comparisons of Means: Tukey Contrasts
    ##
    ##
    ## Fit: lm(formula = prostac ~ dose, data = prostacyclin)
    ##
    ## Linear Hypotheses:
    ##              Estimate Std. Error t value Pr(>|t|)
    ## 25 - 10 == 0    8.258      8.698   0.949 0.613390
    ## 50 - 10 == 0   43.258      8.698   4.974  < 1e-04 ***
    ## 50 - 25 == 0   35.000      8.698   4.024 0.000835 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## (Adjusted p values reported -- single-step method)

``` {.sourceCode .r}
confint(model1.mcp)
```

    ##
    ##   Simultaneous Confidence Intervals
    ##
    ## Multiple Comparisons of Means: Tukey Contrasts
    ##
    ##
    ## Fit: lm(formula = prostac ~ dose, data = prostacyclin)
    ##
    ## Quantile = 2.4539
    ## 95% family-wise confidence level
    ##
    ##
    ## Linear Hypotheses:
    ##              Estimate lwr      upr
    ## 25 - 10 == 0   8.2583 -13.0849  29.6016
    ## 50 - 10 == 0  43.2583  21.9151  64.6016
    ## 50 - 25 == 0  35.0000  13.6567  56.3433

Merk op dat de Tukey methode smallere BIs en kleinere aangepaste p-waarden teruggeeft dan Bonferroni en dus minder conservatief is. De betrouwbaarheidsintervallen kunnen ook grafisch worden weergegeven wat handig is als er veel vergelijkingen worden uitgevoerd (zie Figuur [7.6](index.md)).

``` {.sourceCode .r}
plot(confint(model1.mcp))
```

<span id="fig:prostacTukey"></span> <img src="Statistiek_2019_2020_files/figure-html/prostacTukey-1.png" style="width:100.0%" alt="$95\%$ experimentsgewijze betrouwbaarheidsintervallen voor de paarsgewijze verschillen in gemiddeld prostacycline niveau tussen alle arachidonzuur dosisgroepen. De BIs zijn gecorrigeerd voor multipliciteit via de Tukey methode." />

Figuur 7.6: <span class="math inline">\$95\\%\$</span> experimentsgewijze betrouwbaarheidsintervallen voor de paarsgewijze verschillen in gemiddeld prostacycline niveau tussen alle arachidonzuur dosisgroepen. De BIs zijn gecorrigeerd voor multipliciteit via de Tukey methode.

Hierop zien we onmiddellijk dat het effect van de hoogste dosisgroep verschillend is van de laagste en middelste dosisgroep en dat er geen significant verschil is tussen de laagste en de middelste dosisgroep op het 5% experimentsgewijze significantieniveau.

Tenslotte gaan we ook via simulatie na of de Tukey methode de FWER correct kan controleren.

``` {.sourceCode .r}
g<-3 # aantal behandelingen (g=3)
ni<-12 # aantal herhalingen in iedere groep
n<-g*ni # totaal aantal observaties
alpha<-0.05 # significantieniveau van een individuele test
N=10000 #aantal simulaties
set.seed(302) #seed zodat resultaten exact geproduceerd kunnen worden
trt=factor(rep(1:g,ni)) #factor
cnt<-0 #teller voor aantal foutieve verwerpingen
for(i in 1:N) {
if (i%%1000==0) cat(i,"/",N,"\n")
y <- rnorm(n)
m<-lm(y~trt)
m.mcp<-glht(m,linfct=mcp(trt="Tukey"))
tests<-summary(m.mcp)$test
verwerp<-min(as.numeric(tests$pvalues),na.rm=T)<alpha
if(verwerp) cnt<-cnt+1
}
```

    ## 1000 / 10000
    ## 2000 / 10000
    ## 3000 / 10000
    ## 4000 / 10000
    ## 5000 / 10000
    ## 6000 / 10000
    ## 7000 / 10000
    ## 8000 / 10000
    ## 9000 / 10000
    ## 10000 / 10000

``` {.sourceCode .r}
cnt/N
```

    ## [1] 0.0503

We vinden dus een FWER van <span class="math inline">\$5.03\\%\$</span> wat heel dicht hij het nominale FWER<span class="math inline">\$=5\\%\$</span> ligt. Voor <span class="math inline">\$g=5\$</span> groepen, vinden we een FWER van <span class="math inline">\$5.2\\%\$</span>, wat ook vrij goed is.<a href="#fn50" id="fnref50" class="footnoteRef"><sup>50</sup></a>

---

[← 7.2 Variantie-analyse](02-7-2-variantie-analyse.md) · [Up: contents](index.md) · [7.4 Conclusies: Prostacycline Voorbeeld →](04-7-4-conclusies-prostacycline-voorbeeld.md)

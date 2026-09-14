---
title: Wat doet onze functies?
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/niet-parametrische-statistiek.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/niet-parametrische-statistiek.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Wat doet onze functies?

**Source:** [`niet-parametrische-statistiek.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/niet-parametrische-statistiek.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

#Er wordt een t-test uitgevoerd na het permuteren van
#de groepslabels sample(groep).
#De t-statistic wordt teruggegeven.
head(tStar2)
```

    ##          t          t          t          t          t          t
    ##  1.8043424  1.1215813 -0.8768193 -1.0377368 -0.1884269  1.0377368

``` {.sourceCode .r}
pval2=(sum(abs(tStar2)>=mean(tOrig))+1)/(B+1)
pval2
```

    ## [1] 0.01769823

``` {.sourceCode .r}
par(mfrow=c(2,1))
plot(table(tStar2),type="h",xaxt="n",
     xlab=expression("permutatiestatistiek t"^"*"))
axis(1,at=-4:4)
abline(v=tOrig,col=2,lwd=2)
hist(tStar2,
     xlab=expression("permutatiestatistiek t"^"*"))
abline(v=tOrig,col=2,lwd=2)
```

<span id="fig:tPermDist2"></span> <img src="Statistiek_2019_2020_files/figure-html/tPermDist2-1.png" style="width:100.0%" alt="Approximatieve permutatie nulldistributie van de Welch t-test voor het cholestorol voorbeeld op basis van 10000 permutaties. De geobserveerde waarde voor de test-statistiek is aangeduid met een rode verticale lijn." />

Figuur 8.3: Approximatieve permutatie nulldistributie van de Welch t-test voor het cholestorol voorbeeld op basis van 10000 permutaties. De geobserveerde waarde voor de test-statistiek is aangeduid met een rode verticale lijn.

We vinden een approximatieve <span class="math inline">\$p\$</span>-waarde van 0.0177, wat niet ver verwijderd is van de exacte <span class="math inline">\$p\$</span>-waarde (p=0.0159) die we eerder berekend hadden. Het histogram van de approximatieve permutatiedistributie is weergegeven in Figuur [8.3](index.md).

### <span class="header-section-number">8.2.3</span> Rank Testen

De ontwikkeling van rank testen startte in de eerste helft van de twintigste eeuw, maar ze vormen vandaag nog steeds de belangrijkste groep van niet-parametrische testen. Aanvankelijk hadden ze hun populariteit te danken aan het feit dat ze niet-parametrisch zijn en dat ze exacte <span class="math inline">\$p\$</span>-waarden geven op basis van de permutatienuldistributie. In tegenstelling tot de test besproken in de vorige sectie, hebben rank testen geen nood aan het numeriek opstellen van de permutatienuldistributie voor iedere nieuwe dataset. De permutatienuldistributie van rank testen hangt alleen af van de steekproefgroottes. Bovendien zal blijken dat de testen erg robust zijn tegen uitschieters (Engels: *outliers*) en dat ze nuttig zijn als het locatie-shift model niet opgaat.

Rank testen starten vanuit rank-getransformeerde uitkomsten.

<span id="def:unnamed-chunk-116" class="definition">**Definitie 8.1 (Rank)** </span>Beschouw <span class="math inline">\$Y\_1, \\ldots, Y\_n\$</span>. We veronderstellen voorlopig dat er geen twee gelijke observaties voorkomen (i.e. geen *ties*). De rank van observatie <span class="math inline">\$Y\_i\$</span> wordt dan gedefinieerd als <span class="math display">\\$$\\begin{equation\*} R\_i=R(Y\_i) = \\#\\{Y\_j: Y\_j\\leq Y\_i; j=1,\\ldots, n\\}. \\end{equation\*}\\$$</span>

De kleinste observatie krijgt dus rank 1, de tweede kleinste rank 2, enzovoort, en de grootste observatie, tenslotte, krijgt rank <span class="math inline">\$n\$</span>.

**Einde Definitie**

De rank transformatie wordt geïllustreerd op basis van het cholestorol voorbeeld.

``` {.sourceCode .r}
sort(chol$cholest)
```

    ##  [1] 160 186 188 198 206 212 236 242 244 278

``` {.sourceCode .r}
rank(sort(chol$cholest))
```

    ##  [1]  1  2  3  4  5  6  7  8  9 10

``` {.sourceCode .r}
chol$cholest
```

    ##  [1] 244 206 242 278 236 188 212 186 198 160

``` {.sourceCode .r}
rank(chol$cholest)
```

    ##  [1]  9  5  8 10  7  3  6  2  4  1

Soms komen *ties* voor in de data, i.e. minstens twee observaties hebben dezelfde numerieke waarde. Een klein voorbeeld:

``` {.sourceCode .r}
metTies=c(403,507,507,610,651,651,651,830,900)
rank(metTies)
```

    ## [1] 1.0 2.5 2.5 4.0 6.0 6.0 6.0 8.0 9.0

De numerieke waarde 507 komt tweemaal voor en de numerieke waarde 651 komt driemaal voor. Dit zijn voorbeelden van *ties*. Wanneer *ties* voorkomen, wordt dikwijls de definitie van *midranks* toegepast voor de rank-transformatie.

<span id="def:unnamed-chunk-119" class="definition">**Definitie 8.2 (Midrank)** </span>Beschouw <span class="math inline">\$Y\_1, \\ldots, Y\_n\$</span>. De **midrank** van observatie <span class="math inline">\$Y\_i\$</span> wordt dan gedefinieerd als <span class="math display">\\$$\\begin{eqnarray\*} R\_i &=& \\frac{ \\#\\{Y\_j: Y\_j\\leq Y\_i\\} + ( \\#\\{Y\_j: Y\_j &lt; Y\_i\\} +1)}{2}. \\end{eqnarray\*}\\$$</span>

**Einde Definitie**

In wat volgt hebben we dikwijls de ranks van de uitkomsten nodig in de gepoolde steekproef. Bijvoorbeeld: beschouw de uitkomsten <span class="math inline">\$Y\_{ij}\$</span>, <span class="math inline">\$i=1,\\ldots, n\_j\$</span> en <span class="math inline">\$j=1,2\$</span>. Deze uitkomsten kunnen ook gerepresenteerd worden door <span class="math inline">\$Z\_1,\\ldots, Z\_n\$</span> (<span class="math inline">\$n=n\_1+n\_2\$</span>), de uitkomsten uit de gepoolde steekproef.

``` {.sourceCode .r}
chol
```

    ##    group cholest
    ## 1      1     244
    ## 2      1     206
    ## 3      1     242
    ## 4      1     278
    ## 5      1     236
    ## 6      2     188
    ## 7      2     212
    ## 8      2     186
    ## 9      2     198
    ## 10     2     160

``` {.sourceCode .r}
z=chol$cholest
z
```

    ##  [1] 244 206 242 278 236 188 212 186 198 160

``` {.sourceCode .r}
rank(z)
```

    ##  [1]  9  5  8 10  7  3  6  2  4  1

### <span class="header-section-number">8.2.4</span> Wilcoxon-Mann-Whitney Test

De test werd gelijktijdig ontwikkeld door Wilcoxon en door Mann en Whitney. Om deze reden wordt de test dikwijls de **Wilcoxon-Mann-Whitney** (WMW) test genoemd. Soms wordt de test ook de **Wilcoxon rank sum test** of de **Mann-Whitney U test** genoemd.

De test werd ontwikkeld voor het testen van de nulhypothese [(8.1)](index.md) tegenover het alternatief <span class="math inline">\$H\_1: \\mu\_1\\neq \\mu\_2\$</span> (of de eenzijdige versies). Eerst wordt er een distributionele veronderstelling gemaakt: het **locatie-shift** model, later relaxeren we deze aanname.

Stel dat <span class="math inline">\$Y\_1\$</span> en <span class="math inline">\$Y\_2\$</span> uitkomsten zijn uit respectievelijk de eerste en tweede behandelingsgroep, met respectievelijke verdelingen <span class="math inline">\$f\_1\$</span> en <span class="math inline">\$f\_2\$</span>. Het locatie-shift model geldt als er een <span class="math inline">\$\\Delta\$</span> bestaat waarvoor geldt <span class="math display">\\$$ f\_1(y)=f\_2(y-\\Delta) \\;\\;\\;\\text{ voor alle } y. \\$$</span>

Locatie-shift betekent dat <span class="math inline">\$f\_1\$</span> en <span class="math inline">\$f\_2\$</span> dezelfde vorm hebben, maar ze mogen over <span class="math inline">\$\\Delta\$</span> verschoven zijn. De <span class="math inline">\$\\Delta\$</span> uit de definitie heeft als interpretatie: <span class="math inline">\$\\Delta = \\mu\_1-\\mu\_2\$</span>. Door locatie-shift aan te nemen, zal het verwerpen van <span class="math inline">\$H\_0: f\_1=f\_2\$</span> de conclusie <span class="math inline">\$\\mu\_1\\neq \\mu\_2\$</span> impliceren.

De klassieke two-sample <span class="math inline">\$t\$</span>-teststatistiek is gebouwd rond het verschil in steekproefgemiddelden <span class="math inline">\$\\bar{Y}\_1-\\bar{Y}\_2\$</span>. We beschouwen nu ook het verschil in steekproefgemiddelden, maar niet op basis van de oorspronkelijke uitkomsten, maar op basis van de rank-getransformeerde uitkomsten. De ranks zijn toegekend op basis van de gepoolde observaties (i.e. na samenvoegen van de uitkomsten uit groep 1 en groep 2); dus <span class="math inline">\$R\_{ij}=R(Y\_{ij})\$</span> is de rank van uitkomst <span class="math inline">\$Y\_{ij}\$</span> in de gepoolde steekproef. Beschouw de teststatistiek <span class="math display">\\$$ T = \\frac{1}{n\_1}\\sum\_{i=1}^{n\_1} R(Y\_{i1}) - \\frac{1}{n\_2}\\sum\_{i=1}^{n\_2} R(Y\_{i2}) . \\$$</span>

De statistiek vergelijkt dus de gemiddelde rank in groep 1 met de gemiddelde rank in groep 2.

Dit is een zinvolle teststatistiek, want

- als <span class="math inline">\$H\_0\$</span> waar is, dan verwachten we dat de gemiddelde rank in de eerste groep ongeveer gelijk is aan de gemiddelde rank in de tweede groep en dus verwachten we dat <span class="math inline">\$T\$</span> dicht bij nul ligt.

- als <span class="math inline">\$H\_1\$</span> waar is dan verwachten we dat de gemiddelde ranks zullen verschillen en dus dat <span class="math inline">\$T\$</span> niet dicht bij nul zal liggen.

Er kan echter worden aangetoond dat het volstaat het om <span class="math display">\\$$S\_1=\\sum\_{i=1}^{n\_1} R(Y\_{i1})\\$$</span> als teststatistiek te beschouwen. <span class="math inline">\$S\_1\$</span> is de som van de ranks van de observaties uit de eerste behandelingsgroep; dit verklaart de naam *rank sum test*.

<span class="math inline">\$S\_1\$</span> en <span class="math inline">\$S\_2\$</span> bevatten immers dezelfde informatie en zijn gerelateerd via <span class="math display">\\$$ S\_1+S\_2 = \\text{som van alle ranks} = 1+2+\\cdots + n=\\frac{1}{2}n(n+1). \\$$</span>

Nu we weten dat <span class="math inline">\$S\_1\$</span> (en <span class="math inline">\$S\_2\$</span>) een goede teststatistiek is, kan de permutatietestmethode toegepast worden om de exacte permutatienuldistributie op te stellen en de test uit te voeren. Voor een gegeven steekproefgrootte <span class="math inline">\$n\$</span>, en veronderstellend dat er geen *ties* zijn, nemen de rank-getransformeerde uitkomsten altijd de waarden <span class="math inline">\$1, 2, \\ldots, n\$</span> aan. Voor gegeven groepsgroottes <span class="math inline">\$n\_1\$</span> en <span class="math inline">\$n\_2\$</span>, zal de permutatienuldistributie dan ook steeds dezelfde zijn! In de vorige eeuw (tot ongeveer de jaren 1980) werd dit als een groot voordeel beschouwd omdat de nuldistributies voor gegeven <span class="math inline">\$n\_1\$</span> en <span class="math inline">\$n\_2\$</span> getabuleerd konden worden (belangrijke kwantielen werden als tabellen in boeken gepubliceerd zodat ze konden gebruikt worden voor het bepalen van kritische waarden en <span class="math inline">\$p\$</span>-waarden), waardoor de gebruiker geen nood had aan zware rekencapaciteit. Vandaag de dag speelt dit argument niet meer mee, maar toch blijven de rank testen erg populair, maar dan wel om andere, heel belangrijke redenen.

Niettegenstaande <span class="math inline">\$S\_1\$</span> en <span class="math inline">\$S\_2\$</span> perfect als teststatistieken gebruikt kunnen worden, wordt dikwijls gewerkt met de gestandaardiseerde teststatistiek <span class="math display">\\$$ T = \\frac{S\_1-\\text{E}\_{0}\\left\[S\_1\\right$$}{\\sqrt{\\text{Var}\_{0}\\left$$S\_1\\right$$}}, \\\]</span> met <span class="math inline">\$\\text{E}\_{0}\\left$$S\_1\\right$$\$</span> en <span class="math inline">\$\\text{Var}\_{0}\\left$$S\_1\\right$$\$</span> de verwachtingswaarde en variantie van <span class="math inline">\$S\_1\$</span> onder <span class="math inline">\$H\_0\$</span>. Dit zijn dus het gemiddelde en variantie van de permutatienuldistributie van <span class="math inline">\$S\_1\$</span>.

Onder <span class="math inline">\$H\_0\$</span> geldt <span class="math display">\\$$ \\text{E}\_{0}\\left\[S\_1\\right$$= \\frac{1}{2}n\_1(n+1) \\;\\;\\;\\;\\text{ en }\\;\\;\\;\\; \\text{Var}\_{0}\\left$$S\_1\\right$$=\\frac{1}{12}n\_1n\_2(n+1). \\\]</span>

Verder kan men onder <span class="math inline">\$H\_0\$</span> en als <span class="math inline">\$\\min(n\_1,n\_2)\\rightarrow \\infty\$</span> opgaat aantonen dat, <span class="math display">\\$$ T = \\frac{S\_1-\\text{E}\_{0}\\left\[S\_1\\right$$}{\\sqrt{\\text{Var}\_{0}\\left$$S\_1\\right$$}} \\rightarrow N(0,1). \\\]</span>

Asymptotisch volgt de gestandaardiseerde teststatistiek dus een standaardnormaal verdeling.

We illustreren de WMW test aan de hand van de R functie `wilcox.test`.

``` {.sourceCode .r}
wilcox.test(cholest~group,data=chol)
```

    ##
    ##  Wilcoxon rank sum test
    ##
    ## data:  cholest by group
    ## W = 24, p-value = 0.01587
    ## alternative hypothesis: true location shift is not equal to 0

We zien dat we op basis van de test de nulhypothese kunnen verwerpen op het 5% significantie-niveau.

De output geeft de teststatistiek <span class="math inline">\$W=\$</span> 24. In volgende lijnen berekenen we <span class="math inline">\$S\_1\$</span> en <span class="math inline">\$S\_2\$</span> manueel voor de dataset.

``` {.sourceCode .r}
attach(chol)
S1=sum(rank(cholest)[group==1])
S1
```

    ## [1] 39

``` {.sourceCode .r}
S2=sum(rank(cholest)[group==2])
S2
```

    ## [1] 16

``` {.sourceCode .r}
detach(chol)
```

Waar komt <span class="math inline">\$W=\$</span> 24 vandaan? Dit wordt zodadelijk toegelicht.

De teststatistieken <span class="math inline">\$S\_1\$</span> en <span class="math inline">\$S\_2\$</span> werden voorgesteld door Wilcoxon, maar tezelfdertijd werd een equivalente test voorgesteld door Mann en Whitney. Hun teststatistiek wordt gegeven door<a href="#fn52" id="fnref52" class="footnoteRef"><sup>52</sup></a> <span class="math display">\\$$ U\_1 = \\sum\_{i=1}^{n\_1}\\sum\_{k=1}^{n\_2} \\text{I}\\left\\{Y\_{i1}\\geq Y\_{k2}\\right\\}. \\$$</span>

waarbij <span class="math inline">\$\\text{I}\\left\\{.\\right\\}\$</span> een indicator is die 1 is als de uitdrukking waar is en 0 als dit niet het geval is. Er wordt voor elke observatie uit de eerste groep geteld hoeveel keer zij groter of gelijk is aan een observatie uit de tweede groep. We berekenen de Mann-Whitney statistiek nu manueel in R.

``` {.sourceCode .r}
y1=subset(chol,group==1)$cholest
y2=subset(chol,group==2)$cholest
u1Hlp=sapply(y1,function(y1i,y2) {y1i>=y2},y2=y2)
colnames(u1Hlp)=y1
rownames(u1Hlp)=y2
u1Hlp
```

    ##      244   206  242  278  236
    ## 188 TRUE  TRUE TRUE TRUE TRUE
    ## 212 TRUE FALSE TRUE TRUE TRUE
    ## 186 TRUE  TRUE TRUE TRUE TRUE
    ## 198 TRUE  TRUE TRUE TRUE TRUE
    ## 160 TRUE  TRUE TRUE TRUE TRUE

``` {.sourceCode .r}
U1=sum(u1Hlp)
U1
```

    ## [1] 24

Er kan worden aangetoond dat

<span class="math display">\\$$U\_1 = S\_1 - \\frac{1}{2}n\_1(n\_1+1).\\$$</span>

``` {.sourceCode .r}
S1-nGroups[1]*(nGroups[1]+1)/2
```

    ##  1
    ## 24

Hieruit concluderen we (1) dat <span class="math inline">\$U\_1\$</span> en <span class="math inline">\$S\_1\$</span> dezelfde informatie bevatten, (2) dat <span class="math inline">\$U\_1\$</span> ook een rankstatistiek is en dat exacte testen gebaseerd op <span class="math inline">\$U\_1\$</span> en <span class="math inline">\$S\_1\$</span> equivalent zijn.

De statistiek <span class="math inline">\$U\_1\$</span> heeft als voordeel dat het een informatieve interpretatie heeft. Stel <span class="math inline">\$Y\_j\$</span> een willekeurige uitkomst uit behandelingsgroep <span class="math inline">\$j\$</span> (<span class="math inline">\$j=1,2\$</span>). Dan geldt <span class="math display">\\$$\\begin{eqnarray\*} \\frac{1}{n\_1n\_2}\\text{E}\\left\[U\_1\\right$$ &=& \\text{P}\\left$$Y\_1 \\geq Y\_2\\right$$. \\end{eqnarray\*}\\\]</span>

Intuïtief voelen we dit aan: Op basis van de steekproef kunnen we die kans schatten door het gemiddelde te berekenen van alle indicator waarden <span class="math inline">\$\\text{I}\\left\\{Y\_{i1}\\geq Y\_{k2}\\right\\}\$</span>. We voerden inderdaad <span class="math inline">\$n\_1 \\times n\_2\$</span> vergelijkingen uit.

``` {.sourceCode .r}
mean(u1Hlp)
```

    ## [1] 0.96

``` {.sourceCode .r}
U1/(nGroups[1]*nGroups[2])
```

    ##    1
    ## 0.96

De kans <span class="math inline">\$\\text{P}\\left$$Y\_1 \\geq Y\_2\\right$$\$</span> wordt een **probabilistische index** (Engels: *probabilistic index*) genoemd. Het is de kans dat een uitkomst uit de eerste groep groter of gelijk is dan een uitkomst uit de tweede groep. Als <span class="math inline">\$H\_0\$</span> waar is, dan is <span class="math inline">\$\\text{P}\\left$$Y\_1 \\geq Y\_2\\right$$=\\frac{1}{2}\$</span>.

De gestandaardiseerde Mann-Whitney statistiek is <span class="math display">\\$$ T = \\frac{U\_1 - \\frac{n\_1n\_2}{2}}{\\sqrt{\\frac{1}{12}n\_1n\_2(n+1)}}. \\$$</span>

De R functie `wilcox.test` geeft niet de Wilcoxon rank sum statistiek, maar wel de Mann-Whitney statistiek <span class="math inline">\$U\_1\$</span>. We weten echter dat exacte permutatietesten gebaseerd op <span class="math inline">\$U\_1\$</span>, <span class="math inline">\$U\_2\$</span>, <span class="math inline">\$S\_1\$</span> of <span class="math inline">\$S\_2\$</span> dezelfde resultaten geven. We bekijken nogmaals de output

``` {.sourceCode .r}
wTest=wilcox.test(cholest~group,data=chol)
wTest
```

    ##
    ##  Wilcoxon rank sum test
    ##
    ## data:  cholest by group
    ## W = 24, p-value = 0.01587
    ## alternative hypothesis: true location shift is not equal to 0

``` {.sourceCode .r}
U1
```

    ## [1] 24

``` {.sourceCode .r}
probInd=wTest$statistic/prod(nGroups)
probInd
```

    ##    W
    ## 0.96

Aangezien <span class="math inline">\$p=\$</span> 0.0159 <span class="math inline">\$&lt;0.05\$</span> besluiten we op het <span class="math inline">\$5\\%\$</span> significantieniveau dat de gemiddelde cholestorolconcentratie groter is bij hartpatiënten kort na een hartaanval dan bij gezonde personen. We nemen aan dat locatie-shift opgaat.

Nu we weten hoe <span class="math inline">\$U\_1\$</span> berekend wordt, weten we ook meteen dat een cholestorolwaarde van hartpatiënten met een kans van <span class="math inline">\$U1/(n\_1\\times n\_2)=\$</span> 96% groter is die van gezonde personen. Aangezien we het locatie-shift model veronderstellen, besluiten we ook dat de gemiddelde uitkomst uit de behandelingsgroep groter is dan de gemiddelde uitkomst uit de placebogroep.

We zouden de veronderstelling van de locatie-shift moeten nagaan, maar met slechts 5 observaties in elke behandelingsgroep is dit zinloos. Zonder verder theorie hierover te geven, geven we nog mee dat zonder de locatie-shift veronderstelling de conclusie in termen van de probabilistische index correct blijft en de conclusie ook zo zou moeten worden geformuleerd.

Dus wanneer we geen locatie-shift veronderstellen en een tweezijdige test uitvoeren testen we eigenlijk

<span class="math display">\\$$H\_0: F\_1=F\_2 \\text{ vs P}(Y\_1 \\geq Y\_2) \\neq 0.5.\\$$</span>

### <span class="header-section-number">8.2.5</span> Conclusie Cholestorol Voorbeeld

Er is een significant verschil in de distributie van de cholestorolconcentraties bij hartpatiënten 2 dagen na hun hartaanval en gezonde individuen (<span class="math inline">\$p=\$</span> 0.0159). Het is meer waarschijnlijk om hogere cholestorolconcentraties te observeren bij hartpatiënten dan bij gezonde individuen. De puntschatting voor deze kans bedraagt 96%.

## <span class="header-section-number">8.3</span> Vergelijken van <span class="math inline">\$g\$</span> Behandelingen

In deze sectie veralgemenen we de methoden uit de vorige sectie. De methoden kunnen ook gezien worden als niet-parametrische tegenhangers van de <span class="math inline">\$F\$</span>-test uit een one-way ANOVA.

### <span class="header-section-number">8.3.1</span> DMH Voorbeeld

Nieuwe (en bestaande) chemische substaties moeten getest worden op genotoxiciteit. De resultaten van genotoxiciteitstesten vormen de basis voor risic0-analyses en de classificatie en labeling van chemische substanties in de EU (*Dangerous Substances Directive 67/548/EEC and Regulation (EC) No. 1272/2008*). In dat kader werd een studie met 24 ratten opgezet voor het testen van de genotoxiciteit van 1,2-dimethylhydrazine dihydrochloride (DMH). De ratten werden at random verdeeld over vier groepen die een verschillende dagelijkse DMH dosis kregen toegediend (controle, laag, medium, hoog). Na drie weken werden de dieren afgemaakt en werd genotoxiciteit van DMH in de lever bepaald a.d.h.v. een comet assay waarbij DNA strengbreuken worden gevisualiseerd via gel electroforese. De lengte van de comet staart is een proxy voor het aantal strengbreuken. De onderzoekers wensen na te gaan of er verschillen zijn in de DNA schade tengevolge van de DMH dosis. Boxplots van de data worden weergegeven in Figuur [8.4](index.md).

``` {.sourceCode .r}
dna <- read.table("dataset/dna.txt",header=TRUE)
dna$dose <- as.factor(dna$dose)
par(mfrow=c(1,2))
boxplot(length~dose,data=dna,ylab="lengte",xlab="dosis",outline=FALSE,ylim=range(dna$length))
set.seed(10)
stripchart(length~dose,data=dna, vertical = TRUE, method = "jitter", pch = 19, col =c("bisque","coral","darkcyan","purple"),  add = TRUE)
set.seed(10)
stripchart(length~dose,data=dna, vertical = TRUE, method = "jitter", pch = 1,  add = TRUE)
boxplot(log(length)~dose,data=dna,ylab="log-lengte",xlab="dosis",outline=FALSE,ylim=range(log(dna$length)))
set.seed(10)
stripchart(log(length)~dose,data=dna, vertical = TRUE, method = "jitter", pch = 19, col =c("bisque","coral","darkcyan","purple"),  add = TRUE)
set.seed(10)
stripchart(log(length)~dose,data=dna, vertical = TRUE, method = "jitter", pch = 1,  add = TRUE)
```

<span id="fig:dnaBox"></span> <img src="Statistiek_2019_2020_files/figure-html/dnaBox-1.png" style="width:100.0%" alt="Boxplot van de comet staart lengte in functie van de DMH dosis." />

Figuur 8.4: Boxplot van de comet staart lengte in functie van de DMH dosis.

De boxplots lijken een indicatie te geven dat de controle groep een andere variabiliteit heeft. Merk wel op dat er slechts 6 observaties zijn per groep wat eigenlijk te weinig is om de aannames na te gaan.

### <span class="header-section-number">8.3.2</span> Permutatietest

Merk eerst op dat het one-way ANOVA model ook een locatie-shift impliceert. De distributies hebben opnieuw dezelfde vorm (normale verdeling met zelfde variantie) maar met een verschillend gemiddeld.

Onder de veronderstellingen van het one-way ANOVA model kunnen we de nulhypothese net zoals bij de permutatie t-test algemener formuleren: <span class="math display">\\$$\\begin{equation\*} H\_0: f\_1(y)=f\_2(y) = \\ldots = f\_t(y) \\text{ voor alle } y. \\end{equation\*}\\$$</span>

Nu veronderstellen we echter niet dat de densiteitsfuncties <span class="math inline">\$f(y)\$</span> normale distributies zijn.

Als we een locatie-shift model kunnen veronderstellen dan is de alternatieve hypothese analoog als bij de ANOVA test nl. <span class="math display">\\$$H\_1: \\exists\\ j,k \\in \\{1,\\ldots,g\\} : \\mu\_j\\neq\\mu\_k.\\$$</span>

We kunnen nu opnieuw de groepslabels permuteren om de nuldistributie van de test-statistiek te bekomen. Men kan aantonen dat er <span class="math display">\\$$m=\\frac{n!}{n\_1!\\ldots n\_g!}\\$$</span> unieke permutaties <span class="math inline">\$\\cal{G}\$</span> bestaan. Voor ons voorbeeld zijn dat er <span class="math inline">\$m=(24!)/(6!)^4=\$</span> 2.31e+12.

De permutatienuldistributie wordt opnieuw opgesteld door de F-teststatistiek te berekenen voor iedere <span class="math inline">\$g\\in \\cal{G}\$</span> of voor een willekeurige steekproef van permutaties uit <span class="math inline">\$\\cal{G}\$</span>.

Hieronder wordt de R code gegeven voor het benaderen van de <span class="math inline">\$p\$</span>-waarde op basis van 10000 willekeurige permutaties.

``` {.sourceCode .r}
set.seed(165)
B=10000
fOrig=anova(lm(log(length)~dose,data=dna))$F[1]
fStar=sapply(X=1:B, FUN=function(b,y,groep) {anova(lm(y~sample(groep)))$F[1]},y=log(dna$length),groep=dna$dose)
pval=(sum(fStar>=fOrig)+1)/(B+1)
pval
```

    ## [1] 9.999e-05

``` {.sourceCode .r}
hist(fStar,breaks=100)
```

<span id="fig:fPermDist"></span> <img src="Statistiek_2019_2020_files/figure-html/fPermDist-1.png" style="width:100.0%" alt="Approximatieve permutatie nulldistributie van de F-statistiek voor het DMH voorbeeld op basis van 10000 permutaties. De geobserveerde waarde voor de F-statistiek is 367.76." />

Figuur 8.5: Approximatieve permutatie nulldistributie van de F-statistiek voor het DMH voorbeeld op basis van 10000 permutaties. De geobserveerde waarde voor de F-statistiek is 367.76.

De benaderde <span class="math inline">\$p\$</span>-waarde is <span class="math inline">\$p&lt;0.001\$</span>, dus we besluiten dat het effect van de dosis van DMH op DNA beschadiging in levercellen van ratten extreem significant is. Via een posthoc analyse zouden we de groepen paarsgewijs met elkaar kunnen vergelijken.

Merk op, dat als het locatie-shift model niet opgaat, het moeilijk is om inzicht te krijgen in de precieze alternatieve hypothese van de toets. De verdelingen hebben dan een andere vorm. Vandaar dat we geen formele conclusie formuleren voor dit voorbeeld.

### <span class="header-section-number">8.3.3</span> Kruskal-Wallis Rank Test

De Kruskal-Wallis Rank Test (KW-test) is een niet-parameterisch alternatief voor de ANOVA F-test.

De klassieke <span class="math inline">\$F\$</span>-teststatistiek kan geschreven worden als <span class="math display">\\$$ F = \\frac{\\text{SST}/(g-1)}{\\text{SSE}/(n-g)} = \\frac{\\text{SST}/(g-1)}{(\\text{SSTot}-\\text{SST})/(n-g)} , \\$$</span> met <span class="math inline">\$g\$</span> het aantal groepen.

Merk op dat SSTot enkel afhangt van de uitkomsten <span class="math inline">\$\\mathbf{y}\$</span> en niet zal variëren bij permutaties. Het is dus eigenlijk voldoende om SST als teststatistiek te gebruiken. Ter herinnering: <span class="math inline">\$\\text{SST}=\\sum\_{j=1}^t n\_j(\\bar{Y}\_j-\\bar{Y})^2\$</span>.

De KW teststatistiek maakt gebruik van SST maar dan gebaseerd op de rank-getransformeerde uitkomsten<a href="#fn53" id="fnref53" class="footnoteRef"><sup>53</sup></a>, <span class="math display">\\$$ \\text{SST} = \\sum\_{j=1}^g n\_j \\left(\\bar{R}\_j - \\bar{R}\\right)^2 = \\sum\_{j=1}^g n\_j \\left(\\bar{R}\_j - \\frac{n+1}{2}\\right)^2 , \\$$</span> met <span class="math inline">\$\\bar{R}\_j\$</span> het gemiddelde van de ranks in behandelingsgroep <span class="math inline">\$j\$</span>, en <span class="math inline">\$\\bar{R}\$</span> het gemiddelde van alle ranks, <span class="math display">\\$$ \\bar{R} = \\frac{1}{n}(1+2+\\cdots + n) = \\frac{1}{n}\\frac{1}{2}n(n+1) = \\frac{n+1}{2}. \\$$</span> De KW teststatistiek wordt gegeven door <span class="math display">\\$$ KW = \\frac{12}{n(n+1)} \\sum\_{j=1}^g n\_j \\left(\\bar{R}\_j - \\frac{n+1}{2}\\right)^2. \\$$</span> De factor <span class="math inline">\$\\frac{12}{n(n+1)}\$</span> zorgt ervoor dat <span class="math inline">\$KW\$</span> een eenvoudige asymptotische nuldistributie heeft. In het bijzonder, onder <span class="math inline">\$H\_0\$</span>, als <span class="math inline">\$\\min(n\_1,\\ldots, n\_g)\\rightarrow \\infty\$</span>, <span class="math display">\\$$ KW \\rightarrow \\chi^2\_{t-1}. \\$$</span>

De exacte KW-test kan uitgevoerd worden via de berekening van de permutatienuldistributie (die enkel afhangt van <span class="math inline">\$n\_1, \\ldots, n\_g\$</span>) voor het testen van <span class="math display">\\$$H\_0: f\_1=\\ldots=f\_g \\text{ vs } H\_1: \\text{ minstens twee gemiddelden verschillend}.\\$$</span>

Om toe te laten dat <span class="math inline">\$H\_1\$</span> geformuleerd is in termen van gemiddelden, moet locatie-shift verondersteld worden. Indien locatie-shift niet opgaat, zou <span class="math inline">\$H\_1\$</span> eigenlijk geformuleerd moeten worden in termen van probabilistische indexen: <span class="math display">\\$$H\_0: f\_1=\\ldots=f\_g \\text{ vs } H\_1: \\exists\\ j,k \\in \\{1,\\ldots,g\\} : \\text{P}\\left\[Y\_j\\geq Y\_k\\right$$\\neq 0.5\\\]</span>

#### <span class="header-section-number">8.3.3.1</span> DNA Schade Voorbeeld

Eerst analyseren we de data met de R functie `kruskal.test`

``` {.sourceCode .r}
kruskal.test(length~dose,data=dna)
```

    ##
    ##  Kruskal-Wallis rank sum test
    ##
    ## data:  length by dose
    ## Kruskal-Wallis chi-squared = 14, df = 3, p-value = 0.002905

De waarde van de KW teststatistiek is 14, met een <span class="math inline">\$p\$</span>-waarde van 0.00291. Dus op het <span class="math inline">\$5\\%\$</span> significantieniveau kan de nulhypothese worden verworpen.

Het is belangrijk om op te merken dat de R-functie `kruskal.test` steeds de asymptotische benadering gebruikt voor de berekening van de <span class="math inline">\$p\$</span>-waarden. Met slechts 6 observaties per groep, is dit geen optimale benadering van de exacte <span class="math inline">\$p\$</span>-waarde! Met de `coin` R package kunnen we de exacte <span class="math inline">\$p\$</span>-waarde wel berekenen via het argument `distribution='exact'`of benaderen a.d.h.v. simulaties `distribution=approximate(B=100000)`, waarbij B het aantal permutaties is.

``` {.sourceCode .r}
library(coin)
kwPerm <- kruskal_test(length~dose,data=dna,
         distribution=approximate(B=100000))
kwPerm
```

    ##
    ##  Approximative Kruskal-Wallis Test
    ##
    ## data:  length by dose (0, 1.25, 2.5, 5)
    ## chi-squared = 14, p-value = 0.00038

We kunnen besluiten dat er een extreem significant verschil is in distributie van de DNA schade ten gevolge van de dosis. We voeren nu verdere posthoc testen uit voor alle paarsgewijse verschillen a.d.h.v WMW testen.

``` {.sourceCode .r}
pairWilcox <- pairwise.wilcox.test(dna$length,dna$dose)
pairWilcox
```

    ##
    ##  Pairwise comparisons using Wilcoxon rank sum test
    ##
    ## data:  dna$length and dna$dose
    ##
    ##      0     1.25  2.5
    ## 1.25 0.013 -     -
    ## 2.5  0.013 0.818 -
    ## 5    0.013 0.721 0.788
    ##
    ## P value adjustment method: holm

De output geeft pairsgewijze p-waarden weer voor elke vergelijking. De output wordt in een matrix geordend. De p-waarde voor elk element van de matrix behoort tot de paarsgewijze vergelijking van de groep in de kolom en de groep in de rij. Standaard wordt de Holm multiple testing methode gebruikt. Dat is een variant van Bonferroni die minder conservatief is.

We zien dat alle DMH behandelingen significant verschillen van de controle. Maar er is geen significant verschil in de distributie van de DNA schade tussen de verschillende dosisgroepen waarbij DMH werd toegediend. Om een puntschatter op de kans op hogere DNA-schade te berekenen voor de vergelijkingen tussen de behandelingen met DMH en de controle zouden we ook de statistieken U1 nodig hebben. Dit kunnen we niet bekomen uit de `pairwise.wilcox.test` output. Hiervoor zullen we de individuele wilcoxon testen aan moeten roepen.

``` {.sourceCode .r}
nGroep <- table(dna$dose)
probInd <- combn(levels(dna$dose),2,function(x) wilcox.test(length~dose,subset(dna,dose%in%x))$statistic/prod(nGroep[x]))
names(probInd) <- combn(levels(dna$dose),2,paste,collapse="vs")
probInd
```

    ##   0vs1.25    0vs2.5      0vs5 1.25vs2.5   1.25vs5    2.5vs5
    ## 0.0000000 0.0000000 0.0000000 0.4444444 0.2777778 0.3333333

Omdat er twijfels zijn of het locatie-shift model geldig is, doen we enkel uitspraken in termen van de probabilistische index.

We besluiten dat er extreem significant verschil is in de distributie van de DNA-schade metingen tengevolge van de DMH behandeling (<span class="math inline">\$p&lt;0.001\$</span> KW-test). DNA-schade is meer waarschijnlijk na behandeling met DMH dan in de controle behandeling (alle p=0.013, WMW-testen). De kansen op hogere DNA-schade na blootstelling aan DMH bedraagt 100%<a href="#fn54" id="fnref54" class="footnoteRef"><sup>54</sup></a>. Er zijn geen significante verschillen in de distributies van de comit-lengtes tussen de DMH behandelingen onderling (<span class="math inline">\$p=\$</span> 0.72-0.82). DMH vertoont dus al bij de lage dosis genotoxische effecten. (Alle paarsgewijze testen werden gecorrigeerd voor multiple testing d.m.v. Holm’s methode).

------------------------------------------------------------------------

1.  in ons geval de t-test statistiek door de originele reponses te gebruiken die nu gekoppeld worden aan de gepermuteerde groepslabels <span class="math inline">\$G\_g^\*\$</span>[↩](index.md)

2.  in de afwezigheid van *ties*[↩](index.md)

3.  we veronderstellen afwezigheid van *ties*[↩](index.md)

4.  Het berekenen van een BI op deze kansen valt buiten het bestek van de cursus[↩](index.md)

---

[← Argumenten van onze functie](04-argumenten-van-onze-functie.md) · [Up: contents](index.md)

---
title: 10.6 ANOVA Tabel
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-glm.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-glm.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 10.6 ANOVA Tabel

**Source:** [`chap-glm.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-glm.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">10.6.1</span> SSTot, SSR en SSE

Voor de enkelvoudige lineaire regressie hebben we in detail de decompositie van SSTot=SSR+SSE besproken. In deze sectie breiden we die resultaten uit naar meervoudige lineaire regressie.

De totale kwadratensom SSTot is gedefinieerd zoals voorheen, <span class="math display">\\$$ \\text{SSTot} = \\sum\_{i=1}^n (Y\_i - \\bar{Y})^2. \\$$</span>

Het is nog steeds een maat voor de totale variabiliteit in de geobserveerde uitkomsten. Ook de residuele kwadratensom is zoals voorheen. <span class="math display">\\$$ \\text{SSE} = \\sum\_{i=1}^n (Y\_i-\\hat{Y}\_i)^2. \\$$</span>

Beschouw nu een meervoudig lineair regressiemodel met <span class="math inline">\$p-1\$</span> regressoren. Dan geldt de volgende decompositie van de totale kwadratensom, <span class="math display">\\$$ \\text{SSTot} = \\text{SSR} + \\text{SSE} , \\$$</span> met <span class="math display">\\$$ \\text{SSR} = \\sum\_{i=1}^n (\\hat{Y}\_i-\\bar{Y})^2. \\$$</span>

De kwadratensom van de regressie (SSR) kan nog steeds geïnterpreteerd worden als de variabiliteit in de uitkomsten die verklaard kan worden door het regressiemodel.

Voor de vrijheidsgraden en de gemiddelde kwadratensommen geldt:

- SSTot heeft <span class="math inline">\$n-1\$</span> vrijheidsgraden en <span class="math inline">\$\\text{SSTot}/(n-1)\$</span> is een schatter voor de variantie van <span class="math inline">\$Y\$</span> (van de marginale distributie van <span class="math inline">\$Y\$</span>).
- SSE heeft <span class="math inline">\$n-p\$</span> vrijheidsgraden en <span class="math inline">\$\\text{MSE}=\\text{SSE}/(n-p)\$</span> is een schatter voor de residuele variantie van <span class="math inline">\$Y\$</span> gegeven de regressoren (i.e. een schatter voor de residuele variantie <span class="math inline">\$\\sigma^2\$</span> van de foutterm <span class="math inline">\$\\epsilon\$</span>).
- SSR heeft <span class="math inline">\$p-1\$</span> vrijheidsgraden en <span class="math inline">\$\\text{MSR}=\\text{SSR}/(p-1)\$</span> is de gemiddelde kwadratensom van de regressie.

Een gevolg van de decompositie van SSTot is dat de determinatiecoëfficiënt blijft zoals voorheen, i.e. <span class="math display">\\$$ R^2 = 1-\\frac{\\text{SSE}}{\\text{SSTot}} = \\frac{\\text{SSR}}{\\text{SSTot}} \\$$</span> is de fractie van de totale variabiliteit in de uitkomsten die verklaard wordt door het regressiemodel.

De teststatistiek <span class="math inline">\$F=\\text{MSR}/\\text{MSE}\$</span> is onder <span class="math inline">\$H\_0:\\beta\_1=\\ldots=\\beta\_{p-1}=0\$</span> verdeeld als <span class="math inline">\$F\_{p-1;n-p}\$</span>. De F-test test m.a.w. het effect van alle predictoren simultaan. Onder de nulhypothese is er geen associatie tussen de respons en elk van de predictoren. De output van deze F-test wordt standaard gegeven onderaan in de summary output.

``` {.sourceCode .r}
summary(lmVWS)
```

    ##
    ## Call:
    ## lm(formula = lpsa ~ lcavol + lweight + svi, data = prostate)
    ##
    ## Residuals:
    ##      Min       1Q   Median       3Q      Max
    ## -1.72966 -0.45767  0.02814  0.46404  1.57012
    ##
    ## Coefficients:
    ##             Estimate Std. Error t value Pr(>|t|)
    ## (Intercept) -0.26807    0.54350  -0.493  0.62301
    ## lcavol       0.55164    0.07467   7.388  6.3e-11 ***
    ## lweight      0.50854    0.15017   3.386  0.00104 **
    ## sviinvasion  0.66616    0.20978   3.176  0.00203 **
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ##
    ## Residual standard error: 0.7168 on 93 degrees of freedom
    ## Multiple R-squared:  0.6264, Adjusted R-squared:  0.6144
    ## F-statistic: 51.99 on 3 and 93 DF,  p-value: < 2.2e-16

We zien dat de algemene nulhypothese heel significant kan worden verworpen. Minstens 1 predictor is extreem significant geassocieerd met de respons. In de individuele t-testen zien we dat elk van de predictoren een sterk significante associatie vertonen.

### <span class="header-section-number">10.6.2</span> Extra Kwadratensommen

We kunnen een stap verder gaan en voor iedere individuele regressor een kwadratensom definiëren. Er zijn echter verschillende mogelijkheden.

Beschouw de volgende twee regressiemodellen voor regressoren <span class="math inline">\$x\_1\$</span> en <span class="math inline">\$x\_2\$</span>: <span class="math display">\\$$ Y\_i = \\beta\_0+\\beta\_1 x\_{i1} + \\epsilon\_i, \\$$</span> met <span class="math inline">\$\\epsilon\_i\\text{ iid } N(0,\\sigma\_1^{2})\$</span>, en <span class="math display">\\$$ Y\_i = \\beta\_0+\\beta\_1 x\_{i1}+\\beta\_2 x\_{i2} + \\epsilon\_i, \\$$</span> met <span class="math inline">\$\\epsilon\_i\\text{ iid } N(0,\\sigma\_2^{2})\$</span>.

Merk op dat we subscript 1 en 2 toegevoegd hebben aan de residuele varianties, maar dat we dezelfde <span class="math inline">\$\\beta\$</span>-parameternotatie gebruiken voor beide modellen; dit is om de notatie niet nodeloos complex te maken, maar je moet je ervan bewust zijn dat de <span class="math inline">\$\\beta\$</span>-parameters uit beide modellen niet noodzakelijk gelijk zijn.

Voor het eerste (gereduceerde) model geldt de decompositie <span class="math display">\\$$ \\text{SSTot} = \\text{SSR}\_1 + \\text{SSE}\_1 \\$$</span> en voor het tweede (niet-gereduceerde) model <span class="math display">\\$$ \\text{SSTot} = \\text{SSR}\_2 + \\text{SSE}\_2 \\$$</span> (SSTot is uiteraard dezelfde in beide modellen omdat dit niet afhangt van het regressiemodel).

**Definitie extra kwadratensom** De *extra kwadratensom* (Engels: *extra sum of squares*) van predictor <span class="math inline">\$x\_2\$</span> t.o.v. het model met enkel <span class="math inline">\$x\_1\$</span> als predictor wordt gegeven door <span class="math display">\\$$ \\text{SSR}\_{2\\mid 1} = \\text{SSE}\_1-\\text{SSE}\_2=\\text{SSR}\_2-\\text{SSR}\_1. \\$$</span>

**Einde definitie**

Merk eerst op dat <span class="math inline">\$\\text{SSE}\_1-\\text{SSE}\_2=\\text{SSR}\_2-\\text{SSR}\_1\$</span> triviaal is gezien de decomposities van de totale kwadratensommen.

De extra kwadratensom <span class="math inline">\$\\text{SSR}\_{2\\mid 1}\$</span> kan eenvoudig geïnterpreteerd worden als de extra variantie van de uitkomst die verklaard kan worden door regressor <span class="math inline">\$x\_2\$</span> toe te voegen aan een model waarin regressor <span class="math inline">\$x\_1\$</span> reeds aanwezig is.

Met dit nieuw soort kwadratensom kunnen we voor het model met twee predictoren schrijven <span class="math display">\\$$ \\text{SSTot} = \\text{SSR}\_1+ \\text{SSR}\_{2\\mid 1} + \\text{SSE}. \\$$</span> Dit volgt rechtstreeks uit de definitie van de extra kwadratensom <span class="math inline">\$\\text{SSR}\_{2\\mid 1}\$</span>.

De definitie voor de extra kwadratensom kan uitgebreid worden naar een situatie waar twee geneste lineaire regressiemodellen beschouwd worden.

Zonder in te boeten in algemeenheid starten we met de regressiemodellen (<span class="math inline">\$s&lt;p-1\$</span>) <span class="math display">\\$$ Y\_i = \\beta\_0 + \\beta\_1 x\_{i1} + \\cdots + \\beta\_{s} x\_{is} + \\epsilon\_i \\$$</span> met <span class="math inline">\$\\epsilon\_i\\text{ iid }N(0,\\sigma\_1^{2})\$</span>, en (<span class="math inline">\$s&lt; q\\leq p-1\$</span>) <span class="math display">\\$$ Y\_i = \\beta\_0 + \\beta\_1 x\_{i1} + \\cdots + \\beta\_{s} x\_{is} + \\beta\_{s+1} x\_{is+1} + \\cdots \\beta\_{q}x\_{iq}+ \\epsilon\_i \\$$</span> met <span class="math inline">\$\\epsilon\_i\\text{ iid } N(0,\\sigma\_2^{2})\$</span>.

De **extra kwadratensom** van predictoren <span class="math inline">\$x\_{s+1}, \\ldots, x\_q\$</span> t.o.v. het model met enkel de predictoren <span class="math inline">\$x\_1,\\ldots, x\_{s}\$</span> wordt gegeven door <span class="math display">\\$$ \\text{SSR}\_{s+1, \\ldots, q\\mid 1,\\ldots, s} = \\text{SSE}\_1-\\text{SSE}\_2=\\text{SSR}\_2-\\text{SSR}\_1. \\$$</span>

De extra kwadratensom <span class="math inline">\$\\text{SSR}\_{s+1, \\ldots, q\\mid 1,\\ldots, s}\$</span> meet de extra variabiliteit in uitkomst die verklaard wordt door de predictoren <span class="math inline">\$x\_{s+1}, \\ldots, x\_q\$</span> toe te voegen aan een model met predictoren <span class="math inline">\$x\_1,\\ldots, x\_{s}\$</span>. Anders gezegd: het meet de variatie van de uitkomsten verklaard door predictoren <span class="math inline">\$x\_{s+1}, \\ldots, x\_q\$</span> die niet verklaard wordt door de predictoren <span class="math inline">\$x\_1,\\ldots, x\_{s}\$</span>.

We hebben hier SSR notatie gebruikt met lange indexen (bv. <span class="math inline">\$\\text{SSR}\_{s, \\ldots, q\\mid 1,\\ldots, s-1}\$</span>). Soms wordt de voorkeur gegeven aan de notatie <span class="math display">\\$$ \\text{SSR}(s+1, \\ldots, q\\mid 1,\\ldots, s). \\$$</span>

### <span class="header-section-number">10.6.3</span> Type I Kwadratensommen

Stel dat <span class="math inline">\$p-1\$</span> regressoren beschouwd worden, en beschouw een sequentie van modellen (<span class="math inline">\$s=2,\\ldots, p-1\$</span>) <span class="math display">\\$$ Y\_i = \\beta\_0 + \\sum\_{j=1}^{s} \\beta\_j x\_{ij} + \\epsilon\_i \\$$</span> met <span class="math inline">\$\\epsilon\_i\\text{ iid } N(0,\\sigma^{2})\$</span>. De overeenkomstige kwadratensommen worden genoteerd als <span class="math inline">\$\\text{SSR}\_{s}\$</span> en <span class="math inline">\$\\text{SSE}\_{s}\$</span>. De modelsequentie geeft ook aanleiding tot extra kwadratensommen <span class="math inline">\$\\text{SSR}\_{s\\mid 1,\\ldots, s-1}\$</span>. Deze laatste kwadratensom wordt een type I kwadratensom genoemd. Merk op dat deze afhangt van de volgorde (nummering) van regressoren.

Er kan aangetoond worden dat voor Model met <span class="math inline">\$s=p-1\$</span> geldt <span class="math display">\\$$ \\text{SSTot} = \\text{SSR}\_1 + \\text{SSR}\_{2\\mid 1} + \\text{SSR}\_{3\\mid 1,2} + \\cdots + \\text{SSR}\_{p-1\\mid 1,\\ldots, p-2} + \\text{SSE}, \\$$</span> met <span class="math inline">\$\\text{SSE}\$</span> de residuele kwadratensom van het model met alle <span class="math inline">\$p-1\$</span> regressoren en <span class="math display">\\$$ \\text{SSR}\_1 + \\text{SSR}\_{2\\mid 1} + \\text{SSR}\_{3\\mid 1,2} + \\cdots + \\text{SSR}\_{p-1\\mid 1,\\ldots, p-2} = \\text{SSR} \\$$</span> met <span class="math inline">\$\\text{SSR}\$</span> de kwadratensom van de regressie van het model met alle <span class="math inline">\$p-1\$</span> regressoren.

De interpretatie van iedere individuele SSR term werd eerder gegeven, maar het is belangrijk om op te merken dat de interpretatie van iedere term afhangt van de volgorde van de regressoren in de sequentie van regressiemodellen.

Dus de type I kwadratensommen laten een decompositie van SSTot toe, maar de SSR-termen hangen af van de volgorde waarin de regressoren in het regressiemodel voorkomen.

Iedere type I SSR heeft betrekking op het effect van 1 regressor en heeft dus 1 vrijheidsgraad. Voor iedere type I SSR term kan een gemiddelde kwadratensom gedefinieerd worden als <span class="math inline">\$\\text{MSR}\_{j\\mid 1,\\ldots, j-1}=\\text{SSR}\_{j\\mid 1,\\ldots, j-1}/1\$</span>. De teststatistiek <span class="math inline">\$F=\\text{MSR}\_{j\\mid 1,\\ldots, j-1}/\\text{MSE}\$</span> is onder <span class="math inline">\$H\_0:\\beta\_j=0\$</span> met <span class="math inline">\$s=j\$</span> verdeeld als <span class="math inline">\$F\_{1;n-(j+1)}\$</span>.

Deze kwadratensommen worden standaard weergegeven door de anova functie in R.

### <span class="header-section-number">10.6.4</span> Type III Kwadratensommen

Beschouw opnieuw het regressiemodel met <span class="math inline">\$p-1\$</span> regressoren. De type III kwadratensom van regressor <span class="math inline">\$x\_j\$</span> wordt gegeven door de extra kwadratensom <span class="math display">\\$$ \\text{SSR}\_{j \\mid 1,\\ldots, j-1,j+1,\\ldots, p-1} = \\text{SSE}\_1-\\text{SSE}\_2 \\$$</span>

- <span class="math inline">\$\\text{SSE}\_2\$</span> de residuele kwadratensom van regressiemodel met alle <span class="math inline">\$p-1\$</span> regressoren.
- <span class="math inline">\$\\text{SSE}\_1\$</span> de residuele kwadratensom van regressiemodel met alle <span class="math inline">\$p-1\$</span> regressoren, uitgezonderd regressor <span class="math inline">\$x\_j\$</span>.

De type III kwadratensom <span class="math inline">\$\\text{SSR}\_{j \\mid 1,\\ldots, j-1,j+1,\\ldots, p-1}\$</span> kwantificeert dus het aandeel van de totale variantie van de uitkomst dat door regressor <span class="math inline">\$x\_j\$</span> verklaard wordt en dat niet door de andere <span class="math inline">\$p-2\$</span> regressoren verklaard wordt.

De type III kwadratensom heeft ook 1 vrijheidsgraad omdat het om 1 <span class="math inline">\$\\beta\$</span>-parameter gaat.

Voor iedere type III SSR term kan een gemiddelde kwadratensom gedefinieerd worden als <span class="math inline">\$\\text{MSR}\_{j \\mid 1,\\ldots, j-1,j+1,\\ldots, p-1}=\\text{SSR}\_{j \\mid 1,\\ldots, j-1,j+1,\\ldots, p-1}/1\$</span>.

De teststatistiek <span class="math inline">\$F=\\text{MSR}\_{j \\mid 1,\\ldots, j-1,j+1,\\ldots, p-1}/\\text{MSE}\$</span> is onder <span class="math inline">\$H\_0:\\beta\_j=0\$</span> verdeeld as <span class="math inline">\$F\_{1;n-p}\$</span>.

Deze kwadratensommen kunnen worden verkregen d.m.v. de Anova functie van het car package. In de Anova functie wordt hiervoor het argument ‘type=3’ gebruikt.

``` {.sourceCode .r}
library(car)
Anova(lmVWS,type=3)
```

    ## Anova Table (Type III tests)
    ##
    ## Response: lpsa
    ##             Sum Sq Df F value    Pr(>F)
    ## (Intercept)  0.125  1  0.2433  0.623009
    ## lcavol      28.045  1 54.5809 6.304e-11 ***
    ## lweight      5.892  1 11.4678  0.001039 **
    ## svi          5.181  1 10.0841  0.002029 **
    ## Residuals   47.785 93
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Merk op dat de p-waarden die we verkrijgen voor het testen van elk van de effecten identiek zijn als de p-waarden van de tweezijdige t-testen. De F-test o.b.v. een type III kwadratensom voor 1 parameter is equivalent met de tweezijdige t-test voor deze parameter.

---

[← 10.5 Het niet-additieve meervoudig lineair regressiemodel](05-10-5-het-niet-additieve-meervoudig-lineair-regressiemodel.md) · [Up: contents](index.md) · [10.7 Regressiediagnostieken →](07-10-7-regressiediagnostieken.md)

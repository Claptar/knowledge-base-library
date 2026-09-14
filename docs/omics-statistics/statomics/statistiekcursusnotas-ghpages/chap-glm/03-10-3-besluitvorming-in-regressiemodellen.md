---
title: 10.3 Besluitvorming in regressiemodellen
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-glm.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-glm.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 10.3 Besluitvorming in regressiemodellen

**Source:** [`chap-glm.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-glm.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

Als de gegevens representatief zijn voor de populatie kan men in de meervoudige lineaire regressiecontext eveneens aantonen dat de kleinste kwadraten schatters voor het intercept en de hellingen onvertekend zijn, m.a.w <span class="math display">\\$$E\[\\hat \\beta\_j$$=\\beta\_j,\\quad j=0,\\ldots,p-1.\\\]</span>

Het feit dat de schatters gemiddeld (over een groot aantal vergelijkbare studies) niet afwijken van de waarden in de populatie, impliceert niet dat ze niet rond die waarde variëren. Om inzicht te krijgen hoe dicht we de parameterschatters bij het werkelijke intercept <span class="math inline">\$\\beta\_0\$</span> en de werkelijke hellingen <span class="math inline">\$\\beta\_j\$</span> mogen verwachten, wensen we bijgevolg ook haar variabiliteit te kennen.

Net zoals in Hoofdstuk [6](../chap-linReg/index.md) is het op basis van de puntschatters voor de hellingen niet duidelijk of de verbanden werkelijk voorkomen in de populatie of indien we de verbanden door toeval hebben geobserveerd in de dataset. De schatting van de hellingen is immers onnauwkeurig en zal variëren van steekproef tot steekproef. Zoals steeds is het resultaat van een data-analyse dus niet interpreteerbaar zonder die variabiliteit in kaart te brengen.

Om de resultaten uit de steekproef te kunnen veralgemenen naar de populatie zullen we in deze context eveneens inzicht nodig hebben op de verdeling van de parameterschatters. Om op basis van slechts één steekproef te kunnen voorspellen hoe de parameterschatters variëren van steekproef tot steekproef zullen we naast de onderstelling van

1.  *Lineariteit*

bijkomende aannames moeten maken over de verdeling van de gegevens, met name

1.  *Onafhankelijkheid*: de metingen <span class="math inline">\$(X\_{11},\\dots, X\_{1p-1}, Y\_1), ..., (X\_{n1},\\ldots,X\_{np-1},Y\_n)\$</span> werden gemaakt bij n onafhankelijke subjecten/observationele eenheden
2.  *Homoscedasticiteit* of *gelijkheid van variantie*: de observaties variëren met een gelijke variantie rond het regressievlak. De residuen <span class="math inline">\$\\epsilon\_i\$</span> hebben dus een gelijke variantie <span class="math inline">\$\\sigma^2\$</span> voor elk covariaat patroon <span class="math inline">\$(X\_1=x\_1, ..., X\_{p-1}=x\_{p-1})\$</span>. Dat impliceert ook dat de conditionele variantie van <span class="math inline">\$Y\$</span> gegeven <span class="math inline">\$X\_1,\\ldots,X\_{p-1}\$</span>, <span class="math inline">\$\\text{var}(Y\\vert X\_1,\\ldots,X\_{p-1})\$</span> dus gelijk is, met name <span class="math inline">\$\\text{var}(Y\\vert X\_1,\\ldots,X\_{p-1}) = \\sigma^2\$</span> voor elk covariaat patroon <span class="math inline">\$(X\_1=x\_1, ..., X\_{p-1}=x\_{p-1})\$</span>. De constante <span class="math inline">\$\\sigma\$</span> wordt opnieuw de *residuele standaarddeviatie* genoemd.
3.  *Normaliteit*: de residuen <span class="math inline">\$\\epsilon\_i\$</span> zijn normaal verdeeld.

Uit aannames 2, 3 en 4 volgt dus dat de residuen <span class="math inline">\$\\epsilon\_i\$</span> onafhankelijk zijn en dat ze allen eenzelfde Normale verdeling volgen <span class="math display">\\$$\\epsilon\_i \\sim N(0,\\sigma^2).\\$$</span> Als we ook steunen op de veronderstelling van lineariteit weten we dat de originele observaties conditioneel op <span class="math inline">\$X\_1,\\ldots,X\_{p-1}\$</span> eveneens Normaal verdeeld zijn <span class="math display">\\$$Y\_i\\sim N(\\beta\_0+\\beta\_1 X\_{i1}+\\ldots+\\beta\_{p-1} X\_{ip-1},\\sigma^2),\\$$</span> met een gemiddelde dat varieert in functie van de waarde van de onafhankelijke variabelen <span class="math inline">\$X\_{i1},\\ldots,X\_{ip-1}\$</span>.

Merk op dat de onzekerheid op de hellingen af zal nemen wanneer er meer observaties zijn en/of wanneer de observaties meer gespreid zijn. Voor het opzetten van een experiment kan dit belangrijke informatie zijn. Uiteraard wordt de precisie ook beïnvloed door de grootte van de variabiliteit van de observaties rond het regressievlak, <span class="math inline">\$\\sigma^2\$</span>, maar dat heeft een onderzoeker typisch niet in de hand.

De conditionele variantie (<span class="math inline">\$\\sigma^2\$</span>) is echter niet gekend en is noodzakelijk voor de berekening van de variantie op de parameterschatters. We kunnen <span class="math inline">\$\\sigma^2\$</span> echter opnieuw schatten op basis van de *mean squared error* (MSE):

<span class="math display">\\$$\\hat\\sigma^2=MSE=\\frac{\\sum\\limits\_{i=1}^n \\left(y\_i-\\hat\\beta\_0-\\hat\\beta\_1 X\_{i1}-\\ldots-\\hat\\beta\_{p-1} X\_{ip-1}\\right)^2}{n-p}=\\frac{\\sum\\limits\_{i=1}^n e^2\_i}{n-p}.\\$$</span>

Analoog als in Hoofdstuk [6](../chap-linReg/index.md) kunnen we opnieuw toetsen en betrouwbaarheidsintervallen construeren op basis van de teststatistieken
<span class="math display">\\$$T\_k=\\frac{\\hat{\\beta}\_k-\\beta\_k}{SE(\\hat{\\beta}\_k)} \\text{ met } k=0, \\ldots, p-1.\\$$</span> Als aan alle aannames is voldaan dan volgen deze statistieken <span class="math inline">\$T\_k\$</span> een t-verdeling met <span class="math inline">\$n-p\$</span> vrijheidsgraden. Wanneer niet is voldaan aan de veronderstelling van normaliteit maar wel aan lineariteit, onafhankelijkheid en homoscedasticiteit dan kunnen we voor inferentie opnieuw beroep doen op de centrale limietstelling die zegt dat de statistiek <span class="math inline">\$T\_k\$</span> bij benadering een standaard Normale verdeling zal volgen wanneer het aantal observaties voldoende groot is.

Voor het prostaatkanker voorbeeld kunnen we de effecten in de steekproef opnieuw veralgemenen naar de populatie toe door betrouwbaarheidsintervallen te bouwen voor de hellingen: <span class="math display">\\$$\[\\hat\\beta\_j - t\_{n-p,\\alpha/2} \\text{SE}\_{\\hat\\beta\_j},\\hat\\beta\_j + t\_{n-p,\\alpha/2} \\text{SE}\_{\\hat\\beta\_j}$$\\\]</span>.

``` {.sourceCode .r}
confint(lmVWS)
```

    ##                  2.5 %    97.5 %
    ## (Intercept) -1.3473509 0.8112061
    ## lcavol       0.4033628 0.6999144
    ## lweight      0.2103288 0.8067430
    ## sviinvasion  0.2495824 1.0827342

Gezien nul niet in de intervallen ligt weten we eveneens dat de associaties tussen lpsa <span class="math inline">\$\\leftrightarrow\$</span> lcavol, lpsa <span class="math inline">\$\\leftrightarrow\$</span> lweight, lpsa <span class="math inline">\$\\leftrightarrow\$</span> svi, statistisch significant zijn op het 5% significantieniveau.

Anderzijds kunnen we ook formele hypothesetoetsen uitvoeren. Onder de nulhypothese veronderstellen we dat er geen associatie is tussen lpsa en de predictor <span class="math inline">\$X\_j\$</span>: <span class="math display">\\$$H\_0: \\beta\_j=0\\$$</span> en onder de alternatieve hypothese is er een associatie tussen response en predictor <span class="math inline">\$X\_j\$</span>: <span class="math display">\\$$H\_1: \\beta\_j\\neq0\\$$</span>

Met de test statistiek <span class="math display">\\$$T=\\frac{\\hat{\\beta}\_j-0}{SE(\\hat{\\beta}\_j)}\\$$</span> kunnen we de nulhypothese falsifiëren. Onder <span class="math inline">\$H\_0\$</span> volgt de statistiek een t-verdeling met <span class="math inline">\$n-p\$</span> vrijheidsgraden, waarbij p het aantal model parameters is van het regressiemodel inclusief het intercept.

Deze tweezijdige testen zijn standaard geïmplementeerd in de standaard output van R.

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

De testen geven weer dat de associaties tussen lpsa<span class="math inline">\$\\leftrightarrow\$</span>lcavol, lpsa<span class="math inline">\$\\leftrightarrow\$</span>lweight en lpsa<span class="math inline">\$\\leftrightarrow\$</span>svi, respectievelijk extreem significant (<span class="math inline">\$p &lt;&lt; 0.001\$</span>) en sterk significant (<span class="math inline">\$p=0.001\$</span> en <span class="math inline">\$p=0.002\$</span>) zijn.

---

[← 10.2 Het additieve meervoudig lineaire regressie model](02-10-2-het-additieve-meervoudig-lineaire-regressie-model.md) · [Up: contents](index.md) · [10.4 Nagaan van modelveronderstellingen {#nagaan-van-modelveronderstellingen} →](04-10-4-nagaan-van-modelveronderstellingen-nagaan-van-modelvero.md)

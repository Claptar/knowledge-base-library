---
title: lijn van het bestand de namen van de variabelen bevat
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-linReg.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-linReg.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# lijn van het bestand de namen van de variabelen bevat

**Source:** [`chap-linReg.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-linReg.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

borstkanker <- read.table("dataset/borstkanker.txt",header=TRUE)
knitr::kable(head(borstkanker),caption="Overzicht van de variabelen in de borstkanker dataset.",booktabs = TRUE)
```

| sample\_name | filename | treatment | er | grade | node | size | age | ESR1 | S100A8 |
|:---|:---|:---|---:|---:|---:|---:|---:|---:|---:|
| OXFT\_209 | gsm65344.cel.gz | tamoxifen | 1 | 3 | 1 | 2.5 | 66 | 1939.1990 | 207.19682 |
| OXFT\_1769 | gsm65345.cel.gz | tamoxifen | 1 | 1 | 1 | 3.5 | 86 | 2751.9521 | 36.98611 |
| OXFT\_2093 | gsm65347.cel.gz | tamoxifen | 1 | 1 | 1 | 2.2 | 74 | 379.1951 | 2364.18306 |
| OXFT\_1770 | gsm65348.cel.gz | tamoxifen | 1 | 1 | 1 | 1.7 | 69 | 2531.7473 | 23.61504 |
| OXFT\_1342 | gsm65350.cel.gz | tamoxifen | 1 | 3 | 0 | 2.5 | 62 | 141.0508 | 3218.74109 |
| OXFT\_2338 | gsm65352.cel.gz | tamoxifen | 1 | 3 | 1 | 1.4 | 63 | 1495.4213 | 107.56868 |

<span id="tab:brcaMicroLin">Tabel 6.1: </span>Overzicht van de variabelen in de borstkanker dataset.

### <span class="header-section-number">6.1.2</span> Data exploratie

In Sectie [4.6.3](../chap-describe/index.md) werd de associatie tussen beide genen uitgebreid verkend. Daarin hebben we de genexpressie data eerst log-getransformeerd.

In dit hoofdstuk zullen we om didactische redenen eerst werken met de expressiemetingen op de originele schaal. De expressie van het S100A8 gen wordt weergegeven in Figuur [6.1](index.md). Op de originele schaal zien we drie heel grote outliers. Omwille van didactische redenen worden deze eerst verwijderd uit de dataset. In principe mogen outliers enkel worden verwijderd uit een studie als daar een goede reden voor is. We kunnen op basis van de informatie over de studie echter niet argumenteren waarom de outliers niet representatief zijn, zoals bijvoorbeeld wel het geval zou zijn wanneer zich meetfouten of problemen voordeden m.b.t. deze observaties in de studie. Later in het hoofdstuk zullen we zien hoe we op een correcte wijze alle data kunnen modelleren.

``` {.sourceCode .r}
boxplot(borstkanker$S100A8,ylab="S100A8 expressie")
```

<span id="fig:s100a8Boxplot"></span> <img src="Statistiek_2019_2020_files/figure-html/s100a8Boxplot-1.png" style="width:100.0%" alt="Expressie van het S100A8 gen." />

Figuur 6.1: Expressie van het S100A8 gen.

Om meerdere variabelen in de borstkanker dataset te bestuderen, kunnen we gebruik maken van de grafische scatterplot matrix voorstelling (zie Figuur [6.2](index.md)). Hierbij wordt een matrix met paarsgewijze dotplots voor alle variabelen geproduceerd.

``` {.sourceCode .r}
plot(subset(borstkanker,S100A8<2000)[,-(1:4)])
```

<span id="fig:brcaGenAl"></span> <img src="Statistiek_2019_2020_files/figure-html/brcaGenAl-1.png" style="width:100.0%" alt="Scatterplot matrix voor de observaties in de borstkanker dataset na verwijdering van outliers in de S100A8 expressie (merk op dat we deze outliers in principe niet mochten verwijderen uit de dataset)." />

Figuur 6.2: Scatterplot matrix voor de observaties in de borstkanker dataset na verwijdering van outliers in de S100A8 expressie (merk op dat we deze outliers in principe niet mochten verwijderen uit de dataset).

In de scatterplot matrix zien we bijvoorbeeld dat er een positieve associatie lijkt te zijn tussen de leeftijd (age) en de lymfeknoop status (node; geeft aan of de lymfeknopen al dan niet aangetast zijn en chirurgisch werden verwijderd, node 0: niet aangetast, 1: aangetast). Daarnaast observeren we ook een indicatie voor een negatieve associatie (dalende trend) tussen de ESR1 en S100A8 gen expressie.

In dit hoofdstuk zullen we ons in het bijzonder focussen op de relatie tussen de ESR1 en de S100A8 gen expressie. Een individuele scatterplot met smoother (zie Figuur [6.3](index.md)) geeft de associatie tussen beide genen nog beter weer. Smoothers kunnen trends visualiseren tussen variabelen zonder vooraf veronderstellingen te doen over de vorm van het verband en zijn daarom heel erg nuttig bij data exploratie. We zien dat de genexpressie van S100A8 gemiddeld gezien daalt voor patiënten met een hogere expressie van ESR1.

``` {.sourceCode .r}
with(subset(borstkanker,S100A8<2000), scatter.smooth(ESR1,S100A8))
```

<span id="fig:brcaSmooth"></span> <img src="Statistiek_2019_2020_files/figure-html/brcaSmooth-1.png" style="width:100.0%" alt="Scatterplot voor S100A8 expressie in functie van de ESR1 expressie met smoother die het verband tussen beide genen samenvat (na verwijdering van outliers in de S100A8 expressie, merk op dat we deze outliers in principe niet mochten verwijderen uit de dataset)." />

Figuur 6.3: Scatterplot voor S100A8 expressie in functie van de ESR1 expressie met smoother die het verband tussen beide genen samenvat (na verwijdering van outliers in de S100A8 expressie, merk op dat we deze outliers in principe niet mochten verwijderen uit de dataset).

### <span class="header-section-number">6.1.3</span> Model

Op basis van Figuur [6.3](index.md) zien we dat er een relatie is tussen de S100A8 (Y) en ESR1 (X) expressie. De expressiemetingen voor het S100A8 gen zijn echter onderhevig aan ruis onder andere door biologische variabiliteit en technische variabiliteit. Voor een gegeven waarde <span class="math inline">\$X=x\$</span> neemt de genexpressie <span class="math inline">\$Y\$</span> dus niet steeds dezelfde waarde aan. Generiek kunnen we de S100A8 gen expressie dus beschrijven als <span class="math display">\\$$\\text{observatie = signaal + ruis.}\\$$</span>

Wiskundig kunnen we dat modelleren als <span class="math display">\\$$Y\_i=g(X\_i)+\\epsilon\_i\\$$</span> waarbij we de toevallige veranderlijke S100A8 genexpressie voor subject <span class="math inline">\$i\$</span> (<span class="math inline">\$Y\_i\$</span>) modelleren in functie van de genexpressie van het ESR1 gen (<span class="math inline">\$X\_i\$</span>). Uiteraard is dit verband niet perfect. Dat wordt aangegeven door de foutterm <span class="math inline">\$\\epsilon\_i\$</span> die uitdrukt dat observaties <span class="math inline">\$Y\_i\$</span> variëren rond dit verband, m.a.w. het verband modelleert een conditioneel gemiddelde: <span class="math display">\\$$E\[Y\_i\|X\_i=x$$=g(x),\\\]</span> het is de verwachte uitkomst<a href="#fn38" id="fnref38" class="footnoteRef"><sup>38</sup></a> (<span class="math inline">\$E$$Y$$\$</span>) bij subjecten met een expressieniveau <span class="math inline">\$X\_i=x\$</span> voor het ESR1 gen.

Zo geeft <span class="math inline">\$E(Y\|X=2400)\$</span> de gemiddelde genexpressie aan van het S100A8 gen voor subjecten die een expressie hebben van 2400 voor het ESR1 gen. Men zou dit gemiddelde bekomen door van alle patiënten in de studiepopulatie, die een ESR1 expressie hebben van 2400, de S100A8 expressie te meten en hier vervolgens het gemiddelde van te nemen. Het gemiddelde <span class="math inline">\$E(Y\|X=x)\$</span> wordt een *conditioneel gemiddelde* genoemd omdat het een gemiddelde uitkomst beschrijft, conditioneel op het feit dat <span class="math inline">\$X=x\$</span>.

Gezien <span class="math display">\\$$E\[Y\_i\|X\_i=x$$=g(x)\\\]</span> het gemiddelde beschrijft voor subjecten met een ESR1 expressieniveau van <span class="math inline">\$x\$</span> is de foutterm <span class="math inline">\$\\epsilon\_i\$</span> gemiddeld 0 voor deze subjecten: <span class="math display">\\$$E\[\\epsilon\_i\\vert X\_i=x$$=0.\\\]</span>

## <span class="header-section-number">6.2</span> Lineaire regressie

Om accurate en interpreteerbare resultaten te bekomen gaat men vaak bepaalde veronderstellingen doen over de structuur van <span class="math inline">\$g(x)\$</span>. Zo modelleert men <span class="math inline">\$g(x)\$</span> vaak als een lineaire functie van ongekende parameters. Dat wordt geïllustreerd in Figuur [6.4](index.md).

``` {.sourceCode .r}
plot(S100A8~ESR1,data=subset(borstkanker,S100A8<2000))
#lm functie fit een linear model
#abline functie voegt een lijn toe aan een plot
abline(lm(S100A8~ESR1,data=subset(borstkanker,S100A8<2000)))
```

<span id="fig:brcaLin1"></span> <img src="Statistiek_2019_2020_files/figure-html/brcaLin1-1.png" style="width:100.0%" alt="Scatterplot voor S100A8 expressie in functie van de ESR1 expressie met lineair model dat het verband tussen beide genen samenvat (na verwijdering van outliers in de S100A8 expressie, merk op dat we deze outliers in principe niet mochten verwijderen uit de dataset zoals we verder in dit hoofdstuk zullen zien)." />

Figuur 6.4: Scatterplot voor S100A8 expressie in functie van de ESR1 expressie met lineair model dat het verband tussen beide genen samenvat (na verwijdering van outliers in de S100A8 expressie, merk op dat we deze outliers in principe niet mochten verwijderen uit de dataset zoals we verder in dit hoofdstuk zullen zien).

Men veronderstelt dan het onderstaande lineaire regressiemodel <span id="eq:linreg" class="math display">\\$$\\begin{equation} E(Y\|X =x)=\\beta\_0 + \\beta\_1 x \\tag{6.1} \\end{equation}\\$$</span>

waarbij <span class="math inline">\$\\beta\_0\$</span> en <span class="math inline">\$\\beta\_1\$</span> onbekende modelparameters zijn. In deze uitdrukking stelt <span class="math inline">\$E(Y\|X=x)\$</span> de waarde op de <span class="math inline">\$Y\$</span>-as voor, <span class="math inline">\$x\$</span> de waarde op de <span class="math inline">\$X\$</span>-as, het *intercept* <span class="math inline">\$\\beta\_0\$</span> stelt het snijpunt met de <span class="math inline">\$Y\$</span>-as voor en de *helling* <span class="math inline">\$\\beta\_1\$</span> geeft de richtingscoëfficiënt van de rechte weer. Uitdrukking [(6.1)](index.md) wordt een *statistisch model* genoemd. Merk op dat dit model enkel een onderstelling maakt over het gemiddelde van de S100A8 expressie.

Deze naamgeving suggereert dat het bepaalde onderstellingen legt op de verdeling van de geobserveerde gegevens. In het bijzonder onderstelt het dat de gemiddelde uitkomst lineair varieert in functie van één verklarende variabele <span class="math inline">\$X\$</span>. Om die reden wordt Model [(6.1)](index.md) ook een *enkelvoudig lineair regressiemodel* genoemd. Onder dit model kan elke meting <span class="math inline">\$Y\$</span> op een foutterm <span class="math inline">\$\\epsilon\$</span> na beschreven worden als een lineaire functie van de verklarende variabele <span class="math inline">\$X\$</span>, verder in deze cursus ook de predictor genoemd:

<span class="math display">\\$$Y=E(Y\|X=x)+\\epsilon=\\beta\_0+\\beta\_1 x+\\epsilon\\$$</span>

waarbij <span class="math inline">\$\\epsilon\$</span> de afwijking tussen de uitkomst en haar (conditioneel) gemiddelde waarde voorstelt, dit is de onzekerheid in de responsvariabele.

Gezien het lineair regressiemodel onderstellingen doet over de verdeling van X en Y , kunnen deze onderstellingen ook vals zijn. Later in dit hoofdstuk zullen we zien hoe deze onderstellingen geëvalueerd kunnen worden. Als echter voldaan is aan de onderstellingen, laat dit een efficiënte data-analyse toe: alle observaties worden benut om te leren over verwachte uitkomst bij X = x.

Het lineair regressiemodel kan worden gebruikt voor
- *predictie* (voorspellingen): als <span class="math inline">\$Y\$</span> ongekend is, maar <span class="math inline">\$X\$</span> wel gekend is, kunnen we <span class="math inline">\$Y\$</span> voorspellen op basis van <span class="math inline">\$X\$</span> <span class="math display">\\$$\\text{E}\\left\[Y\|X =x\\right$$=\\beta\_0 + \\beta\_1 x.\\\]</span> - *associatie*: beschrijven van de biologische relatie tussen variabele <span class="math inline">\$X\$</span> en continue meting <span class="math inline">\$Y\$</span>:

<span class="math display">\\$$\\text{E}\\left\[Y\|X=x+\\delta\\right$$-\\text{E}\\left$$Y\|X=x\\right$$= \\left$$\\beta\_0+\\beta\_1(x+\\delta)\\right$$-(\\beta\_0+\\beta\_1x)=\\beta\_1\\delta\\\]</span>

waarbij <span class="math inline">\$\\beta\_1\$</span> het verschil is in gemiddelde uitkomst tussen subjecten die 1 eenheid verschillen in de genexpressie van het ESR1 gen.

## <span class="header-section-number">6.3</span> Parameterschatting

De parameters <span class="math inline">\$\\beta\_0\$</span> en <span class="math inline">\$\\beta\_1\$</span> zijn onbekenden. Indien de volledige studiepopulatie geobserveerd werd, dan zouden beide parameters exact bepaald kunnen worden (door bijvoorbeeld in 2 x-waarden de gemiddelde uitkomst te berekenen en vervolgens het resulterende stelsel van 2 vergelijkingen, bepaald door Model [(6.1)](index.md), op te lossen).

In de praktijk observeert men slechts een beperkte steekproef uit de studiepopulatie en is de taak om die parameters te schatten op basis van de beschikbare observaties. Deze schatting gebeurt door naar de lijn te zoeken die “het best past” bij de gegevens. Daarbij wil men dat bij een gegeven waarde <span class="math inline">\$x\_i\$</span> voor het <span class="math inline">\$i\$</span>-de subject het punt op de regressielijn, <span class="math inline">\$(x\_i, \\beta\_0 + \\beta\_1 x\_i)\$</span>, zo weinig mogelijk afwijkt van de overeenkomstige observatie <span class="math inline">\$(x\_i, y\_i)\$</span>. Dit realiseert men door deze waarden voor <span class="math inline">\$\\beta\_0\$</span> en <span class="math inline">\$\\beta\_1\$</span> te kiezen die de som van die kwadratische afstanden tussen de voorspelde en geobserveerde punten,

<span class="math display">\\$$\\sum\_{i=1}^n (y\_i-\\beta\_0-\\beta\_1 x\_i)^2=\\sum\_{i=1}^n e\_i^2\\$$</span>

zo klein mogelijk maakt. Waarbij <span class="math inline">\$e\_i\$</span> de verticale afstanden van de observaties tot de gefitte regressierechte, ook wel residuen genoemd (zie Figuur [6.5](index.md)).

``` {.sourceCode .r}
borstkankerSubset<-subset(borstkanker,S100A8<2000)
plot(S100A8~ESR1,borstkankerSubset)
lm1 <- lm(S100A8~ESR1,borstkankerSubset)
abline(lm1,col=2)
points(borstkankerSubset$ESR1,lm1$fitted,col=2,pch=2)
 for (i in 1:length(borstkankerSubset$S100A8)) lines(rep(borstkankerSubset$ESR1[i],2),c(lm1$fitted[i],borstkankerSubset$S100A8[i]),lty=2,col=1)
legend("topright",lty=c(0,2,0,1),col=c(1,1,2,2),pch=c(1,26,2,26),legend=c("observatie","residu","predictie","regressielijn"))
```

<span id="fig:brcaLinRes"></span> <img src="Statistiek_2019_2020_files/figure-html/brcaLinRes-1.png" style="width:100.0%" alt="Scatterplot voor S100A8 expressie in functie van de ESR1 expressie met lineair model en residuen." />

Figuur 6.5: Scatterplot voor S100A8 expressie in functie van de ESR1 expressie met lineair model en residuen.

De rechte die men aldus bekomt, noemt men de *kleinste kwadratenlijn* en is de best passende rechte door de puntenwolk.

De overeenkomstige waarden of schattingen <span class="math inline">\$\\hat{\\beta}\_0\$</span> voor <span class="math inline">\$\\beta\_0\$</span> en <span class="math inline">\$\\hat{\\beta}\_1\$</span> voor <span class="math inline">\$\\beta\_1\$</span>, noemt men *kleinste kwadratenschattingen*.

Men kan eenvoudig aantonen dat <span class="math display">\\$$\\hat{\\beta\_1}= \\frac{\\sum\\limits\_{i=1}^n (y\_i-\\bar y)(x\_i-\\bar x)}{\\sum\\limits\_{i=1}^n (x\_i-\\bar x\_i)^2}=\\frac{\\mbox{cor}(x,y)s\_y}{s\_x} \\$$</span> en dat

<span class="math display">\\$$\\hat{\\beta\_0}=\\bar y - \\hat{\\beta}\_1 \\bar x \\$$</span> Merk op dat de helling van de kleinste kwadratenlijn evenredig is met de correlatie tussen de uitkomst en de verklarende variabele.

Voor gegeven schattingen <span class="math inline">\$\\hat{\\beta}\_0\$</span> voor <span class="math inline">\$\\beta\_0\$</span> en <span class="math inline">\$\\hat{\\beta}\_1\$</span> voor <span class="math inline">\$\\beta\_1\$</span> laat het lineaire regressiemodel [(6.1)](index.md) toe om:

- de verwachte uitkomst te voorspellen voor subjecten met een gegeven waarde <span class="math inline">\$x\$</span> voor de verklarende variabele. Deze kan geschat worden als <span class="math inline">\$\\hat{\\beta}\_0+\\hat{\\beta}\_1x\$</span>.
- na te gaan hoeveel de uitkomst gemiddeld verschilt tussen 2 groepen subjecten met een verschil van <span class="math inline">\$\\delta\$</span> eenheden in de verklarende variabele. Namelijk:

<span class="math display">\\$$\\text{E}\\left\[Y\|X=x+\\delta\\right$$-\\text{E}\\left$$Y\|X=x\\right$$= \\hat{\\beta}\_1\\delta\\\]</span>

Voor de borstkanker dataset levert een analyse van de gegevens in R de volgende resultaten op.

``` {.sourceCode .r}
lm1 <- lm(S100A8~ESR1,borstkankerSubset)
summary(lm1)
```

    ##
    ## Call:
    ## lm(formula = S100A8 ~ ESR1, data = borstkankerSubset)
    ##
    ## Residuals:
    ##    Min     1Q Median     3Q    Max
    ## -95.43 -34.81  -6.79  34.23 145.21
    ##
    ## Coefficients:
    ##              Estimate Std. Error t value Pr(>|t|)
    ## (Intercept) 208.47145   28.57207   7.296 7.56e-08 ***
    ## ESR1         -0.05926    0.01212  -4.891 4.08e-05 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ##
    ## Residual standard error: 59.91 on 27 degrees of freedom
    ## Multiple R-squared:  0.4698, Adjusted R-squared:  0.4502
    ## F-statistic: 23.93 on 1 and 27 DF,  p-value: 4.078e-05

De software rapporteert <span class="math inline">\$\\hat{\\beta}\_0=\$</span> 208.47 en <span class="math inline">\$\\hat{\\beta}\_1=\$</span>-0.059. We besluiten dat, de verwachte S100A8 expressie gemiddeld -59 eenheden lager ligt bij patiënten met een ESR1 expressieniveau die 1000 eenheden hoger ligt. Bovendien kunnen we de S100A8 expressie voorspellen die men mag verwachten bij een gegeven ESR1 expressieniveau. Bijvoorbeeld, bij een ESR1 expressieniveau van 1300 verwachten we een S100A8 expressieniveau van 208.47 <span class="math inline">\$-\$</span> 0.059 <span class="math inline">\$\\times\$</span> 1300= 131.43.

Merk op in Figuur [6.4](index.md) dat er in de dataset geen patiënt is geobserveerd die een ESR1 expressieniveau had van 1300. Op basis van de dataset zou het bijgevolg niet mogelijk zijn om, zonder gebruik te maken van een statistisch model, een schatting te bekomen voor de S100A8 expressie bij deze ESR1 expressiewaarde. Onder de veronderstelling dat de gemiddelde S100A8 expressie lineair varieert in functie van de ESR1 expressie, kunnen we alle observaties gebruiken om dit gemiddelde te schatten. Bijgevolg bekomen we een zinvol en precies resultaat, op voorwaarde dat aan de veronderstelling van lineariteit is voldaan. Het zal bijgevolg belangrijk zijn om de veronderstelling van lineariteit na te gaan (zie verder).

Gezien de lineariteit van het model enkel kan worden nagegaan over het geobserveerde bereik van de verklarende variabele (bijvoorbeeld, over het interval 396.1,3967.2), is het belangrijk om te begrijpen dat de resultaten van een lineair regressiemodel niet zomaar kunnen geëxtrapoleerd worden voorbij de kleinste of grootste geobserveerde <span class="math inline">\$X\$</span>-waarde. Met het model kunnen we de verwachte S100A8 intensiteit voor patiënten met een ESR1 expressie-niveau van 4500 schatten, maar de geobserveerde data laten niet toe om na te gaan of dit een betrouwbare schatting is. Het zou immers kunnen dat de regressielijn bij hoge waarden van de predictorvariabele afbuigt of opklimt waardoor een lineaire extrapolatie misleidend zou zijn. Merk zo bijvoorbeeld op dat predictie bij een ESR1 intensiteit van 4500 bijzonder misleidend is vermits ze een negatief resultaat oplevert wat onmogelijk is voor een intensiteitsmeting (208.47 <span class="math inline">\$+\$</span> -0.059 <span class="math inline">\$\\times\$</span> 4500= -58.22).

## <span class="header-section-number">6.4</span> Statistische besluitvorming {#statistische-besluitvorming}

Als de gegevens representatief zijn voor de populatie kan men in de regressiecontext eveneens aantonen dat de kleinste kwadraten schatters voor het intercept en de helling onvertekend zijn, m.a.w <span class="math display">\\$$E\[\\hat \\beta\_0$$=\\beta\_0 \\text{ en } E$$\\hat \\beta\_1$$=\\beta\_1\\\]</span> Het feit dat de schatters gemiddeld (over een groot aantal vergelijkbare studies) niet afwijken van de waarden in de populatie, impliceert niet dat ze niet rond die waarde variëren. Om inzicht te krijgen hoe dicht we de parameterschatters bij het werkelijke intercept <span class="math inline">\$\\beta\_0\$</span> en de werkelijke helling <span class="math inline">\$\\beta\_1\$</span> mogen verwachten, wensen we bijgevolg ook haar variabiliteit te kennen.

In de borstkanker dataset hebben we een negatieve associatie geobserveerd tussen de S100A8 en ESR1 gen expressie. Net zoals in Hoofdstuk [5](../chap-besluit/index.md) is het op basis van de puntschatters voor de helling niet duidelijk of dat verband werkelijk voorkomt in de populatie of indien we het verband door toeval hebben geobserveerd in de dataset. De schatting van de helling is immers onnauwkeurig en zal variëren van steekproef tot steekproef. Het resultaat van een data-analyse is dus niet interpreteerbaar zonder die variabiliteit in kaart te brengen.

Om de resultaten uit de steekproef te kunnen veralgemenen naar de populatie zullen we in deze context eveneens inzicht nodig hebben op de verdeling van de parameterschatters. Om te kunnen voorspellen hoe de parameterschatters variëren van steekproef tot steekproef enkel en alleen op basis van slechts één steekproef zullen we naast de onderstelling van

1.  *Lineariteit*

bijkomende aannames moeten maken over de verdeling van de gegevens, met name

1.  *Onafhankelijkheid*: de metingen <span class="math inline">\$(X\_1,Y\_1), ..., (X\_n,Y\_n)\$</span> werden gemaakt bij n onafhankelijke subjecten/observationele eenheden
2.  *Homoscedasticiteit* of *gelijkheid van variantie*: de observaties variëren met een gelijke variantie rond de regressierechte. De residuen <span class="math inline">\$\\epsilon\_i\$</span> hebben dus een gelijke variantie <span class="math inline">\$\\sigma^2\$</span> voor elke <span class="math inline">\$X\_i=x\$</span>. Dat impliceert ook dat de conditionele variantie van Y gegeven X<a href="#fn39" id="fnref39" class="footnoteRef"><sup>39</sup></a>, <span class="math inline">\$\\text{var}(Y\\vert X=x)\$</span> dus gelijk is, met name <span class="math inline">\$\\text{var}(Y\\vert X=x) = \\sigma^2\$</span> voor elke waarde <span class="math inline">\$X=x\$</span>. De constante <span class="math inline">\$\\sigma\$</span> wordt ook de *residuele standaarddeviatie* genoemd.
3.  *Normaliteit*: de residuen <span class="math inline">\$\\epsilon\_i\$</span> zijn normaal verdeeld.

Uit 2, 3 en 4 volgt dus dat de residuen <span class="math inline">\$\\epsilon\_i\$</span> onafhankelijk zijn en dat ze allen eenzelfde Normale verdeling volgen <span class="math display">\\$$\\epsilon\_i \\sim N(0,\\sigma^2).\\$$</span> Als we ook steunen op de veronderstelling van lineariteit weten we dat de originele observaties conditioneel op <span class="math inline">\$X\$</span> eveneens Normaal verdeeld zijn <span class="math display">\\$$Y\_i\\sim N(\\beta\_0+\\beta\_1 X\_i,\\sigma^2),\\$$</span> met een gemiddelde dat varieert in functie van de waarde van de onafhankelijke variabele <span class="math inline">\$X\_i\$</span>.

Verder kan men aantonen dat onder deze aannames <span class="math display">\\$$\\sigma^2\_{\\hat{\\beta}\_0}=\\frac{\\sum\\limits\_{i=1}^n X^2\_i}{\\sum\\limits\_{i=1}^n (X\_i-\\bar X)^2} \\times\\frac{\\sigma^2}{n} \\text{ en } \\sigma^2\_{\\hat{\\beta}\_1}=\\frac{\\sigma^2}{\\sum\\limits\_{i=1}^n (X\_i-\\bar X)^2}\\$$</span> en dat de parameterschatters eveneens normaal verdeeld zijn <span class="math display">\\$$\\hat\\beta\_0 \\sim N\\left(\\beta\_0,\\sigma^2\_{\\hat \\beta\_0}\\right) \\text{ en } \\hat\\beta\_1 \\sim N\\left(\\beta\_1,\\sigma^2\_{\\hat \\beta\_1}\\right)\\$$</span>

Merk op dat de onzekerheid op de helling af zal nemen wanneer er meer observaties zijn en/of wanneer de observaties meer gespreid zijn. Voor het opzetten van een experiment kan dit belangrijke informatie zijn. Uiteraard wordt de precisie ook beïnvloed door de grootte van de variabiliteit van de observaties rond de rechte, <span class="math inline">\$\\sigma^2\$</span>, maar dat heeft een onderzoeker meestal niet in de hand.

De conditionele variantie (<span class="math inline">\$\\sigma^2\$</span>) is echter niet gekend en is noodzakelijk voor de berekening van de variantie op de parameterschatters. We kunnen <span class="math inline">\$\\sigma^2\$</span> echter ook schatten op basis van de observaties. Zoals beschreven in Hoofdstuk [4](../chap-describe/index.md) kunnen we de variatie van de uitkomsten rond hun conditionele gemiddelde beschrijven d.m.v. de afwijkingen tussen de observaties <span class="math inline">\$y\_i\$</span> en hun (geschatte) gemiddelde <span class="math inline">\$\\hat{g}(x)=\\hat{\\beta}\_0+\\hat{\\beta}\_1x\_i\$</span>, de residu’s. Het gemiddelde van die residu’s is echter altijd 0 omdat positieve en negatieve residu’s mekaar opheffen. Bijgevolg levert het gemiddelde residu geen goede maat op voor de variatie en is het beter om naar kwadratische afwijkingen <span class="math inline">\$e\_i^2\$</span> te kijken. Net zoals de steekproefvariantie een goede schatter was voor de variantie (Sectie [4.3.2](../chap-describe/index.md)), zal in de regressiecontext het gemiddelde van die kwadratische afwijkingen rond de regressierechte opnieuw een goede schatter zijn voor <span class="math inline">\$\\sigma^2\$</span>. Deze schatter wordt in de literatuur ook wel de *mean squared error* (MSE) genoemd. <span class="math display">\\$$\\hat\\sigma^2=MSE=\\frac{\\sum\\limits\_{i=1}^n \\left(y\_i-\\hat\\beta\_0-\\hat\\beta\_1\\times x\_i\\right)^2}{n-2}=\\frac{\\sum\\limits\_{i=1}^n e^2\_i}{n-2}.\\$$</span> Voor het bekomen van deze schatter steunen we op onafhankelijkheid (aanname 2) en homoscedasticiteit (aanname 3). Merk op dat we bij deze schatter niet delen door het aantal observaties <span class="math inline">\$n\$</span>, maar door <span class="math inline">\$n-2\$</span>. Hierbij corrigeren we voor het feit dat voor de berekening van MSE 2 vrijheidsgraden worden gespendeerd aan het schatten van het intercept en de helling.

Na het schatten van MSE kunnen we <span class="math inline">\$\\sigma^2\$</span> door MSE vervangen zodat schatters worden bekomen voor de variantie en standard error op de schatters van model parameters, <span class="math display">\\$$\\text{SE}\_{\\hat{\\beta}\_0}=\\hat\\sigma\_{\\hat{\\beta}\_0}=\\sqrt{\\frac{\\sum\\limits\_{i=1}^n X^2\_i}{\\sum\\limits\_{i=1}^n (X\_i-\\bar X)^2} \\times\\frac{\\text{MSE}}{n}} \\text{ en } \\text{SE}\_{\\hat{\\beta}\_1}=\\hat\\sigma\_{\\hat{\\beta}\_1}=\\sqrt{\\frac{\\text{MSE}}{\\sum\\limits\_{i=1}^n (X\_i-\\bar X)^2}}\\$$</span>

Analoog als in Hoofdstuk [5](../chap-besluit/index.md) kunnen we opnieuw toetsen en betrouwbaarheidsintervallen construeren op basis van de teststatistieken
<span class="math display">\\$$T=\\frac{\\hat{\\beta}\_k-\\beta\_k}{SE(\\hat{\\beta}\_k)} \\text{ met } k=1,2.\\$$</span> Als aan alle aannames is voldaan dan volgen deze statistieken <span class="math inline">\$T\$</span> een t-verdeling met n-2 vrijheidsgraden. Wanneer niet is voldaan aan de veronderstelling van normaliteit maar wel aan lineariteit, onafhankelijkheid en homoscedasticiteit dan kunnen we voor inferentie opnieuw beroep doen op de centrale limietstelling die zegt dat de statistiek T bij benadering een standaard Normaal verdeling zal volgen wanneer het aantal observaties voldoende groot is.

In de borstkanker dataset hebben we een negatieve associatie geobserveerd tussen de S100A8 en ESR1 gen expressie. We kunnen het effect in de steekproef nu veralgemenen naar de populatie toe door een betrouwbaarheidsinterval te bouwen voor de helling: <span class="math display">\\$$\[\\hat\\beta\_1 - t\_{n-2,\\alpha/2} \\text{SE}\_{\\hat\\beta\_1},\\hat\\beta\_1 + t\_{n-2,\\alpha/2} \\text{SE}\_{\\hat\\beta\_1}$$\\\]</span>.

``` {.sourceCode .r}
confint(lm1)
```

    ##                    2.5 %       97.5 %
    ## (Intercept) 149.84639096 267.09649989
    ## ESR1         -0.08412397  -0.03440378

Op basis van de R-output bekomen we een 95% betrouwbaarheidsinterval voor de helling $$-0.084,-0.034$$. Gezien nul niet in het interval ligt weten we eveneens dat de negatieve associatie statistisch significant is op het 5% significantieniveau.

Anderzijds kunnen we ook een formele hypothesetoets uitvoeren. Onder de nulhypothese veronderstellen we dat er geen associatie is tussen de expressie van beide genen: <span class="math display">\\$$H\_0: \\beta\_1=0\\$$</span> en onder de alternatieve hypothese is er een associatie tussen beide genen: <span class="math display">\\$$H\_1: \\beta\_1\\neq0\\$$</span>

Met de test statistiek <span class="math display">\\$$T=\\frac{\\hat{\\beta}\_1-0}{SE(\\hat{\\beta}\_k)}\\$$</span> kunnen we de nulhypothese falsifiëren. Onder <span class="math inline">\$H\_0\$</span> volgt de statistiek een t-verdeling met n-2 vrijheidsgraden.

Deze tweezijdige test is geïmplementeerd in de standaard output van R.

``` {.sourceCode .r}
summary(lm1)
```

    ##
    ## Call:
    ## lm(formula = S100A8 ~ ESR1, data = borstkankerSubset)
    ##
    ## Residuals:
    ##    Min     1Q Median     3Q    Max
    ## -95.43 -34.81  -6.79  34.23 145.21
    ##
    ## Coefficients:
    ##              Estimate Std. Error t value Pr(>|t|)
    ## (Intercept) 208.47145   28.57207   7.296 7.56e-08 ***
    ## ESR1         -0.05926    0.01212  -4.891 4.08e-05 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ##
    ## Residual standard error: 59.91 on 27 degrees of freedom
    ## Multiple R-squared:  0.4698, Adjusted R-squared:  0.4502
    ## F-statistic: 23.93 on 1 and 27 DF,  p-value: 4.078e-05

De test geeft weer dat de associatie tussen de S100A8 en ESR1 genexpressie extreem significant is (p&lt;&lt;0.001). Als de nulhypothese waar is en als aan alle voorwaarden is voldaan dan is er een kans van 4 op 100000 om een helling te vinden die minstens even extreem is door toeval. Het is bijgevolg heel onwaarschijnlijk om dergelijke associatie te observeren in een steekproef wanneer de nulhypothese waar is.

Vooraleer we een conclusie trekken is het echter belangrijk dat we alle aannames verifiëren omdat de statistische test en de betrouwbaarheidsintervallen anders incorrect zijn.

## <span class="header-section-number">6.5</span> Nagaan van modelveronderstellingen

Voor de statistische besluitvorming hebben we volgende aannames gedaan

1.  Lineariteit
2.  Onafhankelijkheid
3.  Homoscedasticiteit
4.  Normaliteit

Onafhankelijkheid is moeilijk te verifiëren op basis van de data, dat zou gegarandeerd moeten zijn door het design van de studie. Als we afwijkingen zien van lineariteit dan heeft besluitvorming geen zin gezien het de primaire veronderstelling is. In dat geval moeten we het conditioneel gemiddeld eerst beter modelleren. In geval van lineariteit maar schendingen van homoscedasticiteit of normaliteit dan weten we dat de besluitvorming mogelijks incorrect is omdat de teststatistiek dan niet langer een t-verdeling volgt.

### <span class="header-section-number">6.5.1</span> Lineariteit

De primaire veronderstelling in lineaire regressie-analyse is de aanname dat de uitkomst (afhankelijke variabele) lineair varieert ten opzichte van de verklarende variabele. Deze veronderstelling kan men gemakkelijk grafisch verifiëren op basis van een scatterplot waarbij men de uitkomst uitzet in functie van de verklarende variabele. Vervolgens gaat men na of het verband een lineair patroon volgt.
In Figuur [6.4](index.md) zien we systematische afwijkingen bij kleine en grote waarden voor de ESR1 expressie. De observaties liggen dan steeds systematisch boven de regressierechte wat aangeeft dat het gemiddelde in deze regio’s systematisch wordt onderschat. Afwijkingen van lineariteit worden vaak echter makkelijker opgespoord d.m.v. een *residuplot*. Dit is een scatterplot met de verklarende variabele op de <span class="math inline">\$X\$</span>-as en de *residuen* op de <span class="math inline">\$Y\$</span>-as <span class="math display">\\$$e\_i=y\_i-\\hat{g}(x\_i)=y\_i-\\hat\\beta\_0-\\hat\\beta\_1\\times x\_i,\\$$</span> deze werden weergegeven in Figuur [6.5](index.md).

Als de veronderstelling van lineariteit opgaat, krijgt men in een residuplot geen patroon te zien. De residuen zijn immers gemiddeld nul voor elke waarde van de predictor en zouden dus mooi rond nul moeten variëren.

Wanneer de residu’s echter een niet-lineair patroon onthullen, dan geeft dit aan dat extra termen in het model moeten worden opgenomen om de gemiddelde uitkomst correct te voorspellen. Bijvoorbeeld, wanneer de residu’s een kwadratisch patroon onthullen, dan kunnen we schrijven dat bij benadering <span class="math inline">\$e\_i\\approx \\delta\_0+\\delta\_1 x\_i+\\delta\_2 x\_i^2\$</span> voor zekere getallen <span class="math inline">\$\\delta\_0,\\delta\_1,\\delta\_2\$</span>, en bijgevolg dat de uitkomst <span class="math inline">\$y\_i=\\hat{\\alpha}+\\hat{\\beta}x\_i+e\_i\\approx (\\hat{\\alpha}+\\delta\_0)+(\\hat{\\beta}+\\delta\_1)x\_i+\\delta\_2 x\_i^2\$</span> (op een foutterm na) een kwadratische functie is van <span class="math inline">\$x\_i\$</span>. In dat geval is het aangewezen om op een kwadratisch regressiemodel over te stappen (zie Hoofdstuk [10](../chap-glm/index.md)). Residuplots worden standaard gegenereerd door de R-software. Hier worden de residuen echter geplot ten opzichte van de gefitte waarden wat eenvoudiger is wanneer meerdere predictoren in het model worden opgenomen (zie Hoofdstuk [10](../chap-glm/index.md)).

``` {.sourceCode .r}
par(mfrow=c(2,2))
plot(lm1)
```

<span id="fig:brcaLinDiag1"></span> <img src="Statistiek_2019_2020_files/figure-html/brcaLinDiag1-1.png" style="width:100.0%" alt="Diagnostische plots voor het nagaan van de veronderstellingen van het lineair regressiemodel waarbij de S100A8 expressie wordt gemodelleerd i.f.v de ESR1 expressie (na verwijdering van 3 outliers)." />

Figuur 6.6: Diagnostische plots voor het nagaan van de veronderstellingen van het lineair regressiemodel waarbij de S100A8 expressie wordt gemodelleerd i.f.v de ESR1 expressie (na verwijdering van 3 outliers).

De residu plot voor het borstkanker voorbeeld wordt weergegeven in Figuur [6.6](index.md) boven links. De residuen zijn niet overal mooi gespreid rond nul. Bij lage en hoge voorspelde waarden voor het model (dus bij hoge en lage waarden voor de predictor, negatieve helling) zijn de residuen overwegend positief wat opnieuw aangeeft dat het model de data in deze regio’s systematisch onderschat. Dat was ergens te verwachten gezien de smoother in Figuur [6.3](index.md) immers eerder een exponentiëel verband suggereerde. Bovendien voorspelde het regressiemodel eveneens negatieve waarden voor de S100A8 expressie wat onmogelijk is voor intensiteitsmetingen die immers steeds positief zijn.

### <span class="header-section-number">6.5.2</span> Veronderstelling van homoscedasticiteit (gelijkheid van variantie)

Residuen en kwadratische residu’s dragen informatie in zich over residuele variabiliteit. Als er homoscedasiticiteit is dan verwachten we dat de residuen eenzelfde spreiding hebben voor elke waarde van de predictor en voor elke predictie. Als de spreiding in de residuen geassocieerd zijn met de verklarende variabelen, dan is er indicatie van heteroscedasticiteit. De diagnostische plots van het software pakket R geven een residu-plot weer en een plot van de vierkantswortel van de absolute waarde van de gestandardiseerde error <span class="math inline">\$\\sqrt{\|e\_i\|/\\sqrt{MSE}}\$</span> in functie van de predicties. De residu-plot voor het borstkanker voorbeeld Figuur [6.6](index.md) boven links geeft afwijkingen weer van homoscedasiticiteit. De spreiding in de residuen lijkt toe te nemen met een toenemende waarde van de predictor. De plot beneden links is specifiek om de voorwaarde van gelijkheid van variantie na te gaan en geeft eveneens aan dat de variantie toeneemt met het conditioneel gemiddelde. Een dergelijke trend komt dikwijls voor bij concentratiemetingen en intensiteitsmetingen, die vaak een multiplicatieve errorstructuur vertonen i.p.v. een additieve error.

Voor bepaalde types uitkomsten bestaan er *variantie-stabiliserende transformaties* voor de afhankelijke variabele die erop gericht zijn om de onderstelling van homoscedasticiteit te doen opgaan. Voor proporties of percentages, gebruikt men bijvoorbeeld vaak de arcsin-transformatie die de uitkomst <span class="math inline">\$Y\$</span> omzet in <span class="math inline">\$\\arcsin\\sqrt{Y}\$</span>, omdat men kan aantonen dat percentages (onder bepaalde onderstellingen) een constante variantie hebben na deze transformatie. Voor concentraties en intensiteitsmetingen gebruikt men dan weer vaak een logaritmische transformatie gezien deze (a) positief zijn, (b) vaak gekenmerkt worden door een variantie die toeneemt met het gemiddelde en (c) veelal een scheve verdeling vertonen maar rechts. Indien transformatie van de uitkomst niet helpt of niet wenselijk is (bijvoorbeeld, omdat het de interpretatie van het model niet ten goede komt) en er is een consistent patroon van ongelijke variantie (bijvoorbeeld, toenemende variantie in uitkomst bij toenemende predictorwaarden), dan kan men ook *gewogen kleinste kwadratenschatters* (in het Engels: *weighted least squares*) bepalen. Een verder alternatief is om *veralgemeende lineaire modellen* (in het Engels: *generalized linear models*) te schatten die tevens andere verdelingen voor de uitkomst dan de Normale verdeling toelaten. Beide klassen van oplossingen (d.i. gewogen kleinste kwadratenschatters en veralgemeende lineaire modellen) vallen echter buiten het bestek van deze cursus.

### <span class="header-section-number">6.5.3</span> Veronderstelling van normaliteit

Opnieuw kunnen we de veronderstelling van normaliteit nagaan door gebruik te maken van QQ-plots. Een QQ-plot van de afhankelijke variabele is misleidend omdat deze nagaat of de metingen voor alle subjecten samen Normaal verdeeld zijn. Dat is echter niet het geval gezien de normale verdeling per subject varieert. Elk subject kan immers andere waarde hebben voor de predictor <span class="math inline">\$X\$</span> (ESR1 expressie) en bijgevolg hebben ze een verschillend conditioneel gemiddelde. Normaal verdeelde uitkomsten bij gegeven <span class="math inline">\$x\$</span>-waarde impliceert echter dat de residu’s bij benadering Normaal verdeeld zijn. Afwijkingen van Normaliteit in een QQ-plot van de residu’s levert dus een indicatie dat de uitkomsten niet Normaal verdeeld zijn bij vaste <span class="math inline">\$x\$</span>.

Figuur [6.6](index.md) rechts boven geeft de QQ-plot weer van de residuen voor het borstkanker voorbeeld. We zien wat afwijkingen in de rechterstaart die wijzen op meerdere outliers of op observaties die systematisch hoger liggen dan wat verwacht kan worden op basis van de normaalverdeling. Dit is niet verrassend omdat heterogeniteit van de variantie vaak samengaat met niet-Normaliteit, i.h.b. scheefheid, van de gegevens. Dat komt vaak voor bij concentratie- en intensiteitsmetingen.

## <span class="header-section-number">6.6</span> Afwijkingen van Modelveronderstellingen

De primaire onderstelling in lineaire regressie-analyse is de aanname dat de uitkomst lineair varieert in de predictor. Wanneer residuplots suggereren dat aan deze onderstelling niet is voldaan, dan kan men overwegen om de verklarende variabele te transformeren. In genexpressie studies waarbij expressie als een covariaat wordt gebruikt om een andere variabele te verklaren, is het bijvoorbeeld vaak zo dat de (gemiddelde) uitkomst niet lineair varieert in functie van de predictor, maar wel in functie van het logaritme van de genexpressie. In dat geval kan men ervoor kiezen om de log-transformatie van de verklarende variabele als predictor in het model op te nemen. Vaak wordt in expressie studies een <span class="math inline">\$\\log\_2\$</span> transformatie gebruikt. In andere voorbeelden kan een andere transformatie dan de log-transformatie beter geschikt zijn, zoals de vierkantswortel (<span class="math inline">\$\\sqrt{x}\$</span>) of inverse (<span class="math inline">\$1/x\$</span>) transformatie.

Een transformatie van de verklarende variabele is vaak makkelijk uit te voeren, maar bemoeilijkt wel vaak de interpretatie van de parameters in het model. Dit laatste is echter niet het geval wanneer de log-transformatie wordt gebruikt, een stijging in <span class="math inline">\$log\_2\$</span>-expressie met bijvoorbeeld 1 eenheid is immers equivalent met een wijziging in genexpressie met een factor <span class="math inline">\$2^1=2\$</span>. Kenmerkend aan transformatie van de verklarende variabele is dat ze geen rechtstreekse invloed heeft op de homogeniteit van de variantie en de Normaliteit van de uitkomst (bij vaste waarden van de predictorvariabele), tenzij door het verbeteren van de lineariteit van het model. Om die reden is deze optie vaak minder geschikt wanneer er sterke afwijkingen van Normaliteit zijn.

Een alternatieve mogelijkheid om de lineariteit van het model te verbeteren, is hogere orde regressie (in het Engels: *higher order regression*. Hierbij modelleert men rechtstreeks niet-lineaire relaties door hogere orde termen in het model op te nemen. Zo kan men bijvoorbeeld een tweede orde model beschouwen: <span class="math display">\\$$E(Y\|X)=\\beta\_0+\\beta\_1X+\\beta\_2X^2\\$$</span> zodat de regressiekromme eruit ziet als een parabool, of een derde orde model: <span class="math display">\\$$E(Y\|X)=\\beta\_0+\\beta\_1X+\\beta\_2X^2+\\beta\_3X^3\\$$</span> zodat de regressiekromme een derdegraadspolynoom is. Deze methode kan gezien worden als een vorm van transformatie van de verklarende variabele en bezit wezenlijk dezelfde eigenschappen en voor- en nadelen. Een bijkomend voordeel is echter dat het hier niet nodig is om zelf een transformatie te zoeken, maar dat de methode zelf impliciet een goede polynoom als transformatie schat.

Tenslotte kan men ook overwegen om, in plaats van de verklarende variabele, de uitkomst te transformeren. Bijvoorbeeld, wanneer de uitkomsten scheef verdeeld zijn naar rechts is het vaak aangewezen om een log-transformatie van de uitkomst uit te voeren en deze nieuwe variabele als uitkomst in het model op te nemen. Doorgaans verbetert dit niet alleen de lineariteit van het model, maar maakt het ook de residu’s beter Normaal verdeeld met een meer constante variabiliteit. Deze methode heeft dezelfde voor- en nadelen als transformatie van de verklarende variabele. Een groot verschil dat de keuze tussen beide methoden beïnvloedt is dat transformaties van de onafhankelijke variabele weinig of geen invloed hebben op de verdeling van de residu’s (tenzij via wijzigingen in hun gemiddelde) in tegenstelling tot transformaties van de afhankelijke variabele. In het bijzonder blijven Normaal verdeelde residu’s vrij Normaal verdeeld na transformatie van de verklarende variabele, terwijl ze mogelijks niet langer Normaal verdeeld zijn na transformatie van de uitkomst, en vice versa.

In het borstkanker voorbeeld wordt de S100A8 genexpressie gemodelleerd in functie van de ESR1 genexpressie. Er waren problemen m.b.t. heteroscedasticiteit, mogelijkse afwijking van normaliteit (scheefheid naar rechts), negatieve concentratievoorspellingen die theoretisch niet mogelijk zijn en niet-lineairiteit. Dergelijke problemen treden veelal op bij concentratie en intensiteitsmetingen. Deze zijn vaak log-normaal verdeeld (normale verdeling na log-transformatie) en worden daarom vaak log-getransformeerd. Bovendien zagen we in Figuur [6.3](index.md) eveneens een soort exponentiële trend. In de genexpressie literatuur wordt veelal gebruik gemaak van <span class="math inline">\$\\log\_2\$</span> transformatie gezien een verschil van 1 op log-schaal een verdubbeling impliceert in de expressie op de originele schaal. Wanneer men gen-expressie op log-schaal modelleert, modellert men dus in feite proportionele verschillen op de originele schaal wat ook meer relevant is vanuit een biologisch standpunt.

In deze sectie zullen we beide genexpressies <span class="math inline">\$\\log\_2\$</span> transformeren en een log-lineaire regressie uitvoeren. Zoals we zullen zien vormen de outliers in de S100A8 expressie na log-transformatie ook geen problemen meer.

``` {.sourceCode .r}
borstkanker$log2S100A8 <- log2(borstkanker$S100A8)
borstkanker$log2ESR1 <- log2(borstkanker$ESR1)
lm2 <- lm(log2S100A8~log2ESR1,borstkanker)
with(borstkanker, scatter.smooth(log2ESR1,log2S100A8,lpars=list(lty=2)))
abline(lm2)
legend("topright",lty=1:2,legend=c("Lineair model","Smoother"))
```

<span id="fig:brcaLogLin"></span> <img src="Statistiek_2019_2020_files/figure-html/brcaLogLin-1.png" style="width:100.0%" alt="Scatterplot voor log2-S100A8 expressie in functie van de log2-ESR1 expressie met smoother en lineair model die het verband tussen beide genen samenvatten (outliers worden niet langer verwijderd uit de dataset)." />

Figuur 6.7: Scatterplot voor log2-S100A8 expressie in functie van de log2-ESR1 expressie met smoother en lineair model die het verband tussen beide genen samenvatten (outliers worden niet langer verwijderd uit de dataset).

In Figuur [6.7](index.md) zien we duidelijk een dalende lineaire trend van de S100A8 expressie i.f.v. de ESR1 expressie na log-transformatie. De smoother toont ook niet langer een afwijking aan van lineariteit. Daarnaast kunnen we alle data meenemen in de analyse en kan het model geen negatieve expressiewaarden meer voorspellen na terugtransformatie. In Figuur [6.8](index.md) zien we tevens dat er niet langer afwijkingen zijn van lineariteit, normaliteit en gelijkheid van variantie. De residuen in de residu-plot liggen mooi rond nul en hebben een constante spreiding. De QQ-plot toont geen systematische afwijkingen van normaliteit en de plot links beneden toont ook geen trend in de variantie van de residuen.

``` {.sourceCode .r}
par(mfrow=c(2,2))
plot(lm2)
```

<span id="fig:brcaLogLin2"></span> <img src="Statistiek_2019_2020_files/figure-html/brcaLogLin2-1.png" style="width:100.0%" alt="Diagnostische plots voor het lineair model voor log2-S100A8 expressie in functie van de log2-ESR1." />

Figuur 6.8: Diagnostische plots voor het lineair model voor log2-S100A8 expressie in functie van de log2-ESR1.

Na log-transformatie zijn alle voorwaarden voldaan en kunnen we overgaan tot statistische besluitvorming en interpretatie van de modelparameters.

``` {.sourceCode .r}
summary(lm2)
```

    ##
    ## Call:
    ## lm(formula = log2S100A8 ~ log2ESR1, data = borstkanker)
    ##
    ## Residuals:
    ##      Min       1Q   Median       3Q      Max
    ## -1.94279 -0.66537  0.08124  0.68468  1.92714
    ##
    ## Coefficients:
    ##             Estimate Std. Error t value Pr(>|t|)
    ## (Intercept)   23.401      1.603   14.60 3.57e-15 ***
    ## log2ESR1      -1.615      0.150  -10.76 8.07e-12 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ##
    ## Residual standard error: 1.026 on 30 degrees of freedom
    ## Multiple R-squared:  0.7942, Adjusted R-squared:  0.7874
    ## F-statistic: 115.8 on 1 and 30 DF,  p-value: 8.07e-12

``` {.sourceCode .r}
confint(lm2)
```

    ##                 2.5 %    97.5 %
    ## (Intercept) 20.128645 26.674023
    ## log2ESR1    -1.921047 -1.308185

Er is een extreem significante negatieve associatie tussen de S100A8 en ESR1 genexpressie (<span class="math inline">\$p&lt;&lt;0.001\$</span>).

**Interpretatie 1**

Een groep patiënten met een ESR1 expressie die 1 eenheid op de <span class="math inline">\$\\log\_2\$</span> schaal hoger ligt dan dat van een andere groep patiënten heeft gemiddeld gezien een expressie-niveau van het S100A8 gen dat 1.61 eenheden lager ligt (95% BI $$-1.92,-1.31$$). <span class="math display">\\$$\\log\_2 \\hat\\mu\_1=23.401 -1.615 \\times \\text{logESR}\_1,\\text{ } \\log\_2 \\hat\\mu\_2=23.401 -1.615 \\times \\text{logESR}\_2 \\$$</span> <span class="math display">\\$$\\log\_2 \\hat\\mu\_2-\\log\_2 \\hat\\mu\_1= -1.615 (\\log\_2 \\text{ESR}\_2-\\log\_2 \\text{ESR}\_1) = -1.615 \\times 1 = -1.615\\$$</span>

**Interpretatie 2** Wanneer de data op log-schaal wordt gemodelleerd, worden na terugtransformatie geometrische gemiddelden bekomen. Ter illustratie herschrijven we bijvoorbeeld het rekenkundig gemiddelde op de log schaal: <span class="math display">\\$$\\begin{eqnarray\*} \\sum\\limits\_{i=1}^n \\frac{\\log x\_i}{n}&=&\\frac{\\log x\_1 + \\ldots + \\log x\_n}{n}\\\\\\\\ &\\stackrel{(1)}{=}&\\frac{\\log(x\_1 \\times \\ldots \\times x\_n)}{n}=\\frac{\\log\\left(\\prod\\limits\_{i=1}^n x\_i\\right)}{n}\\\\\\\\ &\\stackrel{(2)}{=}&\\log \\left(\\sqrt\[\\leftroot{-1}\\uproot{2}\\scriptstyle n$${\\prod\\limits\_{i=1}^n x\_i}\\right) \\end{eqnarray\*}\\\]</span>

waarbij in overgang (1) en (2) wordt gesteund op de eigenschappen van logaritmen en <span class="math inline">\$\\prod\$</span> de product operator is. Na terug transformatie wordt dus een geometrisch gemiddelde <span class="math inline">\$\\sqrt$$\\leftroot{-1}\\uproot{2}\\scriptstyle n$${\\prod\\limits\_{i=1}^n x\_i}\$</span> bekomen.

In de onderstaande notatie worden de populatiegemiddelden <span class="math inline">\$\\mu\$</span> dus geschat a.d.h.v. geometrisch gemiddelden. Omdat de logaritmische transformatie een monotone transformatie is, kunnen we ook betrouwbaarheidsintervallen berekend op log-schaal terugtransformeren!

``` {.sourceCode .r}
2^lm2$coef[2]
```

    ##  log2ESR1
    ## 0.3265519

``` {.sourceCode .r}
2^-lm2$coef[2]
```

    ## log2ESR1
    ##   3.0623

``` {.sourceCode .r}
2^-confint(lm2)[2,]
```

    ##    2.5 %   97.5 %
    ## 3.786977 2.476298

Een groep patiënten met een dubbel zo hoge ESR1 expressie hebben gemiddeld een S100A8 expressie die 3.06 keer lager ligt (95% BI $$2.48,3.79$$).

<span class="math display">\\$$\\log\_2 \\hat\\mu\_1=23.401 -1.615 \\times \\text{logESR}\_1,\\text{ } \\log\_2 \\hat\\mu\_2=23.401 -1.615 \\times \\text{logESR}\_2 \\$$</span> <span class="math display">\\$$\\log\_2 \\hat\\mu\_2-\\log\_2 \\hat\\mu\_1= -1.615 (\\log\_2 \\text{ESR}\_2-\\log\_2 \\text{ESR}\_1) \\$$</span> <span class="math display">\\$$\\log\_2 \\left\[\\frac{\\hat\\mu\_2}{\\hat\\mu\_1}\\right$$= -1.615 \\log\_2\\left$$\\frac{ \\text{ESR}\_2}{\\text{ESR}\_1}\\right$$ \\\]</span> <span class="math display">\\$$\\frac{\\hat\\mu\_2}{\\hat\\mu\_1}=\\left\[\\frac{ \\text{ESR}\_2}{\\text{ESR}\_1}\\right$$^{-1.615}=2^ {-1.615} =0.326\\\]</span> of <span class="math display">\\$$\\frac{\\hat\\mu\_1}{\\hat\\mu\_2}=2^{1.615} =3.06\\$$</span>

**Interpretatie 3** Een groep patiënten met een ESR1 expressie die 1% hoger ligt dan dat van een andere groep patiënten heeft gemiddeld gezien een expressie-niveau van het S100A8 gen dat ongeveer -1.61% lager ligt (95% BI $$-1.92,-1.31$$)%. <span class="math display">\\$$\\log\_2 \\hat\\mu\_1=23.401 -1.615 \\times \\text{logESR}\_1,\\text{ } \\log\_2 \\hat\\mu\_2=23.401 -1.615 \\times \\text{logESR}\_2 \\$$</span> <span class="math display">\\$$\\log\_2 \\hat\\mu\_2-\\hat\\log\_2 \\mu\_1= -1.615 (\\log\_2 \\text{ESR}\_2-\\log\_2 \\text{ESR}\_1) \\$$</span> <span class="math display">\\$$\\log\_2 \\left\[\\frac{\\hat\\mu\_2}{\\hat\\mu\_1}\\right$$= -1.615 \\log\_2\\left$$\\frac{ \\text{ESR}\_2}{\\text{ESR}\_1}\\right$$ \\\]</span> <span class="math display">\\$$\\frac{\\hat\\mu\_2}{\\hat\\mu\_1}=\\left\[\\frac{ \\text{ESR}\_2}{\\text{ESR}\_1}\\right$$^{-1.615}=1.01^ {-1.615} =0.984 \\approx -1.6\\%\\\]</span>

Merk op dat voor waarden van <span class="math display">\\$$−10&lt; \\beta\_1&lt;10 \\rightarrow 1.01 ^{\\beta\_1}−1 \\approx \\frac{\\beta\_1}{100}.\\$$</span> Dus voor log-getransformeerde predictoren met kleine tot gematigde waarden voor <span class="math inline">\$\\beta\_1\$</span> kan de helling <span class="math inline">\$\\beta\_1\$</span> als volgt geïnterpreteerd worden: een 1% toename in de predictor resulteert gemiddelde in een <span class="math inline">\$\\beta\_1\$</span>% verschil in de uitkomst.

## <span class="header-section-number">6.7</span> Besluitvorming over gemiddelde uitkomst

In de sectie [6.4](index.md) toonden we dat de parameterschatters van het linear regressie model normaal verdeeld zijn onder de voorwaarden van onafhankelijkheid, lineariteit, homoscedasticiteit en (conditionele) normaliteit van de gegevens. Het regressie model wordt niet enkel gebruikt om de associatie tussen twee variabelen te bestuderen, maar ook om voorspellingen te doen van de response gegeven een gekende waarde voor de predictor. In dat geval wenst men vaak besluitvorming te doen over de gemiddelde uitkomst geschat met het model bij een gegeven waarde <span class="math inline">\$x\$</span>, m.a.w. <span class="math display">\\$$\\hat{g}(x)= \\hat{\\beta}\_0 + \\hat{\\beta}\_1 x\\$$</span>

Hierbij is de gemiddelde uitkomst <span class="math inline">\$\\hat{g}(x)\$</span> een schatter van het conditionele gemiddelde <span class="math inline">\$E$$Y\\vert X=x$$\$</span>. Wanneer de parameterschatters een Normale verdeling volgen zal de schatter voor de gemiddelde uitkomst ook Normaal verdeeld zijn gezien het een lineaire combinatie is van de parameterschatters. Gezien de parameterschatters onvertekend zijn, is de schatter van de gemiddelde uitkomst dat ook.

Men kan aantonen dat de standard error op de schatter voor de gemiddelde uitkomst <span class="math display">\\$$\\text{SE}\_{\\hat{g}(x)}=\\sqrt{MSE\\left\\{\\frac{1}{n}+\\frac{(x-\\bar X)^2}{\\sum\\limits\_{i=1}^n (X\_i-\\bar X)^2}\\right\\}}.\\$$</span> Dit geeft aan dat de schatter voor de gemiddelde uitkomst het meest precies is voor <span class="math inline">\$x=\\bar x\$</span> en in dit punt zelfs even precies zijn dan wanneer alle observaties <span class="math inline">\$x\_1,\\ldots, x\_n\$</span> in de steekproef gelijk zouden zijn aan <span class="math inline">\$x\$</span>.

Opnieuw kan men aantonen dat de statistiek <span class="math display">\\$$T=\\frac{\\hat{g}(x)-g(x)}{SE\_{\\hat{g}(x)}}\\sim t\_{n-2}\\$$</span> een t-verdeling volgt met <span class="math inline">\$n-2\$</span> vrijheidsgraden.

Deze statistiek kan opnieuw gebruikt worden voor besluitvorming d.m.v. hypothese testen of door de constructie van betrouwbaarheidsintervallen.

De gemiddelde uitkomst en betrouwbaarheidsintervallen op de gemiddelde uitkomst kunnen eenvoudig worden verkregen in R via de `predict(.)` functie. De predictorwaarden (x-waarden) voor het berekenen van gemiddelde uitkomsten kunnen worden meegegeven via het `newdata` argument. Betrouwbaarheidsintervallen op de geschatte gemiddelde uitkomsten kunnen worden verkregen d.m.v. het argument `interval="confidence"`. Zonder het newdata argument wordt de gemiddelde uitkomsten berekend voor alle predictorwaarden van de dataset.

``` {.sourceCode .r}
grid=log2(140:4000)
g <- predict(lm2,newdata=data.frame(log2ESR1=grid), interval="confidence")
head(g)
```

    ##        fit      lwr      upr
    ## 1 11.89028 10.76082 13.01974
    ## 2 11.87370 10.74721 13.00019
    ## 3 11.85724 10.73370 12.98078
    ## 4 11.84089 10.72028 12.96151
    ## 5 11.82466 10.70696 12.94237
    ## 6 11.80854 10.69372 12.92336

De gemiddelde uitkomst en hun 95% puntgewijze betrouwbaarheidsintervallen kunnen eveneens grafisch worden weergegeven (Figuur [6.9](index.md))

``` {.sourceCode .r}
plot(log2S100A8~log2ESR1,borstkanker,ylab="S100A8 (log2)",xlab="ESR1 (log2)")
lines(grid,g[,1])
lines(grid,g[,2],lty=2)
lines(grid,g[,3],lty=2)
legend("topright",lty=1:2,legend=c("Lineair model","95% puntgewijze BI"))
```

<span id="fig:brcaLogLinPred1"></span> <img src="Statistiek_2019_2020_files/figure-html/brcaLogLinPred1-1.png" style="width:100.0%" alt="Scatterplot voor log2-S100A8 expressie in functie van de log2-ESR1 expressie met model schattingen en 95$\%$ betrouwbaarheidsintervallen." />

Figuur 6.9: Scatterplot voor log2-S100A8 expressie in functie van de log2-ESR1 expressie met model schattingen en 95<span class="math inline">\$\\%\$</span> betrouwbaarheidsintervallen.

De gemiddelde uitkomst en hun 95% betrouwbaarheidsintervallen kunnen makkelijk worden teruggetransformeerd naar de originele schaal, zodat een geometrisch gemiddelde wordt bekomen met 95% betrouwbaarheidsintervallen op het geometrische gemiddelde. Deze kunnen dan grafisch worden weergegeven op de originele schaal in een gewone scatterplot (Figuur [6.10](index.md) links) of in een scatterplot met logaritmische assen (Figuur [6.10](index.md) rechts). In Figuur [6.10](index.md) (links) is het duidelijk dat we met het model na log-transformatie een exponentieel verband kunnen modelleren op de originele schaal.

``` {.sourceCode .r}
par(mfrow=c(1,2))
gOrig <- 2^g
plot(S100A8~ESR1,borstkanker)
lines(2^grid,gOrig[,1])
lines(2^grid,gOrig[,2],lty=2)
lines(2^grid,gOrig[,3],lty=2)
legend("topright",lty=1:2,legend=c("Geometrisch gemiddelde","95% puntgewijze BI"),cex=.5)
#cex=.5 wordt gebruikt voor kleiner lettertype
#standaard staat cex=1
plot(S100A8~ESR1,borstkanker,log="xy")
lines(2^grid,gOrig[,1])
lines(2^grid,gOrig[,2],lty=2)
lines(2^grid,gOrig[,3],lty=2)
legend("topright",lty=1:2,legend=c("Geometrisch gemiddelde","95% puntgewijze BI"),cex=.5)
```

<span id="fig:brcaLogLinPred2"></span> <img src="Statistiek_2019_2020_files/figure-html/brcaLogLinPred2-1.png" style="width:100.0%" alt="Scatterplot voor S100A8 expressie in functie van de ESR1 expressie met model schattingen (geometrische gemiddeldes) een 95$\%$ betrouwbaarheidsintervallen (links: originele schaal, rechts: originele schaal met logaritmische assen)." />

Figuur 6.10: Scatterplot voor S100A8 expressie in functie van de ESR1 expressie met model schattingen (geometrische gemiddeldes) een 95<span class="math inline">\$\\%\$</span> betrouwbaarheidsintervallen (links: originele schaal, rechts: originele schaal met logaritmische assen).

## <span class="header-section-number">6.8</span> Predictie-intervallen

Het geschatte regressiemodel kan ook worden gebruikt om een **predictie** te maken voor één uitkomst van één experiment waarbij een nieuwe uitkomst <span class="math inline">\$Y^\*\$</span> bij een gegeven <span class="math inline">\$x\$</span> zal geobserveerd worden. Het is belangrijk in te zien dat dit experiment nog moet worden uitgevoerd. We wensen dus een nog niet-geobserveerde individuele uitkomst te voorspellen.

Aangezien <span class="math inline">\$Y^\*\$</span> een nieuwe, onafhankelijke observatie voorstelt, weten we dat <span class="math display">\\$$ Y^\* = g(x) + \\epsilon^\* \\$$</span> met <span class="math inline">\$\\epsilon^\*\\sim N(0,\\sigma^2)\$</span> en <span class="math inline">\$\\epsilon^\*\$</span> onafhankelijk van de steekproefobservaties <span class="math inline">\$Y\_1,\\ldots, Y\_n\$</span>.

We weten dat <span class="math inline">\$\\hat{g}(x)\$</span> een schatting is van de gemiddelde log-S100A8 expressie bij de log-ESR1 expressie <span class="math inline">\$x\$</span>, met name een schatting van het conditioneel gemiddelde <span class="math inline">\$\\text{E}$$Y\\vert x$$\$</span>. We argumenteren nu dat <span class="math inline">\$\\hat{g}(x)\$</span> ook een goede predictie is van een nieuwe log-S100A8 expressiewaarde <span class="math inline">\$Y^\*\$</span> bij een gegeven log-ESR1 expressieniveau <span class="math inline">\$x\$</span>.

We weten reeds dat <span class="math inline">\$\\hat{g}(x)\$</span> een schatting is van <span class="math inline">\$\\text{E}$$Y\\vert x$$\$</span>, wat het punt op de regressierechte bij <span class="math inline">\$x\$</span> voorstelt. Het regressiemodel stelt dat bij een gegeven <span class="math inline">\$x\$</span>, de individuele uitkomsten <span class="math inline">\$Y\$</span> Normaal verdeeld zijn rond dit punt op de regressierechte. Aangezien een Normale verdeling symmetrisch is, is het even waarschijnlijk om een uitkomst groter dan <span class="math inline">\$\\text{E}$$Y\\vert x$$\$</span> te observeren, als een uitkomst kleiner dan <span class="math inline">\$\\text{E}$$Y\\vert x$$\$</span> te observeren. We beschikken echter niet over meer informatie dat ons zou toelaten om te vermoeden dat een uitkomst eerder groter, dan wel kleiner dan <span class="math inline">\$\\text{E}$$Y\\vert x$$\$</span> zou zijn. Om die reden is het punt op de (geschatte) regressierechte de beste predictie van een individuele uitkomst bij een gegeven <span class="math inline">\$x\$</span>.

We voorspellen dus een nieuwe log-S100A8 meting bij een gekend log2-ESR1 expressieniveau x door <span class="math display">\\$$ \\hat{y}(x)=\\hat{\\beta}\_0+\\hat{\\beta}\_1 \\times x \\$$</span> Merk op dat <span class="math inline">\$\\hat{y}(x)\$</span> eigenlijk numeriek gelijk is aan <span class="math inline">\$\\hat{g}(x)\$</span>. Gezien het verschil in interpretatie tussen een predictie en een schatting van een conditioneel gemiddelde, gebruiken we een andere notatie.

Hoewel de geschatte gemiddelde uitkomst en de predictie voor een nieuwe uitkomst gelijk zijn, zullen hun steekproefdistributies echter verschillend zijn: de onzekerheid op de geschatte gemiddelde uitkomst wordt gedreven door de onzekerheid op de parameterschatters <span class="math inline">\$\\hat\\beta\_0\$</span> en <span class="math inline">\$\\hat\\beta\_1\$</span>. De onzekerheid op de ligging van een nieuwe observatie, daarentegen, wordt gedreven door de *onzekerheid op het geschatte gemiddelde* en de *bijkomende onzekerheid* ten gevolge van het feit dat *nieuwe observaties at random variëren rond de het conditionele gemiddelde* (de regressie rechte) met een variantie <span class="math inline">\$\\sigma^2\$</span>. De nieuwe observatie is eveneens onafhankelijk van de observaties in de steekproef zodat de error <span class="math inline">\$\\epsilon\$</span> onafhankelijk zal zijn van de schatter van de gemiddelde uitkomst <span class="math inline">\$\\hat{g}(x)\$</span>. De standard error op een predictie voor een nieuwe observatie wordt dus

<span class="math display">\\$$\\text{SE}\_{\\hat{Y}(x)}=\\sqrt{\\hat\\sigma^2+\\hat\\sigma^2\_{\\hat{g}(x)}}=\\sqrt{MSE\\left\\{1+\\frac{1}{n}+\\frac{(x-\\bar X)^2}{\\sum\\limits\_{i=1}^n (X\_i-\\bar X)^2}\\right\\}}.\\$$</span>

Opnieuw kan worden aangetoond dat de statistiek <span class="math display">\\$$\\frac{\\hat{Y}(x)-Y}{\\text{SE}\_{\\hat{Y}(x)}}\\sim t\_{n-2}\\$$</span> een t-verdeling volgt met n-2 vrijheidsgraden. Deze statistiek kan gebruikt worden om een betrouwbaarheidsinterval op de predictie te construeren, ook wel een **predictie-interval** (PI) genoemd. Merk op dat dit predictie-interval een verbeterde versie is van een referentie-interval wanneer de modelparameters niet gekend zijn. Het PI houdt immers rekening met de onzekerheid op het geschatte gemiddelde (gebruik van standard error op predictie i.p.v. standaard deviatie) en deze op de geschatte standaard deviatie (gebruik van t-verdeling i.p.v Normale verdeling).

Predicties en predictie-intervallen (PIs) kunnen opnieuw eenvoudig worden verkregen in R via de `predict(.)` functie. De predictorwaarden (x-waarden) voor het berekenen van de predicties<a href="#fn40" id="fnref40" class="footnoteRef"><sup>40</sup></a> worden opnieuw meegegeven via het `newdata` argument. PIs op de predicties kunnen worden verkregen d.m.v. het argument `interval="prediction"`.

``` {.sourceCode .r}
grid=log2(140:4000)
p <- predict(lm2,newdata=data.frame(log2ESR1=grid), interval="prediction")
head(p)
```

    ##        fit      lwr      upr
    ## 1 11.89028 9.510524 14.27004
    ## 2 11.87370 9.495354 14.25205
    ## 3 11.85724 9.480288 14.23419
    ## 4 11.84089 9.465324 14.21646
    ## 5 11.82466 9.450461 14.19886
    ## 6 11.80854 9.435698 14.18138

De predicties en hun 95% puntgewijze predictie-intervallen kunnen eveneens grafisch worden weergegeven (Figuur [6.11](index.md)). Merk op dat de intervallen veel breder zijn dan de betrouwbaarheidsintervallen. Merk ook op dat de meeste observaties binnen de predictie-intervallen liggen. We verwachten inderdaad gemiddeld 95% van de observaties binnen de predictie-intervallen. Dat is niet zo voor de betrouwbaarheidsintervallen, die immers geen informatie geven over de verwachte locatie van een nieuwe observatie, maar wel over waar men het conditioneel gemiddelde verwacht op basis van de steekproef!

``` {.sourceCode .r}
plot(log2S100A8~log2ESR1,borstkanker,ylab="S100A8 (log2)",xlab="ESR1 (log2)",ylim=range(p))
lines(grid,p[,1])
lines(grid,g[,2],lty=2)
lines(grid,g[,3],lty=2)
lines(grid,p[,2],lty=3,col=2)
lines(grid,p[,3],lty=3,col=2)
legend("topright",lty=1:3,legend=c("Lineair model","95% puntsgewijze BI","95% puntsgewijs PI"),col=c(1,1,2))
```

<span id="fig:brcaLogLinPred3"></span> <img src="Statistiek_2019_2020_files/figure-html/brcaLogLinPred3-1.png" style="width:100.0%" alt="Scatterplot voor log2-S100A8 expressie in functie van de log2-ESR1 expressie met model voorspellingen en 95$\%$ betrouwbaarheidsintervallen en 95$\%$ predictie-intervallen." />

Figuur 6.11: Scatterplot voor log2-S100A8 expressie in functie van de log2-ESR1 expressie met model voorspellingen en 95<span class="math inline">\$\\%\$</span> betrouwbaarheidsintervallen en 95<span class="math inline">\$\\%\$</span> predictie-intervallen.

**NHANES voorbeeld** Aangezien een predictie-interval een verbeterde versie is van een referentie-interval bij ongekend populatie gemiddelde en de standaardafwijking, kunnen we a.d.h.v. de `lm(.)` functie het referentie-interval voor de normale bloeddruk in Sectie [4.4.1](../chap-describe/index.md) vervangen door een predictie-interval. Het PI zal eveneens de onzekerheid meenemen op de parameterschattingen (gemiddelde en standard error). Het referentie-interval in Sectie [4.4.1](../chap-describe/index.md) bedroeg $$91.9, 147$$mmHg.

Een predictie-interval kan als volgt worden bekomen in de R software.

``` {.sourceCode .r}
lmBpNorm <- lm(bpSys~1,data=nhanesSubHealthy)
predInt <- predict(lmBpNorm,interval="prediction",newdata=data.frame(geenpredictor=1))
round(predInt,1)
```

    ##     fit  lwr   upr
    ## 1 119.5 91.7 147.2

De formule `bpSys~1` drukt uit dat we enkel een intercept hebben in het model. We modelleren de bloeddruk dus als <span class="math display">\\$$Y\_i=\\beta\_0 + \\epsilon\_i,\\$$</span> waarbij de parameter <span class="math inline">\$\\beta\_0\$</span> de interpretatie heeft van de gemiddelde bloeddruk. Merk op dat het predictie-interval voor de bloeddruk van “gezonde personen tussen 40 en 65 jaar” in de NHANES studie maar een klein beetje breder is dan het referentie-interval. De subset van “gezonde personen tussen 40 en 65 jaar” in de NHANES studie bevat immers 275 subjecten. Hierdoor kan het gemiddelde heel nauwkeurig worden geschat en heeft de t-verdeling voor de constructie van het predictie-interval 274 vrijheidsgraden waardoor het 2.5% kwantiel van de t-verdeling, <span class="math inline">\$t\_{0.025,n-1}=\$</span> 1.97, bijna overeenkomt met het 2.5% kwantiel van de normaal verdeling <span class="math inline">\$z\_{0.025}=\$</span> 1.96.

## <span class="header-section-number">6.9</span> Kwadratensommen en Anova-tabel {#kwadratensommen-en-anova-tabel}

In deze sectie bespreken we de constructie van kwadratensommen die typisch in een tabel worden gegeven en die behoren tot de klassieke presentatiewijze van een regressie-analyse. De tabel wordt de variantie-analyse tabel of anova tabel genoemd.

De **totale kwadratensom** is gelijk aan <span class="math display">\\$$\\text{SSTot} = \\sum\_{i=1}^n (Y\_i-\\bar{Y})^2.\\$$</span>

Het is de som van de kwadratische afwijkingen van de observaties rond het steekproefgemiddelde <span class="math inline">\$\\bar Y\$</span>. Deze kwadratensom kan worden gebruikt om de variantie te schatten van de **marginale distributie** van de uitkomsten.

- In dit hoofdstuk wordt de focus hoofdzakelijk gelegd op de **conditionele distributie** van <span class="math inline">\$Y\\vert X=x\$</span>.
- We weten reeds dat MSE een schatter is van de variantie van de conditionele distributie van <span class="math inline">\$Y\\vert X=x\$</span>.
- De **marginale distributie** van <span class="math inline">\$Y\$</span> is de verdeling van <span class="math inline">\$Y\$</span> wanneer we geen rekening houden met de waarde voor de predictor <span class="math inline">\$X\$</span>. Het heeft als gemiddelde <span class="math inline">\$E$$Y$$\$</span> wat geschat wordt door het steekproefgemiddelde <span class="math inline">\$\\bar{Y}\$</span> en een variantie <span class="math inline">\$\\text{var}$$Y$$\$</span> die geschat kan worden aan de hand van <span class="math inline">\$\\frac{\\text{SSTot}}{n-1}\$</span>, de steekproefvariantie van <span class="math inline">\$Y\$</span> (zie Sectie [4.3.2](../chap-describe/index.md)).

Een grafische interpretatie van SSTot wordt weergegeven in Figuur [6.13](index.md).

``` {.sourceCode .r}
plot(log2S100A8~log2ESR1,data=borstkanker,xlab="ESR1 expressie (log2)",ylab="S100A8 expressie (log2)",cex.axis=1.5,cex.main=1.5,cex.lab=1.5,col=4)
abline(h=mean(borstkanker$log2S100A8))
for (i in 1:length(borstkanker$log2S100A8)) lines(rep(borstkanker$log2ESR1[i],2),c(mean(borstkanker$log2S100A8),borstkanker$log2S100A8[i]),lty=2,col=4)
```

<span id="fig:brcaLogSSTot"></span> <img src="Statistiek_2019_2020_files/figure-html/brcaLogSSTot-1.png" style="width:100.0%" alt="Interpretatie van de totale kwadratensom (SSTot): de som van de kwadratische afwijkingen rond het steekproefgemiddelde." />

Figuur 6.12: Interpretatie van de totale kwadratensom (SSTot): de som van de kwadratische afwijkingen rond het steekproefgemiddelde.

Daarnaast kunnen we eveneens een tweede kwadratensom definiëren: de **kwadratensom van de regressie, SSR,** die een maat is voor de variabiliteit die verklaard kan worden door de regressie. Het is de som van de kwadratische afwijkingen van de voorspelde response <span class="math inline">\$\\hat{Y}\_i\$</span><a href="#fn41" id="fnref41" class="footnoteRef"><sup>41</sup></a> rond het steekproefgemiddelde <span class="math inline">\$\\bar Y\$</span>.

De kwadratensom van de regressie is gelijk aan <span class="math display">\\$$\\text{SSR} = \\sum\_{i=1}^n (\\hat{Y}\_i - \\bar{Y})^2 = \\sum\_{i=1}^n (\\hat{g}(x\_i) - \\bar{Y})^2.\\$$</span>

SSR is een maat voor de afwijking tussen de predicties op de geschatte regressierechte en het steekproefgemiddelde van de uitkomsten. Het kan ook geïnterpreteerd worden als een maat voor de afwijking tussen de geschatte regressierechte <span class="math inline">\$\\hat{g}(x)=\\hat\\beta\_0+\\hat\\beta\_1x\$</span> en een “geschatte regressierechte” waarbij de regressor geen effect heeft op de gemiddelde uitkomst. Deze laatste is dus eigenlijk een schatting van de regressierechte <span class="math inline">\$g(x)=\\beta\_0\$</span>, waarin <span class="math inline">\$\\beta\_0\$</span> geschat wordt door <span class="math inline">\$\\bar{Y}\$</span>. Anders geformuleerd: SSR meet de grootte van het regressie-effect zodat <span class="math inline">\$\\text{SSR} \\approx 0\$</span> duidt op geen effect van de regressor en <span class="math inline">\$\\text{SSR}&gt;0\$</span> duidt op een effect van de regressor. We voelen reeds aan dat <span class="math inline">\$\\text{SSR}\$</span> zal kunnen worden gebruikt voor het ontwikkelen van een statistische test die de associatie tussen <span class="math inline">\$X\$</span> en <span class="math inline">\$Y\$</span> evalueert.

Een grafische interpretatie van SSR wordt weergegeven in Figuur [6.13](index.md).

``` {.sourceCode .r}
plot(log2S100A8~log2ESR1,borstkanker,xlab="ESR1 expressie (log2)",ylab="S100A8 expressie (log2)",cex.axis=1.5,cex.main=1.5,cex.lab=1.5)
abline(h=mean(borstkanker$log2S100A8))
abline(lm2,col=2)
points(borstkanker$log2ESR1,lm2$fitted,pch=2,col=2)
for (i in 1:length(borstkanker$log2S100A8)) lines(rep(borstkanker$log2ESR1[i],2),c(mean(borstkanker$log2S100A8),lm2$fitted[i]),lty=2,col=2)
```

<span id="fig:brcaLogSSR"></span> <img src="Statistiek_2019_2020_files/figure-html/brcaLogSSR-1.png" style="width:100.0%" alt="Interpretatie van de kwadratensom van de regressie (SSR): de som van de kwadratische afwijkingen tussen de geschatte regressierechte en het steekproefgemiddelde van de uitkomsten." />

Figuur 6.13: Interpretatie van de kwadratensom van de regressie (SSR): de som van de kwadratische afwijkingen tussen de geschatte regressierechte en het steekproefgemiddelde van de uitkomsten.

Tenslotte herhalen we de **kwadratensom van de fout**: <span class="math display">\\$$ \\text{SSE} = \\sum\_{i=1}^n (Y\_i-\\hat{Y}\_i )^2 = \\sum\_{i=1}^n \\left\\{Y\_i-\\hat{g}\\left(x\_i\\right)\\right\\}^2.\\$$</span> Van SSE weten we reeds dat het een maat is voor de afwijking tussen de observaties en de predicties bij de geobserveerde <span class="math inline">\$x\_i\$</span> uit de steekproef. Hoe kleiner SSE, hoe beter de fit (schatting) van de regressierechte voor predictiedoeleinden. We hebben deze immers geminimaliseerd om tot de kleinste kwadratenschatters te komen.

Een interpretatie van SSE voor het log-log model wordt weergegeven in Figuur [6.14](index.md).

``` {.sourceCode .r}
plot(log2S100A8~log2ESR1,borstkanker,xlab="ESR1 expressie (log2)",ylab="S100A8 expressie (log2)",cex.axis=1.5,cex.main=1.5,cex.lab=1.5)
abline(lm2,col=2)
points(borstkanker$log2ESR1,lm2$fitted,pch=2,col=2)
for (i in 1:length(borstkanker$log2S100A8)) lines(rep(borstkanker$log2ESR1[i],2),c(borstkanker$log2S100A8[i],lm2$fitted[i]),lty=2)
```

<span id="fig:brcaLogSSE"></span> <img src="Statistiek_2019_2020_files/figure-html/brcaLogSSE-1.png" style="width:100.0%" alt="Interpretatie van de kwadratensom van de error (SSE): de som van de kwadratische afwijkingen tussen uitkomsten en de predicties op de geschatte regressierechte." />

Figuur 6.14: Interpretatie van de kwadratensom van de error (SSE): de som van de kwadratische afwijkingen tussen uitkomsten en de predicties op de geschatte regressierechte.

Verder kan worden aangetoond dat de totale kwadratensom als volgt kan ontbonden worden <span class="math display">\\$$\\begin{eqnarray\*} \\text{SSTot} &=& \\sum\_{i=1}^n (Y\_i-\\bar{Y})^2 \\\\ &=& \\sum\_{i=1}^n (Y\_i-\\hat{Y}\_i+\\hat{Y}\_i-\\bar{Y})^2 \\\\ &=& \\sum\_{i=1}^n (Y\_i-\\hat{Y}\_i)^2+\\sum\_{i=1}^n(\\hat{Y}\_i-\\bar{Y})^2 \\\\ &=& \\text{SSE }+\\text{SSR} \\end{eqnarray\*}\\$$</span>

Merk op dat de dubbel product term wegvalt. Er kan aangetoond worden dat de ze gelijk is aan nul. Dat valt buiten het bestek van de ze cursus. De ontbinding van de totale kwadratensom kan als volgt worden geïnterpreteerd: De totale variabiliteit in de data (SSTot) wordt gedeeltelijk verklaard door het regressieverband (SSR). De variabiliteit die niet door het regressieverband verklaard wordt, is de residuele variabiliteit (SSE).

### <span class="header-section-number">6.9.1</span> Determinatie-coëfficiënt {#determinatie-coëfficiënt}

De **determinatiecoëfficiënt** wordt gedefinieerd door <span class="math display">\\$$ R^2 = 1-\\frac{\\text{SSE}}{\\text{SSTot}}=\\frac{\\text{SSR}}{\\text{SSTot}}.\\$$</span> Het is dus *de fractie van de totale variabiliteit in de steekproef-uitkomsten die verklaard wordt door het geschatte regressieverband*.

Een grote <span class="math inline">\$R^2\$</span> is meestal een indicatie dat het model potentieel tot goede predicties kan leiden (kleine SSE), maar de waarde van <span class="math inline">\$R^2\$</span> is slechts in beperkte mate indicatief voor de p-waarde van de test <span class="math inline">\$H\_0:\\beta\_1=0\$</span> vs <span class="math inline">\$H\_1:\\beta\_1\\neq0\$</span>.

- De p-waarde wordt immers sterk beïnvloed door SSE, maar niet door SSTot. Ook de steekproefgrootte n heeft een grote invloed op de p-waarde.
- De determinatiecoëfficiënt <span class="math inline">\$R^2\$</span> wordt door SSE en SSTot bepaald, maar niet door de steekproefgrootte n.

<span class="math inline">\$R^2\$</span> vormt een maat voor de *predictieve waarde* van de verklarende variabele. Dat wil zeggen dat ze uitdrukt hoe goed de verklarende variabele de uitkomst voorspelt. <span class="math inline">\$R^2\$</span> is steeds gelegen tussen 0 en 1. Een waarde gelijk aan 1 geeft aan dat er geen residuele variatie is rond de regressielijn en dat de uitkomst dus een perfect lineaire relatie met de predictor vertoont. Analoog impliceert een <span class="math inline">\$R^2\$</span> waarde van 0 dat er geen associatie is tussen de uitkomst en de predictor.

Vaak wordt er verkeerdelijk beweerd dat een lineair regressiemodel slecht is wanneer de determinatiecoëfficiënt klein is (bvb. <span class="math inline">\$R^2=0.2\$</span>). Wanneer het doel van de studie erin bestaat om de uitkomst te voorspellen o.b.v. verklarende variabele, dan is een hoge <span class="math inline">\$R^2\$</span> inderdaad vereist omdat er bij een lage waarde veel variabiliteit op de uitkomsten overblijft, die niet wordt opgevangen door de verklarende variabele. Wanneer het doel van de studie er echter in bestaat om het effect van een blootstelling op de uitkomst te bepalen, dan is een lineair regressiemodel goed zodra het correct de associatie beschrijft tussen de uitkomst enerzijds en de blootstelling anderzijds. Wanneer blootstelling zwak geassocieerd zijn met de uitkomst, dan wordt een kleine <span class="math inline">\$R^2\$</span>-waarde verwacht, zelfs wanneer een correct regressiemodel wordt gebruikt.

``` {.sourceCode .r}
summary(lm2)
```

    ##
    ## Call:
    ## lm(formula = log2S100A8 ~ log2ESR1, data = borstkanker)
    ##
    ## Residuals:
    ##      Min       1Q   Median       3Q      Max
    ## -1.94279 -0.66537  0.08124  0.68468  1.92714
    ##
    ## Coefficients:
    ##             Estimate Std. Error t value Pr(>|t|)
    ## (Intercept)   23.401      1.603   14.60 3.57e-15 ***
    ## log2ESR1      -1.615      0.150  -10.76 8.07e-12 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ##
    ## Residual standard error: 1.026 on 30 degrees of freedom
    ## Multiple R-squared:  0.7942, Adjusted R-squared:  0.7874
    ## F-statistic: 115.8 on 1 and 30 DF,  p-value: 8.07e-12

In de output voor het borstkankervoorbeeld zien we een <span class="math inline">\$R^2\$</span>=0.79 en kunnen we besluiten dat 79% van de variabiliteit in de <span class="math inline">\$\\log\_2\$</span>-S100A8 expressie kan worden verklaard door de <span class="math inline">\$\\log\_2\$</span>-ESR1 expressie-waarden.

### <span class="header-section-number">6.9.2</span> F-Testen in het enkelvoudig lineair regressiemodel

De kwadratensommen vormen de basis van een belangrijke klasse van hypothesetesten. De <span class="math inline">\$F\$</span>-teststatistiek wordt gedefinieerd als <span class="math display">\\$$ F = \\frac{\\text{MSR}}{\\text{MSE}}\\$$</span>

met
<span class="math display">\\$$\\text{MSR} = \\frac{\\text{SSR}}{1} \\text{ en } \\text{MSE} = \\frac{\\text{SSE}}{n-2}.\\$$</span>

MSR wordt de gemiddelde kwadratensom van de regressie genoemd. De noemers 1 en <span class="math inline">\$n-2\$</span> zijn de vrijheidsgraden van SSR en SSE. Ze kan worden gebruikt om de nulhypothese <span class="math inline">\$H\_0: \\beta\_1=0\$</span>, dat er geen associatie is tussen de uitkomst (response) en de blootstelling (predictor) te evalueren t.o.v de alternatieve hypothese <span class="math inline">\$H\_1: \\beta\_1\\neq0\$</span>.

Onder <span class="math inline">\$H\_0: \\beta\_1=0\$</span> volgt de teststatistiek <span class="math display">\\$$H\_0:F = \\frac{\\text{MSR}}{\\text{MSE}} \\sim F\_{1,n-2},\\$$</span> een F-verdeling met 1 vrijheidsgraad in de teller en n-2 vrijheidsgraden in de noemer.

De teststatistiek kan enkel gebruikt worden voor het testen tegenover <span class="math inline">\$H\_1:\\beta\_1\\neq 0\$</span> (tweezijdig alternatief), waarvoor de <span class="math inline">\$p\$</span>-waarde gegeven wordt door

<span class="math display">\\$$ p = P\_0\\left\[F\\geq f\\right$$=1-F\_F(f;1,n-2),\\\]</span>

de kans onder de nulhypothese<a href="#fn42" id="fnref42" class="footnoteRef"><sup>42</sup></a> om een test statistiek F te bekomen die ten minste zo extreem is<a href="#fn43" id="fnref43" class="footnoteRef"><sup>43</sup></a> als de waarde f die werd geobserveerd in de steekproef, <span class="math inline">\$F\_F(.;1,n-2)\$</span> de cumulatieve distributie is van een F-verdeling met 1 vrijheidsgraad in de teller en n-2 vrijheidsgraden in de noemer. De kritieke waarde op het <span class="math inline">\$\\alpha\$</span> significantieniveau is <span class="math inline">\$F\_{1,n-2;1-\\alpha}\$</span>.

### <span class="header-section-number">6.9.3</span> Anova Tabel

De kwadratensommen en de F-test worden meestal in een zogenaamde variantie-analyse tabel of een anova tabel gerapporteerd.

|           | Df                  | Sum Sq | Mean Sq | F value      | Pr(&gt;F) |
|-----------|---------------------|--------|---------|--------------|-----------|
| Regressie | vrijheidsgraden SSR | SSR    | MSR     | f-statistiek | p-waarde  |
| Error     | vrijheidsgraden SSE | SSE    | MSE     |              |           |

De anovatabel voor het borstkanker voorbeeld kan als volgt in de R-software worden bekomen

``` {.sourceCode .r}
anova(lm2)
```

    ## Analysis of Variance Table
    ##
    ## Response: log2S100A8
    ##           Df  Sum Sq Mean Sq F value   Pr(>F)
    ## log2ESR1   1 121.814 121.814   115.8 8.07e-12 ***
    ## Residuals 30  31.559   1.052
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

We besluiten dus dat er een extreem significant lineair verband is tussen de <span class="math inline">\$\\log\_2\$</span> ESR1 expressie en de <span class="math inline">\$\\log\_2\$</span> S100A8 expressie. De <span class="math inline">\$F\$</span>-test is tweezijdig. Door te kijken naar het teken van <span class="math inline">\$\\hat\\beta\_1\$</span> (<span class="math inline">\$\\hat\\beta\_1=-1.615\$</span>) kunnen we tevens besluiten dat er een negatieve associatie is tussen beiden. Merk op dat de <span class="math inline">\$p\$</span>-waarde van de <span class="math inline">\$F\$</span>-test en de <span class="math inline">\$p\$</span>-waarde van de tweezijdige <span class="math inline">\$t\$</span>-test exact gelijk zijn. Voor het enkelvoudig lineair regressie-model zijn beide testen equivalent!

## <span class="header-section-number">6.10</span> Dummy variabelen {#dummy-variabelen}

Het lineaire regressiemodel kan ook gebruikt worden voor het vergelijken van twee gemiddelden. In het Borstkanker voorbeeld kunnen we bijvoorbeeld nagaan of er een verschil is in de gemiddelde leeftijd van de patiënten met onaangetaste lymfeknopen en patiënten waarvan de lymfeknopen werden verwijderd.

Hiervoor definiëren we eerst een <span class="math inline">\$dummy\$</span> variabele <span class="math display">\\$$x\_i = \\left\\{ \\begin{array}{ll} 1 & \\text{aangetaste lymfeknopen} \\\\ 0 & \\text{onaangetaste lymfeknopen} \\end{array}\\right.\\$$</span>

De groep met <span class="math inline">\$x\_i=0\$</span> wordt de **referentiegroep** genoemd. Het regressiemodel blijft ongewijzigd, <span class="math display">\\$$Y\_i = \\beta\_0 + \\beta\_1 x\_i +\\epsilon\_i\\$$</span> met <span class="math inline">\$\\epsilon\_i \\text{ iid } N(0,\\sigma^2)\$</span><a href="#fn44" id="fnref44" class="footnoteRef"><sup>44</sup></a>.

Gezien <span class="math inline">\$x\_i\$</span> slechts twee waarden kan aannemen, is het eenvoudig om het regressiemodel voor beide waarden van <span class="math inline">\$x\_i\$</span> afzonderlijk te bekijken: <span class="math display">\\$$ \\begin{array}{lcll} Y\_i &=& \\beta\_0 +\\epsilon\_i &\\text{onaangetaste lymfeknopen} (x\_i=0) \\\\ Y\_i &=& \\beta\_0 + \\beta\_1 +\\epsilon\_i &\\text{ aangetaste lymfeknopen} (x\_i=1) . \\end{array}\\$$</span>

Dus <span class="math display">\\$$\\begin{eqnarray\*} E\\left\[Y\_i\\mid x\_i=0\\right$$ &=& \\beta\_0 \\\\ E\\left$$Y\_i\\mid x\_i=1\\right$$ &=& \\beta\_0 + \\beta\_1, \\end{eqnarray\*}\\\]</span>

waaruit direct de interpretatie van <span class="math inline">\$\\beta\_1\$</span> volgt: <span class="math display">\\$$ \\beta\_1 = E\\left\[Y\_i\\mid x\_i=1\\right$$-E\\left$$Y\_i\\mid x\_i=0\\right$$\\\]</span>

<span class="math inline">\$\\beta\_1\$</span> is dus het gemiddelde verschil in leeftijd tussen patiënten met aangetaste lymfeknopen en patiënten met onaangetaste lymfeknopen (referentiegroep).

Met de notatie <span class="math inline">\$\\mu\_1= E\\left$$Y\_i\\mid x\_i=0\\right$$\$</span> en <span class="math inline">\$\\mu\_2= E\\left$$Y\_i\\mid x\_i=1\\right$$\$</span> wordt dit <span class="math display">\\$$\\beta\_1 = \\mu\_2-\\mu\_1.\\$$</span><a href="#fn45" id="fnref45" class="footnoteRef"><sup>45</sup></a>

Er kan aangetoond worden dat <span class="math display">\\$$\\begin{array}{ccll} \\hat\\beta\_0 &=& \\bar{Y}\_1&\\text{ (steekproefgemiddelde in referentiegroep)} \\\\ \\hat\\beta\_1 &=& \\bar{Y}\_2-\\bar{Y}\_1&\\text{(schatter van effectgrootte)} \\\\ \\text{MSE} &=& S\_p^2 . \\end{array}\\$$</span>

De testen voor <span class="math inline">\$H\_0:\\beta\_1=0\$</span> vs. <span class="math inline">\$H\_1:\\beta\_1\\neq0\$</span> kunnen gebruikt worden voor het testen van de nulhypothese van de two-sample <span class="math inline">\$t\$</span>-test, <span class="math inline">\$H\_0:\\mu\_1=\\mu\_2\$</span> t.o.v. <span class="math inline">\$H\_1:\\mu\_1\\neq\\mu\_2\$</span>.

``` {.sourceCode .r}
borstkanker$node=as.factor(borstkanker$node)
lm3 <- lm(age~node,borstkanker)
t.test(age~node,borstkanker,var.equal=TRUE)
```

    ##
    ##  Two Sample t-test
    ##
    ## data:  age by node
    ## t = -2.7988, df = 30, p-value = 0.008879
    ## alternative hypothesis: true difference in means is not equal to 0
    ## 95 percent confidence interval:
    ##  -15.791307  -2.467802
    ## sample estimates:
    ## mean in group 0 mean in group 1
    ##        59.94737        69.07692

``` {.sourceCode .r}
summary(lm3)
```

    ##
    ## Call:
    ## lm(formula = age ~ node, data = borstkanker)
    ##
    ## Residuals:
    ##      Min       1Q   Median       3Q      Max
    ## -19.9474  -5.3269   0.0526   5.3026  18.0526
    ##
    ## Coefficients:
    ##             Estimate Std. Error t value Pr(>|t|)
    ## (Intercept)   59.947      2.079  28.834  < 2e-16 ***
    ## node1          9.130      3.262   2.799  0.00888 **
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ##
    ## Residual standard error: 9.063 on 30 degrees of freedom
    ## Multiple R-squared:  0.207,  Adjusted R-squared:  0.1806
    ## F-statistic: 7.833 on 1 and 30 DF,  p-value: 0.008879

``` {.sourceCode .r}
par(mfrow=c(2,2))
plot(lm3)
```

<span id="fig:brcaLymf"></span> <img src="Statistiek_2019_2020_files/figure-html/brcaLymf-1.png" style="width:100.0%" alt="Diagnostische plot voor het model waarbij leeftijd wordt gemodelleerd a.d.h.v. een dummy variabele voor factor lymfe knoop status." />

Figuur 6.15: Diagnostische plot voor het model waarbij leeftijd wordt gemodelleerd a.d.h.v. een dummy variabele voor factor lymfe knoop status.

We zien in de R output dat de output van de t-test en het lineaire model met 1 dummy variabele identieke resultaten geeft voor de test statistiek en de p-waarde. We zien eveneens een heel significante associatie tussen de leeftijd en de lymfe node status (p=0.009). De leeftijd van personen met aangetaste lymfeknopen is gemiddeld 9.1 jaar hoger dan die van patiënten zonder aantasting van de lymfeknopen.

**Let op**: We kunnen echter niet besluiten dat oudere personen een hoger risico hebben op aantasting van de lymfeknopen ten gevolge van hun leeftijd. Aangezien de studie een observationele studie is, kunnen de groepen patiënten met aangetaste lymfeknopen en niet-aangetaste lymfeknopen nog in andere karateristieken van elkaar verschillen. We kunnen dus enkel besluiten dat er een associatie is tussen de lymfeknoop status en de leeftijd. Het is dus niet noodzakelijkerwijs een causaal verband! Het is immers steeds **moeilijk om causale verbanden** te trekken op basis van **observationele studies** gezien **confounding** kan optreden. We hebben de patiënten immers niet kunnen randomiseren over de twee groepen, de lymfeknoopstatus werd niet geïnduceerd door de onderzoekers maar enkel geobserveerd en we kunnen daarom niet garanderen dat de patiënten enkel verschillen in de lymfeknoopstatus!

Hetzelfde geldt voor het lineair model voor de <span class="math inline">\$\\log\_2\$</span>-S100A8-expressie. Aangezien we de ESR1-expressie niet experimenteel vast hebben kunnen leggen, kunnen we niet besluiten dat een hogere ESR1-expressie de S100A8-expressie doet verlagen. We hebben beide genexpressies enkel geobserveerd dus kunnen we alleen besluiten dat ze negatief geassocieerd zijn met elkaar. Om te evalueren of de expressie van een bepaald gen de expressie van ander genen beïnvloedt, gaat men vaak knockout constructen generenen in het labo, dat zijn mutanten die een bepaald gen niet tot expressie kunnen brengen. Wanneer de wild type (normale genotype) en de knockout dan onder identieke condities worden opgegroeid in het lab, weten onderzoekers dat verschillen in genexpressie worden geïnduceerd door de afwezigheid van de expressie van het knockout gen. Experimentele studies zijn immers essentieel om causale verbanden te kunnen trekken.

**Veronderstellingen:** We moeten echter ook nog de veronderstellingen van het model voor de leeftijd nagaan! In Figuur [6.15](index.md) zien we geen afwijkingen van normaliteit in de QQ-plot. Er lijkt echter wel een aanwijzing dat de variantie in beide groepen verschillend is. De residuen lijken meer gespreid in de groep met lagere gemiddelde leeftijd (node=0) dan in de groep met een hogere gemiddelde leeftijd (node=1).
Merk echter ook op dat er een verschil is in het aantal observaties in beide groepen. Wanneer we een boxplot maken, zoals we ook deden in het hoofdstuk [5](../chap-besluit/index.md) om gelijkheid van variantie na te gaan bij het uitvoeren van een t-test, zien we dat het verschil in interkwartiel afstand (IRQ, boxgrootes) niet zo groot is (Figuur [6.16](index.md)). Als we data simuleren die <span class="math inline">\$iid\$</span> normaal verdeeld zijn en deze at random opslitsen in twee groepen die gelijk zijn in grootte als die voor de lymfeknoop status (19 vs 13 patiënten) zien we dat een dergelijk verschil in IQR gerust kan voorkomen door toeval (Figuur [6.17](index.md)). We kunnen dus besluiten dat aan alle aannames is voldaan voor de statistische besluitvorming en dat we de R-output van het statistisch model voor de response age i.f.v de dummy variabele voor de node-status mogen gebruiken om conclusies te formuleren over de associatie tussen leeftijd en node status (zie hoger).

``` {.sourceCode .r}
plot(age~node,borstkanker)
```

<span id="fig:boxNode"></span> <img src="Statistiek_2019_2020_files/figure-html/boxNode-1.png" style="width:100.0%" alt="boxplot van de leeftijd vs lymfeknoop status in de borstkanker dataset." />

Figuur 6.16: boxplot van de leeftijd vs lymfeknoop status in de borstkanker dataset.

``` {.sourceCode .r}
par(mfrow=c(3,3))
set.seed(354)
for(i in 1:9) plot(rnorm(32)~node,borstkanker,ylab="iid N(0,1)")
```

<span id="fig:boxSim"></span> <img src="Statistiek_2019_2020_files/figure-html/boxSim-1.png" style="width:100.0%" alt="Simulatie van normaal verdeelde gegevens met gelijk gemiddelde en variantie. Zoals in de borstkanker dataset zijn er 19 observaties in ene groep en 13 observaties in de andere groep. We zien dat er door puur toeval een behoorlijk verschil kan optreden in de IQR tussen beide groepen in de steekproef." />

Figuur 6.17: Simulatie van normaal verdeelde gegevens met gelijk gemiddelde en variantie. Zoals in de borstkanker dataset zijn er 19 observaties in ene groep en 13 observaties in de andere groep. We zien dat er door puur toeval een behoorlijk verschil kan optreden in de IQR tussen beide groepen in de steekproef.

Zoals we illustreerden is het steeds nuttig om simulaties te gebruiken om in te leren schatten wanneer de diagnostische plots duiden op een afwijking van de voorwaarden.

### References {#references}

Sotiriou, Christos, Pratyaksha Wirapati, Sherene Loi, Adrian Harris, Steve Fox, Johanna Smeds, Hans Nordgren, et al. 2006. “Gene Expression Profiling in Breast Cancer: Understanding the Molecular Basis of Histologic Grade to Improve Prognosis.” *Journal of the National Cancer Institute* 98 (4). Functional Genomics; Translational Research Unit, Universite Libre de Bruxelles, Brussels, Belgium. christos.sotiriou@bordet.be: 262–72. doi:[10.1093/jnci/djj052](https://doi.org/10.1093/jnci/djj052).

------------------------------------------------------------------------

1.  In de cursus zullen we naar Y refereren met de term afhankelijke variable, response variabele of uitkomst, wat 3 synoniemen zijn[↩](index.md)

2.  Analoog aan het conditionele gemiddelde <span class="math inline">\$E(Y\|X=x)\$</span>, geeft <span class="math inline">\$\\text{var}(Y\\vert X=x) = \\sigma^2\$</span> de variantie weer op de uitkomsten voor de subgroep van de studiepopulatie bestaande uit subjecten met een ESR1 gen expressie gelijk aan <span class="math inline">\$x\$</span>.[↩](index.md)

3.  die zoals reeds geargumenteerd numeriek gelijk zijn aan de gemiddelde uitkomst[↩](index.md)

4.  in de predictorpunten <span class="math inline">\$X\_i\$</span> die werden geobserveerd in de steekproef[↩](index.md)

5.  Vandaar <span class="math inline">\$P\_0\$</span> waarbij subscript 0 aangeeft dat het een kans is onder <span class="math inline">\$H\_0\$</span>[↩](index.md)

6.  Hier groter of gelijk aan[↩](index.md)

7.  Merk op dat iid staat voor independent and identically distributed of onafhankelijk en gelijk verdeeld[↩](index.md)

8.  Noot: de indexen 1 en 2 mogen gerust vervangen worden door 0 en 1 om explicieter naar <span class="math inline">\$x\_i=0\$</span> en <span class="math inline">\$x\_1=1\$</span> te verwijzen; dan wordt <span class="math inline">\$\\beta\_1=\\mu\_1-\\mu\_0\$</span>[↩](index.md)

---

[← Het argument header=TRUE wordt gebruikt omdat de eerste](04-het-argument-header-true-wordt-gebruikt-omdat-de-eerste.md) · [Up: contents](index.md)

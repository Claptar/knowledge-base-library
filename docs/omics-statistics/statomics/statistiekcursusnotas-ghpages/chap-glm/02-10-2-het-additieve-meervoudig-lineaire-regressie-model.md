---
title: 10.2 Het additieve meervoudig lineaire regressie model
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-glm.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-glm.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 10.2 Het additieve meervoudig lineaire regressie model

**Source:** [`chap-glm.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-glm.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

Afzonderlijke lineaire regressiemodellen, zoals

<span class="math display">\\$$E(Y\|X\_v)=\\alpha+\\beta\_v X\_v\\$$</span>

laten enkel toe om de associatie tussen de prostaat specifieke antigeen concentratie te evalueren op basis van 1 variabele, bijvoorbeeld het log-tumorvolume. Het spreekt voor zich dat meer accurate predicties kunnen bekomen worden door meerdere predictoren simultaan in rekening te brengen. Bovendien geeft de parameter <span class="math inline">\$\\beta\_v\$</span> in dit model mogelijks geen zuiver effect van het tumorvolume weer. Inderdaad, <span class="math inline">\$\\beta\_v\$</span> is het gemiddeld verschil in log-psa voor patiënten die 1 eenheid in het log tumorvolume (lcavol) verschillen. Zelfs als lcavol niet is geassocieerd met het lpsa, dan nog kunnen patiënten met een groter tumorvolume een hoger lpsa hebben omdat ze bijvoorbeeld een aantasting van de zaadblaasjes hebben (svi status 1). Dit is een probleem van confounding (nl. het effect van lcavol wordt verward met het effect van svi) dat kan verholpen worden door patiënten te vergelijken met verschillend log-tumorvolume, maar met dezelfde status voor svi. We zullen in dit hoofdstuk aantonen dat meervoudige lineaire regressiemodellen dit op een natuurlijke wijze mogelijk maken.

### <span class="header-section-number">10.2.1</span> Statistisch model

De techniek die we hiertoe gaan gebruiken heet *meervoudige lineaire regressie*, in tegenstelling tot *enkelvoudige lineaire regressie* die we eerder gebruikt hebben. Stel dat we <span class="math inline">\$p-1\$</span> verklarende variabelen <span class="math inline">\$X\_1,...,X\_{p-1}\$</span> en een uitkomst <span class="math inline">\$Y\$</span> beschikbaar hebben voor <span class="math inline">\$n\$</span> subjecten. Stel bovendien dat de gemiddelde uitkomst lineair kan beschreven worden in functie van deze verklarende variabelen; d.w.z.

<span class="math display">\\$$\\begin{equation} Y\_i =\\beta\_0 + \\beta\_1 X\_{i1} + ... +\\beta\_{p-1} X\_{ip-1} + \\epsilon\_i \\end{equation}\\$$</span>

waarbij <span class="math inline">\$\\beta\_0,\\beta\_1,...,\\beta\_{p-1}\$</span> onbekende parameters zijn en <span class="math inline">\$\\epsilon\_i\$</span> de residuen die niet kunnen worden verklaard a.d.h.v. de predictoren. Het principe van de *kleinste kwadratenmethode* kan ook voor dit model worden gebruikt om schatters te bekomen voor de onbekende parameters <span class="math inline">\$\\beta\_0, \\ldots, \\beta\_{p-1}\$</span>. De formules voor deze schattingen zijn nu een stuk complexer dan voorheen, maar worden door de software automatisch uitgerekend. Voor gegeven schattingen <span class="math inline">\$\\hat{\\beta}\_0,\\hat{\\beta}\_1,...,\\hat{\\beta}\_{p-1}\$</span> laat het lineaire regressiemodel dan toe om:

1.  de verwachte uitkomst te voorspellen voor subjecten met gegeven waarden <span class="math inline">\$x\_1,...,x\_{p-1}\$</span> voor de verklarende variabelen. Dit kan geschat worden als <span class="math inline">\$E$$Y\\vert X\_1=x\_1, \\ldots X\_{p-1}=x\_{p-1}$$=\\hat{\\beta}\_0+\\hat{\\beta}\_1x\_1+...+\\hat{\\beta}\_{p-1}x\_{p-1}\$</span>.
2.  na te gaan in welke mate de gemiddelde uitkomst verschilt tussen 2 groepen subjecten met <span class="math inline">\$\\delta\$</span> eenheden verschil in een verklarende variabele <span class="math inline">\$X\_j\$</span> met <span class="math inline">\$j=1,\\ldots,p\$</span>, maar met dezelfde waarden voor alle andere variabelen <span class="math inline">\$\\{X\_k,k=1,...,p,k\\ne j\\}\$</span>. Namelijk: <span class="math display">\\$$ \\begin{array}{l} E(Y\|X\_1=x\_1,...,X\_j=x\_j+\\delta,...,X\_{p-1}=x\_{p-1}) - E(Y\|X\_1=x\_1,...,X\_j=x\_j,...,X\_{p-1}=x\_{p-1}) \\\\ \\quad =\\beta\_0 + \\beta\_1 x\_1 + ... + \\beta\_j(x\_j+\\delta)+...+\\beta\_{p-1} x\_{p-1} - \\beta\_0 - \\beta\_1 x\_1 - ... - \\beta\_jx\_j-...-\\beta\_{p-1} x\_{p-1} \\\\ \\quad= \\beta\_j\\delta \\end{array} \\$$</span>

In het bijzonder kan <span class="math inline">\$\\beta\_j\$</span> geïnterpreteerd worden als het verschil in gemiddelde uitkomst tussen subjecten die 1 eenheid verschillen in de waarde van <span class="math inline">\$X\_j\$</span>, maar dezelfde waarde hebben van de overige verklarende variabelen in het model. Dit kan geschat worden als <span class="math inline">\$\\hat{\\beta}\_j\$</span>.

Voor het prostaatkanker voorbeeld levert een analyse van het enkelvoudige lineaire regressiemodel <span class="math inline">\$E(Y\|X\_v)=\\beta\_0+\\beta\_v X\_v\$</span> in R de volgende output.

``` {.sourceCode .r}
lmV <- lm(lpsa~lcavol,prostate)
summary(lmV)
```

    ##
    ## Call:
    ## lm(formula = lpsa ~ lcavol, data = prostate)
    ##
    ## Residuals:
    ##      Min       1Q   Median       3Q      Max
    ## -1.67624 -0.41648  0.09859  0.50709  1.89672
    ##
    ## Coefficients:
    ##             Estimate Std. Error t value Pr(>|t|)
    ## (Intercept)  1.50730    0.12194   12.36   <2e-16 ***
    ## lcavol       0.71932    0.06819   10.55   <2e-16 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ##
    ## Residual standard error: 0.7875 on 95 degrees of freedom
    ## Multiple R-squared:  0.5394, Adjusted R-squared:  0.5346
    ## F-statistic: 111.3 on 1 and 95 DF,  p-value: < 2.2e-16

We besluiten op basis van deze gegevens dat patiënten met een tumorvolume dat 1% hoger ligt, gemiddeld gezien een prostaat antigeen concentratie zullen hebben die ongeveer 0.72% hoger zal liggen. Merk op dat we voor deze interpretatie beroep hebben gedaan op het feit dat beide variabelen log getransformeerd zijn.

Een analyse van het meervoudige lineaire regressiemodel met de predictoren lcavol (index v), lweight (index w) en svi (index s) <span class="math display">\\$$E(Y\|X\_f,X\_s,X\_p,X\_r)=\\beta\_0 +\\beta\_v X\_v+\\beta\_w X\_w+\\beta\_s X\_s,\\$$</span>

wijzigt dit resultaat vrij behoorlijk, zoals onderstaande output aangeeft.

``` {.sourceCode .r}
lmVWS <- lm(lpsa~lcavol + lweight + svi ,prostate)
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

De parameter bij lcavol geeft nu aan dat patiënten met een tumorvolume dat 1% hoger ligt, maar eenzelfde prostaat gewicht en svi status hebben, een prostaat antigeen concentratie zullen hebben dat gemiddeld slechts 0.55% hoger ligt. De reden dat we eerder een verschil van meer dan 0.7% vonden, kan worden verklaard doordat patiënten met een verschil in tumorvolume vaak ook verschillen in prostaat gewicht en svi status.

De parameter voor svi kunnen we als volgt interpreteren: de prostaat antigeen concentratie ligt gemiddeld een factor exp(0.666)=1.95 hoger voor patiënten met invasie van de zaadblaasjes dan voor patiënten zonder invasie van de zaadblaasjes na correctie voor het prostaat gewicht en het tumorvolume. De introductie van de factor svi in het additieve model zorgt ervoor dat we twee regressievlakken bekomen die evenwijdig zijn maar een verschillend intercept hebben (zie Figuur [10.2](index.md)).

De <span class="math inline">\$R^2\$</span>-waarde in bovenstaande analyse bedraagt 62.6% en geeft aan 62.6% in de variabiliteit van het log-PSA verklaard kan worden d.m.v. het tumorvolume, het prostaat gewicht en de status van de zaadblaasjes.

<span id="fig:prosAdditiveFit"></span> <img src="Statistiek_2019_2020_files/figure-html/prosAdditiveFit-1.png" style="width:100.0%" alt="Fit van het additieve model met termen lcavol, lweight en svi. De figuur geeft duidelijk weer dat de gemiddelde lpsa toeneemt i.f.v. het log-tumorvolume, het log-prostaatgewicht en de invasie van de zaadblaasjes. Merk op dat de fit resulteert in twee parallele vlakken, een regressievlak voor patiënten zonder (blauw) en met invasie van de zaadblaasjes (oranje)." />

Figuur 10.2: Fit van het additieve model met termen lcavol, lweight en svi. De figuur geeft duidelijk weer dat de gemiddelde lpsa toeneemt i.f.v. het log-tumorvolume, het log-prostaatgewicht en de invasie van de zaadblaasjes. Merk op dat de fit resulteert in twee parallele vlakken, een regressievlak voor patiënten zonder (blauw) en met invasie van de zaadblaasjes (oranje).

---

[← 10.1 Inleiding {#inleiding}](01-10-1-inleiding-inleiding.md) · [Up: contents](index.md) · [10.3 Besluitvorming in regressiemodellen →](03-10-3-besluitvorming-in-regressiemodellen.md)

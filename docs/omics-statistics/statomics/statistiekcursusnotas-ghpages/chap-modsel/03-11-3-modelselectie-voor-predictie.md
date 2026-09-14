---
title: 11.3 Modelselectie voor predictie
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-modsel.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-modsel.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 11.3 Modelselectie voor predictie

**Source:** [`chap-modsel.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-modsel.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">11.3.1</span> Inleiding {#inleiding-1}

In het vroege stadium van de ontwikkeling van een nieuw geneesmiddel (Engels: *early drug development*) kijkt men tegenwoordig ook naar het effect van de werkzame stof (*compound*) op genexpressie. Dit kan een dieper inzicht geven in de werking van het geneesmiddel, of kan toxiciteit van de compound in een vroeg stadium detecteren (toxicogenomics). De gewenste activiteit van een compound wordt in vitro bepaald aan de hand van bio-assays (BA). De uitkomst is bv. een maat voor de bindingscapaciteiten van de compound aan de geviseerde receptor op de celwand (IC<span class="math inline">\$\_{50}\$</span>). Deze receptor wordt de target genoemd.

In deze vroege fase van de ontwikkeling van een geneesmiddel worden typisch 20 tot 50 gelijkaardige compounds uitvoerig getest. Op basis van de in vitro resultaten nemen de chemici beslissingen over hoe de molecules moeten aangepast worden om tot een (hopelijk) betere compound te komen (i.e. een hogere on-target activiteit en minder toxiciteit).

De kleine variaties in moleculaire structuur geven aanleiding tot variaties in BA en genexpressies.

De doelstelling van de studie is het opstellen van een model dat toelaat de bioactiviteit (BA) te voorspellen aan de hand van genexpressies in een levercellijn.

In het volgend voorbeeld, wordt het effect van 35 compounds getest op de genexpressie van levercellen. De levercellen werden gedurende 24 uur blootgesteld aan de compound, waarna genexpressie gemeten werd m.b.v. microarrays. De on-target bioactiviteit van ieder van de 35 compounds wordt via een in-vitro bioassay bekomen (IC<span class="math inline">\$\_{50}\$</span>).

We beperken ons hier tot 10 genen (geselecteerd door het onderzoeksteam op basis van a-priori kennis van de pathways betrokken bij de ontwikkeling van de ziekte). Figuur [11.1](index.md) toont de scatter plot matrix.

``` {.sourceCode .r}
mcx<-read.table("dataset/mcx.txt",header=TRUE)
head(mcx)
```

    ##     BA    HOXB5    PNISR     ATRX LOC100505650   PLK1S1  DNAJC12    ZFHX4
    ## 1 5.70 9.864744 9.421823 8.557665     11.08555 8.892243 8.198292 8.846125
    ## 2 5.87 9.847176 9.301424 8.550591     11.18236 9.196701 8.343191 8.873578
    ## 3 5.70 9.859438 9.360302 8.536606     11.03822 8.903690 8.231318 8.859549
    ## 4 5.54 9.862448 9.283498 8.535854     10.98804 9.136609 8.292451 8.857473
    ## 5 5.32 9.836761 9.309442 8.543522     10.94489 8.855404 8.197822 8.826820
    ## 6 5.73 9.848315 9.318502 8.545635     11.01789 8.919469 8.272741 8.838364
    ##      BSDC1    FTSJ1    YPEL1
    ## 1 8.848922 10.38470 8.265589
    ## 2 9.022556 10.23077 8.426856
    ## 3 8.888275 10.37585 8.244617
    ## 4 8.985628 10.35854 8.257426
    ## 5 8.832436 10.37179 8.250075
    ## 6 8.864538 10.38892 8.280436

``` {.sourceCode .r}
plot(mcx)
```

<span id="fig:MCXScatter"></span> <img src="Statistiek_2019_2020_files/figure-html/MCXScatter-1.png" style="width:100.0%" alt="Scatterplot matrix voor de observaties in de bioactiviteit dataset." />

Figuur 11.1: Scatterplot matrix voor de observaties in de bioactiviteit dataset.

Figuur [11.1](index.md) suggereert dat de BA uitkomst sterk gecorreleerd is met alle genexpressies, maar de figuur toont tevens dat vele genexpressies ook onderling sterk gecorreleerd zijn. Het zal dus waarschijnlijk niet nodig zijn om alle genen simultaan in het model op te nemen. Niettegenstaande de hypothesetest-gebaseerde methoden toepasbaar lijken, argumenteren we hier dat die methoden niet geschikt zijn in de huidige context.

De doelstelling is om een zo optimaal mogelijk model te selecteren dat gebruikt kan worden voor predictie van de uitkomst. Niettegenstaande de predictie voor een lineair regressiemodel gegeven wordt door <span class="math inline">\$\\hat{Y}=\\beta\_0+\\sum\_{j=1}^{p-1}\\beta\_jX\_j\$</span>, weten we dat de <span class="math inline">\$\\beta\$</span>-parameters een interpretatie hebben met betrekking tot de gemiddelde uitkomst <span class="math inline">\$\\text{E}$$Y\\mid (X\_1,\\ldots,X\_{p-1})$$=\\beta\_0+\\sum\_{j=1}^{p-1}\\beta\_jX\_j\$</span>. Hypothesetesten voor <span class="math inline">\$H\_0:\\beta\_j=0\$</span> gaan dus na of predictor <span class="math inline">\$X\_j\$</span> (conditioneel op de andere regressoren in het model) gerelateerd is tot de gemiddelde uitkomst. Het al dan niet verwerpen van <span class="math inline">\$H\_0\$</span> heeft niet enkel te maken met de werkelijke waarde van <span class="math inline">\$\\beta\_j\$</span>, maar ook met de kracht van de hypothesetest en dus ook met de steekproefgrootte <span class="math inline">\$n\$</span>. Hypothesetesten maken een afweging van de evidentie in de data tegen/voor de gestelde hypotheses die betrekking hebben op de gemiddelde uitkomst. Voor een goed predictiemodel is het minder belangrijk dat het model de werkelijkheid weerspiegelt met betrekking tot het verband tussen de gemiddelde uitkomst en de regressoren; het is enkel belangrijk dat het model goede predicties geeft voor individuele uitkomsten. Om deze reden wordt modelselectie voor predictiemodellen uitgevoerd door gebruik te maken van specifieke modelselectiecriteria die de kwaliteit van het predictieve karakter van een model kwantificeert.

### <span class="header-section-number">11.3.2</span> Selectie-criterium

Het is aanlokkelijk om <span class="math inline">\$R^2\$</span> te gebruiken als een criterium voor hoe goed het model in staat is om predicties te maken, gezien het aangeeft hoeveel procent van de variabiliteit in de data verklaard kan worden door het model. <span class="math inline">\$R^2\$</span> is echter geen goed criterium. Hoe complexer het model (hoe meer predictoren er worden opgenomen) hoe hoger <span class="math inline">\$R^2\$</span> wordt. <span class="math inline">\$R^2 = 1-SSE/SSTot = SSR/SSTot\$</span> en SSE (SSR) neemt immers steeds af(toe) als een extra predictor in het model wordt opgenomen terwijl SSTot constant blijft. Het gebruik van <span class="math inline">\$R^2\$</span> zal dus aanleiding geven tot overfitting. We zullen immers steeds het meest complexe model selecteren. Hierdoor zal het model niet meer goed veralgemenen naar nieuwe data toe: het model wordt als het ware te goed getuned naar de dataset die is gebruikt om het model te trainen waardoor het niet meer bruikbaar is om predicties te doen.

Het Akaike Information Criterium (AIC) is een criterium dat een compromis maakt tussen de kwaliteit van de fit en de complexiteit van het model. <span class="math display">\\$$AIC = -2 \\text{ln } L(\\hat \\beta\_0, \\ldots, \\hat \\beta\_{p-1}, \\hat \\sigma^2) + 2 (p+1),\\$$</span>

waarbij de eerste term het natuurlijke logaritme is van likelihood, die voor een steekproef van <span class="math inline">\$n\$</span> i.i.d. normaal verdeelde observaties met dichtheidsfunctie <span class="math inline">\$f(Y\_i \\vert x\_{i1} \\ldots x\_{ip-1}, \\beta\_0,\\ldots, \\beta\_{p-1} ,\\sigma^2)\$</span> en conditioneel gemiddelde <span class="math inline">\$E$$Y\_i \\vert x\_{i1} \\ldots x\_{ip-1}$$=\\beta\_0 + \\sum\_{j=1}^{p-1} \\beta\_j x\_{j}\$</span> gedefinieerd is als: <span class="math display">\\$$ L(\\beta\_0, \\ldots, \\beta\_{p-1}, \\sigma^2) = \\prod\\limits\_{i=1}^n f(y\_i \\ldots x\_{ip-1}, \\beta\_0,\\ldots, \\beta\_{p-1} ,\\sigma^2) \\$$</span>

De likelihood geeft dus weer hoe waarschijnlijk het is om de data te observeren onder het normale regressiemodel. Gezien we de parameters niet kennen zullen we ze vervangen door de geschatte modelparameters. We kunnen voor het Normale lineaire regressie model aantonen dat <span class="math inline">\$-2 \\text{ln } L(\\hat \\beta\_0, \\ldots, \\hat \\beta\_{p-1}, \\hat \\sigma^2)\$</span> evenredig is met SSE. Hoe slechter de fit is, hoe hoger het AIC criterium.

De tweede term straft de kwaliteit van de fit als het ware af voor complexiteit. Merk op dat <span class="math inline">\$p+1\$</span> het aantal modelparameters is die we schatten met het normale regressie model: <span class="math inline">\$p\$</span> parameters van het lineaire model + de parameter <span class="math inline">\$\\sigma^2\$</span>. Het AIC criterium zal dus ook toenemen i.f.v. de complexiteit van het model (aantal parameters). Hierdoor wordt een afweging gemaakt tussen de kwaliteit van de model fit (term 1) en de complexiteit van het model (term 2).

Merk op dat de data analist het werkelijk model niet kent. Hij/zij zal dus verschillende kandidaat modellen met elkaar vergelijken. Vervolgens wordt het model geselecteerd waaronder het zo waarschijnlijk mogelijk is om de geobserveerde data te trekken in een steekproef (eerste term minimaal, SSE zo laag mogelijk), maar zonder dat de modelcomplexiteit daarbij te hoog wordt (tweede term). De analist zal dus het modelselecteren met een zo klein mogelijke AIC.

Opnieuw kan men gebruik maken van voorwaarts, achterwaartse of stapsgewijze modelselectie. Dat kan eenvoudig in R worden geïmplementeerd a.d.h.v. de ‘step’ functie.

We passen de strategie nu toe op het bioactiviteitsvoorbeeld. We zullen opnieuw voorwaartse, achterwaartse en stapsgewijze modelselectie uitvoeren.

Bij voorwaartse modelselectie starten we van een model zonder predictoren:

``` {.sourceCode .r}
m1 <- lm(BA~1,mcx)
m1
```

    ##
    ## Call:
    ## lm(formula = BA ~ 1, data = mcx)
    ##
    ## Coefficients:
    ## (Intercept)
    ##        5.55

``` {.sourceCode .r}
mfull <- lm(BA~.,mcx)
mfull
```

    ##
    ## Call:
    ## lm(formula = BA ~ ., data = mcx)
    ##
    ## Coefficients:
    ##  (Intercept)         HOXB5         PNISR          ATRX  LOC100505650
    ##      -9.5823        1.1665        2.6174       -2.0386        0.3095
    ##       PLK1S1       DNAJC12         ZFHX4         BSDC1         FTSJ1
    ##       0.4614        0.4616       -0.7015       -0.2761       -1.6318
    ##        YPEL1
    ##       1.3044

``` {.sourceCode .r}
mForward <- step(m1,scope=formula(mfull),direction="forward")
```

    ## Start:  AIC=-19.33
    ## BA ~ 1
    ##
    ##                Df Sum of Sq     RSS     AIC
    ## + LOC100505650  1    14.668  4.3588 -68.910
    ## + PNISR         1    14.376  4.6505 -66.643
    ## + ATRX          1    14.104  4.9231 -64.650
    ## + ZFHX4         1    13.869  5.1574 -63.022
    ## + PLK1S1        1    13.860  5.1671 -62.956
    ## + FTSJ1         1    13.781  5.2459 -62.426
    ## + BSDC1         1    13.703  5.3234 -61.913
    ## + DNAJC12       1    13.412  5.6141 -60.052
    ## + HOXB5         1    13.400  5.6263 -59.976
    ## + YPEL1         1    13.049  5.9774 -57.858
    ## <none>                      19.0266 -19.333
    ##
    ## Step:  AIC=-68.91
    ## BA ~ LOC100505650
    ##
    ##           Df Sum of Sq    RSS     AIC
    ## + YPEL1    1   1.20478 3.1540 -78.233
    ## + DNAJC12  1   0.91062 3.4482 -75.112
    ## + PLK1S1   1   0.81030 3.5485 -74.109
    ## + FTSJ1    1   0.78960 3.5692 -73.905
    ## + BSDC1    1   0.75759 3.6012 -73.592
    ## + HOXB5    1   0.69933 3.6595 -73.031
    ## + ZFHX4    1   0.69895 3.6599 -73.027
    ## + ATRX     1   0.63276 3.7261 -72.400
    ## + PNISR    1   0.36333 3.9955 -69.956
    ## <none>                 4.3588 -68.910
    ##
    ## Step:  AIC=-78.23
    ## BA ~ LOC100505650 + YPEL1
    ##
    ##           Df Sum of Sq    RSS     AIC
    ## <none>                 3.1540 -78.233
    ## + PNISR    1  0.133032 3.0210 -77.741
    ## + HOXB5    1  0.116332 3.0377 -77.548
    ## + FTSJ1    1  0.063065 3.0910 -76.940
    ## + ATRX     1  0.048977 3.1051 -76.781
    ## + DNAJC12  1  0.044347 3.1097 -76.729
    ## + ZFHX4    1  0.029234 3.1248 -76.559
    ## + BSDC1    1  0.029032 3.1250 -76.557
    ## + PLK1S1   1  0.025778 3.1283 -76.520

Nu achterwaartse modelselectie:

``` {.sourceCode .r}
mBackward <- step(mfull,direction="backward")
```

    ## Start:  AIC=-67.34
    ## BA ~ HOXB5 + PNISR + ATRX + LOC100505650 + PLK1S1 + DNAJC12 +
    ##     ZFHX4 + BSDC1 + FTSJ1 + YPEL1
    ##
    ##                Df Sum of Sq    RSS     AIC
    ## - BSDC1         1  0.003369 2.7288 -69.302
    ## - DNAJC12       1  0.005688 2.7312 -69.272
    ## - LOC100505650  1  0.014735 2.7402 -69.156
    ## - PLK1S1        1  0.025044 2.7505 -69.025
    ## - ZFHX4         1  0.030840 2.7563 -68.951
    ## - HOXB5         1  0.039762 2.7652 -68.838
    ## - ATRX          1  0.063271 2.7887 -68.542
    ## - YPEL1         1  0.139909 2.8654 -67.593
    ## - FTSJ1         1  0.157697 2.8832 -67.376
    ## <none>                      2.7255 -67.345
    ## - PNISR         1  0.211967 2.9374 -66.723
    ##
    ## Step:  AIC=-69.3
    ## BA ~ HOXB5 + PNISR + ATRX + LOC100505650 + PLK1S1 + DNAJC12 +
    ##     ZFHX4 + FTSJ1 + YPEL1
    ##
    ##                Df Sum of Sq    RSS     AIC
    ## - DNAJC12       1  0.006916 2.7357 -71.213
    ## - LOC100505650  1  0.014255 2.7431 -71.119
    ## - PLK1S1        1  0.025052 2.7539 -70.982
    ## - ZFHX4         1  0.028026 2.7569 -70.944
    ## - HOXB5         1  0.036934 2.7658 -70.831
    ## - ATRX          1  0.087988 2.8168 -70.191
    ## - YPEL1         1  0.136972 2.8658 -69.587
    ## - FTSJ1         1  0.155963 2.8848 -69.356
    ## <none>                      2.7288 -69.302
    ## - PNISR         1  0.228042 2.9569 -68.492
    ##
    ## Step:  AIC=-71.21
    ## BA ~ HOXB5 + PNISR + ATRX + LOC100505650 + PLK1S1 + ZFHX4 + FTSJ1 +
    ##     YPEL1
    ##
    ##                Df Sum of Sq    RSS     AIC
    ## - LOC100505650  1  0.014893 2.7506 -73.023
    ## - ZFHX4         1  0.025561 2.7613 -72.887
    ## - PLK1S1        1  0.031313 2.7671 -72.815
    ## - HOXB5         1  0.044757 2.7805 -72.645
    ## - ATRX          1  0.081205 2.8170 -72.189
    ## <none>                      2.7357 -71.213
    ## - YPEL1         1  0.171775 2.9075 -71.082
    ## - FTSJ1         1  0.183246 2.9190 -70.944
    ## - PNISR         1  0.221272 2.9570 -70.491
    ##
    ## Step:  AIC=-73.02
    ## BA ~ HOXB5 + PNISR + ATRX + PLK1S1 + ZFHX4 + FTSJ1 + YPEL1
    ##
    ##          Df Sum of Sq    RSS     AIC
    ## - ZFHX4   1   0.02825 2.7789 -74.665
    ## - HOXB5   1   0.04052 2.7912 -74.511
    ## - PLK1S1  1   0.05611 2.8068 -74.316
    ## - ATRX    1   0.13350 2.8841 -73.364
    ## - YPEL1   1   0.15739 2.9080 -73.075
    ## <none>                2.7506 -73.023
    ## - FTSJ1   1   0.31935 3.0700 -71.178
    ## - PNISR   1   0.90015 3.6508 -65.114
    ##
    ## Step:  AIC=-74.67
    ## BA ~ HOXB5 + PNISR + ATRX + PLK1S1 + FTSJ1 + YPEL1
    ##
    ##          Df Sum of Sq    RSS     AIC
    ## - HOXB5   1   0.02391 2.8028 -76.365
    ## - PLK1S1  1   0.03749 2.8164 -76.196
    ## - YPEL1   1   0.14939 2.9283 -74.832
    ## <none>                2.7789 -74.665
    ## - ATRX    1   0.19488 2.9738 -74.293
    ## - FTSJ1   1   0.29613 3.0750 -73.121
    ## - PNISR   1   0.89851 3.6774 -66.860
    ##
    ## Step:  AIC=-76.37
    ## BA ~ PNISR + ATRX + PLK1S1 + FTSJ1 + YPEL1
    ##
    ##          Df Sum of Sq    RSS     AIC
    ## - PLK1S1  1   0.05400 2.8568 -77.698
    ## - YPEL1   1   0.15995 2.9628 -76.423
    ## <none>                2.8028 -76.365
    ## - ATRX    1   0.17201 2.9748 -76.281
    ## - FTSJ1   1   0.28291 3.0857 -75.000
    ## - PNISR   1   1.01508 3.8179 -67.548
    ##
    ## Step:  AIC=-77.7
    ## BA ~ PNISR + ATRX + FTSJ1 + YPEL1
    ##
    ##         Df Sum of Sq    RSS     AIC
    ## - ATRX   1   0.11974 2.9766 -78.260
    ## <none>               2.8568 -77.698
    ## - YPEL1  1   0.26844 3.1252 -76.554
    ## - FTSJ1  1   0.50227 3.3591 -74.029
    ## - PNISR  1   0.96156 3.8184 -69.543
    ##
    ## Step:  AIC=-78.26
    ## BA ~ PNISR + FTSJ1 + YPEL1
    ##
    ##         Df Sum of Sq    RSS     AIC
    ## <none>               2.9766 -78.260
    ## - YPEL1  1   0.18969 3.1662 -78.098
    ## - FTSJ1  1   0.39421 3.3708 -75.907
    ## - PNISR  1   1.59191 4.5685 -65.266

We kunnen ook stapsgewijze modelselectie doen startende vanaf het meest eenvoudige model:

``` {.sourceCode .r}
mForStep <- step(m1,scope=list(lower=formula(m1),upper=formula(mfull)), direction="both")
```

    ## Start:  AIC=-19.33
    ## BA ~ 1
    ##
    ##                Df Sum of Sq     RSS     AIC
    ## + LOC100505650  1    14.668  4.3588 -68.910
    ## + PNISR         1    14.376  4.6505 -66.643
    ## + ATRX          1    14.104  4.9231 -64.650
    ## + ZFHX4         1    13.869  5.1574 -63.022
    ## + PLK1S1        1    13.860  5.1671 -62.956
    ## + FTSJ1         1    13.781  5.2459 -62.426
    ## + BSDC1         1    13.703  5.3234 -61.913
    ## + DNAJC12       1    13.412  5.6141 -60.052
    ## + HOXB5         1    13.400  5.6263 -59.976
    ## + YPEL1         1    13.049  5.9774 -57.858
    ## <none>                      19.0266 -19.333
    ##
    ## Step:  AIC=-68.91
    ## BA ~ LOC100505650
    ##
    ##                Df Sum of Sq     RSS     AIC
    ## + YPEL1         1    1.2048  3.1540 -78.233
    ## + DNAJC12       1    0.9106  3.4482 -75.112
    ## + PLK1S1        1    0.8103  3.5485 -74.109
    ## + FTSJ1         1    0.7896  3.5692 -73.905
    ## + BSDC1         1    0.7576  3.6012 -73.592
    ## + HOXB5         1    0.6993  3.6595 -73.031
    ## + ZFHX4         1    0.6990  3.6599 -73.027
    ## + ATRX          1    0.6328  3.7261 -72.400
    ## + PNISR         1    0.3633  3.9955 -69.956
    ## <none>                       4.3588 -68.910
    ## - LOC100505650  1   14.6678 19.0266 -19.333
    ##
    ## Step:  AIC=-78.23
    ## BA ~ LOC100505650 + YPEL1
    ##
    ##                Df Sum of Sq    RSS     AIC
    ## <none>                      3.1540 -78.233
    ## + PNISR         1   0.13303 3.0210 -77.741
    ## + HOXB5         1   0.11633 3.0377 -77.548
    ## + FTSJ1         1   0.06306 3.0910 -76.940
    ## + ATRX          1   0.04898 3.1051 -76.781
    ## + DNAJC12       1   0.04435 3.1097 -76.729
    ## + ZFHX4         1   0.02923 3.1248 -76.559
    ## + BSDC1         1   0.02903 3.1250 -76.557
    ## + PLK1S1        1   0.02578 3.1283 -76.520
    ## - YPEL1         1   1.20478 4.3588 -68.910
    ## - LOC100505650  1   2.82334 5.9774 -57.858

Nu stapsgewijze modelselectie startende vanaf het meest complexe model:

``` {.sourceCode .r}
mBackStep <- step(mfull,scope=list(lower=formula(m1),upper=formula(mfull)), direction="both")
```

    ## Start:  AIC=-67.34
    ## BA ~ HOXB5 + PNISR + ATRX + LOC100505650 + PLK1S1 + DNAJC12 +
    ##     ZFHX4 + BSDC1 + FTSJ1 + YPEL1
    ##
    ##                Df Sum of Sq    RSS     AIC
    ## - BSDC1         1  0.003369 2.7288 -69.302
    ## - DNAJC12       1  0.005688 2.7312 -69.272
    ## - LOC100505650  1  0.014735 2.7402 -69.156
    ## - PLK1S1        1  0.025044 2.7505 -69.025
    ## - ZFHX4         1  0.030840 2.7563 -68.951
    ## - HOXB5         1  0.039762 2.7652 -68.838
    ## - ATRX          1  0.063271 2.7887 -68.542
    ## - YPEL1         1  0.139909 2.8654 -67.593
    ## - FTSJ1         1  0.157697 2.8832 -67.376
    ## <none>                      2.7255 -67.345
    ## - PNISR         1  0.211967 2.9374 -66.723
    ##
    ## Step:  AIC=-69.3
    ## BA ~ HOXB5 + PNISR + ATRX + LOC100505650 + PLK1S1 + DNAJC12 +
    ##     ZFHX4 + FTSJ1 + YPEL1
    ##
    ##                Df Sum of Sq    RSS     AIC
    ## - DNAJC12       1  0.006916 2.7357 -71.213
    ## - LOC100505650  1  0.014255 2.7431 -71.119
    ## - PLK1S1        1  0.025052 2.7539 -70.982
    ## - ZFHX4         1  0.028026 2.7569 -70.944
    ## - HOXB5         1  0.036934 2.7658 -70.831
    ## - ATRX          1  0.087988 2.8168 -70.191
    ## - YPEL1         1  0.136972 2.8658 -69.587
    ## - FTSJ1         1  0.155963 2.8848 -69.356
    ## <none>                      2.7288 -69.302
    ## - PNISR         1  0.228042 2.9569 -68.492
    ## + BSDC1         1  0.003369 2.7255 -67.345
    ##
    ## Step:  AIC=-71.21
    ## BA ~ HOXB5 + PNISR + ATRX + LOC100505650 + PLK1S1 + ZFHX4 + FTSJ1 +
    ##     YPEL1
    ##
    ##                Df Sum of Sq    RSS     AIC
    ## - LOC100505650  1  0.014893 2.7506 -73.023
    ## - ZFHX4         1  0.025561 2.7613 -72.887
    ## - PLK1S1        1  0.031313 2.7671 -72.815
    ## - HOXB5         1  0.044757 2.7805 -72.645
    ## - ATRX          1  0.081205 2.8170 -72.189
    ## <none>                      2.7357 -71.213
    ## - YPEL1         1  0.171775 2.9075 -71.082
    ## - FTSJ1         1  0.183246 2.9190 -70.944
    ## - PNISR         1  0.221272 2.9570 -70.491
    ## + DNAJC12       1  0.006916 2.7288 -69.302
    ## + BSDC1         1  0.004597 2.7312 -69.272
    ##
    ## Step:  AIC=-73.02
    ## BA ~ HOXB5 + PNISR + ATRX + PLK1S1 + ZFHX4 + FTSJ1 + YPEL1
    ##
    ##                Df Sum of Sq    RSS     AIC
    ## - ZFHX4         1   0.02825 2.7789 -74.665
    ## - HOXB5         1   0.04052 2.7912 -74.511
    ## - PLK1S1        1   0.05611 2.8068 -74.316
    ## - ATRX          1   0.13350 2.8841 -73.364
    ## - YPEL1         1   0.15739 2.9080 -73.075
    ## <none>                      2.7506 -73.023
    ## + LOC100505650  1   0.01489 2.7358 -71.213
    ## - FTSJ1         1   0.31935 3.0700 -71.178
    ## + DNAJC12       1   0.00755 2.7431 -71.119
    ## + BSDC1         1   0.00409 2.7466 -71.075
    ## - PNISR         1   0.90015 3.6508 -65.114
    ##
    ## Step:  AIC=-74.67
    ## BA ~ HOXB5 + PNISR + ATRX + PLK1S1 + FTSJ1 + YPEL1
    ##
    ##                Df Sum of Sq    RSS     AIC
    ## - HOXB5         1   0.02391 2.8028 -76.365
    ## - PLK1S1        1   0.03749 2.8164 -76.196
    ## - YPEL1         1   0.14939 2.9283 -74.832
    ## <none>                      2.7789 -74.665
    ## - ATRX          1   0.19488 2.9738 -74.293
    ## - FTSJ1         1   0.29613 3.0750 -73.121
    ## + ZFHX4         1   0.02825 2.7506 -73.023
    ## + LOC100505650  1   0.01759 2.7613 -72.887
    ## + DNAJC12       1   0.00489 2.7740 -72.727
    ## + BSDC1         1   0.00072 2.7782 -72.674
    ## - PNISR         1   0.89851 3.6774 -66.860
    ##
    ## Step:  AIC=-76.37
    ## BA ~ PNISR + ATRX + PLK1S1 + FTSJ1 + YPEL1
    ##
    ##                Df Sum of Sq    RSS     AIC
    ## - PLK1S1        1   0.05400 2.8568 -77.698
    ## - YPEL1         1   0.15995 2.9628 -76.423
    ## <none>                      2.8028 -76.365
    ## - ATRX          1   0.17201 2.9748 -76.281
    ## - FTSJ1         1   0.28291 3.0857 -75.000
    ## + HOXB5         1   0.02391 2.7789 -74.665
    ## + LOC100505650  1   0.01287 2.7899 -74.526
    ## + ZFHX4         1   0.01165 2.7912 -74.511
    ## + DNAJC12       1   0.01066 2.7921 -74.499
    ## + BSDC1         1   0.00070 2.8021 -74.374
    ## - PNISR         1   1.01508 3.8179 -67.548
    ##
    ## Step:  AIC=-77.7
    ## BA ~ PNISR + ATRX + FTSJ1 + YPEL1
    ##
    ##                Df Sum of Sq    RSS     AIC
    ## - ATRX          1   0.11974 2.9766 -78.260
    ## <none>                      2.8568 -77.698
    ## - YPEL1         1   0.26844 3.1252 -76.554
    ## + PLK1S1        1   0.05400 2.8028 -76.365
    ## + HOXB5         1   0.04042 2.8164 -76.196
    ## + LOC100505650  1   0.03471 2.8221 -76.125
    ## + BSDC1         1   0.03081 2.8260 -76.077
    ## + DNAJC12       1   0.02797 2.8288 -76.042
    ## + ZFHX4         1   0.00022 2.8566 -75.700
    ## - FTSJ1         1   0.50227 3.3591 -74.029
    ## - PNISR         1   0.96156 3.8184 -69.543
    ##
    ## Step:  AIC=-78.26
    ## BA ~ PNISR + FTSJ1 + YPEL1
    ##
    ##                Df Sum of Sq    RSS     AIC
    ## <none>                      2.9766 -78.260
    ## - YPEL1         1   0.18969 3.1662 -78.098
    ## + ATRX          1   0.11974 2.8568 -77.698
    ## + LOC100505650  1   0.08940 2.8871 -77.328
    ## + ZFHX4         1   0.04005 2.9365 -76.735
    ## + BSDC1         1   0.00413 2.9724 -76.309
    ## + HOXB5         1   0.00203 2.9745 -76.284
    ## + PLK1S1        1   0.00173 2.9748 -76.281
    ## + DNAJC12       1   0.00061 2.9759 -76.268
    ## - FTSJ1         1   0.39421 3.3708 -75.907
    ## - PNISR         1   1.59191 4.5685 -65.266

``` {.sourceCode .r}
mForward
```

    ##
    ## Call:
    ## lm(formula = BA ~ LOC100505650 + YPEL1, data = mcx)
    ##
    ## Coefficients:
    ##  (Intercept)  LOC100505650         YPEL1
    ##      -32.240         1.671         2.337

``` {.sourceCode .r}
mBackward
```

    ##
    ## Call:
    ## lm(formula = BA ~ PNISR + FTSJ1 + YPEL1, data = mcx)
    ##
    ## Coefficients:
    ## (Intercept)        PNISR        FTSJ1        YPEL1
    ##      -6.538        2.165       -1.784        1.240

``` {.sourceCode .r}
mForStep
```

    ##
    ## Call:
    ## lm(formula = BA ~ LOC100505650 + YPEL1, data = mcx)
    ##
    ## Coefficients:
    ##  (Intercept)  LOC100505650         YPEL1
    ##      -32.240         1.671         2.337

``` {.sourceCode .r}
mBackStep
```

    ##
    ## Call:
    ## lm(formula = BA ~ PNISR + FTSJ1 + YPEL1, data = mcx)
    ##
    ## Coefficients:
    ## (Intercept)        PNISR        FTSJ1        YPEL1
    ##      -6.538        2.165       -1.784        1.240

### <span class="header-section-number">11.3.3</span> Alternatieve criteria

Recent zijn er binnen de machine learning diverse alternatieve technieken voor modelbouw ontwikkeld die hoofdzakelijk steunen op crossvalidatie, d.i. een techniek waarbij men telkens het regressiemodel schat op basis van een subset van de observaties en haar performantie evalueert door na te gaan hoe goed ze de resterende observaties voorspelt. Deze methoden zijn nog beter geschikt voor het bouwen van predictiemodellen. Ze evalueren het model immers op data die het model nog niet heeft gezien tijdens de training (fitting) fase.

Davenas, E., F. Beauvais, J. Amara, M. Oberbaum, B. Robinzon, A. Miadonnai, A. Tedeschi, et al. 1988. “Human Basophil Degranulation Triggered by Very Dilute Antiserum Against Ige.” *Nature* 333 (6176): 816–18. <http://dx.doi.org/10.1038/333816a0>.

Jacques, S., B. Ghesquière, P. De Bock, H. Demol, K. Wahni, P. Willems, J. Messens, F. Van Breusegem, and K. Gevaert. 2015. “Protein Methionine Sulfoxide Dynamics in Arabidopsis Thaliana Under Oxidative Stress.” *Molecular and Cellular Proteomics* 14 (5): 1217–29.

Rogovin, Konstantin A., Anastasiya M. Khrushchova, Olga N. Shekarova, Nina A. Vasilieva, and Nina Yu Vasilieva. 2017. “Females Choose Gentle, but Not Healthy or Macho Males in Campbell Dwarf Hamsters (Phodopus Campbelli Thomas 1905).” *Current Zoology* 63 (5): 545–54. doi:[10.1093/cz/zow090](https://doi.org/10.1093/cz/zow090).

Sotiriou, Christos, Pratyaksha Wirapati, Sherene Loi, Adrian Harris, Steve Fox, Johanna Smeds, Hans Nordgren, et al. 2006. “Gene Expression Profiling in Breast Cancer: Understanding the Molecular Basis of Histologic Grade to Improve Prognosis.” *Journal of the National Cancer Institute* 98 (4). Functional Genomics; Translational Research Unit, Universite Libre de Bruxelles, Brussels, Belgium. christos.sotiriou@bordet.be: 262–72. doi:[10.1093/jnci/djj052](https://doi.org/10.1093/jnci/djj052).

Valdés-López, O., S. Khan, R. Schmitz, S. Cui, J. Qiu, T. Joshi, D. Xu, B. Diers, J. Ecker, and G. Stacey. 2014. “Genotypic Variation of Gene Expression During the Soybean Innate Immunity Response.” *Plant Genetic Resources* 12 (S1): S27–S30.

---

[← 11.2 Modelselectie op basis van hypothesetesten](02-11-2-modelselectie-op-basis-van-hypothesetesten.md) · [Up: contents](index.md)

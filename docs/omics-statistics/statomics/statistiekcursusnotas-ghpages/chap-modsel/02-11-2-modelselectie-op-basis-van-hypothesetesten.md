---
title: 11.2 Modelselectie op basis van hypothesetesten
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-modsel.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-modsel.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 11.2 Modelselectie op basis van hypothesetesten

**Source:** [`chap-modsel.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-modsel.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

Stel, we willen een model selecteren voor lpsa waarbij lcavol, lweight en svi als predicoren worden toegelaten, alsook alle paarsgewijze interactietermen. We zullen drie verschillende strategiën beschouwen voorwaartse modelselectie, achterwaartse modelselecties en stapsgewijze modelselectie waarbij er in elke stap geëvalueerd wordt of een term in het model kan worden opgenomen en of er een andere term kan worden verwijderd.

### <span class="header-section-number">11.2.1</span> Voorwaartse modelselectie

De procedure kan als volgt beschreven worden:

1.  Start met het minimale model <span class="math inline">\$m\_1\$</span> met enkel het intercept
2.  Test voor alle modellen met slechts 1 predictor (er zijn dus <span class="math inline">\$p-1\$</span> dergelijke modellen) of de toegevoegde regressor significant verschillend is van 0 op het <span class="math inline">\$\\alpha\_{\\text{IN}}\$</span> significantieniveau.
3.  Indien geen enkele van de <span class="math inline">\$p\$</span>-waarden kleiner is dan <span class="math inline">\$\\alpha\_{\\text{IN}}\$</span>, stop de procedure. Het finale model is het minimale model <span class="math inline">\$m\_1\$</span>, <span class="math display">\\$$ Y\_i = \\beta\_0 + \\epsilon\_i \\$$</span> met <span class="math inline">\$\\epsilon\_i \\text{ i.i.d. } N(0,\\sigma^2)\$</span>.
4.  Indien er minstens 1 <span class="math inline">\$p\$</span>-waarde kleiner is dan <span class="math inline">\$\\alpha\_{\\text{IN}}\$</span>, selecteer het model dat overeenkomt met de kleinste <span class="math inline">\$p\$</span>-waarde. Dit model wordt <span class="math inline">\$m\_2\$</span> genoemd.
5.  Stel <span class="math inline">\$k=2\$</span>.
6.  Definieer de verzameling van modellen met 1 predictor toegevoegd aan <span class="math inline">\$m\_{k}\$</span>. Test dat de parameter van de toegevoegde regressor significant verschillend is van 0 op het <span class="math inline">\$\\alpha\_{\\text{IN}}\$</span> significantieniveau.
7.  Indien geen enkel van de <span class="math inline">\$p\$</span>-waarden kleiner is dan <span class="math inline">\$\\alpha\_{\\text{IN}}\$</span>, stop de procedure. Het finale model is <span class="math display">\\$$ Y\_i = \\beta\_0 + \\sum\_{j \\in m\_k} \\beta\_j x\_{ij} + \\epsilon\_i \\$$</span> met <span class="math inline">\$\\epsilon\_i \\text{ i.i.d. } N(0,\\sigma^2)\$</span>.
8.  Indien er minstens één <span class="math inline">\$p\$</span>-waarde kleiner is dan <span class="math inline">\$\\alpha\_{\\text{IN}}\$</span>, selecteer het model dat overeenkomt met de kleinste <span class="math inline">\$p\$</span>-waarde. Dit model wordt <span class="math inline">\$m\_{k+1}\$</span> genoemd.
9.  Verhoog <span class="math inline">\$k\$</span> met 1 (i.e. <span class="math inline">\$k\\leftarrow k+1\$</span>) en ga naar stap 6.

Voorbeeld voor lpsa. We laten interactietermen toe, maar de modelbouw moet zich houden aan de hiërarchie van hoofd- en interactietermen. We stellen <span class="math inline">\$\\alpha\_{\\text{IN}}=5\\%\$</span>.

``` {.sourceCode .r}
m1 <- lm(lpsa ~ 1, data=prostate)
add1(m1,scope=~lweight+lcavol+svi+lweight:lcavol+lweight:svi +lcavol:svi,test="F")
```

    ## Single term additions
    ##
    ## Model:
    ## lpsa ~ 1
    ##         Df Sum of Sq     RSS     AIC F value    Pr(>F)
    ## <none>               127.918  28.838
    ## lweight  1    16.041 111.877  17.841  13.621  0.000373 ***
    ## lcavol   1    69.003  58.915 -44.366 111.267 < 2.2e-16 ***
    ## svi      1    41.011  86.907  -6.658  44.830 1.499e-09 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

``` {.sourceCode .r}
m2 <- update(m1,~. + lcavol)
add1(m2,scope=~lweight+lcavol+svi+lweight:lcavol+lweight:svi +lcavol:svi,test="F")
```

    ## Single term additions
    ##
    ## Model:
    ## lpsa ~ lcavol
    ##         Df Sum of Sq    RSS     AIC F value   Pr(>F)
    ## <none>               58.915 -44.366
    ## lweight  1    5.9484 52.966 -52.690 10.5567 0.001606 **
    ## svi      1    5.2375 53.677 -51.397  9.1719 0.003172 **
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

``` {.sourceCode .r}
m3 <- update(m2,~ . + lweight)
add1(m3,scope=~lweight+lcavol+svi+lweight:lcavol+lweight:svi +lcavol:svi,test="F")
```

    ## Single term additions
    ##
    ## Model:
    ## lpsa ~ lcavol + lweight
    ##                Df Sum of Sq    RSS     AIC F value   Pr(>F)
    ## <none>                      52.966 -52.690
    ## svi             1    5.1814 47.785 -60.676  10.084 0.002029 **
    ## lweight:lcavol  1    0.1222 52.844 -50.914   0.215 0.643962
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

``` {.sourceCode .r}
m4 <- update(m3,~ . + svi)
add1(m4,scope=~lweight+lcavol+svi+lweight:lcavol+lweight:svi +lcavol:svi,test="F")
```

    ## Single term additions
    ##
    ## Model:
    ## lpsa ~ lcavol + lweight + svi
    ##                Df Sum of Sq    RSS     AIC F value Pr(>F)
    ## <none>                      47.785 -60.676
    ## lweight:lcavol  1   0.36606 47.419 -59.422  0.7102 0.4016
    ## lweight:svi     1   1.16445 46.621 -61.069  2.2979 0.1330
    ## lcavol:svi      1   0.02433 47.761 -58.725  0.0469 0.8291

``` {.sourceCode .r}
summary(m4)
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

Het geselecteerde model is <span class="math display">\\$$ Y\_i = \\beta\_0 + \\beta\_v X\_{iv} + \\beta\_w X\_{iw} + \\beta\_s X\_{is} + \\epsilon\_i \\$$</span> met <span class="math inline">\$\\epsilon\_i \\text{ i.i.d. } N(0,\\sigma^2)\$</span>.

### <span class="header-section-number">11.2.2</span> Achterwaartse modelselectie

Achterwaartse modelselectie is een procedure die ook gekend staat als achterwaartse eliminatie (Engels: *backward elimination*).

De procedure start van het maximale model en gaat na welke predictoren uit het model kunnen worden verwijderd.

1.  Start met het maximale model <span class="math inline">\$m\_1\$</span> met alle <span class="math inline">\$p-1\$</span> regressoren
2.  Bouw alle modellen waar 1 predictor wordt weggelaten en ga via een F-test na of het verwijderen van de predictoren significant is op het <span class="math inline">\$\\alpha\_{\\text{OUT}}\$</span> significantieniveau. Merk op dat deze test in model <span class="math inline">\$m\_1\$</span> moet uitgevoerd worden.
3.  Indien geen enkele van de <span class="math inline">\$p\$</span>-waarden groter is dan <span class="math inline">\$\\alpha\_{\\text{OUT}}\$</span>, stop de procedure. Het finale model is het maximale model <span class="math inline">\$m\_1\$</span>.
4.  Indien er minstens één <span class="math inline">\$p\$</span>-waarde groter dan <span class="math inline">\$\\alpha\_{\\text{OUT}}\$</span> is, selecteer het model dat overeenkomt met de grootste <span class="math inline">\$p\$</span>-waarde. Dit model wordt <span class="math inline">\$m\_2\$</span> genoemd.
5.  Stel <span class="math inline">\$k=2\$</span>
6.  Bouw alle modellen waar 1 predictor wordt weggelaten uit <span class="math inline">\$m\_k\$</span> en ga via een F-test na of het verwijderen van de predictoren significant is op het <span class="math inline">\$\\alpha\_{\\text{OUT}}\$</span> significantieniveau. Merk op dat deze test in model <span class="math inline">\$m\_k\$</span> moet uitgevoerd worden.
7.  Indien geen enkel van de <span class="math inline">\$p\$</span>-waarden groter is dan <span class="math inline">\$\\alpha\_{\\text{OUT}}\$</span>, stop de procedure. Het finale model is <span class="math inline">\$m\_k\$</span>
8.  Indien er minstens één <span class="math inline">\$p\$</span>-waarde groter is dan <span class="math inline">\$\\alpha\_{\\text{OUT}}\$</span>, selecteer het model dat overeenkomt met de grootste <span class="math inline">\$p\$</span>-waarde. Dit model wordt <span class="math inline">\$m\_{k+1}\$</span> genoemd.
9.  Verhoog <span class="math inline">\$k\$</span> met één (i.e. <span class="math inline">\$k\\leftarrow k+1\$</span>) en ga naar stap 6.

We passen de achterwaartse modelselectie toe op het prostaatkanker voorbeeld. We zoeken naar een model met enkel de belangrijke termen (i.e. significante termen) die geassocieerd zijn met lpsa. We laten interactietermen toe, maar de modelbouw moet zich houden aan de hiërarchie van hoofd- en interactietermen. We stellen <span class="math inline">\$\\alpha\_{\\text{OUT}}=5\\%\$</span>.

``` {.sourceCode .r}
alphaOut <- 0.05
m<- lm(lpsa~lweight+lcavol+svi+lweight:lcavol+lweight:svi +lcavol:svi,prostate)
dropHlp<-drop1(m,test="F")
dropHlp
```

    ## Single term deletions
    ##
    ## Model:
    ## lpsa ~ lweight + lcavol + svi + lweight:lcavol + lweight:svi +
    ##     lcavol:svi
    ##                Df Sum of Sq    RSS     AIC F value Pr(>F)
    ## <none>                      46.478 -57.365
    ## lweight:lcavol  1   0.00012 46.479 -59.365  0.0002 0.9878
    ## lweight:svi     1   0.87404 47.353 -57.558  1.6925 0.1966
    ## lcavol:svi      1   0.14093 46.619 -59.071  0.2729 0.6027

Merk op dat eerst enkel de interactietermen worden getest. De hoofdeffecten mogen niet uit het model worden weggelaten zolang er interactie termen in het model zijn opgenomen waarin deze hoofdeffecten voorkomen.

``` {.sourceCode .r}
while (sum(dropHlp[,6]>=alphaOut,na.rm=TRUE))
{
dropVarName<-rownames(dropHlp)[which.max(dropHlp[,6])]
m <- update(m,as.formula(paste("~.-",dropVarName)))
dropHlp<-drop1(m,test="F")
print(dropHlp)
}
```

    ## Single term deletions
    ##
    ## Model:
    ## lpsa ~ lweight + lcavol + svi + lweight:svi + lcavol:svi
    ##             Df Sum of Sq    RSS     AIC F value Pr(>F)
    ## <none>                   46.479 -59.365
    ## lweight:svi  1    1.2820 47.761 -58.725  2.5100 0.1166
    ## lcavol:svi   1    0.1419 46.621 -61.069  0.2778 0.5994
    ## Single term deletions
    ##
    ## Model:
    ## lpsa ~ lweight + lcavol + svi + lweight:svi
    ##             Df Sum of Sq    RSS     AIC F value    Pr(>F)
    ## <none>                   46.621 -61.069
    ## lcavol       1   28.1995 74.820 -17.184 55.6484 4.711e-11 ***
    ## lweight:svi  1    1.1644 47.785 -60.676  2.2979     0.133
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## Single term deletions
    ##
    ## Model:
    ## lpsa ~ lweight + lcavol + svi
    ##         Df Sum of Sq    RSS     AIC F value    Pr(>F)
    ## <none>               47.785 -60.676
    ## lweight  1    5.8923 53.677 -51.397  11.468  0.001039 **
    ## lcavol   1   28.0446 75.830 -17.884  54.581 6.304e-11 ***
    ## svi      1    5.1814 52.966 -52.690  10.084  0.002029 **
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Merk op dat opnieuw hetzelfde model wordt gekozen. Dat is in het algemeen niet het geval. Vaak heeft achterwaartse modelselectie de eigenschap om te resulteren in een meer complex model dan voorwaartse selectie.

### <span class="header-section-number">11.2.3</span> Stapsgewijze modelselectie

Deze methode is een combinatie van voorwaartse en achterwaartse modelselectie. Het kan starten van het maximale of het minimale model. We implementeren de methode, startende van het minimale model. In elke stap zal eerst worden gekeken of een predictor kan worden toegevoegd, vervolgens zal worden nagegaan of een predictor kan worden verwijderd van het model.

``` {.sourceCode .r}
alphaIn <- alphaOut <- 0.05
m <- lm(lpsa ~ 1 ,prostate)
notConverged <- TRUE
while (notConverged)
{
addHlp <- add1(m,scope= ~lweight+lcavol+svi+lweight:lcavol+lweight:svi +lcavol:svi,test="F")
print(addHlp)
addVarName<-rownames(addHlp)[which.min(addHlp[,6])]
if ((sum(addHlp[,6] < alphaIn,na.rm=TRUE))>0) m <- update(m,as.formula(paste("~.+",addVarName)))
dropHlp<-drop1(m,test="F")
print(dropHlp)
if ((sum(dropHlp[,6]>=alphaOut,na.rm=TRUE))>0) m <- update(m,as.formula(paste("~.-",dropVarName)))
if ((sum(addHlp[,6] < alphaIn,na.rm=TRUE) + sum(dropHlp[,6]>=alphaOut,na.rm=TRUE))>0) notConverged <- TRUE else notConverged <- FALSE
}
```

    ## Single term additions
    ##
    ## Model:
    ## lpsa ~ 1
    ##         Df Sum of Sq     RSS     AIC F value    Pr(>F)
    ## <none>               127.918  28.838
    ## lweight  1    16.041 111.877  17.841  13.621  0.000373 ***
    ## lcavol   1    69.003  58.915 -44.366 111.267 < 2.2e-16 ***
    ## svi      1    41.011  86.907  -6.658  44.830 1.499e-09 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## Single term deletions
    ##
    ## Model:
    ## lpsa ~ lcavol
    ##        Df Sum of Sq     RSS     AIC F value    Pr(>F)
    ## <none>               58.915 -44.366
    ## lcavol  1    69.003 127.918  28.838  111.27 < 2.2e-16 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## Single term additions
    ##
    ## Model:
    ## lpsa ~ lcavol
    ##         Df Sum of Sq    RSS     AIC F value   Pr(>F)
    ## <none>               58.915 -44.366
    ## lweight  1    5.9484 52.966 -52.690 10.5567 0.001606 **
    ## svi      1    5.2375 53.677 -51.397  9.1719 0.003172 **
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## Single term deletions
    ##
    ## Model:
    ## lpsa ~ lcavol + lweight
    ##         Df Sum of Sq     RSS     AIC F value    Pr(>F)
    ## <none>                52.966 -52.690
    ## lcavol   1    58.910 111.877  17.841 104.549 < 2.2e-16 ***
    ## lweight  1     5.948  58.915 -44.366  10.557  0.001606 **
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## Single term additions
    ##
    ## Model:
    ## lpsa ~ lcavol + lweight
    ##                Df Sum of Sq    RSS     AIC F value   Pr(>F)
    ## <none>                      52.966 -52.690
    ## svi             1    5.1814 47.785 -60.676  10.084 0.002029 **
    ## lweight:lcavol  1    0.1222 52.844 -50.914   0.215 0.643962
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## Single term deletions
    ##
    ## Model:
    ## lpsa ~ lcavol + lweight + svi
    ##         Df Sum of Sq    RSS     AIC F value    Pr(>F)
    ## <none>               47.785 -60.676
    ## lcavol   1   28.0446 75.830 -17.884  54.581 6.304e-11 ***
    ## lweight  1    5.8923 53.677 -51.397  11.468  0.001039 **
    ## svi      1    5.1814 52.966 -52.690  10.084  0.002029 **
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## Single term additions
    ##
    ## Model:
    ## lpsa ~ lcavol + lweight + svi
    ##                Df Sum of Sq    RSS     AIC F value Pr(>F)
    ## <none>                      47.785 -60.676
    ## lweight:lcavol  1   0.36606 47.419 -59.422  0.7102 0.4016
    ## lweight:svi     1   1.16445 46.621 -61.069  2.2979 0.1330
    ## lcavol:svi      1   0.02433 47.761 -58.725  0.0469 0.8291
    ## Single term deletions
    ##
    ## Model:
    ## lpsa ~ lcavol + lweight + svi
    ##         Df Sum of Sq    RSS     AIC F value    Pr(>F)
    ## <none>               47.785 -60.676
    ## lcavol   1   28.0446 75.830 -17.884  54.581 6.304e-11 ***
    ## lweight  1    5.8923 53.677 -51.397  11.468  0.001039 **
    ## svi      1    5.1814 52.966 -52.690  10.084  0.002029 **
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Merk op dat er voor dit voorbeeld nooit een predictor uit het model werd verwijderd eens die werd opgenomen in het model. Dat is in het algemeen niet het geval.

### <span class="header-section-number">11.2.4</span> Opmerkingen

Eerst een opmerking over de toepassing van de drie modelselectiemethoden op het prostaat voorbeeld. De drie methoden resulteerden in hetzelfde finale geselecteerde model (met enkel hoofdeffecten van lcavol, lweight en svi). In het algemeen leiden de drie methoden niet noodzakelijk tot eenzelfde finale model.

De <span class="math inline">\$p\$</span>-waarden in het geselecteerde model mogen niet geïnterpreteerd worden. Dit is minder eenvoudig om in te zien. We hebben immers meerdere hypothese testen uitgevoerd om tot dit model te komen. Bovendien zorgt de modelselectie ervoor dat enkel “significante” termen in het finale model staan; de selectieprocedure is dus een doelbewuste aanrijkingsprocedure. Herinner je dat de definitie van de <span class="math inline">\$p\$</span>-waarde de kans onder <span class="math inline">\$H\_0\$</span> is dat de teststatistiek “door zuiver toeval” minstens zo extreem is dan deze die waargenomen werd. Door de aanrijking via de modelselectieprocedure, is het niet langer “zuiver toeval” dat de teststatistiek groter is dan de geobserveerde.

Er is geen theoretische basis voor de selectieprocedure. Intuïtief lijkt de procedure zinvol omdat we gewend zijn om beslissingen te nemen aan de hand van hypothesetesten, maar hypothesetesten zijn eigenlijk enkel geldig wanneer ze doelgericht toegepast worden om een vooraf (i.e. voor het observeren van de data) duidelijk omschreven onderzoeksvraag te beantwoorden. Bij modelselectie wordt het pad doorheen de modellenruimte bepaald door de geobserveerde data, waardoor de <span class="math inline">\$p\$</span>-waarden hun betekenis verliezen, i.e. de hypotheses worden niet vooraf door de onderzoekers geformuleerd, maar ze worden door de data bepaald.

De analyse van lpsa in het vorige hoofdstuk zou ook als modelselectie kunnen worden bekeken: we startten met het model met de hoofdeffecten en met interactietermen. Vervolgens werd getest of de interactieterm nul was. Indien de interactieterm niet significant was, dan werd deze verwijderd en werden de hoofdeffecten getest. Dit lijkt op een achterwaartse modelselectie, maar in dat voorbeeld moeten we de procedure interpreteren als een klassieke hypothesetest (voor interactie) waarvan de nulhypothese in de onderzoeksvraag verscholen lag en dus niet door de data gesuggereerd werd.

---

[← 11.1 Inleiding](01-11-1-inleiding.md) · [Up: contents](index.md) · [11.3 Modelselectie voor predictie →](03-11-3-modelselectie-voor-predictie.md)

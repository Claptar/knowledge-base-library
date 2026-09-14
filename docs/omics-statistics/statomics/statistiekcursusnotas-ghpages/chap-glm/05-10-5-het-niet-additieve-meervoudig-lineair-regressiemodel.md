---
title: 10.5 Het niet-additieve meervoudig lineair regressiemodel
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-glm.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-glm.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 10.5 Het niet-additieve meervoudig lineair regressiemodel

**Source:** [`chap-glm.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-glm.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">10.5.1</span> Interactie tussen twee continue variabelen {#interactie-tussen-twee-continue-variabelen}

We breiden het meervoudig lineaire regressie model nu uit door toevoeging van interactie-termen.

Het model in de vorige secties werd een additief model genoemd omdat de bijdrage van het kanker volume in lpsa niet afhangt van de hoogte van het prostaat gewicht en de status van de zaadblaasjes. De helling voor lcavol hangt m.a.w. niet af van de hoogte van het log prostaat gewicht en de status van de zaadblaasjes.

<span class="math display">\\$$\\beta\_0 + \\beta\_v (x\_{v}+\\delta\_v) + \\beta\_w x\_{w} +\\beta\_s x\_{s} - \\beta\_0 - \\beta\_v x\_{v} - \\beta\_w x\_{w} -\\beta\_s x\_s = \\beta\_v \\delta\_v \\$$</span>

De svi status en de hoogte van het log-prostaatgewicht (<span class="math inline">\$x\_w\$</span>) heeft geen invloed op de bijdrage van het log-tumorvolume (<span class="math inline">\$x\_v\$</span>) in de gemiddelde log-prostaat antigeen concentratie en vice versa.

Het zou nu echter kunnen zijn dat de associatie tussen lpsa en lcavol wel afhangt van het prostaatgewicht. De gemiddelde toename in lpsa tussen patiënten die één eenheid van log-tumorvolume verschillen zou bijvoorbeeld lager kunnen zijn voor patiënten met een hoog prostaatgewicht dan bij patiënten met een laag prostaatgewicht. Het effect van het tumorvolume op de prostaat antigeen concentratie hangt in dit geval af van het prostaatgewicht.

Om een dergelijke of tussen 2 variabelen <span class="math inline">\$X\_v\$</span> en <span class="math inline">\$X\_w\$</span> statistisch te modelleren, kan men het product van beide variabelen in kwestie aan het model toevoegen:

<span class="math display">\\$$ Y\_i = \\beta\_0 + \\beta\_v x\_{iv} + \\beta\_w x\_{iw} +\\beta\_s x\_{is} + \\beta\_{vw} x\_{iv}x\_{iw} +\\epsilon\_i \\$$</span>

Deze term kwantificeert het *interactie-effect* van de predictoren <span class="math inline">\$x\_v\$</span> en <span class="math inline">\$x\_w\$</span> op de gemiddelde uitkomst. In dit model worden de termen <span class="math inline">\$\\beta\_vx\_{iv}\$</span> en <span class="math inline">\$\\beta\_wx\_{iw}\$</span> dikwijls de *hoofdeffecten* van de predictoren <span class="math inline">\$x\_v\$</span> en <span class="math inline">\$x\_w\$</span> genoemd.

Het ‘effect’ van een verschil in 1 eenheid in <span class="math inline">\$X\_v\$</span> op de gemiddelde uitkomst bedraagt nu:

<span class="math display">\\$$ \\begin{array}{l} E(Y\|X\_v=x\_v+1,X\_w=x\_w,X\_s=x\_s) − E(X\_v=x\_v,X\_w=x\_w,X\_s=x\_s) \\\\ \\quad = \\beta\_0 + \\beta\_v (x\_{v}+1) + \\beta\_w x\_w +\\beta\_s x\_{s} + \\beta\_{vw} (x\_{v}+1) x\_w - \\beta\_0 - \\beta\_v x\_{v} - \\beta\_w x\_w -\\beta\_s x\_{s} - \\beta\_{vw} (x\_{v}) x\_w \\\\ \\quad = \\beta\_v + \\beta\_{vw} x\_w \\end{array} \\$$</span>

wanneer het log-prostaatgewicht <span class="math inline">\$X\_w=c\$</span> en de <span class="math inline">\$X\_s=x\_s\$</span> status ongewijzigd blijven. Merk op dat het ‘effect’ van een wijzing in het tumorvolume bij constant log-prostaat gewicht nu inderdaad afhankelijk is van de hoogte van het log-prostaatgewicht <span class="math inline">\$x\_w\$</span>.

``` {.sourceCode .r}
lmVWS_IntVW <- lm(lpsa~lcavol + lweight + svi + lcavol:lweight ,prostate)
summary(lmVWS_IntVW)
```

    ##
    ## Call:
    ## lm(formula = lpsa ~ lcavol + lweight + svi + lcavol:lweight,
    ##     data = prostate)
    ##
    ## Residuals:
    ##      Min       1Q   Median       3Q      Max
    ## -1.65886 -0.44673  0.02082  0.50244  1.57457
    ##
    ## Coefficients:
    ##                Estimate Std. Error t value Pr(>|t|)
    ## (Intercept)     -0.6430     0.7030  -0.915  0.36278
    ## lcavol           1.0046     0.5427   1.851  0.06734 .
    ## lweight          0.6146     0.1961   3.134  0.00232 **
    ## sviinvasion      0.6859     0.2114   3.244  0.00164 **
    ## lcavol:lweight  -0.1246     0.1478  -0.843  0.40156
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ##
    ## Residual standard error: 0.7179 on 92 degrees of freedom
    ## Multiple R-squared:  0.6293, Adjusted R-squared:  0.6132
    ## F-statistic: 39.05 on 4 and 92 DF,  p-value: < 2.2e-16

De output van het model geeft een schatting van -0.125 voor de interactie <span class="math inline">\$\\beta\_{vw}\$</span> tussen het log-tumorvolume en het log-prostaatgewicht. Dat betekent dat de gemiddelde toename in lpsa tussen patiënten met een verschil in het log-tumorvolume maar met eenzelfde prostaatgewicht afhankelijk zal zijn van het prostaatgewicht. In het bijzonder suggereert de output dat patiënten die 1% verschillen in het tumorvolume maar hetzelfde log prostaat gewicht hebben gemiddeld (<span class="math inline">\$1.004-0.125 \\times x\_w\$</span>)% verschillen in prostaat antigeen concentratie (interpretatie volgt uit log transformatie van de response en tumorvolume). Patiënten die 1% verschillen in tumorvolume en die een log-prostaatgewicht hebben van 3 zullen gemiddeld 0.631% in prostaat antigeen concentratie verschillen. Terwijl patiënten die 1% verschillen in tumorvolume en die een log-prostaatgewicht hebben van 4 gemiddeld een verschil van 0.506% in prostaat antigeen concentratie hebben. De associatie van het log-tumorvolume en de log prostaat antigeen concentratie neemt dus af met toenemend prostaatgewicht.

Grafische interpretatie wordt weergegeven in Figuur [10.4](index.md). Hier worden het additieve model en het model met de lcavol:lweight interactie vergeleken. De fit toont duidelijk aan dat de associate tussen lpsa en lcavol gelijk is ongeacht de grootte van het prostaatgewicht voor het additieve model (parallele lijnen in het regressieoppervlak). Voor het model met interactie is dat niet het geval, de associate (helling) neemt af met toenemend prostaatgewicht. We zien een analoog effect wanneer we focussen op de associatie tussen lpsa en lweight. De lpsa <span class="math inline">\$\\leftrightarrow\$</span> lweight associatie neemt af met toenemend log-tumorvolume.

<span id="fig:prosIntFit1"></span> <img src="Statistiek_2019_2020_files/figure-html/prosIntFit1-1.png" style="width:100.0%" alt="Fit van het additieve model met de termen lcavol, lweight, svi (links) en het model met interactie lcavol, lweight, svi en lcavol:lweight (rechts). Merk op dat we enkel het regressieoppervlak weergeven voor patiënten zouder invasie van de zaadblaasjes. Dat voor patiënten met invasie van de zaadblaasjes is parallel met het getoonde oppervlak, maar ligt iets hoger. De rechtse figuur toont duidelijk dat de interactie ervoor zorgt dat de associatie tussen de response en het tumorvolume afhankelijk is van de hoogte van het prostaatgewicht en vice versa, dat zorgt voor een torsie in het regressievlak." />

Figuur 10.4: Fit van het additieve model met de termen lcavol, lweight, svi (links) en het model met interactie lcavol, lweight, svi en lcavol:lweight (rechts). Merk op dat we enkel het regressieoppervlak weergeven voor patiënten zouder invasie van de zaadblaasjes. Dat voor patiënten met invasie van de zaadblaasjes is parallel met het getoonde oppervlak, maar ligt iets hoger. De rechtse figuur toont duidelijk dat de interactie ervoor zorgt dat de associatie tussen de response en het tumorvolume afhankelijk is van de hoogte van het prostaatgewicht en vice versa, dat zorgt voor een torsie in het regressievlak.

Merk op, dat het interactie effect dat geobserveerd wordt in de steekproef echter statistisch niet significant is (p=0.4). Gezien de hoofdeffecten die betrokken zijn in een interactie term niet los van elkaar kunnen worden geïnterpreteerd is de conventie om een interactieterm uit het model te verwijderen wanneer die niet significant is. Na verwijdering van de niet-significante interactieterm kunnen de hoofdeffecten worden geïnterpreteerd.

### <span class="header-section-number">10.5.2</span> Interactie tussen continue variabele en factor variabele

We kunnen ook de interactie bestuderen tussen lcavol <span class="math inline">\$\\leftrightarrow\$</span> svi en lweight <span class="math inline">\$\\leftrightarrow\$</span> svi. Merk op dat svi een factor is. Het model wordt dan

<span class="math display">\\$$Y=\\beta\_0+\\beta\_vX\_v+\\beta\_wX\_w+\\beta\_sX\_s+\\beta\_{vs}X\_vX\_s + \\beta\_{ws}X\_wX\_s +\\epsilon\\$$</span>

``` {.sourceCode .r}
lmVWS_IntVS_WS <- lm(lpsa ~ lcavol + lweight + svi + svi:lcavol + svi:lweight,data=prostate)
summary(lmVWS_IntVS_WS)
```

    ##
    ## Call:
    ## lm(formula = lpsa ~ lcavol + lweight + svi + svi:lcavol + svi:lweight,
    ##     data = prostate)
    ##
    ## Residuals:
    ##      Min       1Q   Median       3Q      Max
    ## -1.50902 -0.44807  0.06455  0.45657  1.54354
    ##
    ## Coefficients:
    ##                     Estimate Std. Error t value Pr(>|t|)
    ## (Intercept)         -0.52642    0.56793  -0.927 0.356422
    ## lcavol               0.54060    0.07821   6.912 6.38e-10 ***
    ## lweight              0.58292    0.15699   3.713 0.000353 ***
    ## sviinvasion          3.43653    1.93954   1.772 0.079771 .
    ## lcavol:sviinvasion   0.13467    0.25550   0.527 0.599410
    ## lweight:sviinvasion -0.82740    0.52224  -1.584 0.116592
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ##
    ## Residual standard error: 0.7147 on 91 degrees of freedom
    ## Multiple R-squared:  0.6367, Adjusted R-squared:  0.6167
    ## F-statistic: 31.89 on 5 and 91 DF,  p-value: < 2.2e-16

Het effect van lcavol op lpsa en het effect van lweight op lpsa zal nu afhangen van de waarde voor svi. <span class="math inline">\$X\_s\$</span> is echter een dummy variabele die twee waarden aan kan nemen, <span class="math inline">\$X\_s=0\$</span> als de zaadblaasjes niet aangetast zijn en <span class="math inline">\$X\_s=1\$</span> als er invasie is van de zaadblaadjes. Gezien <span class="math inline">\$X\_S\$</span> een dummy variabele is bekomen we nu twee verschillende regressievlakken:

1.  Een regressievlak voor <span class="math inline">\$X\_s=0\$</span>: <span class="math display">\\$$Y=\\beta\_0+\\beta\_vX\_v+\\beta\_wX\_w + \\epsilon\\$$</span> waar de hellingen voor lcavol en lweight de hoofdeffecten zijn.
2.  En een regressievlak voor <span class="math inline">\$X\_s=1\$</span>: <span class="math display">\\$$Y=\\beta\_0+\\beta\_vX\_v+\\beta\_s+\\beta\_wX\_w+\\beta\_{vs}X\_v + \\beta\_{ws}X\_w +\\epsilon=(\\beta\_0+\\beta\_s)+(\\beta\_v+\\beta\_{vs})X\_v+(\\beta\_w+\\beta\_{ws})X\_w+\\epsilon\\$$</span> waar het intercept <span class="math inline">\$\\beta\_0 + \\beta\_s\$</span> is, de som van het intercept en het hoofdeffect voor <span class="math inline">\$X\_s\$</span>, en de hellingen voor lcavol en lweight respectievelijk <span class="math inline">\$\\beta\_v+\\beta\_{vs}\$</span> en <span class="math inline">\$\\beta\_w+\\beta\_{ws}\$</span> zijn, m.a.w. de sum van het hoofdeffect en de overeenkomstige interactieterm.

Grafisch wordt het model weergegeven in Figuur [10.5](index.md).

<span id="fig:prosIntFit2"></span> <img src="Statistiek_2019_2020_files/figure-html/prosIntFit2-1.png" style="width:100.0%" alt="Fit van het additieve model met de termen lcavol, lweight, svi (links) en het model met interacties lcavol, lweight, svi . lcavol:svi, lweight:svi (rechts). De rechtse figuur toont duidelijk dat de interactie er nu voor zorgt dat de associaties tussen de response &lt;-&gt; het log-tumorvolume en de response &lt;-&gt; het log-gewicht afhankelijk is van de status van de zaadblaasjes. De interacties zorgen voor andere hellingen bij patiënten met (rood) en zonder invasie (blauw) van de zaadblaasjes. Voor het additieve model (links) zien we enkel een verschuiving van het regressievlak, maar parallelle hellingen. Het hoofdeffect voor een factor variabele zorgt m.a.w. voor een ander intercept." />

Figuur 10.5: Fit van het additieve model met de termen lcavol, lweight, svi (links) en het model met interacties lcavol, lweight, svi . lcavol:svi, lweight:svi (rechts). De rechtse figuur toont duidelijk dat de interactie er nu voor zorgt dat de associaties tussen de response &lt;-&gt; het log-tumorvolume en de response &lt;-&gt; het log-gewicht afhankelijk is van de status van de zaadblaasjes. De interacties zorgen voor andere hellingen bij patiënten met (rood) en zonder invasie (blauw) van de zaadblaasjes. Voor het additieve model (links) zien we enkel een verschuiving van het regressievlak, maar parallelle hellingen. Het hoofdeffect voor een factor variabele zorgt m.a.w. voor een ander intercept.

Merk op dat de helling voor lcavol groter is bij patiënten met invasie van de zaadblaasjes dan bij patiënten zonder invasie van de zaadblaasjes en dat de helling voor lweight van teken veranderd. Verder zijn beide interactie-termen opnieuw niet significant.

---

[← 10.4 Nagaan van modelveronderstellingen {#nagaan-van-modelveronderstellingen}](04-10-4-nagaan-van-modelveronderstellingen-nagaan-van-modelvero.md) · [Up: contents](index.md) · [10.6 ANOVA Tabel {#anova-tabel} →](06-10-6-anova-tabel-anova-tabel.md)

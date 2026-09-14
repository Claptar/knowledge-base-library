---
title: 5.6 Two-sample t-test
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-besluit.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 5.6 Two-sample t-test

**Source:** [`chap-besluit.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

Een two-sample t-test is een statistische toets die werd ontwikkeld om verschillen in gemiddelde te detecteren tussen twee onafhankelijke groepen. We introduceren eerst een motiverende dataset. Men vermoedt dat hinderlijke geur onder de oksels (bromhidrosis) wordt veroorzaakt door specifieke microorganismen die behoren tot de groep van de *Corynebacterium spp.*. Het is immers niet het zweet dat de geur veroorzaakt, maar de geur is het resultaat van specifieke bacteriën die het zweet metaboliseren. Een andere sterk abundante groep wordt gevormd door de *Staphylococcus spp.*. In de CMET onderzoeksgroep van de Universiteit Gent wordt onderzoek verricht naar de mogelijkheid van microbiële transplanties in de oksels om mensen van de hinderlijke okselgeur te verlossen. Deze therapie bestaat erin om eerst het oksel-microbioom te verwijderen door een lokale antibiotica behandeling, en vervolgens via een microbiële transplantie de populatie te beïnvloeden. (zie: <https://youtu.be/9RIFyqLXdVw> )

De primaire onderzoeksvraag: leidt de microbiële transplantatie na zes weken tot een verandering in de relatieve abundantie van *Staphylococcus spp.* in het oksel microbioom in vergelijking met een placebo behandeling die enkel bestaat uit een antibiotica behandeling? Twintig personen met een hinderlijke okselgeur worden willekeurig toegekend aan twee behandelingsgroepen: placebo (enkel antibiotica) en transplantie (antibiotica, gevolgd door microbiële transplantatie). Zes weken na de start van de behandeling wordt een staal van de huid uit de okselholte genomen en worden de relatieve abundanties van *Staphylococcus spp.* en *Corynebacterium spp.* in het microbioom gemeten via DGGE (*Denaturing Gradient Gel Electrophoresis*).

De dataset bevat de variabelen Staph en Cor die de relatieve abundanties (%) weergeven van *Staphylococcus spp.* en *Corynebacterium spp.* De variabele Rel werd berekend als <span class="math display">\\$$ \\text{Rel}=\\frac{\\text{Staph}}{\\text{Staph}+\\text{Cor}}. \\$$</span> Deze variabele is het relatief aandeel van *Staphylococcus spp.* op het totaal aantal *Staphylococcus spp.* en *Corynebacterium spp.*.

In de folder dataset staat de file `oksel.rda`, een dump van het R object `oksel`, een data frame voor het oksel voorbeeld. R objecten die zijn opgeslagen kunnen via de `load(.)` functie worden ingelezen. De resultaten worden weergegeven in Figuur [5.14](index.md).

``` {.sourceCode .r}
load("dataset/oksel.rda")
head(oksel)
```

    ##              trt Staph  Cor      Rel
    ## 1 trt 2: placebo  34.7 28.4 54.99208
    ## 2 trt 2: placebo  16.4 35.1 31.84466
    ## 3 trt 2: placebo  31.4 45.0 41.09948
    ## 4 trt 2: placebo  44.7 30.4 59.52064
    ## 5 trt 2: placebo  45.9 26.3 63.57341
    ## 6 trt 2: placebo  30.7 43.3 41.48649

``` {.sourceCode .r}
#outline = FALSE, geen outliers
#alle datapunten worden toegevoegd via stripchart
#dus ook outliers zijn zichtbaar
boxplot(Rel~trt,data=oksel,xlab="behandeling",ylab="Relatieve abundantie",outline=FALSE)
set.seed(394)
stripchart(Rel~trt, data=oksel,vertical = TRUE, method = "jitter", pch = 19, col =c("bisque","coral"), add = TRUE)
set.seed(394)
stripchart(Rel~trt, data=oksel,vertical = TRUE, method = "jitter", pch = 1, add = TRUE)
```

<span id="fig:okselBox"></span> <img src="Statistiek_2019_2020_files/figure-html/okselBox-1.png" style="width:100.0%" alt="Boxplot van de relatieve Staphylococcus spp. abundantie t.o.v. het totaal van Staphylococcus spp. en Corynebacterium spp., voor beide behandelingsgroepen." />

Figuur 5.14: Boxplot van de relatieve Staphylococcus spp. abundantie t.o.v. het totaal van Staphylococcus spp. en Corynebacterium spp., voor beide behandelingsgroepen.

``` {.sourceCode .r}
par(mfrow=c(1,2))
oksel$trt=as.factor(oksel$trt)#zet charactervector om in factor
for (i in levels(oksel$trt))
    with(subset(oksel,trt==i), {
         qqPlot(Rel,main=i)
})
```

<span id="fig:okselQQ"></span> <img src="Statistiek_2019_2020_files/figure-html/okselQQ-1.png" style="width:100.0%" alt="QQ-plots van relatieve Staphylococcus spp. abundantie t.o.v. het totaal van Staphylococcus spp. en Corynebacterium spp." />

Figuur 5.15: QQ-plots van relatieve Staphylococcus spp. abundantie t.o.v. het totaal van Staphylococcus spp. en Corynebacterium spp.

Normaliteit van de data in beide groepen wordt ook nagegaan d.m.v. QQ-plots (zie Figuur [5.15](index.md)). De QQ-plots geven geen te grote afwijkingen weer van normaliteit.

We introduceren eerst de notatie. Stel <span class="math inline">\$Y\_{ij}\$</span> de uitkomst van observatie <span class="math inline">\$i=1,\\ldots, n\_j\$</span> uit populatie <span class="math inline">\$j=1,2\$</span>. We zullen dikwijls de term **behandeling** of **groep** gebruiken in plaats van populatie, zelfs wanneer de twee populaties niet geïnterpreteerd kunnen worden als behandelingen. Beschouw het als een (misgroeide) conventie. In de context van het voorbeeld is behandeling <span class="math inline">\$j=1\$</span> de microbiële transplantatie en behandeling <span class="math inline">\$j=2\$</span> de placebo behandeling.

We veronderstellen

<span class="math display">\\$$Y\_{ij}\\text{ i.i.d. } N(\\mu\_j,\\sigma^2)\\;\\;\\;i=1,\\ldots,n\_i\\;j=1,2.\\$$</span>

Merk op dat dit inhoudt dat gelijke varianties verondersteld worden. De eigenschap van gelijke varianties wordt ook aangeduid met de term **homoskedasticiteit**, en ongelijke varianties met **heteroskedasticiteit**.

We zijn geïnteresseerd in het testen van de nulhypothese <span class="math display">\\$$ H\_0: \\mu\_1 = \\mu\_2 \\$$</span> tegenover de alternatieve hypothese <span class="math display">\\$$ H\_1: \\mu\_1 \\neq \\mu\_2 .\\$$</span> De alternatieve hypothese drukt dus de onderzoeksvraag uit: een verschil in relatieve abundantie van *Staphylococcus spp.* na microbiële transplantatie t.o.v. de placebo behandeling.
De nul en alternatieve hypothese kunnen ook worden uitgedrukt in termen van de effectgrootte tussen behandeling en placebo groep <span class="math inline">\$\\mu\_1-\\mu\_2\$</span>: <span class="math display">\\$$H\_0: \\mu\_1-\\mu\_2 = 0,\\$$</span> <span class="math display">\\$$H\_1: \\mu\_1-\\mu\_2 \\neq 0.\\$$</span>

We kunnen de effectgrootte in het experiment schatten a.d.h.v. de steekproefgemiddeldes: <span class="math display">\\$$\\hat \\mu\_1-\\hat \\mu\_2=\\bar Y\_1 -\\bar Y\_2.\\$$</span> Gezien de experimentele eenheden onafhankelijk zijn, zijn de steekproefgemiddeldes dat ook en is de variantie op het verschil: <span class="math display">\\$$\\text{Var}\_{\\bar Y\_1 -\\bar Y\_2}=\\frac{\\sigma^2}{n\_1}+\\frac{\\sigma^2}{n\_2}=\\sigma^2 \\left(\\frac{1}{n\_1}+\\frac{1}{n\_2}\\right).\\$$</span> De standard error is bijgevolg: <span class="math display">\\$$\\sigma\_{\\bar Y\_1 -\\bar Y\_2}=\\sigma\\sqrt{\\frac{1}{n\_1}+\\frac{1}{n\_2}}.\\$$</span>

We zouden de variantie apart kunnen schatten in elke groep aan de hand van de steekproefvariatie, maar als we gelijkheid van variantie kunnen veronderstellen kan de variantie meer precies worden geschat door gebruik te maken van alle gegevens in beide groepen. Deze variatieschatter wordt ook de gepoolde variantieschatter genoemd: <span class="math inline">\$S^2\_p\$</span>.

Op basis van de observaties uit de eerste groep kan <span class="math inline">\$\\sigma^2\_1\$</span> geschat worden als <span class="math display">\\$$S\_1^2 = \\frac{1}{n\_1-1}\\sum\_{i=1}^{n\_1} (Y\_{i1}-\\bar{Y}\_1)^2.\\$$</span>

Analoog: op basis van de observaties uit de tweede groep kan <span class="math inline">\$\\sigma^2\_2\$</span> geschat worden als <span class="math display">\\$$S\_2^2 = \\frac{1}{n\_2-1}\\sum\_{i=1}^{n\_2} (Y\_{i2}-\\bar{Y}\_2)^2.\\$$</span>

Merk op dat we homoscedasticiteit veronderstellen, <span class="math inline">\$\\sigma\_1^2=\\sigma\_2^2=\\sigma^2\$</span>. Dus <span class="math inline">\$S\_1^2\$</span> en <span class="math inline">\$S\_2^2\$</span> zijn schatters zijn voor dezelfde parameter <span class="math inline">\$\\sigma^2\$</span>. Daarom kunnen ze gezamenlijk gebruikt worden om tot één schatter te komen die alle <span class="math inline">\$n\_1+n\_2\$</span> observaties gebruikt: <span class="math display">\\$$ S\_p^2 = \\frac{n\_1-1}{n\_1+n\_2-2} S\_1^2 + \\frac{n\_2-1}{n\_1+n\_2-2} S\_2^2 = \\frac{1}{n\_1+n\_2-2}\\sum\_{j=1}^2\\sum\_{i=1}^{n\_j} (Y\_{ij} - \\bar{Y}\_j)^2.\\$$</span>

De gepoolde variantieschatter wordt dus geschat door gebruik te maken van de kwadratische afwijkingen tussen de observaties en hun groepsgemiddelde en dat te delen door het aantal vrijheidsgraden <span class="math inline">\$n\_1+n\_2-2\$</span><a href="#fn36" id="fnref36" class="footnoteRef"><sup>36</sup></a>.

Nu we de effectgrootte en de standard error op de effectgrootte hebben kunnen schatten, kunnen we opnieuw een t-statistiek definiëren (two-sample <span class="math inline">\$t\$</span>-teststatistiek):

<span class="math display">\\$$T = \\frac{\\bar{Y}\_1-\\bar{Y}\_2}{\\sqrt{\\frac{S\_p^2}{n\_1}+\\frac{S\_p^2}{n\_2}}} = \\frac{\\bar{Y}\_1 - \\bar{Y}\_2}{S\_p\\sqrt{\\frac{1}{n\_1}+\\frac{1}{n\_2}}}.\\$$</span>

Als de data onafhankelijk zijn, de steekproefgemiddelden normaal verdeeld zijn en de variantie in beide groepen gelijk zijn, dan kan men aantonen de teststatistiek T opnieuw een t-verdeling volgt met <span class="math inline">\$n\_1+n\_2-2\$</span> vrijheidsgraden onder de nulhypothese.

Aangezien de alternatieve hypothese <span class="math inline">\$H\_1: \\mu\_1 \\neq \\mu\_2\$</span> impliceert dat de probabiliteitsmassa van de distributie van <span class="math inline">\$T\$</span> onder <span class="math inline">\$H\_1\$</span> verschuift naar hogere of lagere waarden, zullen we <span class="math inline">\$H\_0\$</span> wensen te verwerpen ten gunste van <span class="math inline">\$H\_1\$</span> voor grote absolute waarde van de teststatistiek. De <span class="math inline">\$p\$</span>-waarde wordt dus <span class="math display">\\$$\\begin{eqnarray\*} p&=&\\text{P}\_0\\left\[T\\leq -\|t\|\\right$$ + \\text{P}\_0\\left$$T\\geq \|t\|\\right$$\\\\ &=&\\text{P}\_0\\left$$\\vert T\\vert \\geq \\vert t \\vert\\right$$\\\\ &=&\\text{P}\_0\\left$$T \\geq \\vert t \\vert\\right$$\\times 2\\\\ &=& 2\\times(1-F\_T(\\vert t\\vert;n\_1+n\_2-2)), \\end{eqnarray\*}\\\]</span>

met <span class="math inline">\$F\_T(\\cdot;n\_1+n\_2-2)\$</span> de cumulatieve distributiefunctie van <span class="math inline">\$t\_{n\_1+n\_2-2}\$</span>.

### <span class="header-section-number">5.6.1</span> Oksel-voorbeeld

De onderzoeksvraag van het oksels-voorbeeld kan vertaald worden in een nulhypothese en een alternatieve hypothese.

De nulhypothese verwoordt de stelling dat de behandeling geen effect heeft op de gemiddelde relatieve abundantie van *Staphylococcus spp.*.

Indien <span class="math inline">\$\\mu\_1\$</span> en <span class="math inline">\$\\mu\_2\$</span> de gemiddelde abundanties voorstellen in respectievelijk de transplantatie groep en de placebo groep, dan schrijven we <span class="math display">\\$$ H\_0: \\mu\_1=\\mu\_2.\\$$</span> De alternatieve hypothese correspondeert met wat we wensen te bewijzen aan de hand van de experimentele data: een verschil in gemiddelde abundantie van *Staphylococcus spp.* in de transplantatie groep i.v.m. de placebo groep. Dus <span class="math display">\\$$H\_1: \\mu\_1\\neq \\mu\_2.\\$$</span>

De berekeningen kunnen als volgt in R worden uitgevoerd:

``` {.sourceCode .r}
ybar1<-mean(oksel$Staph[oksel$trt=="trt 1: transplant"])
ybar1
```

    ## [1] 49.79

``` {.sourceCode .r}
ybar2<-mean(oksel$Staph[oksel$trt=="trt 2: placebo"])
ybar2
```

    ## [1] 31.9

``` {.sourceCode .r}
var1<-var(oksel$Staph[oksel$trt=="trt 1: transplant"])
var1
```

    ## [1] 64.95656

``` {.sourceCode .r}
var2<-var(oksel$Staph[oksel$trt=="trt 2: placebo"])
var2
```

    ## [1] 76.78222

``` {.sourceCode .r}
n1<-sum(oksel$trt=="trt 1: transplant")
n1
```

    ## [1] 10

``` {.sourceCode .r}
n2<-sum(oksel$trt=="trt 2: placebo")
n2
```

    ## [1] 10

``` {.sourceCode .r}
#gepoolde variantieschatting
sp2<-((n1-1)*var1+(n2-1)*var2)/(n1+n2-2)
sp2
```

    ## [1] 70.86939

``` {.sourceCode .r}
#geobserveerde t-statistiek
t.obs<-(ybar1-ybar2)/sqrt(sp2/n1+sp2/n2)
t.obs
```

    ## [1] 4.751886

``` {.sourceCode .r}
#p-waarde
p<-(1-pt(abs(t.obs),df=n1+n2-2))*2
p
```

    ## [1] 0.0001592919

``` {.sourceCode .r}
#De p-waarde kon ook worden berekend door
#gebruik te maken van de probabiliteit in de linker staart
#dat is vaak stabieler in R
p<-pt(-abs(t.obs),df=n1+n2-2)*2
p
```

    ## [1] 0.0001592919

De R software heeft ook een specifieke functie voor het uitvoeren van deze <span class="math inline">\$t\$</span>-test.

``` {.sourceCode .r}
t.test(Staph~trt,data=oksel,var.equal=TRUE)
```

    ##
    ##  Two Sample t-test
    ##
    ## data:  Staph by trt
    ## t = 4.7519, df = 18, p-value = 0.0001593
    ## alternative hypothesis: true difference in means is not equal to 0
    ## 95 percent confidence interval:
    ##   9.980404 25.799596
    ## sample estimates:
    ## mean in group trt 1: transplant    mean in group trt 2: placebo
    ##                           49.79                           31.90

Uit deze analyse lezen we <span class="math inline">\$p\\approx 0.16 \\times 10^{-3}&lt;&lt;0.05\$</span>.

Dus op het <span class="math inline">\$5\\%\$</span> significantieniveau verwerpen we de nulhypothese ten voordele van de alternatieve en besluiten we dat de gemiddelde abundantie van *Staphylococcus spp.* extreem significant hoger is in de transplantatie groep dan in de placebo groep<a href="#fn37" id="fnref37" class="footnoteRef"><sup>37</sup></a>.

Indien de transplantatie geen effect heeft op de gemiddelde abundantie van *Staphylococcus spp.*, dan is er slechts een kans van 16 in de <span class="math inline">\$100000\$</span> om een teststatistiek te bekomen in een willekeurige steekproef die minstens zo extreem is als deze die wij geobserveerd hebben.

Dit is uiterst zeldzaam onder de hypothese dat <span class="math inline">\$H\_0\$</span> waar is, en het is kleiner dan <span class="math inline">\$5\\%\$</span> (het significantieniveau). Indien <span class="math inline">\$H\_1\$</span> waar zou zijn, dan verwachten we grotere absolute waarden van de teststatistiek en verwachten we dus ook kleine <span class="math inline">\$p\$</span>-waarden. Om deze reden wensen we niet verder te geloven dat <span class="math inline">\$H\_0\$</span> waar is, en besluiten we dat er veel evidentie in de steekproefdata zit om te besluiten dat <span class="math inline">\$H\_1\$</span> waar is op het <span class="math inline">\$5\\%\$</span> significantieniveau.

**Good statistical practice** houdt ook in dat niet enkel de <span class="math inline">\$p\$</span>-waarde van de hypothesetest wordt gerapporteerd, maar dat ook de gemiddelden en een maat voor de betrouwbaarheid van de schattingen (bv. BI) worden gerapporteerd.

**Conclusie** Gemiddeld is de relatieve abundantie van *Staphylococcus spp.* in het microbioom van de oksel in de transplantatie groep extreem significant verschillend van dat in de controle groep (<span class="math inline">\$p&lt;&lt;0.001\$</span>). De relatieve abundantie van *Staphylococcus spp.* is gemiddeld 17.9% hoger in de transplantie groep dan in de controle groep (95% BI $$10.0,25.8$$%).

---

[← 5.5 Principe van Hypothesetoetsen (via one sample t-test)](05-5-5-principe-van-hypothesetoetsen-via-one-sample-t-test.md) · [Up: contents](index.md) · [5.7 Aannames →](07-5-7-aannames.md)

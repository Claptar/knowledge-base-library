---
title: 9.3 Toets voor associatie tussen 2 kwalitatieve variabelen
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-categorisch.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-categorisch.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 9.3 Toets voor associatie tussen 2 kwalitatieve variabelen

**Source:** [`chap-categorisch.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-categorisch.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">9.3.1</span> Gepaarde gegevens

Net zoals bij het vergelijken van gemiddelden (uitkomsten op 2 continue veranderlijken) is het ook hier in principe mogelijk dezelfde individuen 2 keer te meten (bijvoorbeeld, vóór en na blootstelling aan de experimentele stof) en telkens de uitkomst te observeren. In dat geval hebben we te maken met *gepaarde binaire uitkomsten* en moeten we in de statistische analyse rekening houden met de paring.

#### <span class="header-section-number">9.3.1.1</span> Voorbeeld

<span class="citation">Rogovin et al. (2017)</span> onderzochten de partnerkeuze van seksueel mature vrouwelijke *Campbelli* dwerghamster. Hiervoor bekeken ze verschillende karakteristieken van de mannetjes, waaronder seksgerelateerde morfologische kenmerken (lichaamsmassa, externe testikel diameter), testosteron niveau, immunocompetentie kenmerken (de concentratie aan T-cel en B-cel immuuncellen in het bloed), maar ook gedragskenmerken zoals agressiviteit en seksuele dominantie van het mannetje.

De experimentele set-up betreft een rechthoekige doos van plexiglas met drie compartimenten, waarin het vrouwtje zich in het middenste gedeelte bevindt (zie Figuur [9.4](index.md)).

<span id="fig:hamsterKooi"></span> <img src="Statistiek_2019_2020_files/figure-html/hamsterKooi-1.png" style="width:100.0%" alt="Experimentele opstelling voor het bepalen van de partnerkeuze bij dwerghamsters" />

Figuur 9.4: Experimentele opstelling voor het bepalen van de partnerkeuze bij dwerghamsters

De mannetjes, die overigens broers zijn, hangen vast aan de doos waardoor ze zich slechts over drie vierden van de ruimte van hun compartiment vrij kunnen bewegen. Na alle dieren enkele minuten te laten acclimatiseren worden niet-doorzichtige wanden die de compartimenten scheidden, opgetrokken waardoor het vrouwtje zich via de aangegeven deurtjes naar de mannetjes kan begeven. Aangezien de mannetjes zich niet buiten hun compartiment kunnen begeven, ligt de keuze volledig in de handen van het vrouwtje. Het wordt aangenomen dat het vrouwtje een partnerkeuze maakt indien ze meer dan twee derden van de tijd met één mannetje doorbrengt, relatief ten opzichte van de totale tijd die ze met mannetjes doorbrengt.

Elk vrouwtje onderging tweemaal de test, waarbij ze telkens kon kiezen tussen één agressief en één niet-agressief mannetje. Om te onderzoeken of de partnerkeuze van het vrouwtje beïnvloed wordt door de omgeving, kwam het vrouwtje in één van de testen uit een vijandige omgeving (hoge populatie, weinig voedsel, veel concurrentie) en in een andere test uit een vriendelijkere omgeving.

De resultaten van de studie zijn samengevat in de onderstaande kruistabel (Tabel [9.1](index.md)).

``` {.sourceCode .r}
hamster <- matrix(c(3,17,1,13),ncol=2,byrow=TRUE)
rownames(hamster) <- c("vijandig-agressief", "vijandig-niet-agressief")
colnames(hamster) <- c("vriendelijk-agressief","vriendelijk-niet-agressief")
```

|  | vriendelijk-agressief | vriendelijk-niet-agressief | totaal |
|:---|:---|:---|:---|
| vijandig-agressief | 3 (e) | 17 (f) | 20 |
| vijandig-niet-agressief | 1 (g) | 13 (h) | 14 |
| totaal | 4 | 30 | 34 |

<span id="tab:catHamster">Tabel 9.1: </span>Kruistabel van partnerkeuze bij dwerghamster.

De kans op de keuze voor een agressief mannetje na verblijf in een vijandige omgeving noteren we als <span class="math inline">\$\\pi\_1\$</span> en kunnen we schatten als <span class="math inline">\$(e+f)/n\$</span>, waarbij <span class="math inline">\$n=e+f+g+h\$</span>. De kans op de keuze voor een agressief mannetje na een vriendelijke omgeving noteren we met <span class="math inline">\$\\pi\_0\$</span> en kunnen we schatten als <span class="math inline">\$(e+g)/n\$</span>. Het verschil tussen beide kansen, het absoluut riscoverschil (ARV), schatten we als <span class="math display">\\$$\\begin{equation\*} \\widehat{\\text{ARV}}=\\hat\\pi\_1-\\hat\\pi\_0=\\frac{e+f}{n}-\\frac{e+g}{n}=\\frac{f-g}{n} \\end{equation\*}\\$$</span> en wordt enkel beïnvloed door de aantallen discordante paren <span class="math inline">\$f\$</span> en <span class="math inline">\$g\$</span><a href="#fn56" id="fnref56" class="footnoteRef"><sup>56</sup></a>. Men kan aantonen dat de standaard error van dit verschil gelijk is aan <span class="math display">\\$$\\begin{equation\*} \\text{SE}\_{\\widehat{\\text{ARV}}}=\\frac{1}{n}\\sqrt{f+g-\\frac{(f-g)^2}{n}} \\end{equation\*}\\$$</span>

Als er voldoende gegevens zijn, kan men een <span class="math inline">\$(1-\\alpha)100\\%\$</span> betrouwbaarheidsinterval voor het absolute risicoverschil op de keuze voor een agressief mannetje t.g.v. de omgeving schatten als <span class="math display">\\$$\\left\[\\widehat{\\text{ARV}}-z\_{\\alpha/2}\\text{SE}\_{\\widehat{\\text{ARV}}},\\widehat{\\text{ARV}}-z\_{\\alpha/2}\\text{SE}\_{\\widehat{\\text{ARV}}}\\right$$\\\]</span> of <span class="math display">\\$$\\left\[\\frac{f-g}{n}-\\frac{z\_{\\alpha/2}}{n}\\sqrt{f+g-\\frac{(f-g)^2}{n}},\\frac{f-g}{n}+\\frac{z\_{\\alpha/2}}{n}\\sqrt{f+g-\\frac{(f-g)^2}{n}}\\right$$ \\\]</span>

``` {.sourceCode .r}
f=hamster[1,2]
g=hamster[2,1]
n=sum(hamster)
riskdiff=(f-g)/n
riskdiff
```

    ## [1] 0.4705882

``` {.sourceCode .r}
se=sqrt(f+g-(f-g)^2/n)/n
se
```

    ## [1] 0.09517144

``` {.sourceCode .r}
bi=riskdiff+c(-1,1)*qnorm(0.975)*se
bi
```

    ## [1] 0.2840556 0.6571208

Het absolute risicoverschil op de keuze van een agressief mannetje tussen een verblijf in een vijandige en vriendelijke omgeving bedraagt
<span class="math display">\\$$\\begin{equation\*} \\widehat{\\text{ARV}}=\\frac{17-1}{34}=0.471 \\end{equation\*}\\$$</span> of 47.1%. De standaard error van dit verschil is <span class="math display">\\$$\\begin{equation\*} \\text{SE}\_{\\widehat{\\text{ARV}}}=\\frac{1}{34}\\sqrt{17+1-\\frac{(17-1)^2}{34}}=0.0952 \\end{equation\*}\\$$</span> Een 95% betrouwbaarheidsinterval absolute risicoverschil op de keuze van een agressief mannetje tussen een verblijf in een vijandige en vriendelijke omgeving is bijgevolg <span class="math display">\\$$\\begin{equation\*} \\left\[0.471-1.96\\times 0.0952,0.471+1.96\\times 0.0952\\right$$=$$0.284,0.658$$ \\end{equation\*}\\\]</span>

We hebben dus geschat dat het absolute risico met 95% kans in het interval $$28.4,65.8$$% ligt.

#### <span class="header-section-number">9.3.1.2</span> McNemar test

We gaan vervolgens na hoe we kunnen toetsen of de risico’s verschillen tussen de vijandige en vriendelijke omgeving. Indien alle vrouwtjes in zowel de vijandige als vriendelijke omgeving dezelfde partnerkeuze hadden, dan was er geen informatie over de vraag of de omgeving geassocieerd is met de partnerkeuze. Enkel de discordante paren leveren hier informatie over. Als er meer discordante paren zijn waar een vrouwtje een agressief mannetje kiest na verblijf in een vijandige omgeving en een niet-agressief mannetje na een vriendelijke omgeving, dan discordante paren waar het vrouwtje een niet-agressief mannetje kiest na verblijf in een vijandige omgeving en een agressief mannetje kiest na een vriendelijke omgeving, dan is er een indicatie tegen de nulhypothese dat er geen associatie is tussen de partnerkeuze en de omgeving. Men kan daarom toetsen of de partnerkeuze geassocieerd is met de omgeving door de kans te evalueren dat in een lukraak discordant paar, het vrouwtje na verblijf in een vijandige omgeving kiest voor het agressieve mannetje. Deze kans wordt geschat als <span class="math inline">\$f/(f+g)\$</span> en wordt verwacht in de buurt van 0.5 te liggen als de nulhypothese geldt dat er geen associatie is tussen partnerkeuze en omgeving. Meer bepaald volgt het getal <span class="math inline">\$f\$</span> binnen de groep discordante paren onder de nulhypothese een Binomiale verdeling met parameters <span class="math inline">\$f+g\$</span> en 0.5. De standaarddeviatie van <span class="math inline">\$f\$</span> is bijgevolg gelijk aan <span class="math display">\\$$\\begin{equation\*} \\sqrt{(f+g)\\times 0.5\\times 0.5}=\\frac{\\sqrt{f+g}}{2} \\end{equation\*}\\$$</span> onder de nulhypothese. Op voorwaarde dat er voldoende observaties zijn, kan men nu de one-sample z-test<a href="#fn57" id="fnref57" class="footnoteRef"><sup>57</sup></a> gebruiken om te toetsen of de kans dat een lukraak discordant paar in de cel rechtsboven van de tabel gelegen is, 0.5 bedraagt. M.a.w. bekijken we het gestandaardiseerde verschil tussen <span class="math inline">\$f\$</span> en haar verwachtingswaarde onder de nulhypothese: <span class="math display">\\$$\\begin{equation\*} \\frac{f-(f+g)/2}{\\sqrt{f+g}/2}=\\frac{f-g}{\\sqrt{f+g}} \\end{equation\*}\\$$</span>

die bij benadering een Normale verdeling volgt onder de nulhypothese. De Normale benadering is goed als <span class="math display">\\$$f \\times g/(f+g) \\geq 5\\$$</span> De toets gebaseerd op bovenstaande toetsingsgrootheid heet de *Mc Nemar toets*.

In kleine steekproeven is het meer aangewezen om een continuïteitscorrectie te gebruiken d.m.v. de toetsingsgrootheid <span class="math display">\\$$\\begin{equation\*} \\frac{\|f-g\|-1}{\\sqrt{f+g}} \\end{equation\*}\\$$</span>

De **Mc Nemar test** wordt gebruikt om te toetsen of er een associatie is tussen 2 kwalitatieve, binaire variabelen, i.h.b. om te toetsen of de kans op succes voor de ene variabele verschilt tussen de 2 strata van de andere kwalitatieve variabele. Ze vereist dat alle metingen voor de ene kwalitatieve variabele (uitkomst) in het ene stratum van de andere kwalitatieve variabele, onafhankelijk zijn, en dat elke meting uit het ene stratum gepaard is met een meting uit het andere stratum in die zin dat ze van verwante subjecten afkomstig zijn. Op die manier vormt ze het analogon van de gepaarde t-test voor binaire, kwalitatieve i.p.v. continue variabelen.

We voeren nu de analyse uit voor het hamstervoorbeeld in R:

``` {.sourceCode .r}
correct=f*g/(f+g)
correct
```

    ## [1] 0.9444444

``` {.sourceCode .r}
#continuiteitscorrectie
t= (abs(f-g)-1)/sqrt(f+g)
t
```

    ## [1] 3.535534

``` {.sourceCode .r}
p=(1-pnorm(t))*2
p
```

    ## [1] 0.000406952

Voor het dwerghamster voorbeeld observeren we dat <span class="math inline">\$f\\times g/(f+g)=\$</span> 0.944 <span class="math inline">\$&lt;5\$</span>. We zullen dus de continuïteitscorrectie uitvoeren. De McNemar toetsingsgrootheid bedraagt <span class="math inline">\$(\\vert 17-1 \\vert -1)/\\sqrt{17+1}=\$</span> 3.54. De kans dat een Normaal verdeelde toevalsveranderlijke groter is dan 3.54 of kleiner is dan -3.54 bedraagt 0.0407% en stelt ook de p-waarde van de toets voor. We verwerpen bijgevolg de nulhypothese op het 5% significantieniveau en besluiten dat de parternkeuze extreem significant geassocieerd is met de omgeving.

In R kan de analyse ook worden uitgevoerd a.d.h.v. de `mcnemar.test` functie

``` {.sourceCode .r}
mcnemar.test(hamster)
```

    ##
    ##  McNemar's Chi-squared test with continuity correction
    ##
    ## data:  hamster
    ## McNemar's chi-squared = 12.5, df = 1, p-value = 0.000407

We zien dat hier eveneens de continuïteitscorrectie werd uitgevoerd en dat we exact dezelfde p-waarde bekomen.

Merk echter op dat de Normale benadering van deze toetstatistiek niet ideaal is omdat <span class="math inline">\$f \\times g/(f+g)=\$</span> 0.944 <span class="math inline">\$&lt;5\$</span>. Bovenstaande p-waarde is om die reden niet accuraat. Het is hier meer aangewezen om een exacte toets te gebruiken op basis van het principe in Sectie [9.2.1](index.md). Dergelijke toetsen maken gebruik van de exacte Binomiale verdeling van de gegevens om te toetsen of de kans dat een lukraak discordant paar in de cel rechtsboven van de tabel gelegen is, 0.5 bedraagt.

``` {.sourceCode .r}
binom.test(x=f,n=f+g,p=0.5)
```

    ##
    ##  Exact binomial test
    ##
    ## data:  f and f + g
    ## number of successes = 17, number of trials = 18, p-value =
    ## 0.000145
    ## alternative hypothesis: true probability of success is not equal to 0.5
    ## 95 percent confidence interval:
    ##  0.7270564 0.9985944
    ## sample estimates:
    ## probability of success
    ##              0.9444444

#### <span class="header-section-number">9.3.1.3</span> Conclusie

Op basis van de exacte test besluiten we eveneens dat de parternkeuze extreem significant geassocieerd is met de omgeving (<span class="math inline">\$p&lt;0.001\$</span>). De kans op de keuze van een agressief mannetje ligt 47.1% hoger als een dwerghamster vrouwtje zich in een vijandige omgeving bevindt dan wanneer ze zich in een vriendelijke omgeving bevindt (95% BI $$28.4,65.7$$%).

### <span class="header-section-number">9.3.2</span> Ongepaarde gegevens {#ongepaarde-gegevens}

We beschouwen hier opnieuw Voorbeeld [3.16](../chap-design/index.md). Het is belangrijk om dit voorbeeld eerst grondig door te nemen alsook de Sectie rond data exploratie van categorische variabelen (Sectie [4.5](../chap-describe/index.md)).

Deze genetische associatiestudie was erop gericht om na te gaan of polymorfismen in het BRCA1 gen geassocieerd is met borstkanker. Het was een retrospectieve case-controle studie die 800 borstkankercases en 572 controles omvatte. Een R object met de data is opgeslagen in de file `brca.rda` in de dataset folder.

``` {.sourceCode .r}
load("dataset/brca.rda")
head(brca)
```

    ##    cancer variant variant2
    ## 1 control pro/pro   andere
    ## 2 control pro/pro   andere
    ## 3 control pro/pro   andere
    ## 4 control pro/pro   andere
    ## 5 control pro/pro   andere
    ## 6 control pro/pro   andere

``` {.sourceCode .r}
summary(brca)
```

    ##      cancer       variant       variant2
    ##  control:572   pro/pro:608   andere :1227
    ##  case   :800   pro/leu:619   leu/leu: 145
    ##                leu/leu:145

De dataset bevat 3 categorische variabelen: de ziekte status (factor cancer: controle vs case), brca variant (variant: wild type Pro/Pro, enkele mutatie Pro/Leu, dubbele mutatie Leu/Leu) en een factor of men de dubbele Leu/Leu mutatie bevat of niet (variant2).

Een kruistabel kan in R verkregen worden door

``` {.sourceCode .r}
brcaTab <- table(brca$variant,brca$cancer)
brcaTab
```

    ##
    ##           control case
    ##   pro/pro     266  342
    ##   pro/leu     250  369
    ##   leu/leu      56   89

Informatie omtrent het BRCA1-polymorfisme werd bekomen via DNA-analyse en staat opnieuw getabuleerd in Tabel [9.2](index.md).

| Genotype | Controles   | Cases       | Totaal    |
|:---------|:------------|:------------|:----------|
| Pro/Pro  | 266 (a)     | 342 (d)     | 608 (a+d) |
| Pro/Leu  | 250 (b)     | 369 (e)     | 619 (b+e) |
| Leu/Leu  | 56 (c)      | 89 (f)      | 145 (c+f) |
| Totaal   | 572 (a+b+c) | 800 (d+e+f) | 1372 (n)  |

<span id="tab:leu3">Tabel 9.2: </span>Kruistabel van borstkanker-status versus BRCA1-allel.

In Sectie [4.5.2](../chap-describe/index.md) zagen we reeds dat *het relatief risico* op de aandoening (d.w.z. op *case*) in de populatie voor blootgestelden versus niet-blootgestelden niet rechtstreeks kan geschat worden op basis van gegevens uit een *case-controle studie*. We zagen dat we wel een uitspraak konden doen hierover a.d.h.v. odds ratio’s, gezien het een symmetrische associatie maat is.
In voorbeeld [3.16](../chap-design/index.md) konden we daarom de odds op borstkanker berekenen voor vrouwen met allel Leu/Leu versus vrouwen zonder de dubbele mutatie als <span class="math inline">\$OR=89\\times (266+250)/(56\\times (342+369))=89\\times 512/(56 \\times 711)=1.15\$</span>. De odds op borstkanker is bijgevolg 15% hoger bij vrouwen met die specifieke allelcombinatie. We kunnen ons nu afvragen of dat verschil groot genoeg is zodat we het effect die we in de steekproef zien kunnen veralgemenen naar de populatie toe.

Hiertoe zullen we de kruistabel eerst herschrijven tot een 2x2 tabel zodat we de vrouwen met een Leu/Leu variant vergelijken met de vrouwen in de studie die niet homozygoot zijn in de mutatie<a href="#fn58" id="fnref58" class="footnoteRef"><sup>58</sup></a> (Tabel [9.3](index.md)).

``` {.sourceCode .r}
brcaTab2 <- table(brca$variant2,brca$cancer)
brcaTab2
```

    ##
    ##           control case
    ##   andere      516  711
    ##   leu/leu      56   89

| Genotype | Controles | Cases     | Totaal     |
|:---------|:----------|:----------|:-----------|
| andere   | 516 (a)   | 711 (c)   | 1227 (a+c) |
| Leu/Leu  | 56 (b)    | 89 (d)    | 145 (b+d)  |
| Totaal   | 572 (a+b) | 800 (c+d) | 1372 (n)   |

<span id="tab:leu4">Tabel 9.3: </span>Kruistabel van borstkanker-status versus Leu/Leu-variant.

### <span class="header-section-number">9.3.3</span> De Pearson Chi-kwadraat test voor ongepaarde gegevens

We zullen een toets ontwikkelen voor het testen van associatie tussen de categorische blootstelling (bvb. variant, X) en de categorische uitkomst (bvb. ziekte, Y). Concreet zullen we <span class="math display">\\$$H\_0: \\text{Er is geen associatie tussen } X \\text{ en } Y \\text{ vs } H\_1: X \\text{ en } Y \\text{ zijn geassocieerd}\\$$</span> testen.

Beschouw de rijtotalen <span class="math inline">\$n\_\\text{andere}=a+c\$</span>, <span class="math inline">\$n\_\\text{leu,leu}=b+d\$</span> enerzijds en de kolomtotalen <span class="math inline">\$n\_\\text{contr}=a+b\$</span> en <span class="math inline">\$n\_\\text{case}=c+d\$</span> anderzijds. Zij verstrekken informatie over de *marginale verdeling* van de blootstelling (bvb. variant, X) en de uitkomst (bvb. ziekte, Y), maar niet over de associatie tussen die veranderlijken. Als de nulhypothese waar is dat <span class="math inline">\$X\$</span> en <span class="math inline">\$Y\$</span> onafhankelijk zijn, dan verwacht men dat een proportie <span class="math inline">\$(b+d)/n\$</span> van <span class="math inline">\$a+b\$</span> controles met een Leu/Leu variant, of dat <span class="math inline">\$(a+b)(b+d)/n\$</span> een Leu/Leu variant hebben omdat een proportie <span class="math inline">\$(b+d)/n\$</span> van alle geobserveerde individuen een Leu/Leu variant heeft. Analoog kan men op basis van de marginale gegevens het verwachte aantal berekenen dat onder de nulhypothese in *elke cel* van de <span class="math inline">\$2\\times 2\$</span> tabel zou liggen. Dit verwachte aantal onder <span class="math inline">\$H\_0\$</span> in de <span class="math inline">\$(i,j)\$</span>-de cel (conditioneel op de marges van de tabel) wordt aangeduid met <span class="math inline">\$E\_{ij}\$</span> en is het product van het <span class="math inline">\$i\$</span>-de rijtotaal met het <span class="math inline">\$j\$</span>-de kolomtotaal gedeeld door het algemene totaal. In bovenstaand voorbeeld vinden we

- <span class="math inline">\$E\_{11}\$</span> = het verwachte aantal onder <span class="math inline">\$H\_0\$</span> in de (1,1)-cel = 1227 <span class="math inline">\$\\times\$</span> 572/1372 = 511.5 ;

- <span class="math inline">\$E\_{12}\$</span> = het verwachte aantal onder <span class="math inline">\$H\_0\$</span> in de (1,2)-cel = 1227 <span class="math inline">\$\\times\$</span> 800/1372 = 715.5 ;

- <span class="math inline">\$E\_{21}\$</span> = het verwachte aantal onder <span class="math inline">\$H\_0\$</span> in de (2,1)-cel = 145 <span class="math inline">\$\\times\$</span> 572/1372 = 60.45 ;

- <span class="math inline">\$E\_{22}\$</span> = het verwachte aantal onder <span class="math inline">\$H\_0\$</span> in de (2,2)-cel = 145 <span class="math inline">\$\\times\$</span> 800/1372 = 84.55 ;

Een toets van de nulhypothese gebeurt nu op basis van een vergelijking tussen de geobserveerde aantallen in cellen <span class="math inline">\$(i,j),\$</span> genoteerd met <span class="math inline">\$O\_{ij}\$</span> en de verwachte aantallen <span class="math inline">\$E\_{ij}\$</span>. In dat opzicht levert de toetsingsgrootheid
<span class="math display">\\$$\\begin{equation\*} X^2 = \\frac{\\left (\|O\_{11} - E\_{11}\| - .5 \\right)^2 }{ E\_{11}} + \\frac{ \\left ( \|O\_{12} - E\_{12}\| - .5 \\right)^2 }{E\_{12} }+ \\frac{ \\left ( \|O\_{21} - E\_{21}\| - .5 \\right)^2 }{E\_{21}}+ \\frac{ \\left ( \|O\_{22} - E\_{22}\| - .5 \\right)^2 }{E\_{22} } \\end{equation\*}\\$$</span>

een goede discriminatie tussen de nulhypothese en de alternatieve hypothese. Men kan aantonen dat ze onder de nulhypothese bij benadering een zogenaamde <span class="math inline">\$\\chi^2\$</span>-verdeling volgt met 1 vrijheidsgraad. Deze verdeling neemt uiteraard alleen positieve waarden aan en is scheef naar rechts verdeeld, behalve als het aantal vrijheidsgraden groot is (minstens 100), in welk geval ze meer symmetrisch wordt.

Figuur [9.5](index.md) toont haar algemene vorm.

``` {.sourceCode .r}
grid=seq(0,10,.1)
plot(grid,dchisq(grid,1),type="l",lwd=2)
dfs=c(1,2,5)
for (i in 2:3)
    lines(grid,dchisq(grid,dfs[i]),col=i,lwd=2)
legend("topright",lty=1,lwd=2,col=1:3,legend=sapply(dfs, function(d) as.expression(substitute(chi[df==val]^2,list(val=d)))))
```

<span id="fig:chidist"></span> <img src="Statistiek_2019_2020_files/figure-html/chidist-1.png" style="width:100.0%" alt="Dichtheidsfuncties voor enkele Chi-kwadraat verdelingen" />

Figuur 9.5: Dichtheidsfuncties voor enkele Chi-kwadraat verdelingen

Een grote waarde van de toetsingsgrootheid geeft een indicatie van een afwijking van de nulhypothese. Concreet zal een toets op het <span class="math inline">\$\\alpha 100\\%\$</span> significantieniveau de nulhypothese verwerpen zodra de geobserveerde waarde van de toetsingsgrootheid het <span class="math inline">\$100\\%(1-\\alpha)\$</span>-percentiel, <span class="math inline">\$\\chi^2\_{1, \\alpha}\$</span>, van de <span class="math inline">\$\\chi^2\_1\$</span>-verdeling overschrijdt. Ze kan niet verwerpen in het andere geval. De p-waarde voor een 2-zijdige toets is in dit geval de kans om een grotere waarde voor de toetsingsgrootheid te observeren dan de geobserveerde waarde <span class="math inline">\$x^2\$</span> als de nulhypothese waar is. Dit is de kans dat een <span class="math inline">\$\\chi^2\_1\$</span>-verdeelde toevalsveranderlijke waarden groter dan <span class="math inline">\$x^2\$</span> aanneemt.

``` {.sourceCode .r}
expected <- matrix(0,nrow=2,ncol=2)
for (i in 1:2)
    for (j in 1:2)
        expected[i,j] <- sum(brcaTab2[i,])*sum(brcaTab2[,j])/sum(brcaTab2)
expected
```

    ##          [,1]     [,2]
    ## [1,] 511.5481 715.4519
    ## [2,]  60.4519  84.5481

``` {.sourceCode .r}
x2 <- sum((abs(brcaTab2-expected) - .5)^2/expected)
1-pchisq(x2,1)
```

    ## [1] 0.481519

Omdat de observaties <span class="math inline">\$O\_{ij}\$</span> in feite discrete getallen zijn, kan de toetsingsgrootheid <span class="math inline">\$X^2\$</span> slechts discrete waarden aannemen en kan een continue verdeling zoals de <span class="math inline">\$\\chi^2\_1\$</span>-verdeling slechts een benadering zijn voor haar werkelijke verdeling. Om de discrete verdeling beter bij de continue <span class="math inline">\$\\chi^2\_1\$</span>-verdeling te doen aansluiten, heeft men in de uitdrukking van de toetsingsgrootheid voor elke cel telkens 0.5 afgetrokken. Dit wordt een *continuïteitscorrectie* genoemd. In dit geval gaat het om de correctie van Yates en noemt men deze toets dan ook de *Pearson Chi-kwadraat toets met Yates correctie*. Wanneer de correctie niet gebruikt wordt (d.w.z. wanneer de getallen \`0.5’ in de uitdrukking voor <span class="math inline">\$X^2\$</span> door 0 vervangen worden), dan spreekt men van de *Pearson Chi-kwadraat toets*. In R kan je deze toetsen uitvoeren door de optie op TRUE of FALSE te zetten:

``` {.sourceCode .r}
chisq.test(brcaTab2)
```

    ##
    ##  Pearson's Chi-squared test with Yates' continuity correction
    ##
    ## data:  brcaTab2
    ## X-squared = 0.49542, df = 1, p-value = 0.4815

``` {.sourceCode .r}
chisq.test(brcaTab2,correct=FALSE)
```

    ##
    ##  Pearson's Chi-squared test
    ##
    ## data:  brcaTab2
    ## X-squared = 0.62871, df = 1, p-value = 0.4278

Zelfs wanneer de continuïteitscorrectie wordt gebruikt, zal de <span class="math inline">\$\\chi^2\_1\$</span> benadering voor de verdeling van de toetsingsgrootheid slechts verantwoord zijn als in geen enkele van de cellen het verwachte aantal onder <span class="math inline">\$H\_0\$</span> kleiner is dan 5. Wanneer de <span class="math inline">\$\\chi^2\$</span>-benadering niet verantwoord is, kan men een *exacte toets* uitvoeren die rekening houdt met de echte mogelijke verdelingen van de marginale tellingen over de individuele cellen in de tabel. Dergelijke test maakt bijgevolg geen <span class="math inline">\$\\chi^2\$</span>-benadering voor de verdeling van de toetsingsgrootheid onder de nulhypothese. De test die met de exacte verdeling van de marginale tellingen over de individuele cellen rekening houdt, wordt in de literatuur *Fisher’s exact test* genoemd. De nulhypothese van deze test is eveneens dat <span class="math inline">\$X\$</span> en <span class="math inline">\$Y\$</span> onafhankelijk zijn, en de alternatieve hypothese dat <span class="math inline">\$X\$</span> en <span class="math inline">\$Y\$</span> afhankelijk zijn. Een nadeel van de exacte test, is dat ze conservatief is (d.w.z. dat ze een kleinere kans hebben op een Type I fout dan vooropgesteld, en bijgevolg een grotere kans op Type II fouten). In R bekomt men deze test als volgt:

``` {.sourceCode .r}
fisher.test(brcaTab2)
```

    ##
    ##  Fisher's Exact Test for Count Data
    ##
    ## data:  brcaTab2
    ## p-value = 0.4764
    ## alternative hypothesis: true odds ratio is not equal to 1
    ## 95 percent confidence interval:
    ##  0.7998798 1.6738449
    ## sample estimates:
    ## odds ratio
    ##   1.153279

Merk op dat deze functie tevens 95% betrouwbaarheidsintervallen rapporteert voor de bijhorende odds ratio.

#### <span class="header-section-number">9.3.3.1</span> Uitbreiding naar categorische variabelen met meerdere niveaus

Als minstens 1 van de discrete variabelen <span class="math inline">\$X\$</span> en <span class="math inline">\$Y\$</span> meer dan 2 mogelijke waarden aanneemt, kan men nagaan of de kansverdeling van <span class="math inline">\$Y\$</span> afhangt van de <span class="math inline">\$X\$</span>-waarde in de populatie door een veralgemening van de <span class="math inline">\$\\chi^2\$</span>-toets uit vorige sectie. Ook hier toetst men de nulhypothese <span class="math inline">\$H\_0: X\$</span> en <span class="math inline">\$Y\$</span> zijn onafhankelijk, ten opzichte van het tweezijdig alternatief <span class="math inline">\$H\_A: X\$</span> en <span class="math inline">\$Y\$</span> zijn niet onafhankelijk. Als de variabele voorgesteld op de rijen <span class="math inline">\$r\$</span> mogelijke uitkomsten heeft en die op de kolommen <span class="math inline">\$c\$</span> mogelijke uitkomsten, dan noemt men de kruistabel die <span class="math inline">\$X\$</span> tegenover <span class="math inline">\$Y\$</span> uitzet, een <span class="math inline">\$r \\times c\$</span> tabel.

Zoals voorheen vergelijkt men het aantal geobserveerde waarden in cel <span class="math inline">\$(i,j)\$</span>, <span class="math inline">\$O\_{ij}\$</span> genoteerd, met het aantal verwachte waarden onder de nulhypothese in deze cel, <span class="math inline">\$E\_{ij}\$</span> genoemd, op basis van de marginale totalen. Net als voorheen is <span class="math inline">\$E\_{ij}\$</span> het product van het <span class="math inline">\$i\$</span>-de rijtotaal met het <span class="math inline">\$j\$</span>-de kolomtotaal gedeeld door het algemene totaal. De toetsingsgrootheid is nu <span class="math display">\\$$\\begin{equation\*} X^2 = \\sum\_{ij} \\frac{\\left (O\_{ij} - E\_{ij}\\right)^2 }{ E\_{ij}} \\end{equation\*}\\$$</span>

Men kan aantonen dat ze een Chi-kwadraat verdeling volgt met <span class="math inline">\$(r-1) \\times (c-1)\$</span> vrijheidsgraden als de nulhypothese waar is. De continuïteitscorrectie wordt meestal niet gebruikt bij meer dan 2 rijen of kolommen.

We voeren nu de test uit voor het BRCA voorbeeld waarbij we nu gebruik maken van alle varianten

``` {.sourceCode .r}
chisq.test(brcaTab)
```

    ##
    ##  Pearson's Chi-squared test
    ##
    ## data:  brcaTab
    ## X-squared = 2.0551, df = 2, p-value = 0.3579

Om te onderzoeken of het BRCA1 gen geassocieerd is met borstkanker, berekenen we de Pearson chi-kwadraat toets voor de case-controle studie uit Tabel [9.2](index.md). De toetsingsgrootheid bedraagt nu 2.055 en volgt een Chi-kwadraat verdeling met 2 vrijheidsgraden. De kans dat zo’n <span class="math inline">\$\\chi^2\$</span>- verdeelde toevalsveranderlijke extremer is dan 2.055, bedraagt 36%. Op het 5% significantieniveau kunnen we dus niet besluiten dat het BRCA1 gen geassocieerd is met borstkanker.

De **Pearson <span class="math inline">\$\\chi^2\$</span> test** wordt gebruikt om te toetsen of er een associatie is tussen 2 kwalitatieve (mogelijks niet binaire) variabelen, i.h.b. om te toetsen of de verdeling<a href="#fn59" id="fnref59" class="footnoteRef"><sup>59</sup></a> van de ene kwalitatieve variabele verschilt alnaargelang de waarde van de andere kwalitatieve variabele. Ze vereist dat de 2 metingen voor de 2 kwalitatieve variabelen telkens bekomen werden van onafhankelijke subjecten, en dat minstens 80% van de cellen in de overeenkomstige kruistabel een verwacht aantal observaties van minstens 5 bezitten. Op die manier vormt ze het analogon van de one-way variantie-analyse voor kwalitatieve i.p.v. continue variabelen.

---

[← 9.2 Toetsen voor een proportie](02-9-2-toetsen-voor-een-proportie.md) · [Up: contents](index.md) · [9.4 Logistische regressie →](04-9-4-logistische-regressie.md)

---
title: Hoofdstuk 8 Niet-parametrische statistiek
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/niet-parametrische-statistiek.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/niet-parametrische-statistiek.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Hoofdstuk 8 Niet-parametrische statistiek

**Source:** [`niet-parametrische-statistiek.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/niet-parametrische-statistiek.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## <span class="header-section-number">8.1</span> Inleiding {#inleiding}

Alle methoden die in de vorige hoofdstukken behandeld werden, zijn zogenaamde parametrische methoden. Deze term duidt erop dat de geldigheid van de inferentie enkel correct is als er voldaan is aan parametrische veronderstellingen. Dit zijn voornamelijk de distributionele veronderstellingen, zoals dat de observaties normaal verdeeld zijn. Andere voorbeelden van een parametrische veronderstelling zijn de gelijkheid van varianties bij de two-sample <span class="math inline">\$t\$</span>-test en ANOVA en de lineariteit van een regressiemodel.

Wanneer we over statistische besluitvorming spreken, is bijvoorbeeld de <span class="math inline">\$p\$</span>-waarde van een statistische test, of de probabilistische interpretatie van een betrouwbaarheidsinterval enkel correct interpreteerbaar onder bepaalde veronderstellingen:

- De <span class="math inline">\$p\$</span>-waarde is de kans dat de teststatistiek <span class="math inline">\$T\$</span> onder de nulhypothese meer extreem is dan de waargenomen waarde <span class="math inline">\$t\$</span> (gegeven dat <span class="math inline">\$H\_0\$</span> waar is). Die kans wordt berekend op basis van de nuldistributie van <span class="math inline">\$T\$</span>. Deze distributie wordt bij parametrische testen afgeleid door te steunen op veronderstellingen over de verdeling van de observaties. Indien er niet voldaan is aan deze veronderstellingen, is de berekende <span class="math inline">\$p\$</span>-waarde fout. Dit betekent dat de conclusies die op <span class="math inline">\$p\$</span> gebaseerd worden, eveneens mogelijks fout kunnen zijn.

- De berekening van bv. een <span class="math inline">\$95\\%\$</span> betrouwbaarheidsinterval steunt eveneens op distributionele veronderstellingen. Als er niet voldaan is aan de veronderstellingen, is er geen garantie meer dat de berekende intervallen de (correcte) interpretatie hebben dat dergelijke intervallen de juiste parameterwaarde omvatten met <span class="math inline">\$95\\%\$</span> kans.

Asymptotische theorie is misschien moeilijker te plaatsen onder parametrisch of niet-parametrisch. Je zou kunnen stellen dat bv. een <span class="math inline">\$t\$</span>-test asymptotisch niet-parametrisch is, omdat bij erg grote steekproefgroottes de distributionele veronderstelling van normaliteit niet meer belangrijk is.

De reden waarom we in deze cursus een focus hebben op parametrische methoden is omdat ze efficiënter en meer flexibel zijn wanneer er aan de voorwaarden voldaan is. Efficiëntie betekent dat bij een constante steekproefgrootte de testen een grotere power hebben en dat de betrouwbaarheidsintervallen smaller zijn. Met meer flexibel bedoelen we dat het eenvoudiger is om de methoden in te zetten voor experimenten met meer complexe designs. Als er niet voldaan is aan de veronderstellingen van de parameterische methoden kunnen we voor bepaalde designs overschakelen naar niet-parametrische methoden die in deze situatie nog steeds formeel geldig zijn.

## <span class="header-section-number">8.2</span> Vergelijken van twee groepen

### <span class="header-section-number">8.2.1</span> Cholestorol voorbeeld

In een studie werd de cholestorolconcentratie in het bloed gemeten bij 5 patiënten (groep=1) die twee dagen geleden een hartaanval hadden en bij 5 gezonde personen (groep=2). De onderzoekers wensen na te gaan of de cholestorolconcentratie verschillend is bij hartpatiënten en gezonde personen. Boxplots van de data worden weergegeven in Figuur [8.1](index.md).

``` {.sourceCode .r}
chol <- read.table("dataset/chol.txt",header=TRUE)
chol$group <- as.factor(chol$group)
head(chol)
```

    ##   group cholest
    ## 1     1     244
    ## 2     1     206
    ## 3     1     242
    ## 4     1     278
    ## 5     1     236
    ## 6     2     188

``` {.sourceCode .r}
boxplot(cholest~group,data=chol,ylab="cholestorol (mg/dl)",outline=FALSE,ylim=range(chol$cholest))
set.seed(10)
stripchart(cholest~group,data=chol, vertical = TRUE, method = "jitter", pch = 19, col =c("bisque","coral"),  add = TRUE)
set.seed(10)
stripchart(cholest~group,data=chol, vertical = TRUE, method = "jitter", pch = 1,  add = TRUE)
```

<span id="fig:cholBox"></span> <img src="Statistiek_2019_2020_files/figure-html/cholBox-1.png" style="width:100.0%" alt="Boxplot van de cholesterol concentratie in het bloed bij hartpatiënten (groep 1) en gezonde individuen (groep 2)." />

Figuur 8.1: Boxplot van de cholesterol concentratie in het bloed bij hartpatiënten (groep 1) en gezonde individuen (groep 2).

``` {.sourceCode .r}
nGroups=table(chol$group)
n=sum(nGroups)
```

De boxplots geven aan dat er mogelijks outliers in de data voorkomen. Het is moeilijk om inzicht te krijgen in de verdeling van de data gezien we maar 5 observaties hebben per groep.

### <span class="header-section-number">8.2.2</span> Permutatietesten

De vraagstelling van het cholestorol voorbeeld is geformuleerd in erg ruime bewoordingen en dit laat vrijheid in de vertaling ervan naar een nulhypothese.

Laten we starten met een nulhypothese in termen van gemiddelden. Stel dat <span class="math inline">\$\\mu\_1\$</span> en <span class="math inline">\$\\mu\_2\$</span> de gemiddelde uitkomsten in behandelingsgroep 1 (hartpatiënten) en 2 (gezonde personen) voorstellen, dan zouden de hypotheses kunnen zijn: <span class="math display">\\$$H\_0: \\mu\_1=\\mu\_2 \\text{ versus } H\_1: \\mu\_1\\neq \\mu\_2.\\$$</span>

Voor het testen van deze hypotheses kunnen we bijvoorbeeld gebruik maken van de two-sample <span class="math inline">\$t\$</span>-test.

We gaan de voorwaarden na:

- Normaliteit van de uitkomsten in de twee behandelingsgroepen. Met slechts 5 observaties in iedere groep, kan de veronderstelling niet nagegaan worden.
- Gelijkheid van varianties. Met slechts 5 observaties in iedere groep, kan de veronderstelling niet nagegaan worden.

We kunnen dus de veronderstellingen van de two-sample <span class="math inline">\$t\$</span>-test niet nagaan. We kunnen ook geen beroep doen op de asymptotische benadering omdat 5 observaties per groep te weinig is.

Samengevat: de veronderstellingen van de <span class="math inline">\$t\$</span>-test kunnen niet worden nagegaan en er zijn te weinig observaties om gebruik te kunnen maken van de asymptotische benadering. Aangezien het erg gevaarlijk is een statistische methode te gebruiken waarvan de voorwaarden niet nagegaan kunnen worden, is de klassieke <span class="math inline">\$t\$</span>-test niet de geschikte methode. De oplossing die in dit hoofdstuk besproken wordt, zijn permutatietesten. Om deze te kunnen beschrijven, zullen we eerst de nulhypothese anders formuleren.

#### <span class="header-section-number">8.2.2.1</span> Hypothesen

De oplossing die in deze sectie besproken wordt, zijn de permutatietesten. Om deze te kunnen beschrijven, zullen we eerst de nulhypothese anders formuleren.

De veronderstelling voor de two-sample <span class="math inline">\$t\$</span>-test kunnen we als volgt schrijven, met <span class="math inline">\$Y\_{1j}\$</span> en <span class="math inline">\$Y\_{2j}\$</span> de notatie voor de uitkomsten uit respectievelijk groep 1 en 2: <span class="math display">\\$$Y\_{1j} \\text{ iid } N(\\mu\_1,\\sigma^2) \\;\\;\\;\\text{ en }\\;\\;\\; Y\_{2j} \\text{ iid } N(\\mu\_2,\\sigma^2).\\$$</span> Onder <span class="math inline">\$H\_0:\\mu\_1=\\mu\_2\$</span>, wordt dit (stel <span class="math inline">\$\\mu=\\mu\_1=\\mu\_2\$</span> onder <span class="math inline">\$H\_0\$</span>) <span class="math display">\\$$ Y\_{ij} \\text{ iid } N(\\mu,\\sigma^2),\\$$</span>

wat uitdrukt dat alle <span class="math inline">\$n=n\_1+n\_2\$</span> uitkomsten uit dezelfde normale distributie komen en onafhankelijk verdeeld zijn. Dit laat ons dus toe om de oorspronkelijke nulhypothese van de two-sample <span class="math inline">\$t\$</span>-test anders te schrijven: <span id="eq:H0F1F2" class="math display">\\$$\\begin{equation} H\_0: F\_1(y) = F\_2(y) \\text{ voor alle } y \\;\\;\\;\\text{ of }\\;\\;\\; H\_0: f\_1(y) = f\_2(y) \\text{ voor alle } y \\tag{8.1} \\end{equation}\\$$</span>

met <span class="math inline">\$F\_1\$</span> en <span class="math inline">\$F\_2\$</span> de distributiefuncties en <span class="math inline">\$f\_1\$</span> en <span class="math inline">\$f\_2\$</span> de densiteitfuncties van de verdeling van de uitkomsten in respectievelijk behandelingsgroep 1 en 2, en met de bijkomende veronderstelling dat <span class="math inline">\$f\_1\$</span> en <span class="math inline">\$f\_2\$</span> de distributiefuncties van Normale verdelingen zijn.

Onder de alternatieve hypothese wordt een locatie-shift verondersteld: <span class="math display">\\$$H\_1: f\_1(y)=f\_2(y-\\Delta) \\;\\;\\;\\text{ voor alle } y\\$$</span> met <span class="math inline">\$\\Delta=\\mu\_1-\\mu\_2\$</span>, verder hebben de Normale verdelingen dezelfde variantie.

We illustreren dit in R voor <span class="math inline">\$f\_1\\sim N(0,1)\$</span> en <span class="math inline">\$f\_2\\sim N(1,1)\$</span> en <span class="math inline">\$\\Delta=-1\$</span>.

``` {.sourceCode .r}
mu1 <- 0
sigma1 <- 1
mu2 <- 1
sigma2 <- 1
y <- -2:2
delta <- mu1-mu2
delta
```

    ## [1] -1

``` {.sourceCode .r}
dnorm(y,mu1,sigma1)
```

    ## [1] 0.05399097 0.24197072 0.39894228 0.24197072 0.05399097

``` {.sourceCode .r}
dnorm(y-delta,mu2,sigma2)
```

    ## [1] 0.05399097 0.24197072 0.39894228 0.24197072 0.05399097

De permutatietesten die in de volgende sectie ontwikkeld worden, kunnen gebruikt worden voor het testen van de hypothese [(8.1)](index.md), maar dan zonder de Normaliteitsveronderstelling.

We schrijven hypothese [(8.1)](index.md) verkort als <span class="math display">\\$$ H\_0: F\_1=F\_2 \\;\\;\\;\\text{ of }\\;\\;\\; H\_0:f\_1=f\_2. \\$$</span>

Als de nulhypothese waar is, met name dat de verdelingen van de cholestorolconcentraties gelijk zijn voor hartpatiënten en gezonde personen, dan zijn de groep-labels van de 10 personen niet informatief. Gezien er geen verschil is in de verdeling tussen beide groepen is elke groepering immers irrelevant. We kunnen bijgevolg de verdeling van de test-statistiek onder de nulhypothese bekomen door de groepslabels <span class="math inline">\$G\$</span> te permuteren.

#### <span class="header-section-number">8.2.2.2</span> Verdeling van de statistiek onder <span class="math inline">\$H\_0\$</span>

In praktijk zijn er <span class="math inline">\$m=\\binom{n\_1+n\_2}{n\_1}=\\binom{n}{n\_1}=\\binom{n}{n\_2}\$</span> mogelijke unieke permutaties <span class="math inline">\$\\cal{G}\$</span> van de groepslabels. Voor ons voorbeeld zijn dat er <span class="math inline">\$m=\$</span> 252. Als <span class="math inline">\$m\$</span> niet te groot is dan kunnen alle unieke permutaties van de groepslabels berekend worden. Voor iedere unique permutatie <span class="math inline">\$g \\in \\cal{G}\$</span> wordt de teststatistiek <span class="math inline">\$t^\*\_g\$</span> berekend<a href="#fn51" id="fnref51" class="footnoteRef"><sup>51</sup></a>.

We kunnen alle m=252 permutaties in R genereren a.d.h.v. de functie `combn(n,n_1)`. Dit wordt geïllustreerd in de onderstaande R code:

``` {.sourceCode .r}
G=combn(n,nGroups[1])
dim(G)
```

    ## [1]   5 252

``` {.sourceCode .r}
G[,1:10]
```

    ##      [,1] [,2] [,3] [,4] [,5] [,6] [,7] [,8] [,9] [,10]
    ## [1,]    1    1    1    1    1    1    1    1    1     1
    ## [2,]    2    2    2    2    2    2    2    2    2     2
    ## [3,]    3    3    3    3    3    3    3    3    3     3
    ## [4,]    4    4    4    4    4    4    5    5    5     5
    ## [5,]    5    6    7    8    9   10    6    7    8     9

De matrix G bevat voor elke permutatie de volgnummers van de observaties die tot de eerste groep zullen behoren. We tonen enkel de eerste 10 permutaties. We kunnen nu de teststatistiek berekenen voor de originele steekproef en voor elke permutatie

``` {.sourceCode .r}
#Originele test statistiek
tOrig=t.test(cholest~group,chol)$statistic
#bereken alle permutatiecombinaties en voer voor
#elke combinantie een functie uit die de t-test statistiek
#berekent voor de gepermuteerde groepslabels
tStar=combn(n,nGroups[1], function(g,y=chol$cholest) t.test(y[g],y[-g])$statistic)
head(tStar)
```

    ## [1] 3.6644253 1.6397911 2.3973923 1.5876250 1.9217173 0.9967105

``` {.sourceCode .r}
length(tStar)
```

    ## [1] 252

Merk op dat `y[g]` de data selecteert met volgnummers g uit de vector y en `y[-g]` de data waarvoor de volgnummers niet tot g behoren. De vector `tStar` bevat de waarden van de teststatistiek <span class="math inline">\$t^\*\_g\$</span> voor alle <span class="math inline">\$g \\in {\\cal{G}}\$</span>.

We kunnen een frequentietabel van de teststatistiek verkrijgen en de unieke resultaten uitzetten in een plot of er een histogram van maken.

``` {.sourceCode .r}
tab=table(tStar)
head(tab)
```

    ## tStar
    ## -4.17457930205164 -3.66442526456221 -3.14250320139171 -2.64368173056088
    ##                 1                 1                 1                 1
    ## -2.55798397117996 -2.39739232497298
    ##                 1                 1

``` {.sourceCode .r}
par(mfrow=c(2,1))
plot(table(tStar),xaxt="n",ylab="Frequency",
     xlab=expression("permutatiestatistiek t"^"*"))
axis(1,at=seq(-4,4,1))
abline(v=tOrig,col=2,lwd=2)
hist(tStar,ylab="Frequency",
     xlab=expression("permutatiestatistiek t"^"*"))
abline(v=tOrig,col=2,lwd=2)
```

<span id="fig:tPermDist"></span> <img src="Statistiek_2019_2020_files/figure-html/tPermDist-1.png" style="width:100.0%" alt="Exacte permutatie nuldistributie van de Welch t-test voor het cholestorol voorbeeld. Bovenaan histogram van elke mogelijke waarde voor de test-statistiek. Onderaan een gewoon histogram met balkbreedtes gelijk aan 1. De geobserveerde waarde voor de test-statistiek is aangeduid met een rode verticale lijn." />

Figuur 8.2: Exacte permutatie nuldistributie van de Welch t-test voor het cholestorol voorbeeld. Bovenaan histogram van elke mogelijke waarde voor de test-statistiek. Onderaan een gewoon histogram met balkbreedtes gelijk aan 1. De geobserveerde waarde voor de test-statistiek is aangeduid met een rode verticale lijn.

De frequentietabel of het histogram (Figuur [8.2](index.md)) bevat alle informatie voor de permutatienuldistributie van de two-sample <span class="math inline">\$t\$</span>-teststatistiek voor de geobserveerde uitkomsten; merk op dat er 110 unieke waarden van de teststatistiek berekend zijn.
Het histogram in Figuur [8.2](index.md) is de verdeling van de teststatistiek onder de nulhypothese. We zien eveneens dat de geobserveerde teststatistiek vrij extreem is.

#### <span class="header-section-number">8.2.2.3</span> p-waarde

Nu we in staat zijn de permutatienuldistributie te berekenen, kunnen we hypothesetesten uitvoeren net als in de parametrische statistiek. Voor een permutatietest is de <span class="math inline">\$p\$</span>-waarde voor de tweezijdige test (immers <span class="math inline">\$H\_1: \\mu\_1 \\neq \\mu\_2\$</span>) <span class="math display">\\$$p=\\text{P}\_0\\left\[\\vert T\\vert \\geq \\vert t\\vert \\mid \\mathbf{y}\\right$$.\\\]</span>

Merk op dat deze p-waarde geconditioneerd is op de geobserveerde cholestorolwaarden die weergegeven worden in de vector <span class="math inline">\$\\mathbf{y}=(y\_{11},\\ldots,y\_{51},y\_{12},\\ldots,y\_{52})^T\$</span>.

Aangezien de permutatienuldistrubutie van <span class="math inline">\$T\$</span> bepaald wordt door <span class="math inline">\$t^\*\_g\$</span>, <span class="math inline">\$g \\in{\\cal{G}}\$</span>, berekenen we <span class="math display">\\$$p = \\text{P}\_0\\left\[\\left\\vert T\\right\\vert \\geq \\left\\vert t\\right\\vert \\mid \\mathbf{y}\\right$$ = \\frac{\\#\\{g\\in {\\cal{G}}: \\vert t^\*\_g\\vert \\geq \\vert t \\vert \\}}{m},\\\]</span>

m.a.w. als de ratio van het aantal permutaties waarvoor de statistiek minstens even extreem is als de geobserveerde statistiek op het totaal aantal permutaties. In R kunnen we dit als volgt berekenen.

``` {.sourceCode .r}
pval=mean(abs(tStar)>=abs(tOrig))
pval
```

    ## [1] 0.01587302

We vinden dus een <span class="math inline">\$p\$</span>-waarde van 0.0159. Aangezien <span class="math inline">\$p&lt;5\\%\$</span>, besluiten we op het <span class="math inline">\$5\\%\$</span> significantieniveau dat de distributies van de cholestorol concentraties niet gelijk zijn bij hartpatiënten en bij gezonde personen. De <span class="math inline">\$p\$</span>-waarde die gevonden wordt via de permutatienuldistributie op basis van alle permutaties wordt een **exacte** <span class="math inline">\$p\$</span>-waarde genoemd. De permutatienuldistributie wordt een **exacte** nuldistributie genoemd. De term **exact** betekent dat de resultaten correct zijn voor iedere steekproefgrootte <span class="math inline">\$n\$</span>.

#### <span class="header-section-number">8.2.2.4</span> Kritieke waarde {#kritieke-waarde}

Ook de kritieke waarde <span class="math inline">\$c\$</span> voor de test op het <span class="math inline">\$\\alpha\$</span> significantieniveau kan eenvoudig bekomen worden. <span class="math display">\\$$ \\text{P}\_0\\left\[\\vert T\\vert&gt; c \\mid \\mathbf{y}\\right$$ =\\alpha. \\\]</span> Gezien de discrete natuur van de permutatienuldistributie van <span class="math inline">\$T\$</span>, is het onwaarschijnlijk om een kritieke waarde te vinden zodat deze gelijkheid exact opgaat. Daarom zoeken we de kleinste waarde <span class="math inline">\$c\$</span> zodat <span class="math display">\\$$ \\text{P}\_0\\left\[\\vert T\\vert&gt; c \\mid \\mathbf{y}\\right$$ \\leq \\alpha. \\\]</span> Dit impliceert dat een permutatietest mogelijks conservatief is, maar meestal is <span class="math inline">\$m\$</span> voldoende groot zodat de kans op een type I fout (<span class="math inline">\$\\text{P}\_{0}\\left$$ \\vert T \\vert &gt; c \\mid \\mathbf{y}\\right$$\$</span>) erg dicht bij het nominale significantieniveau ligt.

``` {.sourceCode .r}
alpha<-0.05
m <- length(tStar)
t.crit<-sort(abs(tStar))[ceiling((1-alpha)*m)]
t.crit
```

    ## [1] 2.179236

``` {.sourceCode .r}
mean(abs(tStar)>t.crit)
```

    ## [1] 0.04761905

De kans op een type I fout wordt dus gecontroleerd door een permutatietest, maar wel conditioneel op de geobserveerde uitkomsten data <span class="math inline">\$\\mathbf{y}\$</span>.

We hebben steeds geconditioneerd op de observaties van de steekproef. **We kunnen ons nu afvragen of we de conclusies kunnen veralgemenen naar de populatie toe? Het antwoord is ja, als de subjecten at random getrokken zijn uit de populatie.** Het bewijs hiervan valt buiten het bestek van de cursus.

Soms treedt er een praktisch probleem op omdat het aantal permutaties <span class="math inline">\$m=\\#{\\cal{G}}\$</span> erg groot is. Enkele voorbeelden: <span class="math inline">\$\\binom{20}{10}=\$</span> 184756, <span class="math inline">\$\\binom{30}{15}=\$</span> 1.55e+08 en <span class="math inline">\$\\binom{40}{20}=\$</span> 1.38e+11. Dus zelfs met slechts 40 observaties en een gebalanceerde proefopzet is het quasi onmogelijk om alle permutaties één voor één door te rekenen. De oplossing bestaat erin om niet alle <span class="math inline">\$g \\in {\\cal{G}}\$</span> te beschouwen, maar slechts een beperkt aantal (bv. 10000 of 100000). We kunnen m.a.w. de nuldistributie benaderen door een groot aantal random permutaties uit te voeren. We illustreren dit principe voor ons voorbeeld waar we in alle permutaties door konden rekenen en de exacte p-waarde kennen.

Merk op dat wanneer men een aantal random permutaties genereert de p-waarde lichtjes anders wordt berekend. Als men niet alle permutaties uitvoert, kan het dat de geobserveerde statistiek niet berekend wordt in de permutaties die worden beschouwd. Als de statistiek erg extreem is, dan kan het voorkomen dat de de statistiek groter is dan alle statistieken die in de permutaties werden berekend. Als we de p-waarde dan berekenen zoals voor de exacte p-waarde, dan kan het voorkomen dat de approximatieve p-waarde op basis van het aantal random permutatries gelijk is aan nul. Dat is theoretisch niet mogelijk omdat de geobserveerde waarde voor de teststatistiek ten minste 1 keer dient te worden behaald in de permutatiedistributie. Daarom wordt de p-waarde op basis van B willekeurige permutaties vaak berekend als <span class="math display">\\$$p=\\frac{\\#\\{\\vert t^\*\_g\\vert \\geq \\vert t \\vert \\}+1}{B+1},\\$$</span> zodat ze nooit nul wordt.

``` {.sourceCode .r}
set.seed(304)
B=10000
tStar2=sapply(X=1:B, FUN=function(b,y,groep) {t.test(y~sample(groep))$statistic},y=chol$cholest,groep=chol$group)
#een for lus is niet efficient mbt tot
#geheugengebruik in R daarom gebruikt men beter
#de sapply functie.

---

[Up: contents](index.md) · [argument X: een vector of lijst →](02-argument-x-een-vector-of-lijst.md)

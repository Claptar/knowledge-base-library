---
title: 9.2 Toetsen voor een proportie
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-categorisch.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-categorisch.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 9.2 Toetsen voor een proportie

**Source:** [`chap-categorisch.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-categorisch.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

In Saksen werd een studie opgezet binnen een vrij gesloten populatie mensen (weinig immigratie en emigratie) om te bepalen hoe waarschijnlijk het was dat een ongeboren kind mannelijk is.

``` {.sourceCode .r}
boys <- 3175
n <- 6155
```

Op 6155 ongeboren kinderen werden 3175 jongens geobserveerd. We wensen na te gaan of er een verschil is in de kans dat het ongeboren kind een jongen is of een meisje. In het vervolg van deze sectie vatten we deze gegevens op als uitkomsten van een numerieke toevalsveranderlijke <span class="math inline">\$X\$</span> met uitkomst 1 voor jongens en 0 voor meisjes. Merk op dat we hier met een zogenaamd telprobleem te maken hebben omdat de uitkomst een telling (nl. het aantal jongens) voorstelt.

Formeel hebben we nu een populatie van ongeboren kinderen beschouwd waarin elk individu gekenmerkt wordt door een 0 of een 1. De uitkomst variabele is dus binair. Binaire data kan worden gemodelleerd a.d.h.v. een Bernoulli verdeling: <span class="math display">\\$$X\_i \\sim B(\\pi) \\text{ met}\\$$</span> <span class="math display">\\$$B(\\pi)=\\pi^{X\_i}(1-\\pi)^{(1-X\_i)},\\$$</span> een distributie met 1 model parameter <span class="math inline">\$\\pi\$</span>. <span class="math inline">\$\\pi\$</span> is de verwachte waarde van <span class="math inline">\$X\_i\$</span>: <span class="math display">\\$$\\text{E}\[X\_i$$=\\pi,\\\]</span> de proportie van ongeboren jongens (d.i. kinderen met een 1) in de populatie. Bijgevolg is <span class="math inline">\$\\pi\$</span> ook de kans dat een lukraak getrokken individu een jongen is (een observatie die 1 oplevert).

De variantie van Bernoulli data is eveneens gerelateerd aan de kans <span class="math inline">\$\\pi\$</span>. <span class="math display">\\$$\\text{Var}\[X\_i$$=\\pi (1-\\pi).\\\]</span>

Een grafische weergave van enkele Bernoulli kansverdelingen wordt weergegeven in Figuur [9.1](index.md).

``` {.sourceCode .r}
par(mfrow=c(1,3))
probs=c(0.25,.5,.75)
for (i in 1:length(probs))
{
plot(c(0,1),c(1-probs[i],probs[i]),ylim=c(0,1),type="h",xaxt="n",xlab="X",ylab="Kans (Dichtheid)",main= as.expression(substitute(pi == val,list(val=probs[i]))),lwd=3)
axis(1,at=c(0,1))
}
```

<span id="fig:bernoulli"></span> <img src="Statistiek_2019_2020_files/figure-html/bernoulli-1.png" style="width:100.0%" alt="Bernoulli verdelingen." />

Figuur 9.1: Bernoulli verdelingen.

In het voorbeeld werden lukraak 6155 observaties getrokken uit de populatie. We kunnen <span class="math inline">\$\\pi\$</span> schatten op basis van de data d.m.v. het steekproefgemiddelde van de binaire data: <span class="math display">\\$$\\hat \\pi = \\bar X = \\frac{\\sum\\limits\_{i=1}^n X\_i}{n},\\$$</span>

``` {.sourceCode .r}
pi=boys/n
pi
```

    ## [1] 0.5158408

In ons voorbeeld is <span class="math inline">\$\\bar x =\$</span> 3175 / 6155 = 51.6%.

### <span class="header-section-number">9.2.1</span> Binomiale test {#binomiale-test}

De vraag stelt zich nu of het feit dat 51.6% van de kinderen in de studie mannelijk zijn, voldoende overtuigingskracht draagt om te beweren dat er meer kans is dat een ongeboren kind een jongen is dan een meisje. Met andere woorden, we wensen op basis van deze observaties statistisch te toetsen of de kans <span class="math inline">\$\\pi\$</span> al dan niet gelijk is aan 50%. Om een toets te kunnen construeren van de nulhypothese dat <span class="math display">\\$$H\_0: \\pi=1/2 \\text{ versus } H\_1: \\pi\\neq 1/2,\\$$</span> moeten we de verdeling van de gegevens <span class="math inline">\$X\$</span> en van de proportie <span class="math inline">\$\\bar X\$</span> (of equivalent de som <span class="math inline">\$S=n\\bar X\$</span>) kennen.

Stel dat het voorkomen van jongens en meisjes in de populatie even waarschijnlijk zijn; m.a.w. stel dat de nulhypothese waar is. Bij lukrake trekking van één individu uit de populatie is de kans dat men een jongen observeert dan gelijk aan <span class="math inline">\$P(X=1) = \\pi = 1/2.\$</span> Als twee kinderen onafhankelijk van elkaar getrokken worden (en de populatie is bij benadering oneindig groot) dan heeft zowel het eerste als het tweede kind kans 1/2 om mannelijk te zijn (onafhankelijk van elkaar). De uitkomsten <span class="math inline">\$(x\_1, x\_2)\$</span> voor beide kinderen hebben dan 4 mogelijke waarden: <span class="math inline">\$(0,0), (0,1),(1,0)\$</span> en <span class="math inline">\$(1,1).\$</span> Deze komen elk voor met kans <span class="math inline">\$1/4 = 1/2 \\times 1/2\$</span>. Bijgevolg kan de toevalsveranderlijke <span class="math inline">\$S\$</span> die de som van de uitkomsten weergeeft, de volgende waarden aannemen:

| <span class="math inline">\$(x\_1,x\_2)\$</span> | <span class="math inline">\$s\$</span> | <span class="math inline">\$P(S = s)\$</span> |
|:--:|:--:|:--:|
| (0,0) | 0 | 1/4 |
| (0,1), (1,0) | 1 | 1/2 |
| (1,1) | 2 | 1/4 |

In het algemeen, als men <span class="math inline">\$n\$</span> onafhankelijke observaties trekt telkens met kans <span class="math inline">\$\\pi\$</span> op “succes” (uitkomst 1), dan kan het totaal aantal successen <span class="math inline">\$S\$</span> (of de som van alle 1-en), <span class="math inline">\$n+1\$</span> mogelijke waarden hebben. Men kan aantonen dat elke waarde <span class="math inline">\$k\$</span> tussen 0 en <span class="math inline">\$n\$</span> dan de volgende kans op voorkomen heeft: <span id="eq:binomk" class="math display">\\$$\\begin{equation} P(S=k) = \\left ( \\begin{array}{c} n \\\\ k \\\\ \\end{array} \\right ) \\pi^k (1-\\pi)^{n-k} \\tag{9.1} \\end{equation}\\$$</span> waarbij <span class="math inline">\$1-\\pi\$</span> de kans is op mislukking in 1 enkele trekking (uitkomst met 0 genoteerd) en <span class="math inline">\$\\left(\\begin{array}{c} n \\\\ k \\\\ \\end{array}\\right)\$</span> de binomiaalcoëfficient<a href="#fn55" id="fnref55" class="footnoteRef"><sup>55</sup></a>
<span class="math display">\\$$\\begin{equation\*} \\left ( \\begin{array}{c} n \\\\ k \\\\ \\end{array} \\right ) = \\frac{n \\times (n-1) \\times ...\\times (n-k+1) }{ k!} = \\frac{ n!}{ k!(n-k)! } \\end{equation\*}\\$$</span>

is, waarbij <span class="math inline">\$0!=1!=1\$</span>.

In R kan je die kansen opvragen met behulp van het commando `dbinom(k,n,p)`.

Een toevalsveranderlijke <span class="math inline">\$S\$</span> met een kansverdeling zoals in Model [(9.1)](index.md) noemt men een *Binomiaal verdeelde toevalsveranderlijke*. De bijhorende kansverdeling is de *Binomiale kansverdeling* met parameters <span class="math inline">\$n\$</span> (d.i. het aantal trekkingen of, equivalent, de maximale uitkomstwaarde) en <span class="math inline">\$\\pi\$</span> (de kans op een \`succes’ bij elke trekking). Ze kan gebruikt worden om te berekenen wat de kans is dat er zich op een vast totaal van <span class="math inline">\$n\$</span> onafhankelijke experimenten <span class="math inline">\$k\$</span> gebeurtenissen van een bepaald type voordoen, als je weet dat de kans dat zich 1 zo’n gebeurtenis voordoet op 1 experiment, <span class="math inline">\$\\pi\$</span> bedraagt. De Binomiale kansverdeling wordt vooral gebruikt voor de analyse van gegevens die slechts 2 mogelijke waarden kunnen aannemen. Dergelijke gegevens komen vaak voor in wetenschappelijk onderzoek (bijvoorbeeld: al dan niet besmet met HIV, wild type van een gen vs een mutant,…). Kennis van de Binomiale verdeling kan dan helpen om proporties of risico’s op een gebeurtenis van een bepaald type te vergelijken tussen verschillende groepen. Een grafische weergave van enkele Binomiale kansverdelingen is gegeven in Figuur [9.2](index.md).

``` {.sourceCode .r}
par(mfrow=c(2,2))
probs=c(0.25,.5,.75)
for (i in 1:length(probs))
{
plot(0:10,dbinom(0:10,prob=probs[i],size=10),ylim=c(0,1),type="h",xlab="X",ylab="Kans (Dichtheid)",main= as.expression(substitute(pi == val,list(val=paste(probs[i],", nobs=10")))),lwd=3)
}
plot(2925:3225,dbinom(2925:3225,prob=.5,size=n),type="h",xlab="X",ylab="Kans (Dichtheid)",main= as.expression(substitute(pi == val,list(val=paste0("0.5, nobs=",n)))))
```

<span id="fig:binoms"></span> <img src="Statistiek_2019_2020_files/figure-html/binoms-1.png" style="width:100.0%" alt="Binomiale verdelingen." />

Figuur 9.2: Binomiale verdelingen.

Om nu te toetsen of <span class="math inline">\$\\pi=1/2\$</span> versus het alternatief dat <span class="math inline">\$\\pi\\neq 1/2\$</span>, is een voor de hand liggende toetsstatistiek <span class="math inline">\$\\bar X-1/2\$</span> of, equivalent, <span class="math inline">\$\\Delta=n(\\bar X-\\pi\_0)=S-s\_0\$</span>. De verdeling van deze laatste toetsstatistiek volgt rechtstreeks uit de Binomiale verdeling.

We observeren <span class="math inline">\$s=\$</span> 3175 en dus <span class="math inline">\$\\delta=s-s\_0=\$</span> 3175 <span class="math inline">\$-\$</span> 6155 <span class="math inline">\$\\times 0.5=\$</span> 97.5. In de onderstelling dat jongens en meisjes even waarschijnlijk zijn (d.i. onder de nulhypothese <span class="math inline">\$H\_0:\\pi=1/2\$</span>), kunnen we de bijhorende tweezijdige p-waarde berekenen als de kans dat de uitkomst <span class="math display">\\$$p=\\text{P}\_0\\left\[S-s\_0\\geq \\vert \\delta\\vert \\right$$ + \\text{P}\_0\\left$$S-s\_0\\leq - \\vert \\delta\\vert \\right$$.\\\]</span>

Merk op dat we dit kunnen herschrijven in termen van S. <span class="math display">\\$$p=\\text{P}\_0\\left\[S\\geq s\_0+ \\vert \\delta\\vert \\right$$ + \\text{P}\_0\\left$$S \\leq s\_0 - \\vert \\delta\\vert \\right$$.\\\]</span>

Voor ons voorbeeld kunnen we deze kansen als volgt berekenen:

<span class="math display">\\$$\\begin{eqnarray\*} \\text{P}\_0\\left\[S\\geq s\_0+ \\vert \\delta\\vert \\right$$ &=& P(S \\geq 6155 \\times 0.5 + \\vert 3175 - 6155 \\times 0.5\\vert ) = P(S \\geq 3175)\\\\ &= &P(S= 3175) + P(S=3176) + ... + P(S=6155)\\\\ & =& 0.0067\\\\\\\\ \\text{P}\_0\\left$$S \\leq s\_0 - \\vert \\delta\\vert \\right$$ &=& P(S \\leq 6155 \\times 0.5 - \\vert 3175- 6155 \\times 0.5\\vert) = P(S \\leq 2980)\\\\ &= &P(S=0) + ... + P(S=2980) \\\\ &=&0.0067 \\end{eqnarray\*}\\\]</span>

Gezien <span class="math inline">\$\\pi=0.5\$</span> zijn deze kansen gelijk omdat de binomiale distributie dan symmetrisch is. Dat is niet langer het geval wanneer <span class="math inline">\$\\pi\$</span> afwijkt van 0.5.

In R kan men de kansen berekenen via de commando’s:

``` {.sourceCode .r}
pi0 <- 0.5
s0 <- pi0 *n
delta <- abs(boys- s0)
delta
```

    ## [1] 97.5

``` {.sourceCode .r}
sUp <- s0 + delta
sDown <- s0 -delta
c(sDown,sUp)
```

    ## [1] 2980 3175

``` {.sourceCode .r}
#Merk op dat we voor de berekening naar rechts
#pbinom(sUp-1,n,pi) gebruiken omdat we met
#pbinom de kans berekenen in de linkse staart
#anders wordt s=3175 er niet bij geteld!
pUp <- 1-pbinom(sUp-1,n,pi0)
pUp
```

    ## [1] 0.006699883

``` {.sourceCode .r}
pDown <- pbinom(sDown,n,pi0)
pDown
```

    ## [1] 0.006699883

``` {.sourceCode .r}
p <- pUp+pDown
p
```

    ## [1] 0.01339977

waarbij `pbinom(sUp-1,n,pi0)` de kans op een resultaat kleiner of gelijk aan <span class="math inline">\$s\_0+\\vert \\delta\\vert -1 =\$</span> 3174 berekent. Als <span class="math inline">\$\\pi= 1/2\$</span>, dan zou de kans om door toeval minstens <span class="math inline">\$\\delta=\$</span> 97.5 jongens meer of minder te observeren dan het gemiddelde onder <span class="math inline">\$H\_0: s\_0=\$</span> 3077.5 , slechts 1.34% is, de <span class="math inline">\$p\$</span>-waarde van de binomiale test.
Dit geeft aan dat het heel onwaarschijnlijk is om een dergelijk groot aantal jongens te observeren als in realiteit jongens en meisjes even waarschijnlijk zijn. Het drukt met andere woorden uit dat de onderstelling dat jongens en meisjes even waarschijnlijk zijn, weinig gesteund wordt door de data. Dit blijkt ook uit Figuur [9.3](index.md).

``` {.sourceCode .r}
plot(s0+seq(-150.5,150.5,1),dbinom(s0+seq(-150.5,150.5,1),prob=.5,size=n),type="h",xlab="X",ylab="Kans (Dichtheid)",main= as.expression(substitute(pi == val,list(val=paste0("0.5, nobs=",n)))),ylim=c(-.0009,0.011))
abline(v=s0,lwd=2,col=4)
abline(v=boys,lwd=2,col=2)
abline(v=sDown,lwd=1,col=2,lty=2)
text(c(sDown,s0,boys,boys),c(rep(0.011,3),0.01),labels=c(expression(paste(s[0]-delta)),expression(s[0]),expression(s==s[0]+delta),as.expression(substitute(s==val,list(val=boys)))),pos=4,col=c(2,4,2))
text(sDown-50,-.0005,label="p-waarde",col=2,pos=4)
text(sUp,-.0005,label="p-waarde",col=2,pos=4)
arrows(s0+1500.5,-.0009,sUp,-.0009,col=2,lwd=2,angle=20,length=.1)
arrows(s0-1500.5,-.0009,sDown,-.0009,col=2,lwd=2,angle=20,length=.1)
```

<span id="fig:pitests"></span> <img src="Statistiek_2019_2020_files/figure-html/pitests-1.png" style="width:100.0%" alt="Binomiale verdeling van het aantal jongens S onder $H_0: \pi=0.5 (n=6155)$." />

Figuur 9.3: Binomiale verdeling van het aantal jongens S onder <span class="math inline">\$H\_0: \\pi=0.5 (n=6155)\$</span>.

De test kan eveneens worden uitgevoerd a.d.h.v. de `binomial.test` functie in R.

``` {.sourceCode .r}
binom.test(x=boys,n=n,p=pi0)
```

    ##
    ##  Exact binomial test
    ##
    ## data:  boys and n
    ## number of successes = 3175, number of trials = 6155, p-value =
    ## 0.0134
    ## alternative hypothesis: true probability of success is not equal to 0.5
    ## 95 percent confidence interval:
    ##  0.5032696 0.5283969
    ## sample estimates:
    ## probability of success
    ##              0.5158408

Op het 5% significantie-niveau besluiten we dat er gemiddeld meer kans is dat een ongeboren kind mannelijk dan vrouwelijk is.

### <span class="header-section-number">9.2.2</span> Betrouwbaarheidsinterval op een proportie

De schatter van de proportie van jongens in de populatie, is het steekproefgemiddelde <span class="math inline">\$\\hat \\pi=\\bar x=\$</span> 0.516 en de standaard error is <span class="math display">\\$$SE\_{\\bar x}=\\sqrt{\\frac{\\text{Var}\[X$$}{n}}=\\sqrt{\\frac{\\pi(1-\\pi)}{n}}\\\]</span> We kunnen dit schatten o.b.v. de steekproef: <span class="math inline">\$SE\_{\\bar x}=\\sqrt{\\frac{\\hat\\pi(1-\\hat\\pi)}{n}}=\$</span> 0.0064. Op basis van de centrale limietstelling (CLT, Sectie [5.3.3](../chap-besluit/index.md)) kunnen we nu eveneens een 95% betrouwbaarheidsinterval bouwen:

<span class="math display">\\$$\\hat\\pi \\pm 1.96 SE\_{\\hat\\pi}.\\$$</span>

We kunnen dit in R bekomen:

``` {.sourceCode .r}
se=sqrt(pi*(1-pi)/n)
pi+c(-1,1)*qnorm(0.975)*se
```

    ## [1] 0.5033559 0.5283257

Een alternatief dat geen grote dataset vereist, is het inverteren van de one-sample test voor proporties. Stop daartoe in het 95% betrouwbaarheidsinterval alle waarden <span class="math inline">\$\\pi\_0\$</span> die niet verworpen worden door deze test op het 5% significantieniveau. Dit is geïmplementeerd in de `binom.test` functie.

``` {.sourceCode .r}
BI <- binom.test(x=boys,n=n,p=pi0)$conf.int
BI
```

    ## [1] 0.5032696 0.5283969
    ## attr(,"conf.level")
    ## [1] 0.95

We verfiëren dit nu:

``` {.sourceCode .r}
binom.test(x=boys,n=n,p=BI[1],alternative="greater")
```

    ##
    ##  Exact binomial test
    ##
    ## data:  boys and n
    ## number of successes = 3175, number of trials = 6155, p-value =
    ## 0.025
    ## alternative hypothesis: true probability of success is greater than 0.5032696
    ## 95 percent confidence interval:
    ##  0.5052779 1.0000000
    ## sample estimates:
    ## probability of success
    ##              0.5158408

``` {.sourceCode .r}
binom.test(x=boys,n=n,p=BI[2],alternative="less")
```

    ##
    ##  Exact binomial test
    ##
    ## data:  boys and n
    ## number of successes = 3175, number of trials = 6155, p-value =
    ## 0.025
    ## alternative hypothesis: true probability of success is less than 0.5283969
    ## 95 percent confidence interval:
    ##  0.0000000 0.5263925
    ## sample estimates:
    ## probability of success
    ##              0.5158408

De p-waardes van de exacte eenzijdige testen waarbij <span class="math inline">\$\\pi\_0\$</span> gelijk gesteld wordt aan de onder- en bovengrens van het 95% BI zijn inderdaad beiden gelijk aan 0.025. Het exacte BI is te verkiezen boven het BI dat gebaseerd is op de CLT. Voor de Saksen-studie ligt het BI op basis van de CLT heel dicht bij het exacte BI omdat de studie is gebaseerd op een grote steekproef (<span class="math inline">\$n=\$</span> 6155).

### <span class="header-section-number">9.2.3</span> Conclusie

Merk op dat het testen voor een proportie kan gezien worden als het equivalent van een one-sample t-test voor binaire data.

Voor de Saksen populatie besluiten we op het 5% significantieniveau dat er meer kans is dat een ongeboren kind mannelijk dan vrouwelijk is (<span class="math inline">\$p=\$</span> 0.013). De kans dat een ongeboren kind mannelijk is, bedraagt 51.6% (95% BI $$50.3,52.8$$%).

---

[← 9.1 Inleiding {#inleiding}](01-9-1-inleiding-inleiding.md) · [Up: contents](index.md) · [9.3 Toets voor associatie tussen 2 kwalitatieve variabelen →](03-9-3-toets-voor-associatie-tussen-2-kwalitatieve-variabelen.md)

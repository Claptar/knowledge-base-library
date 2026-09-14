---
title: waarnemingen (NA) voorkomen
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-describe.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-describe.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# waarnemingen (NA) voorkomen

**Source:** [`chap-describe.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-describe.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

```

De verdeling kan ook geëvalueerd worden aan de hand van een *box-and-whisker-plot*, kortweg *boxplot* genoemd. Deze is meer compact dan een histogram en laat om die reden gemakkelijker vergelijkingen tussen verschillende groepen toe (zie verder). Een Boxplot voor het BMI wordt getoond in Figuur [4.6](index.md). De boxplot toont een doos lopend van het 25% tot 75% percentiel met een lijntje ter hoogte van de mediaan (het 50% percentiel) en verder 2 snorharen. Die laatste kunnen in principe lopen tot het minimum en maximum, of tot het 2.5% en 97.5 % of 5% en 95% percentiel. R kiest voor de kleinste en de grootste geobserveerde waarde die geen outlier of extreme waarde zijn. Een meting wordt hierbij een outlier genoemd wanneer ze meer dan 1.5 keer de boxlengte beneden het eerste of boven het derde kwartiel ligt. Een meting wordt een extreme waarde genoemd wanneer ze meer dan 3 keer de boxlengte beneden het eerste of boven het derde kwartiel ligt.

<span id="def:unnamed-chunk-35" class="definition">**Definitie 4.1 (percentiel)** </span>Het *25% percentiel* of *25% kwantiel* <span class="math inline">\$x\_{25}\$</span> van een reeks waarnemingen wordt gedefinieerd als een uitkomstwaarde <span class="math inline">\$x\_{25}\$</span> zodat minstens <span class="math inline">\$25\\%\$</span> van die waarnemingen kleiner of gelijk zijn aan <span class="math inline">\$x\_{25}\$</span> en minstens <span class="math inline">\$75\\%\$</span> van die waarnemingen groter of gelijk zijn aan <span class="math inline">\$x\_{25}\$</span>. Het *75% percentiel* of *75% kwantiel* van een reeks waarnemingen definieert men als een uitkomstwaarde <span class="math inline">\$x\_{75}\$</span> zodat minstens 75% kleiner of gelijk zijn aan <span class="math inline">\$x\_{75}\$</span> en minstens <span class="math inline">\$25\\%\$</span> van die waarnemingen groter of gelijk zijn aan <span class="math inline">\$x\_{75}\$</span>. Algemeen wordt het *<span class="math inline">\$k\\%\$</span> percentiel* van een reeks waarnemingen gedefinieerd als een waarde (van <span class="math inline">\$x\$</span>) waarvoor de cumulatieve frequentie gelijk is aan <span class="math inline">\$k/100.\$</span> Als er meerdere observaties aan voldoen neemt men vaak het gemiddelde van die waarden.

**Einde definitie**

In R kunnen die als volgt worden bekomen

``` {.sourceCode .r}
quantile(NHANES$BMI,c(0.25,.5,.75),na.rm=TRUE)
```

    ##   25%   50%   75%
    ## 21.58 25.98 30.89

``` {.sourceCode .r}
#code om boxplot te genereren
boxplot(NHANES$BMI,ylab="BMI")

#Code om text toe te voegen aan plot
#Dit hoef je zelf normaal gezien niet te doen
BMI=na.exclude(NHANES$BMI)
rangeCl<-quantile(BMI,c(.25,.75))+c(-1,1)*diff(quantile(BMI,c(.25,.75)))*1.5
boxYs<-c(range(BMI[BMI<=rangeCl[2]&BMI>=rangeCl[1]]),quantile(BMI,c(.25,.5,.75)),rangeCl[2]+(max(BMI)-rangeCl[2])/2)

text(1.3,boxYs,labels=c("wisker","wisker","x25","mediaan","x75","outliers"),pos=4,cex=1.3)
lines(c(1.1,1.3,1.3,1.1),c(rangeCl[2],rangeCl[2]+(max(BMI)-rangeCl[2])/2,rangeCl[2]+(max(BMI)-rangeCl[2])/2,max(BMI)),lty=2)
```

<span id="fig:boxBMI"></span> <img src="Statistiek_2019_2020_files/figure-html/boxBMI-1.png" style="width:100.0%" alt="Boxplot van BMI in de NHANES studie." />

Figuur 4.6: Boxplot van BMI in de NHANES studie.

Bij de inspectie van een dataset speelt het detecteren van outliers in het algemeen een belangrijke rol. Ze kunnen wijzen op fouten, zoals tikfouten of andere fouten die gecheckt en gecorrigeerd moeten worden. Als het geen foutief genoteerde waarden zijn, dan kan het soms wijzen op een subject dat niet echt in de studiepopulatie thuis hoort. Als het in alle opzichten om een bona fide waarde gaat, dan nog is het belangrijk om outliers te detecteren: ze kunnen zeer invloedrijk zijn op de schatting van statistische parameters (zie Sectie [4.3](index.md)). Als de conclusies van een studie anders liggen met of zonder inclusie van de outlier, dan is dit een ongewenst fenomeen. Men wil immers nooit dat 1 observatie beslissend is voor de conclusies. Dit soort onzekerheid ondermijnt de geloofwaardigheid van de onderzoeksresultaten en vraagt om verdere studie. Binnen de statistiek bestaat een grote waaier aan technieken, zogenaamde *robuuste statistische technieken*, die erop gericht zijn om de invloed van outliers te minimaliseren. In deze cursus gaan we hier slechts in zeer beperkte mate op in (zie Sectie [4.3](index.md), mediaan).

## <span class="header-section-number">4.3</span> Samenvattingsmaten voor continue variabelen {#samenvattingsmaten-voor-continue-variabelen}

Een histogram levert reeds een sterke samenvatting van de geobserveerde, continue gegevens, maar in wetenschappelijke rapporten is er zelden plaats om per geobserveerde variabele dergelijke grafiek voor te stellen. Om die reden is vaak een veel drastischere samenvattingsmaat noodzakelijk. In deze sectie geven we aan hoe de centrale locatie van de gegevens kan beschreven worden, alsook de spreiding van die gegevens rond hun centrale locatie.

### <span class="header-section-number">4.3.1</span> Maten voor de centrale ligging

<span id="def:unnamed-chunk-37" class="definition">**Definitie 4.2 (rekenkundig gemiddelde)** </span>Het **(rekenkundig) gemiddelde** <span class="math inline">\$\\overline{x}\$</span> (spreek uit: *x-streep* of *x-bar*) van een reeks waarnemingen <span class="math inline">\$x\_i, i=1, 2, \\dots, n\$</span> is per definitie de som van de observaties gedeeld door hun aantal <span class="math inline">\$n\$</span>: <span class="math display">\\$$\\begin{equation\*} \\overline{x}= \\frac{x\_1 + x\_2 + \\dots + x\_n}{n} =\\frac{1}{n} \\sum\_{i=1}^n x\_i \\end{equation\*}\\$$</span>

**Einde definitie**

Een groot voordeel van het gemiddelde als een maat voor de centrale locatie van de observaties is dat het alle data-waarden efficiënt gebruikt vanuit statistisch perspectief. Dit wil zeggen dat ze (onder bepaalde statistische modellen) het maximum aan informatie uit de gegevens haalt en om die reden relatief gezien zeer stabiel blijft wanneer ze herberekend wordt op basis van een nieuwe, even grote steekproef die onder identieke omstandigheden werd bekomen. Bovendien beschrijft het gemiddelde ook verschillende belangrijke modellen voor de verdeling van de gegevens, zoals de Normale verdeling (zie Sectie [4.4](index.md)). Een groot nadeel van het gemiddelde is dat het zeer gevoelig is aan de aanwezigheid van outliers in de dataset. Om die reden is het vooral een interessante maat van locatie wanneer de verdeling van de observaties (zoals weergegeven door bijvoorbeeld een histogram) min of meer symmetrisch is.

``` {.sourceCode .r}
mean(NHANES$BMI,na.rm=TRUE)
```

    ## [1] 26.66014

``` {.sourceCode .r}
#opnieuw is de na.rm statement hier nodig
#omdat ontbrekende waarden voorkomen.
```

*Indien men de grootste observatie (81.25) vervangt door 8125 om als het ware ene tikfout voor te stellen, dan wijzigt het rekenkundig gemiddelde naar 27.5 en dat terwijl er bijna 10000 BMI metingen zijn. Merk op dat het gemiddelde vrij sterk beïnvloed kan worden door één outlier.*

**Eigenschap**

Als alle uitkomsten <span class="math inline">\$x\_i\$</span> met een willekeurige constante <span class="math inline">\$a\$</span> worden vermenigvuldigd, dan ook het gemiddelde van die reeks uitkomsten. Als bij alle uitkomsten een constante <span class="math inline">\$a\$</span> wordt opgeteld, dan ook bij het gemiddelde van die reeks uitkomsten. Formeel betekent dit: <span class="math display">\\$$\\begin{eqnarray\*} \\overline{ax} &= &a \\overline{x} \\\\ \\overline{a + x} &= &a + \\overline{x} \\end{eqnarray\*}\\$$</span> Voor 2 reeksen getallen <span class="math inline">\$x\_i\$</span> en <span class="math inline">\$y\_i\$</span>, <span class="math inline">\$i=1,...,n\$</span>, geldt dat het gemiddelde van de som van de observaties gelijk is aan de som van hun gemiddelden: <span class="math display">\\$$\\begin{equation\*} \\overline{x + y} = \\overline{x} + \\overline{y}. \\end{equation\*}\\$$</span> Als de gegevens <span class="math inline">\$x\_i\$</span> enkel de waarden 0 of 1 aannemen, dan is <span class="math inline">\$\\overline{x}\$</span> de proportie subjecten voor wie de waarde 1 werd geobserveerd. Immers, zij <span class="math inline">\$n\_1\$</span> het aantal subjecten binnen de groep van <span class="math inline">\$n\$</span> subjecten waarvoor de waarde 1 werd geobserveerd, dan is <span class="math display">\\$$\\begin{equation\*} \\overline{x}= \\sum\_{i=1}^n \\frac{x\_i}{n} = \\frac{n\_1}{n}. \\end{equation\*}\\$$</span>

Bijvoorbeeld, als we de variabele **Gender** zó coderen dat mannen een waarde 0 aannemen en vrouwen een waarde 1, dan is het gemiddelde van de variabele **Gender** gelijk aan 50.2%, hetgeen de proportie is van het aantal vrouwen in de studie. Een percentage kan dus steeds opgevat worden als het gemiddelde van een geschikte variabele.

**Einde eigenschap**

Een centrale maat die robuuster reageert dan het gemiddelde, d.w.z. minder of niet gevoelig is aan outliers, is de *mediaan* of het *50% percentiel*.

<span id="def:unnamed-chunk-39" class="definition">**Definitie 4.3 (mediaan)** </span>De **mediaan**, het **50% percentiel** of het **50% kwantiel** <span class="math inline">\$x\_{50}\$</span> van een reeks waarnemingen <span class="math inline">\$x\_i, i=1, 2, \\dots, n\$</span> is per definitie een uitkomstwaarde <span class="math inline">\$x\_{50}\$</span> zodat minstens <span class="math inline">\$50\\%\$</span> van die waarnemingen groter of gelijk zijn aan <span class="math inline">\$x\_{50}\$</span> en minstens <span class="math inline">\$50\\%\$</span> van die waarnemingen kleiner of gelijk zijn aan <span class="math inline">\$x\_{50}\$</span>.

**Einde definitie**

Om de mediaan te schatten, rangschikt men eerst de gegevens volgens grootte. Als het aantal observaties <span class="math inline">\$n\$</span> oneven is, dan is een schatting voor de mediaan de middelste waarneming. Indien <span class="math inline">\$n\$</span> even is, dan zijn er 2 middelste waarnemingen en schat men de mediaan (meestal) als hun gemiddelde. Een voordeel van de mediaan is dat ze niet gevoelig is aan outliers. In het bijzonder kan ze vaak nuttig aangewend worden wanneer sommige gegevens *gecensureerd* zijn. Dit wil zeggen dat men voor een aantal gegevens enkel weet dat ze boven of onder een bepaalde drempelwaarde liggen.

``` {.sourceCode .r}
median(NHANES$BMI,na.rm=TRUE)
```

    ## [1] 25.98

``` {.sourceCode .r}
#Merk op dat we hier gebruik maken van het argument na.rm=TRUE
#Dit komt omdat we niet beschikken over het BMI
#voor elke persoon: ontbrekende waarnemingen
#Die worden in R als een NA voorgesteld
#Als we het argument na.rm=TRUE gebruiken wordt
#de mediaan berekend op basis van de beschikbare observaties
```

Indien men de grootste observatie (81.25) vervangt 8125, dan wijzigt de mediaan niet. Merk ook op dat de mediaan lager is dan het gemiddelde, hij is minder gevoelig voor de outliers in de dataset.

<span id="def:unnamed-chunk-41" class="definition">**Definitie 4.4 (modus)** </span>De **modus** van een reeks observaties is de waarde die het meest frequent is, of wanneer de gegevens gegroepeerd worden, de klasse met de hoogste frequentie.

**Einde definitie**

De modus wordt niet vaak gebruikt in statistische analyse omdat haar waarde sterk afhangt van de nauwkeurigheid waarmee de gegevens werden gemeten. Zo is de modus van de reeks observaties <span class="math inline">\$1, 1, 1, 1.5, 1.75, 1.9, 2, 2.1, 2.4\$</span> gelijk aan 1, maar wordt ze 2 wanneer alle observaties afgerond worden tot gehele getallen. Bovendien is de modus niet eenvoudig te schatten voor continue data waar de frequentie van elke geobserveerde waarde meestal 1 is. De modus is daarom het meest zinvol voor kwalitatieve en discrete numerieke gegevens, waar ze de meest frequente klasse aanduidt.

Als de observaties uit een *symmetrische verdeling* afkomstig zijn, vallen de mediaan en het gemiddelde nagenoeg samen (als de geobserveerde verdeling perfect symmetrisch is, vallen ze theoretisch exact samen). De beste schatter voor het centrum van de verdeling op basis van de beschikbare steekproef is dan het gemiddelde eerder dan de mediaan van die observaties. Inderdaad, als men telkens opnieuw een lukrake steekproef neemt uit de gegeven studiepopulatie en voor elke steekproef het gemiddelde en de mediaan berekent, dan zal het gemiddelde minder variëren van steekproef tot steekproef dan de mediaan. Ze is bijgevolg stabieler en wordt daarom een *meer precieze schatter* genoemd. Intuïtief kan men begrijpen dat het gemiddelde meer informatie uit de gegevens gebruikt: niet alleen of iets groter of kleiner is dan <span class="math inline">\$x\_{50}\$</span> maar ook hoeveel groter of kleiner de exacte waarde van elke observatie is, wordt in de berekening betrokken.

<span id="def:unnamed-chunk-42" class="definition">**Definitie 4.5 (scheve verdeling)** </span>Een niet-symmetrische verdeling wordt **scheef** genoemd. Als de waarden rechts van de mediaan verder uitlopen dan links, dan is de verdeling *scheef naar rechts* (in het Engels: *positively skew*) en is het gemiddelde (meestal) groter dan de mediaan. Als de waarden links van de mediaan verder uitlopen dan rechts, dan is de verdeling *scheef naar links* (in het Engels: *negatively skew*) en is het gemiddelde (meestal) kleiner dan de mediaan.

**Einde definitie**

Voor een niet-symmetrische verdeling is de mediaan veelal een beter interpreteerbare maat dan het gemiddelde omdat ze minder beïnvloed is door de staarten van de verdeling en daarom beter het centrum van de verdeling aanduidt. Maar in sommige gevallen, zoals bijvoorbeeld voor \`de gemiddelde opbrengst per week’, blijft het gemiddelde zinvol omdat het meteen verwijst naar de totale opbrengst over alle weken (gelijk aan <span class="math inline">\$n\$</span> keer het gemiddelde als <span class="math inline">\$n\$</span> weken werden geobserveerd). Ook voor kwalitatieve variabelen kan een gemiddelde zinvol zijn. Voor binaire nominale variabelen die als 1 of 0 gecodeerd zijn, geeft het gemiddelde immers het percentage observaties gelijk aan 1 weer. Voor ordinale variabelen die bijvoorbeeld gecodeerd zijn als <span class="math inline">\$1, 2, 3, ...\$</span> levert het gemiddelde soms nuttigere informatie dan de mediaan. Niettemin berust het dan op de impliciete onderstelling dat een wijziging van score van 1 naar 2 even belangrijk is als een wijziging van 2 naar 3.

Om scheve verdelingen in een paar woorden te beschrijven is het vaak nuttig om

- ofwel de gegevens te beschrijven in termen van percentielen,
- ofwel de gegevens te transformeren naar een andere schaal (bvb. door logaritmen te nemen), zodat ze op de nieuwe schaal bij benadering symmetrisch verdeeld zijn.

Wanneer het gemiddelde groter is dan de mediaan en alle metingen positief zijn (vb concentraties, BMI), dan is een logaritmische transformatie van de gegevens vaak nuttig om de scheefheid weg te nemen. In dit geval is vooral het *geometrisch gemiddelde* interessant.

<span id="def:unnamed-chunk-43" class="definition">**Definitie 4.6 (geometrisch gemiddelde)** </span>Het **geometrische gemiddelde** van een reeks waarnemingen <span class="math inline">\$x\_i, i=1, 2, \\dots, n\$</span> ontstaat door er de natuurlijke logaritme van te berekenen, het gemiddelde hiervan te nemen en dit vervolgens terug te transformeren naar de originele schaal door er de exponentiële functie van te nemen: <span class="math display">\\$$\\begin{equation\*} \\exp\\left\\{\\frac{1}{n} \\sum\_{i=1}^n \\log(x\_i)\\right\\} \\end{equation\*}\\$$</span>

**Einde definitie**

``` {.sourceCode .r}
par(mfrow=c(1,2))
hist(NHANES$BMI, main="histogram van BMI",xlab="BMI")
hist(log(NHANES$BMI), main="histogram van log(BMI)",xlab="log(BMI)")
```

<span id="fig:histLogBMI"></span> <img src="Statistiek_2019_2020_files/figure-html/histLogBMI-1.png" style="width:100.0%" alt="Boxplot van BMI en log(BMI) in de NHANES studie." />

Figuur 4.7: Boxplot van BMI en log(BMI) in de NHANES studie.

In situaties waar de log-transformatie inderdaad de scheefheid wegneemt, zal het geometrisch gemiddelde dichter bij de mediaan liggen dan het gemiddelde. Wanneer de verdeling scheef is, is ze soms zelfs een nuttigere maat voor centrale locatie dan de mediaan:

1.  omdat ze ook gebruik maakt van de exacte waarden van de observaties en daarom doorgaans preciezer is dan de mediaan;

2.  omdat ze, op een transformatie na, berekend wordt als een rekenkundig gemiddelde (weliswaar van de logaritmisch getransformeerde observaties) en algemene statistische technieken voor een gemiddelde (zoals betrouwbaarheidsintervallen (zie volgende hoofdstukken) en toetsen van hypothesen (zie volgende hoofdstukken) daardoor vrijwel rechtstreeks toepasbaar zijn voor geometrische gemiddelden.

<span id="exm:unnamed-chunk-44" class="example">**Voorbeeld 4.2 (BMI)** </span>

Het gemiddelde en mediane BMI bedraagt 26.66 en 25.98 , respectievelijk. Het gemiddelde is hier groter dan de mediaan omdat de BMI scheef verdeeld is naar rechts (zie Figuur [4.7](index.md)). De verdeling wordt meer symmetrisch na log-transformatie. Het gemiddelde en mediane log-BMI liggen ook dichter bij elkaar en bedragen respectievelijk 3.25 en 3.26. De geometrisch gemiddelde BMI-concentratie bekomen we door de exponentiële functie te evalueren in 3.25, hetgeen ons 25.69 oplevert. Merk op dat dit inderdaad beter met de mediaan overeenstemt dan het rekenkundig gemiddelde.

`**Einde voorbeeld**`

Tot slot, vooraleer een eenvoudige maat voor de centrale ligging (en spreiding) te construeren of interpreteren, is het goed om altijd eerst de volledige verdeling te bekijken! Immers, stel dat men het gemiddelde of mediaan berekent van gegevens uit een bimodale verdeling (d.i. een verdeling met 2 modi, voor bvb. zieken en niet-zieke dieren). Dan kan het gemiddelde of mediaan makkelijk een zeer zeldzame waarde aannemen die geenszins in de buurt van 1 van beide maxima ligt.

### <span class="header-section-number">4.3.2</span> Spreidingsmaten {#spreidingsmaten}

Nadat de centrale ligging van de gegevens werd bepaald, is men in tweede instantie geïnteresseerd in de spreiding van de gegevens rond die centrale waarde. Er zijn verschillende redenen waarom daar interesse in bestaat:

1.  Om risico’s te berekenen (zie Sectie [4.4](index.md)) volstaat het niet om de centrale locatie van de gegevens te kennen, maar moet men bovendien weten hoeveel de gegevens rond die waarde variëren. Inderdaad, stel dat men wenst te weten welk percentage van de subjecten een BMI heeft van boven de 35. Wetende dat een geometrisch gemiddelde van 25.69 wordt geobserveerd, zal dat percentage relatief hoog zijn wanneer de metingen zeer gespreid zijn en relatief laag anders.
2.  Veldbiologen zijn vaak geïnteresseerd in de mate waarin dieren of planten verspreid zijn over een zeker studiegebied. Op die manier kunnen ze immers leren over de relaties tussen individuen onderling en met hun omgeving. Daartoe zal men in de praktijk op verschillende plaatsen in het studiegebied tellingen maken van het aantal individuen op die plaats. Men kan aantonen dat, onder bepaalde veronderstellingen, individuen lukraak verspreid zijn over het studiegebied wanneer de spreiding op die tellingen, zoals gemeten door de variantie (zie verder), van dezelfde grootte-orde is als de gemiddelde telling. Indien de spreiding groter is, dan hebben individuen de neiging om zich te groeperen. Andersom, indien de spreiding op die tellingen lager is dan de gemiddelde telling, dan zijn de individuen zeer uniform verdeeld over het studiegebied.
3.  Stel dat men een zekere uitkomst (bvb. het aantal species ongewervelde dieren in een stuk bodemkorst) wenst te vergelijken tussen 2 groepen (bvb. gebieden met en zonder bosbrand), dan zal men een duidelijk beeld van het groepseffect krijgen wanneer de uitkomst weinig gespreid is, maar een veel minder duidelijk beeld wanneer de gegevens meer chaotisch (en dus meer gespreid) zijn. Om uit te maken of een interventie-effect toevallig of systematisch is, moet men daarom een idee hebben van de spreiding op de gegevens.

Dat uitkomsten variëren tussen individuen en binnen individuen omwille van allerlei redenen ligt aan de basis van de statistische analyse van veel fenomenen. Het goed beschrijven van variatie naast de centrale locatie van de gegevens is daarom belangrijk! Hierbij zal men typisch een onderscheid maken tussen variatie die men kan verklaren (door middel van karakteristieken, zoals bijvoorbeeld de leeftijd, van de bestudeerde individuen) en onverklaarde variatie. We gaan dieper in op dit onderscheid in Hoofdstuk [6](../chap-linReg/index.md) rond lineaire regressie.

Variatie betekent dat niet alle observaties <span class="math inline">\$x\_i\$</span> gelijk zijn aan het gemiddelde <span class="math inline">\$\\overline{x}\$</span>. De afwijking <span class="math inline">\$x\_i - \\bar{x}\$</span> is om die reden interessant. Het gemiddelde van die afwijkingen is echter altijd 0 (verifieer!) omdat positieve en negatieve afwijkingen mekaar opheffen. Bijgevolg levert de gemiddelde afwijking geen goede maat op voor de variatie en is het beter om bijvoorbeeld naar kwadratische afwijkingen <span class="math inline">\$(x\_i - \\bar{x})^2\$</span> te kijken. Het gemiddelde van die *kwadratische afwijkingen rond het gemiddelde*, het gemiddelde dus van <span class="math inline">\$(x\_i - \\bar{x})^2\$</span>, levert daarom wel een goede maat op. Merk op dat we bij het berekenen van het gemiddelde niet delen door het aantal observaties <span class="math inline">\$n\$</span>, maar door <span class="math inline">\$n-1\$</span> waarbij we corrigeren voor het feit dat we voor de berekening van de steekproef variantie 1 vrijheidsgraad hebben gespendeerd aan het schatten van het gemiddelde.

<span id="def:unnamed-chunk-45" class="definition">**Definitie 4.7 (variantie)** </span>De **variantie** een reeks waarnemingen <span class="math inline">\$x\_i, i=1, 2, \\dots, n\$</span> is per definitie <span class="math display">\\$$\\begin{equation\*} s^2\_x = \\sum\_{i=1}^{n} \\frac{(x\_i - \\bar{x})^2}{n-1} \\end{equation\*}\\$$</span>

Als duidelijk is om welke waarnemingen het gaat, wordt dit ook met <span class="math inline">\$s^2\$</span> genoteerd.

**Einde definitie**

Indien alle observaties gelijk waren en er dus geen variatie was, dan zou hun variantie 0 bedragen. Hoe meer de gegevens uitgesmeerd zijn rond hun gemiddelde, hoe groter <span class="math inline">\$s^2\$</span>. Helaas is de waarde van de variantie zelf niet gemakkelijk te interpreteren. Dit is deels omdat door het kwadrateren de variantie niet langer de dimensie van de oorspronkelijke waarnemingen heeft. Handiger om mee te werken is daarom de *standaarddeviatie* of *standaardafwijking*: <span class="math display">\\$$\\begin{equation\*} s\_x= \\sqrt{s\_x^2} . \\end{equation\*}\\$$</span>

De standaarddeviatie is gedefinieerd voor elke numerieke variabele, maar is vooral nuttig omdat voor heel wat variabelen (in het bijzonder Normaal verdeelde variabelen - zie Sectie [4.4](index.md)) bij benadering 68% van de waarnemingen liggen tussen <span class="math inline">\$\\bar{x} - s\_x\$</span> en <span class="math inline">\$\\bar{x} + s\_x\$</span>, en 95% van de waarnemingen liggen tussen<a href="#fn14" id="fnref14" class="footnoteRef"><sup>14</sup></a> <span class="math inline">\$\\bar{x} - 2 s\_x\$</span> en <span class="math inline">\$\\bar{x} + 2 s\_x\$</span>. Deze intervallen noemt men respectievelijk 68% en 95% *referentie-intervallen*. Het is precies deze eigenschap die de standaarddeviatie zo nuttig maakt in de praktijk. De standaarddeviatie van een reeks waarnemingen wordt vaak afgekort als SD in de wetenschappelijke literatuur.

**Eigenschap**

Als alle uitkomsten <span class="math inline">\$x\_i\$</span> met een willekeurige constante <span class="math inline">\$a\$</span> worden vermenigvuldigd, dan wordt hun variantie vermenigvuldigd met <span class="math inline">\$a^2\$</span> en hun standaarddeviatie met <span class="math inline">\$\|a\|\$</span> (de absolute waarde van <span class="math inline">\$a\$</span>). Als bij alle uitkomsten <span class="math inline">\$a\$</span> wordt opgeteld, wijzigen hun variantie en standaarddeviatie niet.

**Einde eigenschap**

``` {.sourceCode .r}

---

[← argument na.rm=TRUE omdat er ontbrekende](08-argument-na-rm-true-omdat-er-ontbrekende.md) · [Up: contents](index.md) · [Het gebruik van functie sd() levert de standarddeviatie →](10-het-gebruik-van-functie-sd-levert-de-standarddeviatie.md)

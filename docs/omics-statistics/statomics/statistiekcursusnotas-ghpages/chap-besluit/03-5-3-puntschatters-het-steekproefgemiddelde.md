---
title: '5.3 Puntschatters: het steekproefgemiddelde'
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-besluit.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 5.3 Puntschatters: het steekproefgemiddelde

**Source:** [`chap-besluit.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

Zij <span class="math inline">\$X\$</span> een lukrake trekking uit de populatie van de bestudeerde karakteristiek en onderstel dat haar theoretische verdeling$$bvb. de Normale verdeling$$ een gemiddelde <span class="math inline">\$\\mu\$</span> en variatie <span class="math inline">\$\\sigma^2\$</span> heeft. Onderstel bovendien dat we geïnteresseerd zijn in het gemiddelde <span class="math inline">\$\\mu\$</span> van die karakteristiek in de studiepopulatie. Dan kunnen we <span class="math inline">\$\\mu\$</span> schatten op basis van een eenvoudige lukrake steekproef, <span class="math inline">\$X\_1,...,X\_n\$</span>, als het (rekenkundig) gemiddelde <span class="math display">\\$$\\begin{equation\*} \\bar X = \\frac{X\_1+ X\_2+ ... + X\_n}{n} = \\frac{\\sum\_{i=1}^{n} X\_i}{n} \\end{equation\*}\\$$</span>

van de toevalsveranderlijken <span class="math inline">\$X\_1,X\_2, ..., X\_n\$</span>. Dit wordt het *steekproefgemiddelde* genoemd. Het is belangrijk om te begrijpen dat het steekproefgemiddelde opnieuw een toevalsveranderlijke<a href="#fn24" id="fnref24" class="footnoteRef"><sup>24</sup></a> is, d.w.z. dat haar waarde zal variëren van steekproef tot steekproef. Hoewel er slechts 1 populatie is, zijn er heel wat verschillende steekproeven die men daaruit kan trekken. Dat heeft tot gevolg dat verschillende onderzoekers (die verschillende steekproeven uit dezelfde populatie analyseren) verschillende waarden zullen vinden voor het steekproefgemiddelde. Om die reden heeft het steekproefgemiddelde zelf een verdeling. Men zou die theoretisch kunnen bekomen door een oneindig aantal keer een steekproef van <span class="math inline">\$n\$</span> experimentele eenheden uit de populatie te trekken, telkens het steekproefgemiddelde te berekenen en al deze steekproefgemiddelden vervolgens uit te zetten in een histogram.

We zullen in deze sectie de theoretische verdeling van het steekproefgemiddelde bestuderen. Dat is belangrijk (a) omdat ze ons inzicht geeft in welke mate het resultaat van de studie zou variëren indien men een nieuwe, gelijkaardige studie zou opzetten; en (b) omdat ze ons leert hoe ver <span class="math inline">\$\\bar X\$</span> van het gezochte populatiegemiddelde <span class="math inline">\$\\mu\$</span> kan afwijken. Omdat we slechts over 1 steekproef beschikken (en dus slechts over 1 observatie voor <span class="math inline">\$\\bar X\$</span>), is het niet evident<a href="#fn25" id="fnref25" class="footnoteRef"><sup>25</sup></a> hoe we inzicht kunnen ontwikkelen in de verdeling van het steekproefgemiddelde. In het vervolg van deze sectie tonen we hoe dit toch mogelijk is op basis van de beschikbare steekproef wanneer we bepaalde aannames doen over de gegevens.

### <span class="header-section-number">5.3.1</span> Het steekproefgemiddelde is onvertekend

In de praktijk hoopt men uiteraard dat de schattingen die men bekomt op basis van de steekproef vergelijkbaar zijn met de overeenkomstige populatieparameters die men voor de volledige populatie zou bekomen.
Of dat zo is, hangt er in eerste instantie vanaf of de steekproef representatief is voor de studiepopulatie en bijgevolg of men al dan niet lukraak individuen uit de populatie gekozen heeft ter observatie (m.a.w. het hangt af van het design van de studie). Het volgende voorbeeld illustreert dit.

<span id="exm:unnamed-chunk-64" class="example">**Voorbeeld 5.1 (Ecstasy)** </span>

Aan Stanford University werd een survey uitgevoerd om de prevalentie van ecstasy-gebruik onder de studenten van deze universiteit te bepalen. Twee assistenten werden op het hoofdplein van de campus geplaatst en kregen de opdracht om alle studenten te interviewen die op bepaalde tijdstippen voorbij kwamen. Van de 369 studenten die geïnterviewd werden, rapporteerde 39% ooit ecstasy gebruikt te hebben. Dit resultaat wordt uiteraard deels bepaald door het algemene ecstasy-gebruik onder Stanford-studenten (d.i. door de verdeling van het ecstasy-gebruik over de populatie van Stanford-studenten). Maar ook door het feit dat de studenten die geïnterviewd werden, vermoedelijk een selectieve groep vormen van studenten die bijvoorbeeld niet in de les aanwezig waren of die in de buurt van het hoofdplein les kregen en bijgevolg voornamelijk uit 1 bepaalde studierichting afkomstig waren.

`**Einde voorbeeld**`

Omwille hiervan is het design van een studie van primair belang om lukrake en representatieve steekproeven te garanderen (zie Sectie [3.2](../chap-design/index.md)). Zoals u doorheen deze cursus zult vaststellen, zullen de meeste wetenschappelijke rapporten daarom een gedetailleerde beschrijving geven van de manier waarop de data bekomen werden. Dit moet de lezer toelaten om de validiteit van de studie te beoordelen.

Algemeen zullen we met <span class="math inline">\$E(X)\$</span>, <span class="math inline">\$\\text{Var}(X)\$</span> en <span class="math inline">\$\\text{Cor}(X,Y)\$</span> respectievelijk het gemiddelde, de variantie en de correlatie noteren van 2 toevalsveranderlijken <span class="math inline">\$X\$</span> en <span class="math inline">\$Y\$</span> in de populatie. Deze worden respectievelijk de *theoretische verwachtingswaarde* van <span class="math inline">\$X\$</span>, *theoretische variantie* van <span class="math inline">\$X\$</span> en *theoretische correlatie* van <span class="math inline">\$X\$</span> en <span class="math inline">\$Y\$</span> genoemd. Men zou ze bekomen door voor alle individuen in de populatie de karakteristieken <span class="math inline">\$X\$</span> en <span class="math inline">\$Y\$</span> op te meten en vervolgens respectievelijk het rekenkundig gemiddelde, de variantie en de Pearson correlatie te berekenen. Om die reden blijven de rekenregels voor gemiddelden en varianties geldig<a href="#fn26" id="fnref26" class="footnoteRef"><sup>26</sup></a> voor populatiegemiddelden en -varianties.

In de onderstelling dat we over een eenvoudige lukrake steekproef beschikken van metingen <span class="math inline">\$X\_1,...,X\_n\$</span> voor een karakteristiek <span class="math inline">\$X\$</span>, volgen <span class="math inline">\$X\_1,...,X\_n\$</span> allen dezelfde verdeling. In het bijzonder hebben ze allen gemiddelde <span class="math inline">\$\\mu\$</span> en variantie <span class="math inline">\$\\sigma^2\$</span>; d.i. <span class="math inline">\$E(X\_1)=...=E(X\_n)=\\mu\$</span> en <span class="math inline">\$\\text{Var}(X\_1)=...=\\text{Var}(X\_n)=\\sigma^2\$</span>. Het feit dat we subjecten 1 tot <span class="math inline">\$n\$</span> lukraak uit de populatie getrokken hebben, staat er m.a.w. garant voor dat verdeling van de karakteristiek in deze steekproef representatief is voor de theoretische verdeling in de doelpopulatie. Gebruik makend van de rekenregels voor gemiddelden, vinden we bijgevolg dat: <span class="math display">\\$$\\begin{eqnarray\*} E(\\bar X) &=& E \\left(\\frac{X\_1+ X\_2+ ... + X\_n}{n}\\right) \\\\ &= & \\frac{E(X\_1)+ E(X\_2)+ ... + E(X\_n)}{n} \\\\ &=& \\frac{\\mu + \\mu + ... +\\mu}{n} \\\\ &= & \\mu \\end{eqnarray\*}\\$$</span>

Dit geeft aan dat het verwachte steekproefgemiddelde in een eenvoudige lukrake steekproef gelijk is aan het beoogde populatiegemiddelde <span class="math inline">\$\\mu\$</span>. Men zegt dan dat <span class="math inline">\$\\bar X\$</span> een *onvertekende schatter* is voor <span class="math inline">\$\\mu\$</span>. We kunnen in dat geval verwachten dat de waarde <span class="math inline">\$\\bar x\$</span> die we schatten voor <span class="math inline">\$\\mu\$</span> op basis van de steekproef, niet systematisch hoger of lager dan de gezochte waarde <span class="math inline">\$\\mu\$</span> zal zijn. Het spreekt voor zich dat dit een zeer wenselijke eigenschap is.

<span id="def:unnamed-chunk-65" class="definition">**Definitie 5.1 (Onvertekende schatter)** </span>Een statistiek of schatter <span class="math inline">\$S\$</span> voor een parameter <span class="math inline">\$\\theta\$</span> wordt **onvertekend** genoemd als haar theoretische verwachtingswaarde gelijk is aan die parameter, d.w.z. <span class="math inline">\$E(S)= \\theta\$</span>.

**Einde definitie**

### <span class="header-section-number">5.3.2</span> Imprecisie/standard error

Het feit dat het steekproefgemiddelde (over een groot aantal vergelijkbare studies) *gemiddeld* gezien niet afwijkt van de gezochte waarde <span class="math inline">\$\\mu\$</span>, impliceert niet dat ze niet rond die waarde varieert. Om inzicht te krijgen hoe dicht we het steekproefgemiddelde bij <span class="math inline">\$\\mu\$</span> mogen verwachten, wensen we bijgevolg ook haar variabiliteit te kennen. Om dit te bepalen, zullen we ervan uitgaan dat de metingen <span class="math inline">\$X\_1, X\_2, ..., X\_n\$</span> werden gemaakt bij <span class="math inline">\$n\$</span> *onafhankelijke* observationele eenheden. In woorden betekent onafhankelijkheid dat elk subject een volledig nieuw stukje informatie bijdraagt tot het geheel. Een voorbeeld van afhankelijkheid tussen studie-objecten komt klassiek uit de studie van kankerverwekkende stoffen. Bij testen op zwangere ratten, worden metingen gedaan op hun levende foetussen of boorlingen. Foetussen van eenzelfde moeder delen dezelfde genetische achtergrond en zijn daarom waarschijnlijk meer aan elkaar gelijk dan foetussen van verschillende moeders. Zelfs al zijn de moeders die opgenomen worden in zo’n studie onafhankelijk van elkaar gekozen, de verschillende kleine ratjes leveren niet langer onafhankelijke stukjes informatie: via de gedeelde moeders is een afhankelijkheid ingebouwd. Afhankelijke gegevens worden ondermeer ook verzameld in pre-test/post-test designs en cross-over studies. De volgende eigenschap illustreert de noodzaak om over onafhankelijke gegevens te beschikken, wil men gemakkelijk de variabiliteit van het steekproefgemiddelde kunnen bepalen.

**Eigenschap**

Als <span class="math inline">\$X\$</span> en <span class="math inline">\$Y\$</span> onafhankelijke toevalsveranderlijken zijn, dan geldt<a href="#fn27" id="fnref27" class="footnoteRef"><sup>27</sup></a>: <span class="math display">\\$$\\begin{equation\*} \\text{Var}(X+Y) = \\text{Var}(X) + \\text{Var}(Y) \\end{equation\*}\\$$</span> Algemeen (d.i. voor mogelijks afhankelijke toevalsveranderlijken <span class="math inline">\$X\$</span> en <span class="math inline">\$Y\$</span>) geldt voor constanten <span class="math inline">\$a\$</span> en <span class="math inline">\$b\$</span>: <span class="math display">\\$$\\begin{eqnarray\*} \\text{Var}(aX+bY) &=& a^2 \\text{Var}(X) + b^2 \\text{Var}(Y) + 2 ab {% \\text{Cor}}(X,Y)\\sqrt{\\text{Var}(X)}\\sqrt{\\text{Var}(Y)} \\end{eqnarray\*}\\$$</span>

**Einde Eigenschap**

Een veelgemaakte fout is dat men beweert dat <span class="math inline">\$\\text{Var}(X-Y)=\\text{Var}(X)-\\text{Var}(Y)\$</span>. Niets is minder waar! Stel bijvoorbeeld dat de lengte <span class="math inline">\$X\$</span> van moeders en de lengte <span class="math inline">\$Y\$</span> van vaders evenveel variëren zodat <span class="math inline">\$\\text{Var}(X)=\\text{Var}(Y)\$</span>. Dan impliceert dat nog niet dat als je het verschil <span class="math inline">\$X-Y\$</span> neemt tussen de lengte van een moeder en haar partner, dat dit verschil variantie nul heeft; d.w.z. dat het niet varieert en bijgevolg voor alle moeder-vader paren exact dezelfde waarde aanneemt! Bovenstaande formules geven inderdaad integendeel aan dat: <span class="math display">\\$$\\begin{equation\*} \\text{Var}(X-Y) = \\text{Var}(X) + \\text{Var}(Y) -2{\\text{Cor}}(X,Y)\\sqrt{\\text{Var}(X)}\\sqrt{\\text{Var}(Y)}. \\end{equation\*}\\$$</span> Gebruik makend van deze rekenregels en steunend op de onafhankelijkheid van de observaties (waarvan we gebruik maken in de derde overgang, \*) kunnen we nu verder berekenen dat: <span class="math display">\\$$\\begin{eqnarray\*} \\text{Var}(\\bar X)&=&\\text{Var} \\left(\\frac{X\_1+ X\_2+ ... + X\_n}{n}\\right) \\\\ &= & \\frac{\\text{Var} (X\_1+ X\_2+ ... + X\_n)}{n^2} \\\\ &\\overset{\*}{=} & \\frac{\\text{Var}(X\_1)+ \\text{Var}(X\_2)+ ... + \\text{Var}(X\_n)}{n^2} \\\\ &=& \\frac{\\sigma^2 + \\sigma^2 + ... \\sigma^2}{n^2} \\\\ &= & \\frac{\\sigma^2}{n}. \\end{eqnarray\*}\\$$</span>

Het steekproefgemiddelde heeft dus een spreiding (standaarddeviatie) rond haar gemiddelde <span class="math inline">\$\\mu\$</span> die <span class="math inline">\$\\sqrt{n}\$</span> keer kleiner is dan de deviatie op de oorspronkelijke observaties. Vandaar dat we meer over <span class="math inline">\$\\mu\$</span> kunnen leren door het steekproefgemiddelde <span class="math inline">\$\\bar X\$</span> te observeren dan door een individuele waarde <span class="math inline">\$X\$</span> te observeren.

<span id="def:unnamed-chunk-66" class="definition">**Definitie 5.2 (Standaard error)** </span>De standaarddeviatie van <span class="math inline">\$\\bar{X}\$</span> is <span class="math inline">\$\\sigma/\\sqrt{n}\$</span> en krijgt in de literatuur de speciale naam {standard error} van het gemiddelde. Algemeen noemt men de standaarddeviatie van een schatter voor een bepaalde parameter <span class="math inline">\$\\theta\$</span>, de **standard error** van die schatter. Men noteert dit als <span class="math inline">\$SE\$</span>.

**Einde definitie**

<span id="exm:unnamed-chunk-67" class="example">**Voorbeeld 5.2 (Gemiddelde bloeddrukverandering)** </span>

Stel dat we <span class="math inline">\$n = 15\$</span> systolische bloeddrukobservaties zullen meten en dat de standaarddeviatie van de bloeddrukverschillen in de populatie <span class="math inline">\$\\sigma = 9.0\$</span> mmHg bedraagt, dan is standard error (SE) van de systolische bloeddrukveranderingen <span class="math inline">\$\\bar X\$</span>: <span class="math display">\\$$ SE= \\frac{9.0}{\\sqrt{15}}=2.32\\text{mmHg.} \\$$</span>

Meestal is <span class="math inline">\$\\sigma\$</span>, en bijgevolg de standard error van het steekproefgemiddelde, ongekend. Men moet dan de standard error schatten. Een voor de hand liggende schatter met goede eigenschappen is <span class="math inline">\$S/\\sqrt{n},\$</span> waarbij <span class="math inline">\$S^2\$</span> de *steekproefvariantie* van de reeks observaties <span class="math inline">\$X\_1,...,X\_n\$</span> is en <span class="math inline">\$S\$</span> de *steekproef standaarddeviatie* wordt genoemd.

Voor het captopril voorbeeld kunnen we de standard error op het steekproefgemiddelde van de bloeddrukveranderingen schatten in R als

``` {.sourceCode .r}
n=length(delta)
se=sd(delta)/sqrt(n)
se
```

    ## [1] 2.330883

#### <span class="header-section-number">5.3.2.1</span> Standaarddeviatie vs standard error

Er is vaak nogal wat verwarring over het onderscheid tussen standard error en standaarddeviatie. De standard error verwijst steeds naar de spreiding op een geschatte parameter zoals het steekproefgemiddelde. Omdat een schatting steeds precieser wordt naarmate de steekproef groter wordt, daalt de standard error met stijgende steekproefgrootte <span class="math inline">\$n\$</span>. Als de term standaarddeviatie verwijst naar het steekproefgemiddelde (m.a.w. als men spreekt over de standaarddeviatie van het steekproefgemiddelde), dan is deze standaarddeviatie identiek gelijk aan de standard error. Als ze verwijst naar de individuele observaties, dan niet. Dit kun je ondermeer zien aan het feit dat de individuele observaties niet minder variabel zijn in grote steekproeven dan in kleine steekproeven; m.a.w. de standaarddeviatie van de individuele observaties neemt niet af naarmate de steekproef groter wordt, het is immers een karakteristiek van de populatie.

De standaarddeviatie op de observaties is een maat voor de variabiliteit tussen individuen met betrekking tot een bepaalde meetwaarde. De standaard error van een schatter meet de onzekerheid in die schatter voor een bepaalde parameter.

Beide statistieken worden ook anders beïnvloed door de steekproefgrootte. De variabiliteit in de populatie verandert niet. Buiten het feit dat we de standaarddeviatie meer nauwkeurig kunnen schatten in een grotere steekproef zal ze dus steeds in dezelfde grootteorde liggen. Ze heeft als verwachte waarde immers de theoretische standaarddeviatie <span class="math inline">\$\\sigma\$</span> in de populatie. De standard error van een schatter wordt echter sterk beïnvloed door de steekproefgrootte: hoe groter de steekproef hoe nauwkeuriger de schatter voor een bepaalde parameter en hoe kleiner zijn standard error!

#### <span class="header-section-number">5.3.2.2</span> Geclusterde metingen

De data in studies zijn niet altijd onafhankelijk. Dat heeft zijn consequenties voor het schatten van de standaard errors. Beschouw een studiedesign waarbij voor <span class="math inline">\$n\$</span> planten, tijdens een bepaalde fase in de groei, de expressie van een bepaald gen 2 maal wordt gemeten om meetfouten te drukken. Men is geïnteresseerd in de gemiddelde genexpressie. Als we met <span class="math inline">\$Y\_{i1}\$</span> en <span class="math inline">\$Y\_{i2}\$</span> de eerste en tweede meting, respectievelijk, voorstellen voor plant <span class="math inline">\$i=1,...,n\$</span>, dan kunnen we dit schatten als <span class="math display">\\$$\\begin{equation\*} \\bar Y = \\sum\_{i=1}^n \\frac{Y\_{i1}+Y\_{i2}}{2n} \\end{equation\*}\\$$</span> In de onderstelling dat de <span class="math inline">\$n\$</span> planten onafhankelijk van elkaar gekozen werden en de eerste en tweede metingen even variabel zijn (d.w.z. <span class="math inline">\$\\text{Var}(Y\_{i1})=\\text{Var}(Y\_{i2})=\\sigma^2\$</span>), bedraagt de variantie op dit steekproefgemiddelde <span class="math display">\\$$\\begin{eqnarray\*} \\text{Var}(\\bar Y)&=&\\sum\_{i=1}^n \\frac{\\text{Var}(Y\_{i1}+Y\_{i2})}{4n^2} \\\\ &=&\\sum\_{i=1}^n \\frac{\\sigma^2+\\sigma^2+2\\text{Cor}(Y\_{i1},Y\_{i2})\\sigma^2}{% 4n^2} \\\\ &=&\\frac{\\sigma^2}{2n}\\{1+\\text{Cor}(Y\_{1},Y\_{2})\\} \\end{eqnarray\*}\\$$</span>

Vermits verschillende metingen afkomstig van eenzelfde plant doorgaans positief met elkaar gecorreleerd zijn, is de standard error op <span class="math inline">\$\\bar Y\$</span> dus groter dan wanneer de <span class="math inline">\$2n\$</span> metingen van <span class="math inline">\$2n\$</span> verschillende, onafhankelijke planten afkomstig zouden zijn. Dat is omdat, gegeven de eerste meting <span class="math inline">\$Y\_{i1}\$</span>, de tweede meting <span class="math inline">\$Y\_{i2}\$</span> geen volledig nieuwe informatie toevoegt en er bijgevolg minder informatie beschikbaar is om het gemiddelde te schatten dan wanneer alle gegevens van verschillende planten afkomstig waren. In het bijzonder, wanneer <span class="math inline">\$\\text{Cor}(Y\_{1},Y\_{2})=1\$</span>, dan levert de tweede meting geen nieuwe informatie en bekomt men eenzelfde nauwkeurigheid als wanneer men slechts 1 meting per plant had bekomen. Wanneer <span class="math inline">\$\\text{Cor}(Y\_{1},Y\_{2})=0\$</span>, dan levert de tweede meting volledig nieuwe informatie en bekomt men eenzelfde nauwkeurigheid als wanneer men 1 meting had bekomen voor <span class="math inline">\$2n\$</span> i.p.v. <span class="math inline">\$n\$</span> verschillende planten. Vermits <span class="math display">\\$$\\frac{\\sigma^2}{2n}\\{1+\\text{Cor}(Y\_{1},Y\_{2})\\}\\geq \\frac{\\sigma^2}{2n}\\$$</span>

*Wanneer de correlatie tussen herhaalde genexpressie metingen positief is (hetgeen we verwachten), zal men in de praktijk meer preciese resultaten bekomen door 1 meting te bepalen voor <span class="math inline">\$2n\$</span> verschillende planten dan door 2 metingen te bepalen voor <span class="math inline">\$n\$</span> verschillende planten.*

De metingen in de captopril voorbeeld zijn eveneens geclusterd. We hebben immers twee systolische bloeddrukmetingen per patiënt. 1 meting voor en 1 meting na het toedienen van captopril. We beogen om de gemiddelde bloeddrukverandering <span class="math inline">\$\\mu\$</span> te schatten a.d.h.v. de gegevens <span class="math display">\\$$(Y\_{i1} , Y\_{i2}),\\$$</span> voor subjecten <span class="math inline">\$i = 1, ..., n\$</span>. En we bekomen de volgende schatting: <span class="math display">\\$$\\bar X = \\sum\_{i=1}^n \\frac{Y\_{i2}-Y\_{i1}}{n}\\$$</span>

Uit de rekenregels voor de variantie weten we dat <span class="math display">\\$$\\begin{eqnarray\*} \\text{Var}\\left\[\\bar X\\right$$&=&\\sum\_{i=1}^n \\frac{\\text{Var}\\left$$Y\_{i1}-Y\_{i2}\\right$$}{n^2}\\\\ &=&\\sum\_{i=1}^n \\frac{\\sigma^2\_1+\\sigma^2\_2-2\\text{Cor}\\left$$Y\_{i1},Y\_{i2}\\right$$\\sigma\_1\\sigma\_2}{n^2}\\\\ &=&\\frac{\\sigma^2\_1+\\sigma^2\_2-2\\text{Cor}\\left$$Y\_{i1},Y\_{i2}\\right$$\\sigma\_1\\sigma\_2}{n},\\\\ \\end{eqnarray\*}\\\]</span>

In R kunnen we dit als volgt berekenen:

``` {.sourceCode .r}
#functie var op een matrix berekent varianties sigma_1^2, sigma_2^2
#covariantie sigma_{12}
vars=var(captopril[,c("SBPb","SBPa")])
vars
```

    ##          SBPb     SBPa
    ## SBPb 422.9238 370.7857
    ## SBPa 370.7857 400.1429

``` {.sourceCode .r}
cor(captopril$SBPa,captopril$SBPb)
```

    ## [1] 0.9013312

``` {.sourceCode .r}
varXbarDelta=(vars[1,1]+vars[2,2]-2*vars[1,2])/15
sqrt(varXbarDelta)
```

    ## [1] 2.330883

We zien dat de metingen heel sterk gecorreleerd zijn, waardoor de variantie op het verschil veel lager zal liggen dan op de originele metingen.

Gezien we voor elke patiënt twee metingen hebben bestaat een alternatieve methode om de standard error te bepalen erin om alle gecorreleerde metingen tot 1 meting te reduceren. Merk op dat we dit enkel kunnen doen voor gepaarde metingen. Alle resulterende metingen zijn dan onafhankelijk. Concreet kunnen we voor elke patiënt <span class="math inline">\$i\$</span> in de steekproef het bloeddrukverschil berekenen: <span class="math display">\\$$X\_{i}=Y\_{ai}-Y\_{bi}\\$$</span> en vervolgens standard error op <span class="math inline">\$\\bar X\$</span>. In het captopril voorbeeld wordt de schatting

``` {.sourceCode .r}
sd(delta)/sqrt(15)
```

    ## [1] 2.330883

We zien dat we exact dezelfde schatting voor de standard error bekomen. Verder zien we ook dat het design een groot voordeel heeft: Aangezien de bloeddrukmetingen voor en na het toedienen van captopril sterk positief gecorreleerd zijn is de variantie van het verschil veel lager dan deze op de originele bloeddrukmetingen. Iedere patiënt in de studie dient immers als zijn eigen controle en op die manier kunnen we de variabiliteit in de bloeddrukmetingen tussen patiënten uit de analyse verwijderen!

#### <span class="header-section-number">5.3.2.3</span> Normaal verdeelde gegevens

Als de gegevens Normaal verdeeld zijn, dan zijn er meerdere onvertekende schatters voor het populatiegemiddelde <span class="math inline">\$\\mu\$</span>, bvb. het steekproefgemiddelde en de mediaan. Men kan echter aantonen dat in dat geval het steekproefgemiddelde <span class="math inline">\$\\bar{X}\$</span> de onvertekende schatter is voor <span class="math inline">\$\\mu\$</span> met de kleinste standard error. Dat betekent dat ze gemiddeld minder afwijkt van de echte parameterwaarde dan de mediaan, die veel meer varieert van steekproef tot steekproef. Het steekproefgemiddelde is bijgevolg een schatter die accuraat is (want onvertekend) en meest precies (kleinste standaarddeviatie).

### <span class="header-section-number">5.3.3</span> Verdeling van het steekproefgemiddelde {#verdeling-van-het-steekproefgemiddelde}

Om ondermeer goed de betekenis van de standard error te kunnen vatten, moeten we van <span class="math inline">\$\\bar X\$</span> niet alleen het gemiddelde en de standaarddeviatie, maar ook de exacte verdeling kennen. De standard error is immers een standaardeviatie (bvb. van het steekproefgemiddelde), waarvan de betekenis het meest duidelijk is wanneer de metingen (in dit geval, het steekproefgemiddelde) Normaal verdeeld zijn. In het bijzonder geval dat de individuele observaties <span class="math inline">\$X\_i\$</span> een Normale verdeling hebben met gemiddelde <span class="math inline">\$\\mu\$</span> en variantie <span class="math inline">\$\\sigma^2\$</span>, kan men aantonen dat ook <span class="math inline">\$\\bar X\$</span> Normaal verdeeld is met gemiddelde <span class="math inline">\$\\mu\$</span> en variantie <span class="math inline">\$\\sigma^2/n.\$</span> Dit fenomeen wordt geïllustreerd in Figuur [5.7](index.md). De linkse figuur illustreert een lukrake trekking of steekproef van observaties uit een Normale verdeling. Als men dit blijft herhalen en voor alle bekomen steekproeven het steekproefgemiddelde berekent en en vervolgens deze gemiddeldes uitzet in een histogram, dan krijgt men het histogram uit rechtse figuur. De steekproefgemiddeldes in deze figuur lijken inderdaad een Normale verdeling te volgen.

<span id="fig:meansim"></span> <img src="Statistiek_2019_2020_files/figure-html/meansim-1.png" style="width:100.0%" alt="Simulaties van steekproeven met n=15 observaties uit een normale verdeling met gemiddelde systolische bloeddrukdaling 19 mmHg en standaard deviate van 9 mmHg. (links één steekproef, rechts een histogram van steekproefgemiddelden voor 1000 steekproeven. Het gemiddelde in de populatie is weergegeven d.m.v. rode lijn)." />

Figuur 5.7: Simulaties van steekproeven met n=15 observaties uit een normale verdeling met gemiddelde systolische bloeddrukdaling 19 mmHg en standaard deviate van 9 mmHg. (links één steekproef, rechts een histogram van steekproefgemiddelden voor 1000 steekproeven. Het gemiddelde in de populatie is weergegeven d.m.v. rode lijn).

In het captopril voorbeeld zagen we dat de systolische bloeddrukverandering approximatief normaal verdeeld is. De standard error op de bloeddrukverandering bedroeg 2.32 mm Hg. Dus op 100 studies met n = 15 subjecten, verwachten we dat de geschatte gemiddelde systolische bloeddrukafwijking (<span class="math inline">\$\\bar X\$</span>) op minder dan 2 × 2.32 = 4.64mm Hg van het werkelijke populatiegemiddelde (<span class="math inline">\$\\mu\$</span>) ligt in 95 studies.

In het algemeen, wanneer de individuele observaties <span class="math inline">\$X\_i\$</span> geen Normale verdeling hebben, is <span class="math inline">\$\\bar X\$</span> toch nog Normaal verdeeld zodra het aantal observaties groot genoeg is. Hoe groot de steekproef hiervoor moet zijn, hangt hierbij af van hoe scheef de verdeling van de oorspronkelijke observaties is. Dat is het gevolg van de volgende fundamentele en veel toegepaste wiskundestelling.

**De Centrale Limietstelling (CLT)**

Stel dat <span class="math inline">\$X\_1, X\_2, \\dots, X\_n, \\; n\$</span> onafhankelijke lukrake trekkingen van de toevalsveranderlijke <span class="math inline">\$X\$</span> voorstellen, met allen dezelfde theoretische verdeling. Laat <span class="math inline">\$X\$</span> gemiddelde <span class="math inline">\$\\mu\$</span> en variantie <span class="math inline">\$\\sigma^2\$</span> hebben maar verder een ongespecifieerde verdeling, dan wordt de verdeling van het steekproefgemiddelde <span class="math inline">\$\\bar{X}\_n = {\\sum\_{i=1}^{n} X\_i}/{n}\$</span> naarmate <span class="math inline">\$n\$</span> groter wordt steeds beter benaderd door de Normale verdeling met gemiddelde <span class="math inline">\$\\mu\$</span> en variantie <span class="math inline">\$\\sigma^2/n.\$</span>

**Einde Stelling**

Deze belangrijke eigenschap zal ons toelaten om de meeste technieken die in deze cursus aan bod komen toe te passen op een zeer uitgebreid spectrum van experimenten.

We illustreren deze stelling in Figuur [5.8](index.md). We simuleren data uit een experiment waarbij we een munt opwerpen. De data zijn dan Bernouilli verdeeld en kunnen de waarde <span class="math inline">\$X=0\$</span> (munt) of <span class="math inline">\$X=1\$</span> (kop) aannemen met een kans van 50% en zijn duidelijk niet-Normaal verdeeld. We simuleren steekproeven met een steekproefgrootte van 10 observaties en 100 observaties en onderzoeken de verdeling van het steekproefgemiddelde voor elke steekproefgrootte. We zien duidelijk dat CLT niet van toepassing is bij een steekproefgrootte van 10. Voor steekproeven met 100 observaties zien we dat de verdeling van het steekproefgemiddelde al beter benaderd kan worden door een Normale verdeling.

<span id="fig:CLT"></span> <img src="Statistiek_2019_2020_files/figure-html/CLT-1.png" style="width:100.0%" alt="Illustratie van de Centrale Limietstelling d.m.v. Bernouilli verdeelde gegevens (opwerpen van een muntstuk) Steekproefgroottes (n=10, links, en n=100, rechts). Densiteit van de normale verdeling worden weergegeven in rood. We zien duidelijk dat CLT niet van toepassing is bij een steekproefgrootte van 10. Voor steekproeven met 100 observaties zien we dat de verdeling van het steekproefgemiddelde al beter benaderd kan worden door een Normale verdeling." />

Figuur 5.8: Illustratie van de Centrale Limietstelling d.m.v. Bernouilli verdeelde gegevens (opwerpen van een muntstuk) Steekproefgroottes (n=10, links, en n=100, rechts). Densiteit van de normale verdeling worden weergegeven in rood. We zien duidelijk dat CLT niet van toepassing is bij een steekproefgrootte van 10. Voor steekproeven met 100 observaties zien we dat de verdeling van het steekproefgemiddelde al beter benaderd kan worden door een Normale verdeling.

---

[← 5.2 Captopril voorbeeld](02-5-2-captopril-voorbeeld.md) · [Up: contents](index.md) · [5.4 Intervalschatters →](04-5-4-intervalschatters.md)

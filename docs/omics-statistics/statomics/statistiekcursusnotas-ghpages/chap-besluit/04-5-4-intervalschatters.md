---
title: 5.4 Intervalschatters
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-besluit.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 5.4 Intervalschatters

**Source:** [`chap-besluit.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

In de vorige sectie hebben we vastgesteld dat het steekproefgemiddelde van steekproef tot steekproef varieert rond het populatiegemiddelde dat we willen schatten. Om die reden wensen we in deze sectie een interval rond het steekproefgemiddelde te bepalen waarbinnen we het populatiegemiddelde met gegeven kans (bvb. 95% kans) kunnen verwachten. In Sectie [5.4.1](index.md) zullen we dit uitwerken voor het geval waar de populatievariantie <span class="math inline">\$\\sigma^2\$</span> op de metingen gekend is. Deze onderstelling is meestal onredelijk<a href="#fn28" id="fnref28" class="footnoteRef"><sup>28</sup></a>, maar wordt hier gemaakt om redenen van eenvoud. In Sectie [5.4.2](index.md) zullen we van deze onderstelling afstappen.

### <span class="header-section-number">5.4.1</span> Gekende variantie op de metingen {#gekende-variantie-op-de-metingen}

Wanneer de individuele observaties <span class="math inline">\$X\$</span> Normaal verdeeld zijn met gemiddelde <span class="math inline">\$\\mu\$</span> en gekende variantie <span class="math inline">\$\\sigma^2\$</span>, noteren we dat als volgt: <span class="math inline">\$X\\sim N(\\mu,\\sigma^2)\$</span>. Uit vorige sectie volgt dan dat het steekproefgemiddelde <span class="math inline">\$\\bar{X}\$</span> eveneens Normaal verdeeld is volgens <span class="math inline">\$N(\\mu,\\sigma^2/n)\$</span>. Een 95% referentie-interval voor het steekproefgemiddelde ziet er bijgevolg uit als

<span class="math display">\\$$\\begin{equation\*} \\left\[\\mu - 1.96 \\frac{\\sigma}{\\sqrt{n}},\\mu + 1.96 \\frac{\\sigma}{\\sqrt{n}}% \\right$$ \\end{equation\*}\\\]</span> Het bevat met 95% kans het steekproefgemiddelde van een lukrake steekproef. Dit interval kunnen we niet expliciet berekenen op basis van de geobserveerde gegevens, omdat <span class="math inline">\$\\mu\$</span> ongekend is (we gaan er hier voorlopig van uit dat <span class="math inline">\$\\sigma\$</span> wel gekend is). Het kan wel geschat worden als <span class="math display">\\$$\\begin{equation\*} \\left\[\\bar X - 1.96 \\frac{\\sigma}{\\sqrt{n}},\\bar X + 1.96 \\frac{\\sigma}{\\sqrt{n}}\\right$$ \\end{equation\*}\\\]</span> Hoewel dit laatste interval nog steeds kan geïnterpreteerd worden als een referentie-interval voor het steekproefgemiddelde, kunnen we er een veel nuttigere interpretatie aan geven. Immers, de ongelijkheid <span class="math inline">\$\\mu - 1.96 \\ \\sigma/\\sqrt{n} &lt; \\bar{X}\$</span> kan equivalent worden herschreven als <span class="math inline">\$\\mu &lt; \\bar{X} + 1.96 \\ \\sigma/\\sqrt{n}\$</span>. Hieruit volgt: <span class="math display">\\$$\\begin{eqnarray\*} 95\\% &=& P( \\mu - 1.96 \\ \\sigma/\\sqrt{n} &lt; \\bar{X} &lt; \\mu + 1.96 \\ \\sigma/\\sqrt{n} ) \\\\ &=&P( \\bar{X} - 1.96 \\ \\sigma/\\sqrt{n} &lt; \\mu &lt; \\bar{X} + 1.96 \\ \\sigma/\\sqrt{n} ) \\end{eqnarray\*}\\$$</span>

Dit leidt tot volgende definitie.

<span id="def:unnamed-chunk-71" class="definition">**Definitie 5.3 (95<span class="math inline">\$\\%\$</span> betrouwbaarheidsinterval voor populatiegemiddelde)** </span>Het interval <span id="eq:bi" class="math display">\\$$\\begin{equation} \[\\bar{X} - 1.96 \\ \\sigma/\\sqrt{n} , \\bar{X} + 1.96 \\ \\sigma/\\sqrt{n} $$, \\tag{5.1} \\end{equation}\\\]</span>

bevat met 95% kans het populatiegemiddelde <span class="math inline">\$\\mu\$</span>. Het wordt een **95% betrouwbaarheidsinterval** (in het Engels: *95% confidence interval*) voor het populatiegemiddelde <span class="math inline">\$\\mu\$</span> genoemd. De kans dat het de populatieparameter <span class="math inline">\$\\mu\$</span> bevat, d.i. 95%, wordt het *betrouwbaarheidsniveau* genoemd.

**Einde definitie**

Een 95% betrouwbaarheidsinterval bepaalt met andere woorden een reeks waarden waarbinnen de gezochte populatieparameter *waarschijnlijk* (namelijk met 95% kans) valt.

Stel dat we in een steekproef een bloeddrukdaling van -18.93mmHg observeren en dat we weten dat de standaarddeviatie van de bloeddrukmetingen 9mmHg bedraagt. Dan vinden we een betrouwbaarheidsinterval voor de gemiddelde bloeddrukdaling van <span class="math inline">\$\\left$$-18.93-1.96\\times 9/\\sqrt{15},-18.9+1.95\\times 9/\\sqrt{15}\\right$$=\$</span>$$-23.48,-14.38$$mmHg.

De reden waarom over “95% kans” gesproken wordt, is omdat de eindpunten van het 95% betrouwbaarheidsinterval toevalsveranderlijken zijn die variëren van steekproef tot steekproef. Met andere woorden, verschillende steekproeven leveren telkens andere betrouwbaarheidsintervallen op, vermits die intervallen berekend zijn op basis van de gegevens in de steekproef. Men noemt het om die reden *stochastische intervallen*. Voor 95% van alle steekproeven zal het berekende 95% betrouwbaarheidsinterval de gezochte waarde van de populatieparameter bevatten, en voor de overige 5% niet. Dat wordt geïllustreerd a.d.h.v. een simulatiestudie in Sectie [5.4.3](index.md) (nadat we de intervallen hebben uitgebreid voor de meer realistische setting waarbij de variantie in de populatie ongekend is).

Uiteraard kunnen de onderzoekers o.b.v. een gegeven betrouwbaarheidsinterval niet besluiten of het de gezochte parameterwaarde bevat of niet, vermits ze precies op zoek zijn naar die onbekende waarde. Maar ze gebruiken een procedure die in 95% van de gevallen werkt; m.a.w. die in 95% van de gevallen de gezochte waarde bevat. Of nog, als men dagelijks gegevens zou verzamelen en telkens een 95% betrouwbaarheidsinterval zou berekenen voor een nieuwe parameter <span class="math inline">\$\\theta\$</span> (bvb. een odds ratio), dan zou men op lange termijn in 95% van de gevallen de gezochte waarde omvat hebben.

Tot nog toe zijn we ervan uitgegaan dat de individuele observaties Normaal verdeeld zijn en dat hun variantie gekend is (want als de variantie <span class="math inline">\$\\sigma^2\$</span> niet gekend is, kan men de grenzen van het interval niet berekenen). Wegens de Centrale Limietstelling bevat Vergelijking [(5.1)](index.md) het gemiddelde <span class="math inline">\$\\mu\$</span> bij benadering met 95% kans wanneer de steekproef groot is en de variantie van de individuele observaties gekend, maar hun verdeling ongekend is.

Wanneer bovendien de variantie ongekend is, kan me ze schatten door gebruik te maken van de steekproefvariantie <span class="math inline">\$S^2\$</span> van de reeks observaties <span class="math inline">\$X\_1,...,X\_n\$</span>. Men kan aantonen dat het interval <span class="math inline">\$$$\\bar{X} - 1.96 \\ s/\\sqrt{n} , \\bar{X} + 1.96 \\ s/\\sqrt{n} $$\$</span> dan het populatiegemiddelde met bij benadering 95% kans bevat, op voorwaarde dat de steekproef groot is. In de volgende sectie gaan we na hoe een betrouwbaarheidsinterval voor het populatiegemiddelde geconstrueerd kan worden wanneer de variantie ongekend is en de steekproef relatief klein.

Om een betrouwbaarheidsinterval met een ander betrouwbaarheidsniveau, <span class="math inline">\$(1- \\alpha)100\\%\$</span> te construeren, vervangt men 1.96 door het relevante kwantiel <span class="math inline">\$z\_{\\alpha/2}.\$</span>

De breedte van een <span class="math inline">\$100\\%(1-\\alpha)\$</span> betrouwbaarheidsinterval voor een populatiegemiddelde <span class="math inline">\$\\mu\$</span> is <span class="math inline">\$2 z\_{\\alpha/2} \\ \\sigma/\\sqrt{n}\$</span>. Ze wordt dus bepaald door 3 factoren: de standaarddeviatie op de individuele observaties, <span class="math inline">\$\\sigma\$</span>, de grootte van de steekproef, <span class="math inline">\$n\$</span>, en het betrouwbaarheidsniveau, <span class="math inline">\$1-\\alpha\$</span>:

- <span class="math inline">\$n\$</span>: naarmate de steekproefgrootte toeneemt, krimpt het betrouwbaarheidsinterval. In grote steekproeven beschikken we immers over veel informatie en kunnen we de gezochte populatieparameter bijgevolg relatief nauwkeurig afschatten.

- <span class="math inline">\$\\sigma\$</span>: naarmate de standaarddeviatie van de oorspronkelijke observaties toeneemt, neemt de lengte van het betrouwbaarheidsinterval toe. Indien er immers veel ruis op de gegevens zit, dan is het moeilijker om populatieparameters of -kenmerken te identificeren.

- <span class="math inline">\$1-\\alpha\$</span>: naarmate het betrouwbaarheidsniveau toeneemt, wordt het betrouwbaarheidsinterval breder. Indien we immers eisen dat het interval met 99.9% kans de populatiewaarde bevat i.p.v. met 80% kans, dan zullen we duidelijk een breder interval nodig hebben.

Betrouwbaarheidsintervallen worden niet enkel gebruikt voor het populatiegemiddelde, maar kunnen in principe voor om het even welke populatieparameter worden gedefinieerd. Zo kunnen ze bijvoorbeeld gedefinieerd worden voor een verschil tussen 2 gemiddelden, voor een odds ratio, voor een variantie, … De manier om die intervallen te berekenen is vaak complex en sterk afhankelijk van de gebruikte schatter voor de populatieparameter. Er wordt daarom niet van u verwacht dat u voor alle populatieparameters die we in deze cursus ontmoeten, een betrouwbaarheidsinterval kunt berekenen, maar wel dat u het kunt interpreteren.

<span id="def:unnamed-chunk-72" class="definition">**Definitie 5.4 (Betrouwbaarheidsinterval)** </span>Een **<span class="math inline">\$(1-\\alpha)100\$</span>% betrouwbaarheidsinterval** voor een populatieparameter <span class="math inline">\$\\theta\$</span> is een geschat (en bijgevolg stochastisch) interval dat met <span class="math inline">\$(1-\\alpha)100\$</span>% kans de echte waarde van die populatieparameter <span class="math inline">\$\\theta\$</span> bevat.

**Einde Definitie**

### <span class="header-section-number">5.4.2</span> Ongekende variantie op de metingen {#ongekende-variantie-op-de-metingen}

Tot nog toe werd verondersteld dat de populatievariantie <span class="math inline">\$\\sigma^2\$</span> gekend is bij het berekenen van een betrouwbaarheidsinterval voor <span class="math inline">\$\\mu\$</span>. Betrouwbaarheidsintervallen voor <span class="math inline">\$\\mu\$</span> werden dan opgebouwd door op te merken dat de gestandaardiseerde waarde <span class="math inline">\$(\\bar{X} - \\mu)/(\\sigma/\\sqrt{n})\$</span> standaardnormaal verdeeld is en bijgevolg <span class="math display">\\$$\\begin{equation\*} \\left\[\\mu - 1.96 \\frac{\\sigma}{\\sqrt{n}},\\mu + 1.96 \\frac{\\sigma}{\\sqrt{n}}% \\right$$ \\end{equation\*}\\\]</span>

een 95% referentie-interval voor het steekproefgemiddelde voorstelt.

In de praktijk komt het quasi nooit voor dat men de populatievariantie <span class="math inline">\$\\sigma^2\$</span> exact kent. In de praktijk wordt deze geschat als <span class="math inline">\$S^2\$</span> op basis van de voorhanden zijnde steekproef. Als gevolg hiervan zullen de betrouwbaarheidsintervallen uit voorgaande sectie doorgaans iets te smal zijn (omdat ze er geen rekening mee houden dat ook de variantie werd geschat) en is het noodzakelijk om bij de berekening <span class="math inline">\$(\\bar{X} - \\mu)/(S/\\sqrt{n})\$</span> te gebruiken als gestandaardiseerde waarde i.p.v. <span class="math inline">\$(\\bar{X} - \\mu)/(\\sigma/\\sqrt{n})\$</span>. Wanneer de steekproef voldoende groot is, ligt de vierkantswortel van variantie <span class="math inline">\$S^2\$</span> voldoende dicht bij <span class="math inline">\$\\sigma\$</span> zodat <span class="math inline">\${(\\bar{X} - \\mu)}/{(S/\\sqrt{n}) }\$</span> bij benadering een standaardnormale verdeling volgt en, bijgevolg, <span class="math display">\\$$\\begin{equation\*} \\left\[\\bar{X} - z\_{\\alpha/2} \\ \\frac{S}{\\sqrt{n}} , \\bar{X} + z\_{\\alpha/2} \\ \\frac{S}{\\sqrt{n}}\\right$$ \\end{equation\*}\\\]</span>

een benaderd <span class="math inline">\$(1- \\alpha)100\\%\$</span> betrouwbaarheidsinterval is voor <span class="math inline">\$\\mu\$</span>. Voor kleine steekproeven is dit niet langer het geval. Daardoor introduceert men een extra onnauwkeurigheid in de gestandaardiseerde waarde <span class="math inline">\${(\\bar{X} - \\mu)}/{(S/\\sqrt{n})}\$</span>. Deze is nog wel gecentreerd rond nul en symmetrisch, maar niet langer Normaal verdeeld. De echte verdeling voor eindige steekproefgrootte <span class="math inline">\$n\$</span> heeft zwaardere staarten dan de Normale. Hoeveel zwaarder de staarten zijn, hangt van de steekproefgrootte <span class="math inline">\$n\$</span> af. Als <span class="math inline">\$n\$</span> oneindig groot wordt, komt <span class="math inline">\$S\$</span> zodanig dicht bij <span class="math inline">\$\\sigma\$</span> te liggen dat de extra onnauwkeurigheid in de gestandaardiseerde waarde verwaarloosbaar is en bijgevolg ook het verschil met de Normale verdeling. Maar voor relatief kleine steekproeven hangt de verdeling van <span class="math inline">\${(\\bar{X} - \\mu)}/({S/\\sqrt{n}})\$</span> af van de grootte <span class="math inline">\$n\$</span> van de steekproef. Ze krijgt de naam (Student) <span class="math inline">\$t\$</span>-verdeling met <span class="math inline">\$n-1\$</span> vrijheidsgraden (in het Engels: *degrees of freedom*). Deze verdeling wordt voor een aantal verschillende vrijheidsgraden geïllustreerd in Figuur [5.9](index.md). De t-verdelingen in de figuur hebben duidelijk bredere staarten dan de normaalverdeling, waardoor ze ook een grotere percentielwaarden hebben voor een vooropgesteld betrouwbaarheidsniveau. Dat zal leiden tot bredere intervallen, wat logisch is aangezien we de extra onzekerheid inbouwen die gerelateerd is aan het schatten van de standaarddeviatie.

<span id="def:unnamed-chunk-73" class="definition">**Definitie 5.5 (t-verdeling)** </span>Als <span class="math inline">\$X\_1, X\_2, ..., X\_n\$</span> een steekproef vormen uit de Normale verdeling <span class="math inline">\$N(\\mu, \\sigma^2)\$</span>, dan is <span class="math inline">\$(\\bar{X} - \\mu)/(S/\\sqrt{n})\$</span> verdeeld als een <span class="math inline">\$t\$</span>-verdeling met <span class="math inline">\$n-1\$</span> vrijheidsgraden.

\*\*Einde Definitie

``` {.sourceCode .r}
grid=seq(-5,5,.1)
plot(grid,dnorm(grid),ylab="densiteit",xlab="X",type="l",lwd=2)
dfs=c(2,5,14)
for (i in 1:length(dfs))
     lines(grid,dt(grid,dfs[i]),col=i+1,lwd=2)
legend("topright",lty=1,col=1:4,legend=c("N(X,mean=0,sd=1)",paste0("t(X,df=",dfs,")")))
```

<span id="fig:tdist"></span> <img src="Statistiek_2019_2020_files/figure-html/tdist-1.png" style="width:100.0%" alt="Normale verdeling en t-verdeling met verschillende vrijheidsgraden." />

Figuur 5.9: Normale verdeling en t-verdeling met verschillende vrijheidsgraden.

Percentielen van de <span class="math inline">\$t\$</span>-verdeling kunnen niet met de hand berekend worden, maar kan men voor de verschillende waarden van <span class="math inline">\$n\$</span> aflezen in Tabellen of berekenen in R. In de onderstaande code wordt het 95%, 97.5%, 99.5% percentiel berekend voor een t-verdeling met 14 vrijheidsgraden, die gebruik kunnen worden voor de berekening van 90%, 95% en 99% betrouwbaarheidsintervallen.

``` {.sourceCode .r}
qt(.975,df=14)
```

    ## [1] 2.144787

``` {.sourceCode .r}
qt(c(.95,.975,.995),df=14)
```

    ## [1] 1.761310 2.144787 2.976843

We zien dat het 97.5% percentiel 2.14 voor een t-verdeling met <span class="math inline">\$n-1=14\$</span> vrijheidsgraden inderdaad groter is dan het kwantiel uit de normaal verdeling 1.96.

Een gelijkaardige logica als voor de Normale verdeling met gekende variantie, geeft dan aan dat een <span class="math inline">\$100\\% (1-\\alpha)\$</span> betrouwbaarheidsinterval voor het gemiddelde <span class="math inline">\$\\mu\$</span> van een Normaal verdeelde veranderlijke <span class="math inline">\$X\$</span> met onbekende variantie kan berekend worden als <span class="math display">\\$$\\begin{equation\*} \\left\[\\bar{X} - t\_{n-1, \\alpha/2} \\frac{s}{\\sqrt{n}} , \\bar{X} + t\_{n-1, \\alpha/2} \\frac{s}{\\sqrt{n}}\\right$$ \\end{equation\*}\\\]</span>

Deze uitdrukking verschilt van deze in de vorige sectie doordat het <span class="math inline">\$(1-\\alpha/2)100\\%\$</span> percentiel van de Normale verdeling wordt vervangen door het <span class="math inline">\$(1-\\alpha/2)100\\%\$</span> percentiel van de t-verdeling met <span class="math inline">\$n-1\$</span> vrijheidsgraden.

Voor het captopril voorbeeld kunnen we dus een 95% betrouwbaarheidsinterval bekomen door

``` {.sourceCode .r}
mean(delta) -  qt(.975,df=14)*sd(delta)/sqrt(n)
```

    ## [1] -23.93258

``` {.sourceCode .r}
mean(delta) + qt(.975,df=14)*sd(delta)/sqrt(n)
```

    ## [1] -13.93409

Een 99% betrouwbaarheidsinterval voor gemiddelde bloeddrukverandering wordt als volgt bekomen:

``` {.sourceCode .r}
mean(delta) -  qt(.995,df=14)*sd(delta)/sqrt(n)
```

    ## [1] -25.87201

``` {.sourceCode .r}
mean(delta) + qt(.995,df=14)*sd(delta)/sqrt(n)
```

    ## [1] -11.99466

### <span class="header-section-number">5.4.3</span> Interpretatie van betrouwbaarheidsintervallen {#interpretatie-van-betrouwbaarheidsintervallen}

We zullen de interpretatie van betrouwbaarheidsintervallen weergegeven a.d.h.v. een simulatie studie waarbij we 1000 herhaalde steekproeven simuleren met 15 observaties uit een normaal verdeling. De gemiddelde bloeddrukdaling in de populatie bedraagt -18.9 mmHg en de standaarddeviate 9.0 mmHg. We houden voor elke steekproef volgende gegevens bij: het gemiddelde, de ondergrens en bovengrens van het BI en of het BI het werkelijke gemiddelde.

``` {.sourceCode .r}
set.seed(115)
mu <- -18.9
sigma <- 9.0
nSim <- 1000
alpha <- 0.05
n <- 15
muHat <- sigmaHat <- BI.ondergrens <- BI.bovengrens <- omvat <- array(dim=nSim)
cnt<-0
for(i in 1:nSim) {
  y<-rnorm(n,mean=mu,sd=sigma)
  muHat[i]<-mean(y)
  sigmaHat[i]<-sd(y)/sqrt(n)
  BI.ondergrens[i]<-muHat[i]-qt(1-alpha/2,df=n-1)*sigmaHat[i]
   BI.bovengrens[i]<-muHat[i]+qt(1-alpha/2,df=n-1)*sigmaHat[i]
  omvat[i]<-(mu<BI.bovengrens[i])&(BI.ondergrens[i]<mu)
  cnt<-cnt+as.numeric(omvat[i])
 }
 cnt/nSim
```

    ## [1] 0.951

Op basis van de 1000 herhaalde steekproeven van de simulatiestudie zien we dat voor 95.1% van de steekproeven de intervallen het werkelijke populatiegemiddelde bevat<a href="#fn29" id="fnref29" class="footnoteRef"><sup>29</sup></a>. De simulatiestudie toont dus op een empirische wijze aan dat de constructie correct is. Het demonstreert bovendien de interpretatie van probabiliteit via herhaalde steekproefname. In Figuur [5.10](index.md) wordt de interpretatie ook grafisch weergegeven voor de eerste 100 gesimuleerde steekproeven. De figuur toont duidelijk aan dat het werkelijke populatiegemiddelde vast is maar ongekend. Het wordt geschat aan de hand van het steekproefgemiddelde dat at random varieert van steekproef tot steekproef rond het werkelijk gemiddelde. We zien ook dat de grenzen van de betrouwbaarheidsintervallen variëren van steekproef tot steekproef. Daarnaast varieert de breedte van de betrouwbaarheidsintervallen eveneens omdat de steekproefstandaarddeviatie eveneens varieert van steekproef tot steekproef<a href="#fn30" id="fnref30" class="footnoteRef"><sup>30</sup></a>.

In de praktijk zullen we op basis van 1 steekproef besluiten dat het betrouwbaarheidsinterval het populatiegemiddelde bevat en we weten dat dergelijke uitspraken met een kans van <span class="math inline">\$1-\\alpha\$</span> (hier 95%) correct zijn.

<span id="fig:biInterpret"></span> <img src="Statistiek_2019_2020_files/figure-html/biInterpret-1.png" style="width:100.0%" alt="Interpretatie van 95$\%$ betrouwbaarheidintervallen. Resultaten op basis van 100 gesimuleerde steekproeven. We zien in de figuur duidelijk dat het populatiegemiddelde vast is maar ongekend (blauwe lijn) en dat de bovengrens en ondergrens van betrouwbaarheidsintervallen voor het populatiegemiddelde varieert van steekproef tot steekproef. Van de 100 betrouwbaarheidsintervallen die worden geplot bevatten 95 intervallen het werkelijke steekproef gemiddelde (zwarte BIs). Voor 5 intervallen is dat niet het geval (rode BIs)." />

Figuur 5.10: Interpretatie van 95<span class="math inline">\$\\%\$</span> betrouwbaarheidintervallen. Resultaten op basis van 100 gesimuleerde steekproeven. We zien in de figuur duidelijk dat het populatiegemiddelde vast is maar ongekend (blauwe lijn) en dat de bovengrens en ondergrens van betrouwbaarheidsintervallen voor het populatiegemiddelde varieert van steekproef tot steekproef. Van de 100 betrouwbaarheidsintervallen die worden geplot bevatten 95 intervallen het werkelijke steekproef gemiddelde (zwarte BIs). Voor 5 intervallen is dat niet het geval (rode BIs).

We zullen nu de simulatie herhalen, maar zullen het aantal observaties in de steekproef verdubbelen.

``` {.sourceCode .r}
mu <- -18.9
sigma <- 9.0
nSim <- 1000
alpha <- 0.05
n <- 30
muHat <- sigmaHat <- BI.ondergrens <- BI.bovengrens <- omvat <- array(dim=nSim)
cnt<-0
for(i in 1:nSim) {
  y<-rnorm(n,mean=mu,sd=sigma)
  muHat[i]<-mean(y)
  sigmaHat[i]<-sd(y)/sqrt(n)
  BI.ondergrens[i]<-muHat[i]-qt(1-alpha/2,df=n-1)*sigmaHat[i]
   BI.bovengrens[i]<-muHat[i]+qt(1-alpha/2,df=n-1)*sigmaHat[i]
  omvat[i]<-(mu<BI.bovengrens[i])&(BI.ondergrens[i]<mu)
  cnt<-cnt+as.numeric(omvat[i])
 }
 cnt/nSim
```

    ## [1] 0.949

We zien een coverage van 94.9% wat opnieuw dicht ligt bij de nominale coverage van 95%.

Wanneer we opnieuw de eerste 100 betrouwbaarheidsintervallen plotten (Figuur [5.11](index.md)) merken we op dat de intervallen smaller zijn dan in Figuur [5.10](index.md) (waarom is dat het geval, ga zelf na met welke factor de intervallen ongeveer versmallen?)

<span id="fig:biInterpretLargeSample"></span> <img src="Statistiek_2019_2020_files/figure-html/biInterpretLargeSample-1.png" style="width:100.0%" alt="Interpretatie van 95$\%$ betrouwbaarheidintervallen. Resultaten op basis van 100 gesimuleerde steekproeven. We zien in de figuur duidelijk dat het populatiegemiddelde vast is maar ongekend (blauwe lijn) en dat de bovengrens en ondergrens van betrouwbaarheidsintervallen voor het populatiegemiddelde varieert van steekproef tot steekproef. Van de 100 betrouwbaarheidsintervallen die worden geplot bevatten 95 intervallen het werkelijke steekproef gemiddelde (zwarte BIs). Voor 5 intervallen is dat niet het geval (rode BIs)." />

Figuur 5.11: Interpretatie van 95<span class="math inline">\$\\%\$</span> betrouwbaarheidintervallen. Resultaten op basis van 100 gesimuleerde steekproeven. We zien in de figuur duidelijk dat het populatiegemiddelde vast is maar ongekend (blauwe lijn) en dat de bovengrens en ondergrens van betrouwbaarheidsintervallen voor het populatiegemiddelde varieert van steekproef tot steekproef. Van de 100 betrouwbaarheidsintervallen die worden geplot bevatten 95 intervallen het werkelijke steekproef gemiddelde (zwarte BIs). Voor 5 intervallen is dat niet het geval (rode BIs).

### <span class="header-section-number">5.4.4</span> Wat rapporteren?

Rapporteer dus zeker steeds de onzekerheid op de resultaten! Conclusies trekken op basis van 1 schatting kan zeer misleidend zijn! In statistische analyses rapporteert men daarom systematisch betrouwbaarheidsintervallen. Betrouwbaarheidsintervallen vormen een goed compromis: ze zijn smal genoeg om informatief te zijn, maar haast nooit zeer misleidend. We besluiten dat de parameter die ons interesseert in het 95% betrouwbaarheidsinterval zit, en weten dat die uitspraak met 95% kans correct is. In de statistiek trekt men dus nooit absolute conclusies.

Op basis van de data-analyse voor het captopril voorbeeld kunnen we dus besluiten dat de gemiddelde bloeddrukdaling 18.9mmHg bedraagt na het toedienen van captopril. Met een 95% betrouwbaarheidsinterval op het gemiddelde van $$-22.3,-15.6$$mmHg. Op basis van het betrouwbaarheidsinterval is het duidelijk dat het toedienen van captopril resulteert in een sterke bloeddrukdaling bij patiënten met hypertensie.

---

[← 5.3 Puntschatters: het steekproefgemiddelde](03-5-3-puntschatters-het-steekproefgemiddelde.md) · [Up: contents](index.md) · [5.5 Principe van Hypothesetoetsen (via one sample t-test) →](05-5-5-principe-van-hypothesetoetsen-via-one-sample-t-test.md)

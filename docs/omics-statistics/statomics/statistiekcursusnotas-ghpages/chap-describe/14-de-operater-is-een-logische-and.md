---
title: de & operater is een logische AND
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-describe.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-describe.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# de & operater is een logische AND

**Source:** [`chap-describe.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-describe.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

#subset van gezonde personen
nhanesSubHealthy=subset(nhanesSub,Smoke100n=="Non-Smoker"&Diabetes=="No"&as.double(BMI_WHO)%in%c(2,3)&HardDrugs=="No"&HealthGen!="Poor"&SleepTrouble=="No")
par(mfrow=c(1,2))
hist(nhanesSub$bpSys,xlab="Systolische bloeddruk (mm Hg)",main="Personen tussen 40-65 jaar")
hist(nhanesSubHealthy$bpSys,xlab="Systolische bloeddruk (mm Hg)",main="Gezonde personen tussen 40-65 jaar")
```

<span id="fig:sysBp"></span> <img src="Statistiek_2019_2020_files/figure-html/sysBp-1.png" style="width:100.0%" alt="Systolische bloeddruk bij personen tussen de 40 en 65 jaar oud." />

Figuur 4.9: Systolische bloeddruk bij personen tussen de 40 en 65 jaar oud.

De systolische bloeddruk voor gezonde personen is symmetrisch en we zullen later aantonen dat deze approximatief normaal verdeeld zijn. Als het gemiddelde en de standard deviatie van de bloeddruk in de populatie gekend zijn kunnen we normale bloeddrukwaarden afleiden. In de praktijk zijn deze typisch niet gekend en worden deze geschat op basis van de data. In de gezonde subset is het steekproefgemiddelde 119.5mmHg en de standaarddeviatie 14.1mmHg. Als we het populatiegemiddelde en het populatiestandaarddeviatie door deze schattingen vervangen dan bekomen we volgend referentie interval: $$91.9, 147$$mmHg.

Merk ook op dat de bovengrens van de normale systolische bloeddruk iets boven de grens van hypertensie van 140 mmHg ligt die in de literatuur wordt gehanteerd.

`**Einde voorbeeld**`

``` {.sourceCode .r}
mean(nhanesSubHealthy$bpSys)+qnorm(c(0.025,0.975))*sd(nhanesSubHealthy$bpSys)
```

    ## [1]  91.88971 147.03393

### <span class="header-section-number">4.4.2</span> QQ-plots {#qq-plots}

Hoewel heel wat metingen in de biologische wetenschappen en scheikunde, zoals concentraties van een bepaalde stof, scheef verdeeld zijn naar rechts, worden ze door het nemen van een logaritme vaak getransformeerd naar gegevens waarvoor het histogram de vorm heeft van een Normale dichtheidsfunctie. Dit is uiteraard niet altijd zo en stappen om te verifiëren of observaties Normaal verdeeld zijn, zijn daarom van groot belang om de technieken in Sectie [4.4.1](index.md) te kunnen gebruiken, alsook heel wat technieken uit de verdere hoofdstukken die er zullen van uit gaan dat de gegevens Normaal verdeeld zijn. Hoewel een vergelijking van het histogram van de gegevens met de vorm van de Normale curve wel inzicht geeft of de gegevens al dan niet Normaal verdeeld zijn, is dit vaak niet makkelijk te zien en wordt de uiteindelijke beslissing nogal makkelijk beïnvloed door de keuze van de klassebreedtes op het histogram. Om die reden zullen we kwantielgrafieken gebruiken die duidelijker toelaten om na te gaan of gegevens Normaal verdeeld zijn.

*QQ-plots* of *kwantielgrafieken* (in het Engels: *quantile-quantile plots*) zijn grafieken die toelaten te verifiëren of een reeks observaties lukrake trekkingen zijn uit een Normale verdeling. Met andere woorden, ze laten toe om na te gaan of een reeks observaties al dan niet de onderstelling tegenspreken dat ze realisaties zijn van een reeks Normaal verdeelde gegevens. Het principe achter deze grafieken is vrij eenvoudig. Verschillende percentielen die men heeft berekend voor de gegeven reeks observaties worden uitgezet t.o.v. de overeenkomstige percentielen die men verwacht op basis van de Normale curve. Als de onderstelling correct is dat de gegevens Normaal verdeeld zijn, dan komen beide percentielen telkens vrij goed met elkaar overeen en verwacht men bijgevolg een reeks puntjes min of meer op een rechte te zien (zoals in Figuur [4.10](index.md), rechtsboven). Systematische afwijkingen van een rechte wijzen op systematische afwijkingen van Normaliteit. Lukrake afwijkingen van een rechte kunnen het gevolg zijn van toevallige biologische variatie en zijn daarom niet indicatief voor afwijkingen van Normaliteit. We gebruiken hiervoor de functie `qqPlot` uit het package `car`. De qqPlot functie geeft op de figuur ook banden weer waarbinnen punten uit de normaal verdeling met een kans van 95% kunnen worden verwacht.

    ## [1]  60 235

<span id="fig:qq"></span> <img src="Statistiek_2019_2020_files/figure-html/qq-1.png" style="width:100.0%" alt="Histogrammen (links) en bijhorende kwantielgrafieken (rechts) voor een aantal verdelingen." />

Figuur 4.10: Histogrammen (links) en bijhorende kwantielgrafieken (rechts) voor een aantal verdelingen.

    ## [1] 150 181

Het berekenen van de percentielen die men verwacht op basis van de Normale curve verloopt vrij eenvoudig. Beschouw bijvoorbeeld <span class="math inline">\$4n-1\$</span> geordende observaties <span class="math inline">\$x\_1,...,x\_{4n-1}\$</span>. Dan is <span class="math inline">\$x\_{2n}\$</span> de bijhorende mediaan en is <span class="math inline">\$\\mu\$</span> de mediaan die men verwacht voor een Normaal verdeelde meting met gemiddelde <span class="math inline">\$\\mu\$</span> en standaarddeviatie <span class="math inline">\$\\sigma\$</span>. Analoog is <span class="math inline">\$x\_n\$</span> het <span class="math inline">\$25\\%\$</span>-percentiel van de gegeven reeks observaties en is <span class="math inline">\$\\mu-z\_{0.25}\\sigma=\\mu-0.674\\sigma\$</span> het <span class="math inline">\$25\\%\$</span>-percentiel dat men verwacht voor een Normaal verdeelde meting met gemiddelde <span class="math inline">\$\\mu\$</span> en standaarddeviatie <span class="math inline">\$\\sigma\$</span>. Algemeen is voor <span class="math inline">\$k=1,...,4n-1\$</span> en <span class="math inline">\$p=k/4n\$</span>, <span class="math inline">\$x\_k\$</span> het <span class="math inline">\$p 100\\%\$</span>-percentiel van de gegeven reeks observaties en <span class="math inline">\$\\mu-z\_{p}\\sigma\$</span> het overeenkomstige <span class="math inline">\$p 100\\%\$</span>-percentiel van een Normaal verdeelde meting met gemiddelde <span class="math inline">\$\\mu\$</span> en standaarddeviatie <span class="math inline">\$\\sigma\$</span>. Omdat <span class="math inline">\$\\mu\$</span> en <span class="math inline">\$\\sigma\$</span> ongekend zijn, kiest men er meestal voor om de percentielen voor de gegeven reeks observaties uit te zetten t.o.v. de gestandaardiseerde percentielen voor de Normale verdeling. Men bekomt deze laatste door de percentielen <span class="math inline">\$\\mu-z\_{p}\\sigma\$</span>, die berekend werden voor de Normale verdeling, te standaardiseren. Aldus bekomt men een grafiek waar men voor elke <span class="math inline">\$k=1,...,4n-1\$</span> het percentiel <span class="math inline">\$x\_k\$</span> uitzet t.o.v. <span class="math inline">\$-z\_{p}=z\_{1-p}\$</span> met <span class="math inline">\$p=k/4n\$</span>. Het resultaat wordt voor een aantal fictieve datasets weergegeven in Figuur [4.10](index.md) (rechts) en noemt men een QQ-plot.

De gegevens in Figuur [4.10](index.md), rij 1, zijn met een computer gesimuleerd als lukrake trekkingen uit een grote reeks Normaal verdeelde observaties. Zoals verwacht liggen de gegevens in bijhorende QQ-plot nagenoeg op een rechte lijn. Door toevallige variatie is dit geen perfecte rechte lijn, maar kunnen geen systematische afwijkingen van een rechte worden vastgesteld. Dit geeft een suggestie dat de onderstelling van een Normale verdeling hier vermoedelijk voldaan is. In Figuur [4.10](index.md) (onder, rechts) stellen we een systematische afwijking van een rechte lijn vast. Op de X-as vinden we de gestandaardiseerde percentielen die worden verwacht voor een Normale verdeling en op de Y-as vinden we de observaties zelf. Merk op dat kleine observaties minder gespreid zijn dan Normaal verdeelde gegevens en dat hoge waarden meer gespreid zijn. Dit wijst erop dat hun verdeling scheef is naar rechts, zoals men ook kan zien op basis van het histogram Figuur [4.10](index.md) (onder, links).
Het grote voordeel van een QQ-plot (in vergelijking met een histogram) om afwijkingen van Normaliteit te detecteren, is dat ze dergelijke afwijkingen duidelijker weergeeft dan een histogram.

Hetzelfde principe als voor Normaal verdeelde observaties kan ook herhaald worden voor andere theoretische verdelingen, die we later in deze cursus zullen ontmoeten. Bijvoorbeeld kan men analoge kwantielgrafieken opstellen voor de Poissonverdeling (verdeling voor tellingen) om na te gaan of een reeks observaties lukrake trekkingen vormen uit zo’n Poissonverdeling.

<span id="exm:unnamed-chunk-54" class="example">**Voorbeeld 4.4 (NHANES vervolg)** </span>

    ## [1] 260 238

    ## [1] 255  56

<span id="fig:qqBp"></span> <img src="Statistiek_2019_2020_files/figure-html/qqBp-1.png" style="width:100.0%" alt="Kernel density schatters (boven) een QQ-plots (onder) voor de systolische bloeddruk en directe HDL cholestorol bij de subset van gezonde personen tussen de 40 en 65 jaar." />

Figuur 4.11: Kernel density schatters (boven) een QQ-plots (onder) voor de systolische bloeddruk en directe HDL cholestorol bij de subset van gezonde personen tussen de 40 en 65 jaar.

    ## [1] 255  71

De QQ-plot in Figuur [4.11](index.md) (links onder) geeft aan dat de systolische bloeddruk bij gezonde personen bij benadering Normaal verdeeld is, hetgeen bevestigd wordt door het histogram met de kernel density schatter (links boven).
Op basis van het gemiddelde van 119.5mmHg en de standaarddeviatie van 14.1 mmHg kunnen we aldus besluiten dat 95% van de bloeddruk waarden gelegen zijn tussen de $$91.9,147$$ mmHg.

De QQ-plot in Figuur [4.11](index.md) (midden en rechts) geeft aan dat de directe cholestorol bij gezonde personen tussen de 40 en 65 jaar duidelijk scheef verdeeld is en dat de Normale benadering beter wordt na log-transformatie. De log-cholestorol is gemiddeld 0.37 en heeft een standaarddeviatie van 0.29. We kunnen bij benadering stellen dat 95% van de log-bloeddrukken liggen tussen $$-0.19,0.93$$. Bijgevolg verwachten we benadering 95% van de cholestorol metingen tussen <span class="math inline">\$\\exp(-0.27)=0.76\$</span> en <span class="math inline">\$\\exp(0.85)=2.34\$</span> <span class="math inline">\$\\mu\$</span>mol/l. Deze wijken ietwat af van de overeenkomstige 2.5% en 97.5% percentielen $$0.87, 2.52$$ <span class="math inline">\$\\mu\$</span>mol/l deels doordat steekproefpercentielen minder precies (lees: minder stabiel) zijn dan schattingen die men ervoor bekomt op basis van de Normale verdeling.

`**Einde voorbeeld**`

## <span class="header-section-number">4.5</span> Samenvattingsmaten voor categorische variabelen {#samenvattingsmaten-voor-categorische-variabelen}

De samenvattingsmaten uit de vorige sectie (gemiddelde, mediaan, standaarddeviatie, …) kunnen niet zomaar toegepast worden voor de beschrijving van categorische variabelen. In deze sectie gaan we hier dieper op in, daarbij onderscheid makend tussen enerzijds gegevens die uit prospectieve studies of lukrake steekproeven afkomstig zijn, en anderzijds gegevens uit retrospectieve studies.

### <span class="header-section-number">4.5.1</span> Prospectieve studies en lukrake steekproeven

<span id="exm:unnamed-chunk-55" class="example">**Voorbeeld 4.5 (Houtluizen)** </span>

Een bioloog verzamelt \`s nachts bladerafval op een lukrake plaats van 1 m<span class="math inline">\$^2\$</span> in 2 wouden, waarvan 1 met klei- en 1 met kalkgrond. Op elke plaats telt hij het aantal houtluizen van de species Armadilidium of Oniscus, met als doel na te gaan of de ene soort vaker voorkomt op kleigrond dan op kalkgrond<a href="#fn18" id="fnref18" class="footnoteRef"><sup>18</sup></a>. Tabel [4.2](index.md) toont de bekomen gegevens. Hier stelt <span class="math inline">\$a\$</span> (<span class="math inline">\$c\$</span>) het aantal houtluizen van de soort Armadilidium (Oniscus) voor op kleigrond, en <span class="math inline">\$b\$</span> (<span class="math inline">\$d\$</span>) het aantal houtluizen van de soort Armadilidium (Oniscus) op kalkgrond.

|        | Armadil. | Oniscus  | Totaal   |
|:-------|:---------|:---------|:---------|
| Klei   | 14 (a)   | 6 (c)    | 20 (a+c) |
| Kalk   | 22 (b)   | 46 (d)   | 68 (b+d) |
| Totaal | 36 (a+b) | 52 (c+d) | 88 (n)   |

<span id="tab:cox">Tabel 4.2: </span>Kruistabel van species houtluis versus type grond.

`**Einde voorbeeld**`

Er zijn verschillende manieren om de resultaten van deze studie te beschrijven. De kans dat 1 van beide species houtluizen van de soort Armadilidium is, is <span class="math inline">\$p\_{kl}=a/(a+c)=0.70\$</span> of 70% op kleigrond en <span class="math inline">\$p\_{ka}=b/(b+d)=0.32\$</span> of 32% op kalkgrond.

<span id="def:unnamed-chunk-56" class="definition">**Definitie 4.11 (absolute risico verschil)** </span>Het **absolute risico verschil** of absolute kansverschil op een gegeven gebeurtenis (bvb. om Armadilidium aan te treffen) voor populatie T (Test, bvb. kleigrond) versus C (Controle, bvb. kalkgrond) wordt met ARV genoteerd en gedefinieerd als het verschil <span class="math display">\\$$\\begin{equation\*} ARV=p\_T-p\_C \\end{equation\*}\\$$</span>

tussen de kansen dat deze gebeurtenis zich voordoet in populaties T en C.

**Einde definitie**

Het ARV op Armadilidium tussen klei- en kalkgrond bedraagt 0.38, hetgeen suggereert dat de kans dat 1 van beide species houtluizen van de soort Armadilidium is, 38% hoger is op kleigrond dan op kalkgrond. Een absoluut kansverschil van 0 drukt uit dat de overeenkomstige kansen even groot zijn in beide populaties en dat beide populaties dus vergelijkbaar zijn in termen van de bestudeerde uitkomst.

Het absolute kansverschil zegt echter niet alles omtrent het bestudeerde effect. Een kansverschil kan immers een grotere impact hebben alnaargelang beide proporties <span class="math inline">\$p\_T\$</span> en <span class="math inline">\$p\_C\$</span> dicht bij 0 of 1 liggen, dan wanneer ze in de buurt van 0.5 liggen. Bijvoorbeeld, wanneer we de proportie vrouwen jonger dan 60 jaar meten die borstkanker ontwikkelen, is een risicoverschil tussen <span class="math inline">\$p\_A=0.01\$</span> voor vrouwen die het allel Leu/Leu bezitten op het BRCA1 gen en <span class="math inline">\$p\_B=0.001\$</span> voor de overige vrouwen, wellicht belangrijker dan een verschil tussen <span class="math inline">\$p\_C=0.41\$</span> en <span class="math inline">\$p\_D=0.401\$</span> voor beide populaties. Een uitspraak dat het risico 0.9% lager is in de ene dan in de andere populatie geeft om die reden slechts een beperkt beeld van het belang van die reductie. Een goede vergelijking van risico’s, kansen of percentages moet om die reden ook rekening houden met het basisrisico (d.w.z. de kans op de bestudeerde uitkomst in een referentiepopulatie). Het ARV doet dit niet, in tegenstelling tot volgende associatiemaat.

<span id="def:unnamed-chunk-57" class="definition">**Definitie 4.12 (relatief risico)** </span>Het **relatief risico** op een gegeven gebeurtenis (bvb. om Armadilidium aan te treffen) voor populatie T (Test, bvb. kleigrond) versus C (Controle, bvb. kalkgrond) wordt met RR genoteerd en gedefinieerd als het quotiënt <span class="math display">\\$$\\begin{equation\*} RR=\\frac{p\_T}{p\_C} \\end{equation\*}\\$$</span>

van de kansen dat deze gebeurtenis zich voordoet in populaties T en C.

**Einde definitie**

In de studie naar houtluizen bedraagt dit <span class="math inline">\$RR=0.70/0.32=2.2\$</span>. Dit suggereert dat er 2.2 keer zoveel kans om een houtluis van de soort Armadilidium (i.p.v. Oniscus) aan te treffen op kleigrond dan op kalkgrond. Een relatief risico van 1 drukt uit dat beide populaties dus vergelijkbaar zijn in termen van de bestudeerde uitkomst.

Een nadeel van het relatief risico is dat ze, in tegenstelling tot het absolute risico verschil, niet goed duidelijk maakt hoeveel meer individuen de bestudeerde uitkomst ondervinden in de ene dan in de andere populatie. Bijvoorbeeld, zelfs wetende dat het relatief risico op Armidilidium in klei-versus kalkgrond 2.2 bedraagt, is het niet mogelijk om uit te maken hoeveel meer houtluizen van de soort Armidilidium zich manifesteren op kleigrond. Als de kans om Armidilidium aan te treffen i.p.v. Oniscus 0.1% bedraagt op kalkgrond, dan verwacht men dat er per 10000 houtluizen (van de soort Armidilidium of Oniscus) er 10 van de soort Armidilidium zullen zijn op kalkgrond en 22 op kleigrond, wat neerkomt op een verwaarloosbaar verschil van 12. Als de kans om Armidilidium aan te treffen i.p.v. Oniscus 40% bedraagt op kalkgrond, dan verwacht men dat er per 10000 houtluizen (van de soort Armidilidium of Oniscus) er 4000 van de soort Armidilidium zullen zijn op kalkgrond en 8800 op kleigrond, wat neerkomt op een aanzienlijk verschil van 4800. Soms rapporteert men in de plaats van het relatief risico, het *relatieve risico verschil* <span class="math inline">\$ARV/p\_C=RR-1\$</span>. Voor de gegeven studie bedraagt dit 1.2. Het drukt uit dat de toename (van kalk- naar kleigrond) in kans om Armadilidium aan te treffen succes meer dan 1 keer zo groot is als het basisrisico in de controlegroep (kalkgrond).

Merk op dat alle bovenstaande associatiematen eveneens gebruikt kunnen worden wanneer men, in tegenstelling tot wat in een prospectieve studie gebeurt, een volledig lukrake groep proefpersonen selecteert zonder vast te leggen hoeveel van hen al dan niet blootgesteld zijn.

### <span class="header-section-number">4.5.2</span> Retrospectieve studies {#retrospectieve-studies}

Beschouw de case-controle studie uit Voorbeeld [3.16](../chap-design/index.md), waarvan de gegevens samengevat zijn in Tabel [4.3](index.md). Omdat men in zo’n design op zoek gaat naar <span class="math inline">\$a+b+c\$</span> lukraak gekozen controles en <span class="math inline">\$d+e+f\$</span> lukraak gekozen cases, liggen de marges <span class="math inline">\$a+b+c\$</span> en <span class="math inline">\$d+e+f\$</span> vast en is het bijgevolg onmogelijk om het risico op case (bvb. risico op borstkanker) te schatten. Dit is noch mogelijk binnen de totale groep, noch binnen de groep van blootgestelden (d.i. vrouwen met allel Leu/Leu), noch binnen de groep niet-blootgestelden. Immers, de kans op case binnen die geobserveerde groep reflecteert hoofdzakelijk de verhouding waarin cases en controles in totaal werden gekozen door het design. Alleen analyses die de kolomtotalen in de tabel vast gegeven veronderstellen, zijn hier zinvol. Dit heeft tot gevolg dat *het relatief risico* op de aandoening (d.w.z. op *case*) in de populatie voor blootgestelden versus niet-blootgestelden niet rechtstreeks kan geschat worden op basis van gegevens uit een *case-controle studie*. Analoog kan ook het bijhorende *absolute risicoverschil niet geschat* worden.

| Genotype | Controles   | Cases       | Totaal    |
|:---------|:------------|:------------|:----------|
| Pro/Pro  | 266 (a)     | 342 (d)     | 608 (a+d) |
| Pro/Leu  | 250 (b)     | 369 (e)     | 619 (b+e) |
| Leu/Leu  | 56 (c)      | 89 (f)      | 145 (c+f) |
| Totaal   | 572 (a+b+c) | 800 (d+e+f) | 1372 (n)  |

<span id="tab:leu2">Tabel 4.3: </span>Kruistabel van borstkanker-status versus BRCA1-allel.

Wel heeft men informatie over de kans om het allel Leu/Leu aan te treffen bij cases, <span class="math inline">\$\\pi\_1=f/(d+e+f)=89/800=11.1\\%\$</span>, en de kans op het allel Leu/Leu bij controles, <span class="math inline">\$\\pi\_0=c/(a+b+c)=56/572=9.8\\%\$</span>. Het relatief risico op blootstelling voor cases versus controles is bijgevolg <span class="math inline">\$11.1/9.8=1.14\$</span>. Vrouwen met borstkanker hebben dus 14% meer kans om de allelcombinatie Leu/Leu te hebben op het BRCA1 gen dan vrouwen zonder borstkanker. Dit suggereert dat er een associatie<a href="#fn19" id="fnref19" class="footnoteRef"><sup>19</sup></a> is tussen het polymorfisme op het BRCA1 gen en borstkanker, maar drukt helaas niet uit hoeveel hoger het risico op borstkanker is voor vrouwen met de allelcombinatie Leu/Leu dan voor andere vrouwen. Om toch een antwoord te vinden op deze laatste vraag, voeren we een nieuwe risicomaat in.

<span id="def:unnamed-chunk-58" class="definition">**Definitie 4.13 (Odds)** </span>De *odds* op een gebeurtenis wordt gedefinieerd als <span class="math display">\\$$\\begin{equation\*} \\frac{p}{1-p} \\end{equation\*}\\$$</span>

waarbij <span class="math inline">\$p\$</span> de kans is op die gebeurtenis.

**Einde definitie**

De odds is dus een transformatie van het risico, met onder andere de volgende eigenschappen:

- de odds neemt waarden aan tussen nul en oneindig.

- de odds is gelijk aan 1 als en slechts als de kans zelf gelijk is aan 1/2.

- de odds neemt toe als de kans toeneemt.

Het gebruik van odds is populair onder gokkers omdat het uitdrukt hoeveel waarschijnlijker het is om te winnen dan om te verliezen. Een odds op winnen gelijk aan 1 drukt bijvoorbeeld uit dat het even waarschijnlijk is om te winnen dan om te verliezen. Een odds op winnen gelijk aan 0.9 drukt uit men per 10 verliesbeurten, 9 keer verwacht te winnen. In de genetische associatiestudie uit Voorbeeld [3.16](../chap-design/index.md) is de odds op allel Leu/Leu bij cases gelijk aan <span class="math inline">\$\\mbox{odds}\_1=f/(d+e)=89/711=0.125\$</span> en bij controles gelijk aan <span class="math inline">\$\\mbox{odds}\_2=c/(a+b)=56/516=0.109\$</span>. Vrouwen met borstkanker hebben bijgevolg ongeveer 8 (<span class="math inline">\$\\approx 1/0.125\$</span>) keer meer kans om de allelcombinatie Leu/Leu niet te hebben op het BRCA1 gen dan om het wel te hebben. Om de associatie tussen blootstelling en uitkomst te beschrijven, kan men nu een verhouding van odds (odds ratio) gebruiken in plaats van een verhouding van risico’s (relatief risico).

<span id="def:unnamed-chunk-59" class="definition">**Definitie 4.14 (Odds ratio)** </span>De **odds ratio** op een gegeven gebeurtenis (bvb. borstkanker) voor populatie T (bvb. vrouwen met allel Leu/Leu) versus C (bvb. vrouwen zonder allel Leu/Leu) wordt met OR genoteerd en gedefinieerd als het quotiënt <span class="math display">\\$$\\begin{equation\*} OR=\\frac{\\mbox{odds}\_T}{\\mbox{odds}\_C} \\end{equation\*}\\$$</span>

van de odds op deze gebeurtenis in populaties T en C.

**Einde definitie**

Op basis van de gegevens in Tabel [4.3](index.md) kan de odds ratio op blootstelling voor cases versus controles geschat worden d.m.v. het kruisproduct <span class="math display">\\$$\\begin{equation\*} \\frac{ \\frac{ f/(d+e+f)}{(d+e)/(d+e+f)} }{ \\frac{c/(a+b+c)}{(a+b)/(a+b+c)}} = \\frac{f(a+b)}{c (d+e)} \\end{equation\*}\\$$</span>

In het bijzonder vinden we dat de odds op allelcombinatie Leu/Leu voor vrouwen met versus zonder borstkanker gelijk is aan <span class="math inline">\$OR=(89\\times 516)/(56\\times 711)=1.15\$</span>. Helaas drukt dit resultaat nog steeds niet uit hoeveel meer risico op borstkanker vrouwen met de allelcombinatie Leu/Leu lopen.

Was de bovenstaande studie echter een volledig lukrake steekproef geweest (waarbij het aantal cases en controles niet per design werden vastgelegd), dan konden we daar ook de odds ratio op borstkanker berekenen voor mensen met versus zonder het allel Leu/leu. We zouden dan vaststellen dat dit gelijk is aan <span class="math display">\\$$\\begin{equation\*} \\frac{ \\frac{ f/(c+f)}{c/(c+f)} }{ \\frac{(d+e)/(a+b+d+e)}{(a+b)/(a+b+d+e)}} = \\frac{f(a+b)}{c(d+e)}, \\end{equation\*}\\$$</span>

en bijgevolg dezelfde waarde aanneemt. Dat is omdat de odds ratio een *symmetrische associatiemaat* is zodat de odds ratio op \`case’ voor blootgestelden versus niet-blootgestelden steeds gelijk is aan de odds op blootstelling voor cases versus controles. Hieruit volgt dat voor het schatten van de odds ratio het er niet toe doet of we prospectief werken zoals in een typische cohort studie, of retrospectief zoals in een typische case-controle studie. In het bijzonder kunnen we in de genetische associatiestudie uit Voorbeeld [3.16](../chap-design/index.md) de odds op borstkanker voor vrouwen met allel Leu/leu versus zonder berekenen als <span class="math inline">\$OR=89\\times 516/(56\\times 711)=1.15\$</span>. De odds op borstkanker is bijgevolg 15% hoger bij vrouwen met die specifieke allelcombinatie.

Stel nu dat we met <span class="math inline">\$p\_T\$</span> en <span class="math inline">\$p\_C\$</span> respectievelijk de kans op case noteren voor blootgestelden en niet-blootgestelden. Wanneer beide kansen klein zijn (namelijk <span class="math inline">\$p\_T&lt;5\\%\$</span> en <span class="math inline">\$p\_C&lt;5\\%\$</span>), dan is de odds een goede benadering voor het risico. Dit is omdat in dat geval <span class="math inline">\$\\mbox{odds}\_T=p\_T/(1-p\_T)\\approx p\_T\$</span> en <span class="math inline">\$\\mbox{odds}\_C=p\_C/(1-p\_C)\\approx p\_C\$</span>. Er volgt dan bovendien dat de odds ratio een goede benadering voor het relatief risico: <span class="math display">\\$$\\begin{equation\*} OR=\\frac{\\mbox{ odds}\_T}{\\mbox{ odds}\_C}\\approx \\frac{p\_T}{p\_C}=RR \\end{equation\*}\\$$</span>

Wetende dat het risico op borstkanker laag is, mogen we op basis van de gevonden OR van 1.15 bijgevolg besluiten dat het risico (i.p.v. de odds) op borstkanker (bij benadering) 15% hoger ligt bij vrouwen met het allel Leu/Leu op het BRCA1 gen. Dit is een bijzonder nuttige eigenschap omdat (a) het relatief risico, dat niet rechtstreeks geschat kan worden in case-controle studies, gemakkelijker te interpreteren is dan de odds ratio; en (b) de odds ratio bepaalde wiskundige eigenschappen heeft die ze aantrekkelijker maakt dan een relatief risico in statistische modellen<a href="#fn20" id="fnref20" class="footnoteRef"><sup>20</sup></a>. Algemeen is de odds ratio echter steeds verder van 1 verwijderd dan het relatief risico. Wetende dat de odds ratio op borstkanker 1.15 bedraagt voor vrouwen met versus zonder de allelcombinatie Leu/Leu, kunnen we bijgevolg meer nauwkeurig besluiten dat het overeenkomstige relatief risico tussen 1 en 1.15 gelegen is (maar niettemin dicht bij 1.15).

Omdat de odds ratio moeilijker te interpreteren is dan een relatief risico en bijgevolg misleidend kan zijn, valt deze laatste steeds te verkiezen in situaties (zoals prospectieve studies) waar het mogelijk is om het relatief risico in de populatie te schatten. In sommige case-controle studies (nl. matched case-controle studies) wordt voor elke case een controle gezocht die bepaalde karakteristieken gemeenschappelijk heeft, teneinde een betere onderlinge vergelijkbaarheid te garanderen. In dat geval moet de statistische analyse (inclusief de manier om odds ratio’s te schatten) rekening houden met het feit dat de resultaten van elke case gecorreleerd of verwant zijn met de resultaten van de bijhorende controle.

### <span class="header-section-number">4.5.3</span> Rates versus risico’s

Vaak wordt het begrip *risico* verward met het begrip *rate*. Een *rate* drukt een aantal gebeurtenissen (bvb. aantal sterfte- of ziektegevallen) uit per eenheid in de populatie in een bepaalde tijdspanne. Bijvoorbeeld, een *crude mortality rate (CMR)* voor een bepaald jaartal is gedefinieerd als 1000 maal het aantal sterftegevallen dat optreedt in dat jaar gedeeld door de grootte van de beschouwde populatie halfweg dat jaar. De reden dat met 1000 wordt vermenigvuldigd is dat het bijvoorbeeld makkelijker na te denken is over een CMR van 12 sterftes per 1000 in Engeland en Wales, dan over 0.012 sterftes per individu. Indien een specifieke leeftijdsgroep wordt gekozen, verkrijgt men de *leeftijdsspecifieke mortality rate* als 1000 maal het aantal sterftegevallen dat optreedt in een bepaald jaar en bepaalde leeftijdsgroep gedeeld door de grootte van de beschouwde populatie in die leeftijdsklasse halfweg dat jaar. In tegenstelling tot de incidentie, is de prevalentie geen rate omdat ze niet een aantal gebeurtenissen uitdrukt over een zekere tijdspanne.

## <span class="header-section-number">4.6</span> Associaties tussen twee variabelen

Tot nog toe zijn we hoofdzakelijk ingegaan op zogenaamde univariate beschrijvingen waarbij slechts 1 variabele onderzocht wordt. In de meeste wetenschappelijke studies wenst men echter associaties tussen 2 of meerdere variabelen te onderzoeken, bijvoorbeeld tussen een interventie en de daarop volgende respons. In deze Sectie onderzoeken we hoe associaties tussen 2 variabelen kunnen beschreven worden. We maken daarbij onderscheid naargelang het type van de variabelen.

### <span class="header-section-number">4.6.1</span> Associatie tussen twee kwalitatieve variabelen {#associatie-tussen-twee-kwalitatieve-variabelen}

Als twee kwalitatieve variabelen niet veel verschillende waarden aannemen, dan is een *kruistabel* aangewezen om hun associatie voor te stellen. In deze tabel worden de verschillende waarden die de ene variabele aanneemt in de kolommen uitgezet en de verschillende waarden die de andere variabele aanneemt in de rijen. In elke cel van de tabel (die overeenkomt met 1 specifieke combinatie van waarden voor beide variabelen) wordt de frequentie neergeschreven.

|        | 12.0\_18.5 | 18.5\_to\_24.9 | 25.0\_to\_29.9 | 30.0\_plus |
|:-------|-----------:|---------------:|---------------:|-----------:|
| female |        629 |           1616 |           1179 |       1402 |
| male   |        648 |           1295 |           1485 |       1349 |

<span id="tab:genderBMI">Tabel 4.4: </span>Kruistabel van Gender vs BMI klasse.

Tabel [4.4](index.md) toont zo’n kruistabel voor het aantal mannen en vrouwen per BMI klasse. Dergelijke eenvoudige kruistabel met slechts 2 rijen en 4 kolommen, noemt men ook een <span class="math inline">\$2\\times 4\$</span> tabel.

### <span class="header-section-number">4.6.2</span> Associatie tussen één kwalitatieve en één continue variabele {#associatie-tussen-één-kwalitatieve-en-één-continue-variabele}

De eenvoudigste grafische weergave met het maximum aan informatie om de associatie tussen een kwalitatieve en een continue variabele te beschrijven is een *dot-plot*.

``` {.sourceCode .r}
ggplot(NHANES[1:100,], aes(x = Gender, y = log(DirectChol))) +
  geom_dotplot(binaxis = "y", stackdir = "center")
```

<span id="fig:dotCholGender"></span> <img src="Statistiek_2019_2020_files/figure-html/dotCholGender-1.png" style="width:100.0%" alt="Dotplot van log-getransformeerde directe HDL cholestorol concentratie in functie van Gender voor de eerste 100 subjecten van de NHANES studie." />

Figuur 4.12: Dotplot van log-getransformeerde directe HDL cholestorol concentratie in functie van Gender voor de eerste 100 subjecten van de NHANES studie.

Dit wordt geïllustreerd in Figuur [4.12](index.md) waarbij de log directe cholestorol concentratie is geplot in functie van het geslacht voor de eerste 100 personen in de studie. Deze voorstellingsmethode behoudt de individuele waarden van de observaties en laat gemakkelijke vergelijkingen toe tussen de verschillende groepen. Een bijkomend voordeel is dat outliers meteen zichtbaar zijn in een dot-plot. Een nadeel ontstaat wanneer de steekproef groot is en bijgevolg vele observaties samenvallen op de figuur. Vandaar dat we de plot hebben gemaakt voor een subset van de data.

Als het aantal observaties groot is, kan een dot-plot vervangen worden door *boxplots*. Deze is meer compact dan een histogram en laat om die reden gemakkelijker vergelijkingen tussen verschillende groepen toe. Twee dergelijke boxplots worden getoond in Figuur [4.13](index.md).

``` {.sourceCode .r}
boxplot(log(DirectChol)~Gender,data=NHANES,ylab="log(Direct Cholestorol)")
```

<span id="fig:boxplotCholGender"></span> <img src="Statistiek_2019_2020_files/figure-html/boxplotCholGender-1.png" style="width:100.0%" alt="Dotplot van log-getransformeerde directe HDL cholestorol concentratie in functie van Gender voor alle subjecten van de NHANES studie." />

Figuur 4.13: Dotplot van log-getransformeerde directe HDL cholestorol concentratie in functie van Gender voor alle subjecten van de NHANES studie.

Op basis van deze figuur stellen we vast dat hogere log-cholestorol concentraties geobserveerd worden bij vrouwen dan bij mannen, maar dat de variabiliteit van de log-concentraties vergelijkbaar is tussen de 2 groepen. De vraag blijft of we hier kunnen spreken van een systematisch hogere log-cholestorol concentratie tussen vrouwen en mannen. We zullen in Hoofdstuk [5](../chap-besluit/index.md) dieper op deze vraag ingaan.

Figuur [4.13](index.md) kan men samenvatten door gemiddelde verschillen tussen beide groepen te rapporteren. Hier stellen we een gemiddeld verschil van 0.17 in directe HDL cholestorol concentratie vast op de log schaal tussen vrouwen en mannen. Gezien we weten dat <span class="math inline">\$\\log(C\_2)-\\log(C\_1)=\\log(C\_2/C\_1)\$</span> besluiten we dat de HDL cholestorol concentratie in de NHANES studie gemiddeld 1.19 keer hoger ligt voor vrouwen dan voor mannen.

Dot-plots zijn bijzonder interessant in pre-test post-test designs waar dezelfde subjecten op verschillende tijdstippen worden geobserveerd. In dat geval kunnen de uitkomsten uitgezet worden op de Y-as en de tijdstippen op de X-as, en kunnen de metingen voor eenzelfde subject worden verbonden met een lijn.

Een voorbeeld hiervan is weergegeven in Figuur [4.14](index.md). De figuur vat de gegevens samen van de captopril studie die de centrale dataset vormt van Hoofdstuk [5](../chap-besluit/index.md). In de studie wenst men het effect van een bloeddrukverlagend geneesmiddel captopril evalueren. Voor elke patiënt in de studie werd de systolische bloeddruk twee keer gemeten: één keer voor en één keer na de behandeling met het bloeddruk verlagende medicijn captopril. In Figuur [4.14](index.md) worden de metingen van dezelfde patiënt met een lijntje verbonden. Hierdoor krijgen we een heel duidelijk beeld van de gegevens. Namelijk, we krijgen een sterke indruk dat de bloeddruk daalt na het toedienen van captopril gezien we bijna voor alle patiënten een daling observeren.

    ##   id SBPb DBPb SBPa DBPa
    ## 1  1  210  130  201  125
    ## 2  2  169  122  165  121
    ## 3  3  187  124  166  121
    ## 4  4  160  104  157  106
    ## 5  5  167  112  147  101
    ## 6  6  176  101  145   85

<span id="fig:captoDot"></span> <img src="Statistiek_2019_2020_files/figure-html/captoDot-1.png" style="width:100.0%" alt="Dotplot van de systolische bloeddruk in de captopril studie voor en na het toedienen van het bloeddruk verlagend middel captopril." />

Figuur 4.14: Dotplot van de systolische bloeddruk in de captopril studie voor en na het toedienen van het bloeddruk verlagend middel captopril.

### <span class="header-section-number">4.6.3</span> Associatie tussen twee continue variabelen {#associatie-tussen-twee-continue-variabelen}

De associatie tussen 2 kwantitatieve variabelen kan worden onderzocht aan de hand van een *puntenwolk* of *spreidingsdiagram* (in het Engels: *scatterplot*). Hier worden de geobserveerde waarden van de ene variabele uitgezet tegen de andere. In Hoofdstuk [6](../chap-linReg/index.md) wordt gewerkt rond een centrale dataset m.b.t. borstkanker. Voor 32 borstkanker patiënten werd gen-expressie gemeten van de tumor a.d.h.v. microarray technologie. Figuur [4.15](index.md) zet de log-expressie uit van het S100A8 gen ten opzichte van estrogen recepter gen (ESR1). Beide genen spelen een belangrijke rol in kanker. Expressie van het ESR1 gen is een indicator dat de tumor vatbaar is voor hormoontherapie wat gunstig is voor de prognose. Het S100A8-gen daarentegen is betrokken bij de onderdrukking van het immuunsysteem en het gen speelt een rol in het creëren van een inflamatoir milieu in de tumor.

``` {.sourceCode .r}
borstkanker=read.table("dataset/borstkanker.txt",header=TRUE)
with(borstkanker, scatter.smooth(log2(ESR1),log2(S100A8),lpars=list(lty=2)))
```

<span id="fig:brcaLogFit"></span> <img src="Statistiek_2019_2020_files/figure-html/brcaLogFit-1.png" style="width:100.0%" alt="Expressie van het S100A8 gen in functie van de ESR1 gen-expressie." />

Figuur 4.15: Expressie van het S100A8 gen in functie van de ESR1 gen-expressie.

De lijn op de figuur is een *(niet-parametrische) regressielijn*. Deze vat de associatie tussen beide variabelen samen door de gemiddelde log2-expressie voor S100A8 weer te geven in functie van de log2-expressie van het ESR1 gen.

We observeren in Figuur [4.15](index.md) een negatieve associatie tussen de S100A8 en ESR1 expressie. De expressie van S100A8 neemt gemiddeld gezien af bij patiënten waar het ESR1 gen hoger geëxpresseerd is.

In de praktijk wenst men de sterkte van de samenhang tussen 2 continue variabelen graag ook beknopt uit te kunnen drukken d.m.v. een samenvattingsmaat. Zo’n veelgebruikte maat om de *lineaire* samenhang tussen 2 continue metingen uit te drukken, is de *(Pearson) correlatiecoëfficiënt* of kortweg *correlatie*.

<span id="def:unnamed-chunk-60" class="definition">**Definitie 4.15 (Correlatie)** </span>Stel dat <span class="math inline">\$x\_{i}\$</span> (bvb. lengte) en <span class="math inline">\$y\_{i}\$</span> (bvb. gewicht) 2 metingen zijn die opgemeten werden bij eenzelfde individu <span class="math inline">\$i=1,...,n\$</span>. Dan wordt de **Pearson correlatie** tussen de rij getallen <span class="math inline">\$x\$</span> en <span class="math inline">\$y\$</span> gedefinieerd als: <span class="math display">\\$$\\begin{equation\*} \\mbox{Cor}(x,y)=\\frac{\\sum\_{i=1}^{n}(x\_{i}-\\bar{x})(y\_{i}-\\bar{y})}{ (n-1)s\_{x}s\_{y}}, \\end{equation\*}\\$$</span>

met <span class="math inline">\$s\_{x}\$</span> en <span class="math inline">\$s\_{y}\$</span> de standaarddeviatie van respectievelijk de rij getallen <span class="math inline">\$x\$</span> en <span class="math inline">\$y\$</span>. De Pearson correlatie wordt typisch met <span class="math inline">\$r\$</span> genoteerd.

**Einde definitie**

De teller in bovenstaande uitdrukking gaat na in welke mate positieve (negatieve) afwijkingen tussen <span class="math inline">\$x\$</span> en zijn gemiddelde samengaan met positieve of negatieve afwijkingen tussen <span class="math inline">\$y\$</span> en zijn gemiddelde. Het teken van de correlatie geeft bijgevolg de richting van de lineaire trend aan: het teken is positief (negatief) wanneer hogere waarden voor de ene variabele samengaan met hogere (lagere) waarden voor de andere. Men zegt in dat geval dat er een *positieve (negatieve) associatie* is. De noemer in de uitdrukking standaardiseert het geheel waardoor, zoals men wiskundig kan aantonen, de correlatie(coëfficiënt) een getal is gelegen tussen -1 en 1. Uitkomsten die perfect lineair afhankelijk zijn van elkaar (d.w.z. dat ze in een scatterplot gelegen zijn op een rechte lijn) hebben een correlatie van 1 of -1. *Onafhankelijke variabelen* (d.w.z. variabelen waarvoor kennis van de waarde voor de ene variabele geen informatie levert over de waarde voor de andere variabele) hebben een correlatie gelijk aan 0.

De correlatie tussen de log2-S100A8 en log2-ESR1 expressie bedraagt -0.89. Wat opnieuw op een sterke negatieve correlatie wijst tussen de log-expressie van beide genen.

``` {.sourceCode .r}
par(mfrow=c(2,3))
for ( i in c(.3,.7,.99,-.3,-.5,-.9))
  plot(rmvnorm(100,sigma=matrix(c(1,i,i,1),ncol=2)),xlab="x",ylab="y",main=paste("correlatie",i))
```

<span id="fig:regr1"></span> <img src="Statistiek_2019_2020_files/figure-html/regr1-1.png" style="width:100.0%" alt="Gesimuleerde gegevens met verschillende correlatie." />

Figuur 4.16: Gesimuleerde gegevens met verschillende correlatie.

Figuur [4.16](index.md) toont ter illustratie verschillende scatterplots waar fictieve gegevens met verschillende correlaties werden gesimuleerd. Merk op dat het lineaire patroon tussen de twee reeksen gegevens sterker wordt met toenemende correlatie en van richting wijzigt naarmate de correlatie negatief wordt.

**Eigenschap**

De correlatie tussen 2 reeksen metingen <span class="math inline">\$(x\_i)\$</span> en <span class="math inline">\$(y\_i)\$</span> blijft ongewijzigd

- wanneer bij alle uitkomsten <span class="math inline">\$x\_i\$</span> een willekeurige constante <span class="math inline">\$a\$</span> wordt opgeteld;

- wanneer alle uitkomsten <span class="math inline">\$x\_i\$</span> met een willekeurige constante <span class="math inline">\$a\$</span> worden vermenigvuldigd;

- wanneer <span class="math inline">\$(x\_i,\\bar x)\$</span> en <span class="math inline">\$(y\_i,\\bar y)\$</span> van plaats worden verwisseld in de uitdrukking voor de correlatie.

**Einde eigenschap**

Op basis van deze eigenschap kunnen we bijvoorbeeld besluiten dat de correlatie tussen de expressie van het S100A8 en ESR1 gen niet gewijzigd wordt wanneer we een log10 transformatie hadden gebruikt ipv een log2 tranformatie. Door de eigenschappen van logaritmes weten we immers dat <span class="math inline">\$\\log\_{2}(x)=\\log\_{10}(x)/\\log\_{10}(2)\$</span>

``` {.sourceCode .r}
set.seed(100)
#Een seed wordt gebruikt om ervoor te zorgen
#dat dezelfde resultaten opnieuw kunnen worden
#bekomen wanneer men at random data genereerd
par(mfrow=c(1,2)) #twee plots naast elkaar
#simuleer
scheef=exp(rmvnorm(100,mean=rep(1.5,2),sigma=matrix(c(1.5,.75*1.5,.75*1.5,1.5),ncol=2)))
#plot
plot(scheef,main=paste("Correlatie",round(cor(scheef)[1,2],2)),xlab="x",ylab="y")
#simuleer
normal <- rmvnorm(100,mean=rep(1.5,2),sigma=matrix(c(1.5,.71*1.5,.71*1.5,1.5),ncol=2))
#plot
plot(normal,main=paste("Correlatie",round(cor(normal)[1,2],2)),xlab="x",ylab="y")
```

<span id="fig:regr3"></span> <img src="Statistiek_2019_2020_files/figure-html/regr3-1.png" style="width:100.0%" alt="Links: scheef verdeelde observaties; Rechts: Normaal verdeelde observaties." />

Figuur 4.17: Links: scheef verdeelde observaties; Rechts: Normaal verdeelde observaties.

Bij het interpreteren van correlaties, alsook bij het uitvoeren van regressie-analyses in de volgende secties, zijn de volgende waarschuwingen van zeer groot belang:

1.  Correlaties zijn het makkelijkst te interpreteren tussen 2 groepen Normaal verdeelde observaties. Een kleine training laat immers toe om snel inzicht te krijgen in de grootte van de correlatiecoëfficiënt zonder zich verder over de specifieke verdeling te hoeven bekommeren. In het bijzonder kan men voor Normaal verdeelde observaties visueel inzicht krijgen in de sterkte van de correlatie door een ellips rond de puntenwolk te tekenen die (nagenoeg) alle punten bevat. Als de ellips op een cirkel lijkt, dan is er geen correlatie. Hoe dunner de ellips, hoe sterker de correlatie. De oriëntatie van de ellips geeft hierbij het teken van de correlatie weer.

Voor niet-Normale gegevens hangt de betekenis van een correlatiecoëfficiënt van zekere grootte, nauw samen met de specifieke vorm van de verdeling. Figuur [4.17](index.md) toont ter illustratie 1 paar scheef verdeelde (links) en 1 paar Normaal verdeelde (rechts) observaties. Hoewel de correlatie in beide figuren 0.65 bedraagt, tonen beide figuren een verschillende associatie. Merk ook op in Figuur [4.18](index.md) (rechts) dat de grootte van de correlatie sterk beïnvloed kan worden door een paar outliers. De correlatie tussen deze variabelen bedraagt slechts 0.44, maar 0.93 na verwijdering van de 2 outliers.

Wanneer de 2 variabelen die we onderzoeken niet Normaal verdeeld zijn, dan zijn er 2 mogelijkheden om een zinvolle correlatiecoëfficiënt weer te geven. Variabelen die scheef verdeeld zijn, kan men transformeren (bvb. een log-transformatie) in de hoop dat de getransformeerde gegevens bij benadering Normaal verdeeld zijn en lineair samenhangen. Bemerk dat we de genexpressie van S100A8 en ESR1 daarom log-getransformeerd hebben in Figuur [4.15](index.md), concentraties en intensiteitsmetingen zijn immers vaak log-normaal verdeeld.

Indien transformatie niet helpt of wanneer er outliers zijn, kan men een meer *robuuste* maat voor de samenhang tussen 2 variabelen rapporteren, zoals de *Spearman’s rank correlatie*. Dit is per definitie de Pearson correlatiecoëfficiënt van de *rangen* van de 2 beschouwde variabelen. Dergelijke rangen worden bekomen door voor elke variabele afzonderlijk de metingen te vervangen door de rangorde waarin ze voorkomen. In het bijzonder krijgt de kleinste meting rangorde 1 toegekend, de tweede kleinste rangorde 2, etc. Door aldus rangordes voor de 2 variabelen afzonderlijk te nemen, blijft de samenhang ruwweg behouden, maar wordt de invloed van outliers gevoelig afgezwakt (omdat rangordes relatief gezien nooit extreem worden).

``` {.sourceCode .r}
par(mfrow=c(1,2))
set.seed(34)
x=c(rnorm(100))
y=3*x^2+rnorm(100,sd=2)
plot(x,y,main=paste("Correlation",round(cor(x,y),2)))
simHlp=matrix(0,ncol=2,nrow=20)
simHlp[1:18,]=rmvnorm(18,sigma=matrix(c(1,.9,.9,1),ncol=2))
simHlp[19:20,]=cbind(max(simHlp[,1])*c(1.1,1.3),c(-2,-2.8))
plot(simHlp,main=paste("Correlation",round(cor(simHlp)[1,2],2)),xlab="x",ylab="y")
```

<span id="fig:regr2"></span> <img src="Statistiek_2019_2020_files/figure-html/regr2-1.png" style="width:100.0%" alt="Links: gesimuleerde gegevens met kwadratische associatie; Rechts: gesimuleerde gegevens met een werkelijke correlatie van 0.9 en 2 outliers." />

Figuur 4.18: Links: gesimuleerde gegevens met kwadratische associatie; Rechts: gesimuleerde gegevens met een werkelijke correlatie van 0.9 en 2 outliers.

``` {.sourceCode .r}
#Met outliers
cor(simHlp)
```

    ##           [,1]      [,2]
    ## [1,] 1.0000000 0.4399447
    ## [2,] 0.4399447 1.0000000

``` {.sourceCode .r}
#Zonder outliers
cor(simHlp[1:18,])
```

    ##           [,1]      [,2]
    ## [1,] 1.0000000 0.9270999
    ## [2,] 0.9270999 1.0000000

1.  Merk op dat een correlatiecoëfficiënt van 0 tussen 2 variabelen <span class="math inline">\$X\$</span> en <span class="math inline">\$Y\$</span> niet noodzakelijk impliceert dat deze variabelen onafhankelijk zijn. Figuur [4.18](index.md) (links) toont ter bijvoorbeeld 2 variabelen die vrij sterk geassocieerd zijn, hoewel hun correlatie nagenoeg 0 bedraagt. De oorzaak hiervan is dat de correlatie enkel de lineaire samenhang tussen 2 variabelen meet en bijgevolg niet noodzakelijk niet-lineaire verbanden detecteert. Dit betekent meer concreet dat de correlatie, op een factor na, de helling weergeeft van de \`best passende rechte’ (nl. de kleinste kwadratenrechte, zie Hoofdstuk [6](../chap-linReg/index.md)) doorheen de puntenwolk. Een correlatie gelijk aan 0 geeft bijgevolg aan dat een best passende rechte doorheen de puntenwolk helling 0 heeft (d.w.z. dat ze horizontaal verloopt). In Figuur [4.18](index.md) is de correlatie heel laag omdat er bij negatieve <span class="math inline">\$X\$</span>-waarden een dalende associatie is en bij positieve <span class="math inline">\$X\$</span>-waarden een stijgende associatie, zodat de 2 variabelen geen lineaire samenhang meer hebben.

Omwille van het voorgaande fenomeen is het van belang om de aard van samenhang tussen 2 variabelen steeds te onderzoeken via een scatterplot alvorens een correlatiecoëfficiënt te rapporteren. Wanneer het verband monotoon is, maar sterk niet-lineair is, dan is het aangewezen om niet de Pearson correlatiecoëfficiënt, maar Spearman’s correlatiecoëfficiënt te rapporteren.

Figuur [4.19](index.md) geeft het verband van de microarray intensiteitsmetingen weer voor het S100A8 gen in functie van deze voor het ESR1 gen. Het verband is moeilijk interpreteerbaar op de originele schaal door de aanwezigheid van heel hoge intensiteiten (en dus concentraties). Het verband op de originele schaal is exponentieel. Pearson’s correlatiecoëfficiënt zakt hierdoor van -0.89 op log-schaal naar -0.54 op de originele schaal. Spearman’s correlatiecoëfficiënt daarentegen blijft gelijk voor en na transformatie gezien de log2 transformatie monotoon is en de ordening (rangen) van de data niet verandert. Spearman’s correlatiecoëfficiënt blijft -0.73 op de originele schaal alsook op log-schaal en wijst op een sterke negatieve associatie tussen de expressie van beiden genen.

``` {.sourceCode .r}
par(mfrow=c(1,3))
with(borstkanker, scatter.smooth(log2(ESR1),log2(S100A8),span=1/2,        main=paste("Correlatie",c("Pearson","Spearman"),round(c(cor(log2(ESR1),log2(S100A8)),cor(log2(ESR1),log2(S100A8),method = "spearman")),2))))
with(borstkanker, scatter.smooth(ESR1,S100A8,span=1/2,main=paste("Correlatie",c("Pearson","Spearman"),round(c(cor(ESR1,S100A8),cor(ESR1,S100A8,method = "spearman")),2))))
with(borstkanker, scatter.smooth(ESR1,S100A8,span=1/2,ylim=c(0,500),main=paste("Correlatie",c("Pearson","Spearman"),round(c(cor(ESR1,S100A8),cor(ESR1,S100A8,method = "spearman")),2))))
```

<span id="fig:brcaOrigFit"></span> <img src="Statistiek_2019_2020_files/figure-html/brcaOrigFit-1.png" style="width:100.0%" alt="Expressie van het S100A8 gen in functie van de ESR1 gen-expressie op de log2 en originele schaal." />

Figuur 4.19: Expressie van het S100A8 gen in functie van de ESR1 gen-expressie op de log2 en originele schaal.

Indien het verband niet-monotoon is, dan zijn correlatiecoëfficiënten niet geschikt en moet men overstappen op meer geavanceerde regressietechnieken.

1.  Bij jonge kinderen is de grootte van hun schoenmaat uiteraard sterk gecorreleerd met hun leescapaciteiten. Dat op zich impliceert echter niet dat het leren van nieuwe woorden hun voeten doet groeien of dat het groeien van hun voeten impliceert dat ze beter kunnen lezen. Ook algemeen<a href="#fn21" id="fnref21" class="footnoteRef"><sup>21</sup></a> hoeft een correlatie tussen 2 variabelen niet te impliceren dat er een causaal verband is. De relatie tussen 2 metingen kan immers sterk verstoord worden door confounders (bvb. de leeftijd in bovenstaand voorbeeld). Hoewel dit overduidelijk is in bovenstaand voorbeeld, is het in vele andere contexten veel minder duidelijk en worden er, vooral in de populaire literatuur, vaak causale beweringen gemaakt die niet (volledig) door de gegevens worden gestaafd. Volgend voorbeeld illustreert dit.

<span id="exm:unnamed-chunk-61" class="example">**Voorbeeld 4.6 (Associatie versus causatie)** </span>

Wanneer men de incidentie van sterfte ten gevolge van borstkanker uitzet t.o.v. van de vetinname per capita per dag voor een grote steekproef van landen over de ganse wereld, dan stelt men vast dat er sterke positieve correlatie is. Deze correlatie wordt vaak gebruikt om aan te geven dat vetinname leidt tot borstkanker (analoog voor darmkanker). Het bewijs hiervoor is echter zeer zwak. Immers, landen met een grote vetinname hebben ook een hoge inname van suiker. Een grafiek van de incidentie van sterfte ten gevolge van borstkanker t.o.v. van de suikerinname per capita per dag toont een vrijwel even sterke correlatie, hoewel nagenoeg niemand beweert dat suiker borstkanker veroorzaakt. Bovendien zijn vet en suiker op wereldschaal relatief dure producten. Landen met hoge vetinname zijn bijgevolg voornamelijk industrielanden die in heel wat meer verschillen van de andere landen dan alleen hun vetinname… Recente studies (Holmes et al., 1999) hebben intussen sterke indicaties geleverd dat hoog vetverbruik vermoedelijk niet tot borstkanker leidt.

`**Einde voorbeeld**`

1.  Een *ecologische analyse* is een statistische analyse waarbij men associaties bestudeert tussen samenvattingsmaten (zoals gemiddelden, incidenties, …) die reeds berekend werden voor groepen subjecten. Dit is het geval in voorgaand voorbeeld waar de associatie wordt onderzocht tussen de incidentie van sterfte t.g.v. borstkanker en de (gemiddelde) dagelijkse vetinname per capita in verschillende landen. Wanneer men aldus een *ecologische correlatie* vaststelt voor groepen subjecten of individuen (in dit geval, landen), impliceert dat niet noodzakelijk dat deze correlatie ook voor de subjecten zelf opgaat<a href="#fn22" id="fnref22" class="footnoteRef"><sup>22</sup></a>. Volgend voorbeeld illustreert dit.

<span id="exm:unnamed-chunk-62" class="example">**Voorbeeld 4.7 (Ecological fallacy)** </span>

Voor de 48 staten in de V.S. werden telkens 2 getallen berekend: het percentage van de mensen die in een ander land geboren zijn en het percentage geletterden. De correlatie ertussen bedraagt 0.53 (Robinson, 1950). Dit is een *ecologische correlatie* omdat de eenheid van de analyse de groep residenten uit een zelfde staat is, en niet de individuele residenten zelf. Deze ecologische correlatie suggereert dat mensen van vreemde afkomst doorgaans beter geschoold zijn (in Amerikaans Engels) dan de oorspronkelijke inwoners. Wanneer men echter de correlatie berekent op basis van de gegevens voor alle individuele residenten, bekomt men -0.11. De ecologische analyse is hier duidelijk misleidend: het teken van de correlatie is er positief omdat mensen van vreemde origine de neiging hebben om te gaan wonen in staten waar de oorspronkelijke bevolking relatief goed geschoold is.

`**Einde voorbeeld**`

## <span class="header-section-number">4.7</span> Onvolledige gegevens {#onvolledige-gegevens}

Het gebeurt vaak in de biowetenschappen dat, ondanks zorgvuldig veld- en laboratoriumwerk, metingen die men plande te verzamelen, niet bekomen werden. Men noemt deze dan *ontbrekende gegevens* of *missing data (points)*.

Minder drastisch, kunnen observaties soms slechts ten dele gekend zijn. Bijvoorbeeld bij een studie van de overlevingsduur van dieren en planten wacht men niet steeds tot alle subjecten gestorven zijn. Op het eind van de studie zal men bijvoorbeeld voor een 50-jarige olifant die in leven is, slechts weten dat de overlevingstijd minstens 50 jaar bedraagt, maar niet de exacte waarde kennen. Zo’n gegeven wordt *rechts-gecensureerd* genoemd: we weten dat de gewenste observatie rechts van 50 ligt, maar verder niets meer.

Analoog kunnen observaties *links-gecensureerd* zijn. Bij het meten van bepaalde concentraties kan een detectielimiet bestaan: een ondergrens beneden dewelke het meettoestel geen aanwezigheid kan detecteren. Men weet in zo’n geval dat de concentratie kleiner dan die ondergrens is, maar niet hoeveel kleiner.

Tenslotte vermelden we nog *interval-gecensureerde* gegevens. Bij het screenen naar HIV bijvoorbeeld, zal men weten dat een subject seropositief geworden is ergens tussen de laatste negatieve HIV test en de eerste positieve HIV test, maar het exacte tijdstip van seroconversie blijft onbekend.

De aanwezigheid van gegevens die niet of slechts partieel zijn opgemeten zorgt altijd voor extra moeilijkheden bij de analyse en interpretatie van de onderzoeksresultaten. Dat is omdat de missende gegevens mogelijks afkomstig zijn van een speciale populatie. Dat is het meest duidelijk in klinische experimenten bij mensen. Patiënten zullen hier vaak de studie verlaten wanneer ze genezen zijn, in welk geval men de metingen van deze patiënten niet te zien krijgt. Dit negeren door enkel de aanwezige gegevens te analyseren, zal de resultaten er slechter doen uitzien dan ze in werkelijkheid zijn. Meestal houdt dat immers de veronderstelling in dat de aanwezige gegevens representatief blijven voor de populatie die men wenst te bestuderen. Dit kan in sommige gevallen de resultaten sterk vertekenen. In de statistische literatuur zijn de laatste jaren heel wat complexe technieken ontwikkeld om hiervoor te corrigeren. Deze technieken worden meer en meer in de statistische software ingebouwd en recent heeft ook R verschillende bibliotheken toegevoegd. Het is echter aangewezen om voor het gebruik van deze gevorderde technieken een statisticus te consulteren.

------------------------------------------------------------------------

1.  Zie Sectie [4.4.2](index.md).[↩](index.md)

2.  Later zullen we zien dat het nog iets correcter is om te stellen dat 95% van de waarnemingen liggen tussen <span class="math inline">\$\\bar{x} - 1.96 s\_x\$</span> en <span class="math inline">\$\\bar{x} + 1.96 s\_x\$</span>.[↩](index.md)

3.  Hierbij maken we gebruik van het feit dat voor een Normaal verdeelde observatie <span class="math inline">\$X\$</span>, <span class="math inline">\$P(X=a)=0\$</span> voor elk reëel getal <span class="math inline">\$a\$</span>, zodat <span class="math inline">\$P(X\\leq a)=P(X&lt;a)\$</span>.[↩](index.md)

4.  Let wel op want in verschillende boeken krijgt het symbool <span class="math inline">\$z\_{\\alpha}\$</span> verschillende definities\![↩](https://raw.githubusercontent.com/statOmics/statistiekCursusNotas/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-describe.html)

5.  Dit interval bevat niet exact <span class="math inline">\$(1-\\alpha)100\\%\$</span> van de observaties, maar slechts bij benadering, omdat het geen rekening houdt met het feit dat <span class="math inline">\$\\bar x\$</span> en <span class="math inline">\$\\sigma\_x\$</span> impreciese schattingen zijn voor <span class="math inline">\$\\mu\$</span> en <span class="math inline">\$\\sigma\$</span> op basis van een eindige steekproef. Meer accurate referentie-intervallen die deze imprecisie in rekening brengen, ook predictie-intervallen genoemd[↩](index.md)

6.  Merk op dat dit design niet optimaal is omdat replicaties op de verkeerde schaal werden bekomen. Idealiter moesten meer dan 2 stukken grond in de studie opgenomen worden omdat de 2 gekozen stukken grond in veel meer kunnen verschillen dan alleen het bodemtype. Verschillen in de verdeling van houtluizen kunnen bijgevolg niet zomaar aan het bodemtype kunnen toegeschreven worden.[↩](index.md)

7.  Al is het nog de vraag of die associatie toevallig is, dan wel systematisch. We komen in het hoofdstuk [9](../chap-categorisch/index.md). terug op technieken om dit te onderzoeken.[↩](index.md)

8.  Dit is bijvoorbeeld het geval in logistische regressiemodellen die gebruikt worden om het risico op een bepaalde aandoening te modelleren in functie van prognostische factoren.[↩](index.md)

9.  In het Engels is dit welbekend onder de zinsnede *\`Association is not causation!’*.[↩](index.md)

10. In het Engels is dit welbekend onder de naam *\`ecological fallacy’*.[↩](index.md)

---

[← ontbrekende waarnemingen voorkomen.](13-ontbrekende-waarnemingen-voorkomen.md) · [Up: contents](index.md)

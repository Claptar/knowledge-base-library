---
title: Statistische besluitvorming
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/Statistiek_2019_2020.tex
source_file: sources/statomics-statistiekcursusnotas-ghpages/Statistiek_2019_2020.tex
licence: unresolved
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Statistische besluitvorming

**Source:** [`Statistiek_2019_2020.tex`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/Statistiek_2019_2020.tex) · **Licence:** unresolved · Converted 2026-09-14 from `.tex` (high)

## Inleiding {#inleiding-3}

In dit hoofdstuk zullen we werken rond de *Captopril dataset*. Captopril is een medicijn dat wordt voorgeschreven bij hypertensie en chronisch hartfalen. Het behoort tot de klasse van ACE remmers die activiteit van het renine-angiotensine-aldosteronsysteem onderdrukken. Dat systeem zet het hormoon angiotensineI om in angiotensine II, die een krachtige vaatvernauwende werking heeft. ACE remmers verminderen de omzetting van angiotensine I naar angiotensine II waardoor de vaatvernauwing wordt onderdrukt. Tijdens de ontwikkeling van het medicijn werd een eerste kleine studie opgezet om na te gaan of captopril een bloeddrukverlagend effect heeft bij patiënten met hypertensie.

Observaties bij een klein aantal subjecten mogen een onderzoeker er dan al van overtuigen iets nieuws te hebben ontdekt, maar om anderen te overtuigen zijn objectieve, wetenschappelijke argumenten nodig. Vooreerst moeten de resultaten voldoende *representatief* zijn, d.w.z. veralgemeenbaar naar een ruime biologische populatie (bvb. naar de volledige populatie van patiënten met hypertensie). Ten tweede moet er rekening mee gehouden worden dat de resultaten *variabel* zijn, d.w.z. dat men door toeval doorgaans andere resultaten zou vinden indien men een andere, vergelijkbare groep subjecten zou analyseren. Om die reden is het belangrijk om uit te drukken in welke mate de resultaten (bvb. de geschatte bloeddrukdaling) zouden variëren van steekproef tot steekproef en of men op basis van de steekproef kan aantonen dat er een effect is van een behandeling (b.v. dat het middel captopril bloeddrukverlagend werkt in de populatie). Dit vormt het doel van dit hoofdstuk.

Om een representatieve groep subjecten te waarborgen, vertrekt een goede onderzoeksopzet vanuit een belangrijke, precies geformuleerde vraagstelling omtrent een duidelijk omschreven populatie.

Zoals eerder in de cursus aangegeven, zal men in de praktijk om financiële en logistieke redenen bijna nooit een volledige populatie kunnen bestuderen. Populatieparameters kunnen daarom meestal niet exact bepaald worden. Enkel een deel van de populatie kan onderzocht worden, wat men een *steekproef* noemt. Volgens een gestructureerd design worden daartoe lukraak subjecten uit de doelpopulatie getrokken en geobserveerd. De onbekende parameters worden vervolgens geschat o.b.v. die steekproef en noemt men schattingen. In de praktijk hoopt men uiteraard dat de schattingen die men bekomt op basis van de steekproef vergelijkbaar zijn met de overeenkomstige populatieparameters die men voor de volledige populatie zou bekomen.
Typisch kan de onderzoeksvraag worden vertaald naar een populatieparameter. Ze kan bijvoorbeeld worden uitgedrukt in termen van een populatiegemiddelde, bijvoorbeeld de gemiddelde bloeddrukverandering na de inname van captopril bij patiënten met hypertensie.

## Captopril voorbeeld {#captopril-voorbeeld}

Onderzoekers wensen na te gaan of het medicijn Captopril een bloeddruk verlagend effect heeft. De onderzoekers wensen uitspraken te kunnen doen over het effect van captopril op de systolische bloeddruk van huidige en toekomstige patiënten met hypertensie, m.a.w. ze wensen uitspraken te doen over het effect van captopril op het niveau van de *Populatie*. Ze zullen hiervoor een experiment opzetten om het effect van captopril bestuderen (*Proefopzet*) waarbij een *steekproef* (sample) van de patiënten met hypertensie is getrokken uit de populatie. Vervolgens zullen ze de data exploreren en het effect van captopril besturen in de steekproef (*Data Exploratie & Beschrijvende Statistiek*). Op basis van de steekproef zullen ze dan het effect van captopril *Schatten* in de populatie en zullen ze a.d.h.v. methoden uit *Statistische besluitvorming*[^23] nagaan in hoeverre de geobserveerde effecten in de steekproef veralgemeend kunnen worden naar de algemene populatie toe.

Deze verschillende stappen worden geïllustreerd in Figuur <a href="#fig:captoPop2Samp2Pop" data-reference-type="ref" data-reference="fig:captoPop2Samp2Pop">5.1</a>.

<figure id="fig:captoPop2Samp2Pop">
<img src="Statistiek_2019_2020_files/figure-latex/captoPop2Samp2Pop-1" style="width:100.0%" />
<figcaption>Verschillende stappen in de captopril studie.</figcaption>
</figure>

### Proefopzet {#proefopzet}

Bij proefopzet zullen we een gestructureerd design voorstellen om lukraak subjecten uit de doelpopulatie te selecteren, toe te wijzen aan een behandeling en te observeren. We zullen hierbij een response variabele meten, een karakteristiek van interesse. In het captopril voorbeeld is dit de systolische bloeddruk.

In de captopril studie hebben de onderzoekers gebruik gemaakt van een een pre-test/post-test design. De patiënten werden at random gekozen uit de populatie. Van elke patiënt in de studie werd de systolische en diasystolische bloeddruk gemeten voor en na het toedienen van captopril. Het pre-test/post-test design heeft als voordeel dat we het effect van het toedienen van captopril op de bloeddruk kunnen meten voor elke patiënt. Een nadeel daarentegen is dat er geen controle behandeling is waardoor we een mogelijkse bloeddrukverlaging niet noodzakelijkerwijs kunnen toeschrijven aan de werking van captopril. Er zou immers ook een placebo-effect kunnen optreden waardoor de bloeddruk van de patiënt daalt omdat men weet dat men een medicijn kreeg tegen een hoge bloeddruk.

### Data Exploratie & Beschrijvende Statistiek {#data-exploratie-beschrijvende-statistiek}

Eens de data zijn geobserveerd, is het belangrijk om deze te exploreren om inzicht te krijgen in hun verdeling en karakteristieken. Vervolgens zullen we de gegevens samenvatten zodat we het effect van interesse kunnen kwantificeren in de steekproef. In deze studie is de systolische bloeddruk en de diasystolische bloeddruk gemeten voor elke patiënt voor en na het toedienen van captopril. De data is opgeslagen in een tekstbestand met naam `captopril.txt` in de folder dataset. We zullen eerst exploreren welke figuren nuttig zijn in onze context. In wetenschappelijke artikels worden vaak figuren gemaakt van het gemiddelde en de standaardafwijking (zie Figuur <a href="#fig:captoBar" data-reference-type="ref" data-reference="fig:captoBar">5.2</a>).

<span style="color: 0.56,0.35,0.01">*\# Eerst lezen we de data in. Deze bevindt zich in*</span> <span style="color: 0.56,0.35,0.01">*\# de subdirectory dataset Het is een tekstbestand*</span> <span style="color: 0.56,0.35,0.01">*\# waarbij de kolommen van elkaar gescheiden zijn*</span> <span style="color: 0.56,0.35,0.01">*\# d.m.v kommas. sep=’,’ De eerste rij bevat de*</span> <span style="color: 0.56,0.35,0.01">*\# namen van de variabelen*</span> captopril &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**read.table**</span>(<span style="color: 0.31,0.60,0.02">"dataset/captopril.txt"</span>, <span style="color: 0.13,0.29,0.53">header =</span> <span style="color: 0.56,0.35,0.01">TRUE</span>, <span style="color: 0.13,0.29,0.53">sep =</span> <span style="color: 0.31,0.60,0.02">","</span>) <span style="color: 0.13,0.29,0.53">**head**</span>(captopril)

    ##   id SBPb DBPb SBPa DBPa
    ## 1  1  210  130  201  125
    ## 2  2  169  122  165  121
    ## 3  3  187  124  166  121
    ## 4  4  160  104  157  106
    ## 5  5  167  112  147  101
    ## 6  6  176  101  145   85

<span style="color: 0.56,0.35,0.01">*\# We gebruiken de apply functie om het gemiddelde*</span> <span style="color: 0.56,0.35,0.01">*\# en de standaard deviatie te berekenen voor de*</span> <span style="color: 0.56,0.35,0.01">*\# kolommen die bloeddruk data bevatten (kolom 2:4)*</span> <span style="color: 0.56,0.35,0.01">*\# We gebruiken argument MARGIN=2 om de functie toe*</span> <span style="color: 0.56,0.35,0.01">*\# te passen op de kolommen MARGIN=1 kan gebruikt*</span> <span style="color: 0.56,0.35,0.01">*\# worden om de functie op de rijen toe te passen*</span> mm &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**apply**</span>(captopril$$, <span style="color: 0.00,0.00,0.81">2</span><span style="color: 0.81,0.36,0.00">**:**</span><span style="color: 0.00,0.00,0.81">5</span>$$, <span style="color: 0.13,0.29,0.53">MARGIN =</span> <span style="color: 0.00,0.00,0.81">2</span>, <span style="color: 0.13,0.29,0.53">FUN =</span> mean) hh &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**apply**</span>(captopril$$, <span style="color: 0.00,0.00,0.81">2</span><span style="color: 0.81,0.36,0.00">**:**</span><span style="color: 0.00,0.00,0.81">5</span>$$, <span style="color: 0.13,0.29,0.53">MARGIN =</span> <span style="color: 0.00,0.00,0.81">2</span>, <span style="color: 0.13,0.29,0.53">FUN =</span> sd)

mp &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**barplot**</span>(mm, <span style="color: 0.13,0.29,0.53">ylim =</span> <span style="color: 0.13,0.29,0.53">**c**</span>(<span style="color: 0.00,0.00,0.81">0</span>, <span style="color: 0.00,0.00,0.81">250</span>), <span style="color: 0.13,0.29,0.53">ylab =</span> <span style="color: 0.31,0.60,0.02">"Gemiddelde bloeddruk (mmHg)"</span>, <span style="color: 0.13,0.29,0.53">main =</span> <span style="color: 0.31,0.60,0.02">""</span>) <span style="color: 0.56,0.35,0.01">*\# fouten vlaggen*</span> <span style="color: 0.13,0.29,0.53">**segments**</span>(mp, mm, mp, mm <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">2</span> <span style="color: 0.81,0.36,0.00">**\***</span><span style="color: 0.31,0.60,0.02"> </span>hh) <span style="color: 0.13,0.29,0.53">**segments**</span>(mp <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">0.2</span>, mm <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">2</span> <span style="color: 0.81,0.36,0.00">**\***</span><span style="color: 0.31,0.60,0.02"> </span>hh, mp <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">0.2</span>, mm <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">2</span> <span style="color: 0.81,0.36,0.00">**\***</span><span style="color: 0.31,0.60,0.02"> </span> <span style="color: 0.31,0.60,0.02"> </span>hh)

<figure id="fig:captoBar">
<img src="Statistiek_2019_2020_files/figure-latex/captoBar-1" style="width:100.0%" />
<figcaption>Barplot van de gemiddelde bloeddruk in de captopril studie. De foutenvlag is 2x de standaard deviatie op de metingen (SBPb: systolic BloodPressure before, DBPb: Diasystolic BloodPressure before, SBPa: systolic BloodPressure after, DBPa: Diasystolic BloodPressure after).</figcaption>
</figure>

De figuur is echter niet informatief. De hoogte van de balken zegt enkel iets over het gemiddelde. We kunnen onmogelijk weten wat het bereik van de ruwe gegevens is bijvoorbeeld. Daarom is het beter om de gegevens zo ruw mogelijk weer te geven in een plot. We kunnen hiervoor bijvoorbeeld gebruik maken van boxplots (Figuur <a href="#fig:captoBox" data-reference-type="ref" data-reference="fig:captoBox">5.3</a>). Aangezien we maar over 15 patiënten beschikken kunnen we ook de ruwe datapunten toevoegen. In de figuur zien we dat de systolische bloeddruk in de steekproef gemiddeld lager ligt na de behandeling met captopril. We krijgen ook een duidelijk beeld op het bereik van de data.

<span style="color: 0.13,0.29,0.53">**boxplot**</span>(captopril$$, <span style="color: 0.00,0.00,0.81">2</span><span style="color: 0.81,0.36,0.00">**:**</span><span style="color: 0.00,0.00,0.81">5</span>$$, <span style="color: 0.13,0.29,0.53">ylim =</span> <span style="color: 0.13,0.29,0.53">**c**</span>(<span style="color: 0.00,0.00,0.81">0</span>, <span style="color: 0.00,0.00,0.81">250</span>), <span style="color: 0.13,0.29,0.53">ylab =</span> <span style="color: 0.31,0.60,0.02">"Bloeddruk (mmHg)"</span>, <span style="color: 0.13,0.29,0.53">main =</span> <span style="color: 0.31,0.60,0.02">""</span>) <span style="color: 0.56,0.35,0.01">*\# toevoegen van originele datapunten op de plot*</span> <span style="color: 0.56,0.35,0.01">*\# jitter zal de punten random verspreiden set seed*</span> <span style="color: 0.56,0.35,0.01">*\# om gekleurde volle bol pch=19 te zetten en daarna*</span> <span style="color: 0.56,0.35,0.01">*\# een zwarte rand te kunnen zetten op zelfde*</span> <span style="color: 0.56,0.35,0.01">*\# plaats.*</span> <span style="color: 0.13,0.29,0.53">**set.seed**</span>(<span style="color: 0.00,0.00,0.81">19</span>) <span style="color: 0.13,0.29,0.53">**stripchart**</span>(captopril$$, <span style="color: 0.00,0.00,0.81">2</span><span style="color: 0.81,0.36,0.00">**:**</span><span style="color: 0.00,0.00,0.81">5</span>$$, <span style="color: 0.13,0.29,0.53">vertical =</span> <span style="color: 0.56,0.35,0.01">TRUE</span>, <span style="color: 0.13,0.29,0.53">method =</span> <span style="color: 0.31,0.60,0.02">"jitter"</span>, <span style="color: 0.13,0.29,0.53">pch =</span> <span style="color: 0.00,0.00,0.81">19</span>, <span style="color: 0.13,0.29,0.53">col =</span> <span style="color: 0.13,0.29,0.53">**c**</span>(<span style="color: 0.31,0.60,0.02">"bisque"</span>, <span style="color: 0.31,0.60,0.02">"coral"</span>, <span style="color: 0.31,0.60,0.02">"darkcyan"</span>, <span style="color: 0.31,0.60,0.02">"purple"</span>), <span style="color: 0.13,0.29,0.53">add =</span> <span style="color: 0.56,0.35,0.01">TRUE</span>) <span style="color: 0.13,0.29,0.53">**set.seed**</span>(<span style="color: 0.00,0.00,0.81">19</span>) <span style="color: 0.13,0.29,0.53">**stripchart**</span>(captopril$$, <span style="color: 0.00,0.00,0.81">2</span><span style="color: 0.81,0.36,0.00">**:**</span><span style="color: 0.00,0.00,0.81">5</span>$$, <span style="color: 0.13,0.29,0.53">vertical =</span> <span style="color: 0.56,0.35,0.01">TRUE</span>, <span style="color: 0.13,0.29,0.53">method =</span> <span style="color: 0.31,0.60,0.02">"jitter"</span>, <span style="color: 0.13,0.29,0.53">pch =</span> <span style="color: 0.00,0.00,0.81">1</span>, <span style="color: 0.13,0.29,0.53">col =</span> <span style="color: 0.00,0.00,0.81">1</span>, <span style="color: 0.13,0.29,0.53">add =</span> <span style="color: 0.56,0.35,0.01">TRUE</span>)

<figure id="fig:captoBox">
<img src="Statistiek_2019_2020_files/figure-latex/captoBox-1" style="width:100.0%" />
<figcaption>Boxplot en ruwe data van de bloeddruk in de captopril studie (SBPb: systolic BloodPressure before, DBPb: Diasystolic BloodPressure before, SBPa: systolic BloodPressure after, DBPa: Diasystolic BloodPressure after).</figcaption>
</figure>

Als alle bloeddrukmetingen onafhankelijk zouden zijn dan is Figuur <a href="#fig:captoBox" data-reference-type="ref" data-reference="fig:captoBox">5.3</a> een goede figuur om de data te exploreren. We weten echter dat de metingen voor en na het toedienen van captopril afkomstig zijn van dezelfde patiënt. We kunnen die informatie toevoegen in een dotplot zoals we illustreren voor de systolische bloeddruk in Figuur <a href="#fig:captoDotBsl" data-reference-type="ref" data-reference="fig:captoDotBsl">5.4</a>. In deze figuur zijn de twee bloeddrukmetingen voor dezelfde persoon verbonden met een lijn. Deze figuur geeft duidelijk weer dat de bloeddruk daalt voor elke patiënt wat een sterke aanwijzing is dat er een effect is van het toedienen van captopril op de systolische bloeddruk.

<span style="color: 0.56,0.35,0.01">*\# D.m.v de matplot functie kunnen we eenvoudig de*</span> <span style="color: 0.56,0.35,0.01">*\# data van dezelfde patient (per kolom) vandaar dat*</span> <span style="color: 0.56,0.35,0.01">*\# we de dataset transponeren (t(.)) functie en*</span> <span style="color: 0.56,0.35,0.01">*\# verbinden a.d.h.v. een lijn. (lty=1) we gebruiken*</span> <span style="color: 0.56,0.35,0.01">*\# ook een dezelfde kleur. en gebruiken zowel een*</span> <span style="color: 0.56,0.35,0.01">*\# punt als een lijn om de data voor te stellen*</span> <span style="color: 0.56,0.35,0.01">*\# type=’b’*</span> <span style="color: 0.13,0.29,0.53">**matplot**</span>(<span style="color: 0.13,0.29,0.53">**t**</span>(captopril$$, <span style="color: 0.13,0.29,0.53">**c**</span>(<span style="color: 0.31,0.60,0.02">"SBPb"</span>, <span style="color: 0.31,0.60,0.02">"SBPa"</span>)$$), <span style="color: 0.13,0.29,0.53">pch =</span> <span style="color: 0.00,0.00,0.81">1</span>, <span style="color: 0.13,0.29,0.53">lty =</span> <span style="color: 0.00,0.00,0.81">1</span>, <span style="color: 0.13,0.29,0.53">col =</span> <span style="color: 0.31,0.60,0.02">"black"</span>, <span style="color: 0.13,0.29,0.53">type =</span> <span style="color: 0.31,0.60,0.02">"b"</span>, <span style="color: 0.13,0.29,0.53">xaxt =</span> <span style="color: 0.31,0.60,0.02">"none"</span>, <span style="color: 0.13,0.29,0.53">xlim =</span> <span style="color: 0.13,0.29,0.53">**c**</span>(<span style="color: 0.00,0.00,0.81">0.5</span>, <span style="color: 0.00,0.00,0.81">2.5</span>), <span style="color: 0.13,0.29,0.53">ylab =</span> <span style="color: 0.31,0.60,0.02">"Systolische bloeddruk (mmHg)"</span>, <span style="color: 0.13,0.29,0.53">cex =</span> <span style="color: 0.00,0.00,0.81">0.5</span>) <span style="color: 0.13,0.29,0.53">**axis**</span>(<span style="color: 0.00,0.00,0.81">1</span>, <span style="color: 0.13,0.29,0.53">**c**</span>(<span style="color: 0.00,0.00,0.81">1</span>, <span style="color: 0.00,0.00,0.81">2</span>), <span style="color: 0.13,0.29,0.53">labels =</span> <span style="color: 0.13,0.29,0.53">**c**</span>(<span style="color: 0.31,0.60,0.02">"voor"</span>, <span style="color: 0.31,0.60,0.02">"na"</span>))

<figure id="fig:captoDotBsl">
<img src="Statistiek_2019_2020_files/figure-latex/captoDotBsl-1" style="width:100.0%" />
<figcaption>Dotplot van de systolische bloeddruk in de captopril studie voor en na het toedienen van captopril.</figcaption>
</figure>

Aangezien we slechts twee bloeddrukmetingen hebben per patiënt kunnen we het effect van captopril ook berekenen per patiënt door het verschil in de systolische bloeddruk na en voor de toediening van captopril te berekenen. Dat is één van de voordelen van een pre-test/post-test design.

<figure id="fig:captoBoxDelta">
<img src="Statistiek_2019_2020_files/figure-latex/captoBoxDelta-1" style="width:100.0%" />
<figcaption>Boxplot van het verschil in systolische bloeddruk voor en na het toedienen van captopril.</figcaption>
</figure>

We observeren in Figuur <a href="#fig:captoBoxDelta" data-reference-type="ref" data-reference="fig:captoBoxDelta">5.5</a> een bloeddrukdaling voor elke patiënt in de steekproef wat opnieuw een heel sterke indicatie is voor een gunstig effect van het toedienen van captopril op de bloeddruk. De verschillen in systolische bloeddruk zijn een goede maat om het effect van captopril te bepalen. We kunnen de data als volgt samenvatten.

<span style="color: 0.13,0.29,0.53">**summary**</span>(delta)

    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
    ##  -33.00  -24.50  -20.00  -18.93  -13.50   -3.00

<span style="color: 0.13,0.29,0.53">**sd**</span>(delta)

    ## [1] 9.027471

We observeren gemiddeld een systolische bloeddrukdaling van 18.93 mmHg en een standaard deviatie van 9.03 mmHg.

### Schatten {#schatten}

Pre-test/post-test design: Het effect van captopril in de steekproef kan worden bestudeerd door het verschil te bepalen in systolische bloeddruk na en voor de behandeling ($X=\Delta_\text{na-voor}$)! Hoe kunnen we de bloeddrukverschillen modelleren en het effect van het toedienen van captopril schatten?

<figure id="fig:captoBoxDiffQQ">
<img src="Statistiek_2019_2020_files/figure-latex/captoBoxDiffQQ-1" style="width:100.0%" />
<figcaption>QQ-plot voor het verschil in systolische bloeddruk voor en na het toedienen van captopril.</figcaption>
</figure>

    ## [1] 4 2

We zien geen grote afwijkingen van Normaliteit in Figuur <a href="#fig:captoBoxDiffQQ" data-reference-type="ref" data-reference="fig:captoBoxDiffQQ">5.6</a>. We kunnen de bloeddrukverschillen dus modelleren aan de hand van een Normale verdeling en kunnen het effect van captopril in de populatie beschrijven a.d.h.v. de gemiddelde bloeddrukverschil $\mu$. Het bloeddrukverschil $\mu$ in de populatie kan worden geschat a.d.h.v. het steekproefgemiddelde $\bar x$=-18.93 en de standaard afwijking $\sigma$ a.d.h.v. de steekproefstandaarddeviatie $\text{SD}$=9.03.

We vragen ons nu af of het effect dat we observeren in de steekproef groot genoeg is om te kunnen spreken van een effect van captopril in de populatie. We weten immers dat onze statistiek voor de schatting van het effect van captopril in de populatie berekend wordt op basis van de gegevens uit de steekproef en daarom zal variëren van steekproef tot steekproef. Het is daarom belangrijk om een inzicht te krijgen in hoe het steekproefgemiddelde zal variëren van steekproef tot steekproef.

## Puntschatters: het steekproefgemiddelde {#puntschatters-het-steekproefgemiddelde}

Zij $X$ een lukrake trekking uit de populatie van de bestudeerde karakteristiek en onderstel dat haar theoretische verdeling$$bvb. de Normale verdeling$$ een gemiddelde $\mu$ en variatie $\sigma^2$ heeft. Onderstel bovendien dat we geïnteresseerd zijn in het gemiddelde $\mu$ van die karakteristiek in de studiepopulatie. Dan kunnen we $\mu$ schatten op basis van een eenvoudige lukrake steekproef, $X_1,...,X_n$, als het (rekenkundig) gemiddelde

$$\begin{equation*}
\bar X = \frac{X_1+ X_2+ ... + X_n}{n} = \frac{\sum_{i=1}^{n} X_i}{n}
\end{equation*}$$

van de toevalsveranderlijken $X_1,X_2, ..., X_n$. Dit wordt het *steekproefgemiddelde* genoemd. Het is belangrijk om te begrijpen dat het steekproefgemiddelde opnieuw een toevalsveranderlijke[^24] is, d.w.z. dat haar waarde zal variëren van steekproef tot steekproef. Hoewel er slechts 1 populatie is, zijn er heel wat verschillende steekproeven die men daaruit kan trekken. Dat heeft tot gevolg dat verschillende onderzoekers (die verschillende steekproeven uit dezelfde populatie analyseren) verschillende waarden zullen vinden voor het steekproefgemiddelde. Om die reden heeft het steekproefgemiddelde zelf een verdeling. Men zou die theoretisch kunnen bekomen door een oneindig aantal keer een steekproef van $n$ experimentele eenheden uit de populatie te trekken, telkens het steekproefgemiddelde te berekenen en al deze steekproefgemiddelden vervolgens uit te zetten in een histogram.

We zullen in deze sectie de theoretische verdeling van het steekproefgemiddelde bestuderen. Dat is belangrijk (a) omdat ze ons inzicht geeft in welke mate het resultaat van de studie zou variëren indien men een nieuwe, gelijkaardige studie zou opzetten; en (b) omdat ze ons leert hoe ver $\bar X$ van het gezochte populatiegemiddelde $\mu$ kan afwijken. Omdat we slechts over 1 steekproef beschikken (en dus slechts over 1 observatie voor $\bar X$), is het niet evident[^25] hoe we inzicht kunnen ontwikkelen in de verdeling van het steekproefgemiddelde. In het vervolg van deze sectie tonen we hoe dit toch mogelijk is op basis van de beschikbare steekproef wanneer we bepaalde aannames doen over de gegevens.

### Het steekproefgemiddelde is onvertekend {#het-steekproefgemiddelde-is-onvertekend}

In de praktijk hoopt men uiteraard dat de schattingen die men bekomt op basis van de steekproef vergelijkbaar zijn met de overeenkomstige populatieparameters die men voor de volledige populatie zou bekomen.
Of dat zo is, hangt er in eerste instantie vanaf of de steekproef representatief is voor de studiepopulatie en bijgevolg of men al dan niet lukraak individuen uit de populatie gekozen heeft ter observatie (m.a.w. het hangt af van het design van de studie). Het volgende voorbeeld illustreert dit.

**Voorbeeld 5.1** (Ecstasy). <span id="exm:unnamed-chunk-64"></span><span id="exm:unnamed-chunk-64" label="exm:unnamed-chunk-64"></span>

Aan Stanford University werd een survey uitgevoerd om de prevalentie van ecstasy-gebruik onder de studenten van deze universiteit te bepalen. Twee assistenten werden op het hoofdplein van de campus geplaatst en kregen de opdracht om alle studenten te interviewen die op bepaalde tijdstippen voorbij kwamen. Van de 369 studenten die geïnterviewd werden, rapporteerde 39% ooit ecstasy gebruikt te hebben. Dit resultaat wordt uiteraard deels bepaald door het algemene ecstasy-gebruik onder Stanford-studenten (d.i. door de verdeling van het ecstasy-gebruik over de populatie van Stanford-studenten). Maar ook door het feit dat de studenten die geïnterviewd werden, vermoedelijk een selectieve groep vormen van studenten die bijvoorbeeld niet in de les aanwezig waren of die in de buurt van het hoofdplein les kregen en bijgevolg voornamelijk uit 1 bepaalde studierichting afkomstig waren.

`**Einde voorbeeld**`

Omwille hiervan is het design van een studie van primair belang om lukrake en representatieve steekproeven te garanderen (zie Sectie <a href="#sec:steekproefdesigns" data-reference-type="ref" data-reference="sec:steekproefdesigns">3.2</a>). Zoals u doorheen deze cursus zult vaststellen, zullen de meeste wetenschappelijke rapporten daarom een gedetailleerde beschrijving geven van de manier waarop de data bekomen werden. Dit moet de lezer toelaten om de validiteit van de studie te beoordelen.

Algemeen zullen we met $E(X)$, $\text{Var}(X)$ en $\text{Cor}(X,Y)$ respectievelijk het gemiddelde, de variantie en de correlatie noteren van 2 toevalsveranderlijken $X$ en $Y$ in de populatie. Deze worden respectievelijk de *theoretische verwachtingswaarde* van $X$, *theoretische variantie* van $X$ en *theoretische correlatie* van $X$ en $Y$ genoemd. Men zou ze bekomen door voor alle individuen in de populatie de karakteristieken $X$ en $Y$ op te meten en vervolgens respectievelijk het rekenkundig gemiddelde, de variantie en de Pearson correlatie te berekenen. Om die reden blijven de rekenregels voor gemiddelden en varianties geldig[^26] voor populatiegemiddelden en -varianties.

In de onderstelling dat we over een eenvoudige lukrake steekproef beschikken van metingen $X_1,...,X_n$ voor een karakteristiek $X$, volgen $X_1,...,X_n$ allen dezelfde verdeling. In het bijzonder hebben ze allen gemiddelde $\mu$ en variantie $\sigma^2$; d.i. $E(X_1)=...=E(X_n)=\mu$ en $\text{Var}(X_1)=...=\text{Var}(X_n)=\sigma^2$. Het feit dat we subjecten 1 tot $n$ lukraak uit de populatie getrokken hebben, staat er m.a.w. garant voor dat verdeling van de karakteristiek in deze steekproef representatief is voor de theoretische verdeling in de doelpopulatie. Gebruik makend van de rekenregels voor gemiddelden, vinden we bijgevolg dat:

$$\begin{eqnarray*}
E(\bar X) &=& E \left(\frac{X_1+ X_2+ ... + X_n}{n}\right) \\
&= & \frac{E(X_1)+ E(X_2)+ ... + E(X_n)}{n} \\
&=& \frac{\mu + \mu + ... +\mu}{n} \\
&= & \mu
\end{eqnarray*}$$

Dit geeft aan dat het verwachte steekproefgemiddelde in een eenvoudige lukrake steekproef gelijk is aan het beoogde populatiegemiddelde $\mu$. Men zegt dan dat $\bar X$ een *onvertekende schatter* is voor $\mu$. We kunnen in dat geval verwachten dat de waarde $\bar x$ die we schatten voor $\mu$ op basis van de steekproef, niet systematisch hoger of lager dan de gezochte waarde $\mu$ zal zijn. Het spreekt voor zich dat dit een zeer wenselijke eigenschap is.

**Definitie 5.1** (Onvertekende schatter). <span id="def:unnamed-chunk-65"></span><span id="def:unnamed-chunk-65" label="def:unnamed-chunk-65"></span> Een statistiek of schatter $S$ voor een parameter $\theta$ wordt **onvertekend** genoemd als haar theoretische verwachtingswaarde gelijk is aan die parameter, d.w.z. $E(S)= \theta$.

**Einde definitie**

### Imprecisie/standard error {#imprecisiestandard-error}

Het feit dat het steekproefgemiddelde (over een groot aantal vergelijkbare studies) *gemiddeld* gezien niet afwijkt van de gezochte waarde $\mu$, impliceert niet dat ze niet rond die waarde varieert. Om inzicht te krijgen hoe dicht we het steekproefgemiddelde bij $\mu$ mogen verwachten, wensen we bijgevolg ook haar variabiliteit te kennen. Om dit te bepalen, zullen we ervan uitgaan dat de metingen $X_1, X_2, ..., X_n$ werden gemaakt bij $n$ *onafhankelijke* observationele eenheden. In woorden betekent onafhankelijkheid dat elk subject een volledig nieuw stukje informatie bijdraagt tot het geheel. Een voorbeeld van afhankelijkheid tussen studie-objecten komt klassiek uit de studie van kankerverwekkende stoffen. Bij testen op zwangere ratten, worden metingen gedaan op hun levende foetussen of boorlingen. Foetussen van eenzelfde moeder delen dezelfde genetische achtergrond en zijn daarom waarschijnlijk meer aan elkaar gelijk dan foetussen van verschillende moeders. Zelfs al zijn de moeders die opgenomen worden in zo’n studie onafhankelijk van elkaar gekozen, de verschillende kleine ratjes leveren niet langer onafhankelijke stukjes informatie: via de gedeelde moeders is een afhankelijkheid ingebouwd. Afhankelijke gegevens worden ondermeer ook verzameld in pre-test/post-test designs en cross-over studies. De volgende eigenschap illustreert de noodzaak om over onafhankelijke gegevens te beschikken, wil men gemakkelijk de variabiliteit van het steekproefgemiddelde kunnen bepalen.

**Eigenschap**

Als $X$ en $Y$ onafhankelijke toevalsveranderlijken zijn, dan geldt[^27]:

$$\begin{equation*}
\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)
\end{equation*}$$

Algemeen (d.i. voor mogelijks afhankelijke toevalsveranderlijken $X$ en $Y$) geldt voor constanten $a$ en $b$:

$$\begin{eqnarray*}
\text{Var}(aX+bY) &=& a^2 \text{Var}(X) + b^2 \text{Var}(Y) + 2 ab {%
\text{Cor}}(X,Y)\sqrt{\text{Var}(X)}\sqrt{\text{Var}(Y)}
\end{eqnarray*}$$

**Einde Eigenschap**

Een veelgemaakte fout is dat men beweert dat $\text{Var}(X-Y)=\text{Var}(X)-\text{Var}(Y)$. Niets is minder waar! Stel bijvoorbeeld dat de lengte $X$ van moeders en de lengte $Y$ van vaders evenveel variëren zodat $\text{Var}(X)=\text{Var}(Y)$. Dan impliceert dat nog niet dat als je het verschil $X-Y$ neemt tussen de lengte van een moeder en haar partner, dat dit verschil variantie nul heeft; d.w.z. dat het niet varieert en bijgevolg voor alle moeder-vader paren exact dezelfde waarde aanneemt! Bovenstaande formules geven inderdaad integendeel aan dat:

$$\begin{equation*}
\text{Var}(X-Y) = \text{Var}(X) + \text{Var}(Y) -2{\text{Cor}}(X,Y)\sqrt{\text{Var}(X)}\sqrt{\text{Var}(Y)}.
\end{equation*}$$

Gebruik makend van deze rekenregels en steunend op de onafhankelijkheid van de observaties (waarvan we gebruik maken in de derde overgang, \*) kunnen we nu verder berekenen dat:

$$\begin{eqnarray*}
\text{Var}(\bar X)&=&\text{Var} \left(\frac{X_1+ X_2+ ... + X_n}{n}\right) \\
&= & \frac{\text{Var} (X_1+ X_2+ ... + X_n)}{n^2} \\
&\overset{*}{=} & \frac{\text{Var}(X_1)+ \text{Var}(X_2)+ ... + \text{Var}(X_n)}{n^2} \\
&=& \frac{\sigma^2 + \sigma^2 + ... \sigma^2}{n^2} \\
&= & \frac{\sigma^2}{n}.
\end{eqnarray*}$$

Het steekproefgemiddelde heeft dus een spreiding (standaarddeviatie) rond haar gemiddelde $\mu$ die $\sqrt{n}$ keer kleiner is dan de deviatie op de oorspronkelijke observaties. Vandaar dat we meer over $\mu$ kunnen leren door het steekproefgemiddelde $\bar X$ te observeren dan door een individuele waarde $X$ te observeren.

**Definitie 5.2** (Standaard error). <span id="def:unnamed-chunk-66"></span><span id="def:unnamed-chunk-66" label="def:unnamed-chunk-66"></span> De standaarddeviatie van $\bar{X}$ is $\sigma/\sqrt{n}$ en krijgt in de literatuur de speciale naam {standard error} van het gemiddelde. Algemeen noemt men de standaarddeviatie van een schatter voor een bepaalde parameter $\theta$, de **standard error** van die schatter. Men noteert dit als $SE$.

**Einde definitie**

**Voorbeeld 5.2** (Gemiddelde bloeddrukverandering). <span id="exm:unnamed-chunk-67"></span><span id="exm:unnamed-chunk-67" label="exm:unnamed-chunk-67"></span>

Stel dat we $n = 15$ systolische bloeddrukobservaties zullen meten en dat de standaarddeviatie van de bloeddrukverschillen in de populatie $\sigma = 9.0$ mmHg bedraagt, dan is standard error (SE) van de systolische bloeddrukveranderingen $\bar X$: $$SE= \frac{9.0}{\sqrt{15}}=2.32\text{mmHg.}$$

Meestal is $\sigma$, en bijgevolg de standard error van het steekproefgemiddelde, ongekend. Men moet dan de standard error schatten. Een voor de hand liggende schatter met goede eigenschappen is $S/\sqrt{n},$ waarbij $S^2$ de *steekproefvariantie* van de reeks observaties $X_1,...,X_n$ is en $S$ de *steekproef standaarddeviatie* wordt genoemd.

Voor het captopril voorbeeld kunnen we de standard error op het steekproefgemiddelde van de bloeddrukveranderingen schatten in R als

n =<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**length**</span>(delta) se =<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**sd**</span>(delta)<span style="color: 0.81,0.36,0.00">**/**</span><span style="color: 0.13,0.29,0.53">**sqrt**</span>(n) se

    ## [1] 2.330883

#### Standaarddeviatie vs standard error {#standaarddeviatie-vs-standard-error}

Er is vaak nogal wat verwarring over het onderscheid tussen standard error en standaarddeviatie. De standard error verwijst steeds naar de spreiding op een geschatte parameter zoals het steekproefgemiddelde. Omdat een schatting steeds precieser wordt naarmate de steekproef groter wordt, daalt de standard error met stijgende steekproefgrootte $n$. Als de term standaarddeviatie verwijst naar het steekproefgemiddelde (m.a.w. als men spreekt over de standaarddeviatie van het steekproefgemiddelde), dan is deze standaarddeviatie identiek gelijk aan de standard error. Als ze verwijst naar de individuele observaties, dan niet. Dit kun je ondermeer zien aan het feit dat de individuele observaties niet minder variabel zijn in grote steekproeven dan in kleine steekproeven; m.a.w. de standaarddeviatie van de individuele observaties neemt niet af naarmate de steekproef groter wordt, het is immers een karakteristiek van de populatie.

De standaarddeviatie op de observaties is een maat voor de variabiliteit tussen individuen met betrekking tot een bepaalde meetwaarde. De standaard error van een schatter meet de onzekerheid in die schatter voor een bepaalde parameter.

Beide statistieken worden ook anders beïnvloed door de steekproefgrootte. De variabiliteit in de populatie verandert niet. Buiten het feit dat we de standaarddeviatie meer nauwkeurig kunnen schatten in een grotere steekproef zal ze dus steeds in dezelfde grootteorde liggen. Ze heeft als verwachte waarde immers de theoretische standaarddeviatie $\sigma$ in de populatie. De standard error van een schatter wordt echter sterk beïnvloed door de steekproefgrootte: hoe groter de steekproef hoe nauwkeuriger de schatter voor een bepaalde parameter en hoe kleiner zijn standard error!

#### Geclusterde metingen {#geclusterde-metingen}

De data in studies zijn niet altijd onafhankelijk. Dat heeft zijn consequenties voor het schatten van de standaard errors. Beschouw een studiedesign waarbij voor $n$ planten, tijdens een bepaalde fase in de groei, de expressie van een bepaald gen 2 maal wordt gemeten om meetfouten te drukken. Men is geïnteresseerd in de gemiddelde genexpressie. Als we met $Y_{i1}$ en $Y_{i2}$ de eerste en tweede meting, respectievelijk, voorstellen voor plant $i=1,...,n$, dan kunnen we dit schatten als

$$\begin{equation*}
\bar Y = \sum_{i=1}^n \frac{Y_{i1}+Y_{i2}}{2n}
\end{equation*}$$

In de onderstelling dat de $n$ planten onafhankelijk van elkaar gekozen werden en de eerste en tweede metingen even variabel zijn (d.w.z. $\text{Var}(Y_{i1})=\text{Var}(Y_{i2})=\sigma^2$), bedraagt de variantie op dit steekproefgemiddelde

$$\begin{eqnarray*}
\text{Var}(\bar Y)&=&\sum_{i=1}^n \frac{\text{Var}(Y_{i1}+Y_{i2})}{4n^2} \\
&=&\sum_{i=1}^n \frac{\sigma^2+\sigma^2+2\text{Cor}(Y_{i1},Y_{i2})\sigma^2}{%
4n^2} \\
&=&\frac{\sigma^2}{2n}\{1+\text{Cor}(Y_{1},Y_{2})\}
\end{eqnarray*}$$

Vermits verschillende metingen afkomstig van eenzelfde plant doorgaans positief met elkaar gecorreleerd zijn, is de standard error op $\bar Y$ dus groter dan wanneer de $2n$ metingen van $2n$ verschillende, onafhankelijke planten afkomstig zouden zijn. Dat is omdat, gegeven de eerste meting $Y_{i1}$, de tweede meting $Y_{i2}$ geen volledig nieuwe informatie toevoegt en er bijgevolg minder informatie beschikbaar is om het gemiddelde te schatten dan wanneer alle gegevens van verschillende planten afkomstig waren. In het bijzonder, wanneer $\text{Cor}(Y_{1},Y_{2})=1$, dan levert de tweede meting geen nieuwe informatie en bekomt men eenzelfde nauwkeurigheid als wanneer men slechts 1 meting per plant had bekomen. Wanneer $\text{Cor}(Y_{1},Y_{2})=0$, dan levert de tweede meting volledig nieuwe informatie en bekomt men eenzelfde nauwkeurigheid als wanneer men 1 meting had bekomen voor $2n$ i.p.v. $n$ verschillende planten. Vermits $$\frac{\sigma^2}{2n}\{1+\text{Cor}(Y_{1},Y_{2})\}\geq \frac{\sigma^2}{2n}$$

*Wanneer de correlatie tussen herhaalde genexpressie metingen positief is (hetgeen we verwachten), zal men in de praktijk meer preciese resultaten bekomen door 1 meting te bepalen voor $2n$ verschillende planten dan door 2 metingen te bepalen voor $n$ verschillende planten.*

De metingen in de captopril voorbeeld zijn eveneens geclusterd. We hebben immers twee systolische bloeddrukmetingen per patiënt. 1 meting voor en 1 meting na het toedienen van captopril. We beogen om de gemiddelde bloeddrukverandering $\mu$ te schatten a.d.h.v. de gegevens $$(Y_{i1} , Y_{i2}),$$ voor subjecten $i = 1, ..., n$. En we bekomen de volgende schatting: $$\bar X = \sum_{i=1}^n \frac{Y_{i2}-Y_{i1}}{n}$$

Uit de rekenregels voor de variantie weten we dat

$$\begin{eqnarray*}
\text{Var}\left[\bar X\right]&=&\sum_{i=1}^n \frac{\text{Var}\left[Y_{i1}-Y_{i2}\right]}{n^2}\\
&=&\sum_{i=1}^n \frac{\sigma^2_1+\sigma^2_2-2\text{Cor}\left[Y_{i1},Y_{i2}\right]\sigma_1\sigma_2}{n^2}\\
&=&\frac{\sigma^2_1+\sigma^2_2-2\text{Cor}\left[Y_{i1},Y_{i2}\right]\sigma_1\sigma_2}{n},\\
\end{eqnarray*}$$

In R kunnen we dit als volgt berekenen:

<span style="color: 0.56,0.35,0.01">*\# functie var op een matrix berekent varianties*</span> <span style="color: 0.56,0.35,0.01">*\# sigma\_1^2, sigma\_2^2 covariantie sigma\_{12}*</span> vars =<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**var**</span>(captopril$$, <span style="color: 0.13,0.29,0.53">**c**</span>(<span style="color: 0.31,0.60,0.02">"SBPb"</span>, <span style="color: 0.31,0.60,0.02">"SBPa"</span>)$$) vars

    ##          SBPb     SBPa
    ## SBPb 422.9238 370.7857
    ## SBPa 370.7857 400.1429

    ## [1] 0.9013312

varXbarDelta =<span style="color: 0.31,0.60,0.02"> </span>(vars$$<span style="color: 0.00,0.00,0.81">1</span>, <span style="color: 0.00,0.00,0.81">1</span>$$ <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span>vars$$<span style="color: 0.00,0.00,0.81">2</span>, <span style="color: 0.00,0.00,0.81">2</span>$$ <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">2</span> <span style="color: 0.81,0.36,0.00">**\***</span><span style="color: 0.31,0.60,0.02"> </span>vars$$<span style="color: 0.00,0.00,0.81">1</span>, <span style="color: 0.00,0.00,0.81">2</span>$$)<span style="color: 0.81,0.36,0.00">**/**</span><span style="color: 0.00,0.00,0.81">15</span> <span style="color: 0.13,0.29,0.53">**sqrt**</span>(varXbarDelta)

    ## [1] 2.330883

We zien dat de metingen heel sterk gecorreleerd zijn, waardoor de variantie op het verschil veel lager zal liggen dan op de originele metingen.

Gezien we voor elke patiënt twee metingen hebben bestaat een alternatieve methode om de standard error te bepalen erin om alle gecorreleerde metingen tot 1 meting te reduceren. Merk op dat we dit enkel kunnen doen voor gepaarde metingen. Alle resulterende metingen zijn dan onafhankelijk. Concreet kunnen we voor elke patiënt $i$ in de steekproef het bloeddrukverschil berekenen: $$X_{i}=Y_{ai}-Y_{bi}$$ en vervolgens standard error op $\bar X$. In het captopril voorbeeld wordt de schatting

<span style="color: 0.13,0.29,0.53">**sd**</span>(delta)<span style="color: 0.81,0.36,0.00">**/**</span><span style="color: 0.13,0.29,0.53">**sqrt**</span>(<span style="color: 0.00,0.00,0.81">15</span>)

    ## [1] 2.330883

We zien dat we exact dezelfde schatting voor de standard error bekomen. Verder zien we ook dat het design een groot voordeel heeft: Aangezien de bloeddrukmetingen voor en na het toedienen van captopril sterk positief gecorreleerd zijn is de variantie van het verschil veel lager dan deze op de originele bloeddrukmetingen. Iedere patiënt in de studie dient immers als zijn eigen controle en op die manier kunnen we de variabiliteit in de bloeddrukmetingen tussen patiënten uit de analyse verwijderen!

#### Normaal verdeelde gegevens {#normaal-verdeelde-gegevens}

Als de gegevens Normaal verdeeld zijn, dan zijn er meerdere onvertekende schatters voor het populatiegemiddelde $\mu$, bvb. het steekproefgemiddelde en de mediaan. Men kan echter aantonen dat in dat geval het steekproefgemiddelde $\bar{X}$ de onvertekende schatter is voor $\mu$ met de kleinste standard error. Dat betekent dat ze gemiddeld minder afwijkt van de echte parameterwaarde dan de mediaan, die veel meer varieert van steekproef tot steekproef. Het steekproefgemiddelde is bijgevolg een schatter die accuraat is (want onvertekend) en meest precies (kleinste standaarddeviatie).

### Verdeling van het steekproefgemiddelde {#subsec:verdelingXbar}

Om ondermeer goed de betekenis van de standard error te kunnen vatten, moeten we van $\bar X$ niet alleen het gemiddelde en de standaarddeviatie, maar ook de exacte verdeling kennen. De standard error is immers een standaardeviatie (bvb. van het steekproefgemiddelde), waarvan de betekenis het meest duidelijk is wanneer de metingen (in dit geval, het steekproefgemiddelde) Normaal verdeeld zijn. In het bijzonder geval dat de individuele observaties $X_i$ een Normale verdeling hebben met gemiddelde $\mu$ en variantie $\sigma^2$, kan men aantonen dat ook $\bar X$ Normaal verdeeld is met gemiddelde $\mu$ en variantie $\sigma^2/n.$ Dit fenomeen wordt geïllustreerd in Figuur <a href="#fig:meansim" data-reference-type="ref" data-reference="fig:meansim">5.7</a>. De linkse figuur illustreert een lukrake trekking of steekproef van observaties uit een Normale verdeling. Als men dit blijft herhalen en voor alle bekomen steekproeven het steekproefgemiddelde berekent en en vervolgens deze gemiddeldes uitzet in een histogram, dan krijgt men het histogram uit rechtse figuur. De steekproefgemiddeldes in deze figuur lijken inderdaad een Normale verdeling te volgen.

<figure id="fig:meansim">
<img src="Statistiek_2019_2020_files/figure-latex/meansim-1" style="width:100.0%" />
<figcaption>Simulaties van steekproeven met n=15 observaties uit een normale verdeling met gemiddelde systolische bloeddrukdaling 19 mmHg en standaard deviate van 9 mmHg. (links één steekproef, rechts een histogram van steekproefgemiddelden voor 1000 steekproeven. Het gemiddelde in de populatie is weergegeven d.m.v. rode lijn).</figcaption>
</figure>

In het captopril voorbeeld zagen we dat de systolische bloeddrukverandering approximatief normaal verdeeld is. De standard error op de bloeddrukverandering bedroeg 2.32 mm Hg. Dus op 100 studies met n = 15 subjecten, verwachten we dat de geschatte gemiddelde systolische bloeddrukafwijking ($\bar X$) op minder dan 2 × 2.32 = 4.64mm Hg van het werkelijke populatiegemiddelde ($\mu$) ligt in 95 studies.

In het algemeen, wanneer de individuele observaties $X_i$ geen Normale verdeling hebben, is $\bar X$ *bij benadering* toch nog Normaal verdeeld zodra het aantal observaties groot genoeg is. Hoe groot de steekproef hiervoor moet zijn, hangt hierbij af van hoe scheef de verdeling van de oorspronkelijke observaties is. Dat is het gevolg van de volgende fundamentele en veel toegepaste wiskundestelling.

**De Centrale Limietstelling (CLT)**

Stel dat $X_1, X_2, \dots, X_n, \; n$ onafhankelijke lukrake trekkingen van de toevalsveranderlijke $X$ voorstellen, met allen dezelfde theoretische verdeling. Laat $X$ gemiddelde $\mu$ en variantie $\sigma^2$ hebben maar verder een ongespecifieerde verdeling, dan wordt de verdeling van het steekproefgemiddelde $\bar{X}_n = {\sum_{i=1}^{n} X_i}/{n}$ naarmate $n$ groter wordt steeds beter benaderd door de Normale verdeling met gemiddelde $\mu$ en variantie $\sigma^2/n.$

**Einde Stelling**

Deze belangrijke eigenschap zal ons toelaten om de meeste technieken die in deze cursus aan bod komen toe te passen op een zeer uitgebreid spectrum van experimenten.

We illustreren deze stelling in Figuur <a href="#fig:CLT" data-reference-type="ref" data-reference="fig:CLT">5.8</a>. We simuleren data uit een experiment waarbij we een munt opwerpen. De data zijn dan Bernouilli verdeeld en kunnen de waarde $X=0$ (munt) of $X=1$ (kop) aannemen met een kans van 50% en zijn duidelijk niet-Normaal verdeeld. We simuleren steekproeven met een steekproefgrootte van 10 observaties en 100 observaties en onderzoeken de verdeling van het steekproefgemiddelde voor elke steekproefgrootte. We zien duidelijk dat CLT niet van toepassing is bij een steekproefgrootte van 10. Voor steekproeven met 100 observaties zien we dat de verdeling van het steekproefgemiddelde al beter benaderd kan worden door een Normale verdeling.

<figure id="fig:CLT">
<img src="Statistiek_2019_2020_files/figure-latex/CLT-1" style="width:100.0%" />
<figcaption>Illustratie van de Centrale Limietstelling d.m.v. Bernouilli verdeelde gegevens (opwerpen van een muntstuk) Steekproefgroottes (n=10, links, en n=100, rechts). Densiteit van de normale verdeling worden weergegeven in rood. We zien duidelijk dat CLT niet van toepassing is bij een steekproefgrootte van 10. Voor steekproeven met 100 observaties zien we dat de verdeling van het steekproefgemiddelde al beter benaderd kan worden door een Normale verdeling.</figcaption>
</figure>

## Intervalschatters {#intervalschatters}

In de vorige sectie hebben we vastgesteld dat het steekproefgemiddelde van steekproef tot steekproef varieert rond het populatiegemiddelde dat we willen schatten. Om die reden wensen we in deze sectie een interval rond het steekproefgemiddelde te bepalen waarbinnen we het populatiegemiddelde met gegeven kans (bvb. 95% kans) kunnen verwachten. In Sectie <a href="#subsec:bigek" data-reference-type="ref" data-reference="subsec:bigek">5.4.1</a> zullen we dit uitwerken voor het geval waar de populatievariantie $\sigma^2$ op de metingen gekend is. Deze onderstelling is meestal onredelijk[^28], maar wordt hier gemaakt om redenen van eenvoud. In Sectie <a href="#sec:tBI" data-reference-type="ref" data-reference="sec:tBI">5.4.2</a> zullen we van deze onderstelling afstappen.

### Gekende variantie op de metingen {#subsec:bigek}

Wanneer de individuele observaties $X$ Normaal verdeeld zijn met gemiddelde $\mu$ en gekende variantie $\sigma^2$, noteren we dat als volgt: $X\sim N(\mu,\sigma^2)$. Uit vorige sectie volgt dan dat het steekproefgemiddelde $\bar{X}$ eveneens Normaal verdeeld is volgens $N(\mu,\sigma^2/n)$. Een 95% referentie-interval voor het steekproefgemiddelde ziet er bijgevolg uit als

$$\begin{equation*}
\left[\mu - 1.96 \frac{\sigma}{\sqrt{n}},\mu + 1.96 \frac{\sigma}{\sqrt{n}}%
\right]
\end{equation*}$$

Het bevat met 95% kans het steekproefgemiddelde van een lukrake steekproef. Dit interval kunnen we niet expliciet berekenen op basis van de geobserveerde gegevens, omdat $\mu$ ongekend is (we gaan er hier voorlopig van uit dat $\sigma$ wel gekend is). Het kan wel geschat worden als

$$\begin{equation*}
\left[\bar X - 1.96 \frac{\sigma}{\sqrt{n}},\bar X + 1.96 \frac{\sigma}{\sqrt{n}}\right]
\end{equation*}$$

Hoewel dit laatste interval nog steeds kan geïnterpreteerd worden als een referentie-interval voor het steekproefgemiddelde, kunnen we er een veel nuttigere interpretatie aan geven. Immers, de ongelijkheid $\mu - 1.96 \
\sigma/\sqrt{n} < \bar{X}$ kan equivalent worden herschreven als $\mu < \bar{X} + 1.96 \ \sigma/\sqrt{n}$. Hieruit volgt:

$$\begin{eqnarray*}
95\% &=& P( \mu - 1.96 \ \sigma/\sqrt{n} < \bar{X} < \mu + 1.96 \ \sigma/\sqrt{n} ) \\
&=&P( \bar{X} - 1.96 \ \sigma/\sqrt{n} < \mu < \bar{X} + 1.96 \ \sigma/\sqrt{n} )
\end{eqnarray*}$$

Dit leidt tot volgende definitie.

**Definitie 5.3** (95$\%$ betrouwbaarheidsinterval voor populatiegemiddelde). <span id="def:unnamed-chunk-71"></span><span id="def:unnamed-chunk-71" label="def:unnamed-chunk-71"></span> Het interval

$$\begin{equation}
[\bar{X} - 1.96 \ \sigma/\sqrt{n} , \bar{X} + 1.96 \ \sigma/\sqrt{n} ], \label{eq:bi}
\end{equation}$$

bevat met 95% kans het populatiegemiddelde $\mu$. Het wordt een **95% betrouwbaarheidsinterval** (in het Engels: *95% confidence interval*) voor het populatiegemiddelde $\mu$ genoemd. De kans dat het de populatieparameter $\mu$ bevat, d.i. 95%, wordt het *betrouwbaarheidsniveau* genoemd.

**Einde definitie**

Een 95% betrouwbaarheidsinterval bepaalt met andere woorden een reeks waarden waarbinnen de gezochte populatieparameter *waarschijnlijk* (namelijk met 95% kans) valt.

Stel dat we in een steekproef een bloeddrukdaling van -18.93mmHg observeren en dat we weten dat de standaarddeviatie van de bloeddrukmetingen 9mmHg bedraagt. Dan vinden we een betrouwbaarheidsinterval voor de gemiddelde bloeddrukdaling van $\left[-18.93-1.96\times 9/\sqrt{15},-18.9+1.95\times 9/\sqrt{15}\right]=$$$-23.48,-14.38$$mmHg.

De reden waarom over “95% kans” gesproken wordt, is omdat de eindpunten van het 95% betrouwbaarheidsinterval toevalsveranderlijken zijn die variëren van steekproef tot steekproef. Met andere woorden, verschillende steekproeven leveren telkens andere betrouwbaarheidsintervallen op, vermits die intervallen berekend zijn op basis van de gegevens in de steekproef. Men noemt het om die reden *stochastische intervallen*. Voor 95% van alle steekproeven zal het berekende 95% betrouwbaarheidsinterval de gezochte waarde van de populatieparameter bevatten, en voor de overige 5% niet. Dat wordt geïllustreerd a.d.h.v. een simulatiestudie in Sectie <a href="#subsec:interpretBI" data-reference-type="ref" data-reference="subsec:interpretBI">5.4.3</a> (nadat we de intervallen hebben uitgebreid voor de meer realistische setting waarbij de variantie in de populatie ongekend is).

Uiteraard kunnen de onderzoekers o.b.v. een gegeven betrouwbaarheidsinterval niet besluiten of het de gezochte parameterwaarde bevat of niet, vermits ze precies op zoek zijn naar die onbekende waarde. Maar ze gebruiken een procedure die in 95% van de gevallen werkt; m.a.w. die in 95% van de gevallen de gezochte waarde bevat. Of nog, als men dagelijks gegevens zou verzamelen en telkens een 95% betrouwbaarheidsinterval zou berekenen voor een nieuwe parameter $\theta$ (bvb. een odds ratio), dan zou men op lange termijn in 95% van de gevallen de gezochte waarde omvat hebben.

Tot nog toe zijn we ervan uitgegaan dat de individuele observaties Normaal verdeeld zijn en dat hun variantie gekend is (want als de variantie $\sigma^2$ niet gekend is, kan men de grenzen van het interval niet berekenen). Wegens de Centrale Limietstelling bevat Vergelijking <a href="#eq:bi" data-reference-type="eqref" data-reference="eq:bi">[eq:bi]</a> het gemiddelde $\mu$ bij benadering met 95% kans wanneer de steekproef groot is en de variantie van de individuele observaties gekend, maar hun verdeling ongekend is.

Wanneer bovendien de variantie ongekend is, kan me ze schatten door gebruik te maken van de steekproefvariantie $S^2$ van de reeks observaties $X_1,...,X_n$. Men kan aantonen dat het interval $[\bar{X} - 1.96 \ s/\sqrt{n} , \bar{X} + 1.96 \ s/\sqrt{n} ]$ dan het populatiegemiddelde met bij benadering 95% kans bevat, op voorwaarde dat de steekproef groot is. In de volgende sectie gaan we na hoe een betrouwbaarheidsinterval voor het populatiegemiddelde geconstrueerd kan worden wanneer de variantie ongekend is en de steekproef relatief klein.

Om een betrouwbaarheidsinterval met een ander betrouwbaarheidsniveau, $(1- \alpha)100\%$ te construeren, vervangt men 1.96 door het relevante kwantiel $z_{\alpha/2}.$

De breedte van een $100\%(1-\alpha)$ betrouwbaarheidsinterval voor een populatiegemiddelde $\mu$ is $2 z_{\alpha/2} \ \sigma/\sqrt{n}$. Ze wordt dus bepaald door 3 factoren: de standaarddeviatie op de individuele observaties, $\sigma$, de grootte van de steekproef, $n$, en het betrouwbaarheidsniveau, $1-\alpha$:

- $n$: naarmate de steekproefgrootte toeneemt, krimpt het betrouwbaarheidsinterval. In grote steekproeven beschikken we immers over veel informatie en kunnen we de gezochte populatieparameter bijgevolg relatief nauwkeurig afschatten.

- $\sigma$: naarmate de standaarddeviatie van de oorspronkelijke observaties toeneemt, neemt de lengte van het betrouwbaarheidsinterval toe. Indien er immers veel ruis op de gegevens zit, dan is het moeilijker om populatieparameters of -kenmerken te identificeren.

- $1-\alpha$: naarmate het betrouwbaarheidsniveau toeneemt, wordt het betrouwbaarheidsinterval breder. Indien we immers eisen dat het interval met 99.9% kans de populatiewaarde bevat i.p.v. met 80% kans, dan zullen we duidelijk een breder interval nodig hebben.

Betrouwbaarheidsintervallen worden niet enkel gebruikt voor het populatiegemiddelde, maar kunnen in principe voor om het even welke populatieparameter worden gedefinieerd. Zo kunnen ze bijvoorbeeld gedefinieerd worden voor een verschil tussen 2 gemiddelden, voor een odds ratio, voor een variantie, … De manier om die intervallen te berekenen is vaak complex en sterk afhankelijk van de gebruikte schatter voor de populatieparameter. Er wordt daarom niet van u verwacht dat u voor alle populatieparameters die we in deze cursus ontmoeten, een betrouwbaarheidsinterval kunt berekenen, maar wel dat u het kunt interpreteren.

**Definitie 5.4** (Betrouwbaarheidsinterval). <span id="def:unnamed-chunk-72"></span><span id="def:unnamed-chunk-72" label="def:unnamed-chunk-72"></span> Een **$(1-\alpha)100$% betrouwbaarheidsinterval** voor een populatieparameter $\theta$ is een geschat (en bijgevolg stochastisch) interval dat met $(1-\alpha)100$% kans de echte waarde van die populatieparameter $\theta$ bevat.

**Einde Definitie**

### Ongekende variantie op de metingen {#sec:tBI}

Tot nog toe werd verondersteld dat de populatievariantie $\sigma^2$ gekend is bij het berekenen van een betrouwbaarheidsinterval voor $\mu$. Betrouwbaarheidsintervallen voor $\mu$ werden dan opgebouwd door op te merken dat de gestandaardiseerde waarde $(\bar{X} - \mu)/(\sigma/\sqrt{n})$ standaardnormaal verdeeld is en bijgevolg

$$\begin{equation*}
\left[\mu - 1.96 \frac{\sigma}{\sqrt{n}},\mu + 1.96 \frac{\sigma}{\sqrt{n}}%
\right]
\end{equation*}$$

een 95% referentie-interval voor het steekproefgemiddelde voorstelt.

In de praktijk komt het quasi nooit voor dat men de populatievariantie $\sigma^2$ exact kent. In de praktijk wordt deze geschat als $S^2$ op basis van de voorhanden zijnde steekproef. Als gevolg hiervan zullen de betrouwbaarheidsintervallen uit voorgaande sectie doorgaans iets te smal zijn (omdat ze er geen rekening mee houden dat ook de variantie werd geschat) en is het noodzakelijk om bij de berekening $(\bar{X} - \mu)/(S/\sqrt{n})$ te gebruiken als gestandaardiseerde waarde i.p.v. $(\bar{X} - \mu)/(\sigma/\sqrt{n})$. Wanneer de steekproef voldoende groot is, ligt de vierkantswortel van variantie $S^2$ voldoende dicht bij $\sigma$ zodat ${(\bar{X} - \mu)}/{(S/\sqrt{n}) }$ bij benadering een standaardnormale verdeling volgt en, bijgevolg,

$$\begin{equation*}
\left[\bar{X} - z_{\alpha/2} \ \frac{S}{\sqrt{n}} , \bar{X} + z_{\alpha/2} \
\frac{S}{\sqrt{n}}\right]
\end{equation*}$$

een benaderd $(1- \alpha)100\%$ betrouwbaarheidsinterval is voor $\mu$. Voor kleine steekproeven is dit niet langer het geval. Daardoor introduceert men een extra onnauwkeurigheid in de gestandaardiseerde waarde ${(\bar{X} - \mu)}/{(S/\sqrt{n})}$. Deze is nog wel gecentreerd rond nul en symmetrisch, maar niet langer Normaal verdeeld. De echte verdeling voor eindige steekproefgrootte $n$ heeft zwaardere staarten dan de Normale. Hoeveel zwaarder de staarten zijn, hangt van de steekproefgrootte $n$ af. Als $n$ oneindig groot wordt, komt $S$ zodanig dicht bij $\sigma$ te liggen dat de extra onnauwkeurigheid in de gestandaardiseerde waarde verwaarloosbaar is en bijgevolg ook het verschil met de Normale verdeling. Maar voor relatief kleine steekproeven hangt de verdeling van ${(\bar{X} - \mu)}/({S/\sqrt{n}})$ af van de grootte $n$ van de steekproef. Ze krijgt de naam (Student) $t$-verdeling met $n-1$ vrijheidsgraden (in het Engels: *degrees of freedom*). Deze verdeling wordt voor een aantal verschillende vrijheidsgraden geïllustreerd in Figuur <a href="#fig:tdist" data-reference-type="ref" data-reference="fig:tdist">5.9</a>. De t-verdelingen in de figuur hebben duidelijk bredere staarten dan de normaalverdeling, waardoor ze ook een grotere percentielwaarden hebben voor een vooropgesteld betrouwbaarheidsniveau. Dat zal leiden tot bredere intervallen, wat logisch is aangezien we de extra onzekerheid inbouwen die gerelateerd is aan het schatten van de standaarddeviatie.

**Definitie 5.5** (t-verdeling). <span id="def:unnamed-chunk-73"></span><span id="def:unnamed-chunk-73" label="def:unnamed-chunk-73"></span> Als $X_1, X_2, ..., X_n$ een steekproef vormen uit de Normale verdeling $N(\mu, \sigma^2)$, dan is $(\bar{X} - \mu)/(S/\sqrt{n})$ verdeeld als een $t$-verdeling met $n-1$ vrijheidsgraden.

\*\*Einde Definitie

grid =<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**seq**</span>(<span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.00,0.00,0.81">5</span>, <span style="color: 0.00,0.00,0.81">5</span>, <span style="color: 0.00,0.00,0.81">0.1</span>) <span style="color: 0.13,0.29,0.53">**plot**</span>(grid, <span style="color: 0.13,0.29,0.53">**dnorm**</span>(grid), <span style="color: 0.13,0.29,0.53">ylab =</span> <span style="color: 0.31,0.60,0.02">"densiteit"</span>, <span style="color: 0.13,0.29,0.53">xlab =</span> <span style="color: 0.31,0.60,0.02">"X"</span>, <span style="color: 0.13,0.29,0.53">type =</span> <span style="color: 0.31,0.60,0.02">"l"</span>, <span style="color: 0.13,0.29,0.53">lwd =</span> <span style="color: 0.00,0.00,0.81">2</span>) dfs =<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**c**</span>(<span style="color: 0.00,0.00,0.81">2</span>, <span style="color: 0.00,0.00,0.81">5</span>, <span style="color: 0.00,0.00,0.81">14</span>) <span style="color: 0.13,0.29,0.53">**for**</span> (i <span style="color: 0.13,0.29,0.53">**in**</span> <span style="color: 0.00,0.00,0.81">1</span><span style="color: 0.81,0.36,0.00">**:**</span><span style="color: 0.13,0.29,0.53">**length**</span>(dfs)) <span style="color: 0.13,0.29,0.53">**lines**</span>(grid, <span style="color: 0.13,0.29,0.53">**dt**</span>(grid, dfs$$i$$), <span style="color: 0.13,0.29,0.53">col =</span> i <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">1</span>, <span style="color: 0.13,0.29,0.53">lwd =</span> <span style="color: 0.00,0.00,0.81">2</span>) <span style="color: 0.13,0.29,0.53">**legend**</span>(<span style="color: 0.31,0.60,0.02">"topright"</span>, <span style="color: 0.13,0.29,0.53">lty =</span> <span style="color: 0.00,0.00,0.81">1</span>, <span style="color: 0.13,0.29,0.53">col =</span> <span style="color: 0.00,0.00,0.81">1</span><span style="color: 0.81,0.36,0.00">**:**</span><span style="color: 0.00,0.00,0.81">4</span>, <span style="color: 0.13,0.29,0.53">legend =</span> <span style="color: 0.13,0.29,0.53">**c**</span>(<span style="color: 0.31,0.60,0.02">"N(X,mean=0,sd=1)"</span>, <span style="color: 0.13,0.29,0.53">**paste0**</span>(<span style="color: 0.31,0.60,0.02">"t(X,df="</span>, dfs, <span style="color: 0.31,0.60,0.02">")"</span>)))

<figure id="fig:tdist">
<img src="Statistiek_2019_2020_files/figure-latex/tdist-1" style="width:100.0%" />
<figcaption>Normale verdeling en t-verdeling met verschillende vrijheidsgraden.</figcaption>
</figure>

Percentielen van de $t$-verdeling kunnen niet met de hand berekend worden, maar kan men voor de verschillende waarden van $n$ aflezen in Tabellen of berekenen in R. In de onderstaande code wordt het 95%, 97.5%, 99.5% percentiel berekend voor een t-verdeling met 14 vrijheidsgraden, die gebruik kunnen worden voor de berekening van 90%, 95% en 99% betrouwbaarheidsintervallen.

<span style="color: 0.13,0.29,0.53">**qt**</span>(<span style="color: 0.00,0.00,0.81">0.975</span>, <span style="color: 0.13,0.29,0.53">df =</span> <span style="color: 0.00,0.00,0.81">14</span>)

    ## [1] 2.144787

<span style="color: 0.13,0.29,0.53">**qt**</span>(<span style="color: 0.13,0.29,0.53">**c**</span>(<span style="color: 0.00,0.00,0.81">0.95</span>, <span style="color: 0.00,0.00,0.81">0.975</span>, <span style="color: 0.00,0.00,0.81">0.995</span>), <span style="color: 0.13,0.29,0.53">df =</span> <span style="color: 0.00,0.00,0.81">14</span>)

    ## [1] 1.761310 2.144787 2.976843

We zien dat het 97.5% percentiel 2.14 voor een t-verdeling met $n-1=14$ vrijheidsgraden inderdaad groter is dan het kwantiel uit de normaal verdeling 1.96.

Een gelijkaardige logica als voor de Normale verdeling met gekende variantie, geeft dan aan dat een $100\% (1-\alpha)$ betrouwbaarheidsinterval voor het gemiddelde $\mu$ van een Normaal verdeelde veranderlijke $X$ met onbekende variantie kan berekend worden als

$$\begin{equation*}
\left[\bar{X} - t_{n-1, \alpha/2} \frac{s}{\sqrt{n}} , \bar{X} + t_{n-1,
\alpha/2} \frac{s}{\sqrt{n}}\right]
\end{equation*}$$

Deze uitdrukking verschilt van deze in de vorige sectie doordat het $(1-\alpha/2)100\%$ percentiel van de Normale verdeling wordt vervangen door het $(1-\alpha/2)100\%$ percentiel van de t-verdeling met $n-1$ vrijheidsgraden.

Voor het captopril voorbeeld kunnen we dus een 95% betrouwbaarheidsinterval bekomen door

<span style="color: 0.13,0.29,0.53">**mean**</span>(delta) <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**qt**</span>(<span style="color: 0.00,0.00,0.81">0.975</span>, <span style="color: 0.13,0.29,0.53">df =</span> <span style="color: 0.00,0.00,0.81">14</span>) <span style="color: 0.81,0.36,0.00">**\***</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**sd**</span>(delta)<span style="color: 0.81,0.36,0.00">**/**</span><span style="color: 0.13,0.29,0.53">**sqrt**</span>(n)

    ## [1] -23.93258

<span style="color: 0.13,0.29,0.53">**mean**</span>(delta) <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**qt**</span>(<span style="color: 0.00,0.00,0.81">0.975</span>, <span style="color: 0.13,0.29,0.53">df =</span> <span style="color: 0.00,0.00,0.81">14</span>) <span style="color: 0.81,0.36,0.00">**\***</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**sd**</span>(delta)<span style="color: 0.81,0.36,0.00">**/**</span><span style="color: 0.13,0.29,0.53">**sqrt**</span>(n)

    ## [1] -13.93409

Een 99% betrouwbaarheidsinterval voor gemiddelde bloeddrukverandering wordt als volgt bekomen:

<span style="color: 0.13,0.29,0.53">**mean**</span>(delta) <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**qt**</span>(<span style="color: 0.00,0.00,0.81">0.995</span>, <span style="color: 0.13,0.29,0.53">df =</span> <span style="color: 0.00,0.00,0.81">14</span>) <span style="color: 0.81,0.36,0.00">**\***</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**sd**</span>(delta)<span style="color: 0.81,0.36,0.00">**/**</span><span style="color: 0.13,0.29,0.53">**sqrt**</span>(n)

    ## [1] -25.87201

<span style="color: 0.13,0.29,0.53">**mean**</span>(delta) <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**qt**</span>(<span style="color: 0.00,0.00,0.81">0.995</span>, <span style="color: 0.13,0.29,0.53">df =</span> <span style="color: 0.00,0.00,0.81">14</span>) <span style="color: 0.81,0.36,0.00">**\***</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**sd**</span>(delta)<span style="color: 0.81,0.36,0.00">**/**</span><span style="color: 0.13,0.29,0.53">**sqrt**</span>(n)

    ## [1] -11.99466

### Interpretatie van betrouwbaarheidsintervallen {#subsec:interpretBI}

We zullen de interpretatie van betrouwbaarheidsintervallen weergegeven a.d.h.v. een simulatie studie waarbij we 1000 herhaalde steekproeven simuleren met 15 observaties uit een normaal verdeling. De gemiddelde bloeddrukdaling in de populatie bedraagt -18.9 mmHg en de standaarddeviate 9.0 mmHg. We houden voor elke steekproef volgende gegevens bij: het gemiddelde, de ondergrens en bovengrens van het BI en of het BI het werkelijke gemiddelde.

<span style="color: 0.13,0.29,0.53">**set.seed**</span>(<span style="color: 0.00,0.00,0.81">115</span>) mu &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.00,0.00,0.81">18.9</span> sigma &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">9</span> nSim &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">1000</span> alpha &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">0.05</span> n &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">15</span> muHat &lt;-<span style="color: 0.31,0.60,0.02"> </span>sigmaHat &lt;-<span style="color: 0.31,0.60,0.02"> </span>BI.ondergrens &lt;-<span style="color: 0.31,0.60,0.02"> </span>BI.bovengrens &lt;-<span style="color: 0.31,0.60,0.02"> </span>omvat &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**array**</span>(<span style="color: 0.13,0.29,0.53">dim =</span> nSim) cnt &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">0</span> <span style="color: 0.13,0.29,0.53">**for**</span> (i <span style="color: 0.13,0.29,0.53">**in**</span> <span style="color: 0.00,0.00,0.81">1</span><span style="color: 0.81,0.36,0.00">**:**</span>nSim) { y &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**rnorm**</span>(n, <span style="color: 0.13,0.29,0.53">mean =</span> mu, <span style="color: 0.13,0.29,0.53">sd =</span> sigma) muHat$$i$$ &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**mean**</span>(y) sigmaHat$$i$$ &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**sd**</span>(y)<span style="color: 0.81,0.36,0.00">**/**</span><span style="color: 0.13,0.29,0.53">**sqrt**</span>(n) BI.ondergrens$$i$$ &lt;-<span style="color: 0.31,0.60,0.02"> </span>muHat$$i$$ <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**qt**</span>(<span style="color: 0.00,0.00,0.81">1</span> <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span>alpha<span style="color: 0.81,0.36,0.00">**/**</span><span style="color: 0.00,0.00,0.81">2</span>, <span style="color: 0.13,0.29,0.53">df =</span> n <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">1</span>) <span style="color: 0.81,0.36,0.00">**\***</span><span style="color: 0.31,0.60,0.02"> </span>sigmaHat$$i$$ BI.bovengrens$$i$$ &lt;-<span style="color: 0.31,0.60,0.02"> </span>muHat$$i$$ <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**qt**</span>(<span style="color: 0.00,0.00,0.81">1</span> <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span>alpha<span style="color: 0.81,0.36,0.00">**/**</span><span style="color: 0.00,0.00,0.81">2</span>, <span style="color: 0.13,0.29,0.53">df =</span> n <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">1</span>) <span style="color: 0.81,0.36,0.00">**\***</span><span style="color: 0.31,0.60,0.02"> </span>sigmaHat$$i$$ omvat$$i$$ &lt;-<span style="color: 0.31,0.60,0.02"> </span>(mu <span style="color: 0.81,0.36,0.00">**&lt;**</span><span style="color: 0.31,0.60,0.02"> </span>BI.bovengrens$$i$$) <span style="color: 0.81,0.36,0.00">**&**</span><span style="color: 0.31,0.60,0.02"> </span>(BI.ondergrens$$i$$ <span style="color: 0.81,0.36,0.00">**&lt;**</span><span style="color: 0.31,0.60,0.02"> </span> <span style="color: 0.31,0.60,0.02"> </span>mu) cnt &lt;-<span style="color: 0.31,0.60,0.02"> </span>cnt <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**as.numeric**</span>(omvat$$i$$) } cnt<span style="color: 0.81,0.36,0.00">**/**</span>nSim

    ## [1] 0.951

Op basis van de 1000 herhaalde steekproeven van de simulatiestudie zien we dat voor 95.1% van de steekproeven de intervallen het werkelijke populatiegemiddelde bevat[^29]. De simulatiestudie toont dus op een empirische wijze aan dat de constructie correct is. Het demonstreert bovendien de interpretatie van probabiliteit via herhaalde steekproefname. In Figuur <a href="#fig:biInterpret" data-reference-type="ref" data-reference="fig:biInterpret">5.10</a> wordt de interpretatie ook grafisch weergegeven voor de eerste 100 gesimuleerde steekproeven. De figuur toont duidelijk aan dat het werkelijke populatiegemiddelde vast is maar ongekend. Het wordt geschat aan de hand van het steekproefgemiddelde dat at random varieert van steekproef tot steekproef rond het werkelijk gemiddelde. We zien ook dat de grenzen van de betrouwbaarheidsintervallen variëren van steekproef tot steekproef. Daarnaast varieert de breedte van de betrouwbaarheidsintervallen eveneens omdat de steekproefstandaarddeviatie eveneens varieert van steekproef tot steekproef[^30].

In de praktijk zullen we op basis van 1 steekproef besluiten dat het betrouwbaarheidsinterval het populatiegemiddelde bevat en we weten dat dergelijke uitspraken met een kans van $1-\alpha$ (hier 95%) correct zijn.

<figure id="fig:biInterpret">
<img src="Statistiek_2019_2020_files/figure-latex/biInterpret-1" style="width:100.0%" />
<figcaption>Interpretatie van 95<span class="math inline">%</span> betrouwbaarheidintervallen. Resultaten op basis van 100 gesimuleerde steekproeven. We zien in de figuur duidelijk dat het populatiegemiddelde vast is maar ongekend (blauwe lijn) en dat de bovengrens en ondergrens van betrouwbaarheidsintervallen voor het populatiegemiddelde varieert van steekproef tot steekproef. Van de 100 betrouwbaarheidsintervallen die worden geplot bevatten 95 intervallen het werkelijke steekproef gemiddelde (zwarte BIs). Voor 5 intervallen is dat niet het geval (rode BIs).</figcaption>
</figure>

We zullen nu de simulatie herhalen, maar zullen het aantal observaties in de steekproef verdubbelen.

mu &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.00,0.00,0.81">18.9</span> sigma &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">9</span> nSim &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">1000</span> alpha &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">0.05</span> n &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">30</span> muHat &lt;-<span style="color: 0.31,0.60,0.02"> </span>sigmaHat &lt;-<span style="color: 0.31,0.60,0.02"> </span>BI.ondergrens &lt;-<span style="color: 0.31,0.60,0.02"> </span>BI.bovengrens &lt;-<span style="color: 0.31,0.60,0.02"> </span>omvat &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**array**</span>(<span style="color: 0.13,0.29,0.53">dim =</span> nSim) cnt &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">0</span> <span style="color: 0.13,0.29,0.53">**for**</span> (i <span style="color: 0.13,0.29,0.53">**in**</span> <span style="color: 0.00,0.00,0.81">1</span><span style="color: 0.81,0.36,0.00">**:**</span>nSim) { y &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**rnorm**</span>(n, <span style="color: 0.13,0.29,0.53">mean =</span> mu, <span style="color: 0.13,0.29,0.53">sd =</span> sigma) muHat$$i$$ &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**mean**</span>(y) sigmaHat$$i$$ &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**sd**</span>(y)<span style="color: 0.81,0.36,0.00">**/**</span><span style="color: 0.13,0.29,0.53">**sqrt**</span>(n) BI.ondergrens$$i$$ &lt;-<span style="color: 0.31,0.60,0.02"> </span>muHat$$i$$ <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**qt**</span>(<span style="color: 0.00,0.00,0.81">1</span> <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span>alpha<span style="color: 0.81,0.36,0.00">**/**</span><span style="color: 0.00,0.00,0.81">2</span>, <span style="color: 0.13,0.29,0.53">df =</span> n <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">1</span>) <span style="color: 0.81,0.36,0.00">**\***</span><span style="color: 0.31,0.60,0.02"> </span>sigmaHat$$i$$ BI.bovengrens$$i$$ &lt;-<span style="color: 0.31,0.60,0.02"> </span>muHat$$i$$ <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**qt**</span>(<span style="color: 0.00,0.00,0.81">1</span> <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span>alpha<span style="color: 0.81,0.36,0.00">**/**</span><span style="color: 0.00,0.00,0.81">2</span>, <span style="color: 0.13,0.29,0.53">df =</span> n <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">1</span>) <span style="color: 0.81,0.36,0.00">**\***</span><span style="color: 0.31,0.60,0.02"> </span>sigmaHat$$i$$ omvat$$i$$ &lt;-<span style="color: 0.31,0.60,0.02"> </span>(mu <span style="color: 0.81,0.36,0.00">**&lt;**</span><span style="color: 0.31,0.60,0.02"> </span>BI.bovengrens$$i$$) <span style="color: 0.81,0.36,0.00">**&**</span><span style="color: 0.31,0.60,0.02"> </span>(BI.ondergrens$$i$$ <span style="color: 0.81,0.36,0.00">**&lt;**</span><span style="color: 0.31,0.60,0.02"> </span> <span style="color: 0.31,0.60,0.02"> </span>mu) cnt &lt;-<span style="color: 0.31,0.60,0.02"> </span>cnt <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**as.numeric**</span>(omvat$$i$$) } cnt<span style="color: 0.81,0.36,0.00">**/**</span>nSim

    ## [1] 0.949

We zien een coverage van 94.9% wat opnieuw dicht ligt bij de nominale coverage van 95%.

Wanneer we opnieuw de eerste 100 betrouwbaarheidsintervallen plotten (Figuur <a href="#fig:biInterpretLargeSample" data-reference-type="ref" data-reference="fig:biInterpretLargeSample">5.11</a>) merken we op dat de intervallen smaller zijn dan in Figuur <a href="#fig:biInterpret" data-reference-type="ref" data-reference="fig:biInterpret">5.10</a> (waarom is dat het geval, ga zelf na met welke factor de intervallen ongeveer versmallen?)

<figure id="fig:biInterpretLargeSample">
<img src="Statistiek_2019_2020_files/figure-latex/biInterpretLargeSample-1" style="width:100.0%" />
<figcaption>Interpretatie van 95<span class="math inline">%</span> betrouwbaarheidintervallen. Resultaten op basis van 100 gesimuleerde steekproeven. We zien in de figuur duidelijk dat het populatiegemiddelde vast is maar ongekend (blauwe lijn) en dat de bovengrens en ondergrens van betrouwbaarheidsintervallen voor het populatiegemiddelde varieert van steekproef tot steekproef. Van de 100 betrouwbaarheidsintervallen die worden geplot bevatten 95 intervallen het werkelijke steekproef gemiddelde (zwarte BIs). Voor 5 intervallen is dat niet het geval (rode BIs).</figcaption>
</figure>

### Wat rapporteren? {#wat-rapporteren}

Rapporteer dus zeker steeds de onzekerheid op de resultaten! Conclusies trekken op basis van 1 schatting kan zeer misleidend zijn! In statistische analyses rapporteert men daarom systematisch betrouwbaarheidsintervallen. Betrouwbaarheidsintervallen vormen een goed compromis: ze zijn smal genoeg om informatief te zijn, maar haast nooit zeer misleidend. We besluiten dat de parameter die ons interesseert in het 95% betrouwbaarheidsinterval zit, en weten dat die uitspraak met 95% kans correct is. In de statistiek trekt men dus nooit absolute conclusies.

Op basis van de data-analyse voor het captopril voorbeeld kunnen we dus besluiten dat de gemiddelde bloeddrukdaling 18.9mmHg bedraagt na het toedienen van captopril. Met een 95% betrouwbaarheidsinterval op het gemiddelde van $$-22.3,-15.6$$mmHg. Op basis van het betrouwbaarheidsinterval is het duidelijk dat het toedienen van captopril resulteert in een sterke bloeddrukdaling bij patiënten met hypertensie.

## Principe van Hypothesetoetsen (via one sample t-test) {#principe-van-hypothesetoetsen-via-one-sample-t-test}

We wensen een uitspraak te kunnen doen of er al dan niet een effect is van het toedienen van Captopril op de systolische bloeddruk? Beslissen op basis van gegevens is niet evident. Er is immers onzekerheid of de bevindingen uit de steekproef generaliseerbaar zijn naar de populatie. We stellen ons dus de vraag of het schijnbaar gunstig effect systematisch of toevallig is? Een natuurlijke beslissingsbasis is het gemiddeld verschil $X$ in de systolische bloeddruk:

$\bar x=$ -18.93mmHg ($s =$ 9.03, $SE =$ 2.33).

Dat $\bar{x}< 0$ volstaat niet om te beslissen dat de gemiddelde systolische bloeddruk lager is na het toedienen van captopril *op het niveau van de volledige populatie*. Om het effect die we in de steekproef observeren te kunnen *veralgemenen* naar de populatie moet de bloeddrukverlaging voldoende groot zijn. Maar hoe groot moet dit effect nu zijn?

Hiervoor hebben statistici zogenaamde *toetsen* ontwikkeld om met dit soort vragen om te gaan. Deze leveren een ja/nee antwoord op de vraag of een geobserveerde associatie systematisch is (d.w.z. opgaat voor de studiepopulatie) of als er integendeel onvoldoende informatie in de steekproef voorhanden is om te besluiten dat de geobserveerde associatie ook aanwezig is in de volledige studiepopulatie. Tegenwoordig is het haast onmogelijk om een wetenschappelijk onderzoeksartikel te lezen zonder de resultaten van dergelijke toetsen te ontmoeten. Om die reden wensen we in dit hoofdstuk in te gaan op de betekenis van statistische toetsen en hun nomenclatuur.

We weten dat we volgens het *falcificatieprincipe* van Popper nooit een hypothese kunnen bewijzen op basis van data (zie Sectie <a href="#sec:wetMeth" data-reference-type="ref" data-reference="sec:wetMeth">1.1</a>). Daarom zullen we twee hypotheses introduceren: een nulhypothese en een alternatieve hypothese. We zullen dan later a.d.h.v. de toets de nulhypothese trachten te ontkrachten.

### Hypotheses {#hypotheses}

Algemeen starten we met het vertalen van de wetenschappelijke vraagstelling naar een nulhypothese ($H_0$) en een alternatieve hypothese ($H_1$). Dit kan pas nadat de probleemstelling vertaald is naar een geparametriseerd statistisch model. Uit de beschrijving van de proefopzet volgt dat $X_1,...,X_n$ i.i.d.[^31] $f(X)$ met $f(X)$ de dichtheidsfunctie van de bloeddrukverschillen.

**Vereenvoudiging**: veronderstel dat $f(X)$ gekend is op een eindig-dimensionale set van parameters $\mathbf{\theta}$ na (parametrisch statistisch model). Voor het captopril voorbeeld veronderstellen we dat $f(X)$ een normale distributie $N(\mu,\sigma^2)$ volgt met parameters $\mathbf{\theta}=(\mu,\sigma^2)$, het gemiddelde $\mu$ en variantie $\sigma^2$.

De vraagstelling is geformuleerd in termen van de gemiddelde bloeddrukdaling: $\mu=E_f[X]$.

De **alternatieve hypothese** wordt geformuleerd in termen van een parameter van $f(X)$ en dient uit te drukken wat de onderzoekers wensen te bewijzen aan de hand van de studie. Hier: $$H_1: \mu<0.$$ Gemiddeld gezien daalt de bloeddruk bij patiënten met hypertensie na toediening van captopril.

De **nulhypothese** is meestal een uitdrukking van de nultoestand, i.e. de omstandigheden waarin niets bijzonders aan de hand is. De onderzoekers wensen meestal te bewijzen via empirisch onderzoek dat de nulhypothese niet waar is: **Falsificatie principe**. De **nulhypothese wordt veelal uitgedrukt door gebruik te maken van dezelfde parameter als deze die in $H_1$** gebruikt is. Hier: $$H_0 : \mu=0$$ m.a.w. gemiddeld gezien blijft de systolische bloeddruk na toediening van captopril onveranderd.

### Test-statistiek {#test-statistiek}

Eens de populatie, de parameters en de nulhypothese en alternatieve hypothese bepaald zijn, kan de basisgedachte van een hypothesetest als volgt bondig beschreven worden.

Construeer een teststatistiek zodanig dat deze

1.  de evidentie meet die aanwezig is in de steekproef,

2.  tegen de gestelde nulhypothese,

3.  ten voordele van de alternatieve hypothese.

Een teststatistiek is dus noodzakelijk een functie van de steekproefobservaties.

Voor het captopril voorbeeld drukt de statistiek $$T=\bar X - \mu_0$$ uit hoever het steekproefgemiddelde van de bloeddrukdaling ligt van het gemiddelde $\mu_0=0$ in de populatie onder de nulhypothese[^32].

- Als $H_0$ waar is en er dus geen effect is van captopril in de populatie, dan verwachten we dat de teststatistiek T dicht ligt bij $T=0$

- Als $H_1$ waar is, dan verwachten we dat $T<0$.

In de praktijk gebruiken we echter meestal teststatistieken die niet alleen de grootte van het effect in rekening brengen maar ook de onzekerheid op het effect. We doen dit door de effectgrootte te balanceren t.o.v. de standard error.

$$T=\frac{\bar{X}-0}{\text{SE}_{\bar X}}$$ Waarbij $\mu_0=0$ voor het captopril voorbeeld.

Opnieuw geldt dat

- Als $H_0$ waar is en er dus geen effect is van captopril in de populatie, dan verwachten we dat de teststatistiek T dicht ligt bij $T=0$

- Als $H_1$ waar is, dan verwachten we dat $T<0$.

- Voor het captopril voorbeeld vinden we $t=(-18.93-0)/2.33=-8.12$.

- Is $t = -8.12$ groot genoeg in absolute waarde om te kunnen besluiten dat $\mu < 0$ en met welke zekerheid kunnen we dit besluiten?

Om daar een uitspraak over te doen zullen we de teststatistiek T verder bestuderen. T is een toevalsveranderlijke en de verdeling van T hangt af van de verdeling van de steekproefobservaties, maar die verdeling is ongekend! We hebben normaliteit verondersteld, maar dit laat nog steeds het gemiddelde en de variantie onbepaald. Bovendien wordt de hypothesetest net geconstrueerd om een uitspraak te kunnen doen over het gemiddelde $\mu$! De oplossing zit in de nulhypothese die we kunnen veronderstellen als er geen effect is van captopril. De $H_0$ stelt dat $\mu=0$. Als we aannemen dat $H_0$ waar is, dan is het gemiddelde van de normale distributie gekend! Als de bloeddrukverschillen $X_1, \ldots X_{15}$ onafhankelijk en identiek normaal verdeeld (i.i.d.) zijn, dan weten we dat $$\bar X  \stackrel{H_0}{\sim} N(0, \sigma^2/n)$$

Gezien we $\sigma^2$ niet kennen kunnen we deze vervangen door de steekproef variantie. Dan weten we dat $$T=\frac{\bar{X}-0}{\text{SE}_{\bar X}}\stackrel{H_0}{\sim} t(n-1)$$ een t-verdeling volgt met n-1 vrijheidsgraden onder de **nulhypothese**. We weten dat indien de alternatieve hypothese waar zou zijn, we mogen verwachten dat er meer kans is op het observeren van een kleine waarde voor de teststatistiek dan wat verwacht wordt onder de nulhypothese. We zullen de verdeling van de teststatistiek onder de nulhypothese gebruiken om na te gaan of de geobserveerde test-statistiek $t = -8.12$ klein genoeg is om te kunnen besluiten dat $\mu < 0$.

- **Is de geobserveerde teststatistiekwaarde ($t=-8.12$) een waarde die we verwachten als $H_0$ waar is**, of is het een waarde die onwaarschijnlijk klein is als $H_0$ waar is?

- In het laatste geval deduceren we dat we niet langer kunnen aannemen dat $H_0$ waar is, en dienen we dus $H_1$ te concluderen.

- De vraag blijft: (a) hoe groot moet de geobserveerde teststatistiek $t$ zijn opdat we $H_0$ verwerpen zodat (b) we bereid zijn om $H_1$ te besluiten en (c) hoe zeker zijn we van deze beslissing?

- Het antwoord hangt samen met de interpretatie van de kansen die berekend kunnen worden op basis van de nuldistributie[^33] en de geobserveerde teststatistiek $t$.

### De p-waarde {#de-p-waarde}

De kans waarop de keuze tussen $H_0$ en $H_1$ gebaseerd wordt, wordt de **$p$-waarde** genoemd. De berekeningswijze is context-afhankelijk, maar voor het huidige voorbeeld wordt de $p$-waarde gegeven door $$p = P\left[T \leq t \mid H_0\right] = \text{P}_0\left[T\leq t\right],$$ waar de index “0” in $\text{P}_0\left[.\right]$ aangeeft dat de kans onder de nulhypothese berekend wordt. Het is met andere woorden de kans om in een willekeurige steekproef onder de nulhypothese een waarde voor de teststatistiek T te bekomen die lager of gelijk is aan[^34] de waarde die in de huidige steekproef werd geobserveerd.

De $p$-waarde voor het captopril voorbeeld wordt berekend als $$p= \text{P}_0\left[T\leq -8.12\right]=F_t(-8.12;14) = 0.6\ 10^{-6}.$$

waarbij $F_t(;14)$ de cumulatieve distributie functie is van een t-verdeling met 14 vrijheidsgraden, $$F_t(x;14)=\int\limits_{-\infty}^{x} f_t(x;14).$$ Waarbij $f_t(.;14)$ de densiteitsfunctie is van de t-verdeling. De oppervlakte onder de densiteitsfunctie is opnieuw een kans. Deze kans kan berekend worden in R m.b.v. de functie `pt(x,df)` die twee argumenten heeft, de waarde van de test-statistiek `x` en het aantal vrijheidsgraden van de t-verdeling `df`. `pt(x,df)` berekent de kans om een waarde te observeren die kleiner of gelijk is aan x wanneer men een willekeurige observatie trekt uit een t-verdeling met df vrijheidsgraden.

n &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**length**</span>(delta) stat &lt;-<span style="color: 0.31,0.60,0.02"> </span>(<span style="color: 0.13,0.29,0.53">**mean**</span>(delta) <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">0</span>)<span style="color: 0.81,0.36,0.00">**/**</span>(<span style="color: 0.13,0.29,0.53">**sd**</span>(delta)<span style="color: 0.81,0.36,0.00">**/**</span><span style="color: 0.13,0.29,0.53">**sqrt**</span>(n)) stat

    ## [1] -8.122816

<span style="color: 0.13,0.29,0.53">**pt**</span>(stat, n <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">1</span>)

    ## [1] 5.731936e-07

**Definitie 5.6** ($p$-waarde). <span id="def:unnamed-chunk-80"></span><span id="def:unnamed-chunk-80" label="def:unnamed-chunk-80"></span> De **p-waarde** (ook wel **geobserveerd significantieniveau** genoemd) is de kans om onder de nulhypothese een even of meer “extreme” toetsinggrootheid waar te nemen (in de richting van het alternatief) dan de waarde $t$ die geobserveerd werd o.b.v. de steekproef. Hoe kleiner die kans is, hoe sterker het bewijs tegen de nulhypothese.

Merk op dat de p-waarde de kans **niet** uitdrukt dat de nulhypothese waar is![^35].

**Einde Definitie**

Het woord “extreem” duidt op de richting waarvoor de teststatistiek onder de alternatieve hypothese meer waarschijnlijk is. In het voorbeeld is $H_1: \mu < 0$ en verwachten we dus kleinere waarden van $t$ onder $H_1$. Vandaar de kans op $T\leq t$. Uit de definitie van de $p$-waarde volgt dat een kleine $p$-waarde betekent dat de geobserveerde teststatistiek eerder onwaarschijnlijk is als aangenomen wordt dat $H_0$ correct is. Dus een voldoende kleine $p$-waarde noopt ons tot het **verwerpen van $H_0$** ten voordele van $H_1$. De drempelwaarde waarmee de $p$-waarde vergeleken wordt, wordt het **significanctieniveau** genoemd en wordt voorgesteld door $\alpha$.

**Definitie 5.7** (significantieniveau). <span id="def:unnamed-chunk-81"></span><span id="def:unnamed-chunk-81" label="def:unnamed-chunk-81"></span> De drempelwaarde $\alpha$ staat gekend als het **significantieniveau** van de statistische test. Een statistische test uitgevoerd op het $\alpha$ significantieniveau wordt een **niveau-$\alpha$ test** genoemd (Engels: *level-$\alpha$ test*).

**Einde definitie**

Een toetsingsresultaat wordt *statistisch significant* genoemd wanneer de bijhorende p-waarde kleiner is dan $\alpha$, waarbij $\alpha$ meestal gelijk aan 5% wordt genomen. Hoe kleiner de p-waarde hoe meer ‘significant’ het testresultaat afwijkt van de verwachting onder de nulhypothese. Het aangeven van een p-waarde voor een toets geeft bijgevolg meer informatie over het resultaat dan een eenvoudig ja/nee antwoord of de nulhypothese wordt verworpen op een vast gekozen $\alpha$-niveau. Het geeft immers niet alleen aan of de nulhypothese verworpen wordt op een gegeven significantieniveau, maar ook op welke significantieniveaus de nulhypothese verworpen wordt.

Ze vat dus de bewijskracht tegen de nulhypothese samen $$\begin{array}{cl}>0.10 & \text{ niet significant (zwak bewijs)}\\0.05-0.10 & \text{ marginaal significant, suggestief}\\0.01-0.05 & \text{ significant}\\0.001-0.01 & \text{ sterk significant}\\<0.001 & \text{ extreem significant}\end{array}$$

### Kritieke waarde {#kritieke-waarde}

Een **alternatieve wijze voor de formulering van de beslissingsregel** kan worden bekomen door gebruik te maken van een kritieke waarde. In plaats van $p$-waarden, kan de beslissingsregel geschreven worden in termen van de teststatistiek. Bij gebruik van $p$-waarden bepaalt $p=\alpha$ de grens. Een $p$-waarde van $\alpha$ schrijven we als $$p=\text{P}_0 \left[ T \leq t \right]=\alpha.$$

Dat is exact de definitie van het het $\alpha$-percentiel van de distributie van $T$. In het voorbeeld is de nuldistributie $t_{n-1}$. Dus,$$\text{P}_0\left[T\leq -t_{n-1;\alpha}\right]=\alpha.$$

De beslissingsregel mag dus ook geschreven worden als

$$\begin{eqnarray*}
\text{als } & t< -t_{n-1;\alpha} & \text{ dan verwerp }H_0\text{ en besluit }H_1 \\
  \text{als } & t\geq -t_{n-1;\alpha} & \text{ dan aanvaard }H_0.
\end{eqnarray*}$$

Het percentiel $t_{n-1;\alpha}$ dat de drempelwaarde vormt in de beslissingsregel wordt in deze context de **kritieke waarde** op het $5\%$ significantieniveau genoemd. De beslissingsregel waarbij de geobserveerde $t$ vergeleken wordt met een kritieke waarde is minder algemeen geformuleerd dan deze gebruik makend van de $p$-waarde omdat het expliciet gebruik maakt van de nuldistributie die van teststatistiek tot teststatistiek, of zelfs van dataset tot dataset kan variëren.

De begrippen p-waarde, kritieke waarde, significantie-niveau, verwerpings- en aanvaardingsregio worden weergegeven in Figuur <a href="#fig:captoTest" data-reference-type="ref" data-reference="fig:captoTest">5.12</a>.

<figure id="fig:captoTest">
<img src="Statistiek_2019_2020_files/figure-latex/captoTest-1" style="width:100.0%" />
<figcaption>Interpretatie van p-waarde, kritieke waarde, verwerpingsgebied, aanvaardingsgebied voor het captopril voorbeeld.</figcaption>
</figure>

### Beslissingsfouten {#beslissingsfouten}

Aangezien de beslissing over het al dan niet verwerpen van de nulhypothese bepaald wordt door slechts een steekproef te observeren, kunnen volgende beslissing genomen worden:

<table>
<thead>
<tr>
<th style="text-align: center;"></th>
<th colspan="2" style="text-align: center;">Werkelijkheid</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><span>2-3</span> Besluit</td>
<td style="text-align: center;">H0</td>
<td style="text-align: center;">H1</td>
</tr>
<tr>
<td style="text-align: center;">Aanvaard H0</td>
<td style="text-align: center;">OK</td>
<td style="text-align: center;">Type II (β)</td>
</tr>
<tr>
<td style="text-align: center;">Verwerp H0</td>
<td style="text-align: center;">Type I (α)</td>
<td style="text-align: center;">OK</td>
</tr>
</tbody>
</table>

Het schema geeft de vier mogelijke situaties:

- $H_0$ is in werkelijkheid waar, en dit wordt ook besloten aan de hand van de statistische test (dus geen beslissingsfout)

- $H_1$ is in werkelijkheid waar, en dit wordt ook besloten aan de hand van de statistische test (dus geen beslissingsfout)

- $H_0$ is in werkelijkheid waar, maar aan de hand van de statistische test wordt besloten om $H_0$ te verwerpen en $H_1$ te concluderen. Dus $H_1$ wordt foutief besloten. Dit is een zogenaamde **type I** fout.

- $H_1$ is in werkelijkheid waar, maar aan de hand van de statistische test wordt besloten om $H_0$ te aanvaarden. Dit is een zogenaamde **type II** fout. Dus $H_0$ wordt foutief aanvaard.

De beslissing is gebaseerd op een teststatistiek $T$ die een toevalsveranderlijke is. De beslissing is dus ook stochastisch en aan de vier mogelijke situaties uit bovenstaand schema kunnen dus probabiliteiten toegekend worden. Net zoals voor het afleiden van de steekproefdistributie van de teststatistiek, moeten we de distributie van de steekproefobservaties kennen alvorens het stochastisch gedrag van de beslissingen te kunnen beschrijven. Indien we aannemen dat $H_0$ waar is, dan is de distributie van $T$ gekend en kunnen ook de kansen op de beslissingen bepaald worden voor de eerste kolom van de tabel.

We starten met de kans op een type I fout (hier uitgewerkt voor het captopril voor beeld): $$\text{P}\left[\text{type I fout}\right]=\text{P}\left[\text{verwerp }H_0 \mid H_0\right] = \text{P}_0\left[T<t_{n-1;1-\alpha}\right]=\alpha.$$ Dit geeft ons meteen een interpretatie van het significantieniveau $\alpha$: het is de kans op het maken van een type I fout. De constructie van de statistische test garandeert dus dat de kans op het maken van een type I fout gecontroleerd wordt op het significantieniveau $\alpha$. De kans op het correct aanvaarden van $H_0$ is dus $1-\alpha$. Verder kan aangetoond worden dat de p-waarde onder $H_0$ uniform verdeeld is. Het leidt dus tot een uniforme beslissingsstrategie.

Het bepalen van de kans op een type II fout is minder evident omdat de alternatieve hypothese minder éénduidig is als de nulhypothese. In het captopril voorbeeld is $H_1: \mu<0$; met deze informatie wordt de distributie van de steekproefobservaties niet volledig gespecifieerd en dus ook niet de distributie van de teststatistiek. Dit impliceert dat we eigenlijk de kans op een type II fout niet kunnen berekenen. De klassieke *work-around* bestaat erin om één specifieke distributie te kiezen die voldoet aan $H_1$.

$$H_1(\delta): \mu=0-\delta \text{ voor een }\delta>0.$$

De parameter $\delta$ kwantificeert de afwijking van de nulhypothese.

De **kracht** van een test (Engels: *power*) is een kans die meer frequent gebruikt wordt dan de kans op een type II fout $\beta$. De kracht wordt gedefinieerd als

$$\pi(\delta) = 1-\beta(\delta) = \text{P}_\delta\left[T>t_{n-1;1-\alpha}\right]=\text{P}_\delta\left[P<\alpha\right].$$

De kracht van een niveau-$\alpha$ test voor het detecteren van een afwijking $\delta$ van het gemiddelde onder de nulhypothese $\mu_0=0$ is dus de kans dat de niveau-$\alpha$ test dit detecteert wanneer de afwijking in werkelijkheid $\delta$ is.

Merk op dat $\pi(0)=\alpha$ en de kracht van een test toeneemt als de afwijking van de nulhypothese toeneemt.

De **kracht** van de test (d.i. de kans om Type II fouten te vermijden) wordt typisch niet gecontroleerd, tenzij d.m.v. studiedesign en steekproefgrootte.

**Interpretatie**

Stel dat we voor een gegeven dataset bekomen dat $p<\alpha$, m.a.w. $H_0$ wordt verworpen. Volgens het schema van de beslissingsfouten zijn er dan slechts twee mogelijkheden (zie onderste rij van schema): ofwel is de beslissing correct, ofwel hebben we een type I fout gemaakt. Over de type I fout weten we echter dat ze slechts voorkomt met een kleine kans. Anderzijds, indien $p\geq \alpha$ en we $H_0$ niet verwerpen, dan zijn er ook twee mogelijkheden: ofwel is de beslissing correct, ofwel hebben we een type II fout gemaakt. De kans op een type II fout ($\beta$) is echter niet gecontroleerd op een gespecifieerde waarde. De statistische test is zodanig geconstrueerd dat ze enkel de kans op een type I fout controleert (op $\alpha$). Om wetenschappelijk eerlijk te zijn, moeten we een pessimistische houding aannemen en er rekening mee houden dat $\beta$ groot zou kunnen zijn (i.e. een kleine kracht).

Bij $p < \alpha$ wordt de nulhypothese verworpen en we mogen hieruit concluderen dat $H_1$ waarschijnlijk juist is. Dit noemen we een sterke conclusie. Bij $p\geq \alpha$ wordt de nulhypothese aanvaard, maar dat impliceert niet dat we concluderen dat $H_0$ juist is. We kunnen enkel besluiten dat de data onvoldoende bewijskracht tegen $H_0$ ten gunste van $H_1$ bevatten. Dit noemen we een daarom zwakke conclusie.

### Conclusies Captopril voorbeeld. {#conclusies-captopril-voorbeeld.}

De test die we hebben uitgevoerd is in de literatuur ook bekend als de **one sample t-test** op het verschil of als een **gepaarde t-test**, we beschikken immers over gepaarde gegevens per patiënt. De test is eenzijdig uitgevoerd. We testen tegen het alternatief dat er een bloeddrukdaling is.

Beide testen (one sample t-test op het verschil en de gepaarde t-test) geven ons inderdaad dezelfde resultaten:

<span style="color: 0.13,0.29,0.53">**t.test**</span>(delta, <span style="color: 0.13,0.29,0.53">alternative =</span> <span style="color: 0.31,0.60,0.02">"less"</span>)

    ##
    ##  One Sample t-test
    ##
    ## data:  delta
    ## t = -8.1228, df = 14, p-value = 5.732e-07
    ## alternative hypothesis: true mean is less than 0
    ## 95 percent confidence interval:
    ##       -Inf -14.82793
    ## sample estimates:
    ## mean of x
    ## -18.93333

<span style="color: 0.13,0.29,0.53">**with**</span>(captopril, <span style="color: 0.13,0.29,0.53">**t.test**</span>(SBPa, SBPb, <span style="color: 0.13,0.29,0.53">paired =</span> <span style="color: 0.56,0.35,0.01">TRUE</span>, <span style="color: 0.13,0.29,0.53">alternative =</span> <span style="color: 0.31,0.60,0.02">"less"</span>))

    ##
    ##  Paired t-test
    ##
    ## data:  SBPa and SBPb
    ## t = -8.1228, df = 14, p-value = 5.732e-07
    ## alternative hypothesis: true difference in means is less than 0
    ## 95 percent confidence interval:
    ##       -Inf -14.82793
    ## sample estimates:
    ## mean of the differences
    ##               -18.93333

We kunnen op basis van de test het volgende concluderen: Na toediening van captopril is er een extreem significante verlaging van de systolische bloeddruk bij patiënten met hypertensie ($p << 0.001$). De systolische bloeddruk neemt gemiddeld met 18.9 mm kwik af na de behandeling met captopril (95% BI $$$-\infty,-14.82$$$ mm Hg).

Merk op dat we

1.  Een eenzijdig interval rapporteren gezien we enkel geïnteresseerd zijn om aan te tonen dat er een bloeddrukdaling is.

2.  Door het pre-test/post-test design geen uitsluitsel kunnen geven of dit te wijten is aan de werking van het middel of aan een placebo effect. Er was geen goeie controle! Het gebrek van een goeie controle is veelal een probleem bij pre-test/post-test designs.

### Eenzijdig of tweezijdig toetsen? {#eenzijdig-of-tweezijdig-toetsen}

De test in het captopril voorbeeld was een eenzijdige test. We wensen immers enkel te detecteren of de captopril behandeling de bloeddruk gemiddeld gezien doet dalen.

In andere gevallen of een andere context wenst men enkel een stijging te detecteren.
Stel dat men het bloeddrukverschil had gedefineerd als $X_{i}^\prime=Y_{i}^\text{voor}-Y_{i}^\text{na}$ dan zouden positieve waarden aangeven dat er een bloeddrukdaling was na de behandeling van captopril: de bloeddruk bij aanvang is dan immers groter dan na de behandeling. De gemiddelde bloeddrukverandering in de populatie noteren we nu als $\mu^\prime=\text{E}[X^*]$. In dat geval hadden we een eenzijdige test uit moeten voeren om $H_0: \mu^\prime=0$ te testen tegen $H_1: \mu^\prime>0$. Voor deze test kunnen we de p-waarde als volgt berekenen: $$p=\text{P}_0\left[T\geq t\right].$$

We voeren nu de analyse uit in R op basis van de toevallige veranderlijke $X^\prime$. We zullen nu het argument `alternative="greater"` gebruiken in de `t.test` functie zodat we de nulhypothese toetsen tegen het alternatief $H_1: \mu^\prime>0$:

    ##
    ##  One Sample t-test
    ##
    ## data:  delta2
    ## t = 8.1228, df = 14, p-value = 5.732e-07
    ## alternative hypothesis: true mean is greater than 0
    ## 95 percent confidence interval:
    ##  14.82793      Inf
    ## sample estimates:
    ## mean of x
    ##  18.93333

Uiteraard bekomen we met deze analyse exact dezelfde p-waarde en hetzelfde betrouwbaarheidsinterval. Enkel het teken is omgewisseld.

Naast eenzijdige testen kunnen eveneens tweezijdige testen worden uitgevoerd. Het had gekund dat de onderzoekers de werking van het nieuwe medicijn captopril wensten te testen, maar het werkingsmechanisme nog niet kenden in de ontwerpfase. In dat geval zou het eveneens interessant geweest zijn om zowel een stijging als een daling van de bloeddruk te kunnen detecteren. Hiervoor zou men een tweezijdige toetsstrategie moeten gebruiken waarbij men de nulhypothese $$H_0: \mu=0$$ gaat testen versus het alternatieve hypothese $$H_1: \mu\neq0,$$ zodat het gemiddelde onder de alternatieve hypothese verschillend is van 0. Het kan zowel een positieve of negatieve afwijking zijn en men weet niet bij aanvang van de studie in welke richting het werkelijk gemiddelde zal afwijken onder de alternatieve hypothese.

We kunnen tweezijdig testen op het $\alpha=5\%$ significantieniveau door

1.  een kritieke waarde af te leiden:

    - Bij een tweezijdige test kan het effect onder de alternatieve hypothese zowel positief of negatief zijn. Hierdoor zullen we onder de nulhypothese de kans berekenen om onder de nulhypothese een effect te observeren dat meer extreem is dan het resultaat dat werd geobserveerd in de steekproef. In deze context betekent “meer extreem” dat de statistiek groter is in absolute waarde dan het geobserveerde resultaat, want zowel grote (sterk positieve) als kleine (sterk negatieve) waarden zijn een indicatie van een afwijking van de nulhypothese.

    - Om een kritieke waarde af te leiden,zullen we het significatie-niveau $\alpha$ daarom verdelen over de linker en rechter staart van de verdeling onder $H_0$. Gezien de t-verdeling symmetrisch is, volgt dat we een kritieke waarde $c$ kiezen zodat er een kans is van $\alpha/2=2.5\%$ dat $T\geq c$ en er $\alpha/2=2.5\%$ kans is dat $T\leq -c$. We kunnen dit ook nog als volgt formuleren: Er is onder $H_0$ $\alpha=5\%$ kans dat $\vert T\vert\geq c$ (zie Figuur <a href="#fig:captoTest2" data-reference-type="ref" data-reference="fig:captoTest2">5.13</a>).

2.  We kunnen ook gebruik maken van een tweezijdige p-waarde:

    $$\begin{eqnarray*}
        p&=&\text{P}_0\left[T\leq -|t|\right] + \text{P}_0\left[T\geq |t|\right]\\
        &=&\text{P}_0\left[\vert T\vert \geq \vert t \vert\right]\\
        &=&\text{P}_0\left[T \geq \vert t \vert\right]\times 2.
    \end{eqnarray*}$$

We berekenen dus de kans dat de t-statistiek onder $H_0$ meer extreem is dan de geobserveerde teststatistiek $t$ in de steekproef. Waarbij meer extreem tweezijdig moet geïnterpreteerd worden. De teststatistiek onder $H_0$ is meer extreem als hij groter is in absolute waarde dan $\vert t \vert$, de geobserveerde test statistiek. Gezien de verdeling symmetrisch is, kunnen we ook eerst de kans in de rechter staart van de verdeling berekenen en deze kans vervolgens vermenigvuldigen met 2 zodoende een tweezijdige p-waarde te bekomen.

Als de onderzoekers niet vooraf gedefineerd hadden dat ze enkel een bloeddrukdaling wensten te detecteren, dan hadden ze dus een twee-zijdige test uitgevoerd. Merk op dat het argument `alternative` van de `t.test` functie een default waarde heeft `alternative="two.sided"` zodat er standaard tweezijdig wordt getoetst.

<span style="color: 0.13,0.29,0.53">**t.test**</span>(delta)

    ##
    ##  One Sample t-test
    ##
    ## data:  delta
    ## t = -8.1228, df = 14, p-value = 1.146e-06
    ## alternative hypothesis: true mean is not equal to 0
    ## 95 percent confidence interval:
    ##  -23.93258 -13.93409
    ## sample estimates:
    ## mean of x
    ## -18.93333

We bekomen nog steeds een exteem significant resultaat. De p-waarde is echter dubbel zo groot omdat we tweezijdig testen. We verkrijgen eveneens een tweezijdig betrouwbaarheidsinterval. De tweezijdige toetsstrategie wordt weergegeven in Figuur <a href="#fig:captoTest2" data-reference-type="ref" data-reference="fig:captoTest2">5.13</a>.

<figure id="fig:captoTest2">
<img src="Statistiek_2019_2020_files/figure-latex/captoTest2-1" style="width:100.0%" />
<figcaption>Interpretatie van p-waarde, kritieke waarde, verwerpingsgebied, aanvaardingsgebied voor het captopril voorbeeld wanneer we een tweezijdige toets uitvoeren.</figcaption>
</figure>

We kunnen ons nu de vraag stellen wanneer we eenzijdig of tweezijdig toetsen. Met een eenzijdige toets kan men gemakkelijker een alternatieve hypothese aantonen (op voorwaarde dat ze waar is) dan met een tweezijdige toets. Dit komt essentieel omdat bij zo’n toets alle informatie kan worden aangewend om in 1 enkele richting te zoeken. Precies daarom vergt de eenzijdige toets een extra beschouwing vóór de aanvang van de studie. Ook al hebben we sterke a priori vermoedens, vaak kunnen we niet zeker zijn dat dat zo is. Anders was er immers geen reden om dit te willen toetsen.

Als men een eenzijdige test voorstelt, maar men vindt een resultaat in de andere richting dat formeel statistisch significant is, dan is het niet geschikt om dit te zien als bewijs voor een werkelijk effect in die richting. Dat is omdat de onderzoekers die mogelijkheid uitgesloten hebben bij de planning van de studie en het resultaat daarom zó onverwacht is dat het als een vals positief resultaat kan gezien worden. Een eenzijdige test is om die reden niet aanbevolen. Een tweezijdige toets is altijd verdedigbaar omdat ze in principe toelaat om elke afwijking van de nulhypothese te detecteren. Ze worden daarom het meest gebruikt en ten zeerste aangeraden. Het is **nooit toegelaten** om een tweezijdige toets in een eenzijdige toets om te zetten **op basis van wat men observeert in de gegevens**! Anders wordt de type I fout van de toetsingsstrategie niet correct gecontroleerd.

Dat wordt geïllustreerd in de onderstaande simulatie. We evalueren twee strategieën, de correcte tweezijdige test en een test waar we eenzijdig toetsen op basis van het teken van het geobserveerde effect.

    ## [1] 0.049

<span style="color: 0.13,0.29,0.53">**mean**</span>(pvalsInCor <span style="color: 0.81,0.36,0.00">**&lt;**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">0.05</span>)

    ## [1] 0.106

We zien inderdaad dat de type I fout correct gecontroleerd wordt op het nominaal significantie-niveau $\alpha$ wanneer we tweezijdig testen en dat dit helemaal niet het geval is wanneer we eenzijdige toetsen op basis van het teken van het geobserveerde effect.

## Two-sample t-test {#two-sample-t-test}

Een two-sample t-test is een statistische toets die werd ontwikkeld om verschillen in gemiddelde te detecteren tussen twee onafhankelijke groepen. We introduceren eerst een motiverende dataset. Men vermoedt dat hinderlijke geur onder de oksels (bromhidrosis) wordt veroorzaakt door specifieke microorganismen die behoren tot de groep van de *Corynebacterium spp.*. Het is immers niet het zweet dat de geur veroorzaakt, maar de geur is het resultaat van specifieke bacteriën die het zweet metaboliseren. Een andere sterk abundante groep wordt gevormd door de *Staphylococcus spp.*. In de CMET onderzoeksgroep van de Universiteit Gent wordt onderzoek verricht naar de mogelijkheid van microbiële transplanties in de oksels om mensen van de hinderlijke okselgeur te verlossen. Deze therapie bestaat erin om eerst het oksel-microbioom te verwijderen door een lokale antibiotica behandeling, en vervolgens via een microbiële transplantie de populatie te beïnvloeden. (zie: <https://youtu.be/9RIFyqLXdVw> )

De primaire onderzoeksvraag: leidt de microbiële transplantatie na zes weken tot een verandering in de relatieve abundantie van *Staphylococcus spp.* in het oksel microbioom in vergelijking met een placebo behandeling die enkel bestaat uit een antibiotica behandeling? Twintig personen met een hinderlijke okselgeur worden willekeurig toegekend aan twee behandelingsgroepen: placebo (enkel antibiotica) en transplantie (antibiotica, gevolgd door microbiële transplantatie). Zes weken na de start van de behandeling wordt een staal van de huid uit de okselholte genomen en worden de relatieve abundanties van *Staphylococcus spp.* en *Corynebacterium spp.* in het microbioom gemeten via DGGE (*Denaturing Gradient Gel Electrophoresis*).

De dataset bevat de variabelen Staph en Cor die de relatieve abundanties (%) weergeven van *Staphylococcus spp.* en *Corynebacterium spp.* De variabele Rel werd berekend als $$\text{Rel}=\frac{\text{Staph}}{\text{Staph}+\text{Cor}}.$$ Deze variabele is het relatief aandeel van *Staphylococcus spp.* op het totaal aantal *Staphylococcus spp.* en *Corynebacterium spp.*.

In de folder dataset staat de file `oksel.rda`, een dump van het R object `oksel`, een data frame voor het oksel voorbeeld. R objecten die zijn opgeslagen kunnen via de `load(.)` functie worden ingelezen. De resultaten worden weergegeven in Figuur <a href="#fig:okselBox" data-reference-type="ref" data-reference="fig:okselBox">5.14</a>.

<span style="color: 0.13,0.29,0.53">**load**</span>(<span style="color: 0.31,0.60,0.02">"dataset/oksel.rda"</span>) <span style="color: 0.13,0.29,0.53">**head**</span>(oksel)

    ##              trt Staph  Cor      Rel
    ## 1 trt 2: placebo  34.7 28.4 54.99208
    ## 2 trt 2: placebo  16.4 35.1 31.84466
    ## 3 trt 2: placebo  31.4 45.0 41.09948
    ## 4 trt 2: placebo  44.7 30.4 59.52064
    ## 5 trt 2: placebo  45.9 26.3 63.57341
    ## 6 trt 2: placebo  30.7 43.3 41.48649

<span style="color: 0.56,0.35,0.01">*\# outline = FALSE, geen outliers alle datapunten*</span> <span style="color: 0.56,0.35,0.01">*\# worden toegevoegd via stripchart dus ook outliers*</span> <span style="color: 0.56,0.35,0.01">*\# zijn zichtbaar*</span> <span style="color: 0.13,0.29,0.53">**boxplot**</span>(Rel <span style="color: 0.81,0.36,0.00">** **</span><span style="color: 0.31,0.60,0.02"> </span>trt, <span style="color: 0.13,0.29,0.53">data =</span> oksel, <span style="color: 0.13,0.29,0.53">xlab =</span> <span style="color: 0.31,0.60,0.02">"behandeling"</span>, <span style="color: 0.13,0.29,0.53">ylab =</span> <span style="color: 0.31,0.60,0.02">"Relatieve abundantie"</span>, <span style="color: 0.13,0.29,0.53">outline =</span> <span style="color: 0.56,0.35,0.01">FALSE</span>) <span style="color: 0.13,0.29,0.53">**set.seed**</span>(<span style="color: 0.00,0.00,0.81">394</span>) <span style="color: 0.13,0.29,0.53">**stripchart**</span>(Rel <span style="color: 0.81,0.36,0.00">** **</span><span style="color: 0.31,0.60,0.02"> </span>trt, <span style="color: 0.13,0.29,0.53">data =</span> oksel, <span style="color: 0.13,0.29,0.53">vertical =</span> <span style="color: 0.56,0.35,0.01">TRUE</span>, <span style="color: 0.13,0.29,0.53">method =</span> <span style="color: 0.31,0.60,0.02">"jitter"</span>, <span style="color: 0.13,0.29,0.53">pch =</span> <span style="color: 0.00,0.00,0.81">19</span>, <span style="color: 0.13,0.29,0.53">col =</span> <span style="color: 0.13,0.29,0.53">**c**</span>(<span style="color: 0.31,0.60,0.02">"bisque"</span>, <span style="color: 0.31,0.60,0.02">"coral"</span>), <span style="color: 0.13,0.29,0.53">add =</span> <span style="color: 0.56,0.35,0.01">TRUE</span>) <span style="color: 0.13,0.29,0.53">**set.seed**</span>(<span style="color: 0.00,0.00,0.81">394</span>) <span style="color: 0.13,0.29,0.53">**stripchart**</span>(Rel <span style="color: 0.81,0.36,0.00">** **</span><span style="color: 0.31,0.60,0.02"> </span>trt, <span style="color: 0.13,0.29,0.53">data =</span> oksel, <span style="color: 0.13,0.29,0.53">vertical =</span> <span style="color: 0.56,0.35,0.01">TRUE</span>, <span style="color: 0.13,0.29,0.53">method =</span> <span style="color: 0.31,0.60,0.02">"jitter"</span>, <span style="color: 0.13,0.29,0.53">pch =</span> <span style="color: 0.00,0.00,0.81">1</span>, <span style="color: 0.13,0.29,0.53">add =</span> <span style="color: 0.56,0.35,0.01">TRUE</span>)

<figure id="fig:okselBox">
<img src="Statistiek_2019_2020_files/figure-latex/okselBox-1" style="width:100.0%" />
<figcaption>Boxplot van de relatieve Staphylococcus spp. abundantie t.o.v. het totaal van Staphylococcus spp. en Corynebacterium spp., voor beide behandelingsgroepen.</figcaption>
</figure>

<figure id="fig:okselQQ">
<img src="Statistiek_2019_2020_files/figure-latex/okselQQ-1" style="width:100.0%" />
<figcaption>QQ-plots van relatieve Staphylococcus spp. abundantie t.o.v. het totaal van Staphylococcus spp. en Corynebacterium spp.</figcaption>
</figure>

Normaliteit van de data in beide groepen wordt ook nagegaan d.m.v. QQ-plots (zie Figuur <a href="#fig:okselQQ" data-reference-type="ref" data-reference="fig:okselQQ">5.15</a>). De QQ-plots geven geen te grote afwijkingen weer van normaliteit.

We introduceren eerst de notatie. Stel $Y_{ij}$ de uitkomst van observatie $i=1,\ldots, n_j$ uit populatie $j=1,2$. We zullen dikwijls de term **behandeling** of **groep** gebruiken in plaats van populatie, zelfs wanneer de twee populaties niet geïnterpreteerd kunnen worden als behandelingen. Beschouw het als een (misgroeide) conventie. In de context van het voorbeeld is behandeling $j=1$ de microbiële transplantatie en behandeling $j=2$ de placebo behandeling.

We veronderstellen

$$Y_{ij}\text{ i.i.d. } N(\mu_j,\sigma^2)\;\;\;i=1,\ldots,n_i\;j=1,2.$$

Merk op dat dit inhoudt dat gelijke varianties verondersteld worden. De eigenschap van gelijke varianties wordt ook aangeduid met de term **homoskedasticiteit**, en ongelijke varianties met **heteroskedasticiteit**.

We zijn geïnteresseerd in het testen van de nulhypothese $$H_0: \mu_1 = \mu_2$$ tegenover de alternatieve hypothese $$H_1: \mu_1 \neq \mu_2 .$$ De alternatieve hypothese drukt dus de onderzoeksvraag uit: een verschil in relatieve abundantie van *Staphylococcus spp.* na microbiële transplantatie t.o.v. de placebo behandeling.
De nul en alternatieve hypothese kunnen ook worden uitgedrukt in termen van de effectgrootte tussen behandeling en placebo groep $\mu_1-\mu_2$: $$H_0: \mu_1-\mu_2 = 0,$$ $$H_1: \mu_1-\mu_2 \neq 0.$$

We kunnen de effectgrootte in het experiment schatten a.d.h.v. de steekproefgemiddeldes: $$\hat \mu_1-\hat \mu_2=\bar Y_1 -\bar Y_2.$$ Gezien de experimentele eenheden onafhankelijk zijn, zijn de steekproefgemiddeldes dat ook en is de variantie op het verschil: $$\text{Var}_{\bar Y_1 -\bar Y_2}=\frac{\sigma^2}{n_1}+\frac{\sigma^2}{n_2}=\sigma^2 \left(\frac{1}{n_1}+\frac{1}{n_2}\right).$$ De standard error is bijgevolg: $$\sigma_{\bar Y_1 -\bar Y_2}=\sigma\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}.$$

We zouden de variantie apart kunnen schatten in elke groep aan de hand van de steekproefvariatie, maar als we gelijkheid van variantie kunnen veronderstellen kan de variantie meer precies worden geschat door gebruik te maken van alle gegevens in beide groepen. Deze variatieschatter wordt ook de gepoolde variantieschatter genoemd: $S^2_p$.

Op basis van de observaties uit de eerste groep kan $\sigma^2_1$ geschat worden als $$S_1^2 = \frac{1}{n_1-1}\sum_{i=1}^{n_1} (Y_{i1}-\bar{Y}_1)^2.$$

Analoog: op basis van de observaties uit de tweede groep kan $\sigma^2_2$ geschat worden als $$S_2^2 = \frac{1}{n_2-1}\sum_{i=1}^{n_2} (Y_{i2}-\bar{Y}_2)^2.$$

Merk op dat we homoscedasticiteit veronderstellen, $\sigma_1^2=\sigma_2^2=\sigma^2$. Dus $S_1^2$ en $S_2^2$ zijn schatters zijn voor dezelfde parameter $\sigma^2$. Daarom kunnen ze gezamenlijk gebruikt worden om tot één schatter te komen die alle $n_1+n_2$ observaties gebruikt: $$S_p^2 = \frac{n_1-1}{n_1+n_2-2} S_1^2 + \frac{n_2-1}{n_1+n_2-2} S_2^2 = \frac{1}{n_1+n_2-2}\sum_{j=1}^2\sum_{i=1}^{n_j} (Y_{ij} - \bar{Y}_j)^2.$$

De gepoolde variantieschatter wordt dus geschat door gebruik te maken van de kwadratische afwijkingen tussen de observaties en hun groepsgemiddelde en dat te delen door het aantal vrijheidsgraden $n_1+n_2-2$[^36].

Nu we de effectgrootte en de standard error op de effectgrootte hebben kunnen schatten, kunnen we opnieuw een t-statistiek definiëren (two-sample $t$-teststatistiek):

$$T = \frac{\bar{Y}_1-\bar{Y}_2}{\sqrt{\frac{S_p^2}{n_1}+\frac{S_p^2}{n_2}}} =
  \frac{\bar{Y}_1 - \bar{Y}_2}{S_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}.$$

Als de data onafhankelijk zijn, de steekproefgemiddelden normaal verdeeld zijn en de variantie in beide groepen gelijk zijn, dan kan men aantonen de teststatistiek T opnieuw een t-verdeling volgt met $n_1+n_2-2$ vrijheidsgraden onder de nulhypothese.

Aangezien de alternatieve hypothese $H_1: \mu_1 \neq \mu_2$ impliceert dat de probabiliteitsmassa van de distributie van $T$ onder $H_1$ verschuift naar hogere of lagere waarden, zullen we $H_0$ wensen te verwerpen ten gunste van $H_1$ voor grote absolute waarde van de teststatistiek. De $p$-waarde wordt dus

$$\begin{eqnarray*}
  p&=&\text{P}_0\left[T\leq -|t|\right] + \text{P}_0\left[T\geq |t|\right]\\
  &=&\text{P}_0\left[\vert T\vert \geq \vert t \vert\right]\\
  &=&\text{P}_0\left[T \geq \vert t \vert\right]\times 2\\
  &=& 2\times(1-F_T(\vert t\vert;n_1+n_2-2)),
\end{eqnarray*}$$

met $F_T(\cdot;n_1+n_2-2)$ de cumulatieve distributiefunctie van $t_{n_1+n_2-2}$.

### Oksel-voorbeeld {#oksel-voorbeeld}

De onderzoeksvraag van het oksels-voorbeeld kan vertaald worden in een nulhypothese en een alternatieve hypothese.

De nulhypothese verwoordt de stelling dat de behandeling geen effect heeft op de gemiddelde relatieve abundantie van *Staphylococcus spp.*.

Indien $\mu_1$ en $\mu_2$ de gemiddelde abundanties voorstellen in respectievelijk de transplantatie groep en de placebo groep, dan schrijven we $$H_0: \mu_1=\mu_2.$$ De alternatieve hypothese correspondeert met wat we wensen te bewijzen aan de hand van de experimentele data: een verschil in gemiddelde abundantie van *Staphylococcus spp.* in de transplantatie groep i.v.m. de placebo groep. Dus $$H_1: \mu_1\neq \mu_2.$$

De berekeningen kunnen als volgt in R worden uitgevoerd:

    ## [1] 49.79

    ## [1] 31.9

    ## [1] 64.95656

    ## [1] 76.78222

    ## [1] 10

    ## [1] 10

<span style="color: 0.56,0.35,0.01">*\# gepoolde variantieschatting*</span> sp2 &lt;-<span style="color: 0.31,0.60,0.02"> </span>((n1 <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">1</span>) <span style="color: 0.81,0.36,0.00">**\***</span><span style="color: 0.31,0.60,0.02"> </span>var1 <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span>(n2 <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">1</span>) <span style="color: 0.81,0.36,0.00">**\***</span><span style="color: 0.31,0.60,0.02"> </span>var2)<span style="color: 0.81,0.36,0.00">**/**</span>(n1 <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span>n2 <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span> <span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">2</span>) sp2

    ## [1] 70.86939

<span style="color: 0.56,0.35,0.01">*\# geobserveerde t-statistiek*</span> t.obs &lt;-<span style="color: 0.31,0.60,0.02"> </span>(ybar1 <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span>ybar2)<span style="color: 0.81,0.36,0.00">**/**</span><span style="color: 0.13,0.29,0.53">**sqrt**</span>(sp2<span style="color: 0.81,0.36,0.00">**/**</span>n1 <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span>sp2<span style="color: 0.81,0.36,0.00">**/**</span>n2) t.obs

    ## [1] 4.751886

<span style="color: 0.56,0.35,0.01">*\# p-waarde*</span> p &lt;-<span style="color: 0.31,0.60,0.02"> </span>(<span style="color: 0.00,0.00,0.81">1</span> <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**pt**</span>(<span style="color: 0.13,0.29,0.53">**abs**</span>(t.obs), <span style="color: 0.13,0.29,0.53">df =</span> n1 <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span>n2 <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">2</span>)) <span style="color: 0.81,0.36,0.00">**\***</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">2</span> p

    ## [1] 0.0001592919

<span style="color: 0.56,0.35,0.01">*\# De p-waarde kon ook worden berekend door gebruik*</span> <span style="color: 0.56,0.35,0.01">*\# te maken van de probabiliteit in de linker staart*</span> <span style="color: 0.56,0.35,0.01">*\# dat is vaak stabieler in R*</span> p &lt;-<span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.13,0.29,0.53">**pt**</span>(<span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.13,0.29,0.53">**abs**</span>(t.obs), <span style="color: 0.13,0.29,0.53">df =</span> n1 <span style="color: 0.81,0.36,0.00">**+**</span><span style="color: 0.31,0.60,0.02"> </span>n2 <span style="color: 0.81,0.36,0.00">**-**</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">2</span>) <span style="color: 0.81,0.36,0.00">**\***</span><span style="color: 0.31,0.60,0.02"> </span><span style="color: 0.00,0.00,0.81">2</span> p

    ## [1] 0.0001592919

De R software heeft ook een specifieke functie voor het uitvoeren van deze $t$-test.

<span style="color: 0.13,0.29,0.53">**t.test**</span>(Staph <span style="color: 0.81,0.36,0.00">** **</span><span style="color: 0.31,0.60,0.02"> </span>trt, <span style="color: 0.13,0.29,0.53">data =</span> oksel, <span style="color: 0.13,0.29,0.53">var.equal =</span> <span style="color: 0.56,0.35,0.01">TRUE</span>)

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

Uit deze analyse lezen we $p\approx 0.16 \times 10^{-3}<<0.05$.

Dus op het $5\%$ significantieniveau verwerpen we de nulhypothese ten voordele van de alternatieve en besluiten we dat de gemiddelde abundantie van *Staphylococcus spp.* extreem significant hoger is in de transplantatie groep dan in de placebo groep[^37].

Indien de transplantatie geen effect heeft op de gemiddelde abundantie van *Staphylococcus spp.*, dan is er slechts een kans van 16 in de $100000$ om een teststatistiek te bekomen in een willekeurige steekproef die minstens zo extreem is als deze die wij geobserveerd hebben.

Dit is uiterst zeldzaam onder de hypothese dat $H_0$ waar is, en het is kleiner dan $5\%$ (het significantieniveau). Indien $H_1$ waar zou zijn, dan verwachten we grotere absolute waarden van de teststatistiek en verwachten we dus ook kleine $p$-waarden. Om deze reden wensen we niet verder te geloven dat $H_0$ waar is, en besluiten we dat er veel evidentie in de steekproefdata zit om te besluiten dat $H_1$ waar is op het $5\%$ significantieniveau.

**Good statistical practice** houdt ook in dat niet enkel de $p$-waarde van de hypothesetest wordt gerapporteerd, maar dat ook de gemiddelden en een maat voor de betrouwbaarheid van de schattingen (bv. BI) worden gerapporteerd.

**Conclusie** Gemiddeld is de relatieve abundantie van *Staphylococcus spp.* in het microbioom van de oksel in de transplantatie groep extreem significant verschillend van dat in de controle groep ($p<<0.001$). De relatieve abundantie van *Staphylococcus spp.* is gemiddeld 17.9% hoger in de transplantie groep dan in de controle groep (95% BI $$10.0,25.8$$%).

## Aannames {#aannames}

In de voorgaande secties hebben we t-testen geïntroduceerd en de geldigheid ervan hangt af van enkele distributionele veronderstellingen:

- Onafhankelijke gegevens (design)

- One-sample t-test: normaliteit van de steekproefobservaties

- Paired t-test: normaliteit van de verschillen tussen de gepaarde observaties

- Two-sample t-test: normaliteit van de steekproefobservaties in beide groepen, en gelijkheid van varianties.

Indien niet voldaan is aan de veronderstellingen, is de t-distributie niet noodzakelijk de correcte nuldistributie, en bijgevolg is er geen garantie dat de p-waarde en kritieke waarden correct zijn.

Ook voor de constructie van het betrouwbaarheidsinterval van het gemiddelde hebben we beroep gedaan op de veronderstelling van normaliteit. De normaliteitsveronderstelling was nodig om kwantielen uit de t-verdeling te kunnen gebruiken bij het opstellen van de boven- en ondergrens, en de correcte probabiliteitsinterpretatie van het betrouwbaarheidsinterval hangt hiervan af.

### Nagaan van de veronderstelling van Normaliteit {#nagaan-van-de-veronderstelling-van-normaliteit}

Normaliteit kan via de volgende methoden nagegaan worden.

**Boxplots en histogrammen**

Beide figuren laten toe om een idee te vormen over de vorm van de distributie: symmetrie, outliers. …

**QQ-plots**

Deze plots laten toe om op een grafische wijze na te gaan in welke mate steekproefobservaties zich gedragen als een vooropgestelde distributie.

**Hypothesetesten (goodness-of-fit test)**

Goodness-of-fit testen zijn statistische hypothesetesten die ontwikkeld zijn voor het testen van de nulhypothese dat de steekproefobservaties uit een vooropgestelde distributie getrokken zijn (hier: normale distributie). De alternatieve hypothese is meestal de negatie van de nulhypothese (hier: geen normaliteit). Bekende testen zijn: Kolmogorov-Smirnov, Shapiro-Wilk en Anderson-Darling.

Op het eerste zicht lijkt een goodness-of-fit test een gemakkelijke en zinvolle oplossing. De methode geeft een $p$-waarde en deze laat onmiddellijk toe om te besluiten of de data normaal verdeeld zijn.

Er is echter kritiek te leveren op deze aanpak:

- indien $p\geq \alpha$, dan is normaliteit niet bewezen! Het zegt enkel dat er onvoldoende evidentie is tegen de veronderstelling van normaliteit. In een kleine steekproef is de kracht van een test meestal klein.

- indien $p<\alpha$, dan mag wel besloten worden om de nulhypothese te verwerpen en mag dus besloten worden dat de data niet normaal verdeeld zijn, maar soms is een afwijking van normaliteit niet zo erg.

**Algemeen advies**: Start met een grafische exploratie van de data (boxplots, histogrammen en QQ-plots) en houdt hierbij steeds de steekproefgrootte in het achterhoofd om te vermijden dat je de figuren zou overinterpreteren. Als je twijfelt kan je gebruik maken van simulaties waarbij je nieuwe steekproeven simuleert met eenzelfde steekproefgrootte en data die uit de Normaal verdeling komt met eenzelfde gemiddelde en variantie als wat in de steekproef werd geobserveerd.

Indien een afwijking van normaliteit wordt vastgesteld, tracht dan na te gaan (bv. via literatuur) of de statistische methode die je wenst toe te passen, gevoelig is voor dergelijke afwijkingen (een t-test is bijvoorbeeld vrij ongevoelig voor afwijkingen van Normaliteit als de afwijkingen symetrisch zijn). Eventueel kan je ook beroep doen op de centrale limietstelling.

### Nagaan van homoscedasticiteit {#nagaan-van-homoscedasticiteit}

Dat kan opnieuw via boxplots. De grootte van de box is de interkwartiel range (IQR), een robuuste schatter voor de variantie (zie Sectie <a href="#subsec:spreiding" data-reference-type="ref" data-reference="subsec:spreiding">4.3.2</a>). Als de verschillen tussen de IQR range van beide groepen niet te groot is, kan men besluiten dat de data homoscedastisch zijn. Opnieuw kan inzicht gekregen worden in dergelijke plots door gebruik te maken van simulaties (zie Oefeningen). Men kan eveneens een formele F-test gebruiken om de varianties te vergelijken (zie oefeningen), maar hiervoor geldt dezelfde kritiek als voor het testen van normaliteit (zie vorige sectie).

Als er bij het vergelijken van gemiddelden tussen twee groepen niet aan homoscedasticiteit is voldaan, kan je gebruik maken van de Welch two-sample T-test. Hierbij wordt de gepoolde variantieschatter niet langer gebruikt. $$T =  \frac{\bar{Y}_1 - \bar{Y}_2}{\sqrt{\frac{S^2_1}{n_1}+\frac{S^2_2}{n_2}}}$$ waarbij $S^2_1$ en $S^2_2$ de steekproefvarianties zijn in beide groepen.

Deze statistiek volgt bij benadering een t-verdeling met een aantal vrijheidsgraden dat ligt tussen het kleinste aantal observaties $\text{min}(n_1-1,n_2-1)$ en $n_1+n_2-2$. De vrijheidsgraden worden in R berekend via de Welch–Satterthwaite benadering. Dat kan door in de `t.test` functie het argument `var.equal=FALSE` te zetten.

<span style="color: 0.13,0.29,0.53">**t.test**</span>(Staph <span style="color: 0.81,0.36,0.00">** **</span><span style="color: 0.31,0.60,0.02"> </span>trt, <span style="color: 0.13,0.29,0.53">data =</span> oksel, <span style="color: 0.13,0.29,0.53">var.equal =</span> <span style="color: 0.56,0.35,0.01">FALSE</span>)

    ##
    ##  Welch Two Sample t-test
    ##
    ## data:  Staph by trt
    ## t = 4.7519, df = 17.876, p-value = 0.0001622
    ## alternative hypothesis: true difference in means is not equal to 0
    ## 95 percent confidence interval:
    ##   9.976456 25.803544
    ## sample estimates:
    ## mean in group trt 1: transplant    mean in group trt 2: placebo
    ##                           49.79                           31.90

Merk op dat we in de output zien dat een Welch T-test is uitgevoerd aan de titel boven de analyse. Verder zien we dat voor dit voorbeeld de aangepaste vrijheidsgraden $df = 17.876$ bijna gelijk zijn aan de vrijheidsgraden van de klassieke T-test, omdat de varianties ongeveer gelijk zijn.

## Wat rapporteren? {#wat-rapporteren-1}

- In de wetenschappelijke literatuur is er een overdreven aandacht voor p-waarden.

- Nochtans is het interessanter om een schatting te rapporteren samen met een betrouwbaarheidsinterval (dan met een p-waarde).

**Vuistregel**: Rapporteer een schatting steeds samen met een betrouwbaarheidsinterval (en een p-waarde), want

1.  Het resultaat van een toets kan veelal uit een betrouwbaarheidsinterval worden afgeleid;

2.  Dit laat toe om te oordelen of het resultaat ook **wetenschappelijk van belang** is.

### Reden 1: Relatie toetsen en betrouwbaarheidsintervallen {#reden-1-relatie-toetsen-en-betrouwbaarheidsintervallen}

Stel dat we voor een zekere parameter $\theta$ (bvb. een populatiegemiddelde, verschil in populatiegemiddelden, odds ratio, regressieparameter) de nulhypothese wensen te toetsen dat $H_0 : \theta= \theta_0$ versus het alternatief $H_A : \theta \neq \theta_0$ voor een zeker getal $\theta_0$. Dan kan men aantonen dat men deze tweezijdige toetsingsprocedure kan uitvoeren op het $\alpha 100\%$ significantieniveau door de nulhypothese te verwerpen als en slechts als het $(1-\alpha)100\%$ betrouwbaarheidsinterval voor $\theta$ het getal $\theta_0$ niet omvat. Met andere woorden, het $(1-\alpha)100\%$ betrouwbaarheidsinterval voor $\theta$ bevat alle getallen $\theta_0$ zodat de tweezijdige toets van $H_0 : \theta= \theta_0$ versus $H_1 : \theta \neq \theta_0$ de nulhypothese niet verwerpt.

### Reden 2: Statistische significantie versus wetenschappelijke relevantie {#reden-2-statistische-significantie-versus-wetenschappelijke-relevantie}

Een betrouwbaarheidsinterval laat toe om zowel statistische significantie als wetenschappelijk belang van een resultaat te interpreteren.

Stel dat experimentele behandeling *significant betere* respons oplevert dan standaard/placebo. Een associatie is *statistisch significant* als P $< \alpha$, de data dragen m.a.w. voldoende bewijskracht om te besluiten dat er een associatie is. Dan blijft het mogelijk dat het effect *wetenschappelijk irrelevant* is. Met betrouwbaarheidsintervallen kunnen we dit wel evalueren.

Maar, dat laat echter nog veel subjectiviteit en manipulatie toe. Onderzoekers hopen in de praktijk immers wetenschappelijk belangrijke vondsten te maken en kunnen daarom geneigd zijn om hun oordeel over wat wetenschappelijk belangrijk is, wijzigen in functie van het bekomen betrouwbaarheidsinterval. Om dit te vermijden is het wenselijk dat wetenschappers a priori, d.i. vooraleer de gegevens verzameld werden, hun oordeel over wetenschappelijke relevantie uitdrukken.

## Equivalentie-intervallen {#equivalentie-intervallen}

Betrouwbaarheidsintervallen kunnen ook worden gebruikt om na te gaan of twee interventies **wetenschappelijk equivalent** zijn. Twee interventies worden **wetenschappelijk equivalent** genoemd als het verschil tussen de populatiegemiddelden $\mu_1$ en $\mu_2$ van hun uitkomsten $X_1$ en $X_2$ in een equivalentie-interval ligt (dat 0 zal omvatten), bijvoorbeeld:

$$\begin{equation*}
(\mu_1 - \mu_2) \in [E_1, E_2]
\end{equation*}$$

In de meeste gevallen worden $E_1$ en $E_2$ symmetrisch rond nul gekozen, in welk geval $E_1=-\Delta$ en $E_2=\Delta$ voor gegeven $\Delta$. Het (wetenschappelijk) equivalentie-interval wordt dan gegeven door alle koppels $(\mu_1,\mu_2)$ waarvoor

$$\begin{equation*}
|\mu_1 - \mu_2| < \Delta
\end{equation*}$$

Twee interventies zijn met andere woorden klinisch equivalent wanneer hun verschil in effect verwaarloosbaar klein is vanuit wetenschappelijk oogpunt.

In het vervolg van deze sectie zullen we nagaan of de gemiddelden van 2 onafhankelijke populaties wetenschappelijk equivalent zijn (of wetenschappelijk niet significant van elkaar verschillen). Een eerste stap in dit proces is om op basis van louter wetenschappelijk overwegingen een interval op te stellen waarbinnen het verschil $\mu_1-\mu_2$ verwaarloosbaar klein kan worden genoemd. Dit gebeurt met hulp van een deskundige die kan oordelen over het belang van een gegeven effectgrootte. Vervolgens wordt het gemiddeld verschil in uitkomst onder beide interventies geschat op basis van de gegevens. Nagaan of dit verschil in het equivalentie-interval gelegen is, volstaat op zich niet om wetenschappelijke equivalentie te kunnen besluiten vermits een klein/groot verschil louter het gevolg kan zijn van biologische variatie. Een logische stap is daarom een bijhorend 95% betrouwbaarheidsinterval voor $\mu_1 - \mu_2$ te berekenen op basis van de beschikbare gegevens (gepaard, ongepaard, …). De wetenschappelijke equivalentie zal nu bepaald worden door de ligging van het betrouwbaarheidsinterval te vergelijken met het interval van wetenschappelijke equivalentie.

Het zou verkeerd zijn om wetenschappelijke equivalentie te besluiten zodra het equivalentie-interval volledig omsloten is door het 95% betrouwbaarheidsinterval. Inderdaad, kleine steekproeven produceren brede betrouwbaarheidsintervallen zodat men op die manier in kleine steekproeven gemakkelijk equivalentie zou besluiten louter wegens gebrek aan informatie. We volgen daarom de volgende strategie. Noem $O$ de ondergrens en $B$ de bovengrens van het 95% betrouwbaarheidsinterval voor $\mu_1-\mu_2$.

1.  Als $E_1 < O < B < E_2$, dan is het verschil tussen de populatiegemiddelden met minstens 95% kans binnen de grenzen van wetenschappelijke equivalentie gelegen. Men kan dan met minstens 95% zekerheid besluiten dat de 2 interventies inderdaad wetenschappelijk equivalent zijn.

2.  Als $E_2 < O$ dan kan men met minstens 95% zekerheid besluiten dat $\mu_1$ wetenschappelijk significant groter is dan $\mu_2$. (In dit geval is $\mu_1$ automatisch ook statistisch significant groter dan $\mu_2$ op het 2-zijdig significantieniveau 5%).

3.  Als $B < E_1$ dan kan men met minstens 95% zekerheid besluiten dat $\mu_1$ wetenschappelijk significant kleiner is dan $\mu_2.$

Het resultaat kan ook minder duidelijk zijn.

1.  Als $O < E_1 < E_2 < B$ dan is er te weinig informatie om ook maar iets betekenisvol te kunnen besluiten: meer gegevens zijn nodig.

2.  Als \$O &lt; E\_1 &lt; B &lt; E\_2 \$ dan kan men op het 5% significantieniveau besluiten dat $\mu_1$ *niet* wetenschappelijk groter is dan $\mu_2$. In dat geval zijn zowel de opties wetenschappelijk equivalent met $\mu_2$ als wetenschappelijk significant kleiner dan $\mu_2$ niet uit te sluiten met 95% zekerheid.

3.  Analoog voor de symmetrische situatie waarbij $E_1 < O < E_2 < B.$

In asthmastudies legt men bijvoorbeeld **op voorhand vast** dat een verschil in Peak Expiratory Flow (PEF) van 15 l/min klinisch onbelangrijk is. Men bepaald m.a.w. een equivalentie-interval: $$-15,15$$ l/min. Een 95% BI van $$-10,-5$$ l/min voor gemiddeld verschil in PEF tussen twee geneesmiddelen Formoterol en Salbutamol wijst op een onbelangrijk effect, equivalentie. Het betrouwbaarheidsinterval geeft weer hoe groot het verschil kan zijn. Als men een BI van $$-25,-16$$ l/min had bekomen dan kon men besluiten dat het geneesmiddel Formoterol minder efficient is gezien het gemiddeld gezien PEF waarden oplevert die wetenschappelijk significant lager zijn dan wanneer Salbutamol wordt toegediend. Als het $$-20,-5$$ l/min zou zijn, dan is er ambiguïteit.

[^23]: Ook wel Statistische Inferentie genoemd

[^24]: Om die reden duiden we ze aan met een hoofdletter.

[^25]: Zo is het met 1 observatie voor $\bar X$ niet mogelijk om een histogram voor $\bar X$ uit te zetten.

[^26]: In principe is een meer theoretische, mathematische ontwikkeling nodig omdit aan te tonen, maar voor het bestek van deze cursus volstaat het om het meer intuïtieve argument aan te nemen.

[^27]: Merk op dat de vierkantswortel van een som niet gelijk is aan de som van de vierkantswortels. Bijgevolg is de standaarddeviatie van de som van $X$ en $Y$ niet de som van de corresponderende standaarddeviaties!

[^28]: Denk zelf maar eens na of je gevallen kunt bedenken waar je al op voorhand, zonder ook maar observaties te zien, de variantie op een bepaalde karakteristiek kent…

[^29]: 95.1% is niet exact gelijk aan het nominale 95% omdat er ‘slechts’ 1000 simulaties gelopen zijn

[^30]: De steekproefstandaarddeviatie is eveneens een toevallig veranderlijke die van steekproef tot steekproef varieert rond werkelijke standaarddeviatie. Hierdoor zal de breedte van de intervallen eveneens variëren

[^31]: independent and identically distributed, onafhankelijk en gelijk verdeeld

[^32]: vandaar de index 0 bij $\mu_0$

[^33]: distributie van de teststatistiek onder de nulhypothese

[^34]: meer extreem in de richting van $H_1$

[^35]: In de frequentistische theorie die we hier volgen, is de nulhypothese immers ofwel altijd waar, ofwel altijd vals, en is het dus zelfs niet mogelijk om de kans te definiëren dat de nulhypothese waar is. Teminste, die kans is ofwel 1 ofwel 0.!

[^36]: We hebben $n_1+n_2$ observaties (vrijheidsgraden) in het experiment, om de gepoolde variantie te schatten hebben we echter 2 vrijheidsgraden verloren aangezien we eerst het gemiddelde in elke groep dienden te bepalen om de variantie te kunnen schatten.

[^37]: Merk op dat we de richting “significant hoger is in de transplantatie groep” afleiden uit de groepsgemiddelden in de output en/of het BI

---

[← Data exploratie en beschrijvende statistiek](06-data-exploratie-en-beschrijvende-statistiek.md) · [Up: contents](index.md) · [Enkelvoudige lineaire regressie →](08-enkelvoudige-lineaire-regressie.md)

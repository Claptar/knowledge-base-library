---
title: 5.2 Captopril voorbeeld
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-besluit.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 5.2 Captopril voorbeeld

**Source:** [`chap-besluit.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

Onderzoekers wensen na te gaan of het medicijn Captopril een bloeddruk verlagend effect heeft. De onderzoekers wensen uitspraken te kunnen doen over het effect van captopril op de systolische bloeddruk van huidige en toekomstige patiënten met hypertensie, m.a.w. ze wensen uitspraken te doen over het effect van captopril op het niveau van de *Populatie*. Ze zullen hiervoor een experiment opzetten om het effect van captopril bestuderen (*Proefopzet*) waarbij een *steekproef* (sample) van de patiënten met hypertensie is getrokken uit de populatie. Vervolgens zullen ze de data exploreren en het effect van captopril besturen in de steekproef (*Data Exploratie & Beschrijvende Statistiek*). Op basis van de steekproef zullen ze dan het effect van captopril *Schatten* in de populatie en zullen ze a.d.h.v. methoden uit *Statistische besluitvorming*<a href="#fn23" id="fnref23" class="footnoteRef"><sup>23</sup></a> nagaan in hoeverre de geobserveerde effecten in de steekproef veralgemeend kunnen worden naar de algemene populatie toe.

Deze verschillende stappen worden geïllustreerd in Figuur [5.1](index.md).

<span id="fig:captoPop2Samp2Pop"></span> <img src="Statistiek_2019_2020_files/figure-html/captoPop2Samp2Pop-1.png" style="width:100.0%" alt="Verschillende stappen in de captopril studie." />

Figuur 5.1: Verschillende stappen in de captopril studie.

### <span class="header-section-number">5.2.1</span> Proefopzet

Bij proefopzet zullen we een gestructureerd design voorstellen om lukraak subjecten uit de doelpopulatie te selecteren, toe te wijzen aan een behandeling en te observeren. We zullen hierbij een response variabele meten, een karakteristiek van interesse. In het captopril voorbeeld is dit de systolische bloeddruk.

In de captopril studie hebben de onderzoekers gebruik gemaakt van een een pre-test/post-test design. De patiënten werden at random gekozen uit de populatie. Van elke patiënt in de studie werd de systolische en diasystolische bloeddruk gemeten voor en na het toedienen van captopril. Het pre-test/post-test design heeft als voordeel dat we het effect van het toedienen van captopril op de bloeddruk kunnen meten voor elke patiënt. Een nadeel daarentegen is dat er geen controle behandeling is waardoor we een mogelijkse bloeddrukverlaging niet noodzakelijkerwijs kunnen toeschrijven aan de werking van captopril. Er zou immers ook een placebo-effect kunnen optreden waardoor de bloeddruk van de patiënt daalt omdat men weet dat men een medicijn kreeg tegen een hoge bloeddruk.

### <span class="header-section-number">5.2.2</span> Data Exploratie & Beschrijvende Statistiek

Eens de data zijn geobserveerd, is het belangrijk om deze te exploreren om inzicht te krijgen in hun verdeling en karakteristieken. Vervolgens zullen we de gegevens samenvatten zodat we het effect van interesse kunnen kwantificeren in de steekproef. In deze studie is de systolische bloeddruk en de diasystolische bloeddruk gemeten voor elke patiënt voor en na het toedienen van captopril. De data is opgeslagen in een tekstbestand met naam `captopril.txt` in de folder dataset. We zullen eerst exploreren welke figuren nuttig zijn in onze context. In wetenschappelijke artikels worden vaak figuren gemaakt van het gemiddelde en de standaardafwijking (zie Figuur [5.2](index.md)).

``` {.sourceCode .r}
#Eerst lezen we de data in.
#Deze bevindt zich in de subdirectory dataset
#Het is een tekstbestand waarbij de kolommen van elkaar gescheiden zijn d.m.v kommas.
#sep=","
#De eerste rij bevat de namen van de variabelen
captopril <- read.table("dataset/captopril.txt",header=TRUE,sep=",")
head(captopril)
```

    ##   id SBPb DBPb SBPa DBPa
    ## 1  1  210  130  201  125
    ## 2  2  169  122  165  121
    ## 3  3  187  124  166  121
    ## 4  4  160  104  157  106
    ## 5  5  167  112  147  101
    ## 6  6  176  101  145   85

``` {.sourceCode .r}
#We gebruiken de apply functie om het gemiddelde en de standaard deviatie
#te berekenen voor de kolommen die bloeddruk data bevatten (kolom 2:4)
#We gebruiken argument MARGIN=2 om de functie toe te passen op de kolommen
#MARGIN=1 kan gebruikt worden om de functie op de rijen toe te passen
mm<-apply(captopril[,2:5],MARGIN=2,FUN=mean)
hh<-apply(captopril[,2:5],MARGIN=2,FUN=sd)

mp <- barplot(mm,ylim=c(0,250),ylab="Gemiddelde bloeddruk (mmHg)",main="")
#fouten vlaggen
segments(mp,mm,mp,mm+2*hh)
segments(mp-.2,mm+2*hh,mp+.2,mm+2*hh)
```

<span id="fig:captoBar"></span> <img src="Statistiek_2019_2020_files/figure-html/captoBar-1.png" style="width:100.0%" alt="Barplot van de gemiddelde bloeddruk in de captopril studie. De foutenvlag is 2x de standaard deviatie op de metingen (SBPb: systolic BloodPressure before, DBPb: Diasystolic BloodPressure before, SBPa: systolic BloodPressure after, DBPa: Diasystolic BloodPressure after)." />

Figuur 5.2: Barplot van de gemiddelde bloeddruk in de captopril studie. De foutenvlag is 2x de standaard deviatie op de metingen (SBPb: systolic BloodPressure before, DBPb: Diasystolic BloodPressure before, SBPa: systolic BloodPressure after, DBPa: Diasystolic BloodPressure after).

De figuur is echter niet informatief. De hoogte van de balken zegt enkel iets over het gemiddelde. We kunnen onmogelijk weten wat het bereik van de ruwe gegevens is bijvoorbeeld. Daarom is het beter om de gegevens zo ruw mogelijk weer te geven in een plot. We kunnen hiervoor bijvoorbeeld gebruik maken van boxplots (Figuur [5.3](index.md)). Aangezien we maar over 15 patiënten beschikken kunnen we ook de ruwe datapunten toevoegen. In de figuur zien we dat de systolische bloeddruk in de steekproef gemiddeld lager ligt na de behandeling met captopril. We krijgen ook een duidelijk beeld op het bereik van de data.

``` {.sourceCode .r}
boxplot(captopril[,2:5],ylim=c(0,250),ylab="Bloeddruk (mmHg)",main="")
#toevoegen van originele datapunten op de plot
#jitter zal de punten random verspreiden
#set seed om gekleurde volle bol pch=19 te zetten
#en daarna een zwarte rand te kunnen zetten op zelfde plaats.
set.seed(19)
stripchart(captopril[,2:5],
            vertical = TRUE, method = "jitter",
            pch = 19, col =c("bisque","coral","darkcyan","purple"),
            add = TRUE)
set.seed(19)
stripchart(captopril[,2:5],
            vertical = TRUE, method = "jitter",
            pch = 1, col =1,
            add = TRUE)
```

<span id="fig:captoBox"></span> <img src="Statistiek_2019_2020_files/figure-html/captoBox-1.png" style="width:100.0%" alt="Boxplot en ruwe data van de bloeddruk in de captopril studie (SBPb: systolic BloodPressure before, DBPb: Diasystolic BloodPressure before, SBPa: systolic BloodPressure after, DBPa: Diasystolic BloodPressure after)." />

Figuur 5.3: Boxplot en ruwe data van de bloeddruk in de captopril studie (SBPb: systolic BloodPressure before, DBPb: Diasystolic BloodPressure before, SBPa: systolic BloodPressure after, DBPa: Diasystolic BloodPressure after).

Als alle bloeddrukmetingen onafhankelijk zouden zijn dan is Figuur [5.3](index.md) een goede figuur om de data te exploreren. We weten echter dat de metingen voor en na het toedienen van captopril afkomstig zijn van dezelfde patiënt. We kunnen die informatie toevoegen in een dotplot zoals we illustreren voor de systolische bloeddruk in Figuur [5.4](index.md). In deze figuur zijn de twee bloeddrukmetingen voor dezelfde persoon verbonden met een lijn. Deze figuur geeft duidelijk weer dat de bloeddruk daalt voor elke patiënt wat een sterke aanwijzing is dat er een effect is van het toedienen van captopril op de systolische bloeddruk.

``` {.sourceCode .r}
#D.m.v de matplot functie kunnen we eenvoudig
#de data van dezelfde patient (per kolom)
#vandaar dat we de dataset transponeren (t(.)) functie
#en verbinden a.d.h.v. een lijn. (lty=1)
#we gebruiken ook een dezelfde kleur.
#en gebruiken zowel een punt als een lijn
#om de data voor te stellen type="b"
matplot(t(captopril[,c("SBPb","SBPa")]),pch=1,lty=1,col="black",type="b",xaxt="none",xlim=c(0.5,2.5),ylab="Systolische bloeddruk (mmHg)",cex=.5)
axis(1,c(1,2),labels=c("voor","na"))
```

<span id="fig:captoDotBsl"></span> <img src="Statistiek_2019_2020_files/figure-html/captoDotBsl-1.png" style="width:100.0%" alt="Dotplot van de systolische bloeddruk in de captopril studie voor en na het toedienen van captopril." />

Figuur 5.4: Dotplot van de systolische bloeddruk in de captopril studie voor en na het toedienen van captopril.

Aangezien we slechts twee bloeddrukmetingen hebben per patiënt kunnen we het effect van captopril ook berekenen per patiënt door het verschil in de systolische bloeddruk na en voor de toediening van captopril te berekenen. Dat is één van de voordelen van een pre-test/post-test design.

``` {.sourceCode .r}
#we selecteren de bloeddruk na en voor toedienen
#uit de dataset via naam van variabele d.m.v. $-teken
#en berekenen het verschil
delta <- captopril$SBPa-captopril$SBPb
boxplot(delta,ylab=expression(paste("Verschil in bloeddruk (",Delta[Na - Voor],")")))
set.seed(19)
stripchart(delta,
            vertical = TRUE, method = "jitter",
            pch = 19, col =c("bisque"),
            add = TRUE)
set.seed(19)
stripchart(delta,
            vertical = TRUE, method = "jitter",
            pch = 1, col =1,
            add = TRUE)
```

<span id="fig:captoBoxDelta"></span> <img src="Statistiek_2019_2020_files/figure-html/captoBoxDelta-1.png" style="width:100.0%" alt="Boxplot van het verschil in systolische bloeddruk voor en na het toedienen van captopril." />

Figuur 5.5: Boxplot van het verschil in systolische bloeddruk voor en na het toedienen van captopril.

We observeren in Figuur [5.5](index.md) een bloeddrukdaling voor elke patiënt in de steekproef wat opnieuw een heel sterke indicatie is voor een gunstig effect van het toedienen van captopril op de bloeddruk. De verschillen in systolische bloeddruk zijn een goede maat om het effect van captopril te bepalen. We kunnen de data als volgt samenvatten.

``` {.sourceCode .r}
summary(delta)
```

    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
    ##  -33.00  -24.50  -20.00  -18.93  -13.50   -3.00

``` {.sourceCode .r}
sd(delta)
```

    ## [1] 9.027471

We observeren gemiddeld een systolische bloeddrukdaling van 18.93 mmHg en een standaard deviatie van 9.03 mmHg.

### <span class="header-section-number">5.2.3</span> Schatten

Pre-test/post-test design: Het effect van captopril in de steekproef kan worden bestudeerd door het verschil te bepalen in systolische bloeddruk na en voor de behandeling (<span class="math inline">\$X=\\Delta\_\\text{na-voor}\$</span>)! Hoe kunnen we de bloeddrukverschillen modelleren en het effect van het toedienen van captopril schatten?

<span id="fig:captoBoxDiffQQ"></span> <img src="Statistiek_2019_2020_files/figure-html/captoBoxDiffQQ-1.png" style="width:100.0%" alt="QQ-plot voor het verschil in systolische bloeddruk voor en na het toedienen van captopril." />

Figuur 5.6: QQ-plot voor het verschil in systolische bloeddruk voor en na het toedienen van captopril.

    ## [1] 4 2

We zien geen grote afwijkingen van Normaliteit in Figuur [5.6](index.md). We kunnen de bloeddrukverschillen dus modelleren aan de hand van een Normale verdeling en kunnen het effect van captopril in de populatie beschrijven a.d.h.v. de gemiddelde bloeddrukverschil <span class="math inline">\$\\mu\$</span>. Het bloeddrukverschil <span class="math inline">\$\\mu\$</span> in de populatie kan worden geschat a.d.h.v. het steekproefgemiddelde <span class="math inline">\$\\bar x\$</span>=-18.93 en de standaard afwijking <span class="math inline">\$\\sigma\$</span> a.d.h.v. de steekproefstandaarddeviatie <span class="math inline">\$\\text{SD}\$</span>=9.03.

We vragen ons nu af of het effect dat we observeren in de steekproef groot genoeg is om te kunnen spreken van een effect van captopril in de populatie. We weten immers dat onze statistiek voor de schatting van het effect van captopril in de populatie berekend wordt op basis van de gegevens uit de steekproef en daarom zal variëren van steekproef tot steekproef. Het is daarom belangrijk om een inzicht te krijgen in hoe het steekproefgemiddelde zal variëren van steekproef tot steekproef.

---

[← 5.1 Inleiding](01-5-1-inleiding.md) · [Up: contents](index.md) · [5.3 Puntschatters: het steekproefgemiddelde →](03-5-3-puntschatters-het-steekproefgemiddelde.md)

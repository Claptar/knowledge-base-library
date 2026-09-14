---
title: 10.1 Inleiding {#inleiding}
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-glm.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-glm.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 10.1 Inleiding {#inleiding}

**Source:** [`chap-glm.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-glm.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

Tot nog toe hebben we ons geconcentreerd op het beschrijven van een associatie tussen een uitkomst <span class="math inline">\$Y\$</span> en één enkele predictor <span class="math inline">\$X\$</span>. Vaak is het echter nuttig om de gemiddelde uitkomst niet in termen van één, maar in termen van meerdere predictoren simultaan te beschrijven. De volgende voorbeelden illustreren waarom:

1.  Vaak is de associatie tussen een verklarende variabele X en een uitkomst Y verstoord als gevolg van een confounder C. Bijvoorbeeld, bij het bepalen van het effect van de duur van blootstelling aan asbest (X) op de longfunctie (Y), is leeftijd (C) een confounder omdat het zowel de duur van blootstelling als de longfunctie beïnvloedt. Om hiervoor te corrigeren, is het noodzakelijk om de associatie tussen X en Y afzonderlijk te beschrijven voor mensen van dezelfde leeftijd (m.a.w. individuen met dezelfde waarde voor de confounder). Voor elke geobserveerde leeftijd (C=c) een aparte lineaire regressie uitvoeren onder mensen van die leeftijd (C=c), is weinig zinvol omdat er vaak weinig mensen met exact dezelfde leeftijd in de studie opgenomen zijn. Dit is in het bijzonder zo wanneer er meerdere confounders zijn. In deze sectie zullen we dit probleem oplossen door de confounder C als extra variabele in het lineaire model op te nemen.

2.  In heel wat studies is men geïnteresseerd in welke van een groep variabelen een gegeven uitkomst het meest beïnvloedt. Bijvoorbeeld, het begrijpen van welke aspecten van habitat en menselijke activiteit een voorname impact hebben op de biodiversiteit in het regenwoud is een belangrijk streefdoel van de conservatie-biologie. Daartoe wil men niet alleen de grootte van het woud in rekening brengen, maar ook andere factoren, zoals de ouderdom en hoogteligging van het woud, de nabijheid van andere wouden, … Een studie van het simultane effect van die verschillende variabelen laat toe om beter inzicht te krijgen in de variatie in biodiversiteit tussen verschillende wouden. Door in het bijzonder wouden met hoge of lage biodiversiteit nader te bekijken, kan men nieuwe predictieve factoren voor biodiversiteit ontdekken.

3.  Wanneer men een uitkomst wil voorspellen voor individuen, is het belangrijk om veel predictieve informatie voor hen beschikbaar te hebben en die informatie simultaan in een regressiemodel te kunnen gebruiken. Bijvoorbeeld, na behandeling van patiënten met gevorderde borstkanker is de prognose zeer onzeker. Op basis van gemeten predictoren voor en na de operatie kan men echter regressiemodellen opbouwen die toelaten om in de toekomst voor elke patiënt, op basis van zijn/haar karakteristieken, de prognose te voorspellen. Verwante predicties (maar dan voor het risico op sterfte) worden dagdagelijks gebruikt in eenheden intensieve zorgen om de ernst van de gezondheidstoestand van een patiënt uit te drukken. Het spreekt voor zich dat betere predicties kunnen gemaakt worden wanneer een groot aantal predictoren simultaan worden in rekening gebracht.

In dit hoofdstuk breiden we daarom enkelvoudige lineaire regressie (Hoofdstuk [6](../chap-linReg/index.md)) uit door meerdere predictoren toe te laten. We zullen dus de gemiddelde uitkomsten modelleren als een functie van meerdere predictoren. We illustreren meervoudige lineaire regressie aan de hand van de prostaatkanker dataset.

### <span class="header-section-number">10.1.1</span> Prostaatkanker dataset {#prostaatkanker-dataset}

Stamey et al., 1989, bestudeerden het niveau van het prostaat specific antigen (PSA) en een aantal klinische metingen bij 97 mannen waarvan de prostaat werd verwijderd. Het doel van de studie is om de associatie van de PSA te bestuderen in functie van het tumorvolume (lcavol), het gewicht van de prostaat (lweight), leeftijd (age), de goedaardige prostaathypertrofie hoeveelheid (lbph), een indicator voor de aantasting van de zaadblaasjes (svi), capsulaire penetratie (lcp), Gleason score (gleason) die de graad van kwaadaardigheid van de kanker weergeeft (hoe hoger de score hoe minder de kankercellen op normaal prostaatweefsel lijken), en, het precentage gleason score 4/5 (pgg45), die de proportie aangeeft van de tumor die ingenomen wordt door kankerweefsel van een hoge graad. De onderzoekers die de dataset verspreidden hebben het tumorvolume, het gewicht, de goedaardige prostraat hypertrofie hoeveelheid en de capsulaire penetratie reeds log-getransformeerd.

``` {.sourceCode .r}
prostate<-read.csv("dataset/prostate.csv")
head(prostate)
```

    ##       lcavol  lweight age      lbph     svi       lcp gleason   pgg45
    ## 1 -0.5798185 2.769459  50 -1.386294 healthy -1.386294       6 healthy
    ## 2 -0.9942523 3.319626  58 -1.386294 healthy -1.386294       6 healthy
    ## 3 -0.5108256 2.691243  74 -1.386294 healthy -1.386294       7      20
    ## 4 -1.2039728 3.282789  58 -1.386294 healthy -1.386294       6 healthy
    ## 5  0.7514161 3.432373  62 -1.386294 healthy -1.386294       6 healthy
    ## 6 -1.0498221 3.228826  50 -1.386294 healthy -1.386294       6 healthy
    ##         lpsa
    ## 1 -0.4307829
    ## 2 -0.1625189
    ## 3 -0.1625189
    ## 4 -0.1625189
    ## 5  0.3715636
    ## 6  0.7654678

``` {.sourceCode .r}
plot(prostate)
```

<span id="fig:lpsaAll"></span> <img src="Statistiek_2019_2020_files/figure-html/lpsaAll-1.png" style="width:100.0%" alt="Scatterplot matrix voor de observaties in de prostaat kanker dataset." />

Figuur 10.1: Scatterplot matrix voor de observaties in de prostaat kanker dataset.

Figuur [10.1](index.md) toont de scatter matrix van de data en suggereert dat de lpsa sterk positief gecorreleerd is met het volume en svi. We zien verder dat lcp en lbph links-gecensureerd lijken te zijn. Er lijkt een ondergrens/detectielimiet te zijn voor deze metingen. Verder blijkt het merendeel van de gleason scores gelijk te zijn aan 6 of 7. We zullen de analyse in dit hoofdstuk beperken tot de associatie van lpsa met het log tumorvolume (lcavol), het log gewicht (lweight) en de aantasting van de zaadblaasjes (svi).

---

[Up: contents](index.md) · [10.2 Het additieve meervoudig lineaire regressie model →](02-10-2-het-additieve-meervoudig-lineaire-regressie-model.md)

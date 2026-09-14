---
title: 2.5 Steekproef
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/belangrijke-concepten-conventies.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/belangrijke-concepten-conventies.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2.5 Steekproef

**Source:** [`belangrijke-concepten-conventies.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/belangrijke-concepten-conventies.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

In de praktijk is het om financiële en logistieke redenen bijna nooit mogelijk om de volledige populatie te bestuderen. Populatieparameters kunnen daarom meestal niet exact bepaald worden. Enkel een deel van de populatie kan onderzocht worden, hetgeen men de *steekproef* noemt. Volgens een gestructureerd design worden daartoe **lukraak subjecten** uit de doelpopulatie getrokken en geobserveerd. De onbekende parameters worden vervolgens geschat o.b.v. die steekproef en noemt met schattingen. In de praktijk hoopt men uiteraard dat de schattingen die men bekomt op basis van de steekproef vergelijkbaar zijn met de overeenkomstige populatieparameters die men voor de volledige populatie zou bekomen.

Stel bijvoorbeeld dat we op basis van de NHANES studie hypertensie wensen te definiëren. We zullen hiervoor subjecten met “normale” bloeddrukwaarden moeten selecteren. Veronderstel dat we <span class="math inline">\$n\$</span> gezonde personen zullen selecteren in de studie tussen 40 en 65 jaar en we geïnteresseerd zijn in systolische bloeddruk. Telkens een lukraak individu getrokken wordt uit de populatie zal men een realisatie van de toevalsveranderlijke <span class="math inline">\$X\$</span> kunnen observeren. Die realisatie of geobserveerde waarde duiden we aan met een kleine letter <span class="math inline">\$x\$</span>. Deze stelt dus een welbepaald getal voor en is niet langer een onbekende veranderlijke zoals <span class="math inline">\$X\$</span>. Samengevat zijn de nog onbekende waarden voor de bestudeerde populatiekarakteristiek bij subjecten 1 tot <span class="math inline">\$n\$</span> in de steekproef, toevalsveranderlijken die we algemeen met <span class="math inline">\$X\_1,...,X\_n\$</span> zullen noteren. Na het trekken van de steekproef, ziet men de gerealiseerde uitkomsten <span class="math inline">\$x\_1, x\_2, \\dots, x\_n\$</span>, bijvoorbeeld hun gemeten systolische bloeddruk.

We selecteren hieronder de subset van gezonde personen tussen de 40-65 jaar in de NHANES studie. Deze definiëren we verder als niet rokers, zonder diabetes, met een normaal BMI, zonder historiek van hard drugs, zonder lage gezondheidsstatus en zonder slaapproblemen. Op deze manier hebben we dus inclusie- en exclusiecriteria geformuleerd voor het definiëren van de populatie van interesse.

``` {.sourceCode .r}
library(NHANES)
NHANES2=subset(NHANES,!is.na(Race1)&!is.na(Smoke100n)&!is.na(BMI_WHO)%in%!is.na(Age)&!is.na(HardDrugs)&!is.na(HealthGen)&!is.na(Gender)&!is.na(AlcoholYear)&!is.na(BPSys1)&!is.na(BPSys2)&!is.na(BPSys3)&!is.na(SleepTrouble))
NHANES2$bpSys=rowMeans(NHANES2[,c(27,29,31)])
nhanesSub=subset(NHANES2, Age<=65&Age>=40 &!duplicated(ID) )
nhanesSubHealthy=subset(nhanesSub,Smoke100n=="Non-Smoker"&Diabetes=="No"&as.double(BMI_WHO)%in%c(2,3)&HardDrugs=="No"&HealthGen!="Poor"&SleepTrouble=="No")
head(nhanesSubHealthy$bpSys)
```

    ## [1] 114.00000 140.66667  94.66667 152.66667 128.00000 124.00000

``` {.sourceCode .r}
dim(nhanesSubHealthy)
```

    ## [1] 275  77

Op basis van de inclusie en exclusie-criteria werden <span class="math inline">\$n=275\$</span> gezonde individuen uit de Amerikaanse populatie weerhouden. De toevallig veranderlijke systolische bloeddruk wordt dus genoteerd als <span class="math inline">\$X\$</span> terwijl de n = 275 geobserveerde metingen genoteerd worden als <span class="math inline">\$x\_1,x\_2,...,x\_{275}\$</span>. De variable <span class="math inline">\$X\$</span> is random of stochastisch aangezien zijn waarde veranderlijk is. Voor een random subject uit de populatie kunnen we de systolische bloeddruk niet exact voorspellen, het hangt immers af van het geselecteerde subject, tijdstip van de meting, …

---

[← 2.4 Beschrijven van de populatie](05-2-4-beschrijven-van-de-populatie.md) · [Up: contents](index.md) · [2.6 Schatten van de verdeling in de populatie →](07-2-6-schatten-van-de-verdeling-in-de-populatie.md)

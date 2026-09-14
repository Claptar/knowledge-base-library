---
title: 7.1 Inleiding {#inleiding}
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-anova.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-anova.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 7.1 Inleiding {#inleiding}

**Source:** [`chap-anova.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-anova.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">7.1.1</span> Prostacycline voorbeeld

Prostacycline is een lipide die een belangrijke rol speelt in vasodilatatie (bloedvatverwijding) en bloedstolling. Het inhibeert de activatie van bloedplaatjes en vermijdt de vorming van bloedklonters. Arachidonzuur speelt een belangrijke rol in de productieweg van prostacycline. Onderzoekers willen daarom bestuderen of het toedienen van arachidonzuur een effect heeft op het prostacycline niveau in het bloedplasma. Ze zetten hiervoor een proef op waarbij ze het effect van arachidonzuur zullen nagaan op het prostacycline niveau van ratten. Arachidonzuur wordt hierbij toegediend in drie verschillende concentraties (verklarende variabele met drie behandelingen): laag (L, 10 eenheden), gemiddeld (M, 25 eenheden) en een hoge dosis (H, 50 eenheden). Het prostacycline niveau in het bloedplasma wordt gemeten a.d.h.v. een gecalibreerde elisa fluorescentie meting (responsvariabele).
Het experiment is een *volledige gerandomiseerd proefopzet*, *“completely randomized design” CRD*. In totaal worden 12 ratten (experimentele eenheden) at random toegekend aan elke behandelingsgroep. De data is opgeslagen in een tekst bestand met naam `prostacyclin.txt` in de folder dataset. Een boxplot en QQ-plots voor de data in elke groep worden weergegeven in Figuur [7.1](index.md).

``` {.sourceCode .r}
prostacyclin <- read.table("dataset/prostacyclin.txt",header=TRUE,sep="\t")
#dosis wordt als continue covariaat ingelezen
#zet om naar een factor.
prostacyclin$dose <- as.factor(prostacyclin$dose)
par(mfrow=c(2,2))
#boxplot
plot(prostac~dose,data=prostacyclin,xlab="Arachidonzuurdosis ",ylab="Prostacycline (ng/ml)")
#toevoegen van originele datapunten op de plot
#jitter zal de punten random verspreiden
#set seed om gekleurde volle bol pch=19 te zetten
set.seed(10)
stripchart(prostac~dose,data=prostacyclin,
            vertical = TRUE, method = "jitter",
            pch = 19, col =c("bisque","coral","darkcyan"),
            add = TRUE)
#zelfde seed gebruiken zodat we op zelfde plek een
#ronde open cirkel kunnen zetten zodat punt duidelijker is
#pch =1, col=1 (kleur is zwart)
set.seed(10)
stripchart(prostac~dose,data=prostacyclin,
            vertical = TRUE, method = "jitter",
            pch = 1, col =1,
            add = TRUE)
#3 QQ plot via for loop, we lopen over de niveaus voor de prostacycline dosis
for (i in levels(prostacyclin$dose)) with(subset(prostacyclin,dose==i),{qqnorm(prostac,ylim=c(0,max(prostacyclin$prostac)),main=paste("Dosis",i));qqline(prostac)})
```

<span id="fig:prostBox"></span> <img src="Statistiek_2019_2020_files/figure-html/prostBox-1.png" style="width:100.0%" alt="Data-exploratie van het prostacycline niveau bij 36 ratten die behandeld werden met drie verschillende arachidonzuurconcentraties (12 ratten per behandeling). Links boven: boxplots van prostacycline niveau in functie van de dosis, QQ-plot van prostacycline voor lage, matige en hoge dosisgroep worden respectievelijk rechtsboven, linksonder en rechtsonder weergegeven" />

Figuur 7.1: Data-exploratie van het prostacycline niveau bij 36 ratten die behandeld werden met drie verschillende arachidonzuurconcentraties (12 ratten per behandeling). Links boven: boxplots van prostacycline niveau in functie van de dosis, QQ-plot van prostacycline voor lage, matige en hoge dosisgroep worden respectievelijk rechtsboven, linksonder en rechtsonder weergegeven

Figuur [7.1](index.md) geeft weer dat er een effect lijkt te zijn van de arachidonzuurdosis op de hoogte van het prostacycline niveau. In het bijzonder de hoge dosis lijkt het prostacycline niveau in het bloedplasma te laten toenemen.

### <span class="header-section-number">7.1.2</span> Model {#model}

Op basis van de boxplots in Figuur [7.1](index.md) zien we dat de variantie gelijk lijkt te zijn tussen de verschillende behandelingsgroepen. Er is een indicatie dat het gemiddeld prostacycline niveau verschilt tussen de behandelingsgroepen. In het bijzonder voor de hoge dosisgroep H (50 eenheden). Er zijn geen grote verschillen in de interkwartiel range (box-groottes). De QQ-plots in Figuur [7.1](index.md) tonen geen grote afwijkingen aan van Normaliteit. De QQ-plot geeft een indicatie dat mogelijks een outlier voorkomt in groep L. Deze wordt echter niet door de boxplots gesignaleerd.

We kunnen dus volgend statistisch model voorop stellen:

<span class="math display">\\$$Y\_i \\vert \\text{groep j} \\sim N(\\mu\_j,\\sigma^2),\\$$</span> met <span class="math inline">\$j= \\text{1, 2, 3}\$</span>, respectievelijk de lage, matige en hoge dosisgroep. Hierbij veronderstellen we dus dat de data Normaal verdeeld zijn met een gelijke variantie binnen elk van de <span class="math inline">\$g=3\$</span> groepen, <span class="math inline">\$\\sigma^2\$</span>, maar met een verschillend groepsgemiddelde <span class="math inline">\$\\mu\_j\$</span>.

De onderzoeksvraag kan nu vertaald worden in termen van het model. De onderzoekers wensen aan te tonen dat het arachidonzuur niveau een effect heeft op de gemiddelde prostacycline concentratie in het bloed.

Dat vertaalt zich in volgende nulhypothese, de arachidonzuurconcentratie heeft geen effect op het gemiddelde prostacycline niveau bij ratten, <span class="math display">\\$$H\_0:\\mu\_1=\\mu\_2 = \\mu\_3\\$$</span> en de alternatieve hypothese dat er een effect is van de arachidonzuurconcentratie op het gemiddelde prostacycline niveau bij ratten. Dat betekent dat minstens twee gemiddelden verschillend zijn <span class="math display">\\$$H\_1: \\exists\\ j,k \\in \\{1,\\ldots,g\\} : \\mu\_j\\neq\\mu\_k.\\$$</span> Of letterlijk: er bestaat minstens één koppel behandelingsgroepen (j en k) waarvoor het gemiddelde prostacycline niveau <span class="math inline">\$\\mu\_j\$</span> verschillend is van dat in groep <span class="math inline">\$k\$</span>, <span class="math inline">\$\\mu\_k\$</span>.

Een naïeve benadering zou zijn om de nulhypothese op splitsen in partiële hypothesen <span class="math display">\\$$ H\_{0jk}: \\mu\_j=\\mu\_k \\text{ versus } H\_{1jk}: \\mu\_j \\neq \\mu\_k\\$$</span> Waarbij de gemiddelden tussen de groepen twee aan twee worden vergeleken. Met deze procedure zouden we elk van deze partiële hypothesen kunnen testen met een two-sample <span class="math inline">\$t\$</span>-test. Dat zou echter leiden tot een probleem van meervoudig toetsen en een verlies aan power (zie verder). Voor dit voorbeeld zouden we met deze aanpak immers 3 t-testen moeten uitvoeren om de onderzoeksvraag te evalueren.

In dit hoofdstuk zullen we methoden introduceren om <span class="math inline">\$H\_0:\\mu\_1=\\mu\_2=\\mu\_3\$</span> vs <span class="math inline">\$H\_1: \\exists j,k \\in \\{1,\\ldots,g\\} : \\mu\_j\\neq\\mu\_k\$</span> te testen met **één enkele test**. De correcte oplossing voor het testprobleem waarbij we een continue response meten en wensen te detecteren of er een verschil is in gemiddelde response tussen meerdere groepen wordt een **variantie-analyse of ANOVA** (ANalysis Of VAriance) genoemd.

---

[Up: contents](index.md) · [7.2 Variantie-analyse →](02-7-2-variantie-analyse.md)

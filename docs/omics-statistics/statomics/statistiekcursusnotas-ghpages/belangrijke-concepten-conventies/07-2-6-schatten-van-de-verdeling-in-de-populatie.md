---
title: 2.6 Schatten van de verdeling in de populatie
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/belangrijke-concepten-conventies.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/belangrijke-concepten-conventies.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2.6 Schatten van de verdeling in de populatie

**Source:** [`belangrijke-concepten-conventies.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/belangrijke-concepten-conventies.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

In realiteit kennen we de verdeling van de gegevens niet. We kunnen de verdeling o.b.v. de steekproef schatten en grafisch weergegeven a.d.h.v. een histogram (functie `hist()` in R)

``` {.sourceCode .r}
histAbs<-hist(nhanesSubHealthy$bpSys,xlab="Systolische Bloeddruk (mm kwik).",breaks=seq(65,175,5),ylab="Frequentie",cex.main=1.5,cex.axis=1.5,cex.lab=1.5,main="")
```

<span id="fig:nhanesNormalSteekproef"></span> <img src="Statistiek_2019_2020_files/figure-html/nhanesNormalSteekproef-1.png" style="width:100.0%" alt="Weergave van de verdeling voor de systolische bloeddruk van gezonde personen tussen 40-65 jaar geschat aan de hand van een histogram o.b.v. de geobserveerde steekproef in de NHANES studie. (Absolute frequenties)" />

Figuur 2.3: Weergave van de verdeling voor de systolische bloeddruk van gezonde personen tussen 40-65 jaar geschat aan de hand van een histogram o.b.v. de geobserveerde steekproef in de NHANES studie. (Absolute frequenties)

Merk op dat de hoogte van de balken, aantallen op de y-as, weergeeft hoeveel subjecten vallen in een bepaald interval bloeddrukken ($$80-85\[, \[85-90\[, …). Op basis van de steekproef kunnen we via het histogram schatten wat de kans is om een random persoon te bemonsteren met een bloeddruk tussen 115 - 120 mm Hg uit de populatie .

``` {.sourceCode .r}
tab<-cbind(histAbs$mids,histAbs$counts)
tab
```

    ##        [,1] [,2]
    ##  [1,]  67.5    0
    ##  [2,]  72.5    0
    ##  [3,]  77.5    0
    ##  [4,]  82.5    1
    ##  [5,]  87.5    2
    ##  [6,]  92.5    6
    ##  [7,]  97.5    9
    ##  [8,] 102.5   22
    ##  [9,] 107.5   35
    ## [10,] 112.5   33
    ## [11,] 117.5   41
    ## [12,] 122.5   36
    ## [13,] 127.5   35
    ## [14,] 132.5   17
    ## [15,] 137.5   13
    ## [16,] 142.5   12
    ## [17,] 147.5    8
    ## [18,] 152.5    3
    ## [19,] 157.5    1
    ## [20,] 162.5    0
    ## [21,] 167.5    0
    ## [22,] 172.5    1

``` {.sourceCode .r}
tab[tab[,1]==117.5,2]/sum(tab[,2])
```

    ## [1] 0.1490909

Op basis van de steekproef wordt die kans geschat op 14.9%.

Een histogram kan ook weergegeven worden a.d.h.v. relatieve frequenties/densiteiten.

``` {.sourceCode .r}
hist(nhanesSubHealthy$bpSys,xlab="Systolische Bloeddruk (mm kwik).",breaks=seq(65,175,5),freq=FALSE,ylab="Densiteit",cex.main=1.5,cex.axis=1.5,cex.lab=1.5,main="")
```

<span id="fig:nhanesNormalSteekproefRel"></span> <img src="Statistiek_2019_2020_files/figure-html/nhanesNormalSteekproefRel-1.png" style="width:100.0%" alt="Weergave van de verdeling voor de systolische bloeddruk van gezonde personen tussen 40-65 jaar geschat aan de hand van een histogram o.b.v. de geobserveerde steekproef in de NHANES studie. (Relatieve frequenties)" />

Figuur 2.4: Weergave van de verdeling voor de systolische bloeddruk van gezonde personen tussen 40-65 jaar geschat aan de hand van een histogram o.b.v. de geobserveerde steekproef in de NHANES studie. (Relatieve frequenties)

De oppervlakte in elke balk komt dan overeen met een kans: hoogte van de balk x breedte van de balk. In de histogrammen hebben we voor de breedte van de balk 5 mm Hg gekozen.

``` {.sourceCode .r}
tab2<-cbind(histAbs$mids,histAbs$density)
tab2
```

    ##        [,1]         [,2]
    ##  [1,]  67.5 0.0000000000
    ##  [2,]  72.5 0.0000000000
    ##  [3,]  77.5 0.0000000000
    ##  [4,]  82.5 0.0007272727
    ##  [5,]  87.5 0.0014545455
    ##  [6,]  92.5 0.0043636364
    ##  [7,]  97.5 0.0065454545
    ##  [8,] 102.5 0.0160000000
    ##  [9,] 107.5 0.0254545455
    ## [10,] 112.5 0.0240000000
    ## [11,] 117.5 0.0298181818
    ## [12,] 122.5 0.0261818182
    ## [13,] 127.5 0.0254545455
    ## [14,] 132.5 0.0123636364
    ## [15,] 137.5 0.0094545455
    ## [16,] 142.5 0.0087272727
    ## [17,] 147.5 0.0058181818
    ## [18,] 152.5 0.0021818182
    ## [19,] 157.5 0.0007272727
    ## [20,] 162.5 0.0000000000
    ## [21,] 167.5 0.0000000000
    ## [22,] 172.5 0.0007272727

``` {.sourceCode .r}
tab2[tab2[,1]==117.5,2]
```

    ## [1] 0.02981818

``` {.sourceCode .r}
tab2[tab2[,1]==117.5,2] * 5
```

    ## [1] 0.1490909

We bekomen opnieuw een schatting van 14.9%. We geven dat weer in een figuur, waarbij we de functie `rect()` gebruiken om de rechthoekige balk te tekenen. A.d.h.v. de functie `text()` kunnen we ook tekst toevoegen aan de figuur.

``` {.sourceCode .r}
hist(nhanesSubHealthy$bpSys,xlab="Systolische Bloeddruk (mm kwik).",breaks=seq(65,175,5),freq=FALSE,ylab="Densiteit",cex.main=1.5,cex.axis=1.5,cex.lab=1.5,main="")
rect(115,0,120, tab2[tab2[,1]==117.5,2],col=2)
text(120,tab2[tab2[,1]==117.5,2],paste0("P(115 < X < 120) = ",round(tab2[tab2[,1]==117.5,2] * 5 * 100, 1),"%"),col=2,cex=1,pos=4)
```

<span id="fig:nhanesNormalSteekproefRelProb"></span> <img src="Statistiek_2019_2020_files/figure-html/nhanesNormalSteekproefRelProb-1.png" style="width:100.0%" alt="Weergave van de verdeling voor de systolische bloeddruk van gezonde personen tussen 40-65 jaar geschat aan de hand van een histogram o.b.v. de geobserveerde steekproef in de NHANES studie. (Het histogram wordt weergegeven a.d.h.v. relatieve frequenties en de geschatte kans op een bloeddruk tussen 115-120 wordt aangeduid in het rood)" />

Figuur 2.5: Weergave van de verdeling voor de systolische bloeddruk van gezonde personen tussen 40-65 jaar geschat aan de hand van een histogram o.b.v. de geobserveerde steekproef in de NHANES studie. (Het histogram wordt weergegeven a.d.h.v. relatieve frequenties en de geschatte kans op een bloeddruk tussen 115-120 wordt aangeduid in het rood)

Als we de som van de oppervlakte van alle balken zouden berekenen is die uiteraard gelijk aan 1. De kans om een random persoon uit de steekproef aan te treffen tussen de laagste en hoogste waarde in de steekproef dient immers gelijk te zijn aan 1 of 100%!

Het histogram geeft verder weer dat de verdeling inderdaad vrij symmetrisch blijkt te zijn en een klokvorm lijkt te hebben. Als we kunnen veronderstellen dat de gegevens normaal verdeeld zijn dan kunnen we de verdeling in de populatie ook schatten door enkel het gemiddelde <span class="math inline">\$\\mu\$</span> en de variantie <span class="math inline">\$\\sigma^2\$</span> te *schatten* en de parameterschattingen in te pluggen in de Normale verdeling.

``` {.sourceCode .r}
hist(nhanesSubHealthy$bpSys,xlab="Systolische Bloeddruk (mm kwik).",breaks=seq(65,175,5),freq=FALSE,ylab="Densiteit",cex.main=1.5,cex.axis=1.5,cex.lab=1.5,main="")
lines(grid,dnorm(grid,mean=mean(nhanesSubHealthy$bpSys),sd=sd(nhanesSubHealthy$bpSys)),xlab="Systolische Bloeddruk (mm kwik)",ylab="Densiteit",type="l",lwd=2)
```

<span id="fig:nhanesNormalSteekproefEstimate"></span> <img src="Statistiek_2019_2020_files/figure-html/nhanesNormalSteekproefEstimate-1.png" style="width:100.0%" alt="Weergave van de verdeling voor de systolische bloeddruk van gezonde personen tussen 40-65 jaar geschat aan de hand van een histogram o.b.v. de geobserveerde steekproef in de NHANES studie en a.d.h.v. een normale verdeling met geschat gemiddelde 120.4 mm Hg en geschatte variantie 129.8 (zwarte volle lijn)" />

Figuur 2.6: Weergave van de verdeling voor de systolische bloeddruk van gezonde personen tussen 40-65 jaar geschat aan de hand van een histogram o.b.v. de geobserveerde steekproef in de NHANES studie en a.d.h.v. een normale verdeling met geschat gemiddelde 120.4 mm Hg en geschatte variantie 129.8 (zwarte volle lijn)

In plaats van kansen te berekenen door gebruik te maken van het histogram, bestaat een alternatieve methode erin om het gemiddelde en de variantie te schatten op basis van de steekproef. Vervolgens wordt dan de kans berekend a.d.h.v. een normale verdeling waarbij we als gemiddelde en variantie de overeenkomstige schattingen in de steekproef gebruiken.

We illustreren dit in R. De normale verdeling in R wordt geparameteriseerd a.d.h.v. het gemiddelde <span class="math inline">\$\\mu\$</span> en de standaard afwijking <span class="math inline">\$\\sigma\$</span>. Deze laatste kan direct worden geschat a.d.h.v. de steekproef door gebruik te maken van de steekproef standaard deviatie (functie `sd()`). De kans die we dan bekomen is

``` {.sourceCode .r}
xBar <- mean(nhanesSubHealthy$bpSys)
sBar <- sd(nhanesSubHealthy$bpSys)
pnorm(120,mean=xBar,sd=sBar)-pnorm(115,mean=xBar,sd=sBar)
```

    ## [1] 0.1397006

Merk op dat deze schatting veel dichter ligt bij de werkelijke kans in de populatie dan de schatting die we bekwamen d.m.v. het histogram. De schatting o.b.v. de normale verdeling is inderdaad nauwkeuriger: we kunnen immers gebruik maken van alle data om deze kans te schatten gezien we het steekproefgemiddelde en de steekproefstandaarddeviatie hebben geschat o.b.v. alle gegevens in de steekproef. Voor de kans berekend o.b.v. het histogram konden we daarentegen enkel de gegevens gebruiken van de personen uit de steekproef met een bloeddruk tussen 115 en 120 mmHg.
Uiteraard zal het in de praktijk steeds heel belangrijk zijn om na te gaan of er voldaan is aan de aannames die we maken over de verdeling. Anders zijn onze schattingen immers incorrect en niet bruikbaar. Het nagaan van veronderstellingen over de verdeling is één van de doelstellingen van data exploratie.

We kunnen nu op basis van de steekproef en de aannames van normaliteit een grenswaarde voor de bloeddruk afleiden die extreem is voor “gezonde” personen in de populatie. Dat laat ons bijvoorbeeld toe om een bloeddruk te bepalen die maar met een kans van 5% wordt overschreden in de populatie van gezonde subjecten: <span class="math display">\\\[P(X &gt; t\_\\text{drempel}) = 5\\%\\$$</span> of <span class="math display">\\$$P(X \\leq t\_\\text{drempel}) = 95\\%\\$$</span>

Dat kan met de functie `qnorm()` in R.

``` {.sourceCode .r}
qnorm(0.95,mean=xBar,sd=sBar)
```

    ## [1] 142.6011

Deze waarde ligt dicht bij 140 mmg Hg, een grenswaarde voor hypertensie die vaak in de literatuur wordt gebruikt.

---

[← 2.5 Steekproef](06-2-5-steekproef.md) · [Up: contents](index.md) · [2.7 Statistieken →](08-2-7-statistieken.md)

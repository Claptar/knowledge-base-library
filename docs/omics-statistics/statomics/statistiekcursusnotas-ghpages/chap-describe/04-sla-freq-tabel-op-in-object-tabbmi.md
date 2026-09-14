---
title: sla freq. tabel op in object 'tabBmi'
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-describe.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-describe.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# sla freq. tabel op in object 'tabBmi'

**Source:** [`chap-describe.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-describe.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

tabBmi <- table(NHANES$BMI_WHO)
tabBmi
```

    ##
    ##    12.0_18.5 18.5_to_24.9 25.0_to_29.9    30.0_plus
    ##         1277         2911         2664         2751

``` {.sourceCode .r}
#teken staaf diagram
barplot(tabBmi)
```

<span id="fig:freqmilt"></span> <img src="Statistiek_2019_2020_files/figure-html/freqmilt-1.png" style="width:100.0%" alt="Staafdiagram van het aantal personen in de NHANES studie die behoort tot elke BMI klasse." />

Figuur 4.3: Staafdiagram van het aantal personen in de NHANES studie die behoort tot elke BMI klasse.

Voor *numerieke continue variabelen* wordt het moeilijk om de frequentie van alle uitkomstwaarden in een tabel te klasseren omdat veel waarden hoogstens 1 keer voorkomen. Het *tak-en-blad diagram* (in het Engels: *stem and leaf plot* is een middel om toch nog alle uitkomsten weer te geven. Een voorbeeld is weergegeven in onderstaande R-output voor het BMI in de NHANES studie.

``` {.sourceCode .r}
stem(NHANES$BMI)
```

    ##
    ##   The decimal point is 1 digit(s) to the right of the |
    ##
    ##   1 | 33333333333333333344444444444444444444444444444444444444444444444444+37
    ##   1 | 55555555555555555555555555555555555555555555555555555555555555555555+1389
    ##   2 | 00000000000000000000000000000000000000000000000000000000000000000000+2264
    ##   2 | 55555555555555555555555555555555555555555555555555555555555555555555+2610
    ##   3 | 00000000000000000000000000000000000000000000000000000000000000000000+1693
    ##   3 | 55555555555555555555555555555555555555555555555555555555555555555555+635
    ##   4 | 00000000000000000000000000000000000000000000000000000000000000000000+255
    ##   4 | 55555555555555555555555556666666666666666666666666666666666777777777+46
    ##   5 | 0000011111122222233333444444444444
    ##   5 | 5556677777789999
    ##   6 | 133444
    ##   6 | 567899
    ##   7 |
    ##   7 |
    ##   8 | 111

Hier wordt van alle uitkomsten het eerste cijfer of de eerste paar cijfers op een verticale lijn in volgorde uitgezet in de vorm van een boomstam. Daaraan worden horizontaal de bladeren gehecht, met name de laatste cijfers van de geobserveerde uitkomsten. De output geeft bijvoorbeeld aan dat er 3 personen zijn waarvan het afgeronde BMI 55 bedraagt, 2 personen met een afgerond BMI van 56, …. Gezien de studie zo groot is, is het tak-en-blad diagram niet erg praktisch voor dit voorbeeld.

In een tak-en-blad diagram krijgt men alle individuele uitkomsten nagenoeg exact te zien, terwijl de vorm die het diagram aanneemt reeds een idee van de verdeling geeft zoals in een histogram (zie verder). Een vuistregel om de vorm van de verdeling het best te zien is het aantal takken ongeveer gelijk te maken aan <span class="math inline">\$1 + \\sqrt{n}\$</span>, waarbij <span class="math inline">\$n\$</span> het aantal observaties voorstelt. Dit aantal kan uiteraard aangepast worden aan de omstandigheden. Een populair alternatief voor het tak en blad diagram is de *eenvoudige frequentietabel*. Deze kan men bekomen door de continue variabele (bvb. BMI) om te zetten in een kwalitatieve ordinale variabele, waarvoor vervolgens een frequentietabel wordt weergegeven. Merk op dat dit voor het BMI eerst is gebeurd (Figuur [4.3](index.md)).

Het grafisch equivalent van dergelijke frequentietabel noemt een *histogram*, hetgeen men in R bekomt via

``` {.sourceCode .r}
hist(NHANES$BMI,main="",xlab="BMI") #main is hoofdtitel
```

<span id="fig:histo"></span> <img src="Statistiek_2019_2020_files/figure-html/histo-1.png" style="width:100.0%" alt="Histogram van het BMI in de NHANES studie." />

Figuur 4.4: Histogram van het BMI in de NHANES studie.

Wanneer alle klassen een zelfde breedte hebben, worden de absolute of relatieve frequenties per klasse weergegeven door de hoogte van de bijhorende kolom. Bij ongelijke klassebreedtes is het de oppervlakte van de kolom die met de bijhorende klassefrequentie correspondeert. Omdat een histogram met ongelijke klassebreedtes moeilijker te interpreteren is, zijn histogrammen met gelijke klassebreedtes vaak te verkiezen. Als histogrammen voor verschillende groepen bekeken worden, vergemakkelijkt het gebruik van *relatieve* frequenties i.p.v. absolute frequenties de visuele vergelijkbaarheid.

Op het histogram in Figuur [4.4](index.md) worden absolute frequenties weergegeven en klassen met een breedte van 5 eenheden. We stellen vast dat ongeveer 1500 personen van de 10000, of 15% een BMI heeft tussen de 15 en 20.

De keuze van het aantal klassen is van belang bij een histogram. Als er te weinig klassen zijn, dan gaat veel informatie verloren. Als er teveel zijn, dan wordt het algemene patroon verdoezeld door een grote hoeveelheid overbodige details. Gewoonlijk kiest men tussen 5 en 15 intervallen, maar de specifieke keuze hangt af van het beeld van het histogram dat men te zien krijgt.

Indien een voldoende aantal gegevens beschikbaar is, dan kan men een gladdere indruk van de verdeling van de gegevens bekomen door een zogenaamde *kernel density schatter* te bepalen. Zo’n schatter is een positieve functie die genormaliseerd is in die zin dat de oppervlakte onder de functie 1 is. Ze kan zo geïnterpreteerd worden dat de oppervlakte onder de functie tussen 2 punten <span class="math inline">\$a\$</span> en <span class="math inline">\$b\$</span> op de X-as, de kans voorstelt dat een lukrake meting in het interval <span class="math inline">\$$$a,b$$\$</span> gevonden wordt. Figuur [4.5](index.md) toont een histogram (links) en kernel density schatter (rechts) van de het BMI.

``` {.sourceCode .r}

---

[← op in object 'tab'](03-op-in-object-tab.md) · [Up: contents](index.md) · [deel grafische scherm op in 1 rij en 2 kolommen →](05-deel-grafische-scherm-op-in-1-rij-en-2-kolommen.md)

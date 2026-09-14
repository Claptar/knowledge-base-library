---
title: op in object 'tab'
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-describe.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-describe.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# op in object 'tab'

**Source:** [`chap-describe.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-describe.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

tab <- table(NHANES$Gender)
tab
```

    ##
    ## female   male
    ##   5020   4980

``` {.sourceCode .r}
barplot(tab) #teken staaf diagram
```

<span id="fig:fretabs"></span> <img src="Statistiek_2019_2020_files/figure-html/fretabs-1.png" style="width:100.0%" alt="Staafdiagram van het aantal mannen en vrouwen in de NHANES studie." />

Figuur 4.2: Staafdiagram van het aantal mannen en vrouwen in de NHANES studie.

Er zijn weinig methoden voorhanden om *nominale* variabelen te beschrijven. In Voorbeeld [4.1](index.md) is de variable *Gender* kwalitatief nominaal. Alles is gezegd over de verdeling van het geslacht als we weergeven hoeveel vrouwen en mannen zijn opgenomen in de studie. Meer nog, als het totale aantal personen in de data set eenmaal vast ligt, dan zijn de uitkomsten verder volledig gekarakteriseerd door, bijvoorbeeld, alleen het percentage vrouwen en mannen weergeen. In het softwarepakket R kan men een beeld van de gegevens krijgen door ze in een *frequentietabel* weer te geven of a.d.h.v. een grafiek zoals een *staafdiagram*. Beiden worden gegenereerd in de R-code voor Figuur [4.2](index.md). We stellen vast dat 5020 van de 10000 subjecten, ofwel 50.2% vrouwen in de studie zijn opgenomen.

Een staafdiagram geeft op de X-as de mogelijke uitkomsten van de variabele aan (bvb. geslacht). Daarbovenop komt een staaf met hoogte evenredig aan het totaal aantal keer dat die waarde voorkomt in de dataset. In het bijzonder kan men kiezen tussen de *absolute frequentie* (5020 voor het aantal vrouwen, 4980 voor het aantal mannen) of de *relatieve frequentie* ( 50.2% vrouwen, 49.8% mannen). De staven staan los van elkaar met een breedte die constant is, maar verder willekeurig. Als de steekproef representatief is voor de populatie, dan krijgen we hier misschien een eerste impressie dat er iets meer vrouwen zijn in de populatie.

De variabele met de naam *BMI\_WHO* in de dataset is kwalitatief ordinaal en heeft 4 geordende categorieën die grensen voor ondergewicht, normaal gewicht, licht-overgewicht, obesitas. Voor dergelijke ordinale variabelen worden de mogelijke uitkomsten best in volgorde gesorteerd en in een frequentietabel of staafdiagram weergegeven. Naast de (relatieve) frequentie is het nu ook zinvol om de *cumulatieve (relatieve) frequentie* aan te geven. Deze laatste drukt uit welk percentage van de gegevens in de gegeven klasse of een lagere klasse valt. In Figuur [4.3](index.md) vind je het staafdiagram voor het BMI. In de R-code voor de figuur vind je tevens de bijhorende frequentietabel.

``` {.sourceCode .r}

---

[← We slaan de frequentietabel voor variable Gender](02-we-slaan-de-frequentietabel-voor-variable-gender.md) · [Up: contents](index.md) · [sla freq. tabel op in object 'tabBmi' →](04-sla-freq-tabel-op-in-object-tabbmi.md)

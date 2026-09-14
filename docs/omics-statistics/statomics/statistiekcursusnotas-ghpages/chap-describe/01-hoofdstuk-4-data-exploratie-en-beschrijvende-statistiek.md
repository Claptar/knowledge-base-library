---
title: Hoofdstuk 4 Data exploratie en beschrijvende statistiek
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-describe.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-describe.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Hoofdstuk 4 Data exploratie en beschrijvende statistiek

**Source:** [`chap-describe.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-describe.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## <span class="header-section-number">4.1</span> Inleiding {#inleiding}

Om de resultaten van een experimentele of observationele studie te rapporteren, is het uiteraard niet mogelijk om per subject waarvoor gegegevens verzameld werden in de studie de bekomen gegevens neer te schrijven. Met de veelheid aanwezige informatie is het integendeel belangrijk de gegevens gericht samen te vatten en voor te stellen. Zelfs wanneer het duidelijk is welke analyse er moet uitgevoerd worden, moet er eerst een basisbeschrijving komen van de verzamelde gegevens. Dit zal mee helpen aangeven of er geen fouten zijn gemaakt tijdens het onderzoek of bij de registratie van gegevens. Eventuele anomalieën of zelfs fraude worden in deze fase opgespoord en tenslotte krijgt men een indruk of voldaan is aan de onderstellingen (bvb. de onderstelling dat de gegevens Normaal verdeeld zijn<a href="#fn13" id="fnref13" class="footnoteRef"><sup>13</sup></a>) die aan de grond liggen van de voorgestelde statistische analyses in de latere fase.

De eerste vraag die moet gesteld worden bij het benaderen van een echte data set is:

1.  Wat is de oorspronkelijke vraagstelling (geweest), waarom zijn deze gegevens verzameld?
2.  Hoe en onder welke omstandigheden zijn de subjecten gekozen en de variabelen gemeten? Hierbij stelt men meteen de vraag naar het design van de studie, alsook hoeveel subjecten werden aangezocht voor meetwaarden en hoeveel daar uiteindelijk echt van in de database zijn terecht gekomen (m.a.w. of gegevens die men gepland had te verzamelen, om een of andere reden toch niet bekomen werden). Bovendien laat dit toe om te evalueren of verschillende subjecten in de studie al dan niet meer verwant zijn dan andere subjecten en of de analyse hier rekening mee moet houden.
3.  Is er een specifieke numerieke code die een ontbrekend gegeven of ander type uitzondering voorstelt in plaats van een echte meetwaarde?

Als het vertrekpunt duidelijk is en alle variabelen goed beschreven zijn, kan men starten met een betekenisvolle exploratie van de gerealiseerde observaties.

<span id="fig:pop2Samp2PopDataExpl"></span> <img src="Statistiek_2019_2020_files/figure-html/pop2Samp2PopDataExpl-1.png" style="width:100.0%" alt="Verschillende stappen in een studie. In dit hoofdstuk ligt de focus op de data-exploratie en beschrijvende statistiek" />

Figuur 4.1: Verschillende stappen in een studie. In dit hoofdstuk ligt de focus op de data-exploratie en beschrijvende statistiek

Dit hoofdstuk zullen werken rond een centrale dataset: de NHANES studie.

<span id="exm:nhanesEx" class="example">**Voorbeeld 4.1 (NHANES studie)** </span>

De National Health and Nutrition Examination Survey (NHANES) wordt sinds 1960 op regelmatige basis of genomen. In dit voorbeeld maken we gebruik van de gegevens die werden verzameld tussen 2009-2012 bij 10000 Amerikanen en die werden opgenomen in het R-pakket NHANES. Er werd een groot aantal fysische, demografische, nutritionele, levelsstijl en gezondheidskarakteristieken gecollecteerd in deze studie (zie Tabel [4.1](index.md)). Merk op dat ontbrekende waarnemingen hier gecodeerd worden a.d.h.b. de code `NA` (Not Available / Missing Value)

`**Einde voorbeeld**`

|    ID | Gender | Age | Race1 | Weight | Height |   BMI | BPSysAve | TotChol | SmokeNow | Smoke100 |
|------:|:-------|----:|:------|-------:|-------:|------:|---------:|--------:|:---------|:---------|
| 51624 | male   |  34 | White |   87.4 |  164.7 | 32.22 |      113 |    3.49 | No       | Yes      |
| 51625 | male   |   4 | Other |   17.0 |  105.4 | 15.30 |       NA |      NA | NA       | NA       |
| 51630 | female |  49 | White |   86.7 |  168.4 | 30.57 |      112 |    6.70 | Yes      | Yes      |
| 51638 | male   |   9 | White |   29.8 |  133.1 | 16.82 |       86 |    4.86 | NA       | NA       |
| 51646 | male   |   8 | White |   35.2 |  130.6 | 20.64 |      107 |    4.09 | NA       | NA       |
| 51647 | female |  45 | White |   75.7 |  166.7 | 27.24 |      118 |    5.82 | NA       | No       |

<span id="tab:nhanesDatExpl">Tabel 4.1: </span>Overzicht van een aantal variabelen uit de NHANES studie.

## <span class="header-section-number">4.2</span> Univariate beschrijving van de variabelen {#univariate-beschrijving-van-de-variabelen}

In de regel begint men met een *univariate* inspectie: elke variabele wordt apart onderzocht. Het is absoluut aan te raden om hierbij eerst alle ruwe gegevens te bekijken door middel van grafieken (zie verder) alvorens naar samenvattingsmaten (zoals het gemiddelde) over te stappen. Dit laat toe om een idee te krijgen hoe de geobserveerde waarden van een veranderlijke verdeeld zijn in de studiegroep (bvb. welke verdeling de bloeddrukmetingen in de studie hebben) en of er eventuele *uitschieters* (d.i. extreme metingen of *outliers*) zijn. Met outliers worden observaties aangegeven die ten opzichte van de geobserveerde verdeling van de waarden in de data set, extreem zijn, buitenbeentjes.

``` {.sourceCode .r}
#De data van de NHANES studie bevindt zich
#in het R package NHANES
library(NHANES) #laad NHANES package

#NHANES is een data frame met de gegevens
#De rijen bevatten informatie over elk subject
#De kolommen de variabelen die werden geregistreerd
#vb variabele Gender, BMI, ...
#Een variabele (kolom) kan uit de dataframe
#worden gehaald door gebruik van het $ teken
#en de naam van de variabele

---

[Up: contents](index.md) · [We slaan de frequentietabel voor variable Gender →](02-we-slaan-de-frequentietabel-voor-variable-gender.md)

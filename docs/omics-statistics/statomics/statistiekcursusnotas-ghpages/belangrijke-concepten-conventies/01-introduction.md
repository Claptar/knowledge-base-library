---
title: Introduction
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/belangrijke-concepten-conventies.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/belangrijke-concepten-conventies.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Introduction

**Source:** [`belangrijke-concepten-conventies.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/belangrijke-concepten-conventies.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

# <span class="header-section-number">Hoofdstuk 2</span> Belangrijke concepten & conventies {#hoofdstuk-2-belangrijke-concepten-conventies}

De verschillende stappen in een studie worden geïllustreerd in Figuur [2.1](index.md). Eerst bepaalt de onderzoeker de *populatie* van interesse. Gezien het om financiële en logistieke beperkingen vrijwel nooit mogelijk is om de volledige populatie te onderzoeken zal men vervolgens een steekproef nemen uit de populatie. De manier waarop een steekproef zal worden genomen wordt vastgelegd in het *design van de studie*. *Proefopzet* of *studie design* is een aparte tak van de statisitiek en is een cruciaal onderdeel van een studie. Het studie design moet immers garanderen dat de gegevens en resultaten van de steekproef representatief zijn voor de populatie zodat de resultaten van de studie veralgemeneend kunnen worden naar de populatie toe. Vervolgens wordt de studie uitgevoerd, worden de gegevens verzameld en kan de eigenlijke data-analyse van start gaan. In een eerste fase is het belangrijk om de gegevens grondig te exploreren. *Data-exploratie en beschrijvende statistiek* is een tweede tak van de statistiek die toelaat om gegevens van de steekproef te visualiseren, samen te vatten en om inzicht in de data te verwerven. Dat is belangrijk om de data correct te kunnen modelleren en om aannames na te kunnen gaan die nodig zijn voor de verdere data analyse. Vervolgens zullen we hetgeen we observeren in de steekproef trachten te veralgemenen naar de algemene populatie toe, zodat we algemene conclusies kunnen trekken op populatie-niveau op basis van de steekproef van de studie. Hiervoor zijn methodes nodig van de *statistische besluitvorming*, ook wel *statistische inferentie* genoemd, een derde belangrijke tak van de statistiek.

<span id="fig:pop2Samp2Pop"></span> <img src="Statistiek_2019_2020_files/figure-html/pop2Samp2Pop-1.png" style="width:100.0%" alt="Verschillende stappen in een studie. (1) In de design fase/ proefopzet definieert de onderzoeker de populatie, bepaalt hij/zij op welke manier een steekproef zal worden genomen uit de populatie en hoe het experiment zal worden uitgevoerd. Ook het volledige data analyse plan moet in deze fase zijn vastgelegd. Vervolgens wordt het experiment uitgevoerd en worden de gegevens verzameld. (2) De gegevens worden vervolgens verkend en samengevat. Hierbij verwerft men inzicht in de gegevens en kunnen aannames worden nagegaan die noodzakelijk zijn voor de verdere data analyse stappen. (3) Tenslotte zal men hetgeen men observeert in de steekproef trachten te veralgemenen naar de populatie toe a.d.h.v. statistische inferentie." />

Figuur 2.1: Verschillende stappen in een studie. (1) In de design fase/ proefopzet definieert de onderzoeker de populatie, bepaalt hij/zij op welke manier een steekproef zal worden genomen uit de populatie en hoe het experiment zal worden uitgevoerd. Ook het volledige data analyse plan moet in deze fase zijn vastgelegd. Vervolgens wordt het experiment uitgevoerd en worden de gegevens verzameld. (2) De gegevens worden vervolgens verkend en samengevat. Hierbij verwerft men inzicht in de gegevens en kunnen aannames worden nagegaan die noodzakelijk zijn voor de verdere data analyse stappen. (3) Tenslotte zal men hetgeen men observeert in de steekproef trachten te veralgemenen naar de populatie toe a.d.h.v. statistische inferentie.

Vooraleer we dieper ingaan op studie-design, data-exploratie en statistische besluitvorming zullen we eerst enkele concepten introduceren. We doen dat in dit hoofdstuk aan de hand van de de NHANES studie.

<span id="exm:nhanesExConcepten" class="example">**Voorbeeld 2.1 (NHANES studie)** </span>

De National Health and Nutrition Examination Survey (NHANES) wordt sinds 1960 op regelmatige basis afgenomen. In dit voorbeeld maken we gebruik van de gegevens die werden verzameld tussen 2009-2012 bij 10000 Amerikanen en die werden opgenomen in het R-pakket NHANES. Er werd een groot aantal fysieke, demografische, nutritionele, levelsstijl en gezondheidskarakteristieken gecollecteerd in deze studie (zie Tabel [2.1](index.md)). `**Einde voorbeeld**`

|    ID | Gender | Age | Race1 | Weight | Height |   BMI | BPSysAve | TotChol | SmokeNow | Smoke100 |
|------:|:-------|----:|:------|-------:|-------:|------:|---------:|--------:|:---------|:---------|
| 51624 | male   |  34 | White |   87.4 |  164.7 | 32.22 |      113 |    3.49 | No       | Yes      |
| 51625 | male   |   4 | Other |   17.0 |  105.4 | 15.30 |       NA |      NA | NA       | NA       |
| 51630 | female |  49 | White |   86.7 |  168.4 | 30.57 |      112 |    6.70 | Yes      | Yes      |
| 51638 | male   |   9 | White |   29.8 |  133.1 | 16.82 |       86 |    4.86 | NA       | NA       |
| 51646 | male   |   8 | White |   35.2 |  130.6 | 20.64 |      107 |    4.09 | NA       | NA       |
| 51647 | female |  45 | White |   75.7 |  166.7 | 27.24 |      118 |    5.82 | NA       | No       |

<span id="tab:nhanesConcepten">Tabel 2.1: </span>Overzicht van een aantal variabelen uit de NHANES studie.

---

[Up: contents](index.md) · [2.1 Variabelen →](02-2-1-variabelen.md)

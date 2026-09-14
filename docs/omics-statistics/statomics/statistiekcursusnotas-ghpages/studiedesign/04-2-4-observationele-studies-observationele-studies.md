---
title: 2.4 Observationele studies {#observationele-studies}
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/studiedesign.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/studiedesign.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2.4 Observationele studies {#observationele-studies}

**Source:** [`studiedesign.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/studiedesign.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

Terwijl in een gecontroleerd experiment de onderzoeker zelf beslist welke subjecten een bepaalde interventie ondergaan, observeert men in een *observationele studie* verschillende subjecten die (mogelijks om zelfgekozen redenen) verschillende interventies hebben ondergaan en probeert men hier vervolgens het interventie-effect uit af te leiden. Bijvoorbeeld, om na te gaan wat het effect is van de aanwezigheid van de salamandersoort P. glutinosus op de groei van de populatie P. jordani zou men in een observationele studie verschillende studiegebieden vergelijken waar er om natuurlijke redenen al dan niet een populatie P. glutinosus aanwezig is. Dergelijke studies zijn wel gecontroleerd (omdat men studiegebieden met en zonder P. glutinosus vergelijkt), maar niet experimenteel (omdat de onderzoeker niet zelf beslist in welke studiegebieden de salamandersoort P. glutinosus aanwezig is). Inderdaad, in een experimentele studie zou men ingrijpen door in sommige studiegebieden de populatie P. glutinosus te verwijderen en in andere niet.

Het grote nadeel van observationele studies is dat verschillen in uitkomst tussen verschillende interventiegroepen niet gegarandeerd kunnen toegeschreven worden aan de blootstelling of interventie. Dit komt doordat deze groepen vaak in meer verschillen dan alleen hun blootstelling. Problemen van confounding zijn dus inherent aan observationele studies. Stel bijvoorbeeld dat men vaststelt dat de populatie P. jordani *sneller groeit* in gebieden met dan zonder P. glutinosus. Dan kunnen we besluiten dat er een associatie of verband is tussen de aanwezigheid van P. glutinosus en de populatiegroei van P. jordani. Maar dat op zich bewijst niet dat het toevoegen van de salamandersoort P. glutinosus in gebieden waar ze niet aanwezig is, een gunstig effect zal hebben op de populatiegrootte van P. jordani (d.i. dat het toevoegen van P. glutinosus een *causaal effect* op P. jordani heeft). Er kunnen immers verborgen confounders zijn: zo zou het kunnen dat men meer kans heeft om P. glutinosus aan te treffen in voedselrijke gebieden, waar de populatie P. jordani ook makkelijker zal toenemen omwille van de aanwezigheid van voedsel (maar niet omwille van de aanwezigheid van P. glutinosus). De rijkdom aan voedsel is in dit geval een confounder omdat (in overeenkomst met de eerdere definitie voor confounders) zowel de aanwezigheid van P. glutinosus als de groei van P. jordani geassocieerd zijn met de rijkdom aan voedsel, maar geen van beiden de rijkdom aan voedsel beïnvloeden.

Omwille van confounders is het belangrijk in observationele studies om bij de subjecten waarvoor metingen verzameld worden, zorgvuldig prognostische factoren voor de bestudeerde uitkomst te meten die mogelijks ook met de blootstelling geassocieerd zijn. Voor die confounders die gemeten zijn, kan men immers corrigeren in de statistische analyse. Bijvoorbeeld, om de vergelijking van gebieden met en zonder P. glutonisus te corrigeren voor de confounder voedselrijkdom, kan men proberen een index te verzamelen voor de voedselrijkdom van elk gebied en vervolgens de analyse afzonderlijk uitvoeren bij gebieden met dezelfde voedselrijkdom. Men zegt dan dat de analyse of het geschatte effect van P. glutonisus op de groei van P. jordani *gecontroleerd* (in het Engels: *adjusted* of *controlled*) werd voor de voedselrijkdom van het studiegebied.

<span id="exm:unnamed-chunk-20" class="example">**Voorbeeld 2.12 (Simpson’s paradox)** </span>

De Universiteit van Californië, Berkeley voerde verschillende jaren terug een observationele studie uit om na te gaan of er geslachtsdiscriminatie was bij de toelatingsexamens. Gedurende de studieperiode namen 8442 jongens en 4321 meisjes deel aan het examen. Ongeveer 44% van de jongens en 35% van de meisjes werd toegelaten tot de universiteit. Ervan uit gaande dat jongens en meisjes even capabel zijn om voor het examen te slagen (er is immers geen bewijs van het tegendeel), krijgen we hier de indruk dat jongens en meisjes anders behandeld worden bij de toelatingsprocedure.

Omdat de toelatingsexamens verschillend waren naargelang de studierichting, werd bovenstaande analyse per studierichting opgesplitst om na te gaan welke faculteiten verantwoordelijk waren voor mogelijke discriminatie. De resultaten voor de 6 grootste richtingen staan in Tabel [2.3](index.md) getabuleerd (resultaten voor de andere richtingen waren analoog). In alle studierichtingen ligt het slaagpercentage hoger bij de meisjes dan bij de jongens, behalve in richting E waar de jongens het lichtjes beter doen. Dit lijkt paradoxaal, wetende dat het algemene slaagpercentage voor de jongens dat van de meisjes ruim overstijgt. Hoe kunnen we dit verklaren?

De verklaring is dat de moeilijkheidsgraad van de studierichting (en verwant hiermee de keuze van studierichting) een confounder is voor de associatie tussen geslacht en de slaagkans. Immers, zoals blijkt uit Tabel [2.3](index.md) hebben jongens meer de neiging om studierichtingen te kiezen waar de slaagkansen hoog zijn: meer dan 50% van de jongens schreven zich in voor studierichtingen A en B, waar de slaagkansen hoger waren dan 50%; meer dan 90% van de meisjes kandideerde voor de andere studierichtingen die veel zwaardere toelatingsexamens hadden.

De vergelijking van de slaagkansen per studierichting in Tabel [2.3](index.md) levert een analyse op die gecontroleerd is voor de keuze van studierichting. Na deze controle blijkt relatief weinig verschil in slaagkansen tussen jongens en meisjes. De statistische les is dat relaties tussen percentages kunnen omkeren naarmate men ze al dan niet in subgroepen bekijkt. Dit noemt men *Simpson’s paradox*.

|     | Jongens(aantal) | Jongens(geslaagd %) | Meisjes(aantal) | Meisjes (geslaagd %) |
|:----|----------------:|--------------------:|----------------:|---------------------:|
| A   |             825 |                  62 |             108 |                   82 |
| B   |             560 |                  63 |              25 |                   68 |
| C   |             325 |                  37 |             593 |                   34 |
| D   |             417 |                  33 |             375 |                   35 |
| E   |             191 |                  28 |             393 |                   24 |
| F   |             373 |                   6 |             341 |                    7 |

<span id="tab:sexbias">Tabel 2.3: </span>Resultaten van de toelatingsexamens volgens geslacht en studierichting.

`**Einde voorbeeld**`

<span id="exm:unnamed-chunk-21" class="example">**Voorbeeld 2.13 (Confounders in de NHANES studie)** </span>

De National Health and Nutrition Examination Survey (NHANES 1) is een studie naar gezondheids- en voedingsgewoontes bij 7188 vrouwen tussen 25 en 74 jaar die opgevolgd werden van 1971 tot 1975 en van 1981 tot 1984 (Schatzkin et al., 1987). De onderzoekers vonden een positieve associatie tussen alcoholconsumptie en borstkanker (d.w.z. een hogere kans op borstkanker bij hogere consumptiegraad). Een grote vraag in deze studie was of deze associatie werkelijk het gevolg was van alcoholconsumptie of het gevolg van een mogelijks groot aantal andere factoren die met alcohol consumptie geassocieerd zijn. Het zou bijvoorbeeld kunnen dat vrouwen die meer alcohol verbruiken ook meer roken en om die reden gemakkelijker borstkanker ontwikkelen. In dat geval kan men door de storende invloed van roken mogelijks waarnemen dat het risico op borstkanker toeneemt met stijgend alcoholverbruik, zelfs wanneer in werkelijkheid het alcoholverbruik geen (causaal) effect heeft op borstkanker. Roken is in dat geval een confounder omdat het hogere risico op borstkanker voor alcoholverbruikers dan niet (alleen) het gevolg is van hun alcoholverbruik, maar (ook of vooral) van hun rookgedrag.

Om de invloed van roken op de associatie tussen borstkanker en alcoholconsumptie te doen verdwijnen, heeft men de statistische analyse uitgevoerd bij vrouwen met hetzelfde rookgedrag. Immers, door de analyse te beperken tot vrouwen met hetzelfde rookgedrag, zijn de groepen vrouwen die wel versus niet alcohol consumeren, beter vergelijkbaar en is er dus niet langer een storende invloed van roken. Men zegt in dat geval dat men in de analyse gecorrigeerd (in het Engels: adjusted) heeft voor het rookgedrag, waarmee men bedoelt dat men het effect van alcohol op borstkanker heeft voorgesteld voor vrouwen met hetzelfde rookgedrag. In deze studie vond men dat er na correctie voor roken een associatie bleef bestaan tussen alcoholverbruik en borstkanker. Men besloot dat alcoholconsumptie een verhoogd risico op borstkanker impliceert.

`**Einde voorbeeld**`

Goede analyses van observationele studies controleren voor confounders. In de praktijk is het echter zeer moeilijk om alle mogelijke confounders te kennen voor de associatie tussen een blootstelling en een respons. En zelfs wanneer men ze zou kennen, is het vaak onmogelijk om ze allen te meten. Om die reden zijn de resultaten van observationele studies doorgaans minder betrouwbaar dan de resultaten van gerandomiseerd gecontroleerde experimenten. Niettemin zijn observationele studies krachtig en belangrijk omdat het in vele situaties onmogelijk is om een gerandomiseerd experiment uit te voeren. Zo is het praktisch quasi niet mogelijk om een gerandomiseerde experiment uit te voeren naar het effect van bosbranden op de rijkdom aan ongewervelde dieren in de grond omdat vuur moeilijk te manipuleren valt. Hoewel de onderzoeker in bepaalde studiegebieden brandhaarden kan aanbrengen, bestaat immers steeds het risico dat de brand uit de hand loopt. Om die reden bestudeert men vaak gebieden waar op natuurlijke wijze of door brandstichters brand is ontstaan. Hoewel dergelijke studie typisch te kampen hebben met problemen van confounding, hebben observationele studies, mits correctie voor gemeten confounders, in het verleden heel wat nuttige en correctie informatie gebracht, zoals de boodschap dat roken longkanker veroorzaakt (Doll & Hill, 1964).

<span id="exm:unnamed-chunk-22" class="example">**Voorbeeld 2.14 (Observationele versus gerandomiseerde studies)** </span>

Foetussen kunnen in de baarmoeder onderzocht worden via echografie. Verschillende experimenten op dieren hebben aangetoond dat dergelijk onderzoek kan leiden tot laag geboortegewicht. Om na te gaan of dat ook zo is bij mensen werd verschillende jaren terug een observationele studie opgezet in het Johns Hopkins ziekenhuis, Baltimore. Na correctie voor een aantal confounders stelden de onderzoekers vast dat baby’s die via echografie onderzocht werden in de baarmoeder gemiddeld een lager geboortegewicht hadden dan baby’s die niet blootgesteld werden aan echografie. Kunnen we hieruit besluiten dat echografie leidt tot lager geboortegewicht?

Het antwoord is nee. We kunnen dit niet zomaar besluiten omdat de baby’s die blootgesteld waren aan echografie mogelijks niet vergelijkbaar waren met de andere baby’s in de studie. Om een duidelijk antwoord te vinden, werd later een gerandomiseerd gecontroleerde studie uitgevoerd. Deze toonde een matig beschermend effect van echografie aan! De reden dat de observationele studie hier een andere conclusie opleverde, is omdat echografie ten tijde van deze studie vooral werd toegepast bij probleemzwangerschappen. Om die reden waren de baby’s die in de observationele studie waren blootgesteld aan echografie doorgaans a priori minder gezond dan de andere baby’s. Of het al dan niet om een probleemzwangerschap ging, was dus een confounder voor de associatie tussen geboortegewicht en blootstelling aan echografie.

`**Einde voorbeeld**`

---

[← 2.3 Experimentele studies](03-2-3-experimentele-studies.md) · [Up: contents](index.md) · [2.5 Prospectieve studies {#prospectieve-studies} →](05-2-5-prospectieve-studies-prospectieve-studies.md)

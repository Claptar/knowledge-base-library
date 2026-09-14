---
title: 5.9 Equivalentie-intervallen
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-besluit.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 5.9 Equivalentie-intervallen

**Source:** [`chap-besluit.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

Betrouwbaarheidsintervallen kunnen ook worden gebruikt om na te gaan of twee interventies **wetenschappelijk equivalent** zijn. Twee interventies worden **wetenschappelijk equivalent** genoemd als het verschil tussen de populatiegemiddelden <span class="math inline">\$\\mu\_1\$</span> en <span class="math inline">\$\\mu\_2\$</span> van hun uitkomsten <span class="math inline">\$X\_1\$</span> en <span class="math inline">\$X\_2\$</span> in een equivalentie-interval ligt (dat 0 zal omvatten), bijvoorbeeld: <span class="math display">\\$$\\begin{equation\*} (\\mu\_1 - \\mu\_2) \\in \[E\_1, E\_2$$ \\end{equation\*}\\\]</span> In de meeste gevallen worden <span class="math inline">\$E\_1\$</span> en <span class="math inline">\$E\_2\$</span> symmetrisch rond nul gekozen, in welk geval <span class="math inline">\$E\_1=-\\Delta\$</span> en <span class="math inline">\$E\_2=\\Delta\$</span> voor gegeven <span class="math inline">\$\\Delta\$</span>. Het (wetenschappelijk) equivalentie-interval wordt dan gegeven door alle koppels <span class="math inline">\$(\\mu\_1,\\mu\_2)\$</span> waarvoor <span class="math display">\\$$\\begin{equation\*} \|\\mu\_1 - \\mu\_2\| &lt; \\Delta \\end{equation\*}\\$$</span>

Twee interventies zijn met andere woorden klinisch equivalent wanneer hun verschil in effect verwaarloosbaar klein is vanuit wetenschappelijk oogpunt.

In het vervolg van deze sectie zullen we nagaan of de gemiddelden van 2 onafhankelijke populaties wetenschappelijk equivalent zijn (of wetenschappelijk niet significant van elkaar verschillen). Een eerste stap in dit proces is om op basis van louter wetenschappelijk overwegingen een interval op te stellen waarbinnen het verschil <span class="math inline">\$\\mu\_1-\\mu\_2\$</span> verwaarloosbaar klein kan worden genoemd. Dit gebeurt met hulp van een deskundige die kan oordelen over het belang van een gegeven effectgrootte. Vervolgens wordt het gemiddeld verschil in uitkomst onder beide interventies geschat op basis van de gegevens. Nagaan of dit verschil in het equivalentie-interval gelegen is, volstaat op zich niet om wetenschappelijke equivalentie te kunnen besluiten vermits een klein/groot verschil louter het gevolg kan zijn van biologische variatie. Een logische stap is daarom een bijhorend 95% betrouwbaarheidsinterval voor <span class="math inline">\$\\mu\_1 - \\mu\_2\$</span> te berekenen op basis van de beschikbare gegevens (gepaard, ongepaard, …). De wetenschappelijke equivalentie zal nu bepaald worden door de ligging van het betrouwbaarheidsinterval te vergelijken met het interval van wetenschappelijke equivalentie.

Het zou verkeerd zijn om wetenschappelijke equivalentie te besluiten zodra het equivalentie-interval volledig omsloten is door het 95% betrouwbaarheidsinterval. Inderdaad, kleine steekproeven produceren brede betrouwbaarheidsintervallen zodat men op die manier in kleine steekproeven gemakkelijk equivalentie zou besluiten louter wegens gebrek aan informatie. We volgen daarom de volgende strategie. Noem <span class="math inline">\$O\$</span> de ondergrens en <span class="math inline">\$B\$</span> de bovengrens van het 95% betrouwbaarheidsinterval voor <span class="math inline">\$\\mu\_1-\\mu\_2\$</span>.

1.  Als <span class="math inline">\$E\_1 &lt; O &lt; B &lt; E\_2\$</span>, dan is het verschil tussen de populatiegemiddelden met minstens 95% kans binnen de grenzen van wetenschappelijke equivalentie gelegen. Men kan dan met minstens 95% zekerheid besluiten dat de 2 interventies inderdaad wetenschappelijk equivalent zijn.

2.  Als <span class="math inline">\$E\_2 &lt; O\$</span> dan kan men met minstens 95% zekerheid besluiten dat <span class="math inline">\$\\mu\_1\$</span> wetenschappelijk significant groter is dan <span class="math inline">\$\\mu\_2\$</span>. (In dit geval is <span class="math inline">\$\\mu\_1\$</span> automatisch ook statistisch significant groter dan <span class="math inline">\$\\mu\_2\$</span> op het 2-zijdig significantieniveau 5%).

3.  Als <span class="math inline">\$B &lt; E\_1\$</span> dan kan men met minstens 95% zekerheid besluiten dat <span class="math inline">\$\\mu\_1\$</span> wetenschappelijk significant kleiner is dan <span class="math inline">\$\\mu\_2.\$</span>

Het resultaat kan ook minder duidelijk zijn.

1.  Als <span class="math inline">\$O &lt; E\_1 &lt; E\_2 &lt; B\$</span> dan is er te weinig informatie om ook maar iets betekenisvol te kunnen besluiten: meer gegevens zijn nodig.
2.  Als \$O &lt; E\_1 &lt; B &lt; E\_2 \$ dan kan men op het 5% significantieniveau besluiten dat <span class="math inline">\$\\mu\_1\$</span> *niet* wetenschappelijk groter is dan <span class="math inline">\$\\mu\_2\$</span>. In dat geval zijn zowel de opties wetenschappelijk equivalent met <span class="math inline">\$\\mu\_2\$</span> als wetenschappelijk significant kleiner dan <span class="math inline">\$\\mu\_2\$</span> niet uit te sluiten met 95% zekerheid.
3.  Analoog voor de symmetrische situatie waarbij <span class="math inline">\$E\_1 &lt; O &lt; E\_2 &lt; B.\$</span>

In asthmastudies legt men bijvoorbeeld **op voorhand vast** dat een verschil in Peak Expiratory Flow (PEF) van 15 l/min klinisch onbelangrijk is. Men bepaald m.a.w. een equivalentie-interval: $$-15,15$$ l/min. Een 95% BI van $$-10,-5$$ l/min voor gemiddeld verschil in PEF tussen twee geneesmiddelen Formoterol en Salbutamol wijst op een onbelangrijk effect, equivalentie. Het betrouwbaarheidsinterval geeft weer hoe groot het verschil kan zijn. Als men een BI van $$-25,-16$$ l/min had bekomen dan kon men besluiten dat het geneesmiddel Formoterol minder efficient is gezien het gemiddeld gezien PEF waarden oplevert die wetenschappelijk significant lager zijn dan wanneer Salbutamol wordt toegediend. Als het $$-20,-5$$ l/min zou zijn, dan is er ambiguïteit.

------------------------------------------------------------------------

1.  Ook wel Statistische Inferentie genoemd[↩](index.md)

2.  Om die reden duiden we ze aan met een hoofdletter.[↩](index.md)

3.  Zo is het met 1 observatie voor <span class="math inline">\$\\bar X\$</span> niet mogelijk om een histogram voor <span class="math inline">\$\\bar X\$</span> uit te zetten.[↩](index.md)

4.  In principe is een meer theoretische, mathematische ontwikkeling nodig omdit aan te tonen, maar voor het bestek van deze cursus volstaat het om het meer intuïtieve argument aan te nemen.[↩](index.md)

5.  Merk op dat de vierkantswortel van een som niet gelijk is aan de som van de vierkantswortels. Bijgevolg is de standaarddeviatie van de som van <span class="math inline">\$X\$</span> en <span class="math inline">\$Y\$</span> niet de som van de corresponderende standaarddeviaties\![↩](https://raw.githubusercontent.com/statOmics/statistiekCursusNotas/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html)

6.  Denk zelf maar eens na of je gevallen kunt bedenken waar je al op voorhand, zonder ook maar observaties te zien, de variantie op een bepaalde karakteristiek kent…[↩](index.md)

7.  95.1% is niet exact gelijk aan het nominale 95% omdat er ‘slechts’ 1000 simulaties gelopen zijn[↩](index.md)

8.  De steekproefstandaarddeviatie is eveneens een toevallig veranderlijke die van steekproef tot steekproef varieert rond werkelijke standaarddeviatie. Hierdoor zal de breedte van de intervallen eveneens variëren[↩](index.md)

9.  independent and identically distributed, onafhankelijk en gelijk verdeeld[↩](index.md)

10. vandaar de index 0 bij <span class="math inline">\$\\mu\_0\$</span>[↩](index.md)

11. distributie van de teststatistiek onder de nulhypothese[↩](index.md)

12. meer extreem in de richting van <span class="math inline">\$H\_1\$</span>[↩](index.md)

13. In de frequentistische theorie die we hier volgen, is de nulhypothese immers ofwel altijd waar, ofwel altijd vals, en is het dus zelfs niet mogelijk om de kans te definiëren dat de nulhypothese waar is. Teminste, die kans is ofwel 1 ofwel 0.\![↩](https://raw.githubusercontent.com/statOmics/statistiekCursusNotas/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html)

14. We hebben <span class="math inline">\$n\_1+n\_2\$</span> observaties (vrijheidsgraden) in het experiment, om de gepoolde variantie te schatten hebben we echter 2 vrijheidsgraden verloren aangezien we eerst het gemiddelde in elke groep dienden te bepalen om de variantie te kunnen schatten.[↩](index.md)

15. Merk op dat we de richting “significant hoger is in de transplantatie groep” afleiden uit de groepsgemiddelden in de output en/of het BI[↩](index.md)

---

[← 5.8 Wat rapporteren?](08-5-8-wat-rapporteren.md) · [Up: contents](index.md)

---
title: 5.8 Wat rapporteren?
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-besluit.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 5.8 Wat rapporteren?

**Source:** [`chap-besluit.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

- In de wetenschappelijke literatuur is er een overdreven aandacht voor p-waarden.
- Nochtans is het interessanter om een schatting te rapporteren samen met een betrouwbaarheidsinterval (dan met een p-waarde).

**Vuistregel**: Rapporteer een schatting steeds samen met een betrouwbaarheidsinterval (en een p-waarde), want

1.  Het resultaat van een toets kan veelal uit een betrouwbaarheidsinterval worden afgeleid;
2.  Dit laat toe om te oordelen of het resultaat ook **wetenschappelijk van belang** is.

### <span class="header-section-number">5.8.1</span> Reden 1: Relatie toetsen en betrouwbaarheidsintervallen

Stel dat we voor een zekere parameter <span class="math inline">\$\\theta\$</span> (bvb. een populatiegemiddelde, verschil in populatiegemiddelden, odds ratio, regressieparameter) de nulhypothese wensen te toetsen dat <span class="math inline">\$H\_0 : \\theta= \\theta\_0\$</span> versus het alternatief <span class="math inline">\$H\_A : \\theta \\neq \\theta\_0\$</span> voor een zeker getal <span class="math inline">\$\\theta\_0\$</span>. Dan kan men aantonen dat men deze tweezijdige toetsingsprocedure kan uitvoeren op het <span class="math inline">\$\\alpha 100\\%\$</span> significantieniveau door de nulhypothese te verwerpen als en slechts als het <span class="math inline">\$(1-\\alpha)100\\%\$</span> betrouwbaarheidsinterval voor <span class="math inline">\$\\theta\$</span> het getal <span class="math inline">\$\\theta\_0\$</span> niet omvat. Met andere woorden, het <span class="math inline">\$(1-\\alpha)100\\%\$</span> betrouwbaarheidsinterval voor <span class="math inline">\$\\theta\$</span> bevat alle getallen <span class="math inline">\$\\theta\_0\$</span> zodat de tweezijdige toets van <span class="math inline">\$H\_0 : \\theta= \\theta\_0\$</span> versus <span class="math inline">\$H\_1 : \\theta \\neq \\theta\_0\$</span> de nulhypothese niet verwerpt.

### <span class="header-section-number">5.8.2</span> Reden 2: Statistische significantie versus wetenschappelijke relevantie

Een betrouwbaarheidsinterval laat toe om zowel statistische significantie als wetenschappelijk belang van een resultaat te interpreteren.

Stel dat experimentele behandeling *significant betere* respons oplevert dan standaard/placebo. Een associatie is *statistisch significant* als P <span class="math inline">\$&lt; \\alpha\$</span>, de data dragen m.a.w. voldoende bewijskracht om te besluiten dat er een associatie is. Dan blijft het mogelijk dat het effect *wetenschappelijk irrelevant* is. Met betrouwbaarheidsintervallen kunnen we dit wel evalueren.

Maar, dat laat echter nog veel subjectiviteit en manipulatie toe. Onderzoekers hopen in de praktijk immers wetenschappelijk belangrijke vondsten te maken en kunnen daarom geneigd zijn om hun oordeel over wat wetenschappelijk belangrijk is, wijzigen in functie van het bekomen betrouwbaarheidsinterval. Om dit te vermijden is het wenselijk dat wetenschappers a priori, d.i. vooraleer de gegevens verzameld werden, hun oordeel over wetenschappelijke relevantie uitdrukken.

---

[← 5.7 Aannames](07-5-7-aannames.md) · [Up: contents](index.md) · [5.9 Equivalentie-intervallen →](09-5-9-equivalentie-intervallen.md)

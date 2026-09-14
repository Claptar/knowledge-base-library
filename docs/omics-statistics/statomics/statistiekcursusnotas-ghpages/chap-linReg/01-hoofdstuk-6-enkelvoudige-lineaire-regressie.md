---
title: Hoofdstuk 6 Enkelvoudige lineaire regressie
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-linReg.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-linReg.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Hoofdstuk 6 Enkelvoudige lineaire regressie

**Source:** [`chap-linReg.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-linReg.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## <span class="header-section-number">6.1</span> Inleiding {#inleiding}

### <span class="header-section-number">6.1.1</span> Borstkanker dataset

<span class="citation">Sotiriou et al. (2006)</span> publiceerden onderzoek naar de moleculaire basis van borstkanker. In de studie hebben de onderzoekers voor een groot aantal borstkanker patiënten klinische variabelen geregistreerd alsook de genexpressie in tumor weefsel gemeten voor duizenden genen m.b.v. microarray technologie. De genexpressie werd gemeten op de tumor biopsie die werd genomen voordat de behandeling werd gestart. De studie is een retrospectieve studie in de zin dat niet werd geëxperimenteerd en dat de genexpressie werd geëvalueerd als gevolg van de blootstelling die de individuen hebben ondergaan in het verleden.

In dit hoofdstuk zullen we een subset van de data gebruiken om de associatie te bestuderen tussen de genexpressie van twee sleutelgenen bij borstkanker: de estrogeen receptor 1 (ESR1) gen, een belangrijke biomerker voor de prognose van de patiënt, en het S100A8 gen dat een prominente rol speelt in de regulatie van inflammatie en immuun respons.

De data is opgeslagen in een tekst bestand met naam `borstkanker.txt` in de folder dataset.

``` {.sourceCode .r}

---

[Up: contents](index.md) · [we lezen de data in en slaan die op in het object →](02-we-lezen-de-data-in-en-slaan-die-op-in-het-object.md)

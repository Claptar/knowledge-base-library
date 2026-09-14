---
title: 11.1 Inleiding {#inleiding}
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-modsel.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-modsel.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 11.1 Inleiding {#inleiding}

**Source:** [`chap-modsel.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-modsel.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

In de prostaatkanker dataset (Sectie [10.1.1](../chap-glm/index.md)) zijn veel predictoren aanwezig. Automatische selectieprocedures kunnen behulpzaam zijn als het doel van het regressiemodel erin bestaat om (1) de uitkomst op basis van de predictoren te voorspellen; of (2) associaties tussen de uitkomst en predictoren te beschrijven. Net zoals in vele andere aspecten van de statistiek, zullen we een geobserveerde dataset (steekproef) gebruiken om tot een resultaat te komen (hier: een model) dat ruimer toepasbaar is dan enkel op de geobserveerde data. Het geselecteerde model moet toepasbaar zijn op de ruimere populatie waaruit de steekproefdata bekomen is en waarop de onderzoeksvraag van toepassing is.

Modelselectie kan dan omschreven worden als een methode voor het selecteren van een model dat best geschikt is voor het beantwoorden van de onderzoeksvraag. In dit hoofdstuk beperken we ons tot meervoudige lineaire regressiemodellen waarin sommige van de <span class="math inline">\$p-1\$</span> effecttermen mogelijks interactietermen voorstellen. Het totaal aantal mogelijke modellen is dan (zonder hiërarchie-restrictie) <span class="math inline">\$2^{p-1}\$</span> (ieder van de <span class="math inline">\$p-1\$</span> termen kan opgenomen worden in het model, of niet).

We onderscheiden de volgende algemene procedures:

1.  Alle mogelijke modellen worden geëvalueerd. Deze methode zal enkel haalbaar blijken als het aantal kandidaat modellen niet te groot is.

2.  Niet alle modellen worden geëvalueerd (stapsgewijze procedures): De methode wordt geïnitialiseerd met een model. D.m.v. een regel en een evaluatiecriterium wordt het pad doorheen de modelruimte bepaald.

Merk op dat we hiërarchisch moeten modelleren als we interactietermen toelaten. Een interactieterm mag nooit in het model voorkomen zonder de lagere orde termen.

---

[Up: contents](index.md) · [11.2 Modelselectie op basis van hypothesetesten →](02-11-2-modelselectie-op-basis-van-hypothesetesten.md)

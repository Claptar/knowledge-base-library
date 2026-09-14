---
title: 5.7 Aannames
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-besluit.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 5.7 Aannames

**Source:** [`chap-besluit.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

In de voorgaande secties hebben we t-testen geïntroduceerd en de geldigheid ervan hangt af van enkele distributionele veronderstellingen:

- Onafhankelijke gegevens (design)
- One-sample t-test: normaliteit van de steekproefobservaties
- Paired t-test: normaliteit van de verschillen tussen de gepaarde observaties
- Two-sample t-test: normaliteit van de steekproefobservaties in beide groepen, en gelijkheid van varianties.

Indien niet voldaan is aan de veronderstellingen, is de t-distributie niet noodzakelijk de correcte nuldistributie, en bijgevolg is er geen garantie dat de p-waarde en kritieke waarden correct zijn.

Ook voor de constructie van het betrouwbaarheidsinterval van het gemiddelde hebben we beroep gedaan op de veronderstelling van normaliteit. De normaliteitsveronderstelling was nodig om kwantielen uit de t-verdeling te kunnen gebruiken bij het opstellen van de boven- en ondergrens, en de correcte probabiliteitsinterpretatie van het betrouwbaarheidsinterval hangt hiervan af.

### <span class="header-section-number">5.7.1</span> Nagaan van de veronderstelling van Normaliteit

Normaliteit kan via de volgende methoden nagegaan worden.

**Boxplots en histogrammen**

Beide figuren laten toe om een idee te vormen over de vorm van de distributie: symmetrie, outliers.

**QQ-plots**

Deze plots laten toe om op een grafische wijze na te gaan in welke mate steekproefobservaties zich gedragen als een vooropgestelde distributie.

**Hypothesetesten (goodness-of-fit test)**

Goodness-of-fit testen zijn statistische hypothesetesten die ontwikkeld zijn voor het testen van de nulhypothese dat de steekproefobservaties uit een vooropgestelde distributie getrokken zijn (hier: normale distributie). De alternatieve hypothese is meestal de negatie van de nulhypothese (hier: geen normaliteit). Bekende testen zijn: Kolmogorov-Smirnov, Shapiro-Wilk en Anderson-Darling.

Op het eerste zicht lijkt een goodness-of-fit test een gemakkelijke en zinvolle oplossing. De methode geeft een <span class="math inline">\$p\$</span>-waarde en deze laat onmiddellijk toe om te besluiten of de data normaal verdeeld zijn.

Er is echter kritiek te leveren op deze aanpak:

- indien <span class="math inline">\$p\\geq \\alpha\$</span>, dan is normaliteit niet bewezen! Het zegt enkel dat er onvoldoende evidentie is tegen de veronderstelling van normaliteit. In een kleine steekproef is de kracht van een test meestal klein.
- indien <span class="math inline">\$p&lt;\\alpha\$</span>, dan mag wel besloten worden om de nulhypothese te verwerpen en mag dus besloten worden dat de data niet normaal verdeeld zijn, maar soms is een afwijking van normaliteit niet zo erg.

**Algemeen advies**: Start met een grafische exploratie van de data (boxplots, histogrammen en QQ-plots) en houdt hierbij steeds de steekproefgrootte in het achterhoofd om te vermijden dat je de figuren zou overinterpreteren. Als je twijfelt kan je gebruik maken van simulaties waarbij je nieuwe steekproeven simuleert met eenzelfde steekproefgrootte en data die uit de Normaal verdeling komt met eenzelfde gemiddelde en variantie als wat in de steekproef werd geobserveerd.

Indien een afwijking van normaliteit wordt vastgesteld, tracht dan na te gaan (bv. via literatuur) of de statistische methode die je wenst toe te passen, gevoelig is voor dergelijke afwijkingen (een t-test is bijvoorbeeld vrij ongevoelig voor afwijkingen van Normaliteit als de afwijkingen symetrisch zijn). Eventueel kan je ook beroep doen op de centrale limietstelling.

### <span class="header-section-number">5.7.2</span> Nagaan van homoscedasticiteit

Dat kan opnieuw via boxplots. De grootte van de box is de interkwartiel range (IQR), een robuuste schatter voor de variantie (zie Sectie [4.3.2](../chap-describe/index.md)). Als de verschillen tussen de IQR range van beide groepen niet te groot is, kan men besluiten dat de data homoscedastisch zijn. Opnieuw kan inzicht gekregen worden in dergelijke plots door gebruik te maken van simulaties (zie Oefeningen). Men kan eveneens een formele F-test gebruiken om de varianties te vergelijken (zie oefeningen), maar hiervoor geldt dezelfde kritiek als voor het testen van normaliteit (zie vorige sectie).

Als er bij het vergelijken van gemiddelden tussen twee groepen niet aan homoscedasticiteit is voldaan, kan je gebruik maken van de Welch two-sample T-test. Hierbij wordt de gepoolde variantieschatter niet langer gebruikt. <span class="math display">\\$$T = \\frac{\\bar{Y}\_1 - \\bar{Y}\_2}{\\sqrt{\\frac{S^2\_1}{n\_1}+\\frac{S^2\_2}{n\_2}}}\\$$</span> waarbij <span class="math inline">\$S^2\_1\$</span> en <span class="math inline">\$S^2\_2\$</span> de steekproefvarianties zijn in beide groepen.

Deze statistiek volgt bij benadering een t-verdeling met een aantal vrijheidsgraden dat ligt tussen het kleinste aantal observaties <span class="math inline">\$\\text{min}(n\_1-1,n\_2-1)\$</span> en <span class="math inline">\$n\_1+n\_2-2\$</span>. De vrijheidsgraden worden in R berekend via de Welch–Satterthwaite benadering. Dat kan door in de `t.test` functie het argument `var.equal=FALSE` te zetten.

``` {.sourceCode .r}
t.test(Staph~trt,data=oksel,var.equal=FALSE)
```

    ##
    ##  Welch Two Sample t-test
    ##
    ## data:  Staph by trt
    ## t = 4.7519, df = 17.876, p-value = 0.0001622
    ## alternative hypothesis: true difference in means is not equal to 0
    ## 95 percent confidence interval:
    ##   9.976456 25.803544
    ## sample estimates:
    ## mean in group trt 1: transplant    mean in group trt 2: placebo
    ##                           49.79                           31.90

Merk op dat we in de output zien dat een Welch T-test is uitgevoerd aan de titel boven de analyse. Verder zien we dat voor dit voorbeeld de aangepaste vrijheidsgraden <span class="math inline">\$df = 17.876\$</span> bijna gelijk zijn aan de vrijheidsgraden van de klassieke T-test, omdat de varianties ongeveer gelijk zijn.

---

[← 5.6 Two-sample t-test](06-5-6-two-sample-t-test.md) · [Up: contents](index.md) · [5.8 Wat rapporteren? →](08-5-8-wat-rapporteren.md)

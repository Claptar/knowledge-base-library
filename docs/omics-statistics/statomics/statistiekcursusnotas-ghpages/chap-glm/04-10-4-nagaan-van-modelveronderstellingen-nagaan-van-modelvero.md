---
title: 10.4 Nagaan van modelveronderstellingen {#nagaan-van-modelveronderstellingen}
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-glm.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-glm.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 10.4 Nagaan van modelveronderstellingen {#nagaan-van-modelveronderstellingen}

**Source:** [`chap-glm.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-glm.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

Voor de statistische besluitvorming hebben we volgende aannames gedaan

1.  Lineariteit
2.  Onafhankelijkheid
3.  Homoscedasticiteit
4.  Normaliteit

Onafhankelijkheid is moeilijk te verifiëren op basis van de data, dat zou gegarandeerd moeten zijn door het design van de studie. Als we afwijkingen zien van lineariteit dan heeft besluitvorming geen zin gezien het de primaire veronderstelling is. In dat geval moeten we het conditioneel gemiddelde eerst beter modelleren. In geval van lineariteit maar schendingen van homoscedasticiteit of normaliteit dan weten we dat de besluitvorming mogelijks incorrect is omdat de teststatistieken dan niet langer een t-verdeling volgen.

### <span class="header-section-number">10.4.1</span> Lineariteit {#lineariteit}

De primaire veronderstelling in meervoudige lineaire regressie-analyse is de aanname dat de uitkomst (afhankelijke variabele) lineair varieert in functie van de verklarende variabelen.

Afwijkingen van lineariteit kunnen opnieuw worden opgespoord d.m.v. een *residuplot*. Deze wordt weergegeven in Figuur [10.3](index.md) links boven. Als de veronderstelling van lineariteit opgaat, krijgt men in een residuplot geen patroon te zien. De residuen zijn immers gemiddeld nul voor elke waarde van de predictoren en zouden dus mooi rond nul moeten variëren. Dat is inderdaad het geval voor het meervoudig lineaire regressiemodel dat we hebben gefit o.b.v. de prostaat dataset.

``` {.sourceCode .r}
par(mfrow=c(2,2))
plot(lmVWS)
```

<span id="fig:prosLinDiag1"></span> <img src="Statistiek_2019_2020_files/figure-html/prosLinDiag1-1.png" style="width:100.0%" alt="Diagnostische plots voor het nagaan van de veronderstellingen van het lineair regressiemodel waarbij lpsa gemodelleerd wordt a.d.h.v. de predictoren lcavol, lweight en svi." />

Figuur 10.3: Diagnostische plots voor het nagaan van de veronderstellingen van het lineair regressiemodel waarbij lpsa gemodelleerd wordt a.d.h.v. de predictoren lcavol, lweight en svi.

### <span class="header-section-number">10.4.2</span> Homoscedasticiteit

De residu-plot kan opnieuw worden gebruikt om de veronderstelling na te gaan van homoscedasticiteit of gelijkheid van variantie. De residu-plot voor het prostaatkanker voorbeeld Figuur [10.3](index.md) links boven geeft geen afwijkingen weer van homoscedasiticiteit. Alle residuen zijn mooi gespreid binnen dezelfde grenzen voor elke gefitte waarde <span class="math inline">\$\\hat y\_i\$</span>. De plot van de vierkantswortel van de absolute waarde van de gestandardiseerde error <span class="math inline">\$\\sqrt{\|e\_i\|/\\sqrt{MSE}}\$</span> in functie van de predicties (Figuur [10.3](index.md) links onder) geeft ook geen afwijkingen van homoscedasticiteit weer.

### <span class="header-section-number">10.4.3</span> Normaliteit

Opnieuw kunnen we de veronderstelling van normaliteit nagaan door gebruik te maken van QQ-plots. Figuur [10.3](index.md) rechts boven geeft de QQ-plot weer van de residuen voor het prostaatkanker voorbeeld. We zien in de plot geen aanwijzing voor afwijkingen van normaliteit.

---

[← 10.3 Besluitvorming in regressiemodellen](03-10-3-besluitvorming-in-regressiemodellen.md) · [Up: contents](index.md) · [10.5 Het niet-additieve meervoudig lineair regressiemodel →](05-10-5-het-niet-additieve-meervoudig-lineair-regressiemodel.md)

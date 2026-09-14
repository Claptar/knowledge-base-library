---
title: 2.4 Beschrijven van de populatie
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/belangrijke-concepten-conventies.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/belangrijke-concepten-conventies.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2.4 Beschrijven van de populatie

**Source:** [`belangrijke-concepten-conventies.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/belangrijke-concepten-conventies.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

Voor we een random variabele meten, kunnen we onmogelijk zeggen hoe hoog de meting precies zal zijn. De gerealiseerde waarde van <span class="math inline">\$X\$</span> is dus onderhevig aan random variabiliteit. Onze geobserveerde steekproef <span class="math inline">\$x\_1, x\_2, . . . , x\_{275}\$</span> kan dus als n = 275 realisaties worden beschouwd van dezelfde random variable X, voor subject <span class="math inline">\$i\$</span>, met <span class="math inline">\$i = 1,2,...,275\$</span>. Een random veranderlijke, een karakteristiek van de populatie, wordt beschreven door gebruik te maken van een *verdeling*.

De verdeling beschrijft de waarschijnlijkheid om een bepaalde waarde te observeren voor de toevallig veranderlijke wanneer men volledige lukraak een proefpersoon kiest uit de populatie. De densiteitsfunctie van de verdeling wordt vaak genoteerd als f(X). Heel vaak volgen biologische en chemische data een Normale verdeling. De Normale verdeling is een theoretische verdeling met een klokvorm die volledig gedefineerd wordt door twee parameters, het gemiddelde <span class="math inline">\$\\mu\$</span> en de variantie <span class="math inline">\$\\sigma^2\$</span>. We zullen in latere hoofdstukken dieper ingaan op de normale verdeling.

Veronderstel bijvoorbeeld dat de gemiddelde bloeddruk van subjecten in de populatie van gezonde 40-65 jarigen gelijk is aan <span class="math inline">\$\\mu=120\$</span> mmHg en de variantie <span class="math inline">\$\\sigma^2=196\$</span>. De verdeling van de systolische bloeddruk wordt weergegeven in Figuur [2.2](index.md) die d.m.v. onderstaande code wordt gegenereerd in R.

``` {.sourceCode .r}
grid <- seq(65,175,.1)
plot(grid,dnorm(grid,mean=120,sd=196^.5),xlab="Systolische Bloeddruk (mm kwik)",col=2,ylab="Densiteit",type="l",lwd=2)
grid2<-seq(115,120,.01)
polygon(x=c(grid2,120,115),y=c(dnorm(grid2,120,196^.5),0,0),col=2,border=2)
text(120,dnorm(120,120,196^.5),paste0("P(115 < X < 120) =",round( diff(pnorm(c(115,120),120,196^.5)) * 100, 1),"%"),col=2,cex=1,pos=4)
```

<span id="fig:nhanesNormal"></span> <img src="Statistiek_2019_2020_files/figure-html/nhanesNormal-1.png" style="width:100.0%" alt="Normale verdeling voor de systolische bloeddruk van gezonde personen tussen 40-65 jaar met gemiddelde 120 mm Hg en variantie 196." />

Figuur 2.2: Normale verdeling voor de systolische bloeddruk van gezonde personen tussen 40-65 jaar met gemiddelde 120 mm Hg en variantie 196.

Op basis van de verdeling kunnen we kansen berekenen om bijvoorbeeld een lukraak subject te bemonsteren uit de populatie met een bloeddruk tussen 115 en 120 mmHg. De kansen worden weergegeven door de oppervlakte onder de densiteitsfunctie:

<span class="math display">\\$$P\[115\\leq X\\leq 120$$= \\int\\limits\_{115}^{120} f(x) dx = 0.14\\\]</span>

De grafische interpretatie wordt weergegeven in Figuur [2.2](index.md). De oppervlakte onder de volledige densiteitscurve is gelijk aan 1

<span class="math display">\\$$P\[-\\infty\\leq X \\leq +\\infty$$=\\int\\limits\_{-\\infty}^{+\\infty} f(x) dx=1\\\]</span>

Kansen liggen uiteraard steeds tussen 0 en 1!

Kansen worden veelal berekend door gebruik te maken van de *cumulatieve distributie functie* van de verdeling, F(x), m.a.w. de functie die weergeeft wat de kans is dat een Normaal verdeelde toevallige veranderlijke een waarde zal aannemen die kleiner of gelijk is aan de vooropgestelde kwantiel x: <span class="math display">\\$$F(x)=\\int\\limits\_{-\\infty}^x f(x) dx = P\[X\\leq x$$.\\\]</span>

<img src="Statistiek_2019_2020_files/figure-html/nhanesNormalCum-1.png" style="display: block; margin: auto;;width:60.0%" /><img src="Statistiek_2019_2020_files/figure-html/nhanesNormalCum-2.png" style="display: block; margin: auto;;width:60.0%" /> Merk op dat de de normale distributie in R wordt geparameteriseerd a.d.h.v. het gemiddelde <span class="math inline">\$\\mu\$</span> en de standaard afwijking <span class="math inline">\$\\sigma\$</span>. Op basis van de Normaal verdeling die we veronderstelden voor de systolische bloeddruk in de populatie <span class="math inline">\$N(\\mu=120\$</span>,<span class="math inline">\$\\sigma^2=196)\$</span> bekomen we

``` {.sourceCode .r}
pnorm(120,mean=120,sd=196^.5)
```

    ## [1] 0.5

``` {.sourceCode .r}
pnorm(115,mean=120,sd=196^.5)
```

    ## [1] 0.3604924

``` {.sourceCode .r}
pnorm(120,mean=120,sd=196^.5)-pnorm(115,mean=120,sd=196^.5)
```

    ## [1] 0.1395076

waarbij pnorm de kans berekent dat de bloeddruk bij een willekeurig subject in de populatie lager of gelijk is aan het kwantiel dat wordt opgegeven (hier 120 mm Hg en 115 mm Hg). Het verschil tussen beide kansen geeft dan de kans weer op een bloeddruk tussen 115 en 120 mm Hg. Let wel dat R de parameterisatie gebruikt van het gemiddelde <span class="math inline">\$\\mu\$</span> en de standaard afwijking <span class="math inline">\$\\sigma\$</span>, ipv de variantie <span class="math inline">\$\\sigma^2\$</span>.

In de praktijk kennen we de werkelijke verdeling in de populatie niet en moet deze worden geschat o.b.v. de steekproef.

---

[← 2.3 Toevalsveranderlijken (of toevallige veranderlijken)](04-2-3-toevalsveranderlijken-of-toevallige-veranderlijken.md) · [Up: contents](index.md) · [2.5 Steekproef →](06-2-5-steekproef.md)

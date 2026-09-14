---
title: 5.5 Principe van Hypothesetoetsen (via one sample t-test)
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-besluit.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 5.5 Principe van Hypothesetoetsen (via one sample t-test)

**Source:** [`chap-besluit.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-besluit.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

We wensen een uitspraak te kunnen doen of er al dan niet een effect is van het toedienen van Captopril op de systolische bloeddruk? Beslissen op basis van gegevens is niet evident. Er is immers onzekerheid of de bevindingen uit de steekproef generaliseerbaar zijn naar de populatie. We stellen ons dus de vraag of het schijnbaar gunstig effect systematisch of toevallig is? Een natuurlijke beslissingsbasis is het gemiddeld verschil <span class="math inline">\$X\$</span> in de systolische bloeddruk:

<span class="math inline">\$\\bar x=\$</span> -18.93mmHg (<span class="math inline">\$s =\$</span> 9.03, <span class="math inline">\$SE =\$</span> 2.33).

Dat <span class="math inline">\$\\bar{x}&lt; 0\$</span> volstaat niet om te beslissen dat de gemiddelde systolische bloeddruk lager is na het toedienen van captopril *op het niveau van de volledige populatie*. Om het effect die we in de steekproef observeren te kunnen *veralgemenen* naar de populatie moet de bloeddrukverlaging voldoende groot zijn. Maar hoe groot moet dit effect nu zijn?

Hiervoor hebben statistici zogenaamde *toetsen* ontwikkeld om met dit soort vragen om te gaan. Deze leveren een ja/nee antwoord op de vraag of een geobserveerde associatie systematisch is (d.w.z. opgaat voor de studiepopulatie) of als er integendeel onvoldoende informatie in de steekproef voorhanden is om te besluiten dat de geobserveerde associatie ook aanwezig is in de volledige studiepopulatie. Tegenwoordig is het haast onmogelijk om een wetenschappelijk onderzoeksartikel te lezen zonder de resultaten van dergelijke toetsen te ontmoeten. Om die reden wensen we in dit hoofdstuk in te gaan op de betekenis van statistische toetsen en hun nomenclatuur.

We weten dat we volgens het *falcificatieprincipe* van Popper nooit een hypothese kunnen bewijzen op basis van data (zie Sectie [1.1](../inleiding/index.md)). Daarom zullen we twee hypotheses introduceren: een nulhypothese en een alternatieve hypothese. We zullen dan later a.d.h.v. de toets de nulhypothese trachten te ontkrachten.

### <span class="header-section-number">5.5.1</span> Hypotheses

Algemeen starten we met het vertalen van de wetenschappelijke vraagstelling naar een nulhypothese (<span class="math inline">\$H\_0\$</span>) en een alternatieve hypothese (<span class="math inline">\$H\_1\$</span>). Dit kan pas nadat de probleemstelling vertaald is naar een geparametriseerd statistisch model. Uit de beschrijving van de proefopzet volgt dat <span class="math inline">\$X\_1,...,X\_n\$</span> i.i.d.<a href="#fn31" id="fnref31" class="footnoteRef"><sup>31</sup></a> <span class="math inline">\$f(X)\$</span> met <span class="math inline">\$f(X)\$</span> de dichtheidsfunctie van de bloeddrukverschillen.

**Vereenvoudiging**: veronderstel dat <span class="math inline">\$f(X)\$</span> gekend is op een eindig-dimensionale set van parameters <span class="math inline">\$\\mathbf{\\theta}\$</span> na (parametrisch statistisch model). Voor het captopril voorbeeld veronderstellen we dat <span class="math inline">\$f(X)\$</span> een normale distributie <span class="math inline">\$N(\\mu,\\sigma^2)\$</span> volgt met parameters <span class="math inline">\$\\mathbf{\\theta}=(\\mu,\\sigma^2)\$</span>, het gemiddelde <span class="math inline">\$\\mu\$</span> en variantie <span class="math inline">\$\\sigma^2\$</span>.

De vraagstelling is geformuleerd in termen van de gemiddelde bloeddrukdaling: <span class="math inline">\$\\mu=E\_f$$X$$\$</span>.

De **alternatieve hypothese** wordt geformuleerd in termen van een parameter van <span class="math inline">\$f(X)\$</span> en dient uit te drukken wat de onderzoekers wensen te bewijzen aan de hand van de studie. Hier: <span class="math display">\\$$H\_1: \\mu&lt;0.\\$$</span> Gemiddeld gezien daalt de bloeddruk bij patiënten met hypertensie na toediening van captopril.

De **nulhypothese** is meestal een uitdrukking van de nultoestand, i.e. de omstandigheden waarin niets bijzonders aan de hand is. De onderzoekers wensen meestal te bewijzen via empirisch onderzoek dat de nulhypothese niet waar is: **Falsificatie principe**. De **nulhypothese wordt veelal uitgedrukt door gebruik te maken van dezelfde parameter als deze die in <span class="math inline">\$H\_1\$</span>** gebruikt is. Hier: <span class="math display">\\$$H\_0 : \\mu=0\\$$</span> m.a.w. gemiddeld gezien blijft de systolische bloeddruk na toediening van captopril onveranderd.

### <span class="header-section-number">5.5.2</span> Test-statistiek

Eens de populatie, de parameters en de nulhypothese en alternatieve hypothese bepaald zijn, kan de basisgedachte van een hypothesetest als volgt bondig beschreven worden.

Construeer een teststatistiek zodanig dat deze

1.  de evidentie meet die aanwezig is in de steekproef,
2.  tegen de gestelde nulhypothese,
3.  ten voordele van de alternatieve hypothese.

Een teststatistiek is dus noodzakelijk een functie van de steekproefobservaties.

Voor het captopril voorbeeld drukt de statistiek <span class="math display">\\$$T=\\bar X - \\mu\_0\\$$</span> uit hoever het steekproefgemiddelde van de bloeddrukdaling ligt van het gemiddelde <span class="math inline">\$\\mu\_0=0\$</span> in de populatie onder de nulhypothese<a href="#fn32" id="fnref32" class="footnoteRef"><sup>32</sup></a>.

- Als <span class="math inline">\$H\_0\$</span> waar is en er dus geen effect is van captopril in de populatie, dan verwachten we dat de teststatistiek T dicht ligt bij <span class="math inline">\$T=0\$</span>
- Als <span class="math inline">\$H\_1\$</span> waar is, dan verwachten we dat <span class="math inline">\$T&lt;0\$</span>.

In de praktijk gebruiken we echter meestal teststatistieken die niet alleen de grootte van het effect in rekening brengen maar ook de onzekerheid op het effect. We doen dit door de effectgrootte te balanceren t.o.v. de standard error.

<span class="math display">\\$$T=\\frac{\\bar{X}-0}{\\text{SE}\_{\\bar X}}\\$$</span> Waarbij <span class="math inline">\$\\mu\_0=0\$</span> voor het captopril voorbeeld.

Opnieuw geldt dat

- Als <span class="math inline">\$H\_0\$</span> waar is en er dus geen effect is van captopril in de populatie, dan verwachten we dat de teststatistiek T dicht ligt bij <span class="math inline">\$T=0\$</span>
- Als <span class="math inline">\$H\_1\$</span> waar is, dan verwachten we dat <span class="math inline">\$T&lt;0\$</span>.
- Voor het captopril voorbeeld vinden we <span class="math inline">\$t=(-18.93-0)/2.33=-8.12\$</span>.
- Is <span class="math inline">\$t = -8.12\$</span> groot genoeg in absolute waarde om te kunnen besluiten dat <span class="math inline">\$\\mu &lt; 0\$</span> en met welke zekerheid kunnen we dit besluiten?

Om daar een uitspraak over te doen zullen we de teststatistiek T verder bestuderen. T is een toevalsveranderlijke en de verdeling van T hangt af van de verdeling van de steekproefobservaties, maar die verdeling is ongekend! We hebben normaliteit verondersteld, maar dit laat nog steeds het gemiddelde en de variantie onbepaald. Bovendien wordt de hypothesetest net geconstrueerd om een uitspraak te kunnen doen over het gemiddelde <span class="math inline">\$\\mu\$</span>! De oplossing zit in de nulhypothese die we kunnen veronderstellen als er geen effect is van captopril. De <span class="math inline">\$H\_0\$</span> stelt dat <span class="math inline">\$\\mu=0\$</span>. Als we aannemen dat <span class="math inline">\$H\_0\$</span> waar is, dan is het gemiddelde van de normale distributie gekend! Als de bloeddrukverschillen <span class="math inline">\$X\_1, \\ldots X\_{15}\$</span> onafhankelijk en identiek normaal verdeeld (i.i.d.) zijn, dan weten we dat <span class="math display">\\$$\\bar X \\stackrel{H\_0}{\\sim} N(0, \\sigma^2/n)\\$$</span>

Gezien we <span class="math inline">\$\\sigma^2\$</span> niet kennen kunnen we deze vervangen door de steekproef variantie. Dan weten we dat <span class="math display">\\$$T=\\frac{\\bar{X}-0}{\\text{SE}\_{\\bar X}}\\stackrel{H\_0}{\\sim} t(n-1) \\$$</span> een t-verdeling volgt met n-1 vrijheidsgraden onder de **nulhypothese**. We weten dat indien de alternatieve hypothese waar zou zijn, we mogen verwachten dat er meer kans is op het observeren van een kleine waarde voor de teststatistiek dan wat verwacht wordt onder de nulhypothese. We zullen de verdeling van de teststatistiek onder de nulhypothese gebruiken om na te gaan of de geobserveerde test-statistiek <span class="math inline">\$t = -8.12\$</span> klein genoeg is om te kunnen besluiten dat <span class="math inline">\$\\mu &lt; 0\$</span>.

- **Is de geobserveerde teststatistiekwaarde (<span class="math inline">\$t=-8.12\$</span>) een waarde die we verwachten als <span class="math inline">\$H\_0\$</span> waar is**, of is het een waarde die onwaarschijnlijk klein is als <span class="math inline">\$H\_0\$</span> waar is?
- In het laatste geval deduceren we dat we niet langer kunnen aannemen dat <span class="math inline">\$H\_0\$</span> waar is, en dienen we dus <span class="math inline">\$H\_1\$</span> te concluderen.
- De vraag blijft: (a) hoe groot moet de geobserveerde teststatistiek <span class="math inline">\$t\$</span> zijn opdat we <span class="math inline">\$H\_0\$</span> verwerpen zodat (b) we bereid zijn om <span class="math inline">\$H\_1\$</span> te besluiten en (c) hoe zeker zijn we van deze beslissing?
- Het antwoord hangt samen met de interpretatie van de kansen die berekend kunnen worden op basis van de nuldistributie<a href="#fn33" id="fnref33" class="footnoteRef"><sup>33</sup></a> en de geobserveerde teststatistiek <span class="math inline">\$t\$</span>.

### <span class="header-section-number">5.5.3</span> De p-waarde

De kans waarop de keuze tussen <span class="math inline">\$H\_0\$</span> en <span class="math inline">\$H\_1\$</span> gebaseerd wordt, wordt de **<span class="math inline">\$p\$</span>-waarde** genoemd. De berekeningswijze is context-afhankelijk, maar voor het huidige voorbeeld wordt de <span class="math inline">\$p\$</span>-waarde gegeven door <span class="math display">\\$$ p = P\\left\[T \\leq t \\mid H\_0\\right$$ = \\text{P}\_0\\left$$T\\leq t\\right$$, \\\]</span> waar de index “0” in <span class="math inline">\$\\text{P}\_0\\left$$.\\right$$\$</span> aangeeft dat de kans onder de nulhypothese berekend wordt. Het is met andere woorden de kans om in een willekeurige steekproef onder de nulhypothese een waarde voor de teststatistiek T te bekomen die lager of gelijk is aan<a href="#fn34" id="fnref34" class="footnoteRef"><sup>34</sup></a> de waarde die in de huidige steekproef werd geobserveerd.

De <span class="math inline">\$p\$</span>-waarde voor het captopril voorbeeld wordt berekend als <span class="math display">\\$$p= \\text{P}\_0\\left\[T\\leq -8.12\\right$$=F\_t(-8.12;14) = 0.6\\ 10^{-6}.\\\]</span>

waarbij <span class="math inline">\$F\_t(;14)\$</span> de cumulatieve distributie functie is van een t-verdeling met 14 vrijheidsgraden, <span class="math display">\\$$F\_t(x;14)=\\int\\limits\_{-\\infty}^{x} f\_t(x;14).\\$$</span> Waarbij <span class="math inline">\$f\_t(.;14)\$</span> de densiteitsfunctie is van de t-verdeling. De oppervlakte onder de densiteitsfunctie is opnieuw een kans. Deze kans kan berekend worden in R m.b.v. de functie `pt(x,df)` die twee argumenten heeft, de waarde van de test-statistiek `x` en het aantal vrijheidsgraden van de t-verdeling `df`. `pt(x,df)` berekent de kans om een waarde te observeren die kleiner of gelijk is aan x wanneer men een willekeurige observatie trekt uit een t-verdeling met df vrijheidsgraden.

``` {.sourceCode .r}
n <- length(delta)
stat<-(mean(delta)-0)/(sd(delta)/sqrt(n))
stat
```

    ## [1] -8.122816

``` {.sourceCode .r}
pt(stat,n-1)
```

    ## [1] 5.731936e-07

<span id="def:unnamed-chunk-80" class="definition">**Definitie 5.6 (<span class="math inline">\$p\$</span>-waarde)** </span>De **p-waarde** (ook wel **geobserveerd significantieniveau** genoemd) is de kans om onder de nulhypothese een even of meer “extreme” toetsinggrootheid waar te nemen (in de richting van het alternatief) dan de waarde <span class="math inline">\$t\$</span> die geobserveerd werd o.b.v. de steekproef. Hoe kleiner die kans is, hoe sterker het bewijs tegen de nulhypothese.

Merk op dat de p-waarde de kans **niet** uitdrukt dat de nulhypothese waar is\!<a href="#fn35" id="fnref35" class="footnoteRef"><sup>35</sup></a>.

**Einde Definitie**

Het woord “extreem” duidt op de richting waarvoor de teststatistiek onder de alternatieve hypothese meer waarschijnlijk is. In het voorbeeld is <span class="math inline">\$H\_1: \\mu &lt; 0\$</span> en verwachten we dus kleinere waarden van <span class="math inline">\$t\$</span> onder <span class="math inline">\$H\_1\$</span>. Vandaar de kans op <span class="math inline">\$T\\leq t\$</span>. Uit de definitie van de <span class="math inline">\$p\$</span>-waarde volgt dat een kleine <span class="math inline">\$p\$</span>-waarde betekent dat de geobserveerde teststatistiek eerder onwaarschijnlijk is als aangenomen wordt dat <span class="math inline">\$H\_0\$</span> correct is. Dus een voldoende kleine <span class="math inline">\$p\$</span>-waarde noopt ons tot het **verwerpen van <span class="math inline">\$H\_0\$</span>** ten voordele van <span class="math inline">\$H\_1\$</span>. De drempelwaarde waarmee de <span class="math inline">\$p\$</span>-waarde vergeleken wordt, wordt het **significanctieniveau** genoemd en wordt voorgesteld door <span class="math inline">\$\\alpha\$</span>.

<span id="def:unnamed-chunk-81" class="definition">**Definitie 5.7 (significantieniveau)** </span>De drempelwaarde <span class="math inline">\$\\alpha\$</span> staat gekend als het **significantieniveau** van de statistische test. Een statistische test uitgevoerd op het <span class="math inline">\$\\alpha\$</span> significantieniveau wordt een **niveau-<span class="math inline">\$\\alpha\$</span> test** genoemd (Engels: *level-<span class="math inline">\$\\alpha\$</span> test*).

**Einde definitie**

Een toetsingsresultaat wordt *statistisch significant* genoemd wanneer de bijhorende p-waarde kleiner is dan <span class="math inline">\$\\alpha\$</span>, waarbij <span class="math inline">\$\\alpha\$</span> meestal gelijk aan 5% wordt genomen. Hoe kleiner de p-waarde hoe meer \`significant’ het testresultaat afwijkt van de verwachting onder de nulhypothese. Het aangeven van een p-waarde voor een toets geeft bijgevolg meer informatie over het resultaat dan een eenvoudig ja/nee antwoord of de nulhypothese wordt verworpen op een vast gekozen <span class="math inline">\$\\alpha\$</span>-niveau. Het geeft immers niet alleen aan of de nulhypothese verworpen wordt op een gegeven significantieniveau, maar ook op welke significantieniveaus de nulhypothese verworpen wordt.

Ze vat dus de bewijskracht tegen de nulhypothese samen <span class="math display">\\$$\\begin{array}{cl}&gt;0.10 & \\text{ niet significant (zwak bewijs)}\\\\0.05-0.10 & \\text{ marginaal significant, suggestief}\\\\0.01-0.05 & \\text{ significant}\\\\0.001-0.01 & \\text{ sterk significant}\\\\&lt;0.001 & \\text{ extreem significant}\\end{array}\\$$</span>

### <span class="header-section-number">5.5.4</span> Kritieke waarde

Een **alternatieve wijze voor de formulering van de beslissingsregel** kan worden bekomen door gebruik te maken van een kritieke waarde. In plaats van <span class="math inline">\$p\$</span>-waarden, kan de beslissingsregel geschreven worden in termen van de teststatistiek. Bij gebruik van <span class="math inline">\$p\$</span>-waarden bepaalt <span class="math inline">\$p=\\alpha\$</span> de grens. Een <span class="math inline">\$p\$</span>-waarde van <span class="math inline">\$\\alpha\$</span> schrijven we als <span class="math display">\\$$p=\\text{P}\_0 \\left\[ T \\leq t \\right$$=\\alpha.\\\]</span>

Dat is exact de definitie van het het <span class="math inline">\$\\alpha\$</span>-percentiel van de distributie van <span class="math inline">\$T\$</span>. In het voorbeeld is de nuldistributie <span class="math inline">\$t\_{n-1}\$</span>. Dus,<span class="math display">\\$$\\text{P}\_0\\left\[T\\leq -t\_{n-1;\\alpha}\\right$$=\\alpha.\\\]</span>

De beslissingsregel mag dus ook geschreven worden als <span class="math display">\\$$\\begin{eqnarray\*} \\text{als } & t&lt; -t\_{n-1;\\alpha} & \\text{ dan verwerp }H\_0\\text{ en besluit }H\_1 \\\\ \\text{als } & t\\geq -t\_{n-1;\\alpha} & \\text{ dan aanvaard }H\_0. \\end{eqnarray\*}\\$$</span>

Het percentiel <span class="math inline">\$t\_{n-1;\\alpha}\$</span> dat de drempelwaarde vormt in de beslissingsregel wordt in deze context de **kritieke waarde** op het <span class="math inline">\$5\\%\$</span> significantieniveau genoemd. De beslissingsregel waarbij de geobserveerde <span class="math inline">\$t\$</span> vergeleken wordt met een kritieke waarde is minder algemeen geformuleerd dan deze gebruik makend van de <span class="math inline">\$p\$</span>-waarde omdat het expliciet gebruik maakt van de nuldistributie die van teststatistiek tot teststatistiek, of zelfs van dataset tot dataset kan variëren.

De begrippen p-waarde, kritieke waarde, significantie-niveau, verwerpings- en aanvaardingsregio worden weergegeven in Figuur [5.12](index.md).

<span id="fig:captoTest"></span> <img src="Statistiek_2019_2020_files/figure-html/captoTest-1.png" style="width:100.0%" alt="Interpretatie van p-waarde, kritieke waarde, verwerpingsgebied, aanvaardingsgebied voor het captopril voorbeeld." />

Figuur 5.12: Interpretatie van p-waarde, kritieke waarde, verwerpingsgebied, aanvaardingsgebied voor het captopril voorbeeld.

### <span class="header-section-number">5.5.5</span> Beslissingsfouten

Aangezien de beslissing over het al dan niet verwerpen van de nulhypothese bepaald wordt door slechts een steekproef te observeren, kunnen volgende beslissing genomen worden:

<table class="table" style="margin-left: auto; margin-right: auto;">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center; border-bottom: hidden;"></th>
<th colspan="2" style="text-align: center; border-bottom: hidden; padding-bottom: 0; padding-left: 3px; padding-right: 3px;"><div style="border-bottom: 1px solid #ddd; padding-bottom: 5px; ">
Werkelijkheid
</div></th>
</tr>
<tr>
<th style="text-align: center;">Besluit</th>
<th style="text-align: center;">H0</th>
<th style="text-align: center;">H1</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Aanvaard H0</td>
<td style="text-align: center;">OK</td>
<td style="text-align: center;">Type II (β)</td>
</tr>
<tr>
<td style="text-align: center;">Verwerp H0</td>
<td style="text-align: center;">Type I (α)</td>
<td style="text-align: center;">OK</td>
</tr>
</tbody>
</table>

Het schema geeft de vier mogelijke situaties:

- <span class="math inline">\$H\_0\$</span> is in werkelijkheid waar, en dit wordt ook besloten aan de hand van de statistische test (dus geen beslissingsfout)

- <span class="math inline">\$H\_1\$</span> is in werkelijkheid waar, en dit wordt ook besloten aan de hand van de statistische test (dus geen beslissingsfout)

- <span class="math inline">\$H\_0\$</span> is in werkelijkheid waar, maar aan de hand van de statistische test wordt besloten om <span class="math inline">\$H\_0\$</span> te verwerpen en <span class="math inline">\$H\_1\$</span> te concluderen. Dus <span class="math inline">\$H\_1\$</span> wordt foutief besloten. Dit is een zogenaamde **type I** fout.

- <span class="math inline">\$H\_1\$</span> is in werkelijkheid waar, maar aan de hand van de statistische test wordt besloten om <span class="math inline">\$H\_0\$</span> te aanvaarden. Dit is een zogenaamde **type II** fout. Dus <span class="math inline">\$H\_0\$</span> wordt foutief aanvaard.

De beslissing is gebaseerd op een teststatistiek <span class="math inline">\$T\$</span> die een toevalsveranderlijke is. De beslissing is dus ook stochastisch en aan de vier mogelijke situaties uit bovenstaand schema kunnen dus probabiliteiten toegekend worden. Net zoals voor het afleiden van de steekproefdistributie van de teststatistiek, moeten we de distributie van de steekproefobservaties kennen alvorens het stochastisch gedrag van de beslissingen te kunnen beschrijven. Indien we aannemen dat <span class="math inline">\$H\_0\$</span> waar is, dan is de distributie van <span class="math inline">\$T\$</span> gekend en kunnen ook de kansen op de beslissingen bepaald worden voor de eerste kolom van de tabel.

We starten met de kans op een type I fout (hier uitgewerkt voor het captopril voor beeld): <span class="math display">\\$$\\text{P}\\left\[\\text{type I fout}\\right$$=\\text{P}\\left$$\\text{verwerp }H\_0 \\mid H\_0\\right$$ = \\text{P}\_0\\left$$T&lt;t\_{n-1;1-\\alpha}\\right$$=\\alpha.\\\]</span> Dit geeft ons meteen een interpretatie van het significantieniveau <span class="math inline">\$\\alpha\$</span>: het is de kans op het maken van een type I fout. De constructie van de statistische test garandeert dus dat de kans op het maken van een type I fout gecontroleerd wordt op het significantieniveau <span class="math inline">\$\\alpha\$</span>. De kans op het correct aanvaarden van <span class="math inline">\$H\_0\$</span> is dus <span class="math inline">\$1-\\alpha\$</span>. Verder kan aangetoond worden dat de p-waarde onder <span class="math inline">\$H\_0\$</span> uniform verdeeld is. Het leidt dus tot een uniforme beslissingsstrategie.

Het bepalen van de kans op een type II fout is minder evident omdat de alternatieve hypothese minder éénduidig is als de nulhypothese. In het captopril voorbeeld is <span class="math inline">\$H\_1: \\mu&lt;0\$</span>; met deze informatie wordt de distributie van de steekproefobservaties niet volledig gespecifieerd en dus ook niet de distributie van de teststatistiek. Dit impliceert dat we eigenlijk de kans op een type II fout niet kunnen berekenen. De klassieke *work-around* bestaat erin om één specifieke distributie te kiezen die voldoet aan <span class="math inline">\$H\_1\$</span>.

<span class="math display">\\$$H\_1(\\delta): \\mu=0-\\delta \\text{ voor een }\\delta&gt;0.\\$$</span>

De parameter <span class="math inline">\$\\delta\$</span> kwantificeert de afwijking van de nulhypothese.

De **kracht** van een test (Engels: *power*) is een kans die meer frequent gebruikt wordt dan de kans op een type II fout <span class="math inline">\$\\beta\$</span>. De kracht wordt gedefinieerd als

<span class="math display">\\$$\\pi(\\delta) = 1-\\beta(\\delta) = \\text{P}\_\\delta\\left\[T&gt;t\_{n-1;1-\\alpha}\\right$$=\\text{P}\_\\delta\\left$$P&lt;\\alpha\\right$$.\\\]</span>

De kracht van een niveau-<span class="math inline">\$\\alpha\$</span> test voor het detecteren van een afwijking <span class="math inline">\$\\delta\$</span> van het gemiddelde onder de nulhypothese <span class="math inline">\$\\mu\_0=0\$</span> is dus de kans dat de niveau-<span class="math inline">\$\\alpha\$</span> test dit detecteert wanneer de afwijking in werkelijkheid <span class="math inline">\$\\delta\$</span> is.

Merk op dat <span class="math inline">\$\\pi(0)=\\alpha\$</span> en de kracht van een test toeneemt als de afwijking van de nulhypothese toeneemt.

De **kracht** van de test (d.i. de kans om Type II fouten te vermijden) wordt typisch niet gecontroleerd, tenzij d.m.v. studiedesign en steekproefgrootte.

**Interpretatie**

Stel dat we voor een gegeven dataset bekomen dat <span class="math inline">\$p&lt;\\alpha\$</span>, m.a.w. <span class="math inline">\$H\_0\$</span> wordt verworpen. Volgens het schema van de beslissingsfouten zijn er dan slechts twee mogelijkheden (zie onderste rij van schema): ofwel is de beslissing correct, ofwel hebben we een type I fout gemaakt. Over de type I fout weten we echter dat ze slechts voorkomt met een kleine kans. Anderzijds, indien <span class="math inline">\$p\\geq \\alpha\$</span> en we <span class="math inline">\$H\_0\$</span> niet verwerpen, dan zijn er ook twee mogelijkheden: ofwel is de beslissing correct, ofwel hebben we een type II fout gemaakt. De kans op een type II fout (<span class="math inline">\$\\beta\$</span>) is echter niet gecontroleerd op een gespecifieerde waarde. De statistische test is zodanig geconstrueerd dat ze enkel de kans op een type I fout controleert (op <span class="math inline">\$\\alpha\$</span>). Om wetenschappelijk eerlijk te zijn, moeten we een pessimistische houding aannemen en er rekening mee houden dat <span class="math inline">\$\\beta\$</span> groot zou kunnen zijn (i.e. een kleine kracht).

Bij <span class="math inline">\$p &lt; \\alpha\$</span> wordt de nulhypothese verworpen en we mogen hieruit concluderen dat <span class="math inline">\$H\_1\$</span> waarschijnlijk juist is. Dit noemen we een sterke conclusie. Bij <span class="math inline">\$p\\geq \\alpha\$</span> wordt de nulhypothese aanvaard, maar dat impliceert niet dat we concluderen dat <span class="math inline">\$H\_0\$</span> juist is. We kunnen enkel besluiten dat de data onvoldoende bewijskracht tegen <span class="math inline">\$H\_0\$</span> ten gunste van <span class="math inline">\$H\_1\$</span> bevatten. Dit noemen we een daarom zwakke conclusie.

### <span class="header-section-number">5.5.6</span> Conclusies Captopril voorbeeld.

De test die we hebben uitgevoerd is in de literatuur ook bekend als de **one sample t-test** op het verschil of als een **gepaarde t-test**, we beschikken immers over gepaarde gegevens per patiënt. De test is eenzijdig uitgevoerd. We testen tegen het alternatief dat er een bloeddrukdaling is.

Beide testen (one sample t-test op het verschil en de gepaarde t-test) geven ons inderdaad dezelfde resultaten:

``` {.sourceCode .r}
t.test(delta,alternative="less")
```

    ##
    ##  One Sample t-test
    ##
    ## data:  delta
    ## t = -8.1228, df = 14, p-value = 5.732e-07
    ## alternative hypothesis: true mean is less than 0
    ## 95 percent confidence interval:
    ##       -Inf -14.82793
    ## sample estimates:
    ## mean of x
    ## -18.93333

``` {.sourceCode .r}
with(captopril, t.test(SBPa,SBPb,paired=TRUE,alternative="less"))
```

    ##
    ##  Paired t-test
    ##
    ## data:  SBPa and SBPb
    ## t = -8.1228, df = 14, p-value = 5.732e-07
    ## alternative hypothesis: true difference in means is less than 0
    ## 95 percent confidence interval:
    ##       -Inf -14.82793
    ## sample estimates:
    ## mean of the differences
    ##               -18.93333

We kunnen op basis van de test het volgende concluderen: Na toediening van captopril is er een extreem significante verlaging van de systolische bloeddruk bij patiënten met hypertensie (<span class="math inline">\$p &lt;&lt; 0.001\$</span>). De systolische bloeddruk neemt gemiddeld met 18.9 mm kwik af na de behandeling met captopril (95% BI $$<span class="math inline">\$-\\infty,-14.82\$</span>$$ mm Hg).

Merk op dat we

1.  Een eenzijdig interval rapporteren gezien we enkel geïnteresseerd zijn om aan te tonen dat er een bloeddrukdaling is.
2.  Door het pre-test/post-test design geen uitsluitsel kunnen geven of dit te wijten is aan de werking van het middel of aan een placebo effect. Er was geen goeie controle! Het gebrek van een goeie controle is veelal een probleem bij pre-test/post-test designs.

### <span class="header-section-number">5.5.7</span> Eenzijdig of tweezijdig toetsen?

De test in het captopril voorbeeld was een eenzijdige test. We wensen immers enkel te detecteren of de captopril behandeling de bloeddruk gemiddeld gezien doet dalen.

In andere gevallen of een andere context wenst men enkel een stijging te detecteren.
Stel dat men het bloeddrukverschil had gedefineerd als <span class="math inline">\$X\_{i}^\\prime=Y\_{i}^\\text{voor}-Y\_{i}^\\text{na}\$</span> dan zouden positieve waarden aangeven dat er een bloeddrukdaling was na de behandeling van captopril: de bloeddruk bij aanvang is dan immers groter dan na de behandeling. De gemiddelde bloeddrukverandering in de populatie noteren we nu als <span class="math inline">\$\\mu^\\prime=\\text{E}$$X^\*$$\$</span>. In dat geval hadden we een eenzijdige test uit moeten voeren om <span class="math inline">\$H\_0: \\mu^\\prime=0\$</span> te testen tegen <span class="math inline">\$H\_1: \\mu^\\prime&gt;0\$</span>. Voor deze test kunnen we de p-waarde als volgt berekenen: <span class="math display">\\$$p=\\text{P}\_0\\left\[T\\geq t\\right$$.\\\]</span>

We voeren nu de analyse uit in R op basis van de toevallige veranderlijke <span class="math inline">\$X^\\prime\$</span>. We zullen nu het argument `alternative="greater"` gebruiken in de `t.test` functie zodat we de nulhypothese toetsen tegen het alternatief <span class="math inline">\$H\_1: \\mu^\\prime&gt;0\$</span>:

``` {.sourceCode .r}
delta2 <- captopril$SBPb-captopril$SBPa
t.test(delta2,alternative="greater")
```

    ##
    ##  One Sample t-test
    ##
    ## data:  delta2
    ## t = 8.1228, df = 14, p-value = 5.732e-07
    ## alternative hypothesis: true mean is greater than 0
    ## 95 percent confidence interval:
    ##  14.82793      Inf
    ## sample estimates:
    ## mean of x
    ##  18.93333

Uiteraard bekomen we met deze analyse exact dezelfde p-waarde en hetzelfde betrouwbaarheidsinterval. Enkel het teken is omgewisseld.

Naast eenzijdige testen kunnen eveneens tweezijdige testen worden uitgevoerd. Het had gekund dat de onderzoekers de werking van het nieuwe medicijn captopril wensten te testen, maar het werkingsmechanisme nog niet kenden in de ontwerpfase. In dat geval zou het eveneens interessant geweest zijn om zowel een stijging als een daling van de bloeddruk te kunnen detecteren. Hiervoor zou men een tweezijdige toetsstrategie moeten gebruiken waarbij men de nulhypothese <span class="math display">\\$$H\_0: \\mu=0\\$$</span> gaat testen versus het alternatieve hypothese <span class="math display">\\$$H\_1: \\mu\\neq0,\\$$</span> zodat het gemiddelde onder de alternatieve hypothese verschillend is van 0. Het kan zowel een positieve of negatieve afwijking zijn en men weet niet bij aanvang van de studie in welke richting het werkelijk gemiddelde zal afwijken onder de alternatieve hypothese.

We kunnen tweezijdig testen op het <span class="math inline">\$\\alpha=5\\%\$</span> significantieniveau door

1.  een kritieke waarde af te leiden:
    - Bij een tweezijdige test kan het effect onder de alternatieve hypothese zowel positief of negatief zijn. Hierdoor zullen we onder de nulhypothese de kans berekenen om onder de nulhypothese een effect te observeren dat meer extreem is dan het resultaat dat werd geobserveerd in de steekproef. In deze context betekent “meer extreem” dat de statistiek groter is in absolute waarde dan het geobserveerde resultaat, want zowel grote (sterk positieve) als kleine (sterk negatieve) waarden zijn een indicatie van een afwijking van de nulhypothese.
    - Om een kritieke waarde af te leiden,zullen we het significatie-niveau <span class="math inline">\$\\alpha\$</span> daarom verdelen over de linker en rechter staart van de verdeling onder <span class="math inline">\$H\_0\$</span>. Gezien de t-verdeling symmetrisch is, volgt dat we een kritieke waarde <span class="math inline">\$c\$</span> kiezen zodat er een kans is van <span class="math inline">\$\\alpha/2=2.5\\%\$</span> dat <span class="math inline">\$T\\geq c\$</span> en er <span class="math inline">\$\\alpha/2=2.5\\%\$</span> kans is dat <span class="math inline">\$T\\leq -c\$</span>. We kunnen dit ook nog als volgt formuleren: Er is onder <span class="math inline">\$H\_0\$</span> <span class="math inline">\$\\alpha=5\\%\$</span> kans dat <span class="math inline">\$\\vert T\\vert\\geq c\$</span> (zie Figuur [5.13](index.md)).
2.  We kunnen ook gebruik maken van een tweezijdige p-waarde: <span class="math display">\\$$\\begin{eqnarray\*} p&=&\\text{P}\_0\\left\[T\\leq -\|t\|\\right$$ + \\text{P}\_0\\left$$T\\geq \|t\|\\right$$\\\\ &=&\\text{P}\_0\\left$$\\vert T\\vert \\geq \\vert t \\vert\\right$$\\\\ &=&\\text{P}\_0\\left$$T \\geq \\vert t \\vert\\right$$\\times 2. \\end{eqnarray\*}\\\]</span>

We berekenen dus de kans dat de t-statistiek onder <span class="math inline">\$H\_0\$</span> meer extreem is dan de geobserveerde teststatistiek <span class="math inline">\$t\$</span> in de steekproef. Waarbij meer extreem tweezijdig moet geïnterpreteerd worden. De teststatistiek onder <span class="math inline">\$H\_0\$</span> is meer extreem als hij groter is in absolute waarde dan <span class="math inline">\$\\vert t \\vert\$</span>, de geobserveerde test statistiek. Gezien de verdeling symmetrisch is, kunnen we ook eerst de kans in de rechter staart van de verdeling berekenen en deze kans vervolgens vermenigvuldigen met 2 zodoende een tweezijdige p-waarde te bekomen.

Als de onderzoekers niet vooraf gedefineerd hadden dat ze enkel een bloeddrukdaling wensten te detecteren, dan hadden ze dus een twee-zijdige test uitgevoerd. Merk op dat het argument `alternative` van de `t.test` functie een default waarde heeft `alternative="two.sided"` zodat er standaard tweezijdig wordt getoetst.

``` {.sourceCode .r}
t.test(delta)
```

    ##
    ##  One Sample t-test
    ##
    ## data:  delta
    ## t = -8.1228, df = 14, p-value = 1.146e-06
    ## alternative hypothesis: true mean is not equal to 0
    ## 95 percent confidence interval:
    ##  -23.93258 -13.93409
    ## sample estimates:
    ## mean of x
    ## -18.93333

We bekomen nog steeds een exteem significant resultaat. De p-waarde is echter dubbel zo groot omdat we tweezijdig testen. We verkrijgen eveneens een tweezijdig betrouwbaarheidsinterval. De tweezijdige toetsstrategie wordt weergegeven in Figuur [5.13](index.md).

<span id="fig:captoTest2"></span> <img src="Statistiek_2019_2020_files/figure-html/captoTest2-1.png" style="width:100.0%" alt="Interpretatie van p-waarde, kritieke waarde, verwerpingsgebied, aanvaardingsgebied voor het captopril voorbeeld wanneer we een tweezijdige toets uitvoeren." />

Figuur 5.13: Interpretatie van p-waarde, kritieke waarde, verwerpingsgebied, aanvaardingsgebied voor het captopril voorbeeld wanneer we een tweezijdige toets uitvoeren.

We kunnen ons nu de vraag stellen wanneer we eenzijdig of tweezijdig toetsen. Met een eenzijdige toets kan men gemakkelijker een alternatieve hypothese aantonen (op voorwaarde dat ze waar is) dan met een tweezijdige toets. Dit komt essentieel omdat bij zo’n toets alle informatie kan worden aangewend om in 1 enkele richting te zoeken. Precies daarom vergt de eenzijdige toets een extra beschouwing vóór de aanvang van de studie. Ook al hebben we sterke a priori vermoedens, vaak kunnen we niet zeker zijn dat dat zo is. Anders was er immers geen reden om dit te willen toetsen.

Als men een eenzijdige test voorstelt, maar men vindt een resultaat in de andere richting dat formeel statistisch significant is, dan is het niet geschikt om dit te zien als bewijs voor een werkelijk effect in die richting. Dat is omdat de onderzoekers die mogelijkheid uitgesloten hebben bij de planning van de studie en het resultaat daarom zó onverwacht is dat het als een vals positief resultaat kan gezien worden. Een eenzijdige test is om die reden niet aanbevolen. Een tweezijdige toets is altijd verdedigbaar omdat ze in principe toelaat om elke afwijking van de nulhypothese te detecteren. Ze worden daarom het meest gebruikt en ten zeerste aangeraden. Het is **nooit toegelaten** om een tweezijdige toets in een eenzijdige toets om te zetten **op basis van wat men observeert in de gegevens**! Anders wordt de type I fout van de toetsingsstrategie niet correct gecontroleerd.

Dat wordt geïllustreerd in de onderstaande simulatie. We evalueren twee strategieën, de correcte tweezijdige test en een test waar we eenzijdig toetsen op basis van het teken van het geobserveerde effect.

``` {.sourceCode .r}
set.seed(115)
mu <- 0
sigma <- 9.0
nSim <- 1000
alpha <- 0.05
n <- 15
pvalsCor <- pvalsInCor<-array(0,nSim)
for (i in 1:nSim)
{
    x <- rnorm(n,mean=mu,sd=sigma)
    pvalsCor[i] <- t.test(x)$p.value
    if (mean(x)<0) pvalsInCor[i] <- t.test(x,alternative="less")$p.value else
        pvalsInCor[i] <- t.test(x,alternative="greater")$p.value
}
mean(pvalsCor<0.05)
```

    ## [1] 0.049

``` {.sourceCode .r}
mean(pvalsInCor<0.05)
```

    ## [1] 0.106

We zien inderdaad dat de type I fout correct gecontroleerd wordt op het nominaal significantie-niveau <span class="math inline">\$\\alpha\$</span> wanneer we tweezijdig testen en dat dit helemaal niet het geval is wanneer we eenzijdige toetsen op basis van het teken van het geobserveerde effect.

---

[← 5.4 Intervalschatters](04-5-4-intervalschatters.md) · [Up: contents](index.md) · [5.6 Two-sample t-test →](06-5-6-two-sample-t-test.md)

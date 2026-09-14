---
title: ontbrekende waarnemingen voorkomen.
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-describe.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-describe.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# ontbrekende waarnemingen voorkomen.

**Source:** [`chap-describe.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-describe.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

sd(NHANES$BMI,na.rm=TRUE)
```

    ## [1] 7.376579

``` {.sourceCode .r}
 # levert de variantie van de variabele BMI
var(NHANES$BMI,na.rm=TRUE)
```

    ## [1] 54.41392

Wanneer een variabele niet Normaal verdeeld is (dit is bijvoorbeeld het geval voor het BMI gezien het niet symmetrisch verdeeld is), dan geldt niet langer dat bij benadering 95% van de waarnemingen ligt tussen <span class="math inline">\$\\bar{x} - 2 s\$</span> en <span class="math inline">\$\\bar{x} + 2 s\$</span>. Een symmetrische maat voor de spreiding van de gegevens, zoals de standaarddeviatie, is dan niet langer interessant. In dat geval zijn de range en interkwantielafstand betere maten.

<span id="def:unnamed-chunk-47" class="definition">**Definitie 4.8 (bereik en interkwartielafstand)** </span>Het **bereik** of de **range** <span class="math inline">\$R\_x\$</span> van een reeks waarnemingen <span class="math inline">\$x\_i, i=1,2,...,n\$</span>, is per definitie het verschil tussen de grootste en kleinste geobserveerde waarde. De **interkwartielafstand** van een reeks waarnemingen <span class="math inline">\$x\_i, i=1,2,...,n\$</span> is per definitie de afstand tussen het derde kwartiel <span class="math inline">\$x\_{75}\$</span> en het eerste kwartiel <span class="math inline">\$x\_{25}\$</span>. Dat wordt ook grafisch weergegeven op een boxplot (breedte van de box). Hierbinnen liggen circa 50% van de observaties. Circa 95% van de observaties kan men vinden tussen het 2.5% en 97.5% percentiel.

**Einde definitie**

Het bereik is zeer gevoelig voor outliers en is systematisch afhankelijk van het aantal observaties: hoe groter <span class="math inline">\$n,\$</span> hoe groter men <span class="math inline">\$R\_x\$</span> verwacht. Om die reden vormt een interkwartielafstand een betere maat voor de spreiding van de gegevens dan de range.

Tenslotte is het vaak zo dat de gegevens meer gespreid zijn naarmate hun gemiddelde hogere waarden aanneemt. De *variatiecoëfficiënt*=<span class="math inline">\$VC\_x\$</span> standaardiseert daarom de standaarddeviatie door ze uit te drukken als een percentage van het gemiddelde <span class="math display">\\$$\\begin{equation\*} VC\_x = \\frac{s\_x}{\\bar{x}} 100\\%. \\end{equation\*}\\$$</span>

Omdat ze gestandaardiseerd is, dient ze beter dan de standaarddeviatie zelf om de spreiding op de gegevens te vergelijken tussen populaties met een verschillend gemiddelde. De variatiecoëfficiënt heeft verder de aantrekkelijke eigenschap dat ze geen eenheden heeft en ongevoelig is voor herschaling van de gegevens (d.w.z. wanneer alle gegevens met een constante <span class="math inline">\$a\$</span> worden vermenigvuldigd, dan is <span class="math inline">\$VC\_{ax}=VC\_x\$</span>).

## <span class="header-section-number">4.4</span> De Normale benadering van gegevens {#de-normale-benadering-van-gegevens}

Bij biologische en chemische data is het vaak zo dat het histogram van een continue meting bij verschillende subjecten de karakteristieke vorm heeft van de Normale verdeling, die geïllustreerd wordt in Figuur [4.8](index.md) (linksboven). Dat is bijvoorbeeld zo als men een histogram maakt van het logaritme van de totale cholestorol. Rond 1870 opperde de wereldberoemde Belg Adolphe Quetelet (die tevens de eerste student was die een doctoraat behaalde aan de Universiteit Gent) de idee om deze curve als \`ideaal histogram’ te gebruiken voor de voorstelling en vergelijking van gegevens. Dit zal handig blijken om meer inzicht te krijgen in de gegevens op basis van een minimum aantal samenvattingsvatten, zoals het gemiddelde en de standaarddeviatie die vaak in wetenschappelijke rapporten vermeld staan.

<span id="fig:continu"></span> <img src="Statistiek_2019_2020_files/figure-html/continu-1.png" style="width:100.0%" alt="De Normale dichtheidsfunctie (boven, links), de Normale distributiefunctie (boven, rechts), de Uniforme dichtheidsfunctie (onder, links) en de Uniforme distributiefunctie (onder, rechts)." />

Figuur 4.8: De Normale dichtheidsfunctie (boven, links), de Normale distributiefunctie (boven, rechts), de Uniforme dichtheidsfunctie (onder, links) en de Uniforme distributiefunctie (onder, rechts).

### <span class="header-section-number">4.4.1</span> Bepalen van oppervlaktes onder de Normale curve {#bepalen-van-oppervlaktes-onder-de-normale-curve}

De *Normale curve* of *Normale dichtheidsfunctie* wordt gegeven door: <span class="math display">\\$$\\begin{equation\*} f(x) = \\frac{1}{\\sigma \\sqrt{2 \\pi} } \\exp \\left ( - \\frac{ (x - \\mu)^2 }{ 2 \\sigma^2} \\right ). \\end{equation\*}\\$$</span>

Ze wordt beschreven door 2 onbekende parameters <span class="math inline">\$\\mu\$</span> en <span class="math inline">\$\\sigma\$</span>, waarbij <span class="math inline">\$\\mu\$</span> het gemiddelde van de verdeling van de observaties aangeeft en <span class="math inline">\$\\sigma\$</span> de standaarddeviatie. Deze curve geeft voor elke waarde <span class="math inline">\$x\$</span> weer hoe frequent deze waarde, relatief gezien, voorkomt. De notatie <span class="math inline">\$\\pi\$</span> verwijst naar het getal <span class="math inline">\$\\pi=3.1459...\$</span> Wanneer het gemiddelde 0 is en de variantie 1, spreekt men van de *standaardnormale curve* of *standaardnormale dichtheidsfunctie*.

Een lukrake observatie uit een reeks gegevens wiens verdeling de Normale curve volgt, wordt een **Normaal verdeelde observatie** genoemd. Dergelijke observaties komen frequent voor: voor heel wat reeksen gegevens die symmetrisch verdeeld zijn, vormt de Normale curve met <span class="math inline">\$\\mu\$</span> gelijk aan <span class="math inline">\$\\bar x\$</span> en <span class="math inline">\$\\sigma\$</span> gelijk aan <span class="math inline">\$s\_x\$</span> immers een goede benadering voor het histogram.

Voor Normaal verdeelde gegevens geeft de oppervlakte onder de Normale curve tussen 2 willekeurige getallen <span class="math inline">\$a\$</span> en <span class="math inline">\$b\$</span> het percentage van de observaties weer dat tussen deze 2 getallen gelegen is. Op die manier laat de Normale curve toe om, enkel op basis van kennis van het gemiddelde en de standaarddeviatie, na te gaan welk percentage van de gegevens bij benadering tussen 2 willekeurige getallen <span class="math inline">\$a\$</span> en <span class="math inline">\$b\$</span> gelegen is.

Om deze berekening uit te voeren, gaan we als volgt te werk. Zij <span class="math inline">\$X\$</span> een lukrake meting uit een reeks Normaal verdeelde gegevens met gemiddelde <span class="math inline">\$\\mu\$</span> en standaarddeviatie <span class="math inline">\$\\sigma\$</span>. Dan noteren we met <span class="math inline">\$P(X\\leq b)\$</span> de oppervlakte onder de Normale curve die links van <span class="math inline">\$b\$</span> gelegen is, en met <span class="math inline">\$P(a\\leq X\\leq b)\$</span> de oppervlakte onder de Normale curve tussen <span class="math inline">\$a\$</span> en <span class="math inline">\$b\$</span>. Hierbij is<a href="#fn15" id="fnref15" class="footnoteRef"><sup>15</sup></a> <span class="math display">\\$$\\begin{equation\*} P(a\\leq X\\leq b)=P(X\\leq b)-P(X\\leq a) \\end{equation\*}\\$$</span>

Om <span class="math inline">\$P(a\\leq X\\leq b)\$</span> te berekenen, hebben we dus enkel een strategie nodig om voor een willekeurig getal <span class="math inline">\$x\$</span>, het getal <span class="math inline">\$F(x) = P(X \\leq x)\$</span> uit te rekenen. Dit staat uitgezet in functie van <span class="math inline">\$x\$</span> in Figuur [4.8](index.md) (rechtsboven) voor <span class="math inline">\$\\mu=80\$</span> en <span class="math inline">\$\\sigma=12\$</span> en wordt een *distributiefunctie* genoemd.

<span id="def:unnamed-chunk-48" class="definition">**Definitie 4.9 (distributiefunctie)** </span>De functie die voor elk getal <span class="math inline">\$x\$</span> uitdrukt wat de kans is dat een lukrake meting <span class="math inline">\$X\$</span> met gekende verdeling (bvb. een Normale verdeling) kleiner of gelijk is aan <span class="math inline">\$x\$</span>, wordt de **distributiefunctie** van die verdeling genoemd.

**Einde definitie**

Omdat de Normale dichtheidsfunctie zeer complex is, blijkt dat het getal <span class="math inline">\$F(x)\$</span> niet expliciet uit te rekenen is. Om die reden heeft men de getallen <span class="math inline">\$F(x)\$</span> voor de standaardnormale verdelingsfunctie getabuleerd. Voor deze standaardnormale curve duidt men voor een willekeurige waarde <span class="math inline">\$z\$</span>, het getal <span class="math inline">\$F(z)\$</span> met <span class="math inline">\$\\Phi(z)\$</span> aan. Omwille van de symmetrie rond 0 van de standaardnormale curve kan de waarde van <span class="math inline">\$\\Phi(-z)\$</span> dan uit de waarde van <span class="math inline">\$\\Phi(z)\$</span> worden afgeleid als <span class="math display">\\$$\\begin{equation\*} \\Phi(-z)= 1- \\Phi(z) \\end{equation\*}\\$$</span>

Deze uitdrukking geeft aan dat voor een reeks standaardnormaal verdeelde metingen, het percentage dat kleiner is dan <span class="math inline">\$-z\$</span> gelijk is aan het percentage dat groter is dan <span class="math inline">\$z\$</span>.

Om nu <span class="math inline">\$P(a\\leq X\\leq b)\$</span> te berekenen op basis van de tabellen voor de standaardnormale verdeling gaan we als volgt te werk. Vooreerst kan men aantonen dat het resultaat van een lineaire transformatie <span class="math inline">\$aX+b\$</span> op een Normaal verdeelde meting <span class="math inline">\$X\$</span> met gemiddelde <span class="math inline">\$\\mu\$</span> en standaarddeviatie <span class="math inline">\$\\sigma\$</span> terug een Normaal verdeelde meting toevalsveranderlijke is, maar nu met gemiddelde <span class="math inline">\$a\\mu+b\$</span> en standaarddeviatie <span class="math inline">\$\|a\|\\sigma\$</span>. Op die manier kan men elke Normaal verdeelde meting met gemiddelde <span class="math inline">\$\\mu\$</span> en standaarddeviatie <span class="math inline">\$\\sigma\$</span> omzetten naar een standaardnormale meting door ze als volgt te *standaardiseren*: <span class="math display">\\$$\\begin{equation\*} Z = \\frac{X- \\mu}{\\sigma} \\end{equation\*}\\$$</span>

Verifieer dat <span class="math inline">\$Z\$</span> inderdaad gemiddelde 0 en standaarddeviatie 1 heeft!

Aangezien voor een willekeurig getal <span class="math inline">\$x\$</span> <span class="math display">\\$$\\begin{equation\*} X\\leq x \\Leftrightarrow \\frac{X-\\mu}{\\sigma} \\leq \\frac{x-\\mu}{\\sigma} \\end{equation\*}\\$$</span> vinden we nu dat <span class="math display">\\$$\\begin{eqnarray\*} P(a \\leq X \\leq b) & = & P\\left(\\frac{a-\\mu}{\\sigma} \\leq Z \\leq \\frac{b-\\mu% }{\\sigma} \\right) \\\\ & = & \\Phi \\left (\\frac{b-\\mu}{\\sigma} \\right ) - \\Phi \\left (\\frac{a-\\mu}{% \\sigma} \\right ) \\end{eqnarray\*}\\$$</span>

De getallen <span class="math inline">\$\\Phi \\left (\\frac{b-\\mu}{\\sigma} \\right )\$</span> en <span class="math inline">\$\\Phi \\left (\\frac{a-\\mu}{\\sigma} \\right )\$</span> kunnen hierbij rechtstreeks uit tabellen of R software worden gehaald. In het vervolg zullen we algemeen de notatie <span class="math inline">\$Z\$</span> gebruiken om een standaardnormaal verdeelde meting aan te duiden.

<span id="exr:unnamed-chunk-49" class="exercise">**Oefening 4.1** </span>

Een labo bepaalt in een visstaal Hg via een methode op basis van AAS. In werkelijkheid bevat het staal (gemiddeld) 1.90 ppm. De meetmethode is echter niet perfect, zoals aangegeven door een standaarddeviatie van 0.10 ppm. Wat is de kans dat de laborant die het staal onderzoekt, een meetresultaat van 2.10 ppm of meer vaststelt?

Om op deze vraag te antwoorden, noteren we met <span class="math inline">\$X\$</span> het meetresultaat van de laborant en berekenen we <span class="math display">\\$$\\begin{eqnarray\*} P(X\\geq 2)&=&P\\left(\\frac{X-\\mu}{\\sigma}\\geq \\frac{2.1-1.9}{0.1}\\right) \\\\ &=&P(Z\\geq 2) = 2.28\\% \\end{eqnarray\*}\\$$</span>

We besluiten dat er 2.28% kans is dat de laborant een meetresultaat van minstens 2.10 ppm zal vaststellen. In R kan dit resultaat als volgt bekomen worden:

``` {.sourceCode .r}
1 - pnorm(2.1, mean = 1.9, sd = 0.1)
```

    ## [1] 0.02275013

waarbij de functie pnorm de distributiefunctie van de Normale verdeling voorstelt.

`**Einde oefening**`

Met <span class="math inline">\$z\_{\\alpha}\$</span> duiden<a href="#fn16" id="fnref16" class="footnoteRef"><sup>16</sup></a> we die waarde aan waar <span class="math inline">\$\\alpha100\\%\$</span> van de oppervlakte onder de standaardnormale curve rechts van zit; m.a.w. waarvoor geldt dat <span class="math inline">\$P(Z \\geq z\_{\\alpha}) = \\alpha\$</span>. Als <span class="math inline">\$Z\$</span> een standaardnormaal verdeelde meting is, dan stelt <span class="math inline">\$z\_{\\alpha}\$</span> bijgevolg het <span class="math inline">\$(1-\\alpha)100\\%\$</span> percentiel van die verdeling voor. Voor <span class="math inline">\$z\_{\\alpha/2}\$</span> geldt dat <span class="math inline">\$P(-z\_{\\alpha/2}\\leq Z \\leq z\_{\\alpha/2}) = 1-\\alpha\$</span>. Bijvoorbeeld, <span class="math inline">\$P( - z\_{0.025}\\leq Z \\leq z\_{0.025}) = 95\\%\$</span>. Voor een reeks standaardnormaal verdeelde metingen bevat het interval <span class="math inline">\$$$-z\_{\\alpha/2},z\_{\\alpha/2}$$\$</span> dus <span class="math inline">\$(1-\\alpha)100\\%\$</span> van de observaties.

Stel dat <span class="math inline">\$X\$</span> een Normaal verdeelde meting is met gemiddelde <span class="math inline">\$\\mu\$</span> en standaarddeviatie <span class="math inline">\$\\sigma\$</span>. Dan geldt dat <span class="math display">\\$$\\begin{equation\*} P\\left( - z\_{\\alpha/2}\\leq \\frac{X - \\mu}{\\sigma} \\leq z\_{\\alpha/2}\\right) = 1-\\alpha . \\end{equation\*}\\$$</span> Hieruit volgt dat <span class="math display">\\$$\\begin{equation\*} P( \\mu - z\_{\\alpha/2} \\sigma \\leq X \\leq \\mu + z\_{\\alpha/2} \\sigma ) = 1-\\alpha . \\end{equation\*}\\$$</span>

Voor een reeks Normaal verdeelde metingen met gemiddelde <span class="math inline">\$\\mu\$</span> en standaarddeviatie <span class="math inline">\$\\sigma\$</span> bevat het interval <span class="math inline">\$$$\\mu-z\_{\\alpha/2}\\sigma,\\mu+z\_{\\alpha/2}\\sigma$$\$</span> dus <span class="math inline">\$(1-\\alpha)100\\%\$</span> van de observaties. In de praktijk worden de parameters <span class="math inline">\$\\mu\$</span> en <span class="math inline">\$\\sigma\$</span> hierbij vervangen door <span class="math inline">\$\\bar x\$</span> en <span class="math inline">\$s\_x\$</span>.

Het resulterende interval <span class="math inline">\$$$\\bar x-z\_{\\alpha/2}s\_x,\\bar x+z\_{\\alpha/2}s\_x$$\$</span> wordt vaak gebruikt<a href="#fn17" id="fnref17" class="footnoteRef"><sup>17</sup></a>, o.a. in de klinische chemie, om *referentie-intervallen* te berekenen voor een test ter opsporing van een bepaalde pathologie. Eenmaal zo’n referentie-interval, ook wel *normaal interval* genoemd, werd bepaald, wordt het testresultaat van een patiënt met de vermoede pathologie vergeleken met het interval. Een resultaat buiten het interval is dan indicatief voor de aanwezigheid van de pathologie.

Bij het bepalen van referentie-intervallen is het noodzakelijk om de methode eerst te testen bij mensen zonder de pathologie in kwestie. Voor dit doel worden \`normale en gezonde vrijwilligers’ aangezocht. Vaak worden hiertoe collega’s genomen uit het laboratorium dat de test heeft ontwikkeld, hoewel dit allesbehalve ideaal is. Immers, mensen die in een zelfde laboratorium werken, zijn blootgesteld aan dezelfde werkomgeving, die op zijn beurt een invloed kan hebben op hun bloedsamenstelling. Bijgevolg is de bloedsamenstelling van de studiepersonen mogelijks niet representatief voor een normale, gezonde populatie, hetgeen kan leiden tot vertekende referentie-intervallen. In deze cursus zullen we een referentie-interval meer algemeen als volgt definiëren.

<span id="def:unnamed-chunk-51" class="definition">**Definitie 4.10 (referentie-interval)** </span>Een **<span class="math inline">\$(1-\\alpha)100\\%\$</span> referentie-interval** voor een veranderlijke <span class="math inline">\$X\$</span> (bvb. albumine-concentratie in het bloed) in een gegeven studiepopulatie (bvb. volwassen Belgen onder de 60 jaar) is een interval dat zó gekozen werd dat het met <span class="math inline">\$(1-\\alpha)100\\%\$</span> kans de observatie voor een lukraak individu uit die populatie bevat. Voor een Normaal verdeelde veranderlijke <span class="math inline">\$X\$</span> met gemiddelde <span class="math inline">\$\\mu\$</span> en standaarddeviatie <span class="math inline">\$\\sigma\$</span> kan dit berekend worden als <span class="math display">\\$$\\begin{equation\*} \[\\mu-z\_{\\alpha/2}\\sigma,\\mu+z\_{\\alpha/2}\\sigma$$ \\end{equation\*}\\\]</span> en geschat worden op basis van een lukrake steekproef als <span class="math display">\\$$\\begin{equation\*} \[\\bar x-z\_{\\alpha/2}s\_x,\\bar x+z\_{\\alpha/2}s\_x$$ \\end{equation\*}\\\]</span>

**Einde definitie**

<span id="exm:unnamed-chunk-52" class="example">**Voorbeeld 4.3 (Referentie-intervallen)** </span>

In het Hoofdstuk [5](../chap-besluit/index.md) statistische besluitvorming handelt de centrale dataset rond een studie naar het effect van het toedienen van een bloeddrukverlagend middel captopril. Alvorens de studie aan te vangen dient men eerst een grenswaarde voor normale bloeddrukwaarden op te stellen om subjecten met normale bloeddrukken van patiënten met hypertensie te kunnen onderscheiden. We zullen hiervoor gebruik maken van een subset van de NHANES studie. In Figuur [4.9](index.md) links wordt een histogram gegeven van alle bloeddruk waarden voor subjecten tussen de 40 en 65 jaar. Rechts wordt het histogram weergegeven voor gezonde subjecten tussen de 40 en 65 jaar, waarbij gezonde personen werden geselecteerd op basis van hun BMI klasse, rokers, status algemene gezondheidsstatus, slaapproblemen, of ze aan diabetes lijden en ze in het verleden hard drugs gebruikten.

``` {.sourceCode .r}
#verwijderen van alle subjecten met ontbrekende waarnemingen
NHANES2=subset(NHANES,!is.na(Race1)&!is.na(Smoke100n)&!is.na(BMI_WHO)%in%!is.na(Age)&!is.na(HardDrugs)&!is.na(HealthGen)&!is.na(Gender)&!is.na(AlcoholYear)&!is.na(BPSys1)&!is.na(BPSys2)&!is.na(BPSys3)&!is.na(SleepTrouble))
NHANES2$bpSys=rowMeans(NHANES2[,c(27,29,31)])
#subset van de personen tussen 40 en 65 jaar
nhanesSub=subset(NHANES2, Age<=65&Age>=40 &!duplicated(ID) )
#De == operator resulteert in een bolean (FALSE of TRUE)

---

[← Het na.rm=TRUE argument wordt gebruikt omdat er](12-het-na-rm-true-argument-wordt-gebruikt-omdat-er.md) · [Up: contents](index.md) · [de & operater is een logische AND →](14-de-operater-is-een-logische-and.md)

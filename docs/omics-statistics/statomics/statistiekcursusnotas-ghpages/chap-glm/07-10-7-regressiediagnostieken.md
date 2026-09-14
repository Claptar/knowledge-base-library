---
title: 10.7 Regressiediagnostieken
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-glm.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-glm.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 10.7 Regressiediagnostieken

**Source:** [`chap-glm.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-glm.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

### <span class="header-section-number">10.7.1</span> Multicollineariteit

Het is interessant om in de R output voor het model met lcavol:lweight interactie ook naar schattingen van de hoofdeffecten te kijken (Sectie [10.5.1](index.md)). De waarden van de schattingen zijn niet alleen verschillend van wat we in het additieve model vonden, maar de standaardfouten zijn nu veel groter! De oorzaak moet gezocht worden in het probleem van multicollineariteit. Wanneer 2 predictoren sterk gecorreleerd zijn, dan delen ze voor een groot stuk dezelfde informatie en is het moeilijk om de afzonderlijke effecten van beiden op de uitkomst te schatten. Dit uit zich in het feit dat de computationele berekening van de kleinste kwadratenschatters onstabiel wordt, in die zin dat kleine wijzigingen aan de gegevens of het toevoegen of weglaten van een predictorvariabele een belangrijke impact kunnen hebben op de grootte, en zelfs het teken, van de geschatte regressieparameters. Een tweede effect van multicollineariteit is dat standaard errors bij de geschatte regressieparameters fel kunnen worden opgeblazen en de bijhorende betrouwbaarheidsintervallen bijgevolg zeer breed kunnen worden. Zolang men enkel predicties tracht te bekomen op basis van het regressiemodel zonder daarbij te extrapoleren buiten het bereik van de predictoren is multicollineariteit geen probleem.

``` {.sourceCode .r}
cor(cbind(prostate$lcavol,prostate$lweight,prostate$lcavol*prostate$lweight))
```

    ##           [,1]      [,2]      [,3]
    ## [1,] 1.0000000 0.1941283 0.9893127
    ## [2,] 0.1941283 1.0000000 0.2835608
    ## [3,] 0.9893127 0.2835608 1.0000000

We zien dat de correlatie inderdaad erg hoog is tussen het log-tumorvolume en de interactieterm. Het is gekend dat hogere orde termen (interacties en kwadratische termen) vaak een sterke correlatie vertonen.

Problemen als gevolg van multicollineariteit kunnen herkend worden aan het feit dat de resultaten onstabiel worden. Zo kunnen grote wijzigingen optreden in de parameters na toevoeging van een predictor, kunnen zeer brede betrouwbaarheidsintervallen bekomen worden voor sommige parameters of kunnen gewoonweg onverwachte resultaten worden gevonden. Meer formeel kan men zich een idee vormen van de mate waarin er van multicollineariteit sprake is door de correlaties te inspecteren tussen elk paar predictoren in het regressiemodel of via een scatterplot matrix die elk paar predictoren uitzet op een scatterplot. Dergelijke diagnostieken voor multicollineariteit zijn echter niet ideaal. Vooreerst geven ze geen idee in welke mate de geobserveerde multicollineariteit de resultaten onstabiel maakt. Ten tweede kan het in modellen met 3 of meerdere predictoren, zeg X1, X2, X3, voorkomen dat er zware multicollineariteit is ondanks het feit dat alle paarsgewijze correlaties tussen de predictoren laag zijn. Dit kan bijvoorbeeld optreden wanneer de correlatie hoog is tussen X1 en een lineaire combinatie van X2 en X3.

Bovenstaande nadelen kunnen vermeden worden door de te onderzoeken, die voor de <span class="math inline">\$j\$</span>-de parameter in het regressiemodel gedefinieerd wordt als <span class="math display">\\$$\\textrm{VIF}\_j=\\left(1-R\_j^2\\right)^{-1}\\$$</span> In deze uitdrukking stelt <span class="math inline">\$R\_j^2\$</span> de meervoudige determinatiecoëfficiënt voor van een lineaire regressie van de <span class="math inline">\$j\$</span>-de predictor op alle andere predictoren in het model. De VIF heeft de eigenschap dat ze gelijk is aan 1 indien de <span class="math inline">\$j\$</span>-de predictor niet lineair geassocieerd is met de andere predictoren in het model, en bijgevolg wanneer de <span class="math inline">\$j\$</span>-de parameter in het model niet onderhevig is aan het probleem van multicollineariteit. De VIF is groter dan 1 in alle andere gevallen. In het bijzonder drukt ze uit met welke factor de geobserveerde variantie op de schatting voor de <span class="math inline">\$j\$</span>-de parameter groter is dan wanneer alle predictoren onafhankelijk zouden zijn. Hoe groter de VIF, hoe minder stabiel de schattingen bijgevolg zijn. Hoe kleiner de VIF, hoe dichter de schattingen dus bij de gezochte populatiewaarden verwacht worden. In de praktijk spreekt men van ernstige multicollineariteit voor een regressieparameter wanneer haar VIF de waarde 10 overschrijdt.

We illustreren dat a.d.h.v. onderstaande voorbeeld.

**Voorbeeld vetpercentage**

Het percentage lichaamsvet van een persoon bepalen is een moeilijke en dure meting. Om die reden werden in het verleden verschillende studies opgezet met als doel het patroon te ontrafelen tussen werkelijk percentage lichaamsvet en verschillende, makkelijker te meten surrogaten. In een studie heeft men voor 20 gezonde vrouwen tussen 25 en 34 jaar het percentage lichaamsvet <span class="math inline">\$Y\$</span>, de dikte van de huidplooi rond de triceps <span class="math inline">\$X\_1\$</span>, de dij-omtrek <span class="math inline">\$X\_2\$</span> en de middenarmomtrek <span class="math inline">\$X\_3\$</span> gemeten. Indien we een nauwkeurig regressiemodel kunnen opstellen op basis van de gegevens, dan zal ons dat toelaten om in de toekomst met behulp van dat model voorspellingen te maken voor het percentage lichaamsvet in gezonde vrouwen tussen 25 en 34 jaar, op basis van de huidplooi rond de triceps, de dij-omtrek en de middenarmomtrek.

<span id="fig:vetScatter"></span> <img src="Statistiek_2019_2020_files/figure-html/vetScatter-1.png" style="width:100.0%" alt="Scatterplot matrix van de dataset bodyfat." />

Figuur 10.6: Scatterplot matrix van de dataset bodyfat.

Wanneer we de 3 predictoren simultaan aan een regressiemodel toevoegen, bekomen we de volgende output.

``` {.sourceCode .r}
lmFat <- lm(Body_fat~Triceps+Thigh+Midarm ,data=bodyfat)
summary(lmFat)
```

    ##
    ## Call:
    ## lm(formula = Body_fat ~ Triceps + Thigh + Midarm, data = bodyfat)
    ##
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max
    ## -3.7263 -1.6111  0.3923  1.4656  4.1277
    ##
    ## Coefficients:
    ##             Estimate Std. Error t value Pr(>|t|)
    ## (Intercept)  117.085     99.782   1.173    0.258
    ## Triceps        4.334      3.016   1.437    0.170
    ## Thigh         -2.857      2.582  -1.106    0.285
    ## Midarm        -2.186      1.595  -1.370    0.190
    ##
    ## Residual standard error: 2.48 on 16 degrees of freedom
    ## Multiple R-squared:  0.8014, Adjusted R-squared:  0.7641
    ## F-statistic: 21.52 on 3 and 16 DF,  p-value: 7.343e-06

``` {.sourceCode .r}
vif(lmFat)
```

    ##  Triceps    Thigh   Midarm
    ## 708.8429 564.3434 104.6060

Hoewel het model meer dan 80% van de variabiliteit in het vetpercentage kan verklaren en dat de F-test die test voor alle predictoren simultaan extreem significant is, is de associatie echter voor geen enkele predictor significant volgens de individuele t-testen. De scatterplot matrix in Figuur [10.6](index.md) geeft aan dat er multicollineariteit aanwezig is wat betreft de predictoren <span class="math inline">\$X\_1\$</span> en <span class="math inline">\$X\_2\$</span>, maar niet meteen wat betreft de middenarmomtrek <span class="math inline">\$X\_3\$</span>. Niettemin bekomen we erg hoge VIFs voor alle model parameters. Dit suggereert dat ook de middenarmomtrek gevoelig is aan ernstige multicollineariteit en bijgevolg dat scatterplot matrices inderdaad slechts een beperkt licht werpen op het probleem van multicollineariteit. De VIF varieert van 105-709, hetgeen aantoont dat de (kwadratische) afstand tussen de schattingen voor de regressieparameters en hun werkelijke waarden 105 tot 709 keer hoger kan worden verwacht dan wanneer er geen multicollineariteit zou zijn. Hoewel de paarsgewijze correlatie tussen Midarm en Triceps en Midarm en Thigh laag is, toont de regressie van Midarm op Triceps en Thigh echter aan dat beide variabelen samen 99% van de variabiliteit in de variabiliteit van Midarm kunnen verklaren, wat er voor zorgt dat er ook voor Midarm een extreem hoge multicollineariteit is.

``` {.sourceCode .r}
lmMidarm <- lm(Midarm ~ Triceps+Thigh,data=bodyfat)
summary(lmMidarm)
```

    ##
    ## Call:
    ## lm(formula = Midarm ~ Triceps + Thigh, data = bodyfat)
    ##
    ## Residuals:
    ##      Min       1Q   Median       3Q      Max
    ## -0.58200 -0.30625  0.02592  0.29526  0.56102
    ##
    ## Coefficients:
    ##             Estimate Std. Error t value Pr(>|t|)
    ## (Intercept) 62.33083    1.23934   50.29   <2e-16 ***
    ## Triceps      1.88089    0.04498   41.82   <2e-16 ***
    ## Thigh       -1.60850    0.04316  -37.26   <2e-16 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ##
    ## Residual standard error: 0.377 on 17 degrees of freedom
    ## Multiple R-squared:  0.9904, Adjusted R-squared:  0.9893
    ## F-statistic: 880.7 on 2 and 17 DF,  p-value: < 2.2e-16

**Einde voorbeeld**

We evalueren nu de VIF in het prostaatkanker voorbeeld voor het additieve model en het model met interactie.

``` {.sourceCode .r}
vif(lmVWS)
```

    ##   lcavol  lweight      svi
    ## 1.447048 1.039188 1.409189

``` {.sourceCode .r}
vif(lmVWS_IntVW)
```

    ##         lcavol        lweight            svi lcavol:lweight
    ##      76.193815       1.767121       1.426646      80.611657

We zien dat de variance inflation factors voor het additieve model laag zijn, ze liggen allen dicht bij 1. Deze voor het model met interactie zijn echter hoog, voor lcavol en de interactie liggen ze respectievelijk op 76.2 en 80.6. Wat wijst op zeer ernstige multicollineariteit.

Merk op dat dit voor interactietermen vaak wordt veroorzaakt door het feit dat het hoofdeffect een andere interpretatie krijgt. Voor lcavol wordt dit b.v. het effect van het log-tumorvolume bij een log-prostaatgewicht van 0. Dit kan uiteraard niet voorkomen, alle log-prostaatgewichten liggen tussen 2.37 en 6.108 en berust dus op sterke extrapolatie. In de literatuur wordt daarom vaak voorgesteld om de variabelen te centreren rond het gemiddelde wanneer men hogere orde termen in het model opneemt. Dat is echter niet nodig, we weten immers dat het effect van het log-tumorvolume in het model met de lcavol:lweight interactie niet kan worden bestudeerd zonder het log-prostaatgewicht in rekening te brengen. We zullen in de practica zien dat we i.p.v. de data te centreren evengoed een test kunnen uitvoeren voor het effect van lcavol bij het gemiddelde log-prostaatgewicht, wat de interpretatie is voor het effect van lcavol bij het gecentreerde model.

### <span class="header-section-number">10.7.2</span> Invloedrijke observaties

In onderstaande code wordt data gesimuleerd om de impact van outliers te illustreren.

``` {.sourceCode .r}
set.seed(112358)
nobs<-20
sdy<-1
x<-seq(0,1,length=nobs)
y<-10+5*x+rnorm(nobs,sd=sdy)
x1<-c(x,0.5)
y1 <- c(y,10+5*1.5+rnorm(1,sd=sdy))
x2 <- c(x,1.5)
y2 <- c(y,y1[21])
x3 <- c(x,1.5)
y3 <- c(y,11)
plot(x,y,xlim=range(c(x1,x2,x3)),ylim=range(c(y1,y2,y3)))
points(c(x1[21],x2[21],x3[21]),c(y1[21],y2[21],y3[21]),pch=as.character(1:3),col=2:4)
abline(lm(y~x),lwd=2)
abline(lm(y1~x1),col=2,lty=2,lwd=2)
abline(lm(y2~x2),col=3,lty=3,lwd=2)
abline(lm(y3~x3),col=4,lty=4,lwd=2)
legend("topleft",col=1:4,lty=1:4,legend=paste("lm",c("",as.character(1:3))),text.col=1:4)
```

<span id="fig:influential"></span> <img src="Statistiek_2019_2020_files/figure-html/influential-1.png" style="width:100.0%" alt="Impact van outliers op de regressie. Regressie zonder outliers (zwart), regressie met outlier 1 (groen), regressie met outlier 2 (rood), regressie met outlier 3 (blauw)." />

Figuur 10.7: Impact van outliers op de regressie. Regressie zonder outliers (zwart), regressie met outlier 1 (groen), regressie met outlier 2 (rood), regressie met outlier 3 (blauw).

Een dataset bevat vaak extreme observaties voor zowel de uitkomst <span class="math inline">\$Y\$</span> als de predictoren <span class="math inline">\$X\$</span>. Deze kunnen de geschatte regressieparameters en regressielijn sterk beïnvloeden. Dat is niet verwonderlijk vermits de regressielijn de gemiddelde uitkomst voorstelt in functie van <span class="math inline">\$X\$</span> en gemiddelden zeer gevoelig zijn aan outliers. Figuur [10.7](index.md) toont een puntenwolk met 3 afwijkende observaties samen met 4 lineaire regressielijnen één zonder en één met elk van deze observaties. Merk op dat de regressielijn in bijzondere mate afwijkt wanneer observatie 3 wordt opgenomen in de dataset. Dit kan als volgt worden verklaard. De aanwezigheid van observatie 1 impliceert dat de regressielijn (en bijgevolg het intercept) naar boven wordt getrokken, maar heeft verder geen invloed op het patroon van de regressielijn. Observatie 2 is extreem, maar heeft geen impact op de regressielijn omdat ze het patroon van de rechte volgt. Hoewel observatie 3 niet met een zeer extreme uitkomst <span class="math inline">\$y\$</span> overeenstemt, zal deze observatie toch het meest invloedrijk zijn omdat de predictorwaarde <span class="math inline">\$x\$</span> en, in het bijzonder, de <span class="math inline">\$(x,y)\$</span>-combinatie zeer afwijkend is.

Het spreekt voor zich dat het niet wenselijk is dat een enkele observatie het resultaat van een lineaire regressie-analyse grotendeels bepaalt. We wensen daarom over diagnostieken te beschikken die ons toelaten om extreme observaties op te sporen. *Residu’s* geven weer hoe ver de uitkomst afwijkt van de regressielijn en kunnen bijgevolg gebruikt worden om extreme uitkomsten te identificeren. In het bijzonder hebben we eerder vermeld dat residu’s bij benadering Normaal verdeeld zijn wanneer het model correct is en de uitkomst Normaal verdeeld (bij vaste predictorwaarden) met homogene variantie. Of een residu extreem is, kan in dat opzicht geverifieerd worden door haar te vergelijken met de Normale verdeling. Stel bijvoorbeeld dat men over 100 observaties beschikt, dan verwacht men dat ongeveer 5% van de residu’s in absolute waarde extremer zijn dan 1.96<span class="math inline">\$\\hat{\\sigma}\$</span>. Indien men veel meer extreme residu’s observeert, dan is er een indicatie op outliers.

In de literatuur heeft men een aantal modificaties van residu’s ingevoerd met als doel deze nuttiger te maken voor de detectie van outliers. *Studentized residu’s* zijn een transformatie van de eerder gedefinieerde residu’s die <span class="math inline">\$t\$</span>-verdeeld zijn met <span class="math inline">\$n-1\$</span> vrijheidsgraden onder de onderstellingen van het model. Outliers kunnen aldus nauwkeuriger worden opgespoord door na te gaan of veel meer dan 5% van de studentized residu’s in absolute waarde het 97.5% percentiel van de <span class="math inline">\$t\_{n-1}\$</span>-verdeling overschrijden.

Extreme predictorwaarden kunnen in principe opgespoord worden via een scatterplot matrix voor de uitkomst en verschillende predictoren. Wanneer er meerdere predictoren zijn, hebben deze echter ernstige tekortkomingen omdat het een combinatie van meerdere predictoren kan zijn die ongewoon is en dit niet kan opgespoord worden via dergelijke grafieken. Om die reden is het veel zinvoller om de zogenaamde *leverage (invloed, hefboom)* van elke observatie te onderzoeken. Dit is een diagnostische maat voor de mogelijkse invloed van predictor-observaties (in tegenstelling tot de residu’s die een diagnostische maat vormen voor de invloed van de uitkomsten). In het bijzonder is de leverage van de <span class="math inline">\$i\$</span>-de observatie een maat voor de afstand van predictorwaarde voor de <span class="math inline">\$i\$</span>-de observatie tot de gemiddelde predictorwaarde in de steekproef. Hieruit volgt bijgevolg dat indien de leverage voor de <span class="math inline">\$i\$</span>-de observatie groot is, ze predictorwaarden heeft die sterk afwijken van het gemiddelde. In dat geval heeft die observatie mogelijks ook grote invloed op de regressieparameters en predicties. Leverage waarden variëren normaal tussen <span class="math inline">\$1/n\$</span> en 1 en zijn gemiddeld <span class="math inline">\$(p+1)/n\$</span> met <span class="math inline">\$p+1\$</span> het aantal ongekende parameters (intercept + <span class="math inline">\$p\$</span> hellingen). Een extreme leverage wordt typisch aanschouwd als een waarde groter dan <span class="math inline">\$2p/n\$</span>.

### <span class="header-section-number">10.7.3</span> Cook’s distance

Een meer rechtstreekse maat om de invloed van elke observatie op de regressie-analyse uit te drukken is de *Cook’s distance*. De Cook’s distance voor de <span class="math inline">\$i\$</span>-de observatie is een diagnostische maat voor de invloed van die observatie op alle predicties of, equivalent, voor haar invloed op *alle* geschatte parameters. Men bekomt deze door elke predictie <span class="math inline">\$\\hat{Y}\_j\$</span> die men op basis van het regressiemodel heeft bekomen voor de <span class="math inline">\$j\$</span>-de uitkomst, <span class="math inline">\$j=1,...,n\$</span>, te vergelijken met de overeenkomstige predictie <span class="math inline">\$\\hat{Y}\_{j(i)}\$</span> die men zou bekomen indien de <span class="math inline">\$i\$</span>-de observatie niet gebruikt werd om het regressiemodel te fitten <span class="math display">\\$$D\_i=\\frac{\\sum\_{j=1}^n(\\hat{Y}\_j-\\hat{Y}\_{j(i)})^2}{p\\textrm{MSE}}\\$$</span> Indien de Cook’s distance <span class="math inline">\$D\_i\$</span> groot is, dan heeft de <span class="math inline">\$i\$</span>-de observatie een grote invloed op de predicties en geschatte parameters. In het bijzonder stelt men dat een extreme Cook’s distance het 50% percentiel van de <span class="math inline">\$F\_{p+1,n-(p+1)}\$</span>-verdeling overschrijdt.

Deze plots komen standaard bij diagnose van het lineair model. We evalueren dit voor het additieve model en het model met de lcavol:lweight interactie voor de prostaatkanker studie.

``` {.sourceCode .r}
par(mfrow=c(2,2))
plot(lmVWS,which=5)
plot(lmVWS_IntVW,which=5)
plot(cooks.distance(lmVWS),type="h",ylim=c(0,1),main="Additive model")
abline(h=qf(0.5,length(lmVWS$coef),nrow(prostate)-length(lmVWS$coef)),lty=2)
plot(cooks.distance(lmVWS_IntVW),type="h",ylim=c(0,1), main="Model with lcavol:lweight interaction")
abline(h=qf(0.5,length(lmVWS_IntVW$coef),nrow(prostate)-length(lmVWS_IntVW$coef)),lty=2)
```

<span id="fig:prosCooksAdditiveInt"></span> <img src="Statistiek_2019_2020_files/figure-html/prosCooksAdditiveInt-1.png" style="width:100.0%" alt="Evaluatie van de invloed van individuele observaties op het additieve model (links) en het model met de lcavol:lweight interactie (rechts)." />

Figuur 10.8: Evaluatie van de invloed van individuele observaties op het additieve model (links) en het model met de lcavol:lweight interactie (rechts).

Het is duidelijk dat observatie 32 een grote leverage heeft. Het heeft in het model met interactie ook de grootste invloed van alle datapunten op de fit van het model.

Eenmaal men vastgesteld heeft dat een observatie invloedrijk is, kan men zogenaamde *DFBETAS* gebruiken om te bepalen op welke parameter(s) ze een grote invloed uitoefent. De DFBETAS van de <span class="math inline">\$i\$</span>-de observatie vormen een diagnostische maat voor de invloed van die observatie *op elke regressieparameter afzonderlijk*, in tegenstelling tot de Cook’s distance die de invloed op alle parameters tegelijk evalueert. In het bijzonder bekomt men de DFBETAS voor de <span class="math inline">\$i\$</span>-de observatie en de <span class="math inline">\$j\$</span>-de parameter door de <span class="math inline">\$j\$</span>-de parameter <span class="math inline">\$\\hat{\\beta}\_j\$</span> te vergelijken met de parameter <span class="math inline">\$\\hat{\\beta}\_{j(i)}\$</span> die men zou bekomen indien het regressiemodel gefit werd zonder de <span class="math inline">\$i\$</span>-de observatie in de analyse te betrekken: <span class="math display">\\$$\\textrm{DFBETAS}\_{j(i)}=\\frac{\\hat{\\beta}\_{j}-\\hat{\\beta}\_{j(i)}}{\\textrm{SD}(\\hat{\\beta}\_{j})}\\$$</span> Uit bovenstaande uitdrukking volgt dat het teken van de DFBETAS voor de <span class="math inline">\$i\$</span>-de observatie aangeeft of het weglaten van die observatie uit de analyse een stijging (DFBETAS<span class="math inline">\$&lt;0\$</span>) of daling (DFBETAS<span class="math inline">\$&gt;0\$</span>) in de overeenkomstige parameter veroorzaakt. In het bijzonder stelt men dat een DFBETAS extreem is wanneer ze 1 overschrijdt in kleine tot middelgrote datasets en <span class="math inline">\$2/\\sqrt{n}\$</span> overschrijdt in grote datasets.

``` {.sourceCode .r}
par(mfrow=c(2,2))
dfbetasPlots(lmVWS)
```

<span id="fig:prosDfBetasAdditive"></span> <img src="Statistiek_2019_2020_files/figure-html/prosDfBetasAdditive-1.png" style="width:100.0%" alt="DFBETAS voor additieve model in prostaatkanker." />

Figuur 10.9: DFBETAS voor additieve model in prostaatkanker.

``` {.sourceCode .r}
par(mfrow=c(2,2))
dfbetasPlots(lmVWS_IntVW)
```

<span id="fig:prosDfBetasInt"></span> <img src="Statistiek_2019_2020_files/figure-html/prosDfBetasInt-1.png" style="width:100.0%" alt="DFBETAS voor model met lcavol:lweight interactie." />

Figuur 10.10: DFBETAS voor model met lcavol:lweight interactie.

De Cooks distances en de DFBETAS plots geven aan dat observatie 32 het grootste effect heeft op de regressieparameters. Daarnaast heeft deze observatie ook een extreme “influence”.

We gaan observatie 32 nu wat beter bestuderen.

``` {.sourceCode .r}
exp(prostate[32,"lweight"])
```

    ## [1] 449.25

``` {.sourceCode .r}
boxplot(exp(prostate$lweight),ylab="Prostaatgewicht (g)")
```

<span id="fig:prosInfl"></span> <img src="Statistiek_2019_2020_files/figure-html/prosInfl-1.png" style="width:100.0%" alt="Boxplot met outlier voor prostaatgewicht." />

Figuur 10.11: Boxplot met outlier voor prostaatgewicht.

Wanneer we het gewicht terugtransformeren naar de originele schaal zien we dat het prostaatgewicht voor deze patiënt449.25g bedraagt. De prostaat van een man heeft gewoonlijk een gewicht van 20-30 gram en het kan vergroten tot 50-100 gram. Een prostaatgewicht van meer dan 400 gram komt dus niet voor. De auteurs die de dataset uit de originele publicatie hebben opgenomen in een handboek, hebben gerapporteerd dat ze een tikfout hebben gemaakt en ze hebben het extreme prostaat gewicht later gecorrigeerd naar 49.25 gram, het gewicht dat in de originele publicatie werd gerapporteerd.

Ga zelf na welke invloed het corrigeren van het prostaatgewicht heeft op het geschatte regressiemodel.

---

[← 10.6 ANOVA Tabel](06-10-6-anova-tabel.md) · [Up: contents](index.md)

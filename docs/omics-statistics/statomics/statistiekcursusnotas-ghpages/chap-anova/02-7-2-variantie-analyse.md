---
title: 7.2 Variantie-analyse
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-anova.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-anova.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 7.2 Variantie-analyse

**Source:** [`chap-anova.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-anova.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

We leiden de methode af voor de meest eenvoudige uitbreiding met 3 groepen (prostacycline voorbeeld), maar de veralgemening naar g groepen met <span class="math inline">\$g&gt;3\$</span> is triviaal.

### <span class="header-section-number">7.2.1</span> Model {#model-1}

Zoals bij de t-test kunnen we het probleem ook modelleren a.d.h.v een lineair model door gebruik te maken van dummy variabelen (Sectie [6.10](../chap-linReg/index.md)). We zullen hierbij steeds 1 dummy variable minder nodig hebben dan er groepen zijn.

Voor het prostacycline voorbeeld zijn dus twee dummy variabelen nodig en kunnen we de data dus modelleren met onderstaand lineair regressiemodel: Stel dat <span class="math inline">\$Y\_i\$</span> de uitkomst voorstelt van observatie <span class="math inline">\$i\$</span> (<span class="math inline">\$i=1,\\ldots, n\$</span>), dan beschouwen we <span id="eq:regmu3" class="math display">\\$$\\begin{eqnarray} Y\_i &=& g(x\_{i1},x\_{i2}) + \\epsilon\_i\\\\ Y\_i &=& \\beta\_0+\\beta\_1 x\_{i1} +\\beta\_2 x\_{i2} +\\epsilon\_i \\tag{7.1} \\end{eqnarray}\\$$</span>

waarbij de error term opnieuw i.i.d.<a href="#fn46" id="fnref46" class="footnoteRef"><sup>46</sup></a> normaal verdeeld wordt verondersteld met een constante variantie, <span class="math inline">\$\\epsilon\_i\\sim N(0,\\sigma^2)\$</span>, en waarbij de predictoren dummy-variabelen zijn: <span class="math display">\\$$x\_{i1} = \\left\\{ \\begin{array}{ll} 1 & \\text{ als observatie \$i\$ behoort tot middelste dosisgroep (M)} \\\\ 0 & \\text{ als observatie \$i\$ behoort tot een andere dosisgroep} \\end{array}\\right. .\\$$</span> en <span class="math display">\\$$x\_{i2} = \\left\\{ \\begin{array}{ll} 1 & \\text{ als observatie \$i\$ behoort tot de hoogste dosisgroep (H)} \\\\ 0 & \\text{ als observatie \$i\$ behoort tot een andere dosisgroep} \\end{array}\\right. .\\$$</span>

De lage dosisgroep (L) met <span class="math inline">\$x\_{i1}=x\_{i2}=0\$</span> wordt in deze context de **referentiegroep** genoemd.

Zoals in Sectie [6.10](../chap-linReg/index.md) kunnen we het regressie-model opnieuw herschrijven als een model voor elke groep:

1.  Voor observaties in **dosisgroep L** wordt het Model [(7.1)](index.md) <span class="math display">\\$$Y\_i = \\beta\_0+\\epsilon\_i,\\$$</span> met <span class="math inline">\$\\epsilon\_i \\sim N(0,\\sigma^2)\$</span>.

2.  Voor observaties in **dosisgroep M** wordt het Model [(7.1)](index.md) <span class="math display">\\$$Y\_i = \\beta\_0+\\beta\_1 + \\epsilon\_i,\\$$</span> met <span class="math inline">\$\\epsilon\_i \\sim N(0,\\sigma^2)\$</span>.

3.  Voor observaties in **dosisgroep H** wordt het Model [(7.1)](index.md) <span class="math display">\\$$Y\_i = \\beta\_0+\\beta\_2 + \\epsilon\_i\\$$</span> met <span class="math inline">\$\\epsilon\_i \\sim N(0,\\sigma^2)\$</span>.

Hieruit volgt direct de interpretatie van de modelparameters: <span class="math display">\\$$\\begin{eqnarray\*} \\beta\_0 &=& \\text{E}\\left\[Y\_i \\mid \\text{behandeling met lage dosisgroep L}\\right$$ \\\\ \\beta\_1 &=& (\\beta\_0+\\beta\_1)-\\beta\_0 = \\text{E}\\left$$Y\_i \\mid \\text{behandeling M}\\right$$ - \\text{E}\\left$$Y\_i \\mid \\text{behandeling L}\\right$$ \\\\ \\beta\_2 &=& (\\beta\_0+\\beta\_2)-\\beta\_0 = \\text{E}\\left$$Y\_i \\mid \\text{behandeling H}\\right$$-\\text{E}\\left$$Y\_i \\mid \\text{behandeling L}\\right$$. \\end{eqnarray\*}\\\]</span>

of anders geformuleerd:

1.  parameter <span class="math inline">\$\\beta\_0\$</span> is de gemiddelde uitkomst in de lage dosis groep L.
2.  Parameter <span class="math inline">\$\\beta\_1\$</span> is het effect (verschil in gemiddelde concentratie) van groep M t.o.v. groep L.
3.  Parameter <span class="math inline">\$\\beta\_2\$</span> is het effect van hoge dosis groep H t.o.v. groep L.

We herformuleren de modellen gebruik makend van de <span class="math inline">\$\\mu\$</span>-notaties: <span class="math display">\\$$\\begin{eqnarray\*} Y\_{i\\vert \\text{dose=L}} &=& \\beta\_0+\\epsilon\_i = \\mu\_1+\\epsilon\_i \\\\ Y\_{i\\vert \\text{dose=M}} &=& \\beta\_0+\\beta\_1+ \\epsilon\_i = \\mu\_2+\\epsilon\_i \\\\ Y\_{i\\vert \\text{dose=H}} &=& \\beta\_0+\\beta\_2 + \\epsilon\_i = \\mu\_3+\\epsilon\_i . \\end{eqnarray\*}\\$$</span>

met <span class="math inline">\$\\epsilon\_i \\sim N(0,\\sigma^2)\$</span> en met <span class="math display">\\$$ \\mu\_j = \\text{E}\\left\[Y\_i \\mid \\text{behandelingsgroep } j\\right$$.\\\]</span>

De oorspronkelijk nulhypothese <span class="math inline">\$H\_0:\\mu\_1=\\mu\_2=\\mu\_3\$</span> kan equivalent geformuleerd worden als <span class="math display">\\$$H\_0: \\beta\_1=\\beta\_2=0.\\$$</span>

Gezien Model [(7.1)](index.md) een lineair regressiemodel is, kunnen de methoden van lineaire regressie gebruikt worden voor het schatten van de parameters en hun varianties, het opstellen van hypothesetesten en betrouwbaarheidsintervallen. Het testen van <span class="math inline">\$H\_0: \\beta\_1=\\beta\_2=0\$</span> gebeurt d.m.v. een <span class="math inline">\$F\$</span>-test. Hiermee is bijna de volledige oplossing bekomen.

Voor het prostacycline voorbeeld bekomen we het volgende model in het software pakket R:

``` {.sourceCode .r}
model1=lm(prostac~dose,data=prostacyclin)
summary(model1)
```

    ##
    ## Call:
    ## lm(formula = prostac ~ dose, data = prostacyclin)
    ##
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max
    ## -35.167 -17.117  -4.958  17.927  41.133
    ##
    ## Coefficients:
    ##             Estimate Std. Error t value Pr(>|t|)
    ## (Intercept)   40.108      6.150   6.521 2.10e-07 ***
    ## dose25         8.258      8.698   0.949    0.349
    ## dose50        43.258      8.698   4.974 1.99e-05 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ##
    ## Residual standard error: 21.3 on 33 degrees of freedom
    ## Multiple R-squared:  0.458,  Adjusted R-squared:  0.4252
    ## F-statistic: 13.94 on 2 and 33 DF,  p-value: 4.081e-05

We zien dat R eveneens de lage klasse (dose10) kiest als referentie-klasse aangezien er enkel een intercept voorkomt en parameters voor dose25 (M) en dose50 (H). De output laat dus onmiddellijk toe om het effect te vergelijken tussen de middelste en laagste dosisgroep en de hoogste en laagste dosisgroep a.d.h.v. twee t-testen.
De volledige nulhypothese <span class="math inline">\$H\_0: \\beta\_1=\\beta\_2=0\$</span> kan worden geëvalueerd op basis van de F-test onderaan in de output. De p-waarde van de test geeft aan dat er een extreem significant effect is van de arachidonzuurconcentratie op het gemiddelde prostacycline niveau (<span class="math inline">\$p&lt;&lt;0.001\$</span>). In de volgende Sectie tonen we dat de F-test opnieuw opgebouwd wordt d.m.v. kwadratensommen.

### <span class="header-section-number">7.2.2</span> Kwadratensommen en Anova

Net zoals bij enkelvoudige regressie (Sectie [6.9](../chap-linReg/index.md)) kunnen we opnieuw de kwadratensom van de regressie gebruiken bij het opstellen van de F-test. De kwadratensom van de regressie <span class="math display">\\$$\\begin{eqnarray\*} \\text{SSR}&=&\\sum\\limits\_{i=1}^n (\\hat Y\_{i} -\\bar Y)^2 \\end{eqnarray\*}\\$$</span> kan nu worden herschreven als <span class="math display">\\$$\\begin{eqnarray\*} \\text{SSR}&=&\\sum\\limits\_{i=1}^n (\\hat Y\_i -\\bar Y)^2\\\\ &=& \\sum\\limits\_{i=1}^n (\\hat{g} (x\_{i1},x\_{i2}) - \\bar Y)^2\\\\ &=& \\sum\\limits\_{i=1}^n (\\hat\\beta\_0+\\hat\\beta\_1x\_{i1}+\\hat\\beta\_2x\_{i2}) - \\bar Y)^2\\\\ &=& \\sum\\limits\_{i=1}^{n\_1} (\\hat\\beta\_0 - \\bar Y)^2 +\\sum\\limits\_{i=1}^{n\_2} (\\hat\\beta\_0 + \\hat\\beta\_1 - \\bar Y)^2+\\sum\\limits\_{i=1}^{n\_3} (\\hat\\beta\_0 + \\hat\\beta\_2 - \\bar Y)^2\\\\ &=& \\sum\\limits\_{i=1}^{n\_1} (\\bar Y\_1- \\bar Y)^2 +\\sum\\limits\_{i=1}^{n\_2} (\\bar Y\_2- \\bar Y)^2+\\sum\\limits\_{i=1}^{n\_3} (\\bar Y\_3 - \\bar Y)^2\\\\ \\end{eqnarray\*}\\$$</span>

met <span class="math inline">\$n\_1\$</span>, <span class="math inline">\$n\_2\$</span> en <span class="math inline">\$n\_3\$</span> het aantal observaties in elke groep (<span class="math inline">\$n-1=n\_2=n\_3=12\$</span>).

Net als in Sectie [6.9](../chap-linReg/index.md) is SSR een maat voor de afwijking tussen de predicties van het anova model (groepsgemiddelden) en het steekproefgemiddelde van de uitkomsten. Het kan opnieuw geïnterpreteerd worden als een maat voor de afwijking tussen het geschatte Model [(7.1)](index.md) en een gereduceerd model met enkel een intercept. Deze laatste is dus eigenlijk een schatting van het model <span class="math inline">\$g(x\_1,x\_2)=\\beta\_0\$</span>, waarin <span class="math inline">\$\\beta\_0\$</span> geschat wordt door <span class="math inline">\$\\bar{Y}\$</span>. Anders geformuleerd: SSR meet de grootte van het behandelingseffect zodat <span class="math inline">\$\\text{SSR} \\approx 0\$</span> duidt op de afwezigheid van het effect van de dummy variabelen en <span class="math inline">\$\\text{SSR}&gt;0\$</span> duidt op een effect van de dummy variabelen. We voelen opnieuw aan dat <span class="math inline">\$\\text{SSR}\$</span> zal kunnen worden gebruikt voor het ontwikkelen van een statistische test voor de evaluatie van het behandelingseffect. In de anova context heeft SSR <span class="math inline">\$g-1=3-1=2\$</span> vrijheidsgraden: de kwadratensom is opgebouwd op basis van <span class="math inline">\$g=3\$</span> groepsgemiddelden <span class="math inline">\$\\bar Y\_j\$</span> en we verliezen 1 vrijheidsgraad door de schatting van het algemeen steekproefgemiddelde <span class="math inline">\$\\bar Y\$</span>. Wanneer we SSR interpreteren als een verschil tussen twee modellen, bekomen we eveneens een verschil van <span class="math inline">\$g-1=2\$</span> vrijheidsgraden: <span class="math inline">\$g=3\$</span> model parameters in het volledige model (intercept voor referentie klasse en g-1 parameters voor elk van de dummies) en 1 parameter voor het gereduceerde model (enkel intercept).

In een ANOVA setting is het gebruikelijk om de kwadratensom van de regressie te noteren als <span class="math inline">\$\\text{SST}\$</span>, de **kwadratensom van de behandeling (treatment)** of als SSBetween. De kwadratensom van de behandeling geeft inderdaad de variabiliteit weer tussen de groepen. Het meet immers de afwijkingen tussen de groepsgemiddelden <span class="math inline">\$\\bar Y\_j\$</span> en het steekproefgemiddelde <span class="math inline">\$\\bar Y\$</span> (Zie Figuur [7.2](index.md)). We kunnen eveneens opnieuw een overeenkomstige gemiddelde kwadratensom bekomen als <span class="math display">\\$$\\text{MST}=\\text{SST}/(g-1).\\$$</span> met het aantal groepen <span class="math inline">\$g=3\$</span>.

``` {.sourceCode .r}
#attach dataframe dan kunnen we variabele namen rechtstreeks gebruiken
#zonder dataframe naam en $-teken
attach(prostacyclin)
#maak jitter zelf (variatie rond 1,2 en 3
jitIk=runif(36,-.2,.2)+rep(1:3,each=12)
plot(prostac~dose,data=prostacyclin,xlab="Arachidonzuurdosis ",ylab="Prostacycline (ng/ml)")
cols=dose
levels(cols)=c("bisque","coral","darkcyan")
points(jitIk,prostac,col=cols,pch=19)
points(jitIk,prostac,col=4)
points(1:3,predict(model1,data.frame(dose=factor(c(10,25,50)))),pch=17,col=c("bisque","coral","darkcyan"),cex=1.5)
points(1:3,predict(model1,data.frame(dose=factor(c(10,25,50)))),pch=2,col=2,cex=1.5)
abline(h=mean(prostac),lty=1)
for (i in 1:3) lines(c(i-.2,i+.2),rep(predict(model1,data.frame(dose=levels(dose)[i])),2),col=c("bisque","coral","darkcyan")[i],lwd=3)
for (i in 1:36) lines(rep(jitIk[i],2),c(mean(prostac),model1$fitted[i]),col=2,lty=2)
```

<span id="fig:prostacSST"></span> <img src="Statistiek_2019_2020_files/figure-html/prostacSST-1.png" width="672" alt="Interpretatie van de kwadratensom van de behandeling (SST): de som van de kwadratische afwijkingen tussen de groepsgemiddelden ($\bar Y_j$) en het steekproefgemiddelde van de uitkomsten ($\bar Y$)" />

Figuur 7.2: Interpretatie van de kwadratensom van de behandeling (SST): de som van de kwadratische afwijkingen tussen de groepsgemiddelden (<span class="math inline">\$\\bar Y\_j\$</span>) en het steekproefgemiddelde van de uitkomsten (<span class="math inline">\$\\bar Y\$</span>)

``` {.sourceCode .r}
detach(prostacyclin)
```

Opnieuw kunnen we de totale kwadratensom SSTot ontbinden in <span class="math display">\\$$\\text{SSTot} = \\text{SST} + \\text{SSE}.\\$$</span> Waarbij SSTot opnieuw de totale variabiliteit voorstelt, met name de som van de kwadratische afwijking van de uitkomsten <span class="math inline">\$Y\_{i}\$</span> t.o.v. het algemeen gemiddelde prostacycline niveau <span class="math inline">\$\\bar{Y}\$</span> en SSE de residuele variabiliteit of de som van de kwadratische afwijkingen tussen de observaties <span class="math inline">\$Y\_{i}\$</span> en de modelvoorspellingen (hier groepsgemiddelden) <span class="math inline">\$\\hat{g}(x\_{i1},x\_{i2})=\\hat \\mu\_j=\\bar Y\_j\$</span>.

De interpretatie van de deze kwadratensommen worden weergegeven in Figuur [7.3](index.md).

``` {.sourceCode .r}
#attach dataframe dan kunnen we variabele namen rechtstreeks gebruiken
#zonder dataframe naam en $-teken
par(mfrow=c(1,2))
attach(prostacyclin)
#maak jitter zelf (variatie rond 1,2 en 3
plot(prostac~dose,data=prostacyclin,xlab="Arachidonzuurdosis ",ylab="Prostacycline (ng/ml)",main="SStot")
points(jitIk,prostac,col=cols,pch=19)
points(jitIk,prostac,col=4)
points(1:3,predict(model1,data.frame(dose=factor(c(10,25,50)))),pch=17,col=c("bisque","coral","darkcyan"),cex=1.5)
points(1:3,predict(model1,data.frame(dose=factor(c(10,25,50)))),pch=2,col=1,cex=1.5)
abline(h=mean(prostac),lty=1)
for (i in 1:36) lines(rep(jitIk[i],2),c(mean(prostac),prostac[i]),col=4,lty=2)

plot(prostac~dose,data=prostacyclin,xlab="Arachidonzuurdosis ",ylab="Prostacycline (ng/ml)",main="SSE")
points(jitIk,prostac,col=cols,pch=19)
points(jitIk,prostac,col=1)
points(1:3,predict(model1,data.frame(dose=factor(c(10,25,50)))),pch=17,col=c("bisque","coral","darkcyan"),cex=1.5)
points(1:3,predict(model1,data.frame(dose=factor(c(10,25,50)))),pch=2,col=2,cex=1.5)
for (i in 1:3) lines(c(i-.2,i+.2),rep(predict(model1,data.frame(dose=levels(dose)[i])),2),col=c("bisque","coral","darkcyan")[i],lwd=3)
abline(h=mean(prostac),lty=1)
for (i in 1:36) lines(rep(jitIk[i],2),c(prostac[i],model1$fitted[i]),col=1,lty=2)
```

<span id="fig:prostacSSTotSSE"></span> <img src="Statistiek_2019_2020_files/figure-html/prostacSSTotSSE-1.png" width="672" alt="Interpretatie van de totale kwadratensom (SSTot, som van de kwadratische afwijkingen tussen de uitkomsten $Y_{i}$ en het steekproefgemiddelde van de uitkomsten $\bar Y$, links) en van residuele kwadratensom (SSE, som van de kwadratische afwijkingen tussen de uitkomsten $Y_{i}$ en de groepsgemiddelden $\bar Y_j$, rechts)" />

Figuur 7.3: Interpretatie van de totale kwadratensom (SSTot, som van de kwadratische afwijkingen tussen de uitkomsten <span class="math inline">\$Y\_{i}\$</span> en het steekproefgemiddelde van de uitkomsten <span class="math inline">\$\\bar Y\$</span>, links) en van residuele kwadratensom (SSE, som van de kwadratische afwijkingen tussen de uitkomsten <span class="math inline">\$Y\_{i}\$</span> en de groepsgemiddelden <span class="math inline">\$\\bar Y\_j\$</span>, rechts)

``` {.sourceCode .r}
detach(prostacyclin)
```

### <span class="header-section-number">7.2.3</span> Anova-test

Het testen van <span class="math inline">\$H\_0: \\beta\_1=\\ldots=\\beta\_{g-1}=0\$</span> vs <span class="math inline">\$H\_1: \\exists k \\in\\{1,\\ldots,g-1\\} : \\beta\_k \\neq0\$</span><a href="#fn47" id="fnref47" class="footnoteRef"><sup>47</sup></a> kan d.m.v. onderstaande <span class="math inline">\$F\$</span>-test.

<span class="math display">\\$$F = \\frac{\\text{MST}}{\\text{MSE}}\\$$</span> met <span class="math inline">\$\\text{MST}\$</span> de gemiddelde kwadratensom van de behandeling met <span class="math inline">\$g-1\$</span> vrijheidsgraden en <span class="math inline">\$\\text{MSE}\$</span> de gemiddelde residuele kwadratensom uit het niet-gereduceerde model [(7.1)](index.md), deze heeft <span class="math inline">\$n-g\$</span> vrijheidsgraden (met het aantal groepen <span class="math inline">\$g=3\$</span>). De teststatistiek vergelijkt dus variabiliteit verklaard door het model (MST) met de residuele variabiliteit (MSE) of met andere woorden vergelijkt het de variabiliteit tussen groepen (MST) met de variabiliteit binnen groepen (MSE). Grotere waarden voor de test-statistiek zijn minder waarschijnlijk onder de nulhypothese. Wanneer aan alle modelvoorwaarden is voldaan, dan volgt de statistiek onder de nulhypothese opnieuw een F-verdeling, <span class="math inline">\$F \\sim F\_{g-1,n-g}\$</span>, met <span class="math inline">\$g-1\$</span> vrijheidsgraden in de teller en <span class="math inline">\$n-g\$</span> vrijheidsgraden in de noemer.

### <span class="header-section-number">7.2.4</span> Anova Tabel {#anova-tabel}

De kwadratensommen en de F-test worden meestal in een zogenaamde variantie-analyse tabel of een anova tabel gerapporteerd.

|           | Df                  | Sum Sq | Mean Sq | F value      | Pr(&gt;F) |
|-----------|---------------------|--------|---------|--------------|-----------|
| Treatment | vrijheidsgraden SST | SST    | MST     | F-statistiek | p-waarde  |
| Error     | vrijheidsgraden SSE | SSE    | MSE     |              |           |

De anovatabel voor het prostacycline voorbeeld kan als volgt in de R-software worden bekomen

``` {.sourceCode .r}
anova(model1)
```

    ## Analysis of Variance Table
    ##
    ## Response: prostac
    ##           Df Sum Sq Mean Sq F value    Pr(>F)
    ## dose       2  12658  6329.0  13.944 4.081e-05 ***
    ## Residuals 33  14979   453.9
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

We kunnen dus opnieuw besluiten dat er een extreem significant effect is van de dosering van arachidonzuur op de gemiddelde prostacycline concentratie in het bloed bij ratten (<span class="math inline">\$p&lt;&lt;0.001\$</span>).

In Figuur [7.4](index.md) wordt de F-verdeling weergegeven samen met de kritische waarde op het 5% significantie niveau en de geobserveerde F-statistiek voor het prostacycline voorbeeld.

``` {.sourceCode .r}
grid <- seq(0,17,.01)
df1=anova(model1)[1,1]
df2=anova(model1)[2,1]
fval=anova(model1)[1,4]
crit=qf(0.95,df1,df2)
reject=c(crit,grid[which(grid>crit)])
accept=c(grid[which(grid<crit)],crit)
plot(grid,df(grid,df1,df2),type="l",xlab="Density",ylab="F-statistic")
polygon(c(0,accept,crit,0),c(0,df(accept,df1,df2),0,0),col="blue",border="blue")
text(crit/2,.97,labels="aanvaard\n95%",col="blue")
polygon(c(crit,reject,15,crit),c(0,df(reject,df1,df2),0,0),col="red",border="red")
abline(v=crit,col="red",lwd=2)
text(crit+(fval-crit)/2,.97,labels="verwerp\n5%",col="red")
text(pos=4,crit,df(crit,2,33),labels=paste0("F(0.05,",df1,",",df2,")"),col="red")
text(pos=4,fval,df(crit,df1,df2),labels=paste0("f=",round(fval,1)),col="darkorange")
abline(v=fval,col="darkorange",lwd=2,lty=2)
text(15.5,.97,labels=paste0("p-value\n",format(anova(model1)[1,5],digits=2)),col="darkorange")
arrows(x0=17.5,x1=fval,y0=.9,y1=.9,col="darkorange")
```

<span id="fig:prostacF"></span> <img src="Statistiek_2019_2020_files/figure-html/prostacF-1.png" style="width:100.0%" alt="Een F-verdeling met 2 vrijheidsgraden in de teller en 33 in de noemer. Het aanvaardingsgebied wordt weergegeven in blauw, de kritische waarde en de verwerpingsregio bij het $\alpha=5\%$ niveau in rood, en, de geobserveerde f-waarde en de p-waarde worden in oranje." />

Figuur 7.4: Een F-verdeling met 2 vrijheidsgraden in de teller en 33 in de noemer. Het aanvaardingsgebied wordt weergegeven in blauw, de kritische waarde en de verwerpingsregio bij het <span class="math inline">\$\\alpha=5\\%\$</span> niveau in rood, en, de geobserveerde f-waarde en de p-waarde worden in oranje.

Voorbeelden van meerdere F-verdelingen met een verschillend aantal vrijheidsgraden in teller en noemer worden weergegeven in Figuur [7.5](index.md).

``` {.sourceCode .r}
plot(grid,df(grid,1,5),type="l",xlab="Density",ylab="F-statistic",xlim=c(0,5),ylim=c(0,1.5),lwd=2)
lines(grid,df(grid,5,5),type="l",col=2,lwd=2)
lines(grid,df(grid,10,30),type="l",col=3,lwd=2)
lines(grid,df(grid,20,30),type="l",col=4,lwd=2)
lines(grid,df(grid,50,50),type="l",col=5,lwd=2)
legend("topright",lty=1,col=c(1,2,3,4,5),legend=c("F(1,5)","F(5,5)","F(10,30)","F(20,30)","F(50,50)"),lwd=2)
```

<span id="fig:ftheo"></span> <img src="Statistiek_2019_2020_files/figure-html/ftheo-1.png" style="width:100.0%" alt="Meerdere F-verdelingen met een verschillend aantal vrijheidsgraden in de teller en de noemer." />

Figuur 7.5: Meerdere F-verdelingen met een verschillend aantal vrijheidsgraden in de teller en de noemer.

---

[← 7.1 Inleiding {#inleiding}](01-7-1-inleiding-inleiding.md) · [Up: contents](index.md) · [7.3 Post hoc analyse: Meervoudig Vergelijken van Gemiddelden →](03-7-3-post-hoc-analyse-meervoudig-vergelijken-van-gemiddelden.md)

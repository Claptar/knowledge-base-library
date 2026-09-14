---
title: '7.4 Conclusies: Prostacycline Voorbeeld'
source: https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-anova.html
source_file: sources/statomics-statistiekcursusnotas-ghpages/chap-anova.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 7.4 Conclusies: Prostacycline Voorbeeld

**Source:** [`chap-anova.html`](https://github.com/statOmics/statistiekCursusNotas/blob/a1c505bbdddd3d602fa9cc629bef7ee772233d14/chap-anova.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

We overlopen nog eens de volledige analyse voor het prostacycline voorbeeld. Merk op dat we steeds eerst een anova analyse doen voor posthoc testen worden uitgevoerd. De F-test heeft immers een hogere power voor het vinden van een effect van de behandelingen dan paarsgewijze t-testen omdat de F-test alle data gebruikt en voor deze test geen correctie voor multipliciteit nodig is om de algemene nulhypothese te evalueren.

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

``` {.sourceCode .r}
summary(model1.mcp)
```

    ##
    ##   Simultaneous Tests for General Linear Hypotheses
    ##
    ## Multiple Comparisons of Means: Tukey Contrasts
    ##
    ##
    ## Fit: lm(formula = prostac ~ dose, data = prostacyclin)
    ##
    ## Linear Hypotheses:
    ##              Estimate Std. Error t value Pr(>|t|)
    ## 25 - 10 == 0    8.258      8.698   0.949 0.613433
    ## 50 - 10 == 0   43.258      8.698   4.974  < 1e-04 ***
    ## 50 - 25 == 0   35.000      8.698   4.024 0.000922 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## (Adjusted p values reported -- single-step method)

``` {.sourceCode .r}
confint(model1.mcp)
```

    ##
    ##   Simultaneous Confidence Intervals
    ##
    ## Multiple Comparisons of Means: Tukey Contrasts
    ##
    ##
    ## Fit: lm(formula = prostac ~ dose, data = prostacyclin)
    ##
    ## Quantile = 2.4526
    ## 95% family-wise confidence level
    ##
    ##
    ## Linear Hypotheses:
    ##              Estimate lwr      upr
    ## 25 - 10 == 0   8.2583 -13.0736  29.5902
    ## 50 - 10 == 0  43.2583  21.9264  64.5902
    ## 50 - 25 == 0  35.0000  13.6681  56.3319

We kunnen dus concluderen dan er een extreem significant effect is van de arachidonzuurdosering op de gemiddelde prostacycline concentratie in het bloed bij ratten (<span class="math inline">\$p&lt;0.001\$</span>). De gemiddelde prostacycline concentratie is hoger bij de hoge arachidinezuur dosisgroep dan bij de lage en matige dosisgroep (beide <span class="math inline">\$p&lt;0.001\$</span>). De gemiddelde prostacycline concentratie in de hoge dosis groep is respectievelijk 43.3ng/ml (95% BI $$21.9,64.6$$ng/ml) en 35ng/ml (95% BI $$13.6,56.4$$ng/ml) hoger dan in de lage en matige dosis groep. Het verschil in gemiddelde prostacycline concentratie tussen de matige en lage dosisgroep is niet significant (p=0.61, 95% BI op gemiddelde verschil $$-13.1,29.6$$ng/ml). (De p-waarden en betrouwbaarheidsintervallen van de post-hoc tests werden gecorrigeerd voor multipliciteit d.m.v. de Tukey methode).

Merk op dat we eveneens niet significante resultaten vermelden. Het is namelijk belangrijk om eveneens negatieve resultaten te rapporteren!

------------------------------------------------------------------------

1.  onafhankelijk en identiek verdeeld (i.i.d., independent and identically distributed)[↩](index.md)

2.  Onder <span class="math inline">\$H\_1\$</span> bestaat er dus minimum 1 dummy-variabele in het model waarvoor de overeenkomstige parameter <span class="math inline">\$\\beta\_k\$</span> verschillend is van nul onder de alternatieve hypothese[↩](index.md)

3.  maar enkel van de data in de twee groepen die getest worden[↩](index.md)

4.  De nulhypothese onterecht verwerpen[↩](index.md)

5.  theoretisch moet dit <span class="math inline">\$5\\%\$</span> zijn, maar we tonen “slechts” het resultaat gebaseerd op 10000 simulaties[↩](index.md)

---

[← 7.3 Post hoc analyse: Meervoudig Vergelijken van Gemiddelden](03-7-3-post-hoc-analyse-meervoudig-vergelijken-van-gemiddelden.md) · [Up: contents](index.md)

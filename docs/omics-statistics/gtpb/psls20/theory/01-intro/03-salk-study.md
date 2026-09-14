---
title: Salk Study
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/01-intro.Rmd
source_file: sources/gtpb-psls20/theory/01-intro.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Salk Study

**Source:** [`theory/01-intro.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/01-intro.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- In 1916, the US experienced the first large epidemic of polio.
- John Salk developed a vaccine with promising results in the lab in the early fifties.
- In 1954, the National Foundation
for Infantile Paralysis (NFIP) has setup a large study to assess the effectiveness of the Salk vaccine.
- Suppose that the NFIP would have vaccinated a large number of children in 1954 and would have observed that the polio incidence in 1954 was lower than in 1953. Could they have concluded that the vaccine was effective?

---

## NFIP Study
### Design

- Large simultaneous study with cases, vaccinated children, and controls,  non-vaccinated children.
- All schools in districts with high polio incidence
- Cases: children with consent for vaccination from second grade of primary school.
- Controls: children from  first and third grade.

### Data
```r
nfip<-data.frame(group=c("cases","control","noConcent"),grade=c("g2","g1g3","g2"),vaccin=c("yes","no","no"),total=c(221998,725173,123605),polio=c(54,391,56))
nfip$noPolio<-nfip$total-nfip$polio
knitr::kable(nfip)
```

Compare polio incidence?

```r
nfip$incidencePM<-round(nfip$polio/nfip$total*1e6,0)
knitr::kable(nfip)
```

What can we conclude?

---

## Confounding


```r
plot(c(0,0,1),c(-2,2,0),pch=c("S","V","P"),xaxt="none",yaxt="none",axes=FALSE,xlab="",ylab="",cex=4,ylim=c(-2.2,2.2))
arrows(x0=0.1,x1=.9,y0=1.8,y1=0.1,lwd=4)
arrows(x0=0.1,x1=.9,y0=-1.8,y1=-0.2,lwd=4)
arrows(x0=0,x1=0,y0=-1.4,y1=1.4,lwd=4)
```


- We observe a lower polio (P) incidence for children for who no consent was given than for the children in the control group.

- Consent for vaccination (V) was associated with the socio-economic status (S).

- Children of lower socio-economic status were more resistant to the disease.

- The groups of cases and controls are not comparable:
    - difference in age,
    - difference in socio-economic status and
    - difference in susceptible for disease.

---

## Salk Study

### Design
A new study was conducted: Randomized double blind study

  - Children are assigned at random to the control or case treatment arm after consent was given by the parents.
  - Control: vaccination with placebo
  - Treatment: vaccination with vaccine
  - double blinding:
    - parents did not know if their child was vaccinated or received the placebo
    - care-giver/researchers did not know if the child was vaccinated  or received placebo

---

### Data

```r
salk<-data.frame(group=c("cases","control","noConcent"),treatment=c("vaccine","placebo","none"),total=c(200745,
201229, 338778),polio=c(57,142,157))
salk$noPolio<-salk$total-salk$polio
salk$incidencePM<-round(salk$polio/salk$total*1e6,0)
knitr::kable(salk)
```

- We observe a much larger effect now that the cases and the controls are comparable, incidence of `r salk$incidencePM[1]`  and `r salk$incidencePM[2]` per million, respectively.

- The polio incidence for children with no consent remains similar, `r nfip$incidencePM[3]` and `r salk$incidencePM[3]` per million in the NFIP and Salk study, respectively.

---

---

[← Sample to sample variability](02-sample-to-sample-variability.md) · [Up: contents](index.md) · [Scientific Method →](04-scientific-method.md)

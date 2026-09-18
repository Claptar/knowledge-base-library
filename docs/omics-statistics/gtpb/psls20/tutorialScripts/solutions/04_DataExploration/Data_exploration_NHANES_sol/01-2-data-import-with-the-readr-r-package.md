---
title: 2 Data Import with the readr R package
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_NHANES_sol.html
source_file: sources/gtpb-psls20/tutorialScripts/solutions/04_DataExploration/Data_exploration_NHANES_sol.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`tutorialScripts/solutions/04_DataExploration/Data_exploration_NHANES_sol.html`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_NHANES_sol.html) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2 Data Import with the readr R package

Code

- Download Rmd

## Tutorial 1.1: Exploring the NHANES dataset {#tutorial-1.1-exploring-the-nhanes-dataset .title .toc-ignore}

In this tutorial, we will learn how to import, tidy, wrangle and visualize data. We will work with one specific dataset;

## 1 The NHANES dataset

The National Health and Nutrition Examination Survey (NHANES) contains data that has been collected since 1960. For this tutorial, we will make use of the data that were collected between 2009 and 2012, for 10.000 U.S. civilians. The dataset contains a large number of physical, demographic, nutritional and life-style-related parameters.

However, before we can actually start working with data, we will need to learn how to import the required datasets into our Rstudio environment.

## 2 Data Import with the `readr` R package

``` {.sourceCode .r}
library(readr)
```

Let’s try reading in some data. We will begin by reading in the `NHANES.csv` dataset.

``` {.sourceCode .r}
NHANES <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/NHANES.csv")
```

```
## Parsed with column specification:
## cols(
##   .default = col_double(),
##   SurveyYr = col_character(),
##   Gender = col_character(),
##   AgeDecade = col_character(),
##   Race1 = col_character(),
##   Race3 = col_logical(),
##   Education = col_character(),
##   MaritalStatus = col_character(),
##   HHIncome = col_character(),
##   HomeOwn = col_character(),
##   Work = col_character(),
##   BMICatUnder20yrs = col_logical(),
##   BMI_WHO = col_character(),
##   Testosterone = col_logical(),
##   Diabetes = col_character(),
##   HealthGen = col_character(),
##   LittleInterest = col_character(),
##   Depressed = col_character(),
##   SleepTrouble = col_character(),
##   PhysActive = col_character(),
##   TVHrsDay = col_logical()
##   # ... with 12 more columns
## )

## See spec(...) for full column specifications.

## Warning: 20122 parsing failures.
##  row              col           expected     actual                                                                   file
## 5001 Race3            1/0/T/F/TRUE/FALSE Asian      'https://raw.githubusercontent.com/GTPB/PSLS20/master/data/NHANES.csv'
## 5001 BMICatUnder20yrs 1/0/T/F/TRUE/FALSE NormWeight 'https://raw.githubusercontent.com/GTPB/PSLS20/master/data/NHANES.csv'
## 5001 Testosterone     1/0/T/F/TRUE/FALSE 274.95     'https://raw.githubusercontent.com/GTPB/PSLS20/master/data/NHANES.csv'
## 5001 TVHrsDay         1/0/T/F/TRUE/FALSE 2_hr       'https://raw.githubusercontent.com/GTPB/PSLS20/master/data/NHANES.csv'
## 5001 CompHrsDay       1/0/T/F/TRUE/FALSE 3_hr       'https://raw.githubusercontent.com/GTPB/PSLS20/master/data/NHANES.csv'
## .... ................ .................. .......... ......................................................................
## See problems(...) for more details.
```

``` {.sourceCode .r}
head(NHANES) ## take a look at the first rows of the dataset
```

```
## # A tibble: 6 x 76
##      ID SurveyYr Gender   Age AgeDecade AgeMonths Race1 Race3 Education
##   <dbl> <chr>    <chr>  <dbl> <chr>         <dbl> <chr> <lgl> <chr>
## 1 51624 2009_10  male      34 30-39           409 White NA    High Sch~
## 2 51624 2009_10  male      34 30-39           409 White NA    High Sch~
## 3 51624 2009_10  male      34 30-39           409 White NA    High Sch~
## 4 51625 2009_10  male       4 0-9              49 Other NA    <NA>
## 5 51630 2009_10  female    49 40-49           596 White NA    Some Col~
## 6 51638 2009_10  male       9 0-9             115 White NA    <NA>
## # ... with 67 more variables: MaritalStatus <chr>, HHIncome <chr>,
## #   HHIncomeMid <dbl>, Poverty <dbl>, HomeRooms <dbl>, HomeOwn <chr>,
## #   Work <chr>, Weight <dbl>, Length <dbl>, HeadCirc <dbl>, Height <dbl>,
## #   BMI <dbl>, BMICatUnder20yrs <lgl>, BMI_WHO <chr>, Pulse <dbl>,
## #   BPSysAve <dbl>, BPDiaAve <dbl>, BPSys1 <dbl>, BPDia1 <dbl>,
## #   BPSys2 <dbl>, BPDia2 <dbl>, BPSys3 <dbl>, BPDia3 <dbl>,
## #   Testosterone <lgl>, DirectChol <dbl>, TotChol <dbl>, UrineVol1 <dbl>,
## #   UrineFlow1 <dbl>, UrineVol2 <dbl>, UrineFlow2 <dbl>, Diabetes <chr>,
## #   DiabetesAge <dbl>, HealthGen <chr>, DaysPhysHlthBad <dbl>,
## #   DaysMentHlthBad <dbl>, LittleInterest <chr>, Depressed <chr>,
## #   nPregnancies <dbl>, nBabies <dbl>, Age1stBaby <dbl>,
## #   SleepHrsNight <dbl>, SleepTrouble <chr>, PhysActive <chr>,
## #   PhysActiveDays <dbl>, TVHrsDay <lgl>, CompHrsDay <lgl>,
## #   TVHrsDayChild <dbl>, CompHrsDayChild <dbl>, Alcohol12PlusYr <chr>,
## #   AlcoholDay <dbl>, AlcoholYear <dbl>, SmokeNow <chr>, Smoke100 <chr>,
## #   Smoke100n <chr>, SmokeAge <dbl>, Marijuana <chr>, AgeFirstMarij <dbl>,
## #   RegularMarij <chr>, AgeRegMarij <dbl>, HardDrugs <chr>, SexEver <chr>,
## #   SexAge <dbl>, SexNumPartnLife <dbl>, SexNumPartYear <dbl>,
## #   SameSex <chr>, SexOrientation <chr>, PregnantNow <chr>
```

``` {.sourceCode .r}
tail(NHANES) ## take a look at the last rows of the dataset
```

```
## # A tibble: 6 x 76
##      ID SurveyYr Gender   Age AgeDecade AgeMonths Race1 Race3 Education
##   <dbl> <chr>    <chr>  <dbl> <chr>         <dbl> <chr> <lgl> <chr>
## 1 71909 2011_12  male      28 20-29            NA Mexi~ NA    9 - 11th~
## 2 71909 2011_12  male      28 20-29            NA Mexi~ NA    9 - 11th~
## 3 71910 2011_12  female     0 0-9               5 White NA    <NA>
## 4 71911 2011_12  male      27 20-29            NA Mexi~ NA    College ~
## 5 71915 2011_12  male      60 60-69            NA White NA    College ~
## 6 71915 2011_12  male      60 60-69            NA White NA    College ~
## # ... with 67 more variables: MaritalStatus <chr>, HHIncome <chr>,
## #   HHIncomeMid <dbl>, Poverty <dbl>, HomeRooms <dbl>, HomeOwn <chr>,
## #   Work <chr>, Weight <dbl>, Length <dbl>, HeadCirc <dbl>, Height <dbl>,
## #   BMI <dbl>, BMICatUnder20yrs <lgl>, BMI_WHO <chr>, Pulse <dbl>,
## #   BPSysAve <dbl>, BPDiaAve <dbl>, BPSys1 <dbl>, BPDia1 <dbl>,
## #   BPSys2 <dbl>, BPDia2 <dbl>, BPSys3 <dbl>, BPDia3 <dbl>,
## #   Testosterone <lgl>, DirectChol <dbl>, TotChol <dbl>, UrineVol1 <dbl>,
## #   UrineFlow1 <dbl>, UrineVol2 <dbl>, UrineFlow2 <dbl>, Diabetes <chr>,
## #   DiabetesAge <dbl>, HealthGen <chr>, DaysPhysHlthBad <dbl>,
## #   DaysMentHlthBad <dbl>, LittleInterest <chr>, Depressed <chr>,
## #   nPregnancies <dbl>, nBabies <dbl>, Age1stBaby <dbl>,
## #   SleepHrsNight <dbl>, SleepTrouble <chr>, PhysActive <chr>,
## #   PhysActiveDays <dbl>, TVHrsDay <lgl>, CompHrsDay <lgl>,
## #   TVHrsDayChild <dbl>, CompHrsDayChild <dbl>, Alcohol12PlusYr <chr>,
## #   AlcoholDay <dbl>, AlcoholYear <dbl>, SmokeNow <chr>, Smoke100 <chr>,
## #   Smoke100n <chr>, SmokeAge <dbl>, Marijuana <chr>, AgeFirstMarij <dbl>,
## #   RegularMarij <chr>, AgeRegMarij <dbl>, HardDrugs <chr>, SexEver <chr>,
## #   SexAge <dbl>, SexNumPartnLife <dbl>, SexNumPartYear <dbl>,
## #   SameSex <chr>, SexOrientation <chr>, PregnantNow <chr>
```

``` {.sourceCode .r}
#knitr::kable(NHANES[c(1,4,5,6,7,8),c(1,3,4,7,17,20,21,25)],format = "markdown")
NHANES[c(1,4,5,6,7,8),c(1,3,4,7,17,20,21,25)] ## take a look at a subset of the dataset
```

```
## # A tibble: 6 x 8
##      ID Gender   Age Race1 Weight Height   BMI BPSysAve
##   <dbl> <chr>  <dbl> <chr>  <dbl>  <dbl> <dbl>    <dbl>
## 1 51624 male      34 White   87.4   165.  32.2      113
## 2 51625 male       4 Other   17     105.  15.3       NA
## 3 51630 female    49 White   86.7   168.  30.6      112
## 4 51638 male       9 White   29.8   133.  16.8       86
## 5 51646 male       8 White   35.2   131.  20.6      107
## 6 51647 female    45 White   75.7   167.  27.2      118
```

### 2.1 Take a `glimpse()` at your data

The glimpse function allows us to (obviously) take a first, informative glimpse at our data. The function is part of the `dplyr`, which we will explore in much more detail below!

``` {.sourceCode .r}
dplyr::glimpse(NHANES[,1:10])
```

```
## Observations: 10,000
## Variables: 10
## $ ID            <dbl> 51624, 51624, 51624, 51625, 51630, 51638, 51646,...
## $ SurveyYr      <chr> "2009_10", "2009_10", "2009_10", "2009_10", "200...
## $ Gender        <chr> "male", "male", "male", "male", "female", "male"...
## $ Age           <dbl> 34, 34, 34, 4, 49, 9, 8, 45, 45, 45, 66, 58, 54,...
## $ AgeDecade     <chr> "30-39", "30-39", "30-39", "0-9", "40-49", "0-9"...
## $ AgeMonths     <dbl> 409, 409, 409, 49, 596, 115, 101, 541, 541, 541,...
## $ Race1         <chr> "White", "White", "White", "Other", "White", "Wh...
## $ Race3         <lgl> NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, ...
## $ Education     <chr> "High School", "High School", "High School", NA,...
## $ MaritalStatus <chr> "Married", "Married", "Married", NA, "LivePartne...
```

``` {.sourceCode .r}
# or glimpse(NHANES) to see all the variables in the dataset
```

## 3 Data Tidying

``` {.sourceCode .r}
library(tidyverse)
```

```
## -- Attaching packages ---- tidyverse 1.2.1 --

## v ggplot2 3.2.1     v purrr   0.3.3
## v tibble  2.1.3     v dplyr   0.8.2
## v tidyr   0.8.3     v stringr 1.4.0
## v ggplot2 3.2.1     v forcats 0.4.0

## -- Conflicts ------- tidyverse_conflicts() --
## x dplyr::filter() masks stats::filter()
## x dplyr::lag()    masks stats::lag()
```

\*\* Important \*\* If you are not familiar yet with the concepts of tidy data, have a look at the preliminary\_tidyverse.Rmd file!

If we consider our `NHANES` dataframe, we see it is already in a tidy format, as;

- Each variable forms a column.
- Each observation forms a row.
- Each type of observational unit forms a table.

Each row contains all of the information on a single subject (US civilian) in the study.

In the next tutorial, we will work with a dataset on the effects of a certain drug, *captopril*, on the systolic and diastolic blood pressure of patients. This will not be a *tidy* dataset. As such, the details of tidying data with tidyverse will be described there

---

[Up: contents](index.md) · [4 Data wrangling with dplyr →](02-4-data-wrangling-with-dplyr.md)

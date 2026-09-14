---
title: berkeley stat153 · fall 2026
source: https://github.com/berkeley-stat153/fall-2026.git
licence: CC BY 4.0
converted: 2026-09-14
---

# berkeley stat153 · fall 2026

Converted material from [https://github.com/berkeley-stat153/fall-2026.git](https://github.com/berkeley-stat153/fall-2026.git).

**Licence:** CC BY 4.0 · **Material:** course · **Converted:** 2026-09-14

> Converted, not adapted — the same text in markdown, split so every part has a URL.
> It is regenerable output and is **never edited by hand**: a hand edit is lost on the
> next run and silently diverges from the source it claims to reproduce. To change the
> text, make an adaptation instead.

## Contents

- **CodeLabOne153248Fall2026**
    - [Introduction](CodeLabOne153248Fall2026/01-introduction.md)
    - [US Population Dataset](CodeLabOne153248Fall2026/02-us-population-dataset.md)
    - [Fitting a Quadratic Trend](CodeLabOne153248Fall2026/03-fitting-a-quadratic-trend.md)
    - [Modeling Logarithms](CodeLabOne153248Fall2026/04-modeling-logarithms.md)
- **CodeLabTwo153248Fall2026**
    - [Introduction](CodeLabTwo153248Fall2026/01-introduction.md)
    - [Least Squares Estimates](CodeLabTwo153248Fall2026/02-least-squares-estimates.md)
    - [Fitted Values](CodeLabTwo153248Fall2026/03-fitted-values.md)
    - [Residuals](CodeLabTwo153248Fall2026/04-residuals.md)
    - [ACF Plot](CodeLabTwo153248Fall2026/05-acf-plot.md)
    - [Residual Sum of Squares (RSS) and Residual df](CodeLabTwo153248Fall2026/06-residual-sum-of-squares-rss-and-residual-df.md)
    - [Estimate of $\sigma$: the residual standard error](CodeLabTwo153248Fall2026/07-estimate-of-the-residual-standard-error.md)
    - [Standard Errors of the coefficient estimates](CodeLabTwo153248Fall2026/08-standard-errors-of-the-coefficient-estimates.md)
    - [t-statistic and confidence intervals for the coefficients](CodeLabTwo153248Fall2026/09-t-statistic-and-confidence-intervals-for-the-coefficients.md)
    - [Visualizing Uncertainty](CodeLabTwo153248Fall2026/10-visualizing-uncertainty.md)
    - [Other comments](CodeLabTwo153248Fall2026/11-other-comments.md)
- **CodeLectureFive153248Fall2026**
    - [Introduction](CodeLectureFive153248Fall2026/01-introduction.md)
    - [Plot S(theta)](CodeLectureFive153248Fall2026/02-plot-s-theta.md)
    - [Plot S(thetahat) / S(theta)](CodeLectureFive153248Fall2026/03-plot-s-thetahat-s-theta.md)
- **CodeLectureFour153248Fall2026**
    - [Introduction](CodeLectureFour153248Fall2026/01-introduction.md)
    - [Example of Regression with functions of time: USA Accidents Dataset](CodeLectureFour153248Fall2026/02-example-of-regression-with-functions-of-time-usa-accidents-d.md)
    - [Example of Lagged or Auto Regression](CodeLectureFour153248Fall2026/03-example-of-lagged-or-auto-regression.md)
- **CodeLectureTwo153248Fall2026**
    - [Introduction](CodeLectureTwo153248Fall2026/01-introduction.md)
    - [Predict the next 168 monthly observations](CodeLectureTwo153248Fall2026/02-predict-the-next-168-monthly-observations.md)
    - [Predict the next 168 monthly observations](CodeLectureTwo153248Fall2026/03-predict-the-next-168-monthly-observations.md)
    - [Future time points: n+1, ..., n+168](CodeLectureTwo153248Fall2026/04-future-time-points-n-1-n-168.md)
    - [Design matrix for future observations](CodeLectureTwo153248Fall2026/05-design-matrix-for-future-observations.md)
    - [Fitted and predicted values on the log scale](CodeLectureTwo153248Fall2026/06-fitted-and-predicted-values-on-the-log-scale.md)
    - [Convert back to population scale](CodeLectureTwo153248Fall2026/07-convert-back-to-population-scale.md)
    - [Plot observed data, fitted values, and future predictions](CodeLectureTwo153248Fall2026/08-plot-observed-data-fitted-values-and-future-predictions.md)
    - [Prediction 168 months ahead](CodeLectureTwo153248Fall2026/09-prediction-168-months-ahead.md)
    - [Model 3: $\log yt = \beta0 + \beta1 t + \beta2 t^2 + \epsilont$](CodeLectureTwo153248Fall2026/10-model-3.md)
    - [Predict the next 168 monthly observations](CodeLectureTwo153248Fall2026/11-predict-the-next-168-monthly-observations.md)
    - [Future time points: n+1, ..., n+168](CodeLectureTwo153248Fall2026/12-future-time-points-n-1-n-168.md)
    - [Design matrix for future observations](CodeLectureTwo153248Fall2026/13-design-matrix-for-future-observations.md)
    - [Fitted and predicted values on the log scale](CodeLectureTwo153248Fall2026/14-fitted-and-predicted-values-on-the-log-scale.md)
    - [Convert back to population scale](CodeLectureTwo153248Fall2026/15-convert-back-to-population-scale.md)
    - [Plot observed data, fitted values, and future predictions](CodeLectureTwo153248Fall2026/16-plot-observed-data-fitted-values-and-future-predictions.md)
    - [Monthly log growth rates](CodeLectureTwo153248Fall2026/17-monthly-log-growth-rates.md)
    - [RSS for a given change point c](CodeLectureTwo153248Fall2026/18-rss-for-a-given-change-point-c.md)
    - [Try all possible change points](CodeLectureTwo153248Fall2026/19-try-all-possible-change-points.md)
    - [Best change point](CodeLectureTwo153248Fall2026/20-best-change-point.md)
    - [predicted populations y{n+1},...,y{n+168}](CodeLectureTwo153248Fall2026/21-predicted-populations-y-n-1-y-n-168.md)
    - [Growth rates](CodeLectureTwo153248Fall2026/22-growth-rates.md)
    - [Dates corresponding to the growth rates](CodeLectureTwo153248Fall2026/23-dates-corresponding-to-the-growth-rates.md)
    - [RSS for two change points c1 and c2](CodeLectureTwo153248Fall2026/24-rss-for-two-change-points-c1-and-c2.md)
    - [Possible change points](CodeLectureTwo153248Fall2026/25-possible-change-points.md)
    - [Grid search over all pairs](CodeLectureTwo153248Fall2026/26-grid-search-over-all-pairs.md)
    - [Fitted growth rates](CodeLectureTwo153248Fall2026/27-fitted-growth-rates.md)
    - [Convert fitted growth rates back to population](CodeLectureTwo153248Fall2026/28-convert-fitted-growth-rates-back-to-population.md)
    - [CodeLectureTwo153248Fall2026 Part 29 —](CodeLectureTwo153248Fall2026/29-codelecturetwo153248fall2026-part-29.md)
    - [Predict the next 168 months](CodeLectureTwo153248Fall2026/30-predict-the-next-168-months.md)
    - [CodeLectureTwo153248Fall2026 Part 31 —](CodeLectureTwo153248Fall2026/31-codelecturetwo153248fall2026-part-31.md)
    - [Predicted future growth rates](CodeLectureTwo153248Fall2026/32-predicted-future-growth-rates.md)
    - [Convert predicted growth rates to population](CodeLectureTwo153248Fall2026/33-convert-predicted-growth-rates-to-population.md)
    - [CodeLectureTwo153248Fall2026 Part 34 —](CodeLectureTwo153248Fall2026/34-codelecturetwo153248fall2026-part-34.md)
    - [Plot population: data, fitted values, predictions](CodeLectureTwo153248Fall2026/35-plot-population-data-fitted-values-predictions.md)
    - [CodeLectureTwo153248Fall2026 Part 36 —](CodeLectureTwo153248Fall2026/36-codelecturetwo153248fall2026-part-36.md)
    - [CodeLectureTwo153248Fall2026 Part 37 —](CodeLectureTwo153248Fall2026/37-codelecturetwo153248fall2026-part-37.md)
    - [Plot residuals](CodeLectureTwo153248Fall2026/38-plot-residuals.md)
    - [CodeLectureTwo153248Fall2026 Part 39 —](CodeLectureTwo153248Fall2026/39-codelecturetwo153248fall2026-part-39.md)
- [HandwrittenNotesLectureFive153248Fall2026](HandwrittenNotesLectureFive153248Fall2026.md)
- [HandwrittenNotesLectureFour153248Fall2026](HandwrittenNotesLectureFour153248Fall2026.md)
- [HandwrittenNotesLectureThree153248Fall2026](HandwrittenNotesLectureThree153248Fall2026.md)
- **LectureFive153248Fall2026**
    - [1 Bayesian Inference for Linear Regression](LectureFive153248Fall2026/01-1-bayesian-inference-for-linear-regression.md)
    - [2 Nonlinear Regression](LectureFive153248Fall2026/02-2-nonlinear-regression.md)
- **LectureFour153248Fall2026**
    - [1 Multiple Linear Regression](LectureFour153248Fall2026/01-1-multiple-linear-regression.md)
    - [2 Frequentist Inference for Linear Regression](LectureFour153248Fall2026/02-2-frequentist-inference-for-linear-regression.md)
    - [3 Bayesian Inference for Linear Regression](LectureFour153248Fall2026/03-3-bayesian-inference-for-linear-regression.md)
- **LectureOneSlides153248Fall2026PDF**
    - [What is Time Series?](LectureOneSlides153248Fall2026PDF/01-what-is-time-series.md)
    - [US Population](LectureOneSlides153248Fall2026PDF/02-us-population.md)
    - [Questions](LectureOneSlides153248Fall2026PDF/03-questions.md)
    - [Regression over time](LectureOneSlides153248Fall2026PDF/04-regression-over-time.md)
    - [Topic Two: Nonlinear Regression](LectureOneSlides153248Fall2026PDF/05-topic-two-nonlinear-regression.md)
    - [Topic Four: Variance Modeling](LectureOneSlides153248Fall2026PDF/06-topic-four-variance-modeling.md)
    - [Spectral Analysis](LectureOneSlides153248Fall2026PDF/07-spectral-analysis.md)
    - [ARIMA Example One](LectureOneSlides153248Fall2026PDF/08-arima-example-one.md)
    - [ARIMA Example Two](LectureOneSlides153248Fall2026PDF/09-arima-example-two.md)
    - [Topic Six: Vector Time Series](LectureOneSlides153248Fall2026PDF/10-topic-six-vector-time-series.md)
    - [Topic Seven: Neural Networks](LectureOneSlides153248Fall2026PDF/11-topic-seven-neural-networks.md)
    - [Topic Seven: Neural Networks](LectureOneSlides153248Fall2026PDF/12-topic-seven-neural-networks.md)
- **LectureThree153248Fall2026**
    - [Introduction](LectureThree153248Fall2026/01-introduction.md)
    - [Simple Question 1 {#simple-question-1}](LectureThree153248Fall2026/02-simple-question-1-simple-question-1.md)
    - [Simple Question 2 {#simple-question-2}](LectureThree153248Fall2026/03-simple-question-2-simple-question-2.md)
    - [Simple Question 3 {#simple-question-3}](LectureThree153248Fall2026/04-simple-question-3-simple-question-3.md)
    - [LectureThree153248Fall2026 Part 05 —](LectureThree153248Fall2026/05-lecturethree153248fall2026-part-05.md)
    - [Linear Regression with Time as a Covariate {#linear-regression-with-time-as-a-covariate}](LectureThree153248Fall2026/06-linear-regression-with-time-as-a-covariate-linear-regression.md)
- **LectureTwo153248Fall2026**
    - [Simple Linear Regression {#simple-linear-regression}](LectureTwo153248Fall2026/01-simple-linear-regression-simple-linear-regression.md)
    - [Estimation of $\beta0$ and $\beta1$ {#estimation-of-beta0-and-beta1}](LectureTwo153248Fall2026/02-estimation-of-and-estimation-of-beta0-and-beta1.md)
- [Data](data.md)
- [STAT 153 - STAT 248: Time Series Analysis](home.md)
- **syllabus**
    - [Syllabus](syllabus/01-syllabus.md)
    - [About Dept 999](syllabus/02-about-dept-999.md)
- [Unit 1: Intro](unit1.md)
- [Unit 02 —](unit2.md)

## Not converted

Listed rather than dropped silently, because this is the material that needs a
different approach.

- **administrivia** (2) — `README.md`, `calendar.md`

- **render of .md with the same stem** (1) — `syllabus.pdf`

- **render of .tex with the same stem** (2) — `LectureThree153248Fall2026.pdf`, `LectureTwo153248Fall2026.pdf`

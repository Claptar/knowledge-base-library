---
title: • Structure of the course • What is a time series?
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/01_intro.pdf
source_file: sources/berkeley-stat153/spring-2026/01_intro.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# • Structure of the course • What is a time series?

**Source:** [`01_intro.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/01_intro.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Overview of what you’ll learn

## **Introductions**

• **Instructor:** Liberty Hamilton (Statistics and Neuroscience Departments) - liberty.hamilton@berkeley.edu

• **GSIs:** Nicholas Liskij, Yichen Pan • Office hours starting next week

**Structure of the course** • Course website: stat153.berkeley.edu/spring-2026

• Be sure to look at the syllabus • Lecture materials (slides, notes, code) will be posted _after_ each lecture • Materials for labs and homework will be posted • Links to bCourses, Ed Discussion, etc. • Related reading (PDFs, links)

**Assignments** • 5 homework assignments (Stat 248 includes some additional problems) • 1 midterm (Stat 153 and Stat 248) • Final exam (Stat 153) or final project (Stat 248) • Projected dates on syllabus

- **Prerequisites** • Probability at the level of Stat 134 or Data 140 or EE 126 required • 🐍 We assume basic fluency in Python • Many assignments will take advantage of the Berkeley datahub, but for others you should have Python installed on your computer (I recommend the <u>Anaconda python distribution).</u>

- • Labs will use JupyterLab/Jupyter notebooks

## **Introduce yourselves!**

• 👋 Introduce yourself to 2-3 people sitting near you • 🎓 Are you a grad student or undergrad? • ℹ What's your name, major, interests outside of this class?

## **Let’s start!**

- Related reading for today and next week: Chapter 1 of Shumway and Stoffer (SS)

- Available **free** online (see course website for a link)

- We’ll use this book towards the beginning of the semester


**What is a time series?** • A time series is a sequence of data points collected over time • Examples: hourly temperature readings, stock market fluctuations, brain responses over time to a stimulus


**Why should we care about time series?** • We can uncover regular patterns over time

#### • Includes cycles or trends


## **Where might we see time series data?**

- Neuroscience

- Medicine

- Economics

- Epidemiology

- Social science

• Astronomy

• Large language models (LLMs)

…and more!

## **What is and is not a time series?**

• Go to poll: https://pollev.com/stat153


**A real example (sounds)**

**What is different about time series data?** • Not i.i.d. (independent and identically distributed) • Time dependence / correlation structure • Can have drift over time • Let's step through some examples and discuss...


Example brain recordings from various locations in the frontal and parietal lobes in a patient with epilepsy undergoing surgical monitoring. Recorded at 512 Hz sampling rate, one observation every ~2 milliseconds. (Hamilton lab, unpublished data)


## **Course topics**

- Measures of dependence

- Linear regression - simple, multiple, nonlinear, regularization

- • Power spectral analysis and time-frequency analysis

- AR models

- ARIMA models

- Time-lagged regression

- State-space models

- • Neural networks - CNNs, RNNs, self-supervised learning (WavLM)

## <u>https://fred.stlouisfed.org/series/POPTHM</u> **U.S. Population**


## **Questions**

• What will the U.S. population be in 2050? • What is the rate of growth of the population? • Has the growth rate been constant over time? • In what periods has population been fastest / slowest?

**Time Series Analysis and Prediction** One of the main questions we will address in this class is how to **predict future values based on current data**

## **Simple linear regression**


For a simple linear regression, we fit the relationship between our output       and time: _yt yt_ = _ω_ 0 + _ω_ 1 _xt_


**Simple linear regression - US population**


**What if we look at population change over time?**

## **Seasonal trends - sinusoidal regression** _<mark>yt</mark>_ <mark>=</mark> _<mark>ω</mark>_ <mark>0 +</mark> _<mark>ω</mark>_ <mark>1 cos(</mark> _<mark>εt</mark>_ <mark>) +</mark> _<mark>ω</mark>_ <mark>2 sin(</mark> _<mark>εt</mark>_ <mark>) +</mark> _<mark>ϑ</mark>_

We might know what is (yearly trend?)

**Seasonal trends - sinusoidal regression** _<mark>yt</mark>_ <mark>=</mark> _<mark>ω</mark>_ <mark>0 +</mark> _<mark>ω</mark>_ <mark>1 cos(</mark> _<mark>εt</mark>_ <mark>) +</mark> _<mark>ω</mark>_ <mark>2 sin(</mark> _<mark>εt</mark>_ <mark>) +</mark> _<mark>ϑ</mark>_

We might know what is (yearly trend?), or we can fit it

## **Seasonal trends - sinusoidal regression**

There may be times when relationships don’t hold, need multiple predictors


<!-- Start of picture text -->
Average price per pound of various goods<br>Tomatoes<br>Chicken<br>Oranges<br>https://www.bls.gov/charts/consumer-price-index/<br>consumer-price-index-average-price-data.htm<br><!-- End of picture text -->

## **Sinusoidal models and Fourier Analysis**

• _yt_ = _ω_ 0 + _ω_ 1 cos( _εt_ ) + _ω_ 2 sin( _εt_ ) + _ϑ_ • Models like this are closely related to **Fourier Analysis** , which describes complex, periodic signals as a sum of simpler waveforms • These models are used extensively in engineering, physics, neuroscience, audio signal processing

**Time-frequency analysis** • Example below shows the EEG time series recording and timefrequency spectrogram from an electrode on the back of the head with eyes open vs. closed • The large amplitude waves during “eyes closed” are referred to as the “alpha rhythm”


<!-- Start of picture text -->
Time<br><!-- End of picture text -->

waveform

###### spectrogram


•<sup>For some types of neural data, specific frequency bands may better relate to</sup> sensory input - e.g. “high gamma” frequencies reflect responses to speech

## **AR, ARIMA, and time-lagged regression**

• What is the next number in this series?

• 1, 1, 2, 3, 5, 8, 13, 21, 34, …? _yt_ = _yt→_ 1 + _yt→_ 2 • This is the Fibonacci sequence ( ) • We cannot just fit a linear regression over time


• Must regress over lagged values and

- Called **AutoRegression (AR)**

## **Autoregressive models**

• Using prior data from a time series to predict current data (AutoRegression) is the basis of ARIMA models (AutoRegressive Integrated Moving Average Models)

on • Do a linear regression of


for fixed lag _p_


## **Predictions given by AR model incorporating data for previous 10 years**


## **Time-lagged regression models**


##### • Brain responses to speech modeled as a function of time-lagged sound features • We can test different features (sound frequencies, loudness, phonemes)

## **Time-lagged regression models**


<!-- Start of picture text -->
y(t)<br><!-- End of picture text -->


These models are used widely in neuroscience to describe what aspects of different sensory stimuli increase or decrease brain activity in a given area


<!-- Start of picture text -->
Time (s)<br><!-- End of picture text -->

## **Modern approaches**

- We will also learn about **deep neural network** approaches that can be used to predict continuous time series

- <sup>Nonlinear, nonparametric</sup> approach

• We will discuss **convolutional neural networks (CNNs), recurrent neural networks (RNNs),** and **self-supervised models**


## **Summary of topics**

- Measures of dependence

- • Linear regression - simple, multiple, nonlinear, regularization • Power spectral analysis and time-frequency analysis • AR, ARIMA, time-lagged regression

#### • State-space models • Neural networks - CNNs, RNNs, self-supervised learning (WavLM)

## **Before next time**

- If you haven’t done it yet, fill out the presemester survey!

- • <u>https://forms.gle/2jLWHGeAvXe9EMcG9</u> (or use QR code)

- Next time we will talk about characteristics of time series data

---

[← • Introductions](02-introductions.md) · [Up: contents](index.md)

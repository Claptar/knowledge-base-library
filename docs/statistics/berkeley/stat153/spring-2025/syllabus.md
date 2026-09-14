---
title: 'STAT 153 AND STAT 248: TIME SERIES'
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/syllabus.pdf
source_file: sources/berkeley-stat153/spring-2025/syllabus.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# STAT 153 AND STAT 248: TIME SERIES

**Source:** [`syllabus.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/syllabus.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

INSTRUCTOR: ADITYA GUNTUBOYINA COURSE OUTLINE FOR SPRING 2025 UNIVERSITY OF CALIFORNIA, BERKELEY

- **Instructor** : Aditya Guntuboyina. Email: `aditya@stat.berkeley.edu` and Website: `www.stat.berkeley.edu/~aditya`

- **Lectures** : 3:30 pm to 4:59 pm on Tuesdays and Thursdays in 106 Stanley Hall

- **Office Hours** : 1:30 pm to 2:30 pm on Tuesdays and Thursdays in 422 Evans Hall

- **GSI** : Dohyeong Ki. Email: `dohyeong` ~~`k`~~ `i@berkeley.edu`

- **GSI Lab Section** : 11 am - 12:59 pm or 3 pm - 4:59 pm in 334 Evans Hall on Fridays

- **GSI Office Hours** : 9 - 10 AM, 1 - 2 PM and 5-6 PM on Fridays in 446 Evans Hall

- **Reader** : Jiayi Li. Email: `jiayi.li@berkeley.edu`

**About the course** : Time series (and more generally sequential data) refers to datasets where there is a temporal order for the observations. This course aims to teach you how to analyze such data. The primary objective of time series analysis is to develop mathematical models that provide plausible descriptions for observed time series data. We shall study several time series models in this class including (a) Multiple linear regression models (covariates depending on time), (b) Nonlinear regression models (covariates depending on time), (c) Regularized High-dimensional linear regression models (covariates depending on time), (d) Variance models and spectral analysis, (e) Lagged regressions and ARIMA models, (f) Recurrent Neural Networks.

**Prerequisites** : Undergraduate probability (at the level of STAT 134 or DATA 140) is required. Statistics at the level of STAT 133 and STAT 135 is recommended and may be taken concurrently.

**Programming Language** : You are free to use any language (e.g., R, Python, Julia, Matlab etc.) for working on your homework. We will be using Python code in class and the lab sections.

**Text** : There is no required textbook for the class. Here are some materials that you can use as general references:

- _Time Series Analysis and its Applications_ by Shumway and Stoffer: In the past, this book has been used as required reading for this course. It has good materials on ARIMA modeling and Spectral Analysis.

- Prof. Ryan Tibshirani’s lecture materials for 153 last semester are available at `https://stat153.berkeley.edu/fall-2024/` . These notes will have some overlap with what we will cover.

1

STAT 153 AND STAT 248: TIME SERIES

2

- My lecture notes from the last time I taught the course (Fall 2022). I have uploaded these on bcourses. There will be some overlap here with what we will cover but there will be many departures as well.

I will provide materials for each lecture (including slides or typed lecture notes, and code) which will be posted _after_ the lecture.

**Ed Discussion** : I have created a site for this class at Ed Discussion and we will use this platform for Q & A.

**Homework assignments** : Will be posted on bcourses according to the following schedule. Solutions will need to be uploaded on Gradescope.

- Homework One - will be posted on Jan 30 and due on Feb 10

- Homework Two - will be posted on Feb 13 and due on Feb 24

- Homework Three - will be posted on Feb 27 and due on Mar 10

- Midterm on March 18

- Homework Four - will be posted on 03 April and due on 14 April

- Homework Five - will be posted on 17 April and due on 28 April

You have a total of 120 late hours that you can apply to your homework for the entire semester. No points will be awarded for any homework which brings the total late hours to more than 120.

**Exams** : There will be two exams: midterm and Final. The Midterm will be on 18 March in class. The Final exam will be on May 16 from 7 pm to 10 pm.

**Assessment** : Your final score for the class will be calculated as

50% Homework + 20% Midterm + 30% Final _._

Each homework assignment is worth an equal amount.

**Differences between 153 and 248** : Each homework assignment will have 1-3 additional questions that only students taking STAT 248 need to answer. The exams for 153 and 248 may have different sets of questions.

**Grade Complaints** : If you have a complaint against an assigned homework or exam grade and want to talk to me about it, first send me a written request through email explaining your case clearly.

**Academic Integrity** : You are encouraged to work in small groups on homework problems. However, you must write up solutions on your own, and you must never read or copy the solutions of other students. Similarly, you may use books or online resources to help solve homework problems, but you must credit all such sources in your writeup and you must never copy materials verbatim. Any students found to be cheating automatically risks failing the class and being referred to the Office of Student Conduct. In particular, copying solutions, in whole or in part, from other students in the class or any other source without acknowledgement constitutes cheating.

**Students with disabilities** : If you need accommodations for any physical, psychological, or learning disability, please get in touch with me so that we can make the necessary arrangements.

---

[Up: contents](index.md)

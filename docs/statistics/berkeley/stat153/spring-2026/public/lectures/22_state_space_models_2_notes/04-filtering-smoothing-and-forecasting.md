---
title: Filtering, smoothing, and forecasting
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/22_state_space_models_2_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/22_state_space_models_2_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Filtering, smoothing, and forecasting

**Source:** [`public/lectures/22_state_space_models_2_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/22_state_space_models_2_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

For state space models, we want to estimate our underlying unobserved signal $x_t$ given the data $y_{1:s} = {y_1, \dots, y_s}$ to time $s$. In practice, the steps for the state space models include:

1. Filtering, where we estimate $x_t$ using measurements up through time $t$ (here $s$=$t$)
2. Prediction/forecasting, where we have $s<t$ and want to estimate new data
3. Smoothing, where $s>t$. This allows us to estimate $x_t$ using the entire dataset, including observations after $t$. This can be used to better estimate missing values.

We can write out the unobserved signal $x_t$ using the convention:

$x_t^s = E(x_t | y_{1:s})$

which again, is $x_t$ given $y$ from time 1 to time $s$, which can be $=t$ (filtering), $<t$ (prediction), or $>t$ (smoothing).

We also have the Prediction error covariance (using the notation from Shumway and Stoffer and the original Kalman 1960 paper):

$P_{t1,t2}^s = E{(x_{t1}-x_{t1}^s)(x_{t2}-x_{t2}^s)^\prime}$

from this, we will look at the Kalman Filter, which gives filtering and forecasting equations (Kalman 1960). As it turns out, modifications of this algorithm were most recently used in the Artemis-II mission to send a crewed flight into lunar orbit and back to Earth. The original Apollo 8 mission and subsequent missions to the moon all used improvements to this original algorithm, in the latest case using 4 navigation Extended Kalman Filters (EKFs) as part of the navigation system. From a [technical report](https://ntrs.nasa.gov/api/citations/20230000548/downloads/Orion_EKF_AAS_2023.pdf) related to Artemis-1:

> The Artemis Program is NASA’s campaign to explore the Moon and beyond. Artemis-1, the uncrewed exoLEO test flight of the Orion spacecraft, was completed in 2022. There are four navigation Extended Kalman Filters (EKFs) that are part of the Orion navigation system. The Atmospheric Extended Kalman Filter (ATMEKF) estimates the vehicle position, velocity, and attitude (referred to as the vehicle state) during the ascent and entry phases of flight. Once Orion is outside of Earth’s atmosphere, the Earth Orbit Extended Kalman Filter (EOEKF) and Cislunar Extended Kalman Filter (CLEKF) estimate the translational states, depending on the phase of flight, while the Attitude Extended Kalman Filter (ATTEKF) estimates the rotational state of the vehicle. The Kalman filters propagate the vehicle state forward in time using a combination of dynamics models and the output data from the Inertial Measurement Unit (IMU). The filters update the vehicle states and associated uncertainties, in the form of the covariance matrix, using pseudorange measurements from GPS (in ATMEKF/EOEKF), optical navigation measurements of the Earth or Moon (in CLEKF), and star tracker measurements (in ATTEKF). Simultaneously, the Kalman filters estimate error sources in the sensors, which are included in the state vectors as Exponentially Correlated Random Variables (ECRVs).

One note here - the Kalman Filter we'll show an example for is for a linear system, but the EKF allows us to extend this idea into systems with nonlinear dynamics.

---

[← Advantages of state space models](03-advantages-of-state-space-models.md) · [Up: contents](index.md) · [The Kalman Filter →](05-the-kalman-filter.md)

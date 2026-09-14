---
title: Sample PACF
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyOne153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyOne153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Sample PACF

**Source:** [`CodeLectureTwentyOne153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyOne153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Towards the end of last  lecture, we discussed the Sample PACF (Partial Autocorrelation Function) that is used as an exploratory data analysis tool mainly for determining an appropriate order $p$ for fitting the AR($p$) model to the data. The sample PACF at lag $p$ is simply equal to the esimate $\hat{\phi}_p$ of $\phi_p$ when an AR($p$) model is fit to the data. We also discussed briefly why this quantity (obtained by fitting AR($p$) models for various $p$  is has "partial autocorrelation" in its name). You will revisit this again in tomorrow's lab.

Now, we shall show code for calculating the sample PACF. We shall calculate it directly by fitting AR(p) models with increasing $p$. We shall also use inbuilt functions from statsmodels to compute the sample PACF, and we will verify that we are getting exactly the same answers.

Let us use the GNP dataset that was previously used in Lab 10.

```python
gnp = pd.read_csv("GNP_02April2025.csv")
print(gnp.head())
y = gnp['GNP']
plt.figure(figsize = (12, 6))
plt.plot(y, color = 'black')
plt.show()
```

```
observation_date      GNP
0       1947-01-01  244.142
1       1947-04-01  247.063
2       1947-07-01  250.716
3       1947-10-01  260.981
4       1948-01-01  267.133
```

*(1 figure omitted — see the original notebook.)*

Instead of working with the GNP data directly, we shall first take logarithms and then differences.

```python
ylogdiff = np.diff(np.log(y))
plt.figure(figsize = (12, 6))
plt.plot(ylogdiff)
plt.title('Diff(Log(Quarterly GNP))')
plt.ylabel('Value')
plt.xlabel('Quarter')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Suppose we want to fit an AR($p$) model to this dataset. What is a suitable value of $p$? To figure this out, we can simply compute the sample PACF.

```python
def sample_pacf(y, p_max):
    pautocorr = []
    for p in range(1, p_max + 1):
        armd = AutoReg(ylogdiff, lags = p).fit()
        phi_p = armd.params[-1]
        pautocorr.append(phi_p)
    return pautocorr

p_max = 50
sample_pacf_vals = sample_pacf(ylogdiff, p_max)
plt.figure(figsize = (12, 6))
markerline, stemline, baseline = plt.stem(range(1, p_max + 1), sample_pacf_vals)
markerline.set_marker("None")
plt.xlabel("p")
plt.ylabel('Partial Correlation')
plt.title("Sample Partial Auto Correlation")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Next let us use an inbuilt function from statsmodels to compute the pacf.

```python
from statsmodels.tsa.stattools import pacf
pacf_values = pacf(ylogdiff, nlags=p_max, method = 'ols')
print(np.column_stack([sample_pacf_vals, pacf_values[1:]])) #check that these values match exactly
```

```
[[ 0.2494903   0.2494903 ]
 [ 0.20501251  0.20501251]
 [-0.01395884 -0.01395884]
 [-0.04624678 -0.04624678]
 [-0.03576291 -0.03576291]
 [ 0.00612623  0.00612623]
 [ 0.07954096  0.07954096]
 [ 0.03379382  0.03379382]
 [ 0.09908671  0.09908671]
 [ 0.09148765  0.09148765]
 [ 0.03935477  0.03935477]
 [ 0.00231935  0.00231935]
 [-0.02952129 -0.02952129]
 [ 0.05181593  0.05181593]
 [ 0.0668389   0.0668389 ]
 [ 0.12328399  0.12328399]
 [ 0.10611304  0.10611304]
 [ 0.10657613  0.10657613]
 [ 0.0044102   0.0044102 ]
 [ 0.05242979  0.05242979]
 [-0.03582163 -0.03582163]
 [ 0.01026383  0.01026383]
 [-0.08690484 -0.08690484]
 [ 0.09000221  0.09000221]
 [ 0.1440655   0.1440655 ]
 [-0.07755717 -0.07755717]
 [-0.03216266 -0.03216266]
 [ 0.06553052  0.06553052]
 [-0.02122327 -0.02122327]
 [-0.03054263 -0.03054263]
 [-0.03595624 -0.03595624]
 [ 0.03193371  0.03193371]
 [ 0.03931399  0.03931399]
 [-0.00235186 -0.00235186]
 [ 0.00512543  0.00512543]
 [-0.04618897 -0.04618897]
 [-0.0203755  -0.0203755 ]
 [-0.12254506 -0.12254506]
 [-0.09938421 -0.09938421]
 [-0.02095841 -0.02095841]
 [-0.06731694 -0.06731694]
 [ 0.12911652  0.12911652]
 [ 0.02500216  0.02500216]
 [ 0.04445531  0.04445531]
 [ 0.04253399  0.04253399]
 [-0.04416781 -0.04416781]
 [-0.16020234 -0.16020234]
 [-0.06809175 -0.06809175]
 [ 0.00068818  0.00068818]
 [-0.08538738 -0.08538738]]
```

In comparison to our plot of the sample_pacf values, the inbuilt sample_pacf plot from statsmodels will look slightly different (even though it is plotting the same values). The differences are: (a) it also plots the value 1 at lag 0, (b) it gives a shaded region that can be used to assess whether values are negligible or not.

```python
fig, axes = plt.subplots(figsize = (12, 6))
plot_pacf(ylogdiff, lags = p_max, ax = axes)
axes.set_title("Sample PACF of diff_log_GDP Series")
plt.show()
```

*(1 figure omitted — see the original notebook.)*

From the above plot, it appears that AR(2) is a good model for this dataset.

```python
ar2 = AutoReg(ylogdiff, lags = 2).fit()
print(ar2.summary())
```

```
AutoReg Model Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  311
Model:                     AutoReg(2)   Log Likelihood                 921.191
Method:               Conditional MLE   S.D. of innovations              0.012
Date:                Fri, 11 Apr 2025   AIC                          -1834.381
Time:                        13:06:41   BIC                          -1819.448
Sample:                             2   HQIC                         -1828.411
                                  311
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0092      0.001      7.289      0.000       0.007       0.012
y.L1           0.1984      0.056      3.563      0.000       0.089       0.307
y.L2           0.2050      0.056      3.682      0.000       0.096       0.314
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.7771           +0.0000j            1.7771            0.0000
AR.2           -2.7447           +0.0000j            2.7447            0.5000
-----------------------------------------------------------------------------
```

Another way of fitting AR models in statsmodels is to use the ARIMA function, as shown below.

```python
from statsmodels.tsa.arima.model import ARIMA
ar2_arima = sm.tsa.arima.ARIMA(ylogdiff, order = (2, 0, 0)).fit() #order = (2, 0, 0) refers to the AR(2) model.
print(ar2_arima.summary())
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  311
Model:                 ARIMA(2, 0, 0)   Log Likelihood                 928.043
Date:                Fri, 11 Apr 2025   AIC                          -1848.087
Time:                        13:06:46   BIC                          -1833.128
Sample:                             0   HQIC                         -1842.108
                                - 311
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0154      0.001     10.694      0.000       0.013       0.018
ar.L1          0.1981      0.026      7.683      0.000       0.148       0.249
ar.L2          0.2036      0.068      2.996      0.003       0.070       0.337
sigma2         0.0001   3.88e-06     38.544      0.000       0.000       0.000
===================================================================================
Ljung-Box (L1) (Q):                   0.00   Jarque-Bera (JB):              7805.10
Prob(Q):                              0.96   Prob(JB):                         0.00
Heteroskedasticity (H):               1.61   Skew:                            -0.07
Prob(H) (two-sided):                  0.02   Kurtosis:                        27.54
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

Note that the estimates computed by the ARIMA function are slightly different from the estimates computed by the "conditional MLE" method in AutoReg. There are many methods that are used by these functions. Generally they all should give similar answers.

```python
help(ARIMA)
```

```
Help on class ARIMA in module statsmodels.tsa.arima.model:

class ARIMA(statsmodels.tsa.statespace.sarimax.SARIMAX)
 |  ARIMA(endog, exog=None, order=(0, 0, 0), seasonal_order=(0, 0, 0, 0), trend=None, enforce_stationarity=True, enforce_invertibility=True, concentrate_scale=False, trend_offset=1, dates=None, freq=None, missing='none', validate_specification=True)
 |
 |  Autoregressive Integrated Moving Average (ARIMA) model, and extensions
 |
 |  This model is the basic interface for ARIMA-type models, including those
 |  with exogenous regressors and those with seasonal components. The most
 |  general form of the model is SARIMAX(p, d, q)x(P, D, Q, s). It also allows
 |  all specialized cases, including
 |
 |  - autoregressive models: AR(p)
 |  - moving average models: MA(q)
 |  - mixed autoregressive moving average models: ARMA(p, q)
 |  - integration models: ARIMA(p, d, q)
 |  - seasonal models: SARIMA(P, D, Q, s)
 |  - regression with errors that follow one of the above ARIMA-type models
 |
 |  Parameters
 |  ----------
 |  endog : array_like, optional
 |      The observed time-series process :math:`y`.
 |  exog : array_like, optional
 |      Array of exogenous regressors.
 |  order : tuple, optional
 |      The (p,d,q) order of the model for the autoregressive, differences, and
 |      moving average components. d is always an integer, while p and q may
 |      either be integers or lists of integers.
 |  seasonal_order : tuple, optional
 |      The (P,D,Q,s) order of the seasonal component of the model for the
 |      AR parameters, differences, MA parameters, and periodicity. Default
 |      is (0, 0, 0, 0). D and s are always integers, while P and Q
 |      may either be integers or lists of positive integers.
 |  trend : str{'n','c','t','ct'} or iterable, optional
 |      Parameter controlling the deterministic trend. Can be specified as a
 |      string where 'c' indicates a constant term, 't' indicates a
 |      linear trend in time, and 'ct' includes both. Can also be specified as
 |      an iterable defining a polynomial, as in `numpy.poly1d`, where
 |      `[1,1,0,1]` would denote :math:`a + bt + ct^3`. Default is 'c' for
 |      models without integration, and no trend for models with integration.
 |      Note that all trend terms are included in the model as exogenous
 |      regressors, which differs from how trends are included in ``SARIMAX``
 |      models.  See the Notes section for a precise definition of the
 |      treatment of trend terms.
 |  enforce_stationarity : bool, optional
 |      Whether or not to require the autoregressive parameters to correspond
 |      to a stationarity process.
 |  enforce_invertibility : bool, optional
 |      Whether or not to require the moving average parameters to correspond
 |      to an invertible process.
 |  concentrate_scale : bool, optional
 |      Whether or not to concentrate the scale (variance of the error term)
 |      out of the likelihood. This reduces the number of parameters by one.
 |      This is only applicable when considering estimation by numerical
 |      maximum likelihood.
 |  trend_offset : int, optional
 |      The offset at which to start time trend values. Default is 1, so that
 |      if `trend='t'` the trend is equal to 1, 2, ..., nobs. Typically is only
 |      set when the model created by extending a previous dataset.
 |  dates : array_like of datetime, optional
 |      If no index is given by `endog` or `exog`, an array-like object of
 |      datetime objects can be provided.
 |  freq : str, optional
 |      If no index is given by `endog` or `exog`, the frequency of the
 |      time-series may be specified here as a Pandas offset or offset string.
 |  missing : str
 |      Available options are 'none', 'drop', and 'raise'. If 'none', no nan
 |      checking is done. If 'drop', any observations with nans are dropped.
 |      If 'raise', an error is raised. Default is 'none'.
 |
 |  Notes
 |  -----
 |  This model incorporates both exogenous regressors and trend components
 |  through "regression with ARIMA errors". This differs from the
 |  specification estimated using ``SARIMAX`` which treats the trend
 |  components separately from any included exogenous regressors. The full
 |  specification of the model estimated here is:
 |
 |  .. math::
 |
 |      Y_{t}-\delta_{0}-\delta_{1}t-\ldots-\delta_{k}t^{k}-X_{t}\beta
 |          & =\epsilon_{t} \\
 |      \left(1-L\right)^{d}\left(1-L^{s}\right)^{D}\Phi\left(L\right)
 |      \Phi_{s}\left(L\right)\epsilon_{t}
 |          & =\Theta\left(L\right)\Theta_{s}\left(L\right)\eta_{t}
 |
 |  where :math:`\eta_t \sim WN(0,\sigma^2)` is a white noise process, L
 |  is the lag operator, and :math:`G(L)` are lag polynomials corresponding
 |  to the autoregressive (:math:`\Phi`), seasonal autoregressive
 |  (:math:`\Phi_s`), moving average (:math:`\Theta`), and seasonal moving
 |  average components (:math:`\Theta_s`).
 |
 |  `enforce_stationarity` and `enforce_invertibility` are specified in the
 |  constructor because they affect loglikelihood computations, and so should
 |  not be changed on the fly. This is why they are not instead included as
 |  arguments to the `fit` method.
 |
 |  See the notebook `ARMA: Sunspots Data
 |  <../examples/notebooks/generated/tsa_arma_0.html>`__ and
 |  `ARMA: Artificial Data <../examples/notebooks/generated/tsa_arma_1.html>`__
 |  for an overview.
 |
 |  .. todo:: should concentrate_scale=True by default
 |
 |  Examples
 |  --------
 |  >>> mod = sm.tsa.arima.ARIMA(endog, order=(1, 0, 0))
 |  >>> res = mod.fit()
 |  >>> print(res.summary())
 |
 |  Method resolution order:
 |      ARIMA
 |      statsmodels.tsa.statespace.sarimax.SARIMAX
 |      statsmodels.tsa.statespace.mlemodel.MLEModel
 |      statsmodels.tsa.base.tsa_model.TimeSeriesModel
 |      statsmodels.base.model.LikelihoodModel
 |      statsmodels.base.model.Model
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, endog, exog=None, order=(0, 0, 0), seasonal_order=(0, 0, 0, 0), trend=None, enforce_stationarity=True, enforce_invertibility=True, concentrate_scale=False, trend_offset=1, dates=None, freq=None, missing='none', validate_specification=True)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  fit(self, start_params=None, transformed=True, includes_fixed=False, method=None, method_kwargs=None, gls=None, gls_kwargs=None, cov_type=None, cov_kwds=None, return_params=False, low_memory=False)
 |      Fit (estimate) the parameters of the model.
 |
 |      Parameters
 |      ----------
 |      start_params : array_like, optional
 |          Initial guess of the solution for the loglikelihood maximization.
 |          If None, the default is given by Model.start_params.
 |      transformed : bool, optional
 |          Whether or not `start_params` is already transformed. Default is
 |          True.
 |      includes_fixed : bool, optional
 |          If parameters were previously fixed with the `fix_params` method,
 |          this argument describes whether or not `start_params` also includes
 |          the fixed parameters, in addition to the free parameters. Default
 |          is False.
 |      method : str, optional
 |          The method used for estimating the parameters of the model. Valid
 |          options include 'statespace', 'innovations_mle', 'hannan_rissanen',
 |          'burg', 'innovations', and 'yule_walker'. Not all options are
 |          available for every specification (for example 'yule_walker' can
 |          only be used with AR(p) models).
 |      method_kwargs : dict, optional
 |          Arguments to pass to the fit function for the parameter estimator
 |          described by the `method` argument.
 |      gls : bool, optional
 |          Whether or not to use generalized least squares (GLS) to estimate
 |          regression effects. The default is False if `method='statespace'`
 |          and is True otherwise.
 |      gls_kwargs : dict, optional
 |          Arguments to pass to the GLS estimation fit method. Only applicable
 |          if GLS estimation is used (see `gls` argument for details).
 |      cov_type : str, optional
 |          The `cov_type` keyword governs the method for calculating the
 |          covariance matrix of parameter estimates. Can be one of:
 |
 |          - 'opg' for the outer product of gradient estimator
 |          - 'oim' for the observed information matrix estimator, calculated
 |            using the method of Harvey (1989)
 |          - 'approx' for the observed information matrix estimator,
 |            calculated using a numerical approximation of the Hessian matrix.
 |          - 'robust' for an approximate (quasi-maximum likelihood) covariance
 |            matrix that may be valid even in the presence of some
 |            misspecifications. Intermediate calculations use the 'oim'
 |            method.
 |          - 'robust_approx' is the same as 'robust' except that the
 |            intermediate calculations use the 'approx' method.
 |          - 'none' for no covariance matrix calculation.
 |
 |          Default is 'opg' unless memory conservation is used to avoid
 |          computing the loglikelihood values for each observation, in which
 |          case the default is 'oim'.
 |      cov_kwds : dict or None, optional
 |          A dictionary of arguments affecting covariance matrix computation.
 |
 |          **opg, oim, approx, robust, robust_approx**
 |
 |          - 'approx_complex_step' : bool, optional - If True, numerical
 |            approximations are computed using complex-step methods. If False,
 |            numerical approximations are computed using finite difference
 |            methods. Default is True.
 |          - 'approx_centered' : bool, optional - If True, numerical
 |            approximations computed using finite difference methods use a
 |            centered approximation. Default is False.
 |      return_params : bool, optional
 |          Whether or not to return only the array of maximizing parameters.
 |          Default is False.
 |      low_memory : bool, optional
 |          If set to True, techniques are applied to substantially reduce
 |          memory usage. If used, some features of the results object will
 |          not be available (including smoothed results and in-sample
 |          prediction), although out-of-sample forecasting is possible.
 |          Default is False.
 |
 |      Returns
 |      -------
 |      ARIMAResults
 |
 |      Examples
 |      --------
 |      >>> mod = sm.tsa.arima.ARIMA(endog, order=(1, 0, 0))
 |      >>> res = mod.fit()
 |      >>> print(res.summary())
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from statsmodels.tsa.statespace.sarimax.SARIMAX:
 |
 |  clone(self, endog, exog=None, **kwargs)
 |      Clone state space model with new data and optionally new specification
 |
 |      Parameters
 |      ----------
 |      endog : array_like
 |          The observed time-series process :math:`y`
 |      k_states : int
 |          The dimension of the unobserved state process.
 |      exog : array_like, optional
 |          Array of exogenous regressors, shaped nobs x k. Default is no
 |          exogenous regressors.
 |      kwargs
 |          Keyword arguments to pass to the new model class to change the
 |          model specification.
 |
 |      Returns
 |      -------
 |      model : MLEModel subclass
 |
 |      Notes
 |      -----
 |      This method must be implemented
 |
 |  initialize(self)
 |      Initialize the SARIMAX model.
 |
 |      Notes
 |      -----
 |      These initialization steps must occur following the parent class
 |      __init__ function calls.
 |
 |  initialize_default(self, approximate_diffuse_variance=None)
 |      Initialize default
 |
 |  prepare_data(self)
 |      Prepare data for use in the state space representation
 |
 |  transform_params(self, unconstrained)
 |      Transform unconstrained parameters used by the optimizer to constrained
 |      parameters used in likelihood evaluation.
 |
 |      Used primarily to enforce stationarity of the autoregressive lag
 |      polynomial, invertibility of the moving average lag polynomial, and
 |      positive variance parameters.
 |
 |      Parameters
 |      ----------
 |      unconstrained : array_like
 |          Unconstrained parameters used by the optimizer.
 |
 |      Returns
 |      -------
 |      constrained : array_like
 |          Constrained parameters used in likelihood evaluation.
 |
 |      Notes
 |      -----
 |      If the lag polynomial has non-consecutive powers (so that the
 |      coefficient is zero on some element of the polynomial), then the
 |      constraint function is not onto the entire space of invertible
 |      polynomials, although it only excludes a very small portion very close
 |      to the invertibility boundary.
 |
 |  untransform_params(self, constrained)
 |      Transform constrained parameters used in likelihood evaluation
 |      to unconstrained parameters used by the optimizer
 |
 |      Used primarily to reverse enforcement of stationarity of the
 |      autoregressive lag polynomial and invertibility of the moving average
 |      lag polynomial.
 |
 |      Parameters
 |      ----------
 |      constrained : array_like
 |          Constrained parameters used in likelihood evaluation.
 |
 |      Returns
 |      -------
 |      constrained : array_like
 |          Unconstrained parameters used by the optimizer.
 |
 |      Notes
 |      -----
 |      If the lag polynomial has non-consecutive powers (so that the
 |      coefficient is zero on some element of the polynomial), then the
 |      constraint function is not onto the entire space of invertible
 |      polynomials, although it only excludes a very small portion very close
 |      to the invertibility boundary.
 |
 |  update(self, params, transformed=True, includes_fixed=False, complex_step=False)
 |      Update the parameters of the model
 |
 |      Updates the representation matrices to fill in the new parameter
 |      values.
 |
 |      Parameters
 |      ----------
 |      params : array_like
 |          Array of new parameters.
 |      transformed : bool, optional
 |          Whether or not `params` is already transformed. If set to False,
 |          `transform_params` is called. Default is True..
 |
 |      Returns
 |      -------
 |      params : array_like
 |          Array of parameters.
 |
 |  ----------------------------------------------------------------------
 |  Readonly properties inherited from statsmodels.tsa.statespace.sarimax.SARIMAX:
 |
 |  endog_names
 |      Names of endogenous variables
 |
 |  initial_design
 |      Initial design matrix
 |
 |  initial_selection
 |      Initial selection matrix
 |
 |  initial_state_intercept
 |      Initial state intercept vector
 |
 |  initial_transition
 |      Initial transition matrix
 |
 |  model_latex_names
 |      The latex names of all possible model parameters.
 |
 |  model_names
 |      The plain text names of all possible model parameters.
 |
 |  model_orders
 |      The orders of each of the polynomials in the model.
 |
 |  param_names
 |      List of human readable parameter names (for parameters actually
 |      included in the model).
 |
 |  param_terms
 |      List of parameters actually included in the model, in sorted order.
 |
 |      TODO Make this an dict with slice or indices as the values.
 |
 |  start_params
 |      Starting parameters for maximum likelihood estimation
 |
 |  state_names
 |      (list of str) List of human readable names for unobserved states.
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from statsmodels.tsa.statespace.sarimax.SARIMAX:
 |
 |  params_complete = ['trend', 'exog', 'ar', 'ma', 'seasonal_ar', 'season...
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from statsmodels.tsa.statespace.mlemodel.MLEModel:
 |
 |  __getitem__(self, key)
 |
 |  __setitem__(self, key, value)
 |
 |  filter(self, params, transformed=True, includes_fixed=False, complex_step=False, cov_type=None, cov_kwds=None, return_ssm=False, results_class=None, results_wrapper_class=None, low_memory=False, **kwargs)
 |      Kalman filtering
 |
 |      Parameters
 |      ----------
 |      params : array_like
 |          Array of parameters at which to evaluate the loglikelihood
 |          function.
 |      transformed : bool, optional
 |          Whether or not `params` is already transformed. Default is True.
 |      return_ssm : bool,optional
 |          Whether or not to return only the state space output or a full
 |          results object. Default is to return a full results object.
 |      cov_type : str, optional
 |          See `MLEResults.fit` for a description of covariance matrix types
 |          for results object.
 |      cov_kwds : dict or None, optional
 |          See `MLEResults.get_robustcov_results` for a description required
 |          keywords for alternative covariance estimators
 |      low_memory : bool, optional
 |          If set to True, techniques are applied to substantially reduce
 |          memory usage. If used, some features of the results object will
 |          not be available (including in-sample prediction), although
 |          out-of-sample forecasting is possible. Default is False.
 |      **kwargs
 |          Additional keyword arguments to pass to the Kalman filter. See
 |          `KalmanFilter.filter` for more details.
 |
 |  fit_constrained(self, constraints, start_params=None, **fit_kwds)
 |      Fit the model with some parameters subject to equality constraints.
 |
 |      Parameters
 |      ----------
 |      constraints : dict
 |          Dictionary of constraints, of the form `param_name: fixed_value`.
 |          See the `param_names` property for valid parameter names.
 |      start_params : array_like, optional
 |          Initial guess of the solution for the loglikelihood maximization.
 |          If None, the default is given by Model.start_params.
 |      **fit_kwds : keyword arguments
 |          fit_kwds are used in the optimization of the remaining parameters.
 |
 |      Returns
 |      -------
 |      results : Results instance
 |
 |      Examples
 |      --------
 |      >>> mod = sm.tsa.SARIMAX(endog, order=(1, 0, 1))
 |      >>> res = mod.fit_constrained({'ar.L1': 0.5})
 |
 |  fix_params(self, params)
 |      Fix parameters to specific values (context manager)
 |
 |      Parameters
 |      ----------
 |      params : dict
 |          Dictionary describing the fixed parameter values, of the form
 |          `param_name: fixed_value`. See the `param_names` property for valid
 |          parameter names.
 |
 |      Examples
 |      --------
 |      >>> mod = sm.tsa.SARIMAX(endog, order=(1, 0, 1))
 |      >>> with mod.fix_params({'ar.L1': 0.5}):
 |              res = mod.fit()
 |
 |  handle_params(self, params, transformed=True, includes_fixed=False, return_jacobian=False)
 |      Ensure model parameters satisfy shape and other requirements
 |
 |  hessian(self, params, *args, **kwargs)
 |      Hessian matrix of the likelihood function, evaluated at the given
 |      parameters
 |
 |      Parameters
 |      ----------
 |      params : array_like
 |          Array of parameters at which to evaluate the hessian.
 |      *args
 |          Additional positional arguments to the `loglike` method.
 |      **kwargs
 |          Additional keyword arguments to the `loglike` method.
 |
 |      Returns
 |      -------
 |      hessian : ndarray
 |          Hessian matrix evaluated at `params`
 |
 |      Notes
 |      -----
 |      This is a numerical approximation.
 |
 |      Both args and kwargs are necessary because the optimizer from
 |      `fit` must call this function and only supports passing arguments via
 |      args (for example `scipy.optimize.fmin_l_bfgs`).
 |
 |  impulse_responses(self, params, steps=1, impulse=0, orthogonalized=False, cumulative=False, anchor=None, exog=None, extend_model=None, extend_kwargs=None, transformed=True, includes_fixed=False, **kwargs)
 |      Impulse response function
 |
 |      Parameters
 |      ----------
 |      params : array_like
 |          Array of model parameters.
 |      steps : int, optional
 |          The number of steps for which impulse responses are calculated.
 |          Default is 1. Note that for time-invariant models, the initial
 |          impulse is not counted as a step, so if `steps=1`, the output will
 |          have 2 entries.
 |      impulse : int, str or array_like
 |          If an integer, the state innovation to pulse; must be between 0
 |          and `k_posdef-1`. If a str, it indicates which column of df
 |          the unit (1) impulse is given.
 |          Alternatively, a custom impulse vector may be provided; must be
 |          shaped `k_posdef x 1`.
 |      orthogonalized : bool, optional
 |          Whether or not to perform impulse using orthogonalized innovations.
 |          Note that this will also affect custum `impulse` vectors. Default
 |          is False.
 |      cumulative : bool, optional
 |          Whether or not to return cumulative impulse responses. Default is
 |          False.
 |      anchor : int, str, or datetime, optional
 |          Time point within the sample for the state innovation impulse. Type
 |          depends on the index of the given `endog` in the model. Two special
 |          cases are the strings 'start' and 'end', which refer to setting the
 |          impulse at the first and last points of the sample, respectively.
 |          Integer values can run from 0 to `nobs - 1`, or can be negative to
 |          apply negative indexing. Finally, if a date/time index was provided
 |          to the model, then this argument can be a date string to parse or a
 |          datetime type. Default is 'start'.
 |      exog : array_like, optional
 |          New observations of exogenous regressors for our-of-sample periods,
 |          if applicable.
 |      transformed : bool, optional
 |          Whether or not `params` is already transformed. Default is
 |          True.
 |      includes_fixed : bool, optional
 |          If parameters were previously fixed with the `fix_params` method,
 |          this argument describes whether or not `params` also includes
 |          the fixed parameters, in addition to the free parameters. Default
 |          is False.
 |      **kwargs
 |          If the model has time-varying design or transition matrices and the
 |          combination of `anchor` and `steps` implies creating impulse
 |          responses for the out-of-sample period, then these matrices must
 |          have updated values provided for the out-of-sample steps. For
 |          example, if `design` is a time-varying component, `nobs` is 10,
 |          `anchor=1`, and `steps` is 15, a (`k_endog` x `k_states` x 7)
 |          matrix must be provided with the new design matrix values.
 |
 |      Returns
 |      -------
 |      impulse_responses : ndarray
 |          Responses for each endogenous variable due to the impulse
 |          given by the `impulse` argument. For a time-invariant model, the
 |          impulse responses are given for `steps + 1` elements (this gives
 |          the "initial impulse" followed by `steps` responses for the
 |          important cases of VAR and SARIMAX models), while for time-varying
 |          models the impulse responses are only given for `steps` elements
 |          (to avoid having to unexpectedly provide updated time-varying
 |          matrices).
 |
 |      See Also
 |      --------
 |      simulate
 |          Simulate a time series according to the given state space model,
 |          optionally with specified series for the innovations.
 |
 |      Notes
 |      -----
 |      Intercepts in the measurement and state equation are ignored when
 |      calculating impulse responses.
 |
 |      TODO: add an option to allow changing the ordering for the
 |            orthogonalized option. Will require permuting matrices when
 |            constructing the extended model.
 |
 |  initialize_approximate_diffuse(self, variance=None)
 |      Initialize approximate diffuse
 |
 |  initialize_known(self, initial_state, initial_state_cov)
 |      Initialize known
 |
 |  initialize_statespace(self, **kwargs)
 |      Initialize the state space representation
 |
 |      Parameters
 |      ----------
 |      **kwargs
 |          Additional keyword arguments to pass to the state space class
 |          constructor.
 |
 |  initialize_stationary(self)
 |      Initialize stationary
 |
 |  loglike(self, params, *args, **kwargs)
 |      Loglikelihood evaluation
 |
 |      Parameters
 |      ----------
 |      params : array_like
 |          Array of parameters at which to evaluate the loglikelihood
 |          function.
 |      transformed : bool, optional
 |          Whether or not `params` is already transformed. Default is True.
 |      **kwargs
 |          Additional keyword arguments to pass to the Kalman filter. See
 |          `KalmanFilter.filter` for more details.
 |
 |      See Also
 |      --------
 |      update : modifies the internal state of the state space model to
 |               reflect new params
 |
 |      Notes
 |      -----
 |      [1]_ recommend maximizing the average likelihood to avoid scale issues;
 |      this is done automatically by the base Model fit method.
 |
 |      References
 |      ----------
 |      .. [1] Koopman, Siem Jan, Neil Shephard, and Jurgen A. Doornik. 1999.
 |         Statistical Algorithms for Models in State Space Using SsfPack 2.2.
 |         Econometrics Journal 2 (1): 107-60. doi:10.1111/1368-423X.00023.
 |
 |  loglikeobs(self, params, transformed=True, includes_fixed=False, complex_step=False, **kwargs)
 |      Loglikelihood evaluation
 |
 |      Parameters
 |      ----------
 |      params : array_like
 |          Array of parameters at which to evaluate the loglikelihood
 |          function.
 |      transformed : bool, optional
 |          Whether or not `params` is already transformed. Default is True.
 |      **kwargs
 |          Additional keyword arguments to pass to the Kalman filter. See
 |          `KalmanFilter.filter` for more details.
 |
 |      See Also
 |      --------
 |      update : modifies the internal state of the Model to reflect new params
 |
 |      Notes
 |      -----
 |      [1]_ recommend maximizing the average likelihood to avoid scale issues;
 |      this is done automatically by the base Model fit method.
 |
 |      References
 |      ----------
 |      .. [1] Koopman, Siem Jan, Neil Shephard, and Jurgen A. Doornik. 1999.
 |         Statistical Algorithms for Models in State Space Using SsfPack 2.2.
 |         Econometrics Journal 2 (1): 107-60. doi:10.1111/1368-423X.00023.
 |
 |  observed_information_matrix(self, params, transformed=True, includes_fixed=False, approx_complex_step=None, approx_centered=False, **kwargs)
 |      Observed information matrix
 |
 |      Parameters
 |      ----------
 |      params : array_like, optional
 |          Array of parameters at which to evaluate the loglikelihood
 |          function.
 |      **kwargs
 |          Additional keyword arguments to pass to the Kalman filter. See
 |          `KalmanFilter.filter` for more details.
 |
 |      Notes
 |      -----
 |      This method is from Harvey (1989), which shows that the information
 |      matrix only depends on terms from the gradient. This implementation is
 |      partially analytic and partially numeric approximation, therefore,
 |      because it uses the analytic formula for the information matrix, with
 |      numerically computed elements of the gradient.
 |
 |      References
 |      ----------
 |      Harvey, Andrew C. 1990.
 |      Forecasting, Structural Time Series Models and the Kalman Filter.
 |      Cambridge University Press.
 |
 |  opg_information_matrix(self, params, transformed=True, includes_fixed=False, approx_complex_step=None, **kwargs)
 |      Outer product of gradients information matrix
 |
 |      Parameters
 |      ----------
 |      params : array_like, optional
 |          Array of parameters at which to evaluate the loglikelihood
 |          function.
 |      **kwargs
 |          Additional arguments to the `loglikeobs` method.
 |
 |      References
 |      ----------
 |      Berndt, Ernst R., Bronwyn Hall, Robert Hall, and Jerry Hausman. 1974.
 |      Estimation and Inference in Nonlinear Structural Models.
 |      NBER Chapters. National Bureau of Economic Research, Inc.
 |
 |  score(self, params, *args, **kwargs)
 |      Compute the score function at params.
 |
 |      Parameters
 |      ----------
 |      params : array_like
 |          Array of parameters at which to evaluate the score.
 |      *args
 |          Additional positional arguments to the `loglike` method.
 |      **kwargs
 |          Additional keyword arguments to the `loglike` method.
 |
 |      Returns
 |      -------
 |      score : ndarray
 |          Score, evaluated at `params`.
 |
 |      Notes
 |      -----
 |      This is a numerical approximation, calculated using first-order complex
 |      step differentiation on the `loglike` method.
 |
 |      Both args and kwargs are necessary because the optimizer from
 |      `fit` must call this function and only supports passing arguments via
 |      args (for example `scipy.optimize.fmin_l_bfgs`).
 |
 |  score_obs(self, params, method='approx', transformed=True, includes_fixed=False, approx_complex_step=None, approx_centered=False, **kwargs)
 |      Compute the score per observation, evaluated at params
 |
 |      Parameters
 |      ----------
 |      params : array_like
 |          Array of parameters at which to evaluate the score.
 |      **kwargs
 |          Additional arguments to the `loglike` method.
 |
 |      Returns
 |      -------
 |      score : ndarray
 |          Score per observation, evaluated at `params`.
 |
 |      Notes
 |      -----
 |      This is a numerical approximation, calculated using first-order complex
 |      step differentiation on the `loglikeobs` method.
 |
 |  set_conserve_memory(self, conserve_memory=None, **kwargs)
 |      Set the memory conservation method
 |
 |      By default, the Kalman filter computes a number of intermediate
 |      matrices at each iteration. The memory conservation options control
 |      which of those matrices are stored.
 |
 |      Parameters
 |      ----------
 |      conserve_memory : int, optional
 |          Bitmask value to set the memory conservation method to. See notes
 |          for details.
 |      **kwargs
 |          Keyword arguments may be used to influence the memory conservation
 |          method by setting individual boolean flags.
 |
 |      Notes
 |      -----
 |      This method is rarely used. See the corresponding function in the
 |      `KalmanFilter` class for details.
 |
 |  set_filter_method(self, filter_method=None, **kwargs)
 |      Set the filtering method
 |
 |      The filtering method controls aspects of which Kalman filtering
 |      approach will be used.
 |
 |      Parameters
 |      ----------
 |      filter_method : int, optional
 |          Bitmask value to set the filter method to. See notes for details.
 |      **kwargs
 |          Keyword arguments may be used to influence the filter method by
 |          setting individual boolean flags. See notes for details.
 |
 |      Notes
 |      -----
 |      This method is rarely used. See the corresponding function in the
 |      `KalmanFilter` class for details.
 |
 |  set_inversion_method(self, inversion_method=None, **kwargs)
 |      Set the inversion method
 |
 |      The Kalman filter may contain one matrix inversion: that of the
 |      forecast error covariance matrix. The inversion method controls how and
 |      if that inverse is performed.
 |
 |      Parameters
 |      ----------
 |      inversion_method : int, optional
 |          Bitmask value to set the inversion method to. See notes for
 |          details.
 |      **kwargs
 |          Keyword arguments may be used to influence the inversion method by
 |          setting individual boolean flags. See notes for details.
 |
 |      Notes
 |      -----
 |      This method is rarely used. See the corresponding function in the
 |      `KalmanFilter` class for details.
 |
 |  set_smoother_output(self, smoother_output=None, **kwargs)
 |      Set the smoother output
 |
 |      The smoother can produce several types of results. The smoother output
 |      variable controls which are calculated and returned.
 |
 |      Parameters
 |      ----------
 |      smoother_output : int, optional
 |          Bitmask value to set the smoother output to. See notes for details.
 |      **kwargs
 |          Keyword arguments may be used to influence the smoother output by
 |          setting individual boolean flags.
 |
 |      Notes
 |      -----
 |      This method is rarely used. See the corresponding function in the
 |      `KalmanSmoother` class for details.
 |
 |  set_stability_method(self, stability_method=None, **kwargs)
 |      Set the numerical stability method
 |
 |      The Kalman filter is a recursive algorithm that may in some cases
 |      suffer issues with numerical stability. The stability method controls
 |      what, if any, measures are taken to promote stability.
 |
 |      Parameters
 |      ----------
 |      stability_method : int, optional
 |          Bitmask value to set the stability method to. See notes for
 |          details.
 |      **kwargs
 |          Keyword arguments may be used to influence the stability method by
 |          setting individual boolean flags. See notes for details.
 |
 |      Notes
 |      -----
 |      This method is rarely used. See the corresponding function in the
 |      `KalmanFilter` class for details.
 |
 |  simulate(self, params, nsimulations, measurement_shocks=None, state_shocks=None, initial_state=None, anchor=None, repetitions=None, exog=None, extend_model=None, extend_kwargs=None, transformed=True, includes_fixed=False, pretransformed_measurement_shocks=True, pretransformed_state_shocks=True, pretransformed_initial_state=True, random_state=None, **kwargs)
 |      Simulate a new time series following the state space model
 |
 |      Parameters
 |      ----------
 |      params : array_like
 |          Array of parameters to use in constructing the state space
 |          representation to use when simulating.
 |      nsimulations : int
 |          The number of observations to simulate. If the model is
 |          time-invariant this can be any number. If the model is
 |          time-varying, then this number must be less than or equal to the
 |          number of observations.
 |      measurement_shocks : array_like, optional
 |          If specified, these are the shocks to the measurement equation,
 |          :math:`\varepsilon_t`. If unspecified, these are automatically
 |          generated using a pseudo-random number generator. If specified,
 |          must be shaped `nsimulations` x `k_endog`, where `k_endog` is the
 |          same as in the state space model.
 |      state_shocks : array_like, optional
 |          If specified, these are the shocks to the state equation,
 |          :math:`\eta_t`. If unspecified, these are automatically
 |          generated using a pseudo-random number generator. If specified,
 |          must be shaped `nsimulations` x `k_posdef` where `k_posdef` is the
 |          same as in the state space model.
 |      initial_state : array_like, optional
 |          If specified, this is the initial state vector to use in
 |          simulation, which should be shaped (`k_states` x 1), where
 |          `k_states` is the same as in the state space model. If unspecified,
 |          but the model has been initialized, then that initialization is
 |          used. This must be specified if `anchor` is anything other than
 |          "start" or 0 (or else you can use the `simulate` method on a
 |          results object rather than on the model object).
 |      anchor : int, str, or datetime, optional
 |          First period for simulation. The simulation will be conditional on
 |          all existing datapoints prior to the `anchor`.  Type depends on the
 |          index of the given `endog` in the model. Two special cases are the
 |          strings 'start' and 'end'. `start` refers to beginning the
 |          simulation at the first period of the sample, and `end` refers to
 |          beginning the simulation at the first period after the sample.
 |          Integer values can run from 0 to `nobs`, or can be negative to
 |          apply negative indexing. Finally, if a date/time index was provided
 |          to the model, then this argument can be a date string to parse or a
 |          datetime type. Default is 'start'.
 |      repetitions : int, optional
 |          Number of simulated paths to generate. Default is 1 simulated path.
 |      exog : array_like, optional
 |          New observations of exogenous regressors, if applicable.
 |      transformed : bool, optional
 |          Whether or not `params` is already transformed. Default is
 |          True.
 |      includes_fixed : bool, optional
 |          If parameters were previously fixed with the `fix_params` method,
 |          this argument describes whether or not `params` also includes
 |          the fixed parameters, in addition to the free parameters. Default
 |          is False.
 |      pretransformed_measurement_shocks : bool, optional
 |          If `measurement_shocks` is provided, this flag indicates whether it
 |          should be directly used as the shocks. If False, then it is assumed
 |          to contain draws from the standard Normal distribution that must be
 |          transformed using the `obs_cov` covariance matrix. Default is True.
 |      pretransformed_state_shocks : bool, optional
 |          If `state_shocks` is provided, this flag indicates whether it
 |          should be directly used as the shocks. If False, then it is assumed
 |          to contain draws from the standard Normal distribution that must be
 |          transformed using the `state_cov` covariance matrix. Default is
 |          True.
 |      pretransformed_initial_state : bool, optional
 |          If `initial_state` is provided, this flag indicates whether it
 |          should be directly used as the initial_state. If False, then it is
 |          assumed to contain draws from the standard Normal distribution that
 |          must be transformed using the `initial_state_cov` covariance
 |          matrix. Default is True.
 |      random_state : {None, int, Generator, RandomState}, optional
 |          If `seed` is None (or `np.random`), the
 |          class:``~numpy.random.RandomState`` singleton is used.
 |          If `seed` is an int, a new class:``~numpy.random.RandomState``
 |          instance is used, seeded with `seed`.
 |          If `seed` is already a class:``~numpy.random.Generator`` or
 |          class:``~numpy.random.RandomState`` instance then that instance is
 |          used.
 |
 |      Returns
 |      -------
 |      simulated_obs : ndarray
 |          An array of simulated observations. If `repetitions=None`, then it
 |          will be shaped (nsimulations x k_endog) or (nsimulations,) if
 |          `k_endog=1`. Otherwise it will be shaped
 |          (nsimulations x k_endog x repetitions). If the model was given
 |          Pandas input then the output will be a Pandas object. If
 |          `k_endog > 1` and `repetitions` is not None, then the output will
 |          be a Pandas DataFrame that has a MultiIndex for the columns, with
 |          the first level containing the names of the `endog` variables and
 |          the second level containing the repetition number.
 |
 |      See Also
 |      --------
 |      impulse_responses
 |          Impulse response functions
 |
 |  simulation_smoother(self, simulation_output=None, **kwargs)
 |      Retrieve a simulation smoother for the state space model.
 |
 |      Parameters
 |      ----------
 |      simulation_output : int, optional
 |          Determines which simulation smoother output is calculated.
 |          Default is all (including state and disturbances).
 |      **kwargs
 |          Additional keyword arguments, used to set the simulation output.
 |          See `set_simulation_output` for more details.
 |
 |      Returns
 |      -------
 |      SimulationSmoothResults
 |
 |  smooth(self, params, transformed=True, includes_fixed=False, complex_step=False, cov_type=None, cov_kwds=None, return_ssm=False, results_class=None, results_wrapper_class=None, **kwargs)
 |      Kalman smoothing
 |
 |      Parameters
 |      ----------
 |      params : array_like
 |          Array of parameters at which to evaluate the loglikelihood
 |          function.
 |      transformed : bool, optional
 |          Whether or not `params` is already transformed. Default is True.
 |      return_ssm : bool,optional
 |          Whether or not to return only the state space output or a full
 |          results object. Default is to return a full results object.
 |      cov_type : str, optional
 |          See `MLEResults.fit` for a description of covariance matrix types
 |          for results object.
 |      cov_kwds : dict or None, optional
 |          See `MLEResults.get_robustcov_results` for a description required
 |          keywords for alternative covariance estimators
 |      **kwargs
 |          Additional keyword arguments to pass to the Kalman filter. See
 |          `KalmanFilter.filter` for more details.
 |
 |  transform_jacobian(self, unconstrained, approx_centered=False)
 |      Jacobian matrix for the parameter transformation function
 |
 |      Parameters
 |      ----------
 |      unconstrained : array_like
 |          Array of unconstrained parameters used by the optimizer.
 |
 |      Returns
 |      -------
 |      jacobian : ndarray
 |          Jacobian matrix of the transformation, evaluated at `unconstrained`
 |
 |      See Also
 |      --------
 |      transform_params
 |
 |      Notes
 |      -----
 |      This is a numerical approximation using finite differences. Note that
 |      in general complex step methods cannot be used because it is not
 |      guaranteed that the `transform_params` method is a real function (e.g.
 |      if Cholesky decomposition is used).
 |
 |  ----------------------------------------------------------------------
 |  Class methods inherited from statsmodels.tsa.statespace.mlemodel.MLEModel:
 |
 |  from_formula(formula, data, subset=None) from builtins.type
 |      Not implemented for state space models
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from statsmodels.tsa.statespace.mlemodel.MLEModel:
 |
 |  initial_variance
 |
 |  initialization
 |
 |  loglikelihood_burn
 |
 |  tolerance
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from statsmodels.tsa.base.tsa_model.TimeSeriesModel:
 |
 |  exog_names
 |      The names of the exogenous variables.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from statsmodels.base.model.LikelihoodModel:
 |
 |  information(self, params)
 |      Fisher information matrix of model.
 |
 |      Returns -1 * Hessian of the log-likelihood evaluated at params.
 |
 |      Parameters
 |      ----------
 |      params : ndarray
 |          The model parameters.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from statsmodels.base.model.Model:
 |
 |  predict(self, params, exog=None, *args, **kwargs)
 |      After a model has been fit predict returns the fitted values.
 |
 |      This is a placeholder intended to be overwritten by individual models.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from statsmodels.base.model.Model:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
```

---

[Up: contents](index.md) · [AR(1) with $|\phi1| > 1$ →](02-ar-1-with.md)

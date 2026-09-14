---
title: Define the second derivative
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Define the second derivative

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

def f_deriv2(x):
    return -np.cos(x)# original fxn

def make_plot2(xs, xvals, f, f_deriv1, num, title):
    # gradient subplot
    plt.subplot(3, 2, num)
    plt.plot(xs, f_deriv1(xs), '-', label="f'(x)")
    plt.scatter(np.pi, f_deriv1(np.pi))
    for i in range(len(xvals)):
        plt.text(xvals[i], 0, i, fontsize=12, color = 'red')
    plt.xlabel('x')
    plt.ylabel("f'(x)")
    plt.title(title[0])
    plt.legend(loc='lower right')
    plt.tight_layout()
    # function subplot
    plt.subplot(3, 2, num+1)
    plt.plot(xs, f(xs), '-', label="f(x)")
    plt.scatter(np.pi, f(np.pi))
    for i in range(len(xvals)):
        plt.text(xvals[i], 0, i, fontsize=12, color = 'red')
    plt.xlabel('x')
    plt.ylabel("f(x)")
    plt.title(title[1])
    plt.legend(loc='lower right')
    plt.tight_layout()


xs = np.linspace(0, 2 * np.pi, num=300)

x0 = 5.5 # starting point

## f_deriv1(x0) # positive
## f_deriv2(x0) # negative
## x1 = x0 - f_deriv1(x0)/f_deriv2(x0) # whoops, we've gone uphill
## because of the negative second derivative
xvals = np.zeros(n)

xvals[0] = x0
for t in range(1,10):
    xvals[t] = xvals[t-1] - f_deriv1(xvals[t-1]) / f_deriv2(xvals[t-1])
## print(xvals)

plt.figure(figsize=(10, 7))

make_plot2(xs, xvals, f, f_deriv1, 1, title =
    ['uphill to local maximum, gradient view', 'uphill to local maximum, function view'])

## In contrast, with better starting points we can find the minimum
## (but this nearly diverges).

x0 = 4.3 # ok starting point
## f_deriv1(x0)
## f_deriv2(x0)
## x1 = x0 - f_deriv1(x0)/f_deriv2(x0)  # going downhill

xvals[0] = x0
for t in range(1,10):
    xvals[t] = xvals[t-1] - f_deriv1(xvals[t-1]) / f_deriv2(xvals[t-1])
## print(xvals)

make_plot2(xs, xvals, f, f_deriv1, 3, title =
    ['nearly diverges, gradient view', 'nearly diverges, function view'])

## With a better starting point, we converge quickly.

x0 = 3.8 # good starting point
f_deriv1(x0)
f_deriv2(x0)
x1 = x0 - f_deriv1(x0)/f_deriv2(x0)   # going downhill

xvals[0] = x0
for t in range(1,10):
    xvals[t] = xvals[t-1] - f_deriv1(xvals[t-1]) / f_deriv2(xvals[t-1])
## print(xvals)

make_plot2(xs, xvals, f, f_deriv1, 5, title =
    ['better starting point, gradient view', 'better starting point, function view'])

plt.show(block=False)
```

#### Improving Newton's method

One nice, general idea is to use a fast method such as Newton's method
*safeguarded* by a robust, but slower method. Here's how one can do this
for N-R, safeguarding with a bracketing method such as bisection.
Basically, we check the N-R proposed move to see if N-R is proposing a
step outside of where the root is known to lie based on the previous
steps and the gradient values for those steps. If so, we could choose
the next step based on bisection.

Another approach is backtracking. If a new value is proposed that yields
a larger value of the function, backtrack to find a value that reduces
the function. One possibility is a line search but given that we're
trying to reduce computation, a full line search is often unwise
computationally (also in the multivariate Newton's method, we are in the
middle of an iterative algorithm for which we will just be going off in
another direction anyway at the next iteration). A basic approach is to
keep backtracking in halves. A nice alternative is to fit a polynomial
to the known information about that slice of the function, namely
$f(x_{t+1})$, $f(x_{t})$, $f^{\prime}(x_{t})$ and
$f^{\prime\prime}(x_{t})$ and find the minimum of the polynomial
approximation.

---

[← Define the gradient](06-define-the-gradient.md) · [Up: contents](index.md) · [4. Convergence ideas →](08-4-convergence-ideas.md)

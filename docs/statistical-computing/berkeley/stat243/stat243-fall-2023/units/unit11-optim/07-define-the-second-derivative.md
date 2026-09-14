---
title: Define the second derivative
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit11-optim.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Define the second derivative

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

def fpp(x):
    return -np.cos(x)# original fxn

def make_plot2(xs, xvals, f, fp, num, title):
    # gradient subplot
    plt.subplot(3, 2, num)
    plt.plot(xs, fp(xs), '-', label="f'(x)")
    plt.scatter(np.pi, fp(np.pi))
    for i in range(len(xvals)):
        plt.text(xvals[i], fp(xvals[i]), i, fontsize=14, color = 'red')
    plt.xlabel('x')
    plt.ylabel("f'(x)")
    plt.title(title[0])
    plt.legend(loc='lower right')
    # function subplot
    plt.subplot(3, 2, num+1)
    plt.plot(xs, f(xs), '-', label="f(x)")
    plt.scatter(np.pi, f(np.pi))
    for i in range(len(xvals)):
        plt.text(xvals[i], f(xvals[i]), i, fontsize=14, color = 'red')
    plt.xlabel('x')
    plt.ylabel("f(x)")
    plt.title(title[1])
    plt.legend(loc='lower right')


xs = np.linspace(0, 2 * np.pi, num=300)

x0 = 5.5 # starting point
fp(x0) # positive
fpp(x0) # negative
x1 = x0 - fp(x0)/fpp(x0) # whoops, we've gone uphill
## because of the negative second derivative
xvals = np.zeros(n)

xvals[0] = x0
for t in range(1,10):
    xvals[t] = xvals[t-1] - fp(xvals[t-1]) / fpp(xvals[t-1])
## print(xvals)

plt.figure(figsize=(10, 7))

make_plot2(xs, xvals, f, fp, 1, title =
    ['uphill to local maximum, gradient view', 'uphill to local maximum, function view'])

## In contrast, with better starting points we can find the minimum
## (but this nearly diverges).

x0 = 4.3 # ok starting point
fp(x0)
fpp(x0)
x1 = x0 - fp(x0)/fpp(x0)  # going downhill

xvals[0] = x0
for t in range(1,10):
    xvals[t] = xvals[t-1] - fp(xvals[t-1]) / fpp(xvals[t-1])
## print(xvals)

make_plot2(xs, xvals, f, fp, 3, title =
    ['nearly diverges, gradient view', 'nearly diverges, function view'])

## With a better starting point, we converge quickly.

x0 = 3.8 # good starting point
fp(x0)
fpp(x0)
x1 = x0 - fp(x0)/fpp(x0)   # going downhill

xvals[0] = x0
for t in range(1,10):
    xvals[t] = xvals[t-1] - fp(xvals[t-1]) / fpp(xvals[t-1])
## print(xvals)

make_plot2(xs, xvals, f, fp, 5, title =
    ['better starting point, gradient view', 'better starting point, function view'])

plt.show()
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

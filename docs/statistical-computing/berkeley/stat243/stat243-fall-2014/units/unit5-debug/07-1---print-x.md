---
title: '[1] "<-" "{" "+" "print" "x"'
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit5-debug.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [1] "<-" "{" "+" "print" "x"

**Source:** [`units/unit5-debug.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

If you’ve written your code modularly with lots of functions, you can test individual functions. Often the error will be in what gets passed into and out of each function.

You can have warnings printed as they occurred, rather than saved, using options(warn = 1). This can help figure out where in a loop a warning is being generated. You can also have R convert warnings to error using options(warn = 2).

At the beginning of time (the 1970s?), the standard debugging strategy was to insert print statements in one’s code to see the value of a variable and thereby decipher what could be going wrong. We have better tools nowadays.

### **3.2 Interactive debugging via the browser**

The core strategy for interactive debugging is to use _browser()_ , which pauses the current execution, and provides an interpreter, allowing you to view the current state of R. You can invoke _browser()_ in four ways

- by inserting a call to _browser()_ in your code if you suspect where things are going wrong

5

- by invoking the browser after every step of a function using _debug()_

- by using options(error = recover) to invoke the browser when _error()_ is called

- by temporarily modifying a function to allow browsing using _trace()_

Once in the browser, you can execute any R commands you want. In particular, using _ls()_ to look at the objects residing in the current function environment, looking at the values of objects, and examining the classes of objects is often helpful.

### **3.3 Using** **_debug()_ to step through code**

To step through a function, use debug(nameOfFunction). Then run your code. When the function is executed, R will pause execution just before the first line of the function. You are now using the browser and can examine the state of R and execute R statements.

In addition, you can use “n” or return to step to the next line, “c” to execute the entire current function or current loop, and “Q” to stop debugging. We’ll see an example in the demo code.

To unflag the function so that calling it doesn’t invoke debug, use undebug(nameOfFunction). In addition to working with functions you write you can use debug with standard R functions and functions from packages. For example you could do debug(glm).

### **3.4 Tracing errors in the call stack**

_traceback()_ and _recover()_ allow you to see the call stack (the sequence of nested function calls – see Unit 4) at the time of an error. This helps pinpoint where in a series of function calls the error may be occurring.

If you’ve run the code and gotten an error, you can invoke _traceback()_ after things have gone awry. R will show you the call stack, which can help pinpoint where an error is occurring.

More helpful is to be able to browse within the call stack. To do this invoke options(error = recover) (potentially in your _.Rprofile_ if you do a lot of programming). Then when an error occurs, _recover()_ gets called, usually from the function in which the error occurred. The call to _recover()_ allows you to navigate the stack of active function calls at the time of the error and browse within the desired call. You just enter the number of the call you’d like to enter (or 0 to exit). You can then look around in the frame of a given function, entering an empty line when you want to return to the list of calls again.

You can also combine this with options(warn = 2), which turns warnings into errors to get to the point where a warning was issued.

6

### **3.5 Using** **_trace()_ to temporarily insert code**

_trace()_ lets you temporarily insert code into a function (including standard R functions and functions in packages!) that can then be easily removed. You can use trace in a few ways - here’s how you would do it most simply, where by default the second argument is invoked at the start of the function given as the first argument, but it is also possible to invoke just before exiting a function:

trace(lm, recover) # invoke recover() when the function starts trace(lm, exit = browser) # invoke browser() when the function ends trace(lm, browser, exit = browser) # invoke browser() at start and end

Then in this example, once the browser activates I can poke around within the _lm()_ function and see what is going on.

The most flexible way to use _trace()_ is to use the argument _edit = TRUE_ and then insert whatever code you want wherever you want. If I want to ensure I use a particular editor, such as _emacs_ , I can use the argument _edit = “emacs”_ . A standard approach would be to add a line with _browser()_ to step through the code or _recover()_ (to see the call stack and just look at the current state of objects). Alternatively, you can manually change the code in a function without using _trace()_ , but it’s very easy to forget to change things back and hard to do this with functions in packages, so _trace()_ is a nice way to do things.

You call _untrace()_ , e.g., untrace(lm), to remove the temporarily inserted code; otherwise it’s removed when the session ends.

Alternatively you can do trace(warning, recover) which will insert a call to _recover()_ whenever _warning()_ is called.

---

[← Unit 05 — debug Part 06 —](06-unit-05-debug-part-06.md) · [Up: contents](index.md) · [4 Getting help online →](08-4-getting-help-online.md)

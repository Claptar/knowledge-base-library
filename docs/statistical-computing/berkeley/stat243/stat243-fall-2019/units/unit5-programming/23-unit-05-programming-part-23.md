---
title: Unit 05 — programming Part 23 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 23 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In many cases there will be a default method (here, _summary.default()_ ), so if no method is defined for the class, R uses the default. Sidenote: arguments to a generic method are passed along to the selected method by passing along the calling environment.

We can define new generic methods:

summarize <- **function** (object, ...) **UseMethod** ("summarize")

Once _UseMethod()_ is called, R searches for the specific method associated with the class of _object_ and calls that method, without ever returning to the generic method. Let’s try this out on our _bear_ class. In reality, we’d write either _summary.bear()_ or _print.bear()_ (and of course the generics for _summary_ and _print_ already exist) but for illustration, I wanted to show how we would write both the generic and the specific method, so I’ll write a _summarize_ method.

summarize.bear <- **function** (object) **return** ( **with** (object, **cat** ("Bear of age ", age, " whose name is ", firstname, " ", surname, ".\n", sep = ""))) **summarize** (yog) ## Bear of age 20 whose name is Yogi the Bear.

**The print method** Like _summary()_ , _print()_ is a generic method, with various class-specific methods, such as _print.lm()_ .

25

Note that the _print()_ function is what is called when you simply type the name of the object, so we can have object information printed out in a structured way. Recall that the output when we type the name of an _lm_ object is NOT simply a regurgitation of the elements of the list - rather _print.lm()_ is called.

Similarly, when we used print(object.size(x)) we were invoking the _object_size_ - specific print method which gets the value of the size and then formats it. So there’s actually a fair amount going on behind the scenes.

Surprisingly, the _summary()_ method generally doesn’t actually print out information; rather it computes things not stored in the original object and returns it as a new class (e.g., class _summary.lm_ ), which is then automatically printed, per my comment above, using _print.summary.lm()_ , unless one assigns it to a new object. Note that _print.summary.lm()_ is hidden from user view.

out <- **summary** (mod) out **print** (out) **getS3method** (f="print",class="summary.lm")

**More on inheritance** As noted with _lm_ and _glm_ objects, we can assign more than one class to an object. Here _summarize()_ still works, even though the primary class is _grizzly_bear_ .

**class** (yog) <- **c** ('grizzly_bear', 'bear') **summarize** (yog)

---

[← Unit 05 — programming Part 22 —](22-unit-05-programming-part-22.md) · [Up: contents](index.md) · [Bear of age 20 whose name is Yogi the Bear. →](24-bear-of-age-20-whose-name-is-yogi-the-bear.md)

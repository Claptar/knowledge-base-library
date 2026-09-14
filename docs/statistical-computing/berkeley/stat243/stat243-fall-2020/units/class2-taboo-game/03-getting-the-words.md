---
title: Getting the words
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/class2-taboo-game.md
source_file: sources/berkeley-stat243/stat243-fall-2020/units/class2-taboo-game.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Getting the words

**Source:** [`units/class2-taboo-game.md`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/class2-taboo-game.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

Every person should obtain the necessary code by running the following in R.

```
load(url("https://bit.ly/3j1bHDs"))
```

The presenter starts her or his turn by setting the random number seed so she/he gets random words:

```
set.seed(1)
```

Then each time you need to get a word, run:

```
next_word()
```

The other team should be running the same code, with the same random number seed, so they can see the forbidden words. Of course the presenter’s teammates should not run the code!

In the next round, use set.seed(2), and so on. You can also just use arbitrary random number seed values (instead of 1, 2, etc.) so long as you don’t reuse the same random number seed value in another turn.

There will be some repeats as there are only about 100 underlying word, but the presenter should still use them. To make it more interesting the presenter should not give any indication that the word was already played.

A bit of geekiness: in addition to the use of statistics and computing words, we’re making use of reproducible random numbers (unit 10 of the class), getting data into R (unit 2), and the next_word function uses a functional programming technique called closures (unit 5) to store the underlying word data.

---

[← Game rules](02-game-rules.md) · [Up: contents](index.md)

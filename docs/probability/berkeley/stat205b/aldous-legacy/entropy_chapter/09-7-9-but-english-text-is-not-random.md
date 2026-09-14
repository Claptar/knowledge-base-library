---
title: 7.9 . . . but English text is not random
source: https://www.stat.berkeley.edu/~aldous/205B/entropy_chapter.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/entropy_chapter.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7.9 . . . but English text is not random

**Source:** [`entropy_chapter.pdf`](https://www.stat.berkeley.edu/~aldous/205B/entropy_chapter.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

So one could just demonstrate that compression algorithms work in practice on natural English text, and stop. But this doesn’t address a conceptual issue.

- (B) If you designed a vehicle to work well as an airplane, you wouldn’t expect it to work well as a submarine. So why do algorithms, designed to work well on random data, in fact work well in the completely opposite realm of meaningful English language?

A standard explanation goes as follows. Do we expect that the frequency of any common word (e.g. “the”) in the second half of a book should be about the same as in the first half? Such “stabilization of frequencies” seems plausible – we are not looking at meaning, just syntax, which doesn’t change through the book. This idea of “the rules are not changing” suggests the analogy between written text and a deterministic physical system. An iconic mental picture of the latter is “frictionless billiard balls” which, once set in motion, continue bouncing o↵each other and the table sides forever. For certain kinds of such physical systems, _ergodic theory_ predicts “stabilization of frequencies” – e.g. the proportion of time a ball spends near a corner should be about the same in the first hour as in the second hour. One can

115

#### _7.10. WRAP-UP AND FURTHER READING_

introduce randomness into the story by taking, for the physical system, a random time as “time 0”, or a random page as “page 0” in a text, and then counting time relative to this start. And the notion of “stabilization of frequencies” turns out to be mathematically equivalent to saying that by a special choice of a random initial state (e.g. what we would see at a time chosen at random from a very long time interval) one sees a stationary random process in the sense (7.1). Granted this as a model for English text, we get both “stabilization of frequencies” and the theory for coding that we described earlier, as mathematical consequences.

What is unsatisfactory about that explanation? Well, we are asked to accept, in this particular setting of writing text, the analogy between conscious decisions and a physical system. But it is hard to think of another setting where conscious decisions of a single individual can reasonably be modeled probabilistically, so it begs the question of what is so special about writing text.

---

[← 7.8 Checking for yourself](08-7-8-checking-for-yourself.md) · [Up: contents](index.md) · [7.10 Wrap-up and further reading →](10-7-10-wrap-up-and-further-reading.md)

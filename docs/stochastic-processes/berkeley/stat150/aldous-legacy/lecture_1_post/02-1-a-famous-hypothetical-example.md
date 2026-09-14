---
title: 1. A famous hypothetical example.
source: https://www.stat.berkeley.edu/~aldous/150/lecture_1_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_1_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1. A famous hypothetical example.

**Source:** [`lecture_1_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_1_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A taxi was involved in a hit and run accident at night. Two taxi companies, the Green and the Blue, operate in the city. You are given the following data:


85% of the taxis in the city are Green and 15% are Blue.


A witness identified the taxi as Blue. The court tested the reliability of the witness under the same circumstances that existed on the night of the accident and concluded that the witness correctly identified each one of the two colors 80% of the time and failed 20% of the time.

What is the probability that the taxi involved in the accident was Blue rather than Green?

David Aldous Lecture 1


This is **Bayes rule** , of course. Rather than memorize the formula I find it easier to do the argument directly, as follows.

P(is Blue; and identified as Blue) = 15% _×_ 80% = 12% P(is Green; and identified as Blue) = 85% _×_ 20% = 17% P( identified as Blue) = 12% + 17% = 29% P(is Blue _|_ identified as Blue) = 12% _/_ 29% _≈_ 41%

So the witness is probably wrong!

Extensive work in Psychology and Behavioral Economics on how “ordinary people” think about questions involving probability and risks – “decisions under uncertainty” – see popular book _Thinking, Fast and Slow_ by Kahneman.

David Aldous

Lecture 1

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2. When should you buy every Lotto combination? →](03-2-when-should-you-buy-every-lotto-combination.md)

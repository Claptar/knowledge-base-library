---
title: PS3 Code Review
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/06/codeReview.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/06/codeReview.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# PS3 Code Review

**Source:** [`section/06/codeReview.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/06/codeReview.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Today we will practice paired code review for PS3. In order for this to be of benefit,
you will need to be as honest with your partner as possible. If something is actually
hard to follow, tell them! If you thought that something they did was clever,
also tell them!

### Procedure
First, we will break into pairs of 2. This can be accomplished in one of two ways:

1. You pair up randomly with someone you don't know
2. You count off and I draw numbers for you
    * e.g., `matrix(data = sample(x = 1:n, size = n, replace = FALSE), ncol = 2)`

Second, you will each spend 15-20 minutes reading each other's code while your partner
is available to answer questions you have about their work. I will float around
and can make any clarifying points.

Finally, each of you will fill out [this](https://docs.google.com/forms/d/1xq77Uru0DqZyRTZbQcBywDbEE3uOS31h2dgvJmksyp4/edit)
(also here https://tinyurl.com/statps3rev) google form summarizing the differences
between yours and your partners work, noting anything that was particularly novel
to you.

### Some Guiding Questions

1. Is the code visually easy to break apart? Can you see the entire body of the
functions without scrolling up/down left/right? The general rule-of-thumb is no
more than 80 in either direction (80 character width, 80 lines. The first restriction
should be practiced more religiously)

2. Are the data structures easy to parse? Do you understand what information is in
which objects? Is the type of data appropriate?

3. Are the functions easy to parse? Is it clear what they are doing, what information
is being passed to each function, and what the return value/objects are?

4. Look at the regex. Are there any edge cases that were missed? Was anything handled
particularly well? Any novel expressions that you didn't think of?

5. Look at the plots. Are they well labeled? Is it easy to read information from them?
Do they provide an assurance that the code is running correctly? Was there anything
particularly neat about your partner's solution to the bonus?

6. EXTRA. Look at problem 2, compare/contrast your approaches to OOP. Explain the
logic behind your design.

---

[← PS3 Notes](01-ps3-notes.md) · [Up: contents](index.md)

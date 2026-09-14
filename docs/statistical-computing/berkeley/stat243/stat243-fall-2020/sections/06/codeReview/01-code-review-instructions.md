---
title: Code review instructions
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/06/codeReview.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/06/codeReview.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Code review instructions

**Source:** [`sections/06/codeReview.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/06/codeReview.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

In section this week we will do a paired code review for PS3. In order for this to be beneficial,
you will need to be as honest with your partner as possible. If something is actually hard to follow, tell them! If you thought that something they did was clever, also tell them!

### Procedure
We will break into pairs of 3 (or 2 if necessary) using breakout rooms in Zoom.

Next, you will spend ~10 minutes reading one partner's code, asking questions to the person who's code you are reviewing.  You will rotate this process until each person in the group has their code reviewed.  I will float between breakout rooms to make sure things are going smoothly.

Finally, each of you will fill out the **bCourses assignment PS3 paired code review** summarizing the differences between yours and your two (or one) partner's work, noting anything that was particularly novel to you.

The bCourses assignment is worth 1 point, similar to in class group work or the unit check ins, and will be graded. You will receive credit as long as your response is thoughtful (e.g. at least a couple of sentences). If you choose not to come to section, please find a partner or two on your own to do the paired review with and submit the bCourses assignment by Wed Oct. 7 at 5:59pm to receive credit.

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

[Up: contents](index.md) · [General notes about homeworks →](02-general-notes-about-homeworks.md)

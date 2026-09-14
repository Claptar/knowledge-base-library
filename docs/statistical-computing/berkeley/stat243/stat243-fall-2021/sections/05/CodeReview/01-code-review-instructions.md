---
title: Code review instructions
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/05/CodeReview.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/05/CodeReview.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Code review instructions

**Source:** [`sections/05/CodeReview.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/05/CodeReview.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

In section this week we will do a paired code review for Problem 1 of PS3. In order for this to be beneficial,
you will need to be as honest with your partner as possible. If something is actually hard to follow, tell them! If you thought that something they did was clever, also tell them!

### Procedure
We will break up into pairs of 2 (with a possible group of 3 if necessary).

Next, you will spend ~15 minutes reading one partner's code, asking questions to the person whose code you are reviewing.  You will then switch roles and review the code of the other person in your group.

Finally, each of you will fill out the survey at the following link:
[tinyurl.com/s243-code-review](http://tinyurl.com/s243-code-review), where you will  summarize the differences between your work and  and your  partner's work, noting anything that was particularly novel to you.   You will need to log in with your Berkeley account to access this survey.

The survey response  is worth 1 point, similar to in class group work or the unit check ins, and will be graded. You will receive credit as long as your response is thoughtful (e.g. at least a couple of sentences). If you choose not to come to section, please find a partner or two on your own to do the paired review with and submit the survey  by Wednesday Oct. 6 at 5:59pm to receive credit.

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

6. EXTRA. Look at Problem 2, compare/contrast your approaches to OOP. Explain the
logic behind your design.

---

[Up: contents](index.md) · [General notes about homeworks →](02-general-notes-about-homeworks.md)

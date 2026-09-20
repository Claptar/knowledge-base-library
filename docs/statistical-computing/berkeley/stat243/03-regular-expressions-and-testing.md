---
title: "3. Regular Expressions and Testing"
course: "Berkeley Stat 243 Fall 2024"
chapter: 3
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 3. Regular Expressions and Testing

## What this covers

This chapter works through an assignment that asks a genuinely open question: now that AI tools
write regular expressions fluently, is it still worth learning the syntax by hand? The assignment
answers it by offering a fork — practice the syntax yourself, or hand the pattern to an AI and
spend your effort making sure it is actually correct. It assumes you already know what a regular
expression is (a pattern that matches strings) and have a shell with `grep` available.

## Two ways to work with a pattern-matching problem

The assignment sets up a real trade-off rather than a single exercise. Writing a regular expression
by hand forces you to think in terms of the building blocks — a class of allowable characters at a
position, a count of how many times something repeats, a choice between alternatives, a boundary
that anchors the match. That vocabulary transfers to reading *anyone's* regular expression, AI-written
or not. But it is also syntax that is easy to get wrong in small, silent ways, and current AI tools
are, by the lecturer's own admission, already good at producing it. So the second path is not "skip
the topic" — it is to spend the effort somewhere else: writing down, precisely, what counts as a
match and what does not, *before* looking at any candidate pattern, and then checking a
generated pattern against that specification. Both paths require the same underlying skill —
being exact about what a string does and does not satisfy — just applied at different ends of the
problem.

## Option 1: constructing patterns by hand

Each of the four scenarios isolates one piece of regular-expression vocabulary, without naming it:

1. **"dog" in any mixture of upper and lower case.** This is a question about case: does the match
   need to be case-insensitive, or can each letter be written as a set of its two forms?
2. **"cat", "caat", "caaat", ...** — a single letter repeating an unbounded number of times. This is
   a question about repetition: how do you say "one or more of this" rather than listing every
   length by hand?
3. **"cat", "at", "t"** — each string is the previous one with its front trimmed. This is a
   question about making part of a pattern optional, so that dropping a prefix still matches.
4. **Two words separated by any amount of whitespace.** This combines matching "some sequence of
   non-whitespace characters" with matching "one or more whitespace characters," rather than a
   single fixed-width gap.

The assignment deliberately does not want a single "correct" pattern for each — it asks you to find
more than one way to express the same match, which is the point of practicing the syntax rather
than just producing an answer: several different pieces of vocabulary can solve the same problem,
and comparing them is how the vocabulary sticks.

## Option 2: generating a pattern, then trying to break it

The second path inverts the order of work. Instead of writing the pattern first, you:

1. Pick one target: valid email addresses, English words (including hyphenated and possessive
   forms), or phone numbers from a chosen country.
2. **Write the test cases first** — an extensive set of strings that should match, and, just as
   importantly, strings that look plausible but should *not* match. This step is the actual content
   of the exercise. A regular expression is easy to eyeball and hard to verify by inspection; a
   pattern that looks right can still admit an unintended string or reject a valid one at the
   edges (an email with a `+` in the local part, a possessive that ends in `'s`, a phone number
   with an extension). Writing the negative cases is what forces those edges into view *before* you
   have a candidate pattern to be attached to.
3. Only then ask an AI tool to produce a regular expression for the target.
4. Check the generated pattern against every test case using `grep -E` in the shell, rather than
   trusting it on inspection.

The reasoning behind this order is the same reasoning behind test-driven development in software
more generally: specifying the desired behaviour before you have an implementation stops the
specification from being quietly bent to match whatever the implementation happens to do. Here the
"implementation" is a regular expression you did not write yourself, which makes an independent,
pre-written test set the only real check you have on it.

## Exercises

**Option 1.** Using regular expression syntax (any reasonable form; try to find more than one for
each), write a pattern that matches:

1. The word "dog" in any combination of upper and lower case: "dog", "Dog", "dOg", "doG", "DOg",
   and so on.
2. "cat", "caat", "caaat", and so on — the letter `a` repeated any number of times.
3. All three of "cat", "at", and "t".
4. Two words separated by any amount of whitespace.

**Option 2.** Choose exactly one of the following. First write an extensive set of test strings —
both strings that should match and strings that should not. Then use an AI tool to produce a
regular expression for the pattern, and check it against every test case with `grep -E`.

- Valid email addresses.
- English words, including hyphenated words and possessive forms.
- Phone numbers, from the US or from another country of your choosing.

## Sources

- The assignment text, both options and all seven scenarios: "Assignment: regex/testing problems,"
  `units/assignment2.qmd`, Berkeley STAT 243, Fall 2026 (converted from the course repository,
  licensed CC BY 4.0).
- The assignment refers students to the "regular expression section of the bash shell tutorial" at
  `computing.stat.berkeley.edu/tutorial-using-bash/regex` for the syntax itself. That tutorial page
  was not supplied as input and its content is not reproduced here.

---

[← 2. Bash Shell Tutorial and Exercises](02-bash-shell-tutorial-and-exercises.md) · [Contents](index.md) · [4. The Cohort Location Model →](04-the-cohort-location-model.md)

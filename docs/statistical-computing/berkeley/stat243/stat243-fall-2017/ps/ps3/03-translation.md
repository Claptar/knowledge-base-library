---
title: Translation
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/ps/ps3.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/ps/ps3.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Translation

**Source:** [`ps/ps3.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/ps/ps3.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Your job is to extract data from the complete works of William Shakespeare, available as plain text at **http://www.gutenberg.org/cache/epub/100/pg100.txt** .

The goal of Problem 2 is two-fold: first to give you practice with regular expressions and text manipulation and the second to have you thinking about writing well-structured, readable code. Regarding the latter, please focus your attention on writing short, modular functions that operate in a vectorized manner and also making use of _apply()_ / _lapply()_ / _sapply()_ to apply functions to your data structures. Comment your code as needed so it is clear what each piece of code does. Think carefully about how to structure your objects to store the information about the plays. If you prefer you can use an object-oriented approach, thereby combining problems 2 and 3 of this problem set.

- (a) Extract the plays into a character vector or a list, with one element for each play. Skip the information at the start of the file, the first piece (the sonnets), and the last piece (Lover’s Complaint).

- (b) Extract meta data about each play and extract the body of the play. The result should be in the form of an R object, with one element for each play. By meta data I mean the year of the play, the title, the number of acts, and the number of scenes.

- (c) Extract the actual text spoken by the characters into your object. You should store each chunk of spoken text and store the speaker of each chunk. Discard stage directions, Dramatis personae

2

information, and scene information. Note that the stage directions come in many forms, with inconsistent formatting, so we’re not expecting perfection here – you’ll likely accidentally include a small number of stage directions as part of your spoken text.

- (d) Now use the constructed data object to calculate summary statistics about each play. These should include the following:

   - i. The number of unique speakers.

   - ii. The number of spoken chunks.

iii. The number of sentences and words spoken and average number of words per chunk. iv. The number of unique words.

   - When extracting words, make sure you remove punctuation such as commas and periods but not apostrophes.

- (e) Plot some of your summary statistics as a function of time to see if there are trends in Shakespeare’s plays over the course of his writing career. Also in your solution, please report the number of acts and scenes, number of unique speakers, and number of chunks for each play; we’ll look at this to see if your processing made any large-scale errors.

- (f) Extra credit: particularly clever or thorough treatments of the problem may earn extra credit, such as avoiding excluding any plays or sophisticated treatment of songs and other items that are hard to handle. If you’d like your solution to be considered for extra credit, describe what you’ve done that you think does a good job of handling tricky aspects of the text.

---

[← ACT Post-Berkeley](02-act-post-berkeley.md) · [Up: contents](index.md) · [HINTS →](04-hints.md)

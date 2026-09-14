---
title: 1.5 Greedy Matching
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/regexpr-Lang.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/regexpr-Lang.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.5 Greedy Matching

**Source:** [`units/regexpr-Lang.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/regexpr-Lang.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

To figure out, or disambiguate, the meaning of a word, we can see how it is used in other contexts by other authors. For example in a phrase such as “put a program in place”, we (or software for checking grammar) might not know if the prepositional phrase “in place” modifies the verb “put” or the noun “program”. More generally, with phrases that have the form: verb noun1 preposition noun2, we want to determine if the prepositional phrase modifies the verb or the first noun. One way to determine this is to rearrange these words where the new arrangement clearly implies whether it is the verb or the noun that is being modified. The Web can serve as a corpus of examples, where the occurrence of the particular rearrangement in a Web page would constitute a vote for verb or noun. Search engine can assist us in finding these web entries.

One rearrangement is: preposition noun2 up-to-three-words noun1. The occurrence of this ordering of the words would indicate that the prepositional phrase modifies the verb.

In our example, a Google search for "in place" program returns entries such as the following three.

2003 Total Aging In Place Program. All rights reserved. Web site design, hosting and maintenance provided by The PCA Group, Inc. ...

I will use the knowledge learned from the program in the daily operations of my job as an In-Place Test Technician. Due to the informative materials of the ...

Additionally, qualified students may participate in an internship in place of one of their courses. (See Madrid Internship Program description for details. ...

Notice that in the first phrase, we have the phrase “in place” immediately followed by “program”. However, in the second phrase, program comes before our prepositional phrase, and in the third there are are more than three words between the phrase and “program”.

13

The actual text returned is not plain text as shown above, but HTML. That is, the text is marked up with annotations that tell the Web browser how to display the text. For example, we see below that there is extra text, such as </b> that we wish to ignore when counting words between the preposition and the second noun.

Additionally, qualified students may participate in an internship <b>in place</b> of one of their courses. (See Madrid Internship <b>Program</b> description for details. <b>...</b>

Essentially, we want to strip out the html from the text before we go about checking the order of the noun and prepositional phrase and counting the words between them. Consider the following substitution to do exactly that,

> googleText [1] "Additionally, qualified students may participate in an internship <b>in place</b> of one of their courses. (See Madrid Internship <b>Program</b> description for details." > gsub("<.*>", "", googleText) [1] "Additionally, qualified students may participate in an internship description for details."

This substitution did not give us what we expected. The problem is greedy matching. The pattern <.*> searches for a pair of angle brackets with any characters between. Although, <b> is a match, so is <b>in place</b> and

<b>in place</b> of one of their courses. (See Madrid Internship <b>Program<b>+

also constitutes a match. All begin with < followed by _any_ characters (including > in this case) followed by >. The regular expression engine performs greedy matching here, and matches the largest substring possible, which is more than we want. we need to exclude the > from the set of all characters. Anything but the > can be matched,

> gsub("<[ˆ>]*>", "", googleText) [1] "Additionally, qualified students may participate in an internship in place of one of their courses. (See Madrid Internship Program description for details."

That is the result we are after.

---

[← 1.4 Advanced Notions](04-1-4-advanced-notions.md) · [Up: contents](index.md) · [1.6 Summary →](06-1-6-summary.md)

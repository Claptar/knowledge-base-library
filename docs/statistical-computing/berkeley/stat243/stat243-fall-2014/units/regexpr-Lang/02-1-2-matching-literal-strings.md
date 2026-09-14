---
title: 1.2 Matching literal strings
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/regexpr-Lang.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/regexpr-Lang.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.2 Matching literal strings

**Source:** [`units/regexpr-Lang.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/regexpr-Lang.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The inconsistencies in the various sources of information for making the election map (Section 1.1.1) are easily remedied. For example, “County” or “Parish” can be removed from the end of each county name. Fixing the problem with the missing period in the names such as “St John the Baptist Parish” is slightly more subtle. Many counties in the United States have “St” in their names and we want to make sure that we change all occurrences of “St” to “St.” However, we also want to be sure not to change, a name such as, “Stone County” to “St.one County”. If we search for the pattern ’St ’ and change it to ’St. ’, then that should avoid this problem.

Rather than edit data files manually, it is better to make the changes programmatically in order to keep a record of the changes required in case mistakes are made or the process needs to be repeated when the data change. Using any general programming language such as Matlab, Java, C, Perl, etc., we could develop a function to perform this simple task for operating on strings and patterns within them.

> string

[1] "St John the Baptist Parish" > if ("St " == substring(string, 1, 3)) + newString = paste("St. ", + substring(string, 4, nchar(string)), sep ="")

> newString [1] "St. John the Baptist Parish"

If we are not sure that the pattern will occur at the beginning of the string, then we need a more general approach. Below we split the input string into a vector of single characters, and iterate over these characters looking for the particular string. That is, determine which of these characters are possible starting points of the pattern, i.e. S.

> characters = unlist(strsplit(string, "") )

> characters [1] "S" "t" " " "J" "o" "h" "n" " " "t" "h" [11] "e" " " "B" "a" "p" "t" "i" "s" "t" " " [21] "P" "a" "r" "i" "s" "h" > possible = which(characters == "S") > substring(string, possible[1], possible[1] + 2) [1] "St "

#### **1.2.1 Fundamental Approach**

We can write a more general R function that would determine if an input text _string_ contained the argument _pattern_ .

findPattern = function(pattern, string) { lets = strsplit(string,"") firstLetter = substring(pattern, 1, 1) possibles = which(lets[[1]] == firstLetter) if (length(possibles) > 0) any(pattern == substring(string, possibles, possibles + nchar(pattern) -1)) else return(FALSE) }

This function matches a _literal_ string given by _pattern_ within the given _string_ by searching for all the occurrences of the first character in _pattern_ and then looking at all substrings with the same length as _pattern_ starting from those points. It illustrates the fundamental approach to pattern matching, e.g. when we look for the literal string St in a line of text. When we write down a regular expression pattern like ’St ’,

4

The Slippery St Frances.

|| ||| || ||| Found S _______|| ||| Followed by t?__| No ||| Is it S? _______| No ...||| Keep looking for an S ||| Found S ________________||| Followed by t? __________|| Yes Followed by blank? _______| Yes - A Match!

Figure 1.1: A diagram of a search for the literal string ‘St ’. The regular expression matching engine looks for the first character ‘S’, immediately followed by t’, immediately followed by blank. When it finds the ‘S’ in Slippery, it then checks if the next character is a ‘t’. Since it is not, it starts over and checks to see if it is an ‘S’, and continues looking for an ‘S’. The most basic building block in a language that supports matching patterns in text is a facility for specifying a short string of text in a literal string as a pattern to match.

what is meant is really the following: find the character S immediately (i.e. the next character) followed by t, immediately followed by a blank character. What the regular expression matching engine does is, for the target string, start at the first character and check to see if it is an S. If not, then move to the second character and start looking there. When it finds an S, it then checks if the next character is a t. If not a t, then start over and check if this character is an S and so on. So we can think of the literal string as being made up of three consecutive sub-patterns: S, t and ‘ ’. Thinking of the pattern ’St ’ in this way makes it easier to see how to combine different types of complex patterns to define a sequence (see Figure 1.1 for an example of this search process).

There are two functions in R, _gsub()_ and _sub()_ , that look for the pattern and replace it within a string with some other text. Each of these functions takes three arguments: the regular expression (pattern) defining what to match, another regular expression to use as the replacement text, and the string(s) on which to do the matching and substitution.

The ‘g’ in the name _gsub()_ refers to _global_ . This means that it changes all the matches of the regular expression in the text with the replacement pattern. The _sub()_ is almost exactly the same as _gsub()_ except that it only replaces the first occurrence of the pattern with the replacement text. In our example here, we expect there to be one occurrence of “St ” in the string, and so _sub()_ should work fine.

> countyNames [1] "Dewitt County" "Lac qui Parle County" [3] "St John the Baptist Parish" "Stone County" > gsub("St ", "St. ", countyNames) [1] "Dewitt County" "Lac qui Parle County" [3] "St. John the Baptist Parish" "Stone County"

As an illustration of how _gsub()_ differs from _sub()_ , we replace the word (or literal string, actually) “one” with the digit “1” in the following simple character vector.

> strings = c("a test", "and one and one is two", "one two three")

> gsub("one", "1",strings)

[1] "a test" "and 1 and 1 is two" "1 two three"

Notice, there was no “one” in the first string (“a test”), so there was no way to substitute the match with the replacement text (“1”). So it remains unaltered and is returned as is. In the second string, there are two occurrences of the string “one”. Each of these are replaced with the digit “1”. And similarly, the third string

5

has its single occurrence of “one” replaced with “1”. In contrast, the _sub()_ replaces only the first occurrence of “one” with “1” in the second string.

> sub("one", "1", strings)

[1] "a test" "and 1 and one is two" "1 two three"

The language of regular expressions is far more powerful than illustrated by this simple example. The next examples build on this pattern matching technique to demonstrate the more advanced features of the regular expression language.

---

[← 1.1 Introduction](01-1-1-introduction.md) · [Up: contents](index.md) · [1.3 Character Classes →](03-1-3-character-classes.md)

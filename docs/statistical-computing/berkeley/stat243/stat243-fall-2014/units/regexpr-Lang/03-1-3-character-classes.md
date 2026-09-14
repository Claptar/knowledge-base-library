---
title: 1.3 Character Classes
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/regexpr-Lang.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/regexpr-Lang.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.3 Character Classes

**Source:** [`units/regexpr-Lang.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/regexpr-Lang.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Searching the subject line for “Re:” in an email message (Section 1.1.2) is a task similar to the pattern search in the previous example; the simple function _findPattern()_ should easily handle the job. The other patterns present more of a challenge. For example, if we are looking for email addresses that contain digits, then any digit 0 through 9 found anywhere in the address would be considered a match. The function _findPattern()_ cannot handle this more complicated pattern, as it is only capable of performing a simple literal string comparison. Here we want to ask about alternative patterns, i.e. of the form this or that. In this case, we could split the string into separate characters and check whether any of these are digits. Similarly, to find a fake word that contains punctuation in the middle of it, we could split the subject line into individual characters, search for punctuation or a digit, and if we find it, then look at the preceding character and the succeeding character to ascertain whether they are letters of the alphabet (upper or lower case). So any letter–punctuation or digit–letter combination is a match.

We can write a suite of functions to perform the different types of matching and substitutions required of this problem. Since the search for any digit or any alpha character are commonly needed, it is reasonable to guess that others might have already implemented these for their purposes and we might be able to reuse their code. As with all software, we would like to reuse such code as it is likely to be better tested and more efficient than our initial efforts. Ideally, we would be able to use a language to express these patterns in a unified manner. Indeed, the regular expression language is such a general language that has several implementations that are well-tested and efficient.

It provides basic building blocks for specifying patterns that are to be matched in a piece of text. These allow us to match literal strings, a character from a particular set of characters or its complement (character sets), and one sub-pattern or another (alternation). We can also match by position such as at the beginning or end of a line, and we can create sub-patterns from individual patterns by specifying the number of times the pattern should be matched (quantifiers).

#### **1.3.1 Equivalent Characters**

For the search in an email address for a digit, the pattern we want to match could contain any digit: 0, 1, 2, 3, 4, 5, 6, 7, 8 or 9. Regular expressions allow us to succinctly express the concept of “match a digit”, by explicitly enumerating the equivalent characters. We use the [ ] notation to identify a collection of equivalent characters, called a _character class_ , that specify the collection of characters that constitute a match. For example, to match a digit, we us [0123456789]. Similarly to match a lower case letter, we use

[abcdefghijklmnopqrstuvwxyz]

and to match a space or a TAB character, we use [ \t].

6

|Name|Collection of characters|
|---|---|
|[[:alnum:]]|All alphabetic and numeric|
|[[:alpha:]]|All alphabetic|
|[[:lower:]]|Lower case alphabetic characters|
|[[:upper:]]|Upper case alphabetic characters|
|[[:digit:]]|Digits0123456789|
|[[:punct:]]|Punctuation characters|
|[[:blank:]]|Blank characters, i.e. space or tab|
|[[:space:]]|White space|
|[[:cntrl:]]|Control characters, e.g. new line|
|[[:print:]]|Printable characters|
|[[:graph:]]|Printable character except space|


Table 1.1: Some useful named character classes.

Basically, we can enumerate any collection of characters within the [ ] and these are included in the set of characters that constitutes a match. We also adapt this notation very slightly to indicate a match on the complement of the set of characters. That is, we place a caret _∧_ as the first character within [] to indicate that the equivalent characters are the complement of the characters enumerated within, i.e. anything but these characters is considered a match.

There are many collections of characters that are commonly used. For example, we often want to specify all the letters of the alphabet, lower or upper case or both. And we often want all the digits. And in other cases, we want a subset of these sets. The _−_ character when used within the character class pattern (i.e. the []) typically identifies a range. We can specify the digits 0 through 9 more readily as [0-9] and the subset of the digits 3, 4, 5, 6 can be specified as [3-6]. Similarly, we can specify [0-9A-F] to match all the hexadecimal digits. And you will often see [A-Za-z] for all letters (upper and lower case) in the alphabet. Once again, the pattern expresses a higher level concept that is easier to read than explicitly enumerating the elements of the character set.

Note, if we want to include the character _−_ in our set of characters to match, then we must put this at the beginning of the character set, otherwise it is interpreted as a range. For example, to match the basic arithmetic operators +, _−_ , _∗_ or _/_ , we can use [-+*/] Or to match a digit with either a + or _−_ in front of it, we can use [-+][0-9] That is, we have made an overall pattern from a _sequence_ of two sub-patterns and each of these sub-patterns is made up using the primitive elements. The first - is for the literal character and the second is for the special character that denotes a range.

#### **1.3.2 Named Character Classes**

Character classes are very convenient, and the range operator ( _−_ ) succinctly specifies collections of characters to further simplify their use. The regular expression language also provides a collection of built-in character sets for commonly used collections. Each of these is identified by a short name. See Table 1.1 for a description of some of these named character sets.

We use these collections with the same [] notation, but we specify the named character set with an additional [::] pair. So, for example, to specify the punctuation characters, use [[:punct:]] The [:punct:] term is the named character class. Additional characters can be included in the overall set such as [[:digit:]_] to consider a match any digit _or_ the underscore character.

7

The search for a digit or an underscore in the email can now be easily performed.

###### > Addresses

[1] "Duncan Temple Lang <duncan@wald.ucdavis.edu>"

[2] "depchairs03-04@uclink.berkeley.edu"

[3] "Faustino Britt <Faustino@sfera.umk.pl>" > grep("[[:digit:]_]", Addresses)

[1] 2

The _grep()_ function in R takes two arguments, the regular expression specifying the overall pattern to match and then a character vector containing the different text strings on which to search. It returns the indices of the elements of that character vector for which there was a match (or the empty integer vector if none matched). This can be readily used to subset the character vector to get only the elements containing or not containing that pattern. The return value from the call to _grep()_ above is 2 because a digit was found in the second element of the character vector _Addresses_ . The _grep()_ is also available in the shell (see Chapter **??** ).

The search for a fake word that contains punctuation or a digit in the middle of it is handled by the following pattern

###### [[:alpha:]][[:digit:][:punct:]][[:alpha:]]

Paying careful attention to the square brackets in this pattern, we see that we are looking for three characters. The first can be any letter in the alphabet (upper or lower case), followed by a digit or punctuation mark, followed by another letter. Unfortunately this pattern matches the text string “it’s”, which we do not want. This problem can be resolved by providing the specific punctuation marks that are acceptable in the character class,

[[:alpha:]][[:digit:]!@#$%ˆ&*():;?,.][[:alpha:]]

or we could first remove any quotation marks from the search string and then use the original pattern.

> s = c(subjectLines, "It’s me")

> s [1] " Re: 90 days" "[SPAM:XXXXXXXXX]" [3] " Fancy rep1!c@ted watches" "It’s me" > newString = gsub("’", "", s) > grep("[[:alpha:]][[:digit:][:punct:]][[:alpha:]]", newString) [1] 2 3

Note that the search did not match the “Re:” because the colon is followed by a blank, nor does it match the fourth element because the ’ has been removed from the string. It does find a match in the second element and the third element. To find exactly where the pattern was found in these strings, we can use the _regexpr()_ function.

> regexpr("[[:alpha:]][[:digit:][:punct:]][[:alpha:]]", newString) [1] -1 5 13 -1 attr(,"match.length") [1] -1 3 3 -1

The return value of _−_ 1 indicates that the pattern was not found in the first and fourth elements of _newString_ . As for the second element, the return value of 5 indicates that the pattern was found beginning at the fifth character in the string, and the value of the attribute _match.length_ for this element in the return vector indicates that the match is three characters long. The fifth through eighth characters in [SPAM:XXXXXXXXX] are M:X and so we have found the pattern we expected to find.

Notice that the match found in the third element of _newString_ uncovers one more limitation in our pattern specification: the pattern was found in characters 13-15 in the string, i.e. c@t. That is, we did not find p1!c

8

because it consists of four characters: a letter, followed by a digit, followed by a punctuation mark, followed by a letter. To search for the more general pattern of any number of digits or punctuation marks between letters, we must change the pattern as follows.

##### [[:alpha:]][[:digit:][:punct:]]+[[:alpha:]]

The plus sign between the second and third characters in the pattern indicates that the second character may appear one or more times.

#### **1.3.3 Meta Characters**

The characters [ ] and [: :] and + are given special meaning in a pattern; these special characters are called meta characters. Regular expressions offer a rich set of meta characters for pattern matching. For example, meta characters make easy work of the task to derive is a logical that indicates whether or not the subject line in an email is all capital letters. This phenomena in email is referred to as yelling. Here is a case when the complement of a character set is useful because we allow any character except lower case letters of the alphabet in the subject line of the email. But we face the problem of needing every character in the subject line to _not_ be a lower case letter. We want to specify a pattern that consists of non-lower case letters from the beginning to end without knowing how long it is. Again, we can write a specialized function to do the work,

> subjectLines [1] " Re: 90 days" "[SPAM:XXXXXXXXX]" [3] " Fancy rep1!c@ted watches" > all(strsplit(subjectLines,"")[[1]] %in% LETTERS) > FALSE

but regular expressions provide a clean, clear way to express this pattern via meta characters.

ˆ[ˆ[:lower:]]*$+

To explain, the first character in this pattern, the ˆ is the anchor for the beginning of the string, and the last character, $ is the anchor to specify the end of a string. The asterisk denotes “any number of times” meaning that the character immediately preceding it may be repeated zero or more times. Put all together, the pattern finds a match when the string consists entirely of non-lower case letters from beginning to end. Note that the caret ˆ appears twice in the pattern, and each occurrence has a different meaning. The first caret is the meta character for the beginning of line anchor, and the second caret, which is the first character inside the square brackets, represents the complement meta character that says any character that is not a lower case is a match.

> grep("ˆ[ˆ[:lower:]]*$", subjectLines)

[1] 2

Table 1.2 provides a list of some of the more useful meta characters. Note that the position of a character in a pattern determines whether of not it is treated as a meta character. For example, the * is a meta character in the above pattern that searches for one or more non-lower case letters. However, in the example of Section 1.3.1, the * in the character class is treated not as a meta character but as the literal asterisk, [-+*/].

---

[← 1.2 Matching literal strings](02-1-2-matching-literal-strings.md) · [Up: contents](index.md) · [1.4 Advanced Notions →](04-1-4-advanced-notions.md)

---
title: 1.4 Advanced Notions
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/regexpr-Lang.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/regexpr-Lang.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.4 Advanced Notions

**Source:** [`units/regexpr-Lang.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/regexpr-Lang.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the Web log analysis (Section 1.1.3), our ultimate goal is to transform a line in the Web log into a line of comma-separated values for the IP address, date, file, status, and, bytes. Before we do this, we look at the simpler problem of extracting the date and time only. That is, we want to grab the information between the square brackets, ignoring the time zone piece (e.g. -0800). Square brackets do not appear elsewhere in the line, and so a search for a left square bracket will bring us to the date. Below is one line of text from the web log as a character string in R.

9

|Character|Meaning|
|---|---|
|ˆ|As the first character in the pattern, anchor for beginning of line|
||As the first character inside[ ], exclude these characters.|
|$|End of line anchor|
|?|Character or sub-pattern occurs zero or one time|
|+|Character or sub-pattern occurs one or more times|
|*|Character or sub-pattern occurs zero or more times|
|.|Any single character|
|[ ]|Character class|
|-|Range within a character class|
|( )|Group or sub-pattern|
|||Alternation, i.e. one sub-pattern or another|
|{ }|Quantifier: {n}means exactlynrepeats of the sub-pattern<br>{n,m} ntomrepeats|
||{n,} nor more repeats|


Table 1.2: Some useful meta characters. Note to search for one of these characters as a literal, it may have to be preceded by a backslash (or two backslashes in R).

> weblog [1] "169.237.46.168 - - [26/Jan/2004:10:47:58 -0800] \"GET /stat141/Winter04 HTTP/1.1\" 301 328 \"http://anson.ucdavis.edu/courses/\" \"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322)\""

Notice that quotation marks appear with a backlash that acts as an escape character, so the quotation mark within the character string does not end the character string.

The following regular expression searches for the left square bracket followed by any number of characters followed by a right square bracket:

> regexpr("\$$.*\$$", weblog) [1] 20 attr(,"match.length") [1] 28

To search for a literal square bracket, we need to use the backslash twice, once to escape from R and again to escape from the regular expression use of [ as a meta character. The pattern contains two meta characters, the verb+.+ which stands for any character, and the * which says any character may be repeated many times (actually zero or more times). Essentially, the pattern will produce a match when it finds any string between [ and ].

The function _regexpr()_ returns more detailed information than the other R functions we have seen in this chapter for handling regular expressions. It provides a) which elements of the character vector actually contained the pattern in the regular expression, and also b) identifies the position of the substring that was matched by the regular expression pattern.

The return value from our search is the integer 20, the position of the starting character of the match. In this case, it tells us that the left square bracket is the 20th character in the string. Also, the attribute “match.length” is 28 which indicates that the matching string, from [ to ] is 28 characters long. This length of the matching pattern is returned in a slightly odd form because it allows us to treat the return value from

10

_regexpr()_ directly as a simple integer vector while still carrying around additional information with it. To get the substring in the string that corresponds to the date and time, we can use this return value along with _substring()_ :

> x = regexpr("\$$.*\$$", weblog)

> substring(weblog, x + 1, x + attr(x, "match.length")-8) [1] "26/Jan/2004:10:47:58"

The _regexpr()_ function is a very useful tool for getting an understanding of what a particular pattern actually matches. We can create a pattern to match and then give it different test strings and see which parts actually match. This is a very important exercise to practice to really understand regular expressions. As an example, if we return to the simple example seen earlier where we look for the string ”one”, we can use _regexpr()_ to determine where in the strings it occurs.

> regexpr("one", c("a test", "a basic string", "and one that we want", "one two three"))

[1] -1 -1 5 1 attr(,"match.length") [1] -1 -1 3 3

The return value is an integer vector with an element for each of the elements in the vector. Each element in the return vector gives the position of the starting character of the match, if it exists, and -1 when no match occurs for that string.

#### **1.4.1 Grouping and references**

An alternative way to pull out the date and time from the Web log is via references. That is, we locate the substring in the Web log that is of interest and pull it out by reference. The parentheses meta characters ( ) group together a sub-pattern, which can be referred to in a later pattern. The pattern,

.*\$$(.*) [-+].*\$$.*

looks for a string that consists of any characters any number of times, followed by a left square bracket. Then any characters any number of times followed by a blank, then either a _ or + then and characters, a right square bracket, followed by any characters. Notice that the second pattern of “any characters” is contained in parentheses, i.e. (.*), which makes it a sub-pattern. This sub-pattern can be referred to as \\1 in a substitution string,

> gsub(’.*\$$(.*)\$$.*’, ’\\1’, weblog)

[1] "29/Dec/2003:06:36:18 -0600"

Essentially we have substituted the entire line of text in the Web log with the sub-pattern found in \\1, which is the sub-pattern found between the square brackets. We need the final .* because without it,

> gsub(’.*\$$(.*)\$$’, ’\\1’, weblog) [1] "29/Dec/2003:06:36:18 -0600 \"GET /logo.html HTTP/1.1\" 200 244 "http://anson.ucdavis.edu/courses/" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0;

.NET CLR 1.1.4322)"

the end of the string is not eliminated. The pattern here matches all of the characters in a line in the Web log up to and including the information in the square brackets. It substitutes all of this with the sub-pattern found, i.e. with the characters between the square brackets, but we want to substitute the entire line with the sub-pattern. Further, we can drop the time zone offset by making our pattern a bit more precise,

> gsub(’.*\$$(.*) [-+][0-9]+\$$.*’, ’\\1’, weblog)

[1] "29/Dec/2003:06:36:18"

Here, we sub-pattern consists of those characters in the square brackets that appear before the time zone offset, which is specified by a blank, followed by either a plus or minus, followed by one or more digits and then a right square bracket. The + meta character in [0-9]+ means one or more of the preceding character, i.e. one or more digit in this case.

11

#### **1.4.2 Alternation**

Grouping can be very handy when you want to express the notion of equivalent sub-patterns. For example, in the Web log the command is either GET or PUT, and we see that it appears in quotes along with the file name.

... "GET /logo.html HTTP/1.1" 200 244 ...

In our search for the file name, we see that it occurs between the GET and the HTTP. A regular expression that extracts the file name can use this structure.

> gsub(’.*"GET (.*) HTTP.*’, ’\\1’, weblog) [1] "/logo.html"

However, when the GET is a PUT or when the HTTP is an FTP then our substitution will not work as expected. Alternation comes to the rescue. We search for GET or PUT by using the pattern (GET|PUT) and similarly we can replace HTTP with (HTTP|FTP),

> gsub(’.*"(GET|PUT) (.*) (HTTP|FTP).*’, ’\\1’, weblog) [1] "GET"

We did not get the file name this time. What went wrong? Our regular expression has changed. Now it has three sub-patterns instead of one. The alternation (GET|PUT) is the first sub-pattern, and now the one that we want is the second,

> gsub(’.*"(GET|PUT) (.*) (HTTP|FTP).*’, ’\\2’, weblog) [1] "/logo.html"

Note that we could express a character class using _alternation_ . For example, rather than [0-9], we could use the construction: “(0 _|_ 1 _|_ 2 _|_ 3 _|_ 4 _|_ 5 _|_ 6 _|_ 7 _|_ 8 _|_ 9)” for our pattern. This is tedious to write and becomes difficult to read as the number of characters to be matched becomes lengthy. We are not succinctly expressing the concept of “match a digit”, but instead we are explicitly enumerating the characters. This makes maintaining and understanding the regular expression more difficult. Additionally, these single character alternations are not very efficient. They can slow down the speed with which the regular expression automata performs the matching.

#### **1.4.3 Number of matches**

We have seen two meta characters that can be used to denote multiplicity in matching. These are * for zero or more and + for one or more. Another is ? for zero or one. Regular expressions also allow the specification of an explicit number of matches via the curly braces { }. For example, {4} denote exactly four. Applied to our time zone problem, we could explicitly specify four digits following the plus/minus sign as follows,

> gsub(’.*\$$(.*) [-+][0-9]{4}\$$.*’, ’\\1’, weblog)

[1] "29/Dec/2003:06:36:18"

Ranges can also be specified with the curly braces. For example, {4,} means four or more matches, and {4,7} means four to seven matches.

At last , we have the concepts that will enable us to tackle the original problem to transform a Web log entry:

193.188.97.151 - - [29/Dec/2003:06:36:18 -0600] "GET /logo.html HTTP/1.1" 200 244 ...

into the comma separated values:

193.188.97.151, 29/Dec/2003:06:36:18, /logo.html, 200, 244

12

which has extracted the IP address, date, file name, status, and, number of bytes transferred.

As we have seen, each of these pieces of information can be located in the file by carefully examining the structure of the file. The IP address comes first, and is always followed by two dashes. Then comes the date and time between square brackets, followed by either the command GET or POST command, file name, and HTTP or FTP all in quotation marks. Finally, the last two numbers in the file are the status and the number of bytes, respectively. We can construct a regular expression that describes the Web log line and uses parentheses to extract sub-patterns of interest.

(.*) - - \$$(.*) [-+][0-9]{4}\$$

"(GET|POST) (.*) (HTTP|FTP)(/1.[01])?" ([0-9]+) (-|[0-9]+).*

The first subgroup will match the IP address, the second will match the date and time, the third will match GET or POST, and so on. The subexpressions that we wish to keep are the first, second, fourth, seventh, and eighth. The substitution string can refer to these sub-patterns and build text that consists of these four values separated by commas: \\1,\\2,\\4,\\7,\\8

> gsub(’(.*) - - \$$(.*) [-+][0-9]{4}\$$ "(GET|POST) (.*) (HTTP|FTP)(/1.[01])?" ([0-9]+) (-|[0-9]+).*’, ’\\1, \\2, \\4, \\7, \\8’, weblog) [1] "193.188.97.151, 29/Dec/2003:06:36:18, /logo.html , 200, 244"

The substitution string skipped over the groups that we needed for the match, but not for the output. (It is possible to avoid numbering these groups, if necessary.)

---

[← 1.3 Character Classes](03-1-3-character-classes.md) · [Up: contents](index.md) · [1.5 Greedy Matching →](05-1-5-greedy-matching.md)

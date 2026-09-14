---
title: 5 Basic UNIX utilities
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Basic UNIX utilities

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In some of what follows, we’ll use the _cpds.csv_ file in the _data_ directory of the class repository.

Table 2 shows some basic UNIX programs, which are sometimes referred to as filters. The general syntax for a UNIX program is

- command -options argument1 argument2 ...

For example,

3

<u>Table 2: UNIX utilities</u>

|Name|What it does|
|---|---|
|_tail_|shows last few lines of a file|
|_less_|shows a file one screen at a time|
|_cat_|writes file to screen|
|_wc_|counts words and lines in a file|
|_grep_|findspatterns in files|
|_wget_or_curl_|download files from the web|
|_sort_|sorts a file byline|
|_nl_|numbers lines in a file|
|_diff_|compares two files|
|_uniq_|removes repeated(sequential)rows|
|_cut_|extracts fields(columns)from a file|


#### > grep -i graphics file.txt

looks for _graphics_ (argument 1) in _file.txt_ (argument2) with the option _-i_ , which says to ignore the case of the letters.

#### > less file.txt

simply pages through a text file (you can navigate up and down) so you can get a feel for what’s in it.

UNIX programs often take options that are identified with a minus followed by a letter, followed by the specific option (adding a space before the specific option is fine). Options may also involve two dashes, e.g., R --no-save. Here are some examples using _tail_ :

   - tail --help

   - tail -n 10 cpds.csv # last 10 lines of cpds.csv

   - tail -f cpds.csv # shows end of file, continually refreshing

   - A few more tidbits about _grep_ :

   - grep ^2001 cpds.csv # returns lines that start with ’2001’

   - grep 0$ cpds.csv # returns lines that end with ’0’

- grep 19.0 cpds.csv # returns lines with ’19’ separated from ’0’

- by a single character

   - grep 19.*0 cpds.csv # now separated by any number of characters

- grep -o 19.0 cpds.csv # returns only the content matching the

- pattern from the relevant lines

Note that the first argument to grep is the pattern you are looking for. The syntax is different from that used for wildcards in file names. Also, you can use regular expressions in the pattern. We won’t see this in detail here, but will see regular expressions in R shortly.

It is sometimes helpful to put the pattern inside double quotes, e.g., if you want spaces in your

4

<u>Table 3: Redirection</u>

|Syntax|What it does|
|---|---|
|cmd > file|sends stdout from_cmd_into _file_,overwriting _file_|
|cmd >> file|appends stdout from_cmd_to _file_|
|cmd < file|execute_cmd_readingstdin from _file_|
|cmd <infile >outfile 2>errors|reads from_infile_,sendingstdout to_outfile_and stderr to_errors_|
|cmd <infile >outfile 2>&1|reads from_infile_,sendingstdout and stderr to_outfile_|
|cmd1 | cmd2|sends stdout from_cmd1_as stdin to_cmd2_ (apipe)|


Note that _cmd_ may include options and arguments as seen in the previous section.

pattern, e.g.,

> grep "George .* Bush" cpds.csv

More generally in UNIX, enclosing a string in quotes is often useful to indicate that it is a single argument/value.

If you want to explicitly look for one of the special characters used in creating patterns (such as double quote (“), period (.), etc., you can “escape” them by preceding with a back-slash. For example to look for _“Canada”_ , including the quotes.

> grep "\"Canada\"." cpds.csv

If you have a big data file and need to subset it by line (e.g., with _grep_ ) or by field (e.g., with _cut_ ), then you can do it really fast from the UNIX command line, rather than reading it with R, SAS, Python, etc.

Much of the power of these utilities comes in piping between them (see Section 6) and using wildcards (see Section 4) to operate on groups of files. The utilities can also be used in shell scripts to do more complicated things.

---

[← 4 Wildcards in filenames](04-4-wildcards-in-filenames.md) · [Up: contents](index.md) · [6 Redirection →](06-6-redirection.md)

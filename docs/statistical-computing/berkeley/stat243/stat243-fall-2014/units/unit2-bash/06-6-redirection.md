---
title: 6 Redirection
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Redirection

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

UNIX programs that involve input and/or output often operate by reading input from a stream known as standard input ( _stdin_ ), and writing their results to a stream known as standard output ( _stdout_ ). In addition, a third stream known as standard error ( _stderr_ ) receives error messages, and other information that’s not part of the program’s results. In the usual interactive session, standard output and standard error default to your screen, and standard input defaults to your keyboard. You can change the place from which programs read and write through redirection. The shell provides this service, not the individual programs, so redirection will work for all programs. Table 3 shows some examples of redirection.

Operations where output from one command is used as input to another command (via the | operator) are known as pipes; they are made especially useful by the convention that many UNIX

5

commands will accept their input through the standard input stream when no file name is provided to them.

Here’s an example of finding out how many unique entries there are in the 2rd column of a data file whose fields are separated by commas:

- cut -d’,’ -f2 cpds.csv | sort | uniq | wc

- cut -d’,’ -f2 cpds.csv | sort | uniq > countries.txt

To see if there are any “S” values in certain fields (fixed width) of a set of files (note I did this on 22,000 files (5 Gb or so) in about 5 minutes on my desktop; it would have taken much more time to read the data into R):

> cut -b29,37,45,53,61,69,77,85,93,101,109,117,125,133,141,149, 157,165,173,181,189,197,205,213,221,229,237,245,253,261,269 USC*.dly | grep "S" | less

A closely related, but subtly different, capability is offered by the use of backticks (‘). When the shell encounters a command surrounded by backticks, it runs the command and replaces the backticked expression with the output from the command; this allows something similar to a pipe, but is appropriate when a command reads its arguments directly from the command line instead of through standard input. For example, suppose we are interested in searching for the text _pdf_ in the last 4 R code files (those with suffix _._ r or .R) that were modified in the current directory. We can find the names of the last 4 files ending in “.R” or “.r” which were modified using

> ls -t *.{R,r} | head -4

and we can search for the required pattern using _grep_ . Putting these together with the backtick operator we can solve the problem using

> grep pdf ‘ls -t *.{R,r} | head -4‘

Note that piping the output of the _ls_ command into _grep_ would not achieve the desired goal, since _grep_ reads its filenames from the command line, not standard input.

You can also redirect output as the arguments to another program using the _xargs_ utility. Here’s an example:

> ls -t *.{R,r} | head -4 | xargs grep pdf

And you can redirect output into a shell variable (see section 9) using backticks in a similar manner to that done above:

> files=‘ls -t *.{R,r} | head -4‘ # NOTE - don’t put any spaces around the ’=’

> echo $files

> grep pdf $files

6

---

[← 5 Basic UNIX utilities](05-5-basic-unix-utilities.md) · [Up: contents](index.md) · [7 Job Control →](07-7-job-control.md)

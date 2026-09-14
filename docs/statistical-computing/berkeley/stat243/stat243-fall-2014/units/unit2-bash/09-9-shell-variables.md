---
title: 9 Shell Variables
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 9 Shell Variables

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can define shell variables that will help us when writing shell scripts. Here’s an example of defining a variable:

> myDir="~/stat243-fall-2014/units"

The shell may not like it if you leave any spaces around the = sign. To see the value of a variable we need to precede it by _$_ :

- echo $myDir

- cd $myDir

You can also enclose the variable name in curly brackets, which comes in handy when we’re embedding a variable within a line of code to make sure the shell knows where the variable name ends:

- echo ${myDir}

- touch ${myDir}/tmp.txt

There are also special shell variables called environment variables that help to control the shell’s behavior. These are generally named in all caps. Type **env** to see them. You can create your own environment variable as follows:

9

> export myDir="~/stat243-fall-2014/units"

The _export_ command ensures that other shells created by the current shell (for example, to run a program) will inherit the variable. Without the export command, any shell variables that are set will only be modified within the current shell. More generally, if one wants a variable to always be accessible, one would include the definition of the variable with an _export_ command in your _.bashrc_ file.

Here’s an example of an environment variable that controls what your prompt looks like. We can modify it so that it puts the username, hostname, and pwd in your prompt. This is handy so you know what machine you’re on and where in the filesystem you are. [Note that on the VM, PS1 is already set in a very similar manner.]

> echo $PS1

> export PS1="\u@\h:\w> "

For me, this is one of the most important things to put in my _.bashrc_ file. The **\** syntax tells bash what to put in the prompt string: _u_ for username, _h_ for hostname, and _w_ for working directory.

Finally, a note about using single vs. double quotes in shell code. In general, variables inside double quotes will be evaluated, but variables not inside double quotes will not be:

name="chris" echo "My name is $name" echo 'My name is $name' echo "He said, \"My name is $name.\"" ## My name is chris ## My name is $name ## He said, "My name is chris."

So we’ll generally use double quotes. We can always work with a literal double quote by escaping it as seen above.

---

[← 8 Aliases](08-8-aliases.md) · [Up: contents](index.md) · [10 Functions →](10-10-functions.md)

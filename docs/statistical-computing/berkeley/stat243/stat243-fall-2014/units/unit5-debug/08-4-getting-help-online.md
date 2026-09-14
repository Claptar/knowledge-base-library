---
title: 4 Getting help online
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit5-debug.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Getting help online

**Source:** [`units/unit5-debug.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.1 Searching for help**

There are several mailing lists that have lots of useful postings. In general if you have an error, others have already posted about it.

- R help: R mailing lists archive

- Stack overflow (R stuff will be tagged with [R]: http://stackoverflow.com/questions/tagged/r)

- R help special interest groups (SIG) such as _r-sig-hpc_ (high performance computing), _r-sigmac_ (R on Macs), etc. Unfortunately these are not easily searchable, but can often be found by simple web searchs, potentially including the name of the SIG in the search.

7

- Simple web searches: You may want to include "in R", with the quotes in the search. To search a SIG you might include the name of the SIG in the search string

- Rseek.org for web searches restricted to sites that have information on R

If you are searching you often want to search for a specific error message. Remember to use double quotes around your error message so it is not broken into individual words by the search engine.

Just searching the R mailing list archive often gives you a hint of how to fix things. An example occurred when I was trying to figure out how fix a problem that was reporting a “ _invalid multibyte string_ ” error in some emails in a dataset of Spam emails. I knew it had something to do with the character encoding and R not interpreting the codes for non-ASCII characters correctly but I wasn’t sure how to fix it. So I searched for _“invalid multibyte string_ ”. Around the 8th hit or so there was a comment about using _iconv()_ to convert to the UTF-8 encoding, which solved the problem.

Note: of course the various mailing lists are also helpful for figuring out how to do things, not just for fixing bugs. For example, this blog post has a guide to R based simply on Stack Overflow posts.

### **4.2 Asking questions online**

If you’ve searched the archive and haven’t found an answer to your problem, you can often get help by posting to the _R-help_ mailing list or one of the other lists mentioned above. A few guidelines (generally relevant when posting to mailing lists beyond just the R lists):

1. Search the archives and look through relevant R books or manuals first.

2. Boil your problem down to the essence of the problem, giving an example, including the output and error message

3. Say what version of R, what operating system and what operating system version you’re using. Both _sessionInfo()_ and _Sys.info()_ can be helpful for getting this information.

4. Read the posting guide.

The mailing list is a way to get free advice from the experts, who include some of the world’s most knowledgeable R experts - seriously - members of the R core development team contribute frequently. The cost is that you should do your homework and that sometimes the responses you get may be blunt, along the lines of “read the manual”. I think it’s a pretty good tradeoff - where else do you get the foremost experts in a domain actually helping you?

8

---

[← [1] "<-" "{" "+" "print" "x"](07-1---print-x.md) · [Up: contents](index.md) · [5 Good coding practices →](09-5-good-coding-practices.md)

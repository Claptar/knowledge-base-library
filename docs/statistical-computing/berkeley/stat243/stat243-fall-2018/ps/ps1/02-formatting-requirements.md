---
title: Formatting requirements
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/ps/ps1.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/ps/ps1.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Formatting requirements

**Source:** [`ps/ps1.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/ps/ps1.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. As discussed in the (to-be-revised) syllabus, please turn in (1) a PDF through bCourses, as this makes it easier for us to handle grading AND (2) an electronic copy through Git following Omid’s instructions.

Your electronic solution should be in the form of an R markdown file named _ps1.Rmd_ or a L<sup>A</sup> TEX+knitr file named _ps1.Rtex_ , with bash code chunks included in the file.

2. For problems 3 and 4, your solution should start with a brief textual description of how you solved the problem, with the code following, including description of what your code does interspersed with the code. Do not just give us raw code.

3. All of your operations should be done using UNIX tools (i.e., you are not allowed to read the data into R or Python or other tools except as noted). Also, ALL of your work should be done using shell commands that you save in your solution file. So you can’t say “I downloaded the data from suchand-such website” or “I unzipped the file”; you need to give us the code that we could run to repeat what you did. This is partly for practice in writing shell code and partly to enforce the idea that your work should be replicable and documented.

You should not need to use _awk_ or _sed_ , but you may if you want to.

4. Formatting comments:

   - (a) If the downloading time interferes with generating the PDF, you can use eval=FALSE in one or more of your code chunks and then just cut and paste in example output, but ideally you can just cut down the amount of downloading and get all the chunks to run during the PDF generation.

1

- (b) If you have a lot of lines running off the end of the page you can use a “\”, e.g., grep a file.csv | grep b | \ grep c

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Problems →](03-problems.md)

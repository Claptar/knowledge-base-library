---
title: 3 How to format your scribe notes using LA TEX
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/other/scribingguide-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 How to format your scribe notes using LA TEX

**Source:** `other/scribingguide-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

There are many online resources for learning L<sup>A</sup> TEX. We recommend `http://en.wikibooks.org/wiki/LaTeX` as a starting point.

2

### **3.1 Layout of the book source directory**

The Dropbox directory contains two subdirectories. `templates/` contains macros which you do not need to modify. The `2015` directory contains one subdirectory per lecture, for example `Lecture01` ~~`I`~~ `ntroAndOverview` . Each contains the text, figures, and references for that chapter of the book. In this case, the text for the chapter is in `Lecture01` ~~`I`~~ `ntroAndOverview.tex` , the references are in `Lecture01 IntroAndOverview.bib` , and the figures are in the directory `images/` . `Lecture01 IntroAndOverview standalone.tex` and a `Makefile` are provided for testing purposes. Other files (if any) are auxiliary files generated during the compilation of the book.

### **3.2 Macros you should use**

We provide several pre-defined macros which you should use as appropriate.

- _\_ `mainword` This boldfaces the most important word in the paragraph. Please use this tag to mark the most important word in each paragraph. For example:

   - _\_ `mainword` _{_ `important word` _}_

produces:

#### **important** **~~w~~ ord**

- _\_ `todo` This macro denotes tasks for the scribe and/or other students. The format is as follows: _\_ todo[Who should do this task (optional)] _{_ Type of task (see below) _}{_ Your instructions about what needs to be done _}_ .

The second argument, “type of task”, should be one of the following:

1. **missing:** Information that is missing from the scribe notes.

2. **expand:** Add more information about a certain topic. Fill in an empty/ incomplete section of the notes.

3. **clarify:** Indicates that something in the scribe notes is confusing.

4. **reference:** Add a reference to the bibliography, citing the source of a piece of information.

5. **incorrect:** Point out erroneous/out-dated information in the scribe notes.

6. **editing:** Indicates a typo or a problem with formatting.

For example:

- _\_ `todo[MyName]` _{_ `Reference` _}{_ `What is the source of this information?` _}_ produces:

**TODO: Reference** _@MyName: What is the source of this information?_

And the more generic form:

_\_ `todo` _{_ `Reference` _}{_ `What is the source of this information?` _}_ produces:

**TODO: Reference** _@scribe: What is the source of this information?_

3

- _\_ `sidenote` This macro should be used to hold side-notes and digressions that were presented in lecture.

   - For example:

   - _\_ `sidenote` _{_ `This is an example of a sidenote` _}_

produces:

---

[← 2 Guidelines](02-2-guidelines.md) · [Up: contents](index.md) · [Did You Know? →](04-did-you-know.md)

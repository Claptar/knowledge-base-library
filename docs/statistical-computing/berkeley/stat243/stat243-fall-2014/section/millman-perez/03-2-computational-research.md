---
title: 2 Computational research
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/section/millman-perez.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/section/millman-perez.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Computational research

**Source:** [`section/millman-perez.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/section/millman-perez.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Consider a researcher using Matlab for prototyping a new analysis method, developing high-performance code in C, post-processing by twiddling controls in a graphical user interface, importing data back into Matlab for generating plots, polishing the resulting plots by hand in Adobe Illustrator, and finally pasting the plots into a publication manuscript or PowerPoint presentation. What if months later they realize there is a problem with the results? Will they will be able to remember what buttons they clicked to reproduce the workflow to generate updated plots, manuscript, and presentation? Can they validate that their programs and overall workflow is free of errors? Will other researchers or students be able to reproduce these steps to learn how a new method works or understand how the presented results were obtained?

The pressure to publish encourages us to charge forward chasing the goal of an accepted manuscript, but the term “reproducibility” implies repetition and thus a requirement to also move _back_ —to retrace one’s steps, question or change assumptions, and move for-

2

ward again. Unfortunately, the all-too-common way scientists conduct computational work makes this necessary part of the research process difficult at best, often impossible.

The open source software development community<sup>1</sup> has cultivated tools and practices that, if embraced and adapted by the scientific community, will greatly enhance our ability to achieve reproducible outcomes. Open source software development uses public forums for most discussion and systems for sharing code and data. There is a strong culture of public disclosure, tracking and fixing of bugs, and development often includes exhaustive validation tests that are executed automatically whenever changes are made to the software and whose output is publicly available on the Internet. This detects problems early, mitigates their recurrence, and ensures that the state and quality of the software is known under a wide variety of situations (operating systems, inputs, parameter ranges, etc). The same systems used for sharing code also track the authorship of contributions. All of this ensures an open collaboration that recognizes the work of individual developers and allows for a meritocracy to emerge.

As we learn from the open source process how to improve our scientific practice, we recognize that the ideal of scientific reproducibility is by necessity a reality of shades. We see a gradation from a pure mathematical result whose proof should be accessible to any person skilled in the necessary specialty to one-of-a-kind experiments such as the Large Hadron Collider or the Hubble Space Telescope, that cannot be reproduced in any realistic sense. However, it is always possible to improve our confidence in the results: whether we reexamine the same unique datasets with independently developed packages run by separate groups or we reacquire partial sampling of critical data multiple times.

Similarly, in computational research we also have certain areas where complete reproducibility is more challenging than others. Some projects require computations carried on the largest supercomputers, and these are expensive resources that cannot be arbitrarily allocated for repeated executions of the same problem. Others may require access to enormous datasets that cannot easily be transferred to the desktop of any researcher wishing to re-execute an analysis. But again, alternatives exist: it is possible to partially validate scaled versions of the largest problems against smaller runs created on the same supercomputing environments. Similarly, coarse resolution datasets can be used to conduct an analysis that may provide insights into the reliability of the full analysis. While not every quantity can be studied in this manner and there are deep research questions embedded in this problem, we should not consider this to be a paralyzing impediment to the quest for better computational reproducibility. Fortunately, the vast majority of research is conducted in smaller, simpler environments where full replication is feasible.

### **2.1 Computational research life cycle**

We advocate an integrated approach to computing where the entire life cycle of scientific research is considered, from the initial exploration of ideas and data to the presentation of final results. Schematically, this life cycle can be broken down into the following phases:

> _•_ **Individual exploration:** a single investigator tests an idea, algorithm, or question, likely with a small-scale test data set or simulation.

> 1We take it as a forgone conclusion (see [16]) that to share our research code with one another, we must use open source tools. Instead of discussing the need for using open source software, we focus on adopting development practices used by open source communities.

3

- **Collaboration:** if the initial exploration appears promising, more often than not some kind of collaborative effort ensues to bring together complementary expertise from colleagues.

- **Production-scale execution:** large data sets and complex simulations often require the use of clusters, supercomputers, or cloud resources in parallel.

- **Publication:** whether as a paper or an internal report for discussion with colleagues, results need to be presented to others in a coherent form.

- **Education:** ultimately, research results become part of the corpus of a discipline that is shared with students and colleagues, thus seeding the next iteration in the cycle of research.

Before presenting our approach, we examine the typical patchwork of tools and approaches that researchers use to navigate these phases and discuss how the standard approach makes the goal of reproducibility nearly unattainable.

For **individual work** , researchers use various interactive computing environments: Microsoft Excel, Matlab, Mathematica, Sage, and more specialized systems like R, SPSS, SAS, and STATA for statistics. These environments combine interactive, high-level programming languages with a rich set of numerical and visualization libraries. The impact of these environments cannot be overstated; researchers use them for rapid prototyping, interactive exploration and data analysis, as well as visualization. However, they have limitations: (a) some of them are proprietary and/or expensive (Excel, Matlab, Mathematica), (b) most (except for Sage) are focused on coding in a single, relatively slow, programming language and (c) most (except for Sage and Mathematica) do not have a document format that is rich, i.e., that can include text, equations, images, and video in addition to source code. While the use of proprietary tools is not a problem _per se_ and may be a good solution in industry, it is a barrier to scientific collaboration and to the construction of a common scientific heritage where anyone can validate the work of others and build upon it. Scientists cannot share work unless all colleagues can purchase the same package; students are forced to work with black boxes they are legally prevented from inspecting. Furthermore, because of their limitations in performance and handling large, complex code bases, these tools are mostly used for prototyping: researchers eventually have to switch tools for building production systems.

For **collaboration** , researchers tend to use a mix of email, version control systems and shared network folders (Dropbox, etc.). Version control systems (see _§_ 3.1) are critically important in making research collaborative and reproducible. They allow groups to work collaboratively on documents and track how they evolve over time. Ideally, all aspects of computational research would be hosted on publicly available version control repositories, such GitHub or Google Code. Unfortunately, the common approach is for researchers to email documents to each other with _ad hoc_ naming conventions that provide poor version control (and are the source of endless confusion and frequent mistakes). This form of collaboration makes it nearly impossible to track the development of a large project and establish reproducible and testable workflows. While a small group can make it work, this approach does not scale beyond a few collaborators, as painfully experienced by anyone who has participated in the madness of a flurry of email attachments with oddly-named files such as `paper-final-v2-REALLY-FINAL-john-OCT9.doc` .

For **production-scale execution** , researchers typically turn away from the convenience of interactive computing environments to compiled code (C, C++, Fortran) and libraries

4

for distributed and parallel processing (MPI, Hadoop), These tools are specialized enough that their mastery requires a substantial investment of time. We emphasize, that before production-scale computations begin, the researchers already have a working prototype in an interactive computing environment. Therefore, turning to new parallel tools means starting over and maintaining at least two versions of the code moving forward. Furthermore, data produced by the compiled version is often imported back into the interactive environment for visualization and analysis. The resulting back-and-forth workflow is nearly impossible to capture and put into version control systems, making the computational research difficult to reproduce. Obviously the alternative, taken by many, is simply to run the slow serial code for as long as it takes. This is hardly a solution to the reproducibility problem, as runtimes in the weeks or months become in practice single-shot efforts that no one will replicate.

For **publications** and **education** , researchers use tools such as L<sup>A</sup> TEX, Google Docs, or Microsoft Word and PowerPoint. The most important attribute of these tools in this context is that, L<sup>A</sup> TEX excepted, they integrate poorly with version control systems and are ill-suited for workflow automation. Digital artifacts (code, data, and visualizations) are often manually pasted into these documents, which easily leads to a divergence between the computational outcomes and the publication. The lack of automated integration requires manual updating, something that is error-prone and easy to forget.

From this perspective, we now draw a few lessons:

1. The common approaches and tools used today introduce discontinuities between the different stages of the scientific workflow. Forcing researchers to switch tools at each stage, which in turn makes it difficult to move fluidly back and forth.

2. A key element of the problem is the gap that exists between what we view as “final outcomes” of the scientific effort (papers and presentations that contain artifacts such as figures, tables, and other outcomes of the computation) and the pipeline that feeds these outcomes. Because most workflows involve a manual transfer of information (often with unrecorded changes along the way), the chances that these final outcomes match what the computational pipeline actually produces at any given time are low.

3. The problems listed above are _both_ technical and social. While we largely focus on the tools aspect in this chapter, it is critical to understand that at the end of the day, only when researchers make a conscious decision to adopt better work habits will we see substantial improvements on this problem. Higher quality tools will make it easier and more appealing to adopt such changes; but other factors—from the inertia of ingrained habits to the pressure applied by the incentive models of modern research— are also at play.

Asking about reproducibility by the time a manuscript is ready for submission to a journal is too late: this problem must be tackled from the start, not as an afterthought tacked-on at publication time. We must therefore look for approaches that allow researchers to fluidly move back and forth between the above stages and that integrate naturally into their everyday practices of research, collaboration, and publishing, so that we can simultaneously address the technical and social aspects of this issue.

5

### **2.2 Open source ecosystem**

With the above in mind, our approach focuses on the need for tools and practices that enable researchers to naturally consider the entire cycle of research as a continuum, and where “doing the right thing” is the easy and natural path rather than an awkward and cumbersome one. Rather than the haphazard patchwork of tools and processes described above, we promote the development and adoption of a robust, open source ecosystem that makes reproducible research a central aim.

To illustrate our point, we briefly describe the scientific Python ecosystem [25, 22, 29] and introduce a few core projects, which serve as examples throughout the chapter. While strong proponents of the Python programming language, we understand Python is not the only choice for scientific computing or reproducible research. Rather we consider the scientific Python ecosystem as a case study for the type of community-developed software stack that we believe necessary for improving the reliability and reproducibility of our computational results.

The Python language has a simple, expressive, and accessible syntax that emphasizes code readability (see _§_ 3.4). Rather than imposing a single programming paradigm, it allows one to code at many levels of sophistication, including the procedural programming style familiar to many scientists. Python is available in an easily installable form for almost every platform; and is, therefore, ideal for a heterogeneous computing environment. It is also powerful enough to manage the complexity of large applications, supporting functional programming, object-oriented programming, generic programming, and metaprogramming. Due to excellent support for scripting tools written in other languages (including C, C++, Fortran, and R), Python is often used as an _integration language_ for calling routines from a wide array of high-quality scientific libraries. Finally, it has an extensive standard library that provides built-in functionality for many tasks including database access, Internet protocols, data compression, and operating system services.

Importantly, from our perspective, Python is not specifically designed for scientific computing. As a result, it is extremely capable at a diverse set of general purpose tasks. This benefits the scientific community, by providing an assortment of useful features while we focus on extending them with the specific functionality necessary for our research. While there are numerous libraries and extensions for scientific computing in Python, the three most widely used are NumPy,<sup>2</sup> SciPy,<sup>3</sup> and matplotlib.<sup>4</sup> NumPy [34] provides a high-level multidimensional array object and basic operations to manipulate them. SciPy is a collection of common numerical operations used in scientific computing. Matplotlib [14, 15] is the standard graphics library in Python with support for publication-quality 2- and 3-D plots. In addition to these tools, there are more specialized packages to provide advanced support and algorithms for machine learning, image processing, graph theory, symbolic mathematics, etc. On top of these general scientific libraries, there are more domain specific projects developed by those scientific communities. For instance, we are both members of the Neuroimaging in Python [23] community in addition to participating in the more general parts of the scientific Python software stack. The ability to participate and contribute at multiple levels of the tool chain is possible because of the adoption of common tools, standards, and procedures—many of which we discuss in this chapter.

> 2 `http://numpy.org`

> 3 `http://scipy.org`

> 4 `http://matplotlib.org`

6

In addition to this stack of scientific software packages, we briefly introduce IPython,<sup>5</sup> a system for interactive and parallel computing that has become the _de facto_ standard environment for scientific computing and data analysis in the Python community. It was created by one of us (FP) in 2001 as an interactive command-line shell for Python, and has evolved into a large collaborative open-source project with contributions from a broad team of scientists [28]. We call special attention to it as the natural focus of our integrated approach to the computational life cycle. As such, it will serve as a primary example throughout the chapter and will be discussed in detail in _§_ 5.3.

### **2.3 Communities of practice**

While the case can be made for the use of open source software in science, even more important is the benefit that comes with open source community-driven development practices. In community-developed projects, the distinction between users and developers is more fluid than in proprietary software projects where this distinction is not only expected, but often rigorously enforced by legal mechanisms. This does not mean that everyone must become a _core developer_ . There are still differing levels of contribution, which includes reporting issues, suggesting functionality, contributing enhancements, discussing use cases, answering questions, and much more.

Communities of practice must drive the development of our scientific software [32]. A participatory community of active researchers using and contributing to the development of the code we depend on for our scientific output is necessary for robust software ecosystems where we can share and verify our work. As this work becomes more reliant on computational tools and techniques the questions we can ask will be constrained by what our software can do and how easy it is to extend. Hence moving a field forward will increasingly require scientists to be computationally literate, part of which includes embracing the tools and practices widely adopted by the open source community.

There are real concerns that arise when attempting to transplant the practices of open source development directly to computational research. The open source development model is one where, in practice, the copyright and authorship of any large collaborative project is spread among many authors, possibly thousands. While the source control tools in use allow for a precise provenance analysis to be performed, this is rarely done and its success is contingent on the community having followed certain steps rigorously to ensure that attribution was correctly recorded during development.

This is not a major issue in open source, as the rewards mechanisms tend to be more informal and based on the overall recognition of any one contributor in the community. Sometimes people contribute to open source projects as part of their official work responsibilities, and in that case a company can enact whatever policies it deems necessary; often contributions are made by volunteers for whom acknowledgment in the project’s credits is sufficient recognition.

In the academic world, the authorship of scholarly articles in scientific journals and conference proceedings is currently the main driver of professional advancement and reward. In this system, the order of authorship matters enormously (with the many unpleasant consequences familiar to all of us), and so does the total number of authors in a publication. While in certain communities papers with thousands of authors do exist (experimental highenergy physics being the classic example), most scientists need the prominent visibility they

> 5 `http://ipython.org`

7

can achieve in a short author list. The dilution of authorship resulting from a largely open collaborative development model is an important issue that must be addressed.

Furthermore, the notion of a fully open development model typical of open source projects is at odds with another aspect of the scientific publication and reward system: the “first to publish” race. Many scientists are, understandably, leery of exposing their projects on an openly accessible website when in their embryonic stages. The fear of being scooped by others is real, and again we must properly address it as we consider how to apply the lessons of open source development to the scientific context.

---

[← 1 Introduction](02-1-introduction.md) · [Up: contents](index.md) · [3 Routine practice →](04-3-routine-practice.md)

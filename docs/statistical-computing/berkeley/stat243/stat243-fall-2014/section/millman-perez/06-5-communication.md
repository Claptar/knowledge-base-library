---
title: 5 Communication
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/section/millman-perez.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/section/millman-perez.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Communication

**Source:** [`section/millman-perez.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/section/millman-perez.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Instead of imagining that our main task is to instruct a _computer_ what to do, let us concentrate rather on explaining to _human beings_ what we want a computer to do.

_Literate programming (1984)_ DONALD KNUTH

Whether engaging colleagues in data analysis, educating students about numerical algorithms, or publishing computational results, scientists need to ultimately convey their computational work to others—not just the artifacts of that work, but the specific details of how those artifacts arose. We begin with a brief description of some existing tools for literate programming as a backdrop to present a more recent approach we refer to as literate computing. Again, our view is shaped by the desire to tackle the life cycle of computational research described in _§_ 2.1 in an integrated way. From this perspective, we argue that the literate computing approach is a better fit to the needs of reproducibility in computational research than traditional literate programming tools, and will present the IPython notebook as an example implementation.

### **5.1 Literate programming**

Donald Knuth proposed _literate programming_ in the early 1980s and a complete description of this approach to computer programming can be found in his later book of the same title

> 33 `http://readthedocs.org`

> 34 `http://norvig.com/21-days.html` is recommend reading

19

[19]. Knuth’s concern was the development of a better approach to documenting computer software; he devised a process whereby programmers would write literate source files that describe in full prose the ideas underlying a given program, interspersed with the code fragments implementing the actual computations. Knuth developed tools that can process these input files to produce two different representations via processes he denoted as _tangling_ and _weaving_ : a _tangled_ code file meant for compilation and execution by a computer, and a _woven_ file containing the formatted documentation. Knuth’s original implementation, the WEB system [18], was focused on producing Pascal code and L<sup>A</sup> TEX documentation, but this basic idea has been extended to many other programming languages and documentation systems.

The R community has embraced the ideas behind literate programming, and a mature implementation of the concept exists for R in the Sweave system [20]. Sweave is one of the central elements of the Bioconductor system [10, 8] for computational biology and bioinformatics. All Bioconductor packages must be accompanied by at least one _vignette_ , a literate program that contains executable code illustrating the tasks the package is meant to perform. Vignettes can be read in PDF format, but functions exist to automatically extract all the R code for immediate execution. The journal Biostatistics encourages authors to use literate programming tools such as L<sup>A</sup> TEX and Sweave when submitting articles they wish to be designated reproducible [27].

A new entrant to the R community that is gaining rapid adoption is the knitr package.<sup>35</sup> Knitr can be seen as a highly evolved Sweave with a number of improvements, but still within the conceptual lineage of literate programming tools. The use of literate programming tools are gaining increasing traction in statistical education as well. For instance, at UC Berkeley, students taking computational classes in both the Statistics Department and the Division of Biostatistics are encouraged to use L<sup>A</sup> TEX with Sweave or L<sup>A</sup> TEX (or R Markdown) with knitr.

As the above examples suggest, literate programming has been most commonly adopted when the desired final document is intend primarily for human consumption. Few, if any, large software libraries are written this way. In fact, the most prevalent use of literate programming has been among scientists to communicate computational ideas and results to one another. These ideas have also influenced open source software projects where tools have been developed to automatically generate project documentation based on source files and to create _live documentation_ containing the output from embedded code run during document generation (see _§_ 3.5).

### **5.2 Literate computing**

Tools described in the previous section for literate programming are mature and have been used to great effect to improve the quality of documentation in scientific programs and data analysis, especially in the R community. But they remain rooted in the original model proposed by Knuth, of authoring a literate file that is then post-processed by various tools to produce either documentation or executable code.

In this section, we present an alternate approach to improving the connection between code and documentation that we refer to as _literate computing_ . Our choice of terminology emphasizes the act of computing itself rather than the writing of code, as the systems we describe are all centered around _interactive environments_ where the user can enter code for immediate execution, obtain results, and continue with more commands that produce new

> 35 `http://yihui.name/knitr`

20


Figure 1: The web-based IPython Notebook combines explanatory text, mathematics, multimedia, code and the results from executing the code.

results based on the previous ones. A literate computing environment is one that allows users not only to execute commands but also to store in a literate document format the results of these commands along with figures and free-form text that can include formatted mathematical expressions. In practice it can be seen as a blend of a command-line environment such as the Unix shell with a word processor, since the resulting documents can be read like text, but contain blocks of code that were executed by the underlying computational system.

The earliest full-fledged implementation of these ideas is the graphical user interface of the Mathematica _Notebook_ system, which dates back to early versions of Mathematica on the NeXT computer platform and took advantage of the superior graphical capabilities of NeXT. Today a number of other systems (both open source and proprietary) provide similar capabilities; on the open-source front we notably mention the Maxima<sup>36</sup> symbolic computing package, the Sage<sup>37</sup> mathematical computing system, and the interactive computing project IPython, on which we will focus the rest of our discussion.

### **5.3 IPython notebook**

In 2011, a web-based notebook was developed in IPython that connects to the same interactive core as the original command-line shell, but does so using a web browser as the user interface, automatically enabling either local or remote use as the system running the web browser can be different from that executing the code, with all communication happening over the network. Fig. 1 shows a typical notebook session with code, text, mathematics, and figures.

The driving idea behind the IPython Notebook is to enable researchers to move fluidly between all the phases of the research life cycle described in _§_ 2.1. If the environment

> 36 `http://maxima.sourceforge.net`

> 37 `http://www.sagemath.org`

21

where we conduct our exploratory research can also support all subsequent stages of this cycle, and does so while smoothly integrating with the version control and process practices we’ve previously espoused, the likelihood that a final published result will be reproducible increases significantly. The Notebook system is designed around two central ideas: (a) an openly specified protocol to control an interactive computational engine, and (b) an equally open format to record these interactions between the user and the computational engine, including the results produced by the computations.

Before diving into the specifics of these two ideas, we note that the above design is independent of the Python language: while IPython started its life as a Python-specific project, the vision of the Notebook system is language-agnostic. First, while working in IPython, users can mark entire code blocks for execution via a separate language by using a special syntax on the block’s first line: a user can for example start a block `%%R` , `%%octave` , `%%bash` or `%%ruby` and IPython will execute the entire block with the respective system. The development community is also busy implementing similar support for new and experimental scientific languages such as Julia, enabling a user to control from a single IPython notebook a workflow that combines the most commonly used high-level languages in modern scientific computing. Second, an _entire notebook_ can be executed in a different language if a remote engine (referred to as a _kernel_ ) exists that implements the interaction protocol. As of this writing, prototype kernels are being developed for Ruby, JavaScript, R, and Julia.

The IPython architecture provides a way to capture, version control, re-execute, and convert into other output formats, any computational session. Notebooks can be shared with colleagues in their native form for re-execution or converted into HTML, L<sup>A</sup> TEX, or PDF formats for reading and dissemination. They can be used in slideshow mode to give presentations that remain connected to a live computation and can be exported into plain scripts for traditional execution outside of the IPython framework.

The IPython protocol consists of messages in JSON (JavaScript Object Notation) format that encode all actions that an interactive user can request of a computational kernel, such as executing code, transferring data, or sending results, among many others. While this protocol is implemented in IPython, it can be independently implemented to provide new kernels also able to interact with the notebook interface and clients. The notebook file format is a simple JSON data structure that contains a list of cells. A cell can contain either text or code, and code cells can also have the output corresponding to the execution. All sub-structures in the notebook format (the entire notebook as well as the individual cells) have attached flexible metadata containers; this metadata can be used by post-processing tools. The file format stores the communication protocol’s payloads unmodified, so it can be thought of as a structured and filtered log (since the user chooses what to keep while working interactively) of the computation.

The IPython project has taken elements pioneered by the Mathematica and Sage notebooks and created a generic protocol and file format to control and record literate computing sessions in any programming language. This was a deliberate choice in contrast to the literate programming approach: by providing a tool that operates close to the live workflow of research computing (in contrast to the batch-processing mode encouraged by classic literate programming tools), the resulting documents are immediately reproducible sessions that can be published in their own right or as companion materials to a traditional manuscript. Given how IPython also includes support for parallel computing, which we don’t discuss here in the interest of conciseness, the system provides an end-to-end environment for the creation of reproducible research.

The real-world possibilities this offers were demonstrated during a collaboration in 2012

22

between the IPython team, a microbiology team led by Rob Knight from the University of Colorado and Greg Caporaso from the University of Northern Arizona, and Justin Riley from MIT who created the StarCluster<sup>38</sup> system for deployment and control of parallel resources on Amazon’s EC2 cloud platform. As part of an NIH-funded workshop to explore the future of genomics data analysis in the cloud, this combined team collaborated on creating a fully parallelized analysis comparing the predictive behavior of different sizes and locations of gene sequence reads when reconstructing phylogenetic trees. The microbiologists had developed a serial prototype of this idea using their Qiime libraries [6], but a large-scale analysis with a full dataset would require roughly a month of CPU time on a single workstation. By locating the IPython Notebook server on Amazon cloud instances, the entire team was able to log into a single instance and by editing the code directly in the cloud, in a single day turn this prototype into a set of production notebooks that would execute the analysis in parallel using multiple Amazon servers. Once the parallel code was tested, it became evident that there was not only an interesting example of using cloud technologies for rapid development of research ideas but also a biologically relevant finding; within a week the team had completed a more extensive run using 24 hours of execution on 32 nodes and submitted a manuscript for publication [31]. This paper is now accompanied by all of the IPython notebooks that enable any reader to fully reproduce our analysis, change parameters and question our assumptions, without having to re-implement anything or be hampered by lack of access to the code and data. We have made available not only the final notebooks, but also the Amazon Virtual Machine Images (data files that represent a virtual computer on Amazon’s cloud platform), so that the entire analysis can literally be re-executed under identical conditions by anyone with an Amazon account.

This example, anecdotal as it may be, indicates the validity of the vision we propose here: that by providing tools that encompass the entire cycle of research, from exploration to largescale parallel production and publication, we can provide the scientific community with results that are immediately accessible to others and reproducible, seeding the continued evolution of the research process.

The IPython project has also developed tools to make it easy to share and disseminate content created as notebooks in a variety of forms. The Notebook Viewer<sup>39</sup> is an online service that renders _any_ publicly available IPython notebook as a web page. This enables users to share notebooks by simply putting them online and pointing colleagues to the rendered webpage. The same technology that powers the notebook viewer service can also generate HTML files suitable for inclusion in other websites, in particular, blogs. Since a lot of rapid technical communication is happening today on the Internet via blogs, this is an important aspect of linking reproducible research to the rapid feedback cycle of web-based discussion. With a single command, a user can convert a notebook file into HTML ready for posting to a blog, and this is already being used by scientists to write both short technical posts and also more complex materials: Jose Unpingco, a researcher with the US Department of Defense, is currently working on a book titled _Python for Signal Processing_ , and this book is available during writing as a GitHub repository.<sup>40</sup> This repository contains a series of IPython notebooks so that readers can directly execute the code in the book, and they are also being published as a series of blog posts as they become available,<sup>41</sup> so readers can comment and discuss with the author throughout the process of book development, and they can do so

> 38 `http://star.mit.edu/cluster`

> 39 `http://nbviewer.org`

> 40 `http://github.com/unpingco/Python-for-Signal-Processing`

> 41 `http://python-for-signal-processing.blogspot.com`

23

based directly on the actual code that creates all the examples in the book.

The signal processing book is, to our knowledge, the first example of a full book being written as a collection of executable IPython notebooks, but this follows a tradition created by Mathematica, whose documentation is itself a collection of executable Notebooks. Furthermore, in recent years Rob Beezer, from the University of Puget Sound, has developed a popular Introductory Linear Algebra book [2] that is based on the Sage system and also combines the mathematics and text with code that can be directly executed and modified by the readers. This ability to “close the loop” between what the authors had on their screens and what their readers can execute themselves is an important element of the movement towards reproducibility in research.

As a concrete implementation of the ideas of reproducible research using the tools we’ve described in this chapter, during the ongoing process of research itself, we can point to work being carried by a collaboration where one of us (FP) is a member, on novel ways to model the mathematical structure of the signal generated by MRI devices in the imaging of water diffusion in the brain. This work, as yet unpublished, is being developed as an open repository on GitHub<sup>42</sup> where all code for our research is posted during writing, all computational experiments are created as IPython notebooks, and submitted manuscripts are created directly from the code and notebooks (along with additional narrative written by hand).

The above tools are also playing a central role in the last stage of the computational research life cycle, education. We will increase our chance that the next generation of scientists adopts improved reproducibility practices if we educate them with the same tools that we use for everyday research, and a couple of modern efforts that aim to bring improved computational literacy to scientific research have adopted the IPython notebook. Software Carpentry<sup>43</sup> is a project funded by the Alfred P. Sloan Foundation and led by Greg Wilson at the Mozilla Foundation whose motto is Richard Feynman’s famous “What I cannot create, I do not understand.” They produce, with rigorous follow-up and assessment, workshops aimed at working scientists (typically graduate students and postdoctoral researchers, but always open to broad audiences) and whose purpose is to instill in them a collection of skills and best practices for effectively using computing as a daily research tool. The Software Carpentry workshops cover topics ranging from the basics of the Unix shell to version control, Makefile automation of processes and basics of scientific Python including data analysis and visualization. They have recently adopted the IPython Notebook as the base system for teaching the scientific Python parts of their curricula, and provide the IPython team with direct feedback on its strengths and weaknesses as an educational tool. In a similar vein, Josh Bloom from the astronomy department at UC Berkeley has led, for a number of years, 3-day workshops on the use of Python as a tool for scientific computing.<sup>44</sup> These are open to the entire campus community and followed by an optional for-credit seminar where students learn more advanced skills for using Python as a research tool. F. P´erez and other members of the IPython team at UC Berkeley regularly lecture in the bootcamps and courses, where the notebook is the means for delivery of course materials and interactive lecturing. While we have identified a number of weaknesses and areas for improvement, we have also found this environment to be markedly superior to all previous tools we had used in the past for teaching in similar contexts.

> 42 `http://github.com/fperez/spheredwi`

> 43 `http://software-carpentry.org`

> 44 `http://pythonbootcamp.info`

24

As these capabilities in IPython reach wider usage, with scientists now developing complete books and lecture series based on the system, we are considering a number of new challenges and questions introduced by these capabilities. The interactive computing model is a fluid and natural one, but we need to find ways to extend it into the development of longer-term production codes that are robust, documented, tested and integrated into reusable libraries. This means bridging the gap between a _scripting_ mentality and a _developer_ one, and while we have already made progress on that front in IPython, many questions remain open for the future.

---

[← 4 Collaboration](05-4-collaboration.md) · [Up: contents](index.md) · [6 Conclusion →](07-6-conclusion.md)

---
title: 3 Routine practice
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/section/millman-perez.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/section/millman-perez.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Routine practice

**Source:** [`section/millman-perez.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/section/millman-perez.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The practices recommended in this section are distilled from writing and maintaining software, teaching programming courses to students and scientists, as well as extensive interaction and discussion with a diverse group of scientists and engineers. Whole books have been dedicated to best practices in software development with highly specialized tools and habits for individual programming languages and methodologies. In this short section, we highlight the practices and tools essential to any computational work. For a more detailed discussion, we recommend [17, 13, 1].

We begin by discussing practices and tools that should be applied to even exploratory, individual research. These practices are so essential to efficient and productive use of computational resources that we routinely use them whenever we use a computer. In _§_ 4, we discuss how these practices and tools extend to collaborative work.

### **3.1 Version control**

When collecting data, running analyses, or writing papers, you inevitably need to keep track of the various versions of your work: data is augmented and curated; code is adapted and improved; and writing is revised and expanded. While only keeping the most recent version of your work is possible, this is seldom sufficient. There are tentative new directions, detours, and dead ends.

We have witnessed numerous researchers attempting to manage different versions of their work using manual and laborious kludges. The most common patterns include using _ad hoc_ naming schemes (e.g., `file.txt.bak` , `file.txt.1st` , etc.), emailing different versions to yourself, or using application specific functionality such as Microsoft Word’s “Track Changes” feature. While these approaches are partial solutions to the problem, they are also cumbersome, prone to failure, or limited to specific applications. More importantly, they are unsustainable beyond simple scenarios with only one or two files and do not scale to any kind of sensible collaboration workflow.

Because tracking and managing how work evolves over time is so fundamental to the workflow of software development, programmers have created specialized software tools to do exactly this. These tools are called _version control_ systems. Several open source version control systems (VCS) have been developed over the years, the most well known being CVS, SVN, Git, and Mercurial.

While there are notable differences among these tools, they all share some basic concepts. All project files (code, text, figures, etc.) are stored in a _repository_ (often represented on disk in a directory hierarchy). There are commands to add files to and remove files from a repository. To track changes to a file, it must be _committed_ to the repository, ideally with

8

a meaningful _commit message_ . The repository and commit mechanism provide a complete historical log of the project from inception to current state, including every change made along with timestamps, author, comments, and other metadata for each modification.

Code changes may follow a linear progression of commits. However it is more common for projects to include alternate development paths.<sup>6</sup> Given the exploratory nature of research, several approaches to a problem are often pursued simultaneously. In such cases, commits will resemble a tree with several _branches_ diverging from a common base or trunk. When exploring these alternative approaches on different branches, several branches may eventually converge and need to be _merged_ back together. If the changes in each of these branches do not overlap with one another, the VCS can merge them together in a completely automated fashion. When there are _conflicting_ changes in different branches (e.g., edits to the same line of code), then manual intervention is required. But in all cases, a VCS is the only reasonable solution for managing the evolution of multiple branches of parallel development in a set of files (whether written documents, computer code, or data).

In the design of more modern VCS such as Git,<sup>7</sup> an important consideration is woven into the core of the system: built-in _data integrity verification_ via cryptographically robust fingerprinting of all content. The basic idea is that at every commit, the VCS computes a “fingerprint” of the content being committed as well as the data it depended on.<sup>8</sup> This makes it possible to establish the integrity of the entire history of a repository at any point, by computing these fingerprints and comparing them against the stored one. By the nature of hash functions, even small changes will result in new hashes. This key design idea is used by Git for all kinds of internal operations; but it also means that when a scientist gets a copy of a repository, he or she can be confident the content (including every recorded change) has not been tampered with in any way.

Strong guarantees on data integrity are a necessary condition of any reproducible workflow, and one of the reasons why we emphasize so much the pervasive use of modern version control systems as the foundation of a reproducible research environment.

It is important to note that VCS were developed for the management of human-generated content such as computer source code or text documents, not for the handling of large binary data that is common in science. By virtue of their design, they tend to be somewhat inefficient if you attempt to store all the changes in a project with many frequently changing large binary files, which somewhat limits their use for the tracking of all assets in a research project. But new efforts exist to mitigate these limitations, such as the git-annex<sup>9</sup> project, which uses Git for storing all metadata about large binary assets, along with a static (configurable) storage resource external to Git for the assets themselves. This approach makes it possible to smoothly integrate the management of binary data within a VCS workflow, without creating an explosion in the size of the VCS storage area.

The use of version control should become second nature; we routinely use it for everything— including the writing of this document.<sup>10</sup> We suggest researchers adopt a practice of pervasive version control: research codes, teaching materials, manuscripts, and data analysis

> 6This tendency becomes more pronounced in collaborative projects (see _§_ 4).

> 7From this point on, we will mainly focus on Git, which is our preferred VCS. It is also the one that is most widely used in the scientific Python community.

> 8More precisely, a hash function is evaluated on the content of the commit and the hash of all commits it depends on, which creates a directed acyclic graph of hash values that signs the entire repository. Today these systems employ the SHA1 hash function, but other hashes could be equally used if necessary.

> 9 `http://git-annex.branchable.com`

> 10 `http://github.com/fperez/repro-chapter-oss`

9

projects should be developed, from the beginning, _always_ using version control systems that track the actual history of everyone’s contributions.

### **3.2 Execution automation**

Just as it is impossible to reproduce old results if you don’t have access to the code and data that created them (hence the need for version control), it is equally impossible if you did not record somewhere how the code and data were used. You could write everything down and manually follow these instructions again later on, but a more sensible approach is to record them in a machine-readable way so that the computer can execute them. Furthermore, since most computational processes are a chain of executions where each step depends on the previous or on inputs that may have been modified, ideally you should be able to understand the structure of these dependencies and only run things when necessary.

Since building complex software with many source files is repetitive, full of detail, and time-consuming, this is another task for which the software development world has developed powerful, automated solutions. The venerable `make` system is the workhorse of process automation [30]. It has a declarative syntax for expressing dependencies between sources and targets and a simple (timestamp-based) mechanism for resolving when dependencies need to be rebuilt. To get an idea how this works consider the situation where a plot is created by a script, which reads a data file. In the parlance of `make` , the output `plot` is a _target_ that depends on two _sources_ —the data file and the script. If you type `make plot` , for example, `make` checks whether the script or data has been modified after the current plot was generated; if so, it calls the script on the data to generate an updated plot. In this simple scenario, using `make` does not offer much more than just running the script by hand. However, if the data this script consumes is generated by a chain of other scripts and data files, then the benefit of `make` becomes apparent.

More modern systems also exist, and a detailed review of the options is beyond our scope. But whether running a sequence of scripts to produce some figures, compiling your software, or creating the final PDFs for a grant proposal, you should be able to do so by typing `make results` or the equivalent syntax in your system of choice. Once things are automated in this way, it becomes possible for others (humans or machines, and even yourself on a new system or months later) to reliably repeat the process.

### **3.3 Testing**

Computing is error-prone. While there is no foolproof way to rid computing of error, there are ways to limit and reduce it. One of the most successful and widely used techniques involves comprehensive testing, so that bugs (i.e., errors) are found quickly. Finding bugs as soon as possible in the development process is extremely valuable. Depending on the nature of the bug, it may reveal a fundamental problem with the overall design of your code requiring months more of coding. Even small errors that are easily fixed may require rerunning months of analysis. To reduce the amount of time it takes to uncover bugs and to ease the pain of debugging your code, it is essential to adopt a rigorous testing practice up front.<sup>11</sup>

Testing should be performed on multiple levels and begun as early as possible in the development process. For programs that accept input either from a user or file, it is important

> 11While testing is an extremely useful practice, we should also point out that it is often more interesting work than debugging.

10

that the code validates the input is what it expects to receive. Tests that ensure individual code elements (e.g., functions, classes, and class methods) behave correctly are called _unit tests_ . Writing unit tests early in the process of implementing new functionality helps you think about what you want a piece of code to do, rather than just how it does it. This practice improves code quality by focusing your attention on use cases rather than getting lost in implementation details. By thinking about the test at the outset, you can avoid finding that the code you just wrote is a huge, untestable mess. It also improves documentation because an example (i.e., the test case) is often better than an explanation. And if you regularly run the test, you will quickly know when your code no longer works for the example (something you may never notice in the case of explanatory text). Finally, unit testing leads to more robust code as you will more quickly isolate bugs, which makes them easier to fix [26].

Testing is mainly a language-specific pursuit (as it must be implemented in the programming language of a given project to be most effective). The authors are most familiar with the Python-based world, and [4] is a good hands-on starting point for the tool most widely used in scientific Python projects, namely the nose<sup>12</sup> testing framework.

### **3.4 Readability**

While writing code that is well tested and systematically managed by a modern VCS is important, code that is not easy to read will be difficult to understand, correct, and modify. Readable code is written with explanatory names, clear logical structure, and comprehensive documentation where necessary. There is an extensive and growing literature on stylistic aspects of good programming [3, 9, 17, 13, 21]. Because scientific papers and grant submissions have become the currency of the scientific realm, many scientists have read classics such as Strunk & White’s _Elements of Style_ . Yet, even as an increasing amount of our work is produced in lines of code, there is a paucity of scientists paying the same attention to the elements of good programming style. The emphasis on readability is included in this section because even when you are the only one using or working on your code, the chance that you will need to read your own code is high. Even when your code is widely used and shared, you will still often be the one most frequently reading it.

Self-documenting code, as the name implies, reduces the need for external documentation by placing an emphasis on clear, well-written code that is easy to read and understand. In mathematics, it is accepted practice to follow established naming conventions (e.g., capital letters for sets and lower case letter for set elements). It is equally expected that when making a mathematical argument, one should not arbitrarily switch notation mid-argument. Similarly, using consistent and uniform naming conventions when programming should be standard practice. Brevity in naming should be balanced against explicit and descriptive words. For example, you might use the term `download` rather than `get` in a function call to download a specific dataset from the Internet. Expressions are the next block to readability. While mathematical manipulation (e.g., De Morgan’s laws) can be used to great effect in making your expressions more easily understood, it is often important to use the right level of abstraction. Higher-level programming languages (e.g., Python and R) provide data structures (such as _n_ -dimensional vectors or statistical formulas) that enable the code to be more readily understood at the level of the mathematical ideas they implement. Finally, the overall control flow of your code must be clear and easy to follow. Finding the best control

> 12 `http://nose.readthedocs.org`

11

flow requires a deep understanding of your problem and an in-depth knowledge of programming methodology and the specifics of the language you are using. Like good writing, good coding is achieved through deliberate practice.

Inspired by the idea of self-documenting code, some argue that good code does not need comments. Indeed, liberally commenting your program to compensate for poorly written, obscure code is counterproductive. Comments that merely explain how a piece of code works add limited benefit. If code is so obscure to need explanation, it is better to revise or rewrite it. Another limitation of comments (as with many types of documentation) is that it is often uncoupled from the actual code. This means that there is no way to ensure that the two do not diverge. And, if they diverge, it may not be obvious which is correct.

To illustrate how comments and documentation _can_ enhance readability of your code, we discuss the commenting and documentation system that has been developed by NumPy and is used by other scientific Python projects. While this section is specific to the tools and processes put in place in the scientific Python community, the general ideas are more broadly applicable.

In 2007, NumPy lacked good reference information for the various functions, classes, and modules it provided. Users and developers had access to the source code, a nearly 400 page “Guide to NumPy”, and an active mailing list. Yet, it was clear that this level of documentation was not enough. To address this, the community began a yearlong effort to develop a _documentation string standard_ .<sup>13</sup> In Python, a documentation string (or docstring) is any string in the first line in an object’s (e.g., function, class, etc.) definition. Since docstrings are embedded in the source code, they are readily available to anyone directly viewing the source. When the code is executed this string is associated with the object and can be programmatically accessed and used by introspection tools such as IPython. Docstrings can also be accessed for autogenerating documentation. Similar functionality exists in other programming languages such as R. Even in languages that don’t include this functionality, it is common practice to include comments at the beginning of object definitions that are used similarly.

Given our desire for better documentation and wanting to leverage Python docstrings, the discussion focused on what they should include. Besides the information such as a brief statement of purpose as well as input and output parameters, we identified several issues with particular relevance for scientific applications. For instance, many algorithms had simple mathematical expressions that were not immediately obvious from their implementation in Python, but which a few equations written in L<sup>A</sup> TEX make clear. Often, our code implemented functionality described in peer-reviewed academic journals that could be referenced. Finally, we could provide short mini-examples of how to use the code. Since Python makes it easy to include examples in the docstrings as part of the test suite, this also improves test coverage and helps ensure that the documentation doesn’t get out of sync with the actual code. These types of standards encourage contributors to explicitly think about input, output, equations, examples, and references. This, in turn, helps promote more deliberate and rigorous coding practices. And when reviewing code already written, having these details recorded aids in understanding whether the code is performing as expected.

> 13 `http://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt`

12

### **3.5 Infrastructure**

For small projects, managing everything by hand may be straightforward. But as your research project (code, data, and text) evolves, the burden of running your tests, building your project, and generating reports will become overwhelming. Eventually you will need tools and procedures in place to take care of these details for you. Even when the project is small enough that you can manually manage things, automating these tasks can be extremely beneficial [7].

We have often seen colleagues shy away from adopting certain practices related to the infrastructure that supports their computational research with claims of not having enough time or energy to invest in learning how to use them. This is a good example of being penny wise and pound foolish: a small initial investment in learning best practices pays off manyfold over time in increased productivity and smoother workflows that can support collaboration and scale to complex scenarios. The manual execution and repetition of common computational tasks may appear like an easy solution, but it is error-prone and impossible to apply reliably in collaborative settings beyond two or three people.

In the next section we will discuss collaborative scenarios, but we want to address first how certain tools and practices have enormous value even for the individual researcher. And these are precisely the foundation that will then make it possible to naturally evolve a project from a single-person effort into a collaboration without a breakdown of complexity.

**Hosted version control.** While Git can be used purely locally, there are many advantages to having your repositories replicated on a server that is externally accessible. Git’s design allows it to simultaneously keep track of multiple repositories tied to a single project, and it can synchronize and merge work between these multiple sources. Each of these sources is denoted a _remote_ in Git lingo, and while a remote can be simply another location in your hard drive, the most useful kind of remotes are those that are physically on other computers. By synchronizing your local repository with an external remote you simultaneously have an automatic backup of your entire project’s history. But more importantly, this external remote is now available to synchronize with _other_ computers, so you can cleanly and robustly synchronize multiple machines, even if you do independent development on each of them at some point.

There are many services online that host repositories from Git and other version control systems; in recent years GitHub<sup>14</sup> has gained wide adoption among the community of scientists who write open source software in Python and R. As we discuss in _§_ 4.2, these systems truly shine once you use them to _collaborate_ with others, since collaboration hinges on the ability of multiple parties to synchronize their work.

**Continuous integration.** Once your computational code is stored in version control repositories and has tests and scripts that automate the execution of these tests, then it becomes possible to have a machine do this for you, all the time, bugging you only when something goes wrong. This is known as _continuous integration_ (CI). CI systems are servers that grab the most recent version of a project from version control, execute the test suite, and gather statistics of this process. They are typically configured to log and summarize these results, and to only produce alerts when something goes wrong (typically by email, but more aggressive options such as SMS are possible). The amount of data collected during the test execution can be configured, so it is possible to have setups that range from a basic sum-

> 14 `http://github.com`

13

mary of success and failure to a detailed collection of metrics on the performance evolution of a codebase.

These systems are called _continuous_ because they are meant to be used all the time: as the codebase evolves (typically when changes are committed to an official version control repository), the system fires automatically and collects its data. Therefore, these systems can also fulfill an important role: over time they accumulate a _historical retrospective_ of a project’s evolution. And this is where the importance of collecting detailed metrics is realized: a CI system configured to do a fairly detailed analysis of a project when it runs becomes an invaluable tool to analyze what is happening over time. Is performance degrading in subtle ways that are not evident from day to day? Is the fraction of code that is tested (known as the _test coverage_ ) going down over time, indicating that new contributions are not being tested as thoroughly as the older code? Questions like these are impossible to answer in a manually managed workflow, yet they come _for free_ once a few tools are set up, and can be an extremely important part of managing a healthy computational pipeline. A more detailed discussion of Continuous Integration can be found in [5].

While a number of these tools exist, one of the most widely used by projects from many different programming languages and communities is called _Jenkins_ .<sup>15</sup> Jenkins is a highly configurable CI system that can be run on a personal laptop or internal server and that is available hosted in the cloud as a service from a variety of sources. _Travis CI_<sup>16</sup> is a purely hosted CI system that, while not as configurable for fine-grained statistics as Jenkins, requires minimal setup, is free for open-source projects, and is tightly integrated with the version control hosting service GitHub.

**Documentation generation systems.** We have already discussed the importance of documenting your code, and in recent years a number of systems have been developed that allow you to easily produce complex documentation that combines hand-written narrative sections with parts that are automatically extracted from the code. While the ability to automatically extract and generate documentation is valuable and important, we stress that it is critical that your projects have at least a modicum of _narrative_ explaining the purpose of your tools, their scope, how to use them—with examples, and how the various concepts fit together. This kind of information cannot be gleaned from automatically extracted fragments that refer to individual function calls, and without it, your tools will be much less useful as a building block of robust scientific practice.

A number of tools exist for the generation of documentation, from the well-known L<sup>A</sup> TEX to systems focused on the generation of source-based documentation such as Doxygen<sup>17</sup> and newer ones designed for a combination of narrative and automatic documentation, like Sphinx.<sup>18</sup> There are other such systems, but Doxygen and Sphinx are widely used in the software world, actively developed and with rich toolkits that support complex documentation tasks.

Before discussing these tools, it is important to note that in recent years, new formats for _authoring_ documentation have emerged, in particular reStructuredText<sup>19</sup> (often abbreviated as reST) and Markdown.<sup>20</sup> These formats have slightly different philosophies, but they both

> 15 `http://jenkins-ci.org`

> 16 `http://travis-ci.org`

> 17 `http://doxygen.org`

> 18 `http://sphinx-doc.org`

> 19 `http://docutils.sourceforge.net/rst.html`

> 20 `http://daringfireball.net/projects/markdown/syntax`

14

aim at being more friendly to manual authoring and reading than L<sup>A</sup> TEX, while supporting more convenient integration with HTML output. They both share the basic philosophy of looking like plaintext with simple visual markup for commonly used tasks, for example marking emphasis and boldface with asterisks (e.g., `*italics*` _→ italics_ and `**boldface**` _→_ **boldface** ). Markdown is aimed at the production of HTML and is a strict subset of HTML; it defines only a few special markup rules and leaves more complex tasks to be done by hand in pure HTML. In contrast, reST is a highly extensible format, where new commands (called “roles” and “directives”) can be created and where the user can define entire new output pipelines by adding plugins written in Python to the processing stream. For example, the SciPy Conference Proceedings<sup>21</sup> are written in reST and the PDF version is generated by a custom L<sup>A</sup> TEX translator written in Python.

So while Markdown is simple and easy for the production of basic HTML, it is not well suited to the generation of complex multipart documents with rich internal crossreferencing, bibliographic support, etc. Both Markdown and reST support L<sup>A</sup> TEX for mathematical expressions, and with the right toolchain for rendering the output they can generate a final PDF document that has been typeset by L<sup>A</sup> TEX. In talking about new documentation formats it is important to mention the universal document converter, pandoc.<sup>22</sup> Pandoc is capable of translating between many document formats, including taking Markdown or reST input and producing HTML, L<sup>A</sup> TEX, and many other formats. It is an invaluable tool in managing a modern documentation workflow.

Returning our attention to systems that produce final output based on these formats, Doxygen has its own syntax that combines HTML with special commands for many tasks specific to computer source code, such as the specification of variable types, function arguments, and return values, etc. It also supports Markdown, allowing users to use this more readable and concise syntax for the generation of common HTML markup. Sphinx, on the other hand, is designed around reStructuredText: it supports the basic format and provides a number of additional extensions aimed at the documentation of software projects. Sphinx was originally developed to produce the official documentation for the Python programming language, but has become much more widely used. For instance, the SciPy community has developed an online wiki-like documentation editing system [33] on top of Sphinx that leverages the documentation standard discussed in _§_ 3.4, dramatically increasing the extent and quality of the NumPy and SciPy documentation.<sup>23</sup> Today most Python projects use Sphinx as their documentation system, and because of the flexibility and extensibility of reST, it has also become widely used as a way of creating rich, complex documents with a strong computational base even beyond Python. There are even some statistics courses taught in R, which use Sphinx to create web-based notes with embedded R code and automatically generated output.<sup>24</sup>

We note that all the formats we have discussed here, L<sup>A</sup> TEX, HTML, Markdown, and reST, share one critical feature: they can be hand-written in a plain text editor and they are stored in files amenable to version control with the tools described earlier. This stands in contrast to the binary formats of Microsoft Word and similar tools that lead to a terrible version control experience and which we avoid in computational workflows.

> 21 `http://github.com/scipy-conference/scipy_proceedings`

> 22 `http://johnmacfarlane.net/pandoc`

> 23 `http://docs.scipy.org/doc`

> 24 `http://www.stanford.edu/class/stats191`

15

---

[← 2 Computational research](03-2-computational-research.md) · [Up: contents](index.md) · [4 Collaboration →](05-4-collaboration.md)

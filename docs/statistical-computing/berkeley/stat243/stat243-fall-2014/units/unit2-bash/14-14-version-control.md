---
title: 14 Version Control
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 14 Version Control

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Note: Jarrod will cover the material on version control during Section.

At a basic level, a simple principle is to have version numbers for all your work: code, datasets, manuscripts. Whenever you make a change to a dataset, increment the version number. For code and manuscripts, increment when you make substantial changes or have obvious breakpoints in your workflow.

The basic idea of version control software (VCS) is that instead of manually trying to keep track of what changes you’ve made to code, data, and documents, you use software to help you manage the process. This has several benefits:

- easily allowing you to go back to earlier versions

- allowing you to have multiple version you can switch between

- allowing you to share work easily without worrying about conflicts

- providing built-in backup

The material that follows is borrowed from Jarrod Millman and Fernando Perez.

### **14.1 Warnings about this demo**

1. The demo should work if you just run the demo code ’manually’ on your machine. However, when compiled via knitr from the Lyx/Latex document, some of the later output in the branching section seems to be out of sync. So the output in this PDF is not quite right in a few places.

2. Also, note that the output from the embedded bash code chunks below is a bit annoying in that all the output appears in a group after all of the code lines rather than the output appearing after the individual line of code. This is some sort of issue with how knitr processes bash code chunks.

12


Figure 1: A snapshot of work at a point in time as stored in a ’commit’. Credit: ProGit book, by Scott Chacon, CC License.


Figure 2: A sequence of commits. Credit: ProGit book, by Scott Chacon, CC License.

### **14.2 VCS Overview**

There are a number of version control systems (VCS) including CVS and subversion, which use client-server models. Git is a distributed version control system. VCS store your material in a _repository_ .

The next couple figures show graphical representations of how a repository is structured. Recall that we have been using Git in a very simple fashion. We’ve cloned my class repository onto our local machines and have updated materials from that repository.

cd /tmp

git clone https://github.com/berkeley-stat243/stat243-fall-2014 git pull

The goal of this section is to learn how to do more with Git to actually manage a project of your own.

13

### **14.3 Hashing**

Hashing provides a way to have a fixed-length identifier for a given set of information, such as a file or set of files. The identifier is not guaranteed to be unique, but if the number of items is small, it will almost always be unique.

A toy "implementation"

**library** ("digest") _# first commit_ data1 <- "This is the start of my paper2." meta1 <- "date: 8/20/13" hash1 <- **digest** ( **c** (data1, meta1), algo = "sha1") **cat** ("Hash:", hash1, "\n") ## Hash: 32cff5042299244c8c248f6804bb9756912e5492 _# second commit, linked to the first_ data2 <- "Some more text in my paper..." meta2 <- "date: 8/20/13" _# Note we add the parent hash here! q_ hash2 <- **digest** ( **c** (data2, meta2, hash1), algo = "sha1") **cat** ("Hash:", hash2, "\n") ## Hash: 43925778805d33de28aba5697a967f04613f9153

We’ll see that Git uses hashes as identifiers for different versions of your work.

### **14.4 Local, single-user, linear workflow**

Simply type git (or git help) to see a full list of all the ’core’ commands. We’ll now go through most of these via small practical exercises:

git help ## usage: git [--version] [--exec-path[=<path>]] [--html-path] [--man-path] ## [-p|--paginate|--no-pager] [--no-replace-objects] [--bare] ## [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>] ## [-c name=value] [--help] ## <command> [<args>]

14

|##<br>## T|he most com|monly used git commands are:|
|---|---|---|
|##|add|Add file contents to the index|
|##|bisect|Find by binary search the change that introduced a bug|
|##|branch|List, create, or delete branches|
|##|checkout|Checkout a branch or paths to the working tree|
|##|clone|Clone a repository into a new directory|
|##|commit|Record changes to the repository|
|##|diff|Show changes between commits, commit and working tree, etc|
|##|fetch|Download objects and refs from another repository|
|##|grep|Print lines matching a pattern|
|##|init|Create an empty git repository or reinitialize an existing|
|##|log|Show commit logs|
|##|merge|Join two or more development histories together|
|##|mv|Move or rename a file, a directory, or a symlink|
|##|pull|Fetch from and merge with another repository or a local bra|
|##|push|Update remote refs along with associated objects|
|##|rebase|Forward-port local commits to the updated upstream head|
|##|reset|Reset current HEAD to the specified state|
|##|rm|Remove files from the working tree and from the index|
|##|show|Show various types of objects|
|##|status|Show the working tree status|
|##|tag|Create, list, delete or verify a tag object signed with GPG|
|##|||
|## S|ee 'git hel|p <command>' for more information on a specific command.|


#### **14.4.1 Initializing a Git repository**

We use _git init_ to create an empty repository

cd /tmp rm -rf git-demo git init git-demo ## Initialized empty Git repository in /tmp/git-demo/.git/

Let’s look at what git did:

15

cd /tmp/git-demo ls -al ls -al .git ## total 280 ## drwxr-xr-x 3 paciorek scfstaff 4096 Sep 3 08:34 . ## drwxrwxrwt 52 root root 274432 Sep 3 08:34 .. ## drwxr-xr-x 7 paciorek scfstaff 4096 Sep 3 08:34 .git ## total 40 ## drwxr-xr-x 7 paciorek scfstaff 4096 Sep 3 08:34 . ## drwxr-xr-x 3 paciorek scfstaff 4096 Sep 3 08:34 .. ## drwxr-xr-x 2 paciorek scfstaff 4096 Sep 3 08:34 branches ## -rw-r--r-- 1 paciorek scfstaff 92 Sep 3 08:34 config ## -rw-r--r-- 1 paciorek scfstaff 73 Sep 3 08:34 description ## -rw-r--r-- 1 paciorek scfstaff 23 Sep 3 08:34 HEAD ## drwxr-xr-x 2 paciorek scfstaff 4096 Sep 3 08:34 hooks ## drwxr-xr-x 2 paciorek scfstaff 4096 Sep 3 08:34 info ## drwxr-xr-x 4 paciorek scfstaff 4096 Sep 3 08:34 objects ## drwxr-xr-x 4 paciorek scfstaff 4096 Sep 3 08:34 refs

#### **14.4.2 Adding content to a repository**

Now let’s edit our first file in the test directory with a text editor... I’m doing it programatically here for automation purposes, but you’d normally be editing by hand

cd /tmp/git-demo echo "My first bit of text" > file1.txt

Now we can tell git about this new file using the _add_ command:

cd /tmp/git-demo git add file1.txt

We can now ask git about what happened with _status_ :

16

cd /tmp/git-demo git status ## # On branch master ## # ## # Initial commit ## # ## # Changes to be committed: ## # (use "git rm --cached <file>..." to unstage) ## # ## # new file: file1.txt ## #

#### **14.4.3 Committing changes**

We now permanently record our changes in git’s database.

For now, we are always going to call _git commit_ either with the ‘-a‘ option or with specific filenames (git commit file1 file2...). This avoids discussion of an aspect of git called the _index_ (often referred to also as the ’staging area’). Most everyday work in regular scientific practice doesn’t require understanding the extra moving parts that the index involves, so we’ll bypass it.

cd /tmp/git-demo git commit -am"This is our first commit" git status

---

[← 13 How much shell scripting should I learn?](13-13-how-much-shell-scripting-should-i-learn.md) · [Up: contents](index.md) · [Unit 02 — bash Part 15 — →](15-unit-02-bash-part-15.md)

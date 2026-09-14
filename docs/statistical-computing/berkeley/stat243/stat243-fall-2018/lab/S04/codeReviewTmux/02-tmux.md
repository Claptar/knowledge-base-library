---
title: TMUX
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S04/codeReviewTmux.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2018/lab/S04/codeReviewTmux.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# TMUX

**Source:** [`lab/S04/codeReviewTmux.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/lab/S04/codeReviewTmux.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## What is tmux?

The official verbiage describes tmux as a screen multiplexer, similar to GNU Screen. Essentially that means that tmux lets you tile window panes in a command-line environment. This in turn allows you to run, or keep an eye on, multiple programs within one terminal.

## Installation

This guide will focus on MacOS and Ubuntu. If you are on CentOS or Amazon Linux, you can use `yum` in place of `apt-get`.

### MacOS Installation
The easiest way to get started with tmux on a Mac is to use the Homebrew package manager.

  1. If you don't have Homebrew installed yet, open either Terminal and paste the below command:
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
  2. Once Homebrew is installed, you can use brew to install tmux:
```bash
brew install tmux
```

3. Confirm that it installed by checking the version (note the uppercase V):
```bash
tmux -V
```


### Ubuntu / Debian Linux Installation
Installation for Ubuntu is similar to Mac, except that we will be using the apt-get package manager that comes pre-installed. Note that we will have to run `apt-get` as sudo. This is because a user account won't have enough privileges to install tmux, so sudo will allow us to install it as superuser.

  1. Update apt-get to make sure we are on the latest and greatest:
```bash
sudo apt-get update
```
2. Install tmux:
```bash
sudo apt-get install tmux
```
3. Confirm that it installed by checking the version:
```bash
tmux -V
```

## Getting In & Getting Out

tmux is based around sessions. To start a new session in tmux, simply type `tmux new` in your terminal. Once you are in tmux, the only thing that will be visibly different is the ever-present green bar at the bottom.

To get out, you can type `exit` if you're in a single pane, and you'll return from whence you came.

An important note is that exit is not the only way to get out, and usually not the best way. For that we have `detach`. However before we get to that, we first have to cover the prefix ...

### Using Prefix

All commands in tmux require the prefix shortcut, which by default is `ctrl+b`. We will be using the prefix a lot, so best to just commit it to memory. After entering `ctrl+b` you can then run a tmux command, or type `:` to get a tmux prompt.

When entering the prefix, tmux itself will not change in any way. So, if you enter `ctrl+b` and nothing changes, that does not necessarily mean you typed it wrong.


### Attach, Detach & Kill
As mentioned, a better way to get out of a session without exiting out of everything is to `detach` the session. To do this, you first enter the prefix command and then the detach shortcut of `d`:

```bash
ctrl+b d
```

This will detach the current session and return you to your normal shell.

However, just because you're out doesn't mean your session is closed. The detached session can still available, allowing you to pick up where you left off. To check what sessions are active you can run:

```bash
tmux ls
```

The tmux sessions will each have a number associated with them on the left-hand side (zero indexed as nature intended). This number can be used to attach and get back into this same session. For example, for session number 3 we would type:

```bash
tmux attach-session -t 3
```

or we can go to the last created session with:

```bash
tmux a #
```

### Naming Sessions
Now we could just rely the session numbers, but it would make our life much easier if we give our sessions names based on their intended use.

To start a new session with a specific name we can just do the below:

```bash
tmux new -s [name of session]
```
With named sessions in place, now when we do `tmux ls` we see the session name instead. Likewise, we can then attach a session by using the name:

```bash
tmux a -t [name of session]
```
Note that we substituted `a` for `attach-session` to help save on keystrokes.

## Managing Panes
In a GUI desktop environment, you have windows. In tmux, you have panes. Like windows in a GUI, these panes allow you to interact with multiple applications and similarly can be opened, closed, resized and moved.

Unlike a standard GUI desktop, these panes are tiled, and are primarily managed by tmux shortcuts as opposed to a mouse (although mouse functionality can be added). To create a new pane you simply split the screen horizontally or vertically.

To split a pane horizontally:
```bash
ctrl+b "
```
To split pane vertically:
```bash
ctrl+b %
```

You can split panes further using the same methodology. For example, in the above screenshot, the screen was first split horizontally using `ctrl+b "` and then split vertically within the lower pane using `ctrl+b %`.

To move from pane to pane, simply use the prefix followed by the arrow key:
```bash
ctrl+b [arrow key]
```

### Resizing Panes
Lets say we need a little extra breathing room for one of our panes, and want to expand the pane down a few lines. For this, we will go into the tmux prompt:

```bash
ctrl+b :
```

From there we can type resize-pane followed by a direction flag: `-U` for up, `-D` for down `-L` for left and `-R` for right. The last part is the number of lines to move it over by.

As an example, if we are in the top pane and want to expand it down by 2 lines, we would do the following:
```bash
ctrl+b :
resize-pane -D 2
```


## Additional Resources
The possibilities here are just the tip of the iceberg. If you are ready to go even further down the rabbit-hole, the below links should help fill the gaps.

  - [Cheatsheet](https://gist.github.com/MohamedAlaa/2961058) by MohamedAlaa
  - [tmux-themepack](https://github.com/jimeh/tmux-themepack) by Jim Myhrberg
  - [The Tao of tmux](https://leanpub.com/the-tao-of-tmux/read) by Tony Narlock
  - [Oh My Tmux!](https://github.com/gpakosz/.tmux) by Gregory Pakosz

---

[← Code Review](01-code-review.md) · [Up: contents](index.md)

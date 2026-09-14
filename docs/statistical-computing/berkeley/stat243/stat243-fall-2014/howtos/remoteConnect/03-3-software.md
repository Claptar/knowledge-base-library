---
title: 3 Software
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/howtos/remoteConnect.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/howtos/remoteConnect.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Software

**Source:** [`howtos/remoteConnect.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/howtos/remoteConnect.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **3.1  Linux**

Linux natively runs the X Windows system, and most Linux systems have the ssh program available to securely connect to remote systems.

### **3.2  Mac OS X**

The ssh command is available through the Terminal application (available in /Applications/Utilities /Terminal.app). Versions of the operating system from Panther on provide an installation package for X11 on the Developer Disk (X11User.pkg).

### **3.3  Microsoft Windows**

To connect to the SCF remotely, you can use a free program called putty. You can download it from <u>http://www.chiark.greenend.org.uk/ sgtatham/putty/download.html. This will allow you to run</u> programs remotely, but it will not allow you to use the display manager, or to view graphics. To do this, you need an X Windows emulator. If you have a CalNet ID, you can download Exceed 2008 from UC Berkeley Software Distribution. A free alternative to Exceed is the Cygwin X Windows System. There are excellent instructions for installing this software at Cygwin/X. Basically, you first download a program called setup.exe, which makes it possible to install a wide variety of software;

1 of 3

07/25/2011 01:51 PM

Connecting Remotely to the Statistical Computing...

http://www.stat.berkeley.edu/classes/s243/remote.html

you need choose only four packages: xorg-server, xorg-scripts, inetutils and openssh (Clicking on the View button in the setup.exe window until it displays "Full" makes it easier to find the packages you need). Once everything is installed there should be a Cygwin icon on your desktop. Double click on the Cygwin icon and type

/usr/bin/startxwin.sh

in the window that opens. Another window will open and you can use the ssh command as described below. (Notice when you use Cygwin, there's no need for the putty program, since Cygwin provides the ssh command.)

### **3.4  Commands**

#### **3.4.1  Microsoft Windows: putty**

To use putty with an X Windows emulator, you need to make one change to the default settings: In the left-pane, click the X to the left of SSH under Connections, and click on X11. Check the box marked "Enable X11 forwarding". Once this is done, you can connect to the SCF by choosing "Session" in the left hand pane, filling in a valid hostname, and clicking "Open"

### **3.5  Linux and Mac: ssh**

To connect to the SCF computers, use a command like this in the terminal:

ssh -X s243xx@hostname

where s243xx is your SCF class account, and hostname is one of the SCF computers. The -X flag allows tunneling of X11 connections so that you can view graphics from the SCF computers. Don't forget to include .berkeley.edu after the hostname if you're connecting from outside the Berkeley domain.

---

[← 2 Usernames and Hostnames](02-2-usernames-and-hostnames.md) · [Up: contents](index.md) · [4 File Transfer →](04-4-file-transfer.md)

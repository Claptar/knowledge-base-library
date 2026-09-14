---
title: 4 File Transfer
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/howtos/remoteConnect.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/howtos/remoteConnect.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 File Transfer

**Source:** [`howtos/remoteConnect.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/howtos/remoteConnect.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

If you want to print SCF documents on your own (non-SCF) printer, the easiest route is to copy the files from the SCF computers to your computer and then to print them in the usual way. The best way is to use a file transfer program on your local computer, although other means are possible. Before transfering files, make sure that you can print them on the computer you're transfering them to. PostScript (.ps) files often cause problems. If you want to print a PostScript file, and you're not sure if your program has the necessary software, run the following command on the SCF system:

ps2pdf filename.ps

where filename.ps is the name of the file you'd like to print. You can then copy the resulting pdf file to your computer and view or print it with Adobe Acrobat.

### **4.1  Linux**

The command line scp command, described below, is probably the best way to transfer files from one computer to another. If you'd prefer a graphical client, programs like konqueror will accept the sftp:// protocol.

### **4.2  Mac OS X**

The command line scp command, described below, can be accessed through the terminal

2 of 3

07/25/2011 01:51 PM

Connecting Remotely to the Statistical Computing...

http://www.stat.berkeley.edu/classes/s243/remote.html

(/Applications/Utilities/Terminal.app). Although the finder doesn't directly support the sftp protocol, the freeware program Fugu provides a nice graphical frontend to the sftp command. To use Fugu, enter your username and an appropriate hostname in the Connect to: field; you'll be prompted for a password when Fugu connects to the remote server. Your remote files will appear in Fugu's right-hand pane, where they can be dragged and dropped to a location of your choice in the (local) left-hand pane.

### **4.3  Microsoft Windows**

There are a number of free graphical sftp clients available for Windows; one nice and easy-to-use one is WinSCP. If you choose the Explorer view instead of the default Norton Commander view, your SCF account will appear as a normal explorer window, allowing you to drag and drop files; simply enter your username and a suitable hostname to connect.

### **4.4  If All Else Fails**

If you can't use the previously described methods, you can email files from the SCF system to an email account of your choice. One way is to use the command line program pine. To send files as attachments with pine, enter the following command in an ssh window connect to an SCF computer:

pine emailaddress -attach file1 -attach file2 ...

After hitting Return, type control-X to send the mail, and Y to confirm it. **Note:** There is a 5 Mb limit on attachments to emails sent through the SCF. While this should pose no problems with text files, complex graphics may be too large to send through email. Please check the size of the file you're sending (with the UNIX command ls -l) before reporting a problem.

### **4.5  The scp command**

The syntax for the scp command is:

scp username@hostname:file local-directory

You'll be prompted for your password; after entering it and hitting Return, the file transfer will start.

To use wildcard patterns on the remote (SCF) machine, precede the wildcard character with a backslash (\). For example to copy all the C files from the home directory of your SCF account, to the current directory on your local computer, use a command like:

scp username@hostname:\*.c .

File translated from TEX by <u>TTH, version 3.67.</u> On 2 Sep 2009, 00:44.

3 of 3

07/25/2011 01:51 PM

---

[← 3 Software](03-3-software.md) · [Up: contents](index.md)

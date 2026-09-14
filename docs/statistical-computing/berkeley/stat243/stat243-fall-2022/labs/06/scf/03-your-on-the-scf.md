---
title: Your ~/ on the SCF
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/06/scf.qmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/06/scf.qmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Your ~/ on the SCF

**Source:** [`labs/06/scf.qmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/06/scf.qmd) · **Licence:** unresolved · Converted 2026-09-14 from `.qmd` (lossless)

Nodes in the SCF cluster use the Linux distribution Ubuntu. Every user has a
private home directory which, as usual on Linux-based OSes, has the shortcut
`~/`. In this section, we'll give an overview of access, disk space, and remote
file transfers to and from your SCF home directory.

## Logging in

The SCF has a number of **login nodes** which you can access via `ssh`.

!!! note "Note"
For info on using `ssh` (including on Windows), see
[here](https://statistics.berkeley.edu/computing/ssh).

:::

For example, I'll use `ssh` to connect to the `dorothy` node:

```bash
james@pop-os:~$ ssh jpduncan@dorothy.berkeley.edu
The authenticity of host 'dorothy.berkeley.edu (128.32.135.58)' can't be established.
ED25519 key fingerprint is SHA256:rOY7ED/iIiTgI++Y4XHmiEl+tC+OmSGBvWp03CSII5E.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'dorothy.berkeley.edu' (ED25519) to the list of known hosts.
```

Notice that upon first connecting to a server you haven't visited there is a
warning that the "authenticity of the host ... can't be established". So long as
you have typed in the hostname correctly (`dorothy.berkeley.edu`, in this case),
and trust the host (we trust the SCF!) then you can type `yes` to add the host
to your known hosts file (found on your local machine at `~/.ssh/known_hosts`).

You'll then be asked to enter your password for the SCF cluster. For privacy,
you won't see anything happen in your terminal when you type it in, so type
carefully (you can use `Backspace` if you make a mistake) and press `Enter` when
you're done. If you were successful, you should see a welcome message and your
shell prompt, like:

```bash
jpduncan@dorothy:~$
```

To get your bearings, you can type `pwd` to see where your home directory is
located on the SCF cluster filesystem:

```bash
jpduncan@dorothy:~$ pwd
/accounts/grad/jpduncan
```

Your home directory is likely also in the `/accounts/grad/` directory, as mine
is.

### Other login nodes

!!! important "Important"
Don't run computationally intensive tasks on the login nodes!

They are shared by all the SCF users, and should only be used for non-intensive
interactive work such as job submission and monitoring, basic compilation,
managing your disk space, and transferring data to/from the server.

:::
 If for some reason `dorothy` is not working for you, the SCF has a number of
nodes which can be accessed from your local machine with commands of the form
`ssh <scf-username>@<hostname>.berkeley.edu`. Currently, these are:

- `aragorn`
- `arwen`
- `dorothy`
- `gandalf`
- `gollum`
- `hermione`
- `quidditch`
- `radagast`
- `shelob`

## Disk space

Your home directory has a limited amount of disk space; you can check how much
you have used and available using the `quota` command, which will show your home
directory usage and quota on the line for the `accounts` filesystem.

```bash
jpduncan@dorothy:~$ quota
FILESYSTEM	USE     	QUOTA   	%
  accounts	5.29 G  	20 G    	26.5
```

The `accounts` filesystem is accessible from all the nodes on the SCF cluster.
This means that regardless of which login or compute node you use, you will have
access to the files in your home directory. Moreover, your home directory is
backed up regularly, so you are protected from accidental data loss.

If you're running out of space, you should try to selectively delete large files
that you no longer need. See
[here](https://statistics.berkeley.edu/computing/faqs/how-do-i-manage-my-data)
for some tips on finding large files. If all else fails, you can request
additional space or request access the `/scratch` filesystem. The latter is a
good place for large datasets, but note that `/scratch` is not backed up, unlike
your home directory. See the previous link for more info.

For temporary files (e.g., intermediate results of a computation that you don't
need to store for later), every machine has a `/tmp` filesystem. However, `/tmp`
is _always linked to the specific machine_ you are on, meaning that if you put
something in `/tmp` on `dorothy` and then later go to `aragorn`, you won't find
your files in the `/tmp` directory there. If you go back to `dorothy`, you will
likely find them again, but `/tmp` is automatically wiped when a machine
reboots, so only use it for files you don't care about preserving!

## Data transfer: SCP / SFTP

We can use the `scp` and `sftp` protocols to transfer files to and from any
login node on the SCF cluster. `scp` is a shell program that should be available
by default on macOS and Linux, while on Windows you can use
[WinSCP](https://winscp.net/eng/index.php). WinSCP can also do `sftp` transfers,
or you can use [FileZilla](https://filezilla-project.org/) on any platform for
`sftp`. Both WinSCP and FileZilla have a GUI that allows you to drag and drop
files between your local machine and a remote host.

The syntax for `scp` is `scp <from-place> <to-place>`, and you'll typically use
`scp` on your local machine. For example, we'll show how to transfer the file
`data.csv` (you can find it [here](https://github.com/berkeley-stat243/stat243-fall-2022/tree/main/labs/06))
:

### To SCF while on your local machine

```bash

---

[← SCF cluster capabilities and hardware](02-scf-cluster-capabilities-and-hardware.md) · [Up: contents](index.md) · [transfer to my home directory without renaming the file →](04-transfer-to-my-home-directory-without-renaming-the-file.md)

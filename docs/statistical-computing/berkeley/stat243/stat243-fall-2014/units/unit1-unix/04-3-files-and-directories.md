---
title: 3 Files and directories
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit1-unix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit1-unix.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Files and directories

**Source:** [`units/unit1-unix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit1-unix.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. Files are stored in directories (aka folders) that are in a (inverted) directory tree, with “ **_/_** ” as the _root_ of the tree

2. Where am I?

> pwd

3. What’s in a directory?

> ls

> ls -a

> ls -al

> ls -lrt

4. Moving around

> cd /accounts/gen/vis/paciorek/teaching/243

> cd ~paciorek/teaching/243

> cd ~/teaching/243

> cd stat243-fall14-243 # provided I am in ’teaching’

> cd ..

> cd -

5. Copying and removing

> cp

> cp -r

> cp -rp # preserves timestamps and other metainfo (VERY handy for tracing your workflows if you move files between machines)

> mkdir

> rm

> rm -r

2

> rm -rf # CAREFUL!

To copy between machines, we can use _scp_ , which has similar options to _cp_ :

   - scp file.txt paciorek@radagast.berkeley.edu:~/research/.

   - scp paciorek@radagast.berkeley.edu:/data/file.txt

   - ~/research/renamed.txt

6. File permissions: **ls -al** will show the permissions for the ’ _user_ ’, ’ _group_ ’, ’ _other_ ’ ( _ugo_ ) for **r** eading, **w** riting and e **x** ecuting files ( _rwx_ ):

      - to allow a file to be executed as a program:

         - chmod ugo+x myProg # myProg should be compiled code or a

         - shell script

      - to allow read and write access to all:

         - chmod ugo+rw code.R

      - to prevent write access:

         - chmod go-w myThesisCode.R

7. Compressing files

      - the _zip_ utility compresses in a format compatible with zip files for Windows:

         - zip files.zip a.txt b.txt c.txt

      - _gzip_ is the standard in UNIX:

         - gzip a.txt b.txt c.txt # will create a.txt.gz, b.txt.gz,

         - c.txt.gz

      - _tar_ will nicely wrap up entire directories:

         - tar -cvf files.tar myDirectory

         - tar -cvzf files.tgz myDirectory

      - To unwrap a tarball

         - tar -xvf files.tar

         - tar -xvzf files.tgz

      - To peek into a zipped (text) file:

         - gzip -cd file.gz | less

         - zcat file.zip | less

3

#### 8. Disk space

- To see how much space is free in the various filesystems available on a machine: > df -h

- To see how much space is used in a directory: > du -h

- To see how much space you are using out of your overall quota

   - quota -s

---

[← 2 Version control](03-2-version-control.md) · [Up: contents](index.md) · [4 A variety of UNIX tools/capabilities →](05-4-a-variety-of-unix-tools-capabilities.md)

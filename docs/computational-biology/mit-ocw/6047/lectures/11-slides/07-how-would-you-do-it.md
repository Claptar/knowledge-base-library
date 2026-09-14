---
title: How would you do it
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# How would you do it

**Source:** `lectures/11-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

• L2: Sequence alignment: O(m*n) • L3: Hashing / BLAST: O(m+n)

   - Solution until 2008 (e.g. MAQ, Li et al, GR 2008)

- Other advanced algorithms:

   - Linear-time string matching: O(m+n). L3 addendum

   - Suffix trees and suffix arrays: O(m). L13 addendum

- Challenge: memory requirements

   - Hash table, suffix tree/array require O(m*n) space

- Today: Burrows-Wheeler transformation O(m)

   - Ultrafast/memory efficient. New norm since 2009.

– Introduced in: Bowtie (Langmead GB 2009).

18

18

###### Second Generation Mappers have Leveraged the Burrows Wheeler Transformation


“…35 times faster than Maq and 300 times faster than SOAP under the same conditions”


© Various copyright holders. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

19

## Hashing vs. Burrows Wheeler Transform


<!-- Start of picture text -->
Multi-seed<br>hashing<br>BWT<br>Burrows-<br>Wheeler<br>Transform<br>Today: How does the BW<br>transform actually work?<br><!-- End of picture text -->

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Trapnell, Cole and Steven L. Salzberg. "How to map billions of short reads onto genomes." Nature Biotechnology 27, no. 5 (2009): 455.

20

Burrows-Wheeler Transform (BWT) <u>http://www.hpl.hp.com/techreports/Compaq-DEC/SRC-RR-124.pdf</u> • Transform: ^BANANA@ INTO: BNN^AA@A

**function** BWT ( _string_ s) create a table, rows are all possible rotations of s sort rows alphabetically **return** (last column of the table)

• Reversible

**function** inverseBWT ( _string_ s) create empty table **repeat** length(s) **times**

insert s as a column of table before first column of the table // first insert creates first column sort rows of the table alphabetically

**return** (row that ends with the 'EOF' character)

**Last column only** suffices to reconstruct **entire matrix** , and thus recover **original string**

last 1st pairs 2<sup>nd</sup> triples 3<sup>rd</sup> 4mers 4<sup>th</sup> col 5mers 5<sup>th</sup> col 6-mers 6<sup>th</sup> col 7-mers 7<sup>th</sup> col 8-mers Full matrix 21 col col col

---

[← Mapping Reads to the Genome](06-mapping-reads-to-the-genome.md) · [Up: contents](index.md) · [Searching for an Exact Match →](08-searching-for-an-exact-match.md)

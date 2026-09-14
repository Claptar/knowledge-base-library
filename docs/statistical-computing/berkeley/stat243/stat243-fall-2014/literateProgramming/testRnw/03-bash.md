---
title: bash
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/literateProgramming/testRnw.tex
source_file: sources/berkeley-stat243/stat243-fall-2014/literateProgramming/testRnw.tex
licence: unresolved
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# bash

**Source:** [`literateProgramming/testRnw.tex`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/literateProgramming/testRnw.tex) · **Licence:** unresolved · Converted 2026-09-14 from `.tex` (high)

Now in bash, we have similar problems with line endings but bash allows us to use a backslash to break lines of code. The one thing that doesn’t help us with is long lines of output. Also, we need to break long comments ourselves. And note that all results are printed at the end of a code chunk instead of interspersed immediately after the command generating the output.

    echo "my long line blah blah blah blah more blah more blah more blah blah blah blash blah blah blah of stuff" > tmp.txt

    echo "contents of tmp.txt blah blah blah blah \
    more blah more blah more blah \
    blah blah blash blah blah blah \
    more more more more more more \
    more more more more" > tmp.txt

    echo "my long line"\
    > tmp2.txt

    cat tmp.txt

    # the following long comment line is not broken in my test:
    # asdl lkjsdf jklsdf kladfj jksfd alkfd klasdf klad kla lakjsdf aljdkfad kljafda kaljdf afdlkja lkajdfsa lajdfa adlfjaf jkladf afdl

    # instead manually break it:
    # asdl lkjsdf jklsdf kladfj jksfd alkfd klasdf klad kla
    # lakjsdf aljdkfad kljafda kaljdf afdlkja lkajdfsa lajdfa
    # adlfjaf jkladf afdl
    ## contents of tmp.txt blah blah blah blah more blah more blah more blah blah blah blash blah blah blah more more more more more more more more more more

None of the bash code worked in RStudio.

---

[← R](02-r.md) · [Up: contents](index.md) · [Python →](04-python.md)

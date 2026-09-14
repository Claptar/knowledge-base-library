---
title: Python {#python}
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/literateProgramming/testRnw.tex
source_file: sources/berkeley-stat243/stat243-fall-2014/literateProgramming/testRnw.tex
licence: unresolved
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Python {#python}

**Source:** [`literateProgramming/testRnw.tex`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/literateProgramming/testRnw.tex) · **Licence:** unresolved · Converted 2026-09-14 from `.tex` (high)

In my Sweave+knitr test it only shows Python code evaluation results when you use an explicit print statement. Line breaks are still an issue but manual breaking of long code lines seems to work. As with bash, all output is printed at the end of the chunk.

    2 + 2
    print(2 + 2)
    type(2.0)

    endLine = "."
    name = "sam"
    if name == 'samuel':
      print(intro + name.capitalize() + endLine)
    elif name == "sam":
      print("My nickname is " + name.capitalize() + endLine)
    else:
      print("My name is something else.\n")

    # this overflows the page
    b = "asdl lkjsdf jklsdf kladfj jksfd alkfd klasdf klad kla lakjsdf aljdkfad kljafda kaljdf afdlkja lkajdfsa lajdfa adlfjaf jkladf afdl"
    print(b)

    # this code overflows the page
    zoo = {"lion": "Simba", "panda": None, "whale": "Moby", "numAnimals": 3, "bear": "Yogi", "killer whale": "shamu", "bunny:": "bugs"}
    print(zoo)

    # instead manually break the code
    zoo = {"lion": "Simba", "panda": None, "whale": "Moby",
           "numAnimals": 3, "bear": "Yogi", "killer whale": "shamu",
           "bunny:": "bugs"}
    print(zoo)
    ## 4
    ## My nickname is Sam.
    ## asdl lkjsdf jklsdf kladfj jksfd alkfd klasdf klad kla lakjsdf aljdkfad kljafda kaljdf afdlkja lkajdfsa lajdfa adlfjaf jkladf afdl
    ## {'killer whale': 'shamu', 'lion': 'Simba', 'bunny:': 'bugs', 'bear': 'Yogi', 'numAnimals': 3, 'whale': 'Moby', 'panda': None}
    ## {'killer whale': 'shamu', 'lion': 'Simba', 'bunny:': 'bugs', 'bear': 'Yogi', 'numAnimals': 3, 'whale': 'Moby', 'panda': None}

None of the Python code worked in RStudio.

---

[← bash {#bash}](03-bash-bash.md) · [Up: contents](index.md)

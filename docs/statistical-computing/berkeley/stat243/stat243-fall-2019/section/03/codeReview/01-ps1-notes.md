---
title: PS1 Notes
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/03/codeReview.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/03/codeReview.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# PS1 Notes

**Source:** [`section/03/codeReview.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/03/codeReview.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

1. **SUBMISSIONS MUST BE A PDF DOCUMENT**
Specifically, you must knit the Rmd, so that your code builds, your document builds,
and all of the output is shown. Saving the .Rmd as a pdf is not the same.

2. `suppressWarnings()`
Don't use this. Fix the problems.

3. Read the function documentation
R has very complete function documentation, in terms of what options exist and what
they do. This is easily accessed by using `?write.table()` or `??write.table()`.
This also provides the default values for all of the options.

4. Scoping
We will cover this in detail in unit 5, but here's a short explanation.
R looks for variables within the environment where they are called, ie. within
a function. If it doesn't find it, it then looks in the parent environment.
eg.
    ```r
    # variable defined in .Global
    x <- 1:10

    myFunc <- function(){
      # variable defined in myFunc
      y <- 1:10

      # return
      return(x + y)
    }

    myFunc()
    ```
This occurs again when using `<-` vs `<<-`.
(Potentially interesting [SO](https://stackoverflow.com/questions/2628621/how-do-you-use-scoping-assignment-in-r) discussion.)
    ```r
    # variable defined in .Global
    x <- 1
    y <- 1
    # z <- 1

    # function
    sideEffects <- function(){
      # local assignment
      y <- 2

      # global assignment
      x <<-2

      # global creation
      z <<- 10
    }

    # run function
    sideEffects()

    # see results
    x; y; z;

    ```

5. `suppressPackageStartupMessages()`
Do use this. This function (should) suppress messages from loading a package.
This prevents the long messages from things like `tidyverse`.
**Beware** - This may cover up warnings about function name clashes.

6. `require()` vs. `library()`
See the [bCourses anouncement](https://bcourses.berkeley.edu/courses/1484436/discussion_topics/5588531)
Additionally, I would never put them in functions. I prefer them near the top of the
document (that way you know what you need immediately), or at least at the top
of the chunk that requires them. Within functions, it is best to call things using
the namespace explicitely, ie. `devtools::build()`. The prevents you from loading
all of the functions in a package and cluttering the namespace.

7. Beware base function names. Don't redefine names. ie, `data` or `list`.

8. Use `return()` explicitly in a function
    ```r
    myFunc <- function(x){
      # crazy stuff

      # explicit return
      return(x)
    }
    ```
Also, `print()` is not the same as `return()`. You can't use the output of print
(easily), while a returned object can be stored for later use.

9. if/else Statements
I don't know why this works in functions, but it's not correct.
    ```r
    # basic if statement
    if(TRUE){
      cat("I did the thing!\n")
    }
    ```
    ```r
    # properly formatted if/else statement
    if(FALSE){
      cat("I did the thing!\n")
    } else {
      cat("I like cats\n")
    }
    ```
    ```r
    # improperly formatted if/else statement
    if(FALSE){
      cat("I did the thing!\n")
    }
    else {
      cat("I like cats\n")
    }
    ```
    ```r
    # improper if/else inside function
    printFunc <- function(){
      if(FALSE){
        cat("I did the thing!\n")
      }

      else {
        cat("I like cats\n")
      }
    }

    # function works
    printFunc()

    ```

---

[Up: contents](index.md) · [Code Review →](02-code-review.md)

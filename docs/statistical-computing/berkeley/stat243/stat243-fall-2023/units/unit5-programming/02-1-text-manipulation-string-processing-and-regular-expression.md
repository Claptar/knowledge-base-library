---
title: 1. Text manipulation, string processing and regular expressions (regex)
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit5-programming.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 1. Text manipulation, string processing and regular expressions (regex)

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit5-programming.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

Text manipulations in Python have a number of things in common with UNIX, R,
and Perl, as many of these evolved from UNIX. When I use the term
*string* here, I'll be referring to any sequence of characters that may
include numbers, white space, and special characters, usually stored as an object
of the `str` class.

## String processing and regular expressions in Python

Here we'll see functionality for working with strings in Python, focusing on regular expressions with the `re` package.
This will augment our consideration of regular expressions in the shell, in particular
by seeing how we can replace patterns in addition to finding them.

The `re` package provides Perl-style regular expressions, but it doesn't seem to support named character classes such as `[:digit:]`. Instead use classes such as `\d` and `[0-9]`.

In Python, you apply a matching function and then query the result to get information about what was matched and where in the string.


```python
text = "Here's my number: 919-543-3300."
m = re.search("\d+", text)
m
m.group()
m.start()
m.end()
m.span()
```


Notice that that showed us only the first match.

We can instead use `findall` to get all the matches.

```python
re.findall("\d+", text)
```


This is equivalent to:

```python
pattern = re.compile("\d+")
re.findall(pattern, text)
```

The compile can be omitted and will be done implicitly, but is a good idea to do explicitly if you have a complex regex pattern that you will use repeatedly (e.g. on every line in a file). It is also a reminder that regular expressions is a separate language, that can be compiled into a program. The compilation results in an object that relies on finite state machines to match the pattern.

To ignore case, do the following:

```python
text = "That cat in the Hat"
re.findall("hat", text, re.IGNORECASE)
```

There are several other regex flags (also called compilation flags) that can control the behavior of the matching engine in interesting ways (check out re.VERBOSE and re.MULTILINE for instance).

We can of course use list comprehension to work with multiple strings. But we need to be careful to check whether a match was found.

```python
def return_group(pattern, txt):
    m = re.search(pattern, txt)
    if m:
       return m.group()
    else:
       return None

text = ["Here's my number: 919-543-3300.", "hi John, good to meet you",
        "They bought 731 bananas", "Please call 1.919.554.3800"]
[return_group("\d+", str) for str in text]
```

We can replace matching substrings with `re.sub`.

```python
text = "Here's my number: 919-543-3300."
re.sub("\d", "Z", text   )
```

Recall that we can search for location-specific matches in relation to the start and end of a string.

```python
text = "hats are all that are important to a hatter."
re.findall("^hat\w+", text)
```

Recall that we can search based on repetitions (as already demonstrated with the `\w+` just above).

```python
text = "Here's my number: 919-543-3300. They bought 731 bananas. Please call 1.919.554.3800."
re.findall("\d{3}[-.]\d{3}[-.]\d{4}", text)
```

Next let's consider grouping using `()`.

Here’s a basic example of using grouping via parentheses with the OR operator.

```python
text = "At the site http://www.ibm.com. Some other text. ftp://ibm.com"
re.search("(http|ftp):\\/\\/", text).group()
```

However, if we want to find all the matches and try to use `findall`, we see that it returns only the captured groups when grouping operators are present, as discussed a bit in `help(re.findall)`,
so we'd need to add an additional grouping operator to capture the full pattern when using `findall`:

```python
re.findall("(http|ftp):\\/\\/", text)
re.findall("((http|ftp):\\/\\/)", text)
```

When you are searching for all occurrences of a pattern in a large text object, it may be beneficial to use `finditer`:

```python
it = re.finditer("(http|ftp):\\/\\/", text)  # http or ftp followed by ://

for match in it:
    match.span()
```

This method behaves lazily and returns an iterator that gives us one match at a time, and only scans for the next match when we ask for it. This is similar to the behavior we saw with `pandas.read_csv(chunksize = n)`

As another example, the phone number detection problem could have been done a bit more compactly (as well as more generally to allow for an initial "1-" or "1.") as:

```python
text = "Here's my number: 919-543-3300. They bought 731 bananas. Please call 1.919.554.3800."
re.findall("((1[-.])?(\d{3}[-.]){1,2}\d{4})", text)
```

Question: the above regex would actually match something that is not a valid phone number. What can go wrong?


Groups are also used when we need to reference back to a detected pattern when doing a replacement. This is why they are sometimes referred to as "capturing groups". For example, here we’ll find any numbers and add underscores before and after them:

```python
text = "Here's my number: 919-543-3300. They bought 731 bananas. Please call 919.554.3800."
re.sub("([0-9]+)", "_\\1_", text)
```

Here we’ll remove commas not used as field separators.

```python
text = '"H4NY07011","ACKERMAN, GARY L.","H","$13,242",,,'
re.sub("([^\",]),", "\\1", text)
```

How does that work? Consider that "[^\",]" matches a character that is not a quote and not a comma. The regex is such a character followed by a comma, with the matched character saved in `\\1` because of the grouping operator.

Groups can also be given names, instead of having to refer to them by their numbers, but we will not demonstrate this here.

> **Challenge**: Suppose a text string has dates in the form "Aug-3", "May-9", etc. and I want them in the form "3 Aug", "9 May", etc. How would I do this regex?

Finally, let's consider where a match ends when there is ambiguity.

As a simple example consider that if we try this search, we match as many digits as possible, rather than returning the first "9" as satisfying the request for "one or more" digits.

```python
text = "See the 998 balloons."
re.findall("\d+", text)
```

That behavior is called *greedy* matching, and it's the default. That example also shows why it
is the default. What would happen if it were not the default?

However, sometimes greedy matching doesn't get us what we want.

Consider this attempt to remove multiple html tags from a string.

```python
text = "Do an internship <b> in place </b> of <b> one </b> course."
re.sub("<.*>", "", text)
```

Notice what happens because of greedy matching.

One way to avoid greedy matching is to use a `?` after the repetition specifier.


```python
re.sub("<.*?>", "", text)
```

However, that syntax is a bit frustrating because `?` is also used to indicate
0 or 1 repetitions, making the regex a bit hard to read/understand.

> **Challenge**: Suppose I want to strip out HTML tags but without using the `?` to avoid
greedy matching. How can I be more careful in constructing my regex?


## Special characters in Python

Recall that when characters are used for special purposes, we need to
'escape' them if we want them interpreted as the actual (*literal*) character. In what
follows, I show this in Python, but similar manipulations are sometimes
needed in the shell and in R.

This can get particularly confusing in Python as the backslash is also used
to input special characters such as newline (`\n`) or tab (`\t`).

Here are some examples of using special characters.


```python
tmp = "Harry said, \"Hi\""
print(tmp)   # prints out without a newline -- this is hard to show in rendered doc
tmp = "Harry said, \"Hi\".\n"
print(tmp)      # prints out with the newline -- hard to show in rendered doc

tmp = ["azar", "foo", "hello\tthere\n"]
print(tmp[2])
re.search("[\tZ]", tmp[2])   ## search for a tab or a 'Z'
```

Here are some examples of using various special characters in regex syntax.

```python
## Search for characters that are not 'z'
## (using ^ as regular expression syntax)
re.search("[^z]", "zero")
## Use list comprehension to show results for various input strings:
[print(st + ":\t", re.search("[^z]", st))
    for st in ["a^2", "93", "zzz", "zit", "azar"]]

## Search for either a '^' (as a regular character) or a 'z':
[print(st + ":\t", re.search("[\^z]", st))
    for st in ["a^2", "93", "zzz", "zit", "azar"]]

## Search for exactly three characters
## (using . as regular expression syntax)
[print(st + ":\t", re.search("^.{3}$", st))
    for st in ["abc", "1234", "def"]]

## Search for a period (as a regular character)
[print(st + ":\t", re.search("\.", st)) for st in ["3.9", "27", "4.2"]]
```

> **Challenge**
> Explain why we use a single backslash to get a newline and double backslash to write out a Windows path in the examples here:

```python
## Suppose we want to use a \ in our string:
print("hello\nagain")
print("hello\\nagain")

print("My Windows path is: C:\\Users\\nadal.")
```

Another way to achieve this effect if your string does not contain any special characters is to prefix your string literal with an r for "raw":

```python
print(r"My Windows path is: C:\Users\nadal.")
```


Advanced note: Searching for an actual backslash gets even more
complicated (lookup [backslash plague](https://docs.python.org/3/howto/regex.html#the-backslash-plague) or baskslash hell), because we need to pass two backslashes as the regular expression, so that a literal backslash is searched for. However, to pass two backslashes, we need to escape each of them with a backslash so Python doesn't treat each backslash as part of a special character. So that's four backslashes to search for a single backslash! Yikes. One rule of
thumb is just to keep entering backslashes until things work!

```python
## Search for an actual backslash
tmp = "something \ other\n"
print(tmp)  # notice the escaping of the literal backslash

re.search("\\\\", tmp)
try:
    re.search("\\", tmp)
except Exception as error:
    print(error)
```

Again here you can use "raw" strings, at the price of losing the ability to use any special characters:

```python
## Search for an actual backslash
re.search(r"\\", tmp)
```

This tells python to treat this sting literal without any escaping, but does this does not apply to the regex engine (or else we would have used a single backslash). So yes. This can be quite confusing.

> **Warning**
> Be careful when cutting and pasting from documents that are not text
> files as you may paste in something that looks like a single or double
> quote, but which R cannot interpret as a quote because it's some other
> ASCII quote character. If you paste in a " from PDF, it will not be
> interpreted as a standard R double quote mark.

Similar things come up in the shell and in R, but in the shell you
often don't need as many backslashes. E.g. you could do this to look for a
literal backslash character.

```bash
#| eval: false
echo "hello" > file.txt
echo "with a \ there" >> file.txt
grep '\\' file.txt

## Or without regular expressions
grep -F "\" file.txt
```

---

[← Overview](01-overview.md) · [Up: contents](index.md) · [2. Interacting with the operating system and external code and configuring Python →](03-2-interacting-with-the-operating-system-and-external-code-an.md)

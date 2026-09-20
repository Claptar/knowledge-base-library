---
title: "40. Data Storage, Formats, and I/O"
course: "Berkeley Stat 243 Fall 2024"
chapter: 40
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 40. Data Storage, Formats, and I/O

## What this covers

This chapter follows a dataset from wherever it lives — a file on disk, a web page, a REST API — into
a running Python program and back out again. It answers four practical questions that come up before
any statistical analysis can start: how are the bytes in a file turned into characters or numbers;
which file format should you choose, and why; how do you get data that lives on the web rather than on
your own machine; and once the data is in memory, what structure should hold it. It assumes basic
Python (opening files, list comprehensions, dictionaries) and enough of the UNIX shell to run a command
and read its output.

## Text files and binary files

Every file is, underneath, a sequence of bits — 0s and 1s, grouped into bytes of 8 bits each. Files
split into two broad kinds depending on how those bits are meant to be read.

A **text file** is one in which the bits encode individual characters, one after another — including
the digit characters, so a text file can hold numbers simply by writing out their digits. CSV, XML,
HTML, and JSON files are all text files. A text file may be plain ASCII, where 128 characters fit in
one byte (7 of the 8 bits are meaningful; the 8th is spare) — the upper- and lower-case English
letters, the ten digits, punctuation, and a few control characters, i.e. what is on a US keyboard — or
it may use a richer encoding such as UTF-8, where a character costs between 1 and 4 bytes. (Encodings
get a full treatment later in this chapter; for now, know that they exist and that they set how many
bytes a character costs.)

You can build a text file by hand, byte by byte, to see this concretely. The letter "M" is `01001101`
in ASCII, conventionally regrouped into hex as `4d` (`0100` = 4, `1101` = d); a newline is `0a`. Writing
the raw bytes `4d 6f 6d 0a` to a file and then opening it as text reads back as `"Mom\n"`:

```python
hexvals = b'\x4d\x6f\x6d\x0a'          # "Mom\n" in ASCII, as hex bytes
with open('tmp.txt', 'wb') as textfile:
    textfile.write(hexvals)

with open('tmp.txt', 'r') as textfile:
    print(textfile.readlines())        # ['Mom\n']
```

A **binary file**, by contrast, encodes information in a format specific to whatever program wrote
it — not one byte per character. Binary files are not human-readable, but they can be more compact and
faster to work with, in particular because they allow *random access* (jumping straight to the byte you
want) rather than forcing sequential reading from the start. netCDF files, Python pickle files, R's
`.Rda` files, and compiled code are all binary. A number in a binary file is typically stored in 8
bytes, in a representation that has nothing to do with its digit characters.

## A survey of common file formats

1.  **Flat/delimited text files.** One record per row, one field per column, separated either by a
    fixed character width (*fixed-width format*) or by a delimiter — commonly a tab, comma, space, or
    pipe (`|`). `.txt` and `.csv` are the usual extensions. Metadata (what the columns mean) is
    typically kept in a separate file, not in the CSV itself. A recurring nuisance: if a value
    legitimately contains the delimiter, CSV handles this by quoting the field, which is awkward to
    parse from the shell but is handled correctly by `pandas.read_table`. Another recurring nuisance is
    line endings: Windows terminates a line with both a carriage return and a newline (`\r\n`); UNIX
    uses only `\n`. A stray `^M` at the end of every line is the symptom; `dos2unix`/`fromdos` and
    `unix2dos`/`todos` are the fix in each direction.
2.  **One-item-per-line text**, with no columnar structure — common for free text and some
    bioinformatics data.
3.  **Self-describing interchange formats**, chiefly XML and JSON, where the metadata travels inside
    the file itself rather than in a companion document. Covered in depth later in this chapter.
4.  **HTML**, when the "file" is really a web page you are scraping rather than a dataset someone
    handed you. Also covered later.
5.  **netCDF (`.nc`) and the related HDF5** — the standard formats for gridded scientific data (for
    example, a variable indexed by latitude, longitude, and time), efficient to store and carrying
    their own metadata about each dimension. The `netCDF4` package reads these in Python.
6.  **Other statistical packages' native formats** — Stata, SPSS, SAS — read via `pandas.read_stata`,
    `read_spss`, `read_sas`.
7.  **Excel.** Pandas can read `.xlsx` directly (`read_excel`), but it is generally better to export to
    CSV first and pass that around instead, for four reasons: Excel is proprietary and not everyone has
    it; it silently caps the number of rows; it cannot be manipulated with ordinary UNIX text tools the
    way CSV can; and an Excel workbook often carries more than one sheet, plus charts and macros, so it
    is not really a data format so much as an application file.
8.  **Databases** (SQLite, DuckDB, PostgreSQL, MySQL, Oracle) — queried with SQL, with the result
    handed back to Python. Covered properly in a later unit on large datasets.

### CSV versus a columnar format: Parquet

CSV's virtues are that it is simple, human-readable, and can be processed line by line with ordinary
shell tools. Its cost is structural: storage is **by row**, so a single row mixes together fields of
different types; every comma and newline takes up space of its own; and finding a particular row means
scanning through the file counting newlines — there is no way to jump to row 10 without reading rows
1–9 first.

**Parquet** stores data **by column** instead (in chunks of columns). This suits how tabular data is
actually shaped — a given column is all one type, and often has many repeated values — so a column
compresses well, and a query that only needs a few columns can skip reading the rest. On a real example
(US airline data), the CSV file was 51 MB and the same data as Parquet was 8 MB:

```python
import time
t0 = time.time()
data_from_csv = pd.read_csv('../data/airline.csv')
print(time.time() - t0)

data_from_csv.to_parquet('../data/airline.parquet')
t0 = time.time()
data_from_parquet = pd.read_parquet('../data/airline.parquet')
print(time.time() - t0)
```

Parquet data is also commonly split across multiple files rather than kept as one.

## Reading text data into Python

`pandas.read_table` and `read_csv` are the workhorses for delimited files; `read_fwf` reads fixed-width
files. The key arguments are the delimiter (`sep`) and whether the file has a header row.

The hardest part in practice is getting Pandas to infer the right column types. It will guess, but
telling it explicitly with `dtype` is both safer and faster:

```python
dat = pd.read_table('RTADataSub.csv', sep=',', header=None)
dat.loc[:, 1].unique()          # reveals an 'x' used to mean "missing"
dat2 = pd.read_table('RTADataSub.csv', sep=',', header=None, na_values='x')
```

```python
dat = pd.read_table('hivSequ.csv', sep=',', header=0,
                     dtype={'PatientID': int, 'Resp': int, 'PR Seq': str,
                            'RT Seq': str, 'VL-t0': float, 'CD4-t0': int})
```

`usecols` skips columns you don't need. It is worth looking at a file with `less` or an editor before
reading it in — that is how the stray `'x'` above would have been caught in advance, rather than
discovered as a bug later.

If the fields are not cleanly delimited — a ragged file, or one where a field's width but not its
separator is fixed — you can read each line as a string and slice it by character position, once you
know the field boundaries from the file's metadata:

```python
with open('precip.txt', 'r') as file:
    lines = file.readlines()
year = [int(line[17:21]) for line in lines]
month = [int(line[21:23]) for line in lines]
```

`precip.txt` is actually a fixed-width file, so `pd.read_fwf(..., widths=[...])` is the more direct
tool for it.

!!! tip "Tip"
    `with open(...) as file:` is the standard idiom for opening a file — it closes the file
    automatically once the block finishes, even if an exception is raised inside it.

### Connections and streaming

Python can read from more than a plain file on disk — from a *connection*, which might be a gzip- or
zip-compressed archive, the output of a shell command, or a URL:

```python
import gzip, zipfile, subprocess, io

with gzip.open('dat.csv.gz', 'r') as file:
    lines = file.readlines()

with zipfile.ZipFile('dat.zip', 'r') as archive:
    with archive.open('data.txt', 'r') as file:
        lines = file.readlines()

output = subprocess.check_output("ls -al", shell=True)      # bytes
with io.BytesIO(output) as stream:
    content = stream.readlines()

df = pd.read_csv("https://download.bls.gov/pub/time.series/cu/cu.item", sep="\t")
```

If a file is too large to hold comfortably in memory, read it in **chunks**, process and reduce each
chunk, and discard it — variously called online processing, streaming, or chunking:

```python
with pd.read_csv('RTADataSub.csv', chunksize=50) as reader:
    for chunk in reader:
        print(f'Read {len(chunk)} rows.')      # do the real work here
```

You can also treat an in-memory string as if it were a file, via `io.StringIO` — useful once you have
already read raw text and want to hand it to a parser that expects a file:

```python
stringIOtext = io.StringIO(text)
df = pd.read_fwf(stringIOtext, header=None, widths=[3, 8, 4, 2, 4, 2])
```

### File paths and reproducibility

Do not hard-code an absolute path — it will not exist on anyone else's machine, including your own
after you move the project. Use a path relative to the code file or to a project root, with UNIX-style
forward slashes (they work fine on Windows too, whereas backslashes do not work on Mac or Linux), and
build paths with `os.path.join` so the separator is correct for whoever runs the code:

```python
dat = pd.read_csv(os.path.join('..', 'data', 'cpds.csv'))     # portable
```

### Reading quickly: Arrow, Polars, and friends

Apache Arrow (used from Python via PyArrow) stores data by column in memory, laid out so any single
value can be looked up without touching the rest of the column, and it reads from disk lazily — only as
much as is actually needed — rather than loading an entire dataset up front. `polars` is a
Pandas-alternative built around similar ideas, and is often substantially faster:

```python
import polars
dat = pd.read_csv('../data/airline.csv')
dat2 = polars.read_csv('../data/airline.csv', null_values=['NA'])
```

Dask and `numpy.load(..., mmap_mode=...)` are two other routes to working with data larger than memory
without reading all of it in at once.

## Writing output from Python

Writing mirrors reading. `open(path, 'w')` plus `writelines`/`write` handles plain text; Pandas has
`DataFrame.to_csv` and `DataFrame.to_parquet`. `json.dump` serializes a dictionary or list to JSON —
one reason to do this is to hand the object to a different program entirely. `pickle.dump`/`pickle.load`
serialize an arbitrary Python object to a binary file; unlike some binary formats, pickle files are
platform-independent, so they travel between operating systems.

### Formatting output

Python's [format-spec mini-language](https://docs.python.org/3/library/string.html#formatstrings)
controls width, alignment, and precision:

```python
'{:>10}'.format(3.5)          # right-aligned in a 10-character field
'{:.10f}'.format(1/3)         # 10 decimal places
'{:15.10f}'.format(1/3)       # 15 characters wide, 10 decimal places
```

f-strings interpolate variables directly, and the older `%`-style formatting still works:

```python
print(f"Let's add {val1} and {val2}.")
print("Let's add the %s numbers %.5f and %15.7f." % ('floating point', num1, 32 + 1/7))
```

`round()` is available too, but controlling the *display* format directly, as above, is usually the
better tool — `round` changes the value itself, not just how it is printed.

## File and string encodings

An ASCII file has a fixed cost of one byte per character, but ASCII only covers 128 symbols — a US
keyboard's worth. Once text needs an accented letter, a currency symbol, or a character from a
non-Latin script, something richer is needed, and that raises the same question a binary format raises:
what do these bytes mean?

**Unicode** solves half the problem: it assigns every character (more than 110,000 of them, across
about 100 scripts) a unique integer, its *code point*. `ord()` returns it:

```python
ord('ñ')            # 241
hex(ord('ñ'))       # '0xf1'
```

**UTF-8** solves the other half: it is the encoding that turns a Unicode code point into actual bytes,
in memory or on disk. It is a *variable-length* encoding — 1 to 4 bytes per character — built so that
plain ASCII characters still cost exactly one byte:

```python
bytes('ñ', 'utf-8')     # b'\xc3\xb1'  — two bytes for ñ
bytes('÷', 'utf-8')     # two bytes for ÷, too
```

The cleverness is in exactly how those extra bytes are laid out: the bit pattern is chosen so that the
bytes making up a one-byte character can never appear as part of the encoding of a two-, three-, or
four-byte character (and likewise up the chain), and the leading bit(s) of the first byte alone tell a
reader how many bytes the character occupies — a leading `0` means one byte (plain ASCII); a leading `1`
means look further to find out whether it is two, three, or four bytes. That is what lets a program
read a file one character at a time without knowing in advance where each character starts and stops.

**Latin-1** (ISO 8859-1) is a narrower, one-byte-per-character alternative that is sometimes seen
instead of UTF-8: it covers ASCII plus 191 characters used in European languages (mostly accented
letters), so `ñ` and `÷` above cost one byte each in Latin-1 rather than two in UTF-8. You can watch the
difference directly with Python's `encode`:

```python
text = 'Peña 3÷2'
text.encode('utf-8')     # two extra bytes, one per accented/special character
text.encode('latin1')    # one byte per character, including ñ and ÷
text.encode('ascii')     # raises — ASCII has no code point for ñ or ÷ at all
```

This is also the source of a very common error: opening a file assuming the wrong encoding. Python's
default encoding is UTF-8; if a file was actually written in Latin-1 and you open it as UTF-8 (or vice
versa), you get a decoding error partway through — often deep into the file, at whatever line contains
the first non-ASCII byte, since every plain ASCII byte is valid in both encodings and so causes no
trouble until then:

```python
with open('file_nonascii.txt', 'r') as textfile:      # raises a decode error
    lines = textfile.readlines()

with open('file_nonascii.txt', 'r', encoding='latin1') as textfile:   # works
    lines = textfile.readlines()
```

The UNIX utility `file` (e.g. `file tmp.txt`) can help identify a file's encoding, and `iconv` (from the
shell) or `.encode()`/`.decode()` (in Python) convert between encodings once you know what you have.
Python (like R and Julia) also allows Unicode characters, including things like `σ`, directly in
variable names — legal, if not always advisable.

## Working with information on the web

Not all data arrives as a file someone hands you — often you have to fetch it, either by downloading a
page and parsing it (**webscraping**) or by asking a web service for it directly (an **API**).

### HTTP, briefly

HTTP (hypertext transfer protocol) is how a client (your laptop) and a server (the website) talk: the
client sends a *request*, the server sends a *response* carrying a status code and, usually, content —
HTML, XML, JSON, or raw bytes. A normal page visit in a browser is an HTTP **GET** request. Any URL with
a `?` followed by `key=value` pairs joined by `&` is a GET request carrying parameters — you are
already using an API every time you see one in a URL bar.

### Reading HTML

Before writing any code, it helps to look at a page's raw HTML — in a browser's "View Page Source", or
by downloading the page and opening it in an editor (bearing in mind that some pages, driven heavily by
JavaScript, don't show much useful content this way). The `BeautifulSoup` package (`bs4`) parses HTML
text into a navigable tree of elements:

```python
import requests
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': 'stat243_educational_bot/0.1 (you@berkeley.edu)'}
response = requests.get(URL, headers=headers)
soup = bs(response.content, 'html.parser')

html_tables = soup.find_all('table')
pd_tables = [pd.read_html(io.StringIO(str(tbl)))[0] for tbl in html_tables]
```

`find_all` searches by tag (`'a'`) or by attribute (`href=True`), and `.get('href')` retrieves an
attribute's value — a common use is pulling out every hyperlink on a page. `.get_text()` retrieves an
element's text content, e.g. to pull every headline off a news page. For more targeted extraction,
`soup.select(...)` takes a [CSS selector](https://www.w3schools.com/cssref/css_selectors.asp)
(`"tr th"`, `"th > a"`), and `lxml`'s **XPath** language does the same job with more expressive syntax
(`doc.xpath('//a[@href]')`) — XPath also works directly on XML, below.

The lesson generalizes past HTML specifically: before writing much code by hand to parse a format,
check whether a well-tested package already exists for it.

### XML, JSON, and YAML

All three store the same basic shape of information — key-value pairs, arrays of unnamed elements, and
hierarchical nesting of one inside another — differing mainly in verbosity and typical use.

**XML** is a markup language, structurally similar to HTML, in which elements ("nodes", because of the
tree structure) are identified by tags and can carry attributes:

```xml
<catalog>
   <book id="bk101">
      <author>Gambardella, Matthew</author>
      <title>XML Developer's Guide</title>
      <price>44.95</price>
   </book>
</catalog>
```

It is *self-describing* — the tags carry the metadata, so no separate schema file is required to make
sense of it — and it underlies formats as different as Microsoft Office documents and Google Earth's
KML. `xmltodict` turns an XML document directly into nested Python dicts and lists; `lxml.etree` plus
XPath is the better tool once the structure gets any deeper, since it lets you query for exactly the
nodes you want instead of walking the nesting by hand:

```python
from lxml import etree
doc = etree.fromstring(content)
loans = doc.xpath("//loan")
[loan.xpath("location/country/text()") for loan in loans]
```

**JSON** carries the same kind of information more compactly — braces for a set of key-value pairs,
square brackets for an unnamed array, and native `null`/boolean/number/string types:

```json
{"firstName": "John", "age": 25,
 "address": {"city": "New York", "state": "NY"},
 "phoneNumbers": [{"type": "home", "number": "212 555-1234"}],
 "spouse": null}
```

Python's `json` module reads this straight into the equivalent nested dicts/lists (`json.loads`). One
real limitation: JSON has no representation for a missing value or for infinity — R's `NA` or Python's
`NaN` do not survive a round trip through JSON without a convention layered on top.

**YAML** is the format of choice for configuration files (a GitHub Actions workflow, for example): it
uses indentation for nesting, the way Python does, and mostly dispenses with quotation marks, which
makes it easy to read but correspondingly easy to break by getting the indentation wrong.

```python
import yaml
with open("book.yml") as stream:
    config = yaml.safe_load(stream)     # safe_load refuses to execute embedded code
```

(One quirk worth knowing: an unquoted `on` in a YAML file is parsed as the boolean `True` by the PyYAML
package — a genuine trap for anyone writing a GitHub Actions workflow, which uses `on:` to name its
trigger.)

### REST APIs

Ideally a web service documents an API for retrieving its data programmatically, rather than making you
scrape a page meant for humans. **REST** is the dominant style: it works entirely over ordinary HTTP,
addressing *resources* by URL and returning a result in a standard format (usually JSON) rather than an
HTML page meant to be rendered.

A REST request is usually a base URL (an *endpoint*) plus a query string: it starts with `?`, has one
or more `Parameter=Argument` pairs joined by `&`, and uses `+` for a literal space. Constructing one
programmatically, rather than pasting a URL together by hand, keeps the arguments visible and makes the
request reusable:

```python
baseURL = "https://api.worldbank.org/V2/country"
args = {'incomeLevel': 'MIC', 'format': 'json', 'per_page': 1000}
url = baseURL + '?' + '&'.join('='.join([k, str(v)]) for k, v in args.items())
response = requests.get(url)
data = json.loads(response.content)
```

(`requests.get(baseURL, params=args)` does the same URL-building for you.) Watch for **pagination** —
a request for a large result may come back truncated at some default page size, with the rest available
only via a further request — and for **authentication**, which ranges from sending an access token with
the request to a full browser-based login flow (as with a Google account authorizing access to Drive).

### Deconstructing an undocumented API

Not every service documents, or has, an API. One route is to watch what your own browser does:
requesting a download from a JavaScript-heavy page, then inspecting the actual HTTP request the browser
sent (in the browser's Developer Tools, under "Network"), reveals the URL to hit directly, query
parameters and all. The result may need further unpacking — a real example returns a zip file, so
getting to the actual CSV inside requires unzipping it in memory first:

```python
response = requests.get(url)
with io.BytesIO(response.content) as stream:
    with zipfile.ZipFile(stream, 'r') as archive:
        with archive.open(archive.filelist[0].filename, 'r') as file:
            dat = pd.read_csv(file)
```

This buys two things: a reproducible pipeline you (or your future self) can rerun, and the ability to
automate downloading many such files at once. It is also fragile — the query only works as long as the
site's own internal structure does not change.

### POST requests and packaged APIs

A GET request carrying a lot of information can run into URL length limits (many servers reject
anything past about 2048 characters); an HTTP **POST** request instead carries the data in the request
body, and is also what a web form submission normally uses:

```python
headers = {"Authorization": f"token {ghtoken}", "Accept": "application/vnd.github+json"}
issue = {"title": "This is an example issue", "body": "Filed via the API."}
response = requests.post(f"https://api.github.com/repos/{owner}/{repo}/issues",
                          json=issue, headers=headers)
```

For a popular service, someone has often already wrapped the raw HTTP calls in a friendlier package —
`PyGitHub`, for the GitHub API, turns the same task into a few method calls instead of building a
request by hand:

```python
from github import Github
g = Github(ghtoken)
repo = g.get_repo("owner/repo")
issue = repo.create_issue(title="Test issue", body="Filed via PyGitHub.")
```

`requests` also supports `PUT` and `DELETE`, and some services track a session via cookies that must be
carried from one request to the next.

### Should you, and may you, scrape?

Two questions before writing any scraping code. **Should you?** If the data is available as a direct
download or through a documented API, prefer that — scraping a page meant for human eyes is a fallback,
not a first choice. **May you?** Check the site's Terms of Service and its `robots.txt` file, which
states what an automated crawler is and is not permitted to do, and whether it must wait between
requests; for anything at real scale, consider contacting the site owner directly.

In practice: run an automated request *once*, cache the result, and develop your parsing code against
the saved copy rather than re-requesting the page every time you rerun your script; if you must make
many requests, put a delay between them; and check the API's documentation for any stated rate limit.

### Pages that change under you: dynamic content

Some pages build their content dynamically with JavaScript after the initial HTML loads, so simply
downloading the HTML misses what a human visitor would actually see. `selenium` drives an actual browser
under program control, so it sees the page the way a person does; `scrapy` combined with `splash` is
another route to the same problem.

## Choosing a data structure

Once data is in memory, the structure you store it in shapes three things at once: how much memory it
takes, how quickly you can retrieve or update a piece of it, and how much copying is needed to add or
remove an element — so the choice should be driven by what you plan to *do* with the data, not just by
what shape it started in.

Python and R both lean heavily on **dataframes**, **arrays** (`numpy` arrays in Python), and
**dictionaries** (named vectors, named lists, or environments, in R) for everyday statistical work. In
R, once data stop being rectangular, it is common to fall back on deeply nested lists.

Other structures come up less often in statistical code, but the ideas behind them are worth having:

- A **set** holds elements with no duplicates, exactly as in mathematics.
- A **linked list** stores its elements as separate nodes, each holding a value and a pointer to the
  next node (a doubly-linked list also points back to the previous one). Reaching a given element means
  following pointers from the start — there is no direct index — but *inserting* a new element is
  cheap: only the two pointers on either side of the insertion point change, and nothing else moves. An
  **array**, in contrast, gives direct indexed access to any element, but inserting one in the middle
  means shifting every element after it.

<figure>
<svg viewBox="0 0 460 260" role="img" aria-label="An array stores values in contiguous indexed slots, so inserting one shifts every later value; a linked list stores values in nodes chained by pointers, so inserting one only redirects two pointers.">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
    <marker id="arrowAccent" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#d97706"/>
    </marker>
  </defs>

  <text x="10" y="16" font-size="12" fill="currentColor">Array: fixed slots, reached directly by index</text>
  <g font-size="12" fill="currentColor" stroke="currentColor">
    <rect x="20" y="26" width="50" height="34" fill="none"/>
    <rect x="80" y="26" width="50" height="34" fill="none"/>
    <rect x="140" y="26" width="50" height="34" fill="none" stroke-dasharray="4 3"/>
    <rect x="200" y="26" width="50" height="34" fill="none"/>
    <rect x="260" y="26" width="50" height="34" fill="none"/>
    <text x="45" y="47" text-anchor="middle" stroke="none">12</text>
    <text x="105" y="47" text-anchor="middle" stroke="none">7</text>
    <text x="165" y="47" text-anchor="middle" stroke="none">new</text>
    <text x="225" y="47" text-anchor="middle" stroke="none">4</text>
    <text x="285" y="47" text-anchor="middle" stroke="none">9</text>
    <text x="45" y="74" text-anchor="middle" font-size="11" stroke="none">0</text>
    <text x="105" y="74" text-anchor="middle" font-size="11" stroke="none">1</text>
    <text x="165" y="74" text-anchor="middle" font-size="11" stroke="none">2</text>
    <text x="225" y="74" text-anchor="middle" font-size="11" stroke="none">3</text>
    <text x="285" y="74" text-anchor="middle" font-size="11" stroke="none">4</text>
  </g>
  <g stroke="#d97706" fill="none" stroke-width="1.5">
    <path d="M200,20 h50" marker-end="url(#arrowAccent)"/>
    <path d="M260,20 h50" marker-end="url(#arrowAccent)"/>
  </g>
  <text x="330" y="16" font-size="11" fill="#d97706">every later slot shifts</text>

  <text x="10" y="130" font-size="12" fill="currentColor">Linked list: nodes anywhere in memory, chained by pointers</text>
  <g font-size="12" fill="currentColor" stroke="currentColor">
    <rect x="20" y="145" width="70" height="34" fill="none"/>
    <line x1="65" y1="145" x2="65" y2="179"/>
    <text x="42" y="166" text-anchor="middle" stroke="none">12</text>
    <text x="77" y="166" text-anchor="middle" stroke="none" font-size="10">next</text>

    <rect x="140" y="145" width="70" height="34" fill="none"/>
    <line x1="185" y1="145" x2="185" y2="179"/>
    <text x="162" y="166" text-anchor="middle" stroke="none">7</text>
    <text x="197" y="166" text-anchor="middle" stroke="none" font-size="10">next</text>

    <rect x="260" y="145" width="70" height="34" fill="none"/>
    <line x1="305" y1="145" x2="305" y2="179"/>
    <text x="282" y="166" text-anchor="middle" stroke="none">4</text>
    <text x="317" y="166" text-anchor="middle" stroke="none" font-size="10">next</text>

    <rect x="380" y="145" width="60" height="34" fill="none"/>
    <text x="410" y="166" text-anchor="middle" stroke="none">9</text>
  </g>
  <g fill="none" stroke="currentColor" stroke-width="1.5">
    <path d="M90,162 h50" marker-end="url(#arrow)"/>
    <path d="M210,162 h50" marker-end="url(#arrow)"/>
    <path d="M330,162 h50" marker-end="url(#arrow)"/>
  </g>

  <g font-size="12" fill="currentColor" stroke="currentColor" stroke-dasharray="4 3">
    <rect x="140" y="210" width="70" height="34" fill="none"/>
    <line x1="185" y1="210" x2="185" y2="244"/>
    <text x="162" y="231" text-anchor="middle" stroke="none">new</text>
    <text x="197" y="231" text-anchor="middle" stroke="none" font-size="10">next</text>
  </g>
  <g fill="none" stroke="#d97706" stroke-width="1.5" stroke-dasharray="4 3">
    <path d="M90,179 C115,200 115,215 138,222" marker-end="url(#arrowAccent)"/>
    <path d="M210,227 C240,215 250,190 258,168" marker-end="url(#arrowAccent)"/>
  </g>
  <text x="230" y="256" font-size="11" fill="#d97706" text-anchor="middle">only these two pointers change</text>
</svg>
<figcaption>Inserting a value into an array shifts every element after it; inserting a node into a
linked list only redirects the two pointers on either side of the insertion point.</figcaption>
</figure>

- A **tree** and a **graph** are both collections of nodes joined by links (edges). A tree's links point
  from parent to child, with no cycles; a graph's links need not be directional and can form cycles.
- A **stack** only exposes its most-recently-added element — you can `push` a new one on top or `pop`
  the top one off ("last in, first out"), like a stack of lunch trays. Nested function calls behave
  exactly this way, which is why the memory used for pending calls is called "the stack".
- A **queue** is "first in, first out", like a line at a checkout counter.

Trees and graphs are genuinely common in statistical and machine-learning work; stacks and queues
mostly appear inside the tools you use rather than in code you write directly, likely because
statistical data is usually either rectangular (dataframe-shaped) or array-shaped to begin with.

Three related ideas, picked up again in more depth later in the course: a **type** describes how a
piece of information is stored and what operations make sense on it (booleans, integers, floating-point
numbers, characters, and pointers/references are the usual "primitive" types); a **pointer** is a
reference to another location in memory, used to avoid copying data unnecessarily; and **hashing** maps
a key directly to an address via a hash function, so that looking up the value for a key takes constant
time instead of the cost of scanning every key in turn (an $O(n)$ operation).

## Sources

All of this comes from the "Data Technologies" unit of UC Berkeley's STAT 243, taught across several
years with the same structure and only a presentation-language change (R through fall 2021, Python from
fall 2024 on). This chapter follows the clearest and most current version, **fall-2025**, and cites it
throughout unless noted:

- Text vs. binary files, the common-file-types survey, and CSV vs. Parquet —
  `berkeley-stat243/fall-2025/units/unit2-dataTech.qmd`, section "1. Data storage and file formats on a
  computer" (`fall-2025/units/unit2-dataTech/02-1-data-storage-and-file-formats-on-a-computer.md`). The
  same material, essentially unchanged, appears in `fall-2024`
  (`units/unit2-dataTech/01-1-data-storage-and-file-formats-on-a-computer.md`), in `fall-2026`'s merged
  bash/data-technologies unit (`units/unit2-bash/04-5-data-storage-and-file-formats-on-a-computer.md`),
  and, translated to R, in `stat243-fall-2021`
  (`units/unit2-dataTech/01-1-data-storage-and-file-formats-on-a-computer.md` — that file is a model's
  reconstruction of a PDF with no text layer, per its own banner, so it is cited here only to confirm the
  material is stable across editions, not as a source of specific wording).
- Reading text data into Python (Pandas, connections/streaming, file paths, Arrow/Polars) —
  `fall-2025/units/unit2-dataTech/03-2-reading-data-from-text-files-into-python.md`, section 2. The R
  equivalents (`read.table`, connections via `pipe`/`url`/`curl`, the `readr` package) appear in
  `stat243-fall-2021/units/unit2-dataTech/02-2-reading-data-from-text-files-into-r.md`.
- Writing output and string formatting —
  `fall-2025/units/unit2-dataTech/04-3-output-from-python.md`, section 3 (R equivalent, using
  `cat`/`sprintf`: `stat243-fall-2021/units/unit2-dataTech/03-3-output-from-r.md`).
- HTML/XML/JSON/YAML, REST APIs, webscraping ethics, POST requests, and dynamic pages —
  `fall-2025/units/unit2-dataTech/05-4-working-with-information-on-the-web.md`, section 4 (the
  equivalent `fall-2024` file titles this section "Webscraping and working with HTML, XML, JSON, and
  YAML"; the R/`rvest` version of the same material is
  `stat243-fall-2021/units/unit2-dataTech/04-4-webscraping-and-working-with-html-xml-and-json.md`).
- File and string encodings — `fall-2025/units/unit2-dataTech/06-5-file-and-string-encodings.md`,
  section 5 (R equivalent, using `iconv` in place of `.encode`/`.decode`:
  `stat243-fall-2021/units/unit2-dataTech/05-5-file-and-string-encodings.md`).
- Data structures — `fall-2025/units/unit2-dataTech/07-6-data-structures.md`, section 6.

Also supplied for this chapter, but not drawn on: `fall-2026/units/unit2-bash/01-1-shell-basics.md`,
`02-3-bash-shell-examples.md`, `03-4-bash-shell-challenges.md`, and `05-6-regular-expressions.md`. These
sit in the same file (`unit2-bash.qmd`) as fall-2026's data-storage section because that year folds
shell, regular expressions, and data technologies into one combined unit, but their content is the UNIX
shell and regular expressions, which belongs to a different chapter, not this one.

The lecture points to several texts it does not reproduce: Adler; Deb Nolan and Duncan Temple Lang's
*XML and Web Technologies for Data Sciences with R*; Paul Murrell's *Introduction to Data Technologies*;
and an SCF tutorial on working with large datasets in SQL, R, and Python
(<https://computing.stat.berkeley.edu/tutorial-databases/>) — all listed in
`fall-2025/units/unit2-dataTech/01-overview.md`, which also mentions four optional 2020 recorded videos
(on text files/ASCII, encodings/UTF-8, HTML, and XML/JSON) that are not part of the supplied material.
Neither the referenced texts nor the videos are drawn on beyond noting that the lecture pointed to them.

---

[← 39. Good Practices for Graphics](39-good-practices-for-graphics.md) · [Contents](index.md) · [41. Bash Shell Basics and Pipelines →](41-bash-shell-basics-and-pipelines.md)

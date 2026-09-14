# Courses held in GitHub organisations and repositories

**Verified:** 2026-09-13.

A large share of modern course material is a git repository — Quarto or Jekyll sources, notebooks,
problem sets with solutions on a branch. The rendered website is a build artefact; the repo is the
material, and it carries history the site throws away.

## Where the material actually is

Work through the API rather than the web UI — it is faster, paginates properly, and reports the
licence and default branch in the same call.

```bash
gh api "orgs/<org>/repos?per_page=100" \
  --jq '.[] | "\(.name)  \(.license.spdx_id // "none")  \(.visibility)  \(.pushed_at[:10])"'

gh api "repos/<org>/<repo>/contents" --jq '.[].name'          # top level
gh api "repos/<org>/<repo>/contents/<path>" --jq '.[].name'   # a directory
gh api "repos/<org>/<repo>/contents/LICENSE" --jq .content | base64 -d   # read it, don't trust the field
```

To take a copy, `git clone --depth 1` into `sources/<slug>/` — gitignored, never committed. Clone
shallow unless the history is the point; a course repo with notebook outputs can be hundreds of MB.

Naming conventions worth guessing before searching:

```
github.com/<university>-<dept><num>/<term>      berkeley-stat243/fall-2024
github.com/<org>/<course>-<term>                berkeley-stat243/stat243-fall-2021
github.com/<instructor>/<course>
```

## What is gated

- **Private repos 404 exactly like non-existent ones.** A 404 from `gh api` means "not visible to
  you", not "not there". Say so rather than concluding the course has no repo.
- **Releases and LFS.** Large PDFs are often attached to a release or stored in Git LFS; a plain
  clone gets a pointer file. Check `gh release list` before concluding a file is missing.
- **A repo can be public while the render is behind a campus login** — worth checking both.

## Licence

**Read the LICENSE file. Do not read the API's `license.spdx_id` field.** GitHub infers that field
from whatever licence file it finds, and on a course site repo that is routinely the licence of the
*website theme* rather than the course content. Check whose name is in the copyright line: if it is
not the instructor or the institution, the licence is the template's and the content is unlicensed.

`none` means no licence file, which means **all rights reserved** — not "free to use". Unlicensed
is the most common state for course repos, and `adapted-private/` is where their adaptations go.

`NOASSERTION` means a licence file exists that GitHub could not classify. Open it.

A repo carrying a real CC0, CC BY or BSD licence is genuinely adaptable and publishable — record
the exact SPDX id and the repo it applies to, because the licence often varies *between years* of
the same course.

## Gotchas

- **The content may not be on the default branch, and this is the one that wastes a session.**
  A site served from `<org>.github.io/<repo>/` is often built from a **`gh-pages` branch** while the
  default branch holds a stub. `git clone --depth 1` takes the default branch and returns almost
  nothing — `statOmics/SGA2020` gives **5 files** on `master` and **229 files, 515 MB** on
  `gh-pages`. Data is sometimes split off again onto its own branches (`data`, `data-rnaseq`).
  **List branches before concluding a repo is empty:**

  ```bash
  gh api "repos/<org>/<repo>" --jq .default_branch
  gh api "repos/<org>/<repo>/branches" --jq '.[].name'
  git clone --depth 1 -b gh-pages https://github.com/<org>/<repo>.git <dest>
  ```

  A repo whose size in the API is large but whose clone is tiny is this, every time — the API
  reports the whole repository, all branches included.
- **Course orgs accumulate junk.** `test-repo`, `sec08`, abandoned scaffolds. Judge by
  `pushed_at` and by whether the repo has content, not by its name.
- **Solutions are often on a separate branch or a private sibling repo.** `gh api
  "repos/<org>/<repo>/branches" --jq '.[].name'` before concluding they were never published.
- **The `.github.io` repo is usually the theme, not the content.** It is the render target.
- **Quarto and Jekyll sources are better than the rendered site** for adaptation: `.qmd` and `.md`
  carry the LaTeX as written, while the HTML carries MathJax output that is painful to convert back.

## Extracting text from syllabus and lecture PDFs

A fetch tool will fail to parse a PDF but saves it to disk, and the path is in the result. `Read`
handles PDFs only where `pdftoppm` is installed (`brew install poppler`); without it, pull the text
out directly:

```bash
python3 - "<saved.pdf>" <<'PY'
import sys, zlib, re
raw = open(sys.argv[1], 'rb').read(); out = []
for m in re.finditer(rb'stream\r?\n(.*?)endstream', raw, re.S):
    try: out.append(zlib.decompress(m.group(1)).decode('latin-1'))
    except Exception: pass
s = "".join(c[1:-1] for c in re.findall(r'\((?:[^()\\]|\\.)*\)', "\n".join(out)))
print(re.sub(r'\s+', ' ', s.replace('\\(', '(').replace('\\)', ')')))
PY
```

It emits text without spaces between words — readable, and good enough to pull a reading list or a
topic list out of. It fails on scanned PDFs, which have no text layer at all; say so rather than
guessing at the contents.

**A syllabus's bibliography is usually the most valuable thing in it** — an expert's judgement about
which papers matter. Harvest it as catalogue entries in its own right; see step 4 of `SKILL.md`.

# UC Berkeley — Statistics, and departments that cross-list with it

**Verified:** 2026-09-13.

Berkeley statistics courses publish through a vanity domain per course, built from a GitHub
organisation per course. Graduate courses cross-listed with another department — Public Health,
Political Science, Mathematics — do **not** use that system and have to be chased separately.

## Where the material actually is

```
https://stat<num>.berkeley.edu/                landing page. Lists semesters. No material.
https://stat<num>.berkeley.edu/<term>/         per-offering page: instructor, topics, links
https://github.com/berkeley-stat<num>/<term>/  THE SOURCE. The site is a render of this.
https://github.com/berkeley-stat<num>/berkeley-stat<num>.github.io   theme only — see Licence
```

`<num>` is lowercase with the letter suffix: `205a`, `230a`, `241b`. `<term>` is `fall-2024`,
`spring-2026`. **Go to the GitHub org first** — it has the history, and occasionally files the
rendered site does not link.

Two department-level indexes, both worth checking before guessing:

- <https://statistics.berkeley.edu/courses/websites> — the authoritative list of which courses have
  a vanity domain. If a course is absent here, the `stat<num>.berkeley.edu` guess will fail DNS.
- <https://classes.berkeley.edu> — per-semester class search. The only reliable way to find out
  whether a course still runs.

A quick existence sweep is cheaper than searching:

```bash
for c in 150 153 205a 243; do
  printf '%-8s %s\n' "$c" "$(curl -sL -o /dev/null -w '%{http_code}' --max-time 10 https://stat$c.berkeley.edu)"
done          # 000 = no such host, so no vanity domain
```

```bash
gh api "orgs/berkeley-stat<num>/repos?per_page=100" \
  --jq '.[] | "\(.name)  \(.license.spdx_id // "none")"'    # 404 = no org
```

## Cross-listed graduate courses — the separate system

A `C` prefix means cross-listed, and the material usually lives with the **other** department or on
the instructor's personal page, not under `stat<num>`:

| Statistics | Also | Where the material is |
| --- | --- | --- |
| `STAT C245C–F` | `PB HLTH C240C–F` | Dudoit's pages under `stat.berkeley.edu/~sandrine/` |
| `STAT C247C` | `PB HLTH C240x` | instructor page; offered in even-numbered years only |
| `STAT C205A/B` | `MATH C218A/B` | has a vanity domain *and* legacy pages under `~aldous/205A` |
| `STAT C239A` | `POL SCI C236A` | **retired** — succeeded by `STAT 256` |

## Instructor pages — the second system, and often the better one

**This is where the material is when the course repo is a scaffold.** Independent of the
`stat<num>` system, and it long predates it. Three shapes, all verified:

```
https://www.stat.berkeley.edu/~<user>/<num>/                 ~aldous/205A, ~aldous/150
https://www.stat.berkeley.edu/~<user>/<term>.<num>/          ~bensonau/s24.150, f21.150
https://www.stat.berkeley.edu/~<user>/resources/<Notes>.pdf  ~aditya/resources/FullNotes201AFall2022.pdf
```

A few faculty use their own subdomain instead — `purdom.stat.berkeley.edu/Syllabi/...`.

**Directory listing is disabled**, so the folder 404s while files inside it fetch fine. Don't
browse; fetch `index.html`, extract every `href` ending in a document extension, and download those:

```bash
curl -sfL "$BASE/index.html" -o idx.html
python3 - idx.html "$BASE" <<'PY' | while read u; do curl -sfLO --output-dir "$DEST" "$u"; done
import re,sys,urllib.parse
h=open(sys.argv[1],encoding='utf-8',errors='replace').read()
for m in re.findall(r'href="([^"]+)"',h,re.I):
    if re.search(r'\.(pdf|tex|ps|zip|ipynb|R|py)$',m,re.I):
        print(urllib.parse.urljoin(sys.argv[2]+'/',m))
PY
```

Worth knowing before writing a course off:

- **An instructor's teaching page is the index you actually want.** `~aditya/styled/index.html`
  lists a decade of courses with links to **complete lecture-note PDFs** — 201A, 210B, 248 — none
  of which are reachable from the corresponding `stat<num>` sites.
- **Old offerings persist for years** after the course stops running, and are frequently the only
  public copy. `~aldous/205A` and `~aldous/205B` carry Sinho Chewi's full scribe notes for both
  halves; the current 205A repo is a scaffold.
- **One instructor may hold many offerings.** `~bensonau/{f21,f22,s23,f23,s24}.150` is five terms
  of Stat 150 with complete problem sets, **including the LaTeX source** — while the official
  Stat 150 repo points at bCourses.
- **The problem sets are often the whole point.** Instructor pages post homework where the LMS
  posts everything; homework without solutions is exactly the right shape for this reader.

Find these by searching the department domain rather than guessing usernames:

```
site:stat.berkeley.edu <course number> lecture notes
```

## What is gated

**bCourses** (Berkeley's Canvas) is the common answer, and it is not reachable. A per-offering page
saying *"uses bCourses this semester"* or a syllabus saying *"lecture notes will be provided on the
class website"* means the material is behind a login. `Stat 150 spring-2026` is exactly this: the
page names the instructor and the topics, and links to `bcourses.berkeley.edu`.

Mark these `Access: unreadable` and name bCourses. Do not go looking for a mirror, and never
reconstruct the notes from the topic list.

## Licence

**Berkeley course material carries no blanket licence**, and the licence varies *per offering* —
the same course can be CC BY one semester and unlicensed the next. Resolve it per repo, never per
course.

**The declaration is a `license.qmd` page inside the repo, not a `LICENSE` file.** GitHub cannot
classify a Quarto page, reports the repo as `NOASSERTION`, and an agent reading the API field
concludes "unlicensed" for material that is in fact **CC BY 4.0**. Verified on 30 cloned repos:
11 are CC BY 4.0, one CC BY-NC 4.0, one CC0, one BSD-3-Clause, the rest nothing.

```bash
find <repo> -maxdepth 2 -iname 'licen[sc]e*' -not -path '*/.git/*' -exec cat {} \;
```

`NOASSERTION` is therefore a prompt to look harder, not a verdict. Absence of a root `LICENSE` file
proves nothing.

**The trap.** Every `berkeley-stat<num>.github.io` repo reports `MIT` through the GitHub API. Its
LICENSE file reads:

```
MIT License
Copyright (c) 2019 Kevin Lin
```

Kevin Lin is the author of the *just-the-class* Jekyll template. That MIT licence covers the site
template and says nothing about the course content. **Read the LICENSE file; do not read the API's
licence field.** If the copyright line names someone who is not the instructor or the university,
it is the template's.

Content repos are nearly all unlicensed. Two verified exceptions, both in `berkeley-stat243`:

| Repo | Licence |
| --- | --- |
| `stat243-fall-2021` | **CC0-1.0** — public domain, adaptable and publishable |
| `stat243-fall-2023` | **BSD-3-Clause** — adaptable with attribution |

`NOASSERTION` means GitHub found something it could not classify. Open it and read it.

## Gotchas

- **Course numbers change, and the old number keeps returning results.** `STAT 200A/B` was replaced
  by `STAT 201A/B` in 2012–13 and, per the department's own
  [notice](https://statistics.berkeley.edu/courses/notices/noticeAbout200ABand201AB), *"will not be
  taught in the near future"*. `STAT C239A` was succeeded by `STAT 256`. Search results happily
  return decade-old pages for both. Check `classes.berkeley.edu` before treating a course as live.
- **`guide.berkeley.edu` and the catalog sites are JS-rendered.** They fetch as an empty navigation
  shell. `guide.berkeley.edu/courses/stat/stat.pdf` serves *HTML*, not a PDF, and contains no course
  data. Don't route through the catalogue; use the department pages.
- **A course can be co-taught under two numbers**, with only one of them having a site. `STAT 256`
  has no domain of its own — its syllabus sits under `stat156.berkeley.edu/fall-2024/`.
- **An org with only a `.github.io` repo is an empty shell.** `berkeley-stat157` and
  `berkeley-stat241b` have the theme and no content.
- **A public repo is not public material, and this is the big one.** Many semester repos contain
  *only* the Quarto site — `index`, `syllabus`, `schedule`, `staff`, `license`, a stylesheet and a
  logo, about 13–15 files — with every note and problem set on bCourses. **Check before cataloguing
  it as reachable:**

  ```bash
  find <repo> -type f -not -path '*/.git/*' | wc -l     # under ~25 means scaffolding
  find <repo> -iname '*.pdf' -not -path '*/.git/*' | wc -l
  ```

  The split runs along a predictable line: **theory courses publish a syllabus, applied and
  computational courses publish everything.** Stat 201, 205, 206 are empty; Stat 153, 243, 158, 156
  hold 30–90 PDFs per offering. A permissive licence is no evidence either way — the CC BY licences
  here sit mostly on the *empty* repos.
- **Syllabus PDFs do not parse through a fetch tool** but are saved to disk, and the reading list is
  usually the most valuable thing on them. See `github-courses.md` for the extraction snippet.

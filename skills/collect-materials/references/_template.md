# <Provider>

**Verified:** YYYY-MM-DD — say when, because sites reorganise and a stale recipe is worse than none.

One line on what this provider is and what kind of material it holds.

## Where the material actually is

The route from a course name to the files. Be concrete — an exact URL pattern beats a description.

```
https://<pattern>/<course>/          what this level holds
https://<pattern>/<course>/<term>/   what this level holds
```

Say which level is the *real* material and which is a render, an index or a shell.

## What is gated

What looks public and is not, and which login it wants. This is the field that stops an agent
burning a session on something unreachable, so be specific: naming the LMS is more useful than
"requires login".

## Licence

What the provider's material is actually licensed under, where that statement lives, and — if there
is one — **the trap**: a licence that appears to apply to the content and does not.

## Gotchas

Things that cost time on the first harvest. Directory listing disabled, PDFs that need downloading
before they parse, `.pdf` URLs that serve HTML, redirects, JS-rendered catalogues that fetch empty,
rate limits, course numbers that changed.

## Known courses

Only if the provider has a stable set worth recording. Otherwise delete this section — the
catalogue in `docs/resources/` is where sources live, and duplicating it here creates a second
thing to update.

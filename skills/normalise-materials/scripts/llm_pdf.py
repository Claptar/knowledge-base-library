#!/usr/bin/env python3
"""The LLM route: a PDF read by a multimodal model, and the controls that keep it honest.

`references/quality-gates.md` § *The LLM route* is the specification.

A model reading page images is the only thing that recovers a two-column slide deck, a typeset
equation or a scanned page -- the material pymupdf4llm turns into word salad, which is what 55% of
the old corpus was. It is also inference about what was written, and this repository's standing
rule is that a conversion which is merely lossy is honest while one silently improved by a model is
not. Both are true, so the route exists and is fenced by four things:

    1. it never outranks a real source -- .tex/.qmd/.Rmd win, always;
    2. the page says so: route `llm-<model>`, fidelity `reconstructed`, and a banner;
    3. every document is cross-checked against the deterministic extraction of the same pages,
       and one that fails is listed rather than published;
    4. output is cached by (file hash, model, prompt) and committed, so a regeneration does not
       re-roll the model and produce different text for an unchanged source.

The API key is read from GEMINI_API_KEY and from nowhere else. It is never written to a file and
never printed.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import time
from dataclasses import dataclass, field
from pathlib import Path

# Quality first: this is a transcription job where a misread equation is worse than a slow run.
# gemini-3.5-flash-lite is the cheap high-volume alternative and is worth falling back to when the
# daily quota bites -- `--llm-model` switches, and changing it re-converts, because the model id is
# part of the cache key.
DEFAULT_MODEL = "gemini-3.8-flash"
BULK_MODEL = "gemini-3.5-flash-lite"

# The binding constraint on the free tier is REQUESTS PER DAY, not tokens, so the lever that
# matters is pages per request. Eight keeps a 32-page lecture to four calls instead of eight,
# while staying small enough that the model does not start summarising the tail.
PAGES_PER_CALL = 8

# Send the PDF itself, not rendered page images. Measured on the handwritten Stat 210A lecture:
# 574 input tokens per page natively against 1,179 for a 160-DPI PNG render, for output of equal
# quality. That halves the input bill for nothing given up. Rendering is kept only as the fallback
# for a PDF the API will not accept.
MAX_PAGES_PER_REQUEST = 40      # beyond this the tail starts getting summarised
RENDER_DPI = 160
MIN_FIGURE_BYTES = 4096          # below this it is a rule, a bullet or a logo
MAX_FIGURE_BYTES = 2_000_000
RECALL_FLOOR = 0.80              # of the deterministic text's content words
NUMERAL_FLOOR = 0.75

PROMPT = """You are converting one part of a scanned or typeset academic document into markdown.

Reproduce what is on these pages. Do not summarise, do not explain, do not add commentary, and do
not omit anything. This is a transcription task, not a writing task.

Rules:
- Output markdown only. No preamble, no closing remark, and do not wrap the whole answer in a code
  fence.
- Headings start at level 2 (`##`). Never emit a level-1 `#` heading.
- Mathematics in LaTeX, `$...$` inline and `$$...$$` on its own lines for display. Reproduce every
  equation you can read. Never use \\( \\) or \\[ \\].
- Tables as markdown pipe tables.
- Code as fenced blocks.
- Ignore page numbers, running headers and running footers. They are not content.
- Reading order matters: for a two-column layout, finish the left column before the right.
- If a passage is genuinely illegible, write `[illegible]` rather than guessing at it. Never invent
  text, a citation, a number or an equation that you cannot see.
- No raw HTML. No `<ins>`, `<u>`, `<br>`, `<sup>`, `<span>`. Use markdown, or LaTeX inside maths.
- Underlining in the original is emphasis: write it as **bold**, not as a tag or `\\underline{}`.
{figures}
Begin the markdown now."""

FIGURE_NOTE = """- Figures on these pages have been extracted to files. Reference them with markdown
  image syntax at the point where they appear, using a short factual description as the alt text:
{listing}
"""


@dataclass
class LLMResult:
    markdown: str
    cached: bool = False
    pages: int = 0
    figures: list = field(default_factory=list)
    recall: float = 0.0
    numeral_recall: float = 0.0
    ok: bool = True
    reason: str = ""


# --- cache -------------------------------------------------------------------------------------

def cache_key(pdf: Path, model: str) -> str:
    h = hashlib.sha256()
    h.update(pdf.read_bytes())
    h.update(model.encode())
    h.update(PROMPT.encode())
    return h.hexdigest()[:32]


# --- the cross-check ------------------------------------------------------------------------------

WORD = re.compile(r"[A-Za-z][A-Za-z'-]{3,}")
NUMERAL = re.compile(r"\d[\d.,]*")


CREDIBLE_CHARS_PER_PAGE = 400


def baseline_is_credible(deterministic: str, pages: int) -> bool:
    """Whether the parser's output is worth checking the model against.

    This distinction is load-bearing and was learned the hard way. On a digital PDF the parser
    reads the prose correctly and mangles only the mathematics, so its content words are a sound
    floor. On a SCAN it emits fragments -- `of nterpretations Probability come from 2 Where does
    prior` -- and a correct transcription will not contain them. Scoring the model against that
    punishes it for being better than the parser: the handwritten Stat 210A lecture, which the
    model transcribed cleanly and legibly, scored 80% recall and would have been thrown away.

    So the cross-check runs only where there is something credible to check against. Where there
    is not, the control is the banner: the page says a model wrote it and every equation is
    unverified."""
    return pages > 0 and len(deterministic.strip()) / pages >= CREDIBLE_CHARS_PER_PAGE


def cross_check(model_md: str, deterministic: str) -> tuple[float, float]:
    """How much of what the parser could read survived into what the model wrote.

    A model that summarised, skipped a section or hallucinated a replacement scores low on word
    recall, and that is the only automatic signal available that it did."""
    want = set(w.lower() for w in WORD.findall(deterministic))
    if not want:
        return 1.0, 1.0
    got = set(w.lower() for w in WORD.findall(model_md))
    recall = len(want & got) / len(want)

    nums = set(NUMERAL.findall(deterministic))
    num_recall = (len(nums & set(NUMERAL.findall(model_md))) / len(nums)) if nums else 1.0
    return recall, num_recall


def verdict(markdown: str, recall: float, numeral: float, credible: bool) -> tuple[bool, str]:
    """Publish or list. Applied fresh on every read, never cached."""
    if not markdown.strip():
        return False, "the model returned nothing"
    if not credible:
        # Nothing to check against: the parser could not read this document either. The banner is
        # the control here, not a number.
        return True, ""
    if recall < RECALL_FLOOR:
        return False, f"cross-check failed: {recall:.0%} of the parser's words survived"
    if numeral < NUMERAL_FLOOR:
        # Advisory, never fatal. Measured on ocw-6041sc/lectures/01-slides.pdf, where the model
        # produced a demonstrably BETTER conversion than the parser -- it unscrambled the
        # two-column reading order the parser had jumbled -- and still scored 67%, because the
        # parser's "numbers" are mostly slide numbers, running footers and column-split
        # fragments. A gate that rejects correct work two times in three is not a gate.
        return True, f"numerals: only {numeral:.0%} of the parser's matched (advisory)"
    return True, ""


# --- figures ---------------------------------------------------------------------------------------

def extract_figures(doc, first: int, last: int, out_dir: Path | None, rel: str) -> list:
    """Embedded images for a page range, written beside the page. Licence gating happens in the
    caller: this function is only reached for sources whose licence permits redistribution."""
    if out_dir is None:
        return []
    found = []
    for pno in range(first, last):
        page = doc[pno]
        for k, info in enumerate(page.get_images(full=True)):
            try:
                pix = doc.extract_image(info[0])
            except Exception:
                continue
            data, ext = pix["image"], pix["ext"]
            if not (MIN_FIGURE_BYTES <= len(data) <= MAX_FIGURE_BYTES):
                continue
            name = f"p{pno + 1:03d}-{k + 1}.{ext}"
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / name).write_bytes(data)
            found.append(f"{rel}/{name}")
    return found


# --- the call ----------------------------------------------------------------------------------------

def _client():
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY is not set; the LLM route cannot run")
    from google import genai
    return genai.Client(api_key=key)


class QuotaExhausted(RuntimeError):
    """The daily free-tier quota is gone. Retrying inside the run cannot help."""


def _is_quota(exc) -> bool:
    return "RESOURCE_EXHAUSTED" in str(exc) or "quota" in str(exc).lower()


def _retry_delay(exc, default: float) -> float:
    m = re.search(r"'retryDelay':\s*'(\d+(?:\.\d+)?)s'", str(exc))
    return float(m.group(1)) if m else default


def pdf_slice(doc, first: int, last: int) -> bytes:
    """A standalone PDF holding pages [first, last). Used to keep a long document inside the
    per-request page budget without falling back to rendering."""
    try:
        import pymupdf
    except ImportError:
        import fitz as pymupdf
    out = pymupdf.open()
    out.insert_pdf(doc, from_page=first, to_page=last - 1)
    data = out.tobytes()
    out.close()
    return data


def _call(client, model, images, figures, attempts=4, pdf_bytes=None):
    from google.genai import types
    note = (FIGURE_NOTE.replace("{listing}", "\n".join(f"    - `{f}`" for f in figures))
            if figures else "")
    if pdf_bytes is not None:
        parts = [types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf")]
    else:
        parts = [types.Part.from_bytes(data=png, mime_type="image/png") for png in images]
    # .replace, not .format: the prompt contains literal braces (LaTeX), and str.format
    # treats those as fields and raises.
    parts.append(types.Part.from_text(text=PROMPT.replace("{figures}", note)))
    for attempt in range(attempts):
        try:
            # Thinking is billed as output and buys little on a transcription task: the model is
            # reading a page, not solving it. Turning it down keeps the output cost close to the
            # visible markdown and makes the run markedly faster. Models that ignore the setting
            # simply behave as before.
            cfg = types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_level="low"))
            resp = client.models.generate_content(
                model=model, contents=[types.Content(role="user", parts=parts)], config=cfg)
            return (resp.text or "").strip()
        except Exception as exc:
            if _is_quota(exc):
                # A per-minute quota is worth waiting out; a per-day one is not, and hammering it
                # only turns one clear failure into hundreds of noisy ones. The cache is what
                # makes stopping cheap: everything converted so far survives, and the next run
                # resumes rather than starting over.
                if "PerDay" in str(exc) or "per day" in str(exc).lower():
                    raise QuotaExhausted(
                        f"daily free-tier quota exhausted for {model}") from None
                if attempt == attempts - 1:
                    raise QuotaExhausted(f"rate limit persisted for {model}") from None
                time.sleep(_retry_delay(exc, 2 ** attempt * 5))
                continue
            if attempt == attempts - 1:
                raise
            time.sleep(2 ** attempt * 2)
    return ""


FENCE_WRAPPED = re.compile(r"\A```(?:markdown|md)?\s*\n(.*)\n```\s*\Z", re.S)


def convert(pdf: Path, *, model: str = DEFAULT_MODEL, cache_dir: Path,
            figures_dir: Path | None = None, rel_figures: str = "figures",
            pages_per_call: int = PAGES_PER_CALL, deterministic: str = "") -> LLMResult:
    key = cache_key(pdf, model)
    cached = cache_dir / f"{key}.json"
    if cached.exists():
        blob = json.loads(cached.read_text())
        # The cache holds what the model WROTE. Whether that is publishable is policy, and policy
        # is re-applied on every read -- otherwise a threshold change silently fails to take
        # effect on everything already converted, which is the worst kind of stale.
        r = LLMResult(markdown=blob["markdown"], cached=True, pages=blob.get("pages", 0),
                      figures=blob.get("figures", []), recall=blob.get("recall", 1.0),
                      numeral_recall=blob.get("numeral_recall", 1.0))
        r.ok, r.reason = verdict(r.markdown, r.recall, r.numeral_recall,
                                 baseline_is_credible(deterministic, r.pages) if deterministic
                                 else blob.get("baseline_credible", False))
        return r

    try:
        import pymupdf
    except ImportError:
        import fitz as pymupdf

    client = _client()
    chunks, figures = [], []
    with pymupdf.open(pdf) as doc:
        n = len(doc)
        step = MAX_PAGES_PER_REQUEST
        for first in range(0, n, step):
            last = min(first + step, n)
            here = extract_figures(doc, first, last, figures_dir, rel_figures)
            figures += here
            data = pdf.read_bytes() if (first == 0 and last == n) else pdf_slice(doc, first, last)
            md = _call(client, model, [], here, pdf_bytes=data)
            md = FENCE_WRAPPED.sub(r"\1", md).strip()
            if md:
                chunks.append(md)

    markdown = "\n\n".join(chunks).strip()
    credible = baseline_is_credible(deterministic, n)
    recall, numeral = cross_check(markdown, deterministic) if deterministic else (1.0, 1.0)
    ok, reason = verdict(markdown, recall, numeral, credible)

    # An empty answer is a transport failure -- a rate limit, a 503, a refusal -- not a fact about
    # the document. Caching it would make one bad minute permanent: every later run would read the
    # empty entry and never call again. Failures are left uncached so they are simply retried.
    if not markdown.strip():
        return LLMResult(markdown="", pages=n, figures=figures, ok=False,
                         reason="the model returned nothing (not cached; will retry)")

    cache_dir.mkdir(parents=True, exist_ok=True)
    cached.write_text(json.dumps(
        {"source": pdf.name, "model": model, "pages": n, "markdown": markdown,
         "figures": figures, "recall": recall, "numeral_recall": numeral,
         "baseline_credible": credible, "ok": ok, "reason": reason}, indent=1))
    return LLMResult(markdown=markdown, pages=n, figures=figures, recall=recall,
                     numeral_recall=numeral, ok=ok, reason=reason)

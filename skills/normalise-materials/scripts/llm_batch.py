#!/usr/bin/env python3
"""The LLM route, run through the Batch API.

Same model, same prompt, same cache, half the price. The Batch API trades latency for a 50%
discount: requests are queued and answered within 24 hours instead of immediately. For a corpus
conversion that is the right trade -- nobody is waiting on any single page, and the cache means
the result is fetched once and then belongs to the repository.

Measured on this corpus: 14,689 unique PDF pages, 574 input and ~269 output tokens per page
natively, which is about $21 on gemini-3.8-flash at standard rates and about $10.50 batched.

    llm_batch.py plan                    # what would be sent, and what it will cost
    llm_batch.py submit                  # upload, queue, and record the job ids
    llm_batch.py status                  # where the jobs are
    llm_batch.py collect                 # write finished results into the conversion cache

Nothing here writes to docs/. It fills the cache; `normalise_source.py --apply` then converts
without spending anything, because every document it needs is already answered.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import llm_pdf                                                    # noqa: E402
import normalise_source as ns                                     # noqa: E402

LIBRARY = Path(__file__).resolve().parents[3]
CACHE = LIBRARY / "conversion-cache"
JOBS = CACHE / "batches"
REQUESTS_PER_JOB = 60

# Standard rates per 1M tokens; batch is half. Only used to print an estimate.
PRICES = {"gemini-3.8-flash": (0.75, 3.75), "gemini-3.5-flash": (1.50, 9.00),
          "gemini-3.5-flash-lite": (0.30, 2.50), "gemini-3.1-flash-lite": (0.25, 1.50),
          "gemini-2.5-flash-lite": (0.10, 0.40)}
IN_PER_PAGE, OUT_PER_PAGE = 574, 269


def already_queued() -> set:
    """Cache keys sitting in a batch that has been submitted but not yet collected.

    Without this, re-running submit before the results come back pays for the same documents a
    second time -- the cache cannot protect you from a job that has not finished."""
    keys = set()
    for man in JOBS.glob("*.json"):
        try:
            import json as _json
            for row in _json.loads(man.read_text()).get("index", []):
                keys.add(row["cache_key"])
        except Exception:
            continue
    return keys


def pdfs_to_convert(model: str):
    """Every PDF the converter would send to the model, deduplicated by content.

    Deduplicating here rather than per source is what stops Stat 243 being billed eleven times for
    reprinting the same two papers across eleven course years."""
    try:
        import pymupdf
    except ImportError:
        import fitz as pymupdf
    lock = ns.load_lock(LIBRARY / "sources")
    entries = lock["sources"] if isinstance(lock, dict) else lock
    seen, out = {}, []
    for e in entries:
        root = LIBRARY / "sources" / e["slug"]
        if not root.is_dir():
            continue
        dest, _, _ = ns.destination(e, LIBRARY)
        if dest is None:
            continue
        files, _ = ns.candidate_files(root, False)
        docs, _ = ns.group_documents(root, files)
        for d in docs:
            if d.route != "llm":
                continue
            digest = hashlib.sha256(d.src.read_bytes()).hexdigest()
            if digest in seen:
                continue
            seen[digest] = True
            key = llm_pdf.cache_key(d.src, model)
            if (CACHE / f"{key}.json").exists() or key in already_queued():
                continue
            try:
                with pymupdf.open(d.src) as doc:
                    pages = len(doc)
            except Exception:
                continue
            out.append((key, d.src, pages))
    return out


# How much inline payload to put in one batch job. The PDFs total ~1 GB, so they cannot go in one
# job; this caps each. Kept well under any documented limit because a rejected job wastes the whole
# upload, while an extra job costs nothing.
# Halved after 545 of 920 requests came back "Internal error encountered" -- a server-side failure,
# not a bad request. Smaller jobs are the cheap mitigation: a job that fails takes fewer requests
# down with it, and the retry is smaller. Errored requests are not billed, so retrying costs only
# time.
MAX_JOB_BYTES = 12_000_000


def _parts_for(client, src: Path, pages: int):
    """Request payloads for a document, each within the page budget, with the PDF INLINE.

    Not a Files API reference. A batch request that points at an uploaded file comes back
    `code=7, 'The caller does not have permission'` for every response while the job still reports
    SUCCEEDED -- 920 requests looked fine and contained nothing. Inlining the bytes works, and is
    verified: batches/1bv7wspttq5b6kpbntb84cigolrvk803t7jh returned clean markdown."""
    from google.genai import types
    step = llm_pdf.MAX_PAGES_PER_REQUEST
    prompt = llm_pdf.PROMPT.replace("{figures}", "")
    if pages <= step:
        return [[types.Part.from_bytes(data=src.read_bytes(), mime_type="application/pdf"),
                 types.Part.from_text(text=prompt)]]
    try:
        import pymupdf
    except ImportError:
        import fitz as pymupdf
    out = []
    with pymupdf.open(src) as doc:
        for first in range(0, pages, step):
            last = min(first + step, pages)
            out.append([types.Part.from_bytes(data=llm_pdf.pdf_slice(doc, first, last),
                                              mime_type="application/pdf"),
                        types.Part.from_text(text=prompt)])
    return out


def cmd_plan(a):
    work = pdfs_to_convert(a.model)
    pages = sum(p for _, _, p in work)
    reqs = sum(max(1, -(-p // llm_pdf.MAX_PAGES_PER_REQUEST)) for _, _, p in work)
    cin, cout = PRICES.get(a.model, (0.75, 3.75))
    std = pages * IN_PER_PAGE / 1e6 * cin + pages * OUT_PER_PAGE / 1e6 * cout
    print(f"{len(work)} documents, {pages:,} pages, {reqs} batch requests")
    print(f"estimate on {a.model}: ${std:.2f} standard, ${std / 2:.2f} batched")
    already = len(list(CACHE.glob("*.json")))
    print(f"{already} documents already in the cache and will not be sent again")


def cmd_submit(a):
    from google import genai
    from google.genai import types
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        print("GEMINI_API_KEY is not set", file=sys.stderr)
        return 2
    client = genai.Client(api_key=key)
    work = pdfs_to_convert(a.model)
    if a.limit:
        work = work[:a.limit]
    if not work:
        print("nothing to send: every document is already cached")
        return 0

    JOBS.mkdir(parents=True, exist_ok=True)
    cfg = {"thinking_config": {"thinking_level": "low"}}
    requests, index, sizes = [], [], []
    print(f"building {len(work)} documents…")
    for n, (ckey, src, pages) in enumerate(work, 1):
        for part_no, parts in enumerate(_parts_for(client, src, pages)):
            requests.append({"contents": [types.Content(role="user", parts=parts).model_dump(
                exclude_none=True)], "config": cfg})
            sizes.append(int(src.stat().st_size * 1.4) if pages <= llm_pdf.MAX_PAGES_PER_REQUEST
                         else int(src.stat().st_size * 1.4 * llm_pdf.MAX_PAGES_PER_REQUEST
                                  / max(pages, 1)))
            index.append({"cache_key": ckey, "source": str(src), "pages": pages,
                          "part": part_no})
        if n % 100 == 0:
            print(f"  {n}/{len(work)}")

    submitted, start = [], 0
    while start < len(requests):
        end, size = start, 0
        while end < len(requests) and end - start < REQUESTS_PER_JOB:
            here = sizes[end]
            if end > start and size + here > MAX_JOB_BYTES:
                break
            size += here
            end += 1
        batch = requests[start:end]
        job = client.batches.create(model=a.model, src=batch,
                                    config={"display_name": f"library-{start:05d}"})
        submitted.append({"job": job.name, "first": start, "count": len(batch)})
        print(f"  queued {job.name} ({len(batch)} requests, {size / 1e6:.0f} MB)")
        start = end

    stamp = time.strftime("%Y%m%dT%H%M%S")
    (JOBS / f"{stamp}.json").write_text(json.dumps(
        {"model": a.model, "submitted": submitted, "index": index}, indent=1))
    print(f"\nrecorded in {JOBS / (stamp + '.json')}")
    print("results arrive within 24h; `llm_batch.py collect` writes them into the cache")
    return 0


def _manifests():
    return sorted(JOBS.glob("*.json"))


def _get_job(client, name, attempts=5):
    """Fetch a job, riding out transient server errors.

    A single 503 used to abort the whole collect, losing the results of every job already walked.
    The service was returning them intermittently on the day 545 of 920 requests also came back
    "Internal error encountered" -- so resilience here is not hypothetical."""
    import time
    for attempt in range(attempts):
        try:
            return client.batches.get(name=name)
        except Exception as exc:
            transient = any(s in str(exc) for s in ("503", "UNAVAILABLE", "500", "Internal"))
            if not transient or attempt == attempts - 1:
                raise
            time.sleep(2 ** attempt * 3)
    return None


def cmd_status(a):
    from google import genai
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    for man in _manifests():
        blob = json.loads(man.read_text())
        print(f"\n{man.name}  model={blob['model']}")
        for entry in blob["submitted"]:
            job = _get_job(client, entry["job"])
            print(f"  {entry['job']:52} {job.state.name if hasattr(job.state,'name') else job.state}"
                  f"  ({entry['count']} requests)")
    return 0


def cmd_collect(a):
    from google import genai
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    CACHE.mkdir(parents=True, exist_ok=True)
    written = pending = skipped = 0
    failed: dict[str, int] = {}
    for man in _manifests():
        blob = json.loads(man.read_text())
        index, model = blob["index"], blob["model"]
        pieces: dict[str, dict[int, str]] = {}
        for entry in blob["submitted"]:
            job = client.batches.get(name=entry["job"])
            state = job.state.name if hasattr(job.state, "name") else str(job.state)
            if "SUCCEEDED" not in state:
                pending += entry["count"]
                continue
            responses = getattr(job.dest, "inlined_responses", None) or []
            for offset, resp in enumerate(responses):
                meta = index[entry["first"] + offset]
                err = getattr(resp, "error", None)
                if err:
                    failed[str(getattr(err, "message", err))] = \
                        failed.get(str(getattr(err, "message", err)), 0) + 1
                    continue
                try:
                    text = (resp.response.candidates[0].content.parts[0].text or "").strip()
                except Exception:
                    text = ""
                pieces.setdefault(meta["cache_key"], {})[meta["part"]] = text
        for ckey, parts in pieces.items():
            md = "\n\n".join(parts[i] for i in sorted(parts)).strip()
            md = llm_pdf.FENCE_WRAPPED.sub(r"\1", md).strip()
            if not md:
                # An empty answer is a transport failure, not a fact about the document. Caching
                # it would make one bad job permanent; leaving it out means it is simply retried.
                skipped += 1
                continue
            meta = next(m for m in index if m["cache_key"] == ckey)
            (CACHE / f"{ckey}.json").write_text(json.dumps(
                {"source": Path(meta["source"]).name, "model": model, "pages": meta["pages"],
                 "markdown": md, "figures": [], "recall": 1.0, "numeral_recall": 1.0,
                 "baseline_credible": False, "ok": bool(md),
                 "reason": "" if md else "the model returned nothing"}, indent=1))
            written += 1
    print(f"wrote {written} cache entries; {pending} requests still pending; "
          f"{skipped} empty answers not cached (they will be retried)")
    for why, n in sorted(failed.items(), key=lambda kv: -kv[1]):
        print(f"  {n:5d}  {why}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["plan", "submit", "status", "collect"])
    ap.add_argument("--model", default=llm_pdf.DEFAULT_MODEL)
    ap.add_argument("--limit", type=int, default=0, help="send only the first N documents")
    a = ap.parse_args()
    return {"plan": cmd_plan, "submit": cmd_submit, "status": cmd_status,
            "collect": cmd_collect}[a.command](a) or 0


if __name__ == "__main__":
    raise SystemExit(main())

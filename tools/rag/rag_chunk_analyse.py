"""
Dry-run chunk-analyser voor de Certificaid RAG-index.

Voert dezelfde chunking uit als rag_index.py maar embeddet niet en raakt
ChromaDB niet aan. Antwoordt op drie vragen vóór een full-build:

  1. Welke chunks zouden bij embedding getrunceerd worden?
     bge-m3 op MPS draait met max_seq_length=2048 (~6-8K chars voor NL-juridisch).
     Chunks groter dan dat verliezen hun staart in de embedding.

  2. Welke bronnen produceren "arbitraire" chunks i.p.v. logische?
     Logisch = chunk-grens op een heading (## Art., ## sectie, ## titel).
     Arbitrair = paragraph-cut door `split_long_chunk` omdat de logische
     chunk te groot was (signaal: `_split_part` is gezet, id eindigt op _part1/_part2).

  3. Wat is de char/token-verdeling per bron-rol?
     Sanity-check op de eerste full-build.

Output:
  - Console-tabellen per bron-rol
  - JSON-rapport in data/etl/qa/chunk-analyse-<timestamp>.json

Gebruik:
  python3 tools/rag/rag_chunk_analyse.py                       # alle trusted bronnen
  python3 tools/rag/rag_chunk_analyse.py --bron-rol wettekst   # alleen wetteksten
  python3 tools/rag/rag_chunk_analyse.py --include-unreviewed  # incl. needs-rework
  python3 tools/rag/rag_chunk_analyse.py --top 20              # toon top-20 i.p.v. top-10
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import statistics
import sys
from pathlib import Path

import frontmatter
from tqdm import tqdm

ROOT = Path(__file__).resolve().parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.rag.rag_index import (  # noqa: E402
    BRON_DIRS,
    MAX_CHUNK_CHARS,
    MIN_CHUNK_CHARS,
    MPS_MAX_SEQ_LENGTH,
    _apply_trust_filter,
    _has_real_content,
    _is_toc_only,
    split_generic,
    split_long_chunk,
    split_wettekst,
)

QA_DIR = ROOT / "data" / "qa"
TRUNCATE_THRESHOLD = MPS_MAX_SEQ_LENGTH   # 2048 tokens


# ---------------------------------------------------------------------------
# Tokenizer (bge-m3 = XLM-RoBERTa)
# ---------------------------------------------------------------------------

def load_tokenizer():
    from transformers import AutoTokenizer
    print("→ Laad BAAI/bge-m3 tokenizer ...")
    return AutoTokenizer.from_pretrained("BAAI/bge-m3")


# ---------------------------------------------------------------------------
# Chunk-collectie per bron-rol (re-use rag_index logica zonder Chroma)
# ---------------------------------------------------------------------------

def chunks_for_wettekst(path: Path) -> list[dict]:
    post = frontmatter.load(str(path))
    if _is_toc_only(post.content):
        return []
    fm = post.metadata
    chunks = split_wettekst(post.content, path.stem, fm)
    if not chunks:
        wet_naam = str(fm.get("wet") or fm.get("bron") or path.stem)
        chunks = split_generic(post.content, path.stem, breadcrumb_prefix=f"[{wet_naam}]")
    return [c for c in chunks
            if len(c["text"]) >= MIN_CHUNK_CHARS and _has_real_content(c["text"])]


def chunks_for_norm(path: Path) -> list[dict]:
    post = frontmatter.load(str(path))
    fm = post.metadata
    norm_naam = str(fm.get("norm", path.stem))
    breadcrumb = f"[Norm — {norm_naam}]"
    chunks = split_generic(post.content, path.stem, breadcrumb_prefix=breadcrumb)
    if not chunks:
        full_text = f"{breadcrumb}\n\n{post.content.strip()}"
        if len(full_text) < MIN_CHUNK_CHARS or not _has_real_content(full_text):
            return []
        base = {"id": f"{path.stem}__sec_volledig", "text": full_text,
                "heading": "", "path": [], "breadcrumb": breadcrumb}
        return split_long_chunk(base, MAX_CHUNK_CHARS)
    # Per-sectie long-split (zoals in index_normen)
    out: list[dict] = []
    for c in chunks:
        if len(c["text"]) < MIN_CHUNK_CHARS or not _has_real_content(c["text"]):
            continue
        for fragment in split_long_chunk(c, MAX_CHUNK_CHARS):
            part = fragment.get("_split_part", "")
            fid = f"{c['id']}_part{part.split('/')[0]}" if part else c["id"]
            out.append({**fragment, "id": fid})
    return out


def chunks_for_advies(path: Path) -> list[dict]:
    post = frontmatter.load(str(path))
    fm = post.metadata
    content = post.content.strip()
    nummer_raw = str(fm.get("nummer", path.stem))
    nummer = re.sub(r"^CBN[- ]advies\s*", "", nummer_raw).strip()
    h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    onderwerp = h1_match.group(1).strip() if h1_match else ""
    onderwerp = re.sub(r"^CBN[- ]advies\s*\S+\s*—\s*", "", onderwerp).strip()
    if len(onderwerp) > 80:
        onderwerp = onderwerp[:80].rsplit(" ", 1)[0] + "…"
    breadcrumb = f"[CBN-advies {nummer} — {onderwerp}]" if onderwerp else f"[CBN-advies {nummer}]"

    out: list[dict] = []
    has_headings = bool(re.search(r"^#{2,4} ", content, re.MULTILINE))
    if not has_headings:
        full_text = f"{breadcrumb}\n\n{content}"
        base = {"id": f"{path.stem}__volledig", "text": full_text,
                "heading": "", "path": [], "breadcrumb": breadcrumb}
        for fragment in split_long_chunk(base, MAX_CHUNK_CHARS):
            part = fragment.get("_split_part", "")
            fid = f"{path.stem}__volledig_part{part.split('/')[0]}" if part else f"{path.stem}__volledig"
            out.append({**fragment, "id": fid})
    else:
        chunks = split_generic(content, path.stem, breadcrumb_prefix=breadcrumb)
        for chunk in chunks:
            if len(chunk["text"]) < MIN_CHUNK_CHARS or not _has_real_content(chunk["text"]):
                continue
            for fragment in split_long_chunk(chunk, MAX_CHUNK_CHARS):
                part = fragment.get("_split_part", "")
                fid = f"{chunk['id']}_part{part.split('/')[0]}" if part else chunk["id"]
                out.append({**fragment, "id": fid})
    return out


CHUNKER = {
    "wettekst": chunks_for_wettekst,
    "norm":     chunks_for_norm,
    "advies":   chunks_for_advies,
}


# ---------------------------------------------------------------------------
# Analyse per bron
# ---------------------------------------------------------------------------

def is_arbitrary(chunk: dict) -> bool:
    """True als deze chunk een paragraph-cut is i.p.v. een logische heading-grens."""
    if chunk.get("_split_part"):
        return True
    # Backup: id eindigt op _part<N>
    return bool(re.search(r"_part\d+$", chunk.get("id", "")))


def analyse_bron(path: Path, rol: str, tokenizer) -> dict:
    chunker = CHUNKER[rol]
    try:
        chunks = chunker(path)
    except Exception as e:
        return {"bestand": path.name, "rol": rol, "error": str(e)}

    if not chunks:
        return {"bestand": path.name, "rol": rol, "n_chunks": 0,
                "chars": [], "tokens": [], "n_arbitrary": 0, "n_truncated": 0}

    chars = [len(c["text"]) for c in chunks]
    # Token-count: tokenize batch voor efficiency
    tokens_per_chunk = [
        len(tokenizer.encode(c["text"], add_special_tokens=True, truncation=False))
        for c in chunks
    ]
    n_arbitrary = sum(1 for c in chunks if is_arbitrary(c))
    n_truncated = sum(1 for t in tokens_per_chunk if t > TRUNCATE_THRESHOLD)

    return {
        "bestand":    path.name,
        "rol":        rol,
        "n_chunks":   len(chunks),
        "chars":      chars,
        "tokens":     tokens_per_chunk,
        "n_arbitrary": n_arbitrary,
        "n_truncated": n_truncated,
        # Voor rapport
        "max_chars":  max(chars),
        "max_tokens": max(tokens_per_chunk),
        "p95_tokens": _pct(tokens_per_chunk, 95),
    }


def _pct(xs: list[int], p: int) -> int:
    if not xs:
        return 0
    s = sorted(xs)
    k = max(0, min(len(s) - 1, int(round((p / 100) * (len(s) - 1)))))
    return s[k]


# ---------------------------------------------------------------------------
# Rapport
# ---------------------------------------------------------------------------

def render_summary(rol: str, results: list[dict]) -> str:
    valid = [r for r in results if "error" not in r and r.get("n_chunks", 0) > 0]
    if not valid:
        return f"\n=== {rol.upper()}: geen resultaten ==="
    n_bronnen = len(valid)
    all_chars = [c for r in valid for c in r["chars"]]
    all_tokens = [t for r in valid for t in r["tokens"]]
    total_chunks = sum(r["n_chunks"] for r in valid)
    total_arbitrary = sum(r["n_arbitrary"] for r in valid)
    total_truncated = sum(r["n_truncated"] for r in valid)

    lines = [
        f"\n=== {rol.upper()} — {n_bronnen} bronnen, {total_chunks} chunks ===",
        f"  Chars:   p50={_pct(all_chars, 50):>6}  p95={_pct(all_chars, 95):>6}  max={max(all_chars):>6}",
        f"  Tokens:  p50={_pct(all_tokens, 50):>6}  p95={_pct(all_tokens, 95):>6}  max={max(all_tokens):>6}",
        f"  Arbitrair gesplitst : {total_arbitrary}/{total_chunks} ({100*total_arbitrary/total_chunks:.1f}%)",
        f"  Trunctie-risico    : {total_truncated}/{total_chunks} chunks >{TRUNCATE_THRESHOLD} tokens "
        f"({100*total_truncated/total_chunks:.1f}%)",
    ]
    return "\n".join(lines)


def render_top(label: str, results: list[dict], key: str, top: int) -> str:
    valid = [r for r in results if "error" not in r and r.get(key, 0) > 0]
    if not valid:
        return ""
    valid.sort(key=lambda r: r[key], reverse=True)
    head = valid[:top]
    if not head:
        return ""
    lines = [f"\n  TOP {len(head)} bronnen op `{label}`:"]
    width = max(len(r["bestand"]) for r in head)
    for r in head:
        lines.append(
            f"    {r['bestand']:<{width}}  "
            f"{key}={r[key]:>4}  n_chunks={r['n_chunks']:>3}  "
            f"max_tokens={r['max_tokens']:>4}  max_chars={r['max_chars']:>5}"
        )
    return "\n".join(lines)


def render_errors(results: list[dict]) -> str:
    errs = [r for r in results if "error" in r]
    if not errs:
        return ""
    lines = ["\n  Fouten (overgeslagen):"]
    for r in errs:
        lines.append(f"    {r['bestand']}: {r['error']}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--bron-rol", choices=["wettekst", "norm", "advies"],
                   help="Analyseer alleen deze bron-rol (default: alle drie)")
    p.add_argument("--include-unreviewed", action="store_true",
                   help="Ook bronnen met trust.status != trusted analyseren")
    p.add_argument("--top", type=int, default=15,
                   help="Aantal bronnen in top-tabellen (default: 15)")
    args = p.parse_args()

    tokenizer = load_tokenizer()

    rollen = [args.bron_rol] if args.bron_rol else ["wettekst", "norm", "advies"]
    rapport: dict[str, list[dict]] = {}

    for rol in rollen:
        src = BRON_DIRS[rol]
        files = sorted(src.glob("*.md"))
        files = [f for f in files if "INDEX" not in f.name]
        files, skipped, _ = _apply_trust_filter(files, include_unreviewed=args.include_unreviewed)
        if skipped:
            parts = ", ".join(f"{k}: {v}" for k, v in sorted(skipped.items()))
            print(f"\n→ {rol}: {len(files)} bronnen geanalyseerd, {sum(skipped.values())} geskipt ({parts})")
        else:
            print(f"\n→ {rol}: {len(files)} bronnen geanalyseerd")

        results: list[dict] = []
        for f in tqdm(files, desc=rol):
            results.append(analyse_bron(f, rol, tokenizer))
        rapport[rol] = results

    # Console-rapport
    print("\n" + "=" * 70)
    print("  CHUNK-ANALYSE — samenvatting per bron-rol")
    print("=" * 70)
    for rol, results in rapport.items():
        print(render_summary(rol, results))
        t1 = render_top("trunctie-risico", results, "n_truncated", args.top)
        if t1:
            print(t1)
        t2 = render_top("arbitraire splits", results, "n_arbitrary", args.top)
        if t2:
            print(t2)
        errs = render_errors(results)
        if errs:
            print(errs)

    # JSON-rapport (zonder de char/token-lijsten — die zijn enorm groot)
    QA_DIR.mkdir(parents=True, exist_ok=True)
    ts = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out_path = QA_DIR / f"chunk-analyse-{ts}.json"
    serialisable = {
        rol: [
            {k: v for k, v in r.items() if k not in ("chars", "tokens")}
            for r in results
        ]
        for rol, results in rapport.items()
    }
    out_path.write_text(json.dumps({
        "timestamp": ts,
        "truncate_threshold_tokens": TRUNCATE_THRESHOLD,
        "max_chunk_chars": MAX_CHUNK_CHARS,
        "embedding_model": "BAAI/bge-m3",
        "include_unreviewed": args.include_unreviewed,
        "bronnen": serialisable,
    }, indent=2, ensure_ascii=False))
    print(f"\n→ JSON-rapport: {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

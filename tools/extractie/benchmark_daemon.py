"""
Benchmark voor de Certificaid embedding-daemon (ADR-018).

Meet throughput en kwaliteit van:
  - Sequencieel vs. concurrent /duplicate-check (rerank-batching)
  - Gating-kwaliteitsmeting: bi-encoder-only vs. full-rerank score-delta

Gebruik:
  python tools/extractie/benchmark_daemon.py [--host localhost] [--port 8765] [--rounds 2]

Vereisten:
  pip install httpx   (standaard beschikbaar in de project-venv)

Output:
  - Per-request latency (sequencieel vs. concurrent)
  - Throughput (requests/sec)
  - Gating-ratio en score-delta (kwaliteitsmeting)
"""

from __future__ import annotations

import argparse
import asyncio
import sys
import time
from pathlib import Path
from typing import Any

try:
    import httpx
except ImportError:
    print("httpx is vereist: pip install httpx", file=sys.stderr)
    sys.exit(1)

# Testqueries representatief voor concept-extractie agents
BENCH_QUERIES = [
    "aftrek voor definitief belaste inkomsten DBI participatievoorwaarde",
    "fusie belastingneutraliteit overdracht activa passiva",
    "vennootschapsbelasting tarief notionele interestaftrek",
    "boekhoudkundige verwerking aanschaffingswaarde immateriële vaste activa",
    "antiwitwaswet cliëntenonderzoek uiteindelijk begunstigde",
    "WVV bestuurdersaansprakelijkheid schade vennootschap",
]

BASE_URL_TEMPLATE = "http://{host}:{port}"


async def _check(
    client: httpx.AsyncClient,
    base_url: str,
    query: str,
    chroma_path: str,
) -> dict[str, Any]:
    """Stuur één /duplicate-check en geef resultaat + latency terug."""
    payload = {"naam": query, "top_n": 5, "chroma_path": chroma_path}
    t0 = time.perf_counter()
    resp = await client.post(f"{base_url}/duplicate-check", json=payload, timeout=120.0)
    data = resp.json()
    latency = time.perf_counter() - t0
    return {"query": query, "latency": latency, "result": data}


async def bench_sequencieel(
    base_url: str,
    chroma_path: str,
    queries: list[str],
) -> list[dict]:
    """Stuur queries één voor één (sequencieel)."""
    results = []
    async with httpx.AsyncClient() as client:
        for q in queries:
            r = await _check(client, base_url, q, chroma_path)
            results.append(r)
            top1 = r["result"].get("top1") or {}
            gating = "GATING" if top1.get("gating_used") else "RERANK"
            print(f"  [seq/{gating}] {q[:45]!r:<47} → {r['latency']:.2f}s  bi={top1.get('bi_score', '?')}")
    return results


async def bench_concurrent(
    base_url: str,
    chroma_path: str,
    queries: list[str],
) -> list[dict]:
    """Stuur alle queries tegelijk (concurrent) — triggert batch-worker."""
    async with httpx.AsyncClient() as client:
        tasks = [_check(client, base_url, q, chroma_path) for q in queries]
        wall_t0 = time.perf_counter()
        results = await asyncio.gather(*tasks)
        wall_total = time.perf_counter() - wall_t0
    for r in results:
        top1 = r["result"].get("top1") or {}
        gating = "GATING" if top1.get("gating_used") else "RERANK"
        print(f"  [con/{gating}] {r['query'][:45]!r:<47} → {r['latency']:.2f}s  bi={top1.get('bi_score', '?')}")
    print(f"  Wall-clock concurrent: {wall_total:.2f}s voor {len(queries)} requests")
    return list(results), wall_total


async def bench_gating_kwaliteit(
    base_url: str,
    chroma_path: str,
    queries: list[str],
) -> dict[str, Any]:
    """
    Meet kwaliteitsverlies door gating.

    Vergelijkt de `gating_used`-vlag en score-delta (bi_score vs. rerank_score)
    als proxy voor het risico dat gating een ander resultaat geeft dan volledige rerank.
    Een score_delta van 0 bij gating_used=True betekent: bi≈rerank, geen verlies.
    """
    gating_used_count = 0
    details = []

    async with httpx.AsyncClient() as client:
        for q in queries:
            r = await _check(client, base_url, q, chroma_path)
            top1 = r["result"].get("top1") or {}
            gating_used = top1.get("gating_used", False)
            if gating_used:
                gating_used_count += 1
            bi_score     = top1.get("bi_score", 0) or 0
            rerank_score = top1.get("rerank_score", 0) or 0
            score_delta  = abs(bi_score - rerank_score)
            details.append({
                "query":        q,
                "gating_used":  gating_used,
                "bi_score":     bi_score,
                "rerank_score": rerank_score,
                "score_delta":  score_delta,
            })
            flag = "GATING" if gating_used else "RERANK"
            print(f"  [{flag}] bi={bi_score:.3f} rerank={rerank_score:.3f} delta={score_delta:.4f}  {q[:40]!r}")

    return {
        "gating_ratio": gating_used_count / len(queries) if queries else 0,
        "details": details,
        "gem_score_delta": (
            sum(o["score_delta"] for o in details) / len(details) if details else 0
        ),
    }


def _print_rapport(
    seq_results: list[dict],
    con_results: list[dict],
    con_wall: float,
    gating: dict[str, Any],
    rounds: int,
) -> None:
    print("\n" + "=" * 70)
    print("BENCHMARK RAPPORT — Certificaid Embedding Daemon v2")
    print("=" * 70)

    seq_latencies = [r["latency"] for r in seq_results]
    seq_total     = sum(seq_latencies)
    seq_per_req   = seq_total / len(seq_latencies) if seq_latencies else 0
    seq_throughput = len(seq_latencies) / seq_total if seq_total > 0 else 0

    con_latencies  = [r["latency"] for r in con_results]
    # Wall-clock concurrent = max per-request latency (niet de som, want parallel)
    con_throughput = len(con_latencies) / con_wall if con_wall > 0 else 0

    print(f"\nSEQUENCIEEL ({len(seq_latencies)} requests over {rounds} rondes)")
    print(f"  Totale tijd      : {seq_total:.2f}s")
    print(f"  Per-request p50  : {sorted(seq_latencies)[len(seq_latencies)//2]:.2f}s")
    print(f"  Per-request gem  : {seq_per_req:.2f}s")
    print(f"  Throughput       : {seq_throughput:.2f} req/s")

    print(f"\nCONCURRENT/BATCHED ({len(con_latencies)} requests over {rounds} rondes)")
    print(f"  Wall-clock total : {con_wall:.2f}s")
    print(f"  Throughput       : {con_throughput:.2f} req/s")

    speedup = con_throughput / seq_throughput if seq_throughput > 0 else float("nan")
    tijd_reductie = 1 - (con_wall / seq_total) if seq_total > 0 else float("nan")
    print(f"\n  Throughput-winst : {speedup:.1f}×")
    print(f"  Tijd-reductie    : {tijd_reductie:.0%}  ({seq_total:.1f}s → {con_wall:.1f}s)")

    print(f"\nGATING KWALITEIT")
    print(f"  Gating-ratio     : {gating['gating_ratio']:.0%} van queries skip rerank")
    print(f"  Gem. score-delta : {gating['gem_score_delta']:.4f}")
    print(f"  (score_delta ≈ 0 betekent bi-encoder ≈ reranker: geen kwaliteitsverlies)")
    for d in gating["details"]:
        flag = "GATING" if d["gating_used"] else "RERANK"
        print(f"    [{flag}] {d['query'][:45]!r:<47} delta={d['score_delta']:.4f}")

    print(f"\nRondes : {rounds} | Queries/ronde : {len(BENCH_QUERIES)}")
    print("=" * 70)


async def run_benchmark(host: str, port: int, rounds: int) -> None:
    base_url = BASE_URL_TEMPLATE.format(host=host, port=port)

    # Health-check
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(f"{base_url}/health", timeout=10.0)
            health = resp.json()
        except Exception as exc:
            print(f"FOUT: kan daemon niet bereiken op {base_url}: {exc}", file=sys.stderr)
            sys.exit(1)

    print(f"Daemon: {health.get('status')} — model={health.get('model')} device={health.get('device')}")
    print(f"Daemon versie: {health.get('daemon_version', '1.0 (onbekend)')}")
    opts = health.get("optimalisaties", {})
    if opts:
        rb = opts.get("rerank_batching", {})
        g  = opts.get("gating", {})
        print(f"Batching: window={rb.get('window_sec')}s max={rb.get('max_size')} | "
              f"Gating: {'aan' if g.get('enabled') else 'uit'} top1≥{g.get('top1_threshold')}")

    collectie_groottes = health.get("collectie_groottes", {})
    if not collectie_groottes:
        print("FOUT: geen collectie beschikbaar in de daemon", file=sys.stderr)
        sys.exit(1)
    chroma_path = next(iter(collectie_groottes))
    print(f"Collectie: {chroma_path} ({collectie_groottes[chroma_path]} items)\n")

    all_seq: list[dict] = []
    all_con: list[dict] = []
    con_wall_total = 0.0

    for ronde in range(1, rounds + 1):
        print(f"--- Ronde {ronde}/{rounds} ---")
        print("Sequencieel:")
        seq = await bench_sequencieel(base_url, chroma_path, BENCH_QUERIES)
        all_seq.extend(seq)

        print("Concurrent:")
        con, wall = await bench_concurrent(base_url, chroma_path, BENCH_QUERIES)
        all_con.extend(con)
        con_wall_total += wall

    print("\nGating kwaliteitscheck:")
    gating = await bench_gating_kwaliteit(base_url, chroma_path, BENCH_QUERIES)

    _print_rapport(all_seq, all_con, con_wall_total, gating, rounds)


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark Certificaid embedding-daemon")
    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--rounds", type=int, default=2,
                        help="Aantal benchmark-rondes (default: 2)")
    args = parser.parse_args()
    asyncio.run(run_benchmark(args.host, args.port, args.rounds))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Bulk refresh van alle CBN-adviezen via scrape_cbn_advies.py.

Verwerkt alle CBN-*.md in resources/bronnen/adviezen/ met --apply
(in-place overschrijven). Rate-limited op 0.35s per request.

Gebruik:
    python3 tools/etl/bulk_refresh_adviezen.py                  # alle 436
    python3 tools/etl/bulk_refresh_adviezen.py --limit 10       # eerste 10
    python3 tools/etl/bulk_refresh_adviezen.py --skip-trusted   # skip trust=trusted
"""
from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from tools.etl.scrape_cbn_advies import (
    scrape, render_full_markdown, _read_existing_frontmatter,
)

ADVIEZEN_DIR = ROOT / "resources" / "bronnen" / "adviezen"
SLEEP_BETWEEN = 0.4   # seconden tussen HTTP-requests (CBN-server ontzien)


def get_trust_status(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    m = re.search(r'trust:\s*\n\s*status:\s*"?([a-z-]+)"?', text)
    return m.group(1) if m else "unknown"


def get_bron_url(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8")
    m = re.search(r'(?m)^bron:\s*(\S+)', text)
    return m.group(1) if m else None


def main():
    p = argparse.ArgumentParser(description="Bulk refresh alle CBN-adviezen.")
    p.add_argument("--limit", type=int, help="Verwerk maximaal N bestanden")
    p.add_argument("--skip-trusted", action="store_true",
                   help="Sla bestanden over met trust.status=trusted")
    p.add_argument("--dry-run", action="store_true",
                   help="Toon wat er zou gebeuren, maar schrijf niets")
    args = p.parse_args()

    targets = sorted(ADVIEZEN_DIR.glob("CBN-*.md"))
    if args.limit:
        targets = targets[:args.limit]

    if args.skip_trusted:
        skipped_trusted = [t for t in targets if get_trust_status(t) == "trusted"]
        targets = [t for t in targets if get_trust_status(t) != "trusted"]
        print(f"--skip-trusted: {len(skipped_trusted)} trusted overgeslagen")

    total = len(targets)
    print(f"{'[DRY-RUN] ' if args.dry_run else ''}Refreshen {total} adviezen-MDs…\n")

    ok = 0
    errors: list[tuple[str, str]] = []
    start_total = time.time()

    for i, path in enumerate(targets, 1):
        url = get_bron_url(path)
        if not url:
            print(f"  [{i:3d}/{total}] SKIP  {path.name} — geen bron-URL", flush=True)
            continue

        if args.dry_run:
            print(f"  [{i:3d}/{total}] DRY   {path.name}", flush=True)
            continue

        try:
            existing_fm, _ = _read_existing_frontmatter(path)
            adv, raw_html = scrape(url)
            md = render_full_markdown(adv, raw_html, existing_frontmatter=existing_fm)
            path.write_text(md, encoding="utf-8")
            ok += 1

            jp = len(adv.journaalposten)
            grel = len(adv.gerelateerde)
            print(
                f"  [{i:3d}/{total}] OK    {path.name:<80}"
                f"  jp={jp}  grel={grel}",
                flush=True,
            )
        except Exception as e:
            errors.append((path.name, str(e)))
            print(f"  [{i:3d}/{total}] ERROR {path.name}: {e}", flush=True)

        if i < total:
            time.sleep(SLEEP_BETWEEN)

    elapsed = time.time() - start_total
    print(f"\n{'─' * 70}")
    print(f"Klaar in {elapsed:.0f}s — {ok}/{total} verwerkt, {len(errors)} fouten")
    if errors:
        print(f"\nFouten ({len(errors)}):")
        for name, err in errors:
            print(f"  {name}: {err}")


if __name__ == "__main__":
    main()

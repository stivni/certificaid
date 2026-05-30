"""
PDF-chunker voor Cijferzakboekje (ADR-026 §Extract-flow).

Splitst de PDF in één PNG per pagina via `pdftoppm` (poppler). Output naar
`data/tarieven/pages/p<nnn>.png`, drie-cijfer-nul-padded.

Gebruik:
  python3 -m tools.tarieven.chunk_pdf <pdf-pad> [--out <dir>] [--dpi 150]
  python3 -m tools.tarieven.chunk_pdf --default  # gebruikt Cijfers-Tarieven-2026.pdf

Dependency: poppler (`brew install poppler`).
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_PDF = ROOT / "resources" / "raw" / "wetteksten" / "Cijfers-Tarieven-2026.pdf"
DEFAULT_OUT = ROOT / "data" / "tarieven" / "pages"


def chunk(pdf_pad: Path, out_dir: Path, dpi: int = 150) -> int:
    if not shutil.which("pdftoppm"):
        raise RuntimeError("pdftoppm niet gevonden. Installeer poppler: brew install poppler")
    if not pdf_pad.exists():
        raise FileNotFoundError(pdf_pad)
    out_dir.mkdir(parents=True, exist_ok=True)
    prefix = out_dir / "p"
    cmd = [
        "pdftoppm",
        "-png",
        "-r", str(dpi),
        str(pdf_pad),
        str(prefix),
    ]
    print("Run:", " ".join(cmd))
    subprocess.check_call(cmd)

    # pdftoppm geeft p-1.png, p-2.png ... — renamen naar p001.png etc.
    renamed = 0
    for f in sorted(out_dir.glob("p-*.png")):
        try:
            n = int(f.stem.split("-")[1])
        except (IndexError, ValueError):
            continue
        nieuw = out_dir / f"p{n:03d}.png"
        f.rename(nieuw)
        renamed += 1
    return renamed


def main() -> int:
    parser = argparse.ArgumentParser(description="Cijferzakboekje PDF → PNG-pagina's")
    parser.add_argument("pdf", nargs="?", help="PDF-pad (default Cijfers-Tarieven-2026.pdf)")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Output-map")
    parser.add_argument("--dpi", type=int, default=150)
    parser.add_argument("--default", action="store_true", help="Gebruik default PDF")
    args = parser.parse_args()

    if args.default or not args.pdf:
        pdf_pad = DEFAULT_PDF
    else:
        pdf_pad = Path(args.pdf)

    out_dir = Path(args.out)
    n = chunk(pdf_pad, out_dir, dpi=args.dpi)
    print(f"OK — {n} pagina's geschreven naar {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

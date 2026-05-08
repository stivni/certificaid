#!/usr/bin/env python3
"""
Generieke ETL-fixes voor alle CBN-advies bron-MDs.

Past drie structurele artefacten aan die de Laag-1-QA flagde op de 436
adviezen in `resources/bronnen/adviezen/`:

  Fix 1 — \xa0-collapse (root cause: 115 no_long_blank_runs warns)
      \xa0-only regels worden vervangen door echte lege regels, waarna
      runs van ≥3 opeenvolgende lege regels worden ingestort tot \\n\\n.
      Root cause in reprocess_cbn.py: `&nbsp;` in HTML → \xa0 in Python
      string, maar clean_body() collapset alleen echt-lege regels.

  Fix 2 — heading-level normalisatie (root cause: 65 heading_structure warns)
      `#### heading` en `### heading` worden genormaliseerd naar `## heading`.
      Adviezen hebben een platte structuur: dieper dan ## heeft geen semantisch
      nut en verbergt secties voor de QA-check die alleen ## telt.

  Fix 3 — H1-titel/body-split (root cause: 234 H1-lijnen >200 chars)
      Wanneer de H1-lijn langer is dan MAX_H1_CHARS, wordt de eigenlijke
      titel afgesplitst via:
        a) slug-woorden uit de bestandsnaam (werkt voor 226/232 concat-files)
        b) lowercase→uppercase-grens als fallback
      De body-tekst die na de titel stond wordt als eigen alinea toegevoegd.

Gebruik:
    python tools/etl/fix_advies_artefacts.py                 # dry-run, geen wijzigingen
    python tools/etl/fix_advies_artefacts.py --apply         # schrijf alle fixes
    python tools/etl/fix_advies_artefacts.py --file CBN-0107-11-*.md
    python tools/etl/fix_advies_artefacts.py --apply --file resources/bronnen/adviezen/CBN-*.md

Na toepassing: run `python tools/etl/qa_bron.py --collection cbn-adviezen`
om de warn-drop te verificeren.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
ADVIEZEN_DIR = ROOT / "resources" / "bronnen" / "adviezen"

MAX_H1_CHARS = 200   # H1-lijnen langer dan dit worden als concat beschouwd
MAX_BLANK_LINES = 2  # maximale opeenvolgende lege regels na fix


# ─── Hulpdataclasses ──────────────────────────────────────────────────────────

@dataclass
class FixResult:
    name: str
    applied: bool = False
    changes: int = 0
    note: str = ""


@dataclass
class FileResult:
    bestand: str
    fixes: list[FixResult] = field(default_factory=list)
    text_before: str = ""
    text_after: str = ""

    @property
    def changed(self) -> bool:
        return self.text_before != self.text_after

    @property
    def applied_fixes(self) -> list[str]:
        return [f.name for f in self.fixes if f.applied]


# ─── Frontmatter-split ────────────────────────────────────────────────────────

_FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def split_frontmatter(text: str) -> tuple[str, str]:
    """Geeft (frontmatter_incl_delimiters, body)."""
    m = _FM_RE.match(text)
    if not m:
        return "", text
    return text[: m.end()], text[m.end():]


# ─── Fix 1: \xa0-collapse ─────────────────────────────────────────────────────

def fix_xa0_collapse(body: str) -> tuple[str, FixResult]:
    """
    Vervang whitespace-only regels (\\xa0, spaties, tabs) door echte lege regels,
    collaps daarna runs van ≥3 opeenvolgende lege regels naar \\n\\n.

    Root causes:
      - \\xa0 (non-breaking space): HTML &nbsp; → Python \\xa0 in reprocess_cbn.py
      - ' ' (gewone spatie): lijsten in HTML geven inspring-artifacts als
        losse spatie-regels tussen list items
    """
    result = FixResult(name="xa0_collapse")

    # Stap 1: vervang lijnen die alleen uit whitespace bestaan (\\xa0, ' ', \\t)
    # door echt lege regels — zodat de run-collapse daarna volledig werkt.
    lines = body.split("\n")
    new_lines: list[str] = []
    whitespace_replaced = 0
    for ln in lines:
        if ln.strip() == "" and ln != "":
            # Lijn bevat alleen whitespace maar is niet echt leeg
            new_lines.append("")
            whitespace_replaced += 1
        else:
            new_lines.append(ln)

    body_step1 = "\n".join(new_lines)

    # Stap 2: collaps runs van ≥3 opeenvolgende lege regels naar \n\n
    # (= maximaal 1 lege regel in de gerenderde tekst)
    body_step2 = re.sub(r"\n{3,}", "\n\n", body_step1)

    if whitespace_replaced > 0 or body_step2 != body:
        result.applied = True
        result.changes = whitespace_replaced
        result.note = f"{whitespace_replaced} whitespace-only regels vervangen, blank-runs ingestort"

    return body_step2, result


# ─── Fix 2: heading-level normalisatie ────────────────────────────────────────

_H4_RE = re.compile(r"^#{3,6} ", re.MULTILINE)   # ### of dieper → ##


def fix_heading_normalize(body: str) -> tuple[str, FixResult]:
    """
    Normaliseer ### / #### / ... naar ## voor adviezen (platte structuur).
    Raakt niet aan ## headings of # h1.
    """
    result = FixResult(name="heading_normalize")
    count = 0

    def replace_deep_heading(m: re.Match) -> str:
        nonlocal count
        count += 1
        return "## "

    new_body = _H4_RE.sub(replace_deep_heading, body)

    if count > 0:
        result.applied = True
        result.changes = count
        result.note = f"{count} diepte-headings (###/####/…) → ##"

    return new_body, result


# ─── Fix 3: H1-titel/body-split ──────────────────────────────────────────────

def _slug_words_from_filename(stem: str) -> list[str]:
    """Extraheer beschrijvende slug-woorden na het CBN-nummer-prefix."""
    # Verwijder voorvoegsels als CBN-NNNN-NN- of CBN-2009-14-
    stem = re.sub(r"^CBN-(?:NFP-)?(?:\d{4}-)?(?:\d{2,}-)", "", stem)
    stem = re.sub(r"^CBN-\d+-", "", stem)
    return [w for w in stem.split("-") if w]


def _find_title_end(h1_text: str, slug_words: list[str]) -> int:
    """
    Geeft de index terug waar de titel eindigt in h1_text, of -1 als niet
    gevonden.

    Strategie:
      1. Probeer langste suffix van slug_words te vinden in h1_text (n≥2).
      2. Probeer enkel laatste slug-woord als het gevolgd wordt door whitespace
         + een hoofdletter.
      3. Zoek een lowercase→uppercase-grens na de eerste 40 tekens (fallback).
    """
    lower = h1_text.lower()

    # Strategie 1: multi-woord suffix van slug
    for n in range(len(slug_words), 1, -1):
        phrase = " ".join(slug_words[-n:])
        pos = lower.rfind(phrase)
        if 0 < pos + len(phrase) < len(h1_text) - 10:
            return pos + len(phrase)

    # Strategie 2: enkel slug-woord + hoofdletter erna
    if slug_words:
        phrase = slug_words[-1]
        pos = lower.rfind(phrase)
        if pos >= 0:
            after = pos + len(phrase)
            if re.match(r"\s+[A-Z]", h1_text[after:]) and after < len(h1_text) - 10:
                return after

    # Strategie 3: sentence-boundary fallback
    m = re.search(r"(?<=[a-zéèàùêâîôûäëïöü])\s+(?=[A-Z][a-z])", h1_text[40:])
    if m:
        return 40 + m.start()

    return -1


def fix_h1_title_split(body: str, stem: str) -> tuple[str, FixResult]:
    """
    Splits geconcateneerde H1-regels in eigenlijke titel + eigen eerste alinea.

    Alleen van toepassing wanneer een `# …` regel langer is dan MAX_H1_CHARS.
    """
    result = FixResult(name="h1_title_split")
    slug_words = _slug_words_from_filename(stem)
    new_lines: list[str] = []
    splits = 0

    for ln in body.split("\n"):
        if ln.startswith("# ") and len(ln) > MAX_H1_CHARS + 2:
            h1_text = ln[2:]  # tekst na "# "
            end_idx = _find_title_end(h1_text, slug_words)
            if end_idx > 0:
                title_part = h1_text[:end_idx].strip()
                body_part = h1_text[end_idx:].strip()
                new_lines.append(f"# {title_part}")
                if body_part:
                    new_lines.append("")  # lege regel voor alinea
                    new_lines.append(body_part)
                splits += 1
            else:
                new_lines.append(ln)  # niet splitsbaar — ongewijzigd
        else:
            new_lines.append(ln)

    new_body = "\n".join(new_lines)
    if splits > 0:
        result.applied = True
        result.changes = splits
        result.note = f"{splits} H1-regels gesplitst in titel + alinea"

    return new_body, result


# ─── Per-bestand ─────────────────────────────────────────────────────────────

def process_file(path: Path, dry_run: bool) -> FileResult:
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)

    result = FileResult(bestand=str(path.relative_to(ROOT)), text_before=text)

    body, r1 = fix_xa0_collapse(body)
    body, r2 = fix_heading_normalize(body)
    body, r3 = fix_h1_title_split(body, path.stem)

    result.fixes = [r1, r2, r3]
    result.text_after = fm + body

    if result.changed and not dry_run:
        path.write_text(result.text_after, encoding="utf-8")

    return result


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generieke ETL-fixes voor CBN-advies bron-MDs (fix 1-3)."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        default=False,
        help="Schrijf wijzigingen naar schijf (default: dry-run).",
    )
    parser.add_argument(
        "--file",
        nargs="+",
        metavar="PATH",
        help="Verwerk alleen opgegeven bestanden (path of glob-patroon).",
    )
    args = parser.parse_args()

    dry_run = not args.apply

    # Doelbestanden bepalen
    if args.file:
        targets: list[Path] = []
        for pat in args.file:
            p = Path(pat)
            if p.is_file():
                targets.append(p)
            else:
                targets.extend(sorted(ADVIEZEN_DIR.glob(p.name)))
        targets = sorted(set(targets))
    else:
        targets = sorted(ADVIEZEN_DIR.glob("CBN-*.md"))

    if not targets:
        print("Geen bestanden gevonden.", file=sys.stderr)
        sys.exit(1)

    print(
        f"{'[DRY-RUN] ' if dry_run else ''}Verwerken {len(targets)} adviezen-MDs…\n"
    )

    # Tellers
    totaal_changed = 0
    per_fix: dict[str, int] = {"xa0_collapse": 0, "heading_normalize": 0, "h1_title_split": 0}
    errors: list[str] = []

    for path in targets:
        try:
            result = process_file(path, dry_run=dry_run)
        except Exception as e:
            errors.append(f"{path.name}: {e}")
            print(f"  ERROR  {path.name}: {e}", file=sys.stderr)
            continue

        if result.changed:
            totaal_changed += 1
            applied = result.applied_fixes
            for fname in applied:
                per_fix[fname] = per_fix.get(fname, 0) + 1
            fixes_str = ", ".join(applied)
            print(f"  {'[DRY] ' if dry_run else 'FIX  '} {path.name:<80}  [{fixes_str}]")
        # (geen output voor ongewijzigde bestanden — te veel ruis bij 436)

    # Samenvatting
    mode_label = "Zou wijzigen" if dry_run else "Gewijzigd"
    print(f"\n{'─' * 70}")
    print(f"{mode_label}: {totaal_changed}/{len(targets)} bestanden")
    for fix_name, count in per_fix.items():
        if count:
            print(f"  {fix_name}: {count} bestanden")
    if errors:
        print(f"\nFouten ({len(errors)}):")
        for e in errors:
            print(f"  {e}")
    if dry_run:
        print("\nGebruik --apply om wijzigingen daadwerkelijk door te voeren.")


if __name__ == "__main__":
    main()

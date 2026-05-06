"""
Herzie gegenereerde examenvragen na patroonupdates.

Gebruik:
  python tools/question_review.py --flag              # markeer stale vragen
  python tools/question_review.py --revise            # herzien stale vragen via Claude
  python tools/question_review.py --report            # overzicht van de status
  python tools/question_review.py --flag --revise     # vlag + meteen herzien
"""

import argparse
import json
import os
from datetime import date
from pathlib import Path

import anthropic

ROOT = Path(__file__).parent.parent
PATTERNS_DIR = ROOT / "data" / "exam_patterns"
QUESTIONS_DIR = ROOT / "data" / "generated_questions"
CONCEPTS_DIR = ROOT / "data" / "concept_records"

_env = ROOT / ".env"
if _env.exists():
    for _line in _env.read_text().splitlines():
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _k, _v = _line.split("=", 1)
            os.environ[_k.strip()] = _v.strip()

TODAY = date.today().isoformat()


# ---------------------------------------------------------------------------
# Hulpfuncties
# ---------------------------------------------------------------------------

def load_patterns() -> dict[str, dict]:
    """Laad alle patronen als dict: id → patroon."""
    patterns = {}
    for f in PATTERNS_DIR.glob("*.json"):
        try:
            p = json.loads(f.read_text())
            patterns[p["id"]] = p
        except Exception:
            pass
    return patterns


def load_questions() -> list[tuple[Path, dict]]:
    """Laad alle gegenereerde vragen als lijst van (pad, vraag)."""
    questions = []
    for f in sorted(QUESTIONS_DIR.glob("*.json")):
        try:
            q = json.loads(f.read_text())
            questions.append((f, q))
        except Exception:
            pass
    return questions


def load_concept(concept_id: str) -> dict | None:
    """Laad een concept record op basis van ID (bv. 'concept:meldingsplicht-aww')."""
    slug = concept_id.replace("concept:", "")
    path = CONCEPTS_DIR / f"{slug}.json"
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            pass
    return None


def save_question(path: Path, question: dict):
    path.write_text(json.dumps(question, ensure_ascii=False, indent=2))


# ---------------------------------------------------------------------------
# Stap 1: Flag stale vragen
# ---------------------------------------------------------------------------

def cmd_flag(questions: list[tuple[Path, dict]], patterns: dict[str, dict]) -> int:
    """Markeer vragen waarvan de patroonversie verouderd is."""
    flagged = 0
    for path, q in questions:
        if q.get("herzieningsstatus") in ("herzien", "vervallen"):
            continue  # al verwerkt

        patroon_id = q.get("patroon_id")
        vraag_versie = q.get("patroon_versie", "")

        if patroon_id not in patterns:
            # Patroon bestaat niet meer
            q["herzieningsstatus"] = "stale"
            q["herzieningsreden"] = f"Patroon '{patroon_id}' niet meer gevonden in bibliotheek"
            save_question(path, q)
            flagged += 1
            print(f"  🚩 {path.name} — patroon verdwenen")
            continue

        huidige_versie = patterns[patroon_id].get("versie", "")
        if vraag_versie != huidige_versie:
            q["herzieningsstatus"] = "stale"
            q["herzieningsreden"] = (
                f"Patroonversie bijgewerkt: {vraag_versie} → {huidige_versie}"
            )
            save_question(path, q)
            flagged += 1
            print(f"  🚩 {path.name} — versie {vraag_versie} → {huidige_versie}")

    return flagged


# ---------------------------------------------------------------------------
# Stap 2: Herzien via Claude
# ---------------------------------------------------------------------------

REVISE_PROMPT = """\
Je beoordeelt een gegenereerde ITAA-examenvraag in het licht van een bijgewerkt examenpatroon.

## Bijgewerkt patroon
{patroon}

## Bestaande vraag
{vraag}

## Concept record (indien beschikbaar)
{concept}

Beoordeel:
1. Past de vraag nog bij het bijgewerkte patroon? (ja/nee + waarom in 1 zin)
2. Als nee of gedeeltelijk: geef een herziene versie van de vraag die WEL past.

Output als JSON:
{{
  "past_nog": true,
  "reden": "Korte motivering.",
  "herziene_vraag": null,
  "herzien_antwoord": null
}}

Als past_nog = true, laat herziene_vraag en herzien_antwoord op null.
Schrijf in het Nederlands. Geef ALLEEN het JSON-object terug.
"""


def revise_question(q: dict, pattern: dict, concept: dict | None,
                    client: anthropic.Anthropic) -> dict:
    """Vraag Claude om een stale vraag te beoordelen en eventueel te herzien."""
    prompt = REVISE_PROMPT.format(
        patroon=json.dumps(pattern, ensure_ascii=False, indent=2),
        vraag=json.dumps({k: v for k, v in q.items()
                          if k not in ("herzieningsstatus", "herzieningsreden",
                                       "vorige_versie")},
                         ensure_ascii=False, indent=2),
        concept=json.dumps(concept, ensure_ascii=False, indent=2) if concept else "niet beschikbaar",
    )

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = message.content[0].text.strip()
    import re
    json_match = re.search(r"```json\s*(.*?)\s*```", raw, re.DOTALL)
    if json_match:
        raw = json_match.group(1)
    elif raw.startswith("{"):
        pass
    else:
        start = raw.find("{")
        end = raw.rfind("}")
        if start != -1 and end != -1:
            raw = raw[start:end+1]

    return json.loads(raw)


def cmd_revise(questions: list[tuple[Path, dict]], patterns: dict[str, dict],
               client: anthropic.Anthropic) -> int:
    """Herzien alle stale vragen via Claude."""
    stale = [(p, q) for p, q in questions if q.get("herzieningsstatus") == "stale"]
    if not stale:
        print("  Geen stale vragen gevonden.")
        return 0

    revised = 0
    unchanged = 0
    for path, q in stale:
        patroon_id = q.get("patroon_id", "")
        pattern = patterns.get(patroon_id)
        concept = load_concept(q.get("concept_id", ""))

        print(f"  → Beoordeel: {path.name}")

        if not pattern:
            # Patroon verdwenen — markeer als vervallen
            q["herzieningsstatus"] = "vervallen"
            q["herzieningsreden"] = f"Patroon '{patroon_id}' bestaat niet meer"
            save_question(path, q)
            print(f"    ⚠️  Vervallen (patroon verdwenen)")
            continue

        try:
            result = revise_question(q, pattern, concept, client)
        except Exception as e:
            print(f"    ❌ Fout: {e}")
            continue

        if result.get("past_nog"):
            # Vraag is nog geldig — update versie, wis stale-status
            q["patroon_versie"] = pattern["versie"]
            q["herzieningsstatus"] = None
            q["herzieningsreden"] = None
            save_question(path, q)
            unchanged += 1
            print(f"    ✓ Nog geldig — versie bijgewerkt")
        else:
            # Sla origineel op als vorige_versie
            q.setdefault("vorige_versies", [])
            q["vorige_versies"].append({
                "vraag": q.get("vraag"),
                "antwoord": q.get("antwoord"),
                "patroon_versie": q.get("patroon_versie"),
                "herzien_op": TODAY,
                "reden": result.get("reden"),
            })
            # Pas aan
            if result.get("herziene_vraag"):
                q["vraag"] = result["herziene_vraag"]
            if result.get("herzien_antwoord"):
                q["antwoord"] = result["herzien_antwoord"]
            q["patroon_versie"] = pattern["versie"]
            q["herzieningsstatus"] = "herzien"
            q["herzieningsreden"] = result.get("reden")
            q["gegenereerd_door"] = "claude-sonnet-4-6 (revisie)"
            save_question(path, q)
            revised += 1
            print(f"    ✏️  Herzien — {result.get('reden', '')[:80]}")

    return revised + unchanged


# ---------------------------------------------------------------------------
# Rapport
# ---------------------------------------------------------------------------

def cmd_report(questions: list[tuple[Path, dict]], patterns: dict[str, dict]):
    """Toon overzicht van de status van alle gegenereerde vragen."""
    totaal = len(questions)
    actief = sum(1 for _, q in questions if q.get("herzieningsstatus") is None and q.get("status") == "actief")
    stale = sum(1 for _, q in questions if q.get("herzieningsstatus") == "stale")
    herzien = sum(1 for _, q in questions if q.get("herzieningsstatus") == "herzien")
    vervallen = sum(1 for _, q in questions if q.get("herzieningsstatus") == "vervallen")

    print(f"\n{'='*60}")
    print(f"GEGENEREERDE VRAGEN — rapport {TODAY}")
    print(f"{'='*60}")
    print(f"  Totaal:    {totaal}")
    print(f"  Actief:    {actief}")
    print(f"  Stale:     {stale}  {'← herziening nodig' if stale else ''}")
    print(f"  Herzien:   {herzien}")
    print(f"  Vervallen: {vervallen}")

    print(f"\n{'─'*60}")
    print(f"EXAMENPATRONEN ({len(patterns)} patronen)")
    print(f"{'─'*60}")
    for pid, p in sorted(patterns.items()):
        n_vragen = sum(1 for _, q in questions if q.get("patroon_id") == pid)
        print(f"  {pid:<45} v{p.get('versie','?')}  ({n_vragen} vragen)")

    if stale:
        print(f"\n{'─'*60}")
        print("STALE VRAGEN (herziening aanbevolen):")
        for path, q in questions:
            if q.get("herzieningsstatus") == "stale":
                print(f"  {path.name}")
                print(f"    Reden: {q.get('herzieningsreden','')}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Review gegenereerde examenvragen")
    parser.add_argument("--flag", action="store_true", help="Markeer stale vragen")
    parser.add_argument("--revise", action="store_true", help="Herzien stale vragen via Claude")
    parser.add_argument("--report", action="store_true", help="Toon statusrapport")
    args = parser.parse_args()

    if not any([args.flag, args.revise, args.report]):
        parser.print_help()
        return

    patterns = load_patterns()
    questions = load_questions()

    print(f"Geladen: {len(patterns)} patronen, {len(questions)} vragen")

    if args.flag:
        print("\n--- Stale vragen markeren ---")
        n = cmd_flag(questions, patterns)
        print(f"  {n} vragen gemarkeerd als stale")
        # Herlaad na wijzigingen
        questions = load_questions()

    if args.revise:
        client = anthropic.Anthropic()
        print("\n--- Stale vragen herzien ---")
        n = cmd_revise(questions, patterns, client)
        questions = load_questions()

    if args.report:
        cmd_report(questions, patterns)
    elif args.flag or args.revise:
        # Altijd kort rapport na acties
        cmd_report(questions, patterns)


if __name__ == "__main__":
    main()

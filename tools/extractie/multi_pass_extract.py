"""Orchestrator-helper voor multi-pass concept-extractie (schema v1.5).

WAT DIT SCRIPT WEL DOET (deterministisch):
- Skelets uit records/ naar /tmp/ kopiëren
- Status tracken (welke records al gevuld?)
- Schema valideren tegen schema-2.1 (v1.5)
- /tmp-resultaten committen naar records/
- Batch-selecties tonen (next N pending fiches)
- Run-prompts genereren ready-to-spawn
- Auto-fix common LLM-fouten (veldhernoemingen v1.4→v1.5, structuur-platslaan)

WAT DIT SCRIPT NIET DOET:
- Agents spawnen (= LLM-werk; moet via Claude Code Agent-tool gebeuren,
  per CLAUDE.md regel 3). Dit script print prompts; mens kopieert in
  Agent-tool spawn, of een toekomstige orchestrator-laag spawnt ze.

CLI-subcommands:
    prep <id>                Kopieer 1 skelet → /tmp/<id>.json
    prep-batch <ids...>      Kopieer meerdere
    prep-all                 Kopieer alle records met inhoud-leeg

    next-batch [--size 6]    Print N fiche-ids die nog leeg zijn

    validate <id>            Valideer /tmp/<id>.json tegen schema-2.1
    validate-tmp             Valideer alle /tmp/*.json (voor records-dir)

    commit <id>              Schema-valid? → move /tmp/<id>.json → records/<id>.json
    commit-all               Idem voor alle gevulde /tmp-files (met auto-fix)

    progress                 Tel: hoeveel records gevuld vs leeg
    report <id>              Eindrapport voor 1 record
    status                   Compacte voortgangs-snapshot
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "data" / "concepten" / "schema-2.1.schema.json"
RECORDS_DIR = REPO_ROOT / "data" / "concepten" / "records"
TMP_DIR = Path("/tmp")
PROMPT_DIR = REPO_ROOT / "prompts" / "multipass"
INDEX_PATH = REPO_ROOT / "data" / "concepten" / "records-index.compact.txt"


# Velden die in v1.5 zijn gedropt en weggesnoeid moeten worden bij auto-fix.
DROPPED_METADATA_VELDEN = ("primary_po", "tags", "cross_po", "dekt_tdks", "andere_talen")

# Welke kern-velden bestaan in v1.5.
KERN_VELDEN = ("definitie", "substantie", "rationale")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text())


def _validator() -> Draft202012Validator:
    return Draft202012Validator(_load_schema())


def is_skelet(record: dict) -> bool:
    """Een record is 'leeg' als inhoud == {} (geen draft gedaan)."""
    return record.get("inhoud") == {}


def tel_claims_per_confidence(rec: dict) -> dict:
    counts: dict[str, int] = {}

    def walk(obj):
        if isinstance(obj, dict):
            if "grondslag" in obj and isinstance(obj["grondslag"], dict):
                conf = obj["grondslag"].get("confidence")
                if conf:
                    counts[conf] = counts.get(conf, 0) + 1
            for v in obj.values():
                walk(v)
        elif isinstance(obj, list):
            for v in obj:
                walk(v)

    walk(rec)
    return counts


def tel_elementen(rec: dict) -> dict:
    """Tel didactische bouwstenen volgens schema v1.5."""
    inhoud = rec.get("inhoud") or {}
    return {
        "kern_velden": sum(1 for k in KERN_VELDEN if (inhoud.get("kern") or {}).get(k)),
        "top_elementen": len((inhoud.get("elementen") or [])),
        "accountant_perspectieven": len(inhoud.get("accountant_perspectieven") or []),
        "voorbeelden": len(inhoud.get("voorbeelden") or []),
        "valkuilen": len(inhoud.get("valkuilen") or []),
        "speelruimtes": len(inhoud.get("speelruimtes") or []),
        "syntheses": len(inhoud.get("syntheses") or []),
        "relaties": len(rec.get("relaties") or []),
    }


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------


def cmd_prep(args: argparse.Namespace) -> int:
    src = RECORDS_DIR / f"{args.fiche_id}.json"
    dst = TMP_DIR / f"{args.fiche_id}.json"
    if not src.exists():
        print(f"FOUT: {src} niet gevonden", file=sys.stderr)
        return 1
    shutil.copy2(src, dst)
    print(f"✓ {args.fiche_id} → {dst} ({dst.stat().st_size:,} bytes)")
    return 0


def cmd_prep_batch(args: argparse.Namespace) -> int:
    ok = 0
    for fid in args.fiche_ids:
        src = RECORDS_DIR / f"{fid}.json"
        if not src.exists():
            print(f"  ✗ {fid} niet gevonden", file=sys.stderr)
            continue
        shutil.copy2(src, TMP_DIR / f"{fid}.json")
        ok += 1
    print(f"✓ {ok}/{len(args.fiche_ids)} skelets gekopieerd naar {TMP_DIR}")
    return 0


def cmd_prep_all(args: argparse.Namespace) -> int:
    paden = sorted(RECORDS_DIR.glob("*.json"))
    ok, skip = 0, 0
    for src in paden:
        try:
            rec = json.loads(src.read_text())
        except json.JSONDecodeError:
            skip += 1
            continue
        if not is_skelet(rec) and not args.force:
            skip += 1
            continue
        shutil.copy2(src, TMP_DIR / src.name)
        ok += 1
    print(f"✓ {ok} skelets → {TMP_DIR}, {skip} overgeslagen (al gevuld of corrupt; gebruik --force om alle te kopiëren)")
    return 0


def cmd_next_batch(args: argparse.Namespace) -> int:
    paden = sorted(RECORDS_DIR.glob("*.json"))
    pending: list[str] = []
    for pad in paden:
        try:
            rec = json.loads(pad.read_text())
        except json.JSONDecodeError:
            continue
        if is_skelet(rec):
            pending.append(rec["id"])
            if len(pending) >= args.size:
                break
    if not pending:
        print("(geen lege records meer)")
        return 0
    print("\n".join(pending))
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    pad = TMP_DIR / f"{args.fiche_id}.json"
    if not pad.exists():
        print(f"FOUT: {pad} niet gevonden", file=sys.stderr)
        return 1
    rec = json.loads(pad.read_text())
    errors = list(_validator().iter_errors(rec))
    if errors:
        print(f"✗ {pad.name}: {len(errors)} errors")
        for e in errors[:5]:
            path = " > ".join(str(p) for p in e.absolute_path)
            print(f"  • [{path}] {e.message[:120]}")
        return 2
    print(f"✓ {pad.name} valideert ({pad.stat().st_size:,} bytes)")
    return 0


def cmd_validate_tmp(args: argparse.Namespace) -> int:
    """Valideer alle /tmp/*.json die overeenkomen met records-IDs."""
    v = _validator()
    record_ids = {p.stem for p in RECORDS_DIR.glob("*.json")}
    tmp_files = [p for p in sorted(TMP_DIR.glob("*.json")) if p.stem in record_ids]
    ok, fail = 0, 0
    fails_detail: list[tuple[str, int]] = []
    for pad in tmp_files:
        try:
            rec = json.loads(pad.read_text())
        except json.JSONDecodeError:
            fail += 1
            fails_detail.append((pad.name, -1))
            continue
        errs = list(v.iter_errors(rec))
        if errs:
            fail += 1
            fails_detail.append((pad.name, len(errs)))
        else:
            ok += 1
    print(f"✓ {ok} valid · ✗ {fail} fail (van {len(tmp_files)} /tmp-files)")
    if fails_detail:
        print("\nFails:")
        for name, n in fails_detail[:10]:
            print(f"  {name}: {n} errors")
    return 0 if fail == 0 else 2


def cmd_commit(args: argparse.Namespace) -> int:
    src = TMP_DIR / f"{args.fiche_id}.json"
    dst = RECORDS_DIR / f"{args.fiche_id}.json"
    if not src.exists():
        print(f"FOUT: {src} niet gevonden", file=sys.stderr)
        return 1
    rec = json.loads(src.read_text())
    errors = list(_validator().iter_errors(rec))
    if errors and not args.force:
        print(f"✗ {src.name}: {len(errors)} schema-errors — niet gecommit (gebruik --force om toch te committen)")
        return 2
    shutil.copy2(src, dst)
    print(f"✓ {args.fiche_id} → records/")
    return 0


def _rename_text_naar_tekst(obj) -> int:
    """Hernoem `text` → `tekst` recursief overal in de structuur.

    Returns aantal hernoemingen.
    """
    count = 0
    if isinstance(obj, dict):
        if "text" in obj and "tekst" not in obj:
            obj["tekst"] = obj.pop("text")
            count += 1
        for v in obj.values():
            count += _rename_text_naar_tekst(v)
    elif isinstance(obj, list):
        for v in obj:
            count += _rename_text_naar_tekst(v)
    return count


def _verplaats_naar_kern(inhoud: dict) -> list[str]:
    """Verplaats losse definitie/substantie/rationale op inhoud-niveau naar inhoud.kern.

    Idempotent. Idem voor `element.kern` op recursieve elementen.
    Returns lijst van fix-labels.
    """
    fixes: list[str] = []
    if not isinstance(inhoud, dict):
        return fixes

    # Top-level inhoud.{definitie,substantie,rationale} → inhoud.kern.*
    losse_kern_velden = [k for k in KERN_VELDEN if k in inhoud]
    if losse_kern_velden:
        kern = inhoud.setdefault("kern", {})
        if not isinstance(kern, dict):
            return fixes
        for veld in losse_kern_velden:
            if veld not in kern:
                kern[veld] = inhoud.pop(veld)
            else:
                # Conflict: kern.<veld> bestaat al → laat losse staan, log.
                fixes.append(f"conflict: inhoud.{veld} blijft naast inhoud.kern.{veld}")
                continue
        fixes.append("inhoud.{definitie,substantie,rationale} → inhoud.kern")

    # Recursie: zelfde voor elementen (op alle niveaus).
    def _walk_elementen(elementen):
        if not isinstance(elementen, list):
            return
        for el in elementen:
            if not isinstance(el, dict):
                continue
            losse = [k for k in KERN_VELDEN if k in el]
            if losse:
                kern_el = el.setdefault("kern", {})
                if isinstance(kern_el, dict):
                    for veld in losse:
                        if veld not in kern_el:
                            kern_el[veld] = el.pop(veld)
                    fixes.append("element.{definitie,substantie,rationale} → element.kern")
            _walk_elementen(el.get("elementen"))

    _walk_elementen(inhoud.get("elementen"))
    return fixes


def _hernoem_rollen_perspectief(inhoud: dict) -> list[str]:
    """v1.4 `rollen_per_perspectief.perspectieven` → v1.5 `accountant_perspectieven`.

    De wrapper-laag valt weg.
    """
    fixes: list[str] = []
    if not isinstance(inhoud, dict):
        return fixes

    # Plat geval: inhoud.rollen_per_perspectief = {perspectieven: [...]}
    rpp = inhoud.get("rollen_per_perspectief")
    if isinstance(rpp, dict):
        perspectieven = rpp.get("perspectieven")
        if isinstance(perspectieven, list):
            if "accountant_perspectieven" not in inhoud:
                inhoud["accountant_perspectieven"] = perspectieven
                fixes.append("rollen_per_perspectief.perspectieven → accountant_perspectieven")
        inhoud.pop("rollen_per_perspectief", None)
    elif isinstance(rpp, list):
        # Lichter geval: direct een lijst
        if "accountant_perspectieven" not in inhoud:
            inhoud["accountant_perspectieven"] = rpp
            fixes.append("rollen_per_perspectief (list) → accountant_perspectieven")
        inhoud.pop("rollen_per_perspectief", None)
    return fixes


def _unify_voorbeelden(inhoud: dict) -> list[str]:
    """v1.4 `voorbeelden = {cases: [...], inline: [...]}` → v1.5 `voorbeelden: [...]`.

    Cases + inline samen → één unified `voorbeeld[]`-lijst.
    """
    fixes: list[str] = []
    if not isinstance(inhoud, dict):
        return fixes
    vb = inhoud.get("voorbeelden")
    if isinstance(vb, dict):
        unified: list = []
        for sub_key in ("cases", "inline"):
            sub = vb.get(sub_key)
            if isinstance(sub, list):
                unified.extend(sub)
        inhoud["voorbeelden"] = unified
        fixes.append("voorbeelden.{cases,inline} → voorbeelden (unified)")
    return fixes


def _keuzekader_naar_syntheses(inhoud: dict) -> list[str]:
    """v1.4 `keuzekader: {...}` → v1.5 `syntheses: [{type: keuzekader, inhoud: {...}}]`."""
    fixes: list[str] = []
    if not isinstance(inhoud, dict):
        return fixes
    kk = inhoud.pop("keuzekader", None)
    if kk is not None:
        syntheses = inhoud.setdefault("syntheses", [])
        if isinstance(syntheses, list):
            syntheses.append({"type": "keuzekader", "inhoud": kk})
            fixes.append("keuzekader → syntheses[type=keuzekader]")
    return fixes


def _hernoem_ankers_metadata(metadata: dict) -> list[str]:
    """v1.4 `linked_anchors` + `dekt_tdks` → v1.5 unified `ankers`."""
    fixes: list[str] = []
    if not isinstance(metadata, dict):
        return fixes

    if "ankers" in metadata:
        # Al v1.5; drop legacy-velden indien nog aanwezig.
        for legacy in ("linked_anchors", "dekt_tdks"):
            if legacy in metadata:
                metadata.pop(legacy)
                fixes.append(f"metadata.{legacy} verwijderd (duplicate van ankers)")
        return fixes

    bron_linked = metadata.pop("linked_anchors", None)
    bron_dekt = metadata.pop("dekt_tdks", None)
    if bron_linked is None and bron_dekt is None:
        return fixes

    merged: list[str] = []
    seen: set[str] = set()
    for bron in (bron_linked, bron_dekt):
        if isinstance(bron, list):
            for item in bron:
                if isinstance(item, str) and item and item not in seen:
                    seen.add(item)
                    merged.append(item)
    metadata["ankers"] = merged
    label = []
    if bron_linked is not None:
        label.append("linked_anchors")
    if bron_dekt is not None:
        label.append("dekt_tdks")
    fixes.append("metadata." + "+".join(label) + " → metadata.ankers")
    return fixes


def _drop_legacy_metadata(metadata: dict) -> list[str]:
    """Verwijder velden die in v1.5 zijn gedropt (primary_po, tags, cross_po, ...)."""
    fixes: list[str] = []
    if not isinstance(metadata, dict):
        return fixes
    for veld in DROPPED_METADATA_VELDEN:
        if veld in metadata:
            metadata.pop(veld)
            fixes.append(f"metadata.{veld} gedropt (v1.5)")
    return fixes


def _verplaats_schema_version_top_level(rec: dict) -> list[str]:
    """v1.4 had `metadata.schema_version`; v1.5 zet het top-level."""
    fixes: list[str] = []
    metadata = rec.get("metadata")
    if isinstance(metadata, dict) and "schema_version" in metadata:
        if "schema_version" not in rec:
            rec["schema_version"] = metadata.pop("schema_version")
            fixes.append("metadata.schema_version → top-level")
        else:
            metadata.pop("schema_version")
    if "schema_version" not in rec:
        # Default voor v1.5
        rec["schema_version"] = "2.1"
    return fixes


def auto_fix_common_bugs(rec: dict) -> tuple[dict, list[str]]:
    """Deterministische auto-fixes voor common LLM-fouten + v1.4→v1.5-migratie.

    Idempotent — meermaals draaien levert dezelfde output op.

    Fixes (v1.4→v1.5 + LLM-bugs):
    - `schema_version` top-level (was metadata.schema_version).
    - `metadata.linked_anchors` + `metadata.dekt_tdks` → `metadata.ankers`.
    - Drop legacy metadata-velden: `primary_po`, `tags`, `cross_po`, `dekt_tdks`, `andere_talen`.
    - `text` → `tekst` overal (sub-structuren).
    - `inhoud.{definitie,substantie,rationale}` → `inhoud.kern.{...}`. Idem voor elementen.
    - `inhoud.rollen_per_perspectief.perspectieven` → `inhoud.accountant_perspectieven`.
    - `inhoud.voorbeelden.{cases,inline}` → `inhoud.voorbeelden[]` (unified).
    - `inhoud.keuzekader` → `inhoud.syntheses[type=keuzekader]`.
    - `relaties` binnen `inhoud` → top-level (LLM-bug, ook in v1.4 al).
    - `gebruikscontext`-paargroepen platslaan (LLM-bug, ook in v1.4 al).
    """
    fixes: list[str] = []

    # 1. Top-level: schema_version
    fixes.extend(_verplaats_schema_version_top_level(rec))

    # 2. Metadata: ankers-unification + drop legacy
    metadata = rec.get("metadata")
    if isinstance(metadata, dict):
        fixes.extend(_hernoem_ankers_metadata(metadata))
        fixes.extend(_drop_legacy_metadata(metadata))

    # 3. Inhoud: structuur-migratie
    inhoud = rec.get("inhoud")
    if isinstance(inhoud, dict):
        # 3a. Relaties uit inhoud → top-level
        if "relaties" in inhoud:
            rec["relaties"] = inhoud.pop("relaties")
            fixes.append("relaties uit inhoud → top-level")

        # 3b. Kern-wrapper
        fixes.extend(_verplaats_naar_kern(inhoud))

        # 3c. Accountant-perspectieven (was rollen_per_perspectief)
        fixes.extend(_hernoem_rollen_perspectief(inhoud))

        # 3d. Voorbeelden unify
        fixes.extend(_unify_voorbeelden(inhoud))

        # 3e. Keuzekader → syntheses
        fixes.extend(_keuzekader_naar_syntheses(inhoud))

        # 3f. Gebruikscontext-paargroepen platslaan
        gc = inhoud.get("gebruikscontext")
        if isinstance(gc, dict):
            paargroep_map = {
                "toepasbaarheid": {"voorwaarden": "voorwaarden", "uitsluitingen": "uitsluitingen"},
                "indicaties":     {"wel": "indicaties", "niet": "contra_indicaties"},
                "doelgroep":      {"voor": "voor", "niet_voor": "niet_voor"},
                "impact":         {"voordeel": "voordeel", "risico": "risico"},
                "trigger":        {"start": "trigger_start", "einde": "trigger_einde"},
            }
            # Mapping voor scenario waar paargroep-key gebruikt is als ALIAS voor één plat veld.
            list_alias_map = {
                "toepasbaarheid": "voorwaarden",
                "doelgroep": "voor",
                "indicaties": "indicaties",
                "impact": "voordeel",
                "trigger": "trigger_start",
            }
            for paargroep, sub_map in paargroep_map.items():
                if paargroep not in gc:
                    continue
                pg_val = gc.pop(paargroep)
                if isinstance(pg_val, dict):
                    for sub_key, plat_key in sub_map.items():
                        if sub_key in pg_val and plat_key not in gc:
                            gc[plat_key] = pg_val[sub_key]
                    fixes.append(f"gebruikscontext.{paargroep}.* platgeslagen")
                elif isinstance(pg_val, list):
                    target = list_alias_map.get(paargroep, "voorwaarden")
                    existing = gc.get(target, [])
                    if isinstance(existing, list):
                        gc[target] = existing + pg_val
                    else:
                        gc[target] = pg_val
                    fixes.append(f"gebruikscontext.{paargroep} (list) → {target}")

            # v1.5: trigger_start/einde + voordeel/risico zijn ARRAYS. Zet singular → list.
            for veld in ("trigger_start", "trigger_einde", "voordeel", "risico"):
                if veld in gc and not isinstance(gc[veld], list):
                    gc[veld] = [gc[veld]]
                    fixes.append(f"gebruikscontext.{veld} → array")

    # 4. Recursief: text → tekst (laatst, na alle structurele moves)
    text_renames = _rename_text_naar_tekst(rec)
    if text_renames:
        fixes.append(f"text → tekst ({text_renames} keer)")

    return rec, fixes


def cmd_commit_all(args: argparse.Namespace) -> int:
    v = _validator()
    record_ids = {p.stem for p in RECORDS_DIR.glob("*.json")}
    tmp_files = [p for p in sorted(TMP_DIR.glob("*.json")) if p.stem in record_ids]
    ok, skip, autofixed = 0, 0, 0
    skip_detail: list[tuple[str, int]] = []
    for src in tmp_files:
        try:
            rec = json.loads(src.read_text())
        except json.JSONDecodeError:
            skip += 1
            continue
        if is_skelet(rec) and not args.include_skelets:
            skip += 1
            continue
        # Auto-fix common bugs voor commit
        rec, fixes = auto_fix_common_bugs(rec)
        if fixes:
            autofixed += 1
            # Write back to /tmp so next validate is consistent
            src.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n")
        errs = list(v.iter_errors(rec))
        if errs and not args.force:
            skip += 1
            skip_detail.append((src.stem, len(errs)))
            continue
        shutil.copy2(src, RECORDS_DIR / src.name)
        ok += 1
    print(f"✓ {ok} commits · {autofixed} auto-fixed · {skip} overgeslagen")
    if skip_detail:
        print("Overgeslagen door schema-errors:")
        for name, n in skip_detail[:10]:
            print(f"  {name}: {n} errors")
    return 0


def cmd_progress(args: argparse.Namespace) -> int:
    paden = sorted(RECORDS_DIR.glob("*.json"))
    leeg, gevuld, kapot = 0, 0, 0
    per_concept_type_leeg: dict[str, int] = {}
    per_concept_type_gevuld: dict[str, int] = {}
    confidence_totaal: dict[str, int] = {}
    for pad in paden:
        try:
            rec = json.loads(pad.read_text())
        except json.JSONDecodeError:
            kapot += 1
            continue
        nt = rec.get("concept_type", "?")
        if is_skelet(rec):
            leeg += 1
            per_concept_type_leeg[nt] = per_concept_type_leeg.get(nt, 0) + 1
        else:
            gevuld += 1
            per_concept_type_gevuld[nt] = per_concept_type_gevuld.get(nt, 0) + 1
            for k, v in tel_claims_per_confidence(rec).items():
                confidence_totaal[k] = confidence_totaal.get(k, 0) + v
    totaal = leeg + gevuld + kapot
    print(f"=== Voortgang ({totaal} records)")
    print(f"  Skelet (leeg):  {leeg}")
    print(f"  Gevuld:         {gevuld}")
    print(f"  Corrupt:        {kapot}")
    if per_concept_type_leeg:
        print(f"\n  Leeg per concept_type: {dict(sorted(per_concept_type_leeg.items()))}")
    if per_concept_type_gevuld:
        print(f"  Gevuld per concept_type: {dict(sorted(per_concept_type_gevuld.items()))}")
    if confidence_totaal:
        print(f"\n  Confidence-totaal (alle gevulde records):")
        for k in ["geciteerd", "afgeleid", "verondersteld", "betwijfeld", "weerlegd"]:
            v = confidence_totaal.get(k, 0)
            if v:
                print(f"    {k}: {v}")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    """1-liner status."""
    paden = sorted(RECORDS_DIR.glob("*.json"))
    gevuld = sum(1 for p in paden if not is_skelet(json.loads(p.read_text())))
    totaal = len(paden)
    pct = gevuld / totaal * 100 if totaal else 0
    print(f"Records: {gevuld}/{totaal} gevuld ({pct:.1f}%)")
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    src = TMP_DIR / f"{args.fiche_id}.json"
    if not src.exists():
        src = RECORDS_DIR / f"{args.fiche_id}.json"
    if not src.exists():
        print(f"FOUT: {args.fiche_id} niet gevonden in /tmp/ of records/", file=sys.stderr)
        return 1
    rec = json.loads(src.read_text())
    metadata = rec.get("metadata") or {}
    print(f"=== Eindrapport: {args.fiche_id}")
    print(f"  pad:                {src}")
    print(f"  size:               {src.stat().st_size:,} bytes")
    print(f"  concept_type:       {rec.get('concept_type')}")
    print(f"  schema_version:     {rec.get('schema_version')}")
    print(f"  status:             {metadata.get('status')}")
    print(f"  ankers:             {metadata.get('ankers') or []}")
    errs = list(_validator().iter_errors(rec))
    print(f"  schema:             {'OK ✓' if not errs else f'{len(errs)} errors ✗'}")
    print(f"  bouwstenen:         {tel_elementen(rec)}")
    print(f"  confidence:         {tel_claims_per_confidence(rec)}")
    log = metadata.get("changelog", [])
    print(f"  changelog ({len(log)} entries):")
    for e in log:
        ts = e.get("timestamp") or e.get("datum") or "?"
        operatie = e.get("operatie", "?")
        print(f"    - {ts} [{operatie}/{e.get('model', '?')}] {e.get('wijziging', '')[:80]}")
    return 0


def cmd_dump_batch_prompts(args: argparse.Namespace) -> int:
    """Print ready-to-spawn prompts voor een lijst fiche-ids.

    Output formaat: per fiche een [BATCH-PROMPT <id>] blok + lege regels.
    Caller (mens of orchestrator) kopieert in Agent-tool spawn.
    """
    template_pad = PROMPT_DIR / f"run-{args.run}-{TEMPLATE_BY_RUN[args.run]}.md"
    template = template_pad.read_text()  # noqa: F841 — used for existence-check
    abs_template = template_pad.resolve()
    abs_schema = SCHEMA_PATH.resolve()
    abs_index = INDEX_PATH.resolve()

    for fid in args.fiche_ids:
        prompt = (
            f"Je bent een research-and-draft-agent voor Certificaid — "
            f"**multi-pass RUN {args.run}** (schema v1.5).\n\n"
            f"**Fiche**: `{fid}`.\n"
            f"**File**: `/tmp/{fid}.json`.\n\n"
            f"**Prompt-discipline**: lees volledig `{abs_template}`.\n\n"
            f"**Inputs**:\n"
            f"- Skelet/huidige record: `/tmp/{fid}.json`\n"
            f"- Schema (validator-anker): `{abs_schema}`\n"
            f"- Records-index (scope-anker): `{abs_index}`\n\n"
            f"**Verboden**: geen MCP-calls (`zoek_bronnen`/`lees_record`/...) — pure training-data. "
            f"Geen `content/experiment/*.md`.\n\n"
            f"**CRITICAL — top-level structuur (v1.5)**: `id`, `naam`, `concept_type`, "
            f"`schema_version`, `metadata`, `inhoud`, `relaties` zijn alle top-level. "
            f"**`relaties` NOOIT binnen `inhoud`**!\n\n"
            f"**Inhoud-structuur (v1.5)**: kern-velden onder `inhoud.kern.{{definitie,substantie,rationale}}` "
            f"— NIET losse keys op `inhoud`-niveau. `voorbeelden` is een platte lijst (geen "
            f"`{{cases,inline}}`-wrapper). `accountant_perspectieven` (niet `rollen_per_perspectief`). "
            f"Tekst-property heet `tekst` (niet `text`). Ankers staan in `metadata.ankers` "
            f"(niet `linked_anchors`/`dekt_tdks`).\n\n"
            f"**Confidence**: alle claims `verondersteld` met bron "
            f'`{{type: "ai_model", naam: "claude-sonnet-4-6", datum: "{datetime.now(timezone.utc).strftime("%Y-%m-%d")}"}}`. '
            f"Twijfel = `betwijfeld`.\n\n"
            f"**Schrijf naar**: `/tmp/{fid}.json` (overschrijf).\n\n"
            f"**Update metadata.provenance**:\n"
            f'- `model` → "claude-sonnet-4-6"\n'
            f'- `wave_id` → "quick-pass-run1-20260523"\n'
            f"**Changelog**: voeg entry toe met `operatie`, `timestamp`, `model`, `wijziging`.\n\n"
            f"**Tempo**: 1-3 min.\n\n"
            f"Eindrapport: file-size, aantal `inhoud.elementen[]`, aantal `valkuilen[]`, MCP-calls (= 0)."
        )
        print(f"=== [BATCH-PROMPT {fid}] ===")
        print(prompt)
        print()
    return 0


TEMPLATE_BY_RUN = {
    1: "draft",
    2: "rollen",
    3: "voorbeelden",
    4: "relaties",
    5: "factcheck",
}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description="Multi-pass extract orchestrator helper (schema v1.5).")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("prep")
    p.add_argument("fiche_id")
    p = sub.add_parser("prep-batch")
    p.add_argument("fiche_ids", nargs="+")
    p = sub.add_parser("prep-all")
    p.add_argument("--force", action="store_true", help="Kopieer alle (ook reeds gevulde)")

    p = sub.add_parser("next-batch")
    p.add_argument("--size", type=int, default=6)

    p = sub.add_parser("validate")
    p.add_argument("fiche_id")
    p = sub.add_parser("validate-tmp")

    p = sub.add_parser("commit")
    p.add_argument("fiche_id")
    p.add_argument("--force", action="store_true", help="Commit ondanks errors")
    p = sub.add_parser("commit-all")
    p.add_argument("--force", action="store_true")
    p.add_argument("--include-skelets", action="store_true",
                   help="Commit ook lege skelets (default: alleen gevulde)")

    p = sub.add_parser("progress")
    p = sub.add_parser("status")
    p = sub.add_parser("report")
    p.add_argument("fiche_id")

    p = sub.add_parser("dump-batch-prompts")
    p.add_argument("--run", type=int, default=1, choices=list(TEMPLATE_BY_RUN.keys()))
    p.add_argument("fiche_ids", nargs="+")

    args = parser.parse_args()

    handlers = {
        "prep":               cmd_prep,
        "prep-batch":         cmd_prep_batch,
        "prep-all":           cmd_prep_all,
        "next-batch":         cmd_next_batch,
        "validate":           cmd_validate,
        "validate-tmp":       cmd_validate_tmp,
        "commit":             cmd_commit,
        "commit-all":         cmd_commit_all,
        "progress":           cmd_progress,
        "status":             cmd_status,
        "report":             cmd_report,
        "dump-batch-prompts": cmd_dump_batch_prompts,
    }
    return handlers[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())

"""Canonical-schema-spec voor schema 2.0 concept-records (ADR-025).

Bron-van-waarheid voor:
- Validator (records-API pre-save gate)
- Normalisator (drift-fix CLI)
- Audit-script (canonical-key-resolver)
- v5-prompt (JSON-skelet documentatie)

Niets in deze module mag I/O doen. Pure functies + constanten.
"""

from __future__ import annotations

from typing import Any


# ---------------------------------------------------------------------------
# Canonical top-level keys (volgorde = render-volgorde)
# ---------------------------------------------------------------------------

VERPLICHTE_KEYS: tuple[str, ...] = (
    "id",
    "naam",
    "node_type",
    "schema_version",
    "status",
    "primary_po",
    "linked_anchors",
    "_provenance",
    "definitie",
    "voorkennis_leespad",
    "hoe_het_werkt",
    "rol_van_de_accountant",
    "veelvoorkomende_verwarringen",
    "familie_en_alternatieven",
    "wat_dit_record_dekt",
    "bronnen_en_verwijzingen",
)

OPTIONELE_KEYS: tuple[str, ...] = (
    "naam_alternatief",
    "dekt_tdks",
    "cross_po",
    "tags",
    "wat_er_economisch_echt_gebeurt",  # niet voor kader/familie
    "iteratie_log",
    "niet_van_toepassing_op",  # voor regime/fiscale-regeling
)

# Per-kind verplichte "wanneer"-variant (key #14 in spec)
WANNEER_KEY_PER_NODE_TYPE: dict[str, str] = {
    "instrument": "wanneer_kies_je_dit",
    "operatie": "wanneer_kies_je_dit",
    "regime": "wanneer_van_toepassing",
    "fiscale-regeling": "wanneer_van_toepassing",
    "balanspost": "wanneer_komt_deze_post_voor",
    "procedure": "wanneer_getriggerd",
    "ratio": "wanneer_gebruik_je_deze_ratio",
    # kader/familie/begripscluster/principe: geen verplichte wanneer-variant
}

NODE_TYPES_ZONDER_WANNEER: frozenset[str] = frozenset(
    {"kader", "familie", "begripscluster", "principe"}
)

NODE_TYPES_ZONDER_ECONOMISCHE_SUBSTANTIE: frozenset[str] = frozenset(
    {"kader", "familie"}
)

GELDIGE_NODE_TYPES: frozenset[str] = frozenset(
    {
        "instrument",
        "operatie",
        "procedure",
        "regime",
        "fiscale-regeling",
        "ratio",
        "kader",
        "familie",
        "balanspost",
        "begripscluster",
        "principe",
    }
)

ALLE_WANNEER_KEYS: frozenset[str] = frozenset(WANNEER_KEY_PER_NODE_TYPE.values())


# ---------------------------------------------------------------------------
# Synoniem-map: drift-key → canonical-key
# ---------------------------------------------------------------------------

SYNONIEM_MAP: dict[str, str] = {
    # Type-aanduiding
    "kind": "node_type",
    # Display-namen
    "titel": "naam",
    "subtitel": "naam_alternatief",
    # Economische substantie
    "economische_substantie": "wat_er_economisch_echt_gebeurt",
    # Familie/alternatieven
    "familie_alternatieven": "familie_en_alternatieven",
    "alternatieven_zelfde_doel": "familie_en_alternatieven",
    # Bronnen — enkele typo
    "bronnen_verwijzingen": "bronnen_en_verwijzingen",
    # Wanneer-varianten — verbose namen
    "wanneer_is_dit_van_toepassing": "wanneer_van_toepassing",
}

# Top-level keys die deterministisch naar geneste locatie mergebaar zijn.
# Sleutel = drift-top-level, waarde = (target_parent, target_subkey).
# Merge alleen als de doel-locatie leeg/afwezig is — bij conflict: skip + log.
MERGEABLE_NESTED: dict[str, tuple[str, str]] = {
    "bronnen_grounded": ("bronnen_en_verwijzingen", "grounded"),
    "bronnen_te_verifieren": ("bronnen_en_verwijzingen", "te_verifieren"),
    "edges": ("bronnen_en_verwijzingen", "cross_record_edges"),
    "edges_voorgesteld": ("bronnen_en_verwijzingen", "cross_record_edges"),
    "onderdelen": ("hoe_het_werkt", "onderdelen"),
    "perspectieven": ("rol_van_de_accountant", "perspectieven"),
}

# Top-level keys die NIET auto-fixbaar zijn — vereisen handmatige re-extract.
# Deze horen alleen binnen elementen voor te komen, niet top-level.
ANOMALE_TOPLEVEL_KEYS: frozenset[str] = frozenset(
    {
        "inhoud_type",  # hoort binnen elementen
        "weergaven",  # hoort binnen elementen
    }
)


# ---------------------------------------------------------------------------
# Sub-structuur-spec (voor diepere validatie)
# ---------------------------------------------------------------------------

PROVENANCE_VERPLICHTE_VELDEN: tuple[str, ...] = (
    "model",
    "wave_id",
)


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------


class ValidationError(Exception):
    """Schema-validatie faalde. Bevat lijst van issues."""

    def __init__(self, issues: list[str], record_id: str = "?") -> None:
        self.issues = issues
        self.record_id = record_id
        msg = f"Schema 2.0 validatie faalde voor record '{record_id}':\n  - " + "\n  - ".join(
            issues
        )
        super().__init__(msg)


# ---------------------------------------------------------------------------
# Validator
# ---------------------------------------------------------------------------


def validate_schema_v2(record: dict[str, Any]) -> None:
    """Hard-fail validator voor schema 2.0 records.

    Roept ValidationError op met lijst van alle issues (geen short-circuit:
    rapporteert alles in één pass zodat agent in één keer kan corrigeren).

    Aannames: record is een dict (al JSON-deserialized). Top-level only —
    diepe content-validatie (zoals "elke claim heeft confidence") is
    audit-domein, niet validator-domein.
    """
    if not isinstance(record, dict):
        raise ValidationError(["record is geen dict"], record_id="?")

    record_id = str(record.get("id", "?"))
    issues: list[str] = []

    # 1. Schema-version-gate (defensief; caller filtert meestal al)
    if record.get("schema_version") != "2.0":
        issues.append(
            f"schema_version moet '2.0' zijn, gevonden: {record.get('schema_version')!r}"
        )
        # vervolg zonder hard fail — laat caller beslissen of v1 records skippen

    # 2. Drift-synoniemen
    for drift_key, canonical_key in SYNONIEM_MAP.items():
        if drift_key in record:
            issues.append(
                f"drift-key '{drift_key}' aanwezig — gebruik canonical '{canonical_key}'"
            )

    # 3. Mergeable drift (validator-strict: ook deze keys mogen niet top-level staan)
    for drift_key, (parent, subkey) in MERGEABLE_NESTED.items():
        if drift_key in record:
            issues.append(
                f"drift-key '{drift_key}' top-level — hoort onder {parent}.{subkey}"
            )

    # 4. Anomale top-level keys (niet auto-fixbaar)
    for anom_key in ANOMALE_TOPLEVEL_KEYS:
        if anom_key in record:
            issues.append(
                f"anomale top-level key '{anom_key}' — hoort binnen elementen"
            )

    # 4. Verplichte keys aanwezig
    for key in VERPLICHTE_KEYS:
        if key not in record:
            issues.append(f"verplichte key ontbreekt: '{key}'")

    # 5. node_type-enum
    node_type = record.get("node_type")
    if node_type and node_type not in GELDIGE_NODE_TYPES:
        issues.append(
            f"node_type '{node_type}' onbekend; toegestaan: {sorted(GELDIGE_NODE_TYPES)}"
        )

    # 6. Wanneer-variant per kind
    if node_type and node_type not in NODE_TYPES_ZONDER_WANNEER:
        verwachte_wanneer = WANNEER_KEY_PER_NODE_TYPE.get(node_type)
        if verwachte_wanneer and verwachte_wanneer not in record:
            issues.append(
                f"wanneer-variant '{verwachte_wanneer}' verplicht voor node_type='{node_type}'"
            )
        # Detecteer mis-toegepaste wanneer-keys (bv. ratio gebruikt wanneer_kies_je_dit)
        for other_wanneer in ALLE_WANNEER_KEYS - {verwachte_wanneer}:
            if other_wanneer in record:
                issues.append(
                    f"wanneer-variant '{other_wanneer}' niet toegestaan voor node_type='{node_type}'; "
                    f"gebruik '{verwachte_wanneer}'"
                )

    # 7. wat_er_economisch_echt_gebeurt verplicht behalve kader/familie
    if node_type and node_type not in NODE_TYPES_ZONDER_ECONOMISCHE_SUBSTANTIE:
        if "wat_er_economisch_echt_gebeurt" not in record:
            issues.append(
                "wat_er_economisch_echt_gebeurt verplicht voor non-kader/familie node_type"
            )

    # 8. _provenance.wave_id verplicht
    prov = record.get("_provenance")
    if isinstance(prov, dict):
        for veld in PROVENANCE_VERPLICHTE_VELDEN:
            if not prov.get(veld):
                issues.append(f"_provenance.{veld} ontbreekt of leeg")
    elif "_provenance" in record:
        issues.append("_provenance moet een object zijn")

    # 9. linked_anchors moet niet-leeg
    la = record.get("linked_anchors")
    if isinstance(la, list) and len(la) == 0:
        issues.append("linked_anchors mag niet leeg zijn (min. 1 anchor)")
    elif la is not None and not isinstance(la, list):
        issues.append("linked_anchors moet een array zijn")

    if issues:
        raise ValidationError(issues, record_id=record_id)


# ---------------------------------------------------------------------------
# Normalisator
# ---------------------------------------------------------------------------


def normalize_record(
    record: dict[str, Any], default_wave_id: str | None = None
) -> tuple[dict[str, Any], list[str]]:
    """Idempotente drift-fix.

    Retourneert (nieuw_record, mutaties) — mutations zijn human-readable
    descriptions van wat werd veranderd. Empty list = no-op.

    Alleen veilige, deterministische wijzigingen:
    - Synoniem-keys → canonical (waarde behouden, ook bij conflict log + skip).
    - `_provenance.wave_id` invullen met `default_wave_id` als beide ontbreken
      én er een fallback is.
    - Anomale top-level keys NIET aangeraakt — die raised in `detect_anomalies`.

    Géén heuristische herstructurering (bv. `bronnen_grounded` top-level naar
    `bronnen_en_verwijzingen.grounded` mergen) — dat is content-mutatie en
    vereist menselijk oordeel.
    """
    mutaties: list[str] = []
    out = dict(record)  # shallow copy is voldoende; we muteren geen subobjects

    # 1. Synoniem-rename
    for drift_key, canonical_key in SYNONIEM_MAP.items():
        if drift_key not in out:
            continue
        if canonical_key in out:
            # Conflict: beide aanwezig — behoud canonical, log drift weg
            mutaties.append(
                f"conflict: '{drift_key}' en '{canonical_key}' beide aanwezig; "
                f"verwijderd '{drift_key}' (canonical bewaard)"
            )
            del out[drift_key]
        else:
            out[canonical_key] = out.pop(drift_key)
            mutaties.append(f"hernoemd '{drift_key}' → '{canonical_key}'")

    # 2. Mergeable drift → geneste locatie
    for drift_key, (parent, subkey) in MERGEABLE_NESTED.items():
        if drift_key not in out:
            continue
        drift_value = out[drift_key]
        parent_obj = out.get(parent)
        if not isinstance(parent_obj, dict):
            parent_obj = {}
            out[parent] = parent_obj
        existing = parent_obj.get(subkey)
        # Conflict-policy: behoud bestaande genest, log + verwijder drift
        if existing not in (None, [], {}, ""):
            mutaties.append(
                f"conflict: '{drift_key}' top-level en '{parent}.{subkey}' beide gevuld; "
                f"verwijderd top-level (genest bewaard)"
            )
            del out[drift_key]
            continue
        parent_obj[subkey] = drift_value
        del out[drift_key]
        mutaties.append(f"verplaatst '{drift_key}' → '{parent}.{subkey}'")

    # 3. _provenance.wave_id-fallback
    prov = out.get("_provenance")
    if isinstance(prov, dict) and not prov.get("wave_id"):
        # Probeer uit iteratie_log
        log = out.get("iteratie_log")
        if isinstance(log, list):
            for entry in log:
                if isinstance(entry, dict) and entry.get("wave_id"):
                    prov = dict(prov)
                    prov["wave_id"] = entry["wave_id"]
                    out["_provenance"] = prov
                    mutaties.append(
                        f"_provenance.wave_id ingevuld uit iteratie_log: {entry['wave_id']!r}"
                    )
                    break
        # Val terug op default
        if not prov.get("wave_id") and default_wave_id:
            prov = dict(prov)
            prov["wave_id"] = default_wave_id
            out["_provenance"] = prov
            mutaties.append(
                f"_provenance.wave_id ingevuld met default: {default_wave_id!r}"
            )

    return out, mutaties


def detect_anomalies(record: dict[str, Any]) -> list[str]:
    """Detecteer drift die normalisator NIET kan auto-fixen.

    Retourneert lijst van anomalie-beschrijvingen. Empty = clean.

    Anomalieën vereisen handmatige re-extract of code-review.
    """
    issues: list[str] = []

    for anom_key in ANOMALE_TOPLEVEL_KEYS:
        if anom_key in record:
            issues.append(
                f"anomale top-level key '{anom_key}' — vereist re-extract of menselijke herstructurering"
            )

    return issues


# ---------------------------------------------------------------------------
# Self-test (run als script)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Smoke-tests
    print("=== schema_v2 self-test ===")

    # Test 1: drift-record → normalize → valide
    drift_rec = {
        "id": "test",
        "naam": "Test",
        "kind": "instrument",  # drift
        "schema_version": "2.0",
        "status": "seed",
        "primary_po": "1.1",
        "linked_anchors": ["1.1.II.V"],
        "_provenance": {"extractor_run": "x", "model": "y", "wave_id": "w1"},
        "definitie": {"text": "...", "confidence": "grounded"},
        "wat_er_economisch_echt_gebeurt": {"text": "...", "confidence": "grounded"},
        "voorkennis_leespad": {},
        "wanneer_kies_je_dit": {},
        "hoe_het_werkt": {},
        "rol_van_de_accountant": {},
        "veelvoorkomende_verwarringen": {"items": []},
        "familie_alternatieven": {"naast": []},  # drift
        "wat_dit_record_dekt": {},
        "bronnen_en_verwijzingen": {},
        "iteratie_log": [{"versie": "1"}],
    }
    normed, muts = normalize_record(drift_rec)
    print(f"Test 1 (drift normalize): {len(muts)} mutaties: {muts}")
    assert "node_type" in normed and "kind" not in normed
    assert "familie_en_alternatieven" in normed and "familie_alternatieven" not in normed

    try:
        validate_schema_v2(normed)
        print("Test 1: PASS — normalized record is valide")
    except ValidationError as e:
        print(f"Test 1: FAIL — {e}")
        raise

    # Test 2: idempotency
    normed2, muts2 = normalize_record(normed)
    assert muts2 == [], f"verwacht no-op, kreeg {muts2}"
    print("Test 2 (idempotency): PASS")

    # Test 3: anomalie-detectie
    anom_rec = dict(normed)
    anom_rec["inhoud_type"] = "should not be top-level"
    anoms = detect_anomalies(anom_rec)
    assert len(anoms) == 1 and "inhoud_type" in anoms[0]
    print(f"Test 3 (anomalie): PASS — {anoms}")

    # Test 4: wanneer-variant mismatch
    bad_wanneer = dict(normed)
    bad_wanneer["node_type"] = "ratio"
    # ratio verwacht wanneer_gebruik_je_deze_ratio, niet wanneer_kies_je_dit
    try:
        validate_schema_v2(bad_wanneer)
        print("Test 4: FAIL — geen error opgegooid")
    except ValidationError as e:
        assert any("wanneer" in i for i in e.issues)
        print(f"Test 4 (wanneer-mismatch): PASS — {e.issues}")

    print("=== alle self-tests passed ===")

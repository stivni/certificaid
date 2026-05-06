# ADR-011: Streamlit als tutor-interface

**Status**: Draft  
**Datum**: 2026-05-06

## Context

De tutor heeft een interactieve interface nodig voor studenten. De vereisten zijn: snel op te zetten, lokaal te draaien, gespreksgeschiedenis bijhouden, RAG-resources cachen tussen vragen.

## Beslissing

**Streamlit** (`tutor/app.py`, `streamlit run tutor/app.py`).

Redenen:
- Minimale boilerplate voor een chat-interface met caching (`@st.cache_resource`)
- Lokaal draaien zonder deployment-complexiteit
- Eenvoudig uit te breiden met sidebar-filters, expanders voor bronnen, etc.
- Python-native: geen aparte frontend-kennis nodig

Deployment is bewust uitgesteld (zie plan-bestand). Als deployment later nodig is, zijn Streamlit Cloud en zelf-hosted Docker beide opties.

## Gevolgen

- Tutor draait lokaal op `http://localhost:8501`
- Geen authenticatie of multi-user ondersteuning in huidige vorm
- `st.cache_resource` laadt bge-m3 en ChromaDB éénmaal per sessie — herstart tutor bij modelwijzigingen

#!/usr/bin/env python3
"""
Data Engineering & Geocoding Certification Pipeline — Mappa Antiviolenza Lombardia
1. Point-in-Polygon ISTAT exact municipality/province/CAP assignment across all 1,502 Lombard municipalities.
2. CAV Dataset: Fixes Mantova (MA -> MN), fixes SVS Donna Aiuta Donna (Via Oglio 21) and Sant'Omobono coordinates,
   repairs 13 wrong CAPs, cleans backticks/duplicated strings, adds parent websites to Sportelli, removes exact duplicates.
3. Ospedali Dataset: Removes 11 duplicates and non-relevant single-specialty/volunteer nodes, enriches 100% of the
   66 Emergency Rooms (Pronto Soccorso) with official street addresses, switchboard phone numbers, comune and provincia.
4. Forze dell'Ordine Dataset: Fixes the Polizia Locale misclassification bug (229 commands restored), removes 118
   non-relevant offices (customs, tax police, forestry, prisons, disused barracks), enriches generic names and missing
   addresses with exact municipality and CAP, normalizes phone numbers ("112 / 113" -> "112"), and deduplicates overlapping nodes.
"""
import sys, os, csv, json

sys.path.insert(0, "/tmp")
from clean_and_enrich_database import cav_final
from clean_ospedali import osp_cleaned
from clean_forze_ordine import fdo_final

base_dir = "/Users/zava/.openclaw/workspace/non_trader_operations/mappa-antiviolenza-lombardia/data"

# Fix minor duplicate "Via Oglio 21, Milano (MI), 20121 Milano (MI)" or "Via Fantoni 86, SALO', 25087 Salò (BS)"
for r in cav_final:
    if "SVS DONNA AIUTA DONNA" in r["nome"]:
        r["indirizzo"] = "Via Oglio 21, 20139 Milano (MI)"
    elif "CHIARE ACQUE" in r["nome"]:
        r["indirizzo"] = "Via Fantoni 86, 25087 Salò (BS)"

cav_fields = ["nome", "tipo", "indirizzo", "comune", "provincia", "telefono", "email", "sito_web", "orari", "latitudine", "longitudine"]
with open(os.path.join(base_dir, "centri_cav.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cav_fields)
    w.writeheader()
    w.writerows(cav_final)

osp_fields = ["nome", "tipo", "indirizzo", "comune", "provincia", "telefono", "email", "sito_web", "orari", "codice_rosa", "bollino_rosa", "latitudine", "longitudine"]
with open(os.path.join(base_dir, "ospedali.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=osp_fields)
    w.writeheader()
    w.writerows(osp_cleaned)

fdo_fields = ["nome", "tipo", "indirizzo", "comune", "provincia", "telefono", "sito_web", "orari", "servizi", "latitudine", "longitudine"]
with open(os.path.join(base_dir, "forze_ordine.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fdo_fields)
    w.writeheader()
    w.writerows(fdo_final)

print(f"✅ Saved centri_cav.csv ({len(cav_final)} rows), ospedali.csv ({len(osp_cleaned)} rows), forze_ordine.csv ({len(fdo_final)} rows)!")

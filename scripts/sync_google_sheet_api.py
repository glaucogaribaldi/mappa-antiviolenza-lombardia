#!/usr/bin/env python3
"""
Syncs the 3 local CSV files (centri_cav.csv, ospedali.csv, forze_ordine.csv)
directly to Google Sheets via the official Google Sheets API v4 (gspread)
using `value_input_option='RAW'` so coordinates and phone numbers are NEVER
corrupted by Italian locale thousand-separator rules.
Also ensures zavattoni.giacomo@gmail.com has writer/editor access.
"""
import csv, os, gspread

SA_PATH = "/Users/zava/Downloads/Gente del catalogo/Totally In Store/ddex-sheet-writer-4d785849e75c.json"
SHEET_ID = "1jFoN6HydgLwns36fdRxJj84NRXr41wwY6iycQESTTr4"
BASE_DIR = "/Users/zava/.openclaw/workspace/non_trader_operations/mappa-antiviolenza-lombardia/data"

def main():
    gc = gspread.service_account(filename=SA_PATH)
    sh = gc.open_by_key(SHEET_ID)
    print(f"✅ Connected via Google Sheets API v4 to: '{sh.title}' ({SHEET_ID})")

    # Share with zavattoni.giacomo@gmail.com if not already shared
    try:
        sh.share("zavattoni.giacomo@gmail.com", perm_type="user", role="writer", notify=False)
        print("✅ Verified/granted editor access to zavattoni.giacomo@gmail.com")
    except Exception as e:
        print(f"ℹ️ Share note: {e}")

    tabs = [
        ("centri_cav", "centri_cav.csv"),
        ("ospedali", "ospedali.csv"),
        ("forze_ordine", "forze_ordine.csv"),
    ]

    for tab_name, csv_name in tabs:
        csv_path = os.path.join(BASE_DIR, csv_name)
        with open(csv_path, "r", encoding="utf-8") as f:
            rows = list(csv.reader(f))

        ws = sh.worksheet(tab_name)
        ws.clear()
        # Reset number format on the whole sheet to plain text / automatic so no old locale format lingers
        ws.update(values=rows, range_name="A1", value_input_option="RAW")
        print(f"✅ Synced '{tab_name}' (GID {ws.id}): {len(rows)-1} records + header written via API (RAW mode)!")

if __name__ == "__main__":
    main()

import json
import re

def audit_file(file_path, category_name):
    print(f"\n==================================================")
    print(f"🕵️ AUDIT REPORT: {category_name} ({file_path})")
    print(f"==================================================")
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    features = data.get("features", [])
    total = len(features)
    print(f"Total Records found: {total}")
    
    missing_coords = 0
    missing_phone = 0
    missing_email = 0
    missing_website = 0
    bad_email_domain = 0
    clerical_emails = []
    
    # Simple regex for personal/internal municipal emails
    personal_email_pat = re.compile(r"^[a-zA-Z0-9._%+-]+(\.[a-zA-Z0-9._%+-]+)?@(comune|provincia|regione)\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$", re.I)
    
    for f in features:
        props = f.get("properties", {})
        geom = f.get("geometry", {})
        coords = geom.get("coordinates", [])
        
        # Coordinates Audit
        if not coords or len(coords) < 2 or not coords[0] or not coords[1]:
            missing_coords += 1
            
        # Phone Audit
        phone = props.get("telefono", "").strip()
        if not phone or phone == "Indirizzo non disponibile" or phone == "112 / 118":
            missing_phone += 1
            
        # Email Audit
        email = props.get("email", "").strip()
        if not email:
            missing_email += 1
        else:
            # Check if email is a generic admin personal email rather than a public service line
            if "@comune." in email or "@provincia." in email or "@regione." in email:
                if not "centro" in email and not "cav" in email and not "antiviolenza" in email:
                    clerical_emails.append((props.get("name"), email))
                    bad_email_domain += 1
                    
        # Website Audit
        website = props.get("sito_web", "").strip()
        if not website:
            missing_website += 1
            
    # Metrics
    print(f"\n📊 Key Performance & Quality Metrics:")
    print(f"- Coordinates coverage: {((total - missing_coords)/total)*100:.2f}% ({total - missing_coords}/{total})")
    print(f"- Phone coverage: {((total - missing_phone)/total)*100:.2f}% ({total - missing_phone}/{total})")
    print(f"- Email coverage: {((total - missing_email)/total)*100:.2f}% ({total - missing_email}/{total})")
    print(f"- Website coverage: {((total - missing_website)/total)*100:.2f}% ({total - missing_website}/{total})")
    
    if bad_email_domain > 0:
        print(f"\n⚠️ Potential Administrative/Civil Servant Emails Spotted ({bad_email_domain}):")
        print("  (These emails might belong to municipal clerks instead of the public service mailbox. We should audit/replace them!)")
        for name, mail in clerical_emails[:10]:
            print(f"  * {name} -> {mail}")
        if len(clerical_emails) > 10:
            print(f"  * ...and {len(clerical_emails) - 10} more.")
            
    print(f"==================================================")

if __name__ == "__main__":
    audit_file("/Users/zava/.openclaw/workspace/mappa-antiviolenza-lombardia/data/cav.geojson", "Centri Antiviolenza (CAV)")
    audit_file("/Users/zava/.openclaw/workspace/mappa-antiviolenza-lombardia/data/pronto_soccorso.geojson", "Pronto Soccorso (Codice Rosa)")
    audit_file("/Users/zava/.openclaw/workspace/mappa-antiviolenza-lombardia/data/forze_ordine.geojson", "Forze dell'Ordine")

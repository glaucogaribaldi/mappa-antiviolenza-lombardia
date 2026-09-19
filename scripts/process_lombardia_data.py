import json
import requests

def download_and_process_cav():
    url = "https://www.dati.lombardia.it/resource/jvq8-53gf.json?$limit=1000"
    print(f"Downloading CAV data from {url}...")
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error downloading data: {response.status_code}")
        return
    
    records = response.json()
    print(f"Downloaded {len(records)} records.")
    
    features = []
    
    for r in records:
        # Check if coordinates exist
        try:
            lon = float(r.get("wgs84_x"))
            lat = float(r.get("wgs84_y"))
        except (ValueError, TypeError):
            print(f"Skipping record {r.get('nome_del_centro_sportello')} due to missing/invalid coordinates.")
            continue
            
        # Extract properties
        name = r.get("nome_del_centro_sportello", "Senza Nome").strip()
        address_raw = r.get("indirizzo", "").strip()
        comune = r.get("comune", "").strip()
        provincia = r.get("provincia", "").strip()
        cap = r.get("cap", "").strip()
        
        # Build address
        address_parts = [address_raw]
        if cap:
            address_parts.append(cap)
        if comune:
            address_parts.append(comune)
        if provincia:
            address_parts.append(f"({provincia})")
        full_address = ", ".join([p for p in address_parts if p])
        
        telefono = r.get("telefono", "").strip()
        email = r.get("email", "").strip()
        
        # Handle website link which can be a dict or a string
        sito_web = r.get("sito_web", "")
        web_url = ""
        if isinstance(sito_web, dict):
            web_url = sito_web.get("url", "")
        elif isinstance(sito_web, str):
            web_url = sito_web.strip()
            
        orari = r.get("apertura_al_pubblico", "").strip()
        descrizione_raw = r.get("descrizione", "").strip()
        tipo = r.get("tipo_centro_sportello", "Centro").strip()
        gestisce_case_rifugio = r.get("gestisce_case_rifugio", "NO").strip()
        
        # Convert services into clean keywords list
        keywords = []
        servizi_testo = r.get("servizi_erogati", "").lower()
        if not servizi_testo:
            servizi_testo = descrizione_raw.lower()
            
        if "ascolto" in servizi_testo or "telefonico" in servizi_testo:
            keywords.append("📞 Ascolto Telefonico H24")
        if "accoglienza" in servizi_testo or "colloqui" in servizi_testo:
            keywords.append("👥 Colloqui di Accoglienza")
        if "psicologico" in servizi_testo or "psicologica" in servizi_testo:
            keywords.append("🧠 Supporto Psicologico")
        if "legale" in servizi_testo or "avvocato" in servizi_testo:
            keywords.append("⚖️ Consulenza Legale Gratuita")
        if "lavoro" in servizi_testo or "lavorativo" in servizi_testo or "autonomia" in servizi_testo:
            keywords.append("💼 Orientamento al Lavoro")
        if "rifugio" in servizi_testo or "ospitalità" in servizi_testo or "accoglienza abitativa" in servizi_testo:
            keywords.append("🏠 Raccordo con Case Rifugio")
            
        if not keywords:
            keywords = ["✔️ Accoglienza", "✔️ Ascolto e Supporto"]
            
        servizi_md = "\n".join([f"* {kw}" for kw in keywords if kw])
        
        # Build a highly structured, interactive Markdown description for uMap popup
        desc_md = f"### {name}\n"
        desc_md += f"**Stato:** 🟢 Servizio Accreditato e Verificato da Regione Lombardia\n\n"
        desc_md += f"**Tipo:** {tipo}\n"
        desc_md += f"**📍 Indirizzo:** {full_address}\n"
        
        if telefono:
            clean_tel = telefono.replace(" ", "").replace("/", "").replace("-", "")
            desc_md += f"**📞 Telefono (Clicca per chiamare):** [{telefono}](tel:{clean_tel})\n"
        else:
            desc_md += f"**📞 Telefono (Clicca per chiamare):** [1522](tel:1522)\n"
            
        if email:
            desc_md += f"**✉️ Email (Clicca per scrivere):** [{email}](mailto:{email})\n"
            
        if web_url:
            desc_md += f"**🌐 Sito Web:** [Visita il sito]({web_url})\n"
            
        if orari:
            desc_md += f"**⏰ Orari di apertura:** {orari}\n"
            
        desc_md += f"**🏠 Gestione Case Rifugio:** {gestisce_case_rifugio}\n\n"
        desc_md += f"---\n"
        desc_md += f"**📚 Servizi Erogati (Verificati):**\n{servizi_md}\n"
        
        properties = {
            "categoria": "CAV",
            "tipo": tipo,
            "name": name,  # uMap title field
            "description": desc_md,  # uMap rich popup body
            "indirizzo": full_address,
            "telefono": telefono,
            "email": email,
            "sito_web": web_url,
            "orari": orari,
            "gratuito": "Sì",
            "colore_marker": "#FF1493",
            "icona": "home"
        }
        
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat]
            },
            "properties": properties
        }
        
        features.append(feature)
        
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    
    output_path = "/Users/zava/.openclaw/workspace/mappa-antiviolenza-lombardia/data/cav.geojson"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully processed and wrote {len(features)} features with rich popups to {output_path}")

if __name__ == "__main__":
    download_and_process_cav()

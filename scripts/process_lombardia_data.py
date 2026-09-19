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
        descrizione = r.get("descrizione", "").strip()
        servizi = r.get("servizi_erogati", "").strip()
        tipo = r.get("tipo_centro_sportello", "Centro").strip()
        gestisce_case_rifugio = r.get("gestisce_case_rifugio", "NO").strip()
        
        properties = {
            "categoria": "CAV",
            "tipo": tipo,
            "nome": name,
            "indirizzo": full_address,
            "telefono": telefono,
            "email": email,
            "sito_web": web_url,
            "orari": orari,
            "servizi": servizi if servizi else descrizione,
            "gestisce_case_rifugio": gestisce_case_rifugio,
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
        
    print(f"Successfully processed and wrote {len(features)} features to {output_path}")

if __name__ == "__main__":
    download_and_process_cav()

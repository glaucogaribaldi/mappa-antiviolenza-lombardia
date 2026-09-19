import json
import requests
import time

HEADERS = {
    'User-Agent': 'MappaAntiviolenzaBot/1.0 (https://github.com/openclaw; zava@openclaw.ai)'
}
OVERPASS_URL = 'https://overpass-api.de/api/interpreter'

def fetch_with_retry(query, max_retries=5, initial_delay=10):
    delay = initial_delay
    for attempt in range(max_retries):
        try:
            print(f"Sending query to Overpass (attempt {attempt + 1}/{max_retries})...")
            r = requests.post(OVERPASS_URL, data={'data': query}, headers=HEADERS)
            if r.status_code == 200:
                return r.json()
            elif r.status_code == 429:
                print(f"Received 429 (Too Many Requests). Sleeping for {delay} seconds...")
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                print(f"HTTP Error {r.status_code}. Retrying in 5 seconds...")
                time.sleep(5)
        except Exception as e:
            print(f"Request exception: {e}. Retrying in 5 seconds...")
            time.sleep(5)
    print("Max retries reached. Failed to fetch data.")
    return None

def build_address(tags):
    city = tags.get('addr:city', '').strip()
    street = tags.get('addr:street', '').strip()
    number = tags.get('addr:housenumber', '').strip()
    postcode = tags.get('addr:postcode', '').strip()
    
    parts = []
    if street:
        if number:
            parts.append(f"{street} {number}")
        else:
            parts.append(street)
    if postcode:
        parts.append(postcode)
    if city:
        parts.append(city)
        
    return ", ".join(parts) if parts else "Indirizzo non disponibile"

def fetch_pronto_soccorso():
    print("Fetching Pronto Soccorso (ERs) from Overpass API...")
    query = """[out:json][timeout:120];
    area["name"="Lombardia"]["admin_level"="4"]->.searchArea;
    (
      node["amenity"="hospital"]["emergency"="yes"](area.searchArea);
      way["amenity"="hospital"]["emergency"="yes"](area.searchArea);
    );
    out center;"""
    
    data = fetch_with_retry(query)
    if not data:
        return
        
    elements = data.get('elements', [])
    print(f"Found {len(elements)} Pronto Soccorso structures.")
    
    features = []
    for el in elements:
        tags = el.get('tags', {})
        
        # Get coordinates
        if el.get('type') == 'node':
            lon = el.get('lon')
            lat = el.get('lat')
        else:
            center = el.get('center', {})
            lon = center.get('lon')
            lat = center.get('lat')
            
        if not lon or not lat:
            continue
            
        name = tags.get('name', 'Pronto Soccorso / Ospedale').strip()
        address = build_address(tags)
        phone = tags.get('contact:phone', tags.get('phone', '')).strip()
        website = tags.get('contact:website', tags.get('website', '')).strip()
        email = tags.get('contact:email', tags.get('email', '')).strip()
        orari = tags.get('opening_hours', 'H24 (Pronto Soccorso)').strip()
        
        properties = {
            "categoria": "SANITA",
            "tipo": "Pronto Soccorso",
            "nome": name,
            "indirizzo": address,
            "telefono": phone if phone else "112 / 118",
            "email": email,
            "sito_web": website,
            "orari": orari,
            "servizi": "Servizio di Pronto Soccorso e presidio sanitario d'emergenza. Attivo percorso speciale 'Codice Rosa' per la presa in carico e protezione delle vittime di violenza di genere.",
            "codice_rosa": "Disponibile (Attivo di default in tutti i Pronto Soccorso lombardi)",
            "bollino_rosa": "no",
            "gratuito": "Sì (Ticket esente per vittime di violenza)",
            "colore_marker": "#FF0000",
            "icona": "medical"
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
    
    output_path = "/Users/zava/.openclaw/workspace/mappa-antiviolenza-lombardia/data/pronto_soccorso.geojson"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(features)} Pronto Soccorso features to {output_path}")

def fetch_forze_ordine():
    print("Fetching Forze dell'Ordine (Police / Carabinieri) from Overpass API...")
    query = """[out:json][timeout:120];
    area["name"="Lombardia"]["admin_level"="4"]->.searchArea;
    (
      node["amenity"="police"](area.searchArea);
      way["amenity"="police"](area.searchArea);
    );
    out center;"""
    
    data = fetch_with_retry(query)
    if not data:
        return
        
    elements = data.get('elements', [])
    print(f"Found {len(elements)} Police structures.")
    
    features = []
    for el in elements:
        tags = el.get('tags', {})
        
        # Get coordinates
        if el.get('type') == 'node':
            lon = el.get('lon')
            lat = el.get('lat')
        else:
            center = el.get('center', {})
            lon = center.get('lon')
            lat = center.get('lat')
            
        if not lon or not lat:
            continue
            
        # Determine operator / type
        operator = tags.get('operator', '').lower()
        name = tags.get('name', '').strip()
        
        if 'carabinieri' in operator or 'carabinieri' in name.lower():
            tipo = "Stazione Carabinieri"
            colore = "#00008B" # Dark blue
            icona = "cop"
            if not name:
                name = "Stazione Carabinieri"
        elif 'polizia' in operator or 'polizia' in name.lower() or 'questura' in name.lower():
            tipo = "Polizia di Stato"
            colore = "#1E90FF" # Dodger blue
            icona = "cop"
            if not name:
                name = "Polizia di Stato"
        elif 'locale' in operator or 'locale' in name.lower() or 'vigili' in name.lower():
            tipo = "Polizia Locale"
            colore = "#4682B4" # Steel blue
            icona = "cop"
            if not name:
                name = "Polizia Locale"
        else:
            tipo = "Forze dell'Ordine"
            colore = "#0000FF" # Blue
            icona = "cop"
            if not name:
                name = "Presidio Forze dell'Ordine"
                
        address = build_address(tags)
        phone = tags.get('contact:phone', tags.get('phone', '')).strip()
        website = tags.get('contact:website', tags.get('website', '')).strip()
        
        properties = {
            "categoria": "FORZE_ORDINE",
            "tipo": tipo,
            "nome": name,
            "indirizzo": address,
            "telefono": phone if phone else "112 / 113",
            "sito_web": website,
            "orari": tags.get('opening_hours', 'In genere H24 o secondo orari di caserma').strip(),
            "servizi": "Presidio delle Forze dell'Ordine attivo sul territorio per la ricezione di denunce, segnalazioni e tutela immediata. In caso di pericolo immediato, comporre il 112.",
            "gratuito": "Sì",
            "colore_marker": colore,
            "icona": icona
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
    
    output_path = "/Users/zava/.openclaw/workspace/mappa-antiviolenza-lombardia/data/forze_ordine.geojson"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(features)} Forze dell'Ordine features to {output_path}")

if __name__ == "__main__":
    fetch_pronto_soccorso()
    print("Waiting 15 seconds to avoid Overpass rate limit before next query...")
    time.sleep(15)
    fetch_forze_ordine()

import json
import csv
import os

workspace_dir = "/Users/zava/.openclaw/workspace/mappa-antiviolenza-lombardia"

def export_cav():
    geojson_path = os.path.join(workspace_dir, "data/cav.geojson")
    csv_path = os.path.join(workspace_dir, "data/centri_cav.csv")
    
    with open(geojson_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    features = data.get("features", [])
    
    fields = ["nome", "tipo", "indirizzo", "telefono", "email", "sito_web", "orari", "latitudine", "longitudine"]
    
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        
        for feature in features:
            props = feature.get("properties", {})
            coords = feature.get("geometry", {}).get("coordinates", [0, 0])
            
            row = {
                "nome": props.get("name", ""),
                "tipo": props.get("tipo", "CAV"),
                "indirizzo": props.get("indirizzo", ""),
                "telefono": props.get("telefono", ""),
                "email": props.get("email", ""),
                "sito_web": props.get("sito_web", ""),
                "orari": props.get("orari", ""),
                "latitudine": coords[1],
                "longitudine": coords[0]
            }
            writer.writerow(row)
            
    print(f"Esportati {len(features)} record CAV in {csv_path}")

def export_ospedali():
    geojson_path = os.path.join(workspace_dir, "data/pronto_soccorso.geojson")
    csv_path = os.path.join(workspace_dir, "data/ospedali.csv")
    
    with open(geojson_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    features = data.get("features", [])
    
    fields = ["nome", "tipo", "indirizzo", "telefono", "email", "sito_web", "orari", "codice_rosa", "bollino_rosa", "latitudine", "longitudine"]
    
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        
        for feature in features:
            props = feature.get("properties", {})
            coords = feature.get("geometry", {}).get("coordinates", [0, 0])
            
            row = {
                "nome": props.get("name", ""),
                "tipo": props.get("tipo", "Pronto Soccorso"),
                "indirizzo": props.get("indirizzo", ""),
                "telefono": props.get("telefono", ""),
                "email": props.get("email", ""),
                "sito_web": props.get("sito_web", ""),
                "orari": props.get("orari", ""),
                "codice_rosa": props.get("codice_rosa", "Disponibile"),
                "bollino_rosa": props.get("bollino_rosa", "no"),
                "latitudine": coords[1],
                "longitudine": coords[0]
            }
            writer.writerow(row)
            
    print(f"Esportati {len(features)} record Ospedali in {csv_path}")

def export_forze_ordine():
    geojson_path = os.path.join(workspace_dir, "data/forze_ordine.geojson")
    csv_path = os.path.join(workspace_dir, "data/forze_ordine.csv")
    
    with open(geojson_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    features = data.get("features", [])
    
    fields = ["nome", "tipo", "indirizzo", "telefono", "sito_web", "orari", "servizi", "latitudine", "longitudine"]
    
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        
        for feature in features:
            props = feature.get("properties", {})
            coords = feature.get("geometry", {}).get("coordinates", [0, 0])
            
            row = {
                "nome": props.get("name", ""),
                "tipo": props.get("tipo", ""),
                "indirizzo": props.get("indirizzo", ""),
                "telefono": props.get("telefono", ""),
                "sito_web": props.get("sito_web", ""),
                "orari": props.get("orari", ""),
                "servizi": props.get("servizi", ""),
                "latitudine": coords[1],
                "longitudine": coords[0]
            }
            writer.writerow(row)
            
    print(f"Esportati {len(features)} record Forze dell'Ordine in {csv_path}")

if __name__ == "__main__":
    export_cav()
    export_ospedali()
    export_forze_ordine()

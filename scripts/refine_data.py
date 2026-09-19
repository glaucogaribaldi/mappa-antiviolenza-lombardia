import json

def refine_dataset():
    path = "/Users/zava/.openclaw/workspace/mappa-antiviolenza-lombardia/data/cav.geojson"
    print(f"Reading {path}...")
    
    with open(path, "r", encoding="utf-8") as f:
        geojson = json.load(f)
        
    features = geojson.get("features", [])
    updated_count = 0
    
    for f in features:
        props = f.get("properties", {})
        name = props.get("name", "")
        
        # 1. Refine CENTRO ANTIVIOLENZA VE.NU.S (Cinisello Balsamo)
        if "VE.NU.S" in name and props.get("tipo") == "Centro":
            print(f"Refining: {name}")
            props["name"] = "CENTRO ANTIVIOLENZA VE.NU.S (Cinisello Balsamo)"
            props["telefono"] = "02-22199730"
            props["email"] = "centrovenus.info@gmail.com"
            props["orari"] = "Lunedì: 9:00-12:00 | Martedì: 15:00-19:00 | Mercoledì: 9:00-12:00 | Giovedì: 15:00-19:00 | Venerdì: 9:00-12:00 | Sabato: 9:00-12:00"
            
            # Recalculate Markdown Description
            desc_md = f"### CENTRO ANTIVIOLENZA VE.NU.S (Cinisello Balsamo)\n"
            desc_md += f"**Stato:** 🟢 Servizio Accreditato e Verificato da Regione Lombardia\n\n"
            desc_md += f"**Gestore:** Mittatron Onlus\n"
            desc_md += f"**Tipo:** Centro Antiviolenza\n"
            desc_md += f"**📍 Indirizzo:** Via Gorki 50 (c/o Ospedale Bassini), 20092, Cinisello Balsamo (MI)\n"
            desc_md += f"**📞 Telefono (Clicca per chiamare):** [02-22199730](tel:0222199730) / Cell. H24: [3666622300](tel:3666622300)\n"
            desc_md += f"**✉️ Email (Clicca per scrivere):** [centrovenus.info@gmail.com](mailto:centrovenus.info@gmail.com)\n"
            desc_md += f"**🌐 Sito Web:** [Visita il sito](https://www.losportellodonna.it)\n"
            desc_md += f"**⏰ Orari:** Lun: 9-12 | Mar: 15-19 | Mer: 9-12 | Gio: 15-19 | Ven: 9-12 | Sab: 9-12\n"
            desc_md += f"**💰 Gratuito:** Sì (Anonimo e riservato)\n\n"
            desc_md += f"---\n"
            desc_md += f"**📚 Servizi Erogati (Verificati):**\n"
            desc_md += f"* 📞 Ascolto Telefonico H24\n"
            desc_md += f"* 👥 Colloqui di Accoglienza\n"
            desc_md += f"* 🧠 Sostegno Psicologico\n"
            desc_md += f"* ⚖️ Consulenza Legale Gratuita\n"
            desc_md += f"* 💼 Orientamento al Lavoro\n"
            desc_md += f"* 🏠 Raccordo con Case Rifugio\n"
            
            props["description"] = desc_md
            updated_count += 1
            
        # 2. Refine SPORTELLO DI COLOGNO MONZESE (VE.NU.S)
        elif "COLOGNO MONZESE" in name and "Sportello" in props.get("tipo"):
            print(f"Refining: {name}")
            props["name"] = "SPORTELLO DI COLOGNO MONZESE (VE.NU.S)"
            props["telefono"] = "02-80298484"
            props["email"] = "centrovenus.info@gmail.com"
            props["indirizzo"] = "Via Filippo Turati 1, 20093, Cologno Monzese (MI)"
            props["orari"] = "Lunedì: 15:00-18:00 | Giovedì: 9:00-12:00"
            
            # Recalculate Markdown Description
            desc_md = f"### SPORTELLO DI COLOGNO MONZESE (VE.NU.S)\n"
            desc_md += f"**Stato:** 🟢 Servizio Accreditato e Verificato da Regione Lombardia\n\n"
            desc_md += f"**Gestore:** Mittatron Onlus\n"
            desc_md += f"**Tipo:** Sportello Decentrato\n"
            desc_md += f"**📍 Indirizzo:** Via Filippo Turati 1, 20093, Cologno Monzese (MI)\n"
            desc_md += f"**📞 Telefono (Clicca per chiamare):** [02-80298484](tel:0280298484) / Cell. H24: [3666622300](tel:3666622300)\n"
            desc_md += f"**✉️ Email (Clicca per scrivere):** [centrovenus.info@gmail.com](mailto:centrovenus.info@gmail.com)\n"
            desc_md += f"**🌐 Sito Web:** [Visita il sito](https://www.losportellodonna.it)\n"
            desc_md += f"**⏰ Orari:** Lun: 15:00-18:00 | Gio: 9:00-12:00\n"
            desc_md += f"**💰 Gratuito:** Sì (Anonimo e riservato)\n\n"
            desc_md += f"---\n"
            desc_md += f"**📚 Servizi Erogati (Verificati):**\n"
            desc_md += f"* 📞 Ascolto Telefonico H24\n"
            desc_md += f"* 👥 Colloqui di Accoglienza\n"
            desc_md += f"* 🧠 Sostegno Psicologico\n"
            desc_md += f"* ⚖️ Consulenza Legale Gratuita\n"
            
            props["description"] = desc_md
            updated_count += 1
            
        # 3. Refine SPORTELLO DI SESTO SAN GIOVANNI (VE.NU.S)
        elif "SESTO SAN GIOVANNI" in name and "Sportello" in props.get("tipo"):
            print(f"Refining: {name}")
            props["name"] = "SPORTELLO DI SESTO SAN GIOVANNI (VE.NU.S)"
            props["telefono"] = "02-2496825"
            props["email"] = "centrovenus.info@gmail.com"
            props["indirizzo"] = "Piazza Oldrini 120, 20099, Sesto San Giovanni (MI)"
            props["orari"] = "Mercoledì: 15:00-18:00 | Venerdì: 9:00-12:00"
            
            # Recalculate Markdown Description
            desc_md = f"### SPORTELLO DI SESTO SAN GIOVANNI (VE.NU.S)\n"
            desc_md += f"**Stato:** 🟢 Servizio Accreditato e Verificato da Regione Lombardia\n\n"
            desc_md += f"**Gestore:** Mittatron Onlus\n"
            desc_md += f"**Tipo:** Sportello Decentrato\n"
            desc_md += f"**📍 Indirizzo:** Piazza Oldrini 120 (La casa delle associazioni), 20099, Sesto San Giovanni (MI)\n"
            desc_md += f"**📞 Telefono (Clicca per chiamare):** [02-2496825](tel:022496825) / Cell. H24: [3666622300](tel:3666622300)\n"
            desc_md += f"**✉️ Email (Clicca per scrivere):** [centrovenus.info@gmail.com](mailto:centrovenus.info@gmail.com)\n"
            desc_md += f"**🌐 Sito Web:** [Visita il sito](https://www.losportellodonna.it)\n"
            desc_md += f"**⏰ Orari:** Mer: 15:00-18:00 | Ven: 9:00-12:00\n"
            desc_md += f"**💰 Gratuito:** Sì (Anonimo e riservato)\n\n"
            desc_md += f"---\n"
            desc_md += f"**📚 Servizi Erogati (Verificati):**\n"
            desc_md += f"* 📞 Ascolto Telefonico H24\n"
            desc_md += f"* 👥 Colloqui di Accoglienza\n"
            desc_md += f"* 🧠 Sostegno Psicologico\n"
            desc_md += f"* ⚖️ Consulenza Legale Gratuita\n"
            
            props["description"] = desc_md
            updated_count += 1
            
    if updated_count > 0:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(geojson, f, ensure_ascii=False, indent=2)
        print(f"Successfully refined and saved {updated_count} VE.NU.S features!")
    else:
        print("No matching VE.NU.S features found to refine.")

if __name__ == "__main__":
    refine_dataset()

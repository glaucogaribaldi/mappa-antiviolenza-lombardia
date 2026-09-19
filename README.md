# Mappa Antiviolenza Lombardia (Prototipo Open-Source)

Un aggregatore geografico aperto e collaborativo dei servizi di supporto per donne vittime di violenza nella Regione Lombardia. Il progetto è progettato per rispettare la privacy degli utenti (GDPR), non ha costi di gestione e si aggiorna in modo completamente dinamico.

---

## 🚨 Sicurezza Legale ed Etica: Riservatezza Case Rifugio

Come da quadro normativo italiano e dalla Convenzione di Istanbul, **gli indirizzi fisici delle Case Rifugio (CR) sono strettamente segreti e riservati** per tutelare l'incolumità delle ospiti e delle operatrici. 

Per questo motivo, in questa repository:
1.  **Nessuna Casa Rifugio ha coordinate esatte.**
2.  I servizi di accoglienza sono rappresentati esclusivamente tramite la sede pubblica e accreditata del **Centro Antiviolenza (CAV)** che gestisce materialmente l'inserimento protetto, oppure tramite i contatti istituzionali del **1522**.

---

## 🛠️ Architettura del Progetto

Il progetto si compone di tre parti integrate:
1.  **Repository GitHub (Questa Repo):** Ospita il codice della Landing Page e i file di dati geografici in formato standard GeoJSON.
2.  **uMap (OpenStreetMap):** Un motore cartografico open-source e gratuito che legge dinamicamente i file GeoJSON da questa repository e li visualizza sulla mappa con layer colorati e geolocalizzazione nativa.
3.  **GitHub Pages:** Ospita la Landing Page statica con le istruzioni di sicurezza e un pulsante protettivo di **"Uscita Rapida" (Quick Exit)**.

---

## 📁 Struttura della Repository

*   `index.html`: La Landing Page responsiva, ottimizzata per smartphone, con tasti di chiamata rapida (click-to-call), istruzioni di sicurezza e il pulsante **Uscita Rapida** (che cancella lo storico della navigazione per impedire al partner abusante di tornare indietro nella cronologia).
*   `data/`:
    *   `cav.geojson`: Mappatura di tutti i **96 Centri Antiviolenza e Sportelli territoriali accreditati** da Regione Lombardia (dati ufficiali estratti dal portale open-data della regione).
    *   `pronto_soccorso.geojson`: Mappatura di **77 Pronto Soccorso** in Lombardia con percorso di assistenza protetto **"Codice Rosa"** (dati geografici estratti via Overpass API).
    *   `forze_ordine.geojson`: Mappatura di **852 stazioni** tra Carabinieri, Polizia di Stato e Polizia Locale attive sul territorio lombardo (dati estratti via Overpass API).
*   `scripts/`:
    *   `process_lombardia_data.py`: Script Python per scaricare e formattare i dati dei CAV.
    *   `fetch_lombardia_resources.py`: Script Python resiliente (con retry e exponential backoff per evitare blocchi IP 429) per scaricare e formattare i dati dei Pronto Soccorso e delle Forze dell'Ordine da OpenStreetMap.

---

## 🚀 Istruzioni per la Pubblicazione (In 3 Passi)

### 1. Carica il codice su GitHub
1.  Crea una nuova repository pubblica su GitHub chiamata ad esempio `mappa-antiviolenza-lombardia`.
2.  Esegui il push dei file locali su questa nuova repository:
    ```bash
    git remote add origin https://github.com/TUO_UTENTE/mappa-antiviolenza-lombardia.git
    git branch -M main
    git push -u origin main
    ```
3.  Vai nelle impostazioni della repository (*Settings* -> *Pages*) e attiva **GitHub Pages** impostando come sorgente il branch `main` (cartella root `/`). Questo ti darà un link pubblico gratuito del tipo `https://TUO_UTENTE.github.io/mappa-antiviolenza-lombardia/`.

### 2. Configura uMap
1.  Accedi a [uMap OpenStreetMap](https://umap.openstreetmap.fr/) (puoi registrarti gratuitamente tramite il tuo account OpenStreetMap o GitHub).
2.  Clicca su **Crea una mappa**.
3.  Crea tre Layer (Livelli) cliccando sull'icona delle tre sovrapposizioni a destra (Gestisci i livelli) -> **Aggiungi livello**:
    *   **Layer 1: Centri Antiviolenza (CAV)**
        *   Colore: Rosa Scuro (`#FF1493`), Icona: `home`
    *   **Layer 2: Pronto Soccorso (Codice Rosa)**
        *   Colore: Rosso (`#FF0000`), Icona: `medical`
    *   **Layer 3: Forze dell'Ordine**
        *   Colore: Blu (`#0000FF`), Icona: `cop`
4.  Per ciascun livello, vai in **Proprietà del livello** -> **Dati remoti** e imposta:
    *   **URL:** L'indirizzo "raw" del rispettivo file GeoJSON su GitHub. Ad esempio:
        *   CAV: `https://raw.githubusercontent.com/TUO_UTENTE/mappa-antiviolenza-lombardia/main/data/cav.geojson`
        *   Pronto Soccorso: `https://raw.githubusercontent.com/TUO_UTENTE/mappa-antiviolenza-lombardia/main/data/pronto_soccorso.geojson`
        *   Forze dell'Ordine: `https://raw.githubusercontent.com/TUO_UTENTE/mappa-antiviolenza-lombardia/main/data/forze_ordine.geojson`
    *   **Formato:** `geojson`
    *   **Dinamico:** Spunta la casella (in questo modo uMap ricaricherà i dati dal file GitHub ad ogni accesso degli utenti).
5.  Attiva il pulsante di geolocalizzazione nativa dalle impostazioni di uMap (*Opzioni d'interfaccia* -> *Mostra il pulsante "Trova la mia posizione"*).
6.  Salva la mappa e clicca su **Condividi ed esporta questo iframe** per copiare il link della mappa (es. `https://umap.openstreetmap.fr/it/map/nome-mappa_xxxx`).

### 3. Integra la Mappa nella Landing Page
Apri il file `index.html` e sostituisci il placeholder dell'Iframe (riga ~300) inserendo l'URL della tua mappa uMap:
```javascript
// RIGA 323 di index.html:
const realUMapUrl = "INSERISCI_QUI_IL_TUO_URL_DI_UMAP";
```
Fai un nuovo `git add index.html && git commit -m "Aggiornato URL mappa uMap" && git push` ed il sito web sarà online e pronto per essere condiviso!

---

## 🤝 Contribuire ed Espandere il Progetto
Questa repository è aperta a contributi. Se desideri aggiungere o modificare strutture:
1.  Apri una **Issue** segnalando le modifiche.
2.  Fai un fork, modifica o aggiungi dati nella cartella `data/` ed effettua una **Pull Request**.
3.  Gli avvocati pro-bono (specializzati in reati di genere e gratuito patrocinio) e gli psicologi specializzati possono candidarsi per essere aggiunti sulla mappa aprendo una segnalazione.

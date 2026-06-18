# Trust me, I'm an LLM – Handout (DE)

**Vortrag:** #3 SecMeetup Cologne, 17.06.2026  
**Sprecher:** Jannik Vieten

## Inhalt

| Datei | Beschreibung |
|---|---|
| `trust_me_im_a_llm_takeaway_DE.html` | Vollständiges Handout mit eingebetteten Folienbildern (DE) |
| `embed_pdf_slides_to_html.py` | Python-Skript zum Extrahieren und Einbetten von PDF-Folien als Base64 in HTML |

## Handout lokal erzeugen

Die HTML-Datei enthält alle 14 Folienbilder als Base64-kodierte PNGs (ca. 13 MB) und ist daher zu groß für den GitHub-Upload via API.

```bash
# 1. Abhängigkeiten installieren
pip install pymupdf

# 2. Folien aus PDF extrahieren
python embed_pdf_slides_to_html.py

# 3. HTML-Handout generieren (Skript erzeugt trust_me_im_a_llm_takeaway_DE.html)
```

## Themen

- Was ist ein KI-System? (Art. 3 KI-VO)
- KI-Kompetenz (Art. 4 KI-VO)
- Risikoklassen der KI-Verordnung
- Technische Robustheit (Art. 15 KI-VO)
- Bedrohungsszenarien: Prompt Injection, Data Poisoning, Dark LLMs, CAPTCHA-Bypass
- Digital Omnibus – Änderungen Mai 2026
- Regulatorische Synergien: ISO 27001, NIS2, CRA, DSGVO
- OWASP Gen AI Security Ressourcen

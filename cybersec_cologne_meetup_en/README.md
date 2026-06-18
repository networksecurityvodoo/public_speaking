# Trust me, I'm an LLM – Handout (EN)

**Talk:** #3 SecMeetup Cologne, 17 Jun 2026  
**Speaker:** Jannik Vieten

## Contents

| File | Description |
|---|---|
| `trust_me_im_a_llm_takeaway_EN.html` | Full handout with embedded slide images (EN) |
| `embed_pdf_slides_to_html.py` | Python script to extract and embed PDF slides as Base64 into HTML |

## Generate handout locally

The HTML file contains all 14 slide images as Base64-encoded PNGs (~13 MB) and is therefore too large for upload via GitHub API.

```bash
# 1. Install dependencies
pip install pymupdf

# 2. Extract slides from PDF
python embed_pdf_slides_to_html.py

# 3. Generate HTML handout (script produces trust_me_im_a_llm_takeaway_EN.html)
```

## Topics covered

- What is an AI system? (Art. 3 AI Act)
- AI literacy (Art. 4 AI Act)
- Risk categories under the AI Act
- Technical robustness (Art. 15 AI Act)
- Threat scenarios: Prompt injection, data poisoning, dark LLMs, CAPTCHA bypass
- Digital Omnibus – changes May 2026
- Regulatory synergies: ISO 27001, NIS2, CRA, GDPR
- OWASP Gen AI Security resources

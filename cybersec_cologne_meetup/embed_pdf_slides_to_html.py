import base64
import os
import fitz
from pathlib import Path

PDF_PATH = Path('Prasentation_SecMeetup.pdf')
OUT_DIR = Path('slides')
OUT_DIR.mkdir(exist_ok=True)

def extract_slides(pdf_path: Path, out_dir: Path, dpi: int = 150):
    doc = fitz.open(pdf_path)
    exported = []
    for i, page in enumerate(doc, start=1):
        out_file = out_dir / f'slide_{i:02d}.png'
        pix = page.get_pixmap(dpi=dpi)
        pix.save(out_file)
        exported.append(out_file)
    return exported

def to_b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode('utf-8')

if __name__ == '__main__':
    slides = extract_slides(PDF_PATH, OUT_DIR)
    print(f'Extracted {len(slides)} slides from {PDF_PATH}')
    print('You can now embed them into an HTML file via data:image/png;base64,...')

# Helen's Commercial Site

Static website for Dr. Eleni Anyfanti (Δρ. Ελένη Ανυφαντή), Psychologist – Clinical Neuropsychologist.

## Structure
- `src/*.html` – page content (edit these)
- `build.py` – wraps each page with the shared header/footer and writes the final pages to the repo root
- `assets/style.css`, `assets/main.js` – shared styles and mobile menu

## Editing
1. Edit a file in `src/` (phone and address live at the top of `build.py`).
2. Run `python3 build.py`.
3. Open `index.html` in a browser.

"""Builds the static pages: wraps each src/*.html body with the shared header/footer."""
import pathlib, re

ROOT = pathlib.Path(__file__).parent
NAV = [("index.html", "Αρχική"), ("biografiko.html", "Βιογραφικό"),
       ("ypiresies.html", "Υπηρεσίες"), ("epikoinonia.html", "Επικοινωνία")]
PHONE, PHONE_TEL = "694 508 9035", "+306945089035"
ADDRESS = "Πελοποννήσου 6-10, Ζωγράφου, Αθήνα"

def page(name, title, desc, body):
    current = ' aria-current="page"'
    links = "\n".join(
        f'<li><a href="{h}"{current if h == name else ""}>{l}</a></li>' for h, l in NAV)
    return f"""<!doctype html>
<html lang="el">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Commissioner:wght@300;400;500;600&family=Literata:opsz,wght@7..72,400;7..72,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<script src="assets/main.js" defer></script>
</head>
<body>
<header class="site"><div class="wrap">
  <a class="brand" href="index.html">Δρ. Ελένη Ανυφαντή<small>Ψυχολόγος · Κλινική Νευροψυχολόγος</small></a>
  <button class="menu-toggle" aria-label="Μενού" aria-expanded="false">☰</button>
  <nav class="main"><ul>
{links}
<li><a class="btn" href="epikoinonia.html">Κλείστε ραντεβού</a></li>
  </ul></nav>
</div></header>
<main>
{body}
</main>
<footer class="site"><div class="wrap">
  <div class="cols">
    <div>
      <h4>Δρ. Ελένη Ανυφαντή</h4>
      <p>Ψυχολόγος – Κλινική Νευροψυχολόγος, MSc, PhD.<br>Γνωσιακή-Συμπεριφορική Ψυχοθεραπεία και Νευροψυχολογική Εκτίμηση.</p>
    </div>
    <div>
      <h4>Σελίδες</h4>
      <ul>{"".join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV)}</ul>
    </div>
    <div>
      <h4>Επικοινωνία</h4>
      <ul>
        <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
        <li>{ADDRESS}</li>
        <li>Συνεδρίες δια ζώσης &amp; online</li>
      </ul>
    </div>
  </div>
  <div class="bottom">© <span id="year"></span> Ελένη Ανυφαντή. Με επιφύλαξη παντός δικαιώματος.</div>
</div></footer>
</body>
</html>
"""

for src in sorted((ROOT / "src").glob("*.html")):
    text = src.read_text(encoding="utf-8")
    meta = dict(re.findall(r"<!--\s*(title|desc):\s*(.*?)\s*-->", text))
    body = re.sub(r"<!--\s*(title|desc):.*?-->\n?", "", text)
    body = body.replace("{{PHONE}}", PHONE).replace("{{PHONE_TEL}}", PHONE_TEL).replace("{{ADDRESS}}", ADDRESS)
    (ROOT / src.name).write_text(page(src.name, meta["title"], meta["desc"], body), encoding="utf-8")
    print("built", src.name)

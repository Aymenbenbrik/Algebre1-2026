"""Extrait le corps de chaque chapitre pour le cours complet unifié."""
import os, re, shutil

REPO = r"C:/Users/aymen/Repos/Algebre1-2026"
OUT  = os.path.join(REPO, "cours-complet")

CHAPTERS = [
    ("Chapitre 1 - Calculs algébriques",      "chapitre1.tex", "ch1.tex"),
    ("Chapitre 2 - Vocabulaire ensembliste",  "chapitre2.tex", "ch2.tex"),
    ("Chapitre 3 - Arithmétique dans Z",      "chapitre3.tex", "ch3.tex"),
    ("Chapitre 4 - Structures algébriques",   "chapitre4.tex", "ch4.tex"),
    ("Chapitre 5 - Polynômes",                "chapitre5.tex", "ch5.tex"),
    ("Chapitre 6 - Fractions rationnelles",   "chapitre6.tex", "ch6.tex"),
]

def extract_body(src_path):
    with open(src_path, encoding="utf-8") as f:
        text = f.read()
    body = text.split(r"\begin{document}", 1)[1]
    body = body.rsplit(r"\end{document}", 1)[0]
    body = re.sub(r"\\maketitle[^\n]*\n", "", body)
    body = re.sub(r"\\setcounter\{chapter\}\{\d+\}[^\n]*\n", "", body)
    return body.strip() + "\n"

ch3_dir = os.path.join(REPO, "Chapitres", "Chapitre 3 - Arithmétique dans Z")
for sec in ("section1.tex", "section2.tex", "section3.tex",
            "sectiontd.tex", "sectiontp.tex", "sectionapl.tex", "sectionprojet.tex"):
    shutil.copy(os.path.join(ch3_dir, sec), os.path.join(OUT, sec))
    print(f"  copied {sec}")

for folder, src_file, dst_file in CHAPTERS:
    src = os.path.join(REPO, "Chapitres", folder, src_file)
    dst = os.path.join(OUT, dst_file)
    body = extract_body(src)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(body)
    print(f"  {dst_file}: {body.count(chr(10))} lignes extraites")

print("OK")

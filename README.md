# Algèbre générale — ECUE111 (S1, 2025–2026)

Support de cours, séances et exercices pour le module **Algèbre générale** (UE `UEF110`, ECUE `ECUE111`), Filière Mathématiques — Option Sciences des données.

## 📘 Cours complet (PDF)

➡️ **[Télécharger le cours complet — 111 pages](Tout%20le%20cours/Algebre1-2026%20-%20Cours%20complet.pdf)**

Document unifié des chapitres I à VI : page de titre globale, table des matières navigable (avec hyperliens), numérotation continue, démonstrations, exemples résolus et TPs Python. Compilé depuis [`cours-complet/cours-complet.tex`](cours-complet/cours-complet.tex).

---

- **Volume horaire** : 84 h présentiel (42 h cours + 42 h TD), 21 h travail personnel
- **Coefficient** : 3.5 — **Crédits ECTS** : 7
- **Régime** : CC mixte
- **Responsable** : Moufid Chaima
- **Rédaction du support** : Aymen Ben Brik

## Structure du repo

```
.
├── Chapitres/
│   ├── Chapitre 1 - Calculs algébriques/
│   ├── Chapitre 2 - Vocabulaire ensembliste/
│   ├── Chapitre 3 - Arithmétique dans Z/
│   ├── Chapitre 4 - Structures algébriques/
│   ├── Chapitre 5 - Polynômes/
│   └── Chapitre 6 - Fractions rationnelles/
├── Séances/         (notes SmartBoard de séances)
└── Tout le cours/   (cours complet en un seul PDF)
```

## Programme et état d'avancement

| # | Chapitre | Volume | Pages PDF | TP Python |
|---|---|---|---|---|
| I | Calculs algébriques | 8 h | 14 | ✅ 8 exercices |
| II | Vocabulaire ensembliste | 12 h | 16 | ✅ 8 exercices |
| III | Arithmétique dans ℤ | 14 h | — | ✅ 8 exercices |
| IV | Structures algébriques | 18 h | 18 | ✅ 8 exercices |
| V | Polynômes | 18 h | 22 | ✅ 8 exercices |
| VI | Fractions rationnelles | 14 h | 22 | ✅ 8 exercices |

Chaque chapitre comprend : motivation pédagogique, théorèmes avec démonstrations, exemples résolus à difficulté ascendante, et un TP Python structuré (annotations Bloom + difficulté).

### Détail du programme

**Chapitre I — Calculs algébriques** : sommes et produits finis, sommes doubles, formule du binôme.

**Chapitre II — Vocabulaire ensembliste** : éléments de logique, théorie des ensembles, ensembles finis et dénombrement, applications et relations (ordre, équivalence, quotient).

**Chapitre III — Arithmétique dans ℤ** : division euclidienne et congruence, PGCD/PPCM, théorème de Gauss, identité de Bézout, algorithme d'Euclide.

**Chapitre IV — Structures algébriques** : structure de groupe (sous-groupes, monogène, ordre, théorème de Lagrange, morphismes, *S*ₙ, ℤ/*n*ℤ), structures d'anneau et de corps.

**Chapitre V — Polynômes** : ℝ[*X*] et ℂ[*X*], fonctions polynomiales et racines, arithmétique dans *K*[*X*] (divisibilité, division euclidienne, PGCD/PPCM, Euclide, Hörner — note historique sur Sharaf Eddine Al-Tusi), polynômes irréductibles et décomposition.

**Chapitre VI — Fractions rationnelles** : corps *K*(*X*), forme irréductible, degré/pôles/zéros/multiplicités, décomposition en éléments simples sur ℝ et ℂ.

## Acquis d'apprentissage (AA)

- **AA1** : Maîtriser les opérations algébriques fondamentales et leurs propriétés.
- **AA2** : Utiliser logique et théorie des ensembles pour structurer un raisonnement.
- **AA3** : Appliquer les principes d'arithmétique (division euclidienne, premiers, congruences).
- **AA4** : Manipuler les polynômes (opérations, factorisation, racines).
- **AA5** : Manipuler les fractions rationnelles et simplifications algébriques.
- **AA6** : Rédiger et justifier des arguments mathématiques de manière rigoureuse.

## Compilation

### Chapitre individuel
```bash
cd "Chapitres/Chapitre 1 - Calculs algébriques"
pdflatex chapitre1.tex
```

Le Chapitre 3 utilise un `main.tex` qui inclut les sections via `\input{}`.

### Cours complet unifié
```bash
cd cours-complet
pdflatex cours-complet.tex   # première passe
pdflatex cours-complet.tex   # deuxième passe (table des matières)
pdflatex cours-complet.tex   # troisième passe (références croisées)
```

Le dossier `cours-complet/` contient un fichier maître (`cours-complet.tex`) avec préambule unique, page de titre globale, avant-propos et table des matières. Les corps des chapitres sont extraits dans `ch1.tex` à `ch6.tex` (générés via `_build_bodies.py` à partir des sources individuelles). Pour régénérer ces corps après modification d'un chapitre :
```bash
python cours-complet/_build_bodies.py
```

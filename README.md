# Algèbre générale — ECUE111 (S1, 2025–2026)

Support de cours, séances et exercices pour le module **Algèbre générale** (UE `UEF110`, ECUE `ECUE111`), Filière Mathématiques — Option Sciences des données.

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
│   ├── Chapitre 4 - Structures algébriques/        (à venir)
│   ├── Chapitre 5 - Polynômes/                     (à venir)
│   └── Chapitre 6 - Fractions rationnelles/        (à venir)
├── Séances/         (notes SmartBoard de séances)
└── Tout le cours/   (PDFs combinés)
```

## Programme et état d'avancement

| # | Chapitre | Volume | État |
|---|---|---|---|
| I | Calculs algébriques | 8 h | Rédigé |
| II | Vocabulaire ensembliste | 12 h | Rédigé |
| III | Arithmétique dans ℤ | 14 h | Rédigé |
| IV | Structures algébriques | 18 h | À rédiger |
| V | Polynômes | 18 h | À rédiger |
| VI | Fractions rationnelles | 14 h | À rédiger |

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

Chaque chapitre se compile indépendamment :

```bash
cd "Chapitres/Chapitre 1 - Calculs algébriques"
pdflatex chapitre1.tex
```

Le Chapitre 3 utilise un `main.tex` qui inclut les sections via `\input{}`.

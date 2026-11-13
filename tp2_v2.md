# Programmation Orientée Objet 2

## Travail Pratique 2

Ce projet intégrateur vise à concevoir et implémenter une application complète en appliquant les principes modernes de
l'ingénierie logicielle orientée objet (OO) en Python. L'objectif premier est de maximiser la qualité architecturale, la
maintenabilité et la robustesse de votre code tout en livrant un produit fonctionnel et ergonomique.

### Remise

- Date de remise :
    - Partie 1 : avant la fin semaine 12
        - Recommendation : le plus tôt possible
    - Partie 2 : à déterminer (semaine des examens)
- Format : Dépôt Git dur GitHub, partagé avec l'utilisateur `profdenis`

---

## 1. Objectifs pédagogiques et compétences visées

À terme, ce projet valide votre capacité à :

- Structurer un domaine métier complexe à l'aide de hiérarchies de classes, d'abstractions et de composition cohérentes.
- Appliquer les principes de conception éprouvés (`SOLID`, *Clean Code*, ...) et des patrons de conception adaptés.
- Adopter une approche _Pythonique_ multi-paradigme moderne (typage statique avec `type hints`, programmation
  fonctionnelle ciblée là où elle simplifie le modèle).
- Découpler strictement la logique métier des couches de présentation (interface graphique ou moteur de jeu).
- Utiliser les outils professionnels de développement collaboratif (`git`, `GitHub`, suivi de versions).

---

## 2. Modalités de réalisation

Le projet peut être réalisé **individuellement** ou en **équipe de 2 personnes**.

Afin de maintenir une équité dans la charge de travail et d'optimiser l'expérience d'apprentissage selon la taille de
l'équipe :

| Critère                    | Travail Individuel                                                                       | Équipe de 2 étudiants                                                                                                                                                   |
|:---------------------------|:-----------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Périmètre fonctionnel**  | Application complète à complexité modérée.                                               | Fonctionnalités enrichies (ex. modes de jeu supplémentaires, persistance avancée, filtres/statistiques complexes, automatisation).                                      |
| **Gestion du dépôt `git`** | Historique de commits régulier, atomique et clair sur la branche principale.             | Flux de travail collaboratif documenté : branches de fonctionnalités (`feature branches`), *Pull Requests* / revues mutuelles, répartition équitable des contributions. |
| **Documentation & Tests**  | `README.md` structuré et suite de tests unitaires couvrant les cas critiques du domaine. | `README.md` exhaustif (guide d'architecture, diagramme actualisé, guide de démarrage rapide) et couverture de tests accrue avec `pytest`.                               |

> **Validation préalable :** Le choix de partenaire (le cas échéant) et la proposition de sujet doivent être validés par
> l'enseignant avant d'entamer le développement.

---

## 3. Voies technologiques et suggestions de sujets

Vous devez choisir l'un des deux cadres d'application suivants :

### Option A — Jeu vidéo 2D avec `pygame`

Conception d'un jeu vidéo articulé autour d'une boucle de jeu claire, d'une machine à états et d'entités polymorphes.

**Idées et suggestions de sujets :**

- **Jeu de tir / Arcade (*Shoot 'em up*) :** Vagues d'ennemis variés avec patrons de déplacement distincts, gestion
  d'armements interchangeables, système de collisions et d'événements.
- **Rogue-lite / Dungeon Crawler en tuiles :** Génération de salles, inventaire, équipement modifiant les statistiques,
  système de combat au tour par tour ou en temps réel.
- **Tower Defense :** Placement de tours aux caractéristiques évolutives, calcul de trajectoires/portée, vagues de
  monstres avec résistances spécifiques.
- **Jeu de gestion / simulation minimaliste :** Simulation d'écosystème, circulation routière ou gestion de colonie en
  grille 2D.

### Option B — Application de bureau interactive avec `Qt/PySide6`

Conception d'un logiciel de gestion, d'analyse ou de productivité basé sur le découplage modèle-vue et le mécanisme de
signaux/slots.

**Idées et suggestions de sujets :**

- **Gestionnaire de collection / budget / inventaire :** CRUD complet, tris multi-critères, persistance (JSON/SQLite),
  graphiques récapitulatifs et historique d'opérations.
- **Outil de productivité / Planificateur de tâches :** Tableau type Kanban interactif, filtres avancés,
  alertes/notifications, système de sauvegarde et d'export.
- **Éditeur / Traitement de données ou d'images :** Application permettant d'appliquer des filtres, transformations ou
  calculs statistiques avec prévisualisation en direct et interface paramétrable.
- **Client d'exploration / Dashboard :** Visualisation de données connectée à des fichiers locaux ou à une API externe
  (ex. météo, suivi de cours, données ouvertes) avec traitements locaux asynchrones (`QThread`).

---

## 4. Exigences techniques et architecture logicielle

L'évaluation porte avant tout sur la **qualité du design logiciel**. L'implémentation doit suivre les directives
suivantes :

### A. Design Orienté Objet moderne et pragmatique

- **Découplage strict :** La logique métier (`Domain/Model`) ne doit avoir aucune dépendance directe vers l'interface
  utilisateur (`View/UI`) ou la boucle de rendu (`pygame`/`Qt`). L'interface ne fait qu'observer, afficher et interagir
  avec le modèle métier.
- **Utilisation judicieuse des concepts avancés :**
    - Classes abstraites (`abc.ABC`, `@abstractmethod`) et Protocoles structurels (`typing.Protocol`) lorsque
      l'interchangeabilité est requise.
    - Classes de données (`@dataclass`) pour encapsuler les objets de valeurs ou configurations immutables.
    - Propriétés (`@property`) pour préserver l'encapsulation et valider les invariants métier.
    - Énumérations (`enum.Enum`) pour les états, types et constantes catégorielles.
- **Patrons de conception pertinents :**
    - Intégrez des patrons de conception (*Design Patterns*) là où ils résolvent un problème réel d'architecture (ex.
      *Fabrique*, *Observateur*, *État*, *Commande*, *Stratégie*).
    - **Pragmatisme Pythonique :** Vous n'avez pas à reproduire des patrons lourds issus de langages rigides là où
      Python propose des solutions natives plus efficaces (par exemple : utiliser des fonctions de première classe ou
      des expressions `lambda` pour instancier des stratégies comportementales plutôt que de multiplier inutilement les
      sous-classes).

### B. Typage, Lisibilité et Qualité du Code

- **_Type Hints_ obligatoires :** Toutes les signatures de fonctions, méthodes et attributs de classe doivent être
  rigoureusement typés (`int`, `str`, `list[T]`, `Optional[T]`, `Callable`, etc.).
- **Gestion des erreurs :** Création d'exceptions personnalisées et gestion propre des erreurs sans masquage silencieux
  (`try/except` ciblés).
- **Style et conventions :** Respect strict de la `PEP 8`, nommage explicite des classes/méthodes, modularité (fichiers
  organisés en paquetages cohérents).

---

## 5. Jalons et Livrables

### Étape 1 : Proposition de projet et conception préliminaire

**_Objectif_ : Valider la faisabilité technique, la clarté du domaine et l'architecture initiale.**

À déposer sur le dépôt GitHub :

1. **Description du projet (`README.md` préliminaire) :** Objectif du logiciel/jeu, liste claire des fonctionnalités
   principales prévues, et précision de la répartition des rôles (pour les équipes).
2. **Diagramme de classes initial :** Modélisation UML des classes métier principales (attributs clés, méthodes
   principales, relations d'héritage et de composition). La couche graphique peut être omise ou simplifiée à ce stade.
3. **Maquettes d'interface / de jeu :** Croquis ou captures basse/moyenne fidélité (*wireframes*) illustrant les
   différents écrans, menus ou états de l'application.

### Étape 2 : Remise finale et Démonstration individuelle

*Objectif : Évaluer la qualité du code final, l'exécution logicielle et la maîtrise individuelle des concepts OO.*

1. **Dépôt `GitHub` :**
    - Code source complet, exécutable et documenté.
    - Historique `git` démontrant une progression continue.
    - `README.md` final contenant les instructions de lancement (dépendances avec `uv`) et la documentation
      utilisateur/architecturale complète.
    - Suite de tests unitaires (`pytest`) validant les règles métier critiques.
2. **Présentation en tête-à-tête :**
    - Rencontre en personne avec le professeur à la fin de la session (hors de la présence des autres équipes).
    - Démonstration fonctionnelle de l'application en direct.
    - Revue de code guidée et période de questions ciblées sur les choix d'architecture, l'utilisation des patrons et la
      justification des structures OO.

---

## 6. Grille d'évaluation

| Critère                                    | Pondération | Description                                                                                                                                                                |
|:-------------------------------------------|:-----------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Architecture OO & Découplage**           |  **35 %**   | Séparation modèle / présentation, responsabilités uniques des classes (`SRP`), utilisation logique de l'héritage, de la composition, des protocoles ou classes abstraites. |
| **Patrons de conception & Python moderne** |  **20 %**   | Pertinence des patrons retenus, intégration élégante des fonctionnalités Python (`dataclasses`, lambdas/callables, `Enum`, génériques, ...).                               |
| **Typage statique & Propreté du code**     |  **15 %**   | Couverture complète des `type hints`, conformité `PEP 8`, clarté du nommage, gestion robuste des exceptions.                                                               |
| **Fonctionnalités, Finition & Ergonomie**  |  **15 %**   | Respect du cahier des charges validé, stabilité du jeu/de l'application (absence de plantages majeurs), expérience utilisateur soignée.                                    |
| **Rigueur logicielle (`git`, tests, doc)** |  **15 %**   | Qualité du dépôt, pertinence des tests unitaires (`pytest`), documentation d'installation claire, collaboration démontrée (si équipe de 2).                                |

**Note** : La présentation en tête-à-tête avec le professeur est obligatoire, même s'il n'y a pas de points accordés
directement pour celle-ci. Elle permettra de démontrer votre compréhension du projet, et d'orienter le professeur
dans l'évaluation de votre travail.
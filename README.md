### Chapitre 01 : Programmation Orientée Objet  
**Projet :**  
Création d'une œuvre artistique à base de formes géométriques en programmation orientée objet.

---

#### 1. Description du projet  
Développer un programme en Python permettant de générer des œuvres artistiques basées sur des formes géométriques.

---

#### 2. Objectifs du projet  
- **Manipulation des classes et objets :** Créer et utiliser des classes pour modéliser des formes géométriques.  
- **Utilisation de l’héritage et du polymorphisme :** Étendre des classes spécifiques et redéfinir des méthodes.  
- **Encapsulation :** Contrôler l'accès aux attributs via des méthodes appropriées.  
- **Création d’une interface graphique :** Dessiner des formes dans une interface utilisateur.  
- **Encourager la créativité.**  

---

#### 3. Tâches à réaliser  

**1. Conception des classes :**  
- **Classe de base « Forme » :**  
  - **Attributs :** position (x, y), couleur, épaisseur du contour.  
  - **Méthodes :**  
    - `dessiner()`,  
    - `déplacer(nouveau_x, nouveau_y)`,  
    - `rotation(angle)`,  
    - `changer_taille(facteur)`,  
    - `changer_couleur(nouvelle_couleur)`.  

- **Classes dérivées :**  
  - **Rectangle :**  
    - Attributs : largeur, hauteur.  
    - Méthode : version spécifique de `dessiner()`.  
  - **Ligne :**  
    - Attributs : longueur, orientation.  
    - Méthode : version spécifique de `dessiner()`.  
  - **Cercle :**  
    - Attribut : rayon.  
    - Méthode : version spécifique de `dessiner()`.  

**2. Développement de l'interface graphique :**  
- Utiliser une bibliothèque graphique (ex. Tkinter).  
- Créer une fenêtre principale avec une zone de dessin.  
- Ajouter des outils permettant :  
  - L’ajout de formes (rectangles, cercles, etc.).  
  - La sélection de couleurs.  
  - Le positionnement des formes sur une grille.  
  - La modification (taille, déplacement, rotation) des formes.  

**3. Fonctionnalités principales :**  
- **Grille de composition :** Permettre le placement des formes sur une grille.  
- **Modification des formes :** Inclure des options pour déplacer, redimensionner, faire tourner ou changer la couleur des formes.  
- **Enregistrement :** Sauvegarder la composition sous forme d’image.  
- **Réinitialisation :** Effacer la composition pour recommencer.  

**4. Application des concepts de POO :**  
- **Héritage :** Les classes dérivées héritent de la classe de base « Forme ».  
- **Polymorphisme :** Redéfinir la méthode `dessiner()` pour chaque classe.  
- **Encapsulation :** Protéger les attributs avec des méthodes d’accès.  

---

#### 4. Livrables attendus  
- Code source structuré et commenté.  
- Explication concise de l’interface graphique.  
- Exemples d’œuvres créées avec le programme.


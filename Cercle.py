#=================================================================================================================
# PARTIE 1: APPELS DES FICHERS ET LIBRARIES EXTERNE (IMPORT)
#=================================================================================================================

import tkinter as tk


# ==============================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
# ==============================================================================

class Cercle:
    def __init__(self, x, y, rayon, couleur):
        self.x = x
        self.y = y
        self.rayon = rayon
        self.couleur = couleur
        self.canvas_item = None

    def genere(self, canvas):
        if self.canvas_item:
            canvas.delete(self.canvas_item)

        self.canvas_item = canvas.create_oval(self.x - self.rayon, self.y - self.rayon,self.x + self.rayon, self.y + self.rayon,fill=self.couleur)

    def agrandir(self, canvas, nouveau_rayon):
        self.rayon = nouveau_rayon
        self.genere(canvas)

    def deplacer(self,canvas, noveau_x, noveau_y):
        self.x = noveau_x
        self.y = noveau_y
        self.genere(canvas)

    def rotate(self, canvas, angle):
        """Appliquer une rotation """
        pass

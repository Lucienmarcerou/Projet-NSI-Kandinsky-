#=================================================================================================================
# PARTIE 1: APPELS DES FICHERS ET LIBRARIES EXTERNE (IMPORT)
#=================================================================================================================

import tkinter as tk
from Rectangle import Rectangle

# ==============================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
# ==============================================================================

class Ligne(Rectangle):
    def __init__(self, x, y, x2, y2, couleur, larguer=1):

        width = x2 - x #calcul de la larguer
        height = y2 - y  #calcul de la hauteur
        super().__init__(x, y, width, height, couleur)
        self.largeur = larguer

    def genere(self, canvas):
        """Dessiner la ligne"""
        if self.canvas_item:
            canvas.delete(self.canvas_item)


        self.canvas_item = canvas.create_line(self.x, self.y,self.x + self.width, self.y + self.height,fill=self.couleur, width=self.largeur)

    def change_cord(self, canvas, nouveau_x1, nouveau_y1, nouveau_x2, nouveau_y2):
        """Delacer la ligne"""
        self.x = nouveau_x1
        self.y = nouveau_y1
        self.width = nouveau_x2 - nouveau_x1
        self.height = nouveau_y2 - nouveau_y1
        self.genere(canvas)

    def change_larguer(self, canvas, nouvelle_larguer):
        if self.canvas_item:
            canvas.delete(self.canvas_item)

        self.canvas_item = canvas.create_line(self.x, self.y,self.x + self.width, self.y + self.height,fill=self.couleur, width=nouvelle_larguer)

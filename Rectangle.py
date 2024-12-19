#=================================================================================================================
# PARTIE 1: APPELS DES FICHERS ET LIBRARIES EXTERNE (IMPORT)
#=================================================================================================================

import tkinter as tk
import math


# ==============================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
# ==============================================================================
class Rectangle:
    def __init__(self, x, y, width, height, couleur):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.couleur = couleur
        self.canvas_item = None

        # definie les points OG du rectangle
        self.corners = [
            (x, y),  # haut gauche
            (x + width, y),  # haut droit
            (x + width, y + height),  # bas droit
            (x, y + height)  # bas gauche
        ]

    def genere(self, canvas):
        """Dessiner l'objet choisi."""
        if self.canvas_item:
            canvas.delete(self.canvas_item)

        # Dessine le rectangle a partir des cotes donees
        self.canvas_item = canvas.create_polygon(self.corners, fill=self.couleur)

    def rotate(self, canvas, angle):
        """Appliquer une rotation aux points actuels."""
        radians = math.radians(-angle)

        center_x = (self.corners[0][0] + self.corners[2][0]) / 2
        center_y = (self.corners[0][1] + self.corners[2][1]) / 2

        # Apliquer la roation a chauque point
        rotated_corners = []
        for (x, y) in self.corners:
            # calcul la distance relative du point par rappport au centre
            rel_x = x - center_x
            rel_y = y - center_y

            # Appliquer la rotation
            # grand remerciement a
            # https://www.khanacademy.org/math/geometry/hs-geo-transformations/hs-geo-rotations/v/points-after-rotation
            new_x = center_x + rel_x * math.cos(radians) - rel_y * math.sin(radians)
            new_y = center_y + rel_x * math.sin(radians) + rel_y * math.cos(radians)
            rotated_corners.append((new_x, new_y))

        self.corners = rotated_corners
        # redeisne le nouveau rectnagle
        self.genere(canvas)

    def agrandir(self, canvas, multiplication):
        """Agrandir l'objet """
        # Get the current center
        center_x = (self.corners[0][0] + self.corners[2][0]) / 2
        center_y = (self.corners[0][1] + self.corners[2][1]) / 2

        # Scale each corner relative to the center
        scaled_corners = []
        for (x, y) in self.corners:
            # calcul la distance relative du point par rappport au centre
            rel_x = x - center_x
            rel_y = y - center_y

            # agrandi les cotes
            new_x = center_x + rel_x * multiplication
            new_y = center_y + rel_y * multiplication
            scaled_corners.append((new_x, new_y))

        self.corners = scaled_corners

        # recree le nouveau rectangle
        self.genere(canvas)

    def deplacer(self, canvas, dx, dy):
        """Deplacer l'objet a des nouvelle cord"""

        # change les corrodness
        moved_corners = []
        for (x, y) in self.corners:
            new_x = x + dx
            new_y = y + dy
            moved_corners.append((new_x, new_y))

        self.corners = moved_corners

        # recree le rectangle
        self.genere(canvas)


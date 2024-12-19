#=================================================================================================================
# PARTIE 1: APPELS DES FICHERS ET LIBRARIES EXTERNE (IMPORT)
#=================================================================================================================

import tkinter as tk
from Rectangle import Rectangle

# ==============================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
# ==============================================================================

class Caree(Rectangle):
    def __init__(self, x, y, cote, couleur):
        super().__init__(x, y, cote, cote, couleur)


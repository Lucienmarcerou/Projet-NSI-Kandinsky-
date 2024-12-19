# =================================================================================================================
# PARTIE 1: APPELS DES FICHIERS ET BIBLIOTHÈQUES EXTERNES (IMPORT)
# =================================================================================================================
import tkinter as tk
from Rectangle import Rectangle
from Caree import Caree
from Cercle import Cercle
from Lignes import Ligne
import random
from tkinter import filedialog, messagebox
from PIL import ImageGrab

# ==============================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
# ==============================================================================

# ======================
# Variable Globale
# ======================

shapes = []
selected_shape = None
start_x = None
start_y = None
size_menu = None
line_start = None
drawing = False
delete_mode = False


# =========================================
# Formes
# =========================================

# ================
# Rectangle
# ================
def create_rectangle():
    x = random.randint(0, 400)
    y = random.randint(0, 400)

    width = int(width_entry.get()) if width_entry.get() else 100
    height = int(height_entry.get()) if height_entry.get() else 50

    rectangle = Rectangle(x, y, width, height, selected_color.get())
    rectangle.genere(canvas)

    rotation_value = rotation_entry.get()
    if rotation_value:
        angle = -int(rotation_value)
        rectangle.rotate(canvas, angle)

    shapes.append(rectangle)

    return rectangle


# ================
# Carré
# ================
def create_carre():
    x = random.randint(0, 400)
    y = random.randint(0, 400)

    cote = int(square_side_entry.get()) if square_side_entry.get() else 50

    carre = Caree(x, y, cote, selected_color.get())
    carre.genere(canvas)

    rotation_value = rotation_entry.get()
    if rotation_value:
        angle = -int(rotation_value)
        carre.rotate(canvas, angle)

    shapes.append(carre)

    return carre


# ================
# Cercle
# ================
def create_cercle():
    x = random.randint(0, 400)
    y = random.randint(0, 400)

    rayon = int(circle_radius_entry.get()) if circle_radius_entry.get() else 30

    cercle = Cercle(x, y, rayon, selected_color.get())
    cercle.genere(canvas)
    shapes.append(cercle)

    return cercle


# =========================================
# Ligne
# =========================================
def create_ligne():
    global drawing, line_start
    drawing = True
    line_start = None


def start_line_click(event):
    global line_start, drawing
    if drawing:
        if line_start is None:
            line_start = (event.x, event.y)
        else:
            x1, y1 = line_start
            x2, y2 = event.x, event.y
            ligne = Ligne(x1, y1, x2, y2, selected_color.get())
            ligne.genere(canvas)
            shapes.append(ligne)
            line_start = None
            drawing = False


# =========================================
# Toggle delete mode
# =========================================
def toggle_delete_mode():
    global delete_mode
    delete_mode = not delete_mode
    mode_text = "ON" if delete_mode else "OFF"
    delete_button.config(text=f"Mode Supprimer ({mode_text})")


# ==============================
# Save Image Function
# ==============================
def saveImage():
    # Définit la taille de la capture
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    # Capture l'image
    ImageGrab.grab().crop((x, y, x1, y1)).save(filedialog.asksaveasfilename(defaultextension=".png"))
    messagebox.showinfo("Image Sauvegardée", "Votre image a bien été sauvegardée.")


# ==================================================================================
# Cursor functions
# ==================================================================================

# ======================================
# Mouse click
# ======================================
def on_click(event):
    global selected_shape, start_x, start_y

    if drawing:  # Vérifier si nous sommes en mode dessin
        start_line_click(event)  # Appeler la fonction pour commencer à dessiner une ligne
    else:
        selected_shape = canvas.find_overlapping(event.x, event.y, event.x, event.y)

        if selected_shape:  # Si une forme est trouvée à la position de clic
            # Obtenir la première forme de la liste des formes qui correspond à l'élément de canevas cliqué
            selected_shape = next((s for s in shapes if s.canvas_item in selected_shape), None)

            if delete_mode and selected_shape:
                canvas.delete(selected_shape.canvas_item)  # Supprimer la forme du canevas
                shapes.remove(selected_shape)  # Retirer la forme de la liste des formes
            else:
                # Stocker les coordonnées de départ pour faire bouger la forme
                start_x = event.x
                start_y = event.y


# ==================================
# Mouse drag
# ==================================
def on_drag(event):
    global selected_shape, start_x, start_y
    if selected_shape and not drawing and not delete_mode:
        dx = event.x - start_x
        dy = event.y - start_y
        canvas.move(selected_shape.canvas_item, dx, dy)
        start_x = event.x
        start_y = event.y


# ================================
# Mouse release
# ================================
def on_release(event):
    global selected_shape
    selected_shape = None


# ==============================================================================
# PARTIE 3: APPELS DES FONCTIONS (GUI)
# ==============================================================================

root = tk.Tk()

# ==============================================================
# Menu pour les couleurs et bouton d'enregistrement
# ==============================================================
frame2 = tk.Frame(root)
frame2.pack(side=tk.TOP)

colors = ["blue", "red", "green", "black", "yellow", "purple", "lightseagreen", "pink", "indigo", "violet",]
selected_color = tk.StringVar(frame2)
selected_color.set(colors[0])

color_menu = tk.OptionMenu(frame2, selected_color, *colors)
color_menu.pack(side=tk.LEFT)

save_button = tk.Button(frame2, text="Enregistrer l'image", command=saveImage)
save_button.pack(side=tk.LEFT)

# ==============================================================
# Canvas Set Up
# ==============================================================

canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# ==============================
# Binding
# ==============================

canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)
canvas.bind("<ButtonRelease-1>", on_release)

# ==============================================================
# Boutons pour les dimensions custom
# ==============================================================

frame1 = tk.Frame(root)
frame1.pack(side=tk.RIGHT)

# Rotation
tk.Label(frame1, text="Rotation : (par défaut 0°)").pack()
rotation_entry = tk.Entry(frame1, width=5)
rotation_entry.pack()

# Rectangle
tk.Label(frame1, text="Largeur : (100 par défaut)").pack()
width_entry = tk.Entry(frame1, width=5)
width_entry.pack()

tk.Label(frame1, text="Hauteur : (50 par défaut)").pack()
height_entry = tk.Entry(frame1, width=5)
height_entry.pack()
button1 = tk.Button(frame1, text="Créer un rectangle", command=create_rectangle)
button1.pack()

# Carré
tk.Label(frame1, text="Côté : (50 par défaut)").pack()
square_side_entry = tk.Entry(frame1, width=5)
square_side_entry.pack()
button2 = tk.Button(frame1, text="Créer un carré", command=create_carre)
button2.pack()

# Cercle
tk.Label(frame1, text="Rayon : (30 par défaut)").pack()
circle_radius_entry = tk.Entry(frame1, width=5)
circle_radius_entry.pack()
button3 = tk.Button(frame1, text="Créer un cercle", command=create_cercle)
button3.pack()

# Ligne
button4 = tk.Button(frame1, text="Créer une ligne", command=create_ligne)
button4.pack()

# ======================
# Delete
# ======================

delete_button = tk.Button(frame1, text="Mode Supprimer (OFF)", command=toggle_delete_mode)
delete_button.pack()

# =======================================
root.mainloop()
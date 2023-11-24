from grille_cellule_regles import Grille

def infini_init():
    """Donne les coordonnnées de départ du canon

    Paramètres
    ----------
    Aucun

    Retourne
    --------
    vivantes : liste de coordonnées
        Liste des cellules vivantes pour initialiser le canon
    """
    vivantes = [(11,11),(11,12),(11,13),(11,15),(12,11),(13,14),
                (13,15),(14,12),(14,13),(14,15),(15,11),(15,13),
                (15,15)]
    return vivantes

# Générer la grille

grille = Grille(25)
grille.generer()

# Placer les cellules vivantes dans la grille

vivantes = infini_init()
print(vivantes)
grille.modifier(vivantes)

# Générer l'interface graphique

import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=grille.cote * 20, height=grille.cote * 20)
canvas.pack()

# Montrer les cellules vivantes, appliquer les règles du jeu et mettre à jour l'interface

from interface import jouer_tour

jouer_tour(grille, vivantes, root, canvas)  # lancer le premier tour
root.mainloop()

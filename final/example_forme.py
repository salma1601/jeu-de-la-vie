from grille_cellule_regles import Grille

def canon_init():
    vivantes = [(20,20),(20,21),(20,22),
                (20,23),(20,24),(20,25),
                (20,26),(20,27),(20,28),]
    return vivantes

# Générer la grille

grille = Grille(50)
grille.generer()

# Placer les cellules vivantes dans la grille

vivantes = canon_init()
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

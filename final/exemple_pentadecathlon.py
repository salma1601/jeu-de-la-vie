def penta_decathlon_init():
    vivantes = [(4, 4), (4, 5), (4, 6),
                (13, 4), (13, 5), (13, 6),
                (5, 3), (5, 7),
                (12, 3), (12, 7),
                (6, 2), (6, 8),
                (11, 2), (11, 8),
                (8, 1), (8, 9),
                (9, 1), (9, 9)]
    
    return vivantes

# Générer la grille
from grille_cellule_regles import Grille

grille = Grille(18)
grille.generer()

# Placer les cellules vivantes dans la grille
vivantes = penta_decathlon_init()
print(vivantes)
grille.modifier(vivantes)

# Générer l'interface graphique
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=grille.cote * 20, height=grille.cote * 20)
canvas.pack()

# Montrer les cellules vivantes, appliquer les règles du jeu et mettre à jour
# l'interface
from interface import jouer_tour

jouer_tour(grille, vivantes, root, canvas)  # lancer le premier tour
root.mainloop()

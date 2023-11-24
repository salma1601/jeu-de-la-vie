import tkinter as tk
from random import shuffle

class Grille:
    def __init__(self, cote):
        self.cote = cote
        self.taille = cote * cote

    def generer(self):
        self.matrice = [[0 for _ in range(self.cote)] for _ in range(self.cote)]
        return self.matrice

    def afficher(self):
        for ligne in self.matrice:
            print(ligne)

    def modifier(self, liste):
        self.generer()
        for element in liste:
            self.matrice[element[0]][element[1]] = 1
        return self.matrice

class Cellule:
    def __init__(self, x, y, grille):
        self.x = x
        self.y = y
        self.etat = grille.matrice[x][y]
        self.rang = (x, y)

    def donner_voisines(self, grille):
        self.voisines = []
        a = -1
        for i in range(3):
            b = -1
            for j in range(3):
                voisine = (self.x + a, self.y + b)
                if voisine[0] in range(0, grille.cote):
                    if voisine[1] in range(0, grille.cote):
                        if voisine != (self.x, self.y):
                            self.voisines.append(voisine)
                b = b + 1
            a = a + 1
        return self.voisines

def afficher_grille_graphique(grille, canvas):
    canvas.delete("all")  # Effacer le contenu précédent du canvas

    # Dessiner les lignes horizontales
    for i in range(1, grille.cote):
        canvas.create_line(0, i * 20, grille.cote * 20, i * 20)

    # Dessiner les lignes verticales
    for j in range(1, grille.cote):
        canvas.create_line(j * 20, 0, j * 20, grille.cote * 20)

    for i in range(grille.cote):
        for j in range(grille.cote):
            x0, y0 = j * 20, i * 20
            x1, y1 = x0 + 20, y0 + 20
            if grille.matrice[i][j] == 1:
                canvas.create_rectangle(x0, y0, x1, y1, fill="black")

###
def mouse_click(event):
    x, y = event.x // 20, event.y // 20
    if grille.matrice[y][x] == 0:
        grille.matrice[y][x] = 1
    else:
        grille.matrice[y][x] = 0
    afficher_grille_graphique(grille, canvas)

    
def start_game(event):
    global vivantes
    vivantes = [(i, j) for i in range(grille.cote) for j in range(grille.cote) if grille.matrice[i][j] == 1]
    jouer_tour()

###

def jouer_tour():
    global grille, vivantes
    stock = [] 
    for cellule in vivantes :
        cellule = Cellule(cellule[0], cellule[1], grille)
        cellule_voisines = cellule.donner_voisines(grille)
        
        cnt_cellule = 0 
        for voisine in cellule_voisines :
            voisine = Cellule(voisine[0], voisine[1], grille)
            if voisine.etat == 1:
                cnt_cellule = cnt_cellule + 1
            voisine_entourage = voisine.donner_voisines(grille)
            cnt_voisine = 0
            for voisin in voisine_entourage :
                voisin = Cellule(voisin[0], voisin[1], grille)
                if voisin.etat == 1:
                    cnt_voisine = cnt_voisine + 1
            if cnt_voisine == 3 and voisine.etat == 0 :
                if voisine.rang not in stock :
                    stock.append(voisine.rang)
            elif cnt_voisine in [2,3] and voisine.etat == 1 :
                if voisine.rang not in stock :
                    stock.append(voisine.rang) 
        if cnt_cellule in [2,3] :
            if cellule.rang not in stock:
                stock.append(cellule.rang)
    vivantes = stock
    print(len(vivantes), "cellules vivantes au prochain tour")
    print(vivantes)
    grille.modifier(vivantes)
    afficher_grille_graphique(grille, canvas)
    root.after(100, jouer_tour)

grille = Grille(50)
grille.generer()

root = tk.Tk()
canvas = tk.Canvas(root, width=grille.cote * 20, height=grille.cote * 20)
canvas.pack()

###
canvas.bind("<Button-1>", mouse_click)  # Lier l'événement clic gauche à la fonction mouse_click
root.bind("<Return>", start_game)  # Lier l'événement Entrée à la fonction start_game
###

afficher_grille_graphique(grille, canvas)

root.mainloop()

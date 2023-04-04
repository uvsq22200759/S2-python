import tkinter as tk
import random
from tkinter import filedialog
from tkinter import messagebox

racine = tk.Tk()
racine.title("Sudoku")

# barre de boutons :
def créer_barre_boutons():
    barre_boutons = tk.Frame(racine)

    bouton_nouveau = tk.Button(barre_boutons, text="Nouveau", command=grille)
    bouton_nouveau.pack(side="left", padx=(0, 0))

    bouton_quitter = tk.Button(barre_boutons, text="Quitter", command=racine.destroy)
    bouton_quitter.pack(side="left", padx=(0, 0))

    barre_boutons.pack(side="top", fill="x", pady=(0, 0))

    bouton_verifier = tk.Button(racine, text="Vérifier", command=lambda: verifier_grille(entrees))
    bouton_verifier.pack(side="bottom", pady=10)


# grille :
entrees = []
def grille():
    global entrees # permet d'accéder à la variable globale

    # supprime les anciennes entrées
    for ligne in entrees:
        for entree in ligne:
            entree.destroy()

    entrees = [] # réinitialise la grille

    cadre = tk.Frame(racine)
    for i in range(9):
        ligne = []
        for j in range(9):
            entree = tk.Entry(cadre, width=2, font=("Helvetica", 20), justify="center")
            if j % 3 == 0:
                entree.grid(row=i, column=j, padx=(5, 0), pady=(5, 0))
            else:
                entree.grid(row=i, column=j, pady=(5, 0))
            ligne.append(entree)
        entrees.append(ligne)
    cadre.pack(side="top", padx=10, pady=(0, 10))


def verifier_grille(grille):
    for i in range(9):
        for j in range(9):
            if grille[i][j].get() == "":
                tk.messagebox.showerror("Erreur", f"La case {i+1}, {j+1} est vide.")
                return

    # vérification des blocs de 3x3
    for bloc_i in range(3):
        for bloc_j in range(3):
            valeurs = []
            for i in range(3):
                for j in range(3):
                    valeur = grille[bloc_i*3+i][bloc_j*3+j].get()
                    if valeur != "" and valeur in valeurs:
                        tk.messagebox.showerror("Erreur", f"La case {bloc_i*3+i+1}, {bloc_j*3+j+1} contient une valeur en double.")
                        return
                    valeurs.append(valeur)

    # vérification des lignes
    for i in range(9):
        valeurs = []
        for j in range(9):
            valeur = grille[i][j].get()
            if valeur != "" and valeur in valeurs:
                tk.messagebox.showerror("Erreur", f"La case {i+1}, {j+1} contient une valeur en double.")
                return
            valeurs.append(valeur)

    # vérification des colonnes
    for j in range(9):
        valeurs = []
        for i in range(9):
            valeur = grille[i][j].get()
            if valeur != "" and valeur in valeurs:
                valeurs.append(valeur)
                tk.messagebox.showinfo("Félicitations !", "Vous avez résolu la grille !")


créer_barre_boutons()
grille()

racine.mainloop()

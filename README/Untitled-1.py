import tkinter as tk
import random
from tkinter import filedialog
racine = tk.Tk()
racine.title("Sudoku")

# barre de boutons :
def créer_barre_boutons():
    barre_boutons = tk.Frame(racine)

    bouton_nouveau = tk.Button(barre_boutons, text="Nouveau", command=créer_grille)
    bouton_nouveau.pack(side="left", padx=(0, 0))

    bouton_quitter = tk.Button(barre_boutons, text="Quitter", command=racine.destroy)
    bouton_quitter.pack(side="left", padx=(0, 0))

    barre_boutons.pack(side="top", fill="x", pady=(0, 0))

# grille :
def créer_grille():
    cadre = tk.Frame(racine)
    for i in range(9):
        for j in range(9):
            entree = tk.Entry(cadre, width=2, font=("Helvetica", 20), justify="center")
            if j % 3 == 0:
                entree.grid(row=i, column=j, padx=(5, 0), pady=(5, 0))
            else:
                entree.grid(row=i, column=j, pady=(5, 0))

    cadre.pack(side="top", padx=10, pady=(0, 10))
créer_barre_boutons()
créer_grille()
racine.mainloop()
 

import tkinter as tk
import random as rd

racine = tk.Tk()
racine.title("Sudoku")
 #grille :
def créer_grille():
        for i in range(9):
            for j in range(9):
                entree = tk.Entry(racine, width=2, font=("Helvetica", 20), justify="center")  #justify permet de centrer le widget grille
                if j % 3 == 0:
                    entree.grid(row=i, column=j, padx=(5, 0), pady=(5, 0))
                else:
                    entree.grid(row=i, column=j, pady=(5, 0))
        racine.mainloop()
créer_grille()
 

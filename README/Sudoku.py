import tkinter as tk
import random as rd

racine = tk.Tk()
racine.title("Sudoku")
largeur = 350
hauteur = 350
largeur_case = largeur // 9
hauteur_case = hauteur // 9
epaisseur = 5
canvas = tk.Canvas(racine, bg="white", height=hauteur, width=largeur)
canvas.grid()

for i in range(9):
    for j in range(9):
        #TEXTE POUR LES CASES PEUT ETRE A INSERER ICI
        canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                ((i+1)*largeur_case, (j+1)*hauteur_case), fill="white")
        

###############CASES EN GRAS MAIS FONCTIONNE PAS########################################################
#for i in range(10):
#    if i % 3 == 0:
#        canvas.create_line(0, i*hauteur_case, hauteur_case, i*hauteur_case, width=epaisseur)
#    else:
#        canvas.create_line(0, i*hauteur_case, hauteur_case, i*hauteur_case)
#            
#    if i % 3 == 0:
#        canvas.create_line(i*largeur_case, 0, i*largeur_case, largeur_case, width=epaisseur)
#    else:
#            canvas.create_line(0, i*largeur_case, largeur_case, i*largeur_case)
########################################################################################################

canvas.pack()
racine.mainloop()

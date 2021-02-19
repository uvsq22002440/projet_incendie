
########################################################

# groupe MPCI 3
# 
# Antoine Rios Campo
# Wacil Naoufl 
# Anas Shaik 
# Abdel Hakim Belmehdi
# Lakshmi Kootala 
# Wiliam Mollet
#https://github.com/uvsq21918039/projet_incendie
#########################################################


#########################################################
# import des librairies
import tkinter as tk 
#########################################################


#########################################################
#définition des constantes

LARGEUR=600
HAUTEUR=400
COULEUR_FOND ="white"
COTE_PARCELLE = 25
COULEUR_LIGNE ="purple"
COULEUR_PRAIRIE ="yellow"
COULEUR_FORET ="green"
COULEUR_FEU ="red"
COULEUR_EAU ="blue"
COULEUR_CENDRE_OFF="black"
COULEUR_CENDRE_ON="grey"










#########################################################

#########################################################
#définition des variables globales








#########################################################


#########################################################
#définition des fonctions 

def quadrillage():
    """Affiche un quadrillage constitué de carrés de côté COTE_PARCELLE"""
    y = 0
    while y < HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill=COULEUR_LIGNE)
        y += COTE_PARCELLE
    x = 0
    while x < LARGEUR:
        canvas.create_line((x, 0), (x, HAUTEUR), fill=COULEUR_LIGNE)
        x += COTE_PARCELLE






#########################################################

#########################################################
#programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine,width=LARGEUR,height=HAUTEUR,bg=COULEUR_FOND)
canvas.grid()

quadrillage()

racine.mainloop()
#########################################################



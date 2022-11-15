# -*-coding:Utf-8 -*
from tkinter import *
# --------------------------
# Définitions des fonctions utilisées
# --------------------------
def mise_a_jour():
    monTexte.set("Vous avez appuyé sur le premier bouton !")
def mise_a_jour2():
    monTexte.set("Vous avez appuyé sur le second bouton !")
# --------------------------
# Création de la fenêtre et des objets associés la fenêtre
# --------------------------
fen_princ = Tk()
# Création d'un Label nommé monAffichage ayant monTexte comme textvariable
monTexte = StringVar()
monTexte.set("Texte de base !")
monAffichage = Label(fen_princ, textvariable=monTexte, width=35)
monAffichage.pack()
# Création d'un Button lancant la fonction mise_a_jour
monBouton = Button(fen_princ, text="BOUTON 1", command=mise_a_jour)
monBouton.pack()
# Création d'un Button lancant la fonction mise_a_jour2
monBouton2 = Button(fen_princ, text="BOUTON 2", command=mise_a_jour2)
monBouton2.pack()
# --------------------------
# Bouclage de la fenêtre fen_princ
# --------------------------
fen_princ.mainloop()
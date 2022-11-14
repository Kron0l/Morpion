##-----Importation des Modules-----##
from tkinter import *


##----- Définition des Variables globales -----##



##----- Définition des Fonctions -----##
def afficher(event) :
    """Cette fonction affiche en temps réel les coordonnées de la souris
    obtenues par « event.x » et « event.y ».
    La zone de texte est mise à jour grâce à la méthode .configure()."""
    abscisse = event.x
    ordonnee = event.y
    message.configure(text='Clic en X = {0} et Y = {1}'.format(abscisse, ordonnee))

##-----Création de la fenêtre-----##
fen = Tk()
fen.title('Morpion')


##-----Création des zones de texte-----##
message=Label(fen, text='Ici du texte.')
message.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3, sticky = W+E)


##-----Création des boutons-----##
bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row = 2, column = 1, padx=3, pady=3, sticky = S+W+E)

bouton_reload = Button(fen, text='Recommencer')
bouton_reload.grid(row = 2, column = 0, padx=3, pady=3, sticky = S+W+E)


##-----Création du canevas-----##
dessin=Canvas(fen, bg="white", width=301, height=301)
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)


##-----La grille-----##
lignes = []
for i in range(4):
    lignes.append(dessin.create_line(0, 100*i+2, 303, 100*i+2, width=3))
    lignes.append(dessin.create_line(100*i+2, 0, 100*i+2, 303, width=3))


##-----Evenements-----##
dessin.bind('<Button-1>', afficher)


##-----Programme principal-----##
fen.mainloop()                      # Boucle d'attente des événements

##-----Importation des Modules-----##
from tkinter import *


##----- Définition des Variables globales -----##
cases=[ [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
drapeau = True                              # True pour les croix, False pour les ronds
n = 1                                       # Numéro du tour de jeu


##----- Définition des Fonctions -----##
def afficher(event) :
    """ Entrées : Un événement de la souris
        Sortie : Affiche en temps réel les coordonnées de la case du clic de souris"""
    global drapeau, cases, n
    l = (event.y-2)//100                    # Ligne du clic
    c = (event.x-2)//100                    # Colonne du clic

    if (n < 10) and (cases[l][c] == 0):
        if drapeau:                              # drapeau == True
            dessin.create_line(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, fill = 'blue')
            dessin.create_line(100*c+8, 100*l+96, 100*c+96, 100*l+8, width = 5, fill = 'blue')
            cases[l][c] = 1
            message.configure(text='Aux ronds de jouer')

        else:
            dessin.create_oval(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, outline = 'red')
            cases[l][c] = -1
            message.configure(text='Aux croix de jouer')

        drapeau = not(drapeau)
        if (n >= 5) and (n <= 9):
            somme = verif(cases)
            if somme == 1 or somme == -1:
                n = gagner(somme)
            elif n == 9:
                n = gagner(0)
        n += 1


def verif(tableau):
    """ Entrées : un tableau "carré"
        Sorties : Calcule les sommes de chaque ligne/colonne/diagonale
            et vérifie l'alignement."""
    sommes = [0,0,0,0,0,0,0,0]             # Il y a 8 sommes à vérifier
    # Les lignes :
    sommes[0] = sum(tableau[0])
    sommes[1] = sum(tableau[1])
    sommes[2] = sum(tableau[2])
    # Les colonnes
    sommes[3] = tableau[0][0]+tableau[1][0]+tableau[2][0]
    sommes[4] = tableau[0][1]+tableau[1][1]+tableau[2][1]
    sommes[5] = tableau[0][2]+tableau[1][2]+tableau[2][2]
    # Les diagonales
    sommes[6] = tableau[0][0]+tableau[1][1]+tableau[2][2]
    sommes[7] = tableau[0][2]+tableau[1][1]+tableau[2][0]

    for i in range(8):                     # Parcours des sommes
        if sommes[i] == 3:
            return 1
        elif sommes[i] == -3:
            return -1
    return 0



def gagner(a):
    """Cette fonction indique le gagnant en modifiant le message et en
        renvoyant la valeur 9."""
    if a == 1:
        message.configure(text = 'Les croix ont gagné !')
    elif a == -1:
        message.configure(text = 'Les ronds ont gagné !')
    elif a == 0:
        message.configure(text = 'Match nul !')
    return 9



def reinit():
    """Cette fonction ré-initialise les variables globales."""
    global drapeau, cases, n
    cases = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    drapeau = True          # True pour les croix, False pour les ronds
    n = 1

    message.configure(text='Aux croix de jouer')
    dessin.delete(ALL)      # Efface toutes les figures
    lignes = []
    for i in range(4):
      lignes.append(dessin.create_line(0, 100*i+2, 303, 100*i+2, width=3))
      lignes.append(dessin.create_line(100*i+2, 0, 100*i+2, 303, width=3))


##-----Création de la fenêtre-----##
fen = Tk()
fen.title('Morpion')


##-----Création des zones de texte-----##
message=Label(fen, text='Aux croix de jouer')
message.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3, sticky = W+E)


##-----Création des boutons-----##
bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row = 2, column = 1, padx=3, pady=3, sticky = S+W+E)

bouton_reload = Button(fen, text='Recommencer', command=reinit)
bouton_reload.grid(row = 2, column = 0, padx=3, pady=3, sticky = S+W+E)


##-----Création du canevas-----##
dessin=Canvas(fen, bg="white", width=301, height=301)
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)


##-----La grille-----##
lignes = []


##-----Evenements-----##
dessin.bind('<Button-1>', afficher)


##-----Programme principal-----##
reinit()
fen.mainloop()                      # Boucle d'attente des événements
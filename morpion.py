#on admet la fonction global qui permet un transfert de variable san utiliser de return
#on admet le fonction event qui permet de récupérer les cliques et mouvement de la souris
#on admet la fonction quit qui stop le programme

#on considère la fonction tk qui perment de réaliser du graphique
import tkinter as tk
from tkinter import *


root = tk.Tk()
#assigner la taille des cellules à cellSize
cellSize = 200
#assigner le nombre de cellule composant la largeur et la longueur du tableau (3 pour un morpion normale)
boardSize = 3
#créer canvasSize contenant la taille de la fenêtre principale
canvasSize = cellSize * boardSize


#créer flag contenant True
flag=True


#créer victoire contenant "neutre"
victoire="neutre"
#créer tour contenant 0
tour=0
#assigner "red" à crossColor
crossColor="red"
#assigner "blue" à sphereColor
sphereColor="blue"



#définir la fonction initTableau qui permet de créer tableaAnalyse
def initTableau():

    #récupérer tableAnalyse grâce à la fonction global
    global tableAnalyse

    #créer une liste nommée tableAnalyse contenant [[0,0,0],[0,0,0],[0,0,0]]
    tableAnalyse=[[0,0,0]
                 ,[0,0,0]
                 ,[0,0,0]]



#définir la fonction fenêtre qui permet de remplir la fenêtre principale avec la grille de morpion
def fenetre():
    
    #pour x de 0 à boardSize
    for x in range(boardSize):

        #alors
        #pour y de 0 à boardSize
        for y in range(boardSize):

            #créer un rectangle ayant comme points opposés : y * cellSize; x * cellSize et y * cellSize + cellSize; x * cellSize + cellSize,
            canvas.create_rectangle(
                        
                        y * cellSize,
                        x * cellSize,
                        y * cellSize + cellSize,
                        x * cellSize + cellSize,
                        
                    )


#définir la fonction reinit servant à remettre les valeur à 0
def reinit():

    #récupérer la variable victoire grâce à la fonction global
    global victoire,tour
    
    #assigner 0 à tour
    tour=0
    #assigner la valeur "neutre" à la variable victoire
    victoire="neutre"
    #supprimer tous les dessin de la page principale
    canvas.delete(ALL)
    #invoquer la fonction fenetre
    fenetre()   
    #invoquer la fonction initTableau
    initTableau()


#définir la fonction croix contenant le paramètre cell et permettant de faire le dessin d'une croix
def croix(cell):

    #récupérer tour grâce à la fonction global
    global tour

    #créer une des 2 diagonales de la croix d'épaisseur 5 et de couleur crossColor par rapport a cell et cellSize
    canvas.create_line(cell[0] * cellSize + 10, cell[1] * cellSize + 10, (cell[0] + 1) * cellSize - 10, (cell[1] + 1) * cellSize - 10, width = 5, fill = crossColor)
    #créer l'autre diagonale de la croix d'épaisseur 5 et de couleur crossColor par rapport a cell et cellSize
    canvas.create_line(cell[0] * cellSize + 10, (cell[1] + 1) * cellSize - 10, (cell[0] + 1) * cellSize - 10, cell[1] * cellSize + 10, width = 5, fill = crossColor)
    #insérer 1 dans tableAnalyse en position [cell[0]][cell[1]]
    tableAnalyse[cell[0]][cell[1]]=1
    #incrémenter tour de 1
    tour=tour+1



#définir la fonction rond ayant comme paramètre cell et permettant de déssiner un rond
def rond(cell):

    global tour

    #créer un oval d'épaisseur 5 et de couleur spherreColor par rapport à cell et cellSize
    canvas.create_oval (cell[0] *cellSize+10, cell[1] * cellSize + 10, (cell[0] + 1) * cellSize - 10, (cell[1] + 1) * cellSize - 10, width = 5, outline=sphereColor)
    #insérer -1 dans tableAnalyse en position [cell[0]][cell[1]]
    tableAnalyse[cell[0]][cell[1]]=-1
    #incrémenter tour de 1
    tour=tour+1



#définir la fonction analyse permettant de faire ue analyse de chaque cellule du tableau et donner la victoire si nécessaire
def analyse():

    #récupérer tableAnalyse et victoire grâce à la fonction global
    global tableAnalyse,victoire

    #créer la liste winAnalyse contenant [0,0,0,0,0,0,0,0] (liste des analyses)
    winAnalyse = [0,0,0,0,0,0,0,0]

    """analyse de chaque colonnes"""
    #pour x inférieur à 3
    for x in range(3) :
        #alors
        #faire la somme des cellules composant la colonnes x du tableau et l'assigner à la valeur x de winAnalyse
        winAnalyse[x] = sum(tableAnalyse[x])

    """analyse de chaque lignes"""
    #pour x inférieur à 3
    for x in range(3) : 
    #faire la somme des cellules composant la lignes x et l'assigner à la valeur x+3 de winAnalyse
        winAnalyse[x+3] = tableAnalyse[0][x]+tableAnalyse[1][x]+tableAnalyse[2][x]

    """analyse de chaque diagonales"""
    #faire la somme des cellules composant la première diagonale et l'assigner à la septième valeur de winAnalyse
    winAnalyse[6] = tableAnalyse[0][0]+tableAnalyse[1][1]+tableAnalyse[2][2]
    #faire la somme des cellules composant la seconde diagonale et l'assigner à la huitième valeur de winAnalyse
    winAnalyse[7] = tableAnalyse[0][2]+tableAnalyse[1][1]+tableAnalyse[2][0]
        
    
    #si tour est iférieur ou égal à 9
    if tour <= 9:
        #alors
        #pour i entre 0 et 7 compris
        for i in range(8):
            #alors
            #si la valeur en position [i] dans winAnalyse est égale à 3
            if winAnalyse[i] == 3:
                #alors
                #assigner "croix" à victoire
                victoire="croix"
            #sinon si la valeur en position [i] dans winAnalyse est égale à -3
            elif winAnalyse[i] == -3:
                #alors
                #assigner "rond" à victoire
                victoire="rond"
            #sinon si tour est égal à 9 et victoire est égale à "neutre"
            elif tour == 9 and victoire =="neutre":
                #alors
                #assigner égalité à victoire
                victoire = "égalité"
                    



#définir game avec les paramètre cell
def game(cell):

    #récupérer flag et victoire grâce a la fonction global
    global flag,victoire
    
    #si la position [cell[0]][cell[1]] de tableAnalyse est égale à 0
    if tableAnalyse[cell[0]][cell[1]]==0:
        #alors
        #si flag
        if flag :
            #alors
            #invoquer la fonction croix avec le paramètre cell
            croix(cell)
            #inverser la valeur de flag
            flag=not(flag)
        #sinon
        else:
            #alors
            #invoquer la fonction rond avec le paramètre cell
            rond(cell)
            #inverser la valeur de flag
            flag=not(flag)
    #invoquer la fonction analyse
    analyse()

    #si victoire est différent de "neutre"
    if victoire!="neutre":
        #alors
        #ouvrir une nouvelle fenêtre
        fenPrinc = Tk()
        #si victoire est différent de "égalité"
        if victoire!="égalité":
            #alors
            #afficher { "Les gagnant sont les " victoire } en police "Courrier" de taille 30 et de couleur 'orange'
            monAffichage = Label(fenPrinc, text="Les gagnat sont les "+victoire,font=("Courrier",30), width=0, fg ='orange')
            monAffichage.pack()
        #sinon
        else:
            #alors
            #afficher "Égalité" en police "Courrier" de taille 30 et de couleur 'orange' et un écart dans l'axe x de 50
            monAffichage = Label(fenPrinc, text="Égalité",padx=50, font=("Courrier",30), width=0, fg ='orange')
            monAffichage.pack()

        #créer un boutton réinitialiser avec comme texte "Réinitialiser" et qui invoque la fonction reinit et détruit la fenPrinc
        reinitialiser = Button(fenPrinc, text="Réinitialiser", command=lambda:[reinit(),fenPrinc.destroy()])
        reinitialiser.pack()
        #créer un boutton quitter avec comme texte "Quitter" et qui invoque la fonction quit
        quitter = Button(fenPrinc, text="Quitter", command=quit)
        quitter.pack()
    


#définir la fonction afficher avec comme paramètre event
def afficher(event) :

    #récupérer victoire grâce à la fonction global
    global victoire
    
    # si victoire est égal à "neutre"
    if victoire=="neutre":
        #alors
        #assigner la valeur de event.x à abcisse
        abscisse = event.x
        #assigner la valeur de event.y à ordonnee
        ordonnee = event.y
        #assigner à cell la liste [int (abscisse / cellSize), int (ordonnee/cellSize)] (coordonnée de la cellule cliqué)
        cell=[int (abscisse / cellSize), int (ordonnee/cellSize)]
        #invoquer game avec les paramètre cell
        game(cell)

#créer une fenêtre de longueur canvasSize et de largeur canvasSize
canvas = tk.Canvas(root, width=canvasSize, height=canvasSize)
#invoquer la fonction fenetre
fenetre()
#invoquer la fonction initTableau
initTableau()
canvas.pack()

#invoquer la fonction afficher quand <Button-1> est cliqué (clique gauche)
canvas.bind('<Button-1>', afficher)
root.mainloop()
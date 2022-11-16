#on admet la fonction global qui permet un transfert de variable san utiliser de return
#on admet le fonction event qui permet de récupérer les cliques et mouvement de la souris
#on admet la fonction quit qui stop le programme

#on considère la fonction tk qui perment de réaliser du graphique
import tkinter as tk
from tkinter import *


root = tk.Tk()
#assigner la taille des cellules à cell_size
cell_size = 200
#assigner le nombre de cellule composant la largeur et la longueur du tableau (3 pour un morpion normale)
board_size = 3
#créer canvas_size contenant la taille de la fenêtre principale
canvas_size = cell_size * board_size

#créer un tuple nommé insert_rond contenant ('O',)
insert_rond = ('O',)
#créer un tuple nommé insert_croix contenant ('X',)
insert_croix = ('X',)
#créer flag contenant True
flag=True

#créer victoire contenant "neutre"
victoire="neutre"


#définir la fonction initTableau qui permet de créer deux tableaux dans le terminal
def initTableau():

    #récupérer tableau et tableAnalyse grâce à la fonction global
    global tableau,tableAnalyse

    #créer la liste c contenant les terme 1,2,3
    c=[1,2,3]
    #créer la liste l contenant les terme 1,2,3
    l=[1,2,3]
    #créer une liste nommée tableau contenant les coordonnées de chaque cellules grâce à la liste l et la liste c
    tableau=[[(l[x],c[y]) for y in range (3)]for x in range(3)]
    #créer une liste nommée tableAnalyse contenant 9 fois "_"
    tableAnalyse=["_" for i in range(9)]



#définir la fonction fenêtre qui permet de remplir la fenêtre principale avec la grille de morpion
def fenetre():
    
    #pour x de 0 à board_size
    for x in range(board_size):

        #alors
        #pour y de 0 à board_size
        for y in range(board_size):

            #créer un rectangle ayant comme points opposés : y * cell_size; x * cell_size et y * cell_size + cell_size; x * cell_size + cell_size,
            canvas.create_rectangle(
                        
                        y * cell_size,
                        x * cell_size,
                        y * cell_size + cell_size,
                        x * cell_size + cell_size,
                        
                    )


#définir la fonction reinit servant à remettre les valeur à 0
def reinit():

    #récupérer la variable victoire grâce à la fonction global
    global victoire
    
    #assigner la valeur "neutre" à la variable victoire
    victoire="neutre"
    #supprimer tous les dessin de la page principale
    canvas.delete(ALL)
    #invoquer la fonction fenêtre
    fenetre()   
    #invoquer la fonction initTableau
    initTableau()


#définir la fonction croix contenant le paramètre cell et permettant de faire le dessin d'une croix
def croix(cell):

    #créer une des 2 diagonales de la croix par rapport a cell et cell_size
    canvas.create_line(cell[0] * cell_size + 10, cell[1] * cell_size + 10, (cell[0] + 1) * cell_size - 10, (cell[1] + 1) * cell_size - 10, width = 5, fill = "red")
    #créer l'autre diagonale de la croix par rapport a cell et cell_size
    canvas.create_line(cell[0] * cell_size + 10, (cell[1] + 1) * cell_size - 10, (cell[0] + 1) * cell_size - 10, cell[1] * cell_size + 10, width = 5, fill = "red")
    #insérer insert_croix dans le tableau en position cell[0]][cell[1]
    tableau[cell[0]][cell[1]]=tableau[cell[0]][cell[1]]+insert_croix
    #écrire tbleau dans le terminal
    print("tableau",tableau[cell[0]][cell[1]])



#définir la fonction rond ayant comme paramètre cell et permettant de déssiner un rond
def rond(cell):

    #créer un oval par rapport à cell et cell_size
    canvas.create_oval (cell[0] *cell_size+10, cell[1] * cell_size + 10, (cell[0] + 1) * cell_size - 10, (cell[1] + 1) * cell_size - 10, width = 5, outline="blue")
    #insérer insert_rond dans le tableau en position cell[0]][cell[1]
    tableau[cell[0]][cell[1]]=tableau[cell[0]][cell[1]]+insert_rond
    #écrire tbleau dans le terminal
    print("tableau",tableau[cell[0]][cell[1]])



#définir la fonction analyse permettant de faire ue analyse de chaque cellule dut tableau et donner la victoire si nécessaire
def analyse():

    global tableau,tableAnalyse,victoire

    for x in range (3):

        for y in range (3):

            if tableau[x][y].count('X')==1:

                tableAnalyse[x+y*3]='X'

            elif tableau[x][y].count('O')==1:

                tableAnalyse[x+y*3]='O'

    if tableAnalyse[0]=='X':
    
    
        if tableAnalyse[1]=='X' and tableAnalyse[2]=='X':
            
            victoire='X'
            
        elif tableAnalyse[3]=='X' and tableAnalyse[6]=='X':
            
            victoire='X'
            
        elif tableAnalyse[4]=='X' and tableAnalyse[8]=='X':
            
            victoire='X'
            
    if tableAnalyse[2]=='X':
        
        if tableAnalyse[5]=='X' and tableAnalyse[8]=='X':
            
            victoire='X'
            
        elif tableAnalyse[4]=='X' and tableAnalyse[6]=='X':
            
            victoire='X'
            
    if tableAnalyse[3]=='X' and tableAnalyse[4]=='X' and tableAnalyse[5]=='X':
        
        victoire='X'
        
    if tableAnalyse[6]=='X' and tableAnalyse[7]=='X' and tableAnalyse[8]=='X':
        
        victoire='X'
        
    if tableAnalyse[1]=='X' and tableAnalyse[4]=='X' and tableAnalyse[7]=='X':
        
        victoire='X'
    

    if tableAnalyse[0]=='O':
        
        if tableAnalyse[1]=='O' and tableAnalyse[2]=='O':
            
            victoire='O'
            
        elif tableAnalyse[3]=='O' and tableAnalyse[6]=='O':
            
            victoire='O'
            
        elif tableAnalyse[4]=='O' and tableAnalyse[8]=='O':
            
            victoire='O'
            
    if tableAnalyse[2]=='O':
        
        if tableAnalyse[5]=='O' and tableAnalyse[8]=='O':
            
            victoire='O'
            
        elif tableAnalyse[4]=='O' and tableAnalyse[6]=='O':
            
            victoire='O'
            
    if tableAnalyse[3]=='O' and tableAnalyse[4]=='O' and tableAnalyse[5]=='O':
        
        victoire='O'
        
    if tableAnalyse[6]=='O' and tableAnalyse[7]=='O' and tableAnalyse[8]=='O':
        
        victoire='O'
        
    if tableAnalyse[1]=='O' and tableAnalyse[4]=='O' and tableAnalyse[7]=='O':
        
        victoire='O'
        
    if tableAnalyse.count("_")==0 and victoire=="neutre":
        
        victoire = "égalité"
        
    print(tableAnalyse)
    print(victoire)



#définir game avec les paramètre cell et tableau
def game(cell,tableau):

    #récupérer flag et victoire grâce a la fonction global
    global flag,victoire

    #si flag
    if flag : 

        #alors
        #si la longueur de tableau en position [cell[0]][cell[1]] est égale à 2
        if len(tableau [cell[0]][cell[1]])==2:
            
            #invoquer la fonction croix avec le paramètre cell
            croix(cell)
            #inverser la valeur de flag
            flag=not(flag)   

    #sinon
    else:
        
        #alors
        #si la longueur de tableau e position [cell[0]][cell[1]] est égale à 2
        if len(tableau [cell[0]][cell[1]])==2:

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
        fen_princ = Tk()

        #si victoire est différent de "égalité"
        if victoire!="égalité":

            #alors
            #afficher "Les gagnant sont les " victoire en police courrier de taille 30 et de couleur '#FF6200' (orange)
            monAffichage = Label(fen_princ, text="Les gagnat sont les "+victoire,font=("Courrier",30), width=0, fg ='#FF6200')
            monAffichage.pack()
        
        #sinon
        else:

            #alors
            #afficher #afficher "Égalité" en police courrier de taille 30 et de couleur '#FF6200' (orange) 
            monAffichage = Label(fen_princ, text="Égalité",padx=50, font=("Courrier",30), width=0, fg ='#FF6200')
            monAffichage.pack()

        #créer un boutton réinitialiser avec comme texte "Réinitialiser" et qui invoque la fonction reinit et détruit la fen_princ
        reinitialiser = Button(fen_princ, text="Réinitialiser", command=lambda:[reinit(),fen_princ.destroy()])
        reinitialiser.pack()
        
        #créer un boutton quitter avec comme texte "Quitter" et qui invoque la fonction quit
        quitter = Button(fen_princ, text="Quitter", command=quit)
        quitter.pack()

    #écrire tableau dans le termiinal
    print(tableau)


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
        #assigner à cell la liste [int (abscisse / cell_size), int (ordonnee/cell_size)] (coordonnée de la cellule cliqué)
        cell=[int (abscisse / cell_size), int (ordonnee/cell_size)]
        #écrire abcisse,ordonne,cell dans le terminal
        print (abscisse,ordonnee,cell)
        #invoquer game avec les paramètre cell et tableau
        game(cell,tableau)

#créer une fenêtre de longueur canvas_size et de largeur canvas_size
canvas = tk.Canvas(root, width=canvas_size, height=canvas_size)
#invoquer la fonction fenetre
fenetre()
#invoquer la fonction initTableau
initTableau()
canvas.pack()

#afficher(tableau)
print (tableau)
#afficher tableAnalyse
print (tableAnalyse)
#invoquer la fonction afficher <Button-1> est cliqué (clique gauche)
canvas.bind('<Button-1>', afficher)
root.mainloop()
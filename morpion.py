import tkinter as tk
from tkinter import messagebox
from tkinter import *

fen_princ = Tk()
root = tk.Tk()
cell_size = 200
board_size = 3
canvas_size = cell_size * board_size

insert_rond = ('O',)
insert_croix = ('X',)
flag=True

victoire="neutre"

def initTableau():
    global tableau,tableAnalyse
    c=[1,2,3]
    l=[1,2,3]
    tableau=[[(l[x],c[y]) for y in range (3)]for x in range(3)]
    tableAnalyse=["_" for i in range(9)]

def fenetre():
    for x in range(board_size):
        for y in range(board_size):
            canvas.create_rectangle(
                        y * cell_size,
                        x * cell_size,
                        y * cell_size + cell_size,
                        x * cell_size + cell_size,
                    )

canvas = tk.Canvas(root, width=canvas_size, height=canvas_size)
fenetre()
initTableau()
canvas.pack()


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
    if tableAnalyse.count("_")==0:
        victoire = "égalité"
    print(tableAnalyse)
    print(victoire)


def croix(cell):
    canvas.create_line(cell[0] * cell_size + 10, cell[1] * cell_size + 10, (cell[0] + 1) * cell_size - 10, (cell[1] + 1) * cell_size - 10, width = 5, fill = "red")
    canvas.create_line(cell[0] * cell_size + 10, (cell[1] + 1) * cell_size - 10, (cell[0] + 1) * cell_size - 10, cell[1] * cell_size + 10, width = 5, fill = "red")
    tableau[cell[0]][cell[1]]=tableau[cell[0]][cell[1]]+insert_croix
    print("tableau",tableau[cell[0]][cell[1]])


def rond(cell):
    canvas.create_oval (cell[0] *cell_size+10, cell[1] * cell_size + 10, (cell[0] + 1) * cell_size - 10, (cell[1] + 1) * cell_size - 10, width = 5, outline="blue")
    tableau[cell[0]][cell[1]]=tableau[cell[0]][cell[1]]+insert_rond
    print("tableau",tableau[cell[0]][cell[1]])


def draw(cell,tableau):
    global flag,victoire
    if flag : 
        if len(tableau [cell[0]][cell[1]])==2:
            croix(cell)
            flag=not(flag)    
    else:
        if len(tableau [cell[0]][cell[1]])==2:
            rond(cell)
            flag=not(flag)
    analyse()
    if victoire!="neutre":
        if victoire=="égalité":
            monBouton = Button(fen_princ, text="BOUTON 1", command=lol())
            monBouton.pack()
        else:
            tk.messagebox.showinfo("Victoire",("Les " + victoire + " ont gangnés\n"))
        victoire="neutre"
        canvas.delete(ALL)
        fenetre()   # Efface toutes les figures
        initTableau()

    print(tableau)
    

def lol():
    print("lol")


def afficher(event) :
    global victoire
    """Cette fonction affiche en temps réel les coordonnées de la souris
    obtenues par « event.x » et « event.y ».
    La zone de texte est mise à jour grâce à la méthode .configure()."""
    if victoire=="neutre":
        abscisse = event.x
        ordonnee = event.y
        cell=[int (abscisse / cell_size), int (ordonnee/cell_size)]
        print (abscisse,ordonnee,cell)
        draw(cell,tableau)






print (tableau)
print (tableAnalyse)
canvas.bind('<Button-1>', afficher)
root.mainloop()
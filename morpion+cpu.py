
import tkinter as tk
from tkinter import *
import time
import random


root = tk.Tk()
cellSize = 200
boardSize = 3
canvasSize = cellSize * boardSize




victoire="neutre"
tour=0
crossColor="red"
sphereColor="blue"



def initTableau():

    global tableAnalyse

    tableAnalyse=[[0,0,0]
                 ,[0,0,0]
                 ,[0,0,0]]




def fenetre():
    
    for x in range(boardSize):

        for y in range(boardSize):

            canvas.create_rectangle(
                        
                        y * cellSize,
                        x * cellSize,
                        y * cellSize + cellSize,
                        x * cellSize + cellSize,
                        
                    )


def reinit():

    global victoire,tour
    
    tour=0
    victoire="neutre"
    canvas.delete(ALL)
    fenetre()   
    initTableau()


def croix(cell):

    global tour

    canvas.create_line(cell[0] * cellSize + 10, cell[1] * cellSize + 10, (cell[0] + 1) * cellSize - 10, (cell[1] + 1) * cellSize - 10, width = 5, fill = crossColor)
    canvas.create_line(cell[0] * cellSize + 10, (cell[1] + 1) * cellSize - 10, (cell[0] + 1) * cellSize - 10, cell[1] * cellSize + 10, width = 5, fill = crossColor)
    tableAnalyse[cell[0]][cell[1]]=1
    tour=tour+1



def rond(cell):

    global tour

    canvas.create_oval (cell[0] *cellSize+10, cell[1] * cellSize + 10, (cell[0] + 1) * cellSize - 10, (cell[1] + 1) * cellSize - 10, width = 5, outline=sphereColor)
    tableAnalyse[cell[0]][cell[1]]=-1
    tour=tour+1



def analyse():

    global tableAnalyse,victoire

    winAnalyse = [0,0,0,0,0,0,0,0]

    """analyse de chaque colonnes"""
    for x in range(3) :
        winAnalyse[x] = sum(tableAnalyse[x])

    """analyse de chaque lignes"""
    for x in range(3) : 
        winAnalyse[x+3] = tableAnalyse[0][x]+tableAnalyse[1][x]+tableAnalyse[2][x]

    """analyse de chaque diagonales"""
    winAnalyse[6] = tableAnalyse[0][0]+tableAnalyse[1][1]+tableAnalyse[2][2]
    winAnalyse[7] = tableAnalyse[0][2]+tableAnalyse[1][1]+tableAnalyse[2][0]
        
    
    if tour <= 9:
        for i in range(8):
            if winAnalyse[i] == 3:
                victoire="croix"
            elif winAnalyse[i] == -3:
                victoire="rond"
            elif tour == 9 and victoire =="neutre":
                victoire = "égalité"
    return winAnalyse
                    


def cpu():
    possibleWin="neutre"
    winAnalyse=analyse()
    for i in range(8):
            if winAnalyse[i] == 2:
                possibleWin=i

    if possibleWin=="neutre":

        if tableAnalyse[1][1]==0:
                cell=[1,1]
                rond(cell)
        else:
            cell=[random.choice([0,2]),random.choice([0,2])]
            rond(cell)

    if possibleWin==0:
        for i in range(3):
            if tableAnalyse[0][i]==0:
                cell=[0,i]
                rond(cell)
    if possibleWin==1:
        for i in range(3):
            if tableAnalyse[1][i]==0:
                cell=[1,i]
                rond(cell)
    if possibleWin==2:
        for i in range(3):
            if tableAnalyse[2][i]==0:
                cell=[2,i]
                rond(cell)

    if possibleWin==3:
        for i in range(3):
            if tableAnalyse[i][0]==0:
                cell=[i,0]
                rond(cell)
    if possibleWin==4:
        for i in range(3):
            if tableAnalyse[i][1]==0:
                cell=[i,1]
                rond(cell)
    if possibleWin==5:
        for i in range(3):
            if tableAnalyse[i][2]==0:
                cell=[i,2]
                rond(cell)

    if possibleWin==6:
        for i in range(3):
            if tableAnalyse[i][i]==0:
                cell=[i,i]
                rond(cell)
    if possibleWin==7:
        for i in range(3):
            if tableAnalyse[(i*(0-1)+2)][i]==0:
                cell=[(i*(0-1)+2),i]
                rond(cell)
    
        
                
    

        
    











def game(cell):

    global victoire
    analyse()
    if  tableAnalyse[cell[0]][cell[1]]==0:
        croix(cell)
        cpu()
    


    if victoire!="neutre":
        fenPrinc = Tk()
        if victoire!="égalité":
            monAffichage = Label(fenPrinc, text="Les gagnat sont les "+victoire,font=("Courrier",30), width=0, fg ='orange')
            monAffichage.pack()
        else:
            monAffichage = Label(fenPrinc, text="Égalité",padx=50, font=("Courrier",30), width=0, fg ='orange')
            monAffichage.pack()

        reinitialiser = Button(fenPrinc, text="Réinitialiser", command=lambda:[reinit(),fenPrinc.destroy()])
        reinitialiser.pack()
        quitter = Button(fenPrinc, text="Quitter", command=quit)
        quitter.pack()
    


def afficher(event) :

    global victoire
    
    if victoire=="neutre":
        abscisse = event.x
        ordonnee = event.y
        cell=[int (abscisse / cellSize), int (ordonnee/cellSize)]
        game(cell)

canvas = tk.Canvas(root, width=canvasSize, height=canvasSize)
fenetre()
initTableau()
canvas.pack()

canvas.bind('<Button-1>', afficher)
root.mainloop()
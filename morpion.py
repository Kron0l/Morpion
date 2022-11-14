import tkinter as tk

root = tk.Tk()
cell_size = 200
board_size = 3
canvas_size = cell_size * board_size

insert_rond = ('O',)
insert_croix = ('X',)
flag=True


c=[1,2,3]
l=[1,2,3]
tableau=[[(l[x],c[y]) for y in range (3)]for x in range(3)]


canvas = tk.Canvas(root, width=canvas_size, height=canvas_size)
canvas.pack()


def croix(cell):
    canvas.create_line(cell[0] * cell_size + 10, cell[1] * cell_size + 10, (cell[0] + 1) * cell_size - 10, (cell[1] + 1) * cell_size - 10, width = 5, fill = "red")
    canvas.create_line(cell[0] * cell_size + 10, (cell[1] + 1) * cell_size - 10, (cell[0] + 1) * cell_size - 10, cell[1] * cell_size + 10, width = 5, fill = "red")
    tableau[cell[0]][cell[1]]=tableau[cell[0]][cell[1]]+insert_croix
    print(cell)


def rond(cell):
    canvas.create_oval (cell[0] *cell_size+10, cell[1] * cell_size + 10, (cell[0] + 1) * cell_size - 10, (cell[1] + 1) * cell_size - 10, width = 5, outline="blue")
    tableau[cell[0]][cell[1]]=tableau[cell[0]][cell[1]]+insert_rond
    print(cell)


def draw(cell,flag):
    if flag : 
        croix(cell)
    else:
        rond(cell)
    print(tableau)





def afficher(event) :
    
    global flag
    """Cette fonction affiche en temps réel les coordonnées de la souris
    obtenues par « event.x » et « event.y ».
    La zone de texte est mise à jour grâce à la méthode .configure()."""
    abscisse = event.x
    ordonnee = event.y
    cell=[int (abscisse / cell_size), int (ordonnee/cell_size)]
    print (abscisse,ordonnee,cell)
    
    flag=not(flag)
    draw(cell,flag)



for x in range(board_size):
    for y in range(board_size):
        canvas.create_rectangle(
                    y * cell_size,
                    x * cell_size,
                    y * cell_size + cell_size,
                    x * cell_size + cell_size,
                )



print (tableau)
canvas.bind('<Button-1>', afficher)
root.mainloop()


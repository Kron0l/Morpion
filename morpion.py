import tkinter as tk

root = tk.Tk()
flag=-1
cell_size = 200
board_size = 3
canvas_size = cell_size * board_size



canvas = tk.Canvas(root, width=canvas_size, height=canvas_size)
canvas.pack()


def croix(cell,flag):
    print (flag)
    canvas.create_line(cell[0] * cell_size + 10, cell[1] * cell_size + 10, (cell[0] + 1) * cell_size - 10, (cell[1] + 1) * cell_size - 10, width = 5, fill = "red")
    canvas.create_line(cell[0] * cell_size + 10, (cell[1] + 1) * cell_size - 10, (cell[0] + 1) * cell_size - 10, cell[1] * cell_size + 10, width = 5, fill = "red")
    print(cell)


def rond(cell,flag):
    print (flag)
    canvas.create_oval (cell[0] *cell_size+10, cell[1] * cell_size + 10, (cell[0] + 1) * cell_size - 10, (cell[1] + 1) * cell_size - 10, width = 5, outline="blue")
    print(cell)


def player(cell,flag):
    if flag==1:
        flag=0
    else:
        flag=1
    draw(cell,flag)


def draw(cell,flag):
    if flag == 1:
        croix(cell,flag)
    elif flag == 0:
        rond(cell,flag)
    player(cell,flag)




def afficher(event) :
    """Cette fonction affiche en temps réel les coordonnées de la souris
    obtenues par « event.x » et « event.y ».
    La zone de texte est mise à jour grâce à la méthode .configure()."""
    abscisse = event.x
    ordonnee = event.y
    cell=[int (abscisse / cell_size), int (ordonnee/cell_size)]
    print (abscisse,ordonnee,cell)
    player(cell,flag)
    return abscisse,ordonnee,cell




for x in range(board_size):
    tab = [[(x,y) for y in range (board_size)]for i in range (1)]
    for i in tab :
        print (i)



for x in range(board_size):
    for y in range(board_size):
        canvas.create_rectangle(
                    y * cell_size,
                    x * cell_size,
                    y * cell_size + cell_size,
                    x * cell_size + cell_size,
                )


canvas.bind('<Button-1>', afficher)
root.mainloop()


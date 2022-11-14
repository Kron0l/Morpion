import tkinter as tk


root = tk.Tk()

cell_size = 200
board_size = 3
canvas_size = cell_size * board_size
x=1
y=1



canvas = tk.Canvas(root, width=canvas_size, height=canvas_size)
canvas.pack()


def croix(cell):
    canvas.create_line(cell[0] * cell_size + 10, cell[1] * cell_size + 10, (cell[0] + 1) * cell_size - 10, (cell[1] + 1) * cell_size - 10, width = 5, fill = "red")
    canvas.create_line(cell[0] * cell_size + 10, (cell[1] + 1) * cell_size - 10, (cell[0] + 1) * cell_size - 10, cell[1] * cell_size + 10, width = 5, fill = "red")
    print(cell)
    print((cell[1] + 1) * cell_size - 10)


def draw(cell) :
    if cell[1] < 1 :
        if cell[0] < 1 :
            croix(cell)
        elif cell[0] < 2 :
            croix(cell)
        else:
            croix(cell)
    elif cell[1] < 2 :
        if cell[0] < 1 :
            croix(cell)
        elif cell[0] < 2 :
            croix(cell)
        else:
            croix(cell)
    else :
        if cell[0] < 1 :
            croix(cell)
        elif cell[0] < 2 :
            croix(cell)
        else:
            croix(cell)




def afficher(event) :
    """Cette fonction affiche en temps réel les coordonnées de la souris
    obtenues par « event.x » et « event.y ».
    La zone de texte est mise à jour grâce à la méthode .configure()."""
    abscisse = event.x
    ordonnee = event.y
    cell=[int (abscisse / 200), int (ordonnee/200)]
    print (abscisse,ordonnee,cell)
    draw(abscisse,ordonnee,cell)
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
canvas.bind('<Button-3>', afficher)
root.mainloop()


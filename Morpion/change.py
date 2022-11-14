root = tk.Tk()
 
canvas = tk.Canvas(root, width=canvas_size, height=canvas_size)
canvas.pack()

canvas.create_rectangle(
            y * cell_size,
            x * cell_size,
            y * cell_size + cell_size,
            x * cell_size + cell_size,
        )

root.mainloop()
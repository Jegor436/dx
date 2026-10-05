import tkinter as tk
import math

cell_size = 30
grid_width = 50
grid_height = 45

WIDTH = cell_size * grid_width
HEIGHT = cell_size * grid_height

logs = tk.Tk()
logs.title("Koordinatu plakne")
logs.geometry("900x600")

kanva = tk.Canvas(logs, width=900, height=600, bg="white")
kanva.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

for x in range(0, WIDTH, cell_size):
    kanva.create_line(x, 0, x, HEIGHT, fill="black")

for y in range(0, HEIGHT, cell_size):
    kanva.create_line(0, y, WIDTH, y, fill="black")

kanva.create_line(
    30, 350, 800, 350, 
    fill="black", width=3, arrow=tk.LAST
)

kanva.create_line(
    420, 30, 420, 650, 
    fill="black", width=3, arrow=tk.FIRST
)

logs.mainloop()
    
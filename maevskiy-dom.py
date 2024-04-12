import tkinter as tk

root = tk.Tk()
root.title("Маєвський")

canvas = tk.Canvas(root, width = 400, height = 400, bg = "#00cfff")
canvas.pack()

# поверхи

canvas.create_rectangle(100, 250, 300, 400, fill = "yellow")
canvas.create_rectangle(120, 150, 280, 250, fill = "yellow")
canvas.create_rectangle(130, 60, 270, 150, fill = "yellow")

# двері

canvas.create_rectangle(165, 300, 235, 400, fill = "brown")

# вікна

canvas.create_rectangle(150, 170, 180, 230, fill = "light blue")
canvas.create_rectangle(220, 170, 250, 230, fill = "light blue")
canvas.create_rectangle(150, 80, 180, 130, fill = "light blue")
canvas.create_rectangle(220, 80, 250, 130, fill = "light blue")

# ручка двері

canvas.create_oval(215, 350, 230, 365, fill = "light yellow")

# лінії для вікон

canvas.create_line(165, 170, 165, 230, fill = "black")
canvas.create_line(150, 200, 180, 200, fill = "black")
canvas.create_line(235, 170, 235, 230, fill = "black")
canvas.create_line(220, 200, 250, 200, fill = "black")
canvas.create_line(165, 80, 165, 130, fill = "black")
canvas.create_line(150, 105, 180, 105, fill = "black")
canvas.create_line(235, 80, 235, 130, fill = "black")
canvas.create_line(220, 105, 250, 105, fill = "black")

# дах

canvas.create_polygon(130, 60, 200, 10, 270, 60, fill = "red", outline = "black")

root.mainloop()
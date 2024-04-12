import tkinter as tk

class first_app:
    def __init__(self, master):
        self.master = master
        self.master.title("First app")
        self.canvas = tk.Canvas(master, width=400, height=400, bg='lightgray')
        self.canvas.pack()

        self.draw_circle(100, 100, 50, 'Коло')
        self.draw_square(250, 100, 100, 'Квадрат')
        self.draw_sector(100, 250, 50, 45, 'Сектор')
        self.draw_triangle(250, 250, 100, 'Трикутник')

    def draw_circle(self, x, y, radius, label):
        self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, outline='blue', fill='lightblue')
        self.canvas.create_text(x, y, text=label)

    def draw_square(self, x, y, size, label):
        self.canvas.create_rectangle(x-size/2, y-size/2, x+size/2, y+size/2, outline='green', fill='lightgreen')
        self.canvas.create_text(x, y, text=label)

    def draw_sector(self, x, y, radius, angle, label):
        start_angle = 90 - angle/2
        end_angle = 90 + angle/2
        self.canvas.create_arc(x-radius, y-radius, x+radius, y+radius, start=start_angle, extent=angle, outline='red', fill='pink')
        self.canvas.create_text(x, y, text=label)

    def draw_triangle(self, x, y, size, label):
        half_size = size / 2
        points = [x, y-half_size, x+half_size, y+half_size, x-half_size, y+half_size]
        self.canvas.create_polygon(points, outline='purple', fill='lavender')
        self.canvas.create_text(x, y, text=label)

class second_app:
    def __init__(self, master):
        self.master = master
        self.master.title("Pyramid App")
        self.canvas = tk.Canvas(master, width=400, height=400, bg='white')
        self.canvas.pack()

        self.draw_pyramid(200, 200, 150, 150)

        self.button = tk.Button(master, text="Змінити колір фону", command=self.change_bg_color)
        self.button.pack()

    def draw_pyramid(self, x, y, base_width, height):
        top_x = x
        top_y = y - height

        base_left_x = x - base_width / 2
        base_left_y = y + height / 2
        base_right_x = x + base_width / 2
        base_right_y = y + height / 2

        self.canvas.create_line(top_x, top_y, base_left_x, base_left_y, fill='black', width=2)
        self.canvas.create_line(top_x, top_y, base_right_x, base_right_y, fill='black', width=2)
        self.canvas.create_line(base_left_x, base_left_y, base_right_x, base_right_y, fill='black', width=2)

        self.canvas.create_text(top_x, top_y, text="S", anchor='s', font=('Arial', 12, 'bold'))
        self.canvas.create_text(base_left_x, base_left_y, text="A", anchor='se', font=('Arial', 12, 'bold'))
        self.canvas.create_text(base_right_x, base_right_y, text="B", anchor='sw', font=('Arial', 12, 'bold'))

    def change_bg_color(self):
        colors = ['white', 'lightgray', 'lightcyan', 'lightgreen', 'lightpink']
        current_color = self.canvas['bg']
        next_color_index = (colors.index(current_color) + 1) % len(colors)
        self.canvas['bg'] = colors[next_color_index]

class third_app:
    def __init__(self, master):
        self.master = master
        self.master.title("Shapes App")
        self.canvas = tk.Canvas(master, width=500, height=400, bg='lightgray')
        self.canvas.pack()
        self.draw_shapes()

        self.move_down_button = tk.Button(master, text="Перемістити вниз", command=self.move_down)
        self.move_down_button.pack(side='left', padx=10)
        self.change_color_button = tk.Button(master, text="Змінити колір", command=self.change_color)
        self.change_color_button.pack(side='left')

    def draw_shapes(self):
        self.canvas.create_oval(50, 50, 150, 100, outline='blue', fill='lightblue')
        self.canvas.create_rectangle(200, 50, 300, 100, outline='red', fill='lightcoral')
        self.canvas.create_oval(350, 50, 450, 100, outline='green', fill='lightgreen')

    def move_down(self):
        self.canvas.move("all", 0, 50)

    def change_color(self):
        new_color = 'orange'
        self.canvas.itemconfig("all", outline=new_color, fill=new_color)



root = tk.Tk()
app = first_app(root)
root.mainloop()


root = tk.Tk()
app = second_app(root)
root.mainloop()


root = tk.Tk()
app = third_app(root)
root.mainloop()
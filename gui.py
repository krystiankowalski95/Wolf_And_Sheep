from tkinter import *
from Wolf import Wolf
from Sheep import Sheep,sheepList

init_pos_limit = 200

window = Tk()
window.title('Szymi & Krystiano')
window.geometry(str(3 * init_pos_limit) + 'x' + str(3 * init_pos_limit+50))
window.resizable(False, False)

canvas = Canvas(window, width=3* init_pos_limit, height=3 * init_pos_limit, bg="#363636")
canvas.pack()

label_value = StringVar()
sheep_label = Label(window, width=50, textvariable=label_value).place(x=init_pos_limit, y=3 * init_pos_limit+10)

point_list = []
wolf_point_list = []

def remove_points():
    for point in point_list:
        canvas.delete(point)
    remove_wolf_points()

def remove_wolf_points():
    for point in wolf_point_list:
        canvas.delete(point)

def update_sheep_label():
    label_value.set('Sheeps alive no. : ' + str(len(sheepList)))

def moveAllSheeps():
    remove_points()
    i = 0
    for sheep in sheepList:
        sheep.move()
        point_list.append(create_circle(sheep.x_position, sheep.y_position, 5, "blue"))
        i = i + 1



def create_circle(x, y, r, color):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill=color)

wolf = Wolf(10,init_pos_limit)
wolf_point_list.append(create_circle(wolf.x_position, wolf.y_position, 5, "red"))

def left_click(event):
    add_sheep(event.x, event.y, 5)

def right_click(event):
    remove_wolf_points()
    wolf.change_position(event.x, event.y)
    wolf_point_list.append(create_circle(wolf.x_position,wolf.y_position,5,"red"))


def add_sheep(x,y,sheep_distance):
    sheepList.append(Sheep(sheep_distance, x, y))
    point_list.append(create_circle(x, y, 5, "blue"))
    update_sheep_label()


def step():
    if len(sheepList) == 0:
        popup = Toplevel(window)
        popup.title("No sheep alive !")
        display = Label(popup, text="You have to add sheeps to the map ! ")
        display.pack()
    else:
        simulate()

def reset():
    canvas.delete("all")
    sheepList.clear()
    update_sheep_label()
    remove_wolf_points()
    wolf.change_position(1.5 * init_pos_limit, 1.5 * init_pos_limit)
    wolf_point_list.append(create_circle(wolf.x_position, wolf.y_position, 5, "red"))



def simulate():
    moveAllSheeps()
    wolf.move();
    point_list.append(create_circle(wolf.x_position, wolf.y_position, 5, "red"))
    update_sheep_label()
    if len(sheepList) == 0:
        popup = Toplevel(window)
        popup.title("No sheep alive!")
        display = Label(popup, text = "All sheeps has been eaten!")
        display.pack()

canvas.bind("<Button-1>", left_click)
canvas.bind("<Button-3>", right_click)

step = Button(window, text="Step", width=10, height=1, command=step)\
    .place(x=init_pos_limit + 10, y=3 * init_pos_limit + 10)

reset = Button(window, text="Reset", width=10, height=1, command=reset)\
    .place(x=init_pos_limit - 100, y=3 * init_pos_limit + 10)


if __name__ == '__main__':
    window.mainloop()
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

var = StringVar()
sheep_label = Label(window, width=init_pos_limit//10, textvariable=var).place(x=2 * init_pos_limit, y=3 * init_pos_limit + init_pos_limit//21)

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
    var.set('Sheeps alive no. : ' + str(len(sheepList)))

def moveAllSheeps():
    remove_points()
    for sheep in sheepList:
        sheep.move()
        point_list.append(create_circle(sheep.x_position, sheep.y_position, 1, "blue"))



def create_circle(x, y, r, color):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill=color)

wolf = Wolf(10,init_pos_limit)
wolf_point_list.append(create_circle(wolf.x_position, wolf.y_position, 1, "red"))


def key(event):
    print("pressed", repr(event.char))


def left_click(event):
    add_sheep(event.x, event.y, 5)

def right_click(event):
    remove_wolf_points()
    wolf.change_position(event.x, event.y)
    wolf_point_list.append(create_circle(wolf.x_position,wolf.y_position,1,"red"))


def add_sheep(x,y,sheep_distance):
    sheepList.append(Sheep(sheep_distance, x, y))
    point_list.append(create_circle(x, y, 1, "blue"))
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
    wolf.change_position(1.5 * init_pos_limit, 1.5 * init_pos_limit)
    sheepList.clear()
    update_sheep_label()
    canvas.delete("all")


def simulate():
    moveAllSheeps()
    wolf.move();
    point_list.append(create_circle(wolf.x_position, wolf.y_position, 1, "red"))
    update_sheep_label()

canvas.bind("<Key>", key)
canvas.bind("<Button-1>", left_click)
canvas.bind("<Button-2>", right_click)
canvas.bind("<Button-3>", right_click)

step = Button(window, text="Step", width=init_pos_limit//30, height=1, command=step)\
    .place(x=init_pos_limit + 10, y=3 * init_pos_limit + init_pos_limit//20)

reset = Button(window, text="Reset", width=init_pos_limit//30, height=1, command=reset)\
    .place(x=init_pos_limit - 50, y=3 * init_pos_limit + init_pos_limit//20)


if __name__ == '__main__':
    window.mainloop()
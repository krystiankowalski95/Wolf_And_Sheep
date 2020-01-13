import math
from Animal import Animal
from Sheep import sheep_list,eaten_sheeps
import uuid
import numpy

class Wolf(Animal):
    def __init__(self, wolf_move_dist,init_pos_limit):
        self.id = uuid.uuid1()
        self.move_distance = wolf_move_dist
        self.x_position = 1.5 * init_pos_limit
        self.y_position = 1.5 * init_pos_limit


    def move(self):
        minimum = math.sqrt((sheep_list[0].x_position - self.x_position)**2 +(sheep_list[0].y_position - self.y_position)**2)
        index = 0
        for i in range(len(sheep_list)):
            if i == 0:
                continue    #przed forem, minimum jest liczone dla i=0
            distance = math.sqrt((sheep_list[i].x_position - self.x_position)**2 +(sheep_list[i].y_position - self.y_position)**2)
            if minimum > distance:
                minimum = distance
                index = i

        sheep_to_follow = sheep_list[index]
        if minimum <= self.move_distance:
            self.x_position = sheep_list[index].x_position
            self.y_position = sheep_list[index].y_position
            eaten_sheeps.append(sheep_list[index])
            sheep_list.remove((sheep_list[index]))
        else:
        #  przesunięcie w kierunku pozycji owcy
            vect = numpy.array([sheep_to_follow.x_position - self.x_position, sheep_to_follow.y_position - self.y_position])
            vect = self.normalize(vect) * self.move_distance
            self.x_position += vect[0]
            self.y_position += vect[1]

    def normalize(self, v):
        norm = numpy.linalg.norm(v)
        if norm == 0:
            return v
        return v / norm

    def change_position(self, x, y):
        self.x_position = x
        self.y_position = y






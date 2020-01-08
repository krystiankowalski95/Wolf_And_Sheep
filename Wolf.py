import math
from Animal import Animal
from Sheep import sheepList, eatenSheeps
import uuid
import numpy

class Wolf(Animal):
    def __init__(self, wolf_move_dist,init_pos_limit):
        self.id = uuid.uuid1()
        self.move_distance = wolf_move_dist
        self.x_position = 1.5 * init_pos_limit
        self.y_position = 1.5 * init_pos_limit


    def move(self):
        minimum = math.sqrt((sheepList[0].x_position - self.x_position)**2 +(sheepList[0].y_position - self.y_position)**2)
        index = 0
        for i in range(len(sheepList)):
            if i == 0:
                continue    #przed forem, minimum jest liczone dla i=0
            distance = math.sqrt((sheepList[i].x_position - self.x_position)**2 +(sheepList[i].y_position - self.y_position)**2)
            if minimum > distance:
                minimum = distance
                index = i

        sheep2follow = sheepList[index]
        if minimum <= self.move_distance:
            print("Sheep {} has been eaten".format(sheepList[index].id))
            self.x_position = sheepList[index].x_position
            self.y_position = sheepList[index].y_position
            eatenSheeps.append(sheepList[index])
            sheepList.remove((sheepList[index]))
        else:
        #  przesunięcie w kierunku pozycji owcy
            vect = numpy.array([sheep2follow.x_position - self.x_position, sheep2follow.y_position - self.y_position])
            vect = self.normalize(vect) * self.move_distance
            self.x_position += vect[0]
            self.y_position += vect[1]
        print("Wolf's position = ({0:.3f}, {1:.3f})".format(self.x_position, self.y_position))

    def normalize(self, v):
        norm = numpy.linalg.norm(v)
        if norm == 0:
            return v
        return v / norm

    def change_position(self, x, y):
        self.x_position = x
        self.y_position = y






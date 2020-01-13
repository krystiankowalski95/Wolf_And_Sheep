import uuid

from Animal import Animal
import random

sheep_list = []
eaten_sheeps = []

class Sheep(Animal):
    def __init__(self, sheep_move_dist,init_pos_limit):
        self.id = uuid.uuid1()
        self.move_distance = sheep_move_dist
        self.x_position = random.randrange(-1.5 * init_pos_limit, 1,5 * init_pos_limit)
        self.y_position = random.randrange(-1.5 * init_pos_limit, 1,5 * init_pos_limit)

    def __init__(self, sheep_move_dist, x, y):
        self.id = uuid.uuid1()
        self.move_distance = sheep_move_dist
        self.x_position = x
        self.y_position = y

    def move(self):
        moveList = [(-self.move_distance, 0) , (self.move_distance,0), (0,-self.move_distance), (0,self.move_distance)]
        x,y = random.choice(moveList)
        self.x_position += x
        self.y_position += y

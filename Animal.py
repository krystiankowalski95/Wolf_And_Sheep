from abc import abstractmethod
import uuid

class Animal:
    def __init__(self, x, y):
        self.x_position = x
        self.y_position = y

    @abstractmethod
    def move(self):
        ...
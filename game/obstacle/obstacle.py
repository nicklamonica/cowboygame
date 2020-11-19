from abc import ABC, abstractmethod
import pygame

class Obstacle(ABC):

    def __init__(self, startX, startY):
        self.x, self.y = startX, startY
        self.height, self.width = 0, 0
        self.color = (28, 252, 3)
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def draw(self, window):
        pass

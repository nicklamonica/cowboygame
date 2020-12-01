from abc import ABC, abstractmethod
import pygame

class Obstacle(ABC):

    def __init__(self, startX, startY, asset_dir):
        self.asset_dir =  asset_dir
        self.x, self.y = startX, startY
        self.height, self.width = 0, 0
        self.color = (28, 252, 3)
    def update(self, diff):
        self.x -= diff
    @abstractmethod
    def draw(self, window):
        pass

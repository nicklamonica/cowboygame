import pygame
from .obstacle import Obstacle

class Rock(Obstacle):
    def __init__(self, startX, startY):
        super().__init__(startX, startY)
        self.width, self.height = 20, 20
        self.color = (97, 94, 87)
    def update(self):
        self.x -= 5
        return self.x, self.y
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
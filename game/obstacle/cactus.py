import pygame
import os
from .obstacle import Obstacle

class Cactus(Obstacle):
    def __init__(self, startX, startY, asset_dir):
        super().__init__(startX, startY, asset_dir)
        self.width, self.height = 20, 60
        self.color = (28, 252, 3)
        self.cactus = pygame.image.load(os.path.join(asset_dir, "cactus.png"))
        self.cactus = pygame.transform.scale(self.cactus, (self.width, self.height))
        self.damage = 25
        
    def draw(self, window):
        window.blit(self.cactus, (self.x, self.y))
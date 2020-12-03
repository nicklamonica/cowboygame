import pygame
import os
from .obstacle import Obstacle

class Rock(Obstacle):
    def __init__(self, startX, startY, asset_dir):
        super().__init__(startX, startY, asset_dir)
        self.width, self.height = 32, 32
        self.color = (97, 94, 87)
        self.rock = pygame.image.load(os.path.join(asset_dir, "rock.png"))
        self.rock = pygame.transform.scale(self.rock, (self.width, self.height))
        self.damage = 15

    def draw(self, window):
        window.blit(self.rock, (self.x, self.y))

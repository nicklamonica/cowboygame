import pygame
import os
from .obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, startX, startY, asset_dir):
        super().__init__(startX, startY, asset_dir)
        self.width, self.height = 40, 40
        self.color = (86, 79, 3)
        self.fly = [pygame.image.load(os.path.join(asset_dir, "bird" + str(i) + ".png")) for i in range(4)]
        for i in range(len(self.fly)):
            self.fly[i] = pygame.transform.scale(self.fly[i], (self.width, self.height))
        self.flyingIter = 0
    
    def draw(self, window):
        self.flyingIter = (self.flyingIter+1) % (len(self.fly)*3)
        window.blit(self.fly[self.flyingIter//3], (self.x, self.y))
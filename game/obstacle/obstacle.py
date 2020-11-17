import pygame

class Obstacle:

    def __init__(self, startX, startY):
        self.x, self.y = startX, startY
        self.height, self.width = 0, 0
        self.color = (28, 252, 3)

    def update(self):
        self.x -= 5
        return self.x, self.y

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

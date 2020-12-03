import pygame
import os

class StatusBar:
    def __init__(self, win):
        self.red = (255,0,0)
        self.x = 200
        self.y = 20
        self.width = 200
        self.height = 20
        self.score = 0
        self.font = pygame.font.SysFont('Raleway', 20)

    def updateHealth(self, newHealth):
        self.health = newHealth

    def updateScore(self, newScore):
        self.score = newScore

    def draw(self, win):
        # health bar
        pygame.draw.rect(win, self.red, (self.x, self.y, self.width * (self.health * 0.01), self.height))
        # score 
        text = self.font.render(f"Score: {self.score}", 1, (0,0,0))
        win.blit(text, (390, 10))


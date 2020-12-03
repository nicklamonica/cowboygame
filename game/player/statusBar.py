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
        self.level = 1
        self.font = pygame.font.SysFont('Raleway', 20)

    def updateHealth(self, newHealth):
        self.health = newHealth

    def updateScore(self, newScore):
        self.score = newScore

    def updateLevel(self, newLevel):
        self.level = newLevel
    
    def draw(self, win):
        # health bar
        pygame.draw.rect(win, self.red, (self.x, self.y, self.width * (self.health * 0.01), self.height))
        # score 
        text1 = self.font.render(f"Score: {self.score}", 1, (0,0,0))
        win.blit(text1, (500, 30))
        text2 = self.font.render(f"Level: {self.level}", 1, (0,0,0))
        win.blit(text2, (500, 20))



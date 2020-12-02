import pygame
import os

class HealthBar:
    def __init__(self, color, x, y, width, height, health, win):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.health = health
        self.bar = pygame.draw.rect(win, color, (x, y, width, height))

    def updateHealth(self, newHealth):
        self.health = newHealth

    def draw(self, win):
        self.bar = pygame.draw.rect(win, self.color, (self.x, self.y, self.width * (self.health * 0.01), self.height))

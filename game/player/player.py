import pygame
import os
from game.player.fightBehavior import *


class Player(FightBehavior):
    STANDING_HEIGHT = 60
    DUCKING_HEIGHT = 30

    def __init__(self, startX, startY, assetsPath):
        self.x, self.y = startX, startY
        self.width, self.height = 60, 60
        self.duckingY = self.y + self.DUCKING_HEIGHT
        self.isJumping = False
        self.isDucking = False
        self.jumpHeight = 10
        self.walkingIter = 0
        self.health = 100
        self.fb = FightBehavior()
        self.walk = [pygame.image.load(os.path.join(assetsPath, "walk" + str(i) + ".png")) for i in range(4)]
        for i in range(len(self.walk)):
            self.walk[i] = pygame.transform.scale(self.walk[i], (self.width, self.height))
        
        self.duck = pygame.image.load(os.path.join(assetsPath, "duck.png"))
        self.jump = pygame.image.load(os.path.join(assetsPath, "jump.png"))

    def getHitbox(self):
        return (self.x+5, self.y+15, self.width-20, self.height-15)

    def update(self):
        y = 0
        keys = pygame.key.get_pressed()
        if not self.isJumping:
            if keys[pygame.K_UP]:
                self.isJumping = True
            elif keys[pygame.K_DOWN]:
                self.isDucking = True
            else:
                self.isDucking = False
        if self.isJumping:
            self.y, self.jumpHeight, self.isJumping = self.fb.jump(self.jumpHeight, self.y, self.isJumping)
        elif self.isDucking:
            self.fb.duck(self.height, self.isDucking)
            self.height = self.DUCKING_HEIGHT
            self.y = self.duckingY
        else:
            self.isJumping = False
            self.isDucking = False
            self.height = self.STANDING_HEIGHT
            self.y = 475
        
    def draw(self, win):
        if self.isJumping:
            win.blit(self.jump, (self.x, self.y))
        elif self.isDucking:
            win.blit(self.duck, (self.x, self.y))
        else:
            self.walkingIter = (self.walkingIter+1) % (len(self.walk)*3)
            win.blit(self.walk[self.walkingIter//3], (self.x, self.y))
        pygame.draw.rect(win, (255, 0, 0), self.getHitbox(), 2)
    

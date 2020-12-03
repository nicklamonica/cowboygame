import pygame
import os
from game.player.fightBehavior import *


class Player(FightBehavior):
    def __init__(self, startX, startY, assetsPath):
        self.x, self.y = startX, startY
        self.width, self.height = 60, 60
        self.isJumping = False
        self.jumpHeight = 10
        self.walkingIter = 0
        self.health = 100
        self.fb = FightBehavior()
        print(assetsPath)
        self.walk = [pygame.image.load(os.path.join(assetsPath, "walk" + str(i) + ".png")) for i in range(4)]
        for i in range(len(self.walk)):
            self.walk[i] = pygame.transform.scale(self.walk[i], (self.width, self.height))
        
        self.jump = pygame.image.load(os.path.join(assetsPath, "jump.png"))

    def getHitbox(self):
        return (self.x-2, self.y+10, self.width-5, self.height-10)

    def update(self):
        y = 0
        keys = pygame.key.get_pressed()
        if not self.isJumping:
            if keys[pygame.K_UP]:
                self.isJumping = True
        else:
            self.y, self.jumpHeight, self.isJumping = self.fb.fJump(self.jumpHeight, self.y, self.isJumping)
        return self.x, self.y
    
    def draw(self, win):
        if self.isJumping == True:
            win.blit(self.jump, (self.x, self.y))
        else:
            self.walkingIter = (self.walkingIter+1) % (len(self.walk)*3)
            win.blit(self.walk[self.walkingIter//3], (self.x, self.y))
        pygame.draw.rect(win, (255, 0, 0), self.getHitbox(), 2)

    

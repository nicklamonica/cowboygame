import pygame
from game.player.fightBehavior import *


class Player(FightBehavior):
    def __init__(self, startX, startY):
        self.x, self.y = startX, startY
        self.isJumping = False
        self.jumpHeight = 10
        self.health = 100
        self.fb = FightBehavior()

    def update(self):
        y = 0
        keys = pygame.key.get_pressed()
        if not self.isJumping:
            if keys[pygame.K_UP]:
                self.isJumping = True
        else:
            self.y, self.jumpHeight, self.isJumping = self.fb.fJump(self.jumpHeight, self.y, self.isJumping)
            print(self.y)
        return self.x, self.y

    


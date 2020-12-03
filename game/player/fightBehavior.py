import pygame
from abc import ABC, abstractmethod

class FightBehavior:
    def __init__(self):
        super().__init__()
        pass

    def punch(self):
        p = punch()
    
    def fJump(self, jumpHeight, y, isJumping):
        j = jump(jumpHeight, y, isJumping)
        y = j.doAction()
        return y

    def duck(self):
        d = duck()
    
    def shoot(self):
        s = shoot()
    

class punch(FightBehavior):
    def __init__(self):
        pass

class jump(FightBehavior):
    def __init__(self, jumpHeight, y, isJumping):
        self.y = y
        self.jumpHeight = jumpHeight
        self.isJumping = isJumping

    def doAction(self):
        if self.jumpHeight >= -10:
            reverse = 1
            if self.jumpHeight < 0:
                reverse = -1
            self.y -= (self.jumpHeight ** 2) * 0.4 * reverse
            self.jumpHeight -= 1
        else:
            self.isJumping = False
            self.jumpHeight = 10
        return self.y, self.jumpHeight, self.isJumping


class duck(FightBehavior):
    def __init__(self):
        pass

class shoot(FightBehavior): 
    def __init__(self):
        pass
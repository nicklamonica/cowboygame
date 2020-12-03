import pygame
from abc import ABC, abstractmethod

class FightBehavior:
    def __init__(self):
        super().__init__()
        pass

    def punch(self):
        p = Punch()
    
    def jump(self, jumpHeight, y, isJumping):
        j = Jump(jumpHeight, y, isJumping)
        y = j.doAction()
        return y

    def duck(self, height, isDucking):
        d = Duck(height, isDucking)
        return d.doAction()
    
    def shoot(self):
        s = Shoot()
    

class Punch(FightBehavior):
    def __init__(self):
        pass

class Jump(FightBehavior):
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


class Duck(FightBehavior):
    def __init__(self, height, isDucking):
        self.height, self.isDucking = height, isDucking

    def doAction(self):
        return self.height, True

class Shoot(FightBehavior): 
    def __init__(self):
        pass
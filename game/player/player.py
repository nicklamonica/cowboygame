import pygame

class Player:
    def __init__(self, startX, startY):
        self.x, self.y = startX, startY
        self.isJumping = False
        self.jumpHeight = 10

    def update(self):
        keys = pygame.key.get_pressed()
        if not self.isJumping:
            if keys[pygame.K_UP]:
                self.isJumping = True
        else:
            self.jump()
        
        return self.x, self.y

    def jump(self):
        if self.jumpHeight >= -10:
            reverse = 1
            if self.jumpHeight < 0:
                reverse = -1
            self.y -= (self.jumpHeight ** 2) * 0.5 * reverse
            self.jumpHeight -= 1
        else:
            self.isJumping = False
            self.jumpHeight = 10


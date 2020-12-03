from .obstacleFactory import ObstacleFactory
import random
import pygame

class Map:
    def __init__(self, asset_root, numObs):
        self.numObs = numObs
        self.obstacles = ObstacleFactory().createObstacles(asset_root, numObs)

    def update(self, diff):
        # update obstacles pos, keep track of how many have past the
        numPast = 0
        for obstacle in self.obstacles:
            obstacle.update(diff)
            if obstacle.x <= 0:
                 numPast += 1
        if numPast >= self.numObs:
            self.resetObstacles()
            return True
        else:
            return False

    def draw(self, window):
        for obstacle in self.obstacles:
            obstacle.draw(window)
            pygame.draw.rect(window, (255, 0, 0), obstacle.getHitbox(), 2)

    def resetObstacles(self):
        i = random.randint(0, self.numObs-1)
        for obstacle in self.obstacles:
            obstacle.x = 600 + random.randint(150-i, 200) + (100*i)
            obstacle.hasCollided = False
            i = (i + 3) % (self.numObs*3)

    def checkCollision(self, playerPos):
        playerX, playerY, playerHeight, playerWidth = playerPos
        playerTop, playerBottom =  playerY + (playerHeight / 2) , playerY - (playerHeight / 2)
        playerRight, playerLeft =  playerX + (playerWidth / 2) , playerX - (playerWidth / 2)
        for obstacle in self.obstacles:
            obsX, obsY, obsHeight, obsWidth = obstacle.getHitbox()
            obsTop, obsBottom =  obsY + (obsHeight / 2) , obsY - (obsHeight / 2)
            obsRight, obsLeft =  obsX + (obsWidth / 2) , obsX - (obsWidth / 2)
            # if you have collided with an object
            if (playerLeft < obsRight and playerRight > obsLeft and \
                playerTop > obsBottom and playerBottom < obsTop  and not obstacle.hasCollided):
                obstacle.hasCollided = True
                return obstacle.damage
        return 0

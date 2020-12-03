from .obstacleFactory import ObstacleFactory
import random

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

    def resetObstacles(self):
        i = random.randint(0, self.numObs-1)
        for obstacle in self.obstacles:
            obstacle.x = 600 + random.randint(150-i, 200) + (100*i)
            i = (i + 3) % (self.numObs*3)



            

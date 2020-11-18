from .bird import Bird
from .cactus import Cactus
from .rock import Rock
import random

class ObstacleFactory:
    def createObstacles(self):
        obstacles = []
        for i in range(1, 10):
            rand = random.randint(0, 2)
            if rand == 0:
                obstacles.append(Cactus(random.randint(100, 500) + (100*i), 385))
            elif rand == 1:
                obstacles.append(Bird(random.randint(100, 500) + (100*i), 355))
            else:
                obstacles.append(Rock(random.randint(100, 500) + (100*i), 440))
        return obstacles
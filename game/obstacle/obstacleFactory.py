from obstacle import Obstacle
import random

class ObstacleFactory:
    def createObstacles(self):
        obstacles = []
        for i in range(1, 10):
            obstacles.append(Obstacle(random.randint(100, 500) + (100*i), 385))
        return obstacles

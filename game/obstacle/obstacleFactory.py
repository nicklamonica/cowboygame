from .bird import Bird
from .cactus import Cactus
from .rock import Rock

import random
import os

class ObstacleFactory:
    def createObstacles(self, asset_root):
        obstacles = []
        for i in range(3, 30, 3):
            rand = random.randint(0, 2)
            if rand == 0:
                obstacles.append(Cactus(random.randint(100, 200) + (100*i), 460, os.path.join(asset_root, 'cactus')))
            elif rand == 1:
                obstacles.append(Bird(random.randint(100, 200) + (100*i), 445, os.path.join(asset_root, 'bird')))
            else:
                obstacles.append(Rock(random.randint(100, 200) + (100*i), 505, os.path.join(asset_root, 'rock')))
        return obstacles
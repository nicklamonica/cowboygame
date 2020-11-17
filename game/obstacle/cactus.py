from game.obstacle.obstacle import Obstacle

class Cactus(Obstacle):
    def __init__(self, startX, startY):
        super().__init__(startX, startY)
        self.width, self.height = 20, 75
        self.color = (28, 252, 3)
from game.obstacle.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, startX, startY):
        super().__init__(startX, startY)
        self.width, self.height = 20, 10
        self.color = (86, 79, 3)
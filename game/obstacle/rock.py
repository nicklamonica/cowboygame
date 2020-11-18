from .obstacle import Obstacle

class Rock(Obstacle):
    def __init__(self, startX, startY):
        super().__init__(startX, startY)
        self.width, self.height = 20, 20
        self.color = (97, 94, 87)

class Obstacle:

    def __init__(self, startX, startY):
        self.x = startX
        self.y = startY

    def update(self):
        self.x -= 5
        return self.x, self.y

from mapBlock import MapBlock

class Map(MapBlock):
    # double underscore means it is a private method
    def __init__(self, width, height):
        self.mapWidth = width
        self.mapHeight = height

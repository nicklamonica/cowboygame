import pygame
from game.player.player import Player
from game.obstacle.obstacleFactory import ObstacleFactory

class Game:
    def __init__(self):
        self.run = False
        pygame.init()
        pygame.display.set_caption("Rootin Tootin Yeehaw Simulator")
        self.window = pygame.display.set_mode((500, 500))
        self.obstacles = ObstacleFactory().createObstacles() 
    
    def runGame(self):
        # init game
        self.run = True

        # create player
        self.player = Player(50, 415)

        # obstacle and enemy factory here

        while self.run:
            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            
            # update player position
            self.player.update()

            # update obstacle pos
            for obstacle in self.obstacles:
                obstacle.update()

            # update enemy positions
            enemyPos = []

            self.window.fill((0, 0, 0))
            self.draw()
            pygame.display.update()

        pygame.quit()
    
    
    # render all objects that are on screen
    def draw(self):
        # draw player
        pygame.draw.rect(self.window, (255, 0, 0), (self.player.x, self.player.y, 20, 45))

        # draw obsticals and enemies
        for obstacle in self.obstacles:
            obstacle.draw(self.window)



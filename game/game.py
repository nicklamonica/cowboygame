import pygame
from game.player.player import Player
from game.obstacle.obstacleFactory import ObstacleFactory

class Game:
    def __init__(self):
        self.run = False
        pygame.init()
        pygame.display.set_caption("Rootin Tootin Yeehaw Simulator")
        self.window = pygame.display.set_mode((500, 500))
        obstacleFactory =  ObstacleFactory()
        self.obstacles = obstacleFactory.createObstacles() 
    
    def runGame(self):
        # init game
        self.run = True

        # create player
        player = Player(50, 440)

        # obstacle and enemy factory here

        while self.run:
            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            
            # update player position
            playerPos = player.update()

            # update obstacle pos
            obstaclesPos = []
            for obstacle in self.obstacles:
                obstaclesPos.append(obstacle.update())

            # update enemy positions
            enemyPos = []

            self.window.fill((0, 0, 0))
            
            self.draw(playerPos, obstaclesPos, enemyPos)

            pygame.display.update()

        pygame.quit()
    
    
    # render all objects that are on screen
    def draw(self, playerPos, obstaclesPos, enemyPos):
        # draw player
        pygame.draw.rect(self.window, (255, 0, 0), (playerPos[0], playerPos[1], 20, 20) )
        # draw obsticals and enemies
        for obstaclePos in obstaclesPos:
            pygame.draw.rect(self.window, (28, 252, 3) , (obstaclePos[0], obstaclePos[1], 20, 75))


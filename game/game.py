import pygame
from game.player.player import Player

class Game:
    def __init__(self):
        self.run = False
        pygame.init()
        pygame.display.set_caption("Rootin Tootin Yeehaw Simulator")
        self.window = pygame.display.set_mode((500, 500))
        return
    
    def runGame(self):
        # init game
        self.run = True
        player = Player(50, 440)

        # obstacle and enemy factory here

        while self.run:

            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            

            playerPos = player.update()

            self.window.fill((0, 0, 0))
            
            self.draw(playerPos)

            pygame.display.update()

        pygame.quit()
    
    
    # render all objects that are on screen
    def draw(self, playerPos):
        # draw player
        pygame.draw.rect(self.window, (255, 0, 0), (playerPos[0], playerPos[1], 20, 20) )
        # draw obsticals and enemie

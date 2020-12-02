import pygame
import os
from game.myMap.map import Map
from game.player.player import Player
from game.obstacle.obstacleFactory import ObstacleFactory
from game.player.enemyFactory import EnemyFactory
from game.player.healthBar import HealthBar

class Game(Map, ObstacleFactory, EnemyFactory, Player):
    def __init__(self, root_path):
        self.run = False
        pygame.init()
        pygame.display.set_caption("Rootin Tootin Yeehaw Simulator")
        self.assets_path = os.path.join(root_path, 'assets')
        self.bg = pygame.image.load(os.path.join(self.assets_path, 'background.png'))
        self.bg = pygame.transform.scale(self.bg, (600, 600))
        self.window = pygame.display.set_mode((600, 600))
        self.obstacleFactory = ObstacleFactory()

    def runMenu(self):
        lightblue = (4, 163, 235)
        gold = (252, 186, 3)

        X = 600
        Y = 600

        display_surface = pygame.display.set_mode((X, Y))

        background = pygame.image.load("game/background.png")

        font = pygame.font.SysFont('rockwell', 32)
        text = font.render("Rootin\'", True, gold, lightblue)
        textRect = text.get_rect()
        textRect.center = (X // 2, 50)

        text1 = font.render("Tootin\'", True, gold, lightblue)
        textRect1 = text.get_rect()
        textRect1.center = (X // 2, 100)

        text2 = font.render("Yeehaw", True, gold, lightblue)
        textRect2 = text.get_rect()
        textRect2.center = (290, 150)

        text3 = font.render("Simulator", True, gold, lightblue)
        textRect3 = text.get_rect()
        textRect3.center = (280, 200)

        text4 = font.render("Play", True, lightblue, gold)
        textRect4 = text.get_rect()
        textRect4.center = (320, 400)

        text5 = font.render("Exit", True, gold, lightblue)
        textRect5 = text.get_rect()
        textRect5.center = (325, 500)

        selection = "play"

        while True:
            display_surface.blit(background, (0,0))
            display_surface.blit(text, textRect)
            display_surface.blit(text1, textRect1)
            display_surface.blit(text2, textRect2)
            display_surface.blit(text3, textRect3)
            display_surface.blit(text4, textRect4)
            display_surface.blit(text5, textRect5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        text5 = font.render("Exit", True, gold, lightblue)
                        text4 = font.render("Play", True, lightblue, gold)
                        selection = "play"
                    if event.key == pygame.K_DOWN:
                        text4 = font.render("Play", True, gold, lightblue)
                        text5 = font.render("Exit", True, lightblue, gold)
                        selection = "exit"
                    if event.key == pygame.K_RETURN:
                        if(selection == "play"):
                            self.runGame()
                        else:
                            pygame.quit()
                            quit()

                pygame.display.update()


    def runGame(self):
        # init game
        self.run = True
        diff = 2
        newObs = 0

        # create player
        self.player = Player(50, 485, os.path.join(self.assets_path, 'player'))

        #create healthBar
        self.healthBar = HealthBar((255,0,0), 200, 20, 200, 20, 100, self.window)

        # obstacle and enemy factory here

        while self.run:
            pygame.time.delay(50)

            for event in pygame.event.get():
                # check for quit
                if event.type == pygame.QUIT:
                    self.run = False

            # update player position
            self.player.update()

            # update obstacle pos
            if newObs <= 0:
                self.obstacles = self.obstacleFactory.createObstacles(self.assets_path)
                newObs = 3200
                if diff < 25:
                    diff += 3
            for obstacle in self.obstacles:
                obstacle.update(diff)

            # update enemy positions
            enemyPos = []
            newObs -= diff
            # update screen
            self.draw()


        pygame.quit()


    # render all objects that are on screen
    def draw(self):
        # draw background
        self.window.blit(self.bg, (0,0))

        # draw player
        self.player.draw(self.window)

        # draw obsticals and enemies
        for obstacle in self.obstacles:
            obstacle.draw(self.window)

        # health bar
        self.healthBar.draw(self.window)

        # update the display
        pygame.display.update()

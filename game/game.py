import pygame
import os
from game.obstacle.map import Map

from game.player.player import Player
from game.player.enemyFactory import EnemyFactory
from game.player.statusBar import StatusBar

from game.highScore.highScore import highScore
from game.highScore.fileAdapter import fileAdapter
from game.highScore.myFile import myFile

class Game:
    def __init__(self, root_path):
        self.run = False
        pygame.init()
        pygame.display.set_caption("Rootin Tootin Yeehaw Simulator")
        self.assets_path = os.path.join(root_path, 'assets')
        self.bg = pygame.image.load(os.path.join(self.assets_path, 'background.png'))
        self.bg = pygame.transform.scale(self.bg, (600, 600))
        self.window = pygame.display.set_mode((600, 600))
        self.map = Map(self.assets_path, 15)

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
        difficulty = 9
        score = 0

        # create player
        self.player = Player(50, 475, os.path.join(self.assets_path, 'player'))

        #create statusBar
        self.statusBar = StatusBar(self.window)

        while self.run:
            pygame.time.delay(50)

            for event in pygame.event.get():
                # check for quit
                if event.type == pygame.QUIT:
                    self.run = False

            # update player position
            self.player.update()
            newDiff = self.map.update(difficulty)
            if newDiff and difficulty < 24:
                difficulty += 3
            
            # check if player is colliding with obsticle
            damage = self.map.checkCollision(self.player.getHitbox())
            self.player.health -= damage
            if self.player.health <= 0:
                self.run = False
            score += 1
            # update screen
            self.statusBar.updateHealth(self.player.health)
            self.statusBar.updateScore(score)
            # draw to screen
            self.draw()

        pygame.quit()

    # This function will get you the current highscore, it takes in the currentScore
    # and adds it to the file
    def getHighScore(self, currentScore):
        scoreObject = highScore()
        # Using the adapter pattern here, because when our game gets big we'll need
        # to connect to a database instead of using a text file to log high scores
        myFileAdapter = fileAdapter()
        adaptee = myFile()

        hs = myFileAdapter.highScoreRequest(currentScore)
        return hs

    # render all objects that are on screen
    def draw(self):
        # draw background
        self.window.blit(self.bg, (0,0))

        # draw player
        self.player.draw(self.window)

        # draw map
        self.map.draw(self.window)

        # health bar
        self.statusBar.draw(self.window)

        # update the display
        pygame.display.update()

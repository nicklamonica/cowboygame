from game.game import Game
import os

def main():
    rootDir = os.path.dirname(__file__)
    g = Game(rootDir)
    
    #g.getHighScore(3)
    g.runMenu()
    #g.runGame()

if __name__ == "__main__":
    main()

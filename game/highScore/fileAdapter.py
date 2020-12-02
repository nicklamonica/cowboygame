from .myFile import myFile
from .highScore import highScore

class fileAdapter(highScore, myFile):
    def __init__(self):
        pass
    def highScoreRequest(self, currentScore):
        #add the current score to the file
        obj = myFile()
        obj.addScore(currentScore)
        #return the highScore
        return obj.getHighScore()
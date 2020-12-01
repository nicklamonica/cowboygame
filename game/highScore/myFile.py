import os
import sys
class myFile:
    def __init__(self):
        pass
    def getHighScore(self):
        fileObject = open("game/highScore/scores.txt", "r")
        #search for high score
        fileList = fileObject.readlines()
        newList = []
        for element in fileList:
            newList.append(element.strip("\n"))
        #print(newList)
        fileObject.close()
        #print(max(newList))
        return max(newList)

    def addScore(self, currentScore):
        fileObject = open("game/highScore/scores.txt", "a")
        fileObject.write(str(currentScore) + "\n")
        fileObject.close()

# I used the below code to test just this class
# if __name__ == "__main__":
#     testObj = myFile()
#     testObj.getHighScore())

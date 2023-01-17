import pygame

gameboardwidth = 12
gameboardheight = 20
activeBoardSpot = [[10 for y in range(gameboardheight)] for x in range(gameboardwidth)]
activeBoardColour = [[10 for y in range(gameboardheight)] for x in range(gameboardwidth)]

BLACK = (0, 0, 0)
pygame.init()
linesound = pygame.mixer.Sound("clearline.wav")

class Gameboard():
    def __init__(self, color, blockSize):
        self.boardColour = color
        self.multiplier = blockSize
        self.score = 0
        self.numline = 0
        self.templeveltracker = 0
        self.numpowerup = 0
        self.level = 1
        self.slowtimeon = False
        self.swapon = False
        for i in range(gameboardwidth):
            for j in range(gameboardheight):
                activeBoardSpot[i][j] = False  # initializes it to inactive
                activeBoardColour[i][j] = (0, 0, 0)  # initializes it to black

    def draw(self, screen):
        pygame.draw.rect(screen,self.boardColour, [0, 0, gameboardwidth*self.multiplier,gameboardheight*self.multiplier], 1)
        for i in range(gameboardwidth):
            for j in range(gameboardheight):
                if activeBoardSpot[i][j]:
                    pygame.draw.rect(screen, activeBoardColour[i][j], [i *self.multiplier, j * self.multiplier, self.multiplier - 1, self.multiplier - 1], 0)

    def checkLost(self):
        for i in range(gameboardwidth):
            if activeBoardSpot[i][0]:
                return True
        return False

    def isCompleteLine(self, rowNum):
        for i in range(gameboardwidth):
            if activeBoardSpot[i][rowNum] == False:
                return  False
        return True

    # need review
    def clearFullRow(self):
        for j in range(gameboardheight):
            if self.isCompleteLine(j):
                self.score += 100
                self.numline += 1
                self.templeveltracker += 1
                linesound.play()
                if self.templeveltracker == 3:
                    self.level += 1
                    self.numpowerup += 1
                    self.templeveltracker = 0
                for c in range(j, 1, -1):
                    for i in range(gameboardwidth):
                        activeBoardSpot[i][c] = activeBoardSpot[i][c - 1]
                        activeBoardColour[i][c] = activeBoardColour[i][c - 1]
                for r in range(gameboardwidth):
                    activeBoardSpot[r][0] = False
                    activeBoardColour[r][0] = BLACK
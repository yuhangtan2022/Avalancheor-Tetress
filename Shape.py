import pygame
import random
from Blocks import Blocks
from GameBoard import gameboardheight
from GameBoard import gameboardwidth
from GameBoard import activeBoardSpot
from GameBoard import activeBoardColour

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
orange = (255, 127, 0)
yellow = (255, 255, 0)
pink = (255, 0, 255)
turquoise = (0, 206, 209)

ZSHAPE = [[(gameboardwidth/2)-1, 0], [(gameboardwidth/2)-2, 0], [(gameboardwidth/2)-1, 1], [(gameboardwidth/2), 1]]
SSHAPE = [[(gameboardwidth/2)-1, 0], [(gameboardwidth/2), 0], [(gameboardwidth/2)-2, 1], [(gameboardwidth/2)-1, 1]]
LINESHAPE = [[(gameboardwidth/2)-1, 0], [(gameboardwidth/2)-2, 0], [(gameboardwidth/2), 0], [(gameboardwidth/2)+1, 0]]
SQUARESHAPE = [[(gameboardwidth/2)-1, 0], [(gameboardwidth/2), 0], [(gameboardwidth/2)-1, 1], [(gameboardwidth/2), 1]]
LSHAPE = [[(gameboardwidth/2)-1, 1], [(gameboardwidth/2)-1, 0], [(gameboardwidth/2)-1, 2], [(gameboardwidth/2), 2]]
MLSHAPE = [[(gameboardwidth/2), 1], [(gameboardwidth/2), 0], [(gameboardwidth/2), 2], [(gameboardwidth/2)-1, 2]]
TSHAPE = [[(gameboardwidth/2)-1, 1], [(gameboardwidth/2)-1, 0], [(gameboardwidth/2), 1], [(gameboardwidth/2)-2, 1]]
ALLSHAPES = [ZSHAPE, SSHAPE, LINESHAPE, SQUARESHAPE, LSHAPE, MLSHAPE, TSHAPE]
ALLCOLOURS = [green, red, blue, orange, yellow, pink, turquoise]


class Shape():
    def __init__(self, startingPositionY, startingPositionX, shape):
        self.numblocks = 4
        randomNum = random.randrange(7)
        self.shape = ALLSHAPES[randomNum]
        self.colours = ALLCOLOURS[randomNum]
        if shape is not None:
            while self.shape == shape.shape:
                randomNum = random.randrange(7)
                self.shape = ALLSHAPES[randomNum]
                self.colours = ALLCOLOURS[randomNum]
        self.active = True
        self.blocklist=[]
        for i in range(self.numblocks):
            self.blocklist.append(Blocks(self.colours,self.shape[i][0],self.shape[i][1] + startingPositionY))

    def  draw (self,screen):
        for i in range(self.numblocks):
            self.blocklist[i].draw(screen)

    def MoveLeft(Self):
        blocked = False
        for i in range(Self.numblocks):
             if Self.blocklist[i].gridxPos == 0 or activeBoardSpot[Self.blocklist[i].gridxPos - 1][Self.blocklist[i].gridyPos]:
                blocked = True
        if blocked == False :
            for i in range(Self.numblocks):
                Self.blocklist[i].gridxPos -= 1
    def MoveRight(Self):
        blocked = False
        for i in range(Self.numblocks):
            if Self.blocklist[i].gridxPos == gameboardwidth-1 or activeBoardSpot[Self.blocklist[i].gridxPos + 1][Self.blocklist[i].gridyPos]:
                blocked = True
        if blocked == False:
            for i in range(Self.numblocks):
                Self.blocklist[i].gridxPos += 1
    def MoveDown(self):
        blocked = False
        for i in range(4):
            if self.blocklist[i].gridyPos == gameboardheight-1 or activeBoardSpot[self.blocklist[i].gridxPos][self.blocklist[i].gridyPos + 1]:
                blocked = True
        if blocked == False:
            for i in range(4):
                self.blocklist[i].gridyPos += 1
    # need review
    def drop(self):
        while self.active:
            for i in range(4):
                if self.blocklist[i].gridyPos == gameboardheight - 1 or activeBoardSpot[self.blocklist[i].gridxPos][self.blocklist[i].gridyPos + 1]:
                    self.hitBottom()
            for i in range(4):
                if self.active:
                    self.blocklist[i].gridyPos += 1
    def rotateCW(Self):
        if Self.shape != SQUARESHAPE:
            newBlockX = [0, 0, 0, 0]
            newBlockY = [0, 0, 0, 0]
            canrotate = True
            for i in range(Self.numblocks):
                newBlockX[i] = -(Self.blocklist[i].gridyPos-Self.blocklist[0].gridyPos)+Self.blocklist[0].gridxPos
                newBlockY[i] =(Self.blocklist[i].gridxPos-Self.blocklist[0].gridxPos)+Self.blocklist[0].gridyPos
                if newBlockX[i] < 0 or newBlockX[i] >= gameboardwidth - 1:
                    canrotate = False
                elif newBlockY[i] < 0 or newBlockY[i] >= gameboardheight - 1:
                    canrotate = False
                elif activeBoardSpot[newBlockX[i]][newBlockY[i]]:
                    canrotate = False
            if canrotate:
                for i in range(Self.numblocks):
                    Self.blocklist[i].gridxPos = newBlockX[i]
                    Self.blocklist[i].gridyPos = newBlockY[i]

    def rotateCCW(Self):
        if Self.shape != SQUARESHAPE:
            newBlockX = [0, 0, 0, 0]
            newBlockY = [0, 0, 0, 0]
            canrotate = True
            for i in range(Self.numblocks):
                newBlockX[i] = (Self.blocklist[i].gridyPos-Self.blocklist[0].gridyPos)+Self.blocklist[0].gridxPos
                newBlockY[i] = -(Self.blocklist[i].gridxPos-Self.blocklist[0].gridxPos)+Self.blocklist[0].gridyPos
                if newBlockX[i] < 0 or newBlockX[i] >= gameboardwidth - 1:
                    canrotate = False
                elif newBlockY[i] < 0 or newBlockY[i] >= gameboardheight - 1:
                    canrotate = False
                elif activeBoardSpot[newBlockX[i]][newBlockY[i]]:
                    canrotate = False
            if canrotate:
                for i in range(Self.numblocks):
                    Self.blocklist[i].gridxPos = newBlockX[i]
                    Self.blocklist[i].gridyPos = newBlockY[i]

    def falling(self):
        for i in range(4):
            if self.blocklist[i].gridyPos == gameboardheight - 1 or activeBoardSpot[self.blocklist[i].gridxPos][self.blocklist[i].gridyPos+1]:
                self.hitBottom()
        for i in range(4):
            if self.active:
                self.blocklist[i].gridyPos += 1

    def hitBottom(self):
        for i in range(4):
            activeBoardSpot[self.blocklist[i].gridxPos][self.blocklist[i].gridyPos] = True
            activeBoardColour[self.blocklist[i].gridxPos][self.blocklist[i].gridyPos] = self.blocklist[i].colour
        self.active = False

    def drawnextshape(self,screen):
        for i in range(self.numblocks):
            pygame.draw.rect(screen, self.blocklist[i].colour, [self.blocklist[i].gridxPos * self.blocklist[i].size + 325, self.blocklist[i].gridyPos * self.blocklist[i].size + 150, self.blocklist[i].size - 1, self.blocklist[i].size - 1], 0)
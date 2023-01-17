import pygame
class Blocks():
    def __init__(self, colour, gridxPos, gridyPos):
        self.colour = colour
        self.gridxPos = int(gridxPos)
        self.gridyPos = int(gridyPos)
        self.size = 25

    def draw(self,screen):
        pygame.draw.rect(screen, self.colour, [self.gridxPos*self.size, self.gridyPos*self.size, self.size-1, self.size-1], 0)

# Importing the library
import pygame

color = (255,0,0)
White = (255,255,255)
Black = (0,0,0)
squreWidth = 50

class BoardPiece():
    def __init__(self, color, xCord, yCord):
        self.color = color
        self.xCord = xCord
        self.yCord = yCord
    
    def getColor(self):
        return self.color
    
    def getCordinates(self, xCord, yCord):
        return self.xCord, self.yCord

def determineColor(isWhite):
    if isWhite == True:
        return White
    else:
        return Black

def createBoard():
    isWhite = False
    for r in range(8):
        row = []
        isWhite = not isWhite
        for c in range(8):
            row.append(BoardPiece(determineColor(isWhite), r, c))
            isWhite = not isWhite
        Board.append(row)

def caculateRectangle(x,y):
    pass


Board = []
createBoard()

# Initializing Pygame
pygame.init()
  
# Initializing surface
surface = pygame.display.set_mode((400,400))


for row in Board:
    for sqaure in row:
        pygame.draw.rect(surface, color, pygame.Rect(0, 0, 30, 30))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
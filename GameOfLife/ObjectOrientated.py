from random import randint
import pygame


class Cell(object):
    def __init__(self, x, y):
        self.x, self.y = x + blockSize / 2, y + blockSize / 2

        self.alive = False

        self.neighbours, self.aliveNeighbourCount = [], 0

        self.colorVal = 50

    def updateSelf(self, red, green, blue):
        pygame.draw.circle(scr, (red, green, blue), (self.x, self.y), blockSize / 2)

    def getInitNeighbours(self):
        for cell in cells:
            if (
                (cell.x == self.x + blockSize and cell.y == self.y)
                or (cell.x == self.x - blockSize and cell.y == self.y)
                or (cell.x == self.x and cell.y == self.y + blockSize)
                or (cell.x == self.x and cell.y == self.y - blockSize)
                or (cell.x == self.x + blockSize and cell.y == self.y + blockSize)
                or (cell.x == self.x - blockSize and cell.y == self.y - blockSize)
                or (cell.x == self.x + blockSize and cell.y == self.y - blockSize)
                or (cell.x == self.x - blockSize and cell.y == self.y + blockSize)
            ):
                self.neighbours.append(cell)

    def getAliveNeighbours(self):
        deadCount = 0
        for cell in self.neighbours:
            if not cell.alive:
                deadCount += 1
        self.aliveNeighbourCount = len(self.neighbours) - deadCount

    def nextGeneration(self):
        if self.aliveNeighbourCount == 3 and not self.alive:
            self.alive = True
        elif self.aliveNeighbourCount < 2 or self.aliveNeighbourCount > 3:
            self.alive = False
        elif (
            self.aliveNeighbourCount == 3 or self.aliveNeighbourCount == 2
        ) and self.alive:
            self.alive = True

    def update(self):
        change = 5
        if self.alive:
            if self.colorVal <= 255 - change:
                self.colorVal += change
            self.updateSelf(self.colorVal, 0, 0)
        else:
            self.colorVal = 50
            self.updateSelf(0, 0, 0)


pygame.init()

clock = pygame.time.Clock()

black = (0, 0, 0)
blue = (0, 0, 255)

screenWidth = 500
screenHeight = 500
scr = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("The Game Of Life")
scr.fill(black)

blockSize = 10

done = False

cells = []


createGrid = lambda: (
    [
        cells.append(Cell(row, col))
        for row in range(0, screenWidth, blockSize)
        for col in range(0, screenHeight, blockSize)
    ]
)


def noLife():
    for cell in cells:
        if cell.alive:
            return False
    return True


if __name__ == "__main__":
    createGrid()
    [cell.getInitNeighbours() for cell in cells]

    for cell in cells:
        if randint(1, 2) == 1:
            cell.alive = True

    [cell.update() for cell in cells]

    pygame.display.update()
    clock.tick(1)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        [cell.getAliveNeighbours() for cell in cells]
        [cell.nextGeneration() for cell in cells]
        [cell.update() for cell in cells]
        clock.tick(8)
        pygame.display.update()

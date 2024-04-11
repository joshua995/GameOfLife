'''
Joshua Liu
Last updated: October 6, 2022.
Version: Use the 
    left mouse button to set a cell, 
    right mouse button to clear a cell, 
    middle mouse button to start the simulation
'''

from random import randint
import pygame

pygame.init()

clock = pygame.time.Clock()

background, cellColor = (0, 0, 0), (255, 0, 0)

screenWidth, screenHeight = 500, 500
scr = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
pygame.display.set_caption("The Game Of Life")
scr.fill(background)

cellSize, done, cellData = 10, False, []

reviveOrStay = 3
minStayOrDie = 2


def createGrid():
    for row in range(0, screenWidth, cellSize):
        for col in range(0, screenHeight, cellSize):
            cellData.append([])
            cellData[len(cellData) - 1].append(row + cellSize / 2)  # x pos
            cellData[len(cellData) - 1].append(col + cellSize / 2)  # y pos
            cellData[len(cellData) - 1].append(False)  # is alive
            cellData[len(cellData) - 1].append([])  # neighbour indexes
            cellData[len(cellData) - 1].append(0)  # alive neighbour count
            '''
            num = randint(1, 2)
            if num == 1:
                cellData[len(cellData) - 1][2] = True
            '''


def getNeighbours(cell_data):
    [[cell[3].append(cInd) for cInd, c in enumerate(cell_data) if (cell[0] == c[0] + cellSize and cell[1] == c[1]) or
      (cell[0] == c[0] - cellSize and cell[1] == c[1]) or (cell[0] == c[0] and cell[1] == c[1] + cellSize) or
      (cell[0] == c[0] and cell[1] == c[1] - cellSize) or (cell[0] == c[0] + cellSize and cell[1] == c[1] + cellSize)
      or (cell[0] == c[0] - cellSize and cell[1] == c[1] - cellSize) or
      (cell[0] == c[0] - cellSize and cell[1] == c[1] + cellSize) or
      (cell[0] == c[0] + cellSize and cell[1] == c[1] - cellSize)] for cell in cell_data]


def getAliveNeighbours(cell_data):
    for cell in cell_data:
        deadCount = 0
        for neighbour in cell[3]:
            if not cell_data[neighbour][2]:
                deadCount += 1
        cell[4] = len(cell[3]) - deadCount


def nextGeneration():
    for i, cell in enumerate(cellData):
        if cell[4] == reviveOrStay and not cell[2]:
            cell[2] = True
        elif cell[4] < minStayOrDie or cell[4] > reviveOrStay:
            cell[2] = False
        elif (cell[4] == reviveOrStay or cell[4] == minStayOrDie) and cell[2]:
            cell[2] = True
        if cell[2]:
            pygame.draw.circle(scr, cellColor, (cell[0], cell[1]), cellSize/2)
        elif not cell[2]:
            pygame.draw.circle(scr, background, (cell[0], cell[1]), cellSize/2)


loading = True

if __name__ == "__main__":
    createGrid()
    getNeighbours(cellData)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        if pygame.mouse.get_pressed()[0]:
            for cell in cellData:
                if cell[2]:
                    pygame.draw.circle(scr, cellColor, (cell[0], cell[1]), cellSize/2)
                if pygame.mouse.get_pos()[0] - cellSize/2 < cell[0] <= pygame.mouse.get_pos()[0] + cellSize/2 and \
                        pygame.mouse.get_pos()[1] - cellSize/2 < cell[1] <= pygame.mouse.get_pos()[1] + cellSize/2:
                    pygame.draw.circle(scr, cellColor, (cell[0], cell[1]), cellSize/2)
                    cell[2] = True
        if pygame.mouse.get_pressed()[2]:
            for cell in cellData:
                if pygame.mouse.get_pos()[0] - cellSize/2 < cell[0] <= pygame.mouse.get_pos()[0] + cellSize/2 and \
                        pygame.mouse.get_pos()[1] - cellSize/2 < cell[1] <= pygame.mouse.get_pos()[1] + cellSize/2:
                    pygame.draw.circle(scr, background, (cell[0], cell[1]), cellSize/2)
                    cell[2] = False
        elif pygame.mouse.get_pressed()[1]:
            loading = False
        pygame.display.update()
        if not loading:
            clock.tick(5)
            pygame.display.update()
            getAliveNeighbours(cellData)
            nextGeneration()

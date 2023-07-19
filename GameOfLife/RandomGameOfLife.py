"""
Joshua Liu
Last updated: October 6, 2022.
Version: it has 3 random simulations running simultaneously, overlap shows different colors
"""

from random import randint
import pygame

pygame.init()

clock = pygame.time.Clock()

background, cellColor, cellColor1, cellColor2 = (
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
)
cellColor01, cellColor02, cellColor12, cellColorAll = (
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (255, 255, 255),
)

screenWidth, screenHeight = 700, 700
scr = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
pygame.display.set_caption("The Game Of Life")
scr.fill(background)

blockSize, done, cellData, cellData1, cellData2 = 20, False, [], [], []
generations, listOfStates = 0, []

reviveOrStay = 3
minStayOrDie = 2


def instantiateCellData(row, col, cell_data):
    cell_data.append([])
    cell_data[len(cell_data) - 1].append(row + blockSize / 2)  # x pos
    cell_data[len(cell_data) - 1].append(col + blockSize / 2)  # y pos
    cell_data[len(cell_data) - 1].append(False)  # is alive
    cell_data[len(cell_data) - 1].append([])  # neighbour indexes
    cell_data[len(cell_data) - 1].append(0)  # alive neighbour count


def createGrid():
    for row in range(0, screenWidth, blockSize):
        for col in range(0, screenHeight, blockSize):
            instantiateCellData(row, col, cellData)
            instantiateCellData(row, col, cellData1)
            instantiateCellData(row, col, cellData2)
            num = randint(1, 3)
            if num == 1:
                cellData[len(cellData) - 1][2] = True
            elif num == 2:
                cellData1[len(cellData1) - 1][2] = True
            elif num == 3:
                cellData2[len(cellData2) - 1][2] = True


def getNeighbours(cell_data):
    [
        [
            cell[3].append(cInd)
            for cInd, c in enumerate(cell_data)
            if (cell[0] == c[0] + blockSize and cell[1] == c[1])
            or (cell[0] == c[0] - blockSize and cell[1] == c[1])
            or (cell[0] == c[0] and cell[1] == c[1] + blockSize)
            or (cell[0] == c[0] and cell[1] == c[1] - blockSize)
            or (cell[0] == c[0] + blockSize and cell[1] == c[1] + blockSize)
            or (cell[0] == c[0] - blockSize and cell[1] == c[1] - blockSize)
            or (cell[0] == c[0] - blockSize and cell[1] == c[1] + blockSize)
            or (cell[0] == c[0] + blockSize and cell[1] == c[1] - blockSize)
        ]
        for cell in cell_data
    ]


def getAliveNeighbours(cell_data):
    for cell in cell_data:
        deadCount = 0
        for neighbour in cell[3]:
            if not cell_data[neighbour][2]:
                deadCount += 1
        cell[4] = len(cell[3]) - deadCount


def nextGeneration():
    if generations % 2 == 0:
        listOfStates.append("")
    for i, cell in enumerate(cellData):
        if cell[4] == reviveOrStay and not cell[2]:
            cell[2] = True
        elif cell[4] < minStayOrDie or cell[4] > reviveOrStay:
            cell[2] = False
        elif (cell[4] == reviveOrStay or cell[4] == minStayOrDie) and cell[2]:
            cell[2] = True
        if cell[2]:
            pygame.draw.circle(scr, cellColor, (cell[0], cell[1]), blockSize / 2)
        elif not cell[2]:
            pygame.draw.circle(scr, background, (cell[0], cell[1]), blockSize / 2)
        if generations % 2 == 0:
            listOfStates[len(listOfStates) - 1] += str(cell[2])
    for i, cell in enumerate(cellData1):
        if cell[4] == reviveOrStay and not cell[2]:
            cell[2] = True
        elif cell[4] < minStayOrDie or cell[4] > reviveOrStay:
            cell[2] = False
        elif (cell[4] == reviveOrStay or cell[4] == minStayOrDie) and cell[2]:
            cell[2] = True
        if cell[2] and cellData[i][2]:
            pygame.draw.circle(scr, cellColor01, (cell[0], cell[1]), blockSize / 2)
        elif cell[2]:
            pygame.draw.circle(scr, cellColor1, (cell[0], cell[1]), blockSize / 2)
        if generations % 2 == 0:
            listOfStates[len(listOfStates) - 1] += str(cell[2])
    for i, cell in enumerate(cellData2):
        if cell[4] == reviveOrStay and not cell[2]:
            cell[2] = True
        elif cell[4] < minStayOrDie or cell[4] > reviveOrStay:
            cell[2] = False
        elif (cell[4] == reviveOrStay or cell[4] == minStayOrDie) and cell[2]:
            cell[2] = True
        if cell[2] and cellData[i][2] and cellData1[i][2]:
            pygame.draw.circle(scr, cellColorAll, (cell[0], cell[1]), blockSize / 2)
        elif cell[2] and cellData[i][2]:
            pygame.draw.circle(scr, cellColor02, (cell[0], cell[1]), blockSize / 2)
        elif cell[2] and cellData1[i][2]:
            pygame.draw.circle(scr, cellColor12, (cell[0], cell[1]), blockSize / 2)
        elif cell[2]:
            pygame.draw.circle(scr, cellColor2, (cell[0], cell[1]), blockSize / 2)
        if generations % 2 == 0:
            listOfStates[len(listOfStates) - 1] += str(cell[2])
    if len(listOfStates) > 3:
        listOfStates.pop(0)


def reset():
    listOfStates.clear()
    for i, cell in enumerate(cellData):
        num = randint(1, 3)
        if num == 1:
            cell[2], cellData1[i][2], cellData2[i][2] = True, False, False
        elif num == 2:
            cell[2], cellData1[i][2], cellData2[i][2] = False, True, False
        elif num == 3:
            cell[2], cellData1[i][2], cellData2[i][2] = False, False, True
    return 0


if __name__ == "__main__":
    createGrid()
    getNeighbours(cellData), getNeighbours(cellData1), getNeighbours(cellData2)
    generations = reset()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        clock.tick(5)
        pygame.display.update()
        getAliveNeighbours(cellData), getAliveNeighbours(cellData1), getAliveNeighbours(cellData2)
        nextGeneration()
        generations += 1
        if (len(set(listOfStates)) <= 2 and len(listOfStates) == 3) or generations > 1000:
            generations = reset()

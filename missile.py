import pygame
from graphics import Graphics


class Missile:
    __missileCount = 0
    __isActive = False
    __launchPosition = []
    __currentPosition = []
    __succeeded = False
    __missileImage = pygame.image.load("resources/images/bullet.png")
    __graphics = None
    __missileId = __missileCount

    def __init__(self, launchposition):
        self.__isActive = True
        self.__launchPosition = launchposition
        self.__currentPosition = launchposition
        self.__graphics = Graphics.getInstance()
        Missile.__missileCount += 1
        self.__missileId = Missile.__missileCount
        print(
            f"Missile {self.__missileId}/{Missile.__missileCount} launched from [{self.__currentPosition[0]}, {self.__currentPosition[1]}]")

    def displayData(self):
        print("The current location is " + str(self.__currentPosition[0]) + ", " + str(self.__currentPosition[1]))

    def displayMissile(self):
        self.__graphics.screen.blit(self.__missileImage, self.__currentPosition)
        result = self.moveMissile()
        if result != 0:
            self.__isActive = False

    def moveMissile(self):
        self.__currentPosition[1] -= 10

        # 0 - Missile is inside the canvas
        # 1 - Missile is outside the canvas
        # 2 - Missile has killed the enemy

        if self.__currentPosition[1] > 0:
            # self.isMissileInsideCanvas()
            return 0
        else:
            return 1

    def isMissileInsideCanvas(self):
        print(str(self.__currentPosition[0]) + "," + str(self.__currentPosition[1]))

    def isActive(self):
        return self.__isActive

    def setActive(self, isActive):
        self.__isActive = isActive

    def getMissileId(self):
        return self.__missileId

    def destroy(self, succeeded):
        self.__isActive = False
        self.__succeeded = succeeded

    def getRect(self):
        rect = pygame.Rect(self.__missileImage.get_rect())
        rect.left = self.__currentPosition[0]
        rect.top = self.__currentPosition[1]
        # rect[0] = self.__currentPosition[0]
        # rect[1] = self.__currentPosition[1]
        # rect[2] = self.__currentPosition[0] + rect.width
        # rect[3] = self.__currentPosition[1] + rect.height
        # rect[0] = left
        # rect[1] = top
        # rect[2] = width
        # rect[3] = height


        # print(f" Missile coordinates: {rect.top}, {rect.left}, {rect.bottom}, {rect.right}, {rect.width}, {rect.height}, {rect[0]}, {rect[1]}, {rect[2]}, {rect[3]}")
        return rect
        # pygame.Rect(self.__missileImage.get_rect())

import pygame
from graphics import Graphics


class Enemy:
    enemyCount = 0
    _isActive = False
    __launchPosition = []
    __currentPosition = []
    __succeeded = False
    __enemyImage = pygame.image.load("resources/images/enemy.png")
    __graphics = None
    __enemyId = enemyCount

    def __init__(self, launchposition):
        self._isActive = True
        self.__launchPosition = launchposition
        self.__currentPosition = launchposition
        self.__graphics = Graphics.getInstance()
        # self.displayData()
        Enemy.enemyCount += 1
        self.__enemyId = Enemy.enemyCount
        # self.__graphics.screen.blit(self.__enemyImage, self.__launchPosition)

        # print("Enemy " + str(self.__enemyId) + "/" + str(Enemy.enemyCount) + " Launched from ")
        print(f"Enemy {self.__enemyId}/{Enemy.enemyCount} launched from [{self.__currentPosition[0]}, {self.__currentPosition[1]}]")

    def displayData(self):
        print("The current location is " + str(self.__currentPosition[0]) + ", " + str(self.__currentPosition[1]))

    def displayEnemy(self):
        self.__graphics.screen.blit(self.__enemyImage, self.__currentPosition)
        result = self.moveEnemy()
        if result != 0:
            self._isActive = False

    def moveEnemy(self):
        self.__currentPosition[1] += 5

        # 0 - Missile is inside the canvas
        # 1 - Missile is outside the canvas
        # 2 - Missile has killed the enemy

        if self.__currentPosition[1] <= 550:
            # self.isEnemyInsideCanvas()
            return 0
        else:
            return 1

    def isEnemyInsideCanvas(self):
        print(str(self.__currentPosition[0]) + "," + str(self.__currentPosition[1]))

    def isActive(self):
        return self._isActive

    def setActive(self, isActive):
        self._isActive = isActive

    def getEnemyId(self):
        return self.__enemyId

    def destroy(self, succeeded):
        self._isActive = False
        self.__succeeded = succeeded

    def getRect(self):
        rect = pygame.Rect(self.__enemyImage.get_rect())
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

        # print(f" Enemy coordinates: {rect[0]}, {rect[1]}, {rect[2]}, {rect[3]}")
        return rect

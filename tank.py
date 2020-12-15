from graphics import Graphics
import pygame


class Tank:
    __instance = None
    __tankImage = pygame.image.load("resources/images/tank.png")
    # __tankImage = pygame.image.load("resources/images/boom01.jpg")
    __currentPosition = [290, 400]
    __graphics = None

    @staticmethod
    def getInstance():
        if Tank.__instance is None:
            __instance = Tank()
        return Tank.__instance

    def __init__(self):
        if Tank.__instance is not None:
            raise Exception("This class is a singleton")
        else:
            self.initialize()
            Tank.__instance = self

    def initialize(self):
        self.__graphics = Graphics.getInstance();
        # self.__currentPosition = [int(self.__graphics.getFieldSize()[0]/2), self.__graphics.getFieldSize()[1]]
        self.__currentPosition = [int(self.__graphics.getFieldSize()[0]/2) - int(pygame.Rect(self.__tankImage.get_rect()).width/2),
                               self.__graphics.getFieldSize()[1] - pygame.Rect(self.__tankImage.get_rect()).height]
        self.__graphics.screen.blit(self.__tankImage, self.__currentPosition)
        print("Tank Initialized")

    def setTankPosition(self, tankPosition):
        self.__currentPosition = tankPosition

    def getTankPosition(self):
        return self.__currentPosition

    def displayTank(self):
        self.__graphics.screen.blit(self.__tankImage, self.__currentPosition)

    def getRect(self):
        rect = pygame.Rect(self.__tankImage.get_rect())
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



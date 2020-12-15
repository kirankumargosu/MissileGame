import pygame
from pygame.locals import *


class Graphics:
    __instance = None
    __width = 0
    __height = 0
    __backgroundImage = pygame.image.load("resources/images/warbackground.png")
    # __canvasDimension = [640, 480]
    __canvasDimension = [1000, 566]
    screen = pygame.display.set_mode((__width, __height))

    @staticmethod
    def getInstance():
        if Graphics.__instance is None:
            __instance = Graphics()
        return Graphics.__instance

    def __init__(self):
        if Graphics.__instance is not None:
            raise Exception("This class is a singleton")
        else:
            self.initialize()
            Graphics.__instance = self

    def initialize(self):
        self.__width = self.__canvasDimension[0]
        self.__height = self.__canvasDimension[1]
        self.screen = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption('Keep Calm and Fight!')
        # self.screen.fill(0)
        # for x in range(int(self.__width / self.__backgroundImage.get_width()) + 1):
        #    for y in range(int(self.__height / self.__backgroundImage.get_height()) + 1):
        #        self.screen.blit(self.__backgroundImage, (x * 100, y * 100))
        self.makeField()
        self.displayFlip()
        print("Graphics Initialized")

    def makeField(self):
        self.screen.fill(0)
        # for x in range(int(self.__width / self.__backgroundImage.get_width()) + 1):
        #    for y in range(int(self.__height / self.__backgroundImage.get_height()) + 1):
        #        self.screen.blit(self.__backgroundImage, (x * 100, y * 100))
        self.screen.blit(self.__backgroundImage, (0, 0))

    def displayFlip(self):
        pygame.display.flip()

    def getFieldSize(self):
        return self.__canvasDimension


'''
    def initgraphics(self):

    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))

    missileImage = pygame.image.load("resources/images/missile.png")
    backgroundImage = pygame.image.load("resources/images/grass.png")

    screen.fill(0)
    # 6 - draw the player on the screen at X:100, Y:100
    for x in range(int(width / backgroundImage.get_width()) + 1):
        for y in range(int(height / backgroundImage.get_height()) + 1):
            screen.blit(backgroundImage, (x * 100, y * 100))

    pygame.display.flip()
'''

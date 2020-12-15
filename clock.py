from graphics import Graphics
import pygame


class Clock:
    __instance = None
    __clockImagesSource = ["resources/images/00.png",
                           "resources/images/01.png",
                           "resources/images/02.png",
                           "resources/images/03.png",
                           "resources/images/04.png",
                           "resources/images/05.png",
                           "resources/images/06.png",
                           "resources/images/07.png",
                           "resources/images/08.png",
                           "resources/images/09.png"
                           ]
    __images = []
    __graphics = None
    __iteration = 0

    @staticmethod
    def getInstance():
        if Clock.__instance is None:
            __instance = Clock()
        return Clock.__instance

    def __init__(self):
        if Clock.__instance is not None:
            raise Exception("This class is a singleton")
        else:
            self.initialize()
            Clock.__instance = self
            self.__graphics = Graphics.getInstance()
            for clockImage in self.__clockImagesSource:
                self.__images.append(pygame.image.load(clockImage))

    def initialize(self):
        self.__graphics = Graphics.getInstance();
        print("Clock Initialized")

    def displayClock(self, timeLeft):
        tens = int(timeLeft/10)
        seconds = timeLeft % 10
        tensImage = self.__images[tens]
        secondsImage = self.__images[seconds]
        if Clock.__iteration == 0 and timeLeft <= 5:
            tensImage = pygame.transform.rotozoom(tensImage, -10, 0.5)
            secondsImage = pygame.transform.rotozoom(secondsImage, 10, 0.5)
        if Clock.__iteration == 1 and timeLeft <= 5:
            tensImage = pygame.transform.rotozoom(tensImage, -5, 0.7)
            secondsImage = pygame.transform.rotozoom(secondsImage, 5, 0.7)
        if Clock.__iteration == 2 and timeLeft <= 5:
            tensImage = pygame.transform.rotozoom(tensImage, 0, 0.6)
            secondsImage = pygame.transform.rotozoom(secondsImage, 0, 0.6)
        # playerrot = pygame.transform.rotate(player, 360 - angle * 57.29)
        self.__graphics.screen.blit(secondsImage, (self.__graphics.getFieldSize()[0] - (10 + pygame.Rect(secondsImage.get_rect()).width), 10))
        self.__graphics.screen.blit(tensImage, (self.__graphics.getFieldSize()[0] - (10 + pygame.Rect(secondsImage.get_rect()).width + 5 + pygame.Rect(tensImage.get_rect()).width), 10))
        Clock.__iteration = (Clock.__iteration + 1) % 3

    # def getRect(self):
    #     rect = pygame.Rect(self.__tankImage.get_rect())
    #     rect.left = self.__currentPosition[0]
    #     rect.top = self.__currentPosition[1]
    #     # rect[0] = self.__currentPosition[0]
    #     # rect[1] = self.__currentPosition[1]
    #     # rect[2] = self.__currentPosition[0] + rect.width
    #     # rect[3] = self.__currentPosition[1] + rect.height
    #     # rect[0] = left
    #     # rect[1] = top
    #     # rect[2] = width
    #     # rect[3] = height
    #
    #     # print(f" Enemy coordinates: {rect[0]}, {rect[1]}, {rect[2]}, {rect[3]}")
    #     return rect
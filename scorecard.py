from graphics import Graphics
import pygame


class ScoreCard:
    __instance = None
    __graphics = None
    __lifeImage = pygame.image.load("resources/images/life.png")
    __maxLifeCount = 3
    __remainingLifeCount = 3

    @staticmethod
    def getInstance():
        if ScoreCard.__instance is None:
            __instance = ScoreCard()
        return ScoreCard.__instance

    def __init__(self):
        if ScoreCard.__instance is not None:
            raise Exception("This class is a singleton")
        else:
            ScoreCard.__instance = self
            self.__graphics = Graphics.getInstance()
            self.__remainingLifeCount = self.__maxLifeCount
            print("ScoreCard Initialized")

    def updateScoreCard(self, hit, miss):
        self.displayLives()

    def loseLife(self):
        self.__remainingLifeCount -= 1

    def getExistingLives(self):
        return self.__remainingLifeCount

    def displayLives(self):
        for i in range(self.__remainingLifeCount):
            self.__graphics.screen.blit(ScoreCard.__lifeImage, (30 * (i + 1), 10))

from graphics import Graphics
import pygame


class CollisionController:
    __instance = None
    __collisions = []
    __collisionImagesSource = ["resources/images/collision3.png",
                               "resources/images/collision4.png",
                               "resources/images/collision3.png",
                               "resources/images/collision2.png",
                               "resources/images/collision1.png",
                               "resources/images/collision.5.png"
                               ]
    __images = []
    __maxIteration = 6
    __graphics = None

    @staticmethod
    def getInstance():
        if CollisionController.__instance is None:
            __instance = CollisionController()
        return CollisionController.__instance

    def __init__(self):
        if CollisionController.__instance is not None:
            raise Exception("This class is a singleton")
        else:
            CollisionController.__instance = self
            self.__graphics = Graphics.getInstance()
            for collisionImage in self.__collisionImagesSource:
                self.__images.append(pygame.image.load(collisionImage))
            print("CollisionController Initialized")

    def displayCollision(self):
        self.removeExpiredCollisions()
        for collision in self.__collisions:
            collisionPoint = collision.getCollisionPoint()
            # print(collision.getCollisionIteration())
            # print(f"{pygame.Rect(self.__images[collision.getCollisionIteration()].get_rect())}")
            imageDisplayPoint = (
                collisionPoint[0] - int(pygame.Rect(self.__images[collision.getCollisionIteration() - 1].get_rect()).width / 2),
                collisionPoint[1] - int(pygame.Rect(self.__images[collision.getCollisionIteration() - 1].get_rect()).height / 2))
            print(f"CollisionController - Displaying collision ({collisionPoint[0]}, {collisionPoint[1]}) image for {collision.getCollisionIteration()} with dimensions ({int(pygame.Rect(self.__images[collision.getCollisionIteration() - 1].get_rect()).width / 2), int(pygame.Rect(self.__images[collision.getCollisionIteration() - 1].get_rect()).height / 2)}) at : {imageDisplayPoint[0]}, {imageDisplayPoint[1]}")
            self.__graphics.screen.blit(self.__images[collision.getCollisionIteration() - 1], imageDisplayPoint)
            collision.incrementCollisionIteration()

    def removeExpiredCollisions(self):
        for collision in self.__collisions:
            print(f"removeExpiredCollisions: Current Iteration - {collision.getCollisionIteration()}, {CollisionController.__maxIteration}, {CollisionController.__maxIteration}")
            if collision.getCollisionIteration() > CollisionController.__maxIteration:
                self.__collisions.remove(collision)

    def addCollisions(self, collisions):
        self.__collisions.extend(collisions)


class Collision:
    __collisionPoint = []
    __collisionIteration = 1

    def getCollisionPoint(self):
        return self.__collisionPoint

    def getCollisionIteration(self):
        return self.__collisionIteration

    def incrementCollisionIteration(self):
        self.__collisionIteration += 1

    def setCollisionPoint(self, collisionPoint):
        self.__collisionPoint = collisionPoint
        self.__collisionIteration = 1



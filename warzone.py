import pygame
from graphics import Graphics
from missile import Missile
from enemy import Enemy
from collision import Collision
from scorecard import ScoreCard
from tank import Tank


class WarZoneController:
    __instance = None
    __missiles = []
    __enemies = []
    __graphics = None
    __collisionPoints = []
    __collisions = []
    __scoreCard = None
    __tank = None

    @staticmethod
    def getInstance():
        if WarZoneController.__instance is None:
            __instance = WarZoneController()
        return WarZoneController.__instance

    def __init__(self):
        if WarZoneController.__instance is not None:
            raise Exception("This class is a singleton")
        else:
            WarZoneController.__instance = self
            self.__graphics = Graphics.getInstance()
            self.__scoreCard = ScoreCard.getInstance()
            self.__tank = Tank.getInstance()
            print("WarZoneController Initialized")

    def addMissile(self, launchPosition):
        missile = Missile(launchPosition)
        self.__missiles.append(missile)

    # def destroyMissile(self, missile):
    #    self.__missiles.remove(missile)

    def addEnemy(self, launchPosition):
        enemy = Enemy(launchPosition)
        self.__enemies.append(enemy)

    def displayWarZone(self):
        self.checkForCollision()
        self.removeInActiveMissiles()
        self.removeInactiveEnemies()
        self.displayMissiles()
        self.displayEnemies()
        return self.__collisions

    def checkForCollision(self):
        self.__collisionPoints.clear()
        self.__collisions.clear()

        # for enemy in self.__enemies:
        #    if enemy.getRect().colliderect(self.__tank.getRect()):
        #        print(f"Enemy {enemy.getEnemyId()} brought your tank down")
        #        enemy.setActive(False)
        #        self.__scoreCard.loseLife()

        for missile in self.__missiles:
            if missile.getRect().top <= 5:
                missile.setActive(False)
                print(f"Missile {missile.getMissileId()} missed")

        for enemy in self.__enemies:
            if enemy.getRect().bottom >= (self.__graphics.getFieldSize()[1] - 5):
                enemy.setActive(False)
                print(f"Enemy {enemy.getEnemyId()} attached your fort")
                self.__scoreCard.loseLife()

        for missile in self.__missiles:
            if missile.isActive():
                for enemy in self.__enemies:
                    if enemy.isActive():
                        if missile.getRect().colliderect(enemy.getRect()):
                            # print(f"Missile {missile.getMissileId()} at {missile.getRect()} collides with Enemy "
                            #      f"{enemy.getEnemyId()} at {enemy.getRect()}")
                            # print(missile.getRect())
                            # print(enemy.getRect())
                            missile.setActive(False)
                            enemy.setActive(False)
                            # print("Collision")
                            # collisionPosition = (missile.getRect()[0], missile.getRect()[1])
                            collisionPoint = ((int(enemy.getRect().left + missile.getRect().left) / 2),
                                              (int(enemy.getRect().bottom + missile.getRect().top) / 2))
                            self.__missiles.remove(missile)
                            self.__enemies.remove(enemy)
                            collision = Collision()
                            collision.setCollisionPoint(collisionPoint)
                            self.__collisionPoints.append(collisionPoint)
                            self.__collisions.append(collision)
                            # Collision.createCollisionAnimation(collisionPosition)

                # missileRects.append(missile.getRect())

        # for enemy in self.__enemies:
        #    if enemy.isActive():
        #        enemyRects.append(enemy.getRect())

        # for missileRect in missileRects:
        #    for enemyRect in enemyRects:
        #        if missileRect.colliderect(enemyRect):
        #            print ("Collision")

    def removeInActiveMissiles(self):
        for missile in self.__missiles:
            if not missile.isActive():
                self.__missiles.remove(missile)

    def removeInactiveEnemies(self):
        for enemy in self.__enemies:
            if not enemy.isActive():
                self.__enemies.remove(enemy)

    def displayMissiles(self):
        for missile in self.__missiles:
            missile.displayMissile()

    def displayEnemies(self):

        for enemy in self.__enemies:
            enemy.displayEnemy()


class WarZone:
    __count = 0
    __isActive = False
    __launchPosition = []
    __currentPosition = []
    __succeeded = False
    __Image = ""
    __graphics = None
    __itemId = __count

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
        WarZone.__item
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
        self.__currentPosition[1] -= 5

        # 0 - Missile is inside the canvas
        # 1 - Missile is outside the canvas
        # 2 - Missile has killed the enemy

        if self.__currentPosition[1] > 5:
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
        rect.topleft = [self.__currentPosition[0], self.__currentPosition[1]]
        rect.bottomright = [self.__currentPosition[0] + rect.width, self.__currentPosition[1] + rect.height]
        print(f" Missile coordinates: {rect[0]}, {rect[1]}, {rect[2]}, {rect[3]}")
        return rect
        # pygame.Rect(self.__missileImage.get_rect())

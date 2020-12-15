# 1 - Import library
import pygame
from pygame.locals import *
from tank import Tank
from warzone import WarZoneController
import gc
from datetime import datetime
from graphics import Graphics
from collision import CollisionController
from clock import Clock
from scorecard import ScoreCard

keys = [False, False]
missiles = []
graphics = Graphics.getInstance()
tank = Tank.getInstance()
warZoneController = WarZoneController.getInstance()
scoreCard = ScoreCard.getInstance()
collisionController = CollisionController.getInstance()
clock = Clock.getInstance()
exitCode = 0
running = 1
startTime = datetime.now()
oldTime = startTime

enemyInterval = 2  # 5 seconds interval for enemy
gameDuration = 45  # 30 seconds game
while running:
    gc.collect()
    graphics.makeField()
    tank.displayTank()
    tankPosition = tank.getTankPosition()

    for event in pygame.event.get():

        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                keys[0] = True
            elif event.key == K_RIGHT:
                keys[1] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[0] = False
            elif event.key == pygame.K_RIGHT:
                keys[1] = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            missileLaunchPosition = [0, 0]
            missileLaunchPosition[0] = tankPosition[0] + 30
            missileLaunchPosition[1] = tankPosition[1] - 45
            warZoneController.addMissile(missileLaunchPosition)

    timeNow = datetime.now()
    duration = timeNow - oldTime
    if duration.seconds >= enemyInterval:
        oldTime = timeNow
        enemyLaunchPosition = [0, 0]
        enemyLaunchPosition[0] = (timeNow.microsecond % (graphics.getFieldSize()[0] - 50))
        enemyLaunchPosition[1] = 0
        warZoneController.addEnemy(enemyLaunchPosition)

    clock.displayClock(gameDuration - (timeNow - startTime).seconds)
    # collisionController.addCollisionPoint(warZoneController.displayWarZone())
    collisionController.addCollisions(warZoneController.displayWarZone())
    collisionController.displayCollision()
    scoreCard.updateScoreCard(0, 0)

    if keys[0]:
        if tankPosition[0] >= 0:
            tank.setTankPosition((tankPosition[0] - 20, tankPosition[1]))
    elif keys[1]:
        if tankPosition[0] <= graphics.getFieldSize()[0] - tank.getRect().width / 2:
            tank.setTankPosition((tankPosition[0] + 20, tankPosition[1]))

    graphics.displayFlip()

    # print(scoreCard.getExistingLives())
    if gameDuration - (timeNow - startTime).seconds <= 0 or scoreCard.getExistingLives() <= 0:
        running = 0
        exitCode = 0

gameOver = pygame.image.load("resources/images/youwin.png")
if exitCode == 0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: wow%", True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = graphics.screen.get_rect().centerx
    textRect.centery = graphics.screen.get_rect().centery + 24
    # graphics.screen.blit(gameOver, (0, 0))
    graphics.screen.blit(text, textRect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    graphics.displayFlip()

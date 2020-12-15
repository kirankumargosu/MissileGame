import pygame
from pygame.locals import *
import missile
from graphics import Graphics
from tank import Tank
import math
import random
# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False]
tankPosition = [290, 400]
missiles = []

# 3 - Load Images
missileImage = pygame.image.load("resources/images/missile.png")
backgroundImage = pygame.image.load("resources/images/grass.png")

running = 1
while running:
    screen.fill(0)
    # 6 - draw the player on the screen at X:100, Y:100
    for x in range(int(width / backgroundImage.get_width()) + 1):
        for y in range(int(height / backgroundImage.get_height()) + 1):
            screen.blit(backgroundImage, (x * 100, y * 100))

    # mousePosition = pygame.mouse.get_pos()
    # angle = math.atan2(mousePosition[1] - (tankPosition[1] + 32), mousePosition[0] - (tankPosition[0] + 26))
    # playerRotation = pygame.transform.rotate(missile, 360 - angle * 57.29)
    # playerpos1 = (
    #    tankPosition[0] - playerRotation.get_rect().width / 2,
    #    tankPosition[1] - playerRotation.get_rect().height / 2)
    # screen.blit(playerRotation, playerpos1)
    # screen.blit(missile, (290, 400))
    screen.blit(missileImage, tankPosition)

    # Display Debug Information
    font = pygame.font.Font(None, 15)
    debugText = font.render("Current Tank Position: " + str(tankPosition[0]) + ", " + str(tankPosition[1]), True, (0, 0, 0))
    textRect = debugText.get_rect()
    textRect.topright = [500, 50]
    screen.blit(debugText, textRect)

    # 8 - loop through the events
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
            missiles.append(missile.Missile(tankPosition))
            # missiles[len(missiles) - 1].display()

    # 9 - Move player
    if keys[0]:
        tankPosition[0] -= 5
    elif keys[1]:
        tankPosition[0] += 5

    pygame.display.flip()
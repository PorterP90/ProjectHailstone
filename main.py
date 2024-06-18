import pygame
import random
from player import playerClass
from enemies import *
from functions import *

pygame.init()



#colors :)

red = (134, 49, 54)
yellow = (219,214,7)

#Create game window
screenHeight, screenWidth = 500, 600
screenColor = (49,77,92)
screen = pygame.display.set_mode((screenWidth, screenHeight))

#framerate
clock = pygame.time.Clock()

#game running 
running = True


#create enemy group
enemies = pygame.sprite.Group()

#create player add him to sprite group
player = playerClass(red, screenHeight//2, screenWidth//2, 50, 50)
playerGroup = pygame.sprite.Group() 
playerGroup.add(player)


bulletGroup = pygame.sprite.Group()


gameLoops = 0

#game loop
while running:


    #screen image
    screen.fill(screenColor)


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #so this is working... but nothing on screen is happening
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullet1 = bulletClass(player.rect.x, player.rect.y) #createBullet(player)
                bulletGroup.add(bullet1)
                shooting(player, bullet1)
                print("bullet firing!!")

    #check if enemeis are stacked
    areWeStacked(enemies)
   

    #check for player movement and if he is out of bounds.
    player.checkMovement()
    player.outBounds(screenHeight, screenWidth)
    


    #enemie movement twoards player
    for enemy in enemies:
        enemy.pathForPlayer(player.rect.x, player.rect.y)
    

    #are we doing damage to the player?
    isHittingPlayer(enemies, player)
    

    #draw everything
    screen.fill(screenColor) #clear screen
    bulletGroup.draw(screen)
    screen.blit(player.image, player.rect) #draw player
    enemies.draw(screen) #draw enemies to screen.
    bulletGroup.update(screenWidth, screenHeight)
    enemies.update()

    #this wipes away anything from last frame.
    pygame.display.update()

    

    #add a new enemy every 100 loops :) (manipulate for fun stuff)
    if gameLoops % 1000 == 0:
        createEnemy(yellow, enemies, screenHeight, screenWidth)

    gameLoops += 1
    clock.tick(120)
    

    if player.health == 0:
        running = False
pygame.quit()









#THESE ARE THE NOTES FOR THE PROJECT :))))


#add sprite images to player / enemy
#add sounds?
#create map to navigate?
#add different enemy types
#add weapons to collect?
#add ammo?
#

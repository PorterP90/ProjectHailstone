import pygame
import random
from player import playerClass
from enemies import *
from functions import *

pygame.init()
pygame.mixer.init()

backgroundSound = pygame.mixer.Sound('Kashmir (Remaster).mp3')
bulletSound = pygame.mixer.Sound('M1911-FX1.mp3')


#colors :)

red = (134, 49, 54)
yellow = (219,214,7)

#Create game wind
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

#pygame.mixer.__loader__(Kashmir (remaster.mp3))

#game loop
backgroundSound.play()

while running:


    #screen image
    #screen.fill(screenColor)


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #so this is working... but nothing on screen is happening
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX,mouseY = pygame.mouse.get_pos()
            startX, startY = player.rect.x, player.rect.y
            if event.button == 1:
                bullet1 = bulletClass(player.rect.x, player.rect.y) #createBullet(player)
                bulletGroup.add(bullet1)
                #here we take the vector of the bullet and change the movement of it in its class.
                bullet1.moveX, bullet1.moveY = bulletVector(player, bullet1)
                bulletSound.play()
                
                #so in the game loop we need to update every bullet in the bullet class with their move line 79

    #check if enemeis are stacked
    areWeStacked(enemies)
   

    #check for player movement and if he is out of bounds.
    player.checkMovement()
    player.outBounds(screenHeight, screenWidth)
    


    #enemie movement twoards player
    for enemy in enemies:
        enemy.pathForPlayer(player.rect.x, player.rect.y)
    
    for bullet in bulletGroup:
        bullet.rect.x += bullet.moveX
        bullet.rect.y += bullet.moveY

    
    #are we doing damage to the player?
    isHitting(enemies, playerGroup)


    #are we doing damage to an enemie?
    isHitting(bulletGroup, enemies)

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
    if gameLoops % 1000 == 0:#add sounds?
        createEnemy(yellow, enemies, screenHeight, screenWidth)

    gameLoops += 1
    clock.tick(120)
    
    #check for death
    if player.health == 0:
        running = False

pygame.quit()










#THESE ARE THE NOTES FOR THE PROJECT :))))


#add sprite images to player / enemy
#create map to navigate?
#add different enemy types
#add weapons to collect?
#add ammo?
#

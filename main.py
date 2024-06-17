import pygame
import random
from player import playerClass
from enemies import *


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
dt = 0


running = True


#player = pygame.Rect((300, 250, 50, 50))


#create enemys 
enemies = pygame.sprite.Group()
#createEnemy(yellow, enemies, screenHeight, screenWidth)
#createEnemy(yellow, enemies, screenHeight, screenWidth)


#create player add him to sprite group
player = playerClass(red, screenHeight//2, screenWidth//2, 50, 50)
playerGroup = pygame.sprite.Group() 
playerGroup.add(player)



gameLoops = 0
#game loop
while running:

    screen.fill(screenColor)


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    areWeStacked(enemies)
   #update enemie group
    enemies.update()
   
    #draw enemies group onto screen.
    enemies.draw(screen)


    
    #check for player movement and if he is out of bounds.
    player.checkMovement()
    player.outBounds(screenHeight, screenWidth)


    #enemie movement...
    for enemy in enemies:
        enemy.pathForPlayer(player.rect.x, player.rect.y)

    #draw everything
    screen.fill(screenColor) #clear screen
    screen.blit(player.image, player.rect) #draw player
    enemies.draw(screen) #draw enemies to screen.

    #this wipes away anything from last frame.
    pygame.display.update()

    

    #add a new enemy every 100 loops :)

    if gameLoops % 1000 == 0:
        createEnemy(yellow, enemies, screenHeight, screenWidth)

    gameLoops += 1
    clock.tick(120)
    
pygame.quit()









#THESE ARE THE NOTES FOR THE PROJECT :))))


#create ability to shoot enemy 
    #track mouse position and then check for if click
    #if click take hyptonose of player pos to mouse pos then send "bullet" down the hyp checking for collsion with enemy
#create enemy damage when hit player
    #if enemy collide with player, player health -= damage
#add sprite images to player / enemy
#add sounds?
#create map to navigate?
#add different enemy types
#add weapons to collect
#add ammo?
#

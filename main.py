import pygame
import random
from player import playerClass
from enemies import EnemieClass


pygame.init()



#colors :)

red = (134, 49, 54)
yellow = (219,214,7)

#Create game window
screenHeight, screenWidth = 750, 800
screenColor = (49,77,92)
screen = pygame.display.set_mode((screenWidth, screenHeight))

#framerate
clock = pygame.time.Clock()
dt = 0


running = True


#player = pygame.Rect((300, 250, 50, 50))


#enemie group with first enemy added
enemie1 = EnemieClass(yellow, 500, 300)
enemies = pygame.sprite.Group()
enemies.add(enemie1)


#create player add him to sprite group
player = playerClass(red, screenHeight//2, screenWidth//2, 50, 50)
playerGroup = pygame.sprite.Group() 
playerGroup.add(player)






#game loop
while running:

    screen.fill(screenColor)

    #pygame.draw.rect(screen, (155,25,0), player)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
 
   #update enemie gro
    enemies.update()
   
    #draw enemies group onto screen.
    enemies.draw(screen)


    
    #check for player movement and if he is out of bounds.
    player.checkMovement()
    player.outBounds(screenHeight, screenWidth)

    #draw everything
    screen.fill(screenColor) #clear screen
    screen.blit(player.image, player.rect) #draw player

    #this wipes away anything from last frame.
    pygame.display.update()


    #dt = clock.tick(60) / 100
    
pygame.quit()

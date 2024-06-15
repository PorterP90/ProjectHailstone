import pygame
import random
from player import playerClass
from enemies import EnemieClass


pygame.init()

#Create game window
screenHeight, screenWidth = 1500, 1600
screenColor = (0,12,32)
screen = pygame.display.set_mode((screenWidth, screenHeight))

#framerate
clock = pygame.time.Clock()
dt = 0


running = True


#player = pygame.Rect((300, 250, 50, 50))


#enemie group with first enemy added
enemie1 = EnemieClass((0,0,0), 500, 300)
enemies = pygame.sprite.Group()
enemies.add(enemie1)

player = playerClass((25,0,0), screenHeight//2, screenWidth//2)
playerGroup = pygame.sprite.Group() 
playerGroup.add(player)



def outBounds(object, screenH, screenW):
    if object.right >= screenW:
        object.right = screenW
    if object.left <= 0:
        object.left = 0
    if object.bottom >= screenH:
        object.bottom = screenH
    if object.top <= 0:
        object.top = 0


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


    #outBounds(player, screenHeight, screenWidth)
    player.checkMovement()

    #draw everything
    screen.fill(screenColor) #clear screen
    screen.blit(player.image, player.rect) #draw player

    #this wipes away anything from last frame.
    pygame.display.update()


    #dt = clock.tick(60) / 100
    
pygame.quit()

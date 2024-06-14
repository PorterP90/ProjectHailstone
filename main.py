import pygame
import random
from player import playerClass
from enemies import EnemieClass


pygame.init()

#Create game window
screenHeight, screenWidth = 600, 800
screenColor = (0,12,32)
screen = pygame.display.set_mode((screenWidth, screenHeight))

#framerate
clock = pygame.time.Clock()
dt = 0


running = True


player = pygame.Rect((300, 250, 50, 50))


#enemie group with first enemy added
enemie1 = EnemieClass((0,0,0), 500, 300)
enemies = pygame.sprite.Group()
enemies.add(enemie1)




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

    pygame.draw.rect(screen, (155,25,0), player)
 
 
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-1, 0)
    elif key[pygame.K_d]:
        player.move_ip(1, 0)
    elif key[pygame.K_s]:
        player.move_ip(0, 1)
    elif key[pygame.K_w]:
        player.move_ip(0, -1)
    elif key[pygame.K_a] and key[pygame.K_w]:
        player.move_ip(-1, -1)
    elif key[pygame.K_a and pygame.K_s]:
        player.move_ip(-1, 1)
    elif key[pygame.K_d and pygame.K_w]:
        player.move_ip(1, -1)
    elif key[pygame.K_d and pygame.K_s]:
        player.move_ip(1, 1)
   

   #update enemie group
    enemies.update()
   
    #draw enemies group onto screen.
    enemies.draw(screen)



   
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    outBounds(player, screenHeight, screenWidth)
    

    #this wipes away anything from last frame.
    pygame.display.update()


    #dt = clock.tick(60) / 100
    
pygame.quit()

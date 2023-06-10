import pygame
import random
from enemies import EnemieClass


pygame.init()
screenHeight, screenWidth = 600, 800
screenColor = (0,12,32)
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
running = True
dt = 0

player = pygame.Rect((300, 250, 50, 50))

enemie1 = EnemieClass()



#def createEnemy():
#    startX, startY = random.randrange(0, screenWidth), 25
#    enemy = pygame.Rect((startX, startY, 25, 25))
#    pygame.draw.rect(screen, (0, 0, 0), enemy)
#    enemy.move_ip(0,1)

def outBounds(object, screenH, screenW):
    if object.right >= screenW:
        object.right = screenW
    if object.left <= 0:
        object.left = 0
    if object.bottom >= screenH:
        object.bottom = screenH
    if object.top <= 0:
        object.top = 0

while running:

    screen.fill(screenColor)

    pygame.draw.rect(screen, (155,25,0), player)
    enemie1.draw(screen)
    #enemie1.move_ip(1,0)
    
    #createEnemy()

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    outBounds(player, screenHeight, screenWidth)
    

    #this wipes away anything from last frame.
    pygame.display.update()


    #dt = clock.tick(60) / 100
    
pygame.quit()

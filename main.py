import pygame
import random
from player import playerClass
from enemies import *
from functions import *

pygame.init()
pygame.mixer.init()
pygame.font.init()

backgroundSound = pygame.mixer.Sound('Kashmir (Remaster).mp3')
bulletSound = pygame.mixer.Sound('M1911-FX1.mp3')

backgroundSound.set_volume(.5)
bulletSound.set_volume(.6)

#colors :)
red = (134, 49, 54)
yellow = (219,214,7)

#Create game window
screenHeight, screenWidth = 1000, 1200
screenColor = (49,77,92)
screen = pygame.display.set_mode((screenWidth, screenHeight))

#framerate
clock = pygame.time.Clock()
freamerate = 120

#game running 
running = True


#create enemy group
enemies = pygame.sprite.Group()

#create player add him to sprite group
player = playerClass(screenHeight//2, screenWidth//2)
playerGroup = pygame.sprite.Group() 
playerGroup.add(player)

#create the bullet group *thumbs up*
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
        elif event.type == pygame.MOUSEBUTTONDOWN and player.ammo != 0:
            mouseX,mouseY = pygame.mouse.get_pos()
            startX, startY = player.rect.center[0], player.rect.center[1]
            if event.button == 1:
                bullet1 = bulletClass(startX, startY) #createBullet(player)
                bulletGroup.add(bullet1)
                #here we take the vector of the bullet and change the movement of it in its class.
                bullet1.moveX, bullet1.moveY = bulletVector(player, bullet1)
                bulletSound.play()
                player.ammo -= 1
                
                #so in the game loop we need to update every bullet in the bullet class with their move line 79

    #check if enemeis are stacked
    areWeStacked(enemies)
   

    #check for player movement and if he is out of bounds.
    player.checkMovement()
    player.outBounds(screenHeight, screenWidth)
    


    #enemie movement twoards player
    for enemy in enemies:
        enemy.pathForPlayer(player)
    
    for bullet in bulletGroup:
        bullet.rect.x += bullet.moveX
        bullet.rect.y += bullet.moveY

    
    #are we doing damage to the player?
    isHitting(enemies, playerGroup)


    #are we doing damage to an enemie?
    isHitting(bulletGroup, enemies)
    #update if bullet hit an enemy
    for bullet in bulletGroup:
        bullet.hitEnemy(enemies)


    #draw everything
    
    bulletGroup.draw(screen) #draw our bullets
    screen.blit(player.image, player.rect) #draw player
    for enemy in enemies:
        screen.blit(enemy.image, enemy.rect) #draw enemies to screen.
    bulletGroup.update(screenWidth, screenHeight) #update bullets
    enemies.update() #update our enemys 

    #this wipes away anything from last frame.
    pygame.display.update()
    pygame.display.flip()
    screen.fill(screenColor) #clear screen

    #add a new enemy every 100 loops :) (manipulate for fun stuff)
    if gameLoops % 200 == 0:#add sounds?
        createEnemy(enemies, screenHeight, screenWidth)

    gameLoops += 1
    clock.tick(freamerate)
    
    #check for death
    if player.health == 0:
        running = False
    
    ammoMessage = f"Ammo: {player.ammo}"
    render_text(screen, ammoMessage, 75, 18, 35)

pygame.quit()










#THESE ARE THE NOTES FOR THE PROJECT :))))

#add ammo (funcitonal / visual)
#make it so enemys dont go on top of player (functional)
#make hit markers for bullet and enemy hits (audio thing)
#make bullet images that rotate dependent upon firing vector (visual)

#create map to navigate? (visual / funtional)
#add different enemy types (functional)
#add weapons to collect? (funtional)


#trim gunshot audio

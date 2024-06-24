import pygame
import random
from player import playerClass
from enemies import *
from functions import *
from weapons import *

pygame.init()
pygame.mixer.init()
pygame.font.init()

backgroundSound = pygame.mixer.Sound('Kashmir (Remaster).mp3')

backgroundSound.set_volume(.5)


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
player.weapon1 = M4A4
#player.weapon2 = M1911
player.activeWeapon = player.weapon1
playerGroup = pygame.sprite.Group() 
playerGroup.add(player)

#create the bullet group *thumbs up*
bulletGroup = pygame.sprite.Group()
ammoGroup = pygame.sprite.Group()


gameLoops = 0

#pygame.mixer.__loader__(Kashmir (remaster.mp3))

#game loop
backgroundSound.play()

while running:

    #event handler
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if player.activeWeapon.magAmmo != 0:
                player.shooting(bulletGroup, event)

    print("chekcing keys...")
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        player.startTime = pygame.time.get_ticks()
        player.reloadWeapon()
        print("r key pressed")
    if keys[pygame.K_1]:
        player.switchWeapon()
    if keys[pygame.K_2]:
        player.switchWeapon()
    if keys[pygame.K_3]:
        player.switchWeapon()

    
    #check if enemeis are stacked
    areWeStacked(enemies)
   


    #enemie movement twoards player
    for enemy in enemies:
        enemy.pathForPlayer(player)
    
    for bullet in bulletGroup:
        bullet.rect.x += bullet.moveX
        bullet.rect.y += bullet.moveY

    
    #are we doing damage to the player?
    isHitting(enemies, playerGroup)


    #are we doing damage to an enemy
    for bullet in bulletGroup:
        bullet.hitEnemy(enemies)


    #draw everything
    
    bulletGroup.draw(screen) #draw our bullets
    screen.blit(player.image, player.rect) #draw player
    if True:
        player.activeWeapon.rect.topleft = player.rect.center
        #player.activeWeapon.rect.midleft = player.rect.centery
        rotatedSprite = pygame.transform.rotate(player.activeWeapon.image, player.activeWeapon.imageVectorAngle(player))
        rotatedRect =  rotatedSprite.get_rect(midleft=player.activeWeapon.rect.midright)
        screen.blit(rotatedSprite, rotatedRect )

    for enemy in enemies:
        screen.blit(enemy.image, enemy.rect) #draw enemies to screen.
    for box in ammoGroup:
        screen.blit(box.image, box.rect)
        box.collected(player)

    #update our groups
    bulletGroup.update(screenWidth, screenHeight) #update bullets
    enemies.update() #update our enemys 
    ammoGroup.update()
    player.update(screenHeight, screenWidth)
    #player.reloadWeapon()
    #player.switchWeapon()
    #player.dropWeapon()

    #this wipes away anything from last frame.
    pygame.display.update()
    pygame.display.flip()
    screen.fill(screenColor) #clear screen

    #add a new enemy every 100 loops :) (manipulate for fun stuff)
    if gameLoops % 200 == 0:#add sounds?
       createEnemy(enemies, screenHeight, screenWidth)

    #add ammo box to screen to collect
    if gameLoops % 1000 == 0:
       createAmmoBox(screenHeight, screenWidth, ammoGroup)




    gameLoops += 1
    clock.tick(freamerate)
    
    #check for death
    if player.health == 0:
        running = False
    

    print(player.activeWeapon)
    ammoMessage = f"Ammo: {player.activeWeapon.magAmmo} / {player.activeWeapon.reserveAmmo}"
    render_text(screen, ammoMessage, 75, 18, 35)

pygame.quit()











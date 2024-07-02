import pygame
import random
import math
from enemies import EnemieClass
from player import playerClass
from weapons import bulletClass
from ammoBoxs import ammoBoxs


def createEnemy(enemyGroup, screenHeight, screenWidth):
        if random.choice([True, False]):
            n = random.randint(-250, -50)
        else:
            n = random.randint((screenWidth+50), (screenWidth+250))
        if random.choice([True, False]):
            m = random.randint(-250, -50)
        else:
            m =random.randint((screenHeight + 50), (screenHeight+250))
        
        newEnemy = EnemieClass(n, m)
        enemyGroup.add(newEnemy)

def areWeStacked(enemyGroup):
    #create enemy collisions so they cant stack each other 
        #so I need to take all enemies in the enemy group and check if touching? 
         #if they are touching then space then out by height / width of the enemy
    for enemy1 in enemyGroup:
            for enemy2 in enemyGroup:
                if enemy1 != enemy2 and pygame.sprite.collide_rect(enemy1, enemy2):
                    distance_x = abs(enemy1.rect.centerx - enemy2.rect.centerx)
                    distance_y = abs(enemy1.rect.centery - enemy2.rect.centery)
            

                    if distance_x < enemy1.rect.width and distance_y < enemy1.rect.height:
                        # Calculate how much to move them apart
                        move_x = (enemy1.rect.width + 1) - distance_x
                        move_y = (enemy1.rect.height + 1) - distance_y
                    
                        # Move enemy1 right and down and enemy2 left and up
                        enemy1.rect.x += move_x / 2
                        enemy1.rect.y += move_y / 2
                        enemy2.rect.x -= move_x / 2
                        enemy2.rect.y -= move_y / 2

def createBullet(player):
    #create a bullet rect/sprite and give its starting x,y = players x,y
    #becasue we only create a bullet when player is shooting...
    bullet = bulletClass(player.center.x, player.center.y)



def isHitting(objectGroup, opposition):
     for object in objectGroup:
        for opp in opposition:
            if pygame.sprite.collide_rect(object, opp):
                opp.health -= object.damage
                print(opp)
                print(opp.health)


def render_text(screen, text, x, y, font_size=12, font_color=(255, 255, 255)):
    font = pygame.font.SysFont(None, font_size)  # Use default system font
    text_surface = font.render(str(text), True, font_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)


def createAmmoBox(screenH, screenW, ammoGroup):
    x = random.randint(25, screenH)
    y = random.randint(25, screenW)
    ammoBox = ammoBoxs(x, y)
    ammoGroup.add(ammoBox)


def playerCircleDist(player):
    lenX = player.rect.x + player.rect.right
    lenY = player.rect.y + player.rect.bottom

    #hypno to corner of rect and then make that a offset

    playerCorner = math.hypot(lenX, lenX)

    return playerCorner

def rounds(zombieGroup, round):
    startZoms = 5
    if zombieGroup == 0:
        round += 1
    totalZoms = startZoms * round 
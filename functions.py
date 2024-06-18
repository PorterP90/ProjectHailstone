import pygame
import random
import math
from enemies import EnemieClass
from player import playerClass
from weapons import bulletClass


def createEnemy(color, enemyGroup, screenHeight, screenWidth):
        if random.choice([True, False]):
            n = random.randint(-250, -50)
        else:
            n = random.randint((screenWidth+50), (screenWidth+250))
        if random.choice([True, False]):
            m = random.randint(-250, -50)
        else:
            m =random.randint((screenHeight + 50), (screenHeight+250))
        
        newEnemy = EnemieClass(color, n, m)
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
    bullet = bulletClass(player.rect.x, player.rect.y)

def shooting(player, bulletSpeed, bullet):
        #create ability to shoot enemy 
    #track mouse position and then check for if click
    #if click take hyptonose of player pos to mouse pos then send "bullet" 
    # down the hyp checking for collsion with the enemy
    if pygame.mouse.get_pressed():
        createBullet(player)
        (mouseX,mouseY) = pygame.mouse.get_pos()

        dx = mouseX - player.rect.x
        dy = mouseY - player.rect.y

        dist = math.hypot(dx, dy)

        dx /= dist
        dy /= dist

        moveX = dx * bulletSpeed
        moveY = dx * bulletSpeed

        bullet.rect.x += moveX
        bullet.rect.y += moveY

def isHittingPlayer(enemyGroup, player):
     for enemy in enemyGroup:
        if pygame.sprite.collide_rect(enemy, player):
             player.health -= enemy.damage
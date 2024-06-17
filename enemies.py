import pygame
import random
import math

pygame.init

black = (0,0,0)

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


class EnemieClass(pygame.sprite.Sprite):
    def __init__(self, col, x, y, width = 25, height = 25):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pygame.Surface((width,height))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.health = 100
        self.speed = 1



    #takes the enemies x, y coordinate and slowly transverses the hypotinose to the players x y cord, should change when player x y changes
    def pathForPlayer(self, playerX, playerY):
        # Calculate vector from enemy to player
        dx = playerX - self.rect.x
        dy = playerY - self.rect.y

        # Calculate the distance to the player
        dist = math.hypot(dx, dy)

        # Ensure dist is not zero to avoid division by zero
        if dist != 0:
            # Normalize vector
            dx /= dist
            dy /= dist

            # Calculate movement in both x and y directions
            moveX = dx * self.speed
            moveY = dy * self.speed

            # Update enemy position
            self.rect.x += moveX
            self.rect.y += moveY



    #this function is  what will  update each frame so movement etc. 
    def update(self):
        if self.health <= 0:
            self.kill
        


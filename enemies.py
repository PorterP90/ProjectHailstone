import pygame
import random
import math

pygame.init

black = (0,0,0)




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
        self.damage = 1



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
        


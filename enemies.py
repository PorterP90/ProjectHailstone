import pygame
import random
import math

pygame.init

black = (0,0,0)




class EnemieClass(pygame.sprite.Sprite):
    def __init__(self, x, y,):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/zombie.png')
        self.rect = self.image.get_rect(center = (x//2, y//2))
        self.health = 100
        self.speed = 1
        self.damage = 1
        self.alive = True



    #takes the enemies x, y coordinate and slowly transverses the hypotinose to the players x y cord, should change when player x y changes
    def pathForPlayer(self, player):
        # Calculate vector from enemy to player
        if self.alive:
            dx = player.rect.center[0] - self.rect.center[0]
            dy = player.rect.center[1] - self.rect.center[1]

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
            self.alive = False
            self.kill()
            print("enemy deads")
        
        


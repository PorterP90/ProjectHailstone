import pygame
import random

pygame.init

black = (0,0,0)



class EnemieClass(pygame.sprite.Sprite):
    def __init__(self, col, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((75,75))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.health = 100

    #this function is  what will  update each frame so movement etc. 
    def update(self):
        if self.health <= 0:
            self.kill



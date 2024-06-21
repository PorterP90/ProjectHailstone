import pygame
import math

class ammoBoxs(pygame.sprite.Sprite):
    def __init__(self, x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ammoBox.png')
        self.rect = self.image.get_rect(center = (x//2, y//2))
        self.bulletCount = 25
        self.alive = True

    def collected(self, player):
        if pygame.sprite.collide_rect(self, player):
            player.ammo += self.bulletCount
            self.alive = False
            return True
        return
        
    def update(self):
        if self.alive == False:
            self.kill()


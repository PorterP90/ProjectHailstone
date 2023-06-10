import pygame
import random

pygame.init

class EnemieClass:
    def __init__(self):
        self.width = 25
        self.height = 25
        self.startX = random.randrange(0,775)
        self.startY = 25 #should be -25 but we cant see -25 so if error set to 25
        self.color = (0,0,0)
        self.rect = pygame.Rect((self.startX,self.startY, self.width, self.height))
    
    def draw(self, screen):
        pygame.draw.rect(screen, (0,0,0), self.rect)

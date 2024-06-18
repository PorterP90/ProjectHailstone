import pygame
import math

player_image = pygame.image.load('mouse.png').convert_alpha

#draw to screen
#screen.blit(player_image, x, y)

class playerClass(pygame.sprite.Sprite):
    def __init__(self, color,x ,y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 2

    def checkMovement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= self.speed
        elif key[pygame.K_d]:
            self.rect.x +=  self.speed
        elif key[pygame.K_s]:
            self.rect.y += self.speed
        elif key[pygame.K_w]:
            self.rect.y -= self.speed

    def outBounds(self, screenH, screenW):
        if self.rect.right >= screenW:
            self.rect.right = screenW
        elif self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.bottom >= screenH:
            self.rect.bottom = screenH
        elif self.rect.top <= 0:
            self.rect.top = 0


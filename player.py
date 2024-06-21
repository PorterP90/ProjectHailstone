import pygame
import math
from weapons import bulletClass


player_image = pygame.image.load('mouse.png').convert_alpha

#draw to screen
#screen.blit(player_image, x, y)

class playerClass(pygame.sprite.Sprite):
    def __init__(self, x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.image = pygame.image.load('mouse.png')
        #self.image.fill(color)
        self.rect = self.image.get_rect(center = (x//2, y//2))
        self.speed = 2
        self.ammo = 50
        self.activeWeaponSlot = 2

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

    def shooting(self, bulletGroup, event):
                mouseX, mouseY = pygame.mouse.get_pos()
                startX, startY = self.rect.center[0], self.rect.center[1]
                if event.button == 1:
                    bullet1 = bulletClass(startX, startY) #createBullet(player)
                    bulletGroup.add(bullet1)
                    #here we take the vector of the bullet and change the movement of it in its class.
                    bullet1.moveX, bullet1.moveY = bullet1.bulletVector(self)
                    bullet1.sound.play()
                    self.ammo -= 1
 

    def update(self, screenH, screenW):
        self.checkMovement()
        self.outBounds(screenH, screenW)
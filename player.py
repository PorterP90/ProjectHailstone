import pygame
import math
from weapons import bulletClass


player_image = pygame.image.load('mouse.png').convert_alpha

#draw to screen
#screen.blit(player_image, x, y)

class playerClass(pygame.sprite.Sprite):
    def __init__(self, x ,y):
        #draw player
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('mouse.png')
        self.rect = self.image.get_rect(center = (x//2, y//2))
        #functionality below
        self.speed = 2
        self.health = 100
        self.activeWeapon = None
        self.weapon1 = None
        self.weapon2 = None
        self.weapon3 = None
        self.startTime = pygame.time.get_ticks()
        

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
                startX, startY = self.rect.center[0], self.rect.center[1]
                if event.button == 1: #check for left click
                    bullet1 = bulletClass(startX, startY) #createBullet(player)
                    bullet1.damage = self.activeWeapon.damage
                    bulletGroup.add(bullet1)
                    #here we take the vector of the bullet and change the movement of it in its class.
                    bullet1.moveX, bullet1.moveY = bullet1.bulletVector(self)
                    self.activeWeapon.shootAudio.play() #eventuall change to the actual weapons sound
                    self.activeWeapon.magAmmo -= 1
    
    #def dropWeapon(self):
            #this just sets our active weapon to none, but we need to set our weapon to none
    #        if self.activeWeapon == self.weapon2:
    #            self.weapon2 = None
    #            self.activeWeapon = self.weapon3
    #            print("secondary dropped, new weapon knife")
    #            return
    #        elif self.activeWeapon == self.weapon1:
    #             self.weapon1 = None
    #             self.activeWeapon = self.weapon2
    #             print("Primary weapon dropped, new weapon is secondary")
    #             return

    
    def switchWeapon(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_1] and self.weapon1 != None:
            self.activeWeapon = self.weapon1
        elif key[pygame.K_2] and self.weapon2 != None:
            self.activeWeapon = self.weapon2
        elif key[pygame.K_3]:
            self.activeWeapon = self.weapon3

    def reloadWeapon(self):
        currentTime = pygame.time.get_ticks()
        if self.activeWeapon.magAmmoMax > self.activeWeapon.magAmmo and self.activeWeapon.reserveAmmo > 0:
            if currentTime - self.startTime >= self.activeWeapon.reloadTime:
                #add up to total magAmmoMax if cant fill all the way add all of reserve to activeammo
                toAdd = self.activeWeapon.magAmmoMax - self.activeWeapon.magAmmo
                if toAdd > self.activeWeapon.reserveAmmo:
                    self.activeWeapon.magAmmo += self.activeWeapon.reserveAmmo
                    self.activeWeapon.reserveAmmo = 0
                else:
                    self.activeWeapon.magAmmo = self.activeWeapon.magAmmoMax
                    self.activeWeapon.reserveAmmo -= toAdd
                
            self.activeWeapon.reloadAudio.play()

        

                
            
             

    def update(self, screenH, screenW):
        self.checkMovement()
        self.outBounds(screenH, screenW)
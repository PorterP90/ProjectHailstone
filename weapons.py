import pygame
import math


pygame.mixer.init()
bulletSound = pygame.mixer.Sound('M1911-FX1.mp3')
bulletSound.set_volume(.6)


#here is some rubber ducking.
#so im going to have multiple weapons each has its own unique bullet speed damage ammo and mag size
#

class weaponsClass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bulletSpeed = 5
        self.ammo = 25
        self.magSize = None
        self.damage = 25
        self.weaponSlot = None
        self.sound = bulletSound
    
    def isAuto(self):
        if self.automatic == True:
            return True
        else:
            return False

    
class primaryWeapons(weaponsClass):
    def __init__(self, reserveAmmo, magAmmo, magAmmoMax, damage, automatic, firingRate):
        super().__init__()
        self.weaponSlot = 1 
        self.reserveAmmo = reserveAmmo
        self.magAmmoMax = magAmmoMax
        self.magAmmo = magAmmo
        self.damage = damage
        self.automatic = automatic #This should be a bool
        self.firingRate = firingRate



class secondaryWeapons(weaponsClass):
    def __init__(self, reserveAmmo, magAmmo, magAmmoMax, damage, automatic, firingRate):
        super().__init__()
        self.weaponSlot = 2
        self.reserveAmmo = reserveAmmo
        self.magAmmo = magAmmo
        self.magAmmoMax = magAmmoMax
        self.damage = damage
        self. automatic = automatic
        self.firingRate = firingRate
    


#This class draws and moves the bullet as well as does damage to player... thats all it needs to do
class bulletClass(weaponsClass):
    def __init__(self, startX, startY):
        super().__init__()
        self.image = pygame.Surface((15,15))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (startX, startY)
        self.moveX = 0
        self.moveY = 0
        
    def bulletVector(self, player):
    #create ability to shoot enemy 
    #track mouse position and then check for if click
    #if click take hyptonose of player pos to mouse pos then send "bullet" 
    # down the hyp checking for collsion with the enemy
    #if pygame.mouse.get_pressed():     #RUN THIS LINE BEFORE CALLING FUNCTION IN MAIN LOOP
        if self.alive:    
            mouseX,mouseY = pygame.mouse.get_pos()

            dx = mouseX - player.rect.center[0]
            dy = mouseY - player.rect.center[1]

            dist = math.hypot(dx, dy)

            dx /= dist
            dy /= dist

            moveX = dx * self.bulletSpeed
            moveY = dy * self.bulletSpeed

            self.rect.x += moveX
            self.rect.y += moveY
            return (moveX, moveY)


    def update(self, screenWidth, screenHeight):
        if self.rect.x > screenWidth or self.rect.x < 0 or self.rect.y > screenHeight or self.rect.y < 0:
            print("bullet is dead!")
            self.kill()
            self.alive = False
    
    def hitEnemy(self, enmieGroup):
        for enemy in enmieGroup:
            if pygame.sprite.collide_rect(self, enemy):
                enemy.health -= self.damage 
                self.kill()
                self.alive = False





#rifles
#M4A4 = primaryWeapons(50, 25, 50 , True, 8)
#AK47 = primaryWeapons(50, 30, 40, True, 7)



#pistols
M1911 = secondaryWeapons(24, 15, 15, 25, False, 0)
#GLOCK20 = secondaryWeapons(25, 20, 25, False, 0)
#CZ75 = secondaryWeapons(14, 14, 20, True, 10)
#DEAGLE = secondaryWeapons(14, 7, 50, False, 0)
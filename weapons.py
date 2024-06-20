import pygame




#here is some rubber ducking.
#so im going to have multiple weapons each has its own unique bullet speed damage ammo and mag size
#

class weaponsClass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bulletSpeed = 5
        self.ammo = 0
        self.magSize = 0
        self.damage = 25
        self.weaponSlot = None

    
class primaryWeapons(weaponsClass):
    def __init__(self):
        self.weaponSlot = 1


class bulletClass(weaponsClass):
    def __init__(self, startX, startY):
        super().__init__()
        self.image = pygame.Surface((15,15))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (startX, startY)
        self.moveX = 0
        self.moveY = 0
        


    def update(self, screenWidth, screenHeight):
        if self.rect.x > screenWidth or self.rect.x < 0 or self.rect.y > screenHeight or self.rect.y < 0:
            print("bullet is dead!")
            self.kill()
            self.alive = False
    
    def hitEnemy(self, enmieGroup):
        for enemy in enmieGroup:
            if pygame.sprite.collide_rect(self, enemy):
                self.kill()
                self.alive = False
        


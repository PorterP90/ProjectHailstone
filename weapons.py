import pygame




#here is some rubber ducking.
#so im going to have multiple weapons each has its own unique bullet speed damage ammo and mag size
#

class weaponsClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bulletSpeed = 3
        self.ammo = 0
        self.magSize = 0
        self.damage = 1
        self.weaponSlot = None

    
class primaryWeapons(weaponsClass):
    def __init__(self):
        self.weaponSlot = 1


class bulletClass(weaponsClass):
    def __init__(self, startX, startY):
        pass


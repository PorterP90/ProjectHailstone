import pygame



player_image = pygame.image.load('mouse.png').convert_alpha

#draw to screen
#screen.blit(player_image, x, y)

class playerClass(pygame.sprite.Sprite):
    def __init__(self, color,x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.image = pygame.Surface((50,50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.ret.center = (x, y)
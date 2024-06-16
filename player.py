import pygame



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

    def checkMovement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x += -1
        elif key[pygame.K_d]:
            self.rect.x +=  1
        elif key[pygame.K_s]:
            self.rect.y += 1
        elif key[pygame.K_w]:
            self.rect.y += -1

    def outBounds(self, screenH, screenW):
        if self.rect.right >= screenW:
            self.rect.right = screenW
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= screenH:
            self.rect.bottom = screenH
        if self.rect.top <= 0:
            self.rect.top = 0



import pygame


class Misil(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.disparo = pygame.image.load("imagenes/disparo.png")
        self.rect = self.disparo.get_rect()
        self.velocidadDisparo = 8
        self.rect.top = posY
        self.rect.left = posX

    def recorrido(self):
        self.rect.top = self.rect.top - self.velocidadDisparo

    def dibujar(self, superficie):
        superficie.blit(self.disparo, self.rect)
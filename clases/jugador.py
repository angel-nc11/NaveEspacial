import pygame
from clases import misil

class nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgNave = pygame.image.load("imagenes/nave.png")
        self.imgExplosion = pygame.image.load("imagenes/explosion.png")
        self.rect = self.imgNave.get_rect()
        #posision inicial de la nave
        self.rect.centerx = 380
        self.rect.centery = 670
        self.velocidad = 40
        self.vida = True
        self.listaDisparo = []
       

    def moverNave(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right >800:
                self.rect.right = 800

    def misil(self, x , y):
        disparo = misil.Misil(x,y)
        self.listaDisparo.append(disparo)
        
    def dibujarNave(self, superficie):
        if self.vida == True:
            superficie.blit(self.imgNave, self.rect)
        elif self.vida == False:
            superficie.blit(self.imgExplosion, self.rect)
           


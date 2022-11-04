import pygame
import sys
from pygame.locals import *
from clases import jugador
from clases import asteroide
from random import randint
from time import process_time as clock


ancho = 800
alto = 700
jugando = True
listaAsteroide = []
puntos = 0
colorFuente = (222, 12, 89)
emojyPerdedor=pygame.image.load("imagenes/perdedor.png") 



def cargarAsteroides(x,y):
    meteoro = asteroide.enemy(x,y)
    listaAsteroide.append(meteoro)

def gameOver():
    global jugando
    jugando = False
    for meteoritos in listaAsteroide:
        listaAsteroide.remove(meteoritos)
    sonidoGameOver = pygame.mixer.Sound("C:\python\juego\JuegoMeteorito\sonidoJuego/GameOver.wav")
    sonidoGameOver.play() 
    
    
        

#Funcion principal
def meteoritos():
    pygame.init()
    windowGame = pygame.display.set_mode((ancho, alto))
    fondo = pygame.image.load("imagenes/planetas.jpg")   
    pygame.display.set_caption("GALAXY-KILLER")

    nave = jugador.nave()
    contador = 0

    soundFondo = pygame.mixer.Sound("C:\python\juego\JuegoMeteorito\sonidoJuego/fondos.wav")
    soundFondo.play(50)
    sonidoColision = pygame.mixer.Sound("C:\python\juego\JuegoMeteorito\sonidoJuego/colisionNave.aiff")
    sonidoDisparo = pygame.mixer.Sound("C:\python\juego\JuegoMeteorito\sonidoJuego/Disparo.wav")

    fuenteMarcador = pygame.font.SysFont("Bold Italic", 30)
    mostrarTime = fuenteMarcador.render("Tiempo", True, colorFuente)

    while True:
        windowGame.blit(fondo , (0,0))               
        nave.dibujarNave(windowGame)
        
        global puntos
        marcador = fuenteMarcador.render(
        "Puntos -- "+str(puntos), 0, colorFuente)
        windowGame.blit(marcador, (0, 0))

          
     

        tiempo = clock()
        if tiempo - contador > 1:
            contador = tiempo
            posX = randint(30,850)
            cargarAsteroides(posX,0)

        if len(listaAsteroide) > 0:
            for x in listaAsteroide:
                if jugando == True:
                    x.dibujar(windowGame)
                    x.recorrido()
                if x.rect.top > 690:
                    listaAsteroide.remove(x)
                else:
                    if x.rect.colliderect(nave.rect):
                        listaAsteroide.remove(x)
                        sonidoColision.play()
                        nave.vida = False
                        gameOver()
                        soundFondo.stop()
                        
                        
                        
                        
        if len(nave.listaDisparo) > 0:
            for x in nave.listaDisparo:
                x.dibujar(windowGame)
                x.recorrido()
                if x.rect.top < -10:
                    nave.listaDisparo.remove(x)
                else:
                    for meteoritos in listaAsteroide:
                        if x.rect.colliderect(meteoritos.rect):
                            listaAsteroide.remove(meteoritos)
                            nave.listaDisparo.remove(x)
                            puntos+=1
                             
        
        nave.moverNave()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            
            elif evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    nave.rect.left -= nave.velocidad
                elif evento.key == K_RIGHT:
                    nave.rect.left += nave.velocidad
                elif evento.key == K_SPACE:
                    x=nave.rect.centerx
                    y=nave.rect.centery
                    x1= nave.rect.centerx
                    y1= nave.rect.centery
                    nave.misil(x1-50,y1-50)
                    nave.misil(x+30,y-50)
                    sonidoDisparo.play() 

        if jugando == False:
           FuenteGameOver = pygame.font.SysFont("Bold Italic", 60)
           textoGameOver = FuenteGameOver.render("Game Over", 0, colorFuente)
           windowGame.blit(textoGameOver, (250, 320))   
           windowGame.blit(emojyPerdedor, (500,280))
                
            

        pygame.display.update()
        

meteoritos()

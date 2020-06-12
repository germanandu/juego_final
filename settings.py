import pygame
import random

ANCHO=1024
ALTO=578
AMARILLO=[255,255,0]
AZUL=[0,0,255]
NEGRO=[0,0,0]
VERDE=[0,255,0]
BLANCO=[255,255,255]
#IMAGENES
golem=pygame.image.load('img/golem.png')

#RECORTE
m4=[]
for f in range(4):
    fila=[]
    for c in range(3):
        cuadro=golem.subsurface(64*c,80*f,64,80)
        fila.append(cuadro)
    m4.append(fila)

#VARIABLES
inicio_juego=False
fin_juego=False
fin = False
reloj=pygame.time.Clock()

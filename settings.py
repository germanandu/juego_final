import pygame
import random

ANCHO=768
ALTO=620
AMARILLO=[255,255,0]
AZUL=[0,0,255]
NEGRO=[0,0,0]
VERDE=[0,255,0]
BLANCO=[255,255,255]
#IMAGENES
golem=pygame.image.load('img/golem.png')
#jugador
i_vida=pygame.image.load('img/vida.png')
derecha=pygame.image.load('img/personaje/run.png')
izquierda=pygame.image.load('img/personaje/run2.png')
hide=pygame.image.load('img/personaje/hide.png')
hide2=pygame.image.load('img/personaje/hide2.png')
atack1=pygame.image.load('img/personaje/attack.png')
atack2=pygame.image.load('img/personaje/attack2.png')
#ave
hide_ave=pygame.image.load('img/ave/Flight.png')
bala_ave=pygame.image.load('img/bala_ave.png')
#lobo
walk1=pygame.image.load('img/lobo/walk1.png')
walk2=pygame.image.load('img/lobo/walk2.png')
#BOSS1
boss_hide=pygame.image.load('img/boss1/hide.png')
boss_atack=pygame.image.load('img/boss1/attack.png')
#POCION
pocionv_i=pygame.image.load('img/pocionv.png')
pocionx_i=pygame.image.load('img/pocionx.png')


#RECORTE JUGADOR

m_derecha=[]
for c in range(12):
    cuadro=derecha.subsurface(66*c,48*0,66,48)
    m_derecha.append(cuadro)

m_izquierda=[]
for c in range(12):
    cuadro=izquierda.subsurface(66*c,48*0,66,48)
    m_izquierda.append(cuadro)

m_hide=[]
for c in range(4):
    cuadro=hide.subsurface(38*c,48*0,38,48)
    m_hide.append(cuadro)

m_hide2=[]
for c in range(4):
    cuadro=hide2.subsurface(38*c,48*0,38,48)
    m_hide2.append(cuadro)

m_atack1=[]
for c in range(6):
    cuadro=atack1.subsurface(96*c,48*0,96,48)
    m_atack1.append(cuadro)

m_atack2=[]
for c in range(6):
    cuadro=atack2.subsurface(96*c,48*0,96,48)
    m_atack2.append(cuadro)

#RECORTE GOLEM
m4=[]
for f in range(4):
    fila=[]
    for c in range(3):
        cuadro=golem.subsurface(64*c,80*f,64,80)
        fila.append(cuadro)
    m4.append(fila)

#RECORTE AVE
m_ave=[]
for c in range(8):
    cuadro=hide_ave.subsurface(150*c,150*0,150,150)
    m_ave.append(cuadro)

#RECORTE VIDA
m_vida=[]
for c in range(4):
    cuadro=i_vida.subsurface(54*c,70*0,54,70)
    m_vida.append(cuadro)
#RECORTE LOBO
m_lobo_izq=[]
for c in range(12):
    cuadro=walk1.subsurface(64*c,32*0,64,32)
    m_lobo_izq.append(cuadro)

m_lobo_der=[]
for c in range(12):
    cuadro=walk2.subsurface(64*c,32*0,64,32)
    m_lobo_der.append(cuadro)
#RECORTE BOSS 1
m_boss1_hide=[]
for c in range(6):
    cuadro=boss_hide.subsurface(160*c,144*0,160,144)
    m_boss1_hide.append(cuadro)

m_boss1_attack=[]
for c in range(11):
    cuadro=boss_atack.subsurface(240*c,192*0,240,192)
    m_boss1_attack.append(cuadro)

#RECORTE POCIONES
m_pocionv=[]
for c in range(3):
    cuadro=pocionv_i.subsurface(24*c,24*0,24,24)
    m_pocionv.append(cuadro)

m_pocionx=[]
for c in range(3):
    cuadro=pocionx_i.subsurface(24*c,24*0,24,24)
    m_pocionx.append(cuadro)


#VARIABLES
cruzar_puerta=False
vidas_jugador=0
score_jugador=0
golpear=False
VELOCIDAD=4
milisegundos=0
segundos=0
minutos=0
inicio_juego=False
fin_mapa1=False
fin_mapa2=False
fin_mapa3=False
fin = False
reloj=pygame.time.Clock()

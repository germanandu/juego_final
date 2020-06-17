import pygame
import random

ANCHO=768
ALTO=620
AMARILLO=[255,255,0]
AZUL=[0,0,255]
NEGRO=[0,0,0]
VERDE=[0,255,0]
BLANCO=[255,255,255]

def instruciones(v):
    salir_ins=False
    teclas=pygame.image.load('parcial2/awd.png')
    salir=pygame.image.load('parcial2/volver.png')
    saltar=pygame.image.load('parcial2/Saltar.png')
    izquierda=pygame.image.load('parcial2/Izquierda.png')
    derecha=pygame.image.load('parcial2/Derecha.png')
    espacio=pygame.image.load('parcial2/espacio3.png')
    golpe=pygame.image.load('parcial2/Golpear.png')
    while not salir_ins:
        #Gestion eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    salir_ins=True
        v.blit(fondo_inicio,[0,15])
        v.blit(teclas,[180,80])
        v.blit(saltar,[150,90])
        v.blit(izquierda,[80,280])
        v.blit(derecha,[450,280])
        v.blit(espacio,[200,380])
        v.blit(golpe,[295,360])
        v.blit(salir,[550,500])
        pygame.display.flip()

def Pausa(v):
    salir_ins=False
    pausa=pygame.image.load('img/pausa.png')
    while  not salir_ins:
        #Gestion eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    salir_ins=True
        v.blit(pausa,[200,200])
        pygame.display.flip()


def Pausa2():
    salir_ins=False
    temp=300
    while  not salir_ins:
        #Gestion eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        temp-=1
        if temp < 0:
            salir_ins=True
        

def Felicidades(v):
    salir_ins=False
    felicidades=pygame.image.load('img/felicidades.png')
    nombres=pygame.image.load('img/nombres.png')
    hecho_por=pygame.image.load('img/hecho_por.png')
    while  not salir_ins:
        #Gestion eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    salir_ins=True
        v.blit(felicidades,[20,20])
        v.blit(hecho_por,[250,200])
        v.blit(nombres,[130,290])
        pygame.display.flip()

#IMAGENES
golem=pygame.image.load('img/golem.png')
#inicio
fondo_inicio=pygame.image.load('parcial2/background.png')
fondo_fin=pygame.image.load('parcial2/background2.png')
titulo_inicio=pygame.image.load('parcial2/titulo3.png')
comenzar_inicio=pygame.image.load('parcial2/Comenzar.png')
control_inicio=pygame.image.load('parcial2/Controles.png')
salir_inicio=pygame.image.load('parcial2/Salir.png')
fondo_fin_juego=pygame.image.load('parcial2/finjuego.png')
logo=pygame.image.load('img/logo.png')
#jugador
i_vida=pygame.image.load('img/vida.png')
derecha=pygame.image.load('img/personaje/run.png')
izquierda=pygame.image.load('img/personaje/run2.png')
hide=pygame.image.load('img/personaje/hide.png')
hide2=pygame.image.load('img/personaje/hide2.png')
atack1=pygame.image.load('img/personaje/attack.png')
atack2=pygame.image.load('img/personaje/attack2.png')
bala_j=pygame.image.load('img/bala_j.png')
bala_musgo=pygame.image.load('img/bola.png')
#ave
hide_ave=pygame.image.load('img/ave/Flight.png')
bala_ave=pygame.image.load('img/bala_ave.png')
#lobo
walk1=pygame.image.load('img/lobo/walk1.png')
walk2=pygame.image.load('img/lobo/walk2.png')
#BOSS1
boss_hide=pygame.image.load('img/boss1/hide.png')
boss_atack=pygame.image.load('img/boss1/attack.png')
#BOSS2
boss2_hide=pygame.image.load('img/boss2/hide.png')
boss2_atack=pygame.image.load('img/boss2/attack.png')
#POCION
pocionv_i=pygame.image.load('img/pocionv.png')
pocionx_i=pygame.image.load('img/pocionx.png')
#enemigos 2
enemigos_i=pygame.image.load('img/enemigos2.png')
bala_ojo=pygame.image.load('img/bala_ojo.png')


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
#RECORTE BOSS 2
m_boss2_hide=[]
for c in range(6):
    cuadro=boss2_hide.subsurface(55*c,67*0,55,67)
    m_boss2_hide.append(cuadro)

m_boss2_attack=[]
for c in range(6):
    cuadro=boss2_atack.subsurface(74*c,160*0,74,160)
    m_boss2_attack.append(cuadro)
#RECORTE POCIONES
m_pocionv=[]
for c in range(3):
    cuadro=pocionv_i.subsurface(24*c,24*0,24,24)
    m_pocionv.append(cuadro)

m_pocionx=[]
for c in range(3):
    cuadro=pocionx_i.subsurface(24*c,24*0,24,24)
    m_pocionx.append(cuadro)

#bola
enemigos_m1=[]
for f in range(8):
    fila=[]
    for c in range(12):
        cuadro=enemigos_i.subsurface(32*c,32*f,32,32)
        fila.append(cuadro)
    enemigos_m1.append(fila)

#VARIABLES
cruzar_puerta=False
vidas_jugador=0
score_jugador=0
golpear=False
VELOCIDAD=5
milisegundos=0
segundos=0
minutos=0
inicio_juego=False
fin_mapa1=False
fin_mapa2=False
fin_mapa3=False
fin_level2=False
fin = False
reloj=pygame.time.Clock()


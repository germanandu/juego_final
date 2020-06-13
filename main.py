import pygame
from settings import *
from tilemap import *
from jugador import *
from enemigos import *
from obstaculos import *


if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    #GRUPOS
    jugadores=pygame.sprite.Group()
    aves=pygame.sprite.Group()
    plataformas=pygame.sprite.Group()
    
    #LETRAS
    score=pygame.font.SysFont("Times New Roman, Arial",30)
    tiempo=pygame.font.SysFont("Times New Roman, Arial",30)
    
    #CREACION DEL MAPA
    map = TiledMap('map/mapa2.tmx')
    map_img = map.make_map()
    map_rect = map_img.get_rect()
    camara = Camara(map.width,  map.height)

    for tile_object in map.tmxdata.objects:

        if tile_object.name == 'player':
            j = Jugador([tile_object.x, tile_object.y],m_hide)
            jugadores.add(j)
        if tile_object.name == 'wall':
            p=Plataforma([tile_object.x, tile_object.y],[tile_object.width, tile_object.height])
            plataformas.add(p)
        if tile_object.name == 'ave':
            a=Ave([tile_object.x, tile_object.y],m_ave)
            aves.add(a)
    
    j.plataformas=plataformas

    while not fin:
        #gestion de eventos---------------------------------------------
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fin=True
            #PARA LAS ACCIONES
            j.accion=0
            #SE EVALUA HACIA QUE LADO ESTA MIRANDO
            if j.velx>0 or j.m==m_atack1:
                j.m=m_hide
                j.accion=3
            elif j.velx<0 or j.m==m_atack2:
                j.m=m_hide2
                j.accion=3
            j.velx = 0
            #SE OBTIENE LA TECLA PRESIONADA
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                j.velx=-5
                j.m=m_izquierda
                j.accion=11
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                j.velx=5
                j.m=m_derecha
                j.accion=11
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                j.vely=-10
            if  keys[pygame.K_c]:
                if j.m==m_derecha or j.m==m_hide:
                    j.m=m_atack1
                    j.accion=5
                elif j.m==m_izquierda or j.m==m_hide2:
                    j.m=m_atack2
                    j.accion=5

        #CRONOMETRO
        if milisegundos == 60:
            segundos += 1
            milisegundos=0
        if segundos == 60:
            minutos += 1
            segundos=0
        #REFRESCO
        ventana.fill(NEGRO)
        if segundos>9 and minutos<9:
            msj1='TIME=0'+str(minutos)+':'+str(segundos)
        elif segundos>9 and minutos>9:
            msj1='TIME='+str(minutos)+':'+str(segundos)
        elif segundos<9 and minutos>9:
            msj1='TIME='+str(minutos)+':0'+str(segundos)
        elif segundos<9 and minutos<9:
            msj1='TIME=0'+str(minutos)+':0'+str(segundos)
            
        msj2='SCORE='+str(j.score)
        info1=tiempo.render(msj1,True,BLANCO)
        info2=score.render(msj2,True,BLANCO)
        camara.update(j)
        aves.update()
        jugadores.update()
        ventana.blit(map_img, camara.apply_rect(map_rect))
        ventana.blit(j.image,camara.apply(j))
        for a in aves:
            ventana.blit(a.image,camara.apply(a))
        ventana.blit(info2,[10,5])
        ventana.blit(info1,[850,5])
        pygame.display.flip()
        reloj.tick(60)
        milisegundos += 1
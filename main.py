import pygame
from settings import *
from tilemap import *
from jugador import *
from obstaculos import *


if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    #GRUPOS
    jugadores=pygame.sprite.Group()
    plataformas=pygame.sprite.Group()
    
    
    #CREACION DEL MAPA
    map = TiledMap('map/mapa2.tmx')
    map_img = map.make_map()
    map_rect = map_img.get_rect()
    camara = Camara(map.width,  map.height)

    for tile_object in map.tmxdata.objects:

        if tile_object.name == 'player':
            j = Jugador([tile_object.x, tile_object.y],m4)
            jugadores.add(j)
        if tile_object.name == 'wall':
            p=Plataforma([tile_object.x, tile_object.y],[tile_object.width, tile_object.height])
            plataformas.add(p)
    
    j.plataformas=plataformas

    while not fin:
        #gestion de eventos---------------------------------------------
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fin=True
            j.velx = 0
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                j.velx=-5
                j.dir= 1
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                j.velx=5
                j.dir= 2
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                j.vely=-10
                


        camara.update(j)
        jugadores.update()
        ventana.blit(map_img, camara.apply_rect(map_rect))
        ventana.blit(j.image,camara.apply(j))
        pygame.display.flip()
        reloj.tick(60)
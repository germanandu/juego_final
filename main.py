import pygame
from settings import *
from tilemap import *
from jugador import *
from balas import *
from enemigos import *
from obstaculos import *


if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    #GRUPOS
    jugadores=pygame.sprite.Group()
    aves=pygame.sprite.Group()
    balas_ave=pygame.sprite.Group()
    plataformas=pygame.sprite.Group()
    vacios=pygame.sprite.Group()
    puertas=pygame.sprite.Group()
    lobos=pygame.sprite.Group()
    
    #LETRAS
    score=pygame.font.SysFont("Times New Roman, Arial",30)
    tiempo=pygame.font.SysFont("Times New Roman, Arial",30)
    vida=pygame.font.SysFont("Times New Roman, Arial",30)
    nivel_f=pygame.font.SysFont("Times New Roman, Arial",30)
    
    #CREACION DEL MAPA 1
    map = TiledMap('map/mapa2.tmx')
    map_img = map.make_map()
    map_rect = map_img.get_rect()
    camara = Camara(map.width,  map.height)

    for tile_object in map.tmxdata.objects:

        if tile_object.name == 'player':
            j = Jugador([tile_object.x, tile_object.y],m_hide,m_vida)
            jugadores.add(j)
        if tile_object.name == 'wall':
            p=Plataforma([tile_object.x, tile_object.y],[tile_object.width, tile_object.height])
            plataformas.add(p)
        if tile_object.name == 'puerta':
            p=Puerta([tile_object.x, tile_object.y],[tile_object.width, tile_object.height])
            puertas.add(p)
        if tile_object.name == 'vacio':
            v=Vacio([tile_object.x, tile_object.y],[tile_object.width, tile_object.height])
            vacios.add(v)
        if tile_object.name == 'ave':
            a=Ave([tile_object.x, tile_object.y],m_ave)
            aves.add(a)
        if tile_object.name == 'lobo':
            l=Lobo([tile_object.x, tile_object.y],m_lobo_izq)
            lobos.add(l)
    
    j.plataformas=plataformas

    #MAPA 1 NIVEL 1-----------------------------------------------------------------------------------------------------------
    while not fin and not fin_mapa1:
        #EVENTOS
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fin=True
            #PARA LAS ACCIONES
            golpear=False
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
                j.velx=-VELOCIDAD
                j.m=m_izquierda
                j.accion=11
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                j.velx=VELOCIDAD
                j.m=m_derecha
                j.accion=11
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                j.vely=-10
            if  keys[pygame.K_c]:
                golpear=True
                if j.m==m_derecha or j.m==m_hide:
                    j.m=m_atack1
                    j.accion=5
                elif j.m==m_izquierda or j.m==m_hide2:
                    j.m=m_atack2
                    j.accion=5

        #DAÑO ESPADA
        ls_l=pygame.sprite.spritecollide(j,aves,False)
        for a in ls_l:
            if ((a.rect.top - 80)< j.rect.top) and (j.rect.top < (a.rect.top+80)):
                if golpear:
                    j.score+=1000
                    aves.remove(a)
                    golpear=False
        #CAER AL VACIO
        ls_l=pygame.sprite.spritecollide(j,vacios,False)
        for v in ls_l:
            fin_mapa1=True

        #MOVIMIENTO LOBOS
        for l in lobos:
            if l.bandera == False:
                l.m=m_lobo_izq
                l.velx = -3
                l.temp -=3
                if l.temp < 0:
                    l.bandera=True
            if l.bandera:
                l.m=m_lobo_der
                l.velx = 3
                l.temp +=3
                if l.temp > 100:
                    l.bandera=False


        #PASAR AL OTRO MAPA
        ls_l=pygame.sprite.spritecollide(j,puertas,False)
        for l in ls_l:
            vidas_jugador=j.vida
            score_jugador=j.score
            fin_mapa1=True
            cruzar_puerta=True
            for a in aves:
                aves.remove(a)
            for j in jugadores:
                jugadores.remove(j)
            for p in plataformas:
                plataformas.remove(p)
            for p in puertas:
                puertas.remove(p)
            for v in vacios:
                vacios.remove(v)
        #DISPAROS AVES
        for a in aves:
            if a.temp<0:
                p=a.RetPos()
                b=Bala_ave(p,bala_ave)
                b.vely=5
                balas_ave.add(b)
                a.temp=random.randrange(200)

        #BORRAR BALAS AL IMPACTAR
        for b in balas_ave:
            ls_l=pygame.sprite.spritecollide(b,plataformas,False)
            for l in ls_l:
                balas_ave.remove(b)
            ls_l=pygame.sprite.spritecollide(b,jugadores,False)
            for j in ls_l:
                if j.temp <0:
                    j.vida-=1
                    j.temp=60
                    if j.vida <=0:
                        fin_mapa1=True
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
        
        msj4='NIVEL 1'
        info1=tiempo.render(msj1,True,BLANCO)
        info2=score.render(msj2,True,BLANCO)
        info4=vida.render(msj4,True,BLANCO)
        camara.update(j)
        aves.update()
        lobos.update()
        balas_ave.update()
        jugadores.update()
        ventana.blit(map_img, camara.apply_rect(map_rect))
        ventana.blit(j.image,camara.apply(j))
        for a in aves:
            ventana.blit(a.image,camara.apply(a))
        for b in balas_ave:
            ventana.blit(b.image,camara.apply(b))
        for l in lobos:
            ventana.blit(l.image,camara.apply(l))
        if j.vida==4:
            ventana.blit(j.image_vida,[0,ALTO-70])
            ventana.blit(j.image_vida,[54,ALTO-70])
            ventana.blit(j.image_vida,[109,ALTO-70])
            ventana.blit(j.image_vida,[163,ALTO-70])
        if j.vida==3:
            ventana.blit(j.image_vida,[0,ALTO-70])
            ventana.blit(j.image_vida,[54,ALTO-70])
            ventana.blit(j.image_vida,[109,ALTO-70])
                    
        if j.vida==2:
            ventana.blit(j.image_vida,[0,ALTO-70])
            ventana.blit(j.image_vida,[54,ALTO-70])
                    
        if j.vida==1:
            ventana.blit(j.image_vida,[0,ALTO-70])
        ventana.blit(info2,[10,5])
        ventana.blit(info1,[600,5])
        ventana.blit(info4,[650,590])
        pygame.display.flip()
        reloj.tick(60)
        milisegundos += 1

    #SI CRUZA LA PUERTA
    if cruzar_puerta:
        cruzar_puerta=False
        #CREACION DEL MAPA 2
        map = TiledMap('map/mapa_caida1.tmx')
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
            if tile_object.name == 'puerta':
                p=Puerta([tile_object.x, tile_object.y],[tile_object.width, tile_object.height])
                puertas.add(p)
            if tile_object.name == 'vacio':
                v=Vacio([tile_object.x, tile_object.y],[tile_object.width, tile_object.height])
                vacios.add(v)
            if tile_object.name == 'ave':
                a=Ave([tile_object.x, tile_object.y],m_ave)
                aves.add(a)
        
        j.plataformas=plataformas
        j.vida=vidas_jugador
        j.score=score_jugador

        #MAPA 2 NIVEL 1-----------------------------------------------------------------------------------------------------------
        
        while not fin and not fin_mapa2:
            #EVENTOS
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    fin=True
                #PARA LAS ACCIONES
                golpear=False
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
                    j.velx=-VELOCIDAD
                    j.m=m_izquierda
                    j.accion=11
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    j.velx=VELOCIDAD
                    j.m=m_derecha
                    j.accion=11
                if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                    j.vely=-10
                if  keys[pygame.K_c]:
                    golpear=True
                    if j.m==m_derecha or j.m==m_hide:
                        j.m=m_atack1
                        j.accion=5
                    elif j.m==m_izquierda or j.m==m_hide2:
                        j.m=m_atack2
                        j.accion=5

            #DAÑO ESPADA
            ls_l=pygame.sprite.spritecollide(j,aves,False)
            for a in ls_l:
                if ((a.rect.top - 80)< j.rect.top) and (j.rect.top < (a.rect.top+80)):
                    if golpear:
                        j.score+=1000
                        aves.remove(a)
                        golpear=False
            
            #PASAR AL OTRO MAPA
            ls_l=pygame.sprite.spritecollide(j,puertas,False)
            for l in ls_l:
                vidas_jugador=j.vida
                score_jugador=j.score
                fin_mapa2=True
                cruzar_puerta=True
                for a in aves:
                    aves.remove(a)
                for j in jugadores:
                    jugadores.remove(j)
                for p in plataformas:
                    plataformas.remove(p)
                for p in puertas:
                    puertas.remove(p)
                for v in vacios:
                    vacios.remove(v)
            
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
            msj4='NIVEL 1'
            info1=tiempo.render(msj1,True,BLANCO)
            info2=score.render(msj2,True,BLANCO)
            info4=vida.render(msj4,True,BLANCO)
            camara.update(j)
            aves.update()
            balas_ave.update()
            jugadores.update()
            ventana.blit(map_img, camara.apply_rect(map_rect))
            ventana.blit(j.image,camara.apply(j))
            for a in aves:
                ventana.blit(a.image,camara.apply(a))
            for b in balas_ave:
                ventana.blit(b.image,camara.apply(b))
            if j.vida==4:
                ventana.blit(j.image_vida,[0,ALTO-70])
                ventana.blit(j.image_vida,[54,ALTO-70])
                ventana.blit(j.image_vida,[109,ALTO-70])
                ventana.blit(j.image_vida,[163,ALTO-70])
            if j.vida==3:
                ventana.blit(j.image_vida,[0,ALTO-70])
                ventana.blit(j.image_vida,[54,ALTO-70])
                ventana.blit(j.image_vida,[109,ALTO-70])
                        
            if j.vida==2:
                ventana.blit(j.image_vida,[0,ALTO-70])
                ventana.blit(j.image_vida,[54,ALTO-70])
                        
            if j.vida==1:
                ventana.blit(j.image_vida,[0,ALTO-70])
            ventana.blit(info2,[10,5])
            ventana.blit(info1,[600,5])
            ventana.blit(info4,[650,590])
            pygame.display.flip()
            reloj.tick(60)
            milisegundos += 1

        #SI CRUZA LA PUERTA
        if cruzar_puerta:
            cruzar_puerta=False
            #CREACION DEL MAPA 3
            map = TiledMap('map/mapa_boss1.tmx')
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
                if tile_object.name == 'vacio':
                    v=Vacio([tile_object.x, tile_object.y],[tile_object.width, tile_object.height])
                    vacios.add(v)
                if tile_object.name == 'ave':
                    a=Ave([tile_object.x, tile_object.y],m_ave)
                    aves.add(a)
            
            j.plataformas=plataformas
            j.vida=vidas_jugador
            j.score=score_jugador

            #MAPA 3 NIVEL 1-----------------------------------------------------------------------------------------------------------
            
            while not fin and not fin_mapa3:
                #EVENTOS
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        fin=True
                    #PARA LAS ACCIONES
                    golpear=False
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
                        j.velx=-VELOCIDAD
                        j.m=m_izquierda
                        j.accion=11
                    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                        j.velx=VELOCIDAD
                        j.m=m_derecha
                        j.accion=11
                    if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                        j.vely=-10
                    if  keys[pygame.K_c]:
                        golpear=True
                        if j.m==m_derecha or j.m==m_hide:
                            j.m=m_atack1
                            j.accion=5
                        elif j.m==m_izquierda or j.m==m_hide2:
                            j.m=m_atack2
                            j.accion=5

                #DAÑO ESPADA
                ls_l=pygame.sprite.spritecollide(j,aves,False)
                for a in ls_l:
                    if ((a.rect.top - 80)< j.rect.top) and (j.rect.top < (a.rect.top+80)):
                        if golpear:
                            j.score+=1000
                            aves.remove(a)
                            golpear=False
                
                #PASAR AL OTRO MAPA
                ls_l=pygame.sprite.spritecollide(j,puertas,False)
                for l in ls_l:
                    vidas_jugador=j.vida
                    score_jugador=j.score
                    fin_mapa3=True
                    cruzar_puerta=True
                    for a in aves:
                        aves.remove(a)
                    for j in jugadores:
                        jugadores.remove(j)
                    for p in plataformas:
                        plataformas.remove(p)
                    for p in puertas:
                        puertas.remove(p)
                    for v in vacios:
                        vacios.remove(v)
                
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
                
                msj4='NIVEL 1'
                info1=tiempo.render(msj1,True,BLANCO)
                info2=score.render(msj2,True,BLANCO)
                info4=vida.render(msj4,True,BLANCO)
                camara.update(j)
                aves.update()
                balas_ave.update()
                jugadores.update()
                ventana.blit(map_img, camara.apply_rect(map_rect))
                ventana.blit(j.image,camara.apply(j))
                for a in aves:
                    ventana.blit(a.image,camara.apply(a))
                for b in balas_ave:
                    ventana.blit(b.image,camara.apply(b))
                if j.vida==4:
                    ventana.blit(j.image_vida,[0,ALTO-70])
                    ventana.blit(j.image_vida,[54,ALTO-70])
                    ventana.blit(j.image_vida,[109,ALTO-70])
                    ventana.blit(j.image_vida,[163,ALTO-70])
                if j.vida==3:
                    ventana.blit(j.image_vida,[0,ALTO-70])
                    ventana.blit(j.image_vida,[54,ALTO-70])
                    ventana.blit(j.image_vida,[109,ALTO-70])
                    
                if j.vida==2:
                    ventana.blit(j.image_vida,[0,ALTO-70])
                    ventana.blit(j.image_vida,[54,ALTO-70])
                    
                if j.vida==1:
                    ventana.blit(j.image_vida,[0,ALTO-70])
                    
                ventana.blit(info2,[10,5])
                ventana.blit(info1,[600,5])
                ventana.blit(info4,[650,590])
                pygame.display.flip()
                reloj.tick(60)
                milisegundos += 1
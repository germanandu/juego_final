import pygame
from settings import *
from tilemap import *
from jugador import *
from balas import *
from enemigos import *
from obstaculos import *
from modificadores import *


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
    lineas=pygame.sprite.Group()
    bosses=pygame.sprite.Group()
    pociones=pygame.sprite.Group()
    ojos=pygame.sprite.Group()
    musgos=pygame.sprite.Group()
    #MUSICA
    ambiente_music=pygame.mixer.Sound('music/ambiente.wav')
    ambiente2_music=pygame.mixer.Sound('music/ambiente2.wav')
    slash=pygame.mixer.Sound('music/slash.wav')
    fire_ball=pygame.mixer.Sound('music/fireball.wav')
    pocionv_sound=pygame.mixer.Sound('music/pocionv.wav')
    pocionx_sound=pygame.mixer.Sound('music/pocionx.wav')
    boss1_fire_sound=pygame.mixer.Sound('music/boss1_fire.wav')
    #boss2_fire_sound=pygame.mixer.Sound('music/boss2_fire.wav')
    hit_sound=pygame.mixer.Sound('music/hit.wav')
    boss_win=pygame.mixer.Sound('music/nivel2.wav')
    boss_music=pygame.mixer.Sound('music/boss.wav')
    boss2_music=pygame.mixer.Sound('music/boss2.wav')
    congratulations=pygame.mixer.Sound('music/congratulations.wav')
    kill_enemy=pygame.mixer.Sound('music/kill_enemy.wav')
    inicio_music=pygame.mixer.Sound('music/inicio.wav')
    gameover_music=pygame.mixer.Sound('music/gameover.wav')
    #intro_sound=pygame.mixer.Sound('music/intro.mp3')
    
    #LETRAS
    score=pygame.font.SysFont("Times New Roman, Arial",30)
    tiempo=pygame.font.SysFont("Times New Roman, Arial",30)
    vida=pygame.font.SysFont("Times New Roman, Arial",30)
    nivel_f=pygame.font.SysFont("Times New Roman, Arial",30)
    boss_f=pygame.font.SysFont("Times New Roman, Arial",20)
    
    inicio_music.play(-1)
    #INICIO
    while (not fin) and (not inicio_juego):
        #Gestion eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    inicio_juego=True
                if event.key==pygame.K_2:
                    instruciones(ventana)
                if event.key==pygame.K_3:
                    inicio_juego=True
                    fin=True
        ventana.blit(fondo_inicio,[0,15])
        ventana.blit(titulo_inicio,[100,30])
        ventana.blit(comenzar_inicio,[250,280])
        ventana.blit(control_inicio,[260,350])
        ventana.blit(salir_inicio,[290,420])
        ventana.blit(logo,[ANCHO -201,ALTO -201])
        pygame.display.flip()

    inicio_music.stop()
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
        if tile_object.name == 'linea':
            l=Linea([tile_object.x, tile_object.y],[tile_object.width, tile_object.height])
            lineas.add(l)
        if tile_object.name == 'vacio':
            v=Vacio([tile_object.x, tile_object.y],[tile_object.width, tile_object.height])
            vacios.add(v)
        if tile_object.name == 'ave':
            a=Ave([tile_object.x, tile_object.y],m_ave)
            aves.add(a)
        if tile_object.name == 'lobo':
            l=Lobo([tile_object.x, tile_object.y],m_lobo_izq)
            l.velx = 3
            lobos.add(l)
        if tile_object.name == 'pocionv':
            p=Pocion([tile_object.x, tile_object.y])
            pociones.add(p)
    
    j.plataformas=plataformas
    ambiente_music.set_volume(0.1)
    ambiente_music.play(-1)
    
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
                j.con=0
                j.velx=-VELOCIDAD
                j.m=m_izquierda
                j.accion=11
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                j.con=0
                j.velx=VELOCIDAD
                j.m=m_derecha
                j.accion=11
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                if j.salto < 2:
                    j.con=0
                    j.vely=-10
                    j.salto+=1
            if  keys[pygame.K_SPACE]:
                slash.play()
                j.con=0
                golpear=True
                if j.m==m_derecha or j.m==m_hide:
                    j.m=m_atack1
                    j.accion=5
                elif j.m==m_izquierda or j.m==m_hide2:
                    j.m=m_atack2
                    j.accion=5
            if keys[pygame.K_p]:
                ambiente_music.stop()
                Pausa(ventana)
                ambiente_music.play(-1)
                
        #VIDA EXTRA
        ls_l=pygame.sprite.spritecollide(j,pociones,False)
        for p in ls_l:
            if p.tipo==1:
                if j.temp < 0:
                    pocionv_sound.play()
                    j.vida += 1
                    if j.vida > 4:
                        j.vida=4
                    pociones.remove(p)
        #DAÑO ESPADA AVES
        ls_l=pygame.sprite.spritecollide(j,aves,False)
        for a in ls_l:
            if ((a.rect.top - 80)< j.rect.top) and (j.rect.top < (a.rect.top+80)):
                if golpear:
                    kill_enemy.play()
                    j.score+=1000
                    aves.remove(a)
                    golpear=False

        #CAER AL VACIO
        ls_l=pygame.sprite.spritecollide(j,vacios,False)
        for v in ls_l:
            fin_mapa1=True

        #DAÑO ESPADA LOBOS
        ls_l=pygame.sprite.spritecollide(j,lobos,False)
        for l in ls_l:
            if golpear:
                j.score+=1000
                kill_enemy.play()
                lobos.remove(l)
                golpear=False
            else:
                if j.temp < 0:
                    j.vida-=1
                    j.temp=60
                    hit_sound.play()
                    if j.vida <=0:
                        fin_mapa1=True

        #MOVIMIENTO LOBOS
        for l in lobos:
            ls_l=pygame.sprite.spritecollide(l,lineas,False)
            for ln in ls_l:
                l.velx = l.velx * (-1)
                if l.velx > 0:
                    l.m=m_lobo_der
                else:
                    l.m=m_lobo_izq



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
            for l in lobos:
                lobos.remove(l)
            for l in lineas:
                lineas.remove(l)
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
                    hit_sound.play()
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
            msj1='TIME 0'+str(minutos)+':'+str(segundos)
        elif segundos>9 and minutos>9:
            msj1='TIME '+str(minutos)+':'+str(segundos)
        elif segundos<9 and minutos>9:
            msj1='TIME '+str(minutos)+':0'+str(segundos)
        elif segundos<9 and minutos<9:
            msj1='TIME 0'+str(minutos)+':0'+str(segundos)
            
        msj2='SCORE '+str(j.score)
        
        msj4='NIVEL 1'
        info1=tiempo.render(msj1,True,BLANCO)
        info2=score.render(msj2,True,BLANCO)
        info4=vida.render(msj4,True,BLANCO)
        #UPDATES
        camara.update(j)
        aves.update()
        lobos.update()
        balas_ave.update()
        jugadores.update()
        pociones.update()
        #IMPRIMIR EN PANTALLA
        ventana.blit(map_img, camara.apply_rect(map_rect))
        ventana.blit(j.image,camara.apply(j))
        for a in aves:
            ventana.blit(a.image,camara.apply(a))
        for b in balas_ave:
            ventana.blit(b.image,camara.apply(b))
        for l in lobos:
            ventana.blit(l.image,camara.apply(l))
        for p in pociones:
            ventana.blit(p.image,camara.apply(p))
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
            if tile_object.name == 'linea':
                l=Linea([tile_object.x, tile_object.y],[tile_object.width, tile_object.height])
                lineas.add(l)
            if tile_object.name == 'lobo':
                l=Lobo([tile_object.x, tile_object.y],m_lobo_izq)
                l.velx = -3
                lobos.add(l)
            if tile_object.name == 'pocionv':
                p=Pocion([tile_object.x, tile_object.y])
                pociones.add(p)
        
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
                    j.con=0
                    j.velx=-VELOCIDAD
                    j.m=m_izquierda
                    j.accion=11
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    j.con=0
                    j.velx=VELOCIDAD
                    j.m=m_derecha
                    j.accion=11
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    if j.salto < 2:
                        j.con=0
                        j.vely=-10
                        j.salto+=1
                if  keys[pygame.K_SPACE]:
                    slash.play()
                    j.con=0
                    golpear=True
                    if j.m==m_derecha or j.m==m_hide:
                        j.m=m_atack1
                        j.accion=5
                    elif j.m==m_izquierda or j.m==m_hide2:
                        j.m=m_atack2
                        j.accion=5
                if keys[pygame.K_p]:
                    ambiente_music.stop()
                    Pausa(ventana)
                    ambiente_music.play(-1)

            #VIDA EXTRA
            ls_l=pygame.sprite.spritecollide(j,pociones,False)
            for p in ls_l:
                if p.tipo==1:
                    if j.temp < 0:
                        pocionv_sound.play()
                        j.vida += 1
                        if j.vida > 4:
                            j.vida=4
                        pociones.remove(p)
            #DISPAROS AVES
            for a in aves:
                if a.temp<0:
                    p=a.RetPos()
                    b=Bala_ave(p,bala_ave)
                    b.vely=5
                    balas_ave.add(b)
                    a.temp=random.randrange(200)
            #DAÑO ESPADA
            ls_l=pygame.sprite.spritecollide(j,aves,False)
            for a in ls_l:
                if ((a.rect.top - 80)< j.rect.top) and (j.rect.top < (a.rect.top+80)):
                    if golpear:
                        kill_enemy.play()
                        j.score+=1000
                        aves.remove(a)
                        golpear=False
            
            #DAÑO ESPADA LOBOS
            ls_l=pygame.sprite.spritecollide(j,lobos,False)
            for l in ls_l:
                if golpear:
                    kill_enemy.play()
                    j.score+=1000
                    lobos.remove(l)
                    golpear=False
                else:
                    if j.temp < 0:
                        j.vida-=1
                        j.temp=60
                        hit_sound.play()
                        if j.vida <=0:
                            fin_mapa2=True
                        
            #MOVIMIENTO LOBOS
            for l in lobos:
                ls_l=pygame.sprite.spritecollide(l,lineas,False)
                for ln in ls_l:
                    l.velx = l.velx * (-1)
                    if l.velx > 0:
                        l.m=m_lobo_der
                    else:
                        l.m=m_lobo_izq
                
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
                for l in lobos:
                    lobos.remove(l)
                for l in lineas:
                    lineas.remove(l)
            #BORRAR BALAS AL IMPACTAR
            for b in balas_ave:
                ls_l=pygame.sprite.spritecollide(b,plataformas,False)
                for l in ls_l:
                    balas_ave.remove(b)
                ls_l=pygame.sprite.spritecollide(b,jugadores,False)
                for j in ls_l:
                    if j.temp <0:
                        j.vida-=1
                        hit_sound.play()
                        j.temp=60
                        if j.vida <=0:
                            fin_mapa2=True
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
                msj1='TIME 0'+str(minutos)+':'+str(segundos)
            elif segundos>9 and minutos>9:
                msj1='TIME '+str(minutos)+':'+str(segundos)
            elif segundos<9 and minutos>9:
                msj1='TIME '+str(minutos)+':0'+str(segundos)
            elif segundos<9 and minutos<9:
                msj1='TIME 0'+str(minutos)+':0'+str(segundos)
                
            msj2='SCORE '+str(j.score)
            msj4='NIVEL 1'
            info1=tiempo.render(msj1,True,BLANCO)
            info2=score.render(msj2,True,BLANCO)
            info4=vida.render(msj4,True,BLANCO)
            camara.update(j)
            lobos.update()
            aves.update()
            pociones.update()
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
            for p in pociones:
                ventana.blit(p.image,camara.apply(p))
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
                if tile_object.name == 'boss1':
                    b=Boss1([tile_object.x, tile_object.y],m_boss1_hide)
                    bosses.add(b)
            
            j.plataformas=plataformas
            j.vida=vidas_jugador
            j.score=score_jugador

            #MAPA 3 NIVEL 1-----------------------------------------------------------------------------------------------------------
            ambiente_music.stop()
            boss_music.play(-1)
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
                        j.con=0
                        j.velx=-VELOCIDAD
                        j.m=m_izquierda
                        j.accion=11
                    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                        j.con=0
                        j.velx=VELOCIDAD
                        j.m=m_derecha
                        j.accion=11
                    if keys[pygame.K_UP] or keys[pygame.K_w]:
                        if j.salto < 2:
                            j.con=0
                            j.vely=-10
                            j.salto+=1
                    if  keys[pygame.K_SPACE]:
                        slash.play()
                        j.con=0
                        golpear=True
                        if j.m==m_derecha or j.m==m_hide:
                            j.m=m_atack1
                            j.accion=5
                        elif j.m==m_izquierda or j.m==m_hide2:
                            j.m=m_atack2
                            j.accion=5
                    if keys[pygame.K_p]:
                        Pausa(ventana)

                #DAÑO ESPADA
                ls_l=pygame.sprite.spritecollide(j,bosses,False)
                for b in ls_l:
                    if golpear:
                        if j.temp <0 :
                            b.vida -= 1
                            j.temp= 30
                            kill_enemy.play()
                            if b.vida <= 0:
                                boss_music.stop()
                                congratulations.play()
                                fin_mapa3=True
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
                                for l in lobos:
                                    lobos.remove(l)
                                for l in lineas:
                                    lineas.remove(l)
                                for b in bosses:
                                    bosses.remove(l)
                                for p in pociones:
                                    pociones.remove(p)

                    if b.accion==10:
                        if j.temp <0 :
                            j.vida -= 1
                            hit_sound.play()
                            j.temp= 30
                            if j.vida <= 0:
                                boss_music.stop()
                                fin_mapa3=True

                        
                #MOVIMIENTO BOSS
                if b.temp < 0:
                    if b.accion == 5:
                        b.con=0
                        b.m= m_boss1_attack
                        b.accion=10
                        b.temp =100
                        b.velx =- 3
                        boss1_fire_sound.play()
                        
                    elif b.accion == 10:
                        b.con=0
                        b.m= m_boss1_hide
                        b.accion=5
                        b.temp =100
                        b.velx =  3
                
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
                    msj1='TIME 0'+str(minutos)+':'+str(segundos)
                elif segundos>9 and minutos>9:
                    msj1='TIME '+str(minutos)+':'+str(segundos)
                elif segundos<9 and minutos>9:
                    msj1='TIME '+str(minutos)+':0'+str(segundos)
                elif segundos<9 and minutos<9:
                    msj1='TIME 0'+str(minutos)+':0'+str(segundos)
                    
                msj2='SCORE '+str(j.score)
                
                msj4='NIVEL 1'
                msj3='VIDAS '+str(b.vida)
                info1=tiempo.render(msj1,True,BLANCO)
                info2=score.render(msj2,True,BLANCO)
                info4=vida.render(msj4,True,BLANCO)
                info3=boss_f.render(msj3,True,BLANCO)
                camara.update(j)
                bosses.update()
                aves.update()
                balas_ave.update()
                jugadores.update()
                ventana.blit(map_img, camara.apply_rect(map_rect))
                ventana.blit(j.image,camara.apply(j))
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
                ventana.blit(info3,[b.rect.x+33,b.rect.y+20])
                ventana.blit(info4,[650,590])
                pygame.display.flip()
                reloj.tick(60)
                milisegundos += 1

            #SI CRUZA LA PUERTA
        if cruzar_puerta:
            cruzar_puerta=False
            #CREACION DEL MAPA 4
            map = TiledMap('map/mapa1_nivel2.tmx')
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
                if tile_object.name == 'ojo':
                    o=Ojo([tile_object.x, tile_object.y])
                    o.velx = -3
                    ojos.add(o)
                if tile_object.name == 'linea':
                    l=Linea([tile_object.x, tile_object.y],[tile_object.width, tile_object.height])
                    lineas.add(l)
                if tile_object.name == 'lobo':
                    l=Lobo([tile_object.x, tile_object.y],m_lobo_izq)
                    l.velx = -3
                    lobos.add(l)
                if tile_object.name == 'pocionv':
                    p=Pocion([tile_object.x, tile_object.y])
                    pociones.add(p)
                if tile_object.name == 'pocionx':
                    p=Pocion([tile_object.x, tile_object.y],m_pocionx)
                    p.tipo=2
                    pociones.add(p)
            
            j.plataformas=plataformas

            #MAPA 1 NIVEL 2-----------------------------------------------------------------------------------------------------------
            ambiente2_music.play(-1)
            while not fin and not fin_level2:
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
                        j.con=0
                        j.velx=-VELOCIDAD
                        j.m=m_izquierda
                        j.accion=11
                    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                        j.con=0
                        j.velx=VELOCIDAD
                        j.m=m_derecha
                        j.accion=11
                    if keys[pygame.K_UP] or keys[pygame.K_w]:
                        if j.salto < 2:
                            j.con=0
                            j.vely=-10
                            j.salto+=1
                    if  keys[pygame.K_SPACE]:
                        slash.play()
                        j.con=0
                        golpear=True
                        if j.m==m_derecha or j.m==m_hide:
                            j.m=m_atack1
                            j.accion=5
                        elif j.m==m_izquierda or j.m==m_hide2:
                            j.m=m_atack2
                            j.accion=5
                        if j.pocionx:
                            p=j.RetPos()
                            b=Bala_ave(p,bala_j)
                            if j.m==m_atack1:
                                b.velx=5
                            elif j.m==m_atack2:
                                b.velx= -5
                            b.tipo=2
                            balas_ave.add(b)
                    if keys[pygame.K_p]:
                        ambiente2_music.stop()
                        Pausa(ventana)
                        ambiente2_music.play()

                 #VIDA EXTRA O BALAS
                ls_l=pygame.sprite.spritecollide(j,pociones,False)
                for p in ls_l:
                    if p.tipo==1:
                        if j.temp < 0:
                            pocionv_sound.play()
                            j.vida += 1
                            if j.vida > 4:
                                j.vida=4
                            pociones.remove(p)
                    else:
                        pocionx_sound.play()
                        j.pocionx=True
                        pociones.remove(p)
                #DAÑO ESPADA
                ls_l=pygame.sprite.spritecollide(j,ojos,False)
                for o in ls_l:
                    if golpear:
                        kill_enemy.play()
                        j.score+=1000
                        ojos.remove(o)
                        golpear=False
                #MOVIMIENTO OJOS
                for o in ojos:
                    ls_l=pygame.sprite.spritecollide(o,lineas,False)
                    for l in ls_l:
                        o.velx= o.velx * (-1)
                        if o.velx > 0:
                            o.dir = 2
                        elif o.velx < 0:
                            o.dir = 1
                    if o.temp < 0:
                        p=o.RetPos()
                        b=Bala_ave(p,bala_ojo)
                        b.vely=3
                        balas_ave.add(b)
                        o.temp=random.randrange(100)

                #CAER AL VACIO
                ls_l=pygame.sprite.spritecollide(j,vacios,False)
                for v in ls_l:
                    ambiente2_music.stop()
                    fin_level2=True
                #PASAR AL OTRO MAPA
                ls_l=pygame.sprite.spritecollide(j,puertas,False)
                for l in ls_l:
                    vidas_jugador=j.vida
                    score_jugador=j.score
                    fin_level2=True
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
                    for l in lobos:
                        lobos.remove(l)
                    for l in lineas:
                        lineas.remove(l)
                    for o in ojos:
                        ojos.remove(o)
                #BORRAR BALAS AL IMPACTAR
                for b in balas_ave:
                    ls_l=pygame.sprite.spritecollide(b,ojos,False)
                    for o in ls_l:
                        if b.tipo==2:
                            ojos.remove(o)
                            kill_enemy.play()
                            balas_ave.remove(b)
                    ls_l=pygame.sprite.spritecollide(b,plataformas,False)
                    for l in ls_l:
                        balas_ave.remove(b)
                    ls_l=pygame.sprite.spritecollide(b,jugadores,False)
                    for j in ls_l:
                        if b.tipo==1:
                            if j.temp <0:
                                hit_sound.play()
                                j.pocionx=False
                                j.vida-=1
                                j.temp=60
                                if j.vida <=0:
                                    ambiente2_music.stop()
                                    fin_level2=True
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
                    msj1='TIME 0'+str(minutos)+':'+str(segundos)
                elif segundos>9 and minutos>9:
                    msj1='TIME '+str(minutos)+':'+str(segundos)
                elif segundos<9 and minutos>9:
                    msj1='TIME '+str(minutos)+':0'+str(segundos)
                elif segundos<9 and minutos<9:
                    msj1='TIME 0'+str(minutos)+':0'+str(segundos)
                    
                msj2='SCORE '+str(j.score)
                msj4='NIVEL 2'
                
                info1=tiempo.render(msj1,True,BLANCO)
                info2=score.render(msj2,True,BLANCO)
                info4=vida.render(msj4,True,BLANCO)
                camara.update(j)
                balas_ave.update()
                jugadores.update()
                pociones.update()
                ojos.update()
                ventana.blit(map_img, camara.apply_rect(map_rect))
                ventana.blit(j.image,camara.apply(j))
                for o in ojos:
                    ventana.blit(o.image,camara.apply(o))
                for b in balas_ave:
                    ventana.blit(b.image,camara.apply(b))
                for p in pociones:
                    ventana.blit(p.image,camara.apply(p))

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
            fin_level2=False
            cruzar_puerta=False
            #CREACION DEL MAPA 4
            map = TiledMap('map/mapa_caida2.tmx')
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
                if tile_object.name == 'ojo':
                    o=Ojo([tile_object.x, tile_object.y])
                    o.velx = -3
                    ojos.add(o)
                if tile_object.name == 'musgo':
                    m=Musgo([tile_object.x, tile_object.y])
                    musgos.add(m)
                if tile_object.name == 'linea':
                    l=Linea([tile_object.x, tile_object.y],[tile_object.width, tile_object.height])
                    lineas.add(l)
                if tile_object.name == 'lobo':
                    l=Lobo([tile_object.x, tile_object.y],m_lobo_izq)
                    l.velx = -3
                    lobos.add(l)
                if tile_object.name == 'pocionv':
                    p=Pocion([tile_object.x, tile_object.y])
                    pociones.add(p)
                if tile_object.name == 'pocionx':
                    p=Pocion([tile_object.x, tile_object.y],m_pocionx)
                    p.tipo=2
                    pociones.add(p)
            
            j.plataformas=plataformas
            j.vida=vidas_jugador
            j.score=score_jugador

            #MAPA 2 NIVEL 2-----------------------------------------------------------------------------------------------------------
            
            while not fin and not fin_level2:
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
                        j.con=0
                        j.velx=-VELOCIDAD
                        j.m=m_izquierda
                        j.accion=11
                    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                        j.con=0
                        j.velx=VELOCIDAD
                        j.m=m_derecha
                        j.accion=11
                    if keys[pygame.K_UP] or keys[pygame.K_w]:
                        if j.salto < 2:
                            j.con=0
                            j.vely=-10
                            j.salto+=1
                    if  keys[pygame.K_SPACE]:
                        slash.play()
                        j.con=0
                        golpear=True
                        if j.m==m_derecha or j.m==m_hide:
                            j.m=m_atack1
                            j.accion=5
                        elif j.m==m_izquierda or j.m==m_hide2:
                            j.m=m_atack2
                            j.accion=5
                        if j.pocionx:
                            fire_ball.play()
                            p=j.RetPos()
                            b=Bala_ave(p,bala_j)
                            if j.m==m_atack1:
                                b.velx=5
                            elif j.m==m_atack2:
                                b.velx= -5
                                b.rect.x -=96
                            b.tipo=2
                            balas_ave.add(b)
                    if keys[pygame.K_p]:
                        ambiente2_music.stop()
                        Pausa(ventana)
                        ambiente2_music.play()

                 #VIDA EXTRA O BALAS
                ls_l=pygame.sprite.spritecollide(j,pociones,False)
                for p in ls_l:
                    if p.tipo==1:
                        if j.temp < 0:
                            pocionv_sound.play()
                            j.vida += 1
                            if j.vida > 4:
                                j.vida=4
                            pociones.remove(p)
                    else:
                        pocionx_sound.play()
                        j.pocionx=True
                        pociones.remove(p)
                #DAÑO ESPADA
                ls_l=pygame.sprite.spritecollide(j,ojos,False)
                for o in ls_l:
                    if golpear:
                        kill_enemy.play()
                        j.score+=1000
                        ojos.remove(o)
                        golpear=False
                #DAÑO ESPADA
                ls_l=pygame.sprite.spritecollide(j,musgos,False)
                for m in ls_l:
                    if golpear:
                        kill_enemy.play()
                        j.score+=1000
                        musgos.remove(m)
                        golpear=False
                #MOVIMIENTO OJOS
                for o in ojos:
                    ls_l=pygame.sprite.spritecollide(o,lineas,False)
                    for l in ls_l:
                        o.velx= o.velx * (-1)
                        if o.velx > 0:
                            o.dir = 2
                        elif o.velx < 0:
                            o.dir = 1
                    if o.temp < 0:
                        p=o.RetPos()
                        b=Bala_ave(p,bala_ojo)
                        b.vely=3
                        balas_ave.add(b)
                        o.temp=random.randrange(100)
                #DISPAROS MUSGOS
                for m in musgos:
                    if m.temp < 0:
                        p=m.RetPos()
                        b=Bala_ave(p,bala_musgo)
                        b.velx=3
                        balas_ave.add(b)
                        m.temp=60
                #CAER AL VACIO
                ls_l=pygame.sprite.spritecollide(j,vacios,False)
                for v in ls_l:
                    fin_level2=True
                #PASAR AL OTRO MAPA
                ls_l=pygame.sprite.spritecollide(j,puertas,False)
                for l in ls_l:
                    ambiente2_music.stop()
                    vidas_jugador=j.vida
                    score_jugador=j.score
                    fin_level2=True
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
                    for l in lobos:
                        lobos.remove(l)
                    for l in lineas:
                        lineas.remove(l)
                    for o in ojos:
                        ojos.remove(o)
                    for p in pociones:
                        pociones.remove(p)
                    for b in balas_ave:
                        balas_ave.remove(b)
                    for b in bosses:
                        bosses.remove(b)
                #BORRAR BALAS AL IMPACTAR
                for b in balas_ave:
                    ls_l=pygame.sprite.spritecollide(b,ojos,False)
                    for o in ls_l:
                        if b.tipo==2:
                            ojos.remove(o)
                            kill_enemy.play()
                            balas_ave.remove(b)
                    ls_l=pygame.sprite.spritecollide(b,plataformas,False)
                    for l in ls_l:
                        balas_ave.remove(b)
                    ls_l=pygame.sprite.spritecollide(b,jugadores,False)
                    for j in ls_l:
                        if b.tipo==1:
                            if j.temp <0:
                                hit_sound.play()
                                j.pocionx=False
                                j.vida-=1
                                j.temp=60
                                if j.vida <=0:
                                    ambiente2_music.stop()
                                    fin_level2=True
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
                    msj1='TIME 0'+str(minutos)+':'+str(segundos)
                elif segundos>9 and minutos>9:
                    msj1='TIME '+str(minutos)+':'+str(segundos)
                elif segundos<9 and minutos>9:
                    msj1='TIME '+str(minutos)+':0'+str(segundos)
                elif segundos<9 and minutos<9:
                    msj1='TIME 0'+str(minutos)+':0'+str(segundos)
                    
                msj2='SCORE '+str(j.score)
                msj4='NIVEL 2'
                
                info1=tiempo.render(msj1,True,BLANCO)
                info2=score.render(msj2,True,BLANCO)
                info4=vida.render(msj4,True,BLANCO)
                #UPDATE
                camara.update(j)
                balas_ave.update()
                jugadores.update()
                pociones.update()
                ojos.update()
                musgos.update()
                #IMPRESION
                ventana.blit(map_img, camara.apply_rect(map_rect))
                ventana.blit(j.image,camara.apply(j))
                for o in ojos:
                    ventana.blit(o.image,camara.apply(o))
                for b in balas_ave:
                    ventana.blit(b.image,camara.apply(b))
                for p in pociones:
                    ventana.blit(p.image,camara.apply(p))
                for m in musgos:
                    ventana.blit(m.image,camara.apply(m))

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
            fin_level2=False
            cruzar_puerta=False
            #CREACION DEL MAPA 4
            map = TiledMap('map/mapa_boss2.tmx')
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
                if tile_object.name == 'ojo':
                    o=Ojo([tile_object.x, tile_object.y])
                    o.velx = -3
                    ojos.add(o)
                if tile_object.name == 'linea':
                    l=Linea([tile_object.x, tile_object.y],[tile_object.width, tile_object.height])
                    lineas.add(l)
                if tile_object.name == 'lobo':
                    l=Lobo([tile_object.x, tile_object.y],m_lobo_izq)
                    l.velx = -3
                    lobos.add(l)
                if tile_object.name == 'pocionv':
                    p=Pocion([tile_object.x, tile_object.y])
                    pociones.add(p)
                if tile_object.name == 'pocionx':
                    p=Pocion([tile_object.x, tile_object.y],m_pocionx)
                    p.tipo=2
                    pociones.add(p)
                if tile_object.name == 'boss2':
                    bss=Boss2([tile_object.x, tile_object.y],m_boss2_hide)
                    bosses.add(bss)
            
            j.plataformas=plataformas
            j.vida=vidas_jugador
            j.score=score_jugador

            #MAPA 3 NIVEL 2-----------------------------------------------------------------------------------------------------------
            boss2_music.play()
            while not fin and not fin_level2:
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
                        j.con=0
                        j.velx=-VELOCIDAD
                        j.m=m_izquierda
                        j.accion=11
                    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                        j.con=0
                        j.velx=VELOCIDAD
                        j.m=m_derecha
                        j.accion=11
                    if keys[pygame.K_UP] or keys[pygame.K_w]:
                        if j.salto < 2:
                            j.con=0
                            j.vely=-10
                            j.salto+=1
                    if  keys[pygame.K_SPACE]:
                        slash.play()
                        j.con=0
                        golpear=True
                        if j.m==m_derecha or j.m==m_hide:
                            j.m=m_atack1
                            j.accion=5
                        elif j.m==m_izquierda or j.m==m_hide2:
                            j.m=m_atack2
                            j.accion=5
                        if j.pocionx:
                            fire_ball.play()
                            p=j.RetPos()
                            b=Bala_ave(p,bala_j)
                            if j.m==m_atack1:
                                b.velx=5
                            elif j.m==m_atack2:
                                b.velx= -5
                                b.rect.x -=96
                            b.tipo=2
                            balas_ave.add(b)
                    if keys[pygame.K_p]:
                        Pausa(ventana)

                 #VIDA EXTRA O BALAS
                ls_l=pygame.sprite.spritecollide(j,pociones,False)
                for p in ls_l:
                    if p.tipo==1:
                        if j.temp < 0:
                            pocionv_sound.play()
                            j.vida += 1
                            if j.vida > 4:
                                j.vida=4
                            pociones.remove(p)
                    else:
                        pocionx_sound.play()
                        j.pocionx=True
                        pociones.remove(p)
                #DAÑO ESPADA
                ls_l=pygame.sprite.spritecollide(j,bosses,False)
                for b in ls_l:
                    if golpear:
                        if j.temp <0 :
                            b.vida -= 1
                            kill_enemy.play()
                            j.temp= 30
                            if b.vida <= 0:
                                boss2_music.stop()
                                boss_win.play()
                                fin_level2=True
                                cruzar_puerta=True
                #DAÑO BOSSES                
                ls_l=pygame.sprite.spritecollide(bss,jugadores,False)
                for j in ls_l:
                    if bss.m == m_boss2_attack:
                        if j.temp <0 :
                            j.pocionx=False
                            j.vida -= 2
                            hit_sound.play()
                            j.temp= 30
                            if j.vida <= 0:
                                boss2_music.stop()
                                fin_level2=True
                #MOVIMIENTO BOSS
                if bss.temp < 0:
                    if bss.m == m_boss2_hide:
                        bss.con=0
                        bss.m= m_boss2_attack
                        bss.rect.y -= 93
                        bss.temp =100
                        bss.velx =  -5
                        
                    elif bss.m == m_boss2_attack:
                        bss.con=0
                        bss.m= m_boss2_hide
                        bss.temp =100
                        bss.rect.y += 93
                        bss.velx =  5
                    
                #BORRAR BALAS AL IMPACTAR
                for b in balas_ave:
                    ls_l=pygame.sprite.spritecollide(b,bosses,False)
                    for bs in ls_l:
                        if b.tipo==2:
                            if j.temp <0 :
                                balas_ave.remove(b)
                                kill_enemy.play()
                                bs.vida -= 1
                                j.temp= 30
                                if bs.vida <= 0:
                                    boss_win.play()
                                    boss2_music.stop()
                                    fin_level2=True
                                    cruzar_puerta=True
                            
                    ls_l=pygame.sprite.spritecollide(b,plataformas,False)
                    for l in ls_l:
                        balas_ave.remove(b)
                    ls_l=pygame.sprite.spritecollide(b,jugadores,False)
                    for j in ls_l:
                        if b.tipo==1:
                            if j.temp <0:
                                hit_sound.play()
                                j.pocionx=False
                                j.vida-=1
                                j.temp=60
                                if j.vida <=0:
                                    boss2_music.stop()
                                    fin_level2=True
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
                    msj1='TIME 0'+str(minutos)+':'+str(segundos)
                elif segundos>9 and minutos>9:
                    msj1='TIME '+str(minutos)+':'+str(segundos)
                elif segundos<9 and minutos>9:
                    msj1='TIME '+str(minutos)+':0'+str(segundos)
                elif segundos<9 and minutos<9:
                    msj1='TIME 0'+str(minutos)+':0'+str(segundos)
                    
                msj2='SCORE '+str(j.score)
                msj3='VIDAS '+str(bss.vida)
                msj4='NIVEL 2'
                
                info1=tiempo.render(msj1,True,BLANCO)
                info2=score.render(msj2,True,BLANCO)
                info3=boss_f.render(msj3,True,BLANCO)
                info4=vida.render(msj4,True,BLANCO)
                camara.update(j)
                balas_ave.update()
                jugadores.update()
                bosses.update()
                pociones.update()
                ojos.update()
                ventana.blit(map_img, camara.apply_rect(map_rect))
                ventana.blit(j.image,camara.apply(j))
                ventana.blit(bss.image,camara.apply(bss))
                for o in ojos:
                    ventana.blit(o.image,camara.apply(o))
                for b in balas_ave:
                    ventana.blit(b.image,camara.apply(b))
                for p in pociones:
                    ventana.blit(p.image,camara.apply(p))

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
                ventana.blit(info3,[bss.rect.x-10,bss.rect.y+20])
                ventana.blit(info4,[650,590])
                pygame.display.flip()
                reloj.tick(60)
                milisegundos += 1
        if cruzar_puerta:
            congratulations.play()
            Felicidades(ventana)
    #FIN JUEGO
    if not cruzar_puerta:
        ambiente_music.stop()
        gameover_music.play()
        while not fin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin=True

            
            ventana.fill(NEGRO)
            ventana.blit(fondo_fin,[0,15])
            ventana.blit(fondo_fin_juego,[100,100])
            pygame.display.flip()
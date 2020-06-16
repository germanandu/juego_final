import pygame 
from settings import *
class Jugador(pygame.sprite.Sprite):
    def __init__(self,pos,m,m2_vida=m_vida):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.m2=m2_vida
        self.accion=3
        self.accion_vida=3
        self.con=0
        self.con_vida=0
        self.image_vida=self.m2[self.con_vida]
        self.image=self.m[self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.vida=4
        self.score=0
        self.temp=60
        self.pocionx=False
        self.plataformas=None

    def gravedad (self, g=0.7):
        if self.vely == 0:
            self.vely = g
        else:
            self.vely += g
    
    def RetPos(self):
        x=self.rect.x +96
        y=self.rect.y +24
        return [x,y]

    def update(self):
        self.temp-=1

        if self.con_vida < self.accion_vida:
            self.con_vida+=1
        else:
            self.con_vida=0
        self.image_vida=self.m2[self.con_vida]

        if self.velx!=self.vely:
            if self.con < self.accion:
                self.con+=1
            else:
                self.con=0
        self.image=self.m[self.con]
        self.rect.x+=self.velx
        ls_col=pygame.sprite.spritecollide(self,self.plataformas,False)
        #Colision  en X
        for b in ls_col:
            if self.velx > 0:
                if self.rect.right > b.rect.left:
                    self.rect.right= b.rect.left
                    self.velx=0
            else:
                if self.rect.left < b.rect.right:
                    self.rect.left= b.rect.right
                    self.velx=0
        #Colision en Y
        self.rect.y+=self.vely
        ls_col=pygame.sprite.spritecollide(self,self.plataformas,False)
        for b in ls_col:
            if self.vely > 0:
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom= b.rect.top
                    self.vely=0
            else:
                if self.rect.top < b.rect.bottom:
                    self.rect.top= b.rect.bottom
                    self.vely=0
        self.gravedad()
        """ if self.rect.bottom > ALTO:
            self.rect.bottom=ALTO
            self.vely=0 """

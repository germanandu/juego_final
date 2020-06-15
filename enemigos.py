import pygame 
from settings import *

class Ave(pygame.sprite.Sprite):
    def __init__(self,pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=7
        self.con=0
        self.image=self.m[self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.temp=random.randrange(200)

    def RetPos(self):
        x=self.rect.x +70
        y=self.rect.y +70
        return [x,y]

    def update(self):
        self.temp -= 1
        if self.con < self.accion:
            self.con+=1
        else:
            self.con=0
        self.image=self.m[self.con]


class Lobo(pygame.sprite.Sprite):
    def __init__(self,pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=11
        self.con=0
        self.image=self.m[self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.temp=100
        self.velx=0
        self.bandera=False
    
    def update(self):
        
        if self.con < self.accion:
            self.con+=1
        else:
            self.con=0
        self.image=self.m[self.con]
        self.rect.x += self.velx


class Boss1(pygame.sprite.Sprite):
    def __init__(self,pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=5
        self.con=0
        self.image=self.m[self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.temp=100
        self.velx=0
        self.vely=0
        self.vida=5
        self.bandera=False
    
    def update(self):
        self.temp -=1
        if self.con < self.accion:
            self.con+=1
        else:
            self.con=0
        self.image=self.m[self.con]
        self.rect.x += self.velx
        self.rect.y += self.vely
        
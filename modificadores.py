import pygame 
from settings import *

class Pocion(pygame.sprite.Sprite):
    def __init__(self,pos,m=m_pocionv):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.con=0
        self.image=self.m[self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.tipo=1

    def update(self):
        if self.con < 2:
            self.con+=1
        else:
            self.con=0
        self.image=self.m[self.con]
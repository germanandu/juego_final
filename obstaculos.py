import pygame 
from settings import *
class Plataforma(pygame.sprite.Sprite):
    def __init__(self,pos,dm, cl=VERDE):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dm)
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
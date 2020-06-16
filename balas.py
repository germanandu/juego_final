import pygame
from settings import *

class Bala_ave(pygame.sprite.Sprite):
    def __init__(self, pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.image=m
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.vely=0
        self.velx=0
        self.tipo=1

    def update(self):
        self.rect.y+=self.vely
        self.rect.x+=self.velx
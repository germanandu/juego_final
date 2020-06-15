import pygame 
from settings import *
class Plataforma(pygame.sprite.Sprite):
    def __init__(self,pos,dm):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dm)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0

class Vacio(pygame.sprite.Sprite):
    def __init__(self,pos,dm):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dm)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]

class Puerta(pygame.sprite.Sprite):
    def __init__(self,pos,dm):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dm)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]

class Linea(pygame.sprite.Sprite):
    def __init__(self,pos,dm):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dm)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
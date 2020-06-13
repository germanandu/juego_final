import pygame 

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

    def update(self):
        
        if self.con < self.accion:
            self.con+=1
        else:
            self.con=0
        self.image=self.m[self.con]
        
        
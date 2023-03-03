import pygame
class Retangulo:
    def __init__(self,pos,dim,cor=(255,255,255)):
        self.pos=pos
        self.dim=dim
        self.cor=cor
        self.vx=0
        self.vy=0

    def update(self):
        self.pos[0]=self.pos[0]+self.vx
        self.pos[1]=self.pos[1]+self.vy

    def draw(self,screen):
        rect=pygame.Rect(self.pos,self.dim)
        pygame.draw.rect(screen,self.cor,rect)

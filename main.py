import pygame
from Retangulo import Retangulo
pygame.init()

screen = pygame.display.set_mode((600,600))
rodando = True
ret=Retangulo([0,0],[50,50])
ret.vx=0
ret.cor=(0,255,0)

def entradaDados():
    for evt in pygame.event.get():
        if evt.type==pygame.QUIT:
                exit()
    keys=pygame.key.get_pressed()
    ret.vx=0
    ret.vy=0
    if keys[pygame.K_LEFT]:
         ret.vx=-0.1
    if keys[pygame.K_RIGHT]:
         ret.vx=0.1
    if keys[pygame.K_UP]:
         ret.vy=-0.1
    if keys[pygame.K_DOWN]:
         ret.vy=0.1

def update():
     ret.update()
    
def draw():
    screen.fill((255, 0, 0))
    ret.draw(screen)
    rect=pygame.Rect(50, 100, 80, 150)
    pygame.draw.rect(screen,(255,255,255),rect)
    pygame.display.flip()

while rodando:
    entradaDados()
    update()
    draw()
                
    
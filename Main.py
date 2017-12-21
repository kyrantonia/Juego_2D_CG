# import pygame as pg
# import random
from Variables import *
import os
from random import *
from CC3501Utils import *
#from Varias_Plataformas import*

from pato import *
from plataforma1 import*
from plataforma_2 import*
from plataforma3 import*
from muros2 import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla
def main():
    n=0
    
    init(ancho, altura, "titulo")
    pygame.mixer.music.load('musica.mp3')
    pygame.mixer.music.play(-1)

    cuac = pygame.mixer.SoundType('cuac.ogg')


    m1 = muros2(Vector(0, 0), Vector(0, 0), Vector(243/0.5, 55), anchoPla)
    m11=muros2(Vector(0, 0), Vector(0, 0), Vector(243/0.5, 55*3), anchoPla)
    m12 = muros2(Vector(0, 0), Vector(0, 0), Vector(243 / 0.5, 55*5), anchoPla)
    m13 = muros2(Vector(0, 0), Vector(0, 0), Vector(243 / 0.5, 55 * 7), anchoPla)
    m14 = muros2(Vector(0, 0), Vector(0, 0), Vector(243 / 0.5, 55 * 9), anchoPla)
    m15 = muros2(Vector(0, 0), Vector(0, 0), Vector(243 / 0.5, 55 * 11), anchoPla)
    m2 = muros2(Vector(0, 0), Vector(0, 0), Vector(15, 55), anchoPla)
    m21 = muros2(Vector(0, 0), Vector(0, 0), Vector(8 / 0.5, 55 * 3), anchoPla)
    m22 = muros2(Vector(0, 0), Vector(0, 0), Vector(8 / 0.5, 55 * 5), anchoPla)
    m23 = muros2(Vector(0, 0), Vector(0, 0), Vector(8/ 0.5, 55 * 7), anchoPla)
    m24 = muros2(Vector(0, 0), Vector(0, 0), Vector(8 / 0.5, 55 * 9), anchoPla)
    m25 = muros2(Vector(0, 0), Vector(0, 0), Vector(8 / 0.5, 55 * 11), anchoPla)

    pato=Pato(Vector(0,0),Vector(0,0))
    muro_izq=[]
    muro_izq.append(m2)
    muro_izq.append(m21)

    muro_der = []
    muro_der.append(m1)
    muro_der.append(m11)




    p2=Plataforma1(Vector(ancho/3,550),anchoPla+50)
    p3 = Plataforma3( Vector(120, 350), anchoPla+20)
    p1 = Plataforma2(Vector(ancho/3,150),anchoPla+50)
    p4 = Plataforma1(Vector(ancho / 2, 300), anchoPla+20)
    p5 = Plataforma3(Vector(ancho-150, 450), anchoPla+20)
    piso = Plataforma(Vector(0,0),ancho,[0.8,0.5,0])
    x = []
    y = []
    anchos = []

    for i in range(0, cantidad_de_plataformas):

        x.append(uniform(100, ancho - 150))
        y.append(uniform(altura, 6*altura))
        anchos.append(uniform(70,100))
    plataformas = []
    Tipo_plataforma=[Plataforma1,Plataforma2,Plataforma3]

    plataformas.append(piso)
    plataformas.append(p1)
    plataformas.append(p2)
    plataformas.append(p3)
    plataformas.append(p4)
    plataformas.append(p5)



    for j in range(0, cantidad_de_plataformas):
        plataformas.append(Tipo_plataforma[randint(0,2)]( Vector(x[j], plataformas[j+1].pos.y+altura), anchos[j]))

    run = True
    while run:


        for event in pygame.event.get():
            if event.type == QUIT:  # cerrar ventana
                run = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if pato.estoy == True:
                        cuac.play()
                        pato.vel.y=abs(pato.vel.x)+velocidadSalto

        if (n < cantidad_de_plataformas):
            while len(plataformas)<cantidad_de_plataformas:

                    j=randint(0, 2)
                    plataformas.append(
                            Tipo_plataforma[j]( Vector(uniform(100, ancho - 100),y[i]+3*altura/4),
                                                       uniform(50, 100)))
                    n = n + 1
        else:
            while len(plataformas) < 5:
                j = randint(0, 2)
                Y=[450,300,150,550,350]
                for k in Y:
                    plataformas.append(
                    Tipo_plataforma[j](
                                           Vector(uniform(100, ancho - 100),pato.pos.y+k),
                                           uniform(50, 100)))
                print(i)
        pato.ActualizarPantalla(plataformas, n)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # limpiar buffers

        #dibujar figuras
        glBegin(GL_QUADS)
        glColor3f(0,0.3,0.4)
        glVertex2f(0, altura)
        glVertex2f(0, 0)
        glVertex2f(ancho, 0)
        glVertex2f(ancho, altura)
        glEnd()
        m1.dibujar()
        m11.dibujar()
        m12.dibujar()
        m13.dibujar()
        m14.dibujar()
        m15.dibujar()
        m2.dibujar()
        m21.dibujar()
        m22.dibujar()
        m23.dibujar()
        m24.dibujar()
        m25.dibujar()


        pato.dibujar()
        for i in range(0,len(plataformas)):
            plataformas[i].dibujar()


        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps


    pygame.quit()
main()

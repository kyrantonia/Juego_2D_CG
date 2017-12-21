from Objetos import *
import os
from random import *
from CC3501Utils import *
#from Varias_Plataformas import*

class Plataforma2(Figura):
    def __init__(self,pos:Vector,anchoPlataforma):#pos=Vector(ancho/2, 200)):
        self.pos = pos
        self.anchoPlataforma=anchoPlataforma
        super().__init__(pos)
    def figura(self):
        glPushMatrix()
        glScalef(self.anchoPlataforma / 200, self.anchoPlataforma / 200, 0)
        glTranslated(-30,30,0)
        glBegin(GL_QUADS)

        glColor3f(0.9,0.1,0.2)
        glVertex2f(0, -43)
        glVertex2f(0, 0)
        glVertex2f(190, 0)
        glVertex2f(190,- 43)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.7, 0.8, 0.7)
        glVertex2f(0, 0)
        glVertex2f(0, 15)
        glVertex2f(30, 15)
        glVertex2f(30, 0)
        glEnd()

        glBegin(GL_TRIANGLES)
        #
        glColor3f(0.8,1,0.9)

        glVertex2f(120,30)
        glVertex2f(170, 0)
        glVertex2f(120, 0)
        glEnd()



        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.9,0.1,0.2)
        radio3 = 60
        glVertex2f(100, 0)
        cantidad_de_triangulos = 2 * radio3
        ang = - pi/4 / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3+150, sin(ang_i) * radio3)

        glVertex2f(1.0 * radio3, 0.0)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.6,1,0)
        glVertex2f(0, 0)
        glVertex2f(0, -43)
        glVertex2f(210, -15)
        glVertex2f(210, 0)
        glEnd()
        glPopMatrix()




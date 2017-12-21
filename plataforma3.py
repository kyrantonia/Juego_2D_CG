from Objetos import *
import os
from random import *
from CC3501Utils import *
#from Varias_Plataformas import*

class Plataforma3(Figura):
    def __init__(self,pos:Vector,anchoPlataforma):#pos=Vector(ancho/2, 200)):
        self.pos = pos


        self.anchoPlataforma=anchoPlataforma
        super().__init__(pos )
    def figura(self):
        glPushMatrix()
        #glScalef(2,2,0)

        glScalef(self.anchoPlataforma / 200, self.anchoPlataforma / 200, 0)
        glTranslatef(50,-70, 0)
        glBegin(GL_QUADS)
        glColor3f(0.4,0.3,0.6)
        glVertex2f(-80, 100)
        glVertex2f(-80, 0)
        glVertex2f(80, 0)
        glVertex2f(80,100)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.7, 0.8, 0.7)
        glVertex2f(30, 40)
        radio3 = 30
        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3, sin(ang_i) * radio3 + 40)

        glVertex2f(1.0 * radio3, 0.0)
        glEnd()
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1,0.3,0.3)
        glVertex2f(20, 40)
        radio3 = 20
        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3, sin(ang_i) * radio3 + 40)

        glVertex2f(1.0 * radio3, 0.0)
        glEnd()

        #boton
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.9,0,0.4)
        glVertex2f(-60, 100)
        radio3 = 18
        cantidad_de_triangulos = 2 * radio3
        ang = pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3-60, sin(ang_i) * radio3 + 100)

        #glVertex2f(1.0 * radio3, 0.0)

        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.7, 0.8, 0.7)
        glVertex2f(-80, 105)
        glVertex2f(-80, 100)
        glVertex2f(-40, 100)
        glVertex2f(-40, 105)
        glEnd()



        #en el rectantangulo grande
        glBegin(GL_QUADS)
        glColor3f(0.7, 0.8, 0.7)
        glVertex2f(-60, 90)
        glVertex2f(-60, 70)
        glVertex2f(-30, 70)
        glVertex2f(-30, 90)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.7, 0.8, 0.7)
        glVertex2f(-80, 30)
        glVertex2f(-80, 10)
        glVertex2f(-60, 10)
        glVertex2f(-60, 30)
        glEnd()

        #flash
        glBegin(GL_QUADS)
        glColor3f(0.7, 0.8, 0.7)
        glVertex2f(80, 100)
        glVertex2f(80, 130)
        glVertex2f(30, 130)
        glVertex2f(30, 100)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.9,0.4,0.6)
        glVertex2f(75, 100)
        glVertex2f(75, 125)
        glVertex2f(35, 125)
        glVertex2f(35, 100)
        glEnd()
        glPopMatrix()



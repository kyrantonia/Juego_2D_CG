from Objetos import *
import os
from random import *
from CC3501Utils import *
#from Varias_Plataformas import*

class Plataforma1(Figura):
    def __init__(self,pos:Vector,anchoPlataforma):#pos=Vector(ancho/2, 200)):
        self.pos = pos
        self.anchoPlataforma=anchoPlataforma
        super().__init__(pos)
    def figura(self):
        glPushMatrix()
        glScalef(self.anchoPlataforma/130,self.anchoPlataforma/130, 0)
        glTranslated(0,15,0)
#atras

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1,1,1)
        radio3 = 20
        glVertex2f(20, 0)
        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3 + 20, sin(ang_i) * radio3)

        glVertex2f(1.0 * radio3, 0.0)
        glEnd()


        glBegin(GL_TRIANGLE_FAN)

        radio3 = 20
        glVertex2f(80, 0)
        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos
        for i in range(cantidad_de_triangulos +1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3+100, sin(ang_i) * radio3 )

        glVertex2f(1.0 * radio3, 0.0)
        glEnd()


        #3
        glBegin(GL_TRIANGLE_FAN)

        radio3 = 25
        glVertex2f(80, 0)

        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3 + 80, sin(ang_i) * radio3)

        glVertex2f(1.0 * radio3, 0.0)
        glEnd()

        #4
        glBegin(GL_TRIANGLE_FAN)

        radio3 = 25
        glVertex2f(80, 0)

        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3 + 50, sin(ang_i) * radio3)

        glVertex2f(1.0 * radio3, 0.0)
        glEnd()

#adelante

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1,0.7,0.6)
        radio3 = 15
        glVertex2f(30, -20)

        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3 + 40, sin(ang_i) * radio3-20)

        glVertex2f(1.0 * radio3, 0.0)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)

        radio3 = 20
        glVertex2f(30, -20)

        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3 + 20, sin(ang_i) * radio3 - 20)

        glVertex2f(1.0 * radio3, 0.0)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)

        radio3 = 15
        glVertex2f(30, -20)

        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3 , sin(ang_i) * radio3 - 20)

        glVertex2f(1.0 * radio3, 0.0)
        glEnd()
        glPopMatrix()

from Objetos import *
import os
from random import *
from CC3501Utils import *
#from Varias_Plataformas import*

class muros2(Figura):
    def __init__(self,vel: Vector, acc:Vector ,pos:Vector,anchoPlataforma,rgb=(1.0, 1.0, 1.0)):#pos=Vector(ancho/2, 200)):
        self.pos = pos
        self.rgb = rgb
        self.vel = vel
        self.acc = acc
        self.anchoPlataforma=anchoPlataforma
        super().__init__(pos, rgb)
    def figura(self):
        glPushMatrix()
        glScalef(0.5, 0.5, 0)
        #glScalef(1,1,0)
        #glTranslated(100,100,0)
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.8,0.4,0.4)
        radio3 = 20
        glVertex2f(0, 0)
        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3, sin(ang_i) * radio3)

        glVertex2f(1.0 * radio3, 0.0)
        glEnd()


        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.7, 0.8, 0.7)
        radio3 = 25
        #glVertex2f(0, 0)
        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3, sin(ang_i) * radio3+40)

        #glVertex2f(1.0 * radio3, 0.0)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.2,0.6,0.5)
        radio3 = 30
        # glVertex2f(0, 0)
        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3, sin(ang_i) * radio3 + 80)

        # glVertex2f(1.0 * radio3, 0.0)
        glEnd()


        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.7, 0.8, 0.7)
        radio3 = 25
        # glVertex2f(0, 0)
        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3, sin(ang_i) * radio3 - 40)

        # glVertex2f(1.0 * radio3, 0.0)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.2, 0.6, 0.5)
        radio3 = 30
        # glVertex2f(0, 0)
        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3, sin(ang_i) * radio3 - 80)

        # glVertex2f(1.0 * radio3, 0.0)
        glEnd()
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.8, 0.4, 0.4)
        radio3 = 20
        glVertex2f(0, 0)
        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3, sin(ang_i) * radio3)

        glVertex2f(1.0 * radio3, 0.0)
        glEnd()
        glPopMatrix()
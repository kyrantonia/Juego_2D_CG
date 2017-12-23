from Objetos import *
import os
from random import *
from CC3501Utils import *
#from Varias_Plataformas import*
from Variables import*
from texto import *

class Pato(Figura):
    def __init__(self,vel: Vector, acc:Vector ,pos=Vector(ancho/2, 49)):
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.estoy=False
        self.run=True
        super().__init__(pos)


    def figura(self):
        glPushMatrix()
        glScalef(0.5, 0.5, 0)
        glTranslatef(0,60,0)
        #arriba
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(255, 255, 0)
        glVertex2f(60, 50)
        radio3 = 60
        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3, sin(ang_i) * radio3 + 50)

        glVertex2f(1.0 * radio3, 0.0)
        glEnd()


        glBegin(GL_TRIANGLE_FAN)
        glColor3f(255, 255, 0)
        glVertex2f(65, 0)
        #abajo
        radio3 = 65
        cantidad_de_triangulos = 2 * radio3
        ang = 2 * pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3, sin(ang_i) * radio3 )

        glVertex2f(1.0 * radio3, 0.0)
        glEnd()
        #boca
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1, 0.5, 0)
        glVertex2f(20, 50)
        radio3 = 20
        cantidad_de_triangulos = 2 * radio3
        ang = 2* pi / cantidad_de_triangulos

        for i in range(cantidad_de_triangulos + 1):
            ang_i = ang * i
            glVertex2f(cos(ang_i) * radio3, sin(ang_i) * radio3 + 50)

        glVertex2f(1.0 * radio3, 0.0)
        glEnd()
        #ojos
        glBegin(GL_QUADS)
        glColor3f(0, 0, 0.6)
        glVertex2f(-25, 75)
        glVertex2f(-25, 60)
        glVertex2f(-33, 60)
        glVertex2f(-33, 75)
        glEnd()
        glBegin(GL_QUADS)

        glVertex2f(33, 75)
        glVertex2f(33, 60)
        glVertex2f(25, 60)
        glVertex2f(25, 75)
        glEnd()


        # linea boca
        glBegin(GL_LINES)
        glColor3f(0.7,0.4,0.1)
        glVertex2f(20, 50)
        glVertex2f(0, 40)
        glVertex2f(0, 40)
        glVertex2f(-20, 50)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(0.7,0.4,0.1)
        glVertex2f(20, 49)
        glVertex2f(0, 39)
        glVertex2f(0, 39)
        glVertex2f(-20, 49)
        glEnd()
        glPopMatrix()

    def ActualizarPantalla(self, plataformas, n):
        rebote = pygame.mixer.SoundType('rebote.ogg')
        end = pygame.mixer.SoundType('disqualified.ogg')
        draw_text(100, 100, "disqualified")
        self.estoy=False
        self.acc = Vector(0, gravedad)
        #pl=Plataforma(Vector(0,0),Vector(0,0),posPla,a)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -Aceleracion
        if keys[pygame.K_RIGHT]:
            self.acc.x = Aceleracion
        ##aplicar roce en el eje x
        self.acc.x += self.vel.x * roce ##a=-b*v/m (roce aire)
        #ecuaciones movimiento
        self.vel += self.acc #vf=vi+a*t
        self.pos += self.vel + ponderar(0.5,self.acc)#x=vi*t+0.5*a*t*t
        # No salirme de la pantalla y rebotar
        if self.pos.x+60 > ancho:
            rebote.play()
            self.pos.x = ancho-60
            self.vel.x=-self.vel.x


        if self.pos.x < 60:
            rebote.play()
            self.pos.x = 60
            self.vel.x = -self.vel.x

        if self.estoy==False and self.pos.y < 0:##morir
                end.play()
                self.run=False


        #choque plataforma

        for plataforma in plataformas:
            if self.choquePlataforma(plataforma) == True:
                self.pos.y = hpla1 + plataforma.pos.y
                if (self.vel.y < 0):  ##si choca con la plataforma desde abajo seguira saltando
                    self.vel.y = 0
                    self.estoy = True  ##actualizo porque ahora si estoy en la plataforma

        ##seguir al personaje
        if self.pos.y>3*altura/4:
            self.pos.y=abs(self.vel.y)+3*altura/4

            y=[]

            for plataforma in plataformas:
                plataforma.pos.y-=abs(self.vel.y)
            i = 0

            if(n<cantidad_de_plataformas):
                for plataforma in plataformas:
                    if plataforma.pos.y+altura<self.pos.y:
                        y.append(plataforma.pos.y)
                        i = i + 1

                        plataformas.remove(plataforma)

            else:
                for plataforma in plataformas:

                    if plataforma.pos.y+altura/2<self.pos.y:
                        y.append(plataforma.pos.y)
                        i = i + 1

                        plataformas.remove(plataforma)

    def choquePlataforma(self,plataforma): ##revisar si estoy en la plataforma
        pl=plataforma
        if (self.pos.y > pl.pos.y and self.pos.y< hpla1 + pl.pos.y and pl.pos.x < self.pos.x + anchoPerso and self.pos.x < pl.pos.x + pl.anchoPlataforma) or (self.pos.y<hpla1 and plataforma.anchoPlataforma==ancho):
            return True
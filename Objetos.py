from CC3501Utils import *
from Variables import *
from random import *
from pato import *

class Persona(Figura):
    def __init__(self,vel: Vector, acc:Vector ,rgb=(1.0, 1.0, 1.0),pos=Vector(ancho/2, hpla1)):
        self.pos = pos
        self.rgb = rgb
        self.vel = vel
        self.acc = acc
        self.estoy=False
        super().__init__(pos, rgb)
    def figura(self):
        glBegin(GL_QUADS)
        glColor3f(1.0, 1.0, 0.0)
        glVertex2f(0, hpersonaje)
        glVertex2f(0, 0)
        glVertex2f(anchoPerso, 0)
        glVertex2f(anchoPerso, hpersonaje)
        glEnd()

    def update(self,plataformas):
        self.estoy=False
        self.acc = Vector(0, gravedad)
        #pl=Plataforma(Vector(0,0),Vector(0,0),posPla,a)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -Aceleración
        if keys[pygame.K_RIGHT]:
            self.acc.x = Aceleración
        ##aplicar roce en el eje x
        self.acc.x += self.vel.x * roce ##a=-b*v/m (roce aire)
        #ecuaciones movimiento en x
        self.vel += self.acc #vf=vi+a*t
        self.pos += self.vel + ponderar(0.5,self.acc)#x=vi*t+0.5*a*t*t
        # No salirme de la pantalla y rebotar
        if self.pos.x+anchoPerso > ancho:
            self.pos.x = ancho-anchoPerso
            self.vel.x=-self.vel.x
            #self.vel.x=-cos(self.vel.angulo())*self.vel.modulo()
            #self.vel.y = sin(self.vel.angulo()) * self.vel.modulo()
        if self.pos.x < 0:
            self.pos.x = 0
            self.vel.x = -self.vel.x
            #self.vel.x = cos(self.vel.angulo()) * self.vel.modulo()
            #self.vel.y = sin(self.vel.angulo()) * self.vel.modulo()

        #choque piso
        #if self.pos.y < hpiso:
        #    self.pos.y = hpiso
        #    self.vel.y = 0
         #    self.estoy = True
        ##la ppñataforma tiene que estar completa en la pantalla sino muere

        if self.estoy==False and self.pos.y < 0:
                print("end")
                quit()



        #choque plataforma

        for plataforma in plataformas:
            if self.choquePlataforma(plataforma) == True:
                self.pos.y = hpla1 + plataforma.pos.y
                if (self.vel.y < 0):  ##si choca con la plataforma esde abajo seguira saltando
                    self.vel.y = 0
                    self.estoy = True  ##actualizo porque ahora si estoy en la plataforma

        ##seguir al personaje
        if self.pos.y>3*altura/4:
            y=[]
            self.pos.y=abs(self.vel.y)+3*altura/4
            for plataforma in plataformas:
                plataforma.pos.y-=abs(self.vel.y)
            for plataforma in plataformas:
                if plataforma.pos.y+altura<self.pos.y:
                    y.append(plataforma)
                    plataformas.remove(plataforma)
                    n = n + 1
                    print(n)




    def choquePlataforma(self,plataforma): ##revisar si estoy en la plataforma
        pl=plataforma
        if (self.pos.y> pl.pos.y and self.pos.y< hpla1 + pl.pos.y and pl.pos.x < self.pos.x + anchoPerso and self.pos.x < pl.pos.x + pl.anchoPlataforma) or (self.pos.y<hpla1 and plataforma.anchoPlataforma==ancho):
            return True

class Plataforma(Figura):
    def __init__(self,pos:Vector,anchoPlataforma,rgb=(1,1,1)):#pos=Vector(ancho/2, 200)):
        self.pos = pos
        self.rgb = rgb
        self.anchoPlataforma=anchoPlataforma
        super().__init__(pos, rgb)
    def figura(self):
        glBegin(GL_QUADS)
        glColor3f(self.rgb[0],self.rgb[1],self.rgb[2])
        glVertex2f(0,hpla1)
        glVertex2f(0,0)
        glVertex2f(self.anchoPlataforma,0)
        glVertex2f(self.anchoPlataforma,hpla1)
        glEnd()
class Piso(Figura):
    def __init__(self,vel: Vector, acc:Vector, rgb=(1.0, 1.0, 1.0), pos=Vector(0, 0)):
        self.pos = pos
        self.rgb = rgb
        self.vel = vel
        self.acc = acc
        super().__init__(pos, rgb)
    def figura(self):
        glBegin(GL_QUADS)
        glColor3f(0, 255, 0)
        glVertex2f(0,hpiso)
        glVertex2f(0,0)
        glVertex2f(ancho,0)
        glVertex2f(ancho,hpiso)
        glEnd()



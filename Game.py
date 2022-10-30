from turtle import right
from ship import Ship
from Sky import Sky
from Bullet import Bullet
import random
import pygame


class Game:

    def __init__ (self):
        self.width=800
        self.height=800
        self.mySky=Sky(self.width, self.height, 1600)
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.clock=pygame.time.Clock()
        self.fps=60
        self.sprites= pygame.image.load("spritesS.png")
        self.shipsprite=pygame.Surface((64,64)).convert()
        self.shipsprite.blit(self.sprites,(0,0),(250,436,64,64))
        self.bala=pygame.image.load("bullet.png")
        self.lista=[0,1,2,3,4,5]
        self.dibujos=[]
        self.coordenates=[]
        self.ship=Ship()
        self.Bullet=Bullet()
    

    def checkkeys(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.Bullet.state="activo"
            pass
            
        elif keys [pygame.K_RIGHT]:
            self.ship.direction="right"
            if self.Bullet.state=="pasivo":
                self.Bullet.state="derecha"
            else:
                self.Bullet.xproyectil=self.Bullet.xproyectil
            
        elif keys[pygame.K_LEFT]:
            self.ship.direction="left"
            if self.Bullet.state=="pasivo":
                self.Bullet.state="izquierda"
            else:
                self.Bullet.xproyectil=self.Bullet.xproyectil
                

        else:
            self.ship.direction="centro"
            self.Bullet.state="pasivo"
            
            



    def run (self):
        pygame.init()
        control=True
        while control:
            self.screen.fill((0,0,0))

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()

            for star in self.mySky.stars:
                r=random.randint(0,255)
                g=random.randint(0,255)
                b=random.randint(0,255)
                pygame.draw.circle(self.screen, (r,g,b), star, 1)      

            self.mySky.move()
            x=self.ship.xnave
            y=700
            x2=self.Bullet.xproyectil
            y2=self.Bullet.yproyectil
   
            self.screen.blit(self.bala,(x2,y2))    
            self.screen.blit(self.shipsprite,(x,y))
            self.clock.tick(self.fps)
            self.checkkeys()
            self.ship.move()
            self.Bullet.move2()
            pygame.display.flip()


myGame=Game()
myGame.run()

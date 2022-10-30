
from ship import Ship
class Bullet:
    def __init__ (self):
        
        self.ship=Ship()
        self.state="pasivo"
        self.xproyectil=400
        self.yproyectil=600
        
    def move2(self):
            
        if self.state=="derecha":
            self.xproyectil=self.xproyectil+10
            
        elif self.state=="izquierda":
            self.xproyectil=self.xproyectil-10   
            
        elif self.state=="activo":
            self.yproyectil=self.yproyectil-5
            pass
        
        elif self.state=="pasivo":
            self.xproyectil=self.xproyectil
        
        return(self.xproyectil,self.yproyectil)
        
        
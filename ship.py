class Ship:
    def __init__ (self):
        self.direction="centro"
        self.xnave=400 
        self.ynave=700
    def move(self):
        
        if self.direction=="right":
            self.xnave=self.xnave+10
            
        if self.direction=="left":
            self.xnave=self.xnave-10
        
        if self.direction=="centro":
            self.xnave=self.xnave
            
        return(self.xnave)
            

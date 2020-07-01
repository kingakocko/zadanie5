class Pokretlo():
    ilosc_wcisniec_wszystkich_pokretel = 0
    def __init__(self, arg_x, arg_y, arg_r):
        self.obrot = 0
        self.wcisniety = False 
        self.x = arg_x
        self.y = arg_y
        self.r = arg_r
    
    def rysuj(self):
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+45), PI+ radians(self.obrot+45), PIE)
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+45), PI+ radians(self.obrot+270), PIE)
    def obroc(self, stopnie):
        self.obrot += stopnie
    def wcisnij(self):
        Pokretlo.ilosc_wcisniec_wszystkich_pokretel +=1
        self.wcisniety = not self.wcisniety
        background(100)
class Kwadrat():
    def __init__(self, bok): 
        self.bok = bok
    def sketch(self, a, b):
        self.a = a
        self.b = b
        rect(self.a, self.b, self.bok, self.bok)
        fill(175, 238, 238)
    
def setup():
    size(500, 500)
    global pokretlo_piekarnika
    pokretlo_piekarnika = Pokretlo(width/2, height/2, 200)
    global przycisk
    przycisk = Kwadrat (50.0)
def mouseClicked():
     pokretlo_piekarnika.wcisnij()
     if mouseX >450 and mouseX<500:
        if mouseY >400 and mouseY <450:
            background(244 ,164, 96)

            
def mouseWheel(event):
    pokretlo_piekarnika.obroc(10)
def draw():
    background(300)
    pokretlo_piekarnika.rysuj()
    przycisk.sketch(70,400)
        

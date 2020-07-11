class Kreciolek():
    def __init__(self, x, y, segmenty):
        self.x = x
        self.y = y
        self.segmenty = segmenty
        self.niebieski = 100
        self.kierunek = True
        self.var = (2*PI)/self.segmenty
        self.start = 0
        self.stop = self.var
        
    def sketch(self):
        pushMatrix()
        strokeWeight(10)
        fill(50)
        self.start = (self.start + self.var) % (2*PI)
        self.stop = (self.stop + self.var) % (2*PI)
        self.niebieski += self.kierunek
        stroke(0, 0, self.niebieski)
        arc(self.x, self.y, 150, 150, self.start, self.stop, OPEN)
        if self.niebieski > 200 or self.niebieski < 50: self.kierunek *= -1
        popMatrix()

def setup():
    size(1200, 1200)
    background(0)
    global pierwszy, drugi, trzeci
    pierwszy = Kreciolek(200, 200, 100)
    drugi = Kreciolek(500, 500, 150)
    trzeci = Kreciolek(500, 200, 500)

def draw():
    pierwszy.sketch()
    drugi.sketch()
    trzeci.sketch()
    
#2pkt

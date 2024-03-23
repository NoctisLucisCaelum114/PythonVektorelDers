import pgzrun
from pgzero.actor import Actor
WIDTH = 300
HEIGHT = 200
TITLE = "UZAYLI"
# kodlar
karakter = Actor('uzayli',(50,240))
arkaplan = Actor('arkaplan',(50,240))
def draw():
    arkaplan.draw()
    karakter.draw()
def update():
    karakter.x +=5
    if karakter.x > 600:
        karakter.x = -50
        karakter.angle += -1
pgzrun.go()
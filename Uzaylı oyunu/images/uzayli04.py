import pgzrun
from pgzero.actor import Actor
# from keyboard import is_pressed
WIDTH = 600
HEIGHT = 300
TITLE = "UZAYLI"
karakter = Actor('uzayli',(50,240))
kutu = Actor('box',(650,260))
ari = Actor('ari',(750,100))
arkaplan = Actor('uzayli_arkaplan')
def draw():
    arkaplan.draw()
    karakter.draw()
    kutu.draw()
    ari.draw()

def update():
    kutu.x -= 4
    if kutu.x < 00: kutu.x = 650
    kutu.angle += 3
    ari.x -=3
    if ari.x < 0: ari.x = 750


if keyboard.left:
            karakter.x -= 5
if keyboard.right:
     karakter.x += 5
        
if keyboard.space:
    karakter.y = 100
    animate(karakter, tween='bounce_end', duration=1, y=240)

pgzrun.go()

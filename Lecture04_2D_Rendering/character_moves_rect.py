from pico2d import *


def bottomgaro():
    x = 0
    while x<800:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x += 2
        delay(0.01)

def rightsero():
    y = 90
    while y<570:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(790,y)
        y += 2
        delay(0.01)

def upgaro():
    x = 799
    while x>0:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,569)
        x -= 2
        delay(0.01)

def leftsero():
    y = 570
    while y>90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,y)
        y -= 2
        delay(0.01)

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
while(True):
    bottomgaro()
    rightsero()
    upgaro()
    leftsero()


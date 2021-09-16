from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')



def drawcircle():
    theta=0
    r=200
    while theta <360:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400+r*math.cos(math.radians(theta)),330+r*math.sin(math.radians(theta)))
        theta+=1
        delay(0.01)

    
while(True):
    drawcircle()

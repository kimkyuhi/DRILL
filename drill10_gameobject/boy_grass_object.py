from pico2d import *
import random

class Ball:

    def __init__(self):
        self.x, self.y, self.small_y = random.randint(0, 700), 599, 599
        self.image_small = load_image('ball21x21.png')
        self.image_big = load_image('ball41x41.png')
    def update(self):
        if self.y > 60:
            self.y -= random.randint(1, 10)
        if self.small_y > 50:
            self.small_y -= random.randint(1, 8)
        self.frame = 0

    def draw_small(self):
        self.image_small.clip_draw(self.frame * 21, 0, 21, 21, self.x, self.small_y)

    def draw_big(self):
        self.image_big.clip_draw(self.frame * 41, 0, 41, 41, self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.image = load_image('run_animation.png')
        self.frame = 0

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1)% 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
grass = Grass() # 생성.
team = [Boy() for i in range(1, 11+1)]
ball_big = [Ball() for i in range(1, 21+1)]
ball_small = [Ball() for i in range(1, 21+1)]

running = True
# game main loop code
while running:
    handle_events()

    #game logic
    for boy in team:
        boy.update()
    for bigball in ball_big:
        bigball.update()
    for smallball in ball_small:
        smallball.update()
    #game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for bigball in ball_big:
        bigball.draw_big()
    for smallball in ball_small:
        smallball.draw_small()

    update_canvas()
# finalization code
close_canvas()
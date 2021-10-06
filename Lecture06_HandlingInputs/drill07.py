from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    global dir
    global remx, remy, makeslowx, makeslowy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            if remx > x:
                dir = -1
                makeslowx = remx
                makeslowy = remy
                remx = x
                remy = y
            else:
                dir = 1
                makeslowx = remx
                makeslowy = remy
                remx = x
                remy = y

            x, y = event.x, KPU_HEIGHT - 1 - event.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
character_left = load_image('run_left_animation.png')

cursor = load_image('hand_arrow.png')

dir = 0
running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
remx = 0
remy = 0
makeslowx = 0
makeslowy = 0
frame = 0
hide_cursor()
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.draw(x, y)
    if dir > 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, makeslowx, makeslowy)
    else:
        character_left.clip_draw(frame * 100, 0, 100, 100, makeslowx, makeslowy)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()

close_canvas()





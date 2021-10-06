from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    global ax, ay
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            ax, ay = event.x, KPU_HEIGHT - 1 - event.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def update_character():
    global x, y
    global running_right

    running_right = x < ax
    x = (1 - 0.005) * x + 0.05 * ax
    y = (1 - 0.005) * y + 0.05 * ay

open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
running_right = True

x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
ax, ay = KPU_WIDTH * 2 // 3, KPU_HEIGHT * 2 // 3
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if running_right:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    cursor.draw(ax, ay)
    update_canvas()
    frame = (frame + 1) % 8
    update_character()
    handle_events()

close_canvas()





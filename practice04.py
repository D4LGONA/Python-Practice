import random

from pico2d import *

Background_WIDTH, Background_HEIGHT = 730, 400


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False  # 게임 종료
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False  # esc 게임 종료


open_canvas(Background_WIDTH, Background_HEIGHT)
tuk_ground = load_image('background.png')
character = load_image('animation_sheet.png')
cursor = load_image('mouse.png')

running = True
x = Background_WIDTH // 2
y = Background_HEIGHT // 2
frame = 0
frame_number = 0
cursorX = random.randint(10, 720)
cursorY = random.randint(10, 390)
hide_cursor()

while running:
    clear_canvas()
    tuk_ground.draw(Background_WIDTH // 2, Background_HEIGHT // 2)
    character.clip_draw(frame * 961 // 10, frame_number * (832 // 8), 961 // 10, 832 // 8, x, y)
    if cursorX == x and cursorY == y:
        cursorX = random.randint(10, 720)
        cursorY = random.randint(10, 390)
    else:
        if cursorX > x:
            x += 1
            frame_number = 0
        elif cursorX < x:
            x -= 1
            frame_number = 2
        elif cursorY > y:
            y += 1
            frame_number = 1
        elif cursorY < y:
            y -= 1
            frame_number = 3
    cursor.draw(cursorX, cursorY, 20, 20)

    update_canvas()
    frame = (frame + 1) % 10

    handle_events()
    delay(0.03)

close_canvas()

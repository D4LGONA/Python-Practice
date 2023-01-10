from pico2d import *


def handle_events():
    global running
    global dirX
    global dirY
    global frame_number
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False  # 게임 종료
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX += 1
                frame_number = 0
            elif event.key == SDLK_LEFT:
                dirX -= 1
                frame_number = 2

            if event.key == SDLK_UP:
                dirY += 1
                frame_number = 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
                frame_number = 3

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
            elif event.key == SDLK_LEFT:
                dirX += 1

            if event.key == SDLK_UP:
                dirY -= 1
            elif event.key == SDLK_DOWN:
                dirY += 1


open_canvas(730, 408)
grass = load_image('background.png')
character = load_image('animation_sheet.png')

running = True
x = 730 // 2
y = 408 // 2
frame = 0
dirX = 0
dirY = 0
frame_number = 0

while running and 730 > x > 0 and 408 > y > 0:
    clear_canvas()
    grass.draw(730 // 2, 408 // 2)
    character.clip_draw(frame * 961 // 10, frame_number * (832 // 8), 961 // 10, 832 // 8, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 10
    x += dirX * 5
    y += dirY * 5
    delay(0.02)

close_canvas()

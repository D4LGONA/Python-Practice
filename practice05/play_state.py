import game_framework
from pico2d import *
import item_state

character = None
character2 = None
bg = None
item = None
ball21 = None
ball41 = None
bItem = False
frame = 0
b21 = False
b41 = False


def enter():
    global character
    global character2
    global bg
    global item
    global ball41
    global ball21
    character = load_image('run_animation.png')
    character2 = load_image('character.png')
    bg = load_image('grass.png')
    item = load_image('item_state.png')
    ball21 = load_image('ball21X21.png')
    ball41 = load_image('ball41X41.png')


def exit():
    global character
    global character2
    global bg
    global item
    global ball41
    global ball21
    del character
    del character2
    del bg
    del item
    del ball41
    del ball21


def update():
    pass


def handle_events():
    global bItem
    global b41
    global b21
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_e):
            bItem = True
            b21 = False
            b41 = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_0):
            bItem = False
            b21 = False
            b41 = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
            bItem = False
            b21 = True
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
            bItem = False
            b41 = True


def draw():
    global frame
    clear_canvas()
    bg.draw(400, 25)
    if bItem:
        character2.draw(200, 90)
        item.draw(400, 300)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, 200, 90)
        frame = (frame + 1) % 10
        delay(0.03)
        if b21:
            ball21.draw(200, 130)
        elif b41:
            ball41.draw(200, 150)

    update_canvas()

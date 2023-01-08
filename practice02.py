from pico2d import *

open_canvas()

grass = load_image('grass.png')
#character = load_image('character.png')
character = load_image('run_animation.png')

#character.draw(100, 100)
#character.draw(200, 200)
x = 0
frame = 0
while x < 800:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    #character.draw(x, 90)
    frame = (frame + 1) % 10
    x += 8
    update_canvas()
    delay(0.05)

close_canvas()
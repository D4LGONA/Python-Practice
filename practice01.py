from pico2d import *

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

grass.draw_now(400, 30)

#for x in range(0,9):
#    for y in range(0,7):
#        character.draw_now(x*100, y*100)

x = 0
while (x<800):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x,90)
    x = x + 2
    delay(0.01)

close_canvas()

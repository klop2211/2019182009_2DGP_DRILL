from pico2d import *
# c++ namespace와 유사한 기능
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while(True):
    #원 운동
    seta = 270
    while(seta < 630):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(math.cos(seta / 360 * 2 * math.pi) * 240 + 400 ,math.sin(seta / 360 * 2 * math.pi) * 240 + 330)
        seta += 1
        delay(0.01)
    #사각형 운동
    x = 400
    while(x < 780):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x ,90)
        x += 3
        delay(0.01)
    y = 90         
    while(y < 560):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x ,y)
        y += 3
        delay(0.01)
    while(x > 20):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x ,y)
        x -= 3
        delay(0.01)
    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y -= 3
        delay(0.01)
    while(x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x ,90)
        x += 3
        delay(0.01)
    

close_canvas()

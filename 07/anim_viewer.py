from pico2d import *
open_canvas()

img = load_image('drill_07_img.png')
# 행(맨아래가 0), 시작하는 칸, 프레임 갯수
motion = {'draw_sword' : (8, 0, 5), 'put_sword' : (8, 6, 4), 'attack' : (7, 0, 5), 'die' : (6, 0, 6), 'climb' : (4, 0, 8), 'walk' : (3,0,8), 'walk_with_sword' : (2, 0, 8), 'run': (1, 0, 10), 'run_with_sword': (0, 0, 10)}

def ani(row, start, count):
    for frame in range(start, start + count):
        clear_canvas()
        img.clip_draw(0 + frame * 128, row * 128, 128, 128, 400, 300)
        update_canvas()
        delay(0.2)
        get_events()

while True:
    for i in motion:
        ani(*motion[i])

close_canvas()

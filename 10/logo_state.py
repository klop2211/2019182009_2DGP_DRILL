from pico2d import *
import game_framework
import play_state
image = None
logo_time = None
# fill here

def enter():
    global image, logo_time
    image = load_image('tuk_credit.png')
    logo_time = 0.0
    pass

def exit():
    global image
    del image

def update():
    global logo_time
    if logo_time > 10.0:
        game_framework.change_state(play_state)
    delay(0.01)
    logo_time += 0.1

def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass

def handle_events():
    events = get_events()






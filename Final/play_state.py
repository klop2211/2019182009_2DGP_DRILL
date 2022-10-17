import game_framework
from pico2d import *

back_ground = None

def enter():
    global back_ground
    back_ground = load_image('./Resource\ice_tile\BGLayer_0 #218364.png')

def update():
    pass

def draw():
    clear_canvas()
    back_ground.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

def exit():
    pass

def pause():
    pass

def resume():
    pass



if __name__ == '__main__':
    open_canvas()
    game_framework.run(__name__)
    close_canvas()
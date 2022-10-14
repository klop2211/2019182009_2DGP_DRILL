import game_framework
import add_delete_state
from boy_grass_object import *

boys = []
grass = None
running = None

# 초기화
def enter():
    global boys, grass, running
    boys += [Boy()]
    grass = Grass()
    running = True

# 종료
def exit():
    global boys, grass
    del boys
    del grass

def pause():
    pass

def resume():
    pass

def update():
    global boys
    for boy in boys:
        boy.update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    grass.draw()
    global boys
    for boy in boys:
        boy.draw()


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_b:
                    game_framework.push_state(add_delete_state)

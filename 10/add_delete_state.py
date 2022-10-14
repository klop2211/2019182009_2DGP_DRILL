import play_state
import game_framework
from boy_grass_object import *

image = None

# 초기화
def enter():
    global image
    image = load_image('add_delete_boy.png')

# 종료
def exit():
    global image
    del image

def update():
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_a:
                    play_state.boys += [Boy()]
                    game_framework.pop_state()
                case pico2d.SDLK_s:
                    play_state.boys.pop()
                    game_framework.pop_state()
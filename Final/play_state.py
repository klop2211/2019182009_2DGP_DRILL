import game_framework
import Camera
import Map_object
from pico2d import *

camera = None
map = None

def enter():
    global map, camera
    map = Map_object.Map()
    camera = Camera.Camera()

def update():
    pass

def draw():
    clear_canvas()
    map.draw(camera.x, camera.y)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_UP:
                    camera.move(0, 50)
                case pico2d.SDLK_DOWN:
                    camera.move(0, -50)
                case pico2d.SDLK_LEFT:
                    camera.move(-50, 0)
                case pico2d.SDLK_RIGHT:
                    camera.move(50, 0)


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
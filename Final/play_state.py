import game_framework
import Camera
import Map_object
import UI_object
from pico2d import *

camera = None
map = None
minimap = None

def enter():
    global map, camera, minimap
    map = Map_object.Map()
    camera = Camera.Camera()
    minimap = UI_object.Minimap()

def update():
    pass

def draw():
    global map, camera, minimap
    clear_canvas()
    map.draw(camera.x, camera.y)
    minimap.draw(map.map_num)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                # 카메라 이동을 위한 임시 문장
                case pico2d.SDLK_UP:
                    camera.move(0, 50)
                case pico2d.SDLK_DOWN:
                    camera.move(0, -50)
                case pico2d.SDLK_LEFT:
                    camera.move(-50, 0)
                case pico2d.SDLK_RIGHT:
                    camera.move(50, 0)
                # 맵 이동을 위한 임시 문장
                case pico2d.SDLK_1:
                    map.map_num = 0
                case pico2d.SDLK_2:
                    map.map_num = 1
                case pico2d.SDLK_3:
                    map.map_num = 2
                case pico2d.SDLK_4:
                    map.map_num = 3



def exit():
    del map, minimap, camera

def pause():
    pass

def resume():
    pass



if __name__ == '__main__':
    open_canvas()
    game_framework.run(__name__)
    close_canvas()
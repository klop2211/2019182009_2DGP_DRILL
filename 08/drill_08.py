from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dx, dy
    global state
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                state = 'left_run'
                dx = -1
            elif event.key == SDLK_RIGHT:
                state = 'right_run'
                dx = 1
            elif event.key == SDLK_UP:
                if state == 'right_stay':
                    state = 'right_run'
                elif state == 'left_stay':
                    state = 'left_run'
                dy = 1
            elif event.key == SDLK_DOWN:
                if state == 'right_stay':
                    state = 'right_run'
                elif state == 'left_stay':
                    state = 'left_run'
                dy = -1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                state = 'left_stay'
                dx = 0
            elif event.key == SDLK_RIGHT:
                state = 'right_stay'
                dx = 0
            elif event.key == SDLK_UP:
                if state == 'right_run':
                    state = 'right_stay'
                elif state == 'left_stay':
                    state = 'left_stay'
                dy = 0
            elif event.key == SDLK_DOWN:
                if state == 'right_run':
                    state = 'right_stay'
                elif state == 'left_stay':
                    state = 'left_stay'
                dy = 0


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
dx, dy = 0, 0
frame = 0
locate = { 'left_run' : 0, 'right_run' : 1, 'left_stay' : 2, 'right_stay' : 3}
state = 'left_stay'
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * locate[state], 100, 100, x, y)
    x += dx * 5
    y += dy * 5
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.01)

    handle_events()

close_canvas()
from pico2d import *
import random
import game_framework
import game_world

class RUN:
    def enter(self, event):
        print('ENTER Bird')

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir

    def do(self):
        self.frame_x = (self.frame_x + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
        if int(self.frame_x) == 4:
            self.frame_x = 0
            self.frame_y = self.frame_y + 1 % 3
        if self.frame_x == 4 and self.frame_y == 4:
            self.frame_y, self.frame_x = 0, 0

        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

        if self.x > 1550:
            self.dir *= -1
        if self.x < 0:
            self.dir *= -1

    def draw(self):
        # print('draw bird')
        if self.dir == 1:
            self.image.clip_draw(int(self.frame_x)*self.frame_size_w, 0, self.frame_size_w, self.frame_size_h - 1, self.x, self.y, 100, 100)
        elif self.dir == -1:
            self.image.clip_composite_draw(int(self.frame_x)*self.frame_size_w, 0, self.frame_size_w, self.frame_size_h - 1, 0, 'h', self.x, self.y ,100 , 100)


PIXEL_PER_METER = 10 / 0.3
RUN_SPEED_KPH = 60
RUN_SPEED_MPM = RUN_SPEED_KPH * 1000.0 / 60
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:

    def __init__(self):
        self.x, self.y = random.randint(100, 1500), random.randint(100, 200)
        self.frame_x = random.randint(0, 4)
        self.frame_y = 0

        self.dir, self.face_dir = 1, 1
        self.image = load_image('bird_animation.png')
        self.frame_size_w = self.image.w // 5 - 1
        self.frame_size_h = self.image.h // 3


        self.event_que = []
        self.cur_state = RUN
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        # if self.event_que:
        #     event = self.event_que.pop()
        #     self.cur_state.exit(self, event)
        #     try:
        #         self.cur_state = next_state[self.cur_state][event]
        #     except KeyError:
        #         print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
        #     self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        # self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f})', (255, 255, 0))

    # def add_event(self, event):
    #     self.event_que.insert(0, event)
    #
    # def handle_event(self, event):
    #     if (event.type, event.key) in key_event_table:
    #         key_event = key_event_table[(event.type, event.key)]
    #         self.add_event(key_event)

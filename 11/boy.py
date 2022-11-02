from pico2d import *

# 이벤트 정의
RD, LD, RU, LU, TIMER, aD = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): aD
}

class SLEEP:
    @staticmethod
    def enter(self, event):
        print('SLEEP_enter')
        self.dir = 0

    @staticmethod
    def exit(self):
        print('SLEEP_exit')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592 / 2, '', self.x, self.y, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592 / 2, '', self.x, self.y, 100, 100)

# 클래스를 이용해서 상태를 만듬.
class IDLE:
    @staticmethod
    def enter(self, event):
        print('idle_enter')
        self.dir = 0
        # 타이머 설정
        self.timer = 1000

    @staticmethod
    def exit(self):
        print('idle_exit')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            # 이벤트 발생
            # self.q.insert(0, TIMER) # 객체지향 프로그래밍 위배
            self.add_event(TIMER) # 객체지향적인 방법

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


class RUN:
    @staticmethod
    def enter(self, event):
        print('run_enter')
        if event == RD: self.dir += 1
        elif event == LD: self.dir -= 1
        elif event == RU: self.dir -= 1
        elif event == LU: self.dir += 1

    @staticmethod
    def exit(self):
        print('run_exit')
        # run 을 나가서, idle 로 갈 때, run의 방향을 알려줄 필요가 있다.
        self.face_dir = self.dir

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        print('run_do')

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class AUTO_RUN:
    @staticmethod
    def enter(self, event):
        print('autorun_enter')
        self.dir = self.face_dir

    @staticmethod
    def exit(self):
        print('autorun_exit')
        # run 을 나가서, idle 로 갈 때, run의 방향을 알려줄 필요가 있다.
        self.face_dir = self.dir
        self.dir = 0

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        if self.x == 0 or self.x == 800:
            self.dir *= -1
        print('autorun_do')

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y + 40, 200, 200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y + 40, 200, 200)



next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, aD:AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE, aD:AUTO_RUN},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, aD:IDLE},
    AUTO_RUN: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, aD:IDLE}
}


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')
        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)
        if self.q: # q에 뭔가 있다면
            event = self.q.pop() # 이벤트를 가져오고
            self.cur_state.exit(self) # 현재 상태를 나가고
            self.cur_state = next_state[self.cur_state][event] # 다음상태를 계산하고
            self.cur_state.enter(self, event)
        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)
        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event): # 소년이 스스로 이벤트 처리
        # event 는 키 이벤트 .. 변환이 필요
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event) # 변환된 이벤트를 큐에 추가


        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1

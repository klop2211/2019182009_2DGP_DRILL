from pico2d import *

# 주인공 : 크기 (40,40)
class Hero:
    def __init__(self):
        self.idle_left = load_image('./Resource/Char/CharIdle_L')
        self.idle_right = load_image('./Resource/Char/CharIdle_R')
        self.run_left = load_image('./Resource/Char/CharRun_L')
        self.run_right = load_image('./Resource/Char/CharRun_R')
        self.jump = load_image('./Resource/Char/CharJump0')
        self.die = load_image('./Resource/Char/CharDie')
        self.jump = load_image('./Resource/Char/CharHand0')
        self.x = int()
        self.y = int()

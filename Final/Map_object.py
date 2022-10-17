from pico2d import *


class Map:
    def __init__(self):
        self.left = load_image('./Resource\ice_tile\Ice_Connect_0.png')
        self.right = load_image('./Resource\ice_tile\Ice_Connect_1.png')
        self.top = load_image('./Resource\ice_tile\Ice_H_Type2_1.png')
        self.bottom = load_image('./Resource\ice_tile\Ice_H_Type2_7.png')
        self.back_ground = load_image('./Resource\ice_tile\BGLayer_0 #218364.png')
    def draw(self, x, y):
        self.back_ground.clip_draw(0, 0, self.back_ground.w, self.back_ground.h, x + 500, y + 400, 1000, 800)
        # 왼쪽벽
        for right in range(0, 800, 20):
            self.right.clip_draw(0, 0, self.right.w, self.right.h, x + 20, y + 20 + right, 40, 40)



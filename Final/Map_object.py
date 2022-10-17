from pico2d import *


class Map:
    def __init__(self):
        self.width = 1200
        self.height = 800
        self.left = load_image('./Resource\ice_tile\Ice_H_Type2_3.png')
        self.right = load_image('./Resource\ice_tile\Ice_H_Type2_5.png')
        self.top = load_image('./Resource\ice_tile\Ice_H_Type2_1.png')
        self.top_left_corner = load_image('./Resource\ice_tile\Ice_H_Type2_9.png')
        self.top_right_corner = load_image('./Resource\ice_tile\Ice_H_Type2_10.png')
        self.bottom = load_image('./Resource\ice_tile\Ice_H_Type2_7.png')
        self.bot_right = load_image('./Resource\ice_tile\Ice_H_Type2_8.png')
        self.bot_right_corner = load_image('./Resource\ice_tile\Ice_H_Type2_12.png')
        self.back_ground = load_image('./Resource\ice_tile\BGLayer_0 #218364.png')

    def draw(self, x, y):
        self.back_ground.clip_draw(0, 0, self.back_ground.w, self.back_ground.h,
                                   x + self.width // 2, y + self.height // 2, self.width, self.height)
        # 왼쪽, 오른쪽 벽
        for dy in range(0, self.height, 40):
            # 왼쪽
            if dy >= 280:
                self.right.clip_draw(0, 0, self.right.w, self.right.h, x + 20, y + 20 + dy, 40, 40)
            if dy == 240:
                self.bot_right.clip_draw(0, 0, self.bot_right.w, self.bot_right.h, x + 20, y + 20 + dy, 40, 40)
            # 오른쪽
            self.left.clip_draw(0, 0, self.left.w, self.left.h, x + 20 + self.width - 40, y + 20 + dy, 40, 40)
        # 위, 아래 벽
        for dx in range(0, self.width, 40):
            # 아래
            self.top.clip_draw(0, 0, self.top.w, self.top.h, x + 20 + dx, y + 20, 40, 40)
            if dx == self.width - 40:
                self.bot_right_corner.clip_draw(0, 0, self.bot_right_corner.w, self.bot_right_corner.h, x + 20 + dx, y + 20, 40, 40)
            # 위
            self.bottom.clip_draw(0, 0, self.bottom.w, self.bottom.h, x + 20 + dx, y + 20 + 760, 40, 40)
            if dx == 0:
                self.top_left_corner.clip_draw(0, 0, self.top_left_corner.w, self.top_left_corner.h, x + 20 + dx, y + 20 + self.height - 40, 40, 40)
            if dx == self.width - 40:
                self.top_right_corner.clip_draw(0, 0, self.top_right_corner.w, self.top_right_corner.h, x + 20 + dx, y + 20 + self.height - 40, 40, 40)




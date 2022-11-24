from pico2d import *
from random import randint

import game_world
import server


class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = randint(21, 1812), randint(21, 1109 - 21)

    def update(self):
        pass

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        Ball.image.draw(sx, sy)

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
    
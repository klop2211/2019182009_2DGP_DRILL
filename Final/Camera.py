class Camera:
    def __init__(self):
        self.x = 400
        self.y = 400

    def move(self, dx, dy):
        self.x -= dx
        if self.x <= 300:
            self.x = 300
        elif self.x >= 500:
            self.x = 500
        self.y -= dy
        if self.y <= 200:
            self.y = 200
        elif self.y >= 400:
            self.y = 400

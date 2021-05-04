import random


class Dead:
    def __init__(self):
        self.x_dead = range(90, 900, 30)
        self.y_dead = range(90, 600, 30)
        self.long = 0
        self.dead_y1, self.dead_y2 = random.choice(self.y_dead), random.choice(self.y_dead)
        self.dead_x1, self.dead_x2 = random.choice(self.x_dead), random.choice(self.x_dead)
        self.guess_y1, self.guess_y2 = random.choice(self.y_dead), random.choice(self.y_dead)
        self.guess_x1, self.guess_x2 = random.choice(self.x_dead), random.choice(self.x_dead)

    def set_dead(self):
        self.dead_y1, self.dead_y2 = self.guess_y1, self.guess_y2
        self.dead_x1, self.dead_x2 = self.guess_x1, self.guess_x2
        self.guess_y1, self.guess_y2 = [random.choice(self.y_dead), random.choice(self.y_dead)]
        self.guess_x1, self.guess_x2 = [random.choice(self.x_dead), random.choice(self.x_dead)]

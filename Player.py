import pygame


class Player:
    def __init__(self):
        self.x = 30
        self.y = 30
        self.move_time = 1

    def reset(self, sets):
        self.x = 30
        self.y = 30
        self.move_time -= 1
        if self.move_time <= 0:
            self.move_time = 1
        if not sets.ds:
            sets.brave = 1

    def draw(self, sets):
        if sets.brave == 0:
            pygame.draw.rect(sets.screen, [0, 0, 0], [self.x + 1, self.y + 1, 28, 28])
        else:
            pygame.draw.rect(sets.screen, [237, 112, 129], [self.x + 1, self.y + 1, 28, 28])

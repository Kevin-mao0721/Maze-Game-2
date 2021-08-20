import pygame


class Player:
    def __init__(self):
        self.x = 30
        self.y = 30
        self.blood = 1
        self.move_time = 1
        self.brave = 1
        self.brave_time = -100000

    def reset(self, sets):
        self.x = 30
        self.y = 30
        if not sets.ds:
            self.brave = 1

    def draw(self, sets):
        if self.brave == 0:
            pygame.draw.rect(sets.screen, [0, 0, 0], [self.x + 1, self.y + 1, 28, 28])
        else:
            pygame.draw.rect(sets.screen, [237, 112, 129], [self.x + 1, self.y + 1, 28, 28])

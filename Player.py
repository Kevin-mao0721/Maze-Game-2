import pygame


class Player:
    def __init__(self):
        self.x = 30
        self.y = 30

    def reset(self):
        self.x = 30
        self.y = 30

    def draw(self, sets):
        if sets.brave == 0:
            pygame.draw.rect(sets.screen, [0, 0, 0], [self.x + 1, self.y + 1, 28, 28])
        else:
            pygame.draw.rect(sets.screen, [237, 112, 129], [self.x + 1, self.y + 1, 28, 28])

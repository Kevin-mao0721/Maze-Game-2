import random

import pygame


class Dead:
    def __init__(self):
        self.x_dead = range(90, 900, 30)
        self.y_dead = range(90, 600, 30)

        self.level_set = {1: [1, 0],
                          2: [1.5, 1],
                          3: [2, 2],
                          4: [2.5, 2],
                          5: [3.5, 2],
                          6: [4.5, 2],
                          7: [6, 3]
                          }
        self.level_set_wujin = [1, 1]

        self.x_dead_list = []
        self.y_dead_list = []

        self.x_guess_list = []
        self.y_guess_list = []

        self.long = 0

    def f_set_dead(self, sets):
        if sets.xh == '正常':
            for i in range(self.level_set[sets.level][1]):
                self.y_dead_list.append(random.choice(self.y_dead))
                self.x_dead_list.append(random.choice(self.x_dead))
                self.y_guess_list.append(random.choice(self.y_dead))
                self.x_guess_list.append(random.choice(self.x_dead))
        else:
            for i in range(self.level_set_wujin[1]):
                self.y_dead_list.append(random.choice(self.y_dead))
                self.x_dead_list.append(random.choice(self.x_dead))
                self.y_guess_list.append(random.choice(self.y_dead))
                self.x_guess_list.append(random.choice(self.x_dead))

    def set_dead(self, sets):
        self.x_guess_list = []
        self.y_guess_list = []
        if sets.xh == '正常':
            for i in range(self.level_set[sets.level][1]):
                self.y_guess_list.append(random.choice(self.y_dead))
                self.x_guess_list.append(random.choice(self.x_dead))
        else:
            for i in range(self.level_set_wujin[1]):
                self.y_guess_list.append(random.choice(self.y_dead))
                self.x_guess_list.append(random.choice(self.x_dead))

    def draw_all(self, sets):
        if sets.xh == '正常':
            for i in range(self.level_set[sets.level][1]):
                self.draw(sets, i)
        else:
            for i in range(self.level_set_wujin[1]):
                self.draw(sets, i)

        if not self.long > 1290:
            if sets.xh == '正常':
                self.long += self.level_set[sets.level][0]
            else:
                self.long += self.level_set_wujin[0]
        else:
            self.long = 0
            self.change()
            self.set_dead(sets)

    def change(self):
        self.x_dead_list = []
        self.y_dead_list = []
        self.y_dead_list = self.y_guess_list
        self.x_dead_list = self.x_guess_list

    def draw(self, sets, i):
        pygame.draw.rect(sets.screen, [254, 0, 0], [0, self.y_dead_list[i], self.long, 30])
        pygame.draw.rect(sets.screen, [254, 0, 0], [self.x_dead_list[i], 0, 30, self.long])
        pygame.draw.rect(sets.screen, [253, 180, 180], [0, self.y_guess_list[i], 30, 30])
        pygame.draw.rect(sets.screen, [253, 180, 180], [self.x_guess_list[i], 0, 30, 30])

    def reset_wujin(self, sets):
        self.level_set_wujin = []
        self.level_set_wujin.append(int(sets.level * random.uniform(0.5, 1.25)) + 1)
        self.level_set_wujin.append(int(sets.level / 3) + 1)

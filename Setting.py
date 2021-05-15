import pygame, mazeData

pygame.init()


class Setting():
    def __init__(self):
        self.screen = pygame.display.set_mode([1300, 690])
        pygame.display.set_caption('迷宫挑战')
        surface = pygame.image.load('image/maze.jpg').convert_alpha()
        pygame.display.set_icon(surface)

        f = open('best_step_n.txt', 'r')
        self.best_step_n = f.readlines()
        f.close()

        num = len(self.best_step_n[0]) - 1
        self.best_step_n[0] = self.best_step_n[0][:num]

        self.maze = mazeData.Maze()

        self.text = pygame.font.SysFont("C:/Windows/Fonts/STZHONGS.TTF", 60)

        self.brave = 1
        self.brave_time = -100000
        self.step = 0
        self.time = 70000
        self.dead_time = 0
        self.level = 1

    def reset_maze(self):
        self.maze = mazeData.Maze()

    def reset_all(self):
        self.reset_maze()
        self.step = 0
        self.time = 70000
        self.dead_time = 0
        self.level = 1

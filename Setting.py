import pygame
import ybc_box as box

import mazeData

pygame.init()


class Setting:
    def __init__(self):
        self.screen = pygame.display.set_mode([1300, 690])
        pygame.display.set_caption('迷宫挑战')
        surface = pygame.image.load('image/maze.jpg').convert_alpha()
        pygame.display.set_icon(surface)

        self.maze = mazeData.Maze()

        self.text = pygame.font.SysFont("C:/Windows/Fonts/STZHONGS.TTF", 60)

        self.step = 0
        self.maze_clear = False
        self.time = 120000
        self.dead_time = 0
        self.level = 1
        self.code = "asdfghjkl;'"

        box.msgbox('↑↓←→操控\n\n碰到红色块（岩浆）死亡回到起点，每过一关都会获得技能')

        s = """请选择模式：
    正常：共7关
    无尽：无限关"""

        self.xh = box.buttonbox(s, ['正常', '无尽'])
        if self.xh is None:
            self.xh = '正常'
        self.ds = box.ynbox('是否开启调试？？？')

        if self.ds:
            an = box.passwordbox('请输入调式密码')
            if an == self.code:
                box.msgbox('密码正确，开启调试')
                self.ds = True
            else:
                box.msgbox('密码错误，无法调试')
                self.ds = False

        if self.xh == '正常':
            f = open('best_step_n.txt', 'r')
        else:
            f = open('best_step.txt', 'r')

        self.best_step_n = f.readlines()
        f.close()

        self.best_step_n[0] = self.best_step_n[0].strip()

    def reset_maze(self):
        self.maze = mazeData.Maze()

    def reset_all(self, xh, sets, dead):
        self.reset_maze()
        self.step = 0
        self.time = 70000
        self.dead_time = 0
        self.level = 1

        if xh == '无尽':
            dead.reset_wujin(sets)

    def draw_maze(self):
        if self.maze_clear:
            self.screen.fill([255, 255, 255])
        else:
            self.screen.fill([161, 207, 143])
        self.maze.draw(self.screen, self.maze_clear)

    def get_mark(self):
        if self.xh == '正常':
            f = open('best_step_n.txt', 'r')
        else:
            f = open('best_step.txt', 'r')

        self.best_step_n = f.readlines()
        self.best_step_n[0] = self.best_step_n[0].strip()
        f.close()

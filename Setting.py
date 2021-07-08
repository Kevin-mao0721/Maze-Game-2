import pygame, secret
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

        self.brave = 1
        self.brave_time = -100000
        self.step = 0
        self.time = 70000
        self.dead_time = 0
        self.level = 1
        self.code = '97707ae8e5a58e4a9575d09ce7f92d26966c7d25c07d68c9359e0a61433150e2e95728bd43efc31be6f4b27c23724fe0996316119e4e6c13efcdd1016a2c36c272361df2d700a33d38f501695054e14da15305d79123b0fbcef53f83b80735850ed'

        box.msgbox('↑↓←→操控\n\n碰到红色块（岩浆）死亡回到起点')

        self.xh = box.buttonbox('请选择模式', ['正常', '无尽'])
        if self.xh is None:
            self.xh = '正常'
        self.ds = box.ynbox('是否开启调试？？？')

        if self.ds:
            an = box.passwordbox('请输入调式密码')
            if secret.secret_question(an) != self.code:
                box.msgbox('密码错误，无法开启调试')
                self.ds = False

        if self.ds is None:
            self.ds = False

        if self.xh == '正常':
            f = open('best_step_n.txt', 'r')
        else:
            f = open('best_step.txt', 'r')

        self.best_step_n = f.readlines()
        f.close()

        num = len(self.best_step_n[0]) - 1
        self.best_step_n[0] = self.best_step_n[0][:num]

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
        self.screen.fill([161, 207, 143])
        self.maze.draw(self.screen)

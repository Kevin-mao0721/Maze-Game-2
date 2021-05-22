# 导入模块
import sys

import pygame
import ybc_box as box

import game_function as gf
from Player import Player
from Setting import Setting
from dead import Dead

sets = Setting()
player = Player()
dead = Dead()

# 初始化pygame并更改名字
# pygame.init()


# 重置岩浆河位置
dead.f_set_dead(sets)
# 主循环
while True:
    if sets.xh == '正常' or sets.xh == '调试' or True:
        if sets.level > 7 and sets.xh == '正常':
            break
        # 使用for循环遍历当前事件列表
        for event in pygame.event.get():
            # 判断【事件类型】是不是【按下键盘事件】
            if event.type == pygame.KEYDOWN:
                # 判断【事件按键】是不是【上移键】
                if event.key == pygame.K_UP:
                    gf.up_check(sets, player)
                # 判断【事件按键】是不是【下移键】
                elif event.key == pygame.K_DOWN:
                    gf.check_down(sets, player)
                # 判断【事件按键】是不是【左移键】
                elif event.key == pygame.K_LEFT:
                    gf.check_left(sets, player)
                # 判断【事件按键】是不是【右移键】
                elif event.key == pygame.K_RIGHT:
                    gf.check_right(sets, player)
                if sets.ds:
                    if event.key == pygame.K_s:
                        if sets.level != 7 or sets.xh == '无尽':
                            if sets.xh == '无尽':
                                dead.reset_wujin(sets)
                            sets.level += 1
                            player.reset()
                            dead.f_set_dead(sets)
                    if event.key == pygame.K_w:
                        if sets.brave == 1:
                            sets.brave = 0
                        else:
                            sets.brave = 1

            if event.type == pygame.QUIT:
                gf.check_win_n(sets)
                sys.exit()

        # 不动时检测岩浆触碰
        color1, color2, color3, color4 = gf.check_yjh(player.x, player.y, sets.screen)

        if sets.brave == 1:
            if color1[0] == 254 \
                    or color2[0] == 254 \
                    or color3[0] == 254 \
                    or color1[0] == 254:
                box.msgbox('你已死亡\n\n原因:触摸岩浆')
                player.x = 30
                player.y = 30
                sets.dead_time += 1
                if sets.dead_time % 2 == 0:
                    sets.reset_maze()

        # 填充背景色
        sets.screen.fill([161, 207, 143])

        # 绘制迷宫
        sets.maze.draw(sets.screen)

        # 更改岩浆河位置

        long_dead = 30

        # 预测岩浆河

        # 绘制方块
        if sets.brave == 0:
            pygame.draw.rect(sets.screen, [0, 0, 0], [player.x + 1, player.y + 1, 28, 28])
        else:
            pygame.draw.rect(sets.screen, [237, 112, 129], [player.x + 1, player.y + 1, 28, 28])

        # 绘制岩浆河
        dead.draw_all(sets)

        # 减少时间
        sets.time -= 1
        # 绘制字体
        now = str(sets.time / 100)
        words = sets.text.render(now, True, (230, 230, 230))
        sets.screen.blit(words, (1150, 20))

        # 绘制等级
        words = sets.text.render("L." + str(sets.level), True, (230, 230, 230))
        sets.screen.blit(words, (1157, 60))

        # 绘制最高纪录
        num = len(sets.best_step_n[0])
        words = sets.text.render(str(sets.best_step_n[0])[:num], True, (230, 230, 230))
        sets.screen.blit(words, (1157, 180))

        # 绘制最高纪录
        words = sets.text.render(str(sets.best_step_n[1]), True, (230, 230, 230))
        sets.screen.blit(words, (1157, 225))

        # 无敌时间计时⏲
        if sets.brave_time == 500:
            sets.brave_time = -100000
            sets.brave = 1
        elif sets.brave_time > -52222:
            sets.brave_time += 1

        # 检查是否到达终点
        if player.x == 1140 and player.y == 630:
            if sets.xh == '正常':
                if sets.level == 7:
                    if int(float(sets.best_step_n[1])) == 7:
                        box.msgbox('恭喜你突破了最高纪录')
                        f = open('best_step_n.txt', 'w')
                        f.write(str(sets.step) + '\n7.1')
                        f.close()
                    elif sets.step < int(sets.best_step_n[0]) and int(float(sets.best_step_n[1])) == 7:
                        box.msgbox('恭喜你突破了最高纪录' + '\n你的记录:' + str(sets.step) + '\n最高纪录:' + str(sets.best_step_n[0]))
                        f = open('best_step_n.txt', 'w')
                        f.write(str(sets.step) + '\n7.1')
                        f.close()
                    elif sets.step > int(sets.best_step_n[0]):
                        box.msgbox(
                            '恭喜你用了' + str(sets.step) + '步来通关\n距离最高纪录还差' + str(sets.step - int(sets.best_step_n[0])))
                    elif sets.step == int(sets.best_step_n[0]):
                        box.msgbox('恭喜你用了' + str(sets.step) + '\n你再少走一步就可以超过最高记录了')
                    sets.reset_all(sets.xh, sets, dead)
                else:
                    box.msgbox('下一关')
                    sets.level += 1
                    dead.f_set_dead(sets)
                player.reset()
            else:
                box.msgbox('下一关')
                sets.level += 1
                dead.f_set_dead(sets)
                player.reset()

        if sets.time == 0:
            gf.check_win_n(sets)
            sys.exit()

        # 更新窗口
        pygame.display.flip()

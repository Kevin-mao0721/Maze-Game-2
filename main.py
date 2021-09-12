# 导入模块
import pygame
import sys
import ybc_box as box
import game_function as gf
from Player import Player
from Setting import Setting
from dead import Dead
from Logger import Logger

sets = Setting()
player = Player()
dead = Dead()
log = Logger('Logging.log')

while True:
    try:
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
                                gf.tiao_shi(event, sets, dead, player)
                            if event.key == pygame.K_w:
                                if not player.brave:
                                    player.brave = True
                                else:
                                    player.brave = False
                        if player.move_time == 2:
                            if event.key == pygame.K_PAGEUP:
                                gf.pgUp(sets, player)
                            if event.key == pygame.K_PAGEDOWN:
                                gf.pgDn(sets, player)

                    if event.type == pygame.QUIT:
                        gf.check_win_n(sets)
                        sys.exit()

                # 不动时检测岩浆触碰
                gf.check_dead_dmove(player, sets)

                # 绘制迷宫、方块、岩浆河
                sets.draw_maze()
                player.draw(sets)
                dead.draw_all(sets)

                # 减少时间
                sets.time -= 1

                # 绘制所有纪录
                gf.draw_all(sets)

                # 无敌时间计时⏲
                if player.brave_time == 500:
                    player.brave_time = -100000
                    player.brave = 1
                elif player.brave_time > -52222:
                    player.brave_time += 1

                # 检查是否到达终点
                if player.x == 1140 and player.y == 630:
                    if sets.xh == '正常':
                        if sets.level == 7:
                            if float(sets.best_step_n[1]) <= 7:
                                gf.win1(sets)
                            elif sets.step < int(sets.best_step_n[0]):
                                gf.win2(sets)
                            elif sets.step > int(sets.best_step_n[0]):
                                gf.lose(sets)
                            elif sets.step == int(sets.best_step_n[0]):
                                gf.no_win(sets)
                            sets.reset_all(sets.xh, sets, dead)
                    if sets.maze.treasure_number == 1:
                        player.move_time = 2
                        box.msgbox('获得技能：加速')
                    elif sets.maze.treasure_number == 2:
                        player.blood += 2
                        box.msgbox('获得技能：加血')
                    elif sets.maze.treasure_number == 6:
                        player.brave = 0
                        box.msgbox('获得技能：天之眷顾')
                    elif sets.maze.treasure_number == 4:
                        if box.ynbox('是否需要清空屏幕服务？？？'):
                            sets.maze_clear = True
                            box.msgbox('获得技能：清空全幕')
                    elif sets.maze.treasure_number == 5:
                        if sets.level != 6:
                            if sets.xh == '正常':
                                sets.level = 6
                                box.msgbox('获得技能：直到最后一关！')
                            else:
                                sets.level += 9
                                box.msgbox('获得技能：直过十关！')
                    elif sets.maze.treasure_number == 6:
                        if sets.level != 6:
                            sets.level += 1
                            box.msgbox('获得技能：额外过一关！')
                    if sets.maze.treasure_number not in [5, 6]:
                        box.msgbox('下一关')
                    sets.level += 1
                    dead.f_set_dead(sets)
                    sets.reset_maze()
                    player.reset(sets)
                    if sets.xh == '无尽':
                        sets.time += 50
                    if sets.maze.treasure_number != 3:
                        sets.maze_clear = False
                if sets.time == 0:
                    gf.check_win_n(sets)
                    sys.exit()

                # 更新窗口
                pygame.display.flip()

    except Exception as e:
        box.msgbox('发现错误，信息为' + str(e))
        log.error('发现错误，信息为' + str(e))

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
                                if not sets.brave:
                                    sets.brave = True
                                else:
                                    sets.brave = False

                    if event.type == pygame.QUIT:
                        gf.check_win_n(sets)
                        sys.exit()

                # 不动时检测岩浆触碰
                gf.check_dead_dmove(player, sets)

                sets.draw_maze()

                # 绘制方块
                player.draw(sets)

                # 绘制岩浆河
                dead.draw_all(sets)

                # 减少时间
                sets.time -= 1

                # 绘制所有纪录
                gf.draw_all(sets)

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
                            if float(sets.best_step_n[1]) <= 7:
                                box.msgbox('恭喜你突破了最高纪录')
                                f = open('best_step_n.txt', 'w')
                                f.write(str(sets.step) + '\n8')
                                f.close()
                                sets.get_mark()
                            elif sets.step < int(sets.best_step_n[0]):
                                box.msgbox(
                                    '恭喜你突破了最高纪录' + '\n你的记录:' + str(sets.step) + '\n最高纪录:' + str(sets.best_step_n[0]))
                                f = open('best_step_n.txt', 'w')
                                f.write(str(sets.step) + '\n8')
                                f.close()
                                sets.get_mark()
                            elif sets.step > int(sets.best_step_n[0]):
                                box.msgbox(
                                    '恭喜你用了' + str(sets.step) + '步来通关\n距离最高纪录还差' + str(
                                        sets.step - int(sets.best_step_n[0])))
                            elif sets.step == int(sets.best_step_n[0]):
                                box.msgbox('恭喜你用了' + str(sets.step) + '\n你再少走一步就可以超过最高记录了')
                            sets.reset_all(sets.xh, sets, dead)
                        else:
                            box.msgbox('下一关')
                            sets.level += 1
                            dead.f_set_dead(sets)
                            sets.reset_maze()
                        player.reset()
                    else:
                        box.msgbox('下一关')
                        sets.level += 1
                        sets.time += 50
                        dead.f_set_dead(sets)
                        player.reset()
                        sets.reset_maze()

                if sets.time == 0:
                    gf.check_win_n(sets)
                    sys.exit()

                # 更新窗口
                pygame.display.flip()

    except Exception as e:
        box.msgbox('发现错误，信息为' + str(e))
        log.error('发现错误，信息为' + str(e))

import ybc_box as box
import pygame


def check_yjh(x, y, screen):
    # 不动时检测岩浆触碰
    try:
        color1 = screen.get_at([x + 10, y])
    except IndexError:
        color1 = [None, None, None]

    try:
        color2 = screen.get_at([x + 20, y])
    except IndexError:
        color2 = [None, None, None]

    try:
        color3 = screen.get_at([x + 29, y])
    except IndexError:
        color3 = [None, None, None]

    try:
        color4 = screen.get_at([x, y + 29])
    except IndexError:
        color4 = [None, None, None]

    return color1, color2, color3, color4


def dead_action(sets, player, because):
    box.msgbox(f'你已死亡\n\n原因:{because}')
    player.x = 30
    player.y = 30
    sets.dead_time += 1
    if sets.dead_time % 2 == 0:
        sets.reset_maze()


def check_win_n(sets):
    box.msgbox('你已死亡')
    if int(float(sets.best_step_n[1])) < sets.level:
        box.msgbox('恭喜你突破了最高纪录的等级')
        if sets.xh == '正常':
            f = open('best_step_n.txt', 'w')
        else:
            f = open('best_step.txt', 'w')
        f.write(str(sets.step) + '\n' + str(sets.level))
        f.close()

        sets.get_mark()
    elif int(float(sets.best_step_n[1])) == sets.level:
        if sets.step < int(sets.best_step_n[0]):
            box.msgbox('恭喜你突破了最高纪录的步数')
            if sets.xh == '正常':
                f = open('best_step_n.txt', 'w')
            else:
                f = open('best_step.txt', 'w')
            f.write(str(sets.step) + '\n' + str(sets.level))
            f.close()

            sets.get_mark()
        else:
            box.msgbox('很遗憾，您没有突破记录')
    else:
        box.msgbox('很遗憾，您没有突破记录')


def up_check(sets, player):
    for i in range(player.move_time):
        try:
            color = sets.screen.get_at([player.x, player.y - 30])
            if color[0] == 255 or color[0] == 253:
                player.y -= 30
                sets.step += 1
            elif sets.brave == 1:
                if color[0] == 254 and i != 0:
                    dead_action(sets, player, '触碰岩浆')
                elif sets.brave == 0 and color[0] != 161:
                    player.y = player.y - 30
                    sets.step += 1
        except IndexError:
            dead_action(sets, player, '离开地图')


def check_down(sets, player):
    for i in range(player.move_time):
        try:
            color = sets.screen.get_at([player.x, player.y + 30])
            if color[0] == 255 or color[0] == 253:
                player.y = player.y + 30
                sets.step += 1
            elif sets.brave == 1:
                if color[0] == 254:
                    if color[0] == 254 and i != 0:
                        dead_action(sets, player, '触碰岩浆')
            elif sets.brave == 0 and color[0] != 161:
                player.y += 30
                sets.step += 1
        except IndexError:
            dead_action(sets, player, '离开地图')


def check_right(sets, player):
    for i in range(player.move_time):
        try:
            color = sets.screen.get_at([player.x + 30, player.y])
            if color[0] == 255 or color[0] == 253:
                player.x = player.x + 30
                sets.step += 1
            elif sets.brave == 1:
                if color[0] == 254:
                    if color[0] == 254 and i != 0:
                        dead_action(sets, player, '触碰岩浆')
            elif sets.brave == 0 and color[0] != 161:
                player.x += 30
                sets.step += 1
        except IndexError:
            dead_action(sets, player, '离开地图')


def check_left(sets, player):
    for i in range(player.move_time):
        try:
            color = sets.screen.get_at([player.x - 30, player.y])
            if color[0] == 255 or color[0] == 253:
                player.x -= 30
                sets.step += 1
            elif sets.brave == 1:
                if color[0] == 254:
                    if color[0] == 254 and i != 0:
                        dead_action(sets, player, '触碰岩浆')
            elif sets.brave == 0 and color[0] != 161:
                player.x -= 30
                sets.step += 1
        except IndexError:
            dead_action(sets, player, '离开地图')


def draw_all(sets):
    now = str(sets.time / 100)
    words = sets.text.render(now, True, (230, 230, 230))
    sets.screen.blit(words, (1150, 20))

    words = sets.text.render("L." + str(sets.level), True, (230, 230, 230))
    sets.screen.blit(words, (1157, 60))

    words = sets.text.render("Best: ", True, (230, 230, 230))
    sets.screen.blit(words, (1157, 180))

    num = len(sets.best_step_n[0])
    words = sets.text.render(str(sets.best_step_n[0])[:num], True, (230, 230, 230))
    sets.screen.blit(words, (1157, 220))

    words = sets.text.render(str(sets.best_step_n[1]), True, (230, 230, 230))
    sets.screen.blit(words, (1157, 265))


def check_dead_dmove(player, sets):
    color1, color2, color3, color4 = check_yjh(player.x, player.y, sets.screen)

    if sets.brave == 1:
        if color1[0] == 254 \
                or color2[0] == 254 \
                or color3[0] == 254 \
                or color1[0] == 254:
            box.msgbox('你已死亡\n\n原因:触摸岩浆')
            player.reset()
            sets.dead_time += 1
            if sets.dead_time % 2 == 0:
                sets.reset_maze()


def tiao_shi(event, sets, dead, player):
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

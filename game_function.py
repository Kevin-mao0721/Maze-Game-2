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


def dead_action(sets, player):
    import ybc_box as box

    box.msgbox('你已死亡\n\n原因:触摸岩浆')
    player.x = 30
    player.y = 30
    sets.dead_time += 1
    if sets.dead_time % 2 == 0:
        sets.reset_maze()


def check_win_n(sets):
    box.msgbox('你已死亡\n原因:超时未通关')
    if int(sets.best_step_n[1]) < sets.level:
        box.msgbox('恭喜你突破了最高纪录的等级')
        f = open('best_step_n.txt', 'w')
        f.write(str(sets.step) + '\n' + str(sets.level))
        f.close()
    elif int(sets.best_step_n[1]) == sets.level:
        if sets.step > int(sets.best_step_n[0]):
            box.msgbox('恭喜你突破了最高纪录的步数')
            f = open('best_step_n.txt', 'w')
            f.write(str(sets.step) + '\n' + str(sets.level))
            f.close()
    else:
        box.msgbox('很抱歉，您没有突破记录')


def up_check(sets, player):
    color = sets.screen.get_at([player.x, player.y - 30])
    if color[0] == 255 or color[0] == 253:
        player.y -= 30
        sets.step += 1
    elif sets.brave == 1:
        if color[0] == 254:
            dead_action(sets, player)
        elif sets.brave == 0 and color[0] != 161:
            player.y = player.y - 30
            sets.step += 1


def check_down(sets, player):
    color = sets.screen.get_at([player.x, player.y + 30])
    if color[0] == 255 or color[0] == 253:
        player.y = player.y + 30
        sets.step += 1
    elif sets.brave == 1:
        if color[0] == 254:
            gf.dead_action(sets, player)
    elif sets.brave == 0 and color[0] != 161:
        player.y += 30
        sets.step += 1


def check_right(sets, player):
    color = sets.screen.get_at([player.x + 30, player.y])
    if color[0] == 255 or color[0] == 253:
        player.x = player.x + 30
        sets.step += 1
    elif sets.brave == 1:
        if color[0] == 254:
            gf.dead_action(sets, player)
    elif sets.brave == 0 and color[0] != 161:
        player.x + 30
        sets.step += 1


def check_left(sets, player):
    color = sets.screen.get_at([player.x - 30, player.y])
    if color[0] == 255 or color[0] == 253:
        player.x -= 30
        sets.step += 1
    elif sets.brave == 1:
        if color[0] == 254:
            gf.dead_action(sets, player)
    elif sets.brave == 0 and color[0] != 161:
        player.x - 30
        sets.step += 1

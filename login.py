from Login import Login
from Login import JsonSetting
import ybc_box as box

js_setting = JsonSetting('user_data.json')
login = Login(js_setting)
word = '欢迎进入迷宫游戏，请选择'
while True:
    dz_choice = box.buttonbox(word + '(按❌ / Cancel退出)', ['登录(请注意大小写)', '注册(不支持重复用户名)'])
    if dz_choice is None:
        box.msgbox('您已退出，回头见……！')
        exit()
    elif dz_choice == '登录(请注意大小写)':
        accepted, name, money = login.login()
        if accepted:
            box.msgbox('欢迎您，{0}，点击🆗马上开始游戏'.format(name))
            player_name = name
            player_dollar = int(money)
            break
        else:
            word = '很抱歉，登录失败，请重试'
            continue
    else:
        if login.registered():
            word = '注册成功！！请登录进入游戏'
            continue
        else:
            word = '很抱歉，注册失败(可能重名了)，请重试'
            continue

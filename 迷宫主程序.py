#导入模块
import pygame
import mazeData
import random
import ybc_box as box
import sys

#初始化pygame并更改名字
pygame.init()
screen = pygame.display.set_mode([1300, 690])
pygame.display.set_caption('迷宫挑战')

#初始化字体
text = pygame.font.SysFont("C:\Windows\Fonts\STZHONGS.TTF", 60)

#更改游戏图标
surface =  pygame.image.load('image\maze.jpg').convert_alpha()
pygame.display.set_icon(surface)

#初始化变量
x = 30
y = 30
long = 0
dead_y1,dead_y2 = random.choice(range(300,600,30)),random.choice(range(300,600,30))
dead_x1,dead_x2 = random.choice(range(300,1170,30)),random.choice(range(300,1170,30))
guess_y1,guess_y2 = random.choice(range(300,600,30)),random.choice(range(300,600,30))
guess_x1,guess_x2 = random.choice(range(300,900,30)),random.choice(range(300,900,30))
brave = 1
brave_time = -100000
step = 0
time = 20000
dead_time = 0



# 生成迷宫地图
maze = mazeData.Maze()

#设置闹钟
clock = pygame.time.Clock()

def set_dead():
	global dead_y1,dead_y2,dead_x1,dead_x2,guess_y1,guess_y2,guess_x1,guess_x2
	dead_y1,dead_y2 = guess_y1,guess_y2
	dead_x1,dead_x2 = guess_x1,guess_x2
	guess_y1,guess_y2 = random.choice(range(300,600,30)),random.choice(range(300,600,30))
	guess_x1,guess_x2 = random.choice(range(300,900,30)),random.choice(range(300,900,30))
	

#主循环
while True:
	print(guess_y1,guess_y2)
	
	# 使用for循环遍历当前事件列表
	for event in pygame.event.get():
		# 判断【事件类型】是不是【按下键盘事件】
		if event.type == pygame.KEYDOWN:
			# 判断【事件按键】是不是【上移键】
			if event.key == pygame.K_UP:
				color = screen.get_at([x, y - 30])
				color1 = screen.get_at([x, y])
				if color[0] == 255 or color[0] == 253:
					y = y - 30
					step += 1
				elif brave == 1:
					if color1[0] == 254:
						y = y - 30
						pygame.draw.rect(screen, [237, 112, 129], [x, y, 30, 30])
						pygame.display.flip()
						box.msgbox('你已死亡\n\n原因:触摸岩浆')
						x = 30
						y = 30
						brave = 0
						brave_time = 1
						dead_time += 1
						if dead_time % 2 == 0:
							maze = mazeData.Maze()
			# 判断【事件按键】是不是【下移键】
			elif event.key == pygame.K_DOWN:
				color = screen.get_at([x,y + 30])
				color1 = screen.get_at([x, y + 29])
				if color[0] == 255 or color[0] == 253:
					y = y + 30
					step += 1
				elif brave == 1:
					if color1[0] == 254:
						y = y + 30
						pygame.draw.rect(screen, [237, 112, 129], [x, y, 30, 30])
						pygame.display.flip()
						box.msgbox('你已死亡\n\n原因:触摸岩浆')
						x = 30
						y = 30
						brave = 0
						brave_time = 1
						dead_time += 1
						if dead_time % 2 == 0:
							maze = mazeData.Maze()
			# 判断【事件按键】是不是【左移键】
			elif event.key == pygame.K_LEFT:
				color = screen.get_at([x - 30,y])
				color1 = screen.get_at([x, y])
				if color[0] == 255 or color[0] == 253:
					x = x - 30
					step += 1
				elif brave == 1:
					if color1[0] == 254:
						x = x - 30
						pygame.draw.rect(screen, [237, 112, 129], [x, y, 30, 30])
						pygame.display.flip()
						box.msgbox('你已死亡\n\n原因:触摸岩浆')
						x = 30
						y = 30
						brave = 0
						brave_time = 1
						dead_time += 1
						if dead_time % 2 == 0:
							maze = mazeData.Maze()
			# 判断【事件按键】是不是【右移键】
			elif event.key == pygame.K_RIGHT:
				color = screen.get_at([x + 30,y])
				color1 = screen.get_at([x + 30, y])
				if color[0] == 255 or color[0] == 253:
					x = x + 30
					step += 1
				elif brave == 1:
					if color1[0] == 254 :
						x = x + 30
						pygame.draw.rect(screen, [237, 112, 129], [x, y, 30, 30])
						pygame.display.flip()
						box.msgbox('你已死亡\n\n原因:触摸岩浆')
						x = 30
						y = 30
						brave = 0
						brave_time = 1
						dead_time += 1
						if dead_time % 2 == 0:
							maze = mazeData.Maze()
		if event.type == pygame.QUIT:
			sys.exit()
			
	# 不动时检测岩浆触碰
	try:
		color1 = screen.get_at([x,y])
	except IndexError:
		color1 = [None,None,None]
		
	try:
		color2 = screen.get_at([x,y])
	except IndexError:
		color2 = [None,None,None]
		
	try:
		color3 = screen.get_at([x+29,y])
	except IndexError:
		color3 = [None,None,None]
		
	try:
		color4 = screen.get_at([x,y+29])
	except IndexError:
		color4 = [None,None,None]
	
	print(color1,color2,color3,color4)
	
	if brave == 1:
		if color1[0] == 254\
			or color2[0] == 254\
				or color3[0] == 254\
					or color1[0] == 254:
			box.msgbox('你已死亡\n\n原因:触摸岩浆')
			x = 30
			y = 30
			brave = 0
			brave_time = 1
			dead_time += 1
			if dead_time % 2 == 0:
				maze = mazeData.Maze()
				
	# 填充背景色
	screen.fill([161, 207, 143])

	# 绘制迷宫
	maze.draw(screen)
	
	#更改岩浆河位置
	if not long > 1290:
		long += 3
	else:
		long = 0
		
		# 重置岩浆河位置
		set_dead()
		
	z = 30
		
	# 预测岩浆河
	pygame.draw.rect(screen, [253, 180, 180], [0, guess_y1, 30, z])
	pygame.draw.rect(screen, [253, 180, 180], [0, guess_y2, 30, z])
	pygame.draw.rect(screen, [253, 180, 180], [guess_x2, 0, z, 30])
	pygame.draw.rect(screen, [253, 180, 180], [guess_x1, 0, z, 30])
	
	
	

	# 绘制方块
	if brave == 0:
		pygame.draw.rect(screen, [0, 0, 0], [x+1, y+1, 28, 28])
	else:
		pygame.draw.rect(screen, [237, 112, 129], [x+1, y+1, 28, 28])
		
	#绘制岩浆河
	pygame.draw.rect(screen, [254, 0, 0], [0, dead_y1, long, z])
	pygame.draw.rect(screen, [254, 0, 0], [0, dead_y2, long, z])
	pygame.draw.rect(screen, [254, 0, 0], [dead_x2, 0, z, long])
	pygame.draw.rect(screen, [254, 0, 0], [dead_x1, 0, z, long])
	
	#减少时间
	time -= 1
	#绘制字体
	now = str(time/100)
	words = text.render(now, 1, (230, 230, 230))
	screen.blit(words,(1150, 20))
	
	#检擦触碰岩浆
	# ~ try:
		# ~ color1 = screen.get_at([x - 1,y - 1])
	# ~ except IndexError:
		# ~ color1 = [None]
	
	# ~ try:
		# ~ color2 = screen.get_at([x + 28,y + 28])
	# ~ except IndexError:
		# ~ color2 = [None]
	
	# ~ try:
		# ~ color3 = screen.get_at([x - 1,y + 28])
	# ~ except IndexError:
		# ~ color3 = [None]
	
	# ~ try:
		# ~ color4 = screen.get_at([x + 28,y - 1])
	# ~ except IndexError:
		# ~ color4 = [None]
		
	# ~ if color1[0]==254 or color2[0]==254 or color3[0]==254 or color4[0]==254:
		# ~ if brave == 1:
			# ~ box.msgbox('你已死亡\n\n原因:触摸岩浆')
			# ~ pygame.display.flip()
			# ~ x = 30
			# ~ y = 30
			# ~ brave = 0
			# ~ brave_time = 1
			# ~ dead_time += 1
			# ~ if dead_time % 2 == 0:
				# ~ maze = mazeData.Maze()
	
	#无敌时间计时⏲
	if brave_time == 500:
		brave_time = -100000
		brave = 1
	elif brave_time > -52222:
		brave_time += 1
	 
	#检查是否到达终点
	if x == 1140 and y == 630:
		f = open('best_step.txt','r')
		best_step = f.read()
		f.close()
		if step < int(best_step):
			box.msgbox('恭喜你突破了最高纪录' + '\n你的记录:' + str(step)  +'\n最高纪录:' + str(best_step))
			f = open('best_step.txt','w')
			f.write(str(step))
			f.close()
			brave_time = -900
		elif step > int(best_step):
			box.msgbox('恭喜你用了' + str(step) + '步来通关\n距离最高纪录还差' + str(step - int(best_step)))
			brave_time = -90
		elif step == int(best_step):
			box.msgbox('恭喜你用了' + str(step) + '\n你再少走一步就可以超过最高记录了')
			brave_time = -450
		#初始化(过关给无敌时间)
		x = 30
		y = 30
		brave = 0
		step = 0
		time = 20000
		maze = mazeData.Maze()
	if time == 0:
		box.msgbox('你已死亡\n原因:超时未通关')
		sys.exit()
		
	
	# 更新窗口
	pygame.display.flip()
	print(x,y)

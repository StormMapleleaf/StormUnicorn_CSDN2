import pygame
from pygame.locals import * #导入pygame的常量
import time
#============基本属性定义=====================
#游戏主窗口尺寸
WIDTH = 512 
HEIGHT = 568
#===========游戏主入口函数====================
def main():
	pygame.init() #初始化pygame
	#创建游戏窗口，第一个参数：（分倍率（宽，高），标志=0、深度=0）
	screen = pygame.display.set_mode((WIDTH,HEIGHT),0,0)
	pygame.display.set_caption("飞机游戏大战") #设置标题
	isRun = True #定义游戏主循环标识
	# 游戏主循环
	while isRun:
		#获取事件，实现窗口的关闭
		for event in pygame.event.get():
			#判断是否点击了关闭按钮
			if event.type == QUIT:
				isRun = False#exit()
		#循环时间间隔
		time.sleep(0.1)
	#退出游戏程序
	pygame.quit()
	exit()

#程序主入口判断
if __name__ == "__main__":
	main()
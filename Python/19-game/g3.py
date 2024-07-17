#定义玩家（英雄）飞机类
import pygame
from pygame.locals import * #导入pygame的常量
import time
#============基本属性定义=====================
#游戏主窗口尺寸
WIDTH = 512
HEIGHT = 568
#定义一些颜色
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
#=============定义各种精灵类==================
#玩家（英雄）飞机类
class HeroPlane(pygame.sprite.Sprite):
	''' 玩家（英雄）飞机类 '''
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("./images/OIP.jpg") #导入飞机图片
		self.image.set_colorkey(BLACK) #设置透明颜色
		self.rect = self.image.get_rect() #获取表面的矩形区域 <rect(0, 0, 106, 76)>
		print(self.rect.center)
		self.rect.x = 200
		self.rect.y = 400
#玩家子弹类
#敌机类
#爆炸类
#===========游戏主入口函数====================

all_sprites = pygame.sprite.Group() #创建一个精灵族对象
hero = HeroPlane() #实例化英雄玩家对象
all_sprites.add(hero)#将玩家放入到精灵组中

def main():
	pygame.init() #初始化pygame
	#创建游戏窗口，第一个参数：（分倍率（宽，高），标志=0、深度=0）
	screen = pygame.display.set_mode((WIDTH,HEIGHT),0,0)
	pygame.display.set_caption("飞机游戏大战") #设置标题
	#创建一个游戏时钟对象
	clock = pygame.time.Clock()
	#创建一个背景图片
	background = pygame.image.load("./images/bg2.png")
	isRun = True #定义游戏主循环标识
	m = -968 #定义背景图片在窗口上的初始y轴坐标
	# 游戏主循环
	while isRun:
		#获取事件，实现窗口的关闭
		for event in pygame.event.get():
			#判断是否点击了关闭按钮
			if event.type == QUIT:
				isRun = False#exit()

		#将背景图片绘制到窗口中,并实现滚动效果
		screen.blit(background,(0,m))
		m += 2
		if m >= -200:
			m = -968

		#将精灵组中的所有精灵绘制到窗口主屏幕中
		all_sprites.draw(screen)

		#更新绘制
		pygame.display.flip()

		#time.sleep(0.1) #循环时间间隔
		clock.tick(60) # 设置屏幕的刷新频率
	#退出游戏程序
	pygame.quit()
	exit()

#程序主入口判断
if __name__ == "__main__":
	main()
#爆炸场面的绘制
import pygame
from pygame.locals import * #导入pygame的常量
import time
import random
#============基本属性定义=====================
#游戏主窗口尺寸
WIDTH = 512
HEIGHT = 568
#定义一些颜色
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
#敌机图片
enemies_images = []
for i in range(0,3):
	file = "./images/e{}.png".format(i) #拼装图片路径
	img = pygame.image.load(file) #加载图片
	img.set_colorkey(BLACK) #设置BLACK为透明色
	img = pygame.transform.scale(img,(80,60))#对原有图片大小调整为80*60
	enemies_images.append(img) #放置到列表中

#爆炸图片
explosion_images = []
for i in range(0,9):
	file = "./images/regularExplosion0{}.png".format(i) #拼装图片路径
	img = pygame.image.load(file) #加载图片
	img.set_colorkey(BLACK) #设置BLACK为透明色
	img = pygame.transform.scale(img,(75,75))#对原有图片大小调整为75*75
	explosion_images.append(img) #放置到列表中

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
		self.speedx = 0 #定义水平移动速度（距离）
		self.speedy = 0 #定义垂直移动速度（距离）
		self.ftime = pygame.time.get_ticks() #记录当前毫秒值

	def update(self):
		self.speedx = 0  # 重置水平移动速度（距离）
		self.speedy = 0  # 重置垂直移动速度（距离）
		#获取键盘信息
		keys = pygame.key.get_pressed()
		if keys[K_a] or keys[K_LEFT]: #左
			self.speedx = -5
		if keys[K_d] or keys[K_RIGHT]: #右
			self.speedx = 5
		if keys[K_w] or keys[K_UP]: #上
			self.speedy = -5
		if keys[K_s] or keys[K_DOWN]: #下
			self.speedy = 5
		if keys[K_SPACE]: #空格 发射
			now = pygame.time.get_ticks()
			if now - self.ftime > 200: #控制发射子弹时间间隔
				self.ftime = now
				#实例化子弹对象，并添加到精灵组中
				bu = Bullet(self.rect.centerx, self.rect.top)
				bullets.add(bu) #添加到子弹精灵组
				all_sprites.add(bu) #添加所有精灵组

		#更新移动距离
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		# 判断防止越界
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > HEIGHT:
			self.rect.bottom = HEIGHT

#玩家子弹类
class Bullet(pygame.sprite.Sprite):
	''' 玩家子弹类 '''
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("./images/pd.png") #导入子弹图片
		self.image.set_colorkey(BLACK) #设置透明颜色
		self.rect = self.image.get_rect() #获取表面的矩形区域 <rect(0, 0, 宽, 高)>
		self.rect.x = x
		self.rect.y = y
		self.speedy = -10 #定义子弹移动速度

	def update(self): #负责子弹的移动
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()#将自己从精灵组中移除

#敌机类
class EnemyPlane(pygame.sprite.Sprite):
	''' 敌机类 '''
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = random.choice(enemies_images).copy() #随机一个图片对象
		self.rect = self.image.get_rect() #获取表面的矩形区域 <rect(0, 0, 宽, 高)>
		self.rect.x = random.randrange(0, WIDTH - self.rect.width)
		self.rect.y = random.randrange(-100, -60)
		self.speedy = random.randrange(2,6) #定义子弹垂直移动速度
		self.speedx = random.randrange(-3,3) #定义子弹水平移动速度

	def update(self): #负责移动
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.left < 0 or self.rect.right > WIDTH:
			self.speedx = -self.speedx
		if self.rect.top > HEIGHT: #当敌机移动出了底部
			self.kill()
			#随机显示到顶部继续
			#self.rect.y = random.randrange(-100, -60)

#爆炸类
class Explosion(pygame.sprite.Sprite):
	''' 爆炸类 '''
	def __init__(self,center):
		pygame.sprite.Sprite.__init__(self)
		self.image = explosion_images[0] #获取第一张图片对象
		self.rect = self.image.get_rect() #获取表面的矩形区域 <rect(0, 0, 宽, 高)>
		self.rect.center = center
		self.frame = 0 #爆炸图片的索引号

	def update(self): #负责切换爆炸图片
		self.frame += 1
		#判断爆炸图片是否切换完毕
		if self.frame == len(explosion_images):
			self.kill()
		else:
			center = self.rect.center #获取上一张图片位置
			self.image = explosion_images[self.frame]  # 获取第frame张图片对象
			self.rect = self.image.get_rect()  # 获取表面的矩形区域 <rect(0, 0, 宽, 高)>
			self.rect.center = center #赋给本张图位置

#===========游戏主入口函数====================

all_sprites = pygame.sprite.Group() #创建一个精灵族对象
hero = HeroPlane() #实例化英雄玩家对象
all_sprites.add(hero)#将玩家放入到精灵组中
bullets = pygame.sprite.Group() #创建一个存放玩家子弹精灵组对象
enemies = pygame.sprite.Group() #创建一个存放敌机精灵组对象

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

		#随机判断放置敌机
		if random.randrange(0,100) == 6:
			print("敌机。。")
			em = EnemyPlane() #实例化敌机
			enemies.add(em)	#放置到敌机组
			all_sprites.add(em) #放置到精灵组

		#敌机组与玩家子弹的碰撞检测判断，True和True表示会自动移除碰撞的敌机和子弹，并返回碰撞的敌机信息
		emlist = pygame.sprite.groupcollide(enemies,bullets,True,True)
		for em in emlist: #遍历并实例化爆炸对象，添加到精灵组
			all_sprites.add(Explosion(em.rect.center))

		#执行精灵组中所有精灵的update()方法
		all_sprites.update()
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
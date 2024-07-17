
import pygame
from pygame.locals import *  #pygame使用的各种常量
import time

pygame.mixer.init()  #初始化音效

#爆炸声音
ready = pygame.mixer.Sound('./sounds/rumble1.ogg')
ready.play()
time.sleep(1)

'''
#发射炮弹声音
#ready = pygame.mixer.Sound('./sounds/rocket.ogg')
ready = pygame.mixer.Sound('./sounds/pew.wav')
ready.play()
time.sleep(1)
ready.play()
time.sleep(1)
ready.play()
time.sleep(1)
'''

'''
#准备开始音乐
ready = pygame.mixer.Sound('./sounds/getready.ogg')
ready.play()
time.sleep(5)
'''

'''
#背景音乐
pygame.mixer.music.stop()
pygame.mixer.music.load('./sounds/tgfcoder-FrozenJam-SeamlessLoop.ogg')
pygame.mixer.music.play(-1) #一直播放
print("start... ")
time.sleep(5)
pygame.mixer.music.stop()
print("stop")
time.sleep(5)
'''
#import pygame as pg
#from pygui import gui
#pg.init()
#screen = pg.display.set_mode((740, 480))
#done = False
#btn = gui.Button(pg.Rect(10,10,100,100),"on", True,pg.Color('lightskyblue3'), pg.Color('dodgerblue2'), pg.Color('dodgerblue'))
#while not done:
#    for event in pg.event.get():
#        if event.type == pg.QUIT:
#            done = True
#        btn.handle_event(event)
#    btn.update()
#    screen.fill((30, 30, 30))
#    btn.draw(screen)
#    pg.display.flip()
#    pg.time.Clock().tick(24)
#pg.quit()


#import pygame
#import math
#
## 初期化
#pygame.init()
#
## 画面の設定
#width, height = 800, 600
#screen = pygame.display.set_mode((width, height))
#pygame.display.set_caption("Half Circle Drawing")
#
## 色の定義
#black = (0, 0, 0)
#white = (255, 255, 255)
#
## 画面の消去
#screen.fill(white)
#pygame.display.flip()
#
## 半円を描画
#center_x = width // 2
#center_y = height // 2
#radius = 100
#start_angle = 0
#end_angle = math.pi  # math.pi は半円の角度
#
## 半円を黒色で描画
#pygame.draw.arc(screen, black, (center_x - radius, center_y - radius, radius * 2, radius * 2), start_angle, end_angle, 5)
#
## 画面を更新
#pygame.display.flip()
#
## イベントループ
#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#
## 終了
#pygame.quit()

import pygame
import numpy as np

# 初期化
pygame.init()

# 画面の設定
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Smooth Half Circle Drawing")

# 色の定義
black = (0, 0, 0)
white = (255, 255, 255)

# 画面の消去
screen.fill(white)
pygame.display.flip()

# 半円を描画
center_x = 20
center_y = 20
radius = 5
points = 30  # 使用する点の数

# 半円の点を生成
angle_range = np.linspace(0, np.pi, points)
points = [(int(center_x + radius * np.cos(angle)), int(center_y + radius * np.sin(angle))) for angle in angle_range]

# 点同士を線でつなぐ
pygame.draw.polygon(screen, black, points)

# 画面を更新
pygame.display.flip()

# イベントループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 終了
pygame.quit()
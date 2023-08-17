import pygame
from pygame.locals import *
import sys
import random
import numpy as np
display = [1010, 1010]
world_size = [100, 100]
num_key = [K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]

class World:
    def __init__(self):
        self.speed = 1 # 描画速度
        self.world = np.zeros(tuple(world_size + [3]))
        self.color = np.asarray([[255.0, 255.0, 255.0], [255.0, 0.0, 0.0], [0.0, 255.0, 0.0], [0.0, 0.0, 255.0], [0.0, 0.0, 0.0]])

    # ランダムに初期化　flag=Trueの場合色もランダム
    def random_init(self, p, color_flag=False):
        for i in range(world_size[0]):
            for j in range(world_size[1]):
                if random.random() > p:
                    continue

                if color_flag:
                    color = self.color[random.randint(0, 3)]
                else:
                    color = self.color[0]
                self.world[i, j] = color

    def draw(self, screen):
        for i in range(world_size[0]):
            for j in range(world_size[1]):
                pygame.draw.rect(screen, tuple(self.world[i, j]), Rect(10*j + 10, 10*i + 10, 10, 10))

    def update(self):
        next_world = np.zeros(tuple(world_size + [3]))
        flags = self.world.sum(axis=2) > 0

        for i in range(world_size[0]):
            for j in range(world_size[1]):
                min_x = max(0, j-1)
                max_x = min(world_size[1], j+2)
                min_y = max(0, i-1)
                max_y = min(world_size[0], i+2)
                count = np.sum(flags[min_y:max_y, min_x:max_x])
                if flags[i, j] == 0: # 死んだセル
                    if count == 3: # 誕生
                        area = self.world[min_y:max_y, min_x:max_x]
                        next_world[i, j] = area.reshape(-1, 3).sum(axis=0) / count
                else:
                    if 3 < count < 6: # not 過疎 or 過密
                        next_world[i, j] = self.world[i, j]

        self.world = next_world

def main():
    pygame.init()
    screen = pygame.display.set_mode(display)
    pygame.display.set_caption("Lifegame")

    world = World()
    world.random_init(0.3, True)
    counter = 0

    while(1):
        screen.fill((0, 0, 0))

        world.draw(screen)
        pygame.display.update()
        pygame.time.wait(5)

        counter += 1
        if counter > world.speed:
            world.update()
            counter = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()      
                if event.key == K_DOWN:
                    world.speed = world.speed+1
                if event.key == K_UP:
                    world.speed = max(0, world.speed-1)
                if event.key in num_key:
                    world.random_init((num_key.index(event.key)+1.0)*0.1, True)

if __name__ == "__main__":
    main()
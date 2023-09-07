import pygame as pg
from pygui import gui
pg.init()
screen = pg.display.set_mode((740, 480))
done = False
btn = gui.Button(pg.Rect(10,10,100,100),"on", True,pg.Color('lightskyblue3'), pg.Color('dodgerblue2'), pg.Color('dodgerblue'))
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        btn.handle_event(event)
    btn.update()
    screen.fill((30, 30, 30))
    btn.draw(screen)
    pg.display.flip()
    pg.time.Clock().tick(24)
pg.quit()
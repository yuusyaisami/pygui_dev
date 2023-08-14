# クラスは updateとdraw関数 handle_eventがあります
# updateはオブジェクトのメイン処理
# drawは描写
# handle_eventはeventについての処理(主にユーザーの操作)です

# 処理は繰り返し処理の中に入れてください
# (例)
# import pygame as pg
# import gui #このguiモジュールをインポートしてくださいまたは, from pygui import guiを入力してください
# pg.init()
# screen = pg.display.set_mode((740, 480))
# done = False
# btn = Button(pg.Rect(10,10,100,100))
# while not done:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             done = True
#         btn.handle_event(event)
#     btn.update()
#     screen.fill((30, 30, 30))
#     btn.draw(screen)
#     pg.display.flip()
# pg.quit()
# 複数オブジェクトがあるときはlistにオブジェクトのインスタンスを宣言し、関数を呼び出してください

import pygame as pg
import constant as ct
import random

pg.init() # pygame initialize
# Constants
constant = ct.Constant()
# button
class Button: # ただのボタン
    def __init__(self, rect = pg.Rect(0,0,0,0), text = "", font = constant.FONT,visible = True, before_clicked_color = constant.COLOR_INACTIVE, after_clicked_color = constant.COLOR_ACTIVE, on_cursor_color = constant.COLOR_INACTIVE):
        self.rect = rect
        self.b_d_c = before_clicked_color #決定する前のいろ
        self.a_d_c = after_clicked_color # 決定した後の色
        self.o_c_c = on_cursor_color # マウスがオブジェクトの上にあるときのオブジェクトの色
        self.color = self.b_d_c
        self.text = text # オブジェクトの中のテキスト
        self.forcing_run = False # 強制的に決定する
        self.clicked = False # 決定されたとき1度trueになる (update関数が再び呼び出されるとFalseになる)
        self.btn_count = 0
        self.Font = font
        self.visible = visible

        self.do_count = False
    def handle_event(self, event):
        if self.visible:
            if event.type == pg.MOUSEBUTTONDOWN:
                # ユーザーがButton rectをクリックした場合。
                if self.rect.collidepoint(event.pos):
                    self.forcing_run = False
                    self.clicked = True
                    self.do_count = True
                    self.btn_count = 10
                    self.color = self.a_d_c
            mouse_x, mouse_y = pg.mouse.get_pos()
            if self.rect.collidepoint(mouse_x, mouse_y):
                if not self.do_count:
                    self.color = self.o_c_c
            elif not self.do_count:
                self.color = self.b_d_c

    def update(self):
        if self.visible:
            if self.forcing_run: # handle_eventなしで決定
                self.forcing_run = False
                self.do_count = True
                self.btn_count = 10
                self.color = self.a_d_c
                self.clicked = True

            if self.btn_count == 9:
                self.clicked = False
            elif self.btn_count < 0:
                self.clicked = False
                self.do_count = False

            if self.do_count:
                self.btn_count -= 1
    def draw(self,screen):
        if self.visible:
            pg.draw.rect(screen, self.color, self.rect, 3)
            screen.blit(constant.FONT.render(self.text, True, self.color), (self.rect.x+5, self.rect.y+5))
class ButtonSwitching: # スイッチ式のボタン
    def __init__(self, rect = pg.Rect(0,0,0,0), text = "",  font = constant.FONT,text_rect = pg.Rect(0,0,0,0),visible = True, before_clicked_color = constant.COLOR_INACTIVE, after_clicked_color = constant.COLOR_ACTIVE, on_cursor_color = constant.COLOR_INACTIVE):
        self.rect = rect
        self.b_d_c = before_clicked_color #決定する前のいろ
        self.a_d_c = after_clicked_color # 決定した後の色
        self.o_c_c = on_cursor_color # マウスがオブジェクトの上にあるときのオブジェクトの色
        self.color = self.b_d_c
        self.text = text # オブジェクトの中のテキスト
        self.forcing_run = False # 強制的に決定する
        self.clicked = False # 決定されたとき1度trueになる (update関数が再び呼び出されるとFalseになる)
        self.btn_count = 0
        self.text_rect = text_rect
        self.Font = font
        self.on_cursor = False
        self.visible = visible
        self.do_count = False
        self.frame = 3
    def handle_event(self, event):
        if self.visible:
            if event.type == pg.MOUSEBUTTONDOWN:
                # ユーザーがButton rectをクリックした場合。
                if self.rect.collidepoint(event.pos):
                    self.forcing_run = False
                    self.clicked = not self.clicked 
                    self.do_count = True
                    self.btn_count = 10
            mouse_x, mouse_y = pg.mouse.get_pos()
            if self.rect.collidepoint(mouse_x, mouse_y):
                self.color = self.o_c_c
                self.on_cursor = True
            else:
                self.on_cursor = False

    def update(self):
        if self.visible:
            if self.forcing_run: # handle_eventなしで決定
                self.forcing_run = False
                self.do_count = True
                self.btn_count = 10
                self.clicked = not self.clicked 

            elif self.btn_count < 0:
                self.do_count = False

            if self.do_count:
                self.btn_count -= 1
            if self.clicked:
                if not self.on_cursor :
                    self.color = self.a_d_c
            else :
                if not self.on_cursor :
                    self.color = self.b_d_c

    def draw(self,screen):
        if self.visible:
            pg.draw.rect(screen, self.color, self.rect, self.frame)
            screen.blit(self.Font.render(self.text, True, self.color), (self.text_rect.x, self.text_rect.y))
class ButtonImageSwitching: # 画像のボタン
    def __init__(self, rect , visible , before_clicked_image, after_clicked_image, on_cursor_image):
        self.rect = rect
        self.b_d_i = before_clicked_image #決定する前のいろ
        self.a_d_i = after_clicked_image # 決定した後の色
        self.o_c_i = on_cursor_image # マウスがオブジェクトの上にあるときのオブジェクトの色
        self.image = self.b_d_i
        self.forcing_run = False # 強制的に決定する
        self.clicked = False # 決定されたとき1度trueになる (update関数が再び呼び出されるとFalseになる)
        self.btn_count = 0
        self.visible = visible

        self.on_cursor = False
        self.do_count = False
    def handle_event(self, event):
        if self.visible:
            if event.type == pg.MOUSEBUTTONDOWN:
                # ユーザーがButton rectをクリックした場合。
                if self.rect.collidepoint(event.pos):
                    self.forcing_run = False
                    self.clicked = not self.clicked
                    self.do_count = True
                    self.btn_count = 10
                    self.image = self.a_d_i
            mouse_x, mouse_y = pg.mouse.get_pos()
            if self.rect.collidepoint(mouse_x, mouse_y):
                if not self.do_count:
                    self.on_cursor = True
                    self.image = self.o_c_i
            elif not self.do_count:
                self.on_cursor = False

    def update(self):
        if self.visible:
            if self.forcing_run: # handle_eventなしで決定
                self.forcing_run = False
                self.do_count = True
                self.btn_count = 10
                self.image = self.a_d_i
                self.clicked = not self.clicked
            elif self.btn_count < 0:
                self.do_count = False
            if self.do_count:
                self.btn_count -= 1
            if self.clicked:
                if not self.on_cursor:
                    self.image = self.a_d_i
            else :
                if not self.on_cursor:
                    self.image = self.b_d_i

    def draw(self,screen):
        if self.visible:
            screen.blit(self.image, (self.rect.x, self.rect.y))
class ButtonImage: # 画像のボタン
    def __init__(self, rect , visible , before_clicked_image, after_clicked_image, on_cursor_image):
        self.rect = rect
        self.b_d_i = before_clicked_image #決定する前のいろ
        self.a_d_i = after_clicked_image # 決定した後の色
        self.o_c_i = on_cursor_image # マウスがオブジェクトの上にあるときのオブジェクトの色
        self.image = self.b_d_i
        self.forcing_run = False # 強制的に決定する
        self.clicked = False # 決定されたとき1度trueになる (update関数が再び呼び出されるとFalseになる)
        self.btn_count = 0
        self.visible = visible

        self.do_count = False
    def handle_event(self, event):
        if self.visible:
            if event.type == pg.MOUSEBUTTONDOWN:
                # ユーザーがButton rectをクリックした場合。
                if self.rect.collidepoint(event.pos):
                    self.forcing_run = False
                    self.clicked = True
                    self.do_count = True
                    self.btn_count = 10
                    self.image = self.a_d_i
            mouse_x, mouse_y = pg.mouse.get_pos()
            if self.rect.collidepoint(mouse_x, mouse_y):
                if not self.do_count:
                    self.image = self.o_c_i
            elif not self.do_count:
                self.image = self.b_d_i

    def update(self):
        if self.visible:
            if self.forcing_run: # handle_eventなしで決定
                self.forcing_run = False
                self.do_count = True
                self.btn_count = 10
                self.image = self.a_d_i
                self.clicked = True
            if self.btn_count == 9:
                self.clicked = False
            elif self.btn_count < 0:
                self.do_count = False
                self.clicked = False
                self.image = self.b_d_i
            if self.do_count:
                self.btn_count -= 1
    def draw(self,screen):
        if self.visible:
            screen.blit(self.image, (self.rect.x, self.rect.y))
class InputBox:
    def __init__(self, rect, text='', font = constant.FONT,  visible = True, clear_text = True, before_clicked_color = constant.COLOR_INACTIVE, after_clicked_color = constant.COLOR_ACTIVE, on_cursor_color = constant.COLOR_INACTIVE ):
        self.rect = rect
        self.color = before_clicked_color
        self.before_color = before_clicked_color
        self.after_color = after_clicked_color
        self.oncursor_color = on_cursor_color
        self.text = text
        self.active = False
        self.clicked = text
        self.clear = clear_text
        self.Font = font
        self.visible = visible

    def handle_event(self, event):
        if self.visible:
            if event.type == pg.MOUSEBUTTONDOWN:
                # ユーザーがinput_box rectをクリックした場合。
                if self.rect.collidepoint(event.pos):
                    # アクティブな変数を切り替える。
                    self.active = not self.active
                    self.color = self.after_color
                else:
                    self.active = False
            mouse_x, mouse_y = pg.mouse.get_pos()
            if self.rect.collidepoint(mouse_x, mouse_y):
                if not self.active:
                    self.color = self.oncursor_color
            else:
                if not self.active:
                    self.color = self.before_color

            if event.type == pg.KEYDOWN:
                if self.active:
                    if event.key == pg.K_RETURN:
                        self.clicked = self.text
                        if self.clear:
                            self.text = ""
                    elif event.key == pg.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode

    def update(self):
        if self.visible:
            # テキストが長すぎる場合は、ボックスのサイズを変更してください。
            width = max(200, constant.FONT.render(self.text, True, self.color).get_width()+10)
            self.rect.w = width

    def draw(self, screen):
        if self.visible:
            # テキストを吹き飛ばす。
            screen.blit(constant.FONT.render(self.text, True, self.color), (self.rect.x+5, self.rect.y+5))
            # レクトを吹き飛ばす。
            pg.draw.rect(screen, self.color, self.rect, 2)
class Text:
    def __init__(self, rect, text = "", font = constant.FONT, visible = True, textcolor = constant.COLOR_INACTIVE):
        self.rect = rect
        self.text = text
        self.font = font
        self.visible = visible
        self.color = textcolor
    def handle_event(self, event):
        pass
    def update(self):
        pass
    def draw(self, screen):
        if self.visible:
            screen.blit(self.font.render(self.text, True, self.color), (self.rect.x+5, self.rect.y+5))
class CheckBox:
    def __init__(self, rect , text, font = constant.FONT, visible = True, clicked = True, color = constant.COLOR_INACTIVE):
        self.rect = rect
        self.text = text
        self.font = font
        self.color = color
        self.visible = visible
        self.clicked = clicked
        self.checkobject = ButtonSwitching(pg.Rect(self.rect.x,self.rect.y,23,23))
        if self.clicked:
            self.checkobject.forcing_run = True
    def handle_event(self, event):
        if self.visible:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.checkobject.clicked = not self.checkobject.clicked
                    if self.checkobject.clicked:
                        self.checkobject.frame = 0
                    else:
                        self.checkobject.frame = 3
                    print(self.checkobject.clicked)
            
    def update(self):
        if self.visible:
            self.clicked = self.checkobject.clicked
    def draw(self, screen):
        if self.visible:
            screen.blit(self.font.render(self.text, True, self.color), (self.rect.x+26, self.rect.y))
            self.checkobject.draw(screen)

if __name__ == '__main__':
    import gui
    pg.init()
    screen = pg.display.set_mode((1280, 880))
    done = False
    image = pg.transform.scale(pg.image.load("ikemen.png"), (60, 60))
    image_d = pg.transform.scale(pg.image.load("drag.png"), (60, 60))
    btn_image = ButtonImage(pg.Rect(200,200,60,60),True,image,image_d,image)
    input = InputBox(pg.Rect(10,250,32,32),"",constant.FONT,True,True,pg.Color('lightskyblue3'),pg.Color('dodgerblue2'),pg.Color('dodgerblue1'))
    btn = ButtonSwitching(pg.Rect(10,10,200,200),"",constant.FONT,pg.Rect(110,110,0,0),True,pg.Color('lightskyblue3'), pg.Color('dodgerblue2'), pg.Color('dodgerblue'))
    text = Text(pg.Rect(10,400,32,32),"helloworld",constant.FONT,True)
    checkbox = CheckBox(pg.Rect(10, 300,126,32), "checked")
    objects = [btn_image, btn, input, text, checkbox]
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for handle in objects:
                handle.handle_event(event)
        for object_update in objects:
            object_update.update()
        screen.fill((30, 30, 30))
        for object_draw in objects:
            object_draw.draw(screen)
        pg.display.flip()
        pg.time.Clock().tick(24)
    pg.quit()
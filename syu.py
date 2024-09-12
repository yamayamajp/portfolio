import pygame
from pygame.locals import *
import sys


class Player():
    def __init__(self):
        self.px = 200
        self.py = 500
        self.player_image = pygame.image.load("mikata.gif").convert_alpha()

    def update(self,screen,gamen):

        # イベント処理

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.px -= 0.1
            gamen.x = self.px+25
        if keys[K_RIGHT]:
            self.px += 0.1
            gamen.x = self.px+25

        for event in pygame.event.get(): 
            if event. type == QUIT: 
                pygame.quit() 
                sys. exit()

            elif event.type == KEYDOWN: 
                if event.key == K_LEFT:
                    self.px -= 5  # 横方向
                    gamen.x = self.px+25
                elif event.key == K_RIGHT:
                    self.px += 5  # 横方向
                    gamen.x = self.px+25
                elif event.key == K_SPACE:
                    gamen.y = self.py
                    gamen.x = self.px+25
                    gamen.vy = -1

         # 画面内に収める処理を追加
        screen_width, screen_height = pygame.display.get_surface().get_size()
        self.px = max(0, min(self.px, screen_width - self.player_image.get_width()))
        self.py = max(0, min(self.py, screen_height - self.player_image.get_height()))


        screen.blit(self.player_image, (self.px, self.py))

class Font():
    def __init__(self, font_name, font_size, color):
        self.font = pygame.font.Font(font_name, font_size)
        self.color = color

    def render(self, text):
        return self.font.render(text, True, self.color)

class UFO():
    def __init__(self):
        self.ux = 200
        self.uy = 100
        self.uw = 150
        self.uh = 50
        self.uvx = 0.5
        self.uhp = 100
        self.enemy_image = pygame.image.load("teki.gif").convert_alpha()
        self.enemy_image = pygame.transform.scale(self.enemy_image, (50, 50)) 


    def update(self,screen,gamen2):
        self.ux = self.ux + self.uvx
        if self.ux>700 or self.ux <0:
            self.uvx *= -1
        #当たり判定    
        if (self.ux <= gamen2.x <= self.ux + self.uw) and (self.uy <= gamen2.y <= self.uy + self.uh):
            self.uhp=0
        if self.uhp > 0:       
         screen.blit(self.enemy_image, (self.ux, self.uy))

class Tama():
    def __init__(self):
        #プレイヤの初期設定
        self.x = 216
        self.y = 480
        self.vy = 0
    def update(self,screen):
        #タマの処理と描画
        self.y = self.y + self.vy
        pygame.draw.circle(screen,(10,10,10),(self.x,self.y),5)              # ●

def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面

    blue = pygame.image.load("blue.jpg").convert_alpha()
    blue = pygame.transform.scale(blue, (800, 600))  # 画面サイズに合わせる
    font = pygame.font.Font(None, 36)
    text = font.render("Space:Attack!", True, (0, 0, 0))
    rect_blue = blue.get_rect()

    T1=Tama()
    P1=Player()
    U1=UFO()
    while True:
        screen.blit(blue, rect_blue) 
        screen.blit(text, (300, 300))  # フォントの描画

        T1.update(screen)
        P1.update(screen,T1)
        U1.update(screen,T1)
        
        pygame.display.update()                                       # 画面更新
            
if __name__ == "__main__":
    main()
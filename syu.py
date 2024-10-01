import pygame
from pygame.locals import *
import sys
import random


class Player():
    def __init__(self):
        self.px = 200
        self.py = 500
        self.player_image = pygame.image.load("mikata.gif").convert_alpha()
        self.width = self.player_image.get_width()
        self.height = self.player_image.get_height()

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
        def get_rect(self):
         return pygame.Rect(self.px, self.py, self.width, self.height)

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
        self.bullets = []  # 弾のリスト


    def update(self,screen,gamen):
        self.ux += self.uvx
        if self.ux>700 or self.ux <0:
            self.uvx *= -1
        #当たり判定    
        if (self.ux <= gamen.x <= self.ux + self.uw) and (self.uy <= gamen.y <= self.uy + self.uh):
            self.uhp=0
        # 敵が弾を発射する
        if random.randint(1, 100) < 5:  # 5%の確率で弾を発射
            self.bullets.append(Bullet(self.ux + 25, self.uy + 50))  # 弾の初期位置

        # 弾の更新と描画
        for bullet in self.bullets[:]:

            if bullet.check_collision(gamen):
                gamen.hp -= 1  # HPを1減少
                print(f"プレイヤーのHP: {gamen.hp}")

                if gamen.hp <= 0:
                    gamen.is_alive = False  # プレイヤーを消失させる
                    print("プレイヤーは消失しました！")

                self.bullets.remove(bullet)
            bullet.update()
            if bullet.y < 0 or bullet.y > 600:  # 画面外に出たら削除
                self.bullets.remove(bullet)


        if self.uhp > 0:       
         screen.blit(self.enemy_image, (self.ux, self.uy))
        
        # 敵がいる場合のみ弾を描画
        if self.uhp > 0:
            for bullet in self.bullets:
                bullet.draw(screen)
        else:
            self.bullets.clear()  # 敵が消えたら弾も消去

        # プレイヤーとの当たり判定
        for bullet in self.bullets[:]:
            if bullet.check_collision(gamen):
                # プレイヤーに当たったときの処理
                print("プレイヤーに当たった！")  # ここでダメージ処理などを追加

                # 弾を消去
                self.bullets.remove(bullet)

class Bullet():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vy = 1  # 弾の速度

    def update(self):
        self.y += self.vy  # 上方向に移動

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 5)  # 赤い弾を描画

    def check_collision(self, player):
        bullet_rect = pygame.Rect(self.x - 5, self.y - 5, 10, 10)  # 弾の範囲
        return bullet_rect.colliderect(player.get_rect())

class Tama():
    def __init__(self):
        #プレイヤの初期設定
        self.x = 216
        self.y = 480
        self.vy = 0
        self.radius = 5  # 半径をここで初期化
        self.hp = 1  # HPを初期化
        self.is_alive = True  # 生存フラグ

    def update(self,screen):
        #タマの処理と描画
        self.y += self.vy
        pygame.draw.circle(screen,(10,10,10),(self.x,self.y),5)              # ●

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

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
        screen.fill((255, 255, 255)) 
        screen.blit(blue, rect_blue) 
        screen.blit(text, (300, 300))  # フォントの描画

        T1.update(screen)
        if T1.is_alive:  # 生存している場合のみ描画
         P1.update(screen,T1)
        U1.update(screen,T1)
        
        pygame.display.update()    # 画面更新
            
if __name__ == "__main__":
    main()
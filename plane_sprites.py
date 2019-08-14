import pygame
import random
####屏幕大小常量
SREEN_RECT=pygame.Rect(0,0,480,700)
###刷新的帧率
FEAME_PRE_SEC =60
###创建定时器的常量
CREATE_ENEMY_EVENT=pygame.USEREVENT
####英雄发射子弹常量
HERO_FIRE_EVENT =pygame.USEREVENT + 1

#制定游戏精灵父rom pla类
class GameSprites(pygame.sprite.Sprite):
    #飞机大战游戏精灵
    def __init__(self,image_name,speed=1):
        ##调用父类的初始化方法
        super().__init__()
        ##定义对象的属性
        self.image=pygame.image.load(image_name)
        self.speed = speed
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += self.speed
class   Background(GameSprites):
    """游戏背景精灵"""
    def __init__(self,is_alt=False):
        ####1.调用父类方法实现精灵的创建（image/rect/speed）
        super().__init__("./images/background.png")
        ###2.判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y= -self.rect.height


    def update(self):
        ###1/调用父类方法实现
        super().update()
        ###2、判断是否溢出屏幕，如果移出屏幕，将图像设置到游戏屏幕上方
        if  self.rect.y >= SREEN_RECT.height:
            self.rect.y = -self.rect.height

        pass
class Enemy(GameSprites):
    """敌机精灵"""
    def __init__(self):
        ###1.调用父类方法，创建敌机精灵，同时制定敌机图片
        super().__init__("./images/enemy1.png")
        ###2.指定敌机的初始随机速度
        self.speed=random.randint(1,3)
        ###3.指定敌机初始随机位置
        self.rect.bottom=0
        max_x = SREEN_RECT.width - self.rect.width
        self.rect.x =random.randint(0,max_x)


    def update(self):
        ##1.调用父类方法，保持垂直方向的飞行
        super().update()
        ###2.判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SREEN_RECT.height:
            #print("飞机飞出屏幕，需从精灵组删除")
            ####kill方法可以将精灵从精灵组移出，精灵就会被自动销毁
            self.kill()

    def __del__(self):
        #print("敌机挂了 %s" % self.rect)
        pass
class Hero(GameSprites):
    """英雄精灵"""
    def __init__(self):
        #1.调用父类方法，设置image和speed
        super().__init__("./images/me1.png",0)
        #2.设置英雄初始化位置
        self.rect.centerx = SREEN_RECT.centerx
        self.rect.bottom = SREEN_RECT.bottom - 120
        #3.创建子弹的精灵组
        self.bullets=pygame.sprite.Group()


    def update(self):
        ##英雄在水平方向移动
        self.rect.x += self.speed
        ###控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x=0
        elif self.rect.right >SREEN_RECT.right:
            self.rect.right = SREEN_RECT.right
    def fire(self):
        print("发射子弹。。。")
        for i in (0,1,2):

            #1.创建子弹精灵
            bullet =Bullet()
            #2.设置精灵位置
            bullet.rect.bottom =self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            #3.将精灵添加到精灵组
            self.bullets.add(bullet)
class Bullet(GameSprites):
    """子弹精灵"""
    def __init__(self):
        super().__init__("./images/bullet1.png",-2)

    def update(self):
        super().update()
        if self.rect.bottom <0:
            self.kill()
    def __del__(self):
        print("子弹被销毁")








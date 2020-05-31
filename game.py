# -*- coding: utf-8 -*-

"""have a nice day.

@author: Khan,ChenJie
@contact:
@time: 2020/5/15 15:34
@file: game.py
@desc: 游戏界面设计类
"""



import sys
import pygame
from cell_list import CellList


BLACK = (119, 136, 153)
BLUE = (100, 149, 237)
WHITE = (255, 255, 255)

# 初始化game模块
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("north.mp3")    # 载入音乐
pygame.mixer.music.set_volume(0.2)      # 设置音量为0.2
pygame.mixer.music.play()               # 播放音乐
pygame.display.set_caption("生命游戏")


class Game:
    """Game.

    游戏界面设计类
    """

    screen = None

    def __init__(self, width, height):
        """构造函数.

        @param width: screen宽度
        @param height: screen高度
        """
        self.screen = None
        self.num = 0
        # 屏幕宽高
        self.width = width
        self.height = height
        #  设置屏幕
        self.set_height_width(width, height)
        self.str_start = True
        self.set_screen_color(BLACK)
        # 时钟
        self.clock = pygame.time.Clock()
        # 平衡代数
        self.balance = 1

    def set_height_width(self, width, height):
        """设置界面的窗体大小.

        @param width: screen宽度
        @param height: screen高度
        @return: None
        """
        self.screen = pygame.display.set_mode([width, height])

    def set_screen_color(self, color):
        """设置背景颜色.
        
        @param color: rgb格式的颜色表示color
        @return: None
        """
        self.screen.fill(color)

    def set_time(self, times):
        """设置界面刷新时间.

        @param times: 时间间隔
        @return: None
        """
        self.clock.tick(times)  # 每秒循环1次


    def set_cell_num(self, num):
        """设置网格的生成边长，并将参数传递给cell_list构造2维数组.

        @param num: 生成网格的边长
        @return: None
        """
        self.cell_list = CellList(int(num))
        self.cell_list.set_example()

    def draw_cell(self):
        """绘制当前状态下区域内的细胞,0-死亡,1-存活.

        @return: None
        """
        # x y  长 宽
        cell_list = self.cell_list.get_cell_list()
        length = int(600 / self.num+1)
        for i in range(1, self.num+1):
            for j in range(1, self.num+1):
                if cell_list[i][j] == 1:
                    pygame.draw.rect(self.screen, BLUE,
                                     [i*(length+1)+10, j*(length+1)+10, length, length])
                else:
                    pygame.draw.rect(self.screen, WHITE,
                                     [i*(length+1)+10, j*(length+1)+10, length, length])

    def draw_text(self, dd_num, flag=False):
        """绘制界面上的相关文字信息.

        @param dd_num: 迭代次数
        @param flag: 是否达到平衡状态，默认为False
        @return: 返回当前状态flag
        """
        # 加载字体
        text_font = pygame.font.Font(r"C:\Windows\Fonts\STHUPO.TTF", 30)
        # True = 抗锯齿
        # (255,255,255) = 使用白色绘制
        # 返回值text_surface = 返回要绘制的文字表面
        text_surface = text_font.render("当前迭代次数： "+str(dd_num), True, (255, 255, 255))
        str_balance = "" if not flag else str(self.balance)
        text_surface3 = text_font.render("平衡代数： " + str_balance, True, (255, 255, 255))
        self.screen.blit(text_surface3, (1000, 250))

        str_flag = "是" if flag else "否"
        text_surface2 = text_font.render("平衡状态： " + str_flag, True, (255, 255, 255))

        # 绘制文字在(900,200)位置
        self.screen.blit(text_surface, (1000, 200))
        self.screen.blit(text_surface2, (1000, 300))

        pygame.draw.rect(self.screen, BLUE, [1140, 100, 150, 80])
        self.screen.blit(text_font.render("输入边长："+str(self.num), True,
                                          (255, 255, 255)), (1000, 125))
        pygame.draw.rect(self.screen, BLUE, [1070, 400, 150, 80])
        start = "开始" if self.str_start else "暂停"
        self.screen.blit(text_font.render(start, True, (255, 255, 255)), (1110, 425))

        pygame.draw.rect(self.screen, BLUE, [1070, 500, 150, 80])
        self.screen.blit(text_font.render("重新开始", True, (255, 255, 255)), (1080, 525))

        return flag

    @staticmethod
    def get_mouse():
        """获得鼠标点击的坐标.

        @return: 返回鼠标点击位置的坐标
        """
        location_x, location_y = pygame.mouse.get_pos()
        return location_x, location_y

    def pre_start(self):
        """初始化界面,并监听操作.

        @return: None
        """
        num = "0"
        location_x = 0
        location_y = 0
        while True:
            self.screen.fill(BLACK)
            self.draw_text(0, False)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    location_x, location_y = self.get_mouse()
                #  关闭窗口
                if event.type == pygame.QUIT:
                    sys.exit()
                # 监听输入
                elif event.type == pygame.KEYDOWN and \
                        (1070 <= location_x <= 1290) and (100 <= location_y <= 180):
                    key_num = int(event.key) - 48
                    print(key_num)
                    if 0 <= key_num <= 9:
                        num = num + str(key_num)
                        print(num)
                    elif key_num == -40 and len(num) > 0:
                        num = num[0:-1]
                    self.num = num
            if 1070 <= location_x <= 1220 and 400 <= location_y <= 480:
                self.num = int(num)
                if self.num >= 980 or self.num <= 0:
                    continue
                self.set_cell_num(num)
                self.str_start = False
                break

            pygame.display.flip()

    def start(self, time):
        """开始游戏，同时监听操作.

        @param time: 设置刷新时间
        @return: None
        """
        self.pre_start()
        round_times = 1
        self.balance = 1
        pre_list = None
        after_list = None
        while True:
            for event in pygame.event.get():
                #  关闭窗口
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    location_x, location_y = self.get_mouse()
                    if (1070 <= location_x <= 1220) and (400 <= location_y <= 480):
                        self.str_start = not self.str_start
                    if (1070 <= location_x <= 1220) and (500 <= location_y <= 580):
                        self.screen.fill(BLACK)
                        pygame.display.flip()
                        round_times = 1
                        self.balance = 0
                        self.str_start = True
                        self.pre_start()
                        break
            # print(self.str_start)
            self.screen.fill(BLACK)
            # 设置刷新时间
            self.set_time(time)
            # 1.获取细胞状态
            self.draw_cell()
            if not self.str_start:
                pre_list = self.cell_list.get_cell_list()
                # 2.绘制细胞
                self.cell_list.change_life()
                after_list = self.cell_list.get_cell_list()
            # 判断是否到达平衡状态
            if pre_list == after_list:
                flag = True
            else:
                flag = False
            self.balance = self.balance if flag else  self.balance + 1
            print("balance:"+str(self.balance))
            # 绘制迭代次数
            if self.draw_text(round_times, flag):
                pygame.display.flip()
                self.str_start = True

            round_times = round_times if self.str_start else round_times+1
            print("round_times:" + str(round_times))
            # 更新屏幕
            pygame.display.flip()

# -*- coding: utf-8 -*-

"""have a nice day.

@author: Khan,ChenJie
@contact:
@time: 2020/5/28 19:06
@file: cell_list.py
@desc: cell网格数组
"""

import random


class CellList:
    """CellList.

    细胞网格类，所有细胞都处在一个长x 宽y的二维数组中.
    """

    def __init__(self, num):
        """构造函数.

        @param num: 输入生成的网格边长
        """
        self.cell_list = []
        self.num = num
        for i in range(num+2):
            self.cell_list.append([])
            for j in range(num+2):
                self.cell_list[i].append(0)
        print('nit=', self.cell_list)

    def set_example(self):
        """设置初始结构.

        @return: None
        """
        for i in range(1, self.num+1):
            for j in range(1, self.num+1):
                self.cell_list[i][j] = int(random.random() > 0.5)

        # 稳定方格
        # self.cell_list[0][0] = 1
        # self.cell_list[0][1] = 1
        # self.cell_list[1][0] = 1
        # self.cell_list[1][1] = 1
        # 滑翔机
        # self.cell_list[1][1] = 1
        # self.cell_list[1][3] = 1
        # self.cell_list[2][2] = 1
        # self.cell_list[2][3] = 1
        # self.cell_list[3][2] = 1
        # 脉冲星
        # self.cell_list[4][2] = self.cell_list[5][2] = self.cell_list[6][2] = 1
        # self.cell_list[4][7] = self.cell_list[5][7] = self.cell_list[6][7] = 1
        # self.cell_list[2][4] = self.cell_list[2][5] = self.cell_list[2][6] = 1
        # self.cell_list[7][4] = self.cell_list[7][5] = self.cell_list[7][6] = 1
        # self.cell_list[10][2] = self.cell_list[11][2] = self.cell_list[12][2] = 1
        # self.cell_list[10][7] = self.cell_list[11][7] = self.cell_list[12][7] = 1
        # self.cell_list[9][4] = self.cell_list[9][5] = self.cell_list[9][6] = 1
        # self.cell_list[14][4] = self.cell_list[14][5] = self.cell_list[14][6] = 1
        # self.cell_list[4][9] = self.cell_list[5][9] = self.cell_list[6][9] = 1
        # self.cell_list[4][14] = self.cell_list[5][14] = self.cell_list[6][14] = 1
        # self.cell_list[2][10] = self.cell_list[2][11] = self.cell_list[2][12] = 1
        # self.cell_list[7][10] = self.cell_list[7][11] = self.cell_list[7][12] = 1
        # self.cell_list[10][9] = self.cell_list[11][9] = self.cell_list[12][9] = 1
        # self.cell_list[10][14] = self.cell_list[11][14] = self.cell_list[12][14] = 1
        # self.cell_list[9][10] = self.cell_list[9][11] = self.cell_list[9][12] = 1
        # self.cell_list[14][10] = self.cell_list[14][11] = self.cell_list[14][12] = 1
    def get_cell_list(self):
        """获取celllist.

        :return: 返回已创建的2为数组
        """
        return self.cell_list

    def get_cell_width(self):
        """获取长度.

        @return: 返回生成区域的边长
        """
        return self.num

    def change_life(self):
        """更新细胞状态.

        @return: 返回了更新后的状态
        """
        next_one = []
        for i in range(self.num+2):
            next_one.append([])
            for j in range(self.num+2):
                next_one[i].append(0)

        for i in range(1, self.num+1):
            for j in range(1, self.num+1):
                summary = self.cell_list[i][j - 1] + self.cell_list[i][j + 1] + \
                      self.cell_list[i - 1][j - 1] \
                      + self.cell_list[i - 1][j] + \
                      self.cell_list[i - 1][j + 1] + \
                      self.cell_list[i + 1][j - 1] + self.cell_list[i + 1][j] + \
                      self.cell_list[i + 1][j + 1]
                # 由死亡条件，列真值表进行逻辑电路分析 sum==3 sum==2 alive[][]==true
                if summary == 3:
                    next_one[i][j] = 1
                elif summary == 2:
                    next_one[i][j] = self.cell_list[i][j]
                else:
                    next_one[i][j] = 0
        print('next_one=', next_one)
        print('len_next_one=', len(next_one))
        print('len=', len(self.cell_list))
        self.cell_list.clear()
        self.cell_list = next_one.copy()
        print('cell_list=', self.cell_list)
        return next_one

# -*- coding: utf-8 -*-

"""have a nice day.

@author: Khan,ChenJie
@contact:
@time: 2020/5/28 19:06
@file: cell_list.py
@desc: 生命游戏（Game of Life）
       游戏规则：
            1. 活细胞周围的细胞数如果小于2个或多于3个则会死亡；（离群或过度竞争导致死亡）
            2. 活细胞周围如果有2或3个细胞可以继续存活；（正常生存）
            3. 死细胞（空格）周围如果恰好有3个细胞则会诞生新的活细胞。（繁殖）
       这三条规则简称B3/S23。如果调整规则对应的细胞数量，还能衍生出其他类型的自动机。
"""

from game import Game


if __name__ == '__main__':
    game = Game(1300, 800)
    game.start(1)

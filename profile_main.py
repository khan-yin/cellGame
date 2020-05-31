# -*- coding: utf-8 -*-

"""have a nice day.

@author: Khan,ChenJie
@contact: 
@time: 2020/5/28 22:16
@file: profile_main.py
@desc: main函数性能测试与优化
"""

import profile
from game import Game


def profile_main():
    """main函数性能测试.

    @return: None
    """
    game = Game(1300, 800)
    game.start(1)

if __name__=="__main__":
    profile.run("profile_main()")
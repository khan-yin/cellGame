# -*- coding: utf-8 -*-

"""have a nice day.

@author: Khan,ChenJie
@contact:
@time: 2020/5/28 21:34
@file: test_cell_list.py
@desc: CellList测试类
"""

from unittest import TestCase
import unittest
from cell_list import CellList


class TestCellList(TestCase):
    """CellList测试类.

    主要测试了CellList中的边长检查和更新算法.
    """

    def setUp(self):
        """创建一个测试用例.

        此处给定其边长为10
        @return: None
        """
        self.cell_list_case = CellList(10)
        print(len(self.cell_list_case.cell_list))

    def test_get_cell_width(self):
        """测试边长是否正确生成.

        @return: None
        """
        print(len(self.cell_list_case.cell_list))
        print("len=", self.cell_list_case.get_cell_list())
        self.assertEqual(self.cell_list_case.get_cell_width(), 10)

    def test_change_life(self):
        """测试changeLife函数.

        @return: None
        """
        self.cell_list_case.set_example()
        self.cell_list_case.cellList = self.cell_list_case.change_life()
        print()
        res = []
        for i in range(12):
            res.append([])
            for j in range(12):
                res[i].append(0)
                print(res[i][j], end=' ')
            print()
        # print(res)

        res[1][3] = 1
        res[2][1] = 1
        res[2][3] = 1
        res[3][2] = 1
        res[3][3] = 1
        print()
        for i in range(12):
            for j in range(12):
                print(self.cell_list_case.cellList[i][j], end=' ')
            print()
        print()
        self.assertEqual(res, self.cell_list_case.cellList)


if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestCellList("test_get_cell_width"))
    suite.addTest(TestCellList("test_change_life"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

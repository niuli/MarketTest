#!/usr/bin/python
# -*- coding: utf-8 -*-
from goods import Goods

class GoodsList(object):
    def __init__(self):
        self.__goods_list = list()

    def add(self, goods):
        self.__goods_list.append(goods)

    def dump(self):
        for r in self.__goods_list:
            r.dump()

    def get_all(self):
        return self.__goods_list

if __name__ == '__main__':
    gl = GoodsList()
    gl.dump()
    name, price, num = "显示器", 1799.00, 1
    goods = Goods(name, price, num)
    gl.add(goods)
    name, price, num = "啤酒", 25.00, 12
    goods = Goods(name, price, num)
    gl.add(goods)
    gl.dump()


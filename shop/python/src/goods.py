#!/usr/bin/python
# -*- coding: utf-8 -*-

class Goods(object):
    def __init__(self, name, price, num):
        self.__name  = name
        self.__price = float(price)
        self.__number = int(num)

    def dump(self):
        print self.__name, self.__price, self.__number

    def get_name(self):
    	return self.__name

    def get_price(self):
        return self.__price

    def get_number(self):
    	return self.__number

if __name__ == '__main__':
    name, price, num = "显示器", 1799.00, 1
    goods = Goods(name, price, num)
    goods.dump()


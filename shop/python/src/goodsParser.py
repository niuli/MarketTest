#!/usr/bin/python
# -*- coding: utf-8 -*-
from goods import Goods
import re

class GoodsParser(object):
    def __init__(self, file):
        self.__goods = set()
        self.load_goods(file)

    def load_goods(self, file):
        f = open(file,"r")
        for r in f.readlines():
            m = r.rstrip().split("：")
            tag, goodsList = m[0], m[1].split("，")
            for m in goodsList:
                self.__goods.add(m)
        f.close()

    def dump_goods_set(self):
        for r in self.__goods:
            print r

    def check_name(self, name):
        if name in self.__goods:
            return True
        return False

    def check_price(self, price):
        if type(eval(price) == float) :
            p = float(price)
            if p > 0 :
                return True
        return False

    def check_num(self, num):
        if type(eval(num) == int) :
            n = int(num)
            if n >= 1:
                return True
        return False

    def parse(self, r):
        r = r.replace(" ", "")
        b = re.findall(r"^(.+?)\*(.+?)：(.+?)$", r)
        if len(b) == 0:
            return None
        else:
            num, name, price = b[0][0], b[0][1], b[0][2]       
            if self.check_num(num) and self.check_price(price) and self.check_name(name):
                gd = Goods(name, price, num) 
                return gd
            else:
                return None
 
if __name__ == "__main__":
    gp = GoodsParser('../config/tags.config')
    gp.dump_goods_set()
    f = open('../testCase/testGoodsParser.txt','r')
    for r in f.readlines():
        gd = gp.parse(r)
        if gd is not None:
            gd.dump()
        else: 
            print "wrong line:" , r
    f.close()

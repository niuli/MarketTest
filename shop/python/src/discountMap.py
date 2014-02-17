#!/usr/bin/python
# -*- coding: utf-8 -*-

from discount import *

class DiscountMap(object):
    def __init__(self):
        self.__discount_map = dict()

    def add(self, discount):
        tag, date, percent = discount.get_tag(), discount.get_date(), discount.get_percent()
        self.__discount_map[tag] = (date, percent)

    def dump(self):
        for k,v in self.__discount_map.items():
            print k, v

    def get_by_tag(self, tag):
        if self.__discount_map.has_key(tag):
            return self.__discount_map[tag]

        return "","",""

    def has_tag(self, tag):
        return self.__discount_map.has_key(tag)

if __name__ == '__main__':
    dm = DiscountMap()
    date, percent, tag = "2014.03.11", 9.0, "电子"
    discount = Discount(date, percent, tag)
    dm.add(discount)
    dm.dump()
    print dm.has_tag("电子")

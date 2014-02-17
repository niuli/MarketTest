#!/usr/bin/python
# -*- coding: utf-8 -*-

from discountMap import DiscountMap
from discount import Discount
from dateformat import *

class DiscountCalculator(object):
    def __init__(self, discountMap):
        self.__discountMap = discountMap

    def get_discount_by_tag(self, tag, price, order_time):
        if self.__discountMap.has_tag(tag):
            date, percent = self.__discountMap.get_by_tag(tag)
            if compare_date(order_time, date) >= 0:
                price *= percent
        return price

    def get_discount_by_name(self, name):
        pass

if __name__ == "__main__":
    dm = DiscountMap()
    date, percent, tag = "2015.03.11", 0.9, "电子"
    discount = Discount(date, percent, tag)
    dm.add(discount)
    dc = DiscountCalculator(dm)
    price = 100.00
    tag = "电子"
    print dc.get_discount_by_tag(tag, price, "2014.02.16")
    print dc.get_discount_by_tag(tag, price, "2015.03.11")

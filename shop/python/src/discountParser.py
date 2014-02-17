#!/usr/bin/python
# -*- coding: utf-8 -*-
from discount import *
from dateformat import *
import re

class DiscountParser(object):
    def __init__(self, file):
        self.__tags = set()
        self.load_tags(file)

    def load_tags(self, file):
        f = open(file,"r")
        for r in f.readlines():
            m = r.rstrip().split("：")
            tag = m[0]
            self.__tags.add(tag)
        f.close()

    def dump_tags_set(self):
        for r in self.__tags:
            print r

    def check_tag(self, tag):
        if tag in self.__tags:
            return True
        return False

    def check_discount(self, discount):
        if type(eval(discount) == float) :
            p = float(discount)
            if p > 0 and p < 1.0:
                return True
        return False

    def check_date(self, date):
        return check_date(date)

    def parse(self, r):
        r = r.replace(" ", "")
        a = re.findall(r"^(.+?)\|(.+?)\|(.+?)$",r)
        if len(a) > 0:
            date, percent, tag = a[0][0], a[0][1], a[0][2] 
            if self.check_tag(tag) and self.check_discount(percent) and self.check_date(date):
                ds = Discount(date, percent, tag)
                return ds
        return None
 
if __name__ == "__main__":
    dp = DiscountParser('../config/tags.config')
    dp.dump_tags_set()
    r = "2013.11.11 | 0.7 | 电子"
    ds = dp.parse(r)
    ds.dump()



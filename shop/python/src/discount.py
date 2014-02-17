#!/usr/bin/python
# -*- coding: utf-8 -*-

class Discount(object):
    def __init__(self, date, percent, tag):
        self.__date  = date
        self.__percent = float(percent)
        self.__tag = tag

    def dump(self):
        print self.__date, self.__percent, self.__tag

    def get_date(self):
    	return self.__date

    def get_percent(self):
        return self.__percent

    def get_tag(self):
    	return self.__tag

if __name__ == '__main__':
    date, percent, tag = "2014.02.16", 0.7, "电子"
    ds = Discount(date, percent, tag)
    ds.dump()

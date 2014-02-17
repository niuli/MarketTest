#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from goodsTags import GoodsTags
from goodsParser import GoodsParser
from goodsList import *
from discountMap import DiscountMap
from discountParser import DiscountParser
from discount import Discount
from discountCalculator import DiscountCalculator
from feedbackMap import FeedbackMap
from feedback import Feedback
from feedbackParser import FeedbackParser
from priceRounder import *

class Calculator(object):
    def __init__(self, config_file, test_file):
        self.__ordertime = ""
        self.__config_file = config_file
        self.__test_file = test_file
        self.__discount_map = dict()
        self.__feedback_map = dict()
        self.__goodsParser = GoodsParser(config_file)
        self.__goodsList = GoodsList()
        self.__discountMap = DiscountMap()
        self.__discountParser = DiscountParser(config_file)
        self.__discountCalculator = DiscountCalculator(self.__discountMap)
        self.__feedbackParser = FeedbackParser()
        self.__feedbackMap = FeedbackMap()

    def parse(self):
        sm = 0
        f = open(self.__test_file, "r")

        for r in f.readlines():
            if r == '\n':
                sm += 1
                continue

            elif r.find('*') != -1:
                sm = 1

            if sm == 0:
                discount = self.__discountParser.parse(r)
                if discount is not None:
                    self.__discountMap.add(discount)

            elif sm == 1:
                goods = self.__goodsParser.parse(r)
                if goods is not None:
                    self.__goodsList.add(goods)

            elif sm == 2:
                self.__ordertime = r[:-1]
                sm += 1

            elif sm == 3:
                fb = self.__feedbackParser.parse(r)
                if fb is not None:
                    self.__feedbackMap.add(fb)
        f.close()

    def calculate(self):
        all_price = 0
        goods_tags = GoodsTags(self.__config_file)

        for goods in self.__goodsList.get_all():
            name, price, num = goods.get_name(), goods.get_price(), goods.get_number()
            current_price =  num * price
            tag = goods_tags.get_tag_by_name(name)
            current_price = self.__discountCalculator.get_discount_by_tag(tag, current_price, self.__ordertime)
            all_price += current_price

        all_price = self.__feedbackMap.calculate_feedback(all_price, self.__ordertime)
        all_price = price_round(all_price)

        print all_price
        return all_price

if __name__ == "__main__":
    config = "../config/tags.config"
    c = Calculator(config,"../testCase/testCaseA.txt")
    c.parse()
    c.calculate()
    c = Calculator(config,"../testCase/testCaseB.txt")
    c.parse()
    c.calculate()




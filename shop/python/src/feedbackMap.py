#!/usr/bin/python
# -*- coding: utf-8 -*-

from feedback import *
from dateformat import *

class FeedbackMap(object):
    def __init__(self):
        self.__feedback_map = dict()

    def add(self, feedback):
        date, upper, feedback = feedback.get_date(), feedback.get_upper(), feedback.get_feedback()
        self.__feedback_map[upper] = (date, feedback)

    def dump(self):
        for k,v in self.__feedback_map.items():
            print k, v

    def calculate_feedback(self, price, order_time):
        for k,v in self.__feedback_map.items():
            date, feedback = v
            if compare_date(order_time, date) >= 0:
                 return (price - feedback)

        return price 

if __name__ == '__main__':
    fm = FeedbackMap()
    date, upper, feedback = "2015.02.16", 1000 , 200
    fb = Feedback(date, upper, feedback)
    fb.dump()
    fm.add(fb)
    fm.dump()
    print fm.calculate_feedback(2000,'2014.2.16')
    print fm.calculate_feedback(2000,'2015.2.16')


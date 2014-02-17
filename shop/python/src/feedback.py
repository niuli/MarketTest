#!/usr/bin/python
# -*- coding: utf-8 -*-

class Feedback(object):
    def __init__(self, date, upper, feedback):
        self.__date  = date
        self.__upper = float(upper)
        self.__feedback = float(feedback)

    def dump(self):
        print self.__date, self.__upper, self.__feedback

    def get_date(self):
    	return self.__date

    def get_upper(self):
        return self.__upper

    def get_feedback(self):
    	return self.__feedback

if __name__ == '__main__':
    date, upper, feedback = "2014.02.16", 1000 , 200
    fb = Feedback(date, upper, feedback)
    fb.dump()

#!/usr/bin/python
# -*- coding: utf-8 -*-
from feedback import *
from dateformat import *
import re

class FeedbackParser(object):
    def __init__(self):
        pass

    def check_upper(self, upper):
        if type(eval(upper) == int) :
            n = int(upper)
            if n >= 1:
                return True
        return False

    def check_feedback(self, feedback):
        if type(eval(feedback) == int) :
            n = int(feedback)
            if n >= 1:
                return True
        return False

    def check_date(self, date):
        return check_date(date)

    def check_limit(self, upper, feedback):
        if int(upper) > int(feedback):
            return True
        return False

    def parse(self, r):
        c = re.findall(r"^(.+?)\ (.+?)\ (.+?)$",r)

        if len(c) > 0:
            date, upper, feedback = c[0][0], c[0][1], c[0][2]
            if self.check_date(date) and self.check_upper(upper) and self.check_feedback(feedback):
                if self.check_limit(upper, feedback):
                    fb = Feedback(date, upper, feedback)
                    return fb
        return None

if __name__ == "__main__":
    fp = FeedbackParser()
    r = "2014.3.2 1000 200"
    fb = fp.parse(r)
    fb.dump()

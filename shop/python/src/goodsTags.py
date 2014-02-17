#!/usr/bin/python
# -*- coding: utf-8 -*-

class GoodsTags(object):
    def __init__(self, file):
        self.__tags = dict()
        self.load_tags(file)

    def load_tags(self, file):
        f = open(file,"r")
        for r in f.readlines():
            m = r.rstrip().split("：")
            tag, goods = m[0], m[1].split("，")
            self.__tags[tag] = goods
        f.close()

    def dump_tags(self):
        for (d,x) in self.__tags.items():
            m = "" 
            for r in x:
                m += r+','
            print d, m

    def judge_tag(self, tag):
        if self.__tags.has_key(tag):
            return True
        else :
            return False

    # If goods type become more, this can be optimized by revert map.
    def get_tag_by_name(self, name):
        for (k,v) in self.__tags.items():
            for r in v:
                if r == name:
                    return k
        return "NoTag"

if __name__ == '__main__':
    goodsTags = GoodsTags("../config/tags.config")
    print "Goods tags:"
    goodsTags.dump_tags()
    print goodsTags.judge_tag("aaa")
    print goodsTags.judge_tag("电子")
    print goodsTags.get_tag_by_name("ipad")
    print goodsTags.get_tag_by_name("面包")

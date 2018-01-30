# -*- coding:utf-8 -*-

#!/usr/bin/env python

class Shape(object):
    def __init__(self, weidth, height):
        self.weidth = weidth
        self.height = height
        self.halfWeidth = weidth/2
        self.halfHeight = height/2

    def refresh(self, weidth = 0, height = 0):
        if weidth > 0:
            self.weidth = weidth
            self.halfWeidth = weidth/2
        if height > 0:
            self.height = height
            self.halfHeight = height/2


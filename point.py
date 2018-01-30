# -*- coding:utf-8 -*-

#!/usr/bin/env python

class Point(object):
    def __init__(self, point):
        self.refresh(point)

    def getPoint(self):
        return (self.x, self.y)

    def refresh(self, point):
        self.x = point[0]
        self.y = point[-1]


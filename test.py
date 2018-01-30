# -*- coding:utf-8 -*-

#!/usr/bin/env python

import pygame
from pygame.locals import *
import sys

BACKGROUND_IMAGE_FILENAME = '123.png'
MOUSE_IMAGE_FILENAME = '456.png'
INIT_BACKGROUND_POINT = (0,0)
REMOVE_SAVE_EVENT = (K_LEFT, K_RIGHT, K_UP, K_DOWN)
REMOVE_SPEED = 1

class Points(object):
    def __init__(self, point):
        self.refresh(point)

    def getPoint(self):
        return (self.x, self.y)

    def refresh(self, point):
        self.x = point[0]
        self.y = point[-1]

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

class WindowManager(object):
    def __init__(self, resolution, colorDepth):
        self.resolution = Points(resolution)
        self.colorDepth = colorDepth
        self.displayMod = RESIZABLE
        self.backgroundPoint = Points((0,0))
        self.continueEvents = []
        self.screen = pygame.display.set_mode(self.resolution.getPoint(), self.displayMod, self.colorDepth)

    def onStart(self):
        pygame.display.set_caption("世界!")
        self.background = pygame.image.load(BACKGROUND_IMAGE_FILENAME).convert_alpha()
        self.mouse_cursor = pygame.image.load(MOUSE_IMAGE_FILENAME).convert_alpha()
        self.mouseData = Shape(self.mouse_cursor.get_width(), self.mouse_cursor.get_height())
        self.font = pygame.font.SysFont("宋体", 40)
        self.onRefresh()

    #事件触发
    def doEvent(self, event):
        type2Action = {QUIT:self._quitAction, KEYDOWN:self._keyDownAction, KEYUP:self._keyUpAction, VIDEORESIZE:self._videoResizeAction,\
                }
        type = event.type
        if type in type2Action:
            type2Action[type](event)

    def _quitAction(self, event):
        sys.exit()

    def _keyDownAction(self, event):
        key = event.key
        key2action = {K_f:self._keyDown4FAction}
        if key in key2action:
            key2action[key]()
        if key in REMOVE_SAVE_EVENT:
            eventData = (event, key)
            if eventData not in self.continueEvents:
                self.continueEvents.append(eventData)

    def _keyDown4FAction(self):
        if self.displayMod == RESIZABLE:
            self.displayMod = FULLSCREEN
        else:
            self.displayMod = RESIZABLE
        self.screen = pygame.display.set_mode(self.resolution.getPoint(), self.displayMod, self.colorDepth)
        pygame.display.update()

    def _keyUpAction(self, event):
        for eventData in self.continueEvents:
            if eventData and event.key == eventData[1]:
                self.continueEvents.remove(eventData)

    def _videoResizeAction(self, event):
        self.resolution.refresh(event.size)
        self.screen = pygame.display.set_mode(self.resolution.getPoint(), self.displayMod, self.colorDepth)
        pygame.display.set_caption("Window resized to "+str(event.size))

    #持续按键事件
    def doContinueEvent(self):
        key2action = {K_LEFT:self._leftContinueAction, K_RIGHT:self._rightContinueAction,\
                K_UP:self._upContinueAction, K_DOWN:self._downContinueAction}
        for eventData in self.continueEvents:
            event = eventData[0]
            if event.type == KEYDOWN:
                key2action[event.key]()

    def _leftContinueAction(self):
        self.backgroundPoint.x -= REMOVE_SPEED

    def _rightContinueAction(self):
        self.backgroundPoint.x += REMOVE_SPEED

    def _upContinueAction(self):
        self.backgroundPoint.y -= REMOVE_SPEED

    def _downContinueAction(self):
        self.backgroundPoint.y += REMOVE_SPEED

    def onRefresh(self):#游戏主循环
        while True:
            for event in pygame.event.get():
                self.doEvent(event)
            if self.continueEvents:
                self.doContinueEvent()

            self.screen.fill((0,0,0)) #填充色
            self.screen.blit(self.background, (0,0))#将背景图画上去
            self.screen.blit(self.background, self.backgroundPoint.getPoint())
            x, y = pygame.mouse.get_pos()#获得鼠标位置
            x -= self.mouseData.halfWeidth
            y -= self.mouseData.halfHeight
            self.screen.blit(self.mouse_cursor, (x, y))#把光标画上去
            textSurface = self.font.render(u"%s"%(str(self.backgroundPoint.getPoint())), True, (0, 0, 0))
            self.screen.blit(textSurface, (0,0))

            pygame.display.update()
            #刷新一下画面

pygame.init()
window = WindowManager((640, 480), 32)
window.onStart()


# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:08:00 2020

@author: jzb
"""
from manimlib.imports import *

class Hello_Manim(Scene):
    def construct(self):
        helloworld=TextMobject("Hello World",color=RED)
        rectangle=Rectangle(color=BLUE)
        #建立一个矩形对象rectangle
        rectangle.surround(helloworld)
        #该矩形正好包裹住helloworld
        group1=VGroup(helloworld,rectangle)
        #把helloworld和rectangle放在一个vgroup组中，方便同时操作
        hellomanim=TextMobject("Hello Manim",color=BLUE)
        #使用mobject创建对象
        hellomanim.scale(2.5)
        #指定hellomanim的大小
        self.play(Write(helloworld))
        self.wait(1)
        self.play(FadeIn(rectangle))
        self.wait(1)
        self.play(ApplyMethod(group1.scale,2.5))
        self.wait(1)
        self.play(Transform(helloworld,hellomanim))
        self.wait(1)
        
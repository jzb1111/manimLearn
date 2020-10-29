# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 23:04:58 2020

@author: jzb
"""
from manimlib.imports import *
import numpy as np

class practice(Scene):
    def construct(self):
        circle01=Circle(color=RED,fill_color=RED,fill_opacity=0.5)#默认半径radius=1
        circle02=Circle(color=RED,fill_color=RED,fill_opacity=0.5)
        square01=Square(color=RED,fill_color=RED,fill_opacity=0.5,side_length=2.0)
        
        #属性有color,fill_color,fill_opacity,height,width
        circle01.shift(LEFT*np.sqrt(2)/2)
        circle02.shift(RIGHT*np.sqrt(2)/2)
        square01.shift(DOWN*np.sqrt(2)/2)
        #经过计算，形成心形的关键是根号2
        square01.rotate(np.pi/4)
        circle_scope=VGroup(circle01,circle02,square01)
        circle_scope.shift(UP*((3/2)*np.sqrt(2)-1)/2)
        
        wid=(3*np.sqrt(2)+2)/(5*np.sqrt(2))
        hei=4*wid
        rectangle01=Rectangle(color=RED,fill_color=RED,fill_opacity=0.5,height=hei,width=wid)
        rectangle02=Rectangle(color=RED,fill_color=RED,fill_opacity=0.5,height=hei,width=wid)
        
        rectangle01.rotate(np.pi/4)
        rectangle02.rotate(-1*np.pi/4)
        
        rectangle_scope=VGroup(rectangle01,rectangle02)
        #rectangle_scope.shift(UP)
        
        square02=Square(color=RED,fill_color=RED,fill_opacity=0.5,side_length=(3*np.sqrt(2)/2)+1)
        circle03=Circle(color=RED,radius=((3*np.sqrt(2)/2)+1)/7,fill_color=BLACK,fill_opacity=0.5)
        circle04=Circle(color=RED,radius=((3*np.sqrt(2)/2)+1)/7,fill_color=BLACK,fill_opacity=0.5)
        circle03.shift(UP*((3*np.sqrt(2)/2)+1)/4+LEFT*((3*np.sqrt(2)/2)+1)/4)
        circle04.shift(UP*((3*np.sqrt(2)/2)+1)/4+RIGHT*((3*np.sqrt(2)/2)+1)/4)
        robo_scope=VGroup(square02,circle03,circle04)
        robo_scope.shift(RIGHT*5)
        
        rectangle_robo_scope=VGroup(rectangle_scope,robo_scope)
        
        all_shape_scope=VGroup(circle_scope,rectangle_robo_scope)
        
        text01=TextMobject("LOVE DEATH + ROBOT",color=RED)
        text01.scale(1.8)
        text01.shift(DOWN*((3/2)*np.sqrt(2)+1)/2+DOWN)
        line01=Line(start=DOWN*((3/2)*np.sqrt(2)+1)/2+DOWN+LEFT*5+LEFT*((3/2)*np.sqrt(2)+1)/2,end=DOWN*((3/2)*np.sqrt(2)+1)/2+DOWN+RIGHT*5+RIGHT*((3/2)*np.sqrt(2)+1)/2)
        all_object=VGroup(all_shape_scope,line01,text01)
        #circle_scope.fill_opacity=1.0
        #self.add(circle_scope)
        #self.add(rectangle_scope)
        
        self.play(FadeIn(circle_scope))
        #ApplyMethod可以在一个对象上应用变化
        self.play(ApplyMethod(circle_scope.shift,LEFT*5))
        #不加FadeIn就无法生成，需要知道原因
        #self.wait(3)
        self.play(FadeIn(rectangle_robo_scope))
        self.play(ApplyMethod(all_shape_scope.set_opacity,1))
        #self.play(ApplyMethod(rectangle_robo_scope.set_opacity,1))
        self.play(ShowCreation(line01))
        self.wait(3)
        self.play(Transform(line01,text01))
        self.wait(3)
        
        self.play(ApplyMethod(all_object.shift,UP))
        self.wait(3)
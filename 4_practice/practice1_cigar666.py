# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:15:40 2020

@author: asus
"""

from manimlib.imports import *
import numpy as np

class practice(Scene):
    def construct(self):
        #################
        #+Making object+#
        #################
        circle01=Circle(color=RED,fill_color=RED,fill_opacity=0.5)#默认半径radius=1
        circle02=Circle(color=RED,fill_color=RED,fill_opacity=0.5)
        square01=Square(color=RED,fill_color=RED,fill_opacity=0.5)
        love=VGroup(circle01,circle02,square01)
        
        rect01=Rectangle(height=0.8,width=4,fill_color=RED,color=RED,fill_opacity=0.5)
        rect02=Rectangle(height=0.8,width=4,fill_color=RED,color=RED,fill_opacity=0.5)
        death=VGroup(rect01,rect02)
        
        square02=Square(fill_color=RED,color=RED,fill_opacity=0.5)
        square02.scale(1.6)
        c01=Circle(fill_color=BLACK,color=RED,fill_opacity=0.5)
        c02=Circle(fill_color=BLACK,color=RED,fill_opacity=0.5)
        c01.scale(0.45)
        c02.scale(0.45)
        robots=VGroup(square02,c01,c02)
        
        line01=Line(np.array([-6,-2.4,0]),np.array([6,-2.4,0]),color=RED)
        line01.set_height(0.2)
        
        text01=TextMobject("LOVE\nDEATH\n+\nROBOTS",color=RED)
        text01.scale(1.8)
        
        group_all=VGroup(love,death,robots,line01,text01)
        #################
        #-Making object-#
        #################
        
        ############
        #+position+#
        ############
        circle01.shift((UP+LEFT)*np.sqrt(2)/2)
        circle02.shift((UP+RIGHT)*np.sqrt(2)/2)
        square01.rotate(np.pi/4)
        
        rect01.rotate(np.pi/4)
        rect02.rotate(-np.pi/4)
        
        c01.shift(np.array([-0.72,0.6,0]))
        c02.shift(np.array([0.72,0.6,0]))
        robots.shift(RIGHT*4)
        
        text01.shift(DOWN*2.5)
        ############
        #-position-#
        ############
        
        ##################
        #+Showing object+#
        ##################
        self.play(ShowCreation(circle01),ShowCreation(circle02),ShowCreation(square01))
        
        self.wait(1)
        self.play(ApplyMethod(love.shift,LEFT*4))
        self.wait(1)
        
        self.play(ShowCreation(rect01),ShowCreation(rect02))
        self.wait(1)
        
        self.play(ShowCreation(square02))
        self.play(ShowCreation(c01),ShowCreation(c02))
        self.wait(1)
        
        self.play(Transform(line01,text01))
        self.wait(1)
        self.play(ApplyMethod(group_all.shift,UP*0.5))
        self.wait(1)
        ##################
        #-Showing object-#
        ##################
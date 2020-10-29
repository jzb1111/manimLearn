# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:17:56 2020

@author: jzb
"""
from manimlib.imports import *
class Basic_Shape(Scene):
    def construct(self):
        #making object
        ring=Annulus(inner_radius=0.4,outer_radius=1,color=BLUE)
        square=Square(color=ORANGE,fill_color=ORANGE,fill_opacity=0.5)
        rect=Rectangle(height=3.2,width=1.2,color=PINK,fill_color=PINK,fill_opacity=0.5)
        
        line01=Line(np.array([0,3.6,0]),np.array([0,2,0]),color=BLUE)
        line02=Line(np.array([-1,2,0]),np.array([-1,-1,0]),color=BLUE)
        line03=Line(np.array([1,2,0]),np.array([1,0.5,0]),color=BLUE)
        #position
        ring.shift(UP*2)
        square.shift(LEFT+DOWN*2)
        rect.shift(RIGHT+DOWN*(3.2/2-0.5))
        #show object
        self.add(line01)
        self.play(GrowFromCenter(ring))
        self.wait(.5)
        self.play(FadeIn(line02),FadeIn(line03))
        self.wait(.5)
        self.play(FadeInFromDown(square))
        self.play(FadeInFromDown(rect))
        self.wait()
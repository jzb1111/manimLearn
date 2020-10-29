# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 08:13:34 2020

@author: asus
"""

from manimlib.imports import *
import numpy as np
import cv2

im1=cv2.imread("1.png")
im2=cv2.imread("2.png")
im3=cv2.imread("3.png")

class Invoker(Scene):
    #CONFIG={'im1':'./11.jpg','im2':'./22.jpg','im3':'./33.jpg'}#换小图试试
    
    def construct(self):
        ice=ImageMobject(im1)
        ice.set_height(5)
        wex=ImageMobject(im2)
        wex.set_height(5)
        fire=ImageMobject(im3)
        fire.set_height(5)
        
        wex.shift(UP*6)
        ice.next_to(wex,LEFT)
        fire.next_to(wex,DOWN)
        
        self.play(FadeIn(ice),run_time=1.5)
        self.play(FadeIn(wex),run_time=1.5)
        self.play(FadeIn(fire),run_time=1.5)
        
        self.wait(1)
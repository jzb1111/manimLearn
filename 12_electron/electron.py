# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 16:59:12 2020

@author: asus
"""

from manimlib.imports import *
import numpy as np

class Electron(Scene):
    def construct(self):
        plane=NumberPlane(color=RED)
        plane.add(plane.get_axis_labels())
        self.add(plane)
        
        vec_list=[]
        center=ORIGIN
        side_len=7
        for i in range(10):
            for j in range(10):
                location=(i-5)*UP+(j-5)*RIGHT
                s=np.sum(np.square(location))**0.8
                
                vec_dire=-(location-ORIGIN)/s
                vec_list.append(Vector(vec_dire).shift(location))
        vec_group=VGroup(*vec_list)
        self.play(ShowCreation(vec_group))
        self.wait(2)
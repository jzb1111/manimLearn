# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:37:49 2020

@author: asus
"""

from manimlib.imports import *
import numpy as np

class SimpleField(Scene):
    def construct(self):
        plane=NumberPlane(color=RED)
        plane.add(plane.get_axis_labels())
        self.add(plane)
        
        points=[x*RIGHT+y*UP for x in np.arange(-5,5,1) for y in np.arange(-3,3,1)]
        
        vec_field=[]
        for point in points:
            field=0.5*RIGHT+0.5*UP
            result=Vector(field).shift(point)
            vec_field.append(result)
        draw_field=VGroup(*vec_field)
        self.play(ShowCreation(draw_field),run_time=4)
        self.wait(2)
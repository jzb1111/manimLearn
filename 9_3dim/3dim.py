# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 22:56:33 2020

@author: asus
"""

from manimlib.imports import *
import numpy as np

class Sun_and_planet(ThreeDScene):
    def construct(self):
        r=7
        sun=Sphere(radius=1.6)
        planet=Sphere(radius=0.4)
        orbit=Circle(radius=r)
        planet.shift(UP*r)
        system=VGroup(orbit,sun,planet)
        system.shift(DOWN*2+LEFT*2)
        
        F_vector=Vector(np.array([0,-5,0]),color=YELLOW)
        F_vector.next_to(planet,DOWN*0.6)
        
        self.set_camera_orientation(phi=65*PI/180,theta=PI/3)
        self.play(ShowCreation(orbit))
        self.play(ShowCreation(sun),FadeIn(planet))
        self.wait(1)
        self.play(ShowCreation(F_vector))
        self.wait(1)
    
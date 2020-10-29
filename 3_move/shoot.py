# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 19:21:24 2020

@author: jzb
"""
from manimlib.imports import *

class Shoot(Scene):
    def construct(self):
        #make aim_scope
        circle1=Circle(color=BLUE)
        circle2=Circle(color=RED,fill_color=RED,fill_capicity=1)
        circle2.scale(0.1)
        line1=Line(np.array([-1,0,0]),np.array([1,0,0]),color=RED)
        line2=Line(np.array([0,1,0]),np.array([0,-1,0]),color=RED)
        aim_scope=VGroup(circle1,circle2,line1,line2)
        
        #making target
        target_list=[]
        for i in range(3):
            for j in range(5):
                targetij=Circle(color=YELLOW,fill_color=YELLOW,fill_capicity=0.4)
                targetij.scale(0.4)
                targetij.shift(np.array([-4+j*2,-2+i*2,0]))
                self.play(FadeIn(targetij))
                target_list.append(targetij)
        self.wait(1)
        #move&shoot animation
        def shoot_ij(i,j):
            target_ij=target_list[j+5*i]
            self.play(ApplyMethod(aim_scope.next_to,target_ij,0))
            self.play(ApplyMethod(target_ij.set_fill,GREY),ApplyMethod(target_ij.set_color,GREY))
            self.wait(0.5)
            ij=TextMobject("(%d,%d)"%(i,j),color=GREY)
            ij.next_to(target_ij,DOWN)
            self.play(Write(ij))
            self.wait(1)
            return 0
        
        self.add(aim_scope)
        self.play(ApplyMethod(aim_scope.shift,DOWN*3+LEFT*6.1))
        shoot_ij(0,1)
        shoot_ij(2,0)
        shoot_ij(1,3)
        shoot_ij(0,0)
        shoot_ij(2,4)
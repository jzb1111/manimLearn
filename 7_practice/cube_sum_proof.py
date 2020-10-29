# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:26:50 2020

@author: asus
"""

from manimlib.imports import *
import numpy as np

class cubesumproof(Scene):
    def construct(self):
        luxunverbtext=TextMobject("Making animation with manim is really funny.")
        luxuntext=TextMobject("--Lu Xun")
        proof1text=TextMobject("Proof 1:")
        proof2text=TextMobject("Proof 2:")
        i1_formula=self.gen_formula(1)
        i2_formula=self.gen_formula(2)
        i3_formula=self.gen_formula(3)
        i_formula_group=VGroup(i1_formula,i2_formula,i3_formula)
        
        square_group1=self.gen_side_square(1,RIGHT,4)
        
        #position
        i1_formula.next_to(proof1text,DOWN)
        i2_formula.next_to(i1_formula,DOWN)
        i3_formula.next_to(i2_formula,DOWN)
        
        i_formula_group.to_edge(LEFT)
        square_group1.to_edge(RIGHT)
        
        #animation
        self.play(ShowCreation(proof1text))
        self.play(ShowCreation(i_formula_group))
        self.play(ShowCreation(square_group1))
        self.wait(5)
    def gen_formula(self,num_i):
        str_i=str(num_i)
        text_left="i="+str_i+","+str(num_i+1)+"^{4} - "+str_i+"^{4}"
        text_right="4 \\times "+str_i+"^{3} + "+"6 \\times"+str_i+"^{2}"+"+ 4\\times "+str_i+" +1"
        text_inner=text_left+"="+text_right
        return TexMobject(text_inner)
    
    def gen_square(self,side):
        return Square(side_length=side)
    
    def gen_side_square(self,side,ori,num):
        a=self.gen_square(side)
        lis=[a]
        out=VGroup(a)
        for i in range(num-1):
            lis.append(self.gen_square(side))
            lis[i+1].next_to(lis[i],ori)
            
            out.add(lis[-1])
        return out
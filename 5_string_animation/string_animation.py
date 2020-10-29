# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:06:43 2020

@author: asus
"""
from manimlib.imports import *
import numpy as np

class luxun(Scene):
    def construct(self):
        quote=TextMobject("使用manim制作数学动画很有意思")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2=TextMobject("Making animation by manim is funny.")
        quote2.set_color(BLUE)
        author=TextMobject("- 鲁迅",color=PINK)
        
        author.next_to(quote.get_corner(DOWN+RIGHT),DOWN)
        
        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote,quote2),
                  ApplyMethod(author.move_to,quote2.get_corner(DOWN+RIGHT)+DOWN+2*LEFT))
        self.play(ApplyMethod(author.scale,1.6))
        author.match_color(quote2)
        self.play(FadeOut(quote),FadeOut(author))
        self.wait()

class skin(Scene):
    def construct(self):
        square=Square(side_length=5,fill_color=BLUE,fill_opacity=0.5)
        label=TextMobject("扭一下身体")
        label.bg=BackgroundRectangle(label,fill_opacity=1)
        label_group=VGroup(label.bg,label)
        label_group.rotate(TAU/8)
        label2=TextMobject("加个边框",color=BLACK)
        label2.bg=SurroundingRectangle(label2,color=BLUE,fill_color=RED,fill_opacity=0.5)
        label2_group=VGroup(label2,label2.bg)
        label2_group.next_to(label_group,DOWN)
        label3=TextMobject("变成彩虹")
        label3.scale(1.8)
        label3.set_color_by_gradient(RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE)
        label3.to_edge(DOWN)
        
        self.add(square)
        self.play(FadeIn(label_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))
        self.wait()
        
class Latex(Scene):
    def construct(self):
        title=TextMobject("This is some \\\LaTex")
        basel=TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
            )
        VGroup(title,basel).arrange(DOWN)
        self.play(Write(title),
                  FadeInFrom(basel,UP)
                  )
        self.wait()
        
class num_square(Scene):
    def construct(self):
    
        #create equation
        equal=TextMobject("=",color=RED)
        eq_left01=TextMobject("$1^3+2^3+3^3+ \quad \dots \quad+n^3$",color=GREEN)
        eq_right01=TextMobject("$(1+2+3+ \quad \dots \quad+n)^2$",color=YELLOW)
        
        eq_left02=TextMobject("$\Sigma_{i=1}^{n} i^{3}$",color=GREEN)
        eq_right02=TextMobject("$(\Sigma_{i=1}^{n} i)^{2}$",color=YELLOW)
        equation02=VGroup(equal,eq_left02,eq_right02)
        
        #position
        eq_left01.next_to(equal,LEFT)
        eq_right01.next_to(equal,RIGHT)
        eq_left02.next_to(equal,LEFT)
        eq_right02.next_to(equal,RIGHT)
        
        #animation
        self.play(FadeIn(eq_left01),FadeIn(equal),FadeIn(eq_right01))
        self.wait(1)
        self.play(ReplacementTransform(eq_left01,eq_left02))
        self.play(ReplacementTransform(eq_right01,eq_right02))
        self.wait(1)
        self.play(ApplyMethod(equation02.scale,2.4))
        self.wait(1)
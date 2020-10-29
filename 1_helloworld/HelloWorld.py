# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 22:15:15 2020

@author: jzb
"""
#from import_manim import importManim
#importManim()
#from big_ol_pile_of_manim_imports import *

from manimlib.imports import *
#import manimlib
#manimlib.main()
class Hello_world(Scene):
    
    def construct(self):
        ######################################################################
        #construct:
        #Use a construct() function to tell Manim what should go on in the 
        #Scene.
        #其实这是个抽象方法，具体实现由实例化时传递的construct实现。
        # To be implemented in subclasses
        ######################################################################
        
        ######################################################################
        #making object创建对象
        helloworld=TextMobject("Hello World",corlor=RED)
        ######################################################################
        #position
        
        #showing object
        self.play(Write(helloworld))
        #helloworld保留在屏幕中秒钟
        self.wait(1)

#运行时cmd cd到manim目录下并activate manim环境
#输入
#python -m manim HelloWorld.py Hello_word -pl
#pl,pm等是动画画质。

##############################################
#方法二
#直接在本文件目录下
#manim HelloWorld.py Hello_world
#即可
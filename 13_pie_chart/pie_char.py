# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 18:50:02 2020

@author: asus
"""

from manimlib.imports import *
import numpy as np
#更多内容在bilibili上，piechart类没有写

class ShowPieChart(PieChart):
    def construct(self):
        color_list=[RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE]
        
        data_info=(15.36,color_list[0],'广东'),(8.35,color_list[1],'江苏'),(7.43,color_list[2],'浙江'),\
                    (5.69,color_list[3],'四川'),(5.55,color_list[4],'山东'),(57.62,color_list[5],'河南')
        
        title='各省'
        
        self.create_anim(title,*data_info)
        
        self.wait()


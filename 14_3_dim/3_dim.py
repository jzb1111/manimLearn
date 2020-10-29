# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 10:14:19 2020

@author: asus
"""

from manimlib.imports import *
import numpy as np

class Test_camera(ThreeDScene):
    
    def construct(self):
        
        axes=ThreeDAxes()
        cube_yellow=Cube(fill_color=YELLOW,stroke_width=2,strok_color=WHITE)
        sphere_blue=Sphere(fill_color=BLUE,checkerboard_color=None).shift(OUT*2)
        cube_green=Cube(fill_color=GREEN).scale([2,0.5,0.5]).shift(RIGHT*3.25)
        
        phi_0,theta_0=0,0#起始角度
        phi,theta=60*DEGREES,-120*DEGREES#目标角度
        
        self.set_camera_orientation(phi=phi_0,theta=theta_0)
        self.add(axes,cube_yellow,sphere_blue,cube_green)
        self.wait()
        dt=1/15
        delta_phi,delta_theta=(phi-phi_0)/30,(theta-theta_0)/60
        for i in range(30):
            phi_0+=delta_phi
            self.set_camera_orientation(phi=phi_0,theta=theta_0)
            self.wait(dt)
        for i in range(60):
            theta_0+=delta_theta
            self.set_camera_orientation(phi_0,theta_0)
            self.wait(dt)
        self.wait(2)
        
class Test_camera2(ThreeDScene):
    
    def construct(self):
        
        axes=ThreeDAxes()
        cube_yellow=Cube(fill_color=YELLOW,stroke_width=2,strok_color=WHITE)
        sphere_blue=Sphere(fill_color=BLUE,checkerboard_color=None).shift(OUT*2)
        cube_green=Cube(fill_color=GREEN).scale([2,0.5,0.5]).shift(RIGHT*3.25)
        
        phi_0,theta_0,distance_0,gamma_0=0,0,50,0#起始角度
        phi,theta,distance=60*DEGREES,-120*DEGREES,500#目标角度
        
        self.set_camera_orientation(phi=phi_0,theta=theta_0)
        self.add(axes,cube_yellow,sphere_blue,cube_green)
        self.wait()
        dt=1/15
        delta_phi,delta_theta,delta_distance,delta_gamma=(phi-phi_0)/30,(theta-theta_0)/60,1,1*DEGREES
        for i in range(30):
            phi_0+=delta_phi
            self.set_camera_orientation(phi=phi_0,theta=theta_0)
            self.wait(dt)
        for i in range(60):
            theta_0+=delta_theta
            #distance_0+=delta_distance
            self.set_camera_orientation(phi_0,theta_0)
            self.wait(dt)
        for i in range(60):
            distance_0+=delta_distance
            self.set_camera_orientation(phi_0,theta_0,distance=distance_0)
            self.wait(dt)
        for i in range(60):
            gamma_0+=delta_gamma
            self.set_camera_orientation(phi_0,theta_0,gamma=gamma_0)
            self.wait(dt)    
        self.wait(2)

class Curve_3D_test(SpecialThreeDScene):
    CONFIG={
        "default_angled_camera_position":{
            "phi":65*DEGREES,
            "theta":-60*DEGREES,
            "distance":50,
            "gamma":0}
        }
    def construct(self):
        self.set_camera_to_default_position()
        r=2#radius
        w=4
        circle=ParametricFunction(lambda t:r*complex_to_R3(np.exp(1j*w*t)),
                                  t_min=0,t_max=TAU*1.5,color=RED,stroke_width=8)
        spiral_line=ParametricFunction(lambda t:r*complex_to_R3(np.exp(1j*w*t))+OUT*t,
                                       t_min=0,t_max=TAU*1.5,color=PINK,stroke_width=8)
        circle.shift(IN*2.5),spiral_line.shift(IN*2.5)
        axes=self.get_axes()
        self.add(axes,circle)
        self.wait()
        self.play(TransformFromCopy(circle,spiral_line,rate_func=there_and_back),run_time=4)
        self.wait()

class Surface_test_01(SpecialThreeDScene):
    CONFIG={
        "default_angled_camera_position":{
            "phi":65*DEGREES,
            "theta":-60*DEGREES,
            "distance":50,
            "gamma":0}
        }        
    def construct(self):
        self.set_camera_to_default_position()
        axes=self.get_axes()
        surface=ParametricSurface(lambda u,v:np.array([u,v,np.sin(u**2+v**2)]),
                                  u_min=-4,u_max=4,v_min=-4,v_max=4,resolution=(120,120))
        self.add(axes,surface)
        self.wait(5)
    
class Surface_test_02(SpecialThreeDScene):
    CONFIG={
        "default_angled_camera_position":{
            "phi":65*DEGREES,
            "theta":-60*DEGREES,
            "distance":50,
            "gamma":0}
        }
    def construct(self):
        self.set_camera_to_default_position()
        axes=self.get_axes()
        w=1
        surface_01=ParametricSurface(lambda u,v:v*complex_to_R3(np.exp(1j*w*u)),
                                     u_min=0,u_max=TAU,v_min=1,v_max=3,checkerboard_colors=None,
                                     fill_color=BLUE_B,fill_opacity=0.8,stroke_color=BLUE_A,resolution=(60,10))
        surface_02=ParametricSurface(lambda u,v:v*complex_to_R3(np.exp(1j*w*u))+OUT*u/PI*2,
                                     u_min=0,u_max=TAU,v_min=1,v_max=3,checkerboard_colors=None,
                                     fill_color=BLUE_D,fill_opacity=0.8,stroke_color=BLUE_A,resolution=(60,10))
        self.add(axes,surface_01)
        self.wait()
        self.play(TransformFromCopy(surface_01,surface_02,rate_func=linear),run_time=5)
        self.wait(2)
        
class Surface_test_03(SpecialThreeDScene):
    CONFIG={
        "default_angled_camera_position":{
            "phi":65*DEGREES,
            "theta":-60*DEGREES,
            "distance":50,
            "gamma":0}
        }
    def construct(self):
        self.set_camera_to_default_position()
        #####################################
        #R=sqrt(x^2+y^2)+eps,z=sin(R)/R*8-2 #eps为一个浮点数达到的最高精度
        #####################################
        R=lambda x,y:np.sqrt(x**2+y**2)+1e-8
        surface_origin=ParametricSurface(lambda u,v:np.array([u,v,8*np.sin(R(u,v))/R(u,v)-2]),
                                         u_min=-8,u_max=8,v_min=-8,v_max=8,resolution=(50,50)).scale(0.5)
        #surface_frame为线框图
        surface_frame=surface_origin.copy().set_fill(color=BLUE,opacity=0)
        #colored_frame和colored_surface为上色后的曲面线框图和上色后的曲面
        r=np.linspace(1e-8,8*np.sqrt(2),1000)
        z=(8*np.sin(r)/r-2)/2
        z_l=max(z)-min(z)
        colors=color_gradient([BLUE,YELLOW,RED],100)
        colored_frame=surface_frame.copy()
        colored_surface=surface_origin.copy()
        for ff,fs in zip(colored_frame,colored_surface):
            f_z=ff.get_center()[-1]
            ff.set_color(colors[int((f_z-min(z))/z_l*90)])
            fs.set_color(colors[int((f_z-min(z))/z_l*90)])
        self.add(surface_origin)
        self.wait()
        self.play(ReplacementTransform(surface_origin,surface_frame),run_time=2)
        self.wait()
        self.play(ReplacementTransform(surface_frame,colored_frame),run_time=2)
        self.wait()
        self.play(ReplacementTransform(colored_frame,colored_surface),run_time=2)    
        self.wait(2)
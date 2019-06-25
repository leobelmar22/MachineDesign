#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 16:42:04 2018

@author: leocosta
"""

''' Machine Design Final Project - Valve Calculations and Data Analysis'''
import numpy as np
import math
import matplotlib.pyplot as plt
from decimal import Decimal
import pandas as pd

def svaj_calculations(follower_stroke,w,poly):
    h = follower_stroke #inches
    beta = math.degrees(math.pi/2) #degrees
    theta = np.linspace(0,beta,100) #degrees
    x = theta/beta
    dx = x[1]-x[0]
    angular_velocity = w #rad/s
    max_list = []
    min_list = []
    
    if poly == 3:
        sr = h*(10*x**3 - 15*x**4 + 6*x**5)
        vr = np.gradient(sr,dx)
        ar = np.gradient(vr,dx)
        jr = np.gradient(ar,dx)
        for i in [sr,vr,ar,jr]:
            max_list.append(max(i))
            min_list.append(min(i))
        plt.figure(1)
        plt.subplot(4,1,1)
        plt.plot(x,sr,color = 'red')
        plt.subplot(4,1,2)
        plt.plot(x,vr, color = 'blue')
        plt.subplot(4,1,3)
        plt.plot(x, ar, color = 'yellow')
        plt.subplot(4,1,4)
        plt.plot(x,jr, color = 'green')
        return max_list, min_list
    
    elif poly == 4:
        sr = h*(35*x**4 - 84*x**5 +70*x**6 -20*x**7)
        vr = np.gradient(sr,dx)
        ar = np.gradient(vr,dx)
        jr = np.gradient(ar,dx)
        for i in [sr,vr,ar,jr]:
            max_list.append(max(i))
            min_list.append(min(i))
        plt.figure(1)
        plt.subplot(4,1,1)
        plt.plot(x,sr,color = 'red')
        plt.subplot(4,1,2)
        plt.plot(x,vr, color = 'blue')
        plt.subplot(4,1,3)
        plt.plot(x, ar, color = 'yellow')
        plt.subplot(4,1,4)
        plt.plot(x,jr, color = 'green')
        return max_list, min_list
    
def svaj_calculation_test():
    follower_stroke = input ("Follower Stroke: ")
    w = input ("Angular Velocity: ")
    poly = input ("Type of Polynomial: ")
    if poly != 3 or poly !=4:
        print ("Invalid size polynomial")
    results = svaj_calculations(follower_stroke,w,poly)
    print(results)
    
def cam_calculations(rp, exc):
    b = 1.5 # distance from center to the intersection of axis of trans and eff link 1
    # exc = distance from center of follower to center of cam
    # rp = radius of prime circle
    s = 1.5 #distance from follower center to intersection of prime circle and axis of motion
    phi_rad = math.atan((b - exc)/(s+math.sqrt((rp**2) - (exc**2)))) # pressure angle
    phi_deg = math.degrees(phi_rad)
    return phi_deg
    
#svaj_calculations_test()
def cam_calculation_test(rp_min, rp_max, exc_min, exc_max):
    rp_list = np.linspace(rp_min,rp_max,100)
    exc_list = np.linspace(exc_min,exc_max,100)
    result_list = []
    rp_exc_list = []
    for i in rp_list:
        i = round(i,3)
        for j in exc_list:
            j = round(j,3)
            if i>j:
                result_list.append(cam_calculations(i,j))
                rp_exc_list.append([i,j])
    min_phi = min(result_list)
    while min_phi < 10:
        result_list.remove(min_phi)
        min_phi = min(result_list)
    min_index = result_list.index(min_phi)
    real_phi = cam_calculations(rp_exc_list[min_index][0],rp_exc_list[min_index][1])
    print "The optimal value of Rp and Excentricity for our system is :"
    print rp_exc_list[min_index]
    print "The pressure angle associated with these values is :"
    print real_phi

def data_collection(filename):
    xls = pd.ExcelFile(filename)
    xls_sheet = xls.parse(1)
    var1 = sheetX['X_Value']
    print(var1[1]) #1 is the row number...

''' Main Program '''

#cam_calculation_test(0,2,0,1)
#svaj_calculation_test()
data_collection("break_0deg_0")

            
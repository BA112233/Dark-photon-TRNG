# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 12:34:20 2022

@author: adlam
"""
import numpy as np

data = 
s_data = 0.000001
transformed_data = 

max_(transformed)_data = 1981359.2458113495
s_max_(transformed)_data = 1833219.8486603182

A1 = 2265.22216  # define values from exponential fit
A2 = 2380.501905
t1 = 163.9803523
t2 = 558.5804155
y0 = 1.50687457

s_A1 = 47.9153343
s_A2 = 64.171205
s_t1 = 6.15408236
s_t2 = 7.85687244
s_y0 = 0.92571907

s_transormed_data = ((s_A1*t1*(1-np.exp(-data/t1)))**2 + (s_A2*t2*(1-np.exp(-data/t2)))**2 +  + (A1*s_t1*(1-np.exp(-data/t1)))**2 + (A2*s_t2*(1-np.exp(-data/t2)))**2 + (data*s_y0)**2 + (A1*(np.exp(-data/t1)) + A2*(np.exp(-data/t2)) + y0*s_data)**2)**0.5

norm_data = transformed_data/max_data
s_norm_data = ((1/max_data*s_transformed)**2 + (-(transformed_data/max_data**2)*s_max_data)**2)**0.5

multiplier = 1/(1-(1/3))
s_multiplier = (255/(255-85)**2)
expanded_data = data*multiplier - (1/3)*multiplier
s_expanded_data = (((norm_data-(1/3))*s_multiplier)**2 + (multiplier*s_norm_data)**2)**0.5

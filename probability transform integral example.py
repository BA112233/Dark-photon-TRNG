# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:09:49 2022

@author: adlam
"""
import numpy as np
import matplotlib.pyplot as plt

# ================= Parameters ===================

mu = 5.0
sd = 2.0
data_cnt = 10**6
bin_cnt = 10**3

print("mean of array :", mu)
print("standard distribution of array :", sd)
# ================ Functions ===================

# Estimates gaussian distribution parameters from data using ML
def gaussian_estimation(vector):
    mu = np.mean(vector)
    sd = np.std(vector)

    return (mu,sd)

# Adjusts the data so it forms a gaussian with mean of 0 and std of 1
def gaussian_normalization(vector, char = None):

    if char is None:
        mu , sd = gaussian_estimation(vector)
    else:
        mu = char[2]
        sd = char[3]

    normalized = (vector-mu)/sd

    return normalized

def CDF(x, max_i = 100):
    sum = x
    value = x
    for i in np.arange(max_i)+1:
        value = value*x*x/(2.0*i+1)
        sum = sum + value

    return 0.5 + (sum/np.sqrt(2*np.pi))*np.exp(-1*(x*x)/2)

def gaussian_to_uniform(vector, if_normal = False):

    if (if_normal == False):
        vector = gaussian_normalization(vector)

    uni = np.apply_along_axis(CDF, 0, vector)

    return uni


# ========== Step1: Data Generation ============

data = np.random.normal(mu, sd, data_cnt)
plt.figure()
fig1 = plt.hist(data, bin_cnt)

# ========= Step2: Data Normalization ==========

data2 = gaussian_normalization(data)
plt.figure()
fig2 = plt.hist(data2, bin_cnt)

# ======== Step3: Data Uniformization ==========

data3 = gaussian_to_uniform(data2, if_normal = True)
plt.figure()
fig3 = plt.hist(data3, bin_cnt)

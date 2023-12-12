# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:53:37 2022

@author: adlam
"""
import numpy as np
import matplotlib.pyplot as plt

data = []
with open('JoeByronData.txt', 'r+') as file:
    for line in file:
        line = float(line.translate({ord(c): None for c in '\n'}))
        data.append(line)
    file.close()
random_data = data

mu = np.mean(random_data)
sd = np.std(random_data)
bin_cnt = len(random_data)
data_cnt = len(random_data) #I think its number of elements in each bin?

print("mean of array :", mu)
print("standard distribution of array :", sd)

def gaussian_estimation(vector):
    mu = np.mean(vector)
    sd = np.std(vector)

    return (mu,sd)

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

data = np.random.normal(mu, sd, data_cnt)
with open('data1', 'w') as file:
    for item in data:
        file.write(str(item) + '\n')
    file.close()
'''fig1 = plt.hist(data, bin_cnt)'''

data2 = gaussian_normalization(data)
with open('data2', 'w') as file:
    for item in data2:
        file.write(str(item) + '\n')
    file.close()
'''fig2 = plt.hist(data2, bin_cnt)'''

data3 = gaussian_to_uniform(data2, if_normal = True)
with open('data3', 'w') as file:
    for item in data3:
        file.write(str(item) + '\n')
    file.close()
fig3 = plt.hist(data3, bin_cnt)
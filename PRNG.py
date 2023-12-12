# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:46:57 2022

@author: adlam
"""

import numpy as np
import matplotlib.pyplot as plt

values1 = [1]
values2 = [213]  # define seed values
a = [3, 9]
c = [7, 15]
modulus = [20, 314]  # define function parameters
for y in range(0, 20):  # generate sequences
    values1.append((a[0] * values1[y] + c[0]) % modulus[0])
for y in range(0, 150):
    values2.append((a[1] * values2[y] + c[1]) % modulus[1])
x1 = np.arange(0, len(values1))  # set x values for the graph
x2 = np.arange(0, len(values2))
fig, ax = plt.subplots(2)  # plot the generated numbers
fig.set_figheight(10)
fig.set_figwidth(6)
fig.suptitle('Linear Congruential Generator Examples', fontsize=14,
             fontweight='bold')
ax[0].plot(x1, values1, linestyle='--', marker='x', color='tab:blue')
ax[0].set_title("seed = "+str(values1[0])+", a = "+str(a[0])+", c = "
                +str(c[0])+", m = "+str(modulus[0]))
ax[1].plot(x2, values2, linestyle='--', marker='x', color='tab:red')
ax[1].set_title("seed = "+str(values2[0])+", a = "+str(a[1])+", c = "
                +str(c[1])+", m = "+str(modulus[1]))
ax[0].set(ylabel='Value')
ax[1].set(xlabel='Number of iterations', ylabel='Value')
fig.tight_layout()
plt.savefig('LCGexample')
plt.show()
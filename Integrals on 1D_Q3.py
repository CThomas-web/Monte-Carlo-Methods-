#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:28:09 2020
#Monte_Carlo_project<thmcha014>
#Estimating Integrals Along 1 Dimension
@author: chad
"""

#------------------------------------------------------------------------------------------------
#Question 3  

#Importing packages...
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm

#Setting constants...
points = 1000
x_upperlimit = 2*np.pi
x_lowerlimit = 0


#Defining the function...
def f(x): 
    return(x*np.cos(x))

x1 = np.linspace(0,2*np.pi,1000)
y_lowerlimit = min(f(x1))
y_upperlimit = max(f(x1))

#Generating x and y values...
x = x_lowerlimit + np.random.random(points)*(x_upperlimit-x_lowerlimit)
y = y_lowerlimit + np.random.random(points)*(y_upperlimit-y_lowerlimit)
n1,n2 = 0,0


#Plotting the graph...
fig,ax = plt.subplots()
x_axis = np.linspace(0, 2*np.pi, 1000)
y_axis = x_axis*np.cos(x_axis)
plt.plot(x_axis, y_axis, label = 'Boundary Line')

for i in range(0,points): 
    if y[i] > 0 and y[i] < f(x[i]):
        plt.scatter(x[i], y[i], color = 'r', marker = 'o')
        n1 = n1 + 1
        
    elif y[i] < 0 and y[i] > f(x[i]):
        plt.scatter(x[i], y[i], color = 'r', marker = 'o')
        n2 = n2 + 1
        
    else: 
        plt.scatter(x[i], y[i], color = 'b', marker = 's')

pos_area = (n1/points)*(2*np.pi*(y_upperlimit-y_lowerlimit))
neg_area = (n2/points)*(2*np.pi*(y_upperlimit-y_lowerlimit))
solution = pos_area - neg_area
print('The analytic solution for this integral is: ', solution)       
plt.show
plt.legend()

#-------------------------------------------------------------------------------------------------------------
runs = 100
array1 = np.zeros(runs)


for i in range (0,runs): 
    x = x_lowerlimit + np.random.random(points)*(x_upperlimit-x_lowerlimit)
    y = y_lowerlimit + np.random.random(points)*(y_upperlimit-y_lowerlimit)
    n1,n2 = 0,0
    
    for j in range(0,points): 
        if y[j] > 0 and y[j] < f(x[j]):
            n1 = n1 + 1
        
        elif y[j] < 0 and y[j] > f(x[j]):
            n2 = n2 + 1
    pos_area = (n1/points)*(2*np.pi*(y_upperlimit-y_lowerlimit))
    neg_area = (n2/points)*(2*np.pi*(y_upperlimit-y_lowerlimit))  
    solution = pos_area - neg_area
    array1[i] = solution 

print(array1)

Mean = np.mean(array1, dtype = np.float64)
Standard_dev = np.std(array1, ddof = 1)

fig,ax =  plt.subplots()
#plt.rcParams["figure.figsize"]=8,4
binnum = 20


n, bins, patches = ax.hist(array1, binnum, density = 1, color= 'y')
gauss = norm.pdf(bins, Mean, Standard_dev)
ax.plot(bins,gauss,'--')


ax.set_xlim([(min(array1)-0.01), max(array1)+0.01])

plt.show()
print(Mean)
err= Mean/np.sqrt(runs)
print(err)











































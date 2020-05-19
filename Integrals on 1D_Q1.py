#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 18:11:32 2020
Module: AST40007W-Computaional Methods 
#Monte_Carlo_project<thmcha014>
#Estimating Integrals Along 1 Dimension
@author: Chad Thomas <thmcha014>
"""

#Importing packages...
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm

#------------------------------------------------------------------------------
#Question 1
#------------------------------------------------------------------------------

#Setting constants
points = 1000
x_upperlimit = 2
x_lowerlimit = 1


#Defining the function
def f(x): 
    return(x**3*np.log(x))
y_lowerlimit = f(x_lowerlimit)
y_upperlimit = f(x_upperlimit)

#Generating x and y values
x = x_lowerlimit + np.random.random(points)*(x_upperlimit-x_lowerlimit)
y = y_lowerlimit + np.random.random(points)*(y_upperlimit-y_lowerlimit)
n = 0

#Plotting the graph
fig,ax = plt.subplots()
x_axis = np.linspace(1, 2, 100)
y_axis= x_axis**3*np.log(x_axis)
plt.plot(x_axis, y_axis, label = 'Boundary Line')

for i in range(0,points): 
    if y[i] > f(x[i]):
        plt.scatter(x[i], y[i], color = 'b', marker = 's')
    else: 
        n = n + 1 
        plt.scatter(x[i], y[i], color = 'r', marker = 'o')


solution = (n/points)*(1*y_upperlimit)
print('The analytic solution for this integral is: ', solution)       
plt.show
plt.legend()
#--------------------------------------------------------------------------------------------------

runs = 500
array1 = np.zeros(runs)


for i in range (0,runs): 
    x = x_lowerlimit + np.random.random(points)*(x_upperlimit-x_lowerlimit)
    y = y_lowerlimit + np.random.random(points)*(y_upperlimit-y_lowerlimit)
    n = 0
    
    for j in range(0,points):
        if y[j] < f(x[j]):
            
            n = n + 1 
        
    solution = (n/points)*(1*y_upperlimit)
    array1[i] = solution 

Mean = np.mean(array1, dtype = np.float64)
Standard_dev = np.std(array1, ddof = 1)
error = (Standard_dev/np.sqrt(runs))

fig,ax =  plt.subplots()
#plt.rcParams["figure.figsize"]=8,4
binnum = 15


n, bins, patches = ax.hist(array1, binnum, density = 1, color= 'g')
gauss = norm.pdf(bins, Mean, Standard_dev)
ax.plot(bins,gauss,'--')


ax.set_xlim([(min(array1)-0.01), max(array1)+0.01])

plt.show()
print(Mean)
print(error)













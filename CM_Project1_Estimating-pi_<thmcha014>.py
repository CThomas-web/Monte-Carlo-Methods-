#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:39:59 2020
Module: AST40007W-Computaional Methods 
#Monte_Carlo_Project<thmcha014>
#Part 1: Estimating the value of pi using the Monte Carlo method.
@author: Chad Thomas <thmcha014>
"""

#Importing packages...
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm
#------------------------------------------------------------------------------
#Part 1: 
#------------------------------------------------------------------------------

#Generating 1000 random points and initial values
points = 1000
x = np.random.random(points)        #Generating 1000 x-values
y = np.random.random(points)        #Gemerating 1000 y-values
r = np.sqrt(x**2 + y**2)            #Calcuating distance between each point using pythagorean theorem 
n = 0                               #Initializing start for counter, counting number of points where r <= 1 

#Starting 'for loop' for random points
for i in range (0,points):
    if r[i] <= 1:
        plt.plot(x[i], y[i], 'ro')
        
        n = n + 1
        
    else:
        plt.plot(x[i], y[i], 'bs')

#plotting boundary line between values for r < 1 & r > 1
x_limit = np.linspace(0, 1, 750)
y_limit = np.sqrt(1 - (x_limit)**2)
plt.plot(x_limit, y_limit, label = 'Boundary Line')

#Calculating the value of pi 
Ao = n/points                       #finding the area of one qaud
pi = 4*Ao                           #We multiply by 4 to get a full circle

print('The value of pi is: ', pi)
print('The numbeer of red dots in Qaud 1 is: ', n)

#------------------------------------------------------------------------------
#Part 2: Calculating the Uncertainty of Your Approximation of pi(π)
#------------------------------------------------------------------------------


runs = 100
array1 = np.zeros(runs)


for i in range (0,runs): 
    x = np.random.random(points)        
    y = np.random.random(points)
    r = np.sqrt(x**2 + y**2)
    n = 0
    
    for j in range(0,points):
        if r[j] <= 1:
            n = n + 1
    pi = 4*(n/points)
    array1[i] = pi 

Mean = np.mean(array1, dtype = np.float64)
Standard_dev = np.std(array1, ddof = 1)

fig,ax =  plt.subplots()
binnum = 20

#Plotting the gaussian fit
n, bins, patches = ax.hist(array1, binnum, density = 1, color= 'orange')
gauss = norm.pdf(bins, Mean, Standard_dev)
ax.plot(bins,gauss,'--')


ax.set_xlim([(min(array1)-0.01), max(array1)+0.01])

plt.show()
print('Mean: {:.4f}'.format(Mean))

#Qouting measured pi and its uncertainty
error = (Standard_dev/np.sqrt(runs))
print('error: {:.4f}'.format(error))
print('standard dev: {:.4f}'.format(Standard_dev))

#------------------------------------------------------------------------------
#Part 3: Comparing different results using data sets of different sizes
#------------------------------------------------------------------------------

list_uncer=[]
list_pi=[]

for M in range (100,1100,100):
    array1 = np.zeros(M)


    for i in range (0,M): 
        x = np.random.random(points)        
        y = np.random.random(points)
        r = np.sqrt(x**2 + y**2)
        n = 0
    
        for j in range(0,points):
            if r[j] <= 1:
                n = n + 1
                pi = 4*(n/points)
                array1[i] = pi 

    Mean = np.mean(array1, dtype = np.float64)
    list_pi.append(Mean)
    Standard_dev = np.std(array1, ddof = 1)
    uncertainty = Standard_dev/np.sqrt(M)
    list_uncer.append(uncertainty)
    print('pi(π) = {:.4f}'.format(Mean), '± {:.4f}'.format(uncertainty), 'for', M , 'runs')
  
    
#plotting error graph 
M=np.array([100,200,300,400,500,600,700,800,900,1000])  
uncertainty =np.array(list_uncer)
Mean_pi=np.array(list_pi)

plt.xlabel('Number of Runs (M)')
plt.ylabel('Uncertainty')
plt.plot(M,uncertainty, 'o')
plt.show()


plt.errorbar(M,Mean_pi, uncertainty, linestyle = 'None')
plt.plot(M, Mean_pi,'o')

x = np.linspace(100,1000, 2000)
y = (np.pi)*np.ones(2000)

plt.xlabel('Number of Runs (M)')
plt.ylabel('Estimated value of pi with error bars')
plt.plot(x,y,'k-', label='actual value of pi')
plt.legend()




#-------------------------------------------------------------------------------------------------------------------------------



























# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:56:22 2021

@author: AVERKHO
"""

import numpy as np
from sklearn_extra.cluster import KMedoids
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
plt.close('all')

X=np.array([[0,4,0,-5],[-6,4,0,2]])



def l2_calc(x1,x2):
    '''
    

    Parameters
    ----------
    x1 : point ([x1,x2])
        DESCRIPTION.
    x2 : point ([x1,x2])
        DESCRIPTION.

    Returns
    -------
    l1 distance between two points

    '''
    
    return np.sqrt((x1[0]-x2[0])**2+(x1[1]-x2[1])**2)

def l1_calc(x1,x2):
    '''
    

    Parameters
    ----------
    x1 : point ([x1,x2])
        DESCRIPTION.
    x2 : point ([x1,x2])
        DESCRIPTION.

    Returns
    -------
    l1 distance between two points

    '''
    
    return np.abs(x1[0]-x2[0])+np.abs(x1[1]-x2[1])

z1=(-5,2)
z2=(0,-6)
Z=np.array([[0,0],
            [0,-6]])
y=[1,0,0,0]


cost=0        
for j in range(X.shape[1]):
    cost+=l2_calc(X[:,j],Z[:,y[j]])

print(cost)




clustering=KMeans(n_clusters=2)

clustering.fit(np.transpose(X))

y=clustering.predict(np.transpose(X))

fig=plt.figure(1)
ax=fig.add_subplot(111)
ax.scatter(X[0],X[1],c=y)
ax.grid(True)



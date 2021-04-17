# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 17:43:44 2021

@author: Konstantinos
"""

import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d



A=sio.loadmat('Simulation_Data.mat')
k=8
PointCloud=A['Cloud']
Intensity=A['Intensity']
Intensity=np.int16(Intensity)
thres=1

color=np.zeros([PointCloud.shape[1],PointCloud.shape[0]])
maximal=max(Intensity)
data=Intensity
for i in range(PointCloud.shape[1]):
    color[i,0]=data[i,0]/maximal[0]
    


'''
Before Processing
'''
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(PointCloud[0,:],PointCloud[2,:],PointCloud[1,:],c=color)
plt.show()

C=np.ndarray.sum(np.multiply(PointCloud,PointCloud),axis=0)
Elements=np.size(C)
sup=np.zeros(Elements)
for i in range(Elements):
    column=np.expand_dims(PointCloud[:,i],axis=1)
    distance=C[i]-2*(np.dot(np.transpose(column),PointCloud))+C
    c=np.where(distance<thres)
    if(np.size(c[1])<k):
        sup[i]=i
indexes=np.where(sup!=0)
inde=np.expand_dims(indexes[0],axis=0)
Cloud=np.delete(PointCloud,inde,axis=1)
Intens=np.delete(Intensity,inde,axis=0)
def Filter(PointCloud,Intensity,thres,k):
    D=np.ndarray.sum(np.multiply(PointCloud,PointCloud),axis=0)
    Elements=np.size(D)
    sup=np.zeros(Elements)
    for i in range(Elements):
        column=np.expand_dims(PointCloud[:,i],axis=1)
        distance=D[i]-2*(np.dot(np.transpose(column),PointCloud))+D
        c=np.where(distance<thres)
        if(np.size(c[1])<k):
            sup[i]=i
    indexes=np.where(sup!=0)
    inde=np.expand_dims(indexes[0],axis=0)
    Cloud=np.delete(PointCloud,inde,axis=1)
    Inte=np.delete(Intensity,inde,axis=0)
    return Cloud,Inte

Au=Filter(PointCloud, Intensity,thres,k)
Audi=Au[0]
MN=Au[0].shape
color=np.zeros([MN[1],MN[0]])
maximal=max(Au[1])
data=Au[1]
for i in range(MN[1]):
    color[i,0]=data[i,0]/maximal[0]
    
'''
Post Processing
'''
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(Audi[0,:],Audi[2,:],Audi[1,:],c=color)
plt.show()
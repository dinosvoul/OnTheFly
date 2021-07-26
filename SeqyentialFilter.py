# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 14:39:31 2021

@author: Konstantinos
"""
import mpl_toolkits.mplot3d.axes3d as p3
from PIL import Image
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

filesOne=[]
filesTwo=[]
for files in range(1,10):
    A=sio.loadmat('SumalateCloud_' + str(files)+ '.mat')

    PointCloud=A['Cloud']
    Intensity=A['Intensity']
    Intensity=np.int16(Intensity)

    k=8
    thres=1
    
    color=np.zeros([PointCloud.shape[1],PointCloud.shape[0]])
    maximal=max(Intensity)
    data=Intensity
    for i in range(PointCloud.shape[1]):
        color[i,0]=data[i,0]/maximal[0]
    

      
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(PointCloud[0,:],PointCloud[2,:],PointCloud[1,:],c=color)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(0,5)
    ax.set_ylim(0,30)
    ax.set_zlim(0,8)
    plt.show()
    filename='3d_cloud_'+str(files)+'.png'
    plt.savefig(filename, dpi=75)
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
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(0,5)
    ax.set_ylim(0,30)
    ax.set_zlim(0,8)
    ax.scatter3D(Audi[0,:],Audi[2,:],Audi[1,:],c=color)
    plt.show()
    filename='3d_filter_'+str(files)+'.png'
    plt.savefig(filename, dpi=75)
    
'''  
data=d
fig = plt.figure()
ax = p3.Axes3D(fig)
ax = p3.Axes3D(fig)
scatters=[ ax.scatter(data[0][i,0:1], data[0][i,1:2], data[0][i,2:]) for i in range(data[0].shape[0]) ]
scatters= [ax.scatter(dat[0, :], dat[2, :], dat[1, :]) for dat in data]


def update_plot(i):
    ax.scatter(data[i][0, :], data[i][2, :], data[i][1, :]) 
   
    
anim=FuncAnimation(fig,update_plot, 
                    
                    interval=1)
'''


for i in range(1,10):
    seq = str(i*2)
    file_names = '3d_cloud_'+str(i)+'.png'
    file_names_Two='3d_filter_'+str(i)+'.png'
    filesOne.append(file_names)
    filesTwo.append(file_names_Two)
    
frames = []
framesFilter=[]
for i in filesOne:
    new_frame = Image.open(i)
    frames.append(new_frame)
    
    
frames[0].save('Original_cloud.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=400, loop=0) 

for i in filesTwo:
    new_frame = Image.open(i)
    framesFilter.append(new_frame)
    
framesFilter[0].save('Filter_cloud.gif', format='GIF',
               append_images=framesFilter[1:],
               save_all=True,
               duration=400, loop=0) 
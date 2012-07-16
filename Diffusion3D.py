#!/usr/bin/python
#
# Author: Daniel Loman
# Date: July 12, 2012
# Filename: Diffusion3D.py
# Description:
#   This program creates 3d matrix then simulates diffusion through the matrix  
# and then it visualizes this diffusion using matplotlib
#


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sys import argv
from os import system, remove

################################################################################
################################################################################
def Usage():
  print 'Diffuse.py [n t Initialize BoundryCondition](optional settings)' 

################################################################################
def Plot(Grid, ax):
  n=len(Grid)
  for i in range(n):  
    x=np.ones(n)*i
    for j in range(n):
      y =np.ones(n)*j
      z =range(n)
      
      c = Grid[i,j,:]
      color = ax.scatter(x, y, z, c=c, marker='o')
  return color

################################################################################
def GetNeighborhoodDifference(Grid,x,y,z,BoundryCondition):
  n=len(Grid)
  BigGrid=np.ones(shape=(n+2,n+2,n+2))*BoundryCondition
  BigGrid[1:n+1,1:n+1,1:n+1]=Grid 
  Diff=0
  for i in range(3): 
    for j in range(3):
      for k in range(3):
         Temp=(Grid[x,y,z]-BigGrid[x+i,y+j,z+k])
         if Temp != 0:
           Diff+= Temp/10
  return Diff
    
################################################################################
def GetNextGrid(Grid,BoundryCondition):
  n=len(Grid)
  NextGrid=np.zeros(shape=(n,n,n))
  for i in range(n):
    for j in range(n):
      for k in range(n):
        NextGrid[i,j,k]=Grid[i,j,k]-GetNeighborhoodDifference(Grid,i,j,k,BoundryCondition)  
  return NextGrid

    
###############################################
################################################################################
def Diffuse(n,t,Initialize=0,BoundryCondition=0):
  if Initialize == 0:
    Grid = np.floor(np.random.rand(n,n,n)*10)
  else:
    print 'add different initializations besides initilize =0'
    return
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  color = Plot(Grid,ax)
  plt.colorbar(color)
  for i in range(t):
    ax.cla()
    Grid=GetNextGrid(Grid,BoundryCondition)
    color = Plot(Grid,ax)
    fname = '_tmp%03d.png'%i
  #  print 'Saving frame', fname
    fig.savefig(fname)
  
  print 'Making movie animation.mpg - this make take a while'
  system("ffmpeg -y -qscale 1 -f image2 -i _tmp%03d.png Animation.mpg")
  system("rm _tmp* ")

################################################################################
################################################################################
if __name__ == '__main__':
  if len(argv)<2:
    Diffuse(10,100)
  elif len(argv) == 2:
    Diffuse(argv[1],100)
  elif len(argv) == 3:
    Diffuse(argv[1],argv[2])
  elif len(argv) == 4:
    Diffuse(argv[1],argv[2],argv[3])
  elif len(argv) == 5:
    Diffuse(argv[1],argv[2],argv[3],argv[4])
  else:
    Usage()



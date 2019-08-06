import numpy as np 
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
 
from meshgen import *
from poltall import *

p,t = meshgen()


def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

# This function to evaluate the Mass Matrix
def massmat(p,t):
    
    np1 = p.shape[1]    # number of nodes
    nt = t.shape[1]     # number of elements 
    
    M = np.zeros((np1,np1)) # allocate the Mass Matrix 
    
    for k in range(nt):
        loc2glob = t[0:3,k]-1
        x = p[0,loc2glob]
        y = p[1,loc2glob]
        area = PolyArea(x,y)
        MK = np.array(([2,1,1],[1,2,1],[1,1,2]))/12*area
        #assmble the local matrix to the global 
        M[np.ix_(loc2glob,loc2glob)] += MK   
         
    return M 


# The given function
def func(x,y):
    return np.sin(np.sqrt(x**2 + y**2))


# This laod vector function evaluation.
def LoadVec2D(p,t):

    np1 = p.shape[1]
    nt = t.shape[1]

    b = np.zeros((np1,1))

    for k in range(nt):
        loc2glob = t[0:3,k]-1
        x = p[0,loc2glob]
        y = p[1,loc2glob]     
        area = PolyArea(x,y)        
        bk =np.array(([func(x[0],y[0])],
                      [func(x[1],y[1])],
                      [func(x[2],y[2])])) /3*area
        b[loc2glob] += bk

    return b
 

M = massmat(p,t)
b = LoadVec2D(p,t)

pf =  M@b


print('The Mass Matrix(M) = \n',M)
print('\nThe load vector (b)= \n',b)
print('\nThe L2 Projection (pf) of the given function f(x) is: \n',pf)
print('\n=======================================\n')
print('The total number of nodes = ',p.shape[1])
print('The total number of elements = ', t.shape[1])
print('\n=======================================\n')

delunay_tri(M)
poltall(x = p[0,:],y = p[1,:], z = pf)
import numpy as np 

#p = np.array(([0,1,2,2,0],[0,0,0,1,1]))
#t =np.array(([1,1,2],[4,2,3],[5,4,4]))


p = np.array([
        [-1,-0.5,0,0.5,1,-1,-0.5,0,0.5,1,-1,-0.5,0,0.5,1,-1,-0.5,0,0.5,1,-1,-0.5,0,0.5,1],
        [-1,-1,-1,-1,-1,-0.5,-0.5,-0.5,-0.5,-0.5,0,0,0,0,0,0.5,0.5,0.5,0.5,0.5,1,1,1,1,1]
        ])
t = np.array([
        [1,2,2,2,3,4,4,
         6,6,12,12,13,14,14,14,
         11,17,17,13,13,19,19,15,
         16,16,17,18,18,18,19,20
         ],
        
        [2,7,8,3,4,9,9,
         11,12,7,7,8,8,9,15,
         12,12,12,12,14,14,14,14,
         21,17,18,22,23,19,20,24
         ],
        
        [6,6,7,8,8,8,10,
         12,7,8,13,14,9,10,10,
         16,16,18,18,18,18,20,20,
         22,22,22,23,24,24,24,25
         ]
        ])
#print(p)
#print(t)
#print(range(t.shape[1]))
#for k in range(t.shape[1]):
#        print(k)


def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

def massmat(p,t):
    np1 = p.shape[1]
    nt = t.shape[1]
    M = np.zeros((np1,np1))
    for k in range(nt):
        loc2glob = t[0:3,k]-1
        x = p[0,loc2glob]
        y = p[1,loc2glob]
      
        area = PolyArea(x,y)
        MK = np.array(([2,1,1],[1,2,1],[1,1,2]))/12*area
    
        M[np.ix_(loc2glob,loc2glob)] += MK
    return M 

def func(x,y):
    return np.cos(x**2+y**2)

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
print(M)
print(b)

pf =  M@b

print(pf)


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.gca(projection='3d')
# Plot the surface.
surf = ax.plot_surface(p[0,:], p[1,:], pf, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.

ax.set_zlim(-0.11, 0.23)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))


fig.colorbar(surf, shrink=0.7, aspect=15)

plt.show()

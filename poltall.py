# This script to plot all the required graphs.
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from scipy.spatial import Delaunay
 

def delunay_tri(M):
 
    points = np.array([[0,0],[1,0],[-1,0],[0,1],
                   [0,-1],[-1, -1], [1, -1], 
                   [1, 1], [-1, 1],[-0.5,1],
                   [0.5,1],[-1,0.5],[0,0.5],
                   [1,0.5],[-0.5,0],[0.5,0],
                   [-1,-0.5],[0,-0.5],[1,-0.5],
                   [-0.5,-1],[0.5,-1],[0.5,0.5],
                   [-0.5,-0.5],[0.5,-0.5],[-0.5,0.5] ])

    print('The nodes are: \n',points)
    tri = Delaunay(points)
    plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
    plt.plot(points[:,0], points[:,1], 'o')
    plt.title('Delanauy Trianglaution of $\Omega = [-1,1] ^2$')
    plt.show()

    # to plot the mass matrix 
    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.suptitle('The Mass Matrix')
    ax1.matshow(M)
    ax2.spy(M)
    plt.show()

def poltall(x,y,zt):


    U = np.zeros(len(zt))

    for i in range(len(zt)):
        U[i] = zt[i][0]

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    z =U
    surf = ax.plot_trisurf(x, y, z, cmap=cm.Spectral,linewidth=0, antialiased=False)
    # Customize the z axis.
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('  %.03f'))
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.7, aspect=9)
    plt.title('$L^2$ projection of f(x)')
    plt.show() 
#    
#    fig = plt.figure()
#    ax = fig.gca(projection='3d')
#    #f = func(p[0,:], p[1,:])
#    # Plot the surface.
#    surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
#                      linewidth=0, antialiased=False)
#    # Customize the z axis.
#    ax.set_zlim(-0.11, 0.23)
#    ax.zaxis.set_major_locator(LinearLocator(10))
#    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#   
#    fig.colorbar(surf, shrink=0.7, aspect=15)
#    plt.show()

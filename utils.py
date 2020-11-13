import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d 
from matplotlib.colors import LogNorm

def plot_coutour(func, box=(-10,10), scale='linear', **kwargs):
    X = np.linspace(box[0],box[1],300)
    Y = np.linspace(box[0],box[1],300)
    X, Y = np.meshgrid(X,Y)
    Z = func(X, Y)

    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(1,1,1)
    if scale is 'linear':
        CS = ax.contour(X, Y, Z, **kwargs, 
                    levels=np.floor(np.linspace(Z.min(), Z.max(), 20)), 
                    cmap='RdYlBu_r')
    else:
        CS = ax.contour(X, Y, Z, **kwargs,
                levels=np.geomspace(Z.min(), Z.max(), 20), 
                cmap='RdYlBu_r', norm = LogNorm())
    # the contour plot is when f(x,y) = the values above
    ax.clabel(CS, inline=True, fontsize=10,)
    plt.show()
    return fig, ax

def plot_surface_2d(func,box=(-10,10),azim=-60,elev=30, scale='linear',
                    dist=10, cmap="RdYlBu_r",**kwargs):
    X = np.linspace(box[0],box[1],300)
    Y = np.linspace(box[0],box[1],300)
    X, Y = np.meshgrid(X,Y)
    Z = func(X, Y)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    plot_args = {'rstride': 1, 
                 'cstride': 1, 
                 'cmap':cmap,
                 'linewidth': 20, 
                 'antialiased': True,
                 'vmin': np.floor(Z.min()), 'vmax': np.ceil(Z.max())}
    ax.plot_surface(X, Y, Z, **plot_args, **kwargs)
    if scale is 'linear':
        _ = ax.contour(X, Y, Z, **kwargs, 
                    levels=np.floor(np.linspace(Z.min(), Z.max(), 20)), 
                    cmap='jet')
    else:
        _ = ax.contour(X, Y, Z, **kwargs,
                levels=np.geomspace(Z.min(), Z.max(), 20), 
                cmap='jet', norm = LogNorm())
    ax.view_init(azim=azim, elev=elev)
    ax.dist=dist
    ax.set_xlim(box[0], box[1])
    ax.set_ylim(box[0], box[1])
    ax.set_zlim(np.floor(Z.min()), np.ceil(Z.max()))
    # plt.xticks([-1, -0.5, 0, 0.5, 1],
    #            [r"$-1$", r"$-1/2$", r"$0$", r"$1/2$", r"$1$"])
    # plt.yticks([-1, -0.5, 0, 0.5, 1],
    #            [r"$-1$", r"$-1/2$", r"$0$", r"$1/2$", r"$1$"])
    # ax.set_zticks([-2, -1, 0, 1, 2])
    # ax.set_zticklabels([r"$-2$", r"$-1$", r"$0$", r"$1$", r"$2$"])
    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0)) 
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0)) 
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.set_xlabel(r"$x$", fontsize=18)
    ax.set_ylabel(r"$y$", fontsize=18)
    ax.set_zlabel(r"z", fontsize=18)
    return fig, ax

def plot_gradient_descent(func, x_vals, y_vals, box=(-10,10), step=20, 
                    scale='linear',cmap='RdYlBu_r',**kwargs):
    X = np.linspace(box[0],box[1],300)
    Y = np.linspace(box[0],box[1],300)
    X, Y = np.meshgrid(X,Y)
    Z = func(X, Y)

    # these 4 lines of code is plotting the contour
    _, ax = plt.subplots(figsize=(10, 8))
    if scale is 'linear':
        CS = ax.contour(X, Y, Z, **kwargs, 
                levels=np.floor(np.linspace(Z.min(), Z.max(), 20)), 
                    cmap=cmap)
    else:
        CS = ax.contour(X, Y, Z, **kwargs,
                levels=np.geomspace(Z.min(), Z.max(), 20), 
                cmap=cmap, norm = LogNorm())

    ax.clabel(CS, inline=True, fontsize=8)
    
    num_steps = len(x_vals)
    delta_n = num_steps//step
    for i in range(0,num_steps-delta_n,delta_n):
        plt.arrow(x_vals[i], y_vals[i], (x_vals[i+delta_n] - x_vals[i]), 
              (y_vals[i+delta_n] - y_vals[i]), 
              head_width=0.3, head_length=0.2, linewidth = 1.5, color='black')

    plt.show()
    return ax
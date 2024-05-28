from Neighbors import *
from Real_Space import *
from Lattice import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.interpolate import griddata

def Simulation(Lx, Ly, fps, frn, initial_position1, initial_position2, dt, alpha, interpolation_factor, scale_fac):
    psi_0=np.zeros((Lx*Ly,1))
    psi_0[initial_position1]=1/np.sqrt(2)
    psi_0[initial_position2]=1/np.sqrt(2)
    time_evo=np.identity(Lx*Ly)-1.j*dt*H(alpha,Lx,Ly)
    a = np.zeros((Lx*Ly,frn))
    for i in range(1,frn):
        psi_0=np.matmul(time_evo, psi_0)
        a[:,[i]]=psi_0
    lattice, arr, xy = Lattice(Lx,Ly)
    X = xy[:,0][0:Lx]
    Y = xy[:,0][0:Lx]
    xv, yv = np.meshgrid(X, Y)
    def update_plot(frame_number, a, plot):
        # Interpolation
        xi = np.linspace(X.min(), X.max(), Lx*interpolation_factor)
        yi = np.linspace(Y.min(), Y.max(), Ly*interpolation_factor)
        xi, yi = np.meshgrid(xi, yi)
        zi = griddata((xv.ravel(), yv.ravel()), np.reshape((np.abs(a[:,[frame_number]])*scale_fac)**2, (Lx,Ly)).ravel(), (xi, yi), method='cubic')
        # End
        plot[0].remove()
        plot[0] = ax.plot_surface(xv, yv, np.reshape((np.abs(a[:,[frame_number]]))**2, (Lx,Ly)), cmap="magma")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(90,0)
    plot = [ax.plot_surface(xv, yv, np.reshape((np.abs(a[:,[0]]))**2, (Lx,Ly)), color='0.75', rstride=1, cstride=1)]
    ax.set_zlim(0,1.1)
    an = animation.FuncAnimation(fig, update_plot, frn, fargs=(a, plot), interval=1000/fps)
    plt.xlabel(r'$x$', fontsize=10)
    plt.ylabel(r'$y$', fontsize=10)
    ax.set_zlabel(r'$|\Psi|^2$', fontsize=10)
    return an
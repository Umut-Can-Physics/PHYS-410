import numpy as np

def Lattice(Lx,Ly):
    lattice = np.arange(Lx*Ly).reshape(Lx,Ly)
    x_co = np.arange(Ly)
    y_co = np.arange(Lx)
    arr = []
    for j in range(len(y_co)):
        for i in range(len(x_co)):
            arr = np.append(arr, [[x_co[i],x_co[j]]])
    xy = arr.reshape((int(arr.size/2),2))
    return lattice, arr, xy
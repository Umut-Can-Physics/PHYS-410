import numpy as np
from Neighbors import *

def H(alpha,Lx,Ly):
    lattice, arr, xy = Lattice(Lx,Ly)
    HardBCLat = HardBc(Lx, Ly)
    H = np.zeros((Lx*Ly, Lx*Ly), dtype=complex)
    for m in range(Lx*Ly):
        for n in range(Lx*Ly):
            if m in HardBCLat[n]:
                if xy[m][0] > xy[n][0]:
                    H[m][n] = -np.exp(1j*2*np.pi*alpha*xy[m][1])
                elif xy[m][0] < xy[n][0]:
                    H[m][n] = -np.exp(-1j*2*np.pi*alpha*xy[m][1])
                else:
                    H[m][n]=-1
    return H
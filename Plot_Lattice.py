from Lattice import Lattice
from matplotlib import pyplot as plt

Lx = Ly = 40

lattice, arr, xy = Lattice(Lx,Ly)

plt.scatter(xy[:,0],xy[:,1])
for i in range(Lx*Ly): 
    plt.annotate(i, (xy[:,0][i]+0.05,xy[:,1][i])) 
plt.show()
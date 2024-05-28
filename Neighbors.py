import numpy as np
from Lattice import *

def HardBc(Lx, Ly):
    lattice, arr, xy = Lattice(Lx,Ly)
    neighbors = {}
    for i in range(len(lattice)):
        for j, value in enumerate(lattice[i]):
            if i == 0 or i == len(lattice) - 1 or j == 0 or j == len(lattice[i]) - 1:
                new_neighbors = []
                if i != 0:
                    new_neighbors.append(lattice[i - 1][j])  
                if j != Ly - 1:
                    new_neighbors.append(lattice[i][j + 1]) 
                if i != Lx - 1:
                    new_neighbors.append(lattice[i + 1][j])  
                if j != 0:
                    new_neighbors.append(lattice[i][j - 1])
            else:
                new_neighbors = [
                    lattice[i - 1][j],  
                    lattice[i][j + 1],  
                    lattice[i + 1][j],  
                    lattice[i][j - 1]   
                ]
            neighbors[value] = new_neighbors
    return neighbors

def PerBc(Lx, Ly):
    lattice, arr, xy = Lattice(Lx,Ly)
    neighbors = {}
    for i in range(len(lattice)):
        for j, value in enumerate(lattice[i]):
            new_neighbors = [
                lattice[(i - 1)%Lx][j%Ly],  
                lattice[i%Lx][(j + 1)%Ly],  
                lattice[(i + 1)%Lx][j%Ly],  
                lattice[i%Lx][(j - 1)%Ly]   
            ]
            neighbors[value] = new_neighbors
    return neighbors
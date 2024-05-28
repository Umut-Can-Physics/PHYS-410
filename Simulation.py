from Edge_States import *

Lx = Ly = 40
fps = 5000 
frn = 1500 
interpolation_factor = 10
scale_fac = 7

# Diffraction Pattern
initial_position1=820
initial_position2=819
alpha = 0
# Cyclotron Motion
initial_position1=820
initial_position2=819
alpha = 1/10
# Edge State
initial_position1=20
initial_position2=19
alpha = 1/10

dt=0.01
sim = Simulation(Lx, Ly, fps, frn, initial_position1, initial_position2, dt, alpha, interpolation_factor, scale_fac)
plt.show()
#sim.save('Simulation.gif', writer='imagemagick', fps=200)
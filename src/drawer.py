from simulation import ElectricCharge, Simulation, SphereCoordinates

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

def draw_simulation(total_time=100000):
    init_coords=SphereCoordinates(1, 0, np.pi / 2)
    init_speeds=SphereCoordinates(1, 1 / 25, 0)
    mass = 1
    q = 1*10**-5
    
    charge = ElectricCharge(init_coords, init_speeds, mass, q)
    simulation = Simulation(charge, total_time)
    points = simulation.run_experiment()
    
    ax = plt.axes(projection='3d')
    x, y, z = points[:, 0], points[:, 1], points[:, 2] 
    ax.plot3D(x, y, z, '--', color='black')
    ax.scatter3D(x[0], y[0], z[0], '*', color='orange', alpha=0.5)
    ax.scatter3D(0, 0, 0, 'A', color='green', alpha=0.9)
    
    plt.show()

if __name__ == "__main__":
    draw_simulation()
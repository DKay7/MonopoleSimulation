from simulation import ElectricCharge, Simulation, SphereCoordinates

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import plotly.graph_objects as go

def local_simulation(total_time=100000):
    init_coords=SphereCoordinates(1, 0, np.pi / 2)
    init_speeds=SphereCoordinates(1, 1 / 25, 0)
    mass = 1
    q = 1*10**-5
    
    charge = ElectricCharge(init_coords, init_speeds, mass, q)
    simulation = Simulation(charge, total_time)
    points = simulation.run_experiment()
    
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax = plt.axes(projection='3d')
    x, y, z = points[:, 0], points[:, 1], points[:, 2]
    ax.plot3D(x, y, z, '--', color='black')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.scatter3D(x[0], y[0], z[0], '*', color='orange', alpha=0.5)
    ax.scatter3D(0, 0, 0, 'A', color='green', alpha=0.9)
    
    plt.show()

def start_simulation(charge, total_time=100000):
    simulation = Simulation(charge, total_time)
    points = simulation.run_experiment()
    
    x, y, z = points[:, 0], points[:, 1], points[:, 2]
    trace = go.Scatter3d(x=x, y=y, z=z, marker={'size': 0.5, 'color': z, 'opacity': 0.8, 'colorscale': 'Viridis'})
    fig = go.Figure(trace, layout=go.Layout())
    
    return fig

if __name__ == "__main__":
    local_simulation()
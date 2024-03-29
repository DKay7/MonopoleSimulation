from simulation import ElectricCharge, Simulation, SphereCoordinates

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import plotly.graph_objects as go

def local_simulation(total_time=500):
    init_coords=SphereCoordinates(100, 0, np.pi / 2)
    init_speeds=SphereCoordinates(1, 1 / 100, 0)
    mass = 20
    q = 1*10**-5
    
    charge = ElectricCharge(init_coords, init_speeds, mass, q)
    simulation = Simulation(charge, total_time)
    points = simulation.run_experiment()
    
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax = plt.axes(projection='3d')
    x, y, z = points[:, 0], points[:, 1], points[:, 2]
    ax.plot3D(x, y, z, '-', label="Траектория", color='black')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.scatter3D(x[0], y[0], z[0], '*', label="начальная позиция заряда", color='orange', alpha=0.5)
    ax.scatter3D(0, 0, 0, 'A', label="монополь", color='green', alpha=0.9)
    ax.legend(loc='upper left')
    plt.show()

def start_simulation(charge, total_time=500):
    simulation = Simulation(charge, total_time)
    points = simulation.run_experiment()
    # print(points[0, 0], points[0, 1], points[0, 2])

    x, y, z = points[:, 0], points[:, 1], points[:, 2]
    monopole = go.Scatter3d(x=[0], y=[0], z=[0], name="Позиция монополя", marker={'size': 2, 'color': 'orange'})
    start_position = go.Scatter3d(x=[x[0]], y=[y[0]], z=[z[0]], name="Начальная позиция заряда",  marker={'size': 2, 'color': 'green'})
    trace = go.Scatter3d(x=x, y=y, z=z, name="Траектория", marker={'size': 0.5, 'color': np.sqrt(x**2 + y**2 + z**2), 'opacity': 0.8, 'colorscale': 'Viridis'})
    
    fig = go.Figure(trace, layout=go.Layout())
    fig.add_trace(monopole)
    fig.add_trace(start_position)

    return fig

if __name__ == "__main__":
    local_simulation()
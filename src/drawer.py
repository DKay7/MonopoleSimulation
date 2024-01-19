from simulation import compute_position, spherical_coordinates_to_decart

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


def start_simulation(total_time=100000):
    points = np.empty([0, 3])
    init_coords=(1, np.pi / 3, np.pi / 2)
    speeds=(1 , 1 / 25 , 0)
    speed_magnitude = np.linalg.norm(speeds)

    for time in np.arange(0, total_time, 10):
        coords = compute_position(time)

        decart_coords = np.array(spherical_coordinates_to_decart(*coords))

        points = np.append(points, [decart_coords], axis=0)
    
    ax = plt.axes(projection='3d')
    x, y, z = points[:, 0], points[:, 1], points[:, 2]
    ax.plot3D(x, y, z)
    ax.scatter3D(x[0], y[0], z[0], '*', color='orange', alpha=0.5)
    
    plt.show()

if __name__ == "__main__":
    start_simulation()
import numpy as np
from math import sqrt

# def collect_points(time):
#     points = np.empty([0, 3])
    
#     coords=(1, 1, np.pi / 2)
#     speeds=(1, 0 , 1)

#     for time in range(total_time):
#         tau, sphere_coords, speeds = compute_position(time, sphere_coords, speeds)
    
#         decart_coords = np.array(spherical_coordinates_to_decart(*sphere_coords))

#         points = np.append(points, [decart_coords], axis=0)
    
def compute_position(time, init_coords=(1, 0, np.pi / 2), init_speeds=(1, 1 / 25, 0), mass=1, q=10**-5):
    # space = (t, r, theta, phi)
    
    k = 9*10**9
    r0 = init_coords[0]
    v_r = init_speeds[0]
    v_phi = init_speeds[1] * r0
    m = mass

    compute_tau = lambda t: t / sqrt(1 + v_phi**2 + v_r**2)
    tau = compute_tau(time)

    compute_r = lambda tau_: sqrt( (v_phi**2 + v_r**2)*tau_**2 - 2*r0*v_r*tau_ + r0**2 )
    r = compute_r(tau)

    L0 = m * r0 * v_phi
    l = sqrt(k**2 * q**2 + L0**2)

    compute_alpha = lambda tau_: l/L0 * (np.arctan( ((v_phi**2 + v_r**2)*tau_ + r0*v_r)/(r0*v_phi) ) - np.arctan( v_r / v_phi ))
    alpha = compute_alpha(tau)
    compute_phi = lambda tau_: np.arctan( -( L0*l*np.sin(alpha) ) / ( L0**2*np.cos(alpha) + k**2 * q**2 ) )
    phi = compute_phi(tau)

    
    # theta = np.pi / 2 + np.arctan( ( l**2 - 2*L0**2 )  / ( 2*k*q*L0 ) )
    theta = np.pi / 2 - np.pi / 100

    return (r, phi, theta)

# def compute_position(time, init_coords=(10, 0, np.pi / 7), init_speeds=(-1, -1, 1), mass=1, q=10**-7):
#     time0 = 0
#     r0 = init_coords[0]
#     theta0 = init_coords[1]
#     phi0 = init_coords[2]
#     speed = np.linalg.norm(np.array(init_speeds))

#     m = mass
#     light_speed = 3*10**8

#     r = np.sqrt(r0**2 + speed**2 * (time - time0)**2)
    
#     theta = theta0 - np.pi / 100
#     # theta = theta0 + np.arctan(m*r0*)
    
#     psi = np.arctan(speed * (time - time0) / r0)
#     phi = psi / np.sin(theta) + phi0


#     return (r, theta, phi)

def derivative(function, point, h=1e-6):
    return (function(point + h) - function(point - h)) / (2 * h)

def spherical_coordinates_to_decart(r, phi, theta):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    return (x, y, z)
 
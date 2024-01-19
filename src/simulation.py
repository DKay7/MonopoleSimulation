import numpy as np
from math import sqrt


class SphereCoordinates:
    def __init__(self, r, phi, theta):
        self.r = r
        self.phi = phi
        self.theta = theta
        self.coords = np.array([r, phi, theta])
    
    @property
    def get_coords(self):
        return self.coords 

    @property
    def decart(self):
        x = self.r * np.sin(self.theta) * np.cos(self.phi)
        y = self.r * np.sin(self.theta) * np.sin(self.phi)
        z = self.r * np.cos(self.theta)

        return np.array([x, y, z])


class ElectricCharge:
    def __init__(self, init_coords: SphereCoordinates=SphereCoordinates(1, 0, np.pi / 2),
                       init_speeds: SphereCoordinates=SphereCoordinates(1, 1 / 25, 0), 
                       mass=1, q=10**-5):
        self.init_coords = init_coords
        self.init_speeds = init_speeds
        self.mass = mass
        self.q = q
    
    def get_params(self):
        return (self.init_coords, self.init_speeds, self.mass, self.q)


class Simulation:
    def __init__(self, charge: ElectricCharge, total_time: int, time_step: int = 10):
        self.charge = charge
        self.total_time = total_time
        self.time_step = time_step
    
    def run_experiment(self):
        points = np.empty((0, 3))

        time = np.arange(0, self.total_time, self.time_step)
        coords = self._compute_position(time)
        return coords.decart.T

    def _compute_position(self, current_time):
        # space = (t, r, phi, theta)
        # some *magic* of ~physics~

        k = 9*10**9
        r0 = self.charge.init_coords.r
        v_r = self.charge.init_speeds.r
        v_phi = self.charge.init_speeds.phi * r0
        m = self.charge.mass
        q = self.charge.q

        tau = current_time / np.sqrt(1 + v_phi**2 + v_r**2)
        r = np.sqrt( (v_phi**2 + v_r**2)*tau**2 - 2*r0*v_r*tau + r0**2 )

        L0 = m * r0 * v_phi
        l = np.sqrt(k**2 * q**2 + L0**2)

        alpha = l/L0 * (np.arctan( ((v_phi**2 + v_r**2)*tau + r0*v_r)/(r0*v_phi) ) - np.arctan( v_r / v_phi ))
        phi = np.arctan( -( L0*l*np.sin(alpha) ) / ( L0**2*np.cos(alpha) + k**2 * q**2 ) )
        theta = np.arccos(-k*q *L0/l * (1 - np.cos(alpha)) )
        
        return SphereCoordinates(r, phi, theta)

 
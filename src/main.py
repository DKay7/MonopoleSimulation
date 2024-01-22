from drawer import start_simulation
from simulation import SphereCoordinates, ElectricCharge

import numpy as np
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as mpld3

def input_data():
    eps = 1e-1

    v_r     = st.sidebar.slider("Линейная скорость (v_r)", -1., 1., 1., 0.2, "%f")
    v_r = (v_r if np.abs(v_r) > eps else eps)
    v_phi   = st.sidebar.slider("Угловая скорость (v_phi)", 1/1000, 1/25, 1/100, 1/100, "%f")
    velocity = SphereCoordinates(v_r, v_phi, 0)

    r     = st.sidebar.slider("радиус-вектор", -100., 100., 100., 0.1, "%f")
    r = (r if np.abs(r) > eps else 2*eps)
    
    phi = 0
    theta = np.pi / 2
    # theta = st.sidebar.slider("theta", 0., 2*np.pi, np.pi / 2, np.pi / 8, "%f")
    # phi   = st.sidebar.slider("phi", -np.pi, np.pi, np.pi / 2, np.pi / 8, "%f")
    coords = SphereCoordinates(r, phi, theta)

    mass =  st.sidebar.slider("Масса", 1, 50, 20, 2, "%d")
    q   =  st.sidebar.slider("Заряд", 1*10**-5, 2*10**-3, 1*10**-5, 5*10**-5, "%f")
    
    charge = ElectricCharge(coords, velocity, mass, q)
    total_time =  st.sidebar.slider("Время эксперимента", 1, int(1e3), 500, 10, "%d")
    return charge, total_time

def main():
    charge, total_time = input_data()
    fig = start_simulation(charge, total_time)
    # fig_html = mpld3.fig_to_html(fig)
    # components.html(fig_html)
    fig.update_layout(height=900)
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
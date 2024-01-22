# Megnetic (Dirac's) monopole simulation

## Description
This project implements simulation of a charged particle trajectory in magnetic monopole's field. All the physics calculations was done in `src/simulation.py` file. Also, the project provides web-interface based on streamlit library for user to be able to check how the trajectory depends on initial parameters such as speed, coordinate, mass and charge.

You can find the paper inside `text` folder.

## How to run
1. First, clone this project

### With Docker
2. `sudo docker build -t simulation-app .`
3. `sudo docker run -p 8501:8501 simulation-app`
4. open the `Network URL` adres in your browser.

### Without Docker
2. Then, create a new python environment with `python3 -m venv .venv` from the project's root
3. Activate environment with `source .venv/bin/activate`
4. Install requirements: `pip3 install -r src/requirements.txt`
5. Finally, run the project: `streamlit run src/main.py`
6. If you want to run the project without streamlit, just run `python3 src/drawer.py`
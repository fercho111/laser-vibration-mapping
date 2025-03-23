"""
Simulation of Laser Reflection Patterns on Vibrating Circular Membranes
Uses Bessel function solutions to the wave equation for circular membranes
"""

import numpy as np
from scipy.special import jn, jn_zeros 
import matplotlib.pyplot as plt

# PARAMETERS
# Radius of the circular membrane (meters)
R = 0.04
# Distance to projection screen (meters)
L = 2.0
# Radial coordinate of reflection point (0 to R)
r0 = 0.02
# Angular coordinate of reflection point (radians)
theta0 = np.pi/4

# Define vibration modes (can add more modes as needed)
# Each mode has:
# - m: angular mode number (number of nodal diameters)
# - n: radial mode number (number of nodal circles)
# - A: amplitude (meters)
# - omega: angular frequency (rad/s)
# - phi: angular phase offset (radians)
# - psi: temporal phase offset (radians)
modes1 = [
    {'m': 1, 'n': 1, 'A': 0.001, 'omega': 50.0, 'phi': 0, 'psi': 0},
    {'m': 2, 'n': 6, 'A': 0.005, 'omega': 80.0, 'phi': np.pi/2, 'psi': 0},
    {'m': 2, 'n': 1, 'A': 0.005, 'omega': 80.0, 'phi': np.pi/2, 'psi': 0},
    {'m': 1, 'n': 5, 'A': 0.005, 'omega': 80.0, 'phi': np.pi/2, 'psi': 0},
    {'m': 2, 'n': 3, 'A': 0.005, 'omega': 80.0, 'phi': np.pi/2, 'psi': 0}
]

modes2 = [
    {'m': 2, 'n': 2, 'A': 0.1, 'omega': 5.0, 'phi': 0, 'psi': 0},
]

# Select modes to graph
modes = modes1

# BESSEL FUNCTION ROOTS
# The alpha_mn values are the nth roots of the mth Bessel function J_m
# These determine where the nodal circles occur
for mode in modes:
    m = mode['m']
    n = mode['n']
    # Find the nth zero of the mth Bessel function
    mode['alpha'] = jn_zeros(m, n)[-1] 

# TIME DOMAIN SETUP
t = np.linspace(0, 2*np.pi, 1000)

# DERIVATIVE CALCULATIONS
# Initialize gradient components (Cartesian coordinates)
dz_dx = 0.0
dz_dy = 0.0

# Loop through each vibration mode and accumulate their contributions
for mode in modes:
    # Extract mode parameters
    m = mode['m']
    n = mode['n']
    A = mode['A']
    alpha = mode['alpha']
    omega = mode['omega']
    phi = mode['phi']
    psi = mode['psi']

    # Dimensionless radial argument for Bessel functions
    arg = alpha * r0 / R  # alpha_mn * normalized radius

    # BESSEL FUNCTION CALCULATIONS
    # J_m(alpha_mn r0/R) - Bessel function value at reflection point
    J = jn(m, arg)
    
    # First derivative of Bessel function using recurrence relation:
    # J'_m(x) = (J_{m-1}(x) - J_{m+1}(x))/2
    dJ = (jn(m-1, arg) - jn(m+1, arg)) / 2.0

    # SPATIAL FACTORS
    # Angular component of mode shape
    cos_m_theta = np.cos(m * theta0 + phi)
    sin_m_theta = np.sin(m * theta0 + phi)


    # TEMPORAL FACTORS
    # Time-varying component cos(omega t + psi)
    cos_t = np.cos(omega * t + psi)

    # RADIAL AND ANGULAR DERIVATIVES (POLAR COORDINATES)
    # dz/dr contribution from this mode
    dz_dr = A * (alpha/R) * dJ * cos_m_theta * cos_t
    
    # dz/dtheta contribution from this mode
    dz_dtheta = -A * J * m * sin_m_theta * cos_t

    # CONVERT TO CARTESIAN GRADIENTS VIA CHAIN RULE
    # Using polar to Cartesian transformation:
    dz_dx += dz_dr * np.cos(theta0) - (dz_dtheta * np.sin(theta0))/r0
    dz_dy += dz_dr * np.sin(theta0) + (dz_dtheta * np.cos(theta0))/r0

# REFLECTION CALCULATION
# Using small angle approximation for reflection:
# Screen coordinates are proportional to gradient components
x_screen = -2 * L * dz_dx
y_screen = -2 * L * dz_dy

# VISUALIZATION
plt.figure(figsize=(8, 8))
plt.plot(x_screen, y_screen, linewidth=0.5)
plt.title("Laser Reflection Pattern\n(m,n) Modes: " + 
         ", ".join([f"({mode['m']},{mode['n']})" for mode in modes]))
plt.xlabel("X Screen Position (m)")
plt.ylabel("Y Screen Position (m)")
plt.grid(True)
plt.axis('equal')
plt.show()
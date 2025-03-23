import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.special import jn, jn_zeros

# Parameters
R = 1.0  # Radius of the membrane
m, n = 2, 5  # Mode numbers (angular, radial)
T = 100.0  # Tension (N/m)
sigma = 0.01  # Surface mass density (kg/m²)
frames = 100  # Number of animation frames
fps = 40  # Frames per second

# Compute k_mn (Bessel function zero for mode (m,n))
k_mn = jn_zeros(m, n)[-1] / R  # Normalize by radius
f_mn = (k_mn / (2 * np.pi)) * np.sqrt(T / sigma)  # Resonant frequency
omega = 2 * np.pi * f_mn  # Angular frequency

# Create polar coordinate grid
N = 100
r = np.linspace(0, R, N)
theta = np.linspace(0, 2 * np.pi, N)
R_grid, Theta_grid = np.meshgrid(r, theta)

# Convert to Cartesian coordinates
X = R_grid * np.cos(Theta_grid)
Y = R_grid * np.sin(Theta_grid)

# Set up the figure
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')
ax.set_zlim(-1, 1)  # Set z-axis limits

# Function to update the plot
def update(frame):
    ax.clear()
    ax.set_zlim(-1, 1)
    
    # Compute vibration at time t
    t = frame / fps  # Time in seconds
    Z = jn(m, k_mn * R_grid) * np.cos(m * Theta_grid) * np.cos(omega * t)

    # Plot surface
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k')
    ax.set_title(f"Vibrating Circular Membrane (m={m}, n={n}) at t={t:.2f}s")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Displacement")

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps)
plt.show()

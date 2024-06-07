import numpy as np
from scipy.optimize import minimize
from scipy.constants import pi

# Example peak positions in degrees (2θ)
peak_positions = np.array([20.0, 29.5, 33.0, 37.5, 40.0])

# Convert degrees to radians
peak_positions = np.deg2rad(peak_positions)

# Wavelength of the X-ray (Cu Kα = 1.5406 Å)
wavelength = 1.5406

# Function to calculate the d-spacings from 2θ angles
def calculate_d_spacing(two_theta, wavelength):
    return wavelength / (2 * np.sin(two_theta / 2))
    
def calculate_d_spacing(two_theta, wavelength):
    return wavelength / (2 * np.sin(two_theta / 2))

# Calculate d-spacings for the given peak positions
d_spacings = calculate_d_spacing(peak_positions, wavelength)

# Example Miller indices for a cubic crystal system
# We need to identify these indices by matching d-spacings
possible_hkls = [
    (1, 0, 0),
    (1, 1, 0),
    (1, 1, 1),
    (2, 0, 0),
    (2, 1, 0),
    (2, 1, 1),
    (2, 2, 0),
    (3, 1, 0)
]

# Function to calculate the theoretical d-spacing for a cubic system
def cubic_d_spacing(a, h, k, l):
    return a / np.sqrt(h**2 + k**2 + l**2)

# Objective function to minimize (difference between observed and calculated d-spacings)
def objective(params):
    a = params[0]
    error = 0
    for d, hkl in zip(d_spacings, possible_hkls):
        h, k, l = hkl
        d_calc = cubic_d_spacing(a, h, k, l)
        error += (d - d_calc) ** 2
    return error

# Initial guess for the lattice parameter 'a'
initial_guess = [5.0]

# Perform the optimization to find the best lattice parameter 'a'
result = minimize(objective, initial_guess)
print(result)

# Extract the optimized lattice parameter
optimized_a = result.x[0]



print(f"Optimized lattice parameter a: {optimized_a:.4f} Å")   

###
To create a Python code that simulates the functionality of a program like Dicvol, which is used for indexing powder diffraction patterns and determining unit cell parameters, you need to follow a few steps. Here is a simplified example of how you might start such a project.

Data Preparation: You need the 2θ angles and corresponding intensities from a powder diffraction experiment.
Peak Detection: Identify the positions of the peaks in the diffraction pattern.
Indexing: Assign hkl indices to the peaks and determine the unit cell parameters.


Imports: We import necessary modules such as numpy and scipy.optimize.
Data Preparation: We define the 2θ peak positions in degrees and convert them to radians.
Calculate d-Spacings: We define a function calculate_d_spacing to calculate d-spacings from 2θ angles and the wavelength of the X-rays.
Possible Miller Indices: For simplicity, we assume some possible Miller indices for a cubic crystal system. In a real application, these would be identified from the data.
Theoretical d-Spacings: We define a function cubic_d_spacing to calculate the theoretical d-spacing for a given cubic lattice parameter and Miller indices.
Objective Function: This function calculates the difference between observed and theoretical d-spacings, which we aim to minimize.
Optimization: We use scipy.optimize.minimize to find the lattice parameter 'a' that minimizes the objective function.
Output: We print the optimized lattice parameter.
###
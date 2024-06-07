import numpy as np
from scipy.special import wofz
import matplotlib.pyplot as plt

def voigt(x, sigma, gamma, A=1.0, u=0.0):
    """
    Compute the Voigt profile at x with given Gaussian (sigma) and Lorentzian (gamma) broadening parameters,
    and additional parameters for amplitude (A) and center (u).

    Parameters:
    x : array_like
        Points at which to evaluate the Voigt profile.
    sigma : float
        Standard deviation of the Gaussian component.
    gamma : float
        Half-width at half-maximum of the Lorentzian component.
    A : float, optional
        Amplitude of the Voigt profile. Default is 1.0.
    u : float, optional
        Center of the Voigt profile. Default is 0.0.

    Returns:
    array_like
        Voigt profile evaluated at x.
    """
    z = ((x - u) + 1j * gamma) / (sigma * np.sqrt(2))
    return A * np.real(wofz(z)) / (sigma * np.sqrt(2 * np.pi))

# Example usage:
x = np.linspace(-10, 10, 1000)
sigma = 1.0
gamma = 1.0
A = 1.0
u = 0.0

voigt_profile = voigt(x, sigma, gamma, A, u)

# Plotting the Voigt profile
plt.plot(x, voigt_profile)
plt.title('Voigt Profile')
plt.xlabel('x')
plt.ylabel('Intensity')
plt.show()